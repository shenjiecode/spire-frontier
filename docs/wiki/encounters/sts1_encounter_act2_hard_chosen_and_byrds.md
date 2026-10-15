# 被拣选者与异鸟 / Chosen and Byrds

> 稳定 ID：`sts1.encounter.act2.hard.chosen_and_byrds`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：被拣选者与异鸟
- English: Chosen and Byrds

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | The City |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 1, "phase": "Remaining Combat Encounters", "weight": 2} |
| `repetition_rules` | 1 Chosen and 1 Byrd |

## 相关条目

- `contains_monster` → [异鸟 / Byrd](../monsters/sts1_monster_byrd.md)
- `contains_monster` → [被拣选者 / Chosen](../monsters/sts1_monster_chosen.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 1 Chosen and 1 Byrd | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "1 Chosen and 1 Byrd", "linked_names": ["Chosen", "Byrds"], "members": [{"entity_id": "sts1.monster.chosen", "label": "Chosen", "origin": "linked", "quantity": 1}, {"entity_id": "sts1.monster.byrd", "label": "Byrds", "origin": "linked", "quantity": 1}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.byrd", "sts1.monster.chosen"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Chosen and Byrds | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 被拣选者与异鸟 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"mode": "fixed_details", "raw": "1 Chosen and 1 Byrd"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 2} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T14:55:08+00:00
