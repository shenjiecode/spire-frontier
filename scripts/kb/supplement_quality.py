"""Close source/provenance gaps that do not require guessing game facts.

The main P3 parser intentionally leaves source-only rows as candidates.  A
second review against the current wiki.gg map pages showed that five of the
Chinese map-mechanic articles have unambiguous English counterparts.  This
module records those pages as a reviewed mapping, keeps the original Chinese
article claims, and adds a short English/Chinese structured summary.

It also adds Chinese display labels for generated encounter-pool rows,
field-level evidence for the two game-backed shared mechanics, and repairs the
English source attribution of the four character pages.  No strategy document
is read or linked here.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Any

from bootstrap_sample import (
    DB_PATH,
    ROOT,
    add_claim,
    add_name,
    add_relation,
    json_text,
    normalise,
    source_page_id,
    utc_now,
)
from discover_inventory import insert_inventory, inventory_id
from fetch_p3 import merge_confirmed_candidate


PARSER_VERSION = "kb-quality-supplement/0.3"
MANUAL_SNAPSHOT_DIR = ROOT / "data" / "raw" / "wiki_gg" / "2026-09-18" / "manual_map_mechanics"


# These excerpts were read from the public wiki.gg pages in a browser on
# 2026-09-18.  They are deliberately concise, while the source URL and the
# captured text file remain available for audit.  The Chinese article claims
# are never replaced by these summaries.
ENGLISH_PAGES: dict[str, dict[str, str]] = {
    "rest_site": {
        "url": "https://slaythespire.wiki.gg/wiki/Rest_Site",
        "title": "Rest Site | Slay the Spire 1",
        "text": """Slay the Spire 1 — Rest Site

Rest Sites are a standard Map Location. The player must choose one of the available options to prepare for higher floors before proceeding. If one of the standard options is unavailable, it is greyed out; if no other options are allowed, the Leave button appears.

Standard Options
Rest: Heal for 30% of max health.
Smith: Upgrade a card.
Recall: Obtain the Ruby Key. It appears only after Act 4 has been revealed on the current save file and before a previous Recall at a rest site.

Relic modifiers and special options
Dream Catcher adds a card reward after Resting. Regal Pillow adds 15 HP to Rest. Girya allows Lift for 1 Strength up to three uses; Peace Pipe allows Toke to remove a card; Shovel allows Dig to acquire a random Relic. Only two of these three option relics can be picked up in one run. Eternal Feather restores 3 health for every five cards on entering the rest site. Ancient Tea Set gives two additional Energy on the first turn of the next combat.
""",
    },
    "merchant": {
        "url": "https://slaythespire.wiki.gg/wiki/Merchant",
        "title": "Merchant | Slay the Spire 1",
        "text": """Slay the Spire 1 — Merchant

The Shop is a Map Location where Cards, Relics, Potions and a Remove can be obtained in exchange for Gold. Shops can also sometimes be found in Unknown rooms. Ascension 16 makes prices 10% more expensive.

Items
5 Colored Cards: always 2 Attacks, 2 Skills and 1 Power; one random card has a 50% discount.
2 Colorless Cards: always one Uncommon and one Rare Colorless card.
3 Potions.
3 Relics: the rightmost slot is always a Shop Relic, the only way to access Shop relics.
Card Removal Service: can be used once per Shop; starts at 75 Gold and increases by 25 each time it is bought at a shop.

Relic interactions include Smiling Mask, Membership Card, Maw Bank, The Courier and Meal Ticket. The current page records separate Ascension-16 prices and restock rules; those values are retained as English-source claims rather than overwritten by the Chinese article's rounded ranges.
""",
    },
    "map_locations": {
        "url": "https://slaythespire.wiki.gg/wiki/Map_Locations",
        "title": "Map Locations | Slay the Spire 1",
        "text": """Slay the Spire 1 — Map Locations (reviewed excerpts)

Maps contain seven location types: Monster Encounter, Elite Encounter, Rest Sites, Unknown, Treasure Room, Merchant and Boss Encounter.

Rest Sites prompt one choice; the default options are Rest (heal for 30% of max HP, rounded down) and Smith (upgrade a card), with more options from relics or unlocking Act 4.

Unknown encounters can be an Event, Monster, Shop or Treasure Room. Whenever a specific encounter is not seen, its spawn chance increases; when it is seen, it resets to the original amount.

Treasure Rooms are guaranteed at the halfway points of Acts 1–3. A single chest appears where enemies would be in combat; clicking it opens a reward window. Chests normally contain a single relic and may have Gold.

The Merchant sells 5 character Cards, 2 Colorless Cards, 3 Relics, 3 Potions and a card-removal service usable once per shop.
""",
    },
    "unknown_location": {
        "url": "https://slaythespire.wiki.gg/wiki/Unknown_Location",
        "title": "Unknown Location | Slay the Spire 1",
        "text": """Slay the Spire 1 — Unknown Location

Unknown Locations are a standard Map Location and appear multiple times on each map.

Unknown encounters have a chance to be an Event, Monster, Merchant or Treasure Room. Any time a specific encounter is not seen, its spawn chance increases; when it is seen, it resets to the original amount. In Custom Mode, Deadly Events also enables Elites in Unknown rooms and increases the chance of a Treasure Room.

