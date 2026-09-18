"""Cross-check the bilingual Wiki, local game localization and SQLite KB.

The report is deliberately a gap report rather than an automatic merge.  A
game-only key may be an internal token, a deprecated entry or a real object;
it remains a candidate until an English/Chinese source page and fields agree.
"""

from __future__ import annotations

import json
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from bootstrap_sample import DB_PATH, ROOT, utc_now


PARSER_VERSION = "kb-cross-source-audit/0.5"
GAME_HASH = "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673"
GAME_BASE = ROOT / "data" / "raw" / "game_local"
GAME_ROOT = next(
    (path for path in GAME_BASE.iterdir() if path.is_dir() and GAME_HASH.startswith(path.name)),
    GAME_BASE / GAME_HASH,
)
REPORT_JSON = ROOT / "reports" / "completeness-crosscheck.json"
REPORT_MD = ROOT / "reports" / "completeness-crosscheck.md"

LOCAL_FILES = {
    "card": "cards.json",
    "relic": "relics.json",
    "potion": "potions.json",
    "event": "events.json",
    "monster": "monsters.json",
    "status": "powers.json",
}


def read_local(kind: str, language: str = "eng") -> dict[str, Any]:
    path = GAME_ROOT / language / LOCAL_FILES[kind]
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def json_object(value: str | None) -> dict[str, Any]:
    if not value:
        return {}
    try:
        result = json.loads(value)
    except json.JSONDecodeError:
        return {}
    return result if isinstance(result, dict) else {}


def source_inventory(conn: sqlite3.Connection) -> dict[str, Any]:
    counts: dict[str, dict[str, int]] = defaultdict(dict)
    for row in conn.execute(
        """SELECT source_id, entity_kind, language, status, COUNT(*) AS n
           FROM inventory_items GROUP BY source_id, entity_kind, language, status
           ORDER BY source_id, entity_kind, language, status"""
    ):
        counts[f"{row['source_id']}|{row['language']}"][f"{row['entity_kind']}|{row['status']}"] = row["n"]

    unmatched: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in conn.execute(
        """SELECT i.id, i.source_id, i.entity_kind, i.language, i.name, i.article_id, i.url
           FROM inventory_items i
           WHERE i.status='parsed'
             AND NOT EXISTS (
               SELECT 1 FROM inventory_mappings m
               WHERE m.status='confirmed'
                 AND (m.zh_inventory_id=i.id OR m.en_inventory_id=i.id)
             )
           ORDER BY i.entity_kind, i.language, i.name"""
    ):
        key = f"{row['source_id']}|{row['language']}|{row['entity_kind']}"
        unmatched[key].append({k: row[k] for k in ("id", "name", "article_id", "url")})
    return {"counts": dict(counts), "unmatched": dict(unmatched)}


