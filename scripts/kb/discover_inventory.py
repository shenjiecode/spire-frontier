"""Discover the audited Slay the Spire 1 directories from both Wikis.

This is the P2 directory step.  It deliberately writes source inventory rows
separately from reconciled ``entities``: a Chinese article and an English
page are not merged merely because they occupy a similar category.  Only the
small set of mappings already present in the reviewed sample database is
copied into ``inventory_mappings``; all other rows remain unmatched until a
field-level review is performed.

Usage (from the repository root)::

    python scripts/kb/discover_inventory.py

The Xiaoheihe homepage is JavaScript-rendered.  The web bundle's public
request signature is reproduced only to request that public directory JSON;
no login, cookie, captcha, or access-control bypass is used.
"""

from __future__ import annotations

import csv
import hashlib
import json
import random
import re
import sqlite3
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlencode, urljoin, urlsplit

from lxml import html

# Reuse the audited snapshot/fetch helpers and source constants from the P1
# bootstrap.  Importing the module does not run its main() function.
from bootstrap_sample import (  # type: ignore
    DB_PATH,
    ROOT,
    WIKI_BASE,
    XIAO_HOME,
    apply_schema,
    fetch_bytes,
    get_or_fetch_page,
    json_text,
    slug,
    source_page_id,
    snapshot_path,
    utc_now,
)


PARSER_VERSION = "kb-inventory/0.1"
XIAO_API_HOME = "https://api.xiaoheihe.cn/wiki/get_homepage_content/?wiki_id=646570"
XIAO_DIRECTORY_DISPLAY_URL = XIAO_HOME + "#directory-api"

WIKI_LISTS = [
    ("card", "Cards_List"),
    ("relic", "Relics_List"),
    ("potion", "Potions_List"),
    ("event", "Events_List"),
    ("monster", "Monsters"),
    ("monster", "Elites"),
    ("monster", "Bosses"),
    ("keyword", "Keywords"),
    ("mechanic", "Mechanics"),
    ("status", "Buffs"),
    ("status", "Debuffs"),
]

XIAO_CARD_CHARACTERS = {
    "铁甲战士": "ironclad",
    "静默猎手": "silent",
    "故障机器人": "defect",
    "观者": "watcher",
}

# The directory contains strategy, daily-challenge and site-maintenance
# blocks as well as game facts.  The former are reported as out of scope and
# are never placed in the basic Wiki inventory.
XIAO_CORE_BLOCKS = {
    "遗物收集": ("relic", None),
    "铁甲战士": ("card", "ironclad"),
    "静默猎手": ("card", "silent"),
    "故障机器人": ("card", "defect"),
    "观者": ("card", "watcher"),
    "无色牌": ("card", None),
    "诅咒牌": ("card", None),
    "事件": ("event", None),
    "怪物图鉴": ("monster", None),
    "药水": ("potion", None),
    "能力/Buff": ("status", None),
}
XIAO_INTRO_TAGS = {"游戏入门知识": "concept", "地图杂项": "mechanic", "角色介绍": "character"}


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", (value or "").replace("\u00a0", " ")).strip()


def canonical_wiki_url(href: str | None) -> str | None:
    if not href:
        return None
    if href.startswith("//"):
        href = "https:" + href
    if href.startswith("/"):
        return urljoin(WIKI_BASE, href)
    if href.startswith(WIKI_BASE):
        return href
    return None


def canonical_xiao_url(article_id: str | int) -> str:
    return f"https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id={article_id}&wiki_id=646570"


def first_wiki_link(node: html.HtmlElement) -> str | None:
    for anchor in node.xpath('.//a[@href]'):
        href = canonical_wiki_url(anchor.get("href"))
        if href and "/wiki/Special:" not in href and "/wiki/File:" not in href:
            return href
    return None


def js_xf(value: int) -> int:
    return ((value << 1) ^ 27) & 255 if value & 128 else (value << 1) & 255


def js_lf(value: int) -> int:
    return js_xf(value) ^ value


def js_tf(value: int) -> int:
    return js_lf(js_xf(value))


def js_ef(value: int) -> int:
    return js_tf(js_lf(js_xf(value)))


def js_df(value: int) -> int:
    return js_ef(value) ^ js_tf(value) ^ js_lf(value)


def js_af(value: str, alphabet: str, count: int) -> str:
    # JavaScript's String.slice(0, negative) is Python's value[:negative].
    prefix = alphabet[:count]
    return "".join(prefix[ord(char) % len(prefix)] for char in value)


