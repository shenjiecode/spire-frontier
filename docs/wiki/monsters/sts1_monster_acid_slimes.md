# 酸液史莱姆 / Acid Slimes

> 稳定 ID：`sts1.monster.acid_slimes`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：酸液史莱姆
- English: Acid Slimes

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 64 |
| `hp_max` | 64 |
| `ascension_json` | {"asc_hp": 67} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Flame Tackle | DebuffAttack2 | 8 |  | {"text": "Deals (8;10) damage. Adds a Slimed into your discard pile."} |
| Split | Unknown |  |  | {"text": "Disappears and spawns 2 Acid Slimes (M) with its current HP."} |
| Tackle | Attack2 | 5 |  | {"text": "Deals (5;6) damage."} |
| Corrosive Spit | DebuffAttack2 | 7 |  | {"text": "Deals (7;8) damage. Adds a Slimed into your discard pile."} |
| Tackle | Attack3 | 10 |  | {"text": "Deals (10;12) damage."} |
| Split | Unknown |  |  | {"text": "Disappears and spawns 2 Spike Slimes (M) with its current HP."} |
| Lick | Debuff |  |  | {"text": "Applies (2;3) Frail."} |
| Corrosive Spit | DebuffAttack3 | 11 |  | {"text": "Deals (11;12) damage. Adds 2 Slimed into your discard pile."} |
| Flame Tackle | DebuffAttack4 | 16 |  | {"text": "Deals (16;18) damage. Adds 2 Slimed into your discard pile."} |
| Lick | Debuff |  |  | {"text": "Applies 1 Weak."} |
| Tackle | Attack1 | 3 |  | {"text": "Deals (3;4) damage."} |
| Lick | Debuff |  |  | {"text": "Applies 2 Weak."} |
| Lick | Debuff |  |  | {"text": "Applies 1 Frail."} |
| Tackle | Attack4 | 16 |  | {"text": "Deals (16;18) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Acid Slime (L) | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 酸液史莱姆（大） | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "AcidSlime_L", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["打断！"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Corrosive Spit", "Split", "Lick"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["腐蚀喷吐", "分裂", "舔舔"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Corrosive Spit` | {"effect": "Deals (11;12) damage. Adds 2 Slimed into your discard pile.", "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Flame Tackle` | {"effect": "Deals (16;18) damage. Adds 2 Slimed into your discard pile.", "intent": "DebuffAttack4"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Lick` | {"effect": "Applies (2;3) Frail.", "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Split` | {"effect": "Disappears and spawns 2 Spike Slimes (M) with its current HP.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tackle` | {"effect": "Deals (5;6) damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 酸液史莱姆（大）<br>（图片未提供文字说明）<br>怪物分布<br>（图片未提供文字说明）<br>行动类型<br>（图片未提供文字说明）<br>行动规律<br>（图片未提供文字说明）<br>进阶17以下<br>只要可能，腐蚀喷吐、重击、舔舔的权重为3:4:3。<br>不可能连续进行两次重击，其余行动不可能连续进行三次。<br>进阶 17以上<br>只要可能，腐蚀喷吐、重击、舔舔的权重为4:3:3。<br>不可能连续进行两次舔舔，其余行动不可能连续进行三次。<br>酸液史莱姆（中）<br>（图片未提供文字说明）<br>怪物分布<br>（图片未提供文字说明）<br>行动类型<br>（图片未提供文字说明）<br>行动规律<br>（图片未提供文字说明）<br>进阶17以下<br>只要可能，腐蚀喷吐、重击、舔舔的权重为3:4:3。<br>不可能连续进行两次重击，其余行动不可能连续进行三次。<br>进阶 17以上<br>只要可能，腐蚀喷吐、重击、舔舔的权重为4:4:2。<br>不可能连续进行两次舔舔，其余行动不可能连续进行三次。<br>酸液史莱姆（小）<br>（图片未提供文字说明）<br>... | `single_source` | [酸液史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411814&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/16/0286d9ec4dab15fbbfd5833ae036db06.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/029675d0d6b21a2b0ea45fa4b9f37c81.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/2c480220fffeea895acb8cd44435b504.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/687cb53e08d77166f7953bc8360dcca2.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/773473d54cfe0617da30116cce0691e7.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/af0d96c24b9b7... | `single_source` | [酸液史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411814&wiki_id=646570) |
| `source.infobox.description` | 64-70 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 酸液史莱姆 | `single_source` | [酸液史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411814&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{TOC limit|2}}<br>== Spike Slime (L) ==<br>{{Enemy Infobox<br>|Name   = Spike Slime (L)<br>|Image  = SpikeSlimeL.png<br>|HP     = 64-70<br>|AscHP  = 67-73<br>|Powers = {{BD|Split}}<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>{{Power Infobox|Split}}<br>'''Spike Slime (L)''' is a normal [[Monsters|Enemy]] found exclusively in Act 1.<br><br>=== Pattern ===<br>{{Intents Table/start|Spike Slime (L)}}<br>{{Intents Table/row<br>|Name   = Lick<br>|Intent = Debuff<br>... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
