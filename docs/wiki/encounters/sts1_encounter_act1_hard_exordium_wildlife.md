# 序幕野兽 / Exordium Wildlife

> 稳定 ID：`sts1.encounter.act1.hard.exordium_wildlife`  
> 类别：`encounter`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：序幕野兽
- English: Exordium Wildlife

## encounter 数据

| 字段 | 值 |
| --- | --- |
| `act` | Exordium |
| `room_type` | monster |
| `pool_type` | hard |
| `weight_json` | {"ordinal": 9, "phase": "Remaining Combat Encounters", "weight": 1.5} |
| `repetition_rules` | First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any) |

## 相关条目

- `contains_monster` → [酸液史莱姆（中） / Acid Slime (M)](../monsters/sts1_monster_acid_slime_m.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `contains_monster` → [真菌兽 / Fungi Beast](../monsters/sts1_monster_fungi_beast.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `contains_monster` → [虱虫 / Green Louse](../monsters/sts1_monster_green_louse.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `contains_monster` → [大颚虫 / Jaw Worm](../monsters/sts1_monster_jaw_worm.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `contains_monster` → [虱虫 / Red Louse](../monsters/sts1_monster_red_louse.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `contains_monster` → [尖刺史莱姆（中） / Spike Slime (M)](../monsters/sts1_monster_spike_slime_m.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `encounter.details` | First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any) | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.members` | {"details": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "linked_names": [], "members": [{"entity_id": "sts1.monster.acid_slime_m", "label": "medium slime", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.spike_slime_m", "label": "medium slime", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.fungi_beast", "label": "fungi beast", "origin": "details", "quantity": 1}, {"entity_id": "sts1.monster.jaw_worm", "label": "ja... | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.en` | Exordium Wildlife | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.name.zh` | 序幕野兽 | `single_source/editorial_zh` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.selection_rule` | {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `encounter.weight` | {"phase": "Remaining Combat Encounters", "weight": 1.5} | `single_source` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |

页面生成时间：2026-09-18T14:55:08+00:00
