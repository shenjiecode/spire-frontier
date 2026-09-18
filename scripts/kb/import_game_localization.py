"""Import localized data from the installed Slay the Spire JAR.

The wiki remains the primary structured source.  This importer adds the
installed game's English and Simplified Chinese localization JSON as a third,
independent source and never replaces existing wiki claims.  Exact bilingual
directory matches are written to a review CSV; the CSV can be applied with
``apply_mapping_decisions.py`` after the import.

Examples (from the repository root)::

    python scripts/kb/import_game_localization.py
    python scripts/kb/import_game_localization.py --jar "D:/Steam/.../desktop-1.0.jar"
    python scripts/kb/import_game_localization.py --kinds card,relic,potion

The default scope deliberately starts with cards, relics, and potions.  The
JAR also contains monsters, events, powers, and other localization files; they
can be enabled later once their source-to-entity boundaries have been audited.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
import sys
import unicodedata
import zipfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from bootstrap_sample import (  # type: ignore
    DB_PATH,
    ROOT,
    add_claim,
    add_entity,
    add_name,
    apply_schema,
    json_text,
    normalise,
    slug,
    utc_now,
)


PARSER_VERSION = "kb-game-local/0.1"
GAME_SOURCE_ID = "game_local"
DEFAULT_JAR = Path(r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\desktop-1.0.jar")
LANGS = {"eng": "en", "zhs": "zh-CN"}
KIND_FILES = {"card": "cards", "relic": "relics", "potion": "potions"}
CARD_SUFFIX_CHARACTER = {"R": "ironclad", "G": "silent", "B": "defect", "P": "watcher"}
CHARACTER_COLOR = {"ironclad": "Red", "silent": "Green", "defect": "Blue", "watcher": "Purple"}


def compact(value: Any) -> str:
    """Comparison key that tolerates punctuation and spaces only."""

    text = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return re.sub(r"[^a-z0-9]+", "", text)


def clean_display(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_build_id(jar_path: Path) -> str | None:
    # .../steamapps/common/SlayTheSpire/desktop-1.0.jar -> steamapps.
    manifest = jar_path.parent.parent.parent / "appmanifest_646570.acf"
    if not manifest.exists():
        return None
    text = manifest.read_text(encoding="utf-8", errors="replace")
    match = re.search(r'"buildid"\s+"([0-9]+)"', text)
    return match.group(1) if match else None


def source_page_id(source_id: str, url: str) -> str:
    return f"source_page.{source_id}.{hashlib.sha1(url.encode('utf-8')).hexdigest()[:16]}"


def ensure_source(conn: sqlite3.Connection, jar_path: Path, jar_sha: str, build_id: str | None) -> None:
    local_url = jar_path.resolve().as_uri()
    notes = json_text({
        "jar_path": str(jar_path.resolve()),
        "jar_sha256": jar_sha,
        "steam_build_id": build_id,
        "recorded_at": utc_now(),
    })
    conn.execute(
        """INSERT INTO sources(id, name, base_url, language, license, source_kind, scope_note, notes)
           VALUES (?, ?, ?, 'mixed', 'proprietary/unknown', 'game_data', ?, ?)
           ON CONFLICT(id) DO UPDATE SET name=excluded.name, base_url=excluded.base_url,
             scope_note=excluded.scope_note, notes=excluded.notes""",
        (
            GAME_SOURCE_ID,
            "本机《杀戮尖塔》游戏包（desktop-1.0.jar）",
            local_url,
            "Installed PC game localization resources; claims are versioned by JAR SHA-256 and Steam Build ID.",
            notes,
        ),
    )


def upsert_source_page(
    conn: sqlite3.Connection,
    *,
    url: str,
    title: str,
    key: str,
    snapshot_path: Path,
    body: bytes,
    notes: str,
    is_index: bool = False,
) -> str:
    page_id = source_page_id(GAME_SOURCE_ID, url)
    conn.execute(
        """INSERT INTO source_pages
           (id, source_id, url, title, source_page_key, fetched_at, http_status,
            content_type, snapshot_path, sha256, parser_version, is_index_page, notes)
           VALUES (?, ?, ?, ?, ?, ?, 200, 'application/json; charset=utf-8', ?, ?, ?, ?, ?)
           ON CONFLICT(id) DO UPDATE SET title=excluded.title,
             source_page_key=excluded.source_page_key, fetched_at=excluded.fetched_at,
             snapshot_path=excluded.snapshot_path, sha256=excluded.sha256,
             parser_version=excluded.parser_version, is_index_page=excluded.is_index_page,
             notes=excluded.notes""",
        (
            page_id,
            GAME_SOURCE_ID,
            url,
            title,
            key,
            utc_now(),
            str(snapshot_path.relative_to(ROOT)).replace("\\", "/"),
            hashlib.sha256(body).hexdigest(),
            PARSER_VERSION,
            1 if is_index else 0,
            notes,
        ),
    )
    return page_id


def load_game_json(zfile: zipfile.ZipFile, lang_dir: str, file_name: str) -> tuple[bytes, Any]:
    raw = zfile.read(f"localization/{lang_dir}/{file_name}.json")
    return raw, json.loads(raw.decode("utf-8"))


def character_for_card_key(key: str) -> str | None:
    match = re.search(r"_([RGBP])$", key)
    return CARD_SUFFIX_CHARACTER.get(match.group(1)) if match else None


def canonical_indexes(conn: sqlite3.Connection, kind: str) -> tuple[dict[str, list[str]], dict[tuple[str, str], list[str]]]:
    """Index non-candidate English entities by display name and card character."""

    by_name: dict[str, list[str]] = defaultdict(list)
    by_name_char: dict[tuple[str, str], list[str]] = defaultdict(list)
    rows = conn.execute(
        """SELECT e.id, n.name, c.character_entity_id
           FROM entities e JOIN names n ON n.entity_id=e.id
           LEFT JOIN cards c ON c.entity_id=e.id
           WHERE e.kind=? AND e.lifecycle!='candidate' AND n.language='en'""",
        (kind,),
    ).fetchall()
    character_names: dict[str, str] = {}
    for row in conn.execute(
        """SELECT c.entity_id, n.name FROM characters c JOIN names n ON n.entity_id=c.entity_id
           WHERE n.language='en' AND n.is_preferred=1"""
    ):
        character_names[row[0]] = normalise(row[1])
    for row in rows:
        key = compact(row[1])
        if not key:
            continue
        if row[0] not in by_name[key]:
            by_name[key].append(row[0])
        if row[2]:
            character = character_names.get(row[2], "")
            if character:
                by_name_char[(key, character)].append(row[0])
    return by_name, by_name_char


def resolve_canonical(
    kind: str,
    game_key: str,
    game_name: str,
    by_name: dict[str, list[str]],
    by_name_char: dict[tuple[str, str], list[str]],
) -> tuple[str | None, str | None]:
    """Resolve a game entry without guessing across same-name cards."""

    names = [clean_display(game_name), clean_display(game_key)]
    if game_name.upper().startswith("DEPRECATED "):
        names.append(clean_display(game_name[11:]))
    character = character_for_card_key(game_key) if kind == "card" else None
    candidates: list[str] = []
    for name in names:
        key = compact(name)
        if not key:
            continue
        values = by_name_char.get((key, character), []) if character else by_name.get(key, [])
        for value in values:
            if value not in candidates:
                candidates.append(value)
    return (candidates[0], "exact_game_name") if len(candidates) == 1 else (None, None)


def ensure_game_candidate(conn: sqlite3.Connection, kind: str, game_key: str) -> str:
    entity_id = f"sts1.game.candidate.{kind}.{slug(game_key)}"
    conn.execute(
        """INSERT INTO entities(id, kind, game, game_id, lifecycle, mapping_status, notes)
           VALUES (?, ?, 'sts1', ?, 'candidate', 'provisional', ?)
           ON CONFLICT(id) DO UPDATE SET game_id=COALESCE(excluded.game_id, entities.game_id),
             notes=COALESCE(excluded.notes, entities.notes)""",
        (entity_id, kind, game_key, "Game localization entry not yet tied to a wiki entity."),
    )
    if kind == "card":
        character = character_for_card_key(game_key)
        color = CHARACTER_COLOR.get(character, "Other")
        conn.execute(
            """INSERT INTO cards(entity_id, character_entity_id, color, card_type, rarity, availability, tags_json)
               VALUES (?, ?, ?, 'Other', NULL, 'game_localization', '[]')
               ON CONFLICT(entity_id) DO UPDATE SET character_entity_id=COALESCE(excluded.character_entity_id, cards.character_entity_id),
                 color=excluded.color, availability=excluded.availability""",
            (entity_id, f"sts1.character.{character}" if character else None, color),
        )
    return entity_id


def add_localized_name_and_claims(
    conn: sqlite3.Connection,
    *,
    entity_id: str,
    kind: str,
    game_key: str,
    language: str,
    payload: dict[str, Any],
    page_id: str,
    candidate: bool,
) -> None:
    display_name = clean_display(payload.get("NAME"))
    if display_name:
        add_name(
            conn,
            entity_id,
            language,
            display_name,
            source_page_id=page_id,
            name_kind="localization",
            status="verified_game",
            preferred=candidate,
            notes=f"Game localization key: {game_key}",
        )
        add_claim(
            conn,
            entity_id,
            "game.localization.name",
            display_name,
            page_id,
            language=language,
            extraction_method="manual",
            status="verified_game",
            notes="Imported from the installed game's localization JSON; see source page hash.",
        )

    if kind == "card":
        description = payload.get("DESCRIPTION")
        if description:
            add_claim(conn, entity_id, "game.card.description", description, page_id, language=language, extraction_method="manual", status="verified_game")
    elif kind == "relic":
        descriptions = payload.get("DESCRIPTIONS")
        flavor = payload.get("FLAVOR")
        if descriptions:
            add_claim(conn, entity_id, "game.relic.descriptions", descriptions, page_id, language=language, extraction_method="manual", status="verified_game")
        if flavor:
            add_claim(conn, entity_id, "game.relic.flavor", flavor, page_id, language=language, extraction_method="manual", status="verified_game")
    elif kind == "potion":
        descriptions = payload.get("DESCRIPTIONS")
        if descriptions:
            add_claim(conn, entity_id, "game.potion.descriptions", descriptions, page_id, language=language, extraction_method="manual", status="verified_game")


def update_game_id(conn: sqlite3.Connection, entity_id: str, game_key: str) -> None:
    row = conn.execute("SELECT game_id FROM entities WHERE id=?", (entity_id,)).fetchone()
    if row and not row[0]:
        conn.execute("UPDATE entities SET game_id=? WHERE id=?", (game_key, entity_id))


def canonical_inventory_entity(conn: sqlite3.Connection, row: sqlite3.Row) -> str | None:
    """Resolve an English inventory row to an existing non-candidate entity."""

    rows = conn.execute(
        """SELECT DISTINCT e.id FROM entities e JOIN names n ON n.entity_id=e.id
           WHERE e.kind=? AND e.lifecycle!='candidate' AND n.language='en'
             AND (n.normalized=? OR n.normalized=?)""",
        (row["entity_kind"], normalise(row["name"]), normalise(re.sub(r"\s+\([^)]*\)$", "", row["name"]))),
    ).fetchall()
    if row["entity_kind"] == "card" and row["character"]:
        filtered = []
        for value in rows:
            if conn.execute(
                """SELECT 1 FROM cards c JOIN names n ON n.entity_id=c.character_entity_id
                   WHERE c.entity_id=? AND n.language='en' AND n.normalized=?""",
                (value[0], row["character"].casefold()),
            ).fetchone():
                filtered.append(value)
        rows = filtered
    return rows[0][0] if len(rows) == 1 else None


def exact_game_mapping_rows(conn: sqlite3.Connection, game_entries: list[dict[str, Any]]) -> list[dict[str, str]]:
    """Return only exact official-name bilingual directory matches."""

    decisions: list[dict[str, str]] = []
    seen_zh: set[str] = set()
    seen_en: set[str] = set()
    for entry in game_entries:
        entity_id = entry.get("entity_id")
        if (
            not entity_id
            or not entry.get("zh_name")
            or entry.get("en_name", "").upper().startswith("DEPRECATED")
            or entry.get("zh_name", "").upper().startswith("DEPRECATED")
        ):
            continue
        kind = entry["kind"]
        en_rows = conn.execute(
            """SELECT * FROM inventory_items WHERE entity_kind=? AND language='en' AND status='parsed'
               ORDER BY id""",
            (kind,),
        ).fetchall()
        en_matches = []
        for row in en_rows:
            if canonical_inventory_entity(conn, row) != entity_id:
                continue
            row_base_name = re.sub(r"\s+\([^)]*\)$", "", row["name"])
            if compact(row["name"]) in {compact(entry["en_name"]), compact(entry["game_key"]), compact(entry["en_name"].removeprefix("DEPRECATED "))} or compact(row_base_name) in {compact(entry["en_name"]), compact(entry["game_key"]), compact(entry["en_name"].removeprefix("DEPRECATED "))}:
                en_matches.append(row)
        if len(en_matches) != 1:
            continue
        en_row = en_matches[0]
        zh_rows = conn.execute(
            """SELECT * FROM inventory_items WHERE entity_kind=? AND language='zh-CN' AND status='parsed'
               AND name=? ORDER BY id""",
            (kind, entry["zh_name"]),
        ).fetchall()
        if kind == "card" and en_row["character"]:
            zh_rows = [row for row in zh_rows if row["character"] == en_row["character"]]
        if len(zh_rows) != 1:
            continue
        zh_row = zh_rows[0]
        if zh_row["id"] in seen_zh or en_row["id"] in seen_en:
            continue
        seen_zh.add(zh_row["id"])
        seen_en.add(en_row["id"])
        evidence = {
            "entity_id": entity_id,
            "game_key": entry["game_key"],
            "game_english_name": entry["en_name"],
            "game_chinese_name": entry["zh_name"],
            "jar_sha256": entry.get("jar_sha256"),
            "steam_build_id": entry.get("steam_build_id"),
            "game_english_source_page_id": entry["en_page_id"],
            "game_source_page_id": entry["zh_page_id"],
            "match": ["official_game_english_name", "official_game_simplified_chinese_name", "same_category", "same_character"],
        }
        decisions.append({
            "zh_inventory_id": zh_row["id"],
            "en_inventory_id": en_row["id"],
            "status": "confirmed",
            "decided_by": "game_local_exact",
            "rationale": "本机游戏包的英文/简体中文本地化名称与两站目录逐字对应，类别与角色字段一致；保留游戏包 SHA-256 及条目键作为证据。",
            "evidence_json": json_text(evidence),
        })
    return decisions


def write_decisions(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["zh_inventory_id", "en_inventory_id", "status", "decided_by", "rationale", "evidence_json"]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", type=Path, default=DEFAULT_JAR, help="Installed desktop-1.0.jar")
    parser.add_argument("--kinds", default="card,relic,potion", help="Comma-separated kinds (default: card,relic,potion)")
    parser.add_argument("--decisions", type=Path, default=ROOT / "data" / "decisions" / "mapping-decisions.game-local.csv")
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

    jar_sha = sha256_file(jar_path)
    build_id = read_build_id(jar_path)
    snapshot_root = ROOT / "data" / "raw" / "game_local" / jar_sha[:16]
    snapshot_root.mkdir(parents=True, exist_ok=True)
    metadata = {
        "jar_path": str(jar_path),
        "jar_sha256": jar_sha,
        "steam_build_id": build_id,
        "jar_size": jar_path.stat().st_size,
        "recorded_at": utc_now(),
        "languages": sorted(LANGS),
        "kinds": kinds,
    }
    metadata_bytes = json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8")
    metadata_path = snapshot_root / "jar-metadata.json"
    metadata_path.write_bytes(metadata_bytes)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    apply_schema(conn)
    ensure_source(conn, jar_path, jar_sha, build_id)
    # A previous run may have recorded the same JAR before Steam's appmanifest
    # was readable.  Replace only those stale key claims so the current build
    # ID is the single displayed provenance value; descriptions and names are
    # kept as immutable evidence rows.
    conn.execute(
        """DELETE FROM claims
           WHERE field_path='game.localization_key'
             AND value_json LIKE '%\"steam_build_id\": null%'"""
    )
    meta_url = f"game://desktop-1.0.jar/{jar_sha}"
    meta_page_id = upsert_source_page(
        conn,
        url=meta_url,
        title="desktop-1.0.jar metadata",
        key="desktop-1.0.jar",
        snapshot_path=metadata_path,
        body=metadata_bytes,
        notes=json_text(metadata),
        is_index=True,
    )

    report: dict[str, Any] = {
        "parser_version": PARSER_VERSION,
        "jar": metadata,
        "source_page_id": meta_page_id,
        "kinds": {},
        "decisions": 0,
    }
    game_entries: list[dict[str, Any]] = []

    try:
        with zipfile.ZipFile(jar_path) as zfile:
            for kind in kinds:
                file_name = KIND_FILES[kind]
                localized: dict[str, dict[str, Any]] = {}
                pages: dict[str, str] = {}
                for lang_dir, language in LANGS.items():
                    raw, payload = load_game_json(zfile, lang_dir, file_name)
                    localized[language] = payload
                    out_path = snapshot_root / lang_dir / f"{file_name}.json"
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    out_path.write_bytes(raw)
                    url = f"game://desktop-1.0.jar/{jar_sha}/localization/{lang_dir}/{file_name}.json"
                    pages[language] = upsert_source_page(
                        conn,
                        url=url,
                        title=f"Game localization {lang_dir}/{file_name}.json",
                        key=f"localization/{lang_dir}/{file_name}.json",
                        snapshot_path=out_path,
                        body=raw,
                        notes=json_text({"jar_sha256": jar_sha, "steam_build_id": build_id, "entry": f"localization/{lang_dir}/{file_name}.json"}),
                    )

                by_name, by_name_char = canonical_indexes(conn, kind)
                kind_report = {"english_entries": len(localized["en"]), "matched_canonical": 0, "new_candidates": 0, "localized_claims": 0}
                for game_key in sorted(set(localized["en"]) | set(localized["zh-CN"])):
                    en_payload = localized["en"].get(game_key) or {}
                    zh_payload = localized["zh-CN"].get(game_key) or {}
                    en_name = clean_display(en_payload.get("NAME")) or clean_display(game_key)
                    zh_name = clean_display(zh_payload.get("NAME"))
                    entity_id, _ = resolve_canonical(kind, game_key, en_name, by_name, by_name_char)
                    candidate = entity_id is None
                    if candidate:
                        entity_id = ensure_game_candidate(conn, kind, game_key)
                        kind_report["new_candidates"] += 1
                    else:
                        kind_report["matched_canonical"] += 1
                        update_game_id(conn, entity_id, game_key)
                    add_claim(
                        conn,
                        entity_id,
                        "game.localization_key",
                        {"kind": kind, "key": game_key, "jar_sha256": jar_sha, "steam_build_id": build_id},
                        pages["en"],
                        extraction_method="manual",
                        status="verified_game",
                        notes="Stable key recorded from the installed game's localization JSON.",
                    )
                    add_localized_name_and_claims(conn, entity_id=entity_id, kind=kind, game_key=game_key, language="en", payload=en_payload, page_id=pages["en"], candidate=candidate)
                    add_localized_name_and_claims(conn, entity_id=entity_id, kind=kind, game_key=game_key, language="zh-CN", payload=zh_payload, page_id=pages["zh-CN"], candidate=candidate)
                    kind_report["localized_claims"] += 1
                    game_entries.append({
                        "kind": kind,
                        "game_key": game_key,
                        "entity_id": entity_id,
                        "en_name": en_name,
                        "zh_name": zh_name,
                        "en_page_id": pages["en"],
                        "zh_page_id": pages["zh-CN"],
                        "jar_sha256": jar_sha,
                        "steam_build_id": build_id,
                    })
                report["kinds"][kind] = kind_report

        decisions = exact_game_mapping_rows(conn, game_entries)
        write_decisions(args.decisions if args.decisions.is_absolute() else ROOT / args.decisions, decisions)
        report["decisions"] = len(decisions)
        report["decisions_path"] = str((args.decisions if args.decisions.is_absolute() else ROOT / args.decisions).relative_to(ROOT)).replace("\\", "/")
        report_path = ROOT / "reports" / "game-localization-report.json"
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
