# 虱虫 / Red Louse

> 稳定 ID：`sts1.monster.red_louse`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：虱虫
- English: Red Louse

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 10 |
| `hp_max` | 15 |
| `ascension_json` | {"ascension_max": 16, "ascension_min": 11, "base_max": 15, "base_min": 10} |
| `encounter_notes` | Split member from sts1.monster.louses; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Bite | Attack2 |  |  | {"text": "Deals N damage. N = Number between (5-7;6-8), chosen at the start of combat."} |
| Grow | Buff |  |  | {"text": "Gains (3;4) Strength."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [2 只虱虫 / 2 Louse](../encounters/sts1_encounter_act1_easy_2_louse.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": ["Red Louse", "Green Louse"], "mode": "independent_per_slot", "probability_each": 0.5, "raw": "2x Louse (each independently has a 50% chance of either color)", "slot_count": 2}}`
- `contains_monster` → [3 只虱虫 / 3 Louse](../encounters/sts1_encounter_act1_hard_3_louse.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": ["Red Louse", "Green Louse"], "mode": "independent_per_slot", "probability_each": 0.5, "raw": "3x Louse (each independently has a 50% chance of either color)", "slot_count": 3}}`
- `contains_monster` → [序幕暴徒 / Exordium Thugs](../encounters/sts1_encounter_act1_hard_exordium_thugs.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Louse (any) or Medium Slime (any) Second Enemy: Slaver (any), Cultist, or Looter", "slots": {"first": "Louse (any) or Medium Slime (any)", "second": "Slaver (any), Cultist, or Looter"}}}`
- `contains_monster` → [序幕野兽 / Exordium Wildlife](../encounters/sts1_encounter_act1_hard_exordium_wildlife.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `has_member` → [虱虫 / Louses](sts1_monster_louses.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "FuzzyLouseNormal", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `monster.hp.range` | {"ascension_max": 16, "ascension_min": 11, "ascension_raw": "11-16", "base_max": 15, "base_min": 10, "base_raw": "10-15"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Bite` | {"effect": {"text": "Deals N damage. N = Number between (5-7;6-8), chosen at the start of combat."}, "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Grow` | {"effect": {"text": "Gains (3;4) Strength."}, "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Red Louse<br>|Image  = RedLouse.png<br>|HP     = 10-15<br>|AscHP  = 11-16<br>|Powers = {{BD|Curl Up}} N, where N is random between 3-7 ({{Asc|7|4-8}} {{!}} {{Asc|17|9-12}})<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>{{Power Infobox|Curl Up}}<br>The '''Red Louse''' is a normal [[Monsters|Enemy]] found exclusively in Act 1.<br><br>=== Pattern ===<br>{{Intents Table/start|Red Louse}}<br>{{Intents Table/row<br>|Name   = Bite<br>|Intent = Attack2<br>|Effect = Deal... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
