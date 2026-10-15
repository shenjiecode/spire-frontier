# 带壳寄生怪与真菌兽 / Shelled Parasite and Fungi

> 稳定 ID：`sts1.encounter.act2.hard.shelled_parasite_and_fungi`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：带壳寄生怪与真菌兽
- English: Shelled Parasite and Fungi

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | The City |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 8, "phase": "Remaining Combat Encounters", "weight": 3} |
| `repetition_rules` | 1 Shelled Parasite, 1 Fungi Beast |

## 相关条目

- `contains_monster` → [真菌兽 / Fungi Beast](../monsters/sts1_monster_fungi_beast.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "1 Shelled Parasite, 1 Fungi Beast"}}`
- `contains_monster` → [带壳寄生怪 / Shelled Parasite](../monsters/sts1_monster_shelled_parasite.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 1 Shelled Parasite, 1 Fungi Beast | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "1 Shelled Parasite, 1 Fungi Beast", "linked_names": ["Shelled Parasite", "Fungi"], "members": [{"entity_id": "sts1.monster.shelled_parasite", "label": "Shelled Parasite", "origin": "linked", "quantity": 1}, {"entity_id": "sts1.monster.fungi_beast", "label": "fungi beast", "origin": "details", "quantity": 1}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.fungi_beast", "sts1.monster.shelled_parasite"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Shelled Parasite and Fungi | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 带壳寄生怪与真菌兽 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"mode": "fixed_details", "raw": "1 Shelled Parasite, 1 Fungi Beast"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 3} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T14:55:08+00:00
