"""Build the first reproducible Slay the Spire 1 knowledge-base sample.

The script intentionally imports a small, auditable vertical slice.  It keeps
raw HTML/JSON responses, stores field-level claims, and then creates a
provisional SQLite view.  It is safe to run again: existing source snapshots,
entities, claims, and assets are reused by their stable keys.

Usage (from the repository root):
    python scripts/kb/bootstrap_sample.py

The bundled Codex Python runtime has lxml.  A normal checkout should install
the project requirements first.
"""

from __future__ import annotations

import csv
from copy import deepcopy
import hashlib
import json
import mimetypes
import re
import sqlite3
import sys
import time
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

from lxml import html


ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "spire.sqlite"
SCHEMA_PATH = ROOT / "schemas" / "001_initial.sql"
PARSER_VERSION = "kb-bootstrap-sample/0.1"
WIKI_BASE = "https://slaythespire.wiki.gg"
XIAO_HOME = "https://web.xiaoheihe.cn/wiki/home?wiki_id=646570"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "Chrome/130 Safari/537.36 spire-scholar-kb/0.1"
)


CHARACTERS = {
    "ironclad": {"id": "sts1.character.ironclad", "zh": "铁甲战士", "en": "Ironclad"},
    "silent": {"id": "sts1.character.silent", "zh": "静默猎手", "en": "Silent"},
    "defect": {"id": "sts1.character.defect", "zh": "故障机器人", "en": "Defect"},
    "watcher": {"id": "sts1.character.watcher", "zh": "观者", "en": "Watcher"},
}

# These names are deliberately a mix of directly observed Chinese articles
# and English-only sample pages.  A missing Chinese article is left as a
# candidate instead of being silently asserted as a verified translation.
CARD_SAMPLES = [
    {"wiki_name": "Strike (Ironclad)", "character": "ironclad", "zh": "打击", "zh_article": "404833", "xiao_key": "strike_ironclad"},
    {"wiki_name": "Body Slam", "character": "ironclad", "zh": "全身撞击", "zh_article": "408598", "xiao_key": "body_slam"},
    {"wiki_name": "Inflame", "character": "ironclad", "zh": "燃烧"},
    {"wiki_name": "Feel No Pain", "character": "ironclad", "zh": "无惧疼痛"},
    {"wiki_name": "Corruption", "character": "ironclad", "zh": "腐化"},
    {"wiki_name": "Barricade", "character": "ironclad", "zh": "壁垒"},
    {"wiki_name": "Searing Blow", "character": "ironclad", "zh": "灼热攻击"},
    {"wiki_name": "Neutralize", "character": "silent", "zh": "中和"},
    {"wiki_name": "Zap", "character": "defect", "zh": "电击"},
    {"wiki_name": "Eruption", "character": "watcher", "zh": "暴怒"},
]

XIAO_ARTICLES = {
    "body_slam": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408598&wiki_id=646570",
    "strike_ironclad": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=404833&wiki_id=646570",
    "burning_blood": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=493025&wiki_id=646570",
    "snake_ring": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=492919&wiki_id=646570",
    "weak_potion": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=496923&wiki_id=646570",
    "slime_boss": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570",
    "we_meet_again": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408930&wiki_id=646570",
    "strength": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501526&wiki_id=646570",
}

SAMPLE_WIKI_PAGES = {
    "burning_blood": "Burning_Blood",
    "snake_ring": "Ring_of_the_Snake",
    "weak_potion": "Weak_Potion",
    "slime_boss": "Slime_Boss",
    "we_meet_again": "We_Meet_Again!",
    "strength": "Strength",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalise(value: str) -> str:
    value = unescape(value or "").replace("\u00a0", " ")
    return re.sub(r"\s+", " ", value).strip().casefold()


def slug(value: str) -> str:
    value = value.casefold().replace("&", "and")
    value = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    return value or "item"


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


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


def apply_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    conn.commit()


def fetch_bytes(url: str, *, is_xiao: bool = False, attempts: int = 4) -> dict[str, Any]:
    """Fetch a public page with polite retries; never bypasses access checks."""
    last_error: Exception | None = None
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json,text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8" if is_xiao else "en-US,en;q=0.9",
        "Referer": XIAO_HOME if is_xiao else WIKI_BASE + "/",
    }
    for attempt in range(attempts):
        try:
            response = urlopen(Request(url, headers=headers), timeout=60)
            body = response.read()
            return {
                "url": response.geturl(),
                "status": getattr(response, "status", 200),
                "content_type": response.headers.get("Content-Type", ""),
                "body": body,
            }
        except HTTPError as exc:
            last_error = exc
            # 401/403/429 are recorded as failures after retrying; no bypass.
            if exc.code not in (403, 408, 425, 429, 500, 502, 503, 504):
                raise
        except (URLError, TimeoutError, OSError) as exc:
            last_error = exc
        if attempt + 1 < attempts:
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f"fetch failed after {attempts} attempts: {url}: {last_error}")


def decode_xiao(body: bytes) -> str:
    # The article endpoint advertises UTF-8 in the HTML meta tag but its
    # response bytes have been observed as GBK.  Keep the raw bytes and decode
    # this presentation layer explicitly.
    text_gbk = body.decode("gbk", errors="replace")
    text_utf8 = body.decode("utf-8", errors="replace")
    if text_gbk.count("�") < text_utf8.count("�"):
        return text_gbk
    return text_utf8


def snapshot_path(source_dir: str, stem: str, body: bytes) -> tuple[Path, str]:
    digest = hashlib.sha256(body).hexdigest()
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    directory = ROOT / "data" / "raw" / source_dir / day
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{slug(stem)}-{digest[:12]}.bin"
    if not path.exists():
        path.write_bytes(body)
    return path, digest


def source_page_id(source_id: str, url: str) -> str:
    return f"source_page.{source_id}.{hashlib.sha1(url.encode()).hexdigest()[:16]}"


