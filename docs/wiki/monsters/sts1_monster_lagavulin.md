# 乐加维林 / Lagavulin

> 稳定 ID：`sts1.monster.lagavulin`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：乐加维林
- English: Lagavulin

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 1 |
| `hp_min` | 109 |
| `hp_max` | 109 |
| `ascension_json` | {"asc_hp": 112} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Stunned | Stunned |  |  | {"text": "Does nothing."} |
| Siphon Soul | DebuffStrong |  |  | {"text": "Applies (-1;-2) Dexterity and (-1;-2) Strength."} |
| Sleep | Sleep |  |  | {"text": "Does nothing."} |
| Attack | Attack4 | 18 |  | {"text": "Deals (18;20) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Lagavulin | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 乐加维林 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Lagavulin", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["", "... NL .....", "...? NL .....!?", "@!!!@ NL @!???@"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["击晕！", "… NL ……", "…？ NL ……！？", "@！！！@ NL @！？？？@"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Siphon Soul"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["灵魂吸取"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Attack` | {"effect": "Deals (18;20) damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Siphon Soul` | {"effect": "Applies (-1;-2) Dexterity and (-1;-2) Strength.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Sleep` | {"effect": "Does nothing.", "intent": "Sleep"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Stunned` | {"effect": "Does nothing.", "intent": "Stunned"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 沉睡状态<br>苏醒状态<br>注意<br>沉睡中的乐加维林会在生命流失时苏醒，亦或是在第四回合自行苏醒。<br>因生命流失而苏醒的乐加维林会在苏醒的那一回合晕眩，不采取任何行动；而自然苏醒的乐加维林会在苏醒后（即第四回合）立即采取攻击。<br>如果乐加维林是因为中毒受伤，那么它将在减少生命后立刻采取攻击而不会晕眩。<br>在“冒险家尸体”事件中，返回的乐嘉维林第一回合即进行灵魂汲取。<br>------------你惊醒了乐加老师！！！<br>行为<br>（图片未提供文字说明）<br>小技巧<br>乐加维林将在自然醒来前睡觉三个回合。这三个回合你可以准备你的战斗（比如打出能力牌），然后一举破盾把它打醒。把它打醒的那一回合尽量造成最高伤害，以缩短与其的战斗时间。<br>与其打消耗战绝不是个好主意。灵魂汲取回合尽管是个很优质的输出机会，但每一次灵魂汲取都会大大降低你的综合实力。<br>轶事<br>“乐加维林”来自盖尔语“Laga”“Mhuilinn”，意思是“磨坊的空洞”。<br>乐加维林的命名灵感可能来源于位于苏格兰艾莱的一家酿酒厂。这里也出产同名的威士忌。<br>目前游戏中，少... | `single_source` | [乐加维林](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421614&wiki_id=646570) |
| `source.infobox.description` | 109-111 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 乐加维林 | `single_source` | [乐加维林](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421614&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Lagavulin<br>|Image  = LagavulinAwake.png<br>|HP     = 109-111<br>|AscHP  = 112-115<br>|Powers = {{BD|Metallicize}} 8 <br> {{KW|Block}} 8<br>|Debut  = Act 1<br>|Type   = Elite<br>}}<br>{{Power Infobox|Metallicize}}<br>Lagavulin is an [[Elite]] enemy found exclusively in [[Act 1]] or in the {{E|Dead Adventurer}} Event.<br>== Pattern ==<br>{{Intents Table/start|Lagavulin}}<br>{{Intents Table/row<br>|Name   = Sleep<br>|Intent = Sleep<br>|Effect = Does nothing.}}<br>{... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
