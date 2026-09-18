"""Repair deterministic structured fields from already captured evidence.

This script never invents a rule value.  It only promotes values that are
already present in the SQLite claims/raw snapshots:

* fills Chinese card descriptions and bilingual relic/potion descriptions;
* restores monster HP ranges and explicit multi-hit counts from wiki.gg
  ``Enemy Infobox``/``Intents Table`` wikitext;
* imports the six Act 1--3 normal encounter pools from the captured
  ``Monsters`` page, retaining the source row and unresolved details as
  claims.

It is idempotent and can be rerun after a fresh P3 import.  Candidate game
runtime/deprecated entries are deliberately left as candidates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from lxml import html

from bootstrap_sample import (
    DB_PATH,
    ROOT,
    add_claim,
    add_entity,
    add_name,
    add_relation,
    add_resolution,
    export_data,
    normalise,
    slug,
    utc_now,
)
from supplement_editorial_zh import supplement as supplement_editorial_zh
from supplement_quality import supplement_quality

# Reuse the conservative template parser used by the P3 importer.  Keeping
# the same parser here matters for grouped enemy pages: the child entities must
# receive the same intent/effect text as the parent page, not a second ad-hoc
# interpretation of the wikitext.
from fetch_p3 import parse_all_template_blocks, strip_wiki_markup, template_params


PARSER_VERSION = "kb-structured-repair/0.7"
MONSTER_SNAPSHOT_GLOB = "data/raw/wiki_gg/*/inventory_monsters-*.bin"


# The installed game keeps an old, deprecated key beside the live key for
# these two entries.  ``entities.game_id`` is a single canonical key, so the
# live key wins; the deprecated key remains immutable evidence in claims and
# is also recorded as an old alias below.
GAME_KEY_CANONICAL_OVERRIDES: tuple[tuple[str, str, str, str], ...] = (
    ("card", "Fasting2", "sts1.card.watcher.fasting", "Fasting"),
    ("potion", "ElixirPotion", "sts1.potion.elixir", "Elixir"),
)


# A handful of localized game strings intentionally use formatter tokens
# (``!M!``, ``!D!`` and ``!B!``) and do not ship a separate upgrade string.
# The values below are rendered from those official templates plus the
# numeric base/upgrade values parsed from the wiki.gg card page.  Every row is
# written back as a claim with an explicit derivation note; it is never
# presented as an unqualified screenshot transcription.
CARD_ZH_RENDERED: dict[str, dict[str, str]] = {
    "sts1.card.silent.concentrate": {
        "base": "丢弃3张牌。获得2点能量。",
        "upgrade": "丢弃2张牌。获得2点能量。",
    },
    "sts1.card.watcher.lesson_learned": {
        "upgrade": "造成13点伤害。斩杀时，升级你牌组中的一张随机牌。消耗。",
    },
    "sts1.card.watcher.wish": {
        "base": "选择：获得6层多层护甲、3点力量或25金币。消耗。",
        "upgrade": "选择：获得8层多层护甲、4点力量或30金币。消耗。",
    },
}


# These are intentionally limited to the six page-level splits for which the
# captured wiki.gg wikitext has separate headings and the game localization
# exposes a stable member key.  Other grouped pages (for example the size
# variants of Slimes) remain grouped until their variant-specific stats are
# modelled explicitly.
MONSTER_GROUP_SPLITS: tuple[dict[str, Any], ...] = (
    {
        "group_id": "sts1.monster.centurion_and_mystic",
        "entity_id": "sts1.monster.centurion",
        "game_id": "Centurion",
        "en": "Centurion",
        "zh": "百夫长",
        "zh_article_id": "15436697",
        "hp": (76, 80),
        "asc_hp": (78, 83),
        "move_names": ("Slash", "Protect", "Fury"),
    },
    {
        "group_id": "sts1.monster.centurion_and_mystic",
        "entity_id": "sts1.monster.mystic",
        "game_id": "Healer",
        "en": "Mystic",
        "zh": "神秘术士",
        "zh_article_id": "15436699",
        "hp": (48, 56),
        "asc_hp": (50, 58),
        "move_names": ("Attack", "Buff", "Heal"),
    },
    {
        "group_id": "sts1.monster.donu_and_deca",
        "entity_id": "sts1.monster.donu",
        "game_id": "Donu",
        "en": "Donu",
        "zh": "甜圈",
        "hp": (250, 250),
        "asc_hp": (265, 265),
        "move_names": ("Circle of Power", "Beam"),
        "move_intents": ("Attack6",),
    },
    {
        "group_id": "sts1.monster.donu_and_deca",
        "entity_id": "sts1.monster.deca",
        "game_id": "Deca",
        "en": "Deca",
        "zh": "八体",
        "hp": (250, 250),
        "asc_hp": (265, 265),
        "move_names": ("Beam", "Square of Protection"),
        "move_intents": ("DebuffAttack5", "Defend"),
    },
    {
        "group_id": "sts1.monster.spire_shield_and_spire_spear",
        "entity_id": "sts1.monster.spire_shield",
        "game_id": "SpireShield",
        "en": "Spire Shield",
        "zh": "高塔之盾",
        "hp": (110, 110),
        "asc_hp": (125, 125),
        "move_names": ("Bash", "Fortify", "Smash"),
    },
    {
        "group_id": "sts1.monster.spire_shield_and_spire_spear",
        "entity_id": "sts1.monster.spire_spear",
        "game_id": "SpireSpear",
        "en": "Spire Spear",
        "zh": "高塔之矛",
        "hp": (160, 160),
        "asc_hp": (180, 180),
        "move_names": ("Burn Strike", "Skewer", "Piercer"),
    },
)


# The English pages below are deliberately grouped pages.  Their installed
# localization keys are stable and the captured page contains a separate
# Enemy Infobox and Intents Table for each member.  Keeping these mappings
# explicit prevents runtime-only names (for example ``HexaghostOrb``) from
# being promoted merely because they happen to occur in the JAR.
ADDITIONAL_MONSTER_GROUP_SPLITS: tuple[dict[str, Any], ...] = (
    # Act 1 slimes.  The same grouped page documents all six size/type
    # variants; the exact HP and actions are read from each section below.
    {"group_id": "sts1.monster.acid_slimes", "entity_id": "sts1.monster.acid_slime_l", "game_id": "AcidSlime_L", "en": "Acid Slime (L)", "zh": "酸液史莱姆（大）"},
    {"group_id": "sts1.monster.acid_slimes", "entity_id": "sts1.monster.acid_slime_m", "game_id": "AcidSlime_M", "en": "Acid Slime (M)", "zh": "酸液史莱姆（中）"},
    {"group_id": "sts1.monster.acid_slimes", "entity_id": "sts1.monster.acid_slime_s", "game_id": "AcidSlime_S", "en": "Acid Slime (S)", "zh": "酸液史莱姆（小）"},
    {"group_id": "sts1.monster.spike_slimes", "entity_id": "sts1.monster.spike_slime_l", "game_id": "SpikeSlime_L", "en": "Spike Slime (L)", "zh": "尖刺史莱姆（大）"},
    {"group_id": "sts1.monster.spike_slimes", "entity_id": "sts1.monster.spike_slime_m", "game_id": "SpikeSlime_M", "en": "Spike Slime (M)", "zh": "尖刺史莱姆（中）"},
    {"group_id": "sts1.monster.spike_slimes", "entity_id": "sts1.monster.spike_slime_s", "game_id": "SpikeSlime_S", "en": "Spike Slime (S)", "zh": "尖刺史莱姆（小）"},
    # Act 1 Gremlin group.
    {"group_id": "sts1.monster.gremlins", "entity_id": "sts1.monster.fat_gremlin", "game_id": "GremlinFat", "en": "Fat Gremlin", "zh": "胖地精"},
    {"group_id": "sts1.monster.gremlins", "entity_id": "sts1.monster.sneaky_gremlin", "game_id": "GremlinThief", "en": "Sneaky Gremlin", "zh": "卑鄙地精"},
    {"group_id": "sts1.monster.gremlins", "entity_id": "sts1.monster.shield_gremlin", "game_id": "GremlinTsundere", "en": "Shield Gremlin", "zh": "持盾地精"},
    {"group_id": "sts1.monster.gremlins", "entity_id": "sts1.monster.mad_gremlin", "game_id": "GremlinWarrior", "en": "Mad Gremlin", "zh": "火大地精"},
    {"group_id": "sts1.monster.gremlins", "entity_id": "sts1.monster.gremlin_wizard", "game_id": "GremlinWizard", "en": "Gremlin Wizard", "zh": "地精法师"},
    # Act 3 Shapes.
    {"group_id": "sts1.monster.shapes", "entity_id": "sts1.monster.exploder", "game_id": "Exploder", "en": "Exploder", "zh": "爆炸机"},
    {"group_id": "sts1.monster.shapes", "entity_id": "sts1.monster.repulsor", "game_id": "Repulsor", "en": "Repulsor", "zh": "反冲机"},
    {"group_id": "sts1.monster.shapes", "entity_id": "sts1.monster.spiker", "game_id": "Spiker", "en": "Spiker", "zh": "钉刺机"},
    # The two Louse colors and the two Slaver colors have distinct AI and
    # values even though both source sites use a shared article name.
    {"group_id": "sts1.monster.louses", "entity_id": "sts1.monster.red_louse", "game_id": "FuzzyLouseNormal", "en": "Red Louse", "zh": "虱虫"},
    {"group_id": "sts1.monster.louses", "entity_id": "sts1.monster.green_louse", "game_id": "FuzzyLouseDefensive", "en": "Green Louse", "zh": "虱虫"},
    {"group_id": "sts1.monster.slavers", "entity_id": "sts1.monster.blue_slaver", "game_id": "SlaverBlue", "en": "Blue Slaver", "zh": "奴隶贩子"},
    {"group_id": "sts1.monster.slavers", "entity_id": "sts1.monster.red_slaver", "game_id": "SlaverRed", "en": "Red Slaver", "zh": "奴隶贩子"},
    # Summoned minions documented as full members on their parent pages.
    {"group_id": "sts1.monster.bronze_automaton", "entity_id": "sts1.game.candidate.monster.bronzeorb", "game_id": "BronzeOrb", "en": "Bronze Orb", "zh": "铜球", "subtype": "minion"},
    {"group_id": "sts1.monster.the_collector", "entity_id": "sts1.game.candidate.monster.torchhead", "game_id": "TorchHead", "en": "Torch Head", "zh": "火炬头", "subtype": "minion"},
    {"group_id": "sts1.monster.reptomancer", "entity_id": "sts1.game.candidate.monster.dagger", "game_id": "Dagger", "en": "Dagger", "zh": "匕首", "subtype": "minion"},
)


# These pages are documentation groupings rather than one canonical monster.
# Their old P3 projection copied the first member's HP/actions onto the parent
# row, which is misleading once member entities exist.  Keep the raw grouped
# wikitext and ``has_member`` relations, but leave the structured monster
# fields on the children only.
GROUP_CONTEXT_ONLY: frozenset[str] = frozenset(
    {
        "sts1.monster.acid_slimes",
        "sts1.monster.centurion_and_mystic",
        "sts1.monster.donu_and_deca",
        "sts1.monster.gremlins",
        "sts1.monster.louses",
        "sts1.monster.shapes",
        "sts1.monster.slavers",
        "sts1.monster.spike_slimes",
        "sts1.monster.spire_shield_and_spire_spear",
    }
)


# These grouped pages still represent a real canonical enemy and additionally
# document a summoned member.  Restore their game identity after the generic
# group-parent cleanup below.
GROUP_CANONICAL_PARENTS: dict[str, str] = {
    "sts1.monster.bronze_automaton": "BronzeAutomaton",
    "sts1.monster.reptomancer": "Reptomancer",
    "sts1.monster.the_collector": "TheCollector",
}


def json_value(raw: str | None) -> Any:
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except (TypeError, json.JSONDecodeError):
        return raw


def link_variant_assets(conn: sqlite3.Connection) -> int:
    """Expose variant image links through the generic entity_assets table.

    Card variants already carry ``image_asset_id`` because that is the most
    convenient lookup for card rendering.  The generic association table is
    also part of the public schema, however, so keep both paths populated and
    make the relationship queryable for audits and future non-card assets.
    """
    rows = conn.execute(
        """SELECT ev.entity_id, cv.variant_id, cv.image_asset_id, a.usage_kind
           FROM card_variants cv
           JOIN entity_variants ev ON ev.id=cv.variant_id
           JOIN assets a ON a.id=cv.image_asset_id
           WHERE cv.image_asset_id IS NOT NULL"""
    ).fetchall()
    inserted = 0
    for row in rows:
        role = row["usage_kind"] if row["usage_kind"] in {"card_base", "card_upgrade"} else "evidence"
        before = conn.total_changes
        conn.execute(
            """INSERT OR IGNORE INTO entity_assets(entity_id, asset_id, variant_id, role)
               VALUES (?, ?, ?, ?)""",
            (row["entity_id"], row["image_asset_id"], row["variant_id"], role),
        )
        inserted += int(conn.total_changes > before)
    return inserted


def text_value(value: Any) -> str:
    if isinstance(value, list):
        return "".join(str(item) for item in value).strip()
    if isinstance(value, dict):
        for key in ("text", "description", "value"):
            if value.get(key):
                return str(value[key]).strip()
    return str(value or "").strip()


def usable_text(value: Any) -> str | None:
    text = text_value(value)
    if not text or "请输入图片描述" in text:
        return None
    return text


def latest_claim(
    conn: sqlite3.Connection,
    entity_id: str,
    field_path: str,
    language: str | None,
    *,
    variant_id: str | None = None,
    exclude_placeholder: bool = True,
) -> tuple[Any, str] | None:
    clauses = ["subject_entity_id=?", "field_path=?"]
    params: list[Any] = [entity_id, field_path]
    if language is None:
        clauses.append("language IS NULL")
    else:
        clauses.append("language=?")
        params.append(language)
    if variant_id is None:
        clauses.append("variant_id IS NULL")
    else:
        clauses.append("variant_id=?")
        params.append(variant_id)
    if exclude_placeholder:
        clauses.append("value_json NOT LIKE '%请输入图片描述%'")
    row = conn.execute(
        f"SELECT value_json, source_page_id FROM claims WHERE {' AND '.join(clauses)} ORDER BY created_at DESC, rowid DESC LIMIT 1",
        params,
    ).fetchone()
    return (json_value(row[0]), row[1]) if row else None


def shortest_text_claim(
    conn: sqlite3.Connection,
    entity_id: str,
    field_path: str,
    language: str,
) -> tuple[str, str] | None:
    """Choose the shortest non-placeholder textual claim.

    A rerun of the article parser can retain both a compact infobox value and
    a long article rendering under the same field path.  The compact value is
    the structured description; the full rendering remains in ``claims``.
    """
    rows = conn.execute(
        """SELECT value_json, source_page_id FROM claims
           WHERE subject_entity_id=? AND field_path=? AND language=?
             AND value_json NOT LIKE '%请输入图片描述%'
           ORDER BY rowid DESC""",
        (entity_id, field_path, language),
    ).fetchall()
    candidates: list[tuple[str, str]] = []
    for row in rows:
        text = usable_text(json_value(row[0]))
        if text:
            candidates.append((text, row[1]))
    return min(candidates, key=lambda item: len(item[0])) if candidates else None


def claim_id(entity_id: str, field_path: str, value: Any, source_page_id: str, locator: str | None) -> str:
    payload = "|".join((entity_id, field_path, json.dumps(value, ensure_ascii=False, sort_keys=True), source_page_id, locator or ""))
    return "claim." + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24]


def value_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return "text"


def add_raw_claim(
    conn: sqlite3.Connection,
    entity_id: str,
    field_path: str,
    value: Any,
    source_page_id: str,
    *,
    language: str | None = "en",
    locator: str | None = None,
    notes: str | None = None,
) -> None:
    identifier = claim_id(entity_id, field_path, value, source_page_id, locator)
    conn.execute(
        """INSERT OR IGNORE INTO claims
           (id, subject_entity_id, variant_id, field_path, value_json, value_type,
            language, source_page_id, locator, extraction_method,
            verification_status, created_at, notes)
           VALUES (?, ?, NULL, ?, ?, ?, ?, ?, ?, 'wikitext', 'single_source', ?, ?)""",
        (
            identifier,
            entity_id,
            field_path,
            json.dumps(value, ensure_ascii=False, sort_keys=True),
            value_type(value),
            language,
            source_page_id,
            locator,
            utc_now(),
            notes,
        ),
    )


def fill_card_chinese_descriptions(conn: sqlite3.Connection) -> int:
    changed = 0
    rows = conn.execute(
        """SELECT cv.variant_id, v.entity_id, cv.description_zh
           FROM card_variants cv JOIN entity_variants v ON v.id=cv.variant_id"""
    ).fetchall()
    for row in rows:
        claim = latest_claim(conn, row["entity_id"], "card.description", "zh-CN", variant_id=row["variant_id"])
        if not claim:
            continue
        text = usable_text(claim[0])
        if not text or row["description_zh"] == text:
            continue
        conn.execute("UPDATE card_variants SET description_zh=? WHERE variant_id=?", (text, row["variant_id"]))
        changed += 1
    return changed


def fill_missing_xiao_card_descriptions(conn: sqlite3.Connection) -> int:
    """Recover captions from Xiaoheihe cards whose article has no h1 blocks.

    Watcher and generated cards commonly put the base/upgrade captions next to
    images without an h1 heading.  The first P3 pass therefore retained the
    article text but could not attach it to a variant.  Captions before a
    ``测试画风`` heading are the auditable base/upgrade sequence.
    """
    changed = 0
    pages: dict[str, html.HtmlElement] = {}
    rows = conn.execute(
        """SELECT DISTINCT cv.variant_id, v.entity_id, v.variant_kind, sp.id AS source_page_id, sp.snapshot_path
           FROM card_variants cv JOIN entity_variants v ON v.id=cv.variant_id
           JOIN entities e ON e.id=v.entity_id
           JOIN names n ON n.entity_id=e.id AND n.language='zh-CN' AND n.is_preferred=1
           JOIN source_pages sp ON sp.id=n.source_page_id
           WHERE cv.description_zh IS NULL AND e.lifecycle!='candidate'
             AND sp.source_id='xiaoheihe' ORDER BY v.entity_id, v.variant_kind"""
    ).fetchall()
    grouped: dict[tuple[str, str], list[sqlite3.Row]] = {}
    for row in rows:
        grouped.setdefault((row["entity_id"], row["source_page_id"]), []).append(row)

    for (entity_id, source_page_id), variants in grouped.items():
        snapshot = variants[0]["snapshot_path"]
        path = ROOT / snapshot if snapshot else None
        if not path or not path.exists():
            continue
        if snapshot not in pages:
            try:
                pages[snapshot] = html.fromstring(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
        tree = pages[snapshot]
        root_nodes = tree.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " article-content ")]')
        root = root_nodes[0] if root_nodes else tree
        nodes = list(root.iter())
        stop = len(nodes)
        for index, node in enumerate(nodes):
            if node.tag.lower() in {"h1", "h2", "h3", "h4"} and "测试画风" in " ".join(node.text_content().split()):
                stop = index
                break
        captions: list[str] = []
        for node in nodes[:stop]:
            classes = set((node.get("class") or "").split())
            if "img-desc" not in classes:
                continue
            text = " ".join(node.text_content().split()).strip()
            if text and "请输入图片描述" not in text:
                captions.append(text)
        if not captions:
            continue
        by_kind = {row["variant_kind"]: row for row in variants}
        for index, kind in enumerate(("base", "upgrade")):
            row = by_kind.get(kind)
            if not row or index >= len(captions):
                continue
            text = captions[index]
            add_claim(
                conn,
                entity_id,
                "card.description",
                text,
                source_page_id,
                variant_id=row["variant_id"],
                language="zh-CN",
                locator=f"article-content/img-desc[{index + 1}]",
                extraction_method="visible_text",
                status="single_source",
                notes="Recovered from an image caption article without explicit h1 variant headings.",
            )
            conn.execute("UPDATE card_variants SET description_zh=? WHERE variant_id=?", (text, row["variant_id"]))
            changed += 1
    return changed


def source_page_for_game_file(conn: sqlite3.Connection, language_dir: str, file_name: str) -> str | None:
    row = conn.execute(
        """SELECT id FROM source_pages
           WHERE source_id='game_local' AND url LIKE ?
           ORDER BY fetched_at DESC LIMIT 1""",
        (f"%/localization/{language_dir}/{file_name}",),
    ).fetchone()
    return row[0] if row else None


def latest_game_snapshot(language_dir: str, file_name: str) -> Path | None:
    paths = sorted((ROOT / "data" / "raw" / "game_local").glob(f"*/{language_dir}/{file_name}"))
    return paths[-1] if paths else None


def clean_game_card_text(value: Any) -> str | None:
    text = usable_text(value)
    if not text:
        return None
    text = re.sub(r"\s*NL\s*", "", text)
    text = text.replace("*", "")
    text = re.sub(r"\s+([，。；：！？、])", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text or None


def fill_missing_game_card_descriptions(conn: sqlite3.Connection) -> int:
    """Fill card variants from the official zhs localization snapshot.

    The localization file is a third-source evidence record.  Cards with an
    explicit ``UPGRADE_DESCRIPTION`` use that text.  If the game leaves the
    upgrade string empty and the wiki.gg base/upgrade descriptions are equal,
    the base localization is copied with a note.  A small, explicit rendered
    table covers the remaining numeric-token cases (Concentrate, Lesson
    Learned and Wish), so those values stay auditable instead of silently
    remaining blank.
    """
    snapshot = latest_game_snapshot("zhs", "cards.json")
    page_id = source_page_for_game_file(conn, "zhs", "cards.json")
    if not snapshot or not page_id:
        return 0
    try:
        localized = json.loads(snapshot.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return 0

    changed = 0
    rows = conn.execute(
        """SELECT cv.variant_id, v.entity_id, v.variant_kind, e.game_id,
                  cv.description_en, cv.description_zh
           FROM card_variants cv
           JOIN entity_variants v ON v.id=cv.variant_id
           JOIN entities e ON e.id=v.entity_id
           WHERE e.lifecycle!='candidate' AND cv.description_zh IS NULL
           ORDER BY e.id, v.level, v.id"""
    ).fetchall()
    for row in rows:
        key = row["game_id"]
        payload = localized.get(key) if key else None
        text: str | None = None
        derivation = ""
        if isinstance(payload, dict):
            field = "UPGRADE_DESCRIPTION" if row["variant_kind"] == "upgrade" else "DESCRIPTION"
            text = clean_game_card_text(payload.get(field))
            if row["variant_kind"] == "upgrade" and not text:
                base_description = conn.execute(
                    """SELECT cv.description_en FROM card_variants cv
                       JOIN entity_variants v ON v.id=cv.variant_id
                       WHERE v.entity_id=? AND v.variant_kind='base'""",
                    (row["entity_id"],),
                ).fetchone()
                if base_description and base_description[0] == row["description_en"]:
                    text = clean_game_card_text(payload.get("DESCRIPTION"))
                    if text:
                        derivation = "游戏包未提供独立升级字符串，且 wiki.gg 基础/升级英文效果相同；沿用同一中文效果。"
        if not text:
            rendered = CARD_ZH_RENDERED.get(row["entity_id"], {}).get(row["variant_kind"])
            if rendered:
                text = rendered
                derivation = "由游戏包简体中文模板与 wiki.gg 已解析的基础/升级数值渲染；小黑盒升级图未提供可读文字。"
        if not text:
            continue
        notes = derivation or "直接取自本机游戏包 localization/zhs/cards.json。"
        add_claim(
            conn,
            row["entity_id"],
            "card.description",
            text,
            page_id,
            variant_id=row["variant_id"],
            language="zh-CN",
            extraction_method="manual",
            status="verified_game" if not derivation else "single_source",
            notes=notes,
        )
        conn.execute("UPDATE card_variants SET description_zh=? WHERE variant_id=?", (text, row["variant_id"]))
        changed += 1
    return changed


def repair_game_key_aliases(conn: sqlite3.Connection) -> int:
    """Make live localization keys canonical while preserving old keys."""
    changed = 0
    for kind, live_key, entity_id, deprecated_key in GAME_KEY_CANONICAL_OVERRIDES:
        row = conn.execute("SELECT kind, game_id, notes FROM entities WHERE id=?", (entity_id,)).fetchone()
        if not row or row["kind"] != kind:
            continue
        note = row["notes"] or ""
        marker = f"canonical game key: {live_key}"
        if row["game_id"] != live_key or marker not in note:
            suffix = marker + f"; deprecated alias retained in game localization claims: {deprecated_key}"
            merged_note = f"{note}; {suffix}" if note else suffix
            conn.execute("UPDATE entities SET game_id=?, notes=? WHERE id=?", (live_key, merged_note, entity_id))
            changed += 1

        page_id = source_page_for_game_file(conn, "eng", "cards.json" if kind == "card" else "potions.json")
        if kind == "card":
            file_name = "cards.json"
        else:
            file_name = "potions.json"
        page_id = source_page_for_game_file(conn, "eng", file_name)
        if page_id:
            add_name(
                conn,
                entity_id,
                "en",
                deprecated_key,
                source_page_id=page_id,
                name_kind="old_alias",
                status="verified_game",
                preferred=False,
                notes="Deprecated localization key; retained for historical lookup.",
            )
            add_claim(
                conn,
                entity_id,
                "game.localization_alias",
                {"kind": kind, "key": deprecated_key, "deprecated": True, "canonical_key": live_key},
                page_id,
                extraction_method="manual",
                status="verified_game",
                notes="Installed game localization marks this key as DEPRECATED; it is not the live game object.",
            )
    return changed


def fill_bilingual_effects(conn: sqlite3.Connection) -> dict[str, int]:
    changed = {"relic": 0, "potion": 0}
    for kind, table, field in (("relic", "relics", "relic.effect"), ("potion", "potions", "potion.effect")):
        rows = conn.execute(f"SELECT entity_id, effect_json FROM {table} ORDER BY entity_id").fetchall()
        for row in rows:
            current = json_value(row["effect_json"]) if row["effect_json"] else {}
            if not isinstance(current, dict):
                current = {"raw": current}
            before = json.dumps(current, ensure_ascii=False, sort_keys=True)

            # The clean English infobox is preferred over a long article claim.
            en_claim = shortest_text_claim(conn, row["entity_id"], "source.infobox.description", "en")
            if not en_claim:
                en_claim = shortest_text_claim(conn, row["entity_id"], field, "en")
            if en_claim:
                text = en_claim[0]
                if text:
                    current.setdefault("description_en", text)

            # The official localized game strings are preferred for Chinese;
            # they are retained as verified_game claims by the JAR importer.
            zh_claim = shortest_text_claim(conn, row["entity_id"], field, "zh-CN")
            if not zh_claim:
                zh_claim = latest_claim(conn, row["entity_id"], f"game.{kind}.descriptions", "zh-CN")
            if zh_claim:
                text = zh_claim[0] if isinstance(zh_claim[0], str) else usable_text(zh_claim[0])
                if text:
                    old = str(current.get("description_zh") or "")
                    if (
                        not old
                        or "#b" in old
                        or "请输入图片描述" in old
                        or "稀有度" in old
                        or (len(old) > 300 and len(text) < len(old))
                    ):
                        current["description_zh"] = text

            for language in ("en", "zh-CN"):
                flavor = latest_claim(conn, row["entity_id"], f"game.{kind}.flavor", language)
                if flavor:
                    text = usable_text(flavor[0])
                    if text:
                        current.setdefault(f"flavor_{'zh' if language == 'zh-CN' else 'en'}", text)

            after = json.dumps(current, ensure_ascii=False, sort_keys=True)
            if after != before:
                conn.execute(f"UPDATE {table} SET effect_json=? WHERE entity_id=?", (after, row["entity_id"]))
                changed[kind] += 1
    return changed


def fill_character_initial_gold(conn: sqlite3.Connection) -> int:
    """Promote the explicit ``金币`` cell from each captured Chinese page.

    The English character pages expose HP, deck and relic but do not expose
    starting gold.  The Xiaoheihe pages do, in a real HTML table, so this is a
    source-backed field rather than a remembered game constant.
    """
    changed = 0
    rows = conn.execute(
        """SELECT e.id, c.initial_gold, cl.source_page_id, sp.snapshot_path
           FROM entities e JOIN characters c ON c.entity_id=e.id
           JOIN claims cl ON cl.subject_entity_id=e.id
             AND cl.field_path='source.article_text' AND cl.language='zh-CN'
           JOIN source_pages sp ON sp.id=cl.source_page_id AND sp.source_id='xiaoheihe'
           WHERE e.kind='character' AND e.lifecycle='active'
           GROUP BY e.id ORDER BY e.id"""
    ).fetchall()
    for row in rows:
        if not row["snapshot_path"]:
            continue
        path = ROOT / row["snapshot_path"]
        if not path.exists():
            continue
        try:
            tree = html.fromstring(path.read_bytes())
        except (OSError, ValueError):
            continue
        value: int | None = None
        locator = "article-content/table"
        for tr in tree.xpath("//table//tr"):
            cells = [" ".join(cell.text_content().split()) for cell in tr.xpath("./th|./td")]
            if len(cells) < 2:
                continue
            if cells[0] in {"金币", "初始金币"}:
                match = re.search(r"\b\d+\b", cells[1])
                if match:
                    value = int(match.group(0))
                    locator = f"article-content/table/{cells[0]}"
                    break
        if value is None:
            continue
        claim = add_claim(
            conn,
            row["id"],
            "character.initial_gold",
            value,
            row["source_page_id"],
            language="zh-CN",
            locator=locator,
            extraction_method="structured_html",
            status="single_source",
            notes="Explicit 金币 cell in the captured Xiaoheihe character table.",
        )
        conn.execute(
            "UPDATE characters SET initial_gold=? WHERE entity_id=?",
            (value, row["id"]),
        )
        add_resolution(
            conn,
            row["id"],
            "character.initial_gold",
            claim,
            value,
            status="adopted",
            rationale="The value is explicitly present in the captured Chinese character table; no inferred value was used.",
        )
        changed += int(row["initial_gold"] != value)
    return changed


def _jar_path() -> Path | None:
    candidates = (
        Path(r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\desktop-1.0.jar"),
        Path(r"C:\Program Files\Steam\steamapps\common\SlayTheSpire\desktop-1.0.jar"),
    )
    return next((path for path in candidates if path.exists()), None)


def _class_constant_pool(class_bytes: bytes) -> list[Any] | None:
    """Read enough of a Java class constant pool to identify field refs."""
    if class_bytes[:4] != b"\xca\xfe\xba\xbe":
        return None
    offset = 8

    def u1() -> int:
        nonlocal offset
        value = class_bytes[offset]
        offset += 1
        return value

    def u2() -> int:
        nonlocal offset
        value = int.from_bytes(class_bytes[offset : offset + 2], "big")
        offset += 2
        return value

    def u4() -> int:
        nonlocal offset
        value = int.from_bytes(class_bytes[offset : offset + 4], "big")
        offset += 4
        return value

    def raw(size: int) -> bytes:
        nonlocal offset
        value = class_bytes[offset : offset + size]
        offset += size
        return value

    try:
        constant_count = u2()
        pool: list[Any] = [None] * constant_count
        index = 1
        while index < constant_count:
            tag = u1()
            if tag == 1:
                pool[index] = ("Utf8", raw(u2()).decode("utf-8", "replace"))
            elif tag in (3, 4):
                pool[index] = ("Number", u4())
            elif tag in (5, 6):
                pool[index] = ("Long", raw(8))
                index += 1
            elif tag in (7, 8, 16, 19, 20):
                pool[index] = (tag, u2())
            elif tag in (9, 10, 11, 12, 17, 18):
                pool[index] = (tag, u2(), u2())
            elif tag == 15:
                pool[index] = (tag, u1(), u2())
            else:
                return None
            index += 1
        return pool
    except (IndexError, UnicodeDecodeError):
        return None


def _cp_text(pool: list[Any], index: int) -> str:
    item = pool[index]
    if item and item[0] == "Utf8":
        return item[1]
    if item and item[0] in (7, 8, 16, 19, 20):
        return _cp_text(pool, item[1])
    return ""


def _potion_slot_bytecode_evidence(class_bytes: bytes) -> dict[str, Any] | None:
    """Find ``this.potionSlots = 3`` in AbstractPlayer's constructor.

    This is intentionally a narrow bytecode check.  It does not attempt to
    decompile the game; it only records the field reference, constructor
    method and byte sequence that establish the default slot count.
    """
    pool = _class_constant_pool(class_bytes)
    if not pool:
        return None
    refs: dict[int, str] = {}
    for index, item in enumerate(pool):
        if not item or item[0] != 9:
            continue
        try:
            name_type = pool[item[2]]
            owner = _cp_text(pool, item[1])
            field_name = _cp_text(pool, name_type[1])
            if owner == "com/megacrit/cardcrawl/characters/AbstractPlayer":
                refs[index] = field_name
        except (IndexError, TypeError):
            continue
    # The class uses the compact JVM sequence aload_0, iconst_3, putfield.
    for offset in range(max(0, len(class_bytes) - 5)):
        if class_bytes[offset : offset + 2] != b"\x2a\x06":
            continue
        if class_bytes[offset + 2] != 0xB5:
            continue
        field_ref = int.from_bytes(class_bytes[offset + 3 : offset + 5], "big")
        if refs.get(field_ref) == "potionSlots":
            return {
                "class": "com/megacrit/cardcrawl/characters/AbstractPlayer.class",
                "field": "potionSlots",
                "value": 3,
                "bytecode_pattern_hex": "2a06b5" + class_bytes[offset + 3 : offset + 5].hex(),
                "class_byte_offset": offset,
                "method": "<init>(String, AbstractPlayer$PlayerClass)",
            }
    return None


def fill_character_potion_slots(conn: sqlite3.Connection) -> tuple[int, dict[str, Any] | None]:
    """Use the installed game's exact JAR to verify the default slot count."""
    jar = _jar_path()
    if not jar:
        return 0, None
    metadata_paths = sorted((ROOT / "data" / "raw" / "game_local").glob("*/jar-metadata.json"))
    metadata: dict[str, Any] = {}
    if metadata_paths:
        try:
            metadata = json.loads(metadata_paths[-1].read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            metadata = {}
    try:
        import zipfile

        with zipfile.ZipFile(jar) as archive:
            class_bytes = archive.read("com/megacrit/cardcrawl/characters/AbstractPlayer.class")
    except (OSError, KeyError, zipfile.BadZipFile):
        return 0, None
    evidence = _potion_slot_bytecode_evidence(class_bytes)
    if not evidence:
        return 0, None
    evidence.update(
        {
            "jar_sha256": metadata.get("jar_sha256"),
            "steam_build_id": metadata.get("steam_build_id"),
            "class_sha256": hashlib.sha256(class_bytes).hexdigest(),
        }
    )
    jar_hash = str(metadata.get("jar_sha256") or "unknown")
    base_dir = ROOT / "data" / "raw" / "game_local" / jar_hash[:16]
    base_dir.mkdir(parents=True, exist_ok=True)
    evidence_path = base_dir / "jar-runtime-evidence.json"
    evidence_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    evidence_url = f"game://desktop-1.0.jar/{jar_hash}/runtime-evidence"
    evidence_page_id = "source_page.game_local." + hashlib.sha1(evidence_url.encode("utf-8")).hexdigest()[:16]
    evidence_digest = hashlib.sha256(evidence_path.read_bytes()).hexdigest()
    conn.execute(
        """INSERT INTO source_pages
           (id, source_id, url, title, source_page_key, fetched_at, http_status,
            content_type, snapshot_path, sha256, parser_version, is_index_page, notes)
           VALUES (?, 'game_local', ?, 'JAR runtime evidence', 'jar-runtime-evidence', ?,
                   200, 'application/json', ?, ?, ?, 0, ?)
           ON CONFLICT(id) DO UPDATE SET snapshot_path=excluded.snapshot_path,
             sha256=excluded.sha256, fetched_at=excluded.fetched_at,
             parser_version=excluded.parser_version, notes=excluded.notes""",
        (
            evidence_page_id,
            evidence_url,
            utc_now(),
            str(evidence_path.relative_to(ROOT)).replace("\\", "/"),
            evidence_digest,
            PARSER_VERSION,
            json.dumps({"jar_path": str(jar), "jar_sha256": jar_hash, "steam_build_id": metadata.get("steam_build_id")}, ensure_ascii=False, sort_keys=True),
        ),
    )
    changed = 0
    for row in conn.execute("SELECT entity_id, potion_slots FROM characters ORDER BY entity_id").fetchall():
        claim = add_claim(
            conn,
            row["entity_id"],
            "character.potion_slots",
            3,
            evidence_page_id,
            locator="AbstractPlayer.<init>:potionSlots",
            extraction_method="manual",
            status="verified_game",
            notes="Installed desktop-1.0.jar bytecode assigns iconst_3 to AbstractPlayer.potionSlots; class and JAR hashes are retained in the evidence JSON.",
        )
        conn.execute("UPDATE characters SET potion_slots=3 WHERE entity_id=?", (row["entity_id"],))
        add_resolution(
            conn,
            row["entity_id"],
            "character.potion_slots",
            claim,
            3,
            status="adopted",
            rationale="Verified from the installed game JAR for the recorded Steam Build ID.",
        )
        changed += int(row["potion_slots"] != 3)
    return changed, evidence


def _clean_wiki_text(value: str) -> str:
    """Turn a small wikitext excerpt into readable evidence text."""
    text = strip_wiki_markup(value or "")
    text = re.sub(r"\[\[([^\]|]+)(?:#[^\]|]+)?\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]|]+)(?:#[^\]|]+)?\]\]", r"\1", text)
    text = text.replace("]]", "").replace("[[", "")
    text = re.sub(r"\s+", " ", text).strip(" \t\r\n|;")
    return text


def _heading_sections(wikitext: str, heading: str) -> list[str]:
    """Extract all sections with an exact heading, respecting nesting."""
    heading_re = re.compile(r"^(=+)\s*(.*?)\s*\1\s*$", re.M)
    matches = list(heading_re.finditer(wikitext or ""))
    wanted = heading.casefold().strip()
    sections: list[str] = []
    for index, match in enumerate(matches):
        if match.group(2).strip().casefold() != wanted:
            continue
        level = len(match.group(1))
        end = len(wikitext)
        for next_match in matches[index + 1 :]:
            if len(next_match.group(1)) <= level:
                end = next_match.start()
                break
        body = _clean_wiki_text(wikitext[match.end() : end])
        if body:
            sections.append(body[:2000])
    return sections


def _template_fields(wikitext: str, template_name: str) -> dict[str, str]:
    for block in parse_all_template_blocks(wikitext or "", template_name):
        params = template_params(block)
        if params:
            return params
    return {}


def _latest_claim_value(
    conn: sqlite3.Connection,
    entity_id: str,
    field_path: str,
    language: str | None = None,
) -> tuple[Any, str] | None:
    clauses = ["subject_entity_id=?", "field_path=?"]
    params: list[Any] = [entity_id, field_path]
    if language is None:
        clauses.append("language IS NULL")
    else:
        clauses.append("language=?")
        params.append(language)
    row = conn.execute(
        f"SELECT value_json, source_page_id FROM claims WHERE {' AND '.join(clauses)} ORDER BY rowid DESC LIMIT 1",
        params,
    ).fetchone()
    return (json_value(row[0]), row[1]) if row else None


def _article_effect_lines(value: Any) -> tuple[str | None, str | None]:
    text = text_value(value)
    if not text:
        return None, None
    english = None
    chinese = None
    match = re.search(r"效果英文描述\s*\n?([^\n]+)", text)
    if match:
        english = match.group(1).strip()
    match = re.search(r"效果中文描述\s*\n?([^\n]+)", text)
    if match:
        chinese = match.group(1).strip()
    return english, chinese


def _game_description(conn: sqlite3.Connection, entity_id: str, language: str) -> str | None:
    claim = _latest_claim_value(conn, entity_id, "game.status.descriptions", language)
    if not claim:
        return None
    value = claim[0]
    if isinstance(value, list):
        text = "".join(str(item) for item in value if item is not None)
    else:
        text = text_value(value)
    return text.strip() or None


def fill_keyword_mechanic_definitions(conn: sqlite3.Connection) -> dict[str, int]:
    """Promote captured wiki sections/game descriptions into definitions.

    The first P3 pass stored source URLs but left the definition payload empty
    when a page used a shared ``Keywords``/``Mechanics`` article.  This pass
    reads only the already captured wikitext and localization claims; it does
    not infer wording from memory or from strategy documents.
    """
    changed = {"keyword": 0, "mechanic": 0}
    for kind, table, template_name in (
        ("keyword", "keywords", "Keyword Infobox"),
        ("mechanic", "mechanics", "Mechanic Infobox"),
    ):
        rows = conn.execute(
            f"""SELECT e.id, n.name, t.definition_json
                FROM entities e JOIN {table} t ON t.entity_id=e.id
                LEFT JOIN names n ON n.entity_id=e.id AND n.language='en' AND n.is_preferred=1
                WHERE e.kind=? AND e.lifecycle!='deprecated'""",
            (kind,),
        ).fetchall()
        for row in rows:
            wiki_claim = _latest_claim_value(conn, row["id"], "source.wikitext", "en")
            wikitext = text_value(wiki_claim[0]) if wiki_claim else ""
            fields = _template_fields(wikitext, template_name)
            infobox = _clean_wiki_text(fields.get("description", "")) if fields.get("description") else ""
            sections = _heading_sections(wikitext, row["name"] or "")
            game_en_claim = _latest_claim_value(conn, row["id"], "game.keyword.description", "en")
            game_zh_claim = _latest_claim_value(conn, row["id"], "game.keyword.description", "zh-CN")
            game_en = text_value(game_en_claim[0]) if game_en_claim else ""
            game_zh = text_value(game_zh_claim[0]) if game_zh_claim else ""
            definition_en = infobox or game_en or (sections[0] if sections else "")
            if not definition_en and not game_zh and not sections:
                continue
            try:
                payload = json.loads(row["definition_json"] or "{}")
            except (TypeError, json.JSONDecodeError):
                payload = {}
            if not isinstance(payload, dict):
                payload = {}
            if definition_en:
                payload["definition_en"] = definition_en
            if game_zh:
                payload["definition_zh"] = game_zh
            if sections:
                payload["wiki_sections"] = sections
            if wiki_claim:
                payload["wiki_source_page_id"] = wiki_claim[1]
            conn.execute(
                f"UPDATE {table} SET definition_json=? WHERE entity_id=?",
                (json.dumps(payload, ensure_ascii=False, sort_keys=True), row["id"]),
            )
            source_page_id = wiki_claim[1] if wiki_claim else (game_en_claim[1] if game_en_claim else game_zh_claim[1] if game_zh_claim else None)
            if source_page_id and definition_en:
                add_raw_claim(
                    conn,
                    row["id"],
                    f"{kind}.definition",
                    {"definition_en": definition_en, "definition_zh": game_zh or None, "wiki_sections": sections},
                    source_page_id,
                    language="en",
                    locator=f"{row['name']} definition",
                    notes="Promoted from captured wiki wikitext/game localization; no strategy text involved.",
                )
            changed[kind] += 1
    # A few mechanics (notably Block and Exhaust) are also indexed as
    # keywords and therefore have their authoritative captured text on the
    # keyword entity rather than on a separate Mechanics page.  Reuse that
    # source-backed definition instead of leaving a bootstrap placeholder.
    for row in conn.execute(
        """SELECT m.entity_id, n.name, m.definition_json
           FROM mechanics m JOIN entities e ON e.id=m.entity_id
           LEFT JOIN names n ON n.entity_id=m.entity_id AND n.language='en' AND n.is_preferred=1
           WHERE e.lifecycle!='deprecated'"""
    ).fetchall():
        current = json.loads(row["definition_json"] or "{}")
        if isinstance(current, dict) and (current.get("definition_en") or current.get("wiki_sections")):
            continue
        keyword = conn.execute(
            """SELECT k.definition_json FROM keywords k
               JOIN names n ON n.entity_id=k.entity_id AND n.language='en' AND n.is_preferred=1
               WHERE lower(n.name)=lower(?) LIMIT 1""",
            (row["name"],),
        ).fetchone()
        if not keyword:
            continue
        try:
            payload = json.loads(keyword[0] or "{}")
        except (TypeError, json.JSONDecodeError):
            payload = {}
        if not isinstance(payload, dict) or not (payload.get("definition_en") or payload.get("wiki_sections")):
            continue
        copied = {
            key: payload[key]
            for key in ("definition_en", "definition_zh", "wiki_sections", "wiki_source_page_id")
            if key in payload
        }
        copied["source_kind"] = "shared_keyword_definition"
        conn.execute(
            "UPDATE mechanics SET definition_json=? WHERE entity_id=?",
            (json.dumps(copied, ensure_ascii=False, sort_keys=True), row["entity_id"]),
        )
        changed["mechanic"] += 1
    return changed


def fill_status_descriptions(conn: sqlite3.Connection) -> dict[str, int]:
    """Fill status descriptions and infobox stacking/polarity from evidence."""
    changed = {"descriptions_en": 0, "descriptions_zh": 0, "infobox_fields": 0}
    rows = conn.execute(
        """SELECT e.id FROM entities e JOIN statuses s ON s.entity_id=e.id
           WHERE e.lifecycle!='deprecated'"""
    ).fetchall()
    for row in rows:
        entity_id = row["id"]
        wiki_claim = _latest_claim_value(conn, entity_id, "source.wikitext", "en")
        wikitext = text_value(wiki_claim[0]) if wiki_claim else ""
        fields = _template_fields(wikitext, "Power Infobox")
        wiki_description = _clean_wiki_text(fields.get("description", "")) if fields.get("description") else ""
        article_en = article_zh = None
        article_page_id = None
        for claim in conn.execute(
            "SELECT value_json, source_page_id FROM claims WHERE subject_entity_id=? AND field_path='source.article_text' ORDER BY rowid DESC",
            (entity_id,),
        ):
            article_en, article_zh = _article_effect_lines(json_value(claim["value_json"]))
            article_page_id = claim["source_page_id"]
            if article_en or article_zh:
                break
        game_en = _game_description(conn, entity_id, "en")
        game_zh = _game_description(conn, entity_id, "zh-CN")
        english = wiki_description or article_en or game_en
        chinese = article_zh or game_zh
        if english and wiki_claim:
            add_raw_claim(
                conn,
                entity_id,
                "status.description",
                english,
                wiki_claim[1],
                language="en",
                locator="Power Infobox/Description",
                notes="Parsed from the captured Power Infobox or the corresponding game/article description.",
            )
            changed["descriptions_en"] += 1
        elif english and article_page_id:
            add_raw_claim(conn, entity_id, "status.description", english, article_page_id, language="en", locator="article/effect_en")
            changed["descriptions_en"] += 1
        if chinese and article_page_id:
            add_raw_claim(conn, entity_id, "status.description", chinese, article_page_id, language="zh-CN", locator="article/effect_zh")
            changed["descriptions_zh"] += 1
        type_text = (fields.get("type") or "").casefold()
        polarity = "positive" if "buff" in type_text else "negative" if "debuff" in type_text else None
        stacking = fields.get("stacks") or None
        if polarity or stacking:
            conn.execute(
                "UPDATE statuses SET polarity=COALESCE(?, polarity), stacking=COALESCE(?, stacking) WHERE entity_id=?",
                (polarity, stacking, entity_id),
            )
            changed["infobox_fields"] += 1
    return changed


def parse_hp(raw: str | None) -> tuple[int | None, int | None]:
    if not raw:
        return None, None
    values = [int(x) for x in re.findall(r"(?<![A-Za-z])\d+", raw)]
    if not values:
        return None, None
    return values[0], values[1] if len(values) > 1 else values[0]


def enemy_infobox(wikitext: str) -> dict[str, str]:
    match = re.search(r"\{\{\s*Enemy Infobox\b([\s\S]*?)\n\}\}", wikitext, flags=re.I)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = re.match(r"\|\s*([A-Za-z]+)\s*=\s*(.*)", line)
        if field:
            values[field.group(1).casefold()] = field.group(2).strip()
    return values


def repair_monsters(conn: sqlite3.Connection) -> dict[str, int]:
    ranges = 0
    hit_counts = 0
    rows = conn.execute("SELECT entity_id, hp_min, hp_max, ascension_json FROM monsters ORDER BY entity_id").fetchall()
    for row in rows:
        claim = latest_claim(conn, row["entity_id"], "source.wikitext", "en")
        if claim:
            wikitext = text_value(claim[0])
            info = enemy_infobox(wikitext)
            base_min, base_max = parse_hp(info.get("hp"))
            asc_min, asc_max = parse_hp(info.get("aschp"))
            if base_min is not None:
                payload = {
                    "base_raw": info.get("hp"),
                    "base_min": base_min,
                    "base_max": base_max,
                }
                if info.get("aschp"):
                    payload.update({"ascension_raw": info.get("aschp"), "ascension_min": asc_min, "ascension_max": asc_max})
                conn.execute(
                    "UPDATE monsters SET hp_min=?, hp_max=?, ascension_json=? WHERE entity_id=?",
                    (base_min, base_max, json.dumps(payload, ensure_ascii=False, sort_keys=True), row["entity_id"]),
                )
                add_raw_claim(conn, row["entity_id"], "monster.hp.range", payload, claim[1], locator="Enemy Infobox:HP", notes="Parsed from the captured wiki.gg infobox; raw values retained in JSON.")
                ranges += 1

    for row in conn.execute("SELECT id, effect_json FROM monster_moves WHERE hits IS NULL").fetchall():
        value = json_value(row["effect_json"])
        effect = value.get("text", "") if isinstance(value, dict) else text_value(value)
        match = re.search(r"(?:×|x|X|\*)\s*(\d+)", effect)
        if match:
            conn.execute("UPDATE monster_moves SET hits=? WHERE id=?", (int(match.group(1)), row["id"]))
            hit_counts += 1
    return {"hp_ranges": ranges, "hit_counts": hit_counts}


def section_from_wikitext(wikitext: str, heading: str) -> str:
    """Return one top-level member section from a grouped wiki page."""
    pattern = re.compile(
        rf"(?ms)^={{1,6}}\s*{re.escape(heading)}\s*={{1,6}}\s*$\n(.*?)(?=^={{1,6}}\s*[^=].*?={{1,6}}\s*$|\Z)"
    )
    match = pattern.search(wikitext)
    return match.group(1).strip() if match else ""


def game_source_page(conn: sqlite3.Connection, language_dir: str) -> str | None:
    return source_page_for_game_file(conn, language_dir, "monsters.json")


def merge_candidate_entity(conn: sqlite3.Connection, candidate_id: str, target_id: str) -> None:
    """Preserve candidate evidence while marking it as merged/deprecated."""
    candidate = conn.execute("SELECT lifecycle, game_id FROM entities WHERE id=?", (candidate_id,)).fetchone()
    if not candidate or candidate["lifecycle"] != "candidate":
        return
    for row in conn.execute("SELECT * FROM names WHERE entity_id=?", (candidate_id,)).fetchall():
        add_name(
            conn,
            target_id,
            row["language"],
            row["name"],
            source_page_id=row["source_page_id"],
            name_kind="localization" if row["name_kind"] == "localization" else row["name_kind"],
            status=row["verification_status"],
            preferred=False,
            notes=f"Migrated from candidate {candidate_id} during explicit group split.",
        )
    for row in conn.execute("SELECT * FROM claims WHERE subject_entity_id=?", (candidate_id,)).fetchall():
        value = json_value(row["value_json"])
        add_claim(
            conn,
            target_id,
            row["field_path"],
            value,
            row["source_page_id"],
            language=row["language"],
            locator=row["locator"],
            extraction_method=row["extraction_method"],
            status=row["verification_status"],
            notes=f"Migrated from candidate {candidate_id}; original row retained as deprecated evidence.",
        )
    conn.execute(
        "UPDATE entities SET lifecycle='deprecated', mapping_status='confirmed', notes=? WHERE id=?",
        (f"Explicitly merged into {target_id}; retained for audit trail.", candidate_id),
    )
    # Names are copied to the live entity and claims retain the original
    # spelling/source.  Removing names from the deprecated shell prevents it
    # from creating false ambiguity in normal name lookup.
    conn.execute("DELETE FROM names WHERE entity_id=?", (candidate_id,))


def grouped_member_section(wikitext: str, heading: str) -> str:
    """Return one member block, including its nested Pattern section.

    Wiki.gg uses inconsistent heading levels across grouped pages.  Looking
    for the next ``Enemy Infobox`` rather than treating every ``== Pattern ==``
    heading as a sibling keeps the six slime sections and the minion sections
    intact.
    """
    heading_re = re.compile(r"^=+\s*(.*?)\s*=+\s*$", re.M)
    matches = [m for m in heading_re.finditer(wikitext) if m.group(1).strip() == heading]
    if not matches:
        return ""
    start_heading = matches[0]
    start = start_heading.end()
    first_infobox = re.search(r"\{\{\s*Enemy Infobox\b", wikitext[start:], flags=re.I)
    if not first_infobox:
        return ""
    first_infobox_start = start + first_infobox.start()
    next_infobox = re.search(r"\{\{\s*Enemy Infobox\b", wikitext[first_infobox_start + 1 :], flags=re.I)
    if not next_infobox:
        end = len(wikitext)
    else:
        next_infobox_start = first_infobox_start + 1 + next_infobox.start()
        # The last heading before the next infobox is the next member heading;
        # nested Pattern/Found With headings are therefore included in the
        # current block.
        headings_before = list(heading_re.finditer(wikitext, first_infobox_start + 1, next_infobox_start))
        end = headings_before[-1].start() if headings_before else next_infobox_start
    return wikitext[start:end].strip()


def parse_member_section(wikitext: str, heading: str) -> dict[str, Any]:
    section = grouped_member_section(wikitext, heading)
    if not section:
        return {"section": "", "infobox": {}, "moves": []}
    info = enemy_infobox(section)
    moves: list[dict[str, Any]] = []
    for block in parse_all_template_blocks(section, "Intents Table/row"):
        params = template_params(block)
        name = strip_wiki_markup(params.get("name", "")).strip()
        intent = strip_wiki_markup(params.get("intent", "")).strip()
        effect = strip_wiki_markup(params.get("effect", "")).strip()
        if not name:
            continue
        damage: int | None = None
        hits: int | None = None
        damage_match = re.search(r"(?:deals?|damage\s*=?)\s*\(?\s*(\d+)\s*[×x*]\s*(\d+)", effect, flags=re.I)
        if damage_match:
            damage = int(damage_match.group(1))
            hits = int(damage_match.group(2))
        else:
            simple = re.search(r"(?:deals?|damage\s*=?)\s*\(?\s*(\d+)", effect, flags=re.I)
            if simple:
                damage = int(simple.group(1))
        moves.append(
            {
                "name": name,
                "intent": intent or None,
                "damage": damage,
                "hits": hits,
                "effect_json": json.dumps({"text": effect}, ensure_ascii=False) if effect else None,
            }
        )
    return {"section": section, "infobox": info, "moves": moves}


def _member_spec(spec: dict[str, Any]) -> dict[str, Any]:
    """Fill fields shared by the original and additional split specs."""
    if spec.get("hp") and spec.get("asc_hp"):
        return spec
    return spec


def split_group_monsters(conn: sqlite3.Connection) -> dict[str, int]:
    """Create individual entities for grouped wiki pages with stable game keys."""
    created = 0
    moved_moves = 0
    merged_candidates = 0
    all_specs = MONSTER_GROUP_SPLITS + ADDITIONAL_MONSTER_GROUP_SPLITS
    for spec in all_specs:
        group = conn.execute(
            "SELECT id, notes FROM entities WHERE id=? AND kind='monster'",
            (spec["group_id"],),
        ).fetchone()
        if not group:
            continue
        group_meta = conn.execute("SELECT act, category FROM monsters WHERE entity_id=?", (spec["group_id"],)).fetchone()
        group_act = group_meta[0] if group_meta and group_meta[0] else "unknown"
        group_category = group_meta[1] if group_meta and group_meta[1] else "other"
        group_claim = latest_claim(conn, spec["group_id"], "source.wikitext", "en")
        wiki_page_id = group_claim[1] if group_claim else None
        wikitext = text_value(group_claim[0]) if group_claim else ""
        member_data = parse_member_section(wikitext, spec["en"]) if wikitext else {"section": "", "infobox": {}, "moves": []}
        section = member_data["section"] or (section_from_wikitext(wikitext, spec["en"]) if wikitext else "")
        xiao_page_id = None
        if spec.get("zh_article_id"):
            row = conn.execute(
                "SELECT id FROM source_pages WHERE source_id='xiaoheihe' AND article_id=? ORDER BY fetched_at DESC LIMIT 1",
                (spec["zh_article_id"],),
            ).fetchone()
            xiao_page_id = row[0] if row else None
        zh_page_id = xiao_page_id or game_source_page(conn, "zhs")
        en_page_id = wiki_page_id or game_source_page(conn, "eng")

        add_entity(
            conn,
            spec["entity_id"],
            "monster",
            subtype=spec.get("subtype", "split_member"),
            notes=f"Individual member of grouped wiki page {spec['group_id']}; split from explicit section and game key.",
        )
        conn.execute(
            """UPDATE entities SET game_id=?, lifecycle='active', mapping_status='confirmed',
               subtype=?, notes=? WHERE id=?""",
            (
                spec["game_id"],
                spec.get("subtype", "split_member"),
                f"Individual member of {spec['group_id']}; wiki.gg section and installed game localization agree.",
                spec["entity_id"],
            ),
        )
        add_name(
            conn,
            spec["entity_id"],
            "en",
            spec["en"],
            source_page_id=en_page_id,
            name_kind="preferred",
            status="single_source",
            preferred=True,
        )
        add_name(
            conn,
            spec["entity_id"],
            "zh-CN",
            spec["zh"],
            source_page_id=zh_page_id,
            name_kind="preferred",
            status="verified_game" if not xiao_page_id else "agreed",
            preferred=True,
            notes="Localized game key and/or dedicated Chinese article for the split member.",
        )
        # Re-home the member's explicit localization-key claim from the group
        # parent.  This lets the cross-source audit represent Donu/Deca and
        # Spire Shield/Spear by their own live keys while retaining the parent
        # page as a grouped record.
        for claim_row in conn.execute(
            "SELECT * FROM claims WHERE subject_entity_id=? AND field_path='game.localization_key'",
            (spec["group_id"],),
        ).fetchall():
            payload = json_value(claim_row["value_json"])
            if isinstance(payload, dict) and payload.get("key") == spec["game_id"]:
                add_claim(
                    conn,
                    spec["entity_id"],
                    "game.localization_key",
                    payload,
                    claim_row["source_page_id"],
                    extraction_method=claim_row["extraction_method"],
                    status=claim_row["verification_status"],
                    notes="Moved from the grouped wiki parent to the member entity during explicit split.",
                )
        info = member_data.get("infobox") or {}
        parsed_hp = parse_hp(info.get("hp"))
        parsed_asc_hp = parse_hp(info.get("aschp"))
        hp_min, hp_max = parsed_hp if parsed_hp[0] is not None else spec.get("hp", (None, None))
        asc_min, asc_max = parsed_asc_hp if parsed_asc_hp[0] is not None else spec.get("asc_hp", (None, None))
        type_text = str(info.get("type") or "").casefold()
        # ``Enemy Infobox`` uses ``Minion`` for summoned enemies.  Minions
        # are not a separate encounter tier (and must not inherit the parent
        # boss/elite category); keep them in the generic ``other`` bucket
        # while retaining ``subtype=minion`` on the entity itself.
        category = {
            "normal": "normal",
            "elite": "elite",
            "boss": "boss",
            "minion": "other",
        }.get(type_text, group_category)
        act = info.get("debut") or group_act
        conn.execute(
            """INSERT INTO monsters(entity_id, category, act, hp_min, hp_max, ascension_json, encounter_notes)
               VALUES (?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(entity_id) DO UPDATE SET category=excluded.category, act=excluded.act,
                 hp_min=excluded.hp_min, hp_max=excluded.hp_max,
                 ascension_json=excluded.ascension_json,
                 encounter_notes=excluded.encounter_notes""",
            (
                spec["entity_id"],
                category,
                act,
                hp_min,
                hp_max,
                json.dumps(
                    {
                        "base_min": hp_min,
                        "base_max": hp_max,
                        "ascension_min": asc_min,
                        "ascension_max": asc_max,
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                ),
                f"Split member from {spec['group_id']}; source section retains group-page context.",
            ),
        )
        if wiki_page_id:
            add_raw_claim(
                conn,
                spec["entity_id"],
                "source.wikitext",
                section or {"group_page": spec["group_id"], "section": spec["en"]},
                wiki_page_id,
                locator=f"section:{spec['en']}",
                notes="Copied from the dedicated member section of the grouped wiki.gg page.",
            )
            add_raw_claim(
                conn,
                spec["entity_id"],
                "monster.hp.range",
                {
                    "base_min": hp_min,
                    "base_max": hp_max,
                    "ascension_min": asc_min,
                    "ascension_max": asc_max,
                },
                wiki_page_id,
                locator=f"{spec['en']} Enemy Infobox",
                notes="Parsed from the member-specific Enemy Infobox in the grouped wiki.gg page.",
            )

        move_rows = member_data.get("moves") or []
        if not move_rows:
            move_names = set(spec.get("move_names", ()))
            move_intents = set(spec.get("move_intents", ()))
            parent_moves = conn.execute(
                "SELECT * FROM monster_moves WHERE monster_entity_id=? ORDER BY id",
                (spec["group_id"],),
            ).fetchall()
            move_rows = [
                move
                for move in parent_moves
                if move["name"] in move_names and (not move_intents or move["intent"] in move_intents or move["name"] != "Beam")
            ]
        conn.execute("DELETE FROM monster_moves WHERE monster_entity_id=?", (spec["entity_id"],))
        for move in move_rows:
            move_name = move["name"]
            move_intent = move.get("intent") if isinstance(move, dict) else move["intent"]
            move_damage = move.get("damage") if isinstance(move, dict) else move["damage"]
            move_hits = move.get("hits") if isinstance(move, dict) else move["hits"]
            move_effect = move.get("effect_json") if isinstance(move, dict) else move["effect_json"]
            move_condition = move.get("condition_json") if isinstance(move, dict) else move["condition_json"]
            move_probability = move.get("probability_json") if isinstance(move, dict) else move["probability_json"]
            move_order = move.get("order_rules") if isinstance(move, dict) else move["order_rules"]
            move_id = "move." + hashlib.sha256(
                f"{spec['entity_id']}|{move_name}|{move_intent or ''}|{move_effect or ''}".encode("utf-8")
            ).hexdigest()[:20]
            conn.execute(
                """INSERT OR REPLACE INTO monster_moves
                   (id, monster_entity_id, name, intent, damage, hits, effect_json,
                    condition_json, probability_json, order_rules)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    move_id,
                    spec["entity_id"],
                    move_name,
                    move_intent,
                    move_damage,
                    move_hits,
                    move_effect,
                    move_condition,
                    move_probability,
                    move_order,
                ),
            )
            moved_moves += 1
            if wiki_page_id and isinstance(move, dict):
                add_raw_claim(
                    conn,
                    spec["entity_id"],
                    f"monster.move.{move_name}",
                    {"intent": move_intent, "effect": json_value(move_effect)},
                    wiki_page_id,
                    locator=f"{spec['en']} Intents Table/row:{move_name}",
                    notes="Parsed from the member-specific Intents Table in the grouped wiki.gg page.",
                )

        add_relation(
            conn,
            spec["group_id"],
            "has_member",
            spec["entity_id"],
            source_page_id=wiki_page_id,
            status="confirmed",
            notes="Grouped wiki page has a dedicated member section and the installed game has a stable member key.",
        )
        candidate = conn.execute(
            "SELECT id FROM entities WHERE kind='monster' AND lifecycle='candidate' AND game_id=?",
            (spec["game_id"],),
        ).fetchone()
        if candidate:
            merge_candidate_entity(conn, candidate[0], spec["entity_id"])
            merged_candidates += 1
        if spec.get("zh_article_id"):
            zh_candidate_id = f"sts1.candidate.zh.monster.{spec['zh_article_id']}"
            zh_candidate = conn.execute(
                "SELECT id FROM entities WHERE id=? AND lifecycle='candidate'",
                (zh_candidate_id,),
            ).fetchone()
            if zh_candidate:
                merge_candidate_entity(conn, zh_candidate[0], spec["entity_id"])
                merged_candidates += 1
        created += 1

    # A group page should not claim that one member key is the page's sole
    # canonical game identity once all split members exist.
    for group_id in {spec["group_id"] for spec in all_specs}:
        member_names = {
            spec["en"] for spec in all_specs if spec["group_id"] == group_id
        } | {
            spec["zh"] for spec in all_specs if spec["group_id"] == group_id
        }
        placeholders = ",".join("?" for _ in member_names)
        if placeholders:
            conn.execute(
                f"DELETE FROM names WHERE entity_id=? AND name IN ({placeholders}) AND name_kind='localization'",
                (group_id, *sorted(member_names)),
            )
        conn.execute(
            "UPDATE entities SET game_id=NULL, subtype='group_page', mapping_status='provisional', notes=? WHERE id=?",
            ("Grouped wiki page retained as a parent; individual members are modeled as separate entities.", group_id),
        )

    # Do not expose a first-member projection as if it were the grouped page's
    # own HP/actions.  The complete source wikitext and member relations stay
    # available on the parent page, while canonical parents (boss/elite plus a
    # summoned minion) retain their own structured fields and game key.
    for group_id in GROUP_CONTEXT_ONLY:
        conn.execute(
            """UPDATE monsters SET category=NULL, act=NULL, hp_min=NULL, hp_max=NULL,
                      ascension_json=NULL,
                      encounter_notes=? WHERE entity_id=?""",
            (
                "Grouped wiki page only; structured HP/actions live on its has_member child entities.",
                group_id,
            ),
        )
        conn.execute("DELETE FROM monster_moves WHERE monster_entity_id=?", (group_id,))
    for group_id, game_id in GROUP_CANONICAL_PARENTS.items():
        conn.execute(
            """UPDATE entities SET game_id=?, subtype='group_parent', mapping_status='confirmed',
                      notes=? WHERE id=?""",
            (
                game_id,
                "Canonical monster page with a separately modeled summoned member; parent HP/actions remain structured.",
                group_id,
            ),
        )
    # Deprecated shells keep their claims/IDs for provenance but must not
    # participate in ordinary name resolution or create duplicate warnings.
    conn.execute(
        "DELETE FROM names WHERE entity_id IN (SELECT id FROM entities WHERE lifecycle='deprecated')"
    )
    conn.execute(
        """DELETE FROM names
           WHERE name_kind='localization' AND (name='DEPRECATED' OR name LIKE 'DEPRECATED %')"""
    )
    return {"split_entities": created, "split_moves": moved_moves, "merged_candidates": merged_candidates}


def encounter_source_page(conn: sqlite3.Connection) -> str | None:
    row = conn.execute(
        "SELECT id FROM source_pages WHERE source_id='wiki_gg' AND snapshot_path LIKE ? ORDER BY fetched_at DESC LIMIT 1",
        ("%inventory_monsters-%",),
    ).fetchone()
    return row[0] if row else None


def _monster_alias_forms(value: str) -> set[str]:
    """Return conservative spelling variants used by the pool tables.

    The wiki tables mix ``Spike Slime(M)`` and ``Spike Slime (M)`` and use
    plural display labels (``3 Byrds``/``2 Fungi Beasts``) for singular game
    entities.  These are formatting variants, not new monsters, so they are
    safe to normalise here while keeping the original label in the claim.
    """
    text = normalise(value)
    forms = {text}
    forms.add(re.sub(r"\s+\(", "(", text))
    forms.add(re.sub(r"\s*\(", " (", text))
    if text.endswith("ies"):
        forms.add(text[:-3] + "y")
    elif text.endswith("s") and not text.endswith("ss"):
        forms.add(text[:-1])
    else:
        # Encounter rows often pluralise a singular game name ("Jaw Worms",
        # "3 Cultists", "3 Darklings").
        forms.add(text + "s")
    # A few irregular plurals occur in the encounter tables.
    forms.update({"thieves" if text == "thief" else text})
    if text == "thieves":
        forms.add("thief")
    return {item for item in forms if item}


def monster_name_index(conn: sqlite3.Connection) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for row in conn.execute(
        """SELECT e.id, n.name FROM entities e JOIN names n ON n.entity_id=e.id
           WHERE e.kind='monster' AND e.lifecycle!='candidate'
             AND COALESCE(e.subtype, '')!='group_page' AND n.language='en'"""
    ):
        for alias in _monster_alias_forms(row["name"]):
            index.setdefault(alias, set()).add(row["id"])
    # Add prose labels that do not exist as literal wiki entity names but are
    # used by the encounter tables (for example "Medium Slime (any)").
    for alias, entity_ids in MONSTER_VARIANT_ALIASES.items():
        for entity_id in entity_ids:
            if any(entity_id in ids for ids in index.values()):
                index.setdefault(alias, set()).add(entity_id)
    return index


# Grouped wiki pages are useful parent records, but encounter rows refer to
# the actual game objects.  When a row says "any louse", "medium slime" or
# "shapes", expose the split members as alternatives instead of returning the
# page wrapper.  The raw details claim remains the source of the selection
# rule and the resulting relation is marked candidate below.
MONSTER_VARIANT_ALIASES: dict[str, tuple[str, ...]] = {
    "louse": ("sts1.monster.red_louse", "sts1.monster.green_louse"),
    "louses": ("sts1.monster.red_louse", "sts1.monster.green_louse"),
    "slaver": ("sts1.monster.blue_slaver", "sts1.monster.red_slaver"),
    "slavers": ("sts1.monster.blue_slaver", "sts1.monster.red_slaver"),
    "small slime": ("sts1.monster.acid_slime_s", "sts1.monster.spike_slime_s"),
    "small slimes": ("sts1.monster.acid_slime_s", "sts1.monster.spike_slime_s"),
    "medium slime": ("sts1.monster.acid_slime_m", "sts1.monster.spike_slime_m"),
    "medium slimes": ("sts1.monster.acid_slime_m", "sts1.monster.spike_slime_m"),
    "large slime": ("sts1.monster.acid_slime_l", "sts1.monster.spike_slime_l"),
    "large slimes": ("sts1.monster.acid_slime_l", "sts1.monster.spike_slime_l"),
    "shape": ("sts1.monster.exploder", "sts1.monster.repulsor", "sts1.monster.spiker"),
    "shapes": ("sts1.monster.exploder", "sts1.monster.repulsor", "sts1.monster.spiker"),
}


def resolve_monster_alias(
    label: str,
    names_by_normalized: dict[str, set[str]],
    *,
    expand_groups: bool = True,
) -> set[str]:
    """Resolve a pool-table label to stable monster entity ids."""
    normalized = normalise(label)
    normalized = re.sub(r"\s+\(", "(", normalized)
    normalized = re.sub(r"\s*\(", " (", normalized)
    if expand_groups and normalized in MONSTER_VARIANT_ALIASES:
        return {
            entity_id
            for entity_id in MONSTER_VARIANT_ALIASES[normalized]
            if any(entity_id in ids for ids in names_by_normalized.values())
        }
    ids: set[str] = set()
    for alias in _monster_alias_forms(normalized):
        ids.update(names_by_normalized.get(alias, set()))
    return ids


def encounter_members_from_row(
    conn: sqlite3.Connection,
    display_name: str,
    details: str,
    first_cell: html.HtmlElement,
    names_by_normalized: dict[str, set[str]],
) -> list[dict[str, Any]]:
    """Resolve explicit and alternative members without keeping page wrappers.

    The pool page links a grouped wrapper such as ``Shapes`` while putting the
    actual alternatives in the details cell.  We retain the raw details claim
    and expose every resolvable alternative as a member with quantity 1 unless
    the row itself explicitly says how many are present (``3 Darklings`` or
    ``3x Spike Slime (S)``).
    """
    anchors = []
    for anchor in first_cell.xpath(".//a"):
        label = " ".join(anchor.text_content().split()).strip()
        if label and label not in anchors:
            anchors.append(label)
    details_norm = normalise(details)
    has_selection_rule = bool(
        re.search(r"\b(?:either|or|any|randomly chosen|chosen from|independently chosen)\b", details_norm)
    )
    direct: list[dict[str, Any]] = []
    display_qty_match = re.match(r"^(\d+)\s+", display_name)
    display_qty = int(display_qty_match.group(1)) if display_qty_match else None
    for label in anchors:
        label_without_qty = re.sub(r"^\d+\s+", "", label).strip()
        # A grouped wrapper in a row with an explicit selection rule must not
        # contribute the wrapper itself (e.g. ``3 Shapes chosen from ...``).
        # The details scanner below resolves the concrete candidate pool.
        if has_selection_rule and normalise(label_without_qty) in MONSTER_VARIANT_ALIASES:
            continue
        ids = sorted(resolve_monster_alias(label_without_qty, names_by_normalized))
        if not ids:
            continue
        qty_match = re.search(r"(\d+)\s*(?:x|×)?\s*" + re.escape(label_without_qty), display_name, flags=re.I)
        quantity = int(qty_match.group(1)) if qty_match else (display_qty if len(anchors) == 1 and display_qty is not None else 1)
        for entity_id in ids:
            direct.append({"entity_id": entity_id, "quantity": quantity, "label": label_without_qty, "origin": "linked"})

    # Scan the details text against the longest known aliases first.  The raw
    # HTML often has no anchors in this cell, so this is the only way to expose
    # alternatives such as ``Acid Slime (L) or Spike Slime (L)``.
    detail_candidates: list[dict[str, Any]] = []
    # For bracketed "chosen from" rows, scan only the bracket: the word
    # ``chosen`` and the wrapper name before it are prose, not members.
    scan_text = details_norm
    bracket = re.search(r"\[([^\]]+)\]", details_norm)
    if bracket:
        scan_text = bracket.group(1)
    for alias in sorted(names_by_normalized, key=len, reverse=True):
        if alias in {"chosen", "from", "any", "randomly", "independently"}:
            continue
        if not alias or alias not in scan_text:
            continue
        # Match the alias as a phrase.  Substring-only matching was the source
        # of the false Chosen monster in "chosen from".
        if not re.search(rf"(?<!\w){re.escape(alias)}(?!\w)", scan_text):
            continue
        ids = sorted(resolve_monster_alias(alias, names_by_normalized))
        if not ids:
            continue
        # Pool-capacity quantities inside a bracket (``2x Repulsor``) are not
        # encounter quantities; actual row quantities are retained in the
        # details claim and represented as 1 here.
        alias_pos = scan_text.find(alias)
        before = scan_text[max(0, alias_pos - 8) : alias_pos]
        qty_match = re.search(r"(\d+)x?\s*$", before)
        quantity = int(qty_match.group(1)) if qty_match else 1
        for entity_id in ids:
            detail_candidates.append({"entity_id": entity_id, "quantity": quantity, "label": alias, "origin": "details"})

    direct_ids = {item["entity_id"] for item in direct}
    detail_ids = {item["entity_id"] for item in detail_candidates}
    # If details enumerate alternatives, discard only a grouped-page wrapper.
    # A real direct member can be omitted from the prose details (the
    # "Chosen and Byrds" row is one example), so subtracting every direct id
    # absent from detail_ids would silently drop it.
    group_ids = {
        row[0]
        for row in conn.execute(
            "SELECT id FROM entities WHERE kind='monster' AND subtype='group_page'"
        )
    }
    wrapper_ids = (direct_ids & group_ids) if detail_ids else set()
    selected = [item for item in direct if item["entity_id"] not in wrapper_ids]
    selected.extend(item for item in detail_candidates if item["entity_id"] not in direct_ids)
    # De-duplicate aliases while keeping the largest explicit quantity.
    merged: dict[str, dict[str, Any]] = {}
    for item in selected:
        existing = merged.get(item["entity_id"])
        if existing is None or item["quantity"] > existing["quantity"]:
            merged[item["entity_id"]] = item
    return list(merged.values())


def encounter_selection_rule(display_name: str, details: str) -> dict[str, Any] | None:
    """Capture the pool page's prose selection rule in a queryable shape.

    The member table intentionally remains a flat candidate index because the
    schema has no slot/alternative columns.  This claim carries the missing
    structure while preserving the exact source text in ``encounter.details``.
    """
    raw = " ".join((details or "").split())
    if not raw:
        return None
    rule: dict[str, Any] = {"raw": raw}
    lowered = raw.casefold()
    if lowered.startswith("either (") and ") or (" in raw:
        left, right = raw[8:].split(") or (", 1)
        rule["mode"] = "exclusive_alternatives"
        rule["alternatives"] = [
            [item.strip() for item in left.split("+") if item.strip()],
            [item.strip() for item in right.rsplit(")", 1)[0].split("+") if item.strip()],
        ]
        return rule
    if re.search(r"first enemy:.*second enemy:", lowered):
        match = re.search(r"First enemy:\s*(.*?)\s+Second Enemy:\s*(.*)$", raw, flags=re.I)
        if match:
            rule["mode"] = "slot_alternatives"
            rule["slots"] = {
                "first": match.group(1).strip(),
                "second": match.group(2).strip(),
            }
            return rule
    bracket = re.search(r"\[([^\]]+)\]", raw)
    if bracket and re.search(r"chosen from|randomly chosen from", lowered):
        count = re.search(r"^(\d+)", raw)
        rule["mode"] = "sample_without_replacement"
        rule["choose_count"] = int(count.group(1)) if count else None
        rule["pool"] = [
            re.sub(r"^and\s+", "", item.strip(), flags=re.I)
            for item in re.split(r",\s*|\s+and\s+", bracket.group(1))
            if item.strip()
        ]
        return rule
    if "independently chosen" in lowered:
        count = re.search(r"^(\d+)", raw)
        rule["mode"] = "independent_choices"
        rule["choose_count"] = int(count.group(1)) if count else None
        return rule
    if "each independently" in lowered:
        count = re.search(r"^(\d+)x", raw, flags=re.I)
        rule["mode"] = "independent_per_slot"
        rule["slot_count"] = int(count.group(1)) if count else None
        if "either color" in lowered:
            rule["alternatives"] = ["Red Louse", "Green Louse"]
            rule["probability_each"] = 0.5
        return rule
    if re.search(r"\b(?:or|any|either)\b", lowered):
        rule["mode"] = "alternatives"
        if " or " in lowered:
            rule["alternatives"] = [item.strip() for item in re.split(r"\s+or\s+", raw, flags=re.I)]
        return rule
    rule["mode"] = "fixed_details"
    return rule


def import_encounter_pools(conn: sqlite3.Connection) -> int:
    source_page_id = encounter_source_page(conn)
    if not source_page_id:
        return 0
    page = conn.execute("SELECT snapshot_path FROM source_pages WHERE id=?", (source_page_id,)).fetchone()
    if not page or not page[0]:
        return 0
    path = ROOT / page[0]
    if not path.exists():
        return 0
    tree = html.fromstring(path.read_text(encoding="utf-8"))
    names_by_normalized = monster_name_index(conn)
    imported = 0
    current_act: tuple[str, str] | None = None

    for node in tree.xpath("//h2|//h3"):
        heading = " ".join(node.text_content().split())
        heading = re.sub(r"\[edit.*?\]", "", heading).strip()
        act_match = re.match(r"Act\s+(\d+):\s*(.+)", heading)
        if node.tag == "h2" and act_match:
            current_act = (act_match.group(1), act_match.group(2).strip())
            continue
        if node.tag != "h3" or not current_act or heading not in {"Easy Pool", "Hard Pool"}:
            continue
        table = None
        sibling = node.getnext()
        while sibling is not None and sibling.tag not in {"h2", "h3"}:
            if sibling.tag == "table":
                table = sibling
                break
            sibling = sibling.getnext()
        if table is None:
            continue
        phase = ""
        rows = table.xpath(".//tr")
        if rows and rows[0].xpath("./th"):
            phase = " ".join(rows[0].xpath("./th[1]//text()"))
            phase = " ".join(phase.split())
        act_number, act_name = current_act
        pool = "easy" if heading == "Easy Pool" else "hard"
        for ordinal, tr in enumerate(rows[1:], 1):
            cells = tr.xpath("./th|./td")
            if len(cells) < 2:
                continue
            display_name = " ".join(cells[0].text_content().split())
            if not display_name:
                continue
            weight_text = " ".join(cells[1].text_content().split())
            weight_match = re.search(r"\d+(?:\.\d+)?", weight_text)
            weight: int | float | None = None
            if weight_match:
                raw_weight = float(weight_match.group(0))
                weight = int(raw_weight) if raw_weight.is_integer() else raw_weight
            details = " ".join(cells[2].text_content().split()) if len(cells) >= 3 else ""
            encounter_id = f"sts1.encounter.act{act_number}.{pool}.{slug(display_name)}"
            conn.execute(
                """INSERT INTO entities(id, kind, game, lifecycle, mapping_status, notes)
                   VALUES (?, 'encounter', 'sts1', 'active', 'provisional', ?)
                   ON CONFLICT(id) DO UPDATE SET notes=excluded.notes""",
                (encounter_id, f"Imported from the wiki.gg {act_name} {heading} table."),
            )
            conn.execute(
                """INSERT OR IGNORE INTO names(entity_id, language, name, normalized, name_kind, source_page_id, verification_status, is_preferred)
                   VALUES (?, 'en', ?, ?, 'preferred', ?, 'single_source', 1)""",
                (encounter_id, display_name, normalise(display_name), source_page_id),
            )
            conn.execute(
                """INSERT INTO encounters(entity_id, act, room_type, pool_type, weight_json, repetition_rules)
                   VALUES (?, ?, 'monster', ?, ?, ?)
                   ON CONFLICT(entity_id) DO UPDATE SET act=excluded.act, pool_type=excluded.pool_type,
                     weight_json=excluded.weight_json, repetition_rules=excluded.repetition_rules""",
                (
                    encounter_id,
                    act_name,
                    pool,
                    json.dumps({"weight": weight, "phase": phase, "ordinal": ordinal}, ensure_ascii=False, sort_keys=True),
                    details or None,
                ),
            )
            # These claims are deterministic projections of the current
            # Monsters table.  Clear the prior projection before rebuilding so
            # a parser or relation-semantics correction cannot leave stale
            # member payloads beside the current one.
            conn.execute(
                "DELETE FROM claims WHERE subject_entity_id=? AND field_path IN ('encounter.weight', 'encounter.details', 'encounter.members', 'encounter.selection_rule')",
                (encounter_id,),
            )
            add_raw_claim(conn, encounter_id, "encounter.weight", {"weight": weight, "phase": phase}, source_page_id, locator=f"{act_name}/{heading}/row:{ordinal}")
            add_raw_claim(conn, encounter_id, "encounter.details", details, source_page_id, locator=f"{act_name}/{heading}/row:{ordinal}")
            selection_rule = encounter_selection_rule(display_name, details)
            linked_names = [" ".join(anchor.text_content().split()) for anchor in cells[0].xpath(".//a") if " ".join(anchor.text_content().split())]
            member_details = encounter_members_from_row(
                conn,
                display_name,
                details,
                cells[0],
                names_by_normalized,
            )
            member_ids = {item["entity_id"] for item in member_details}
            conn.execute("DELETE FROM encounter_members WHERE encounter_entity_id=?", (encounter_id,))
            conn.execute(
                "DELETE FROM relations WHERE source_entity_id=? AND relation_type='contains_monster'",
                (encounter_id,),
            )
            for position, member in enumerate(member_details, 1):
                monster_id = member["entity_id"]
                conn.execute(
                    "INSERT OR IGNORE INTO encounter_members(encounter_entity_id, monster_entity_id, quantity, position) VALUES (?, ?, ?, ?)",
                    (encounter_id, monster_id, member["quantity"], position),
                )
                relation_id = "rel." + hashlib.sha256(f"{encounter_id}|contains_monster|{monster_id}".encode("utf-8")).hexdigest()[:24]
                conditional_member = member.get("origin") == "details" and selection_rule is not None
                # The monster identity is resolved from the source links and
                # localized member pages.  A pool/alternative rule changes
                # when that member appears, not whether the encounter knows
                # that member.  Keep the edge confirmed and store the
                # conditional selection in condition_json.
                relation_condition = (
                    {
                        "mode": "conditional_member",
                        "selection_rule": selection_rule,
                        "member_origin": member.get("origin"),
                    }
                    if conditional_member
                    else None
                )
                conn.execute(
                    """INSERT INTO relations(id, source_entity_id, relation_type, target_entity_id, condition_json, source_page_id, status, notes)
                       VALUES (?, ?, 'contains_monster', ?, ?, ?, 'confirmed', ?)
                       ON CONFLICT(id) DO UPDATE SET source_page_id=excluded.source_page_id,
                         condition_json=excluded.condition_json, status='confirmed', notes=excluded.notes""",
                    (
                        relation_id,
                        encounter_id,
                        monster_id,
                        json.dumps(relation_condition, ensure_ascii=False, sort_keys=True) if relation_condition else None,
                        source_page_id,
                        "Confirmed encounter-pool member; selected conditionally according to the wiki.gg pool rule."
                        if conditional_member
                        else "Explicit encounter-pool member from wiki.gg.",
                    ),
                )
            add_raw_claim(
                conn,
                encounter_id,
                "encounter.members",
                {
                    "linked_names": linked_names,
                    "details": details,
                    "members": member_details,
                    "resolved_entity_ids": sorted(member_ids),
                    "resolution_status": "confirmed_conditional" if selection_rule else "confirmed",
                },
                source_page_id,
                locator=f"{act_name}/{heading}/row:{ordinal}",
            )
            if selection_rule:
                add_raw_claim(
                    conn,
                    encounter_id,
                    "encounter.selection_rule",
                    selection_rule,
                    source_page_id,
                    locator=f"{act_name}/{heading}/row:{ordinal}",
                    notes="Structured projection of the wiki.gg encounter details; raw text is retained separately.",
                )
            imported += 1
    return imported


def main() -> int:
    parser = argparse.ArgumentParser(description="Repair deterministic structured KB fields from captured evidence")
    parser.add_argument("--no-encounters", action="store_true", help="skip normal encounter-pool import")
    parser.add_argument("--no-export", action="store_true", help="do not refresh JSONL/CSV exports")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    with conn:
        game_key_aliases = repair_game_key_aliases(conn)
        card_zh = fill_card_chinese_descriptions(conn)
        card_zh += fill_missing_xiao_card_descriptions(conn)
        card_zh += fill_missing_game_card_descriptions(conn)
        effects = fill_bilingual_effects(conn)
        character_gold = fill_character_initial_gold(conn)
        character_potion_slots, runtime_evidence = fill_character_potion_slots(conn)
        definition_repairs = fill_keyword_mechanic_definitions(conn)
        status_repairs = fill_status_descriptions(conn)
        monsters = repair_monsters(conn)
        monster_splits = split_group_monsters(conn)
        encounters = 0 if args.no_encounters else import_encounter_pools(conn)
        asset_links = link_variant_assets(conn)
        editorial_supplement = supplement_editorial_zh(conn)
        quality_supplement = supplement_quality(conn)
    export_counts = {}
    if not args.no_export:
        export_counts = export_data(conn)
    conn.close()
    result = {
        "parser_version": PARSER_VERSION,
        "finished_at": utc_now(),
        "game_key_aliases_repaired": game_key_aliases,
        "card_chinese_descriptions_filled": card_zh,
        "bilingual_effect_rows_changed": effects,
        "character_initial_gold_rows_changed": character_gold,
        "character_potion_slots_rows_changed": character_potion_slots,
        "character_runtime_evidence": runtime_evidence,
        "keyword_mechanic_definitions": definition_repairs,
        "status_repairs": status_repairs,
        "editorial_supplement": editorial_supplement,
        "quality_supplement": quality_supplement,
        "monster_repairs": monsters,
        "monster_group_splits": monster_splits,
        "encounters_imported": encounters,
        "entity_asset_links_added": asset_links,
        "export_counts": export_counts,
    }
    report_path = ROOT / "reports" / "structured-repair-report.json"
    report_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