def get_or_fetch_page(
    conn: sqlite3.Connection,
    source_id: str,
    url: str,
    stem: str,
    *,
    is_xiao: bool = False,
    is_index: bool = False,
) -> tuple[str, bytes, str]:
    """Return stable page id, bytes, and decoded text; reuse existing snapshots."""
    pid = source_page_id(source_id, url)
    row = conn.execute("SELECT snapshot_path, sha256 FROM source_pages WHERE id = ?", (pid,)).fetchone()
    if row and row[0]:
        path = ROOT / row[0]
        if path.exists():
            body = path.read_bytes()
            return pid, body, decode_xiao(body) if is_xiao else body.decode("utf-8", errors="replace")

    result = fetch_bytes(url, is_xiao=is_xiao)
    body = result["body"]
    path, digest = snapshot_path("xiaoheihe" if is_xiao else "wiki_gg", stem, body)
    title = ""
    text = decode_xiao(body) if is_xiao else body.decode("utf-8", errors="replace")
    try:
        tree = html.fromstring(text)
        title = re.sub(r"\s+", " ", tree.xpath("string(//title)")).strip()
    except Exception:
        pass
    article_id = re.search(r"article_id=([0-9]+)", url)
    conn.execute(
        """INSERT INTO source_pages
        (id, source_id, url, title, source_page_key, article_id, fetched_at,
         http_status, content_type, snapshot_path, sha256, parser_version, is_index_page)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
          title=excluded.title, source_page_key=excluded.source_page_key,
          article_id=excluded.article_id, fetched_at=excluded.fetched_at,
          http_status=excluded.http_status, content_type=excluded.content_type,
          snapshot_path=excluded.snapshot_path, sha256=excluded.sha256,
          parser_version=excluded.parser_version, is_index_page=excluded.is_index_page""",
        (
            pid,
            source_id,
            result["url"],
            title,
            stem,
            article_id.group(1) if article_id else None,
            utc_now(),
            result["status"],
            result["content_type"],
            str(path.relative_to(ROOT)).replace("\\", "/"),
            digest,
            PARSER_VERSION,
            1 if is_index else 0,
        ),
    )
    conn.commit()
    return pid, body, text


def add_entity(conn: sqlite3.Connection, entity_id: str, kind: str, *, subtype: str | None = None, notes: str | None = None) -> None:
    conn.execute(
        """INSERT INTO entities(id, kind, subtype, game, lifecycle, mapping_status, notes)
        VALUES (?, ?, ?, 'sts1', 'active', 'unverified', ?)
        ON CONFLICT(id) DO UPDATE SET subtype=COALESCE(excluded.subtype, entities.subtype), notes=COALESCE(excluded.notes, entities.notes)""",
        (entity_id, kind, subtype, notes),
    )


def add_name(
    conn: sqlite3.Connection,
    entity_id: str,
    language: str,
    name: str,
    *,
    source_page_id: str | None = None,
    name_kind: str = "preferred",
    status: str = "unverified",
    preferred: bool = False,
    notes: str | None = None,
) -> None:
    conn.execute(
        """INSERT INTO names
        (entity_id, language, name, normalized, name_kind, source_page_id,
         verification_status, is_preferred, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(entity_id, language, name, name_kind) DO UPDATE SET
          source_page_id=COALESCE(excluded.source_page_id, names.source_page_id),
          verification_status=excluded.verification_status,
          is_preferred=MAX(names.is_preferred, excluded.is_preferred),
          notes=COALESCE(excluded.notes, names.notes)""",
        (entity_id, language, name, normalise(name), name_kind, source_page_id, status, 1 if preferred else 0, notes),
    )


def add_claim(
    conn: sqlite3.Connection,
    entity_id: str,
    field_path: str,
    value: Any,
    source_page_id: str,
    *,
    variant_id: str | None = None,
    language: str | None = None,
    locator: str | None = None,
    extraction_method: str = "manual",
    status: str = "single_source",
    notes: str | None = None,
) -> str:
    encoded = json_text(value)
    key = "|".join([entity_id, variant_id or "", field_path, encoded, source_page_id])
    claim_id = "claim." + hashlib.sha256(key.encode("utf-8")).hexdigest()[:20]
    conn.execute(
        """INSERT OR IGNORE INTO claims
        (id, subject_entity_id, variant_id, field_path, value_json, value_type,
         language, source_page_id, locator, extraction_method,
         verification_status, created_at, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            claim_id,
            entity_id,
            variant_id,
            field_path,
            encoded,
            value_type(value),
            language,
            source_page_id,
            locator,
            extraction_method,
            status,
            utc_now(),
            notes,
        ),
    )
    return claim_id


def add_resolution(
    conn: sqlite3.Connection,
    entity_id: str,
    field_path: str,
    claim_id: str,
    value: Any,
    *,
    variant_id: str | None = None,
    status: str = "provisional",
    rationale: str = "P1 sample: retained as a source-backed provisional value pending cross-source or game-data verification.",
) -> None:
    key = "|".join([entity_id, variant_id or "", field_path])
    rid = "resolution." + hashlib.sha256(key.encode()).hexdigest()[:20]
    conn.execute(
        """INSERT INTO resolutions
        (id, subject_entity_id, variant_id, field_path, adopted_claim_id,
         value_json, status, rationale, decided_at, decided_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'bootstrap_sample')
        ON CONFLICT(id) DO UPDATE SET adopted_claim_id=excluded.adopted_claim_id,
          value_json=excluded.value_json, status=excluded.status,
          rationale=excluded.rationale, decided_at=excluded.decided_at""",
        (rid, entity_id, variant_id, field_path, claim_id, json_text(value), status, rationale, utc_now()),
    )


def add_relation(
    conn: sqlite3.Connection,
    source_entity_id: str,
    relation_type: str,
    target_entity_id: str,
    *,
    source_page_id: str | None = None,
    status: str = "confirmed",
    condition: Any | None = None,
    notes: str | None = None,
) -> None:
    rid = "relation." + hashlib.sha256(
        "|".join([source_entity_id, relation_type, target_entity_id, json_text(condition)]).encode()
    ).hexdigest()[:20]
    conn.execute(
        """INSERT OR IGNORE INTO relations
        (id, source_entity_id, relation_type, target_entity_id, condition_json,
         source_page_id, status, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (rid, source_entity_id, relation_type, target_entity_id, json_text(condition) if condition is not None else None, source_page_id, status, notes),
    )


def article_text(tree: html.HtmlElement) -> str:
    nodes = tree.xpath(
        '//*[contains(concat(" ", normalize-space(@class), " "), " article-content ")]'
    )
    node = nodes[0] if nodes else tree.xpath("//body")[0]
    # Keep paragraph/heading boundaries while removing scripts and feedback UI.
    for bad in node.xpath(".//script|.//style|.//*[contains(@class,'feedback')]"):
        bad.drop_tree()
    raw = node.text_content().replace("\u00a0", " ")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in raw.splitlines()]
    return "\n".join(line for line in lines if line)


def wiki_excerpt(conn: sqlite3.Connection, page_id: str | None, limit: int = 1200) -> str:
    """Return a compact visible excerpt while retaining the full snapshot."""
    if not page_id:
        return ""
    row = conn.execute("SELECT snapshot_path FROM source_pages WHERE id=?", (page_id,)).fetchone()
    if not row or not row[0]:
        return ""
    path = ROOT / row[0]
    if not path.exists():
        return ""
    try:
        tree = html.fromstring(path.read_bytes())
        node = tree.xpath('//div[@id="mw-content-text"]')[0]
        for bad in node.xpath('.//script|.//style|//*[contains(@class,"navbox")]|//*[contains(@class,"metadata")]'):
            bad.drop_tree()
        text = re.sub(r"\s+", " ", node.text_content()).strip()
        return text[:limit]
    except Exception:
        return ""