def js_jf(value: str, alphabet: str) -> str:
    return "".join(alphabet[ord(char) % len(alphabet)] for char in value)


def xiao_signature(path: str, timestamp: int, nonce: str) -> str:
    """Reproduce the short public hkey function used by the web bundle."""
    alphabet = "AB45STUVWZEFGJ6CH01D237IXYPQRKLMN89"
    clean_path = "/" + "/".join(part for part in path.split("/") if part) + "/"
    parts = [js_af(str(timestamp), alphabet, -2), js_jf(clean_path, alphabet), js_jf(nonce, alphabet)]
    interleaved = "".join(part[index] for index in range(max(map(len, parts))) for part in parts if index < len(part))[:20]
    digest = hashlib.md5(interleaved.encode("utf-8")).hexdigest()
    tail = [ord(char) for char in digest[-6:]]
    transformed = [
        js_df(tail[0]) ^ js_ef(tail[1]) ^ js_tf(tail[2]) ^ js_lf(tail[3]),
        js_lf(tail[0]) ^ js_df(tail[1]) ^ js_ef(tail[2]) ^ js_tf(tail[3]),
        js_tf(tail[0]) ^ js_lf(tail[1]) ^ js_df(tail[2]) ^ js_ef(tail[3]),
        js_ef(tail[0]) ^ js_tf(tail[1]) ^ js_lf(tail[2]) ^ js_df(tail[3]),
    ]
    tail[:4] = transformed
    suffix = str(sum(tail) % 100).zfill(2)
    return js_af(digest[:5], alphabet, -4) + suffix


def fetch_xiao_homepage(conn: sqlite3.Connection) -> tuple[str, dict[str, Any]]:
    """Fetch or reuse the signed homepage directory JSON snapshot."""
    page_id = source_page_id("xiaoheihe", XIAO_API_HOME)
    row = conn.execute("SELECT snapshot_path FROM source_pages WHERE id=?", (page_id,)).fetchone()
    if row and row[0] and (ROOT / row[0]).exists():
        # Keep the clickable provenance URL on the public Wiki page rather
        # than on the signed API request (whose parameters are ephemeral).
        conn.execute("UPDATE source_pages SET url=? WHERE id=?", (XIAO_DIRECTORY_DISPLAY_URL, page_id))
        conn.commit()
        body = (ROOT / row[0]).read_bytes()
        return page_id, json.loads(body.decode("utf-8"))

    timestamp = int(time.time())
    nonce = hashlib.md5(f"{timestamp}{random.random()}".encode("utf-8")).hexdigest().upper()
    params = {
        "os_type": "web",
        "app": "heybox",
        "client_type": "mobile",
        "version": "999.0.4",
        "x_client_type": "web",
        "x_os_type": "Windows",
        "x_app": "heybox",
        "heybox_id": "-1",
        "wiki_id": "646570",
        "verison": "",
        "is_share": "1",
        "_time": str(timestamp),
        "nonce": nonce,
        "hkey": xiao_signature("/wiki/get_homepage_content/", timestamp, nonce),
    }
    request_url = "https://api.xiaoheihe.cn/wiki/get_homepage_content/?" + urlencode(params)
    result = fetch_bytes(request_url, is_xiao=True)
    body = result["body"]
    path, digest = snapshot_path("xiaoheihe", "homepage_api", body)
    payload = json.loads(body.decode("utf-8"))
    conn.execute(
        """INSERT INTO source_pages
        (id, source_id, url, title, source_page_key, fetched_at, http_status,
         content_type, snapshot_path, sha256, parser_version, is_index_page, notes)
        VALUES (?, 'xiaoheihe', ?, ?, 'homepage_api', ?, ?, ?, ?, ?, ?, 1, ?)
        ON CONFLICT(id) DO UPDATE SET fetched_at=excluded.fetched_at,
          http_status=excluded.http_status, content_type=excluded.content_type,
          snapshot_path=excluded.snapshot_path, sha256=excluded.sha256,
          parser_version=excluded.parser_version, notes=excluded.notes""",
        (
            page_id,
            XIAO_DIRECTORY_DISPLAY_URL,
            "小黑盒《杀戮尖塔》百科目录 API",
            utc_now(),
            result["status"],
            result["content_type"],
            str(path.relative_to(ROOT)).replace("\\", "/"),
            digest,
            PARSER_VERSION,
            "Signed public homepage request; the signed URL is intentionally not used as a stable identity.",
        ),
    )
    conn.commit()
    return page_id, payload


