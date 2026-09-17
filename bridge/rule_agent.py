"""A1 规则 Agent：继承 spirecomm 基类，全部决策沿用基类简单 AI，叠加全量日志。

A1 验收只要求"自动通关一层/一局"，策略质量不在此处追求（C2/C3 接知识库后替换）。
"""
import json
import logging
import time
from datetime import datetime
from pathlib import Path

from spirecomm.ai.agent import Agent
from spirecomm.communication.action import CancelAction, ChooseAction, StateAction
from spirecomm.spire.character import PlayerClass
from spirecomm.spire.screen import ScreenType

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
            "hp": getattr(self.game, "current_hp", None),
            "payload": payload,
        }
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def handle_error(self, error):
        """命令被游戏拒绝（如商店动画期间命令竞争）时：记日志、刷新状态、继续玩。

        spirecomm 基类默认直接 raise，会杀死 bridge 进程导致游戏永久等待。"""
        logger.warning("命令被拒，刷新状态重试: %s", error)
        self._log("command_error", {"error": str(error)})
        return StateAction()

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
        if self.game.screen_type == ScreenType.SHOP_SCREEN:
            action = self._shop_screen_action()
            self._log("shop", {"action": str(action.command)})
            return action
        action = super().get_screen_action()
        self._log("screen_action", {"screen": str(self.game.screen_type), "action": str(action.command)})
        return action

    def _shop_screen_action(self):
        """复现 CommunicationMod 商店选择列表的构成顺序，用索引购买（避免本地化卡名编码问题）。

        游戏端列表顺序：purge(若可用且买得起) → 买得起的卡(彩色→无色) → 遗物 → 药水。
        决策策略沿用基类：优先删卡，再买第一张不被跳过的卡，再买第一个遗物，否则取消。
        """
        screen, gold = self.game.screen, self.game.gold
        items = []  # (kind, obj)
        if screen.purge_available and gold >= screen.purge_cost:
            items.append(("purge", None))
        for c in screen.cards:
            if c.price <= gold:
                items.append(("card", c))
        for r in screen.relics:
            if r.price <= gold:
                items.append(("relic", r))
        for p in screen.potions:
            if p.price <= gold:
                items.append(("potion", p))
        if items and items[0][0] == "purge":
            return ChooseAction(choice_index=0)
        for i, (kind, obj) in enumerate(items):
            if kind == "card" and not self.priorities.should_skip(obj):
                return ChooseAction(choice_index=i)
        for i, (kind, obj) in enumerate(items):
            if kind == "relic":
                return ChooseAction(choice_index=i)
        return CancelAction()

    def get_card_reward_action(self):
        """基类发 choose <卡名>，中文名经 stdin 管道易编码错位被游戏拒绝；改用索引。"""
        screen = self.game.screen
        reward_cards = screen.cards
        if screen.can_skip and not self.game.in_combat:
            pickable = [
                card for card in reward_cards
                if self.priorities.needs_more_copies(
                    card, sum(1 for c in self.game.deck if c.card_id == card.card_id)
                )
            ]
        else:
            pickable = reward_cards
        if len(pickable) > 0:
            best = self.priorities.get_best_card(pickable)
            return ChooseAction(choice_index=reward_cards.index(best))
        elif screen.can_bowl:
            return ChooseAction(name="bowl")  # ASCII，无编码风险
        self.skipped_cards = True
        return CancelAction()

    def get_next_boss_reward_action(self):
        """同上：Boss 遗物奖励改用索引（列表顺序 = screen.relics 顺序）。"""
        relics = self.game.screen.relics
        best = self.priorities.get_best_boss_relic(relics)
        return ChooseAction(choice_index=relics.index(best))

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