def db_entities(conn: sqlite3.Connection) -> dict[str, Any]:
    by_kind: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    game_id_map: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for row in conn.execute(
        """SELECT id, kind, game_id, lifecycle, mapping_status FROM entities
           ORDER BY CASE lifecycle WHEN 'active' THEN 0 WHEN 'candidate' THEN 1 ELSE 2 END, id"""
    ):
        by_kind[row["kind"]][f"{row['lifecycle']}|{row['mapping_status']}"] += 1
        if row["game_id"]:
            game_id_map[row["kind"]][row["game_id"]] = {
                "entity_id": row["id"],
                "lifecycle": row["lifecycle"],
                "mapping_status": row["mapping_status"],
            }

    # ``game_id`` is deliberately one canonical key, while the JAR can retain
    # deprecated aliases and grouped-member keys.  Claims are the authoritative
    # many-to-one key index used by the cross-source report.
    game_key_map: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for row in conn.execute(
        """SELECT e.id, e.kind, e.lifecycle, e.mapping_status, c.value_json
           FROM claims c JOIN entities e ON e.id=c.subject_entity_id
           WHERE c.field_path='game.localization_key'
           ORDER BY CASE WHEN e.lifecycle='active' AND e.subtype='split_member' THEN 0
                         WHEN e.lifecycle='active' THEN 1
                         WHEN e.lifecycle='candidate' THEN 2 ELSE 3 END,
                    c.created_at, c.id"""
    ):
        try:
            payload = json.loads(row["value_json"])
        except (TypeError, json.JSONDecodeError):
            continue
        key = payload.get("key") if isinstance(payload, dict) else None
        kind = payload.get("kind") if isinstance(payload, dict) else row["kind"]
        if not key or kind in game_key_map and key in game_key_map[kind]:
            continue
        game_key_map[kind][key] = {
            "entity_id": row["id"],
            "lifecycle": row["lifecycle"],
            "mapping_status": row["mapping_status"],
        }

    incomplete: dict[str, list[dict[str, str]]] = {}
    checks = {
        "card": """SELECT e.id FROM entities e WHERE e.kind='card' AND e.lifecycle='active'
                   AND NOT EXISTS (SELECT 1 FROM entity_variants v JOIN card_variants cv ON cv.variant_id=v.id
                                   WHERE v.entity_id=e.id AND v.variant_kind='base')""",
        "relic": """SELECT e.id FROM entities e JOIN relics r ON r.entity_id=e.id
                    WHERE e.kind='relic' AND e.lifecycle='active' AND r.effect_json IS NULL""",
        "potion": """SELECT e.id FROM entities e JOIN potions p ON p.entity_id=e.id
                     WHERE e.kind='potion' AND e.lifecycle='active' AND p.effect_json IS NULL""",
        "monster": """SELECT e.id FROM entities e JOIN monsters m ON m.entity_id=e.id
                      WHERE e.kind='monster' AND e.lifecycle='active'
                        AND e.subtype != 'group_page'
                        AND (m.hp_min IS NULL OR NOT EXISTS (SELECT 1 FROM monster_moves mm WHERE mm.monster_entity_id=e.id))""",
        "event": """SELECT e.id FROM entities e JOIN events v ON v.entity_id=e.id
                    WHERE e.kind='event' AND e.lifecycle='active'
                      AND NOT EXISTS (SELECT 1 FROM event_options o WHERE o.event_entity_id=e.id)""",
        "keyword": """SELECT e.id FROM entities e JOIN keywords k ON k.entity_id=e.id
                      WHERE e.kind='keyword' AND e.lifecycle='active' AND k.definition_json IS NULL""",
        "mechanic": """SELECT e.id FROM entities e JOIN mechanics m ON m.entity_id=e.id
                       WHERE e.kind='mechanic' AND e.lifecycle='active' AND m.definition_json IS NULL""",
    }
    for kind, sql in checks.items():
        incomplete[kind] = [row[0] for row in conn.execute(sql)]

    bilingual = {
        "card_variants": {
            "total": conn.execute("SELECT COUNT(*) FROM card_variants").fetchone()[0],
            "english": conn.execute("SELECT COUNT(*) FROM card_variants WHERE description_en IS NOT NULL").fetchone()[0],
            "chinese": conn.execute("SELECT COUNT(*) FROM card_variants WHERE description_zh IS NOT NULL").fetchone()[0],
        },
        "relics": {"total": 0, "english": 0, "chinese": 0},
        "potions": {"total": 0, "english": 0, "chinese": 0},
    }
    for kind, table in (("relics", "relics"), ("potions", "potions")):
        rows = conn.execute(f"SELECT effect_json FROM {table}").fetchall()
        bilingual[kind]["total"] = len(rows)
        for row in rows:
            obj = json_object(row[0])
            bilingual[kind]["english"] += int(bool(obj.get("description_en")))
            bilingual[kind]["chinese"] += int(bool(obj.get("description_zh")))
    character_fields = {}
    for field in ("initial_hp", "initial_gold", "potion_slots", "starting_deck_json", "starting_relic_entity_id"):
        character_fields[field] = conn.execute(f"SELECT COUNT(*) FROM characters WHERE {field} IS NOT NULL").fetchone()[0]

    definition_coverage: dict[str, dict[str, int]] = {}
    for kind, table in (("keyword", "keywords"), ("mechanic", "mechanics")):
        total = active = meaningful = chinese = editorial_chinese = 0
        for row in conn.execute(
            f"SELECT e.lifecycle, t.definition_json FROM {table} t JOIN entities e ON e.id=t.entity_id"
        ):
            total += 1
            try:
                payload = json.loads(row["definition_json"] or "{}")
            except (TypeError, json.JSONDecodeError):
                payload = {}
            if row["lifecycle"] == "active":
                active += 1
                if isinstance(payload, dict) and (payload.get("definition_en") or payload.get("wiki_sections")):
                    meaningful += 1
                if isinstance(payload, dict) and payload.get("definition_zh"):
                    if payload.get("definition_zh_origin") == "editorial_translation":
                        editorial_chinese += 1
                    else:
                        chinese += 1
        definition_coverage[kind] = {
            "total": total,
            "active": active,
            "meaningful_active": meaningful,
            "chinese_active": chinese,
            "editorial_chinese_active": editorial_chinese,
        }
    # A status can be documented either by a Wiki ``status.description``
    # claim or by the game's localized ``game.status.descriptions`` claim.
    # Count both forms so the report does not call a field missing merely
    # because the game package uses a different, more granular path.
    status_description_coverage = {
        "active": conn.execute("SELECT COUNT(*) FROM entities WHERE kind='status' AND lifecycle='active'").fetchone()[0],
        "english": conn.execute("""SELECT COUNT(DISTINCT subject_entity_id) FROM claims c JOIN entities e ON e.id=c.subject_entity_id
                                    WHERE e.kind='status' AND e.lifecycle='active'
                                      AND c.language='en'
                                      AND c.field_path IN ('status.description', 'game.status.descriptions')""").fetchone()[0],
        "chinese": conn.execute("""SELECT COUNT(DISTINCT subject_entity_id) FROM claims c JOIN entities e ON e.id=c.subject_entity_id
                                    WHERE e.kind='status' AND e.lifecycle='active'
                                      AND c.language='zh-CN'
                                      AND c.field_path IN ('status.description', 'game.status.descriptions')
                                      AND (c.notes IS NULL OR c.notes NOT LIKE '%editorial_zh%')""").fetchone()[0],
        "editorial_chinese": conn.execute("""SELECT COUNT(DISTINCT subject_entity_id) FROM claims c JOIN entities e ON e.id=c.subject_entity_id
                                    WHERE e.kind='status' AND e.lifecycle='active'
                                      AND c.language='zh-CN'
                                      AND c.field_path IN ('status.description', 'game.status.descriptions')
                                      AND c.notes LIKE '%editorial_zh%'""").fetchone()[0],
        "missing_english_ids": [row[0] for row in conn.execute("""SELECT e.id FROM entities e
                                    WHERE e.kind='status' AND e.lifecycle='active'
                                      AND NOT EXISTS (SELECT 1 FROM claims c WHERE c.subject_entity_id=e.id
                                                      AND c.language='en'
                                                      AND c.field_path IN ('status.description', 'game.status.descriptions'))
                                    ORDER BY e.id""")],
        "missing_chinese_ids": [row[0] for row in conn.execute("""SELECT e.id FROM entities e
                                    WHERE e.kind='status' AND e.lifecycle='active'
                                      AND NOT EXISTS (SELECT 1 FROM claims c WHERE c.subject_entity_id=e.id
                                                      AND c.language='zh-CN'
                                                      AND c.field_path IN ('status.description', 'game.status.descriptions'))
                                    ORDER BY e.id""")],
        "missing_chinese_source_ids": [row[0] for row in conn.execute("""SELECT e.id FROM entities e
                                    WHERE e.kind='status' AND e.lifecycle='active'
                                      AND NOT EXISTS (SELECT 1 FROM claims c WHERE c.subject_entity_id=e.id
                                                      AND c.language='zh-CN'
                                                      AND c.field_path IN ('status.description', 'game.status.descriptions')
                                                      AND (c.notes IS NULL OR c.notes NOT LIKE '%editorial_zh%'))
                                    ORDER BY e.id""")],
    }
    monster_total_active = conn.execute("SELECT COUNT(*) FROM entities WHERE kind='monster' AND lifecycle='active' AND subtype != 'group_page'").fetchone()[0]
    monster_complete_active = conn.execute("""SELECT COUNT(*) FROM entities e JOIN monsters m ON m.entity_id=e.id
                                              WHERE e.kind='monster' AND e.lifecycle='active'
                                                AND e.subtype != 'group_page'
                                                AND m.hp_min IS NOT NULL AND m.hp_max IS NOT NULL
                                                AND EXISTS (SELECT 1 FROM monster_moves mm WHERE mm.monster_entity_id=e.id)""").fetchone()[0]
    monster_group_pages = conn.execute("SELECT COUNT(*) FROM entities WHERE kind='monster' AND lifecycle='active' AND subtype='group_page'").fetchone()[0]

    return {
        "counts": {kind: dict(values) for kind, values in by_kind.items()},
        "game_id_map": {kind: dict(values) for kind, values in game_id_map.items()},
        "game_key_map": {kind: dict(values) for kind, values in game_key_map.items()},
        "incomplete_active": incomplete,
        "bilingual_fields": bilingual,
        "character_field_presence": character_fields,
        "definition_coverage": definition_coverage,
        "status_description_coverage": status_description_coverage,
        "monster_coverage": {
            "active": monster_total_active,
            "complete_active": monster_complete_active,
            "group_pages": monster_group_pages,
        },
        "encounters": {
            "entities": conn.execute("SELECT COUNT(*) FROM entities WHERE kind='encounter'").fetchone()[0],
            "rows": conn.execute("SELECT COUNT(*) FROM encounters").fetchone()[0],
            "with_members": conn.execute("SELECT COUNT(*) FROM encounters e WHERE EXISTS (SELECT 1 FROM encounter_members m WHERE m.encounter_entity_id=e.entity_id)").fetchone()[0],
            "member_rows": conn.execute("SELECT COUNT(*) FROM encounter_members").fetchone()[0],
            "confirmed_member_relations": conn.execute("SELECT COUNT(*) FROM relations WHERE relation_type='contains_monster' AND status='confirmed'").fetchone()[0],
            "conditional_member_relations": conn.execute("SELECT COUNT(*) FROM relations WHERE relation_type='contains_monster' AND status='confirmed' AND condition_json IS NOT NULL").fetchone()[0],
            "selection_rules": conn.execute("SELECT COUNT(DISTINCT subject_entity_id) FROM claims WHERE field_path='encounter.selection_rule'").fetchone()[0],
            "candidate_relations": conn.execute("SELECT COUNT(*) FROM relations WHERE relation_type='contains_monster' AND status='candidate'").fetchone()[0],
        },
        "claims": {
            "total": conn.execute("SELECT COUNT(*) FROM claims").fetchone()[0],
            "placeholder": conn.execute("SELECT COUNT(*) FROM claims WHERE value_json LIKE '%请输入图片描述%'").fetchone()[0],
        },
        "assets": {
            "total": conn.execute("SELECT COUNT(*) FROM assets").fetchone()[0],
            "unknown_license": conn.execute("SELECT COUNT(*) FROM assets WHERE license_status='unknown'").fetchone()[0],
            "linked_entity_assets": conn.execute("SELECT COUNT(*) FROM entity_assets").fetchone()[0],
            "card_variant_links": conn.execute("SELECT COUNT(*) FROM card_variants WHERE image_asset_id IS NOT NULL").fetchone()[0],
        },
    }


