"""Build a deterministic bilingual mapping review queue.

This command is deliberately *report only*.  It never changes ``entities`` or
``inventory_mappings`` and never treats a translated name guessed by a model as
confirmed.  It ranks possible English rows for each parsed Xiaoheihe row using
evidence already present in SQLite: category/character, exact shared names,
numeric signatures, and a small set of cross-language rule markers.  A human
can then record a decision in the database in a later, explicitly reviewed
step.

Usage::

    $env:PYTHONIOENCODING='utf-8'
    python scripts/kb/audit_mappings.py

Outputs are stable-sorted ``data/decisions/mapping-review.csv`` and a JSON
summary under ``reports/``.  The queue is reproducible from the database and
does not read either of the separately maintained strategy documents.
"""

from __future__ import annotations

import csv
import json
import re
import sqlite3
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "spire.sqlite"
REPORT_PATH = ROOT / "reports" / "mapping-review.json"
CSV_PATH = ROOT / "data" / "decisions" / "mapping-review.csv"
PARSER_VERSION = "kb-mapping-audit/0.1"


MARKERS: dict[str, set[str]] = {
    "attack": {"attack", "damage", "hit", "伤害", "攻击", "造成"},
    "block": {"block", "格挡", "护甲"},
    "draw": {"draw", "抽", "抽牌", "抽取"},
    "energy": {"energy", "能量", "费用"},
    "exhaust": {"exhaust", "消耗"},
    "discard": {"discard", "弃牌", "弃置"},
    "strength": {"strength", "力量"},
    "dexterity": {"dexterity", "敏捷"},
    "vulnerable": {"vulnerable", "易伤"},
    "weak": {"weak", "虚弱"},
    "poison": {"poison", "中毒", "毒"},
    "orb": {"orb", "充能球", "球位"},
    "stance": {"stance", "姿态", "平静", "愤怒", "神格"},
    "scry": {"scry", "预见"},
    "retain": {"retain", "保留"},
    "random": {"random", "随机"},
}
MARKER_RE = re.compile(r"[A-Za-z]+|[一-龥]{1,8}")
NUMBER_RE = re.compile(r"(?<![A-Za-z])(?:\d+(?:\.\d+)?|X)(?![A-Za-z])", re.I)


