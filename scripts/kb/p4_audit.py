"""Audit P4 rule/field coverage without inventing missing game facts.

The first P3 pass has source snapshots and conservative parses for all
discovered rows.  This report separates pipeline coverage from fact coverage:
missing event branches or enemy moves are findings to review, while source
claims remain intact.  The command is read-only apart from its JSON/Markdown
reports and never imports either strategy guide.
"""

from __future__ import annotations

import json
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "spire.sqlite"
REPORT_PATH = ROOT / "reports" / "p4-rule-audit.json"
WIKI_PATH = ROOT / "docs" / "wiki" / "p4-rule-audit.md"
PARSER_VERSION = "kb-p4-rule-audit/0.1"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def count(conn: sqlite3.Connection, sql: str, args: tuple[Any, ...] = ()) -> int:
    return int(conn.execute(sql, args).fetchone()[0])


def entity_coverage(conn: sqlite3.Connection, table: str, required_sql: str) -> dict[str, Any]:
    total = count(conn, f"SELECT COUNT(*) FROM {table}")
    rows = conn.execute(
        f"""SELECT e.lifecycle, e.mapping_status, COUNT(*) AS n,
                   SUM(CASE WHEN {required_sql} THEN 1 ELSE 0 END) AS complete
            FROM {table} t JOIN entities e ON e.id=t.entity_id
            GROUP BY e.lifecycle, e.mapping_status ORDER BY e.lifecycle,e.mapping_status"""
    ).fetchall()
    return {
        "total": total,
        "required_complete": sum(int(row["complete"] or 0) for row in rows),
        "by_lifecycle_mapping": [dict(row) for row in rows],
    }