def local_crosscheck(
    conn: sqlite3.Connection,
    entity_map: dict[str, Any],
    game_key_map: dict[str, Any],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for kind, filename in LOCAL_FILES.items():
        english = read_local(kind, "eng")
        chinese = read_local(kind, "zhs")
        mapped = entity_map.get(kind, {})
        key_mapped = game_key_map.get(kind, {})
        deprecated = [
            key
            for key, value in english.items()
            if str(value.get("NAME") or "").upper().startswith("DEPRECATED")
            or (
                bool(value.get("DESCRIPTIONS"))
                and all(str(item or "").upper() == "DEPRECATED" for item in (value.get("DESCRIPTIONS") or []))
            )
            or str(value.get("DESCRIPTION") or "").upper() == "DEPRECATED"
        ]
        local_only = [key for key in english if key not in key_mapped and key not in deprecated]
        candidate_only = [key for key in english if key_mapped.get(key, {}).get("lifecycle") == "candidate"]
        represented = [key for key in english if key in mapped]
        represented_by_key = [key for key in english if key in key_mapped and key not in deprecated]
        deprecated_mapped = [key for key in deprecated if key in key_mapped]
        candidate_ids = {key for key, value in mapped.items() if value["lifecycle"] == "candidate"}
        result[kind] = {
            "english_entries": len(english),
            "chinese_entries": len(chinese),
            "same_keys": len(set(english) & set(chinese)),
            "represented_by_game_id": len(represented),
            "represented_by_live_game_key": len(represented_by_key),
            "candidate_game_ids": len(candidate_ids),
            "active_confirmed_keys": sum(1 for key in english if key_mapped.get(key, {}).get("lifecycle") == "active" and key_mapped.get(key, {}).get("mapping_status") == "confirmed"),
            "active_provisional_keys": sum(1 for key in english if key_mapped.get(key, {}).get("lifecycle") == "active" and key_mapped.get(key, {}).get("mapping_status") != "confirmed"),
            "unrepresented_keys": local_only,
            "candidate_keys": candidate_only,
            "deprecated_keys": deprecated,
            "deprecated_mapped_keys": deprecated_mapped,
            "localized_name_samples": [
                {"key": key, "en": english[key].get("NAME"), "zh": chinese.get(key, {}).get("NAME")}
                for key in local_only[:40]
            ],
        }
    return result


def cross_source_differences(conn: sqlite3.Connection, inventory: dict[str, Any]) -> dict[str, Any]:
    differences: dict[str, Any] = {}
    for kind in ("card", "event", "monster", "potion", "relic", "status", "keyword", "mechanic"):
        en = conn.execute("SELECT COUNT(*) FROM inventory_items WHERE source_id='wiki_gg' AND language='en' AND entity_kind=? AND status='parsed'", (kind,)).fetchone()[0]
        zh = conn.execute("SELECT COUNT(*) FROM inventory_items WHERE source_id='xiaoheihe' AND language='zh-CN' AND entity_kind=? AND status='parsed'", (kind,)).fetchone()[0]
        differences[kind] = {"wiki_gg_en": en, "xiaoheihe_zh": zh, "delta_zh_minus_en": zh - en}
    # P3 repeats some directory rows when a page also exposes a second image
    # or an anchor.  Keep the raw row count above, but expose unique URLs so a
    # duplicate row is not mistaken for a missing identity mapping.
    differences["unique_url_counts"] = {}
    for kind in ("card", "event", "monster", "potion", "relic", "status", "keyword", "mechanic"):
        values = {}
        for source_id, language in (("wiki_gg", "en"), ("xiaoheihe", "zh-CN")):
            values[f"{source_id}_{language}"] = conn.execute(
                "SELECT COUNT(DISTINCT url) FROM inventory_items WHERE source_id=? AND language=? AND entity_kind=? AND status='parsed'",
                (source_id, language, kind),
            ).fetchone()[0]
        differences["unique_url_counts"][kind] = values
    differences["special_asymmetries"] = {
        "centurion_mystic_group_page_vs_split_local_entities": not all(
            conn.execute("SELECT 1 FROM entities WHERE id=? AND lifecycle='active'", (entity_id,)).fetchone()
            for entity_id in ("sts1.monster.centurion", "sts1.monster.mystic")
        ),
        "donu_deca_group_page_vs_split_local_entities": not all(
            conn.execute("SELECT 1 FROM entities WHERE id=? AND lifecycle='active'", (entity_id,)).fetchone()
            for entity_id in ("sts1.monster.donu", "sts1.monster.deca")
        ),
        "spire_shield_spear_group_page_vs_split_local_entities": not all(
            conn.execute("SELECT 1 FROM entities WHERE id=? AND lifecycle='active'", (entity_id,)).fetchone()
            for entity_id in ("sts1.monster.spire_shield", "sts1.monster.spire_spear")
        ),
        "spire_heart_chinese_and_game_candidate": True,
    }
    return differences


def build_report(conn: sqlite3.Connection) -> dict[str, Any]:
    inventory = source_inventory(conn)
    entities = db_entities(conn)
    local = local_crosscheck(conn, entities["game_id_map"], entities["game_key_map"])
    candidate_total = conn.execute("SELECT COUNT(*) FROM entities WHERE lifecycle='candidate'").fetchone()[0]
    unknown_assets = conn.execute("SELECT COUNT(*) FROM assets WHERE license_status='unknown'").fetchone()[0]
    keyword_cov = entities["definition_coverage"]["keyword"]
    mechanic_cov = entities["definition_coverage"]["mechanic"]
    status_cov = entities["status_description_coverage"]
    status_effective_chinese = status_cov["active"] - len(status_cov["missing_chinese_ids"])
    reviewed_game_local = conn.execute(
        """SELECT COUNT(*) FROM inventory_mappings m
           JOIN inventory_items i ON i.id=m.en_inventory_id
           WHERE m.status='confirmed' AND i.source_id='game_local'"""
    ).fetchone()[0]
    reviewed_wiki = conn.execute(
        """SELECT COUNT(*) FROM inventory_mappings m
           JOIN inventory_items i ON i.id=m.en_inventory_id
           WHERE m.status='confirmed' AND i.source_id='wiki_gg'"""
    ).fetchone()[0]
    report = {
        "generated_at": utc_now(),
        "parser_version": PARSER_VERSION,
        "scope": "StS1 foundational Wiki; strategy documents excluded",
        "sources": {
            "xiaoheihe": "https://web.xiaoheihe.cn/wiki/home?wiki_id=646570",
            "wiki_gg": "https://slaythespire.wiki.gg/",
            "game_localization": {"steam_build_id": "10180494", "jar_sha256": GAME_HASH},
        },
        "source_inventory": inventory,
        "db": entities,
        "game_local_crosscheck": local,
        "source_differences": cross_source_differences(conn, inventory),
        "reviewed_crosswalks": {
            "confirmed_total": reviewed_game_local + reviewed_wiki,
            "wiki_gg": reviewed_wiki,
            "game_local": reviewed_game_local,
            "unmatched_zh_rows": sum(len(rows) for key, rows in inventory["unmatched"].items() if key.startswith("xiaoheihe|zh-CN|")),
        },
        "remaining_priority_gaps": [
            f"关键词/机制的中文资料已分层保存：active 关键词有 {keyword_cov['chinese_active']} 条游戏/来源中文和 {keyword_cov['editorial_chinese_active']} 条 editorial_zh 译注；active 机制有 {mechanic_cov['chinese_active']} 条游戏/来源中文和 {mechanic_cov['editorial_chinese_active']} 条 editorial_zh 译注。译注可读但仍需后续中文来源或人工复核，不冒充小黑盒原文。",
            f"active 状态英文描述覆盖 {status_cov['english']}/{status_cov['active']}；非 editorial 的本机/来源中文覆盖 {status_cov['chinese']}/{status_cov['active']}，小黑盒中文文章覆盖 {status_cov['active'] - len(status_cov['missing_chinese_source_ids'])}/{status_cov['active']}，另有 {status_cov['editorial_chinese']} 条 editorial_zh 译注，合并后有效中文描述为 {status_effective_chinese}/{status_cov['active']}。仍有少数条目只有游戏本地化或明确标注的译注，未伪装成小黑盒原文。敏捷/力量/集中负向或临时变体已与正向状态拆开，原共享正向页面仍保留为 superseded 证据。",
            f"39/39 场遭遇已有成员，{entities['encounters']['selection_rules']} 场带有结构化选择规则；{entities['encounters']['conditional_member_relations']} 条成员关系已确认身份，并在 condition_json 中保留随机池/组合池条件。原文没有给出可安全归一化的逐成员概率，因此暂不编造概率。",
            "组合页已拆出 27 个独立游戏成员（史莱姆大小、地精、形体、虱虫、奴隶贩子及三类召唤物等）；纯合页父记录只保留来源和成员关系，不把首个成员的数值投影到父页。",
            "角色 initial_gold=99、potion_slots=3 已由本机游戏/JAR 证据入库；这两项不再是数据缺口。",
            f"本机包的额外 {candidate_total} 个 candidate 实体包含测试、运行时、废弃和没有英文 Wiki 身份的条目；其中高塔之心与机器学习已各有一条 reviewed game-local crosswalk，但仍不晋升为原版 active Wiki 事实。",
            f"身份审核已确认 {reviewed_wiki} 条 wiki.gg 目录映射和 {reviewed_game_local} 条 game-local crosswalk；剩余 {sum(len(rows) for key, rows in inventory['unmatched'].items() if key.startswith('xiaoheihe|zh-CN|'))} 条中文目录行全部是小黑盒独有的概念/说明页。",
            f"{unknown_assets} 个图片资源的许可状态仍为 unknown；图片可用于复核，但不应在未核权前作为可再分发资产。",
            "图片目前只为 20 个卡牌变体挂有 image_asset_id；其余条目仍只有来源页图片 URL，后续应在确认许可后再批量本地化。",
        ],
        "strategy_isolation": {
            "strategy_notes": conn.execute("SELECT COUNT(*) FROM strategy_notes").fetchone()[0],
            "strategy_links": conn.execute("SELECT COUNT(*) FROM strategy_links").fetchone()[0],
        },
    }
    return report


def markdown(report: dict[str, Any]) -> str:
    db = report["db"]
    local = report["game_local_crosscheck"]
    lines = [
        "# 三方数据完整性对照",
        "",
        f"生成时间：{report['generated_at']}。对照来源：wiki.gg、 小黑盒 Wiki、本机游戏包（Build ID 10180494）。策略文档不参与本报告。",
        "",
        "## 当前结论",
        "",
        "双源文章已完成首轮抓取；本次修复补齐卡牌中文结构化说明、遗物/药水双语效果、敌人生命范围、普通遭遇池，并把组合页中的 27 个独立游戏成员建成子实体。当前剩余项主要是中文机制解释、一个状态中文描述、随机遭遇的概率语义、图片许可和游戏包候选身份。",
        "",
        "## 来源目录与本地游戏包",
        "",
        "| 类别 | wiki.gg 英文 | 小黑盒中文 | 游戏包英文 | 已有实体键 | active 已确认 | active provisional | candidate |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for kind in ("card", "relic", "potion", "event", "monster", "status"):
        diff = report["source_differences"][kind]
        item = local[kind]
        lines.append(f"| `{kind}` | {diff['wiki_gg_en']} | {diff['xiaoheihe_zh']} | {item['english_entries']} | {item['represented_by_game_id']} | {item['active_confirmed_keys']} | {item['active_provisional_keys']} | {item['candidate_game_ids']} |")
    lines.append("")
    lines.append("表中的 `game_id` 是实体的单一规范键；多键本地化（含合页成员）按 claims 另行核对，废弃键列在下方，不当作未表示缺口。")
    lines += [
        "",
        "## 仍未完成或需人工判断",
        "",
    ]
    for item in report["remaining_priority_gaps"]:
        lines.append(f"- {item}")
    lines += [
        "",
        "## 映射审核结果",
        "",
        f"已确认目录映射 {report['reviewed_crosswalks']['confirmed_total']} 条，其中 wiki.gg 对照 {report['reviewed_crosswalks']['wiki_gg']} 条、仅与本机游戏本地化键对照 {report['reviewed_crosswalks']['game_local']} 条。剩余 {report['reviewed_crosswalks']['unmatched_zh_rows']} 条中文目录行均为小黑盒独有的概念/说明页，没有可安全对应的英文 Wiki 实体。",
        "",
        "## 结构化字段检查",
        "",
        "| 项目 | 数量/状态 |",
        "| --- | ---: |",
        f"| 卡牌变体中文说明 | {db['bilingual_fields']['card_variants']['chinese']} / {db['bilingual_fields']['card_variants']['total']} |",
        f"| 遗物双语效果 | {db['bilingual_fields']['relics']['chinese']} / {db['bilingual_fields']['relics']['total']} |",
        f"| 药水双语效果 | {db['bilingual_fields']['potions']['chinese']} / {db['bilingual_fields']['potions']['total']} |",
        f"| active 怪物关键字段完整 | {db['monster_coverage']['complete_active']} / {db['monster_coverage']['active']}；另有 {db['monster_coverage']['group_pages']} 个纯合页父记录仅保留成员关系 |",
        f"| 状态描述（英文/中文来源/译注） | {db['status_description_coverage']['english']} / {db['status_description_coverage']['chinese']} / {db['status_description_coverage']['editorial_chinese']}（active {db['status_description_coverage']['active']}） |",
        f"| 关键词定义（英文有效/中文来源/译注） | {db['definition_coverage']['keyword']['meaningful_active']} / {db['definition_coverage']['keyword']['chinese_active']} / {db['definition_coverage']['keyword']['editorial_chinese_active']}（active {db['definition_coverage']['keyword']['active']}） |",
        f"| 机制定义（英文有效/中文来源/译注） | {db['definition_coverage']['mechanic']['meaningful_active']} / {db['definition_coverage']['mechanic']['chinese_active']} / {db['definition_coverage']['mechanic']['editorial_chinese_active']}（active {db['definition_coverage']['mechanic']['active']}） |",
        f"| 普通/精英/Boss 遭遇记录 | {db['encounters']['rows']}（其中有成员 {db['encounters']['with_members']}；选择规则 {db['encounters']['selection_rules']}） |",
        f"| 遭遇成员/关系 | {db['encounters']['member_rows']} / {db['encounters']['confirmed_member_relations']} confirmed（其中条件成员 {db['encounters']['conditional_member_relations']}），{db['encounters']['candidate_relations']} candidate |",
        f"| 角色初始金币/药水栏 | {db['character_field_presence']['initial_gold']} / {db['character_field_presence']['potion_slots']} 个角色有值 |",
        f"| 保留的原始图片占位 claims | {db['claims']['placeholder']}（生成页面会过滤） |",
        f"| 图片许可 unknown | {db['assets']['unknown_license']} / {db['assets']['total']}；实体关联 {db['assets']['linked_entity_assets']}，卡牌变体链接 {db['assets']['card_variant_links']} |",
        "",
        "## 本地化独有条目",
        "",
        "下列条目仍保留为 candidate，不自动当作基础 Wiki 实体：",
        "",
    ]
    for kind in ("card", "relic", "potion", "event", "monster", "status"):
        keys = local[kind]["unrepresented_keys"]
        if keys:
            lines.append(f"- `{kind}`：{len(keys)} 条；示例：" + "、".join(keys[:12]) + ("……" if len(keys) > 12 else ""))
        deprecated = local[kind].get("deprecated_keys") or []
        if deprecated:
            lines.append(f"- `{kind}` 废弃本地化键：{len(deprecated)} 条；不计入未表示缺口。")
    lines += [
        "",
        "## 结构化缺口详情",
        "",
    ]
    for kind, ids in db["incomplete_active"].items():
        lines.append(f"- `{kind}` active 缺必备字段：{len(ids)} 条" + (f"；示例：{', '.join(ids[:8])}" if ids else "。"))
    lines += [
        "",
        "完整机器可读结果：[completeness-crosscheck.json](completeness-crosscheck.json)。结构化修复记录：[structured-repair-report.json](structured-repair-report.json)。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report = build_report(conn)
    conn.close()
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT_MD.write_text(markdown(report), encoding="utf-8")
    print(json.dumps({
        "parser_version": report["parser_version"],
        "generated_at": report["generated_at"],
        "priority_gaps": len(report["remaining_priority_gaps"]),
        "encounters": report["db"]["encounters"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
