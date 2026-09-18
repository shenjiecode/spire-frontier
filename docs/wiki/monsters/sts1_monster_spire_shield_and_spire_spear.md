# 高塔之盾/高塔之矛 / Spire Shield and Spire Spear

> 稳定 ID：`sts1.monster.spire_shield_and_spire_spear`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：高塔之盾/高塔之矛
- English: Spire Shield and Spire Spear

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 4 |
| `hp_min` | 110 |
| `hp_max` | 110 |
| `ascension_json` | {"asc_hp": 125} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Bash | DebuffAttack3 | 12 |  | {"text": "Deals (12;14) damage. If the Player has an Orb Slot], there is 50% chance to apply -1 Focus. Otherwise applies -1 Strength."} |
| Fortify | Defend |  |  | {"text": "All enemies gain 30 Block."} |
| Burn Strike | DebuffAttack3 | 5 |  | {"text": "Deals (5×2;6×2) damage. (Adds 2 Burns into your discard pile.; Adds 2 Burns on top of your draw pile.)"} |
| Piercer | Buff |  |  | {"text": "All enemies gain 2 Strength."} |
| Skewer | Attack7 | 10 |  | {"text": "Deals (10×3;10×4) damage."} |
| Smash | DefendAttack7 | 34 |  | {"text": "Deals (34;38) damage. (Gains Block equal to damage dealt.; Gains 99 Block.)"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

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
| `monster.move.Bash` | {"effect": "Deals (12;14) damage. If the Player has an Orb Slot], there is 50% chance to apply -1 Focus. Otherwise applies -1 Strength.", "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Burn Strike` | {"effect": "Deals (5×2;6×2) damage. (Adds 2 Burns into your discard pile.; Adds 2 Burns on top of your draw pile.)", "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Fortify` | {"effect": "All enemies gain 30 Block.", "intent": "Defend"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Piercer` | {"effect": "All enemies gain 2 Strength.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Skewer` | {"effect": "Deals (10×3;10×4) damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Smash` | {"effect": "Deals (34;38) damage. (Gains Block equal to damage dealt.; Gains 99 Block.)", "intent": "DefendAttack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 高塔之盾/高塔之矛是杀戮尖塔中的一只怪物。<br>（图片未提供文字说明）<br>高塔之盾<br>（图片未提供文字说明）<br>它与高塔之矛一同在终幕的精英战中出现。<br>如果你未面对着它，他将会获得后方攻击效果<br>行动模式<br>名称<br>效果<br>效果（进阶3+）<br>效果（进阶18+）<br>痛击<br>造成12点伤害如果玩家至少有一个充<br>能球栏位，则有50%几<br>率减去1点集中<br>否则，减去1点力量<br>造成14点伤害如果玩家至少有一个充<br>能球栏位，则有50%几<br>率减去1点集中<br>否则，减去1点力量<br>造成14点伤害如果玩家至少有一个充<br>能球栏位，则有50%几<br>率减去1点集中<br>否则，减去1点力量<br>加固<br>给予所有敌人30点格挡<br>给予所有敌人30点格挡<br>给予所有敌人30点格挡<br>粉碎<br>造成34点伤害获得等同于其伤害输出的格挡<br>造成38点伤害获得等同于其伤害输出的格挡<br>造成38点伤害获得99点格挡<br>高塔之盾的攻击呈现出一个三回合的循环：<br>第一回合，各有50%... | `single_source` | [高塔之盾/高塔之矛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9959050&wiki_id=646570) |
| `source.infobox.description` | 110 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 高塔之盾/高塔之矛 | `single_source` | [高塔之盾/高塔之矛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9959050&wiki_id=646570) |
| `source.wikitext` | == Spire Shield ==<br>{{Enemy Infobox<br>|Name   = Spire Shield<br>|Image  = SpireShield.png<br>|HP     = 110<br>|AscHP  = 125<br>|Powers = {{BD|Artifact}} 1 ({{Asc|18|2}})<br>|Debut  = Act 4<br>|Type   = Elite<br>}}<br>{{Power Infobox|Back Attack}}<br>Spire Shield is an [[Elite]] enemy found exclusively in [[Act 4]].<br><br>=== Pattern ===<br>{{Intents Table/start|Spire Shield}}<br>{{Intents Table/row<br>|Name   = Bash<br>|Intent = DebuffAttack3<br>|Effect = Deals (12;{{Asc|3|14}}) damage. I... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
