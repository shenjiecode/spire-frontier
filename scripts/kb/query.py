"""Small read-only query interface for the local Wiki database.

Examples:
    python scripts/kb/query.py entity 全身撞击
    python scripts/kb/query.py entity Strike --kind card
    python scripts/kb/query.py relations sts1.card.ironclad.body_slam
    python scripts/kb/query.py list --kind relic
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "spire.sqlite"


def names(conn: sqlite3.Connection, entity_id: str) -> list[dict[str, str]]:
    return [dict(row) for row in conn.execute("SELECT language, name, name_kind, verification_status FROM names WHERE entity_id=? ORDER BY language, is_preferred DESC, name", (entity_id,))]


def entity(conn: sqlite3.Connection, entity_id: str) -> dict:
    row = conn.execute("SELECT * FROM entities WHERE id=?", (entity_id,)).fetchone()
    if not row:
        return {}
    result = dict(row)
    if conn.execute("SELECT 1 FROM sqlite_master WHERE name='entity_records'").fetchone():
        from build_records import record
        result = record(conn, conn.execute('SELECT * FROM entity_records WHERE id=?', (entity_id,)).fetchone())
    result["names"] = names(conn, entity_id)
    result["relations_out"] = [dict(r) for r in conn.execute("SELECT relation_type, target_entity_id, status, condition_json FROM relations WHERE source_entity_id=? AND status!='rejected' ORDER BY relation_type, target_entity_id", (entity_id,))]
    result["relations_in"] = [dict(r) for r in conn.execute("SELECT relation_type, source_entity_id, status, condition_json FROM relations WHERE target_entity_id=? AND status!='rejected' ORDER BY relation_type, source_entity_id", (entity_id,))]
    result["claims"] = [dict(r) for r in conn.execute("SELECT field_path, variant_id, language, value_json, verification_status, source_page_id FROM claims WHERE subject_entity_id=? ORDER BY field_path, variant_id, language", (entity_id,))]
    return result


def find_entities(conn: sqlite3.Connection, text: str, kind: str | None = None, character: str | None = None) -> list[sqlite3.Row]:
    # Game IDs are case-sensitive and are scoped by entity kind (a card and
    # its power can share an ID). Preserve ambiguity when kind is omitted.
    sql = 'SELECT e.* FROM entities e WHERE e.game_id=? AND e.lifecycle=\'active\''
    params = [text]
    if kind:
        sql += ' AND e.kind=?'
        params.append(kind)
    if character:
        sql += """ AND e.kind='card' AND EXISTS (
                    SELECT 1 FROM cards c JOIN names cn ON cn.entity_id=c.character_entity_id
                    WHERE c.entity_id=e.id AND cn.language='en' AND cn.normalized=?)"""
        params.append(character.casefold())
    exact = conn.execute(sql + ' ORDER BY kind,id', params).fetchall()
    if exact:
        return exact
    params: list[str] = [text.casefold()]
    sql = """SELECT DISTINCT e.* FROM entities e JOIN names n ON n.entity_id=e.id
             WHERE n.normalized=?"""
    if kind:
        sql += " AND e.kind=?"
        params.append(kind)
    if character:
        sql += """ AND e.kind='card' AND EXISTS (
                    SELECT 1 FROM cards c JOIN names cn ON cn.entity_id=c.character_entity_id
                    WHERE c.entity_id=e.id AND cn.language='en' AND cn.normalized=?)"""
        params.append(character.casefold())
    rows = conn.execute(sql + " ORDER BY e.kind, e.id", params).fetchall()
    if rows:
        return rows
    # FTS5 is only a convenience fallback; exact normalized lookup remains the
    # default and makes ambiguity explicit.
    params = [text]
    sql = """SELECT DISTINCT e.* FROM names_fts f JOIN entities e ON e.id=f.entity_id
             WHERE f.name MATCH ?"""
    if kind:
        sql += " AND e.kind=?"
        params.append(kind)
    if character:
        sql += """ AND e.kind='card' AND EXISTS (
                    SELECT 1 FROM cards c JOIN names cn ON cn.entity_id=c.character_entity_id
                    WHERE c.entity_id=e.id AND cn.language='en' AND cn.normalized=?)"""
        params.append(character.casefold())
    return conn.execute(sql + " ORDER BY e.kind, e.id", params).fetchall()


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Slay the Spire 1 KB query")
    sub = parser.add_subparsers(dest="command", required=True)
    p_entity = sub.add_parser("entity")
    p_entity.add_argument("name_or_id")
    p_entity.add_argument("--kind")
    p_entity.add_argument("--character", help="card character filter: ironclad/silent/defect/watcher")
    p_list = sub.add_parser("list")
    p_list.add_argument("--kind")
    p_rel = sub.add_parser("relations")
    p_rel.add_argument("entity_id")
    p_sources = sub.add_parser("sources")
    p_sources.add_argument("entity_id")
    p_sources.add_argument("--field", help="optional exact field_path filter")
    args = parser.parse_args()
    if not DB_PATH.exists():
        parser.error("data/spire.sqlite not found; run bootstrap_sample.py first")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    if args.command == "entity":
        direct = conn.execute("SELECT id FROM entities WHERE id=?", (args.name_or_id,)).fetchone()
        rows = [conn.execute("SELECT * FROM entities WHERE id=?", (direct[0],)).fetchone()] if direct else find_entities(conn, args.name_or_id, args.kind, args.character)
        result = [entity(conn, row["id"]) for row in rows if row]
    elif args.command == "list":
        if args.kind:
            rows = conn.execute("SELECT * FROM entities WHERE kind=? ORDER BY id", (args.kind,)).fetchall()
        else:
            rows = conn.execute("SELECT * FROM entities ORDER BY kind, id").fetchall()
        result = [{"id": row["id"], "kind": row["kind"], "names": names(conn, row["id"])} for row in rows]
    elif args.command == "relations":
        result = entity(conn, args.entity_id).get("relations_out", []) + entity(conn, args.entity_id).get("relations_in", [])
    else:
        params = [args.entity_id]
        sql = """SELECT c.field_path, c.variant_id, c.language, c.value_json,
                        c.verification_status, c.source_page_id, s.url, s.title
                 FROM claims c JOIN source_pages s ON s.id=c.source_page_id
                 WHERE c.subject_entity_id=?"""
        if args.field:
            sql += " AND c.field_path=?"
            params.append(args.field)
        result = [dict(row) for row in conn.execute(sql + " ORDER BY c.field_path,c.variant_id,c.language,c.created_at", params)]
    print(json.dumps(result, ensure_ascii=False, indent=2))
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
