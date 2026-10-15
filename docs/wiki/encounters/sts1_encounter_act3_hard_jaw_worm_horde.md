# 大颚虫群 / Jaw Worm Horde

> 稳定 ID：`sts1.encounter.act3.hard.jaw_worm_horde`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：大颚虫群
- English: Jaw Worm Horde

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | The Beyond |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 7, "phase": "Remaining Combat Encounters", "weight": 1} |
| `repetition_rules` | 3x Jaw Worms (that start combat with the effects of Bellow) Bellow: On Ascension 0 onwards: Gain 3 Strength and 6 Block On Ascension 2 onwards: Gain 4 Strength and 6 Block On Ascension 17 onwards: Gain 5 Strength and 9 Block |

## 相关条目

- `contains_monster` → [大颚虫 / Jaw Worm](../monsters/sts1_monster_jaw_worm.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "3x Jaw Worms (that start combat with the effects of Bellow) Bellow: On Ascension 0 onwards: Gain 3 Strength and 6 Block On Ascension 2 onwards: Gain 4 Strength and 6 Block On Ascension 17 onwards: Gain 5 Strength and 9 Block"}}`

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | 3x Jaw Worms (that start combat with the effects of Bellow) Bellow: On Ascension 0 onwards: Gain 3 Strength and 6 Block On Ascension 2 onwards: Gain 4 Strength and 6 Block On Ascension 17 onwards: Gain 5 Strength and 9 Block | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "3x Jaw Worms (that start combat with the effects of Bellow) Bellow: On Ascension 0 onwards: Gain 3 Strength and 6 Block On Ascension 2 onwards: Gain 4 Strength and 6 Block On Ascension 17 onwards: Gain 5 Strength and 9 Block", "linked_names": ["Jaw Worm Horde"], "members": [{"entity_id": "sts1.monster.jaw_worm", "label": "jaw worms", "origin": "details", "quantity": 3}], "resolution_status": "confirmed_conditional", "resolved_entity_ids": ["sts1.monster.jaw_worm"]} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Jaw Worm Horde | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 大颚虫群 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"mode": "fixed_details", "raw": "3x Jaw Worms (that start combat with the effects of Bellow) Bellow: On Ascension 0 onwards: Gain 3 Strength and 6 Block On Ascension 2 onwards: Gain 4 Strength and 6 Block On Ascension 17 onwards: Gain 5 Strength and 9 Block"} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 1} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T14:55:08+00:00
