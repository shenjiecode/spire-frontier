# 哨卫与圆球守护者 / Sentry and Spheric Guardian

> 稳定 ID：`sts1.encounter.act2.hard.sentry_and_spheric_guardian`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：哨卫与圆球守护者
- English: Sentry and Spheric Guardian

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | The City |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 3, "phase": "Remaining Combat Encounters", "weight": 2} |
| `repetition_rules` | 1 Sentry and 1 Spheric Guardian |

## 相关条目

- `contains_monster` → [哨位(精英) / Sentry](../monsters/sts1_monster_sentry.md)
- `contains_monster` → [圆球守护者 / Spheric Guardian](../monsters/sts1_monster_spheric_guardian.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 1 Sentry and 1 Spheric Guardian | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "1 Sentry and 1 Spheric Guardian", "linked_names": ["Sentry", "Spheric Guardian"], "members": [{"entity_id": "sts1.monster.sentry", "label": "Sentry", "origin": "linked", "quantity": 1}, {"entity_id": "sts1.monster.spheric_guardian", "label": "Spheric Guardian", "origin": "linked", "quantity": 1}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.sentry", "sts1.monster.spheric_guardian"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Sentry and Spheric Guardian | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 哨卫与圆球守护者 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"mode": "fixed_details", "raw": "1 Sentry and 1 Spheric Guardian"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 2} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T11:10:21+00:00
