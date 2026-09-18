# 圆球守护者 + 2 个三机械 / Spheric Guardian + 2 Shapes

> 稳定 ID：`sts1.encounter.act3.hard.spheric_guardian_2_shapes`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：圆球守护者 + 2 个三机械
- English: Spheric Guardian + 2 Shapes

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | The Beyond |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 3, "phase": "Remaining Combat Encounters", "weight": 1} |
| `repetition_rules` | 2 Shapes are independently chosen with equal probability and 1 Spheric Guardian |

## 相关条目

- `contains_monster` → [爆炸机 / Exploder](../monsters/sts1_monster_exploder.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 2, "mode": "independent_choices", "raw": "2 Shapes are independently chosen with equal probability and 1 Spheric Guardian"}}`
- `contains_monster` → [反冲机 / Repulsor](../monsters/sts1_monster_repulsor.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 2, "mode": "independent_choices", "raw": "2 Shapes are independently chosen with equal probability and 1 Spheric Guardian"}}`
- `contains_monster` → [圆球守护者 / Spheric Guardian](../monsters/sts1_monster_spheric_guardian.md)
- `contains_monster` → [钉刺机 / Spiker](../monsters/sts1_monster_spiker.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 2, "mode": "independent_choices", "raw": "2 Shapes are independently chosen with equal probability and 1 Spheric Guardian"}}`

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 2 Shapes are independently chosen with equal probability and 1 Spheric Guardian | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "2 Shapes are independently chosen with equal probability and 1 Spheric Guardian", "linked_names": ["Spheric Guardian", "Shapes"], "members": [{"entity_id": "sts1.monster.spheric_guardian", "label": "Spheric Guardian", "origin": "linked", "quantity": 1}, {"entity_id": "sts1.monster.exploder", "label": "shapes", "origin": "details", "quantity": 2}, {"entity_id": "sts1.monster.repulsor", "label": "shapes", "origin": "details", "quantity": 2}, {"entity_id": "sts1.monster.spiker", "la... | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Spheric Guardian + 2 Shapes | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 圆球守护者 + 2 个三机械 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"choose_count": 2, "mode": "independent_choices", "raw": "2 Shapes are independently chosen with equal probability and 1 Spheric Guardian"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 1} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T11:10:21+00:00
