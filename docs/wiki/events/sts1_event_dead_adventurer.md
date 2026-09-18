# 冒险者尸体 / Dead Adventurer

> 稳定 ID：`sts1.event.dead_adventurer`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：冒险者尸体
- English: Dead Adventurer

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Search |  | {"text": "Find Loot. 25% (35%): monster returns. * Each"} |
| 2 | Search |  | {"text": "attempt will either cause an Act 1 Elite] to return and fight the player, or yield one of the following rewards: ** 30 Gold] ** A random Relic] ** Nothing * Each reward only occurs once - if the player's first search found nothing and the second search found the Relic], the third search will either reward 30 Gold] or start a battle. * Each reward that is acquired before fighting the Elite] will be removed from its combat rewards if the player eventually does fight the Elite] and defeats it. ** For example, if the player's first"} |
| 3 | Search |  | {"text": "is a Relic], the Elite] will not drop a Relic] when it is defeated. ** This is also the reason why this specific Elite] fight can drop 30 extra Gold] compared to a normal Elite]; because the 30 Gold]"} |
| 4 | Search |  | {"text": "reward is added to the normal Gold] reward of defeating an Elite]. * Each subsequent"} |
| 5 | Search |  | {"text": "increases the chance to encounter an Elite] by 25%. * If the player manages to successfully"} |
| 6 | Search |  | {"text": "three times without encountering an Elite], the event will end with a short dialogue detailing the success. * For the second and third searches (assuming the player is not ambushed),"} |
| 7 | Search |  | {"text": "will be called"} |
| 8 | Continue |  | {"text": "instead. Its behavior and description are unchanged."} |
| 9 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Search", "text": "Find Loot. 25% (35%): monster returns. * Each"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Search", "text": "attempt will either cause an Act 1 Elite] to return and fight the player, or yield one of the following rewards: ** 30 Gold] ** A random Relic] ** Nothing * Each reward only occurs once - if the player's first search found nothing and the second search found the Relic], the third search will either reward 30 Gold] or start a battle. * Each reward that is acquired before fighting the Elite] will be removed from its combat rewards if the player eventually does fight... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Search", "text": "is a Relic], the Elite] will not drop a Relic] when it is defeated. ** This is also the reason why this specific Elite] fight can drop 30 extra Gold] compared to a normal Elite]; because the 30 Gold]"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Search", "text": "reward is added to the normal Gold] reward of defeating an Elite]. * Each subsequent"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.5` | {"label": "Search", "text": "increases the chance to encounter an Elite] by 25%. * If the player manages to successfully"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.6` | {"label": "Search", "text": "three times without encountering an Elite], the event will end with a short dialogue detailing the success. * For the second and third searches (assuming the player is not ambushed),"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.7` | {"label": "Search", "text": "will be called"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.8` | {"label": "Continue", "text": "instead. Its behavior and description are unchanged."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.9` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["While searching the adventurer you are caught off guard!", "You exit without a sound.", "You come across a #rdead #radventurer on the floor. NL His #bpants have been stolen! Also, ", "the armor and face appear to be #r@scoured@ #r@by@ #r@flames.@ ", "it looks as though he's been #r@gouged@ #r@and@ #r@trampled@ by a horned beast. ", "he looks to have been #r@eviscerated@ #r@and@ #r@chopped@ by giant claws. ", "NL Though his #ypossessions #yare #ystill #yintact, you're in no mind to find out ... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在搜刮冒险者时你被偷袭了！", "你一声不发地离开了。", "你发现地上有一具 #r冒险者尸体 。 NL 他的 #b裤子 都被偷了！而且，", "他的护甲和脸似乎被 #r@火焰灼烧@ 过。", "看起来他被一个带角的生物 #r@戳伤@ 和 #r@踩踏@ 过。", "他的内脏似乎被巨大的爪子 #r@撕扯出来@ 并 #r@切碎@ 了。", " NL 尽管他随身 #y携带的东西 好像都还在，你实在是不想知道这里究竟发生了什么……", "你找到了一些 #y金币 ！ NL 要继续找吗？", "唔，什么也没找到…… NL 要继续找吗？", "你找到一件 #y遗物 ！ NL 要继续找吗？", "看起来你成功翻遍了他的所有物，什么事也没发生！"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Search] #gFind #gLoot. #r", "[Leave]", "[Fight]", "[Continue] #gFind #gLoot. #r", "%: #rmonster #rreturns."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[搜索] #g寻找东西。 #r", "[离开]", "[战斗]", "[继续] #g寻找东西。 #r", "%： #r遇见回来的怪物。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Dead Adventurer | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 冒险者尸体 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Dead Adventurer", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你发现地上有一具冒险者尸体。他的裤子都被偷了！而且，情况 1：他的护甲和脸似乎被火焰灼烧过。情况 2：看起来他被一个带角的生物戳伤和踩踏过。情况 3：他的内脏似乎被巨大的爪子撕扯出来并切碎了。尽管他随身携带的东西好像都还在，你实在是不想知道这里究竟发生了什么……<br>选项<br>搜索 寻找东西。25%(进阶15：35%) ：遇见回来的怪物。结果 1：你找到了一些金币！要继续找吗？结果 2：唔，什么也没找到……要继续找吗？结果 3：你找到一件遗物！要继续找吗？结果 4：在搜刮冒险者时你被偷袭了！<br>继续 寻找东西。50%(进阶15：60%) ：遇见回来的怪物。<br>继续 寻找东西。75%(进阶15：85%) ：遇见回来的怪物。<br>如果没有遇到怪物：看起来你成功翻遍了他的所有物，什么事也没发生！<br>战斗<br>离开<br>你一声不发地离开了。<br>注意<br>击杀精英会奖励未搜索到的所有奖励。但精英本身不会提供额外的奖励。若玩家已然搜索并找到该遗物，则可能要考虑选择离开，因为此时击杀精英后只会掉落卡牌、金币以及得分奖励。<b... | `single_source` | [冒险者尸体](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375140&wiki_id=646570) |
| `source.title_text` | 冒险者尸体 | `single_source` | [冒险者尸体](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375140&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Dead Adventurer<br>|Image=Event-DeadAdventurer.png<br>}}<br>{{E|Dead Adventurer}} is an [[Event]] found exclusively in [[Act 1]].<br><br>== Options ==<br>{{Frame|Search}} {{TS|positive||Find Loot.}} {{TS|negative||25%}} {{Asc|15|(35%)}}{{TS|negative||: monster returns.}}<br>* Each {{Frame|Search}} attempt will either cause an [[Elites#Act 1 Elites|Act 1 Elite]] to return and fight the player, or yield one of the following rewards:<br>** 30 [[Gold]]<br>** A random [[Re... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
