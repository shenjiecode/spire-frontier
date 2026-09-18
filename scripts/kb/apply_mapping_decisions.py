"""Apply human-reviewed bilingual inventory decisions to SQLite.

The input CSV is intentionally small and explicit.  This command validates
source IDs, category/character boundaries, and one-to-one confirmed choices,
then writes ``inventory_mappings`` in one transaction.  It does not copy
translated prose or infer rules.  After confirming rows, rerun
``fetch_p3.py --refresh --languages zh-CN --kinds ...`` so the Chinese claims
are attached to the canonical English entity.

Create a file from ``data/decisions/mapping-decisions.template.csv`` and edit
only rows that were reviewed against both source pages.  The generated
``mapping-review.csv`` is a ranking aid and is never applied automatically.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "spire.sqlite"
TEMPLATE_PATH = ROOT / "data" / "decisions" / "mapping-decisions.template.csv"
ALLOWED = {"candidate", "confirmed", "conflict", "rejected"}
FIELDS = [
    "zh_inventory_id", "en_inventory_id", "status", "decided_by", "rationale", "evidence_json"
]


def norm(value: str) -> str:
    return " ".join((value or "").split()).casefold()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def stable_id(zh_id: str, en_id: str) -> str:
    return "mapping." + hashlib.sha256(f"{zh_id}|{en_id}".encode("utf-8")).hexdigest()[:24]


def entity_for_inventory(conn: sqlite3.Connection, row: sqlite3.Row) -> str | None:
    names = conn.execute(
        """SELECT DISTINCT e.id FROM entities e JOIN names n ON n.entity_id=e.id
           WHERE e.kind=? AND n.language='en' AND (n.is_preferred=1 OR n.name_kind='source_name')
             AND n.normalized=?""",
        (row["entity_kind"], norm(row["name"])),
    ).fetchall()
    if row["entity_kind"] != "card" or len(names) <= 1:
        return names[0][0] if len(names) == 1 else None
    # Same-name cards (Strike/Defend) are disambiguated by the directory's
    # character value, never by row order.
    for candidate in names:
        char = conn.execute(
            """SELECT n.name FROM cards c JOIN names n ON n.entity_id=c.character_entity_id
               WHERE c.entity_id=? AND n.language='en' AND n.is_preferred=1 LIMIT 1""",
            (candidate[0],),
        ).fetchone()
        if char and row["character"] and char[0].casefold() == row["character"].casefold():
            return candidate[0]
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", required=True, type=Path, help="reviewed CSV with the template columns")
    args = parser.parse_args(argv)
    path = args.file if args.file.is_absolute() else ROOT / args.file
    if not path.exists():
        raise SystemExit(f"decision file not found: {path}")
    if not DB_PATH.exists():
        raise SystemExit("data/spire.sqlite not found")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    seen_zh: dict[str, str] = {}
    seen_en: dict[str, str] = {}
    decisions: list[dict[str, Any]] = []
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        missing = [field for field in FIELDS if field not in (reader.fieldnames or [])]
        if missing:
            raise SystemExit("decision CSV missing columns: " + ", ".join(missing))
        for line_no, raw in enumerate(reader, 2):
            if not any((raw.get(field) or "").strip() for field in FIELDS):
                continue
            zh_id = (raw.get("zh_inventory_id") or "").strip()
            en_id = (raw.get("en_inventory_id") or "").strip()
            status = (raw.get("status") or "").strip().casefold()
            if not zh_id or not en_id or status not in ALLOWED:
                errors.append(f"line {line_no}: IDs and status(candidate/confirmed/conflict/rejected) are required")
                continue
            zh = conn.execute("SELECT * FROM inventory_items WHERE id=?", (zh_id,)).fetchone()
            en = conn.execute("SELECT * FROM inventory_items WHERE id=?", (en_id,)).fetchone()
            if not zh or not en:
                errors.append(f"line {line_no}: inventory ID not found ({zh_id}, {en_id})")
                continue
            if zh["language"] != "zh-CN" or en["language"] != "en":
                errors.append(f"line {line_no}: language boundary violated")
                continue
            if zh["entity_kind"] != en["entity_kind"]:
                errors.append(f"line {line_no}: category mismatch ({zh['entity_kind']} vs {en['entity_kind']})")
                continue
            if zh["status"] == "excluded" or en["status"] == "excluded":
                errors.append(f"line {line_no}: excluded inventory row cannot be mapped")
                continue
            if status == "confirmed" and not (raw.get("rationale") or "").strip():
                errors.append(f"line {line_no}: confirmed mapping requires rationale")
                continue
            if status == "confirmed" and zh["entity_kind"] == "card" and zh["character"] and en["character"] and zh["character"] != en["character"]:
                errors.append(f"line {line_no}: card character mismatch")
                continue
            if status == "confirmed":
                if zh_id in seen_zh and seen_zh[zh_id] != en_id:
                    errors.append(f"line {line_no}: one Chinese row has multiple confirmed targets")
                    continue
                if en_id in seen_en and seen_en[en_id] != zh_id:
                    errors.append(f"line {line_no}: one English row has multiple confirmed targets")
                    continue
                seen_zh[zh_id] = en_id
                seen_en[en_id] = zh_id
            entity_id = entity_for_inventory(conn, en)
            if status == "confirmed" and not entity_id:
                errors.append(f"line {line_no}: English inventory row is not uniquely tied to an entity ({en_id})")
                continue
            evidence = {}
            try:
                evidence = json.loads(raw.get("evidence_json") or "{}")
                if not isinstance(evidence, dict):
                    raise ValueError
            except (json.JSONDecodeError, ValueError):
                errors.append(f"line {line_no}: evidence_json must be a JSON object")
                continue
            if entity_id:
                evidence["entity_id"] = entity_id
            evidence["decided_by"] = (raw.get("decided_by") or "manual").strip() or "manual"
            evidence.setdefault("zh_url", zh["url"])
            evidence.setdefault("en_url", en["url"])
            decisions.append({
                "zh_id": zh_id,
                "en_id": en_id,
                "status": status,
                "rationale": (raw.get("rationale") or "").strip() or None,
                "evidence": evidence,
                "decided_by": (raw.get("decided_by") or "manual").strip() or "manual",
            })
    if errors:
        conn.close()
        for error in errors:
            print("[mapping-error] " + error)
        return 2
    try:
        for decision in decisions:
            conn.execute(
                """INSERT INTO inventory_mappings
                   (id, zh_inventory_id, en_inventory_id, status, rationale, evidence_json, decided_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(zh_inventory_id,en_inventory_id) DO UPDATE SET
                     status=excluded.status, rationale=excluded.rationale,
                     evidence_json=excluded.evidence_json, decided_at=excluded.decided_at""",
                (
                    stable_id(decision["zh_id"], decision["en_id"]),
                    decision["zh_id"], decision["en_id"], decision["status"],
                    decision["rationale"], json.dumps(decision["evidence"], ensure_ascii=False, sort_keys=True), utc_now(),
                ),
            )
        conn.commit()
    except Exception:
        conn.rollback()
        conn.close()
        raise
    count = len(decisions)
    print(json.dumps({"applied": count, "file": str(path), "confirmed": sum(x["status"] == "confirmed" for x in decisions)}, ensure_ascii=False, indent=2))
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
