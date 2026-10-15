# 地精小队 / Gang of Gremlins

> 稳定 ID：`sts1.encounter.act1.hard.gang_of_gremlins`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：地精小队
- English: Gang of Gremlins

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | Exordium |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 1, "phase": "Remaining Combat Encounters", "weight": 1} |
| `repetition_rules` | 4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard] |

## 相关条目

- `contains_monster` → [胖地精 / Fat Gremlin](../monsters/sts1_monster_fat_gremlin.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 4, "mode": "sample_without_replacement", "pool": ["2x Fat Gremlin", "2x Sneaky Gremlin", "2x Mad Gremlin", "Shield Gremlin", "Gremlin Wizard"], "raw": "4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard]"}}`
- `contains_monster` → [地精法师 / Gremlin Wizard](../monsters/sts1_monster_gremlin_wizard.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 4, "mode": "sample_without_replacement", "pool": ["2x Fat Gremlin", "2x Sneaky Gremlin", "2x Mad Gremlin", "Shield Gremlin", "Gremlin Wizard"], "raw": "4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard]"}}`
- `contains_monster` → [火大地精 / Mad Gremlin](../monsters/sts1_monster_mad_gremlin.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 4, "mode": "sample_without_replacement", "pool": ["2x Fat Gremlin", "2x Sneaky Gremlin", "2x Mad Gremlin", "Shield Gremlin", "Gremlin Wizard"], "raw": "4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard]"}}`
- `contains_monster` → [持盾地精 / Shield Gremlin](../monsters/sts1_monster_shield_gremlin.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 4, "mode": "sample_without_replacement", "pool": ["2x Fat Gremlin", "2x Sneaky Gremlin", "2x Mad Gremlin", "Shield Gremlin", "Gremlin Wizard"], "raw": "4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard]"}}`
- `contains_monster` → [卑鄙地精 / Sneaky Gremlin](../monsters/sts1_monster_sneaky_gremlin.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 4, "mode": "sample_without_replacement", "pool": ["2x Fat Gremlin", "2x Sneaky Gremlin", "2x Mad Gremlin", "Shield Gremlin", "Gremlin Wizard"], "raw": "4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard]"}}`

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard] | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard]", "linked_names": ["Gang of Gremlins"], "members": [{"entity_id": "sts1.monster.gremlin_wizard", "label": "gremlin wizard", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.shield_gremlin", "label": "shield gremlin", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.sneaky_gremlin", "label": "sneaky gremlin", "origin": "details", "quantity... | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Gang of Gremlins | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 地精小队 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"choose_count": 4, "mode": "sample_without_replacement", "pool": ["2x Fat Gremlin", "2x Sneaky Gremlin", "2x Mad Gremlin", "Shield Gremlin", "Gremlin Wizard"], "raw": "4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard]"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 1} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T14:55:08+00:00