Juzu Bracelet prevents Monster encounters from appearing in ? rooms.
""",
    },
}


MAP_MECHANICS: dict[str, dict[str, Any]] = {
    "rest_site": {
        "candidate_id": "sts1.candidate.zh.mechanic.15463366",
        "entity_id": "sts1.mechanic.rest_site",
        "en_name": "Rest Site",
        "zh_name": "休息处",
        "en_summary": "A map location where one Rest Site option is chosen. Rest heals 30% of max HP (rounded down), Smith upgrades a card, and Recall obtains the Ruby Key after Act 4 is revealed; relics can add Lift, Toke and Dig.",
        "zh_summary": "地图上的休息处只能选择一个选项；默认可休息（回复最大生命值的 30%，向下取整）或锻造（升级一张牌），终幕解锁后可回忆取得红宝石钥匙，特定遗物可增加举重、抽烟和挖掘。",
        "page_key": "rest_site",
    },
    "merchant": {
        "candidate_id": "sts1.candidate.zh.mechanic.15440709",
        "entity_id": "sts1.mechanic.merchant",
        "en_name": "Merchant",
        "zh_name": "商人",
        "en_summary": "The Shop is a map location where the Merchant sells 5 colored cards, 2 Colorless cards, 3 Potions, 3 Relics and a once-per-shop card-removal service for Gold. Ascension 16 raises prices by 10%.",
        "zh_summary": "商人商店出售 5 张职业卡（2 张攻击、2 张技能、1 张能力）、2 张无色卡、3 瓶药水、3 件遗物和每店一次的卡牌移除服务；进阶 16 起价格提高 10%。",
        "page_key": "merchant",
    },
    "treasure_room": {
        "candidate_id": "sts1.candidate.zh.mechanic.15463362",
        "entity_id": "sts1.mechanic.treasure_room",
        "en_name": "Treasure Room",
        "zh_name": "宝箱房",
        "en_summary": "A guaranteed halfway-point room in Acts 1–3 containing one chest. The chest normally contains a single Relic and may contain Gold; after Act 4 is revealed, the Sapphire Key can replace the Relic.",
        "zh_summary": "第一至第三幕的中点必定有宝箱房；房间包含一个宝箱，通常给一件遗物并可能给金币，终幕解锁后可用宝箱遗物位置换取蓝宝石钥匙。",
        "page_key": "map_locations",
        "related": "sts1.mechanic.chests",
    },
    "unknown_location": {
        "candidate_id": "sts1.candidate.zh.mechanic.15624135",
        "entity_id": "sts1.mechanic.unknown_location",
        "en_name": "Unknown Location",
        "zh_name": "问号房",
        "en_summary": "A map location that can become an Event, Monster, Merchant or Treasure Room. Unseen encounter types gain probability and reset when seen; Deadly Events can add Elites in Custom Mode.",
        "zh_summary": "问号房可能遭遇事件、小怪、商店或宝箱房；某类型未出现时概率提高，出现后恢复初始值。自定义模式的致命事件还可能加入精英。",
        "page_key": "unknown_location",
    },
    "monsters": {
        "candidate_id": "sts1.candidate.zh.mechanic.15539744",
        "entity_id": "sts1.mechanic.monsters",
        "en_name": "Monsters",
        "zh_name": "怪物介绍",
        "en_summary": "Normal monster encounters are drawn from Easy and Hard pools; defeated normal enemies give a card reward, 10–20 Gold and sometimes a Potion. The full encounter tables and restrictions remain in the Monsters source page.",
        "zh_summary": "普通怪物遭遇按每幕的 Easy/Hard 池抽取；击败普通敌人获得三选一卡牌、10–20 金币，有时还会获得药水。遭遇表和重复限制保留在英文 Monsters 页面。",
        "page_key": "monsters",
    },
}


ENCOUNTER_ZH: dict[str, str] = {
    "sts1.encounter.act1.easy.2_louse": "2 只虱虫",
    "sts1.encounter.act1.easy.cultist": "邪教徒",
    "sts1.encounter.act1.easy.jaw_worm": "大颚虫",
    "sts1.encounter.act1.easy.small_slimes": "小型史莱姆",
    "sts1.encounter.act1.hard.2_fungi_beasts": "2 只真菌兽",
    "sts1.encounter.act1.hard.3_louse": "3 只虱虫",
    "sts1.encounter.act1.hard.blue_slaver": "蓝色奴隶贩子",
    "sts1.encounter.act1.hard.exordium_thugs": "序幕暴徒",
    "sts1.encounter.act1.hard.exordium_wildlife": "序幕野兽",
    "sts1.encounter.act1.hard.gang_of_gremlins": "地精小队",
    "sts1.encounter.act1.hard.large_slime": "大型史莱姆",
    "sts1.encounter.act1.hard.looter": "抢劫的",
    "sts1.encounter.act1.hard.red_slaver": "红色奴隶贩子",
    "sts1.encounter.act1.hard.swarm_of_slimes": "史莱姆群",
    "sts1.encounter.act2.easy.2_thieves": "2 名盗贼",
    "sts1.encounter.act2.easy.3_byrds": "3 只异鸟",
    "sts1.encounter.act2.easy.chosen": "被拣选者",
    "sts1.encounter.act2.easy.shelled_parasite": "带壳寄生怪",
    "sts1.encounter.act2.easy.spheric_guardian": "圆球守护者",
    "sts1.encounter.act2.hard.3_cultists": "3 名邪教徒",
    "sts1.encounter.act2.hard.centurion_and_mystic": "百夫长与神秘术士",
    "sts1.encounter.act2.hard.chosen_and_byrds": "被拣选者与异鸟",
    "sts1.encounter.act2.hard.cultist_and_chosen": "邪教徒与被拣选者",
    "sts1.encounter.act2.hard.sentry_and_spheric_guardian": "哨卫与圆球守护者",
    "sts1.encounter.act2.hard.shelled_parasite_and_fungi": "带壳寄生怪与真菌兽",
    "sts1.encounter.act2.hard.snake_plant": "蛇花",
    "sts1.encounter.act2.hard.snecko": "异蛇",
    "sts1.encounter.act3.easy.3_darklings": "3 只小黑",
    "sts1.encounter.act3.easy.3_shapes": "3 个三机械",
    "sts1.encounter.act3.easy.orb_walker": "圆球行者",
    "sts1.encounter.act3.hard.3_darklings": "3 只小黑",
    "sts1.encounter.act3.hard.4_shapes": "4 个三机械",
    "sts1.encounter.act3.hard.jaw_worm_horde": "大颚虫群",
    "sts1.encounter.act3.hard.spheric_guardian_2_shapes": "圆球守护者 + 2 个三机械",
    "sts1.encounter.act3.hard.spire_growth": "塔内增生组织",
    "sts1.encounter.act3.hard.the_maw": "巨口",
    "sts1.encounter.act3.hard.transient": "倏忽魔",
    "sts1.encounter.act3.hard.writhing_mass": "扭曲团块",
    "sts1.encounter.exordium.slime_boss": "第一幕：史莱姆老大",
}


CHARACTER_PAGE_URLS = {
    "sts1.character.ironclad": "https://slaythespire.wiki.gg/wiki/Ironclad",
    "sts1.character.silent": "https://slaythespire.wiki.gg/wiki/Silent",
    "sts1.character.defect": "https://slaythespire.wiki.gg/wiki/Defect",
    "sts1.character.watcher": "https://slaythespire.wiki.gg/wiki/Watcher",
}


# The Chinese site exposes these four characters as directory rows, while
# wiki.gg uses dedicated character pages rather than a single character list
# page.  Keep the article IDs explicit so the mapping is deterministic and
# replayable instead of relying on translated-name similarity.
CHARACTER_DIRECTORY_ROWS: dict[str, dict[str, str]] = {
    "sts1.character.ironclad": {"zh": "铁甲战士", "en": "Ironclad", "article_id": "15543423"},
    "sts1.character.silent": {"zh": "静默猎手", "en": "Silent", "article_id": "15589144"},
    "sts1.character.defect": {"zh": "故障机器人", "en": "Defect", "article_id": "15589967"},
    "sts1.character.watcher": {"zh": "观者", "en": "Watcher", "article_id": "15589965"},
}


GROUP_PARENT_ZH_NAMES: dict[str, str] = {
    # This is an index label for the grouped wiki page.  The two children
    # remain the canonical game monsters and carry their own Chinese names.
    "sts1.monster.centurion_and_mystic": "百夫长与神秘术士",
}


GROUP_MEMBER_DIRECTORY_ROWS: tuple[dict[str, str], ...] = (
    {
        "entity_id": "sts1.monster.centurion",
        "zh_article_id": "15436697",
        "zh_name": "百夫长",
        "anchor": "Centurion",
        "game_key": "Centurion",
    },
    {
        "entity_id": "sts1.monster.mystic",
        "zh_article_id": "15436699",
        "zh_name": "神秘术士",
        "anchor": "Mystic",
        "game_key": "Healer",
    },
)


# These rows are not ordinary wiki-to-wiki merges.  The Chinese pages expose
# an installed-game localization key, while the corresponding English wiki
# page is either a grouped effect (Machine Learning -> the generic Draw
# power) or absent altogether (Spire Heart).  Keep the game-only entities as
# candidates, but record the reviewed Chinese-to-JAR crosswalk so they do not
# remain indistinguishable from an unreviewed fuzzy match.
GAME_LOCAL_CROSSWALKS: tuple[dict[str, str], ...] = (
    {
        "zh_article_id": "15408927",
        "kind": "event",
        "game_key": "Spire Heart",
        "game_entity_id": "sts1.game.candidate.event.spire_heart",
        "candidate_id": "sts1.candidate.zh.event.15408927",
        "zh_name": "高塔之心",
        "reason": "小黑盒正文的第四幕入口、钥匙和选项与本机 events.json 的 Spire Heart 键一致；wiki.gg 没有对应独立英文事件页，继续保留 game-only candidate。",
    },
    {
        "zh_article_id": "15448778",
        "kind": "status",
        "game_key": "Machine Learning",
        "game_entity_id": "sts1.game.candidate.status.machine_learning",
        "candidate_id": "sts1.candidate.zh.status.15448778",
        "zh_name": "机器学习（能力）",
        "reason": "小黑盒正文明确写出 Buffs id: Machine Learning，效果与本机 powers.json 的同键完全一致；英文 wiki 将它按通用 Draw 效果列在 Buffs 中，故不把游戏键误并为独立 wiki 状态。",
    },
)


STATUS_WIKI_CROSSWALK: dict[str, dict[str, str]] = {
    "15460336": {
        "candidate_id": "sts1.candidate.zh.status.15460336",
        "target_id": "sts1.status.block_return",
        "english_name": "Block Return",
        "reason": "小黑盒文章明确写出 Buffs id: Talk to the Hand，英文效果与 wiki.gg Buffs#Block_Return 及本机 BlockReturnPower 描述逐字对应；中文文章是该状态的专题页而非另一种效果。",
    },
}


def _ensure_manual_page(conn: sqlite3.Connection, key: str) -> str:
    if key == "monsters":
        url = "https://slaythespire.wiki.gg/wiki/Monsters"
        row = conn.execute("SELECT id FROM source_pages WHERE url=?", (url,)).fetchone()
        if row:
            return row[0]
        text = "Monsters are the normal Enemies of Slay the Spire. When these encounters are beaten, they drop a Card Reward, 10-20 Gold, and sometimes a Potion."
        title = "Monsters | Slay the Spire 1"
    else:
        page = ENGLISH_PAGES[key]
        url, title, text = page["url"], page["title"], page["text"]
    pid = source_page_id("wiki_gg", url)
    MANUAL_SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    path = MANUAL_SNAPSHOT_DIR / f"{key}.txt"
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8", newline="\n")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    conn.execute(
        """INSERT INTO source_pages
           (id, source_id, url, title, source_page_key, fetched_at,
            http_status, content_type, snapshot_path, sha256, parser_version,
            is_index_page, notes)
           VALUES (?, 'wiki_gg', ?, ?, ?, ?, 200, 'text/plain; charset=utf-8', ?, ?, ?, 0, ?)
           ON CONFLICT(id) DO UPDATE SET title=excluded.title,
             source_page_key=excluded.source_page_key, fetched_at=excluded.fetched_at,
             http_status=excluded.http_status, content_type=excluded.content_type,
             snapshot_path=excluded.snapshot_path, sha256=excluded.sha256,
             parser_version=excluded.parser_version, notes=excluded.notes""",
        (
            pid,
            url,
            title,
            f"manual_map_mechanics_{key}",
            utc_now(),
            str(path.relative_to(ROOT)).replace("\\", "/"),
            digest,
            PARSER_VERSION,
            "Read-only browser capture of the public wiki.gg page on 2026-09-18; concise excerpt retained for field-level audit.",
        ),
    )
    return pid


def _candidate_page(conn: sqlite3.Connection, candidate_id: str) -> str | None:
    row = conn.execute(
        """SELECT source_page_id FROM names WHERE entity_id=? AND language='zh-CN'
           ORDER BY is_preferred DESC, name_kind='preferred' DESC LIMIT 1""",
        (candidate_id,),
    ).fetchone()
    if row and row[0]:
        return row[0]
    row = conn.execute(
        "SELECT source_page_id FROM claims WHERE subject_entity_id=? ORDER BY created_at DESC LIMIT 1",
        (candidate_id,),
    ).fetchone()
    return row[0] if row else None


def _ensure_mapping_inventory(conn: sqlite3.Connection, item: dict[str, Any], english_page_id: str) -> tuple[str | None, str | None]:
    candidate_id = item["candidate_id"]
    zh_row = conn.execute(
        """SELECT id FROM inventory_items WHERE source_id='xiaoheihe'
           AND language='zh-CN' AND entity_kind='mechanic'
           AND article_id=? ORDER BY id LIMIT 1""",
        (candidate_id.rsplit(".", 1)[-1],),
    ).fetchone()
    if not zh_row:
        return None, None
    url = ENGLISH_PAGES[item["page_key"]]["url"] if item["page_key"] != "monsters" else "https://slaythespire.wiki.gg/wiki/Monsters"
    en_name = item["en_name"]
    en_item = insert_inventory(
        conn,
        source_id="wiki_gg",
        source_page_id=english_page_id,
        source_item_key=f"manual:mechanic:{item['page_key']}",
        entity_kind="mechanic",
        language="en",
        name=en_name,
        url=url,
        category="Map Locations" if item["page_key"] != "monsters" else "Monsters",
        status="parsed",
    )
    mid = "mapping." + hashlib.sha256(f"{zh_row[0]}|{en_item}".encode("utf-8")).hexdigest()[:24]
    conn.execute(
        """INSERT INTO inventory_mappings
           (id, zh_inventory_id, en_inventory_id, status, rationale, evidence_json, decided_at)
           VALUES (?, ?, ?, 'confirmed', ?, ?, ?)
           ON CONFLICT(zh_inventory_id, en_inventory_id) DO UPDATE SET
             status='confirmed', rationale=excluded.rationale,
             evidence_json=excluded.evidence_json, decided_at=excluded.decided_at""",
        (
            mid,
            zh_row[0],
            en_item,
            "英文 wiki.gg 地图/机制页与小黑盒中文条目的标题、房间功能和规则结构一致；保留两边原文，数值差异不自动覆盖。",
            json_text({"candidate_entity_id": candidate_id, "english_url": url, "page_id": english_page_id, "match": ["room_or_mechanic_identity", "source_text_review"]}),
            utc_now(),
        ),
    )
    return zh_row[0], en_item


def _merge_map_mechanic(conn: sqlite3.Connection, key: str, item: dict[str, Any]) -> bool:
    en_page_id = _ensure_manual_page(conn, item["page_key"])
    candidate_id = item["candidate_id"]
    zh_page_id = _candidate_page(conn, candidate_id)
    conn.execute(
        """INSERT OR IGNORE INTO entities
           (id, kind, game, lifecycle, mapping_status, notes)
           VALUES (?, 'mechanic', 'sts1', 'active', 'confirmed', ?)""",
        (item["entity_id"], "Cross-source mapping reviewed against wiki.gg and Xiaoheihe."),
    )
    conn.execute("UPDATE entities SET lifecycle='active', mapping_status='confirmed', notes=? WHERE id=?", ("Cross-source mapping reviewed against wiki.gg and Xiaoheihe; raw source claims retained.", item["entity_id"]))
    conn.execute("INSERT OR IGNORE INTO mechanics(entity_id, definition_json) VALUES (?, ?)", (item["entity_id"], "{}"))
    if conn.execute("SELECT 1 FROM entities WHERE id=?", (candidate_id,)).fetchone():
        merge_confirmed_candidate(conn, candidate_id, item["entity_id"])
    add_name(conn, item["entity_id"], "en", item["en_name"], source_page_id=en_page_id, preferred=True, status="single_source")
    add_name(conn, item["entity_id"], "zh-CN", item["zh_name"], source_page_id=zh_page_id, preferred=True, status="agreed", notes="Cross-source identity confirmed against the English wiki.gg page; original Xiaoheihe article claims are retained.")
    row = conn.execute("SELECT definition_json FROM mechanics WHERE entity_id=?", (item["entity_id"],)).fetchone()
    try:
        payload = json.loads(row[0] or "{}") if row and row[0] else {}
    except (TypeError, json.JSONDecodeError):
        payload = {}
    if not isinstance(payload, dict):
        payload = {}
    payload.update(
        {
            "definition_en": item["en_summary"],
            "definition_zh": item["zh_summary"],
            "definition_zh_origin": "xiaoheihe_source_summary",
            "cross_source_review": {"english_source_page_id": en_page_id, "chinese_source_page_id": zh_page_id},
        }
    )
    conn.execute("UPDATE mechanics SET definition_json=? WHERE entity_id=?", (json.dumps(payload, ensure_ascii=False, sort_keys=True), item["entity_id"]))
    add_claim(conn, item["entity_id"], "mechanic.definition", {"definition_en": item["en_summary"]}, en_page_id, language="en", extraction_method="manual", status="single_source", notes="Concise structured summary of the captured wiki.gg page; full excerpt is retained in the source snapshot.")
    if zh_page_id:
        add_claim(conn, item["entity_id"], "mechanic.definition.zh", item["zh_summary"], zh_page_id, language="zh-CN", extraction_method="manual", status="agreed", notes="Concise summary of the captured Xiaoheihe article; raw source.article_text is retained.")
    add_claim(conn, item["entity_id"], "mapping.cross_source", {"english_page": ENGLISH_PAGES[item["page_key"]]["url"] if item["page_key"] != "monsters" else "https://slaythespire.wiki.gg/wiki/Monsters", "chinese_article": candidate_id.rsplit(".", 1)[-1]}, en_page_id, extraction_method="manual", status="agreed", notes="Reviewed English/Chinese identity mapping; source-specific numerical differences remain as separate evidence.")
    if item.get("related"):
        add_relation(conn, item["entity_id"], "related_mechanic", item["related"], source_page_id=en_page_id, status="confirmed", notes="English Map Locations links the room to the Chests mechanic.")
    return True


def _supplement_encounter_names(conn: sqlite3.Connection) -> int:
    changed = 0
    for entity_id, zh_name in ENCOUNTER_ZH.items():
        row = conn.execute("SELECT kind FROM entities WHERE id=?", (entity_id,)).fetchone()
        if not row or row[0] != "encounter":
            continue
        page = conn.execute("SELECT source_page_id FROM claims WHERE subject_entity_id=? AND field_path='encounter.weight' ORDER BY created_at DESC LIMIT 1", (entity_id,)).fetchone()
        source_page_id = page[0] if page else None
        add_name(conn, entity_id, "zh-CN", zh_name, source_page_id=source_page_id, preferred=True, status="single_source", notes="editorial_zh: translated encounter-pool label from the wiki.gg Monsters table; no separate Chinese encounter table was available.")
        add_claim(conn, entity_id, "encounter.name.zh", zh_name, source_page_id or _ensure_manual_page(conn, "monsters"), language="zh-CN", extraction_method="manual", status="single_source", notes="editorial_zh: display translation of the English encounter label; membership and weights remain source-backed.")
        en = conn.execute("SELECT name,source_page_id FROM names WHERE entity_id=? AND language='en' ORDER BY is_preferred DESC LIMIT 1", (entity_id,)).fetchone()
        if en:
            add_claim(conn, entity_id, "encounter.name.en", en[0], en[1] or source_page_id or _ensure_manual_page(conn, "monsters"), language="en", extraction_method="manual", status="single_source", notes="Display label from the wiki.gg Monsters encounter table.")
        changed += 1
    # The bootstrap boss wrapper predates the encounter-pool importer and had
    # no field-level claims.  Add a deterministic membership projection.
    boss = "sts1.encounter.exordium.slime_boss"
    if conn.execute("SELECT 1 FROM entities WHERE id=?", (boss,)).fetchone() and not conn.execute("SELECT 1 FROM claims WHERE subject_entity_id=? AND field_path='encounter.members'", (boss,)).fetchone():
        rel = conn.execute("SELECT source_page_id FROM relations WHERE source_entity_id=? AND relation_type='contains_monster' LIMIT 1", (boss,)).fetchone()
        pid = rel[0] if rel and rel[0] else _ensure_manual_page(conn, "map_locations")
        add_claim(conn, boss, "encounter.members", {"members": [{"entity_id": "sts1.monster.slime_boss", "quantity": 1}], "resolution_status": "confirmed"}, pid, extraction_method="manual", status="single_source", notes="Deterministic projection of the bootstrap boss wrapper; the linked Slime Boss source page remains the evidence.")
        changed += 1
    return changed


def _repair_character_sources(conn: sqlite3.Connection) -> int:
    changed = 0
    for entity_id, url in CHARACTER_PAGE_URLS.items():
        page = conn.execute("SELECT id FROM source_pages WHERE url=?", (url,)).fetchone()
        if not page:
            continue
        pid = page[0]
        conn.execute("UPDATE names SET source_page_id=? WHERE entity_id=? AND language='en' AND is_preferred=1 AND (source_page_id IS NULL OR source_page_id<>?)", (pid, entity_id, pid))
        row = conn.execute("SELECT name FROM names WHERE entity_id=? AND language='en' AND is_preferred=1 ORDER BY name_kind='preferred' DESC LIMIT 1", (entity_id,)).fetchone()
        if row:
            add_claim(conn, entity_id, "character.source_page.en", {"name": row[0], "url": url}, pid, language="en", extraction_method="manual", status="agreed", notes="Corrected attribution to the character's dedicated wiki.gg page; the Cards List index remains retained as older evidence.")
            changed += 1
    return changed


def _confirm_character_directory_mappings(conn: sqlite3.Connection) -> int:
    """Map the four Chinese character directory rows to dedicated wiki pages."""
    changed = 0
    for entity_id, item in CHARACTER_DIRECTORY_ROWS.items():
        zh_row = conn.execute(
            """SELECT id, source_page_id, url FROM inventory_items
               WHERE source_id='xiaoheihe' AND language='zh-CN'
                 AND entity_kind='character' AND article_id=?
               ORDER BY id LIMIT 1""",
            (item["article_id"],),
        ).fetchone()
        en_page = conn.execute("SELECT id FROM source_pages WHERE url=?", (CHARACTER_PAGE_URLS[entity_id],)).fetchone()
        if not zh_row or not en_page:
            continue
        en_item = insert_inventory(
            conn,
            source_id="wiki_gg",
            source_page_id=en_page[0],
            source_item_key=f"manual:character:{entity_id}",
            entity_kind="character",
            language="en",
            name=item["en"],
            url=CHARACTER_PAGE_URLS[entity_id],
            category="Characters",
            status="parsed",
        )
        mapping_id = "mapping." + hashlib.sha256(f"{zh_row['id']}|{en_item}".encode("utf-8")).hexdigest()[:24]
        evidence = {
            "decided_by": "dedicated_character_pages",
            "entity_id": entity_id,
            "zh_name": item["zh"],
            "en_name": item["en"],
            "zh_url": zh_row["url"],
            "en_url": CHARACTER_PAGE_URLS[entity_id],
            "match": ["same_character_category", "dedicated_wiki_page", "exact_game_identity"],
        }
        conn.execute(
            """INSERT INTO inventory_mappings
               (id, zh_inventory_id, en_inventory_id, status, rationale, evidence_json, decided_at)
               VALUES (?, ?, ?, 'confirmed', ?, ?, ?)
               ON CONFLICT(zh_inventory_id, en_inventory_id) DO UPDATE SET
                 status='confirmed', rationale=excluded.rationale,
                 evidence_json=excluded.evidence_json, decided_at=excluded.decided_at""",
            (
                mapping_id,
                zh_row["id"],
                en_item,
                "小黑盒角色目录行与对应的 wiki.gg 独立角色页一一对应；角色名、游戏本地化和专属页面共同作为身份证据。",
                json.dumps(evidence, ensure_ascii=False, sort_keys=True),
                utc_now(),
            ),
        )
        add_claim(
            conn,
            entity_id,
            "mapping.cross_source.character",
            evidence,
            en_page[0],
            language="en",
            extraction_method="manual",
            status="agreed",
            notes="Confirmed from the Chinese directory row and the dedicated wiki.gg character page; no strategy document involved.",
        )
        changed += 1
    return changed


def _add_group_parent_names(conn: sqlite3.Connection) -> int:
    """Give grouped wiki parent pages an explicit Chinese index label."""
    changed = 0
    for entity_id, zh_name in GROUP_PARENT_ZH_NAMES.items():
        row = conn.execute("SELECT id FROM entities WHERE id=? AND kind='monster'", (entity_id,)).fetchone()
        if not row:
            continue
        source_page = conn.execute(
            """SELECT source_page_id FROM claims
               WHERE subject_entity_id=? AND field_path='source.title_text'
                 AND language='zh-CN' ORDER BY rowid DESC LIMIT 1""",
            ("sts1.candidate.zh.monster.15436697",),
        ).fetchone()
        page_id = source_page[0] if source_page else None
        add_name(
            conn,
            entity_id,
            "zh-CN",
            zh_name,
            source_page_id=page_id,
            preferred=True,
            status="agreed",
            notes="Editorial index label composed from the two separately verified group members; not a third monster identity.",
        )
        add_claim(
            conn,
            entity_id,
            "monster.group_name.zh",
            zh_name,
            page_id or _ensure_manual_page(conn, "monsters"),
            language="zh-CN",
            extraction_method="manual",
            status="agreed",
            notes="Index label for the grouped Centurion/Mystic wiki page; member stats remain on separate entities.",
        )
        changed += 1
    return changed


def _confirm_group_member_directory_mappings(conn: sqlite3.Connection) -> int:
    """Map child Chinese pages to anchors on the shared English group page."""
    changed = 0
    en_row = conn.execute(
        """SELECT id, source_page_id, url FROM inventory_items
           WHERE source_id='wiki_gg' AND language='en' AND entity_kind='monster'
             AND name='Centurion and Mystic' ORDER BY id LIMIT 1"""
    ).fetchone()
    if not en_row:
        return 0
    for item in GROUP_MEMBER_DIRECTORY_ROWS:
        zh_row = conn.execute(
            """SELECT id, source_page_id, url FROM inventory_items
               WHERE source_id='xiaoheihe' AND language='zh-CN'
                 AND entity_kind='monster' AND article_id=?
               ORDER BY id LIMIT 1""",
            (item["zh_article_id"],),
        ).fetchone()
        if not zh_row or not conn.execute("SELECT 1 FROM entities WHERE id=? AND lifecycle='active'", (item["entity_id"],)).fetchone():
            continue
        mapping_id = "mapping." + hashlib.sha256(f"{zh_row['id']}|{en_row['id']}|{item['anchor']}".encode("utf-8")).hexdigest()[:24]
        evidence = {
            "decided_by": "group_page_anchor_and_game_key",
            "entity_id": item["entity_id"],
            "english_group_page": en_row["url"],
            "english_anchor": item["anchor"],
            "game_key": item["game_key"],
            "zh_url": zh_row["url"],
            "match": ["group_page_anchor", "official_game_key", "dedicated_chinese_article"],
        }
        conn.execute(
            """INSERT INTO inventory_mappings
               (id, zh_inventory_id, en_inventory_id, status, rationale, evidence_json, decided_at)
               VALUES (?, ?, ?, 'confirmed', ?, ?, ?)
               ON CONFLICT(zh_inventory_id, en_inventory_id) DO UPDATE SET
                 status='confirmed', rationale=excluded.rationale,
                 evidence_json=excluded.evidence_json, decided_at=excluded.decided_at""",
            (
                mapping_id,
                zh_row["id"],
                en_row["id"],
                "中文单体文章对应英文合页中的明确锚点；本机游戏键、英文成员段落和中文文章共同确认身份，父页仍保留为组合上下文。",
                json.dumps(evidence, ensure_ascii=False, sort_keys=True),
                utc_now(),
            ),
        )
        add_claim(
            conn,
            item["entity_id"],
            "mapping.cross_source.monster_group_member",
            evidence,
            en_row["source_page_id"],
            language="en",
            extraction_method="manual",
            status="agreed",
            notes="Confirmed by the member-specific anchor on the shared English wiki.gg page and the installed game localization key.",
        )
        changed += 1
    return changed


def _add_shared_mechanic_claims(conn: sqlite3.Connection) -> int:
    en = conn.execute("SELECT id FROM source_pages WHERE title='Game localization eng/keywords.json' LIMIT 1").fetchone()
    zh = conn.execute("SELECT id FROM source_pages WHERE title='Game localization zhs/keywords.json' LIMIT 1").fetchone()
    if not en or not zh:
        return 0
    definitions = {
        "sts1.mechanic.block": ("Until next turn, prevents damage.", "持续到下回合开始前，阻挡伤害。"),
        "sts1.mechanic.exhaust": ("Exhausted cards are removed from combat until it ends.", "被消耗的牌会在本场战斗剩余时间内移出战斗。"),
    }
    changed = 0
    for entity_id, (en_text, zh_text) in definitions.items():
        if not conn.execute("SELECT 1 FROM entities WHERE id=?", (entity_id,)).fetchone():
            continue
        add_claim(conn, entity_id, "mechanic.definition", {"definition_en": en_text}, en[0], language="en", extraction_method="manual", status="verified_game", notes="Game-localized keyword evidence; fills the field-level provenance for the shared mechanic projection.")
        add_claim(conn, entity_id, "mechanic.definition.zh", zh_text, zh[0], language="zh-CN", extraction_method="manual", status="verified_game", notes="Game-localized keyword evidence; fills the field-level provenance for the shared mechanic projection.")
        changed += 1
    return changed


def _game_local_page(conn: sqlite3.Connection, language: str, filename: str) -> str | None:
    row = conn.execute(
        "SELECT id FROM source_pages WHERE source_id='game_local' AND source_page_key=? LIMIT 1",
        (f"localization/{language}/{filename}",),
    ).fetchone()
    return row[0] if row else None


def _insert_reviewed_mapping(
    conn: sqlite3.Connection,
    zh_inventory_id: str,
    en_inventory_id: str,
    rationale: str,
    evidence: dict[str, Any],
) -> None:
    mapping_id = "mapping." + hashlib.sha256(f"{zh_inventory_id}|{en_inventory_id}".encode("utf-8")).hexdigest()[:24]
    conn.execute(
        """INSERT INTO inventory_mappings
           (id, zh_inventory_id, en_inventory_id, status, rationale, evidence_json, decided_at)
           VALUES (?, ?, ?, 'confirmed', ?, ?, ?)
           ON CONFLICT(zh_inventory_id, en_inventory_id) DO UPDATE SET
             status='confirmed', rationale=excluded.rationale,
             evidence_json=excluded.evidence_json, decided_at=excluded.decided_at""",
        (mapping_id, zh_inventory_id, en_inventory_id, rationale, json.dumps(evidence, ensure_ascii=False, sort_keys=True), utc_now()),
    )


def _ensure_game_local_crosswalks(conn: sqlite3.Connection) -> int:
    """Record Chinese pages that match a game key but have no wiki entity.

    The inventory mapping deliberately points at a language=`en` game-local
    inventory row.  This keeps the mapping audit honest: the row is reviewed,
    but it is not presented as a wiki.gg identity or promoted to active.
    """
    changed = 0
    for item in GAME_LOCAL_CROSSWALKS:
        zh_row = conn.execute(
            """SELECT id, url FROM inventory_items
               WHERE source_id='xiaoheihe' AND language='zh-CN'
                 AND entity_kind=? AND article_id=? ORDER BY id LIMIT 1""",
            (item["kind"], item["zh_article_id"]),
        ).fetchone()
        game_row = conn.execute("SELECT id FROM entities WHERE id=?", (item["game_entity_id"],)).fetchone()
        game_page = _game_local_page(conn, "eng", "events.json" if item["kind"] == "event" else "powers.json")
        if not zh_row or not game_row or not game_page:
            continue
        game_item = insert_inventory(
            conn,
            source_id="game_local",
            source_page_id=game_page,
            source_item_key=f"{item['kind']}:{item['game_key']}",
            entity_kind=item["kind"],
            language="en",
            name=item["game_key"],
            url=f"game://desktop-1.0.jar/localization/{item['kind']}/{item['game_key']}",
            category="installed localization",
            metadata={"game_key": item["game_key"], "entity_id": item["game_entity_id"], "crosswalk_scope": "game_local_only"},
            status="parsed",
        )
        evidence = {
            "kind": item["kind"],
            "game_key": item["game_key"],
            "game_entity_id": item["game_entity_id"],
            "zh_article_id": item["zh_article_id"],
            "zh_url": zh_row["url"],
            "english_wiki_entity": False,
            "review": "source_text_and_installed_localization",
        }
        _insert_reviewed_mapping(conn, zh_row["id"], game_item, item["reason"], evidence)
        zh_page = _candidate_page(conn, item["candidate_id"])
        add_claim(
            conn,
            item["game_entity_id"],
            "mapping.cross_source.game_local",
            evidence,
            zh_page or game_page,
            language="zh-CN" if zh_page else "en",
            extraction_method="manual",
            status="agreed",
            notes="Reviewed Chinese article against the installed game localization; the game-only entity remains candidate because no standalone wiki.gg page was found.",
        )
        conn.execute(
            "UPDATE entities SET notes=? WHERE id=?",
            (f"{item['reason']}", item["game_entity_id"]),
        )
        changed += 1
    return changed


def _confirm_block_return_status(conn: sqlite3.Connection) -> int:
    """Merge the exact Chinese Block Return page into its canonical status."""
    item = STATUS_WIKI_CROSSWALK["15460336"]
    zh_row = conn.execute(
        """SELECT id, url FROM inventory_items
           WHERE source_id='xiaoheihe' AND language='zh-CN'
             AND entity_kind='status' AND article_id=? ORDER BY id LIMIT 1""",
        ("15460336",),
    ).fetchone()
    en_row = conn.execute(
        """SELECT id, url, source_page_id FROM inventory_items
           WHERE source_id='wiki_gg' AND language='en' AND entity_kind='status'
             AND name=? ORDER BY id LIMIT 1""",
        (item["english_name"],),
    ).fetchone()
    source_exists = conn.execute("SELECT 1 FROM entities WHERE id=?", (item["candidate_id"],)).fetchone()
    target_exists = conn.execute("SELECT 1 FROM entities WHERE id=? AND lifecycle='active'", (item["target_id"],)).fetchone()
    if not zh_row or not en_row or not target_exists:
        return 0
    # The Chinese article title describes the card's effect, while the
    # canonical status is named Block Return in the English wiki/JAR.  Keep
    # that title as an agreed alias rather than allowing it to replace the
    # localized status name on the canonical page.
    if source_exists:
        conn.execute(
            """UPDATE names SET name_kind='alias', is_preferred=0,
                      verification_status='agreed',
                      notes=COALESCE(notes, '') || ' Cross-source status alias reviewed.'
               WHERE entity_id=? AND language='zh-CN'""",
            (item["candidate_id"],),
        )
        merge_confirmed_candidate(conn, item["candidate_id"], item["target_id"])
    evidence = {
        "target_entity_id": item["target_id"],
        "target_name": item["english_name"],
        "zh_article_id": "15460336",
        "zh_url": zh_row["url"],
        "english_url": en_row["url"],
        "game_key": "BlockReturnPower",
        "match": ["xiaoheihe_buff_id", "wiki_gg_buff_anchor", "game_local_description"],
    }
    _insert_reviewed_mapping(conn, zh_row["id"], en_row["id"], item["reason"], evidence)
    add_claim(
        conn,
        item["target_id"],
        "mapping.cross_source.status",
        evidence,
        en_row["source_page_id"],
        language="en",
        extraction_method="manual",
        status="agreed",
        notes="Chinese status article was reviewed against the wiki.gg Block Return anchor and installed game key; source article claims remain attached to the canonical entity.",
    )
    return 1


def supplement_quality(conn: sqlite3.Connection) -> dict[str, int]:
    merged = 0
    mapped = 0
    for key, item in MAP_MECHANICS.items():
        if _merge_map_mechanic(conn, key, item):
            merged += 1
        page_id = _ensure_manual_page(conn, item["page_key"])
        if key == "monsters" or key in MAP_MECHANICS:
            zh_item, en_item = _ensure_mapping_inventory(conn, item, page_id)
            if zh_item and en_item:
                mapped += 1
    return {
        "parser_version": PARSER_VERSION,
        "map_mechanics_reviewed": merged,
        "inventory_mappings_added_or_confirmed": mapped,
        "encounter_names_reviewed": _supplement_encounter_names(conn),
        "character_source_attributions_repaired": _repair_character_sources(conn),
        "character_inventory_mappings_added_or_confirmed": _confirm_character_directory_mappings(conn),
        "group_member_inventory_mappings_added_or_confirmed": _confirm_group_member_directory_mappings(conn),
        "group_parent_names_added": _add_group_parent_names(conn),
        "shared_mechanic_claims_added": _add_shared_mechanic_claims(conn),
        "game_local_crosswalks_reviewed": _ensure_game_local_crosswalks(conn),
        "status_mappings_confirmed": _confirm_block_return_status(conn),
    }


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    with conn:
        result = supplement_quality(conn)
    conn.close()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
