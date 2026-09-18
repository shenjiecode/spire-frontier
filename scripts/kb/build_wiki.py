"""Generate the first linked Markdown Wiki from data/spire.sqlite.

Markdown files are generated output.  Edit sources or review decisions in the
database/staging layer, then rerun this command; do not hand-edit generated
entity pages.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "spire.sqlite"
WIKI_ROOT = ROOT / "docs" / "wiki"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def pretty(value_json: str | None) -> str:
    if value_json is None:
        return ""
    if not isinstance(value_json, str):
        return json.dumps(value_json, ensure_ascii=False, sort_keys=True)
    try:
        value = json.loads(value_json)
    except Exception:
        return value_json
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def safe_slug(entity_id: str) -> str:
    # Use the complete project ID so same-name cards (Strike/Defend) and
    # source candidates cannot overwrite one another on disk.  The ID is
    # stable across runs, while display names remain human-friendly in the
    # page title and index.
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", entity_id).strip("_") or "entity"


def entity_path(kind: str, entity_id: str) -> Path:
    folder = {
        "character": "characters",
        "card": "cards",
        "relic": "relics",
        "potion": "potions",
        "monster": "monsters",
        "encounter": "encounters",
        "event": "events",
        "status": "statuses",
        "keyword": "keywords",
        "mechanic": "mechanics",
        "resource": "mechanics",
        "concept": "mechanics",
    }.get(kind, "other")
    return WIKI_ROOT / folder / f"{safe_slug(entity_id)}.md"


def rel_link(from_path: Path, to_path: Path) -> str:
    return Path(os.path.relpath(to_path, from_path.parent)).as_posix()


def names(conn: sqlite3.Connection, entity_id: str) -> dict[str, str]:
    rows = conn.execute(
        """SELECT language, name FROM names WHERE entity_id=?
           ORDER BY is_preferred DESC, CASE name_kind WHEN 'preferred' THEN 0 WHEN 'source_name' THEN 1 ELSE 2 END, name""",
        (entity_id,),
    ).fetchall()
    result: dict[str, str] = {}
    for language, name in rows:
        result.setdefault(language, name)
    return result


def source_page(conn: sqlite3.Connection, page_id: str | None) -> sqlite3.Row | None:
    if not page_id:
        return None
    return conn.execute("SELECT * FROM source_pages WHERE id=?", (page_id,)).fetchone()


def source_label(conn: sqlite3.Connection, page_id: str | None) -> str:
    page = source_page(conn, page_id)
    if not page:
        return "未知来源"
    title = page["title"] or page["source_page_key"] or page_id
    return f"[{title}]({page['url']})"


def claim_rows(conn: sqlite3.Connection, entity_id: str) -> list[sqlite3.Row]:
    return conn.execute(
        """SELECT c.*, r.status AS resolution_status, r.value_json AS resolved_value,
                  r.rationale AS resolution_rationale
           FROM claims c LEFT JOIN resolutions r
             ON r.subject_entity_id=c.subject_entity_id
            AND r.variant_id IS c.variant_id
            AND r.field_path=c.field_path
           WHERE c.subject_entity_id=?
           ORDER BY c.field_path, c.variant_id, c.language, c.created_at DESC, c.id DESC""",
        (entity_id,),
    ).fetchall()


def evidence_section(conn: sqlite3.Connection, entity_id: str, output: Path) -> list[str]:
    lines = ["## 来源与核对状态", "", "字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。", "", "| 字段 | 值 | 状态 | 来源 |", "| --- | --- | --- | --- |"]
    seen: set[tuple[str, str | None, str | None]] = set()
    for row in claim_rows(conn, entity_id):
        key = (row["field_path"], row["variant_id"], row["language"])
        if key in seen:
            continue
        seen.add(key)
        value = row["resolved_value"] or row["value_json"]
        text = pretty(value).replace("\n", "<br>")
        # Placeholder captions belong to the source rendering, not the
        # published knowledge page.  The untouched HTML snapshot remains the
        # evidence record.
        text = text.replace("请输入图片描述", "（图片未提供文字说明）")
        if len(text) > 500:
            text = text[:497] + "..."
        status = row["resolution_status"] or row["verification_status"]
        if row["notes"] and "editorial_zh" in row["notes"]:
            status = f"{status}/editorial_zh"
        variant = f" ({row['variant_id'].split(':')[-1]})" if row["variant_id"] else ""
        lines.append(f"| `{row['field_path']}{variant}` | {text} | `{status}` | {source_label(conn, row['source_page_id'])} |")
    if len(lines) == 6:
        lines.append("| — | 尚无字段级证据 | `unverified` | — |")
    lines += ["", "页面生成时间：" + now()]
    return lines


def card_details(conn: sqlite3.Connection, entity_id: str, output: Path) -> list[str]:
    row = conn.execute("SELECT * FROM cards WHERE entity_id=?", (entity_id,)).fetchone()
    if not row:
        return []
    lines = ["## 卡牌属性", "", f"- 颜色：`{row['color']}`", f"- 类型：`{row['card_type']}`", f"- 稀有度：`{row['rarity'] or '未知'}`", f"- 可获得性：`{row['availability'] or '未知'}`"]
    if row["tags_json"]:
        lines.append(f"- 标签：`{pretty(row['tags_json'])}`")
    lines += ["", "## 变体", "", "| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |", "| --- | --- | --- | --- | --- |"]
    variants = conn.execute(
        """SELECT ev.id, ev.variant_kind, ev.label, cv.cost_type, cv.cost_value,
                  cv.description_en, cv.description_zh, cv.image_asset_id, a.local_path
           FROM entity_variants ev JOIN card_variants cv ON cv.variant_id=ev.id
           LEFT JOIN assets a ON a.id=cv.image_asset_id
           WHERE ev.entity_id=? ORDER BY ev.level, ev.id""",
        (entity_id,),
    ).fetchall()
    for variant in variants:
        zh = variant["description_zh"]
        if not zh:
            zh_row = conn.execute("SELECT value_json FROM claims WHERE subject_entity_id=? AND variant_id=? AND field_path='card.description' AND language='zh-CN' ORDER BY created_at DESC LIMIT 1", (entity_id, variant["id"])).fetchone()
            zh = pretty(zh_row[0]) if zh_row else ""
        image = ""
        if variant["local_path"]:
            asset_path = ROOT / variant["local_path"]
            image = f"[查看图片]({rel_link(output, asset_path)})"
        cost = variant["cost_value"] if variant["cost_value"] is not None else ("X" if variant["cost_type"] == "x" else "未知")
        lines.append(f"| `{variant['label'] or variant['variant_kind']}` | `{cost}` | {variant['description_en'] or '未知'} | {zh or '未采集'} | {image or '未保存'} |")
    return lines


def character_details(conn: sqlite3.Connection, entity_id: str, output: Path) -> list[str]:
    row = conn.execute("SELECT * FROM characters WHERE entity_id=?", (entity_id,)).fetchone()
    if not row:
        return []
    lines = ["## 角色属性", "", "| 字段 | 值 |", "| --- | --- |"]
    if row["initial_hp"] is not None:
        lines.append(f"| `initial_hp` | {row['initial_hp']} |")
    for field, label in (("initial_gold", "initial_gold"), ("potion_slots", "potion_slots")):
        if row[field] is not None:
            lines.append(f"| `{label}` | {row[field]} |")
    if row["resource_json"]:
        lines.append(f"| `resource_json` | {pretty(row['resource_json'])} |")
    if row["mechanics_json"]:
        lines.append(f"| `mechanics_json` | {pretty(row['mechanics_json'])} |")

    relic_id = row["starting_relic_entity_id"]
    if relic_id:
        relic_names = names(conn, relic_id)
        relic_label = " / ".join(value for value in (relic_names.get("zh-CN"), relic_names.get("en")) if value) or relic_id
        relic_row = conn.execute("SELECT kind FROM entities WHERE id=?", (relic_id,)).fetchone()
        if relic_row:
            relic_href = rel_link(output, entity_path(relic_row[0], relic_id))
            lines.append(f"| `starting_relic` | [{relic_label}]({relic_href}) |")
        else:
            lines.append(f"| `starting_relic` | {relic_label} |")

    if row["starting_deck_json"]:
        try:
            deck = json.loads(row["starting_deck_json"])
        except (TypeError, json.JSONDecodeError):
            deck = []
        if isinstance(deck, list):
            lines += ["", "### 初始牌组", "", "| 卡牌 | 数量 |", "| --- | ---: |"]
            for item in deck:
                if not isinstance(item, dict):
                    continue
                card_id = item.get("entity_id")
                label = item.get("name") or card_id or "未知"
                if card_id:
                    card_names = names(conn, card_id)
                    label = " / ".join(value for value in (card_names.get("zh-CN"), card_names.get("en")) if value) or label
                    label = f"[{label}]({rel_link(output, entity_path('card', card_id))})"
                lines.append(f"| {label} | {item.get('quantity', 1)} |")
    return lines


def noncard_details(conn: sqlite3.Connection, entity_id: str, kind: str) -> list[str]:
    table = {"relic": "relics", "potion": "potions", "monster": "monsters", "encounter": "encounters", "event": "events", "status": "statuses", "keyword": "keywords", "mechanic": "mechanics"}.get(kind)
    if not table:
        return []
    row = conn.execute(f"SELECT * FROM {table} WHERE entity_id=?", (entity_id,)).fetchone()
    if not row:
        return []
    group_context = bool(
        kind == "monster"
        and row["entity_id"]
        and conn.execute("SELECT subtype FROM entities WHERE id=?", (entity_id,)).fetchone()[0] == "group_page"
    )
    if group_context:
        lines = [
            "## monster 合页上下文",
            "",
            "本页对应来源中的组合页，只保留来源正文和 `has_member` 关系。生命值与行动请查看下方成员页面；不会把某个成员的数值投影到父页。",
            "",
            "| 字段 | 值 |",
            "| --- | --- |",
        ]
    else:
        lines = [f"## {kind} 数据", "", "| 字段 | 值 |", "| --- | --- |"]
    for key in row.keys():
        if key == "entity_id" or row[key] in (None, ""):
            continue
        if group_context and key != "encounter_notes":
            continue
        value = pretty(row[key])
        value = value.replace("\n", "<br>")
        if len(value) > 800:
            value = value[:797] + "..."
        lines.append(f"| `{key}` | {value} |")
    if kind == "monster":
        moves = conn.execute("SELECT * FROM monster_moves WHERE monster_entity_id=? ORDER BY id", (entity_id,)).fetchall()
        if moves:
            lines += ["", "### 行动", "", "| 名称 | 意图 | 伤害 | 次数 | 效果 |", "| --- | --- | ---: | ---: | --- |"]
            for move in moves:
                lines.append(f"| {move['name']} | {move['intent'] or ''} | {move['damage'] if move['damage'] is not None else ''} | {move['hits'] if move['hits'] is not None else ''} | {pretty(move['effect_json'])} |")
    if kind == "event":
        options = conn.execute("SELECT * FROM event_options WHERE event_entity_id=? ORDER BY ordinal", (entity_id,)).fetchall()
        if options:
            lines += ["", "### 选项", "", "| # | 选项 | 条件/代价 | 结果 |", "| ---: | --- | --- | --- |"]
            for option in options:
                lines.append(f"| {option['ordinal']} | {option['label']} | {pretty(option['cost_json'])} | {pretty(option['outcome_json'])} |")
    return lines


def relation_section(conn: sqlite3.Connection, entity_id: str, output: Path, *, reverse: bool = False) -> list[str]:
    if reverse:
        rows = conn.execute("SELECT r.*, e.kind, e.id AS other_id FROM relations r JOIN entities e ON e.id=r.source_entity_id WHERE r.target_entity_id=? AND r.status != 'rejected' ORDER BY r.relation_type, r.source_entity_id", (entity_id,)).fetchall()
        heading = "被哪些条目引用"
        other_col = "source_entity_id"
    else:
        rows = conn.execute("SELECT r.*, e.kind, e.id AS other_id FROM relations r JOIN entities e ON e.id=r.target_entity_id WHERE r.source_entity_id=? AND r.status != 'rejected' ORDER BY r.relation_type, r.target_entity_id", (entity_id,)).fetchall()
        heading = "相关条目"
        other_col = "target_entity_id"
    lines = [f"## {heading}", ""]
    if not rows:
        lines.append("暂无已确认关系。")
        return lines
    for row in rows:
        other = conn.execute("SELECT kind FROM entities WHERE id=?", (row["other_id"],)).fetchone()
        target_path = entity_path(other[0], row["other_id"])
        target_names = names(conn, row["other_id"])
        label = " / ".join(x for x in (target_names.get("zh-CN"), target_names.get("en")) if x) or row["other_id"]
        condition = f"；条件：`{pretty(row['condition_json'])}`" if row["condition_json"] else ""
        status = f"（{row['status']}）" if row["status"] != "confirmed" else ""
        suffix = f" {status}{condition}" if status or condition else ""
        lines.append(f"- `{row['relation_type']}` → [{label}]({rel_link(output, target_path)}){suffix}")
    return lines


def strategy_section(conn: sqlite3.Connection, entity_id: str, output: Path) -> list[str]:
    rows = conn.execute("SELECT sn.*, sl.link_kind, sl.condition_json, sl.excerpt FROM strategy_links sl JOIN strategy_notes sn ON sn.id=sl.strategy_note_id WHERE sl.entity_id=? ORDER BY sn.id", (entity_id,)).fetchall()
    if not rows:
        # Foundational Wiki pages intentionally remain independent from the
        # separately maintained strategy documents.  Keep this renderer
        # extensible for a future opt-in strategy layer, but do not emit an
        # empty heading or a misleading "暂无" placeholder today.
        return []
    lines = ["## 攻略关联", ""]
    for row in rows:
        target = ROOT / row["document_path"]
        href = rel_link(output, target)
        if row["chapter_anchor"]:
            href += row["chapter_anchor"] if row["chapter_anchor"].startswith("#") else "#" + row["chapter_anchor"]
        excerpt = f"：{row['excerpt']}" if row["excerpt"] else ""
        lines.append(f"- `{row['link_kind']}` [{row['title']}]({href}){excerpt}")
    return lines


def write_sources(conn: sqlite3.Connection) -> None:
    path = WIKI_ROOT / "sources.md"
    lines = ["# 来源与许可", "", f"最近生成：{now()}", "", "原始快照保存在 `data/raw/`，数据库中的 `source_pages` 保存页面哈希、抓取时间和最终 URL。", "", "## 来源", "", "| 来源 | 语言 | 许可 | 范围说明 |", "| --- | --- | --- | --- |"]
    for row in conn.execute("SELECT * FROM sources ORDER BY id"):
        lines.append(f"| [{row['name']}]({row['base_url']}) | `{row['language']}` | `{row['license'] or 'unknown'}` | {row['scope_note'] or ''} |")
    lines += ["", "## 已保存页面", "", "| 页面 | 来源 | 抓取时间 | 快照 |", "| --- | --- | --- | --- |"]
    for row in conn.execute("SELECT sp.*, s.name AS source_name FROM source_pages sp JOIN sources s ON s.id=sp.source_id ORDER BY sp.source_id, sp.url"):
        snapshot = row["snapshot_path"] or ""
        snap_link = f"[{Path(snapshot).name}]({rel_link(path, ROOT / snapshot)})" if snapshot and (ROOT / snapshot).exists() else snapshot
        lines.append(f"| [{row['title'] or row['source_page_key']}]({row['url']}) | {row['source_name']} | {row['fetched_at']} | {snap_link} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_inventory(conn: sqlite3.Connection) -> None:
    """Render the current directory snapshot and mapping totals.

    ``discover_inventory.py`` writes the first P2 view, but later review
    passes add manually confirmed mappings and a few source rows.  Keeping
    this page generated from SQLite prevents it from showing stale P2
    counts after a repair/audit run.
    """
    path = WIKI_ROOT / "inventory.md"
    rows = conn.execute(
        """SELECT source_id, language, entity_kind, status, COUNT(*) AS n
           FROM inventory_items
           GROUP BY source_id, language, entity_kind, status
           ORDER BY source_id, language, entity_kind, status"""
    ).fetchall()
    total = conn.execute("SELECT COUNT(*) FROM inventory_items WHERE status != 'excluded'").fetchone()[0]
    excluded = conn.execute("SELECT COUNT(*) FROM inventory_items WHERE status = 'excluded'").fetchone()[0]
    confirmed = conn.execute("SELECT COUNT(*) FROM inventory_mappings WHERE status = 'confirmed'").fetchone()[0]
    candidate = conn.execute("SELECT COUNT(*) FROM inventory_mappings WHERE status = 'candidate'").fetchone()[0]
    lines = [
        "# 双源目录与身份审核视图（P2）",
        "",
        f"生成时间：{now()}。本页由当前 SQLite 目录重建；目录发现、文章采集和身份确认仍是不同层级。",
        "",
        "- [目录 CSV](../../data/exports/inventory.csv)",
        "- [目录 JSONL](../../data/exports/inventory.jsonl)",
        "- [中英文映射清单](../../data/exports/name_mapping.csv)",
        "",
        "## 目录数量",
        "",
        "| 来源 | 语言 | 类别 | 状态 | 数量 |",
        "| --- | --- | --- | --- | ---: |",
    ]
    for row in rows:
        lines.append(f"| `{row['source_id']}` | `{row['language']}` | `{row['entity_kind']}` | `{row['status']}` | {row['n']} |")
    lines += [
        "",
        "## 读取说明",
        "",
        "- wiki.gg 的目录按 StS1 范围保存；小黑盒目录来自用户指定 Wiki 的公开首页 JSON，文章快照保存在 `data/raw/`。",
        "- `confirmed` 映射是经过英文 Wiki、中文文章和/或本机游戏本地化核对的身份关系；`candidate` 只表示待审线索。",
        "- 目录行不等于规则事实。规则字段要看对应实体页的 claims、来源和验证状态。",
        "",
        "## 当前审核计数",
        "",
        f"- 有效目录行：{total}；排除目录行：{excluded}。",
        f"- 已确认身份映射：{confirmed}；候选映射：{candidate}。",
        "- [身份审核队列](mapping-review.md)；[三方完整性对照](../../reports/completeness-crosscheck.md)。",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def clean_stale_entity_pages(paths: dict[str, Path]) -> int:
    """Remove generated entity pages for entities no longer in SQLite.

    Candidate rows can be merged into a canonical entity between runs.  The
    old Markdown file must not survive that merge, otherwise readers see a
    second, stale page that is absent from the database and index.
    """
    current = {path.resolve() for path in paths.values()}
    removed = 0
    for folder in {
        "cards",
        "characters",
        "encounters",
        "events",
        "keywords",
        "mechanics",
        "monsters",
        "potions",
        "relics",
        "statuses",
    }:
        directory = WIKI_ROOT / folder
        if not directory.exists():
            continue
        for candidate in directory.glob("sts1_*.md"):
            if candidate.resolve() not in current:
                candidate.unlink()
                removed += 1
    return removed


def write_coverage(conn: sqlite3.Connection) -> None:
    rows = conn.execute("SELECT kind, COUNT(*) AS n FROM entities GROUP BY kind ORDER BY kind").fetchall()
    latest_run = conn.execute("SELECT parser_version FROM build_runs WHERE status='success' AND parser_version LIKE 'kb-p3-content/%' ORDER BY started_at DESC LIMIT 1").fetchone()
    if latest_run:
        pending = conn.execute("SELECT COUNT(*) FROM inventory_items WHERE entity_kind IN ('event','monster','status','keyword','mechanic') AND status NOT IN ('parsed','excluded')").fetchone()[0]
        if pending:
            scope_note = f"当前已完成 P3 首轮双源内容采集；卡牌、遗物、药水已进入结构化字段，角色/概念页已保存来源证据，其他类别的已采集条目仍需动作/分支字段审阅，尚有 {pending} 条目录行未抓取。P2 双源目录单独统计，目录发现不等于事实核验完成。"
        else:
            scope_note = "当前已完成 P3 首轮双源内容采集；卡牌、遗物、药水已进入结构化字段，角色/敌人/事件/状态/关键词/机制已保存正文并完成保守字段解析，身份映射和人工抽检仍需继续。P2 双源目录单独统计，目录发现不等于事实核验完成。"
    else:
        scope_note = "当前为 P1 纵向样本；P2 双源目录单独统计，不能把目录发现当作事实核验完成。"
    entity_total = conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
    active_total = conn.execute("SELECT COUNT(*) FROM entities WHERE lifecycle='active'").fetchone()[0]
    candidate_total = conn.execute("SELECT COUNT(*) FROM entities WHERE lifecycle='candidate'").fetchone()[0]
    name_total = conn.execute("SELECT COUNT(*) FROM names").fetchone()[0]
    claim_total = conn.execute("SELECT COUNT(*) FROM claims").fetchone()[0]
    relation_total = conn.execute("SELECT COUNT(*) FROM relations").fetchone()[0]
    source_page_total = conn.execute("SELECT COUNT(*) FROM source_pages").fetchone()[0]
    asset_total = conn.execute("SELECT COUNT(*) FROM assets").fetchone()[0]
    wiki_page_total = sum(1 for _ in WIKI_ROOT.rglob("*.md"))
    lines = ["# 覆盖与缺口", "", f"本页由 SQLite 生成，时间：{now()}。{scope_note}", "", "## 当前数量", "", f"实体共 {entity_total} 个（active {active_total}，candidate {candidate_total}）；名称 {name_total} 个，claims {claim_total} 条，关系 {relation_total} 条，来源页面 {source_page_total} 个，图片资源 {asset_total} 个。当前生成目录包含约 {wiki_page_total} 个 Markdown 页面。", "", "| 实体类别 | 数量 |", "| --- | ---: |"]
    for row in rows:
        lines.append(f"| `{row['kind']}` | {row['n']} |")
    inventory_rows = conn.execute("SELECT source_id, language, entity_kind, status, COUNT(*) AS n FROM inventory_items GROUP BY source_id, language, entity_kind, status ORDER BY source_id, language, entity_kind, status").fetchall()
    if inventory_rows:
        lines += ["", "## P2 双源目录", "", "| 来源 | 语言 | 类别 | 状态 | 数量 |", "| --- | --- | --- | --- | ---: |"]
        for row in inventory_rows:
            lines.append(f"| `{row['source_id']}` | `{row['language']}` | `{row['entity_kind']}` | `{row['status']}` | {row['n']} |")
        mapping_count = conn.execute("SELECT COUNT(*) FROM inventory_mappings").fetchone()[0]
        lines += ["", f"P2 当前保存 {sum(row['n'] for row in inventory_rows)} 条目录行，已生成 {mapping_count} 条确认映射记录；其余身份仍需逐项审阅或保留为候选。"]
    if (ROOT / "reports" / "p3-content-report.json").exists():
        lines += ["", "## P3 内容采集", "", "- [P3 内容采集报告](../../reports/p3-content-report.json)"]
        for kind, label in (("card", "卡牌"), ("relic", "遗物"), ("potion", "药水"), ("monster", "敌人"), ("event", "事件"), ("status", "状态"), ("keyword", "关键词"), ("mechanic", "机制"), ("character", "角色"), ("concept", "概念")):
            en = conn.execute("SELECT COUNT(*) FROM inventory_items WHERE entity_kind=? AND language='en' AND status='parsed'", (kind,)).fetchone()[0]
            zh = conn.execute("SELECT COUNT(*) FROM inventory_items WHERE entity_kind=? AND language='zh-CN' AND status='parsed'", (kind,)).fetchone()[0]
            lines.append(f"- {label}：英文 {en}，中文 {zh} 条文章已采集并解析；未确认身份保留为候选实体。")
    game_reports = [
        ("game-localization-report.json", "游戏本地化导入报告"),
        ("game-localization-extended-report.json", "游戏本地化扩展导入报告"),
    ]
    loaded_game_reports: list[tuple[str, str, dict[str, object]]] = []
    for report_name, report_label in game_reports:
        report_path = ROOT / "reports" / report_name
        if not report_path.exists():
            continue
        try:
            report = json.loads(report_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            report = {}
        loaded_game_reports.append((report_name, report_label, report))
    if loaded_game_reports:
        lines += ["", "## 游戏包第三来源", ""]
        jar_seen = False
        total_decisions = 0
        for report_name, report_label, game_report in loaded_game_reports:
            lines.append(f"- [{report_label}](../../reports/{report_name})")
            jar = game_report.get("jar") or {}
            if not jar_seen and (jar.get("steam_build_id") or jar.get("jar_sha256")):
                lines.append(f"- Steam Build ID：`{jar.get('steam_build_id') or 'unknown'}`；JAR SHA-256：`{jar.get('jar_sha256') or 'unknown'}`。")
                jar_seen = True
            for kind, detail in sorted((game_report.get("kinds") or {}).items()):
                lines.append(f"  - `{kind}`：本地化条目 {detail.get('english_entries', 0)}，已唯一对应现有实体 {detail.get('matched_canonical', 0)}，保留候选 {detail.get('new_candidates', 0)}。")
            decisions = int(game_report.get("decisions") or 0)
            cumulative = int(game_report.get("cumulative_decisions") or 0)
            total_decisions += cumulative if cumulative else decisions
            if cumulative and cumulative != decisions:
                if game_report.get("decisions_preserved"):
                    lines.append(f"  - 本次重放无新增决定，保留已有审核 CSV；扩展决定文件累计 {cumulative} 条。")
                else:
                    lines.append(f"  - 本批精确游戏名映射审核决定：{decisions} 条；扩展决定文件累计 {cumulative} 条。")
            else:
                lines.append(f"  - 本批精确游戏名映射审核决定：{decisions} 条。")
        lines.append(f"- 两批本地化导入共记录 {total_decisions} 条目录映射决定；实体合并另由显式 CSV 控制，未确认身份仍保留候选。")
    if (ROOT / "reports" / "entity-resolution-review.md").exists():
        lines += ["", "## 高风险身份复核", "", "- [实体身份复核记录](../../reports/entity-resolution-review.md)"]
    if (WIKI_ROOT / "mapping-review.md").exists():
        lines += ["", "## 身份审核", "", "- [中英文身份映射审核队列](mapping-review.md)", "- [审核队列 CSV](../../data/decisions/mapping-review.csv)", "- [审核队列 JSON](../../reports/mapping-review.json)"]
    if (WIKI_ROOT / "p4-rule-audit.md").exists():
        lines += ["", "## P4 规则核验", "", "- [P4 机制与规则核验审计](p4-rule-audit.md)", "- [P4 审计 JSON](../../reports/p4-rule-audit.json)"]
    if (ROOT / "reports" / "completeness-crosscheck.md").exists():
        lines += ["", "## 三方完整性对照", "", "- [三方数据完整性对照](../../reports/completeness-crosscheck.md)", "- [机器可读对照结果](../../reports/completeness-crosscheck.json)", "- [结构化修复记录](../../reports/structured-repair-report.json)"]
    pending_rows = conn.execute(
        """SELECT entity_kind, language, COUNT(*) AS n
           FROM inventory_items
           WHERE status NOT IN ('parsed', 'excluded')
           GROUP BY entity_kind, language
           ORDER BY entity_kind, language"""
    ).fetchall()
    if pending_rows:
        pending_text = "；".join(f"{row['entity_kind']}/{row['language']} {row['n']} 条" for row in pending_rows)
        pending_bullet = f"- 仍有目录行未完成文章解析：{pending_text}。"
    else:
        pending_bullet = "- 当前已发现的双源目录行均已完成首轮文章采集；后续重点是字段级抽检和身份映射，而不是重复抓取。"
    lines += ["", "## 状态解释", "", "- `single_source`：只有一站提供或当前只采集到一站。", "- `provisional`：已选择一个候选值，但尚未由第二来源或游戏数据确认。", "- `conflict`：来源值存在差异，保留双方证据。", "- `verified_game`：由本地游戏数据或可复现实验核实。", "", "## 当前缺口", "", "- 中英文大多数条目尚未完成身份审阅；候选实体不能当作双语确认事实。", "- wiki.gg 能量图标和小黑盒图片承载的数值仍需视觉/字段交叉核对。", "- 图片许可目前均标为 `unknown`，不自动将网页文本许可扩展到游戏图片。", pending_bullet, "- 未解决映射、冲突字段和复杂机制必须继续补齐，不能用模型记忆填充。", "- 两份攻略保持独立；当前策略表为空，基础 Wiki 不生成攻略关联。"]
    (WIKI_ROOT / "coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_index(conn: sqlite3.Connection, paths: dict[str, Path]) -> None:
    latest_run = conn.execute("SELECT parser_version FROM build_runs WHERE status='success' AND parser_version LIKE 'kb-p3-content/%' ORDER BY started_at DESC LIMIT 1").fetchone()
    stage = "P3 双源内容采集首轮" if latest_run else "P1 纵向样本"
    lines = ["# 杀戮尖塔 1 双语知识 Wiki", "", f"生成时间：{now()}。当前阶段：{stage}。", "", "数据库：[`data/spire.sqlite`](../../data/spire.sqlite)；生成脚本：[`bootstrap_sample.py`](../../scripts/kb/bootstrap_sample.py)、[`discover_inventory.py`](../../scripts/kb/discover_inventory.py)、[`fetch_p3.py`](../../scripts/kb/fetch_p3.py)、[`build_wiki.py`](../../scripts/kb/build_wiki.py)。", "", "## 实体目录"]
    current_kind = None
    for row in conn.execute("SELECT id, kind FROM entities ORDER BY kind, id"):
        if row["kind"] != current_kind:
            current_kind = row["kind"]
            lines += ["", f"### {current_kind}", ""]
        n = names(conn, row["id"])
        label = " / ".join(x for x in (n.get("zh-CN"), n.get("en")) if x) or row["id"]
        lines.append(f"- [{label}]({Path(os.path.relpath(paths[row['id']], WIKI_ROOT)).as_posix()}) — `{row['id']}`")
    lines += ["", "## 资料与状态", "", "- [来源与许可](sources.md)", "- [覆盖与缺口](coverage.md)", "- [中英文映射 CSV](../../data/exports/name_mapping.csv)", "- [实体映射 CSV](../../data/exports/entity_name_mapping.csv)", "- [审核决定说明](../../data/decisions/README.md)", "- [P1 样本报告](../../reports/p1-sample-report.json)"]
    if (ROOT / "reports" / "p3-content-report.json").exists():
        lines.append("- [P3 内容采集报告](../../reports/p3-content-report.json)")
    if (ROOT / "reports" / "game-localization-report.json").exists():
        lines.append("- [游戏本地化导入报告](../../reports/game-localization-report.json)")
    if (ROOT / "reports" / "game-localization-extended-report.json").exists():
        lines.append("- [游戏本地化扩展导入报告](../../reports/game-localization-extended-report.json)")
    if (ROOT / "reports" / "entity-resolution-review.md").exists():
        lines.append("- [实体身份复核记录](../../reports/entity-resolution-review.md)")
    if (WIKI_ROOT / "mapping-review.md").exists():
        lines.append("- [中英文身份映射审核队列](mapping-review.md)")
    if (WIKI_ROOT / "p4-rule-audit.md").exists():
        lines.append("- [P4 机制与规则核验审计](p4-rule-audit.md)")
    if (ROOT / "reports" / "completeness-crosscheck.md").exists():
        lines.append("- [三方数据完整性对照](../../reports/completeness-crosscheck.md)")
    if (WIKI_ROOT / "inventory.md").exists():
        lines.append("- [P2 双源目录](inventory.md)")
    lines += ["", "## 读取原则", "", "条目中的规则字段与攻略观点分开；`provisional` 和 `single_source` 需要在回答中带出，不应写成无条件真值。"]
    (WIKI_ROOT / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_entity(conn: sqlite3.Connection, row: sqlite3.Row, paths: dict[str, Path]) -> None:
    entity_id = row["id"]
    output = paths[entity_id]
    output.parent.mkdir(parents=True, exist_ok=True)
    n = names(conn, entity_id)
    # Runtime candidates occasionally have only a game key or one localized
    # label.  Use an explicit absence marker instead of the generic
    # "Unnamed" title, which made it look like a parser failure.
    zh = n.get("zh-CN") or "（暂无中文名）"
    en = n.get("en") or row["game_id"] or "（暂无英文名）"
    lines = [f"# {zh} / {en}", "", f"> 稳定 ID：`{entity_id}`  ", f"> 类别：`{row['kind']}`；游戏：`{row['game']}`；映射状态：`{row['mapping_status']}`", "", "## 名称", "", f"- 中文：{zh}", f"- English: {en}"]
    aliases = conn.execute("SELECT language, name, name_kind, verification_status FROM names WHERE entity_id=? AND name_kind IN ('alias','old_alias','candidate') ORDER BY language, name", (entity_id,)).fetchall()
    if aliases:
        lines += ["", "别名/候选：" + "；".join(f"{a['name']} (`{a['language']}`, {a['verification_status']})" for a in aliases)]
    lines += [""]
    if row["kind"] == "card":
        lines += card_details(conn, entity_id, output)
    elif row["kind"] == "character":
        lines += character_details(conn, entity_id, output)
    else:
        lines += noncard_details(conn, entity_id, row["kind"])
    sections = [relation_section(conn, entity_id, output), relation_section(conn, entity_id, output, reverse=True), strategy_section(conn, entity_id, output), evidence_section(conn, entity_id, output)]
    for section in sections:
        if section:
            lines += [""] + section
    output.write_text("\n".join(lines).replace("\n\n\n", "\n\n") + "\n", encoding="utf-8")


def main() -> int:
    if not DB_PATH.exists():
        raise SystemExit("data/spire.sqlite not found; run bootstrap_sample.py first")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    WIKI_ROOT.mkdir(parents=True, exist_ok=True)
    paths = {row["id"]: entity_path(row["kind"], row["id"]) for row in conn.execute("SELECT id, kind FROM entities")}
    reverse_paths: dict[Path, str] = {}
    for entity_id, path in paths.items():
        previous = reverse_paths.setdefault(path, entity_id)
        if previous != entity_id:
            raise RuntimeError(f"entity page path collision: {previous} and {entity_id} -> {path}")
    removed = clean_stale_entity_pages(paths)
    for row in conn.execute("SELECT * FROM entities ORDER BY kind, id"):
        write_entity(conn, row, paths)
    write_sources(conn)
    write_inventory(conn)
    write_coverage(conn)
    write_index(conn, paths)
    conn.close()
    print(f"generated {len(paths)} entity pages under {WIKI_ROOT}; removed {removed} stale pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
