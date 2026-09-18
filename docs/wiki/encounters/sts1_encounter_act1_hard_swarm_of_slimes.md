# 史莱姆群 / Swarm of Slimes

> 稳定 ID：`sts1.encounter.act1.hard.swarm_of_slimes`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：史莱姆群
- English: Swarm of Slimes

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | Exordium |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 3, "phase": "Remaining Combat Encounters", "weight": 1} |
| `repetition_rules` | 3x Spike Slime (S) and 2x Acid Slime (S) |

## 相关条目

- `contains_monster` → [酸液史莱姆（小） / Acid Slime (S)](../monsters/sts1_monster_acid_slime_s.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "3x Spike Slime (S) and 2x Acid Slime (S)"}}`
- `contains_monster` → [尖刺史莱姆（小） / Spike Slime (S)](../monsters/sts1_monster_spike_slime_s.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "3x Spike Slime (S) and 2x Acid Slime (S)"}}`

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 3x Spike Slime (S) and 2x Acid Slime (S) | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "3x Spike Slime (S) and 2x Acid Slime (S)", "linked_names": ["Swarm of Slimes"], "members": [{"entity_id": "sts1.monster.spike_slime_s", "label": "spike slime (s)", "origin": "details", "quantity": 3}, {"entity_id": "sts1.monster.acid_slime_s", "label": "acid slime (s)", "origin": "details", "quantity": 2}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.acid_slime_s", "sts1.monster.spike_slime_s"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Swarm of Slimes | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 史莱姆群 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"mode": "fixed_details", "raw": "3x Spike Slime (S) and 2x Acid Slime (S)"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 1} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T11:10:21+00:00
