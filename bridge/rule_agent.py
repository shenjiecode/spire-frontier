"""A1 规则 Agent：继承 spirecomm 基类，全部决策沿用基类简单 AI，叠加全量日志。

A1 验收只要求"自动通关一层/一局"，策略质量不在此处追求（C2/C3 接知识库后替换）。
"""
import json
import logging
import time
from datetime import datetime
from pathlib import Path

from spirecomm.ai.agent import Agent
from spirecomm.spire.character import PlayerClass

logger = logging.getLogger("rule_agent")

RUN_LOG_DIR = Path(__file__).resolve().parent.parent / "logs"


class RuleAgent(Agent):
    """基类钩子 + 落盘日志。每局一个 JSONL 文件：logs/run-<ts>.jsonl"""

    def __init__(self, chosen_class=PlayerClass.IRONCLAD):
        super().__init__(chosen_class=chosen_class)
        RUN_LOG_DIR.mkdir(exist_ok=True)
        self.log_path = RUN_LOG_DIR / f"run-{datetime.now():%Y%m%d-%H%M%S}.jsonl"
        self._floor_seq = 0

    # ---------- 日志 ----------

    def _log(self, event: str, payload: dict):
        record = {
            "ts": round(time.time(), 3),
            "event": event,
            "floor": getattr(self.game, "floor", None),
            "act": getattr(self.game, "act", None),
            "hp": getattr(getattr(self.game, "player", None), "current_hp", None),
            "payload": payload,
        }
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    # ---------- 基类钩子：决策全部交给基类实现，只记日志 ----------

    def get_next_action_in_game(self, game_state):
        self.game = game_state
        self._floor_seq += 1
        self._log(
            "state",
            {
                "screen_type": str(self.game.screen_type),
                "play_available": self.game.play_available,
                "end_available": self.game.end_available,
                "choice_available": self.game.choice_available,
                "proceed_available": self.game.proceed_available,
            },
        )
        return super().get_next_action_in_game(game_state)

    def get_next_combat_action(self):
        action = super().get_next_combat_action()
        self._log("combat_action", {"action": str(action.command)})
        return action

    def get_screen_action(self):
        action = super().get_screen_action()
        self._log("screen_action", {"screen": str(self.game.screen_type), "action": str(action.command)})
        return action

    def get_card_reward_action(self):
        action = super().get_card_reward_action()
        self._log("card_reward", {"action": str(action.command)})
        return action

    def get_map_choice_action(self):
        action = super().get_map_choice_action()
        self._log("map_choice", {"action": str(action.command)})
        return action

    def get_rest_action(self):
        action = super().get_rest_action()
        self._log("rest", {"action": str(action.command)})
        return action

    def get_next_boss_reward_action(self):
        return super().get_next_boss_reward_action()

    def get_next_combat_reward_action(self):
        return super().get_next_combat_reward_action()

    def before_combat_action(self):
        pass  # 基类仅打 debug 日志

    def change_class(self, new_class):
        super().change_class(new_class)

    def before_game_start(self):
        self._log("game_start", {"class": str(self.chosen_class)})

    def after_game_end(self):
        self._log("game_end", {"victory": getattr(self.game, "victory", None)})

    def after_game_won(self):
        self._log("game_won", {})