def inventory_id(source_id: str, source_item_key: str) -> str:
    return "inventory." + hashlib.sha256(f"{source_id}|{source_item_key}".encode("utf-8")).hexdigest()[:24]


def insert_inventory(
    conn: sqlite3.Connection,
    *,
    source_id: str,
    source_page_id: str,
    source_item_key: str,
    entity_kind: str,
    language: str,
    name: str,
    url: str,
    article_id: str | None = None,
    category: str | None = None,
    subcategory: str | None = None,
    character: str | None = None,
    metadata: dict[str, Any] | None = None,
    status: str = "discovered",
) -> str:
    item_id = inventory_id(source_id, source_item_key)
    conn.execute(
        """INSERT INTO inventory_items
        (id, source_id, source_page_id, source_item_key, entity_kind, language,
         name, article_id, url, category, subcategory, character,
         metadata_json, discovered_at, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(source_id, source_item_key) DO UPDATE SET
          source_page_id=excluded.source_page_id, entity_kind=excluded.entity_kind,
          language=excluded.language, name=excluded.name, article_id=excluded.article_id,
          url=excluded.url, category=excluded.category, subcategory=excluded.subcategory,
          character=excluded.character, metadata_json=excluded.metadata_json,
          discovered_at=excluded.discovered_at, status=excluded.status""",
        (
            item_id,
            source_id,
            source_page_id,
            source_item_key,
            entity_kind,
            language,
            name,
            article_id,
            url,
            category,
            subcategory,
            character,
            json_text(metadata or {}),
            utc_now(),
            status,
        ),
    )
    return item_id


def parse_xiao_inventory(conn: sqlite3.Connection, page_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    added: list[str] = []
    excluded = Counter()
    blocks_report: dict[str, dict[str, int]] = {}
    chunks = payload.get("result", {}).get("chunk", [])
    for chunk in chunks:
        for block in chunk.get("block", []):
            title = clean_text(block.get("block_title"))
            tags = block.get("tag_list", []) or []
            if title in XIAO_CORE_BLOCKS:
                kind, character = XIAO_CORE_BLOCKS[title]
                selected = [tag for tag in tags if tag.get("tag_id") == -2]
                if not selected:
                    selected = tags
                block_added = 0
                # Keep distinct labels for one article (for example the two
                # Chinese aliases used for the Looter).  Repeated appearances
                # of the same label in another filter are still collapsed.
                seen: set[tuple[str, str]] = set()
                for tag in selected:
                    tag_name = clean_text(tag.get("tag_name"))
                    for entry in tag.get("block_entries", []) or []:
                        article_id = entry.get("article_id")
                        if article_id in (None, ""):
                            continue
                        article_key = str(article_id)
                        name = clean_text(entry.get("entry_name") or entry.get("article_name"))
                        seen_key = (article_key, name)
                        if seen_key in seen:
                            continue
                        seen.add(seen_key)
                        if not name:
                            continue
                        item = insert_inventory(
                            conn,
                            source_id="xiaoheihe",
                            source_page_id=page_id,
                            source_item_key=f"article:{article_id}:{name}",
                            entity_kind=kind,
                            language="zh-CN",
                            name=name,
                            article_id=article_key,
                            url=canonical_xiao_url(article_id),
                            category=title,
                            subcategory=tag_name,
                            character=character,
                            metadata={
                                "entry_id": entry.get("entry_id"),
                                "tag_id": tag.get("tag_id"),
                                "entry_type": entry.get("entry_type"),
                                "entry_img": clean_text(entry.get("entry_img")),
                            },
                        )
                        added.append(item)
                        block_added += 1
                blocks_report[title] = {"items": block_added}
                continue

            if title == "游戏入门介绍":
                block_added = 0
                for tag in tags:
                    tag_name = clean_text(tag.get("tag_name"))
                    kind = XIAO_INTRO_TAGS.get(tag_name)
                    if not kind:
                        excluded[f"intro:{tag_name or 'uncategorized'}"] += len(tag.get("block_entries", []) or [])
                        continue
                    for entry in tag.get("block_entries", []) or []:
                        article_id = entry.get("article_id")
                        name = clean_text(entry.get("entry_name") or entry.get("article_name"))
                        if article_id in (None, "") or not name:
                            continue
                        item = insert_inventory(
                            conn,
                            source_id="xiaoheihe",
                            source_page_id=page_id,
                            source_item_key=f"article:{article_id}:{name}",
                            entity_kind=kind,
                            language="zh-CN",
                            name=name,
                            article_id=str(article_id),
                            url=canonical_xiao_url(article_id),
                            category=title,
                            subcategory=tag_name,
                            metadata={"entry_id": entry.get("entry_id"), "tag_id": tag.get("tag_id")},
                        )
                        added.append(item)
                        block_added += 1
                blocks_report[title] = {"items": block_added}
                continue

            # Strategy, daily challenge, troubleshooting and Wiki-maintenance
            # blocks are deliberately outside the basic inventory scope.
            if title:
                excluded[title] += sum(len(tag.get("block_entries", []) or []) for tag in tags)

    return {"items": added, "excluded": dict(excluded), "blocks": blocks_report}


def parse_card_boxes(conn: sqlite3.Connection, page_id: str, tree: html.HtmlElement) -> list[str]:
    color_character = {"Red": "ironclad", "Green": "silent", "Blue": "defect", "Purple": "watcher"}
    ids: list[str] = []
    for box in tree.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " card-box ")]'):
        name = clean_text(box.get("data-name"))
        href = first_wiki_link(box)
        if not name or not href:
            continue
        color = box.get("data-color") or "Other"
        character = color_character.get(color)
        item = insert_inventory(
            conn,
            source_id="wiki_gg",
            source_page_id=page_id,
            source_item_key=f"card:{href}",
            entity_kind="card",
            language="en",
            name=name,
            url=href,
            category="Cards_List",
            subcategory=color,
            character=character,
            metadata={
                "rarity": box.get("data-rarity"),
                "type": box.get("data-type"),
                "cost": box.get("data-cost"),
                "can_upgrade": box.get("data-canupgrade") == "true",
                "tags": (box.get("data-tags") or "").split(),
            },
        )
        ids.append(item)
    return ids


