# 卑鄙地精 / Sneaky Gremlin

> 稳定 ID：`sts1.monster.sneaky_gremlin`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：卑鄙地精
- English: Sneaky Gremlin

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 10 |
| `hp_max` | 14 |
| `ascension_json` | {"ascension_max": 15, "ascension_min": 11, "base_max": 14, "base_min": 10} |
| `encounter_notes` | Split member from sts1.monster.gremlins; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Puncture | Attack2 | 9 |  | {"text": "Deals (9;10) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [地精小队 / Gang of Gremlins](../encounters/sts1_encounter_act1_hard_gang_of_gremlins.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 4, "mode": "sample_without_replacement", "pool": ["2x Fat Gremlin", "2x Sneaky Gremlin", "2x Mad Gremlin", "Shield Gremlin", "Gremlin Wizard"], "raw": "4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard]"}}`
- `has_member` → [地精小队 / Gremlins](sts1_monster_gremlins.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "GremlinThief", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `monster.hp.range` | {"ascension_max": 15, "ascension_min": 11, "ascension_raw": "11-15", "base_max": 14, "base_min": 10, "base_raw": "10-14"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Puncture` | {"effect": {"text": "Deals (9;10) damage."}, "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Sneaky Gremlin<br>|Image  = GremlinThief.png<br>|HP     = 10-14<br>|AscHP  = 11-15<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>'''Sneaky Gremlins''' focus on doing consistent damage each turn.<br><br>=== Pattern ===<br>{{Intents Table/start|Sneaky Gremlin}}<br>{{Intents Table/row<br>|Name   = Puncture<br>|Intent = Attack2<br>|Effect = Deals (9;{{Asc|2|10}}) damage.}}<br>{{Intents Table/end}}<br>'''Sneaky Gremlin''' uses {{Int|Sneaky Gremlin|Puncture}} every tu... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
