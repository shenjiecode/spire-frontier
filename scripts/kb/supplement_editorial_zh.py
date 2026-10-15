"""Add explicitly labelled Chinese editorial supplements and status fixes.

The two project Wiki sources do not provide a Chinese keyword/Mechanics
section for every English entry.  This module fills the readable Chinese
summary from the already captured English Wiki text, while keeping the
provenance explicit (``editorial_zh``).  It also corrects synthetic status
records whose shared Dexterity/Strength page was parsed as the positive
variant.  No strategy document is read here.
"""

from __future__ import annotations

import json
import sqlite3
from typing import Any

from bootstrap_sample import DB_PATH, add_claim, add_name, json_text, utc_now


PARSER_VERSION = "kb-editorial-supplement/0.1"


# These seven records are section/glossary entries from the English Keywords
# page.  They have no separate Chinese article in the selected source, so the
# summaries below are deliberately short and are labelled editorial_zh.
KEYWORD_ZH: dict[str, tuple[str, str]] = {
    "sts1.keyword.cards": (
        "卡牌",
        "卡牌在战斗中从手牌打出；角色以起始牌组开始，战斗外可以获得、移除、升级或变化卡牌。",
    ),
    "sts1.keyword.discard": (
        "弃牌",
        "将手牌中的牌放入弃牌堆。回合结束时自动把手牌放入弃牌堆，不会触发弃牌相关效果。",
    ),
    "sts1.keyword.energy": (
        "能量",
        "能量用于打出卡牌；角色通常在每回合开始获得 3 点能量，也可以由卡牌或遗物改变。",
    ),
    "sts1.keyword.orb_types": (
        "充能球类型",
        "闪电球被动或激发时造成伤害；冰霜球提供格挡；黑暗球逐回合储存伤害并在激发时攻击生命值最低的敌人；等离子球提供能量。集中会影响前三类充能球，但不影响等离子球。",
    ),
    "sts1.keyword.orbs": (
        "充能球",
        "充能球是故障机器人的专属机制。它们占据充能球栏位，并在回合结束触发被动效果；栏位已满时生成新的充能球会先激发最右侧的球。激发会消耗最右侧的球并触发其激发效果。",
    ),
    "sts1.keyword.sources": (
        "来源",
        "该栏目列出某个关键词或机制在卡牌、遗物和药水中的来源；它是 Wiki 索引分组，不是独立的游戏状态。",
    ),
    "sts1.keyword.triggers": (
        "触发",
        "该栏目列出会因对应机制而触发效果的卡牌和遗物；它是 Wiki 索引分组，不是独立的游戏状态。",
    ),
}


