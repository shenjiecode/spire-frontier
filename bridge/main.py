"""CommunicationMod 外部进程入口。

SpireConfig 的 command 指向 bridge/run_agent.sh；游戏通过 stdin/stdout JSON 与本进程通信。
"""
import argparse
import logging
import random
import sys
import time
from pathlib import Path

# vendor 优先，避免环境里装了别的 spirecomm 版本（注意：指向 vendor 内的项目根，包在其下一层）
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "vendor" / "spirecomm"))

from spirecomm.communication.coordinator import Coordinator  # noqa: E402
from spirecomm.spire.character import PlayerClass  # noqa: E402

from bridge.rule_agent import RuleAgent  # noqa: E402

CLASS_MAP = {
    "ironclad": PlayerClass.IRONCLAD,
    "silent": PlayerClass.THE_SILENT,
    "defect": PlayerClass.DEFECT,
    "watcher": PlayerClass.WATCHER,
}


def main():
    parser = argparse.ArgumentParser(description="spire-scholar bridge (A1 rule agent)")
    parser.add_argument("--class", dest="cls", default="ironclad", choices=CLASS_MAP.keys())
    parser.add_argument("--ascension", type=int, default=0)
    parser.add_argument("--seed", default=None, help="不指定则按时间生成")
    parser.add_argument("--loop", action="store_true", help="死亡后自动开新局")
    parser.add_argument("--log-level", default="INFO")
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    agent = RuleAgent(chosen_class=CLASS_MAP[args.cls])
    coordinator = Coordinator()
    coordinator.signal_ready()
    coordinator.register_command_error_callback(agent.handle_error)
    coordinator.register_state_change_callback(agent.get_next_action_in_game)
    coordinator.register_out_of_game_callback(agent.get_next_action_out_of_game)

    while True:
        seed = args.seed or str(int(time.time()))
        logging.info("开局 class=%s ascension=%d seed=%s", args.cls, args.ascension, seed)
        try:
            results = coordinator.play_one_game(agent.chosen_class, ascension_level=args.ascension, seed=seed)
            logging.info("本局结束：%s", results)
        except Exception as exc:  # noqa: BLE001
            logging.exception("一局异常终止: %s", exc)
            if not args.loop:
                raise
        if not args.loop:
            break
        random.seed(seed)


if __name__ == "__main__":
    main()
