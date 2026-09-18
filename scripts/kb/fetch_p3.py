"""Fetch and stage the first P3 content slice for the bilingual StS1 KB.

P2 only records that an item appears in either source's directory.  This
module takes the next reversible step: it fetches the article evidence for
cards, relics and potions, parses the fields that are explicitly present, and
stores source-specific candidates in SQLite.  A Chinese row is merged into an
English entity only when an already reviewed ``inventory_mappings`` row says
``confirmed``.  Everything else remains a candidate so a translation guess
cannot silently become a bilingual fact.

The command is resumable.  Source URLs and content-addressed snapshots are
stable, and every claim is keyed by its source page.  No strategy document is
read or linked by this pipeline.

Usage (repository root)::

    $env:PYTHONIOENCODING='utf-8'
    python scripts/kb/fetch_p3.py                 # cards/relics/potions
    python scripts/kb/fetch_p3.py --all           # include events/monsters/... 
    python scripts/kb/fetch_p3.py --kinds card,relic --limit 20

The default run intentionally omits the later, more irregular enemy/event
parsers.  Their raw article pages can be collected with ``--all`` while the
structured tables remain conservative until their field grammar is reviewed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote, unquote, urlparse

from lxml import html

# The existing sample/discovery modules provide the audited request and
# snapshot helpers.  Importing them has no side effects because both have a
# main guard.
from bootstrap_sample import (  # type: ignore
    CHARACTERS,
    DB_PATH,
    ROOT,
    SCHEMA_PATH,
    WIKI_BASE,
    add_claim,
    add_entity,
    add_name,
    add_relation,
    add_resolution,
    apply_schema,
    article_text,
    export_data,
    get_or_fetch_page,
    json_text,
    normalise,
    parse_card_box,
    resolve_mapping_statuses,
    source_page_id,
    slug,
    utc_now,
)


PARSER_VERSION = "kb-p3-content/0.1"
XIAO_DELAY = 0.25
WIKI_DELAY = 0.8
DEFAULT_KINDS = ("card", "relic", "potion")
# ``character`` and ``concept`` are directory-only Chinese sections in the
# current Xiaoheihe snapshot.  They still deserve source claims, so they are
# valid targeted kinds even though no dedicated structured table is needed
# for the first pass.
ALL_KINDS = (
    "card", "relic", "potion", "event", "monster", "status", "keyword", "mechanic",
    "character", "concept",
)

COLOR_CHARACTER = {
    "Red": "ironclad",
    "Green": "silent",
    "Blue": "defect",
    "Purple": "watcher",
}
CHARACTER_IDS = {
    "ironclad": "sts1.character.ironclad",
    "silent": "sts1.character.silent",
    "defect": "sts1.character.defect",
    "watcher": "sts1.character.watcher",
}

# P1 used compact stable IDs for a few hand-curated samples.  Reuse those IDs
# when the full inventory reaches the same English source name, otherwise a
# harmless rerun would create a second “Ring of the Snake” or “Weak Potion”.
LEGACY_ENGLISH_IDS = {
    ("relic", "ring of the snake"): "sts1.relic.snake_ring",
    ("potion", "weak potion"): "sts1.potion.weak",
}


def clean_text(value: Any) -> str:
    return re.sub(r"\s+", " ", unescape(str(value or ""))).strip()


def title_from_url(url: str) -> str:
    """Return a MediaWiki title, excluding a fragment used by a list row."""
    parsed = urlparse(url)
    path = parsed.path
    if "/wiki/" in path:
        title = path.split("/wiki/", 1)[1]
    else:
        title = path.rsplit("/", 1)[-1]
    return unquote(title).replace("_", " ")


def kind_table(kind: str) -> str | None:
    return {
        "card": "cards",
        "relic": "relics",
        "potion": "potions",
        "monster": "monsters",
        "event": "events",
        "status": "statuses",
        "keyword": "keywords",
        "mechanic": "mechanics",
    }.get(kind)


def source_rows(conn: sqlite3.Connection, kind: str, language: str, *, refresh: bool = False) -> list[sqlite3.Row]:
    status_filter = "" if refresh else " AND status!='parsed'"
    return conn.execute(
        f"""SELECT * FROM inventory_items
           WHERE entity_kind=? AND language=? AND status!='excluded'{status_filter}
           ORDER BY id""",
        (kind, language),
    ).fetchall()


def existing_confirmed_entity(conn: sqlite3.Connection, zh_inventory_id: str) -> str | None:
    row = conn.execute(
        """SELECT evidence_json FROM inventory_mappings
           WHERE zh_inventory_id=? AND status='confirmed'
           ORDER BY id LIMIT 1""",
        (zh_inventory_id,),
    ).fetchone()
    if not row:
        return None
    try:
        evidence = json.loads(row[0] or "{}")
    except json.JSONDecodeError:
        return None
    entity_id = evidence.get("entity_id")
    if not entity_id:
        return None
    return entity_id if conn.execute("SELECT 1 FROM entities WHERE id=?", (entity_id,)).fetchone() else None


def english_entity_id(row: sqlite3.Row) -> str:
    kind = row["entity_kind"]
    name = row["name"]
    if kind == "card":
        character = row["character"]
        if not character:
            # Colorless, status and curse cards have no playable character.
            character = "colorless" if row["subcategory"] == "Colorless" else "other"
        suffix = f" ({character.title()})"
        base = name[:-len(suffix)] if name.endswith(suffix) else name
        return f"sts1.card.{character}.{slug(base)}"
    return f"sts1.{kind}.{slug(name)}"


def canonical_english_entity_id(conn: sqlite3.Connection, row: sqlite3.Row) -> str:
    key = (row["entity_kind"], normalise(row["name"]))
    legacy = LEGACY_ENGLISH_IDS.get(key)
    if legacy and conn.execute("SELECT 1 FROM entities WHERE id=?", (legacy,)).fetchone():
        return legacy
    # Prefer an existing exact English name when one is already present.  The
    # explicit legacy map above handles names whose P1 ID was intentionally
    # abbreviated or otherwise differs from the slug.
    matches = conn.execute(
        """SELECT DISTINCT e.id FROM entities e JOIN names n ON n.entity_id=e.id
           WHERE e.kind=? AND n.language='en' AND n.normalized=?
           ORDER BY e.id""",
        (row["entity_kind"], normalise(row["name"])),
    ).fetchall()
    if len(matches) == 1:
        return matches[0][0]
    return english_entity_id(row)


def chinese_candidate_id(row: sqlite3.Row) -> str:
    article_id = row["article_id"] or slug(row["name"])
    return f"sts1.candidate.zh.{row['entity_kind']}.{slug(str(article_id))}"


def parse_template_block(text: str, template_name: str) -> str | None:
    """Extract one balanced ``{{Template ...}}`` body from wikitext."""
    marker = "{{" + template_name
    start = text.casefold().find(marker.casefold())
    if start < 0:
        return None
    cursor = start + 2
    depth = 0
    i = start
    while i < len(text) - 1:
        pair = text[i : i + 2]
        if pair == "{{":
            depth += 1
            i += 2
            continue
        if pair == "}}":
            depth -= 1
            i += 2
            if depth == 0:
                return text[cursor:i - 2]
            continue
        i += 1
    return None


def parse_all_template_blocks(text: str, template_name: str) -> list[str]:
    """Return all balanced templates with the requested name."""
    marker = "{{" + template_name
    result: list[str] = []
    offset = 0
    while True:
        found = text.casefold().find(marker.casefold(), offset)
        if found < 0:
            break
        cursor = found + 2
        depth = 0
        i = found
        end = None
        while i < len(text) - 1:
            pair = text[i : i + 2]
            if pair == "{{":
                depth += 1
                i += 2
                continue
            if pair == "}}":
                depth -= 1
                i += 2
                if depth == 0:
                    end = i - 2
                    break
                continue
            i += 1
        if end is None:
            break
        result.append(text[cursor:end])
        offset = end + 2
    return result


def template_params(body: str | None) -> dict[str, str]:
    if body is None:
        return {}
    params: dict[str, str] = {}
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|") or "=" not in line:
            continue
        key, value = line[1:].split("=", 1)
        params[key.strip().casefold()] = value.strip()
    return params


def strip_wiki_markup(value: str) -> str:
    """Make a readable candidate while retaining icon meaning when known."""
    value = re.sub(r"<!--.*?-->", "", value, flags=re.S)
    # Common StS wiki templates.  Values are deliberately editorial display
    # text; the untouched wikitext claim remains the authoritative evidence.
    def template_repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        parts = [part.strip() for part in inner.split("|")]
        name = parts[0].casefold()
        if name in {"icon", "relicicon"} and len(parts) > 1:
            return "能量" if parts[1].casefold() in {"re", "energy"} else parts[1]
        if name in {"kw", "bd", "c", "r", "p", "m", "e", "int", "q", "querylink", "frame"}:
            return parts[-1] if parts[-1] else (parts[1] if len(parts) > 1 else "")
        if name == "asc":
            return parts[-1] if len(parts) > 1 else ""
        return parts[-1] if len(parts) > 1 else ""

    # Nested templates are removed from the inside out.  A few pages contain
    # deep condition templates; ten passes cover them without trying to be a
    # full wikitext renderer.
    for _ in range(10):
        updated = re.sub(r"\{\{([^{}]*)\}\}", template_repl, value)
        if updated == value:
            break
        value = updated
    value = re.sub(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]", lambda m: m.group(2) or m.group(1), value)
    value = re.sub(r"\[https?://[^ ]+ ([^\]]+)\]", r"\1", value)
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"'{2,5}", "", value)
    return re.sub(r"\s+", " ", unescape(value)).strip()


def parse_infobox(wikitext: str, names: Iterable[str]) -> dict[str, str]:
    for name in names:
        params = template_params(parse_template_block(wikitext, name))
        if params:
            return {key: strip_wiki_markup(value) for key, value in params.items()}
    return {}


def parse_wiki_page(wikitext: str, title: str) -> dict[str, Any]:
    card = parse_infobox(wikitext, ("Card Infobox",))
    relic = parse_infobox(wikitext, ("Relic Infobox",))
    potion = parse_infobox(wikitext, ("Potion Infobox",))
    enemy = parse_infobox(wikitext, ("Enemy Infobox",))
    event = parse_infobox(wikitext, ("Event Infobox",))
    power = parse_infobox(wikitext, ("Power Infobox",))
    payload: dict[str, Any] = {
        "title": title,
        "card": card,
        "relic": relic,
        "potion": potion,
        "enemy": enemy,
        "event": event,
        "power": power,
    }
    if card:
        payload["description"] = card.get("description")
    elif relic:
        payload["description"] = relic.get("description")
    elif potion:
        payload["description"] = potion.get("description")
    elif enemy:
        payload["description"] = enemy.get("hp") or enemy.get("type")
    elif event:
        payload["description"] = event.get("description")
    elif power:
        payload["description"] = power.get("description")
    return payload


def parse_list_box(box: html.HtmlElement, kind: str) -> dict[str, Any]:
    name = clean_text(box.get("data-name"))
    hrefs = box.xpath('.//a[@href][1]/@href')
    href = WIKI_BASE + hrefs[0] if hrefs and hrefs[0].startswith("/") else (hrefs[0] if hrefs else "")
    desc_cls = {
        "relic": "relic-desc",
        "potion": "potion-desc",
    }.get(kind)
    description = ""
    flavor = ""
    if desc_cls:
        nodes = box.xpath(f'.//*[contains(concat(" ", normalize-space(@class), " "), " {desc_cls} ")]')
        if nodes:
            description = clean_text(nodes[0].text_content())
        flavor_nodes = box.xpath('.//*[contains(concat(" ", normalize-space(@class), " "), " relic-flavor ") or contains(concat(" ", normalize-space(@class), " "), " potion-flavor ")]')
        if flavor_nodes:
            flavor = clean_text(flavor_nodes[0].text_content())
    images = box.xpath('.//span[contains(@class,"img-base")]//img[1]/@src')
    return {
        "name": name,
        "href": href,
        "rarity": box.get("data-rarity"),
        "character": box.get("data-character"),
        "description": description,
        "flavor": flavor,
        "tags": [x for x in (box.get("data-tags") or "").split() if x],
        "image": images[0] if images else None,
    }


def load_compendium(conn: sqlite3.Connection, kind: str) -> dict[str, dict[str, Any]]:
    page_name = {"card": "Cards_List", "relic": "Relics_List", "potion": "Potions_List"}.get(kind)
    if not page_name:
        return {}
    row = conn.execute("SELECT snapshot_path FROM source_pages WHERE url=?", (f"{WIKI_BASE}/wiki/{page_name}",)).fetchone()
    if not row or not row[0]:
        return {}
    path = ROOT / row[0]
    if not path.exists():
        return {}
    tree = html.fromstring(path.read_bytes())
    cls = {"card": "card-box", "relic": "relic-box", "potion": "potion-box"}[kind]
    parsed: dict[str, dict[str, Any]] = {}
    for box in tree.xpath(f'//div[contains(concat(" ", normalize-space(@class), " "), " {cls} ")]'):
        if kind == "card":
            value = parse_card_box(box)
            links = box.xpath('.//a[@href][1]/@href')
            value["href"] = WIKI_BASE + links[0] if links and links[0].startswith("/") else (links[0] if links else "")
        else:
            value = parse_list_box(box, kind)
        if value.get("href"):
            parsed[value["href"].split("#", 1)[0]] = value
    return parsed


def api_batches(rows: list[sqlite3.Row], batch_size: int = 20) -> Iterable[list[sqlite3.Row]]:
    for i in range(0, len(rows), batch_size):
        yield rows[i : i + batch_size]


def fetch_api_batch(conn: sqlite3.Connection, rows: list[sqlite3.Row], kind: str, ordinal: int) -> tuple[str, dict[str, str], dict[str, Any]]:
    titles = [title_from_url(row["url"]) for row in rows]
    title_param = "|".join(title.replace(" ", "_") for title in titles)
    url = (
        WIKI_BASE
        + "/api.php?action=query&format=json&formatversion=1&titles="
        + quote(title_param, safe="|_(),!'")
        + "&prop=revisions&rvprop=content|ids&rvslots=main"
    )
    page_id, body, text = get_or_fetch_page(conn, "wiki_gg", url, f"p3_{kind}_{ordinal:03d}")
    conn.execute(
        "UPDATE source_pages SET title=?, parser_version=? WHERE id=?",
        (f"P3 wiki.gg API batch: {kind} {ordinal}", PARSER_VERSION, page_id),
    )
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"wiki.gg API returned invalid JSON for {kind} batch {ordinal}: {exc}") from exc
    pages = payload.get("query", {}).get("pages", {})
    by_title: dict[str, str] = {}
    revisions: dict[str, Any] = {}
    for value in pages.values():
        title = clean_text(value.get("title"))
        page_wikitext = ""
        revisions_list = value.get("revisions") or []
        if revisions_list:
            slot = revisions_list[0].get("slots", {}).get("main", {})
            page_wikitext = slot.get("*") or slot.get("content") or ""
        if title:
            by_title[title.casefold()] = page_wikitext
            revisions[title.casefold()] = value
    return page_id, by_title, revisions


def ensure_card_row(conn: sqlite3.Connection, entity_id: str, row: sqlite3.Row, box: dict[str, Any] | None) -> None:
    metadata = json.loads(row["metadata_json"] or "{}")
    color = (box or {}).get("color") or row["subcategory"] or "Other"
    card_type = (box or {}).get("type") or metadata.get("type") or "Other"
    allowed_colors = {"Red", "Green", "Blue", "Purple", "Colorless", "Status", "Curse", "Other"}
    allowed_types = {"Attack", "Skill", "Power", "Status", "Curse", "Other"}
    character_id = CHARACTER_IDS.get(row["character"] or COLOR_CHARACTER.get(color))
    conn.execute(
        """INSERT INTO cards(entity_id, character_entity_id, color, card_type, rarity, target, availability, tags_json)
           VALUES (?, ?, ?, ?, ?, NULL, 'card_list', ?)
           ON CONFLICT(entity_id) DO UPDATE SET character_entity_id=COALESCE(excluded.character_entity_id, cards.character_entity_id),
             color=excluded.color, card_type=excluded.card_type, rarity=excluded.rarity,
             availability=COALESCE(excluded.availability, cards.availability), tags_json=excluded.tags_json""",
        (
            entity_id,
            character_id,
            color if color in allowed_colors else "Other",
            card_type if card_type in allowed_types else "Other",
            (box or {}).get("rarity") or metadata.get("rarity"),
            json_text((box or {}).get("tags") or metadata.get("tags") or []),
        ),
    )
    if character_id:
        add_relation(conn, entity_id, "belongs_to_character", character_id, status="confirmed")


def numeric_cost(value: Any) -> tuple[str, float | None]:
    text = clean_text(value)
    if text.casefold() == "x":
        return "x", None
    if text in {"", "-", "—", "unplayable"}:
        return "unplayable" if text.casefold() == "unplayable" else "unknown", None
    try:
        return "fixed", float(text)
    except ValueError:
        return "conditional" if text else "unknown", None


def ensure_card_variant(
    conn: sqlite3.Connection,
    entity_id: str,
    variant_kind: str,
    description: str | None,
    cost: Any,
    source_page_id: str,
    *,
    source_kind: str = "structured_html",
) -> str:
    variant_id = f"{entity_id}:{variant_kind}"
    level = 0 if variant_kind == "base" else 1
    conn.execute(
        """INSERT INTO entity_variants(id, entity_id, variant_kind, level, label)
           VALUES (?, ?, ?, ?, ?)
           ON CONFLICT(id) DO UPDATE SET label=excluded.label, level=excluded.level""",
        (variant_id, entity_id, variant_kind, level, "Base" if variant_kind == "base" else "Upgraded"),
    )
    cost_type, cost_value = numeric_cost(cost)
    conn.execute(
        """INSERT INTO card_variants(variant_id, cost_type, cost_value, description_en, parsed_json, image_asset_id)
           VALUES (?, ?, ?, ?, NULL, NULL)
           ON CONFLICT(variant_id) DO UPDATE SET cost_type=excluded.cost_type,
             cost_value=excluded.cost_value, description_en=COALESCE(excluded.description_en, card_variants.description_en)""",
        (variant_id, cost_type, cost_value, description),
    )
    if description:
        claim_id = add_claim(
            conn,
            entity_id,
            "card.description",
            description,
            source_page_id,
            variant_id=variant_id,
            language="en" if source_kind == "structured_html" else "zh-CN",
            extraction_method=source_kind,
            status="single_source",
        )
        # Keep the first explicit list value as the provisional display value;
        # later wikitext claims remain available for field-level comparison.
        if source_kind == "structured_html":
            # Older parser runs could lose icon-only energy markup and leave
            # ``Gain .`` in the claim.  Keep those historical claims for
            # auditability, but mark them as superseded when a corrected
            # description for the same source/variant is now available.
            conn.execute(
                """UPDATE claims
                   SET notes=CASE
                       WHEN notes IS NULL OR notes='' THEN 'superseded: icon-only text recovered by kb-p3-content/0.1'
                       ELSE notes || '; superseded: icon-only text recovered by kb-p3-content/0.1'
                   END
                   WHERE subject_entity_id=? AND variant_id=? AND field_path='card.description'
                     AND source_page_id=? AND (value_json LIKE '%Gain .%' OR value_json LIKE '%Deal .%')
                     AND id != ?""",
                (entity_id, variant_id, source_page_id, claim_id),
            )
            add_resolution(conn, entity_id, "card.description", claim_id, description, variant_id=variant_id)
    cost_claim = add_claim(
        conn,
        entity_id,
        "card.cost",
        clean_text(cost),
        source_page_id,
        variant_id=variant_id,
        language="en" if source_kind == "structured_html" else "zh-CN",
        extraction_method=source_kind,
        status="single_source",
    )
    if source_kind == "structured_html":
        add_resolution(conn, entity_id, "card.cost", cost_claim, clean_text(cost), variant_id=variant_id)
    return variant_id


def first_number(value: str | None) -> int | None:
    if not value:
        return None
    match = re.search(r"(?<![A-Za-z])\d+(?:\.\d+)?", value)
    if not match:
        return None
    try:
        number = float(match.group(0))
    except ValueError:
        return None
    return int(number) if number.is_integer() else int(number)


def parse_event_options(wikitext: str) -> list[dict[str, Any]]:
    """Extract the explicit option labels and summaries from ``== Options ==``.

    Event pages use ``Frame`` templates for option buttons and free text for
    their effects.  Restricting the scan to the Options section avoids
    treating dialogue buttons (Continue, Leave, and so on) as choices.  The
    full wikitext claim remains the source of truth; these summaries are
    conservative structured candidates.
    """
    match = re.search(r"^==\s*Options\s*==\s*$([\s\S]*?)(?=^==[^=]|\Z)", wikitext, flags=re.I | re.M)
    if not match:
        return []
    section = match.group(1)
    frames = list(re.finditer(r"\{\{\s*Frame\s*\|\s*([^{}|]+?)\s*\}\}", section, flags=re.I))
    options: list[dict[str, Any]] = []
    for index, frame in enumerate(frames, 1):
        label = strip_wiki_markup(frame.group(1))
        if not label:
            continue
        end = frames[index].start() if index < len(frames) else len(section)
        raw = section[frame.end():end]
        text = strip_wiki_markup(raw).strip(" -*\n\t")
        # Bullets immediately following an option are conditions or details;
        # preserving them in the JSON keeps review possible without guessing
        # which sentence is a cost versus an outcome.
        condition = None
        if re.search(r"\b(?:only|appears|replaces|floor|ascension|if|when)\b|仅在|替换|楼层|进阶", text, flags=re.I):
            condition = {"text": text}
        cost_match = re.findall(
            r"(?:become\s+cursed[^.]*|cursed\s*[-–—][^.]*|lose\s+[^.]*|pay\s+[^.]*|you\s+can\s+no\s+longer\s+[^.]*|无法再[^。]*|失去[^。]*|支付[^。]*|诅咒[^。]*)",
            text,
            flags=re.I,
        )
        cost_text = "; ".join(dict.fromkeys(x.strip(" .。") for x in cost_match if x.strip()))
        outcome_text = text
        if cost_text:
            for fragment in cost_match:
                outcome_text = outcome_text.replace(fragment, "")
            outcome_text = re.sub(r"\s+", " ", outcome_text).strip(" .。")
        options.append({
            "ordinal": index,
            "label": label,
            "summary": outcome_text or text,
            "condition": condition,
            "cost": {"text": cost_text} if cost_text else None,
        })
    return options


def upsert_structured_noncard(
    conn: sqlite3.Connection,
    entity_id: str,
    row: sqlite3.Row,
    wikitext: str,
    source_page_id: str,
    kind: str,
    stats: Counter,
) -> None:
    """Populate conservative tables for the irregular P3 categories.

    The parser only adopts fields explicitly named by wiki.gg templates.  The
    complete wikitext remains a claim, so a missing template field is visible
    as NULL rather than a model-filled value.
    """
    info = parse_wiki_page(wikitext, row["name"])
    if kind == "monster":
        enemy = info.get("enemy") or {}
        hp = first_number(enemy.get("hp"))
        asc_hp = first_number(enemy.get("aschp"))
        category = row["subcategory"] if row["subcategory"] in {"normal", "elite", "boss"} else "other"
        conn.execute(
            """INSERT INTO monsters(entity_id, category, act, hp_min, hp_max, ascension_json, encounter_notes)
               VALUES (?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(entity_id) DO UPDATE SET category=COALESCE(excluded.category, monsters.category),
                 act=COALESCE(excluded.act, monsters.act), hp_min=COALESCE(excluded.hp_min, monsters.hp_min),
                 hp_max=COALESCE(excluded.hp_max, monsters.hp_max), ascension_json=COALESCE(excluded.ascension_json, monsters.ascension_json)""",
            (entity_id, category, enemy.get("debut"), hp, hp, json_text({"asc_hp": asc_hp}) if asc_hp is not None else None, None),
        )
        for block in parse_all_template_blocks(wikitext, "Intents Table/row"):
            params = template_params(block)
            move_name = strip_wiki_markup(params.get("name", ""))
            effect = strip_wiki_markup(params.get("effect", ""))
            if not move_name:
                continue
            damage = first_number(effect) if re.search(r"\bdamage\b", effect, flags=re.I) else None
            move_id = "move." + hashlib.sha256(f"{entity_id}|{move_name}|{effect}".encode("utf-8")).hexdigest()[:20]
            conn.execute(
                """INSERT INTO monster_moves(id, monster_entity_id, name, intent, damage, hits, effect_json, condition_json, probability_json, order_rules)
                   VALUES (?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL)
                   ON CONFLICT(id) DO UPDATE SET intent=excluded.intent, damage=excluded.damage,
                     hits=excluded.hits, effect_json=excluded.effect_json""",
                (move_id, entity_id, move_name, strip_wiki_markup(params.get("intent", "")) or None, damage, None, json_text({"text": effect}) if effect else None),
            )
            add_claim(conn, entity_id, f"monster.move.{move_name}", {"intent": strip_wiki_markup(params.get("intent", "")), "effect": effect}, source_page_id, language="en", extraction_method="wikitext", status="single_source", locator=f"Intents Table/row:{move_name}")
        stats["structured"] += 1 if enemy else 0
    elif kind == "event":
        event = info.get("event") or {}
        acts = row["subcategory"] or None
        conn.execute(
            """INSERT INTO events(entity_id, acts_json, room_type, notes)
               VALUES (?, ?, 'unknown', ?)
               ON CONFLICT(entity_id) DO UPDATE SET acts_json=COALESCE(excluded.acts_json, events.acts_json), notes=COALESCE(excluded.notes, events.notes)""",
            (entity_id, json_text({"source_category": acts}) if acts else None, event.get("description")),
        )
        options = parse_event_options(wikitext)
        if options:
            # Parsed option IDs are namespaced so a later parser revision can
            # coexist with an older raw claim while keeping reruns idempotent.
            conn.execute("DELETE FROM event_options WHERE event_entity_id=? AND id LIKE 'event_option.%'", (entity_id,))
            for option in options:
                option_id = "event_option." + hashlib.sha256(
                    f"{entity_id}|{option['ordinal']}|{option['label']}|{option['summary']}".encode("utf-8")
                ).hexdigest()[:20]
                conn.execute(
                    """INSERT INTO event_options
                       (id, event_entity_id, ordinal, label, condition_json, cost_json, outcome_json, locked_when_json)
                       VALUES (?, ?, ?, ?, ?, ?, ?, NULL)
                       ON CONFLICT(id) DO UPDATE SET label=excluded.label,
                         condition_json=excluded.condition_json, cost_json=excluded.cost_json,
                         outcome_json=excluded.outcome_json""",
                    (
                        option_id,
                        entity_id,
                        option["ordinal"],
                        option["label"],
                        json_text(option["condition"]) if option["condition"] else None,
                        json_text(option["cost"]) if option["cost"] else None,
                        json_text({"text": option["summary"]}) if option["summary"] else None,
                    ),
                )
                add_claim(
                    conn,
                    entity_id,
                    f"event.option.{option['ordinal']}",
                    {"label": option["label"], "text": option["summary"]},
                    source_page_id,
                    language="en",
                    extraction_method="wikitext",
                    status="single_source",
                    locator=f"Options/Frame:{option['label']}",
                )
        stats["structured"] += 1 if event else 0
    elif kind == "status":
        power = info.get("power") or {}
        type_value = (power.get("type") or "").casefold()
        polarity = "positive" if "buff" in type_value else "negative" if "debuff" in type_value else "neutral"
        conn.execute(
            """INSERT INTO statuses(entity_id, polarity, affects, stacking, trigger_timing, removal)
               VALUES (?, ?, ?, ?, NULL, NULL)
               ON CONFLICT(entity_id) DO UPDATE SET polarity=COALESCE(excluded.polarity, statuses.polarity),
                 affects=COALESCE(excluded.affects, statuses.affects), stacking=COALESCE(excluded.stacking, statuses.stacking)""",
            (entity_id, polarity, power.get("gives to player") or power.get("gives to enemy"), power.get("stacks")),
        )
        if power.get("description"):
            add_claim(conn, entity_id, "status.description", power["description"], source_page_id, language="en", extraction_method="wikitext", status="single_source")
        stats["structured"] += 1 if power else 0
    elif kind in {"keyword", "mechanic"}:
        table = "keywords" if kind == "keyword" else "mechanics"
        column = "definition_json"
        conn.execute(f"INSERT INTO {table}(entity_id, {column}) VALUES (?, ?) ON CONFLICT(entity_id) DO UPDATE SET {column}=COALESCE(excluded.{column}, {table}.{column})", (entity_id, json_text({"source_page": row["url"], "definition": info.get("description")})))
        stats["structured"] += 1


def article_segments(text: str) -> list[dict[str, Any]]:
    """Extract heading/image/caption triplets from a Xiaoheihe article."""
    try:
        tree = html.fromstring(text)
    except Exception:
        return []
    root_nodes = tree.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " article-content ")]')
    root = root_nodes[0] if root_nodes else tree
    segments: list[dict[str, Any]] = []
    headings = root.xpath(".//h1")
    # Article sections are often nested in a div after the first heading, so
    # sibling-only traversal misses the upgrade block.  Use document order
    # and stop at the next heading instead.
    all_nodes = list(root.iter())
    positions = {id(node): index for index, node in enumerate(all_nodes)}
    for index, heading in enumerate(headings):
        title = clean_text(heading.text_content())
        start = positions.get(id(heading), 0) + 1
        end = positions.get(id(headings[index + 1]), len(all_nodes)) if index + 1 < len(headings) else len(all_nodes)
        descendants = all_nodes[start:end]
        images: list[str] = []
        captions: list[str] = []
        # Keep only the outermost nodes in the slice.  Otherwise a parent
        # ``div`` and each of its children would duplicate the same caption.
        descendant_set = {id(node) for node in descendants}
        text_parts: list[str] = []
        for node in descendants:
            if any(id(parent) in descendant_set for parent in node.iterancestors()):
                continue
            images.extend(node.xpath('.//img/@data-original | .//img/@src'))
            captions.extend(node.xpath('.//*[contains(concat(" ", normalize-space(@class), " "), " img-desc ")]//text()'))
            text_parts.extend(node.xpath('.//text()[not(ancestor::h1)]'))
            if node.tail:
                text_parts.append(node.tail)
        # Xiaoheihe frequently leaves the actual card sentence in a plain
        # paragraph after an image, while ``img-desc`` is only a placeholder.
        # Include both forms and suppress the known placeholder caption.
        caption = clean_text(" ".join(text_parts + captions))
        caption = caption.replace("请输入图片描述", "").strip()
        segments.append({"title": title, "description": caption, "images": [x for x in images if x]})
    return segments


def upsert_english_entity(
    conn: sqlite3.Connection,
    row: sqlite3.Row,
    api_page_id: str,
    wikitext: str,
    revisions: dict[str, Any],
    list_box: dict[str, Any] | None,
    kind: str,
    stats: Counter,
) -> str:
    entity_id = canonical_english_entity_id(conn, row)
    add_entity(conn, entity_id, kind, subtype=row["subcategory"], notes="P3 English source candidate; identity is source-backed and may await Chinese mapping.")
    # Existing P1 sample cards use a concise display name (Strike) while the
    # list source retains the disambiguating parenthetical.  Preserve both.
    preferred_name = row["name"]
    if kind == "card":
        suffix = f" ({(row['character'] or '').title()})"
        if suffix and preferred_name.endswith(suffix):
            add_name(conn, entity_id, "en", preferred_name[: -len(suffix)], source_page_id=api_page_id, preferred=True, status="single_source")
            add_name(conn, entity_id, "en", preferred_name, source_page_id=api_page_id, name_kind="source_name", preferred=False, status="single_source")
        else:
            add_name(conn, entity_id, "en", preferred_name, source_page_id=api_page_id, preferred=True, status="single_source")
    else:
        add_name(conn, entity_id, "en", preferred_name, source_page_id=api_page_id, preferred=True, status="single_source")

    if kind == "card":
        ensure_card_row(conn, entity_id, row, list_box)
        if list_box:
            can_upgrade = bool(list_box.get("can_upgrade"))
            card_info = parse_wiki_page(wikitext, row["name"]).get("card", {})
            # ``0`` is a real upgraded cost.  Do not use a truthiness fallback
            # here: older sample rows used the base cost whenever the
            # wikitext explicitly said ``CostPlus = 0``.
            base_cost = list_box.get("cost") if list_box.get("cost") not in (None, "") else card_info.get("cost")
            upgrade_cost = card_info.get("costplus") if card_info.get("costplus") not in (None, "") else base_cost
            ensure_card_variant(conn, entity_id, "base", list_box.get("description_base"), base_cost, api_page_id)
            if can_upgrade and list_box.get("description_upgrade") is not None:
                ensure_card_variant(conn, entity_id, "upgrade", list_box.get("description_upgrade"), upgrade_cost, api_page_id)
            for field, value in {
                "card.rarity": list_box.get("rarity"),
                "card.type": list_box.get("type"),
                "card.color": list_box.get("color"),
                "card.tags": list_box.get("tags"),
            }.items():
                if value not in (None, ""):
                    claim_id = add_claim(conn, entity_id, field, value, api_page_id, language="en", extraction_method="structured_html", status="single_source")
                    add_resolution(conn, entity_id, field, claim_id, value)
            if list_box.get("images"):
                add_claim(conn, entity_id, "source.image_urls", list_box["images"], api_page_id, language="en", extraction_method="structured_html", status="single_source")
        stats["structured"] += 1 if list_box else 0
    elif kind in {"relic", "potion"}:
        info = parse_wiki_page(wikitext, row["name"])
        box = list_box or {}
        info_box = info.get(kind) or {}
        table = "relics" if kind == "relic" else "potions"
        rarity = box.get("rarity") or info_box.get("rarity") or row["subcategory"]
        char_name = box.get("character") or info_box.get("character")
        char_id = CHARACTER_IDS.get((char_name or "").casefold())
        if kind == "relic":
            conn.execute(
                """INSERT INTO relics(entity_id, rarity, character_entity_id, effect_json)
                   VALUES (?, ?, ?, ?)
                   ON CONFLICT(entity_id) DO UPDATE SET rarity=COALESCE(excluded.rarity, relics.rarity),
                     character_entity_id=COALESCE(excluded.character_entity_id, relics.character_entity_id),
                     effect_json=COALESCE(excluded.effect_json, relics.effect_json)""",
                (entity_id, rarity, char_id, json_text({"description_en": box.get("description") or info_box.get("description"), "flavor": box.get("flavor")})),
            )
            field = "relic.effect"
        else:
            conn.execute(
                """INSERT INTO potions(entity_id, rarity, character_entity_id, effect_json)
                   VALUES (?, ?, ?, ?)
                   ON CONFLICT(entity_id) DO UPDATE SET rarity=COALESCE(excluded.rarity, potions.rarity),
                     character_entity_id=COALESCE(excluded.character_entity_id, potions.character_entity_id),
                     effect_json=COALESCE(excluded.effect_json, potions.effect_json)""",
                (entity_id, rarity, char_id, json_text({"description_en": box.get("description") or info_box.get("description"), "flavor": box.get("flavor")})),
            )
            field = "potion.effect"
        effect = box.get("description") or info_box.get("description")
        if effect:
            claim_id = add_claim(conn, entity_id, field, effect, api_page_id, language="en", extraction_method="structured_html" if box.get("description") else "wikitext", status="single_source")
            add_resolution(conn, entity_id, field, claim_id, effect)
        if box.get("image"):
            add_claim(conn, entity_id, "source.image_urls", [box["image"]], api_page_id, language="en", extraction_method="structured_html")
        stats["structured"] += 1 if (box.get("description") or info_box.get("description")) else 0
    elif kind in {"event", "monster", "status", "keyword", "mechanic"}:
        upsert_structured_noncard(conn, entity_id, row, wikitext, api_page_id, kind, stats)

    # The complete page remains evidence even when a field parser did not
    # understand a template.  A locator makes batch API snapshots auditable.
    if wikitext:
        add_claim(
            conn,
            entity_id,
            "source.wikitext",
            wikitext,
            api_page_id,
            language="en",
            locator=f"page:{row['name']}",
            extraction_method="wikitext",
            status="single_source",
            notes="Raw MediaWiki body from a P3 batch snapshot; retain for re-parsing and conflict review.",
        )
        info = parse_wiki_page(wikitext, row["name"])
        if info.get("description"):
            add_claim(conn, entity_id, "source.infobox.description", info["description"], api_page_id, language="en", extraction_method="wikitext", status="single_source")
    stats["parsed"] += 1
    return entity_id


def upsert_chinese_entity(
    conn: sqlite3.Connection,
    row: sqlite3.Row,
    page_id: str,
    text: str,
    kind: str,
    stats: Counter,
) -> str:
    confirmed_entity_id = existing_confirmed_entity(conn, row["id"])
    candidate_id = chinese_candidate_id(row)
    if confirmed_entity_id and confirmed_entity_id != candidate_id:
        merge_confirmed_candidate(conn, candidate_id, confirmed_entity_id)
    entity_id = confirmed_entity_id or candidate_id
    merged = bool(confirmed_entity_id)
    # A confirmed mapping already has an English subtype (for example card
    # type or relic rarity).  The Chinese directory's generic filter label
    # such as “全部” must never overwrite it.
    add_entity(conn, entity_id, kind, subtype=None if merged else row["subcategory"], notes=("P3 Chinese article candidate; mapping not yet reviewed." if not merged else None))
    if not merged:
        conn.execute("UPDATE entities SET lifecycle='candidate' WHERE id=?", (entity_id,))
    add_name(
        conn,
        entity_id,
        "zh-CN",
        row["name"],
        source_page_id=page_id,
        preferred=True,
        status="single_source",
        notes=None if merged else "Source-specific candidate; do not infer an English identity from the name alone.",
    )
    raw_text = article_text(html.fromstring(text)) if text else ""
    add_claim(conn, entity_id, "source.article_text", raw_text, page_id, language="zh-CN", extraction_method="visible_text", status="single_source")
    add_claim(conn, entity_id, "source.title_text", clean_text(row["name"]), page_id, language="zh-CN", extraction_method="manual", status="single_source")
    segments = article_segments(text)
    images = sorted({url for segment in segments for url in segment["images"]})
    if images:
        add_claim(conn, entity_id, "source.image_urls", images, page_id, language="zh-CN", extraction_method="visible_text", status="single_source")
    if kind == "card":
        # A candidate card still gets a queryable shell; unknown color/type are
        # represented by the schema's explicit Other value, never by guessed
        # zeros or a machine translation.
        char_id = CHARACTER_IDS.get(row["character"] or "")
        conn.execute(
            """INSERT INTO cards(entity_id, character_entity_id, color, card_type, rarity, availability, tags_json)
               VALUES (?, ?, 'Other', 'Other', NULL, 'xiaoheihe_candidate', '[]')
               ON CONFLICT(entity_id) DO UPDATE SET character_entity_id=COALESCE(excluded.character_entity_id, cards.character_entity_id)""",
            (entity_id, char_id),
        )
        if char_id:
            add_relation(conn, entity_id, "belongs_to_character", char_id, status="candidate", source_page_id=page_id)
        useful = [segment for segment in segments if segment["description"] and "请输入图片描述" not in segment["description"]]
        # Keep a base variant shell even when the Chinese page stores the
        # card sentence only inside an image.  The values remain unknown until
        # OCR/visual review; omitting the row would make the card structurally
        # indistinguishable from a non-card article.
        base_variant_id = f"{entity_id}:base"
        conn.execute(
            """INSERT OR IGNORE INTO entity_variants(id, entity_id, variant_kind, level, label)
               VALUES (?, ?, 'base', 0, 'Base')""",
            (base_variant_id, entity_id),
        )
        conn.execute("INSERT OR IGNORE INTO card_variants(variant_id, cost_type) VALUES (?, 'unknown')", (base_variant_id,))
        for index, segment in enumerate(useful[:2]):
            variant = "upgrade" if index == 1 or segment["title"].endswith("+") else "base"
            # Do not overwrite an English display description with Chinese
            # source text; this is a candidate claim for later mapping review.
            variant_id = f"{entity_id}:{variant}"
            conn.execute(
                """INSERT OR IGNORE INTO entity_variants(id, entity_id, variant_kind, level, label)
                   VALUES (?, ?, ?, ?, ?)""",
                (variant_id, entity_id, variant, 1 if variant == "upgrade" else 0, "Upgraded" if variant == "upgrade" else "Base"),
            )
            conn.execute("INSERT OR IGNORE INTO card_variants(variant_id, cost_type) VALUES (?, 'unknown')", (variant_id,))
            add_claim(conn, entity_id, "card.description", segment["description"], page_id, variant_id=variant_id, language="zh-CN", extraction_method="visible_text", status="single_source")
    elif kind == "relic":
        descriptions = [segment["description"] for segment in segments if segment["description"] and "请输入图片描述" not in segment["description"]]
        effect = descriptions[0] if descriptions else raw_text[:500]
        if not merged:
            conn.execute(
                """INSERT INTO relics(entity_id, effect_json) VALUES (?, ?)
                   ON CONFLICT(entity_id) DO UPDATE SET effect_json=COALESCE(relics.effect_json, excluded.effect_json)""",
                (entity_id, json_text({"description_zh": effect}) if effect else None),
            )
        if effect:
            add_claim(conn, entity_id, "relic.effect", effect, page_id, language="zh-CN", extraction_method="visible_text", status="single_source")
    elif kind == "potion":
        descriptions = [segment["description"] for segment in segments if segment["description"] and "请输入图片描述" not in segment["description"]]
        effect = descriptions[0] if descriptions else raw_text[:500]
        if not merged:
            conn.execute(
                """INSERT INTO potions(entity_id, effect_json) VALUES (?, ?)
                   ON CONFLICT(entity_id) DO UPDATE SET effect_json=COALESCE(potions.effect_json, excluded.effect_json)""",
                (entity_id, json_text({"description_zh": effect}) if effect else None),
            )
        if effect:
            add_claim(conn, entity_id, "potion.effect", effect, page_id, language="zh-CN", extraction_method="visible_text", status="single_source")
    elif kind == "event":
        if not merged:
            conn.execute(
                """INSERT INTO events(entity_id, acts_json, room_type, notes)
                   VALUES (?, ?, 'unknown', ?)
                   ON CONFLICT(entity_id) DO UPDATE SET acts_json=COALESCE(events.acts_json, excluded.acts_json), notes=COALESCE(events.notes, excluded.notes)""",
                (entity_id, json_text({"source_category": row["subcategory"]}) if row["subcategory"] else None, raw_text[:500] or None),
            )
    elif kind == "monster":
        category = row["subcategory"] if row["subcategory"] in {"normal", "elite", "boss"} else "other"
        if not merged:
            conn.execute(
                """INSERT INTO monsters(entity_id, category, encounter_notes)
                   VALUES (?, ?, ?)
                   ON CONFLICT(entity_id) DO UPDATE SET category=COALESCE(monsters.category, excluded.category), encounter_notes=COALESCE(monsters.encounter_notes, excluded.encounter_notes)""",
                (entity_id, category, raw_text[:500] or None),
            )
    elif kind == "status":
        if not merged:
            conn.execute(
                """INSERT INTO statuses(entity_id, polarity, affects)
                   VALUES (?, 'neutral', 'unknown')
                   ON CONFLICT(entity_id) DO NOTHING""",
                (entity_id,),
            )
    elif kind == "keyword":
        conn.execute(
            """INSERT INTO keywords(entity_id, definition_json)
               VALUES (?, ?)
               ON CONFLICT(entity_id) DO UPDATE SET definition_json=COALESCE(excluded.definition_json, keywords.definition_json)""",
            (entity_id, json_text({"source_article_text": raw_text[:1000]})),
        )
    elif kind == "mechanic":
        conn.execute(
            """INSERT INTO mechanics(entity_id, definition_json)
               VALUES (?, ?)
               ON CONFLICT(entity_id) DO UPDATE SET definition_json=COALESCE(excluded.definition_json, mechanics.definition_json)""",
            (entity_id, json_text({"source_article_text": raw_text[:1000]})),
        )
    stats["parsed"] += 1
    stats["merged"] += 1 if merged else 0
    return entity_id


def update_inventory_status(conn: sqlite3.Connection, item_id: str, status: str, **metadata: Any) -> None:
    row = conn.execute("SELECT metadata_json FROM inventory_items WHERE id=?", (item_id,)).fetchone()
    current: dict[str, Any] = {}
    if row:
        try:
            current = json.loads(row[0] or "{}")
        except json.JSONDecodeError:
            current = {}
    current.setdefault("p3", {}).update(metadata)
    conn.execute("UPDATE inventory_items SET status=?, metadata_json=? WHERE id=?", (status, json_text(current), item_id))


def _english_entity_by_name(
    conn: sqlite3.Connection,
    kind: str,
    name: str,
    *,
    character_id: str | None = None,
) -> str | None:
    """Resolve a source-page English name without guessing across roles."""

    rows = conn.execute(
        """SELECT DISTINCT e.id
           FROM entities e JOIN names n ON n.entity_id=e.id
           WHERE e.kind=? AND n.language='en' AND n.normalized=?
           ORDER BY e.id""",
        (kind, normalise(name)),
    ).fetchall()
    if character_id:
        rows = [
            row for row in rows
            if conn.execute(
                "SELECT 1 FROM cards WHERE entity_id=? AND character_entity_id=?",
                (row[0], character_id),
            ).fetchone()
        ]
    return rows[0][0] if len(rows) == 1 else None


def _character_section_nodes(tree: html.HtmlElement) -> list[html.HtmlElement]:
    root_nodes = tree.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " mw-parser-output ")]')
    return list(root_nodes[0]) if root_nodes else []


def enrich_characters(conn: sqlite3.Connection) -> None:
    """Populate the character table from the four audited wiki.gg pages.

    The character directory is not duplicated on wiki.gg's card/relic lists,
    so this enrichment runs independently of inventory mappings.  It only
    adopts values visible in the source page: starting HP (including its
    Ascension 14 variant), starting relic, and starting deck quantities.
    """

    for key, info in CHARACTERS.items():
        url = f"{WIKI_BASE}/wiki/{key.title() if key != 'ironclad' else 'Ironclad'}"
        page_id = source_page_id("wiki_gg", url)
        page = conn.execute("SELECT snapshot_path FROM source_pages WHERE id=?", (page_id,)).fetchone()
        if not page or not page[0]:
            continue
        path = ROOT / page[0]
        if not path.exists():
            continue
        try:
            tree = html.fromstring(path.read_bytes())
            nodes = _character_section_nodes(tree)
            infobox = tree.xpath('.//div[contains(concat(" ", normalize-space(@class), " "), " druid-row-MaxHealth ")]//div[contains(concat(" ", normalize-space(@class), " "), " druid-data-MaxHealth ")]')
            hp_text = " ".join(infobox[0].itertext()) if infobox else ""
            hp_numbers = [int(value) for value in re.findall(r"\b\d+\b", hp_text)]
            max_hp = {"base": hp_numbers[0]} if hp_numbers else {}
            if len(hp_numbers) >= 2:
                max_hp["ascension_14"] = hp_numbers[1]

            starting_relic_name: str | None = None
            starting_deck: list[dict[str, Any]] = []
            for index, node in enumerate(nodes):
                if node.tag not in {"h2", "h3"}:
                    continue
                heading = re.sub(r"\s*\[.*?\]", "", " ".join(node.itertext())).strip().casefold()
                if heading == "starting relic" and index + 1 < len(nodes):
                    links = nodes[index + 1].xpath('.//a[@href and not(contains(@href, "Ascension"))]')
                    if links:
                        starting_relic_name = " ".join(links[0].itertext()).strip() or links[0].get("title")
                if heading == "starting deck" and index + 1 < len(nodes):
                    for item in nodes[index + 1].xpath(".//li"):
                        links = item.xpath('.//a[@href]')
                        if not links:
                            continue
                        card_name = " ".join(links[0].itertext()).strip() or links[0].get("title") or ""
                        count_text = " ".join(item.itertext())
                        quantities = re.findall(r"\bx(\d+)\b", count_text, flags=re.I)
                        starting_deck.append({"name": card_name, "quantity": int(quantities[0]) if quantities else 1})

            character_id = info["id"]
            relic_id = _english_entity_by_name(conn, "relic", starting_relic_name or "") if starting_relic_name else None
            for item in starting_deck:
                item["entity_id"] = _english_entity_by_name(conn, "card", item["name"], character_id=character_id)
            deck_json = starting_deck or None
            conn.execute(
                """INSERT INTO characters(entity_id, initial_hp, starting_relic_entity_id, starting_deck_json, resource_json)
                   VALUES (?, ?, ?, ?, ?)
                   ON CONFLICT(entity_id) DO UPDATE SET
                     initial_hp=COALESCE(excluded.initial_hp, characters.initial_hp),
                     starting_relic_entity_id=COALESCE(excluded.starting_relic_entity_id, characters.starting_relic_entity_id),
                     starting_deck_json=COALESCE(excluded.starting_deck_json, characters.starting_deck_json),
                     resource_json=COALESCE(excluded.resource_json, characters.resource_json)""",
                (character_id, max_hp.get("base"), relic_id, json_text(deck_json) if deck_json else None, json_text({"max_hp": max_hp}) if max_hp else None),
            )
            if max_hp:
                claim_id = add_claim(conn, character_id, "character.max_hp", max_hp, page_id, locator="infobox.MaxHealth", language="en", extraction_method="structured_html", status="single_source")
                add_resolution(conn, character_id, "character.max_hp", claim_id, max_hp)
            if starting_relic_name:
                value = {"name": starting_relic_name, "entity_id": relic_id}
                claim_id = add_claim(conn, character_id, "character.starting_relic", value, page_id, locator="section.Starting_Relic", language="en", extraction_method="structured_html", status="single_source")
                add_resolution(conn, character_id, "character.starting_relic", claim_id, value)
                if relic_id:
                    add_relation(conn, character_id, "starts_with_relic", relic_id, source_page_id=page_id, status="confirmed")
            if deck_json:
                claim_id = add_claim(conn, character_id, "character.starting_deck", deck_json, page_id, locator="section.Starting_Deck", language="en", extraction_method="structured_html", status="single_source")
                add_resolution(conn, character_id, "character.starting_deck", claim_id, deck_json)
                for item in deck_json:
                    if item.get("entity_id"):
                        add_relation(
                            conn,
                            character_id,
                            "starting_deck_contains",
                            item["entity_id"],
                            source_page_id=page_id,
                            status="confirmed",
                            condition={"quantity": item["quantity"]},
                        )
        except (OSError, ValueError, IndexError) as exc:
            print(f"[character-warning] {url}: {exc}", file=sys.stderr)


def consolidate_legacy_duplicates(conn: sqlite3.Connection) -> None:
    """Fold duplicate IDs produced by the pre-canonical P3 smoke run.

    This is deliberately limited to the two known P1/P3 collisions.  It does
    not merge any Chinese candidate, because source-specific candidates with
    the same translation are intentionally allowed until human review.
    """
    pairs = (
        ("sts1.relic.ring_of_the_snake", "sts1.relic.snake_ring"),
        ("sts1.potion.weak_potion", "sts1.potion.weak"),
    )
    for duplicate, target in pairs:
        if not conn.execute("SELECT 1 FROM entities WHERE id=?", (duplicate,)).fetchone():
            continue
        if not conn.execute("SELECT 1 FROM entities WHERE id=?", (target,)).fetchone():
            conn.execute("UPDATE entities SET id=? WHERE id=?", (target, duplicate))
            continue
        # Preserve any non-empty fields in the canonical one-row table.
        kind = conn.execute("SELECT kind FROM entities WHERE id=?", (target,)).fetchone()[0]
        table = kind_table(kind)
        if table:
            target_row = conn.execute(f"SELECT * FROM {table} WHERE entity_id=?", (target,)).fetchone()
            duplicate_row = conn.execute(f"SELECT * FROM {table} WHERE entity_id=?", (duplicate,)).fetchone()
            if target_row and duplicate_row:
                for column in target_row.keys():
                    if column == "entity_id" or target_row[column] not in (None, "") or duplicate_row[column] in (None, ""):
                        continue
                    conn.execute(f"UPDATE {table} SET {column}=? WHERE entity_id=?", (duplicate_row[column], target))
                conn.execute(f"DELETE FROM {table} WHERE entity_id=?", (duplicate,))
            elif duplicate_row:
                conn.execute(f"UPDATE {table} SET entity_id=? WHERE entity_id=?", (target, duplicate))
        # Names and claims are evidence and can be transferred without
        # guessing; duplicate rows are ignored by their natural keys.
        for row in conn.execute("SELECT language,name,normalized,name_kind,source_page_id,verification_status,is_preferred,notes FROM names WHERE entity_id=?", (duplicate,)).fetchall():
            conn.execute(
                "INSERT OR IGNORE INTO names(entity_id,language,name,normalized,name_kind,source_page_id,verification_status,is_preferred,notes) VALUES (?,?,?,?,?,?,?,?,?)",
                (target, *row),
            )
        conn.execute("UPDATE claims SET subject_entity_id=? WHERE subject_entity_id=?", (target, duplicate))
        conn.execute("UPDATE resolutions SET subject_entity_id=? WHERE subject_entity_id=?", (target, duplicate))
        # A duplicate relation has no extra meaning once the same object is
        # canonical; dropping just those rows avoids a unique-key collision.
        conn.execute("DELETE FROM relations WHERE source_entity_id=? OR target_entity_id=?", (duplicate, duplicate))
        conn.execute("DELETE FROM entity_assets WHERE entity_id=?", (duplicate,))
        conn.execute("DELETE FROM entities WHERE id=?", (duplicate,))


def merge_confirmed_candidate(conn: sqlite3.Connection, source_id: str, target_id: str) -> None:
    """Move an already-collected Chinese candidate onto a reviewed entity.

    Mapping decisions are separate from parsing.  Once a human confirms a
    pair, a later Chinese refresh must not leave two copies of the same object
    or discard the candidate's source claims.  The canonical English
    structured row wins when both sides have one; source evidence is retained.
    """
    if source_id == target_id or not conn.execute("SELECT 1 FROM entities WHERE id=?", (source_id,)).fetchone():
        return
    target = conn.execute("SELECT kind FROM entities WHERE id=?", (target_id,)).fetchone()
    source = conn.execute("SELECT kind FROM entities WHERE id=?", (source_id,)).fetchone()
    if not target or not source or target[0] != source[0]:
        raise ValueError(f"cannot merge entities with different kinds: {source_id} -> {target_id}")
    kind = source[0]

    for row in conn.execute(
        "SELECT language,name,normalized,name_kind,source_page_id,verification_status,is_preferred,notes FROM names WHERE entity_id=?",
        (source_id,),
    ).fetchall():
        conn.execute(
            """INSERT OR IGNORE INTO names
               (entity_id,language,name,normalized,name_kind,source_page_id,verification_status,is_preferred,notes)
               VALUES (?,?,?,?,?,?,?,?,?)""",
            (target_id, *row),
        )
    conn.execute("DELETE FROM names WHERE entity_id=?", (source_id,))

    if kind == "card":
        source_variants = conn.execute("SELECT * FROM entity_variants WHERE entity_id=? ORDER BY level,id", (source_id,)).fetchall()
        for variant in source_variants:
            target_variant = conn.execute(
                """SELECT id FROM entity_variants WHERE entity_id=? AND variant_kind=?
                   ORDER BY level,id LIMIT 1""",
                (target_id, variant["variant_kind"]),
            ).fetchone()
            if target_variant:
                conn.execute("UPDATE claims SET variant_id=? WHERE variant_id=?", (target_variant[0], variant["id"]))
                conn.execute("UPDATE resolutions SET variant_id=? WHERE variant_id=?", (target_variant[0], variant["id"]))
                conn.execute("DELETE FROM card_variants WHERE variant_id=?", (variant["id"],))
                conn.execute("DELETE FROM entity_assets WHERE entity_id=? AND variant_id=?", (source_id, variant["id"]))
                conn.execute("DELETE FROM entity_variants WHERE id=?", (variant["id"],))
            else:
                conn.execute("UPDATE entity_variants SET entity_id=? WHERE id=?", (target_id, variant["id"]))
        conn.execute("DELETE FROM cards WHERE entity_id=?", (source_id,))

    table = {"relic": "relics", "potion": "potions", "monster": "monsters", "event": "events", "status": "statuses", "keyword": "keywords", "mechanic": "mechanics"}.get(kind)
    if table:
        target_row = conn.execute(f"SELECT 1 FROM {table} WHERE entity_id=?", (target_id,)).fetchone()
        if target_row:
            conn.execute(f"DELETE FROM {table} WHERE entity_id=?", (source_id,))
        else:
            conn.execute(f"UPDATE {table} SET entity_id=? WHERE entity_id=?", (target_id, source_id))
    if kind == "monster":
        if conn.execute("SELECT 1 FROM monsters WHERE entity_id=?", (target_id,)).fetchone():
            conn.execute("DELETE FROM monster_moves WHERE monster_entity_id=?", (source_id,))
        else:
            conn.execute("UPDATE monster_moves SET monster_entity_id=? WHERE monster_entity_id=?", (target_id, source_id))
    if kind == "event":
        if conn.execute("SELECT 1 FROM events WHERE entity_id=?", (target_id,)).fetchone():
            conn.execute("DELETE FROM event_options WHERE event_entity_id=?", (source_id,))
        else:
            conn.execute("UPDATE event_options SET event_entity_id=? WHERE event_entity_id=?", (target_id, source_id))

    conn.execute("UPDATE claims SET subject_entity_id=? WHERE subject_entity_id=?", (target_id, source_id))
    conn.execute("UPDATE resolutions SET subject_entity_id=? WHERE subject_entity_id=?", (target_id, source_id))
    for relation in conn.execute("SELECT * FROM relations WHERE source_entity_id=? OR target_entity_id=?", (source_id, source_id)).fetchall():
        new_source = target_id if relation["source_entity_id"] == source_id else relation["source_entity_id"]
        new_target = target_id if relation["target_entity_id"] == source_id else relation["target_entity_id"]
        if new_source != new_target:
            add_relation(
                conn,
                new_source,
                relation["relation_type"],
                new_target,
                source_page_id=relation["source_page_id"],
                status=relation["status"],
                condition=json.loads(relation["condition_json"]) if relation["condition_json"] else None,
                notes=relation["notes"],
            )
    conn.execute("DELETE FROM relations WHERE source_entity_id=? OR target_entity_id=?", (source_id, source_id))
    for asset in conn.execute("SELECT entity_id,asset_id,variant_id,role FROM entity_assets WHERE entity_id=?", (source_id,)).fetchall():
        conn.execute("INSERT OR IGNORE INTO entity_assets(entity_id,asset_id,variant_id,role) VALUES (?,?,?,?)", (target_id, asset["asset_id"], asset["variant_id"], asset["role"]))
    conn.execute("DELETE FROM entity_assets WHERE entity_id=?", (source_id,))
    conn.execute("DELETE FROM entities WHERE id=?", (source_id,))


def process_english(conn: sqlite3.Connection, kinds: list[str], limit: int | None, report: dict[str, Any], *, refresh: bool = False) -> None:
    for kind in kinds:
        rows = source_rows(conn, kind, "en", refresh=refresh)
        if limit:
            rows = rows[:limit]
        boxes = load_compendium(conn, kind)
        stats = report["english"][kind]
        for ordinal, batch in enumerate(api_batches(rows), 1):
            try:
                page_id, by_title, revisions = fetch_api_batch(conn, batch, kind, ordinal)
                for row in batch:
                    title = title_from_url(row["url"])
                    text = by_title.get(title.casefold(), "")
                    if not text:
                        # API normalisation can change punctuation/spacing;
                        # fall back to a unique page ending in the title.
                        matches = [value for key, value in by_title.items() if key.replace("_", " ") == title.casefold()]
                        text = matches[0] if len(matches) == 1 else ""
                    if not text:
                        update_inventory_status(conn, row["id"], "failed", error="API page missing", fetched_at=utc_now())
                        stats["failed"] += 1
                        continue
                    base_url = row["url"].split("#", 1)[0]
                    box = boxes.get(base_url)
                    upsert_english_entity(conn, row, page_id, text, revisions.get(title.casefold(), {}), box, kind, stats)
                    update_inventory_status(conn, row["id"], "parsed", source_page_id=page_id, fetched_at=utc_now())
                    stats["fetched"] += 1
                conn.commit()
            except Exception as exc:
                for row in batch:
                    update_inventory_status(conn, row["id"], "failed", error=str(exc), failed_at=utc_now())
                    stats["failed"] += 1
                conn.commit()
                print(f"[p3-wiki-warning] {kind} batch {ordinal}: {exc}", file=sys.stderr)
            time.sleep(WIKI_DELAY)


def process_chinese(conn: sqlite3.Connection, kinds: list[str], limit: int | None, report: dict[str, Any], *, refresh: bool = False) -> None:
    for kind in kinds:
        rows = source_rows(conn, kind, "zh-CN", refresh=refresh)
        if limit:
            rows = rows[:limit]
        stats = report["chinese"][kind]
        for index, row in enumerate(rows, 1):
            try:
                page_id, _, text = get_or_fetch_page(conn, "xiaoheihe", row["url"], f"p3_{kind}_{row['article_id']}", is_xiao=True)
                conn.execute("UPDATE source_pages SET parser_version=? WHERE id=?", (PARSER_VERSION, page_id))
                upsert_chinese_entity(conn, row, page_id, text, kind, stats)
                update_inventory_status(conn, row["id"], "parsed", source_page_id=page_id, fetched_at=utc_now())
                stats["fetched"] += 1
                if index % 25 == 0:
                    conn.commit()
                    print(f"[p3-xiao] {kind}: {index}/{len(rows)}", flush=True)
            except Exception as exc:
                update_inventory_status(conn, row["id"], "failed", error=str(exc), failed_at=utc_now())
                stats["failed"] += 1
                print(f"[p3-xiao-warning] {kind} {row['name']} ({row['article_id']}): {exc}", file=sys.stderr)
            time.sleep(XIAO_DELAY)
        conn.commit()


def empty_stats() -> dict[str, dict[str, int]]:
    return {kind: dict(Counter(fetched=0, parsed=0, structured=0, merged=0, failed=0)) for kind in ALL_KINDS}


def write_report(report: dict[str, Any]) -> None:
    path = ROOT / "reports" / "p3-content-report.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="also collect events, monsters, statuses, keywords, mechanics, characters and concepts")
    parser.add_argument("--kinds", help="comma-separated kinds; defaults to cards,relics,potions")
    parser.add_argument("--limit", type=int, help="limit rows per kind (useful for a resumable smoke run)")
    parser.add_argument("--refresh", action="store_true", help="reprocess already parsed rows from existing snapshots")
    parser.add_argument(
        "--languages",
        default="en,zh-CN",
        help="comma-separated source languages to process (default: en,zh-CN); useful for a targeted repair",
    )
    args = parser.parse_args(argv)
    kinds = list(ALL_KINDS if args.all else DEFAULT_KINDS)
    if args.kinds:
        kinds = [value.strip() for value in args.kinds.split(",") if value.strip()]
    unknown = sorted(set(kinds) - set(ALL_KINDS))
    if unknown:
        parser.error(f"unknown kind(s): {', '.join(unknown)}")
    languages = [value.strip() for value in args.languages.split(",") if value.strip()]
    unknown_languages = sorted(set(languages) - {"en", "zh-CN"})
    if unknown_languages:
        parser.error(f"unknown language(s): {', '.join(unknown_languages)}")
    if not languages:
        parser.error("--languages must contain en and/or zh-CN")

    for directory in [ROOT / "data", ROOT / "data" / "raw", ROOT / "data" / "exports", ROOT / "reports"]:
        directory.mkdir(parents=True, exist_ok=True)
    if not DB_PATH.exists():
        raise SystemExit("data/spire.sqlite not found; run bootstrap_sample.py and discover_inventory.py first")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    apply_schema(conn)
    run_id = "run.p3." + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    conn.execute("INSERT OR REPLACE INTO build_runs(id, started_at, status, parser_version) VALUES (?, ?, 'running', ?)", (run_id, utc_now(), PARSER_VERSION))
    conn.commit()
    report: dict[str, Any] = {
        "run_id": run_id,
        "status": "running",
        "parser_version": PARSER_VERSION,
        "started_at": utc_now(),
        "scope": {"kinds": kinds, "languages": languages, "limit_per_kind": args.limit, "game": "sts1"},
        "english": empty_stats(),
        "chinese": empty_stats(),
        "notes": [
            "English card fields come from the audited wiki.gg list boxes; full page wikitext is retained as a batch claim.",
            "Chinese article text is retained as source evidence. Only already confirmed P2 mappings are merged into an English entity.",
            "No strategy document is read, imported or linked.",
            "Image URLs are recorded as evidence; bulk image download awaits per-asset licence review.",
        ],
    }
    try:
        consolidate_legacy_duplicates(conn)
        # Character pages are not present in the wiki.gg compendium lists;
        # enrich their starting loadout whenever the audited snapshots exist.
        enrich_characters(conn)
        if "en" in languages:
            process_english(conn, kinds, args.limit, report, refresh=args.refresh)
        if "zh-CN" in languages:
            process_chinese(conn, kinds, args.limit, report, refresh=args.refresh)
        # Derive the entity-level mapping state from the names actually
        # present after this run.  A source-only English or Chinese candidate
        # is provisional; only bilingual rows with source-backed names become
        # confirmed.
        resolve_mapping_statuses(conn)
        # Export after all writes so JSONL mirrors the database.  The P1
        # exporter is intentionally reused to keep stable table ordering.
        counts = export_data(conn)
        report["inventory_status"] = {
            "|".join(key): value
            for key, value in sorted(
                ((row[0], row[1], row[2], row[3]), row[4])
                for row in conn.execute("SELECT entity_kind, language, source_id, status, COUNT(*) FROM inventory_items GROUP BY entity_kind, language, source_id, status")
            )
        }
        report["cumulative"] = {
            "english": {
                kind: {
                    "inventory": conn.execute("SELECT COUNT(*) FROM inventory_items WHERE entity_kind=? AND language='en' AND status!='excluded'", (kind,)).fetchone()[0],
                    "parsed": conn.execute("SELECT COUNT(*) FROM inventory_items WHERE entity_kind=? AND language='en' AND status='parsed'", (kind,)).fetchone()[0],
                    "failed": conn.execute("SELECT COUNT(*) FROM inventory_items WHERE entity_kind=? AND language='en' AND status='failed'", (kind,)).fetchone()[0],
                }
                for kind in ALL_KINDS
            },
            "chinese": {
                kind: {
                    "inventory": conn.execute("SELECT COUNT(*) FROM inventory_items WHERE entity_kind=? AND language='zh-CN' AND status!='excluded'", (kind,)).fetchone()[0],
                    "parsed": conn.execute("SELECT COUNT(*) FROM inventory_items WHERE entity_kind=? AND language='zh-CN' AND status='parsed'", (kind,)).fetchone()[0],
                    "failed": conn.execute("SELECT COUNT(*) FROM inventory_items WHERE entity_kind=? AND language='zh-CN' AND status='failed'", (kind,)).fetchone()[0],
                }
                for kind in ALL_KINDS
            },
        }
        report["counts"] = counts
        report["finished_at"] = utc_now()
        report["status"] = "success"
        conn.execute("UPDATE build_runs SET finished_at=?, status='success', counts_json=? WHERE id=?", (report["finished_at"], json_text(counts), run_id))
        conn.commit()
        write_report(report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        conn.rollback()
        report["finished_at"] = utc_now()
        report["status"] = "failed"
        report["error"] = str(exc)
        write_report(report)
        conn.execute("UPDATE build_runs SET finished_at=?, status='failed', notes=? WHERE id=?", (report["finished_at"], str(exc), run_id))
        conn.commit()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
