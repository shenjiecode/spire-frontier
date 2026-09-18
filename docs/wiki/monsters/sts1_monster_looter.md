# 抢劫的 / Looter

> 稳定 ID：`sts1.monster.looter`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：抢劫的
- English: Looter

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 44 |
| `hp_max` | 44 |
| `ascension_json` | {"asc_hp": 46} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Smoke Bomb | Defend |  |  | {"text": "Gains 6 Block."} |
| Lunge | Attack4 | 16 |  | {"text": "Deals (16;18) damage."} |
| Escape | Escape |  |  | {"text": "Flees combat with your Gold]."} |
| Lunge | Attack3 | 12 |  | {"text": "Deals (12;14) damage."} |
| Smoke Bomb | Defend |  |  | {"text": "Gains (11;17) Block."} |
| Mug | Attack3 | 10 |  | {"text": "Deals (10;11) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Looter | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 抢劫的 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Looter", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["Give me your gold!", "@NOOOoooo!@", "Where's my smoke bomb... Let's see here...", "Thanks for the money, hehe"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["把钱交出来！", "@不——！@", "我的烟雾弹在哪儿呢……我找找……", "多谢你的钱啦，嘿嘿"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Lunge", "Mug"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["突刺", "打劫"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Escape` | {"effect": "Flees combat with your Gold].", "intent": "Escape"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Lunge` | {"effect": "Deals (12;14) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Mug` | {"effect": "Deals (10;11) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Smoke Bomb` | {"effect": "Gains 6 Block.", "intent": "Defend"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 掠夺者<br>Monster id: Looter<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>44;48(46;50)<br>类型<br>普通<br>意图<br>盗窃;重击;找烟雾弹;逃跑<br>初始能力<br>盗窃15(20)<br>备注<br>无<br>行动<br>行动<br>效果<br>进阶2+<br>进阶17+<br>备注<br>盗窃<br>造成10点伤害<br>造成11点伤害<br>造成11点伤害<br>"<br>把钱交出来!"<br>重击<br>造成12点伤害<br>造成14点伤害<br>造成14点伤害<br>找烟<br>雾弹<br>获得6点格挡<br>获得6点格挡<br>获得6点格挡<br>"<br>我的烟雾弹<br>在哪里呢?"<br>逃跑<br>带着盗窃的金币逃离战斗<br>"<br>我可溜啦!"/<br>"<br>谢谢你的钱了"<br>前两回合将会使用<br>盗窃<br>，第三回合有50%概率使用<br>重击<br>或者<br>找烟雾弹<br>。<br>若使用了<br>重击<br>，则随后使用<br>找烟雾弹<br>。<br>若使用<b... | `single_source` | [抢劫的](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421076&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/17/003f3e46d70e9bae1d315e3def3225c3.png", "https://imgheybox.max-c.com/web/bbs/2024/08/17/43419d2149c9e59ca868f6b6baf6684b.png"] | `single_source` | [抢劫的](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421076&wiki_id=646570) |
| `source.infobox.description` | 44-48 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 抢劫的 | `single_source` | [抢劫的](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421076&wiki_id=646570) |
| `source.wikitext` | == Looter ==<br>{{Enemy Infobox<br>|Name   = Looter<br>|Image  = Looter.png<br>|HP     = 44-48<br>|AscHP  = 46-50<br>|Powers = {{BD|Thievery}} 15 ({{Asc|17|20}})<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>{{Power Infobox|Thievery}}<br>'''Looter''' is a normal [[Monsters|Enemy]] that can show up in [[Act 1]] and [[Act 2]].<br><br>=== Pattern ===<br>{{Intents Table/start|Looter}}<br>{{Intents Table/row<br>|Name   = Mug<br>|Intent = Attack3<br>|Effect = Deals (10;{{Asc|2|11}}) damage.}}<br>... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
