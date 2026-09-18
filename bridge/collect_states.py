"""Passive CommunicationMod state collector.

This process deliberately never starts a run or sends gameplay commands.  It
only asks CommunicationMod for a fresh state at a configurable interval and
stores the JSON messages as JSONL under ``logs/``.  It is useful when checking
the local game build against the Wiki without handing control to the rule
agent.

CommunicationMod starts the child process from the game directory, so the
Windows wrapper used by the manual changes back to the repository before
running this module.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "logs"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def main() -> int:
    parser = argparse.ArgumentParser(description="Passive CommunicationMod JSON state collector")
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="seconds between STATE polls; use 0 to request the next state immediately",
    )
    args = parser.parse_args()
    if args.interval < 0:
        parser.error("--interval must be >= 0")

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"communication-{datetime.now():%Y%m%d-%H%M%S}.jsonl"

    # CommunicationMod waits for this exact line before it unblocks the game.
    print("ready", flush=True)
    # Prompt one state even when the game is already sitting at a stable menu.
    print("state", flush=True)

    with log_path.open("a", encoding="utf-8") as log:
        for line in sys.stdin:
            raw = line.rstrip("\r\n")
            if not raw:
                continue
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                payload = {"_raw": raw}
            record = {"ts": utc_now(), "payload": payload}
            log.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
            log.flush()
            if args.interval:
                time.sleep(args.interval)
            # STATE is read-only: it does not start a run or alter the current
            # screen, and it gives us a fresh snapshot for later comparison.
            print("state", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
