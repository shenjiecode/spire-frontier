"""Import the remaining installed-game localization dictionaries.

``import_game_localization.py`` intentionally started with cards, relics and
potions.  This companion importer handles the other dictionaries in the same
JAR: events, monster labels, powers (the game's status/effect names), the game
dictionary keywords, and the four playable characters.  It only adds
versioned game-data claims; wiki inventory mappings are emitted to a separate
review CSV and are never guessed from name similarity alone.

The installed JAR is treated as a third source.  A game key can represent a
variant or a member of a grouped wiki page (for example ``AcidSlime_L``), so
the explicit group aliases below are intentionally conservative.  A source
page with no safe canonical target becomes a provisional game candidate.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
import unicodedata
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Any

import import_game_localization as base  # type: ignore


ROOT = base.ROOT
DB_PATH = base.DB_PATH
DEFAULT_JAR = base.DEFAULT_JAR
PARSER_VERSION = "kb-game-local-extended/0.1"
LANGS = base.LANGS
KIND_FILES = {
    "event": "events",
    "monster": "monsters",
    "status": "powers",
    "keyword": "keywords",
    "character": "characters",
}


def compact(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", text)


def clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def zh_base(value: Any) -> str:
    """Remove editorial labels used by the Chinese status pages only."""

    text = unicodedata.normalize("NFKC", str(value or "")).casefold()
    for suffix in ("（能力）", "(能力)", "（敌人）", "(敌人)", "（负）", "(负)", "（负面）", "(负面)"):
        text = text.replace(suffix, "")
    return compact(text)


def load_json(zfile: zipfile.ZipFile, lang: str, file_name: str) -> tuple[bytes, Any]:
    raw = zfile.read(f"localization/{lang}/{file_name}.json")
    return raw, json.loads(raw.decode("utf-8"))


def canonical_indexes(conn: sqlite3.Connection, kind: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = defaultdict(list)
    for row in conn.execute(
        """SELECT e.id, n.name FROM entities e JOIN names n ON n.entity_id=e.id
           WHERE e.kind=? AND e.lifecycle!='candidate' AND n.language='en'
           ORDER BY e.id""",
        (kind,),
    ):
        key = compact(row[1])
        if key and row[0] not in result[key]:
            result[key].append(row[0])
    return result


def canonical_name_map(conn: sqlite3.Connection, kind: str) -> dict[str, str]:
    """Preferred English display names for evidence and inventory matching."""

    result: dict[str, str] = {}
    for row in conn.execute(
        """SELECT e.id, n.name FROM entities e JOIN names n ON n.entity_id=e.id
           WHERE e.kind=? AND e.lifecycle!='candidate' AND n.language='en'
             AND n.is_preferred=1""",
        (kind,),
    ):
        result[row[0]] = row[1]
    return result


def event_alias(game_key: str, english_name: str) -> str:
    # The game key is older than the wiki title for this one event.
    if game_key == "Mushrooms":
        return "Hypnotizing Colored Mushrooms"
    return english_name


# The game stores members of a grouped monster article separately.  These are
# grouping decisions based on the monster names and the corresponding wiki
# article/image, not a generic fuzzy-name merge.
MONSTER_GROUP_BY_KEY: dict[str, str] = {
    "AcidSlime_L": "Acid Slimes",
    "AcidSlime_M": "Acid Slimes",
    "AcidSlime_S": "Acid Slimes",
    "SpikeSlime_L": "Spike Slimes",
    "SpikeSlime_M": "Spike Slimes",
    "SpikeSlime_S": "Spike Slimes",
    "FuzzyLouseDefensive": "Louses",
    "FuzzyLouseNormal": "Louses",
    "BanditBear": "Masked Bandits",
    "BanditChild": "Masked Bandits",
    "BanditLeader": "Masked Bandits",
    "Donu": "Donu and Deca",
    "Deca": "Donu and Deca",
    "SlaverBlue": "Slavers",
    "SlaverRed": "Slavers",
    "SlaverBoss": "Taskmaster",
    "SpireShield": "Spire Shield and Spire Spear",
    "SpireSpear": "Spire Shield and Spire Spear",
    "Serpent": "Spire Growth",
    "GremlinFat": "Gremlins",
    "GremlinThief": "Gremlins",
    "GremlinTsundere": "Gremlins",
    "GremlinWarrior": "Gremlins",
    "GremlinWizard": "Gremlins",
    "Spiker": "Shapes",
    "Exploder": "Shapes",
    "Repulsor": "Shapes",
}

# These keys have dedicated active entities after the grouped-page repair.
# Prefer them before the broader group aliases so a rerun does not collapse a
# member back onto its parent page.
MONSTER_SPLIT_BY_KEY: dict[str, str] = {
    "Centurion": "Centurion",
    "Healer": "Mystic",
    "Donu": "Donu",
    "Deca": "Deca",
    "SpireShield": "Spire Shield",
    "SpireSpear": "Spire Spear",
}


# Chinese article titles for grouped pages.  Entries deliberately omitted
# here (notably Centurion/Mystic) have a different source granularity and stay
# in the manual queue.
MONSTER_ZH_TARGET: dict[str, str] = {
    "Acid Slimes": "酸液史莱姆",
    "Spike Slimes": "尖刺史莱姆",
    "Louses": "虱虫",
    "Masked Bandits": "蒙面强盗",
    "Donu and Deca": "八体/甜圈",
    "Slavers": "奴隶主",
    "Taskmaster": "奴隶头子",
    "Spire Shield and Spire Spear": "高塔之盾/高塔之矛",
    "Spire Growth": "塔内增生组织",
    "Gremlins": "地精小队",
    "Shapes": "三机械",
}


# The game has a few internal power keys whose visible name is shared by a
# second, distinct status page.  These explicit choices keep mapping review
# one-to-one and leave the negative/duplicate page provisional.
STATUS_ZH_TARGET_BY_KEY: dict[str, str] = {
    "Dexterity": "敏捷",
    "Focus": "集中",
    "Strength": "力量",
    "Regenerate": "再生（敌人）",
    "Regeneration": "再生",
    "Draw": "抽牌",
    "No Draw": "不能抽牌",
}

# Internal power keys whose display name is a historical/grammatical variant
# of the wiki status title.  This is an explicit game-key mapping, not fuzzy
# matching.
STATUS_EN_ALIAS_BY_KEY: dict[str, str] = {
    "Weakened": "Weak",
    "Flight": "Flying",
    "Spore Cloud": "Spore Clouds",
    "Draw Down": "Draw Reduction",
}


def player_character_key(key: str) -> bool:
    return key in {"Ironclad", "Silent", "Defect", "Watcher"}


def display_pair(kind: str, game_key: str, payload: Any) -> tuple[str, str]:
    """Return the English/Chinese visible name for an entry."""

    if kind == "keyword":
        en_name = ""
        zh_name = ""
        if isinstance(payload, tuple):
            en_payload, zh_payload = payload
            en_name = clean((en_payload.get("NAMES") or [""])[0]) if isinstance(en_payload, dict) else ""
            zh_name = clean((zh_payload.get("NAMES") or [""])[0]) if isinstance(zh_payload, dict) else ""
        return en_name or game_key, zh_name or game_key
    if kind == "character":
        return (
            clean((payload[0].get("NAMES") or [""])[0]) or game_key,
            clean((payload[1].get("NAMES") or [""])[0]) or game_key,
        )
    en_payload, zh_payload = payload
    return clean(en_payload.get("NAME")) or game_key, clean(zh_payload.get("NAME")) or game_key


def resolve_entity(
    conn: sqlite3.Connection,
    kind: str,
    game_key: str,
    en_name: str,
    indexes: dict[str, list[str]],
) -> str | None:
    if kind == "character":
        return {
            "Ironclad": "sts1.character.ironclad",
            "Silent": "sts1.character.silent",
            "Defect": "sts1.character.defect",
            "Watcher": "sts1.character.watcher",
        }.get(game_key)
    if kind == "monster" and game_key in MONSTER_SPLIT_BY_KEY:
        split_name = MONSTER_SPLIT_BY_KEY[game_key]
        split_matches = indexes.get(compact(split_name), [])
        if len(split_matches) == 1:
            return split_matches[0]
    if kind == "monster" and game_key in MONSTER_GROUP_BY_KEY:
        en_name = MONSTER_GROUP_BY_KEY[game_key]
    if kind == "event":
        en_name = event_alias(game_key, en_name)
    if kind == "status":
        en_name = STATUS_EN_ALIAS_BY_KEY.get(game_key, en_name)
    matches = indexes.get(compact(en_name), [])
    return matches[0] if len(matches) == 1 else None


def ensure_candidate(conn: sqlite3.Connection, kind: str, game_key: str) -> str:
    entity_id = f"sts1.game.candidate.{kind}.{base.slug(game_key)}"
    conn.execute(
        """INSERT INTO entities(id,kind,game,game_id,lifecycle,mapping_status,notes)
           VALUES (?,?,'sts1',?,'candidate','provisional',?)
           ON CONFLICT(id) DO UPDATE SET game_id=COALESCE(excluded.game_id,entities.game_id),
             notes=COALESCE(excluded.notes,entities.notes)""",
        (entity_id, kind, game_key, "Installed-game localization entry not yet tied to a wiki entity."),
    )
    if kind == "event":
        conn.execute("INSERT OR IGNORE INTO events(entity_id) VALUES (?)", (entity_id,))
    elif kind == "monster":
        conn.execute("INSERT OR IGNORE INTO monsters(entity_id,category) VALUES (?, 'other')", (entity_id,))
    elif kind == "status":
        conn.execute("INSERT OR IGNORE INTO statuses(entity_id,polarity) VALUES (?, 'neutral')", (entity_id,))
    elif kind == "keyword":
        conn.execute("INSERT OR IGNORE INTO keywords(entity_id) VALUES (?)", (entity_id,))
    return entity_id


def add_localized_entry(
    conn: sqlite3.Connection,
    *,
    kind: str,
    game_key: str,
    entity_id: str,
    en_payload: Any,
    zh_payload: Any,
    en_page_id: str,
    zh_page_id: str,
    jar_sha: str,
    build_id: str | None,
    en_name: str,
    zh_name: str,
    candidate: bool,
) -> None:
    for language, name, page_id in (("en", en_name, en_page_id), ("zh-CN", zh_name, zh_page_id)):
        if not name:
            continue
        base.add_name(
            conn,
            entity_id,
            language,
            name,
            source_page_id=page_id,
            name_kind="localization",
            status="verified_game",
            preferred=candidate,
            notes=f"Game localization key: {game_key}",
        )
        base.add_claim(
            conn,
            entity_id,
            "game.localization.name",
            name,
            page_id,
            language=language,
            extraction_method="manual",
            status="verified_game",
            notes=f"Imported from JAR {jar_sha}; Steam Build ID {build_id or 'unknown'}.",
        )
    base.add_claim(
        conn,
        entity_id,
        "game.localization_key",
        {"kind": kind, "key": game_key, "jar_sha256": jar_sha, "steam_build_id": build_id},
        en_page_id,
        extraction_method="manual",
        status="verified_game",
    )

    if kind == "event":
        for field, payload, page_id, language in (
            ("game.event.descriptions", en_payload.get("DESCRIPTIONS"), en_page_id, "en"),
            ("game.event.options", en_payload.get("OPTIONS"), en_page_id, "en"),
            ("game.event.descriptions", zh_payload.get("DESCRIPTIONS"), zh_page_id, "zh-CN"),
            ("game.event.options", zh_payload.get("OPTIONS"), zh_page_id, "zh-CN"),
        ):
            if payload:
                base.add_claim(conn, entity_id, field, payload, page_id, language=language, extraction_method="manual", status="verified_game")
    elif kind == "monster":
        for field, payload, page_id, language in (
            ("game.monster.moves", en_payload.get("MOVES"), en_page_id, "en"),
            ("game.monster.dialog", en_payload.get("DIALOG"), en_page_id, "en"),
            ("game.monster.moves", zh_payload.get("MOVES"), zh_page_id, "zh-CN"),
            ("game.monster.dialog", zh_payload.get("DIALOG"), zh_page_id, "zh-CN"),
        ):
            if payload:
                base.add_claim(conn, entity_id, field, payload, page_id, language=language, extraction_method="manual", status="verified_game")
    elif kind == "status":
        for field, payload, page_id, language in (
            ("game.status.descriptions", en_payload.get("DESCRIPTIONS"), en_page_id, "en"),
            ("game.status.descriptions", zh_payload.get("DESCRIPTIONS"), zh_page_id, "zh-CN"),
        ):
            if payload:
                base.add_claim(conn, entity_id, field, payload, page_id, language=language, extraction_method="manual", status="verified_game")
    elif kind == "keyword":
        for field, payload, page_id, language in (
            ("game.keyword.names", en_payload.get("NAMES"), en_page_id, "en"),
            ("game.keyword.description", en_payload.get("DESCRIPTION"), en_page_id, "en"),
            ("game.keyword.names", zh_payload.get("NAMES"), zh_page_id, "zh-CN"),
            ("game.keyword.description", zh_payload.get("DESCRIPTION"), zh_page_id, "zh-CN"),
        ):
            if payload:
                base.add_claim(conn, entity_id, field, payload, page_id, language=language, extraction_method="manual", status="verified_game")
    elif kind == "character":
        for field, payload, page_id, language in (
            ("game.character.text", en_payload.get("TEXT"), en_page_id, "en"),
            ("game.character.text", zh_payload.get("TEXT"), zh_page_id, "zh-CN"),
        ):
            if payload:
                base.add_claim(conn, entity_id, field, payload, page_id, language=language, extraction_method="manual", status="verified_game")


def inventory_entity_map(conn: sqlite3.Connection, kind: str) -> dict[str, list[str]]:
    """Map an English inventory name to canonical entity IDs."""

    result: dict[str, list[str]] = defaultdict(list)
    indexes = canonical_indexes(conn, kind)
    for row in conn.execute(
        "SELECT id,name FROM inventory_items WHERE entity_kind=? AND language='en' AND status='parsed'",
        (kind,),
    ):
        ids = indexes.get(compact(row[1]), [])
        if len(ids) == 1:
            result[row[0]] = ids
    return result


def existing_confirmed(conn: sqlite3.Connection, zh_id: str) -> str | None:
    row = conn.execute(
        "SELECT en_inventory_id FROM inventory_mappings WHERE zh_inventory_id=? AND status='confirmed' ORDER BY id LIMIT 1",
        (zh_id,),
    ).fetchone()
    return row[0] if row else None


def decision(
    zh_row: sqlite3.Row,
    en_row: sqlite3.Row,
    *,
    game_key: str,
    en_name: str,
    zh_name: str,
    jar_sha: str,
    build_id: str | None,
    note: str,
) -> dict[str, str]:
    evidence = {
        "game_key": game_key,
        "game_english_name": en_name,
        "game_chinese_name": zh_name,
        "jar_sha256": jar_sha,
        "steam_build_id": build_id,
        "match": ["official_game_english_name", "official_game_simplified_chinese_name", "same_category"],
    }
    return {
        "zh_inventory_id": zh_row["id"],
        "en_inventory_id": en_row["id"],
        "status": "confirmed",
        "decided_by": "game_local_extended",
        "rationale": note,
        "evidence_json": json.dumps(evidence, ensure_ascii=False, sort_keys=True),
    }


def build_decisions(
    conn: sqlite3.Connection,
    entries: list[dict[str, Any]],
    *,
    jar_sha: str,
    build_id: str | None,
) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    used_zh: set[str] = set()
    used_en: set[str] = set()
    canonical_names = {
        kind: canonical_name_map(conn, kind)
        for kind in ("event", "monster", "status")
    }
    for entry in entries:
        kind = entry["kind"]
        if kind not in {"event", "monster", "status"} or not entry.get("entity_id"):
            continue
        entity_id = entry["entity_id"]
        en_name = entry["en_name"]
        zh_name = entry["zh_name"]
        en_rows = list(conn.execute(
            "SELECT * FROM inventory_items WHERE entity_kind=? AND language='en' AND status='parsed'",
            (kind,),
        ))
        en_candidates: list[sqlite3.Row] = []
        for row in en_rows:
            ids = canonical_indexes(conn, kind).get(compact(row["name"]), [])
            if entity_id in ids:
                en_candidates.append(row)

        if kind == "monster" and entity_id == "sts1.monster.sentry":
            en_candidates = [row for row in en_candidates if row["subcategory"] == "elite"] or en_candidates
        if len(en_candidates) != 1:
            continue
        en_row = en_candidates[0]

        zh_rows = list(conn.execute(
            "SELECT * FROM inventory_items WHERE entity_kind=? AND language='zh-CN' AND status='parsed'",
            (kind,),
        ))
        if kind == "event":
            target_name = zh_name
            zh_candidates = [row for row in zh_rows if compact(row["name"]) == compact(target_name)]
            # The page title omits the explanatory question mark in Vampires.
            if not zh_candidates and entry["game_key"] == "Vampires":
                zh_candidates = [row for row in zh_rows if row["name"] == "吸血鬼"]
            # The Chinese wiki uses “幽灵会议”, while the installed game
            # calls the same event “Council of Ghosts” (幽灵议会).
            if not zh_candidates and entry["game_key"] == "Ghosts":
                zh_candidates = [row for row in zh_rows if row["name"] == "幽灵会议"]
        elif kind == "status":
            target_name = STATUS_ZH_TARGET_BY_KEY.get(entry["game_key"], zh_name)
            zh_candidates = [row for row in zh_rows if zh_base(row["name"]) == zh_base(target_name)]
            # Prefer the exact editorial suffix when two pages share a base.
            if entry["game_key"] in STATUS_ZH_TARGET_BY_KEY:
                zh_candidates = [row for row in zh_candidates if row["name"] == target_name] or zh_candidates
        else:
            target_name = MONSTER_ZH_TARGET.get(canonical_names["monster"].get(entity_id, en_name), zh_name)
            zh_candidates = [row for row in zh_rows if row["name"] == target_name]
            if not zh_candidates:
                zh_candidates = [row for row in zh_rows if compact(row["name"]) == compact(target_name)]
        if len(zh_candidates) != 1:
            continue
        zh_row = zh_candidates[0]
        if zh_row["id"] in used_zh or en_row["id"] in used_en:
            continue
        old = existing_confirmed(conn, zh_row["id"])
        if old:
            continue
        used_zh.add(zh_row["id"])
        used_en.add(en_row["id"])
        note = (
            "本机游戏包英文/简体中文本地化键、显示名称与两站目录条目一致；"
            "怪物分组条目另按游戏键对应的小黑盒合页与图片范围确认，保留 JAR 哈希作为证据。"
            if kind == "monster"
            else "本机游戏包英文/简体中文本地化键与两站目录条目一致，保留 JAR 哈希作为证据。"
        )
        out.append(decision(zh_row, en_row, game_key=entry["game_key"], en_name=en_name, zh_name=zh_name, jar_sha=jar_sha, build_id=build_id, note=note))
    return out


def write_decisions(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["zh_inventory_id", "en_inventory_id", "status", "decided_by", "rationale", "evidence_json"]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def load_decisions(path: Path) -> list[dict[str, str]]:
    """Load an existing reviewed CSV so incremental imports cannot erase it."""

    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", type=Path, default=DEFAULT_JAR)
    parser.add_argument("--kinds", default="event,monster,status,keyword,character")
    parser.add_argument("--decisions", type=Path, default=ROOT / "data" / "decisions" / "mapping-decisions.game-extended.csv")
    args = parser.parse_args(argv)
    jar_path = args.jar.expanduser().resolve()
    if not jar_path.exists():
        raise SystemExit(f"game JAR not found: {jar_path}")
    kinds = [value.strip() for value in args.kinds.split(",") if value.strip()]
    unknown = [kind for kind in kinds if kind not in KIND_FILES]
    if unknown:
        raise SystemExit("unsupported kind(s): " + ", ".join(unknown))
    if not DB_PATH.exists():
        raise SystemExit("data/spire.sqlite not found; run the KB bootstrap first")

    jar_sha = base.sha256_file(jar_path)
    build_id = base.read_build_id(jar_path)
    snapshot_root = ROOT / "data" / "raw" / "game_local" / jar_sha[:16]
    snapshot_root.mkdir(parents=True, exist_ok=True)
    metadata = {
        "jar_path": str(jar_path),
        "jar_sha256": jar_sha,
        "steam_build_id": build_id,
        "jar_size": jar_path.stat().st_size,
        "recorded_at": base.utc_now(),
        "languages": sorted(LANGS),
        "kinds": kinds,
    }
    meta_path = snapshot_root / "jar-metadata-extended.json"
    meta_bytes = json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8")
    meta_path.write_bytes(meta_bytes)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    base.apply_schema(conn)
    base.ensure_source(conn, jar_path, jar_sha, build_id)
    meta_page_id = base.upsert_source_page(
        conn,
        url=f"game://desktop-1.0.jar/{jar_sha}/extended-metadata",
        title="desktop-1.0.jar extended metadata",
        key="desktop-1.0.jar extended",
        snapshot_path=meta_path,
        body=meta_bytes,
        notes=base.json_text(metadata),
        is_index=True,
    )
    report: dict[str, Any] = {
        "parser_version": PARSER_VERSION,
        "jar": metadata,
        "source_page_id": meta_page_id,
        "kinds": {},
        "decisions": 0,
    }
    entries: list[dict[str, Any]] = []
    try:
        with zipfile.ZipFile(jar_path) as zfile:
            for kind in kinds:
                file_name = KIND_FILES[kind]
                localized: dict[str, Any] = {}
                pages: dict[str, str] = {}
                for lang_dir, language in LANGS.items():
                    raw, payload = load_json(zfile, lang_dir, file_name)
                    localized[language] = payload
                    out_path = snapshot_root / lang_dir / f"{file_name}.json"
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    out_path.write_bytes(raw)
                    pages[language] = base.upsert_source_page(
                        conn,
                        url=f"game://desktop-1.0.jar/{jar_sha}/localization/{lang_dir}/{file_name}.json",
                        title=f"Game localization {lang_dir}/{file_name}.json",
                        key=f"localization/{lang_dir}/{file_name}.json",
                        snapshot_path=out_path,
                        body=raw,
                        notes=base.json_text({"jar_sha256": jar_sha, "steam_build_id": build_id, "entry": f"localization/{lang_dir}/{file_name}.json"}),
                    )

                if kind == "keyword":
                    en_dict = localized["en"].get("Game Dictionary", {})
                    zh_dict = localized["zh-CN"].get("Game Dictionary", {})
                    game_keys = [
                        key for key in sorted(set(en_dict) | set(zh_dict))
                        if isinstance(en_dict.get(key), dict) or isinstance(zh_dict.get(key), dict)
                    ]
                    payload_pairs = [(en_dict.get(key) or {}, zh_dict.get(key) or {}) for key in game_keys]
                elif kind == "character":
                    en_dict = localized["en"]
                    zh_dict = localized["zh-CN"]
                    game_keys = [key for key in sorted(set(en_dict) | set(zh_dict)) if player_character_key(key)]
                    payload_pairs = [(en_dict.get(key) or {}, zh_dict.get(key) or {}) for key in game_keys]
                else:
                    en_dict = localized["en"]
                    zh_dict = localized["zh-CN"]
                    game_keys = sorted(set(en_dict) | set(zh_dict))
                    payload_pairs = [(en_dict.get(key) or {}, zh_dict.get(key) or {}) for key in game_keys]

                indexes = canonical_indexes(conn, kind)
                report_kind = {"english_entries": len(game_keys), "matched_canonical": 0, "new_candidates": 0, "localized_claims": 0}
                for game_key, payload_pair in zip(game_keys, payload_pairs):
                    en_payload, zh_payload = payload_pair
                    en_name, zh_name = display_pair(kind, game_key, payload_pair)
                    entity_id = resolve_entity(conn, kind, game_key, en_name, indexes)
                    candidate = entity_id is None
                    if candidate:
                        entity_id = ensure_candidate(conn, kind, game_key)
                        report_kind["new_candidates"] += 1
                    else:
                        conn.execute("UPDATE entities SET game_id=COALESCE(game_id, ?) WHERE id=?", (game_key, entity_id))
                        report_kind["matched_canonical"] += 1
                    add_localized_entry(
                        conn,
                        kind=kind,
                        game_key=game_key,
                        entity_id=entity_id,
                        en_payload=en_payload,
                        zh_payload=zh_payload,
                        en_page_id=pages["en"],
                        zh_page_id=pages["zh-CN"],
                        jar_sha=jar_sha,
                        build_id=build_id,
                        en_name=en_name,
                        zh_name=zh_name,
                        candidate=candidate,
                    )
                    entries.append({"kind": kind, "game_key": game_key, "entity_id": entity_id, "en_name": en_name, "zh_name": zh_name})
                    report_kind["localized_claims"] += 1
                report["kinds"][kind] = report_kind

        decisions = build_decisions(conn, entries, jar_sha=jar_sha, build_id=build_id)
        decision_path = args.decisions if args.decisions.is_absolute() else ROOT / args.decisions
        # A rerun after decisions have already been applied can legitimately
        # produce zero *new* rows.  Never replace a reviewed CSV with an empty
        # file in that case; preserving it keeps the audit trail replayable.
        decisions_preserved = False
        existing_decisions = load_decisions(decision_path)
        combined_decisions: list[dict[str, str]] = []
        seen_pairs: set[tuple[str, str]] = set()
        for row in [*existing_decisions, *decisions]:
            pair = ((row.get("zh_inventory_id") or "").strip(), (row.get("en_inventory_id") or "").strip())
            if not pair[0] or not pair[1] or pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            combined_decisions.append(row)
        if decisions or not decision_path.exists():
            write_decisions(decision_path, combined_decisions)
        else:
            decisions_preserved = True
        report["decisions"] = len(decisions)
        report["decisions_path"] = str(decision_path.relative_to(ROOT)).replace("\\", "/")
        report["decisions_preserved"] = decisions_preserved
        # The extended importer is intentionally rerunnable by kind.  Keep a
        # cumulative count in the report so a later status-only run does not
        # make the earlier event/monster decisions appear to have vanished.
        cumulative = 0
        cumulative_paths: list[str] = []
        for candidate_path in (
            ROOT / "data" / "decisions" / "mapping-decisions.game-extended.csv",
            ROOT / "data" / "decisions" / "mapping-decisions.game-extended-status.csv",
        ):
            if not candidate_path.exists():
                continue
            try:
                with candidate_path.open("r", encoding="utf-8-sig", newline="") as handle:
                    cumulative += max(0, sum(1 for _ in csv.DictReader(handle)))
                cumulative_paths.append(str(candidate_path.relative_to(ROOT)).replace("\\", "/"))
            except OSError:
                continue
        report["cumulative_decisions"] = cumulative
        report["cumulative_decision_files"] = cumulative_paths
        report_path = ROOT / "reports" / "game-localization-extended-report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
