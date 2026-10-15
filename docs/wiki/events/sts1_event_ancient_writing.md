# 古老文字 / Ancient Writing

> 稳定 ID：`sts1.event.ancient_writing`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：古老文字
- English: Ancient Writing

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Elegance |  | {"text": "Remove a card from your deck."} |
| 2 | Simplicity |  | {"text": "Upgrade] all Strikes and Defends. * Only includes Basic cards."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Elegance", "text": "Remove a card from your deck."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Simplicity", "text": "Upgrade] all Strikes and Defends. * Only includes Basic cards."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Scaling the city, you notice a wall covered in the writing of #y~Ancients.~ As you try to wrap your head around what the puzzling symbols and glyphs could mean, the writing begins to #b~glow.~ NL Suddenly, the message becomes clear...", "The answer was elegance. NL Of course.", "The truth is always simple."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在攀爬城市区时，你注意到一面墙壁上写满了 #y~先古之民~ 的文字。你正在努力推理这些奇怪的符号和图案可能的意思，却发现文字开始 #b~发起了光~ 。 NL 突然之间，文字的意义变得清晰了……", "答案当然是简洁。", "真相总是朴素的。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Elegance] #gRemove #ga #gcard #gfrom #gyour #gdeck.", "[Simplicity] #gUpgrade #gall #gStrikes #gand #gDefends.", "Select a Card to Remove.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[简约] #g从你的牌组中移除一张牌。", "[质朴] #g升级所有 #g打击 #g与 #g防御 。", "选择一张牌移除。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Ancient Writing | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 古老文字 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Back to Basics", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在攀爬城市区时，你注意到一面墙壁上写满了先古之民的文字。你正在努力推理这些奇怪的符号和图案可能的意思，却发现文字开始发起了光。突然之间，文字的意义变得清晰了……<br>选项<br>简约 从你的牌组中移除一张牌。答案当然是简洁。<br>质朴 升级所有打击与防御。 | `single_source` | [古老文字](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408867&wiki_id=646570) |
| `source.title_text` | 古老文字 | `single_source` | [古老文字](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408867&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Ancient Writing<br>|Image=Event-AncientWriting.png<br>}}<br>{{E|Ancient Writing}} is an [[Event]] found exclusively in [[Act 2]].<br><br>== Options ==<br>{{Frame|Elegance}} {{TS|positive||Remove a card from your deck.}}<br><br><br><br><br>{{Frame|Simplicity}} {{TS|positive||[[Upgrade]] all Strikes and Defends.}}<br>* Only includes {{QueryLink|Cards|rarity:Basic|Basic}} cards.<br><br>== Dialogue ==<br><blockquote><div style="font-style:italic"><br>Scaling the city, you... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
