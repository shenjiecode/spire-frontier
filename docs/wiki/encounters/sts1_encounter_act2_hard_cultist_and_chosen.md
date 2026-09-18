# 邪教徒与被拣选者 / Cultist and Chosen

> 稳定 ID：`sts1.encounter.act2.hard.cultist_and_chosen`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：邪教徒与被拣选者
- English: Cultist and Chosen

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | The City |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 2, "phase": "Remaining Combat Encounters", "weight": 3} |
| `repetition_rules` | 1 Chosen and 1 Cultist |

## 相关条目

- `contains_monster` → [被拣选者 / Chosen](../monsters/sts1_monster_chosen.md)
- `contains_monster` → [邪教徒 / Cultist](../monsters/sts1_monster_cultist.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 1 Chosen and 1 Cultist | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "1 Chosen and 1 Cultist", "linked_names": ["Cultist", "Chosen"], "members": [{"entity_id": "sts1.monster.cultist", "label": "Cultist", "origin": "linked", "quantity": 1}, {"entity_id": "sts1.monster.chosen", "label": "Chosen", "origin": "linked", "quantity": 1}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.chosen", "sts1.monster.cultist"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Cultist and Chosen | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 邪教徒与被拣选者 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"mode": "fixed_details", "raw": "1 Chosen and 1 Cultist"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 3} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T11:10:21+00:00