def main() -> int:
    if not DB_PATH.exists():
        raise SystemExit("data/spire.sqlite not found; run bootstrap_sample.py first")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    coverage = {
        "card": entity_coverage(
            conn,
            "cards",
            "EXISTS (SELECT 1 FROM entity_variants v JOIN card_variants cv ON cv.variant_id=v.id WHERE v.entity_id=t.entity_id AND v.variant_kind='base')",
        ),
        "relic": entity_coverage(conn, "relics", "effect_json IS NOT NULL"),
        "potion": entity_coverage(conn, "potions", "effect_json IS NOT NULL"),
        "monster": entity_coverage(
            conn,
            "monsters",
            "hp_min IS NOT NULL AND EXISTS (SELECT 1 FROM monster_moves m WHERE m.monster_entity_id=t.entity_id)",
        ),
        "event": entity_coverage(
            conn,
            "events",
            "EXISTS (SELECT 1 FROM event_options o WHERE o.event_entity_id=t.entity_id)",
        ),
        "status": entity_coverage(conn, "statuses", "EXISTS (SELECT 1 FROM claims c WHERE c.subject_entity_id=t.entity_id)"),
        "keyword": entity_coverage(conn, "keywords", "definition_json IS NOT NULL"),
        "mechanic": entity_coverage(conn, "mechanics", "definition_json IS NOT NULL"),
    }

    unresolved = {
        "inventory_not_parsed": [dict(row) for row in conn.execute(
            """SELECT entity_kind, language, status, COUNT(*) AS n
               FROM inventory_items WHERE status NOT IN ('parsed','excluded')
               GROUP BY entity_kind, language, status ORDER BY entity_kind,language,status"""
        )],
        "cards_without_base_variant": [dict(row) for row in conn.execute(
            """SELECT e.id, e.lifecycle, n.name
               FROM cards c JOIN entities e ON e.id=c.entity_id
               LEFT JOIN names n ON n.entity_id=e.id AND n.language='en' AND n.is_preferred=1
               WHERE NOT EXISTS (SELECT 1 FROM entity_variants v WHERE v.entity_id=c.entity_id AND v.variant_kind='base')
               ORDER BY e.id"""
        )],
        "monsters_without_moves": [dict(row) for row in conn.execute(
            """SELECT e.id, e.lifecycle, COALESCE(n.name, e.id) AS name
               FROM monsters m JOIN entities e ON e.id=m.entity_id
               LEFT JOIN names n ON n.entity_id=e.id AND n.language='en' AND n.is_preferred=1
               WHERE NOT EXISTS (SELECT 1 FROM monster_moves mm WHERE mm.monster_entity_id=m.entity_id)
               ORDER BY e.id"""
        )],
        "events_without_options": [dict(row) for row in conn.execute(
            """SELECT e.id, e.lifecycle, COALESCE(n.name, e.id) AS name
               FROM events v JOIN entities e ON e.id=v.entity_id
               LEFT JOIN names n ON n.entity_id=e.id AND n.language='en' AND n.is_preferred=1
               WHERE NOT EXISTS (SELECT 1 FROM event_options o WHERE o.event_entity_id=v.entity_id)
               ORDER BY e.id"""
        )],
    }

    suspicious = {
        "possible_energy_icon_loss": count(conn, """SELECT COUNT(*) FROM claims
            WHERE (value_json LIKE '%Gain .%' OR value_json LIKE '%Deal .%')
              AND COALESCE(notes, '') NOT LIKE '%superseded: icon-only text recovered%'""") ,
        "raw_placeholder_claims": count(conn, "SELECT COUNT(*) FROM claims WHERE value_json LIKE '%请输入图片描述%'") ,
        "unknown_image_licence_assets": count(conn, "SELECT COUNT(*) FROM assets WHERE license_status='unknown'"),
        "candidate_entities": count(conn, "SELECT COUNT(*) FROM entities WHERE lifecycle='candidate'"),
        "confirmed_inventory_mappings": count(conn, "SELECT COUNT(*) FROM inventory_mappings WHERE status='confirmed'"),
        "candidate_inventory_mappings": count(conn, "SELECT COUNT(*) FROM inventory_mappings WHERE status='candidate'"),
        "strategy_notes": count(conn, "SELECT COUNT(*) FROM strategy_notes"),
        "strategy_links": count(conn, "SELECT COUNT(*) FROM strategy_links"),
    }

    numeric = {
        "card_variant_cost_types": [dict(row) for row in conn.execute("SELECT cost_type, COUNT(*) AS n FROM card_variants GROUP BY cost_type ORDER BY cost_type")],
        "cards_with_zero_upgrade_cost": count(conn, """SELECT COUNT(*) FROM card_variants cv JOIN entity_variants v ON v.id=cv.variant_id WHERE v.variant_kind='upgrade' AND cv.cost_type='fixed' AND cv.cost_value=0"""),
        "cards_with_x_cost": count(conn, "SELECT COUNT(*) FROM card_variants WHERE cost_type='x'"),
        "claims_by_verification": [dict(row) for row in conn.execute("SELECT verification_status, COUNT(*) AS n FROM claims GROUP BY verification_status ORDER BY verification_status")],
    }

    report = {
        "generated_at": now(),
        "parser_version": PARSER_VERSION,
        "status": "audit_pending_review",
        "scope": "StS1 basic Wiki only; strategy documents excluded",
        "coverage": coverage,
        "unresolved": unresolved,
        "suspicious": suspicious,
        "numeric_checks": numeric,
        "notes": [
            "A complete source parse does not mean the bilingual identity or rule field is verified.",
            "Missing enemy moves/event options are explicit follow-up items; no placeholder values were inserted.",
            "Energy icon and image-license warnings require visual or licensing review.",
            "The separate mapping-review queue ranks candidates but does not confirm them.",
        ],
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# P4 机制与规则核验审计", "", f"生成时间：{report['generated_at']}。状态：`{report['status']}`。", "",
        "此页只报告字段覆盖和待核验项，不把缺失数据补成 0，也不把候选身份当作双语事实。", "",
        "## 字段覆盖", "", "| 类别 | 条目数 | 必备字段齐全 |", "| --- | ---: | ---: |",
    ]
    for kind, value in coverage.items():
        lines.append(f"| `{kind}` | {value['total']} | {value['required_complete']} |")
    lines += ["", "## 待处理数量", "", "| 项目 | 数量 |", "| --- | ---: |"]
    for key, value in suspicious.items():
        lines.append(f"| `{key}` | {value} |")
    lines += ["", "## 未完成字段清单", ""]
    for key, rows in unresolved.items():
        lines.append(f"### {key}（{len(rows)}）")
        if not rows:
            lines.append("无。")
            continue
        for row in rows[:100]:
            label = row.get("name") or row.get("id") or row.get("entity_kind")
            lines.append(f"- `{label}` (`{row.get('lifecycle','')}`)")
        if len(rows) > 100:
            lines.append(f"- ……其余 {len(rows)-100} 条见 JSON 报告。")
    lines += ["", "## 数值与提取检查", "", f"- 升级后固定 0 费变体：{numeric['cards_with_zero_upgrade_cost']} 条。", f"- X 费变体：{numeric['cards_with_x_cost']} 条。", "- 可能的能量图标文本损失和原始图片占位词仍保留在报告中，需对照源图复核。", "", "详细 JSON：[p4-rule-audit.json](../../reports/p4-rule-audit.json)"]
    WIKI_PATH.parent.mkdir(parents=True, exist_ok=True)
    WIKI_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in {"coverage", "unresolved"}}, ensure_ascii=False, indent=2))
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
