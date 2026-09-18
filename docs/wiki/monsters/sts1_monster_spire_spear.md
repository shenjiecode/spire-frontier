# 高塔之矛 / Spire Spear

> 稳定 ID：`sts1.monster.spire_spear`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：高塔之矛
- English: Spire Spear

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 4 |
| `hp_min` | 160 |
| `hp_max` | 160 |
| `ascension_json` | {"ascension_max": 180, "ascension_min": 180, "base_max": 160, "base_min": 160} |
| `encounter_notes` | Split member from sts1.monster.spire_shield_and_spire_spear; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Skewer | Attack7 | 10 | 3 | {"text": "Deals (10×3;10×4) damage."} |
| Piercer | Buff |  |  | {"text": "All enemies gain 2 Strength."} |
| Burn Strike | DebuffAttack3 | 5 | 2 | {"text": "Deals (5×2;6×2) damage. (Adds 2 Burns into your discard pile.; Adds 2 Burns on top of your draw pile.)"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `has_member` → [高塔之盾/高塔之矛 / Spire Shield and Spire Spear](sts1_monster_spire_shield_and_spire_spear.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Spire Spear | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 高塔之矛 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SpireSpear", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 180, "ascension_min": 180, "ascension_raw": "180", "base_max": 160, "base_min": 160, "base_raw": "160"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Burn Strike` | {"effect": {"text": "Deals (5×2;6×2) damage. (Adds 2 Burns into your discard pile.; Adds 2 Burns on top of your draw pile.)"}, "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Piercer` | {"effect": {"text": "All enemies gain 2 Strength."}, "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Skewer` | {"effect": {"text": "Deals (10×3;10×4) damage."}, "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Spire Spear<br>|Image  = SpireSpear.png<br>|HP     = 160<br>|AscHP  = 180<br>|Powers = {{BD|Artifact}} 1 ({{Asc|18|2}})<br>|Debut  = Act 4<br>|Type   = Elite<br>}}<br>{{Power Infobox|Back Attack}}<br>Spire Spear is an [[Elite]] enemy found exclusively in [[Acts#Act 4:The Ending|Act 4]].<br><br>=== Pattern ===<br>{{Intents Table/start|Spire Spear}}<br>{{Intents Table/row<br>|Name   = Burn Strike<br>|Intent = DebuffAttack3<br>|Effect = Deals (5×2;{{Asc|3|6×2}}) dama... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
