# 留给自己的讯息 / A Note For Yourself

> 稳定 ID：`sts1.event.a_note_for_yourself`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：留给自己的讯息
- English: A Note For Yourself

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Take and Give |  | {"text": "Receive and Store a Card * Receive a card that you had stored previously, and store a card in your deck in return. ** The first time the player encounters this event in their save file, it will have Iron Wave stored."} |
| 2 | Ignore |  | {"text": "Nothing happens. You are then given the option to"} |
| 3 | Leave |  | {"text": "."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Take and Give", "text": "Receive and Store a Card * Receive a card that you had stored previously, and store a card in your deck in return. ** The first time the player encounters this event in their save file, it will have Iron Wave stored."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Ignore", "text": "Nothing happens. You are then given the option to"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You spot a loose brick within a pillar that catches your eye.", "You find a folded note and a #ycard inside. It reads, NL \"The Heart awaits.\" NL NL This is your handwriting.", "Choose a Card to Store.", "What is going on?"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["一根柱子吸引了你的注意，你发现上面有一块松动的砖块。", "挪动砖块，你在里面找到了一张折起来的纸条和一张 #y牌 。纸条上写着： NL “高塔之心在等待。” NL NL 这……是你自己的笔迹。", "选择一张牌存放。", "这究竟是怎么回事？"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Continue]", "[Take and Give] #gReceive ", " #gand #gStore #ga #gCard.", "[Ignore]", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[继续]", "[取之与之] #g获得 ", " #g然后存放一张牌。", "[无视]", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | A Note For Yourself | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 留给自己的讯息 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "NoteForYourself", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>一根柱子吸引了你的注意，你发现上面有一块松动的石块。搬动砖块，你在里面找到了一张折起来的纸条和一张牌，纸条上写着：“高塔之心在等待。”这……是你自己的笔迹。<br>选项<br>取之与之 获得XX牌，然后存放一张牌<br>这究竟是怎么回事？<br>无视 （调出地图界面，继续行进）<br>这究竟是怎么回事？<br>注意<br>该事件无法在进阶15及以上或玩家当前的最大进阶等级的游戏中遇到。<br>玩家放入的牌可以在任何遇见该事件的一局中获取（仅一次），同时也允许玩家跨职业获取卡牌。<br>可以存放并取出诅咒牌。<br>取出的诅咒牌不会触发御守，但会触发黑石护符。<br>存放的牌会保留原先的强化状态（包括灼热攻击）。<br>成长型的卡牌（如仪式匕首和遗传算法）的数值会在取出时重置为初始状态。<br>若未开启进阶模式,则无论玩家之前是否获胜，都有可能遇到该事件。<br>玩家在自定义模式中存放的卡牌仍然能在普通模式下遇到，因此玩家可能会获得正常情况下无法获得的卡牌（如傲慢），也可获得升级级数极高的灼热攻击。<br>存放卡牌被视为将卡牌从玩家的牌组中... | `single_source` | [留给自己的讯息](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408938&wiki_id=646570) |
| `source.title_text` | 留给自己的讯息 | `single_source` | [留给自己的讯息](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408938&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=A Note For Yourself<br>|Image=Event-SelfNote.png<br>}}<br>{{E|A Note For Yourself}} is an [[Event]] encountered in all [[Acts]].<br><br>== Options ==<br>{{Frame|Take and Give}} {{TS|positive||Receive and Store a Card}}<br>* Receive a card that you had stored previously, and store a card in your deck in return.<br>** The first time the player encounters this event in their save file, it will have {{C|Iron Wave}} stored.<br>{{Frame|Ignore}} Nothing happens.<br><br><br><... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
