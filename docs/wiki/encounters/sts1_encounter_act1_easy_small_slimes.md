# 小型史莱姆 / Small Slimes

> 稳定 ID：`sts1.encounter.act1.easy.small_slimes`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：小型史莱姆
- English: Small Slimes

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | Exordium |
| `room_type` | monster |
| `pool_type` | easy |
| `weight_json` | {"ordinal": 4, "phase": "First Three Combat Encounters", "weight": 2} |
| `repetition_rules` | Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S)) |

## 相关条目

- `contains_monster` → [酸液史莱姆（中） / Acid Slime (M)](../monsters/sts1_monster_acid_slime_m.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": [["Spike Slime(M)", "Acid Slime (S)"], ["Acid Slime (M)", "Spike Slime (S)"]], "mode": "exclusive_alternatives", "raw": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))"}}`
- `contains_monster` → [酸液史莱姆（小） / Acid Slime (S)](../monsters/sts1_monster_acid_slime_s.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": [["Spike Slime(M)", "Acid Slime (S)"], ["Acid Slime (M)", "Spike Slime (S)"]], "mode": "exclusive_alternatives", "raw": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))"}}`
- `contains_monster` → [尖刺史莱姆（中） / Spike Slime (M)](../monsters/sts1_monster_spike_slime_m.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": [["Spike Slime(M)", "Acid Slime (S)"], ["Acid Slime (M)", "Spike Slime (S)"]], "mode": "exclusive_alternatives", "raw": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))"}}`
- `contains_monster` → [尖刺史莱姆（小） / Spike Slime (S)](../monsters/sts1_monster_spike_slime_s.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": [["Spike Slime(M)", "Acid Slime (S)"], ["Acid Slime (M)", "Spike Slime (S)"]], "mode": "exclusive_alternatives", "raw": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))"}}`

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S)) | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))", "linked_names": ["Small Slimes"], "members": [{"entity_id": "sts1.monster.spike_slime_s", "label": "spike slime (s)", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.acid_slime_m", "label": "acid slime (m)", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.acid_slime_s", "label": "acid slime (s)", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.spike_... | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Small Slimes | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 小型史莱姆 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"alternatives": [["Spike Slime(M)", "Acid Slime (S)"], ["Acid Slime (M)", "Spike Slime (S)"]], "mode": "exclusive_alternatives", "raw": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "First Three Combat Encounters", "weight": 2} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T11:10:21+00:00