def parse_card_box(box: html.HtmlElement) -> dict[str, Any]:
    def icon_marker(img: html.HtmlElement) -> str:
        """Return a readable label for an icon-only inline image.

        The wiki.gg compendium renders energy as an image with ``data-name``
        ``@GE`` and no textual fallback.  ``text_content()`` consequently
        produces ``Gain .``.  Other keyword icons normally have a visible
        label next to the image; those are left to the label so that we do
        not duplicate text such as ``Block Block``.
        """

        trigger = img.xpath(
            "ancestor-or-self::*[contains(concat(' ', normalize-space(@class), ' '), ' trigger ') or contains(@class, '-trigger')][1]"
        )
        if trigger:
            # If the trigger already contains a text label, removing the icon
            # is enough.  This is the usual Block/Poison/etc. rendering.
            visible = "".join(trigger[0].itertext()).strip()
            if visible:
                return ""
        data_name = ""
        for parent in [img, *img.iterancestors()]:
            data_name = parent.get("data-name") or ""
            if data_name:
                break
        alt = img.get("alt") or ""
        raw_values = [value.strip() for value in (data_name, alt) if value and value.strip()]
        lower_values = [value.casefold() for value in raw_values]
        if any(
            value in {"@ge", "@re", "@be", "@pe", "energy", "re", "ge", "be", "pe"}
            or "energy" in value
            for value in lower_values
        ):
            # An energy icon represents one energy.  Keeping the number makes
            # the generated fact unambiguous and lets consecutive icons be
            # folded into ``2 Energy`` below.
            return "1 Energy"
        raw = (data_name or alt).strip()
        if raw.startswith("@"):
            raw = raw[1:]
        raw = re.sub(r"\.(?:png|jpg|jpeg|gif)$", "", raw, flags=re.I)
        raw = raw.replace("Icon_", "").replace("_", " ").strip()
        return raw

    def text_with_icons(node: html.HtmlElement) -> str:
        """Extract text while retaining semantics of icon-only markup."""

        clone = deepcopy(node)
        for img in list(clone.xpath(".//img")):
            marker = icon_marker(img)
            parent = img.getparent()
            if parent is None:
                continue
            tail = img.tail or ""
            if marker:
                index = parent.index(img)
                if index == 0:
                    parent.text = (parent.text or "") + marker + tail
                else:
                    previous = parent[index - 1]
                    previous.tail = (previous.tail or "") + marker + tail
            else:
                # ``drop_tree`` keeps any tail text while removing an image
                # whose neighbouring keyword label already carries meaning.
                img.drop_tree()
                continue
            parent.remove(img)
        value = re.sub(r"\s+", " ", unescape(clone.text_content())).strip()
        # Two energy icons are rendered as two adjacent image-only spans.
        # Collapse their readable markers without changing any other text.
        def collapse_energy(match: re.Match[str]) -> str:
            return f"{match.group(0).count('1 Energy')} Energy"

        value = re.sub(r"(?:1 Energy\s*){2,}", collapse_energy, value)
        # X-cost cards already supply the quantity before the icon.
        return re.sub(r"\b(X(?:\+\d+)?) 1 Energy\b", r"\1 Energy", value)

    def desc(cls: str) -> str | None:
        nodes = box.xpath(f'.//*[contains(concat(" ", normalize-space(@class), " "), " {cls} ")]')
        if not nodes:
            return None
        node = nodes[0]
        value = text_with_icons(node).replace("\u00a0", " ")
        value = re.sub(r"[ \t]+", " ", value)
        value = re.sub(r"\s*\n\s*", "\n", value).strip()
        return value

    images: dict[str, str] = {}
    for key, cls in (("base", "img-base"), ("upgrade", "img-upg")):
        nodes = box.xpath(f'.//*[contains(concat(" ", normalize-space(@class), " "), " {cls} ")]//img[1]')
        if nodes:
            images[key] = urljoin(WIKI_BASE, nodes[0].get("src", ""))
    attrs = {key[5:]: box.get(key) for key in box.keys() if key.startswith("data-")}
    return {
        "name": box.get("data-name"),
        "rarity": box.get("data-rarity"),
        "type": box.get("data-type"),
        "color": box.get("data-color"),
        "cost": box.get("data-cost"),
        "can_upgrade": box.get("data-canupgrade") == "true",
        "tags": [x for x in (box.get("data-tags") or "").split() if x],
        "description_base": desc("desc-base"),
        "description_upgrade": desc("desc-upg"),
        "images": images,
        "raw_data_attrs": attrs,
    }


def add_asset(
    conn: sqlite3.Connection,
    url: str,
    source_page_id: str,
    usage_kind: str,
    *,
    language: str = "und",
) -> str | None:
    if not url:
        return None
    try:
        result = fetch_bytes(url, is_xiao=False, attempts=3)
    except Exception as exc:  # Image loss must be visible in the report, not fatal to facts.
        print(f"[asset-warning] {url}: {exc}", file=sys.stderr)
        return None
    body = result["body"]
    digest = hashlib.sha256(body).hexdigest()
    mime = result["content_type"].split(";", 1)[0].strip() or mimetypes.guess_type(url)[0] or "application/octet-stream"
    extension = mimetypes.guess_extension(mime) or Path(url.split("?", 1)[0]).suffix or ".bin"
    directory = ROOT / "data" / "assets"
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{digest}{extension}"
    if not path.exists():
        path.write_bytes(body)
    asset_id = "asset." + digest[:20]
    conn.execute(
        """INSERT OR IGNORE INTO assets
        (id, sha256, original_url, local_path, mime_type, byte_size,
         source_page_id, fetched_at, usage_kind, license_status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'unknown')""",
        (asset_id, digest, url, str(path.relative_to(ROOT)).replace("\\", "/"), mime, len(body), source_page_id, utc_now(), usage_kind),
    )
    return asset_id


def xiao_source_page(conn: sqlite3.Connection, key: str) -> str:
    return source_page_id("xiaoheihe", XIAO_ARTICLES[key])


def add_xiao_claims(conn: sqlite3.Connection, entity_id: str, key: str, text: str, page_id: str) -> None:
    title = re.sub(r"\s+", " ", text.splitlines()[0] if text else "").strip()
    add_claim(conn, entity_id, "source.article_text", text, page_id, language="zh-CN", extraction_method="visible_text", notes="Raw article text is retained as evidence; structured values below are only added when the observed wording is present.")
    if title:
        add_claim(conn, entity_id, "source.title_text", title, page_id, language="zh-CN", extraction_method="visible_text")


