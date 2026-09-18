# 腐化之心 / Corrupt Heart

> 稳定 ID：`sts1.monster.corrupt_heart`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：腐化之心
- English: Corrupt Heart

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | boss |
| `act` | Act 4 |
| `hp_min` | 750 |
| `hp_max` | 750 |
| `ascension_json` | {"ascension_max": 800, "ascension_min": 800, "ascension_raw": "800", "base_max": 750, "base_min": 750, "base_raw": "750"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Echo | Attack7 | 40 |  | {"text": "Deals (40;45) damage."} |
| Debilitate | DebuffStrong |  |  | {"text": "Applies 2 Vulnerable, 2 Weak and 2 Frail. Adds 1 Burn, 1 Dazed, 1 Slimed, 1 Void and 1 Wound into your draw pile."} |
| Blood Shots | Attack7 | 2 | 12 | {"text": "Deals (2×12;2×15) damage."} |
| Buff | Buff |  |  | {"text": "Loses all negative Strength, then gains 2 Strength. Gains an additional Buff]:"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Corrupt Heart | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 腐化之心 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "CorruptHeart", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 800, "ascension_min": 800, "ascension_raw": "800", "base_max": 750, "base_min": 750, "base_raw": "750"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Blood Shots` | {"effect": "Deals (2×12;2×15) damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Buff` | {"effect": "Loses all negative Strength, then gains 2 Strength. Gains an additional Buff]:", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Debilitate` | {"effect": "Applies 2 Vulnerable, 2 Weak and 2 Frail. Adds 1 Burn, 1 Dazed, 1 Slimed, 1 Void and 1 Wound into your draw pile.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Echo` | {"effect": "Deals (40;45) damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 腐化之心<br>Monster id: Corrupt Heart<br>怪物信息<br>生命值<br>750;(800;)<br>类型<br>Boss<br>意图<br>衰竭;血球连击;死亡回响;强化<br>初始能力<br>死亡律动1(2) 19+;坚不可摧300(200) 19+<br>备注<br>无<br>腐化之心是尖塔的最终BOSS，在塔顶（第四幕）盘踞。它是尖塔最具压迫力的BOSS，拥有强大的多段攻击和重击，随着战斗的进行，它的自我强化能力使其棘手程度倍增，因此快速击杀是个不错的策略，但它的脚下无数冒险家的尸体似乎有话要说........<br>如想降低心脏的压迫力，可在设置处关闭屏幕震动<br>行动类型<br>（图片未提供文字说明）<br>行动规律<br>（图片未提供文字说明）<br>初始能力<br>死亡律动：玩家角色每打出一张牌，就受到1/2点伤害<br>坚不可摧：每回合至多受到300/200伤害<br>行动<br>第一回合衰竭<br>下两回合，先重击后连击、先连击后重击各有一半概率<br>下一回合强化，清除力量下降并获得2力量。此外每次都获得不同的额外能力:<br... | `single_source` | [腐化之心](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408990&wiki_id=646570) |
| `source.infobox.description` | 750 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 腐化之心 | `single_source` | [腐化之心](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408990&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Corrupt Heart<br>|Image  = CorruptHeart.png<br>|Icon   = Map-CorruptHeart.png<br>|HP     = 750<br>|AscHP  = 800<br>|Powers = {{BD|Beat of Death}} 1 ({{Asc|19|2}}) <br> {{BD|Invincible}} 300 ({{Asc|19|200}})<br>|Debut  = Act 4<br>|Type   = Boss<br>}}<br>{{Power Infobox<br>|Name=Beat of Death<br>|Image=Icon_BeatOfDeath.png<br>|Description=Whenever you play a card, take X damage.<br>|Stacks=Intensity<br>|Type=Buff<br>|BetweenTurns=Permanent<br>}}<br>{{Power Infobox<b... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
