"""Apply explicit source-entity merge decisions.

Inventory mappings cover a Chinese directory row and an English directory
row.  Character pages in the Chinese source have no English inventory rows,
so their four game-verified identity merges use this separate, auditable
decision file.  The command never merges by a fuzzy name on its own.
"""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from bootstrap_sample import DB_PATH, ROOT, apply_schema  # type: ignore
from fetch_p3 import merge_confirmed_candidate  # type: ignore


FIELDS = ["source_entity_id", "target_entity_id", "status", "decided_by", "rationale", "evidence_json"]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", required=True, type=Path)
    args = parser.parse_args(argv)
    path = args.file if args.file.is_absolute() else ROOT / args.file
    if not path.exists():
        raise SystemExit(f"decision file not found: {path}")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    apply_schema(conn)
    decisions: list[dict[str, str]] = []
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in FIELDS if field not in (reader.fieldnames or [])]
        if missing:
            raise SystemExit("decision CSV missing columns: " + ", ".join(missing))
        for line_no, raw in enumerate(reader, 2):
            source_id = (raw.get("source_entity_id") or "").strip()
            target_id = (raw.get("target_entity_id") or "").strip()
            status = (raw.get("status") or "").strip().casefold()
            if not source_id or not target_id or status != "confirmed":
                errors.append(f"line {line_no}: source, target and confirmed status are required")
                continue
            source = conn.execute("SELECT * FROM entities WHERE id=?", (source_id,)).fetchone()
            target = conn.execute("SELECT * FROM entities WHERE id=?", (target_id,)).fetchone()
            # A merge is intentionally idempotent.  If a previous successful
            # run already removed the candidate, the canonical target is the
            # evidence that this row has been applied.
            if not source and target:
                continue
            if not source or not target:
                errors.append(f"line {line_no}: entity not found ({source_id}, {target_id})")
                continue
            if source["kind"] != target["kind"]:
                errors.append(f"line {line_no}: kind mismatch ({source['kind']} vs {target['kind']})")
                continue
            if source_id == target_id:
                errors.append(f"line {line_no}: source and target are identical")
                continue
            if source["lifecycle"] != "candidate":
                errors.append(f"line {line_no}: source must be a candidate ({source_id})")
                continue
            if target["lifecycle"] == "candidate":
                errors.append(f"line {line_no}: target must be an active canonical entity ({target_id})")
                continue
            rationale = (raw.get("rationale") or "").strip()
            if not rationale:
                errors.append(f"line {line_no}: confirmed merge requires rationale")
                continue
            try:
                evidence = json.loads(raw.get("evidence_json") or "{}")
                if not isinstance(evidence, dict):
                    raise ValueError
            except (json.JSONDecodeError, ValueError):
                errors.append(f"line {line_no}: evidence_json must be a JSON object")
                continue
            evidence.setdefault("decided_at", utc_now())
            evidence.setdefault("decided_by", (raw.get("decided_by") or "manual").strip() or "manual")
            decisions.append({"source": source_id, "target": target_id, "rationale": rationale, "evidence": evidence})
    if errors:
        conn.close()
        for error in errors:
            print("[merge-error] " + error)
        return 2
    try:
        for item in decisions:
            merge_confirmed_candidate(conn, item["source"], item["target"])
        conn.commit()
    except Exception:
        conn.rollback()
        conn.close()
        raise
    print(json.dumps({"applied": len(decisions), "file": str(path)}, ensure_ascii=False, indent=2))
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