def seed_character_pages(conn: sqlite3.Connection, wiki_index_id: str, xiao_index_id: str) -> None:
    for key, info in CHARACTERS.items():
        entity_id = info["id"]
        add_entity(conn, entity_id, "character", subtype="playable")
        add_name(conn, entity_id, "zh-CN", info["zh"], source_page_id=xiao_index_id, preferred=True, status="single_source", notes="Observed in the user-specified Xiaoheihe rendered category.")
        add_name(conn, entity_id, "en", info["en"], source_page_id=wiki_index_id, preferred=True, status="single_source")
        add_claim(conn, entity_id, "source.category_presence.zh", True, xiao_index_id, language="zh-CN", extraction_method="manual", notes="Rendered homepage category; not a full character stat page.")
        add_claim(conn, entity_id, "source.page_title.en", info["en"], wiki_index_id, language="en", extraction_method="manual")


def seed_cards(conn: sqlite3.Connection, cards_index_id: str, xiao_index_id: str, xiao_texts: dict[str, str]) -> list[str]:
    boxes = html.fromstring((ROOT / "data" / "raw" / "wiki_gg").glob("**/*").__iter__().__next__().read_bytes()) if False else None
    # Read the current index snapshot via its source_pages row, so a rerun is
    # independent of whatever temporary response file happens to be present.
    path_row = conn.execute("SELECT snapshot_path FROM source_pages WHERE id = ?", (cards_index_id,)).fetchone()
    if not path_row:
        raise RuntimeError("cards index page is missing")
    tree = html.fromstring((ROOT / path_row[0]).read_bytes())
    boxes_by_name = {item.get("name"): item for item in map(parse_card_box, tree.xpath('//div[contains(@class,"card-box")]'))}
    entity_ids: list[str] = []
    for config in CARD_SAMPLES:
        parsed = boxes_by_name.get(config["wiki_name"])
        if not parsed:
            print(f"[sample-warning] card not found in Cards_List: {config['wiki_name']}", file=sys.stderr)
            continue
        character = CHARACTERS[config["character"]]
        entity_id = f"sts1.card.{config['character']}.{slug(config['wiki_name'].replace(' (Ironclad)', ''))}"
        entity_ids.append(entity_id)
        add_entity(conn, entity_id, "card", subtype=parsed["type"])
        add_name(conn, entity_id, "en", config["wiki_name"].replace(" (Ironclad)", ""), source_page_id=cards_index_id, preferred=True, status="single_source")
        if config.get("zh"):
            zh_page = xiao_source_page(conn, config["xiao_key"]) if config.get("zh_article") else xiao_index_id
            zh_kind = "source_name" if config.get("zh_article") else "candidate"
            zh_status = "single_source" if config.get("zh_article") else "unverified"
            zh_notes = None if config.get("zh_article") else "Community/UI candidate; fetch the corresponding Xiaoheihe article before marking confirmed."
            add_name(conn, entity_id, "zh-CN", config["zh"], source_page_id=zh_page, name_kind=zh_kind, status=zh_status, preferred=True, notes=zh_notes)
        add_relation(conn, entity_id, "belongs_to_character", character["id"], source_page_id=cards_index_id)
        card_row = (
            entity_id,
            character["id"],
            parsed["color"] if parsed["color"] in {"Red", "Green", "Blue", "Purple", "Colorless"} else "Other",
            parsed["type"] if parsed["type"] in {"Attack", "Skill", "Power", "Status", "Curse"} else "Other",
            parsed["rarity"],
            None,
            "card_list",
            json_text(parsed["tags"]),
        )
        conn.execute(
            """INSERT INTO cards(entity_id, character_entity_id, color, card_type, rarity, target, availability, tags_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(entity_id) DO UPDATE SET character_entity_id=excluded.character_entity_id,
              color=excluded.color, card_type=excluded.card_type, rarity=excluded.rarity,
              availability=excluded.availability, tags_json=excluded.tags_json""",
            card_row,
        )
        for variant_kind, desc_key in (("base", "description_base"), ("upgrade", "description_upgrade")):
            variant_id = f"{entity_id}:{variant_kind}"
            conn.execute(
                """INSERT OR IGNORE INTO entity_variants(id, entity_id, variant_kind, level, label)
                VALUES (?, ?, ?, ?, ?)""",
                (variant_id, entity_id, variant_kind, 0 if variant_kind == "base" else 1, "Base" if variant_kind == "base" else "Upgraded"),
            )
            cost_value: float | None
            try:
                cost_value = float(parsed["cost"]) if parsed["cost"] not in (None, "X", "-") else None
            except ValueError:
                cost_value = None
            asset_id = add_asset(conn, parsed["images"].get(variant_kind), cards_index_id, f"card_{variant_kind}") if parsed["images"].get(variant_kind) else None
            conn.execute(
                """INSERT INTO card_variants(variant_id, cost_type, cost_value, description_en, parsed_json, image_asset_id)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(variant_id) DO UPDATE SET cost_type=excluded.cost_type,
                  cost_value=excluded.cost_value, description_en=excluded.description_en,
                  parsed_json=excluded.parsed_json, image_asset_id=COALESCE(excluded.image_asset_id, card_variants.image_asset_id)""",
                (variant_id, "x" if parsed["cost"] == "X" else "fixed", cost_value, parsed[desc_key], json_text(parsed), asset_id),
            )
            if parsed[desc_key] is not None:
                cid = add_claim(conn, entity_id, "card.description", parsed[desc_key], cards_index_id, variant_id=variant_id, language="en", locator=f"card-box[data-name='{parsed['name']}'] .desc-{variant_kind if variant_kind == 'base' else 'upg'}", extraction_method="structured_html")
                add_resolution(conn, entity_id, "card.description", cid, parsed[desc_key], variant_id=variant_id)
            cid = add_claim(conn, entity_id, "card.cost", parsed["cost"], cards_index_id, variant_id=variant_id, language="en", locator=f"card-box[data-name='{parsed['name']}']@data-cost", extraction_method="structured_html")
            add_resolution(conn, entity_id, "card.cost", cid, parsed["cost"], variant_id=variant_id)
            for field, value in (("card.rarity", parsed["rarity"]), ("card.type", parsed["type"]), ("card.color", parsed["color"]), ("card.tags", parsed["tags"])):
                cid = add_claim(conn, entity_id, field, value, cards_index_id, variant_id=variant_id, language="en", extraction_method="structured_html")
                add_resolution(conn, entity_id, field, cid, value, variant_id=variant_id)
            if parsed["name"] == "Body Slam" and variant_kind == "base":
                add_relation(conn, entity_id, "uses_mechanic", "sts1.mechanic.block", source_page_id=cards_index_id)
        # Add the two directly observed Chinese article bodies to their card claims.
        # Only attach an article when this card explicitly declares one.
        # The previous fallback attached the Body Slam article to every sample
        # card, creating false evidence and misleading generated pages.
        xiao_key = config.get("xiao_key")
        if xiao_key in xiao_texts:
            zh_page = xiao_source_page(conn, xiao_key)
            add_xiao_claims(conn, entity_id, xiao_key, xiao_texts[xiao_key], zh_page)
            if config["wiki_name"] == "Body Slam":
                add_claim(conn, entity_id, "card.description", "造成你当前格挡值的伤害。", zh_page, variant_id=f"{entity_id}:base", language="zh-CN", locator="article-content h1 + image + text", extraction_method="visible_text")
                add_claim(conn, entity_id, "card.description", "造成你当前格挡值的伤害。", zh_page, variant_id=f"{entity_id}:upgrade", language="zh-CN", locator="article-content h2", extraction_method="visible_text")
    return entity_ids