MECHANIC_ZH: dict[str, tuple[str, str]] = {
    "sts1.mechanic.acts": ("幕", "游戏通常分为三幕：Exordium、City 和 Beyond；每幕 17 层，末尾有 Boss 战。用铁甲战士、静默和故障机器人各通关一次后解锁可选的第四幕 Ending。"),
    "sts1.mechanic.ascensions": ("进阶", "进阶会在使用同一角色通关后逐级解锁，并增加运行难度；进阶不会影响连胜记录。"),
    "sts1.mechanic.block": ("格挡", "格挡在下回合开始前抵挡伤害，通常会在玩家回合开始时清除；壁垒、模糊和卡利铂斯等效果可以改变这一规则。"),
    "sts1.mechanic.card_piles": ("牌堆", "牌不在手牌中时位于抽牌堆、弃牌堆或消耗牌堆。抽牌堆抽空会把弃牌堆洗回；消耗的牌在本场战斗结束前不能正常取回。"),
    "sts1.mechanic.cards": ("卡牌", "每名角色以 10 或 12 张起始牌组开始。卡牌在战斗中打出，战斗外可以加入、移除、升级或变化。"),
    "sts1.mechanic.chests": ("宝箱", "非 Boss 宝箱分为小、中、大三种，出现率约为 50%、33% 和 17%，并按宝箱类型抽取遗物稀有度与金币；Boss 宝箱提供 Boss 遗物三选一。"),
    "sts1.mechanic.enemy_turn": ("敌方回合", "敌人的行动由头顶可见的意图决定；多敌人战斗中，敌人按从左到右的顺序行动。"),
    "sts1.mechanic.exhaust": ("消耗", "被消耗的牌会从战斗中移除，直到本场战斗结束；它们进入消耗牌堆，通常不能再被抽到。"),
    "sts1.mechanic.floors_and_floor_types": ("楼层与房间类型", "完成当前楼层的战斗或事件后，通过地图前往下一层；只能选择与当前节点有虚线相连的节点。地图节点有多种房间类型。"),
    "sts1.mechanic.gold": ("金币", "金币是高塔中的货币，可从战斗奖励、事件、宝箱和部分遗物/卡牌获得，并可在商人或部分事件中消费。"),
    "sts1.mechanic.hand": ("手牌", "手牌是抽到但尚未打出的卡牌所在区域；只要有足够能量，玩家可以在自己的回合打出手牌。手牌最多容纳 10 张。"),
    "sts1.mechanic.hand_size_limit": ("手牌上限", "手牌最多容纳 10 张。抽牌或生成卡牌超过上限时，多出的牌会立即进入弃牌堆或抽牌堆。"),
    "sts1.mechanic.health": ("生命", "生命值降到 0 时角色死亡；生命可在休息处、幕间或其他治疗效果中恢复，最大生命值也可能被卡牌、遗物和事件改变。"),
    "sts1.mechanic.keys": ("钥匙", "用铁甲战士、静默和故障机器人通关后，可在同一局收集三把钥匙：休息处的红宝石钥匙、燃烧精英战的翡翠钥匙和宝箱中的蓝宝石钥匙，以进入第四幕。"),
    "sts1.mechanic.player_turn": ("玩家回合", "回合开始时能量恢复到基础值（默认 3），抽牌（默认 5 张）并结算回合开始效果；玩家可打牌或使用药水，结束回合后结算结束效果并把手牌弃掉，再轮到敌方。"),
    "sts1.mechanic.potions": ("药水", "药水是一次性消耗品，可在战斗中使用来获得增益或妨碍敌人，并会保留到后续战斗；药水栏位限制携带数量。"),
    "sts1.mechanic.relics": ("遗物", "遗物是提供持续或触发效果的被动物品，按普通、罕见、稀有和 Boss 等稀有度分组，部分遗物限定角色或获取场景。"),
    "sts1.mechanic.transforming": ("变化", "被变化的牌会变成一张随机稀有度的随机牌。"),
    "sts1.mechanic.turns": ("回合", "战斗按回合进行：玩家回合后是敌方回合，循环直到玩家或敌方死亡。"),
    "sts1.mechanic.upgrading": ("升级", "升级会增强卡牌的效果；普通卡牌通常只能升级一次，特殊卡牌可能有自己的升级规则。"),
}


# Synthetic status records need an explicit variant description.  The shared
# Wiki pages describe the positive Dexterity/Strength infobox, while the game
# and the Debuffs table describe the negative/temporary variants separately.
STATUS_FIXES: dict[str, dict[str, Any]] = {
    "sts1.status.dexterity_negative": {
        "name_zh": "敏捷（负面）",
        "description_en": "Decreases Block gained from cards by X.",
        "description_zh": "使从卡牌获得的格挡减少 X 点。",
        "polarity": "negative",
        "affects": "Block gained from cards",
        "stacking": "Intensity",
    },
    "sts1.status.dexterity_down": {
        "name_zh": "敏捷下降",
        "description_en": "At the end of this turn, lose X Dexterity.",
        "description_zh": "在本回合结束时失去 X 点敏捷。",
        "polarity": "negative",
        "affects": "Dexterity",
        "stacking": "Intensity",
    },
    "sts1.status.focus_negative": {
        "name_zh": "集中（负面）",
        "description_en": "Reduces the potency of Orbs by X. Plasma is unaffected.",
        "description_zh": "使充能球的效果降低 X 点（等离子充能球不受影响）。",
        "polarity": "negative",
        "affects": "Orbs",
        "stacking": "Intensity",
    },
    "sts1.status.strength_negative": {
        "name_zh": "力量（负面）",
        "description_en": "Decreases attack damage by X.",
        "description_zh": "使攻击伤害降低 X 点。",
        "polarity": "negative",
        "affects": "Attack damage",
        "stacking": "Intensity",
    },
    "sts1.status.strength_down": {
        "name_zh": "力量下降",
        "description_en": "At the end of this turn, lose X Strength.",
        "description_zh": "在本回合结束时失去 X 点力量。",
        "polarity": "negative",
        "affects": "Strength",
        "stacking": "Intensity",
    },
}