def parse_relic_boxes(conn: sqlite3.Connection, page_id: str, tree: html.HtmlElement) -> tuple[list[str], int]:
    ids: list[str] = []
    excluded = 0
    for box in tree.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " relic-box ")]'):
        name = clean_text(box.get("data-name"))
        href = first_wiki_link(box)
        if not name or not href:
            continue
        rarity = box.get("data-rarity") or ""
        status = "excluded" if rarity == "Blight" else "discovered"
        if status == "excluded":
            excluded += 1
        item = insert_inventory(
            conn,
            source_id="wiki_gg",
            source_page_id=page_id,
            source_item_key=f"relic:{href}",
            entity_kind="relic",
            language="en",
            name=name,
            url=href,
            category="Relics_List",
            subcategory=rarity,
            character=box.get("data-character"),
            metadata={"rarity": rarity, "ancient_upgrade": box.get("data-ancient-upgrade")},
            status=status,
        )
        ids.append(item)
    return ids, excluded


def parse_potion_boxes(conn: sqlite3.Connection, page_id: str, tree: html.HtmlElement) -> list[str]:
    ids: list[str] = []
    for box in tree.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " potion-box ")]'):
        name = clean_text(box.get("data-name"))
        href = first_wiki_link(box)
        if not name or not href:
            continue
        item = insert_inventory(
            conn,
            source_id="wiki_gg",
            source_page_id=page_id,
            source_item_key=f"potion:{href}",
            entity_kind="potion",
            language="en",
            name=name,
            url=href,
            category="Potions_List",
            subcategory=box.get("data-rarity"),
            character=box.get("data-character"),
            metadata={"rarity": box.get("data-rarity"), "tags": (box.get("data-tags") or "").split()},
        )
        ids.append(item)
    return ids


def parse_event_boxes(conn: sqlite3.Connection, page_id: str, tree: html.HtmlElement) -> list[str]:
    ids: list[str] = []
    for box in tree.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " event-box ")]'):
        title = box.xpath('.//div[contains(@class,"event-title")]//a[1]')
        href = canonical_wiki_url(title[0].get("href")) if title else None
        name = clean_text(title[0].text_content()) if title else ""
        if not name or not href:
            continue
        meta = clean_text(" ".join(box.xpath('.//div[contains(@class,"event-meta")]//text()')))
        item = insert_inventory(
            conn,
            source_id="wiki_gg",
            source_page_id=page_id,
            source_item_key=f"event:{href}",
            entity_kind="event",
            language="en",
            name=name,
            url=href,
            category="Events_List",
            subcategory=meta or None,
            metadata={"shrine": box.get("data-shrine") == "true", "meta": meta},
        )
        ids.append(item)
    return ids


def fragment_name(href: str, fallback: str) -> str:
    fragment = urlsplit(href).fragment
    if fragment:
        return unquote(fragment).replace("_", " ")
    return fallback