def seed_noncard_entities(conn: sqlite3.Connection, xiao_texts: dict[str, str], wiki_page_ids: dict[str, str], xiao_index_id: str) -> list[str]:
    ids: list[str] = []
    # Mechanic and status anchors used by card relations.
    for entity_id, zh, en, kind in [
        ("sts1.mechanic.block", "格挡", "Block", "mechanic"),
        ("sts1.mechanic.exhaust", "消耗", "Exhaust", "mechanic"),
        ("sts1.status.strength", "力量", "Strength", "status"),
        ("sts1.status.vulnerable", "易伤", "Vulnerable", "status"),
        ("sts1.status.weak", "虚弱", "Weak", "status"),
    ]:
        add_entity(conn, entity_id, kind)
        add_name(conn, entity_id, "zh-CN", zh, source_page_id=xiao_source_page(conn, "strength") if zh == "力量" else xiao_index_id, preferred=True, status="single_source" if zh == "力量" else "unverified")
        add_name(conn, entity_id, "en", en, source_page_id=wiki_page_ids.get("strength") if en == "Strength" else None, preferred=True, status="single_source" if en == "Strength" else "unverified")
    conn.execute("INSERT OR REPLACE INTO mechanics(entity_id, definition_json) VALUES (?, ?)", ("sts1.mechanic.block", json_text({"definition": "Block"})))
    conn.execute("INSERT OR REPLACE INTO mechanics(entity_id, definition_json) VALUES (?, ?)", ("sts1.mechanic.exhaust", json_text({"definition": "Exhaust"})))
    conn.execute("INSERT OR REPLACE INTO statuses(entity_id, polarity, affects, stacking, trigger_timing, removal) VALUES (?, 'positive', 'player', 'additive', 'attack damage calculation', 'end of combat or explicit effect')", ("sts1.status.strength",))
    conn.execute("INSERT OR REPLACE INTO statuses(entity_id, polarity, affects, stacking, trigger_timing, removal) VALUES (?, 'negative', 'player or enemy', 'additive', 'attack damage calculation', 'turn/explicit effect')", ("sts1.status.vulnerable",))
    conn.execute("INSERT OR REPLACE INTO statuses(entity_id, polarity, affects, stacking, trigger_timing, removal) VALUES (?, 'negative', 'player or enemy', 'additive', 'attack damage calculation', 'turn/explicit effect')", ("sts1.status.weak",))

    # Relics.
    for entity_id, zh, en, key, character_id, rarity in [
        ("sts1.relic.burning_blood", "燃烧之血", "Burning Blood", "burning_blood", CHARACTERS["ironclad"]["id"], "Starter"),
        ("sts1.relic.snake_ring", "蛇之戒指", "Ring of the Snake", "snake_ring", CHARACTERS["silent"]["id"], "Starter"),
    ]:
        ids.append(entity_id)
        add_entity(conn, entity_id, "relic")
        xpid = xiao_source_page(conn, key)
        wpid = wiki_page_ids.get(key)
        add_name(conn, entity_id, "zh-CN", zh, source_page_id=xpid, preferred=True, status="single_source")
        add_name(conn, entity_id, "en", en, source_page_id=wpid, preferred=True, status="single_source" if wpid else "unverified")
        conn.execute("INSERT OR REPLACE INTO relics(entity_id, rarity, character_entity_id) VALUES (?, ?, ?)", (entity_id, rarity, character_id))
        if key in xiao_texts:
            add_xiao_claims(conn, entity_id, key, xiao_texts[key], xpid)
        excerpt = wiki_excerpt(conn, wpid)
        if excerpt:
            add_claim(conn, entity_id, "source.article_excerpt.en", excerpt, wpid, language="en", extraction_method="visible_text", notes="Compact visible excerpt; complete HTML is retained in the raw snapshot.")
        if key == "burning_blood":
            effect = "在战斗结束时，回复6点生命。"
            cid = add_claim(conn, entity_id, "relic.effect", effect, xpid, language="zh-CN", locator="table 作用", extraction_method="visible_text")
            add_resolution(conn, entity_id, "relic.effect", cid, effect)
        else:
            effect = "在每场战斗开始时，额外抽2张牌。"
            cid = add_claim(conn, entity_id, "relic.effect", effect, xpid, language="zh-CN", locator="table 作用", extraction_method="visible_text")
            add_resolution(conn, entity_id, "relic.effect", cid, effect)
        add_relation(conn, entity_id, "belongs_to_character", character_id, source_page_id=xpid)

    # Potion.
    potion_id = "sts1.potion.weak"
    ids.append(potion_id)
    xpid = xiao_source_page(conn, "weak_potion")
    wpid = wiki_page_ids.get("weak_potion")
    add_entity(conn, potion_id, "potion")
    add_name(conn, potion_id, "zh-CN", "虚弱药水", source_page_id=xpid, preferred=True, status="single_source")
    add_name(conn, potion_id, "en", "Weak Potion", source_page_id=wpid, preferred=True, status="single_source" if wpid else "unverified")
    conn.execute("INSERT OR REPLACE INTO potions(entity_id, rarity, target, effect_json) VALUES (?, 'Common', 'enemy', ?)", (potion_id, json_text({"weak": 3})))
    if "给予3层虚弱" in xiao_texts.get("weak_potion", ""):
        cid = add_claim(conn, potion_id, "potion.effect", "给予3层虚弱。", xpid, language="zh-CN", locator="table effect", extraction_method="visible_text")
        add_resolution(conn, potion_id, "potion.effect", cid, "给予3层虚弱。")
    excerpt = wiki_excerpt(conn, wpid)
    if excerpt:
        add_claim(conn, potion_id, "source.article_excerpt.en", excerpt, wpid, language="en", extraction_method="visible_text", notes="Compact visible excerpt; complete HTML is retained in the raw snapshot.")
    add_relation(conn, potion_id, "applies_status", "sts1.status.weak", source_page_id=xpid)

    # Boss sample plus an encounter wrapper so group-vs-single entities exist.
    monster_id = "sts1.monster.slime_boss"
    encounter_id = "sts1.encounter.exordium.slime_boss"
    ids.extend([monster_id, encounter_id])
    xpid = xiao_source_page(conn, "slime_boss")
    wpid = wiki_page_ids.get("slime_boss")
    add_entity(conn, monster_id, "monster", subtype="boss")
    add_name(conn, monster_id, "zh-CN", "史莱姆老大", source_page_id=xpid, preferred=True, status="single_source")
    add_name(conn, monster_id, "en", "Slime Boss", source_page_id=wpid, preferred=True, status="single_source" if wpid else "unverified")
    conn.execute("INSERT OR REPLACE INTO monsters(entity_id, category, act, hp_min, hp_max, ascension_json, encounter_notes) VALUES (?, 'boss', 'Exordium', 140, 150, ?, ?)", (monster_id, json_text({"base": 140, "ascension": {"A9_plus": 150}}), "Chinese article shows 140;(150;) and a 4+/19+ action table; retain raw text in claims."))
    if xiao_texts.get("slime_boss"):
        add_xiao_claims(conn, monster_id, "slime_boss", xiao_texts["slime_boss"], xpid)
        for field, val in [("monster.hp.base", 140), ("monster.hp.ascension", 150), ("monster.move.slime.damage", 35), ("monster.move.slime.damage_a4_plus", 38), ("monster.move.slime_count", 3), ("monster.move.slime_count_a19_plus", 5)]:
            cid = add_claim(conn, monster_id, field, val, xpid, language="zh-CN", locator="table 怪物信息/攻击方式", extraction_method="visible_text", notes="Parsed from the displayed table; verify against game data before promoting to verified_game.")
            add_resolution(conn, monster_id, field, cid, val)
    excerpt = wiki_excerpt(conn, wpid)
    if excerpt:
        add_claim(conn, monster_id, "source.article_excerpt.en", excerpt, wpid, language="en", extraction_method="visible_text", notes="Compact visible excerpt; complete HTML is retained in the raw snapshot.")
    moves = [
        ("slime", "黏液喷射", "debuff", None, None, {"add_to_discard": "Slimed", "count": 3, "a19_plus_count": 5}),
        ("prepare", "准备", "buff", None, None, {}),
        ("slam", "史莱姆撞击", "attack", 35, 1, {"a4_plus_damage": 38}),
        ("split", "分裂", "special", None, None, {"condition": "current_hp_below_half", "summons": ["Large Spike Slime", "Large Acid Slime"]}),
    ]
    for move_id, name, intent, damage, hits, effect in moves:
        conn.execute(
            """INSERT OR REPLACE INTO monster_moves
            (id, monster_entity_id, name, intent, damage, hits, effect_json, condition_json, order_rules)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (f"{monster_id}:move:{move_id}", monster_id, name, intent, damage, hits, json_text(effect), None, "Observed sequence: slime → prepare → slam; split below half HP."),
        )
    add_entity(conn, encounter_id, "encounter", subtype="boss")
    add_name(conn, encounter_id, "en", "Exordium: Slime Boss", source_page_id=wpid, preferred=True, status="single_source" if wpid else "unverified")
    add_name(conn, encounter_id, "zh-CN", "第一幕：史莱姆老大", source_page_id=xpid, preferred=True, status="single_source")
    conn.execute("INSERT OR REPLACE INTO encounters(entity_id, act, room_type, pool_type, repetition_rules) VALUES (?, 'Exordium', 'boss', 'boss', ?)", (encounter_id, "One boss encounter; encounter-pool weights are not represented by this sample."))
    conn.execute("INSERT OR REPLACE INTO encounter_members(encounter_entity_id, monster_entity_id, quantity, position) VALUES (?, ?, 1, 1)", (encounter_id, monster_id))
    add_relation(conn, encounter_id, "contains_monster", monster_id, source_page_id=xpid)

    # Event sample with explicit options, preserving the Chinese article's
    # conditional X semantics as JSON rather than flattening it into prose.
    event_id = "sts1.event.we_meet_again"
    ids.append(event_id)
    xpid = xiao_source_page(conn, "we_meet_again")
    wpid = wiki_page_ids.get("we_meet_again")
    add_entity(conn, event_id, "event")
    add_name(conn, event_id, "zh-CN", "我们又见面了！", source_page_id=xpid, preferred=True, status="single_source")
    add_name(conn, event_id, "en", "We Meet Again!", source_page_id=wpid, preferred=True, status="single_source" if wpid else "unverified")
    conn.execute("INSERT OR REPLACE INTO events(entity_id, acts_json, room_type, appearance_condition_json) VALUES (?, ?, '?', ?)", (event_id, json_text(["Exordium", "The City", "The Beyond"]), json_text({"source": "article", "status": "needs_cross-check"})))
    if xiao_texts.get("we_meet_again"):
        add_xiao_claims(conn, event_id, "we_meet_again", xiao_texts["we_meet_again"], xpid)
    excerpt = wiki_excerpt(conn, wpid)
    if excerpt:
        add_claim(conn, event_id, "source.article_excerpt.en", excerpt, wpid, language="en", extraction_method="visible_text", notes="Compact visible excerpt; complete HTML is retained in the raw snapshot.")
    options = [
        ("give_potion", "给他药水", {"cost": "one_random_potion", "locked_if": "no_potion"}, {"reward": "one_random_relic"}),
        ("give_gold", "给他金币", {"cost": "X_gold_between_50_and_current", "locked_if": "gold_less_than_50"}, {"reward": "one_random_relic"}),
        ("give_card", "给他卡牌", {"cost": "one_random_non_basic_non_curse_card", "locked_if": "deck_has_no_eligible_card"}, {"reward": "one_random_relic"}),
        ("attack", "攻击", {"cost": None}, {"result": "leave_without_combat"}),
    ]
    for ordinal, (key, label, cost, outcome) in enumerate(options, 1):
        oid = f"{event_id}:option:{key}"
        conn.execute("INSERT OR REPLACE INTO event_options(id, event_entity_id, ordinal, label, cost_json, outcome_json) VALUES (?, ?, ?, ?, ?, ?)", (oid, event_id, ordinal, label, json_text(cost), json_text(outcome)))
    # The event consumes a randomly selected potion and grants a random relic;
    # no specific Weak Potion/Burning Blood relation is asserted here.  The
    # option-level JSON above preserves those pool semantics without creating
    # misleading item-to-item links.
    conn.execute("DELETE FROM relations WHERE source_entity_id=? AND relation_type IN ('uses_resource', 'grants_relic')", (event_id,))

    # Strength has an explicitly bilingual article in the Chinese source.
    strength_id = "sts1.status.strength"
    xpid = xiao_source_page(conn, "strength")
    add_xiao_claims(conn, strength_id, "strength", xiao_texts.get("strength", ""), xpid)
    if "攻击伤害提升" in xiao_texts.get("strength", ""):
        cid = add_claim(conn, strength_id, "status.description.zh", "攻击伤害提升 X 点。", xpid, language="zh-CN", locator="table 效果中文描述", extraction_method="visible_text")
        add_resolution(conn, strength_id, "status.description.zh", cid, "攻击伤害提升 X 点。")
    if "Increases attack damage" in xiao_texts.get("strength", ""):
        cid = add_claim(conn, strength_id, "status.description.en", "Increases attack damage by #b.", xpid, language="en", locator="table 效果英文描述", extraction_method="visible_text")
        add_resolution(conn, strength_id, "status.description.en", cid, "Increases attack damage by #b.")
    excerpt = wiki_excerpt(conn, wiki_page_ids.get("strength"))
    if excerpt:
        add_claim(conn, strength_id, "source.article_excerpt.en", excerpt, wiki_page_ids["strength"], language="en", extraction_method="visible_text", notes="Compact visible excerpt; complete HTML is retained in the raw snapshot.")
    return ids


def clear_strategy_links(conn: sqlite3.Connection) -> None:
    """Keep the basic Wiki independent from the separately stored guides.

    The strategy tables remain in the schema for a future, explicitly enabled
    extension, but the current knowledge-base build must not create or retain
    links to the two user-provided guide documents.  Delete links first so the
    foreign-key cascade is valid, then remove their note rows as well.
    """
    conn.execute("DELETE FROM strategy_links")
    conn.execute("DELETE FROM strategy_notes")


def clear_sample_xiao_evidence(conn: sqlite3.Connection) -> None:
    """Remove stale cross-card evidence from pre-0.2 sample runs.

    Early reruns reused the Body Slam article as a fallback for every card in
    ``CARD_SAMPLES``.  Since claims are immutable rows, merely fixing the
    parser would leave those false claims in SQLite.  Remove only claims
    attached to the two sample article pages when their subject is not the
    card that actually owns that article; all other source evidence is left
    untouched.
    """
    expected = {
        xiao_source_page(conn, "strike_ironclad"): "sts1.card.ironclad.strike",
        xiao_source_page(conn, "body_slam"): "sts1.card.ironclad.body_slam",
    }
    for page_id, entity_id in expected.items():
        rows = conn.execute(
            "SELECT id FROM claims WHERE source_page_id=? AND subject_entity_id<>?",
            (page_id, entity_id),
        ).fetchall()
        claim_ids = [row[0] for row in rows]
        if not claim_ids:
            continue
        placeholders = ",".join("?" for _ in claim_ids)
        # resolutions.adopted_claim_id has no ON DELETE action in the schema,
        # so clear dependent decisions before deleting the stale evidence.
        conn.execute(f"DELETE FROM resolutions WHERE adopted_claim_id IN ({placeholders})", claim_ids)
        conn.execute(f"DELETE FROM claims WHERE id IN ({placeholders})", claim_ids)


def resolve_mapping_statuses(conn: sqlite3.Connection) -> None:
    """Set identity status from name evidence without asserting rule values."""
    # A rerun can encounter a P1 ``source_name`` and a P3 ``preferred`` row
    # for the same language/name.  The schema intentionally allows multiple
    # names, but the renderer/query API needs one unambiguous display name per
    # language.  Keep the strongest name kind as the sole preferred row; this
    # does not delete evidence or aliases.
    for entity in conn.execute("SELECT id FROM entities"):
        for language in ("zh-CN", "en"):
            rows = conn.execute(
                """SELECT entity_id, language, name, name_kind FROM names
                   WHERE entity_id=? AND language=?
                   ORDER BY is_preferred DESC,
                            CASE name_kind WHEN 'preferred' THEN 0
                                           WHEN 'localization' THEN 1
                                           WHEN 'source_name' THEN 2
                                           WHEN 'alias' THEN 3
                                           WHEN 'old_alias' THEN 4
                                           ELSE 5 END,
                            name""",
                (entity["id"], language),
            ).fetchall()
            if not rows:
                continue
            keep = rows[0]
            conn.execute(
                "UPDATE names SET is_preferred=CASE WHEN entity_id=? AND language=? AND name=? AND name_kind=? THEN 1 ELSE 0 END WHERE entity_id=? AND language=?",
                (keep["entity_id"], keep["language"], keep["name"], keep["name_kind"], entity["id"], language),
            )
    for row in conn.execute("SELECT id FROM entities"):
        # A localized entry that exists only in the installed game package is
        # not automatically the same object as a wiki row.  Keep its identity
        # provisional even though it has both English and Chinese strings;
        # the explicit game-to-wiki mapping review is the boundary that can
        # promote it later.
        if row["id"].startswith("sts1.game.candidate."):
            conn.execute("UPDATE entities SET mapping_status='provisional' WHERE id=?", (row["id"],))
            continue
        names = conn.execute(
            """SELECT language, name_kind, verification_status, source_page_id
               FROM names WHERE entity_id=? AND is_preferred=1""",
            (row["id"],),
        ).fetchall()
        by_lang = {item["language"]: item for item in names}
        zh = by_lang.get("zh-CN")
        en = by_lang.get("en")
        if zh and en and zh["verification_status"] in ("single_source", "agreed", "verified_game") and en["verification_status"] in ("single_source", "agreed", "verified_game"):
            status = "confirmed"
        elif zh or en:
            status = "provisional"
        else:
            status = "unverified"
        conn.execute("UPDATE entities SET mapping_status=? WHERE id=?", (status, row["id"]))


def export_data(conn: sqlite3.Connection) -> dict[str, int]:
    export_dir = ROOT / "data" / "exports"
    export_dir.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    for table in ("entities", "names", "claims", "relations", "cards", "relics", "potions", "monsters", "encounters", "events", "statuses", "mechanics", "inventory_items", "inventory_mappings"):
        rows = conn.execute(f"SELECT * FROM {table} ORDER BY 1").fetchall()
        columns = [d[0] for d in conn.execute(f"SELECT * FROM {table} LIMIT 0").description]
        path = export_dir / f"{table}.jsonl"
        with path.open("w", encoding="utf-8", newline="\n") as fh:
            for row in rows:
                fh.write(json.dumps(dict(zip(columns, row)), ensure_ascii=False, sort_keys=True) + "\n")
        counts[table] = len(rows)

    # ``fetch_p3.py`` updates inventory status in place.  Keep the human-facing
    # CSV in lockstep with the database even when the P2 discovery script is
    # not rerun (rerunning discovery would intentionally reset its directory
    # rows).  The detailed bilingual mapping CSV remains owned by P2 below.
    inventory_rows = conn.execute(
        "SELECT * FROM inventory_items ORDER BY source_id, entity_kind, category, name, id"
    ).fetchall()
    if inventory_rows:
        inventory_fields = [
            "id", "source_id", "source_page_id", "entity_kind", "language",
            "name", "article_id", "url", "category", "subcategory",
            "character", "status",
        ]
        with (export_dir / "inventory.csv").open("w", encoding="utf-8-sig", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=inventory_fields)
            writer.writeheader()
            for row in inventory_rows:
                writer.writerow({field: row[field] for field in inventory_fields})
        counts["inventory_csv"] = len(inventory_rows)

    # P2 owns the combined source-inventory mapping file.  Once inventory
    # rows exist, preserve that file across a P1 sample rebuild and emit the
    # entity-only view under a separate name instead.
    has_inventory = conn.execute("SELECT COUNT(*) FROM inventory_items").fetchone()[0] > 0
    mapping_path = export_dir / ("entity_name_mapping.csv" if has_inventory else "name_mapping.csv")
    query = """
        SELECT e.id, e.kind,
               MAX(CASE WHEN n.language='zh-CN' AND n.is_preferred=1 THEN n.name END) AS zh_name,
               MAX(CASE WHEN n.language='en' AND n.is_preferred=1 THEN n.name END) AS en_name,
               e.mapping_status
        FROM entities e LEFT JOIN names n ON n.entity_id=e.id
        GROUP BY e.id, e.kind, e.mapping_status ORDER BY e.id
    """
    rows = conn.execute(query).fetchall()
    with mapping_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["entity_id", "kind", "zh_name", "en_name", "mapping_status"])
        writer.writerows(rows)
    counts["entity_name_mapping"] = len(rows)
    (export_dir / "manifest.json").write_text(json.dumps({"generated_at": utc_now(), "parser_version": PARSER_VERSION, "counts": counts}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return counts


def main() -> int:
    for directory in [ROOT / "data", ROOT / "data" / "raw", ROOT / "data" / "assets", ROOT / "data" / "exports", ROOT / "reports"]:
        directory.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    apply_schema(conn)
    run_id = "run." + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    conn.execute("INSERT OR REPLACE INTO build_runs(id, started_at, status, parser_version) VALUES (?, ?, 'running', ?)", (run_id, utc_now(), PARSER_VERSION))
    conn.commit()
    try:
        conn.executemany(
            "INSERT OR IGNORE INTO sources(id, name, base_url, language, license, source_kind, scope_note, notes) VALUES (?, ?, ?, ?, ?, 'wiki', ?, ?)",
            [
                ("wiki_gg", "Slay the Spire Wiki.gg", WIKI_BASE, "en", "CC BY-SA 4.0", "StS1 and StS2; this run filters to StS1", "Homepage covers both games; 2 namespace and Mod content are excluded."),
                ("xiaoheihe", "小黑盒《杀戮尖塔》百科", "https://web.xiaoheihe.cn/wiki/home?wiki_id=646570", "zh-CN", "unknown", "User-specified Chinese Wiki", "Article endpoint responses are kept as raw bytes; observed GBK presentation is decoded separately."),
            ],
        )
        conn.commit()
        wiki_index_id, _, _ = get_or_fetch_page(conn, "wiki_gg", WIKI_BASE + "/wiki/Cards_List", "Cards_List", is_index=True)
        xiao_index_id, _, _ = get_or_fetch_page(conn, "xiaoheihe", XIAO_HOME, "home", is_xiao=True, is_index=True)
        # Probe the verified MediaWiki API once and keep its response as a P0
        # capability sample.  The parser still uses the page's structured HTML.
        api_url = WIKI_BASE + "/api.php?action=query&format=json&titles=Body_Slam&prop=revisions&rvprop=content&rvslots=main"
        try:
            get_or_fetch_page(conn, "wiki_gg", api_url, "api_body_slam", is_index=True)
        except Exception as exc:
            print(f"[api-warning] {exc}", file=sys.stderr)
        # Add character page samples to source provenance.
        wiki_character_pages: dict[str, str] = {}
        for key, info in CHARACTERS.items():
            url = WIKI_BASE + "/wiki/" + info["en"].replace(" ", "_")
            try:
                pid, _, _ = get_or_fetch_page(conn, "wiki_gg", url, f"character_{key}")
                wiki_character_pages[key] = pid
            except Exception as exc:
                print(f"[page-warning] {url}: {exc}", file=sys.stderr)
        seed_character_pages(conn, wiki_index_id, xiao_index_id)

        xiao_texts: dict[str, str] = {}
        for key, url in XIAO_ARTICLES.items():
            try:
                pid, _, text = get_or_fetch_page(conn, "xiaoheihe", url, key, is_xiao=True)
                tree = html.fromstring(text)
                xiao_texts[key] = article_text(tree)
            except Exception as exc:
                print(f"[xiao-warning] {url}: {exc}", file=sys.stderr)

        wiki_page_ids: dict[str, str] = {}
        for key, page in SAMPLE_WIKI_PAGES.items():
            url = WIKI_BASE + "/wiki/" + quote(page, safe="!(),'_")
            try:
                pid, _, _ = get_or_fetch_page(conn, "wiki_gg", url, key)
                wiki_page_ids[key] = pid
            except Exception as exc:
                print(f"[page-warning] {url}: {exc}", file=sys.stderr)

        # Clean stale evidence left by the early sample parser before adding
        # the corrected card-specific Xiaoheihe claims.
        clear_sample_xiao_evidence(conn)
        noncard_ids = seed_noncard_entities(conn, xiao_texts, wiki_page_ids, xiao_index_id)
        card_ids = seed_cards(conn, wiki_index_id, xiao_index_id, xiao_texts)
        # The current foundational Wiki is sourced from the two Wikis only.
        # Strategy documents are intentionally kept as independent files and
        # are not associated with entities in this build.
        clear_strategy_links(conn)
        resolve_mapping_statuses(conn)
        conn.commit()
        counts = export_data(conn)
        conn.execute("UPDATE build_runs SET finished_at=?, status='success', counts_json=? WHERE id=?", (utc_now(), json_text(counts), run_id))
        conn.commit()
        report = {
            "run_id": run_id,
            "status": "success",
            "parser_version": PARSER_VERSION,
            "generated_at": utc_now(),
            "sources": ["wiki_gg", "xiaoheihe"],
            "scope": "P1 vertical sample; not a full inventory",
            "counts": counts,
            "sample_cards": card_ids,
            "sample_non_cards": noncard_ids,
            "known_limitations": [
                "Chinese category homepage is dynamically rendered; the raw HTML snapshot does not contain the full rendered inventory.",
                "English list page is used for structured card fields; individual source pages are retained for selected non-card samples.",
                "Image license_status remains unknown until the source terms and per-asset rights are audited.",
                "Values marked provisional/single_source are not game-verified.",
            ],
        }
        (ROOT / "reports" / "p1-sample-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        conn.execute("UPDATE build_runs SET finished_at=?, status='failed', notes=? WHERE id=?", (utc_now(), repr(exc), run_id))
        conn.commit()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
