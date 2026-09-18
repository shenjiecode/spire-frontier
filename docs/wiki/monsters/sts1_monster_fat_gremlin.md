# 胖地精 / Fat Gremlin

> 稳定 ID：`sts1.monster.fat_gremlin`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：胖地精
- English: Fat Gremlin

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 13 |
| `hp_max` | 17 |
| `ascension_json` | {"ascension_max": 18, "ascension_min": 14, "base_max": 17, "base_min": 13} |
| `encounter_notes` | Split member from sts1.monster.gremlins; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Smash | DebuffAttack1 | 4 |  | {"text": "Deals (4;5) damage. Applies 1 Weak(.; and 1 Frail.)"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [地精小队 / Gang of Gremlins](../encounters/sts1_encounter_act1_hard_gang_of_gremlins.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 4, "mode": "sample_without_replacement", "pool": ["2x Fat Gremlin", "2x Sneaky Gremlin", "2x Mad Gremlin", "Shield Gremlin", "Gremlin Wizard"], "raw": "4 randomly chosen from: [2x Fat Gremlin, 2x Sneaky Gremlin, 2x Mad Gremlin, Shield Gremlin, and Gremlin Wizard]"}}`
- `has_member` → [地精小队 / Gremlins](sts1_monster_gremlins.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "GremlinFat", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `monster.hp.range` | {"ascension_max": 18, "ascension_min": 14, "ascension_raw": "14-18", "base_max": 17, "base_min": 13, "base_raw": "13-17"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Smash` | {"effect": {"text": "Deals (4;5) damage. Applies 1 Weak(.; and 1 Frail.)"}, "intent": "DebuffAttack1"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Fat Gremlin<br>|Image  = GremlinFat.png<br>|HP     = 13-17<br>|AscHP  = 14-18<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>'''Fat Gremlins''' focus on applying {{BD|Weak}}.<br><br>=== Pattern ===<br>{{Intents Table/start|Fat Gremlin}}<br>{{Intents Table/row<br>|Name   = Smash<br>|Intent = DebuffAttack1<br>|Effect = Deals (4;{{Asc|2|5}}) damage. Applies 1 {{BD|Weak}}(.; and {{Asc|17|1}} {{BD|Frail}}.)}}<br>{{Intents Table/end}}<br>'''Fat Gremlin''' uses {{Int|Fa... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