def parse_monster_images(conn: sqlite3.Connection, page_id: str, tree: html.HtmlElement, page_name: str, css_class: str) -> list[str]:
    ids: list[str] = []
    content = tree.xpath('//div[@id="mw-content-text"]')[0]
    for image in content.xpath(f'.//img[contains(concat(" ", normalize-space(@class), " "), " {css_class} ")]'):
        anchor = image.getparent()
        href = canonical_wiki_url(anchor.get("href")) if anchor is not None else None
        if not href:
            continue
        name = fragment_name(href, clean_text(anchor.get("title")) if anchor is not None else "")
        if not name:
            continue
        item = insert_inventory(
            conn,
            source_id="wiki_gg",
            source_page_id=page_id,
            source_item_key=f"monster:{page_name}:{href}",
            entity_kind="monster",
            language="en",
            name=name,
            url=href,
            category=page_name,
            subcategory={"Monsters": "normal", "Elites": "elite", "Bosses": "boss"}.get(page_name),
            metadata={"image": image.get("src"), "image_alt": image.get("alt")},
        )
        ids.append(item)
    return ids


def parse_headings(conn: sqlite3.Connection, page_id: str, tree: html.HtmlElement, page_name: str, kind: str) -> list[str]:
    ids: list[str] = []
    content = tree.xpath('//div[@id="mw-content-text"]')[0]
    for heading in content.xpath('.//h3|.//h4|.//h5'):
        headline = heading.xpath('.//span[contains(@class,"mw-headline")][1]')
        if not headline:
            continue
        name = clean_text(headline[0].text_content())
        anchor_id = headline[0].get("id")
        if not name or not anchor_id:
            continue
        href = f"{WIKI_BASE}/wiki/{page_name}#{anchor_id}"
        item = insert_inventory(
            conn,
            source_id="wiki_gg",
            source_page_id=page_id,
            source_item_key=f"{kind}:{page_name}#{anchor_id}",
            entity_kind=kind,
            language="en",
            name=name,
            url=href,
            category=page_name,
            subcategory=heading.tag,
            metadata={"heading_id": anchor_id, "heading_level": heading.tag},
        )
        ids.append(item)
    return ids


def parse_status_table(conn: sqlite3.Connection, page_id: str, tree: html.HtmlElement, page_name: str) -> list[str]:
    ids: list[str] = []
    content = tree.xpath('//div[@id="mw-content-text"]')[0]
    tables = content.xpath('.//table[@id="characterTable"]')
    if not tables:
        return ids
    table = tables[0]
    for row in table.xpath('./tbody/tr')[1:]:
        cells = row.xpath('./td')
        if len(cells) < 2:
            continue
        name = clean_text(cells[1].text_content())
        if not name:
            continue
        href = first_wiki_link(cells[1]) or f"{WIKI_BASE}/wiki/{page_name}#{slug(name)}"
        item = insert_inventory(
            conn,
            source_id="wiki_gg",
            source_page_id=page_id,
            source_item_key=f"status:{page_name}:{name}",
            entity_kind="status",
            language="en",
            name=name,
            url=href,
            category=page_name,
            metadata={"columns": len(cells)},
        )
        ids.append(item)
    return ids


def parse_keyword_triggers(conn: sqlite3.Connection, page_id: str, tree: html.HtmlElement) -> list[str]:
    ids: list[str] = []
    content = tree.xpath('//div[@id="mw-content-text"]')[0]
    seen: set[str] = set()
    for span in content.xpath('.//span[contains(concat(" ", normalize-space(@class), " "), " keyword-trigger ")]'):
        name = clean_text(span.get("data-name"))
        href = first_wiki_link(span)
        if not name or not href or href in seen:
            continue
        seen.add(href)
        ids.append(
            insert_inventory(
                conn,
                source_id="wiki_gg",
                source_page_id=page_id,
                source_item_key=f"keyword:{href}",
                entity_kind="keyword",
                language="en",
                name=name,
                url=href,
                category="Keywords",
            )
        )
    # Headings retain definitions that do not happen to appear in an inline
    # trigger, so include them as well and let the source key deduplicate.
    ids.extend(parse_headings(conn, page_id, tree, "Keywords", "keyword"))
    return ids


