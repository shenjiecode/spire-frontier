# 高塔之盾 / Spire Shield

> 稳定 ID：`sts1.monster.spire_shield`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：高塔之盾
- English: Spire Shield

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 4 |
| `hp_min` | 110 |
| `hp_max` | 110 |
| `ascension_json` | {"ascension_max": 125, "ascension_min": 125, "base_max": 110, "base_min": 110} |
| `encounter_notes` | Split member from sts1.monster.spire_shield_and_spire_spear; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Fortify | Defend |  |  | {"text": "All enemies gain 30 Block."} |
| Smash | DefendAttack7 | 34 |  | {"text": "Deals (34;38) damage. (Gains Block equal to damage dealt.; Gains 99 Block.)"} |
| Bash | DebuffAttack3 | 12 |  | {"text": "Deals (12;14) damage. If the Player has an Orb Slot], there is 50% chance to apply -1 Focus. Otherwise applies -1 Strength."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `has_member` → [高塔之盾/高塔之矛 / Spire Shield and Spire Spear](sts1_monster_spire_shield_and_spire_spear.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Spire Shield | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 高塔之盾 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SpireShield", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 125, "ascension_min": 125, "ascension_raw": "125", "base_max": 110, "base_min": 110, "base_raw": "110"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Bash` | {"effect": {"text": "Deals (12;14) damage. If the Player has an Orb Slot], there is 50% chance to apply -1 Focus. Otherwise applies -1 Strength."}, "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Fortify` | {"effect": {"text": "All enemies gain 30 Block."}, "intent": "Defend"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Smash` | {"effect": {"text": "Deals (34;38) damage. (Gains Block equal to damage dealt.; Gains 99 Block.)"}, "intent": "DefendAttack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Spire Shield<br>|Image  = SpireShield.png<br>|HP     = 110<br>|AscHP  = 125<br>|Powers = {{BD|Artifact}} 1 ({{Asc|18|2}})<br>|Debut  = Act 4<br>|Type   = Elite<br>}}<br>{{Power Infobox|Back Attack}}<br>Spire Shield is an [[Elite]] enemy found exclusively in [[Act 4]].<br><br>=== Pattern ===<br>{{Intents Table/start|Spire Shield}}<br>{{Intents Table/row<br>|Name   = Bash<br>|Intent = DebuffAttack3<br>|Effect = Deals (12;{{Asc|3|14}}) damage. If the Player has an [[... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