POSITIVE_POLARITY = {
    "sts1.status.feel_no_pain",
    "sts1.status.regenerate",
    "sts1.status.regeneration",
    "sts1.status.rushdown",
    "sts1.status.strength_up",
}
NEGATIVE_POLARITY = {
    "sts1.status.blasphemer",
    "sts1.status.choked",
    "sts1.status.confusion",
    "sts1.status.dexterity_down",
    "sts1.status.dexterity_negative",
    "sts1.status.draw_reduction",
    "sts1.status.entangled",
    "sts1.status.focus_negative",
    "sts1.status.frail",
    "sts1.status.no_block",
    "sts1.status.no_draw",
    "sts1.status.painful_stabs",
    "sts1.status.poison",
    "sts1.status.shackled",
    "sts1.status.slow",
    "sts1.status.strength_down",
    "sts1.status.strength_negative",
    "sts1.status.vulnerable",
    "sts1.status.weak",
}


def _source_page(conn: sqlite3.Connection, entity_id: str, field_path: str) -> str | None:
    row = conn.execute(
        """SELECT source_page_id FROM claims
           WHERE subject_entity_id=? AND field_path=?
           ORDER BY created_at DESC, id DESC LIMIT 1""",
        (entity_id, field_path),
    ).fetchone()
    return row[0] if row else None


def _game_source_page(conn: sqlite3.Connection, entity_id: str) -> str | None:
    return _source_page(conn, entity_id, "game.status.descriptions") or _source_page(conn, entity_id, "game.keyword.description")


def _ensure_zh_name(
    conn: sqlite3.Connection,
    entity_id: str,
    name: str,
    source_page_id: str | None,
    *,
    status: str = "single_source",
    notes: str,
) -> None:
    add_name(
        conn,
        entity_id,
        "zh-CN",
        name,
        source_page_id=source_page_id,
        name_kind="preferred",
        status=status,
        preferred=True,
        notes=notes,
    )


def _update_definition(
    conn: sqlite3.Connection,
    entity_id: str,
    table: str,
    name_zh: str,
    definition_zh: str,
    source_page_id: str | None,
    *,
    origin: str,
) -> bool:
    row = conn.execute(f"SELECT definition_json FROM {table} WHERE entity_id=?", (entity_id,)).fetchone()
    if not row:
        return False
    try:
        payload = json.loads(row[0] or "{}")
    except (TypeError, json.JSONDecodeError):
        payload = {}
    if not isinstance(payload, dict):
        payload = {}
    changed = payload.get("definition_zh") != definition_zh or payload.get("definition_zh_origin") != origin
    payload["definition_zh"] = definition_zh
    payload["definition_zh_origin"] = origin
    conn.execute(f"UPDATE {table} SET definition_json=? WHERE entity_id=?", (json.dumps(payload, ensure_ascii=False, sort_keys=True), entity_id))
    if source_page_id:
        add_claim(
            conn,
            entity_id,
            f"{table[:-1]}.definition.zh",
            definition_zh,
            source_page_id,
            language="zh-CN",
            extraction_method="manual",
            status="single_source",
            notes="editorial_zh: translated from the captured English Wiki definition; no Chinese source page was available for this field.",
        )
    _ensure_zh_name(
        conn,
        entity_id,
        name_zh,
        source_page_id,
        notes="editorial_zh: Chinese display name translated from the captured English Wiki title.",
    )
    return changed


def _latest_text_claim(conn: sqlite3.Connection, entity_id: str, field_path: str, language: str) -> tuple[str, str] | None:
    row = conn.execute(
        """SELECT value_json, source_page_id FROM claims
           WHERE subject_entity_id=? AND field_path=? AND language=?
           ORDER BY created_at DESC, id DESC LIMIT 1""",
        (entity_id, field_path, language),
    ).fetchone()
    if not row:
        return None
    try:
        value = json.loads(row[0])
    except (TypeError, json.JSONDecodeError):
        value = row[0]
    if isinstance(value, list):
        text = "".join(str(item) for item in value if item is not None)
    else:
        text = str(value or "")
    return text.strip(), row[1]


def _status_claim(
    conn: sqlite3.Connection,
    entity_id: str,
    text: str,
    language: str,
    source_page_id: str | None,
) -> None:
    if not source_page_id:
        return
    # Keep the original positive-page claim for auditability, but mark it as
    # superseded so a generated page can select the corrected latest claim.
    conn.execute(
        """UPDATE claims SET notes=CASE
             WHEN notes IS NULL OR notes='' THEN 'superseded: explicit status variant correction'
             ELSE notes || '; superseded: explicit status variant correction' END
           WHERE subject_entity_id=? AND field_path='status.description'
             AND language=? AND COALESCE(notes,'') NOT LIKE '%superseded: explicit status variant correction%'""",
        (entity_id, language),
    )
    chosen_id = add_claim(
        conn,
        entity_id,
        "status.description",
        text,
        source_page_id,
        language=language,
        extraction_method="manual",
        status="single_source",
        notes="editorial_zh: explicit status variant correction from the captured game/Wiki evidence; the shared positive infobox is retained as superseded evidence.",
    )
    # add_claim is INSERT OR IGNORE: on replay the chosen row may already
    # exist and must be reactivated after older descriptions are superseded.
    conn.execute("UPDATE claims SET notes=? WHERE id=?", (
        "editorial_zh: explicit status variant correction from the captured game/Wiki evidence; the shared positive infobox is retained as superseded evidence.", chosen_id))


