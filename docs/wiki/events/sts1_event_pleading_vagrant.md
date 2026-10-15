# 流浪汉的恳求 / Pleading Vagrant

> 稳定 ID：`sts1.event.pleading_vagrant`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：流浪汉的恳求
- English: Pleading Vagrant

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Offer Gold |  | {"text": "85 Gold]: Obtain a Relic]. * If the player does not have enough Gold], this option will be greyed out."} |
| 2 | Rob | {"text": "Become Cursed - Shame"} | {"text": "Obtain a Relic]"} |
| 3 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Offer Gold", "text": "85 Gold]: Obtain a Relic]. * If the player does not have enough Gold], this option will be greyed out."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Rob", "text": "Obtain a Relic]"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["While sneaking past a group of shrouded figures, one of them approaches you. NL \"Got anything for me friend? Please... maybe some #yCoin?\" NL \"I just need somewhere to stay, I have treasures I can trade...\" NL He seems delusional, but harmless.", "\"Oh yes, ~yes!~ Here here, a fair trade!\"", "You snatch the precious #yrelic from his clutches and walk away. NL From behind you hear, NL \"Have you no shame? ~HAVE~ ~YOU~ ~NO~ ~SHAAAAAME?!\"~ NL You have some #pshame."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你想要从一群披着斗篷的人旁边偷偷潜行过去，其中一个跑到了你面前。 NL “你能给我点儿什么吗，朋友？ 求求你了……一点 #y小钱 就好？” NL “我只是需要找个地方过夜，我身上有财宝可以交换……” NL 他看起来有点疯疯癫癫的，但似乎并不危险。", "“啊啊，太好了， ~太好了！~ 来来，给你，公平交易！”", "你一把抓过他手中珍贵的 #y遗物 转身就走。 NL 身后传来他的声音： NL “你不知道什么是羞耻吗？ ~你就~ ~不知道~ ~什么是羞耻吗？！~” NL 你确实感到了一点 #p羞耻 。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Offer Gold] #y", " #yGold: #gObtain #ga #gRelic.", "[Locked] Requires: ", " Gold.", "[Rob] #gObtain #ga #gRelic. #rBecome #rCursed #r- #rShame.", "[Leave]", "", ""] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[给他金币] #y", "  #y金币： #g获得一件遗物。", "[锁定] 需要： ", " 金币。", "[抢夺] #g获得一件遗物。 #r被诅咒——羞耻。", "[离开]", "", ""] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Pleading Vagrant | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 流浪汉的恳求 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Addict", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你想要从一群披着斗篷的人旁边偷偷潜行过去，这时一个皮肤发红的赤裸男人跑到了你的面前。“你能给我点儿什么吗,朋友？求求你了……一点小钱就好？”<br>“我只是需要找个地方过夜，我身上有财宝可以交换……”他看起来疯疯癫癫的，但并没有危险。<br>选项<br>给他金币 85 金币：得到一件遗物。 需要：85 金币。“啊啊，太好了，太好了！来，给你，这很公平吧！”<br>抢夺. 获得一件遗物。被诅咒——羞耻。你一把抓过他手中珍贵的遗物转身就走。 身后传来他的声音： “你不知道什么是羞耻吗？你就不知道~什么是羞耻吗？！~” 你确实感到了一点羞耻<br>离开无对话，调出地图<br>轶事<br>该事件的英文名称曾为"Addicted", 但后来更名为了"Pleading Vagrant"，大概是想和药物滥用这一负面含义和担忧保持距离。 | `single_source` | [流浪汉的恳求](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408865&wiki_id=646570) |
| `source.title_text` | 流浪汉的恳求 | `single_source` | [流浪汉的恳求](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408865&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Pleading Vagrant<br>|Image=Event-Vagrant.png<br>}} {{Small Card Infobox|Shame}}<br>{{E|Pleading Vagrant}} is an [[Event]] found exclusively in [[Act 2]]. It will only appear if the player has at least 75 [[Gold]].<br><br>== Options ==<br>{{Frame|Offer Gold}} {{TS|gold||85 [[Gold]]:}} {{TS|positive||Obtain a [[Relic]].}}<br>* If the player does not have enough [[Gold]], this option will be greyed out.<br><br>{{Frame|Rob}} {{TS|positive||Obtain a [[Relic]].}} {{TS|negat... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