def norm(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().casefold()


def json_obj(value: str | None) -> Any:
    try:
        return json.loads(value or "")
    except (TypeError, json.JSONDecodeError):
        return value or ""


def text_value(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value or "")


def number_signature(value: str) -> tuple[str, ...]:
    result: set[str] = set()
    for token in NUMBER_RE.findall(value or ""):
        if token.casefold() == "x":
            result.add("x")
            continue
        try:
            number = float(token)
        except ValueError:
            continue
        # Source article IDs, image hashes and footer dates are not game
        # values.  Keeping values in the ordinary StS range avoids letting
        # those technical numbers dominate a translation candidate.
        if number > 1000:
            continue
        result.add(str(int(number)) if number.is_integer() else str(number))
    return tuple(sorted(result))


def marker_signature(value: str) -> set[str]:
    tokens = {token.casefold() for token in MARKER_RE.findall(value or "")}
    result: set[str] = set()
    for marker, variants in MARKERS.items():
        if tokens & {x.casefold() for x in variants}:
            result.add(marker)
    return result


def row_metadata(row: sqlite3.Row) -> dict[str, Any]:
    try:
        value = json.loads(row["metadata_json"] or "{}")
        return value if isinstance(value, dict) else {}
    except json.JSONDecodeError:
        return {}


def entity_text_cache(conn: sqlite3.Connection) -> dict[str, str]:
    values: dict[str, list[str]] = defaultdict(list)
    for row in conn.execute(
        """SELECT subject_entity_id, value_json FROM claims
           WHERE field_path IN ('card.description','relic.effect','potion.effect',
                                'source.article_text','status.description')
              OR field_path LIKE 'monster.move.%'
              OR field_path LIKE 'event.%'
              OR field_path LIKE 'keyword.%'
              OR field_path LIKE 'mechanic.%'
           ORDER BY subject_entity_id, id"""
    ):
        values[row["subject_entity_id"]].append(text_value(json_obj(row["value_json"])))
    return {entity_id: " ".join(parts) for entity_id, parts in values.items()}


def candidate_pool(conn: sqlite3.Connection) -> dict[str, list[dict[str, Any]]]:
    """Precompute English entity/inventory candidates once per audit run."""
    items_by_name: dict[tuple[str, str], list[sqlite3.Row]] = defaultdict(list)
    for item in conn.execute(
        "SELECT * FROM inventory_items WHERE language='en' AND status!='excluded' ORDER BY entity_kind,name,id"
    ):
        items_by_name[(item["entity_kind"], norm(item["name"]))].append(item)
    result: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in conn.execute(
        """SELECT DISTINCT e.id, e.kind, n.name AS en_name
           FROM entities e JOIN names n ON n.entity_id=e.id
           WHERE n.language='en' AND n.is_preferred=1 ORDER BY e.kind,e.id"""
    ):
        expected_character = None
        if row["kind"] == "card":
            char_row = conn.execute(
                """SELECT n.name FROM cards c JOIN names n ON n.entity_id=c.character_entity_id
                   WHERE c.entity_id=? AND n.language='en' AND n.is_preferred=1 LIMIT 1""",
                (row["id"],),
            ).fetchone()
            expected_character = char_row[0].casefold() if char_row else None
        for en_item in items_by_name.get((row["kind"], norm(row["en_name"])), []):
            if expected_character and en_item["character"] and en_item["character"].casefold() != expected_character:
                continue
            result[row["kind"]].append({"entity_id": row["id"], "en_name": row["en_name"], "item": en_item})
    return result


def score_candidate(text_cache: dict[str, str], zh: sqlite3.Row, zh_text: str, candidate: dict[str, Any]) -> dict[str, Any]:
    en = candidate["item"]
    en_text = text_cache.get(candidate["entity_id"], "")
    zh_numbers = set(number_signature(zh_text))
    en_numbers = set(number_signature(en_text))
    zh_markers = marker_signature(zh_text)
    en_markers = marker_signature(en_text)
    metadata = row_metadata(en)
    score = 0.0
    evidence: list[str] = []

    if norm(zh["name"]) == norm(en["name"]):
        score += 100
        evidence.append("exact_shared_name")
    if zh["entity_kind"] == "card":
        if zh["character"] and en["character"]:
            if zh["character"] == en["character"]:
                score += 12
                evidence.append("same_character")
            else:
                score -= 30
                evidence.append("character_mismatch")
        if metadata.get("type") and marker_signature(zh_text) & {"attack", "block"}:
            # Type is only a weak hint because the Chinese article often does
            # not print the type label; never use this to confirm a mapping.
            score += 1
        if metadata.get("rarity") and any(x in zh_text for x in ("普通", "罕见", "稀有", "特殊")):
            score += 1
    elif zh["character"] and en["character"] and zh["character"] == en["character"]:
        score += 5
        evidence.append("same_character")

    if zh_numbers and en_numbers:
        overlap = len(zh_numbers & en_numbers)
        if overlap:
            ratio = overlap / max(len(zh_numbers), len(en_numbers))
            score += 8 * ratio
            evidence.append(f"numeric_overlap:{overlap}/{max(len(zh_numbers), len(en_numbers))}")
    overlap_markers = zh_markers & en_markers
    if overlap_markers:
        score += min(12, 2 * len(overlap_markers))
        evidence.append("markers:" + ",".join(sorted(overlap_markers)))

    # Shared Latin fragments are useful for J.A.X., X-cost names and other
    # untranslated entries, but deliberately carry little weight otherwise.
    latin_zh = " ".join(re.findall(r"[a-z0-9.]+", norm(zh["name"])))
    latin_en = " ".join(re.findall(r"[a-z0-9.]+", norm(en["name"])))
    if latin_zh and latin_en:
        similarity = SequenceMatcher(None, latin_zh, latin_en).ratio()
        if similarity >= 0.85:
            score += 10 * similarity
            evidence.append("shared_latin_name")

    if score >= 100:
        confidence = "exact_name"
    elif score >= 18:
        confidence = "review_first"
    elif score >= 8:
        confidence = "weak_candidate"
    else:
        confidence = "low_signal"
    return {
        "score": round(score, 3),
        "confidence": confidence,
        "evidence": evidence,
        "zh_numbers": sorted(zh_numbers),
        "en_numbers": sorted(en_numbers),
        "marker_overlap": sorted(overlap_markers),
        "entity_id": candidate["entity_id"],
        "en_name": en["name"],
        "en_url": en["url"],
        "en_inventory_id": en["id"],
        "en_character": en["character"],
    }


def main() -> int:
    if not DB_PATH.exists():
        raise SystemExit("data/spire.sqlite not found; run bootstrap_sample.py first")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    text_cache = entity_text_cache(conn)
    candidates_by_kind = candidate_pool(conn)

    confirmed_zh = {
        row[0]
        for row in conn.execute("SELECT zh_inventory_id FROM inventory_mappings WHERE status='confirmed'")
    }
    zh_rows = conn.execute(
        """SELECT * FROM inventory_items
           WHERE language='zh-CN' AND status NOT IN ('excluded','failed')
           ORDER BY entity_kind, name, id"""
    ).fetchall()
    output: list[dict[str, Any]] = []
    summary = Counter()
    for zh in zh_rows:
        if zh["id"] in confirmed_zh:
            summary["confirmed_existing"] += 1
            continue
        candidate_entities = candidates_by_kind.get(zh["entity_kind"], [])
        article_key = re.sub(r"[^a-zA-Z0-9_-]+", "_", str(zh["article_id"] or zh["name"])).strip("_").casefold() or "item"
        zh_entity = conn.execute(
            "SELECT id FROM entities WHERE id=?",
            (f"sts1.candidate.zh.{zh['entity_kind']}.{article_key}",),
        ).fetchone()
        zh_text = text_cache.get(zh_entity[0], zh["name"]) if zh_entity else zh["name"]
        scored = [score_candidate(text_cache, zh, zh_text, candidate) for candidate in candidate_entities]
        scored.sort(key=lambda value: (-value["score"], value["en_name"].casefold(), value["entity_id"]))
        top = scored[:5]
        top_score = top[0]["score"] if top else 0
        margin = round(top[0]["score"] - top[1]["score"], 3) if len(top) > 1 else top_score
        confidence = top[0]["confidence"] if top else "no_candidate"
        if confidence == "exact_name":
            summary["exact_name"] += 1
        elif confidence == "review_first":
            summary["review_first"] += 1
        elif confidence == "weak_candidate":
            summary["weak_candidate"] += 1
        else:
            summary["low_signal_or_none"] += 1
        output.append({
            "zh_inventory_id": zh["id"],
            "entity_kind": zh["entity_kind"],
            "zh_name": zh["name"],
            "zh_article_id": zh["article_id"] or "",
            "zh_url": zh["url"],
            "zh_character": zh["character"] or "",
            "status": "needs_review",
            "top_score": top_score,
            "margin": margin,
            "candidate_count": len(scored),
            "candidates": top,
        })

    output.sort(key=lambda row: (row["entity_kind"], row["zh_name"], row["zh_inventory_id"]))
    report = {
        "parser_version": PARSER_VERSION,
        "status": "review_queue",
        "confirmed_existing_excluded": summary["confirmed_existing"],
        "unmatched_rows": len(output),
        "confidence_counts": dict(sorted((key, value) for key, value in summary.items() if key != "confirmed_existing")),
        "by_kind": dict(sorted(Counter(row["entity_kind"] for row in output).items())),
        "notes": [
            "This is a ranking aid, not an identity decision; no database mapping was changed.",
            "Exact shared names are surfaced for human review because same-name cards and status/card collisions remain possible.",
            "Numbers and rule markers are evidence hints only; translated wording and images still require field-level review.",
            "Strategy documents are not read or linked.",
        ],
        "rows": output,
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    fields = [
        "zh_inventory_id", "entity_kind", "zh_name", "zh_article_id", "zh_url",
        "zh_character", "status", "top_score", "margin", "candidate_count",
        "top_candidate_entity_id", "top_candidate_en_name", "top_candidate_en_url",
        "top_candidate_inventory_id", "top_candidate_confidence", "evidence",
        "alternatives",
    ]
    with CSV_PATH.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in output:
            top = row["candidates"][0] if row["candidates"] else {}
            alternatives = row["candidates"][1:]
            writer.writerow({
                "zh_inventory_id": row["zh_inventory_id"],
                "entity_kind": row["entity_kind"],
                "zh_name": row["zh_name"],
                "zh_article_id": row["zh_article_id"],
                "zh_url": row["zh_url"],
                "zh_character": row["zh_character"],
                "status": row["status"],
                "top_score": row["top_score"],
                "margin": row["margin"],
                "candidate_count": row["candidate_count"],
                "top_candidate_entity_id": top.get("entity_id", ""),
                "top_candidate_en_name": top.get("en_name", ""),
                "top_candidate_en_url": top.get("en_url", ""),
                "top_candidate_inventory_id": top.get("en_inventory_id", ""),
                "top_candidate_confidence": top.get("confidence", "no_candidate"),
                "evidence": ";".join(top.get("evidence", [])),
                "alternatives": json.dumps(alternatives, ensure_ascii=False, sort_keys=True),
            })

    # A compact Markdown view is easier to open from the generated Wiki while
    # the JSON retains every candidate and evidence token.
    wiki_path = ROOT / "docs" / "wiki" / "mapping-review.md"
    lines = [
        "# 中英文身份映射审核队列", "",
        "本页由 `scripts/kb/audit_mappings.py` 从 SQLite 生成。它只提供候选排序，不会自动合并实体；确认后应通过独立审核决定写入 `inventory_mappings`。", "",
        f"待审核中文目录行：{len(output)}；已有 confirmed 映射跳过：{summary['confirmed_existing']}。", "",
        "| 类别 | 中文名 | 首选英文候选 | 分数 | 置信标记 | 备选数 | 证据提示 |", "| --- | --- | --- | ---: | --- | ---: | --- |",
    ]
    for row in output:
        top = row["candidates"][0] if row["candidates"] else {}
        lines.append(
            f"| `{row['entity_kind']}` | [{row['zh_name']}]({row['zh_url']}) | {top.get('en_name','—')} | {row['top_score']} | `{top.get('confidence','no_candidate')}` | {row['candidate_count']} | {', '.join(top.get('evidence', [])) or '无'} |"
        )
    wiki_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    conn.close()
    print(json.dumps({k: v for k, v in report.items() if k != "rows"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
