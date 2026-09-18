# 百夫长与神秘术士 / Centurion and Mystic

> 稳定 ID：`sts1.encounter.act2.hard.centurion_and_mystic`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：百夫长与神秘术士
- English: Centurion and Mystic

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | The City |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 6, "phase": "Remaining Combat Encounters", "weight": 6} |
| `repetition_rules` | 1 Centurion and 1 Mystic |

## 相关条目

- `contains_monster` → [百夫长 / Centurion](../monsters/sts1_monster_centurion.md)
- `contains_monster` → [神秘术士 / Mystic](../monsters/sts1_monster_mystic.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 1 Centurion and 1 Mystic | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "1 Centurion and 1 Mystic", "linked_names": ["Centurion", "Mystic"], "members": [{"entity_id": "sts1.monster.centurion", "label": "Centurion", "origin": "linked", "quantity": 1}, {"entity_id": "sts1.monster.mystic", "label": "Mystic", "origin": "linked", "quantity": 1}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.centurion", "sts1.monster.mystic"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Centurion and Mystic | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 百夫长与神秘术士 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"mode": "fixed_details", "raw": "1 Centurion and 1 Mystic"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 6} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T11:10:21+00:00
