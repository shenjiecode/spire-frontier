# 奴隶贩子 / Red Slaver

> 稳定 ID：`sts1.monster.red_slaver`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：奴隶贩子
- English: Red Slaver

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 46 |
| `hp_max` | 50 |
| `ascension_json` | {"ascension_max": 52, "ascension_min": 48, "base_max": 50, "base_min": 46} |
| `encounter_notes` | Split member from sts1.monster.slavers; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Entangle | DebuffStrong |  |  | {"text": "Applies 1 Entangled."} |
| Scrape | DebuffAttack2 | 8 |  | {"text": "Deals (8;9) damage. Applies (1;2) Vulnerable."} |
| Stab | Attack3 | 13 |  | {"text": "Deals (13;14) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [序幕暴徒 / Exordium Thugs](../encounters/sts1_encounter_act1_hard_exordium_thugs.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Louse (any) or Medium Slime (any) Second Enemy: Slaver (any), Cultist, or Looter", "slots": {"first": "Louse (any) or Medium Slime (any)", "second": "Slaver (any), Cultist, or Looter"}}}`
- `contains_monster` → [红色奴隶贩子 / Red Slaver](../encounters/sts1_encounter_act1_hard_red_slaver.md)
- `has_member` → [奴隶主 / Slavers](sts1_monster_slavers.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SlaverRed", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `monster.hp.range` | {"ascension_max": 52, "ascension_min": 48, "ascension_raw": "48-52", "base_max": 50, "base_min": 46, "base_raw": "46-50"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Entangle` | {"effect": {"text": "Applies 1 Entangled."}, "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Scrape` | {"effect": {"text": "Deals (8;9) damage. Applies (1;2) Vulnerable."}, "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Stab` | {"effect": {"text": "Deals (13;14) damage."}, "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Red Slaver<br>|Image  = SlaverRed.png<br>|HP     = 46-50<br>|AscHP  = 48-52<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>{{Power Infobox|Entangled}}<br>'''Red Slaver''' is a normal [[Monsters|Enemy]] found in Act 1 and Act 2. They can also appear in [[Elite]] combats and {{E|The Colosseum}} [[Event]].<br><br>== Pattern ==<br>{{Intents Table/start|Red Slaver}}<br>{{Intents Table/row<br>|Name   = Stab<br>|Intent = Attack3<br>|Effect = Deals (13;{{Asc|2|14}}) dama... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
