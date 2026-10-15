# 翅膀雕像 / Wing Statue

> 稳定 ID：`sts1.event.wing_statue`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：翅膀雕像
- English: Wing Statue

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Pray | {"text": "Lose 7 HP"} | {"text": "Remove a card from your deck"} |
| 2 | Destroy |  | {"text": "Receive 50 - 80 Gold. * Requires an Attack card in the player's deck that deals 10 or more damage in a single hit (e.g. Twin Strike does not count). * If the player's deck does satisfy the condition, this option is replaced with"} |
| 3 | Locked |  | {"text": "Requires: Card with 10 or more damage. * See the [[#Notes|Notes]] section for more details on which cards satisfy this requirement."} |
| 4 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Pray", "text": "Remove a card from your deck"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Destroy", "text": "Receive 50 - 80 Gold. * Requires an Attack card in the player's deck that deals 10 or more damage in a single hit (e.g. Twin Strike does not count). * If the player's deck does satisfy the condition, this option is replaced with"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Locked", "text": "Requires: Card with 10 or more damage. * See the [[#Notes|Notes]] section for more details on which cards satisfy this requirement."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Among the stone and boulders, you notice an intricate large blue statue resembling a wing. NL You find #ygold spilling from its cracks. Maybe there is more inside...", "Someone once told you of a cult that worshipped a giant bird. As you kneel in prayer, you begin to ~feel~ ... ~lightheaded~ . NL NL You wake up some time later, feeling strangely fleet of foot.", "With all your might, you hack away at the statue. NL It soon @crumbles,@ revealing a #ypile #yof #ygold. You grab as much as you ... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在形状不同的巨石之间，你看见一尊做工精细的翅膀形状的蓝色雕像。 NL 你可以看见雕像的裂缝中有 #y金币 掉出来。或许里面还有更多……", "你曾听人提起过一个崇拜巨大鸟类的邪教。当你跪下祷告的时候，你开始觉得 ~有一些头晕……~ NL NL 过了一会儿，你醒了过来，感觉脚步有点变轻了。", "你使出浑身的力气开始砸雕像。 NL 很快它就 @彻底裂开@ ，里面是 #y一大堆金币 。你把钱尽可能收集起来，重新上路。", "这个雕像让你觉得有点 ~不安~ 。你决定不要去惊扰它，直接离开了。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Pray] #gRemove #ga #gcard #gfrom #gyour #gdeck. #rLose #r", " #rHP.", "[Destroy] #gGain #g", " #g- #g", " #gGold.", "[Locked] Requires: Card with ", " or more damage.", "[Leave]", "[Continue]", "Select a Card to Remove."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[祈祷] #g从你的牌组中移除一张牌。 #r失去 #r", " #r生命。", "[摧毁] #g获得 #g", " #g～ #g", " #g金币。", "[锁定] 需要： 伤害等于或超过 ", " 的牌。", "[离开]", "[继续]", "选择一张牌移除。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Wing Statue | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 翅膀雕像 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Golden Wing", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在形状不同的巨石之间，你看见一尊做工精细的翅膀形状的蓝色雕像。你可以看见雕像的裂缝中有金币掉出来。或许里面还有更多……<br>选项<br>祈祷 从你的牌组中移除一张牌。失去 7 生命。你曾听人提起过一个崇拜巨大鸟类的邪教。当你跪下祷告的时候，你开始觉得有一些头晕……过了一会儿，你醒了过来，感觉脚步有点变轻了。<br>摧毁 获得 50-80 金币。 需要：伤害等于或超过 10 的牌。你使出浑身的力气开始砸雕像。很快它就彻底裂开，里面是一大堆金币。你把钱尽可能收集起来，重新上路。<br>离开这个雕像让你觉得有点不安。你决定不要去惊扰它，直接离开了。<br>轶事<br>该事件的文字描述中的“你曾听人提起过一个崇拜巨大鸟类的邪教”可能是影射对觉醒者的崇拜。 | `single_source` | [翅膀雕像](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375158&wiki_id=646570) |
| `source.title_text` | 翅膀雕像 | `single_source` | [翅膀雕像](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375158&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Wing Statue<br>|Image=Event-WingStatue.png<br>}}<br>{{E|Wing Statue}} is an [[Event]] found in [[Act 1]].<br><br>== Options ==<br>{{Frame|Pray}} {{TS|positive||Remove a card from your deck.}} {{TS|negative||Lose 7 HP.}}<br><br><br><br><br>{{Frame|Destroy}} {{TS|positive||Receive 50 - 80 Gold.}}<br>* Requires an {{QueryLink|Cards|type:Attack|Attack}} card in the player's deck that deals 10 or more damage '''in a single hit''' (e.g. {{C|Twin Strike}} does not count).<br... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
