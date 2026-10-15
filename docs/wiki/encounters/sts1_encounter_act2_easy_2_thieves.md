# 2 名盗贼 / 2 Thieves

> 稳定 ID：`sts1.encounter.act2.easy.2_thieves`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：2 名盗贼
- English: 2 Thieves

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | The City |
| `room_type` | monster |
| `pool_type` | easy |
| `weight_json` | {"ordinal": 5, "phase": "First Two Combat Encounters", "weight": 2} |
| `repetition_rules` | 1 Looter on the left, and 1 Mugger on the right |

## 相关条目

- `contains_monster` → [抢劫的 / Looter](../monsters/sts1_monster_looter.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "1 Looter on the left, and 1 Mugger on the right"}}`
- `contains_monster` → [打劫的 / Mugger](../monsters/sts1_monster_mugger.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "1 Looter on the left, and 1 Mugger on the right"}}`

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 1 Looter on the left, and 1 Mugger on the right | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "1 Looter on the left, and 1 Mugger on the right", "linked_names": ["Thieves"], "members": [{"entity_id": "sts1.monster.looter", "label": "looter", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.mugger", "label": "mugger", "origin": "details", "quantity": 1}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.looter", "sts1.monster.mugger"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | 2 Thieves | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 2 名盗贼 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"mode": "fixed_details", "raw": "1 Looter on the left, and 1 Mugger on the right"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "First Two Combat Encounters", "weight": 2} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T14:55:08+00:00