def discover_wiki(conn: sqlite3.Connection) -> dict[str, Any]:
    counts = Counter()
    page_ids: dict[str, str] = {}
    for kind, page_name in WIKI_LISTS:
        url = f"{WIKI_BASE}/wiki/{page_name}"
        try:
            page_id, _, _ = get_or_fetch_page(conn, "wiki_gg", url, f"inventory_{page_name}", is_index=True)
            page_ids[page_name] = page_id
            path_row = conn.execute("SELECT snapshot_path FROM source_pages WHERE id=?", (page_id,)).fetchone()
            if not path_row or not path_row[0]:
                continue
            tree = html.fromstring((ROOT / path_row[0]).read_bytes())
            if page_name == "Cards_List":
                ids = parse_card_boxes(conn, page_id, tree)
            elif page_name == "Relics_List":
                ids, excluded = parse_relic_boxes(conn, page_id, tree)
                counts["wiki_excluded_sts2_relics"] += excluded
            elif page_name == "Potions_List":
                ids = parse_potion_boxes(conn, page_id, tree)
            elif page_name == "Events_List":
                ids = parse_event_boxes(conn, page_id, tree)
            elif page_name == "Monsters":
                ids = parse_monster_images(conn, page_id, tree, page_name, "monster-img")
            elif page_name == "Elites":
                ids = parse_monster_images(conn, page_id, tree, page_name, "elite-img")
            elif page_name == "Bosses":
                ids = parse_monster_images(conn, page_id, tree, page_name, "boss-img")
            elif page_name == "Keywords":
                ids = parse_keyword_triggers(conn, page_id, tree)
            elif page_name == "Mechanics":
                ids = parse_headings(conn, page_id, tree, page_name, "mechanic")
            elif page_name in {"Buffs", "Debuffs"}:
                ids = parse_status_table(conn, page_id, tree, page_name)
            else:
                ids = []
            counts[f"wiki_{kind}"] += len(set(ids))
            # Requests are serial when a page is actually fetched.  A small
            # pause also makes a fresh run polite to the public site.
            time.sleep(0.8)
        except Exception as exc:
            print(f"[wiki-warning] {url}: {exc}", file=sys.stderr)
    return {"counts": dict(counts), "page_ids": page_ids}


