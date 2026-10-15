# 地精小队 / Gremlins

> 稳定 ID：`sts1.monster.gremlins`  
> 类别：`monster`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：地精小队
- English: Gremlins

## monster 合页上下文

本页对应来源中的组合页，只保留来源正文和 `has_member` 关系。生命值与行动请查看下方成员页面；不会把某个成员的数值投影到父页。

| 字段 | 值 |
| --- | --- |
| `encounter_notes` | Grouped wiki page only; structured HP/actions live on its has_member child entities. |

## 相关条目

- `has_member` → [胖地精 / Fat Gremlin](sts1_monster_fat_gremlin.md)
- `has_member` → [地精法师 / Gremlin Wizard](sts1_monster_gremlin_wizard.md)
- `has_member` → [火大地精 / Mad Gremlin](sts1_monster_mad_gremlin.md)
- `has_member` → [持盾地精 / Shield Gremlin](sts1_monster_shield_gremlin.md)
- `has_member` → [卑鄙地精 / Sneaky Gremlin](sts1_monster_sneaky_gremlin.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Gremlin Wizard | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 胖地精 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "GremlinThief", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["", "@Gonna@ @go@ NL @get@ @help!@", "I'm outta here!"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["", "@我去@ NL @叫援军！@", "溜了溜了！"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Claw"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 18, "ascension_min": 14, "ascension_raw": "14-18", "base_max": 17, "base_min": 13, "base_raw": "13-17"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Charging` | {"effect": "Does nothing.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Protect` | {"effect": "Random enemy gains (7;8 ; 11) Block. Only chooses self if alone.", "intent": "Defend"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Puncture` | {"effect": "Deals (9;10) damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Scratch` | {"effect": "Deals (4;5) damage.", "intent": "Attack1"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Shield Bash` | {"effect": "Deals (6;8) damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Smash` | {"effect": "Deals (4;5) damage. Applies 1 Weak(.; and 1 Frail.)", "intent": "DebuffAttack1"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Ultimate Blast` | {"effect": "Deals (25;30) damage.", "intent": "Attack6"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | （图片未提供文字说明）<br>胖地精<br>（图片未提供文字说明）<br>行为<br>（图片未提供文字说明）<br>火大地精<br>（图片未提供文字说明）<br>（图片未提供文字说明）<br>行为<br>输入图片描述<br>持盾地精<br>（图片未提供文字说明）<br>行为<br>（图片未提供文字说明）<br>如果还有其他敌人，始终对其他敌人进行防御，不会以自己为目标。如果没有其他敌人，才会进行攻击或对自己进行防御。<br>卑鄙地精<br>（图片未提供文字说明）<br>行为<br>（图片未提供文字说明）<br>地精法师<br>（图片未提供文字说明）<br>行为<br>（图片未提供文字说明）<br>地精法师首先蓄能两回合，然后进行一回合终极大爆炸，之后需要进行三回合蓄能才能进行一回合终极大爆炸。<br>进阶17+：地精法师在使用终极大爆炸后不会再蓄能，而是连续使用终极大爆炸。<br>出现<br>（图片未提供文字说明）<br>在第二阶段由地精首领召唤。<br>轶事<br>换脸商换取的脸中有地精容貌，但它不像现有的任何地精。<br>持盾地精在源代码中被命名为“GremlinTsunde... | `single_source` | [小地精](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411818&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/16/05f94912d79ba8ded51ba53b089f914f.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/5dd435cad6b45df896974c20f77dd4c6.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/cd8e37b23422b9e9274d23df952a7436.png"] | `single_source` | [小地精](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411818&wiki_id=646570) |
| `source.infobox.description` | 13-17 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 地精小队 | `single_source` | [小地精](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411818&wiki_id=646570) |
| `source.wikitext` | '''Gremlins''' are encountered as normal [[Monsters|Enemies]] in [[Act 1]]. In [[Act 2]], Gremlins appear only as {{BD|Minion|Minions}} in the {{M|Gremlin Leader|Gremlin Leader's}} [[Elite]] encounter.<br>{{TOC limit|2}}<br><br>== Fat Gremlin ==<br>{{Enemy Infobox<br>|Name   = Fat Gremlin<br>|Image  = GremlinFat.png<br>|HP     = 13-17<br>|AscHP  = 14-18<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>'''Fat Gremlins''' focus on applying {{BD|Weak}}.<br><br>=== Pattern ===<br>{{Intents Table/s... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
