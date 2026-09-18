# 大型史莱姆 / Large Slime

> 稳定 ID：`sts1.encounter.act1.hard.large_slime`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：大型史莱姆
- English: Large Slime

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | Exordium |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 2, "phase": "Remaining Combat Encounters", "weight": 2} |
| `repetition_rules` | Spike Slime (L) or Acid Slime (L) |

## 相关条目

- `contains_monster` → [酸液史莱姆（大） / Acid Slime (L)](../monsters/sts1_monster_acid_slime_l.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": ["Spike Slime (L)", "Acid Slime (L)"], "mode": "alternatives", "raw": "Spike Slime (L) or Acid Slime (L)"}}`
- `contains_monster` → [尖刺史莱姆（大） / Spike Slime (L)](../monsters/sts1_monster_spike_slime_l.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": ["Spike Slime (L)", "Acid Slime (L)"], "mode": "alternatives", "raw": "Spike Slime (L) or Acid Slime (L)"}}`

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | Spike Slime (L) or Acid Slime (L) | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "Spike Slime (L) or Acid Slime (L)", "linked_names": ["Large Slime"], "members": [{"entity_id": "sts1.monster.spike_slime_l", "label": "spike slime (l)", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.acid_slime_l", "label": "acid slime (l)", "origin": "details", "quantity": 1}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.acid_slime_l", "sts1.monster.spike_slime_l"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Large Slime | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 大型史莱姆 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"alternatives": ["Spike Slime (L)", "Acid Slime (L)"], "mode": "alternatives", "raw": "Spike Slime (L) or Acid Slime (L)"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 2} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T11:10:21+00:00