def supplement(conn: sqlite3.Connection) -> dict[str, int]:
    keyword_changed = 0
    mechanic_changed = 0
    status_changed = 0

    for entity_id, (name_zh, definition_zh) in KEYWORD_ZH.items():
        source_page_id = _source_page(conn, entity_id, "keyword.definition") or _source_page(conn, entity_id, "source.wikitext")
        if _update_definition(conn, entity_id, "keywords", name_zh, definition_zh, source_page_id, origin="editorial_translation"):
            keyword_changed += 1

    # Mark the two shared mechanic entries as game-backed when their keyword
    # definition is already present; add editorial translations for the rest.
    for entity_id, (name_zh, definition_zh) in MECHANIC_ZH.items():
        current = conn.execute("SELECT definition_json FROM mechanics WHERE entity_id=?", (entity_id,)).fetchone()
        if not current:
            continue
        try:
            payload = json.loads(current[0] or "{}")
        except (TypeError, json.JSONDecodeError):
            payload = {}
        has_source_zh = isinstance(payload, dict) and bool(payload.get("definition_zh"))
        origin = "game_localization" if entity_id in {"sts1.mechanic.block", "sts1.mechanic.exhaust"} and has_source_zh else "editorial_translation"
        source_page_id = _source_page(conn, entity_id, "mechanic.definition") or _source_page(conn, entity_id, "source.wikitext")
        if not source_page_id and origin == "game_localization":
            source_page_id = _source_page(conn, "sts1.keyword." + entity_id.rsplit(".", 1)[-1], "game.keyword.description")
        if origin == "game_localization" and has_source_zh:
            _ensure_zh_name(conn, entity_id, name_zh, source_page_id, status="verified_game", notes="Game-localized Chinese term reused for the shared keyword/mechanic entry.")
            continue
        if _update_definition(conn, entity_id, "mechanics", name_zh, definition_zh, source_page_id, origin=origin):
            mechanic_changed += 1

    for entity_id, fix in STATUS_FIXES.items():
        row = conn.execute("SELECT 1 FROM statuses WHERE entity_id=?", (entity_id,)).fetchone()
        if not row:
            continue
        game_page = _game_source_page(conn, entity_id)
        wiki_page = _source_page(conn, entity_id, "source.wikitext") or _source_page(conn, entity_id, "status.description")
        source_page_id = game_page or wiki_page
        name_status = "verified_game" if game_page and entity_id not in {"sts1.status.dexterity_negative", "sts1.status.strength_negative", "sts1.status.focus_negative"} else "single_source"
        _ensure_zh_name(conn, entity_id, fix["name_zh"], source_page_id, status=name_status, notes="Explicit negative/temporary status variant name; kept separate from the positive status name.")
        _status_claim(conn, entity_id, fix["description_en"], "en", source_page_id)
        _status_claim(conn, entity_id, fix["description_zh"], "zh-CN", source_page_id)
        conn.execute(
            """UPDATE statuses SET polarity=?, affects=?, stacking=? WHERE entity_id=?""",
            (fix["polarity"], fix["affects"], fix["stacking"], entity_id),
        )
        status_changed += 1

    # A few common statuses have no dedicated infobox in the captured Wiki,
    # so their polarity must be kept explicit rather than left as neutral.
    for entity_id in POSITIVE_POLARITY:
        conn.execute("UPDATE statuses SET polarity='positive' WHERE entity_id=?", (entity_id,))
    for entity_id in NEGATIVE_POLARITY:
        conn.execute("UPDATE statuses SET polarity='negative' WHERE entity_id=?", (entity_id,))

    return {
        "parser_version": PARSER_VERSION,
        "keyword_definitions_changed": keyword_changed,
        "mechanic_definitions_changed": mechanic_changed,
        "status_variants_corrected": status_changed,
        "finished_at": utc_now(),
    }


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    with conn:
        result = supplement(conn)
    conn.close()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
