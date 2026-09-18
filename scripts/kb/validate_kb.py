"""Validate referential integrity and generated links for the local KB."""

from __future__ import annotations

import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "spire.sqlite"
WIKI_ROOT = ROOT / "docs" / "wiki"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


EXPORT_TABLES = (
    "sources",
    "source_pages",
    "entities",
    "names",
    "claims",
    "relations",
    "resolutions",
    "entity_variants",
    "card_variants",
    "monster_moves",
    "event_options",
    "encounter_members",
    "assets",
    "entity_assets",
    "cards",
    "relics",
    "potions",
    "monsters",
    "encounters",
    "events",
    "statuses",
    "keywords",
    "mechanics",
    "inventory_items",
    "inventory_mappings",
    "strategy_notes",
    "strategy_links",
)


def jsonl_count(path: Path) -> int | None:
    try:
        return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    except OSError:
        return None


def jsonl_rows(path: Path) -> list[dict] | None:
    try:
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, json.JSONDecodeError):
        return None


def main() -> int:
    if not DB_PATH.exists():
        raise SystemExit("data/spire.sqlite not found")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    errors: list[str] = []
    warnings: list[str] = []

    fk = conn.execute("PRAGMA foreign_key_check").fetchall()
    errors.extend("foreign_key_check: " + repr(tuple(row)) for row in fk)

    for row in conn.execute("SELECT id, snapshot_path FROM source_pages"):
        if not row["snapshot_path"] or not (ROOT / row["snapshot_path"]).exists():
            errors.append(f"missing source snapshot: {row['id']} -> {row['snapshot_path']}")
    for row in conn.execute("SELECT id, local_path FROM assets"):
        if not row["local_path"] or not (ROOT / row["local_path"]).exists():
            errors.append(f"missing asset: {row['id']} -> {row['local_path']}")

    # A card should have a base variant whenever it has been parsed into the
    # formal card table.  Upgrade variants are optional (status/curse cards
    # and some source candidates cannot be upgraded), so their absence is not
    # itself an error or warning.
    for row in conn.execute("SELECT c.entity_id FROM cards c JOIN entities e ON e.id=c.entity_id WHERE e.lifecycle!='candidate' AND e.id NOT LIKE 'sts1.candidate.%'"):
        variants = {v[0] for v in conn.execute("SELECT variant_kind FROM entity_variants WHERE entity_id=?", (row["entity_id"],))}
        if "base" not in variants:
            warnings.append(f"card without base variant: {row['entity_id']}")

    # Exact normalized names may legitimately be ambiguous (four Strike cards)
    # but the ambiguity must be visible to callers.
    for row in conn.execute(
        """SELECT e.kind, n.language, n.normalized, COUNT(DISTINCT n.entity_id) AS n
           FROM names n JOIN entities e ON e.id=n.entity_id
           GROUP BY e.kind, n.language, n.normalized
           HAVING COUNT(DISTINCT n.entity_id)>1"""
    ):
        warnings.append(f"ambiguous name ({row['language']}/{row['kind']}): {row['normalized']} x{row['n']}")

    fts_count = conn.execute("SELECT COUNT(*) FROM names_fts").fetchone()[0]
    names_count = conn.execute("SELECT COUNT(*) FROM names").fetchone()[0]
    if fts_count != names_count:
        errors.append(f"names_fts count {fts_count} != names count {names_count}")

    # JSONL exports are the portable handoff format used to rebuild or inspect
    # the SQLite database.  Check their row counts against the database so a
    # stale generated file cannot silently look like the current knowledge
    # base.  ``inventory.jsonl`` is a compatibility alias for the canonical
    # ``inventory_items.jsonl`` and must contain the same rows.
    export_counts: dict[str, int | None] = {}
    for table in EXPORT_TABLES:
        path = ROOT / "data" / "exports" / f"{table}.jsonl"
        actual = jsonl_count(path)
        expected = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        export_counts[table] = actual
        if actual is None:
            errors.append(f"missing or unreadable JSONL export: {path.relative_to(ROOT)}")
        elif actual != expected:
            errors.append(f"stale JSONL export: {table}.jsonl has {actual} rows; SQLite has {expected}")
    inventory_items_path = ROOT / "data" / "exports" / "inventory_items.jsonl"
    inventory_legacy_path = ROOT / "data" / "exports" / "inventory.jsonl"
    canonical_rows = jsonl_rows(inventory_items_path)
    legacy_rows = jsonl_rows(inventory_legacy_path)
    if canonical_rows is not None and legacy_rows is not None and canonical_rows != legacy_rows:
        errors.append("stale compatibility export: inventory.jsonl differs from inventory_items.jsonl")

    # Check links emitted by the Markdown generator.  External URLs are not
    # fetched here; local links are resolved relative to the page file.
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for page in WIKI_ROOT.rglob("*.md"):
        text = page.read_text(encoding="utf-8")
        # The foundational Wiki is deliberately independent from the two
        # strategy documents.  Keep this invariant executable so a future
        # import cannot silently add strategy links to generated pages.
        if re.search(r"^##\s+攻略关联\s*$", text, flags=re.M):
            errors.append(f"strategy section emitted in foundational Wiki: {page.relative_to(ROOT)}")
        if re.search(r"(?:端口化入门攻略|胜利的方程式)", text) and page.name not in {"coverage.md"}:
            errors.append(f"strategy document reference emitted in foundational Wiki: {page.relative_to(ROOT)}")
        for target in link_re.findall(text):
            # Source links can point to the web or to a versioned local game
            # resource.  The latter is deliberately recorded as provenance,
            # not treated as a Markdown-relative file path.
            if target.startswith(("http://", "https://", "mailto:", "file://", "game://")):
                continue
            local = target.split("#", 1)[0]
            if not local:
                continue
            target_path = (page.parent / local).resolve()
            if not target_path.exists():
                errors.append(f"broken local link: {page.relative_to(ROOT)} -> {target}")

    placeholders = []
    for row in conn.execute("SELECT id, value_json FROM claims"):
        if "请输入图片描述" in row["value_json"]:
            placeholders.append(row["id"])
    if placeholders:
        warnings.append(f"raw article placeholder text retained in {len(placeholders)} claim(s); generated summaries should filter it")
    energy_loss = conn.execute(
        """SELECT COUNT(*) FROM claims
           WHERE (value_json LIKE '%Gain .%' OR value_json LIKE '%Deal .%')
             AND COALESCE(notes, '') NOT LIKE '%superseded: icon-only text recovered%'"""
    ).fetchone()[0]
    if energy_loss:
        warnings.append(f"possible icon text loss detected in {energy_loss} claim(s); inspect image/alt semantics")

    strategy_notes = conn.execute("SELECT COUNT(*) FROM strategy_notes").fetchone()[0]
    strategy_links = conn.execute("SELECT COUNT(*) FROM strategy_links").fetchone()[0]
    if strategy_notes or strategy_links:
        errors.append(
            f"foundational Wiki strategy tables must be empty: strategy_notes={strategy_notes}, strategy_links={strategy_links}"
        )

    report = {
        "generated_at": now(),
        "status": "failed" if errors else "passed_with_warnings" if warnings else "passed",
        "errors": errors,
        "warnings": warnings,
        "counts": {
            "entities": conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0],
            "names": names_count,
            "claims": conn.execute("SELECT COUNT(*) FROM claims").fetchone()[0],
            "relations": conn.execute("SELECT COUNT(*) FROM relations").fetchone()[0],
            "source_pages": conn.execute("SELECT COUNT(*) FROM source_pages").fetchone()[0],
            "assets": conn.execute("SELECT COUNT(*) FROM assets").fetchone()[0],
            "wiki_pages": len(list(WIKI_ROOT.rglob("*.md"))) if WIKI_ROOT.exists() else 0,
            "strategy_notes": strategy_notes,
            "strategy_links": strategy_links,
        },
        "export_counts": export_counts,
    }
    report_path = ROOT / "reports" / "p1-validation.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    conn.close()
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
