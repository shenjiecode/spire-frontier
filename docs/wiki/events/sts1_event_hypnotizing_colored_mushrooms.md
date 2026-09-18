# 蘑菇 / Hypnotizing Colored Mushrooms

> 稳定 ID：`sts1.event.hypnotizing_colored_mushrooms`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：蘑菇
- English: Hypnotizing Colored Mushrooms

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Stomp |  | {"text": "Anger the Mushrooms. * Enter a battle against 3 Fungi Beasts. Winning grants the exclusive Relic] Odd Mushroom along with regular combat rewards."} |
| 2 | Eat | {"text": "Become Cursed - Parasite"} | {"text": "Heal X HP. . * X is equal to 25% of the player's max HP"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Stomp", "text": "Anger the Mushrooms. * Enter a battle against 3 Fungi Beasts. Winning grants the exclusive Relic] Odd Mushroom along with regular combat rewards."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Eat", "text": "Heal X HP. Become Cursed - Parasite. * X is equal to 25% of the player's max HP."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You give in to the unnatural desire to eat. As you consume mushroom after mushroom, you feel yourself entering into a daze and pass out. As you awake, you feel very odd. NL You #gHeal #b25% of your HP, but you also get #rinfected.", "#r@Ambushed!!@ NL Rodents infested by the mushrooms appear out of nowhere!", "You enter a corridor full of #b~hypnotizing~ #b~colored~ #b~mushrooms.~ NL Due to your lack of specialization in mycology you are unable to identify the specimens. NL You want to esca... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你顺从了这份不自然的食欲，吃下一个又一个蘑菇后，你觉得自己有点晕晕的，然后就失去了意识。当你醒来时，你觉得有点怪怪的 NL 你 #g回复 生命值的 #b25% ，但同时被 #r感染 了。", "#r@有埋伏！！@ NL 被蘑菇感染的啮齿类动物们不知从哪里冒了出来！", "你走进一条遍地是 #b~五彩斑斓蘑菇~ 的走廊， NL 由于你对真菌学毫无研究，你无法辨识它们的种类。 NL 你想要离开这里，但却有一种奇怪的冲动想要去吃一个 #b~蘑菇……~"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Stomp] #rAnger #rthe #rMushrooms.", "[Eat] #gHeal #g", " #gHP. #rBecome #rCursed #r- #rParasite.", "[Fight]", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[踩扁] #r激怒蘑菇们。", "[吃下]  #g回复 #g", " #g点生命。 #r被诅咒——寄生。", "[战斗]", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Mushrooms | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 蘑菇 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Mushrooms", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你走进一条遍地是五彩斑斓蘑菇的走廊，由于你对真菌学毫无研究，你无法辨识它们的种类。你想要离开这里，但却有一种奇怪的冲动想要去吃一个蘑菇……<br>选项<br>踩扁 激怒蘑菇们。有埋伏！！被蘑菇感染的啮齿类动物们不知从哪里冒了出来！<br>吃下 回复 25% 生命。被诅咒——寄生。你顺从了这份不自然的食欲，吃下一个又一个蘑菇后，你觉得自己有点晕晕的，然后就失去了意识。当你醒来时，你觉得有点怪怪的<br>你回复生命值的 25%，但同时被感染了 | `single_source` | [蘑菇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375291&wiki_id=646570) |
| `source.title_text` | 蘑菇 | `single_source` | [蘑菇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375291&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Hypnotizing Colored Mushrooms<br>|Image=Event-Mushrooms.png<br>}} {{Small Relic Infobox|Odd Mushroom}} {{Small Card Infobox|Parasite}}<br>{{E|Hypnotizing Colored Mushrooms}} is an [[Event]] encountered exclusively in [[Act 1]]. It will only appear if the player is on floor 7 or above. This Event is the only way to obtain {{R|Odd Mushroom}}.<br><br>== Options ==<br>{{Frame|Stomp}} {{TS|negative||Anger the Mushrooms.}}<br><br>* Enter a battle against 3 {{M|Fungi Beast|F... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