def build_mappings(conn: sqlite3.Connection) -> dict[str, int]:
    """Copy only already-reviewed sample identities into P2 mapping rows."""
    conn.execute("DELETE FROM inventory_mappings")
    mapped = Counter()
    entities = conn.execute("SELECT id, kind, mapping_status FROM entities ORDER BY id").fetchall()
    for entity in entities:
        names = conn.execute(
            "SELECT language, name FROM names WHERE entity_id=? AND is_preferred=1",
            (entity["id"],),
        ).fetchall()
        zh_names = [r[1] for r in names if r[0] == "zh-CN"]
        en_names = [r[1] for r in names if r[0] == "en"]
        if not zh_names or not en_names:
            continue
        zh_rows = conn.execute(
            "SELECT * FROM inventory_items WHERE language='zh-CN' AND entity_kind=? AND name=? AND status!='excluded'",
            (entity["kind"], zh_names[0]),
        ).fetchall()
        en_rows = conn.execute(
            "SELECT * FROM inventory_items WHERE language='en' AND entity_kind=? AND name=? AND status!='excluded'",
            (entity["kind"], en_names[0]),
        ).fetchall()
        if entity["kind"] == "card":
            # Strike and other same-name cards must agree on the character.
            character = conn.execute(
                "SELECT c.character_entity_id, n.name FROM cards c JOIN names n ON n.entity_id=c.character_entity_id AND n.language='en' WHERE c.entity_id=?",
                (entity["id"],),
            ).fetchone()
            if character:
                character_name = character[1]
                en_rows = [r for r in en_rows if not r["character"] or r["character"] == {"Ironclad": "ironclad", "Silent": "silent", "Defect": "defect", "Watcher": "watcher"}.get(character_name, character_name)]
        for zh in zh_rows:
            for en in en_rows:
                status = "confirmed" if entity["mapping_status"] == "confirmed" else "candidate"
                mid = "mapping." + hashlib.sha256(f"{zh['id']}|{en['id']}".encode("utf-8")).hexdigest()[:24]
                conn.execute(
                    """INSERT INTO inventory_mappings
                    (id, zh_inventory_id, en_inventory_id, status, rationale, evidence_json, decided_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (
                        mid,
                        zh["id"],
                        en["id"],
                        status,
                        (
                            f"Copied from confirmed entity {entity['id']}; no new translation inference was made."
                            if status == "confirmed"
                            else f"Retained as the existing provisional candidate for {entity['id']}; no new translation inference was made."
                        ),
                        json_text({"entity_id": entity["id"]}),
                        utc_now(),
                    ),
                )
                mapped[status] += 1
    return dict(mapped)


def write_exports(conn: sqlite3.Connection, mapping_counts: dict[str, int]) -> dict[str, int]:
    export_dir = ROOT / "data" / "exports"
    export_dir.mkdir(parents=True, exist_ok=True)
    rows = conn.execute("SELECT * FROM inventory_items ORDER BY source_id, entity_kind, category, name, id").fetchall()
    with (export_dir / "inventory.jsonl").open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(dict(row), ensure_ascii=False, sort_keys=True) + "\n")
    csv_fields = ["id", "source_id", "source_page_id", "entity_kind", "language", "name", "article_id", "url", "category", "subcategory", "character", "status"]
    with (export_dir / "inventory.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=csv_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in csv_fields})

    mapping_db_rows = conn.execute("SELECT * FROM inventory_mappings ORDER BY id").fetchall()
    with (export_dir / "inventory_mappings.jsonl").open("w", encoding="utf-8", newline="\n") as fh:
        for row in mapping_db_rows:
            fh.write(json.dumps(dict(row), ensure_ascii=False, sort_keys=True) + "\n")

    mapping_rows: list[dict[str, Any]] = []
    mapped_zh: set[str] = set()
    mapped_en: set[str] = set()
    for row in conn.execute(
        """SELECT m.*, z.name AS zh_name, z.article_id AS zh_article_id, z.url AS zh_url,
                  e.name AS en_name, e.url AS en_url, e.article_id AS en_article_id
           FROM inventory_mappings m
           JOIN inventory_items z ON z.id=m.zh_inventory_id
           JOIN inventory_items e ON e.id=m.en_inventory_id
           ORDER BY z.entity_kind, z.name, e.name"""
    ):
        mapped_zh.add(row["zh_inventory_id"])
        mapped_en.add(row["en_inventory_id"])
        mapping_rows.append(
            {
                "entity_kind": conn.execute("SELECT entity_kind FROM inventory_items WHERE id=?", (row["zh_inventory_id"],)).fetchone()[0],
                "zh_name": row["zh_name"],
                "en_name": row["en_name"],
                "zh_article_id": row["zh_article_id"],
                "en_article_id": row["en_article_id"],
                "zh_url": row["zh_url"],
                "en_url": row["en_url"],
                "mapping_status": row["status"],
                "basis": row["rationale"],
            }
        )
    for row in rows:
        if row["status"] == "excluded":
            continue
        if row["language"] == "zh-CN" and row["id"] not in mapped_zh:
            mapping_rows.append({"entity_kind": row["entity_kind"], "zh_name": row["name"], "en_name": "", "zh_article_id": row["article_id"], "en_article_id": "", "zh_url": row["url"], "en_url": "", "mapping_status": "unmatched_zh", "basis": "目录发现；尚无已审阅英文对应项"})
        if row["language"] == "en" and row["id"] not in mapped_en:
            mapping_rows.append({"entity_kind": row["entity_kind"], "zh_name": "", "en_name": row["name"], "zh_article_id": "", "en_article_id": row["article_id"] or "", "zh_url": "", "en_url": row["url"], "mapping_status": "unmatched_en", "basis": "目录发现；尚无已审阅中文对应项"})
    mapping_fields = ["entity_kind", "zh_name", "en_name", "zh_article_id", "en_article_id", "zh_url", "en_url", "mapping_status", "basis"]
    with (export_dir / "name_mapping.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=mapping_fields)
        writer.writeheader()
        writer.writerows(mapping_rows)

    by_source_kind = Counter((row["source_id"], row["language"], row["entity_kind"]) for row in rows if row["status"] != "excluded")
    by_kind = Counter(row["entity_kind"] for row in rows if row["status"] != "excluded")
    by_language = Counter(row["language"] for row in rows if row["status"] != "excluded")
    summary = {
        "inventory_items": len(rows),
        "inventory_active": sum(1 for row in rows if row["status"] != "excluded"),
        "inventory_excluded": sum(1 for row in rows if row["status"] == "excluded"),
        "mapping_rows": len(mapping_rows),
        "inventory_mapping_records": len(mapping_db_rows),
        "mapped_confirmed": mapping_counts.get("confirmed", 0),
        "mapped_candidate": mapping_counts.get("candidate", 0),
        "by_kind": dict(sorted(by_kind.items())),
        "by_language": dict(sorted(by_language.items())),
        "by_source_language_kind": {"|".join(key): value for key, value in sorted(by_source_kind.items())},
    }
    # Keep the shared export manifest useful after a P2 run while preserving
    # the entity-only counts emitted by the P1 bootstrap.
    manifest_path = export_dir / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    except (OSError, json.JSONDecodeError):
        manifest = {}
    manifest.update({"generated_at": utc_now(), "parser_version": PARSER_VERSION, "inventory": summary})
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def write_inventory_page(conn: sqlite3.Connection, report: dict[str, Any]) -> None:
    path = ROOT / "docs" / "wiki" / "inventory.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = conn.execute("SELECT source_id, language, entity_kind, status, COUNT(*) AS n FROM inventory_items GROUP BY source_id, language, entity_kind, status ORDER BY source_id, language, entity_kind, status").fetchall()
    lines = [
        "# 双源目录（P2）",
        "",
        f"生成时间：{utc_now()}。本页只记录两站目录发现结果，不把未核对的中文/英文条目合并为正式实体。",
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
        "- wiki.gg 的卡牌、遗物、药水和事件列表使用页面结构化盒子；普通敌人、精英和 Boss 使用各自页面的图鉴图像链接。",
        "- 小黑盒目录来自用户指定 Wiki 的动态首页 JSON；原始响应已保存到 `data/raw/xiaoheihe/`，文章正文仍需在后续阶段逐项抓取。",
        "- wiki.gg 遗物清单中的 `Blight` 条目被标记为 `excluded`（StS2 范围），没有写入基础实体。",
        "- 日常挑战、职业打法、常见问题和百科维护栏目不属于当前基础 Wiki；它们的排除数量写在 P2 报告中。",
        "- `confirmed` 映射只复制 P1 中已经审阅的实体；`unmatched_*` 是待核查项，不能当作缺少对应条目的结论。",
        "",
        "## 报告",
        "",
        f"- [P2 目录报告](../../reports/p2-inventory-report.json)",
        f"- 当前发现 {report.get('inventory_active', 0)} 条有效目录记录，{report.get('mapped_confirmed', 0)} 对已审阅映射。",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    for directory in [ROOT / "data", ROOT / "data" / "raw", ROOT / "data" / "exports", ROOT / "reports", ROOT / "docs" / "wiki"]:
        directory.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    apply_schema(conn)
    conn.executemany(
        "INSERT OR IGNORE INTO sources(id, name, base_url, language, license, source_kind, scope_note, notes) VALUES (?, ?, ?, ?, ?, 'wiki', ?, ?)",
        [
            ("wiki_gg", "Slay the Spire Wiki.gg", WIKI_BASE, "en", "CC BY-SA 4.0", "StS1 and StS2; this run filters to StS1", "Inventory parser excludes the Blight/StS2 relic rows."),
            ("xiaoheihe", "小黑盒《杀戮尖塔》百科", "https://web.xiaoheihe.cn/wiki/home?wiki_id=646570", "zh-CN", "unknown", "User-specified Chinese Wiki", "Directory is read from the signed public homepage JSON; article bodies are a later stage."),
        ],
    )
    # Discovery output is reproducible.  Rebuild its rows while retaining the
    # raw source snapshots; mapping rows are regenerated only from reviewed
    # entities below.
    conn.execute("DELETE FROM inventory_mappings")
    conn.execute("DELETE FROM inventory_items")
    conn.commit()
    try:
        xiao_page_id, xiao_payload = fetch_xiao_homepage(conn)
        xiao_report = parse_xiao_inventory(conn, xiao_page_id, xiao_payload)
        wiki_report = discover_wiki(conn)
        mapping_counts = build_mappings(conn)
        conn.commit()
        export_report = write_exports(conn, mapping_counts)
        report = {
            "generated_at": utc_now(),
            "status": "success",
            "parser_version": PARSER_VERSION,
            "sources": ["xiaoheihe", "wiki_gg"],
            "scope": "P2 bilingual directory discovery; facts remain un-reconciled",
            "xiao": {"source_page_id": xiao_page_id, "blocks": xiao_report["blocks"], "excluded": xiao_report["excluded"]},
            "wiki": wiki_report,
            "mappings": mapping_counts,
            **export_report,
            "known_limitations": [
                "Directory presence is not article-content verification.",
                "Most Chinese and English names remain unmatched until field-level identity review.",
                "The Xiaoheihe API response is a directory snapshot; article bodies and images are not fetched in P2.",
                "wiki.gg list counts are source counts after explicit StS2 Blight exclusion, not a claim about game-version completeness.",
            ],
        }
        (ROOT / "reports" / "p2-inventory-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_inventory_page(conn, report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        conn.rollback()
        print(f"inventory discovery failed: {exc}", file=sys.stderr)
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
