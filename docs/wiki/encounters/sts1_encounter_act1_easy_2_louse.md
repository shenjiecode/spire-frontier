# 2 只虱虫 / 2 Louse

> 稳定 ID：`sts1.encounter.act1.easy.2_louse`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：2 只虱虫
- English: 2 Louse

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | Exordium |
| `room_type` | monster |
| `pool_type` | easy |
| `weight_json` | {"ordinal": 3, "phase": "First Three Combat Encounters", "weight": 2} |
| `repetition_rules` | 2x Louse (each independently has a 50% chance of either color) |

## 相关条目

- `contains_monster` → [虱虫 / Green Louse](../monsters/sts1_monster_green_louse.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": ["Red Louse", "Green Louse"], "mode": "independent_per_slot", "probability_each": 0.5, "raw": "2x Louse (each independently has a 50% chance of either color)", "slot_count": 2}}`
- `contains_monster` → [虱虫 / Red Louse](../monsters/sts1_monster_red_louse.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": ["Red Louse", "Green Louse"], "mode": "independent_per_slot", "probability_each": 0.5, "raw": "2x Louse (each independently has a 50% chance of either color)", "slot_count": 2}}`

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 2x Louse (each independently has a 50% chance of either color) | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "2x Louse (each independently has a 50% chance of either color)", "linked_names": ["Louse"], "members": [{"entity_id": "sts1.monster.green_louse", "label": "louse", "origin": "details", "quantity": 2}, {"entity_id": "sts1.monster.red_louse", "label": "louse", "origin": "details", "quantity": 2}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.green_louse", "sts1.monster.red_louse"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | 2 Louse | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 2 只虱虫 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"alternatives": ["Red Louse", "Green Louse"], "mode": "independent_per_slot", "probability_each": 0.5, "raw": "2x Louse (each independently has a 50% chance of either color)", "slot_count": 2} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "First Three Combat Encounters", "weight": 2} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T14:55:08+00:00
