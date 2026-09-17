"""离线冒烟测试：不启动游戏，用 CommunicationMod 协议样例 JSON 验证 bridge 决策链路。

跑法：.venv/bin/python tests/smoke_test.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "vendor"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from spirecomm.spire.game import Game  # noqa: E402
from bridge.rule_agent import RuleAgent  # noqa: E402


def card(name, cid, cost, ctype, playable=True, target=False, rarity="BASIC"):
    return {
        "exhausts": False, "is_playable": playable, "cost": cost, "name": name,
        "id": cid, "type": ctype, "ethereal": False,
        "uuid": f"uuid-{name}-{id(name)}", "upgrades": 0, "rarity": rarity,
        "has_target": target,
    }


def combat_state():
    return {
        "draw_pile": [card("Strike", "Strike_R", 1, "ATTACK"), card("Defend", "Defend_R", 1, "SKILL")],
        "discard_pile": [],
        "exhaust_pile": [],
        "limbo": [],
        "cards_discarded_this_turn": 0,
        "turn": 1,
        "monsters": [{
            "is_gone": False, "move_hits": 1, "move_base_damage": 12,
            "half_dead": False, "move_adjusted_damage": -1, "max_hp": 46,
            "intent": "ATTACK", "move_id": 1, "name": "Jaw Worm",
            "current_hp": 46, "block": 0, "id": "JawWorm", "powers": [],
        }],
        "player": {"orbs": [], "current_hp": 68, "block": 0, "max_hp": 75, "powers": [], "energy": 3},
        "hand": [
            card("Strike", "Strike_R", 1, "ATTACK", target=True),
            card("Strike", "Strike_R", 1, "ATTACK", target=True),
            card("Defend", "Defend_R", 1, "SKILL"),
            card("Defend", "Defend_R", 1, "SKILL"),
            card("Bash", "Bash", 2, "ATTACK", target=True),
        ],
    }


def game_state():
    return {
        "current_hp": 68, "max_hp": 75, "floor": 1, "act": 1, "gold": 99,
        "seed": -3047511808784702860, "class": "IRONCLAD", "ascension_level": 0,
        "relics": [{"name": "Burning Blood", "id": "Burning Blood", "counter": -1, "description": "At the end of combat, heal 6 HP."}],
        "deck": [card("Strike", "Strike_R", 1, "ATTACK"), card("Defend", "Defend_R", 1, "SKILL")],
        "map": [],
        "potions": [],
        "is_screen_up": False, "screen_type": "NONE", "screen_state": {},
        "room_phase": "COMBAT", "room_type": "MonsterRoom",
        "combat_state": combat_state(),
    }


def main():
    state, commands = game_state(), ["play", "end", "potion", "state"]
    game = Game.from_json(state, commands)
    agent = RuleAgent()
    action = agent.get_next_action_in_game(game)

    class FakeCoordinator:
        game_is_ready = True
        last_game_state = game
        sent = []

        @staticmethod
        def send_message(msg):
            FakeCoordinator.sent.append(msg)

    action.execute(FakeCoordinator())
    wire = FakeCoordinator.sent[-1]
    print("wire 消息:", wire)
    assert wire.split()[0] in {"play", "end"}, f"预期 play/end，实际 {wire}"
    if wire.startswith("play"):
        parts = wire.split()
        assert len(parts) in {2, 3}, f"play 参数不对: {wire}"  # play <卡槽> [目标]
    log_file = agent.log_path
    assert log_file.exists() and log_file.read_text(encoding="utf-8").strip(), "日志未落盘"
    print(f"冒烟通过 ✓  日志: {log_file}")


if __name__ == "__main__":
    main()
