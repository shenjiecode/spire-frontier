# 酸液史莱姆（小） / Acid Slime (S)

> 稳定 ID：`sts1.monster.acid_slime_s`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：酸液史莱姆（小）
- English: Acid Slime (S)

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 8 |
| `hp_max` | 12 |
| `ascension_json` | {"ascension_max": 13, "ascension_min": 9, "base_max": 12, "base_min": 8} |
| `encounter_notes` | Split member from sts1.monster.acid_slimes; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Lick | Debuff |  |  | {"text": "Applies 1 Weak."} |
| Tackle | Attack1 | 3 |  | {"text": "Deals (3;4) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [小型史莱姆 / Small Slimes](../encounters/sts1_encounter_act1_easy_small_slimes.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": [["Spike Slime(M)", "Acid Slime (S)"], ["Acid Slime (M)", "Spike Slime (S)"]], "mode": "exclusive_alternatives", "raw": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))"}}`
- `contains_monster` → [史莱姆群 / Swarm of Slimes](../encounters/sts1_encounter_act1_hard_swarm_of_slimes.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "3x Spike Slime (S) and 2x Acid Slime (S)"}}`
- `has_member` → [酸液史莱姆 / Acid Slimes](sts1_monster_acid_slimes.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Acid Slime (S) | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 酸液史莱姆（小） | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "AcidSlime_S", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 13, "ascension_min": 9, "ascension_raw": "9-13", "base_max": 12, "base_min": 8, "base_raw": "8-12"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Lick` | {"effect": {"text": "Applies 1 Weak."}, "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tackle` | {"effect": {"text": "Deals (3;4) damage."}, "intent": "Attack1"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Acid Slime (S)<br>|Image  = AcidSlimeS.png<br>|HP     = 8-12<br>|AscHP  = 9-13<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>'''Acid Slime (S)''' is a normal [[Monsters|Enemy]] that is exclusively found in Act 1.<br><br>=== Pattern ===<br>{{Intents Table/start|Acid Slime (S)}}<br>{{Intents Table/row<br>|Name   = Lick<br>|Intent = Debuff<br>|Effect = Applies 1 {{BD|Weak}}.}}<br>{{Intents Table/row<br>|Name   = Tackle<br>|Intent = Attack1<br>|Effect = Deals (3;{{A... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
