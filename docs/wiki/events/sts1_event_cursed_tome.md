# 诅咒书本 / Cursed Tome

> 稳定 ID：`sts1.event.cursed_tome`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：诅咒书本
- English: Cursed Tome

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Read |  |  |
| 2 | Continue | {"text": "Lose 1 HP"} | {"text": "Lose 1 HP."} |
| 3 | Continue | {"text": "Lose 2 HP"} | {"text": "Lose 2 HP."} |
| 4 | Continue | {"text": "Lose 3 HP"} | {"text": "Lose 3 HP."} |
| 5 | Take | {"text": "Lose 10 (15) HP"} | {"text": "Obtain the book. . * The book may be Enchiridion, Nilry's Codex, or Necronomicon. The player does not know which book they will get until after they choose"} |
| 6 | Take | {"text": "lose their HP"} | {"text": "and"} |
| 7 | Stop | {"text": "Lose 3 HP"} | {"text": "Lose 3 HP."} |
| 8 | Leave | {"text": "lose 0 HP instead of selecting"} | {"text": "Nothing happens. === Practical Options === Because the player can choose to leave the event immediately and"} |
| 9 | Continue |  | {"text": "3 times and then backing out with"} |
| 10 | Stop |  | {"text": "while losing a total of 9 HP, there are really only 2 practical ways to navigate the event. The player can either commit to all the HP loss and obtain the book, or leave immediately to do nothing. For simplicity, the event's options can be thought of in this way instead:"} |
| 11 | Read |  | {"text": ", then all 3"} |
| 12 | Continue |  | {"text": ", and finally"} |
| 13 | Take | {"text": "Lose 16 (21) HP"} | {"text": "Obtain the book"} |
| 14 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Read", "text": ""} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.10` | {"label": "Stop", "text": "while losing a total of 9 HP, there are really only 2 practical ways to navigate the event. The player can either commit to all the HP loss and obtain the book, or leave immediately to do nothing. For simplicity, the event's options can be thought of in this way instead:"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.11` | {"label": "Read", "text": ", then all 3"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.12` | {"label": "Continue", "text": ", and finally"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.13` | {"label": "Take", "text": "Obtain the book. Lose 16 (21) HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.14` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Continue", "text": "Lose 1 HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Continue", "text": "Lose 2 HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Continue", "text": "Lose 3 HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.5` | {"label": "Take", "text": "Obtain the book. Lose 10 (15) HP. * The book may be Enchiridion, Nilry's Codex, or Necronomicon. The player does not know which book they will get until after they choose"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.6` | {"label": "Take", "text": "and lose their HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.7` | {"label": "Stop", "text": "Lose 3 HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.8` | {"label": "Leave", "text": "Nothing happens. === Practical Options === Because the player can choose to leave the event immediately and lose 0 HP instead of selecting"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.9` | {"label": "Continue", "text": "3 times and then backing out with"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["In an abandoned temple, you find a giant book, open, riddled with #p@cryptic@ #p@writings.@ NL NL As you try to interpret the elaborate script, it begins to #b~shift~ and #b~morph~ into writing you are familiar with.", "Odd. The book seems to be about an #yAncient named #yNeow. NL NL This piques your interest, but you have a general feeling of #p~malaise.~", "The Ancient of Resurrection, #yNeow, was exiled to the bottom of the Spire. NL NL You feel compelled to read more, but your body begi... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在一所被遗弃的神庙里，你找到一本翻开着的巨大书本，里面满是 #p@神秘的文字@ 。 NL NL 你刚试着想要解读这些复杂的文本，它就自己开始 #b~移动变化~ 成了你熟悉的文字。", "真奇怪。这本书的内容似乎是关于一名 叫做 #y涅奥 的 #y先古之民 。 NL NL 这引起了你的兴趣，但你总觉得这本书有点让你 #p~不适~ 。", "#y涅奥 是司管复活的先古之民，他被放逐到了高塔的底端。 NL NL 你觉得自己必须要读下去，可是你的身体开始觉得有一点 #r~疼痛~ 。", "#y寻求复仇 的 #y涅奥 会给予外来人祝福，利用他们来达成自己的目的。 NL NL 你开始觉得自己非常 #r~虚弱和疲劳……~", "那些被 #y涅奥 复活的人们只能零碎想起自己过去人生的记忆，他们被诅咒要永远战斗下去。 NL NL 当你快要翻到最后一页时，你的 #r@旧伤口似乎要绽开了@ ！", "看完书后，你决定把它带上。或许手握证据的现在，你将有可能保留住自己的记忆？", "你感觉到高台上的书本散发出一股 #p~黑暗的能量~ ，于是选择立即离开这里。", "你顶着极大的压力，强行用意志力抵抗... | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Read]", "[Continue] #rLose #r1 #rHP.", "[Continue] #rLose #r2 #rHP.", "[Continue] #rLose #r3 #rHP.", "[Stop] #rLose #r3 #rHP.", "[Take] #gObtain #gthe #gBook. #rLose #r", " #rHP.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[阅读]", "[继续] #r失去 #r1 #r生命。", "[继续] #r失去 #r2 #r生命。", "[继续] #r失去 #r3 #r生命。", "[停止] #r失去 #r3 #r生命。", "[拿走] #g获得书。 #r失去 #r", " #r生命。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Cursed Tome | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 诅咒书本 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Cursed Tome", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在一所被遗弃的神庙里，你找到一本翻开着的巨大书本，里面满是神秘的文字。你刚试着想要解读这些复杂的文本，它就自己开始移动变化成了你熟悉的文字。<br>选项<br>阅读真奇怪。这本书的内容似乎是关于一名 叫做涅奥的先古之民。这引起了你的兴趣，但你总觉得这本书有点让你不适。<br>继续 失去 1 生命。<br>涅奥是司管复活的先古之民，他被放逐到了高塔的底端。你觉得自己必须要读下去，可是你的身体开始觉得有一点疼痛。<br>继续 失去 2 生命。<br>寻求复仇的涅奥会给予外来人祝福，利用他们来达成自己的目的。你开始觉得自己非常虚弱和疲劳……<br>继续 失去 3 生命。<br>那些被涅奥复活的人们只能零碎想起自己过去人生的记忆，他们被诅咒要永远战斗下去。当你快要翻到最后一页时，你的旧伤口似乎要绽开了！<br>停止 失去 3 生命。<br>你顶着极大的压力，强行用意志力抵抗住书本的魔力，砰地一下使劲把书合上了。你转身离开神庙，觉得自己精疲力尽……<br>拿走 得到书。失去 10（进阶15以上为15） 生命。<br>看完书后，你决定把它带上。或许手... | `single_source` | [诅咒书本](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408873&wiki_id=646570) |
| `source.title_text` | 诅咒书本 | `single_source` | [诅咒书本](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408873&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Cursed Tome<br>|Image=Event-CursedTome.png<br>}} {{Small Relic Infobox|Enchiridion}} {{Small Relic Infobox|Nilry's Codex}} {{Small Relic Infobox|Necronomicon}}<br>{{E|Cursed Tome}} is an [[Event]] found exclusively in [[Act 2]].<br><br>== Options ==<br>{{Frame|Read}}<br><blockquote><br>{{Frame|Continue}} {{TS|negative||Lose 1 HP.}}<br><blockquote><br>{{Frame|Continue}} {{TS|negative||Lose 2 HP.}}<br><blockquote><br>{{Frame|Continue}} {{TS|negative||Lose 3 HP.}}<br><bl... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
