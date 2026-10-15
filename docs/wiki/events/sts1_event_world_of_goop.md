# 黏液世界 / World of Goop

> 稳定 ID：`sts1.event.world_of_goop`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：黏液世界
- English: World of Goop

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Gather Gold | {"text": "Lose 11 HP"} | {"text": "Gain 75 Gold"} |
| 2 | Leave It | {"text": "Lose X Gold"} | {"text": "* X is a random number between 20 and 50 (35 and 75) Gold. X cannot be more Gold than the player currently has"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Gather Gold", "text": "Gain 75 Gold"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave It", "text": "* X is a random number between 20 and 50 (35 and 75) Gold. X cannot be more Gold than the player currently has"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You fall into a puddle. NL @IT'S@ @MADE@ @OF@ #g@SLIME@ #g@GOOP!!@ NL Frantically, you claw yourself out over several minutes as you feel the goop starting to burn. NL You can feel goop in your ears, goop in your nose, goop everywhere. NL NL Climbing out, you notice that some of your #ygold is missing. Looking back to the puddle you see your missing coins combined with #ygold from unfortunate adventurers mixed together in the puddle.", "Feeling the sting of the goop as the prolonged exposur... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你掉进了一个水坑里。 NL 可是坑里 @全是@ #g@史莱姆黏液@ ！ NL 你感觉到这黏液似乎会灼伤你，便拼命想要从坑中脱身。 NL 你的耳朵、鼻子和全身都被黏液给浸透了。 NL NL 爬出来后，你发现自己的 #y金币 似乎变少了。你回头一看，发现水坑里不但有你掉落的钱，还有不少其他不幸的冒险者们落下的 #y金币 。", "在长时间与黏液接触而导致你的皮肤被烧走之前，你成功地捞出了不少 #y金币 。", "你决定这样做不值得。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Gather Gold] #gGain #g", " #gGold. #rLose #r", " #rHP.", "[Leave It] #rLose #r", " #rGold.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[收集金币] #g获得 #g", " #g金币。 #r失去 #r", " #r生命。", "[放手吧] #r失去 #r", " #r金币。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | World of Goop | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 黏液世界 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "World of Goop", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你掉进了一个水坑里。可是坑里全是史莱姆黏液！你感觉到这黏液似乎会灼伤你，便拼命想要从坑中脱身。你的耳朵、鼻子和全身都被黏液给浸透了。爬出来后，你发现自己的金币似乎变少了。你回头一看，发现水坑里不但有你掉落的钱，还有不少其他不幸的冒险者们落下的金币。<br>选项<br>收集金币 获得 75 金币。失去 11 生命。在长时间与黏液接触而导致你的皮肤被烧走之前，你成功地捞出了不少金币。<br>放手吧 失去 20~50(进阶15以上为35-75) 金币。你决定这样做不值得。<br>轶事<br>该事件的名字"World of Goop"大概来源于游戏"World of Goo"（粘粘世界）。 | `single_source` | [黏液世界](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375165&wiki_id=646570) |
| `source.title_text` | 黏液世界 | `single_source` | [黏液世界](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375165&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=World of Goop<br>|Image=Event-Goop.png<br>}}<br>{{E|World of Goop}} is an [[Event]] encountered exclusively in [[Act 1]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Gather Gold}} {{TS|positive||Gain 75 Gold.}} {{TS|negative||Lose 11 HP.}}<br><br><br><br>{{Frame|Leave It}} {{TS|negative||Lose X Gold.}}<br>* X is a random number between 20 and 50 {{Asc|15|(35 and 75)}} Gold. X cannot be more Gold than the player currently h... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
