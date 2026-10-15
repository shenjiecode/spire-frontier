# 复制祭坛 / Duplicator

> 稳定 ID：`sts1.event.duplicator`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：复制祭坛
- English: Duplicator

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Pray |  | {"text": "Duplicate a card in your deck."} |
| 2 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Pray", "text": "Duplicate a card in your deck."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Before you lies a decorated altar to some ancient entity.", "You kneel respectfully. A ghastly mirror image appears from the shrine and collides into you.", "You ignore the shrine, confident in your choice."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在你面前是一个用来崇拜某种古老存在的华丽祭坛。", "你尊敬地跪了下来，祭坛上出现一个可怖的镜像影像，撞到了你的身上。", "你无视了这个祭坛，认为这才是正确的选择。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Pray] #gDuplicate #ga #gcard #gin #gyour #gdeck.", "[Leave]", "Select a Card to Duplicate."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[祈祷] #g从你的牌组中复制一张牌。", "[离开]", "选择一张牌复制。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Duplicator | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 复制祭坛 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Duplicator", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在你面前是一个用来崇拜某种古老存在的华丽祭坛。<br>选项<br>祈祷 从你的牌组中复制一张牌。你尊敬地跪了下来，祭坛上出现一个可怖的镜像影像，撞到了你的身上。<br>离开你无视了这个祭坛，认为这才是正确的选择。<br>注意<br>若玩家复制升级过的牌，则复制出的牌也同为升级版。<br>复制成长类卡牌（如：遗传算法、仪式匕首等），则此牌所成长的数值亦会保留。<br>被瓶装的卡牌不会保留被瓶装的特性，同时玩家无法在首回合内抽到此牌的复制品。<br>但若复制具有固有属性的卡牌，则此牌仍然可保留此属性。 | `single_source` | [复制祭坛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408940&wiki_id=646570) |
| `source.title_text` | 复制祭坛 | `single_source` | [复制祭坛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408940&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Duplicator<br>|Image=Event-Duplicator.png<br>}}<br>{{E|Duplicator}} is a shrine [[Event]] found in all [[Acts]].<br><br>Shrine events appear less frequently than normal events.<br><br>== Options ==<br>{{Frame|Pray}} {{TS|positive||Duplicate a card in your deck.}}<br><br>{{Frame|Leave}} Nothing happens.<br><br>== Dialogue ==<br><blockquote><div style="font-style:italic"><br>Before you lies a decorated altar to some ancient entity.<br></div><br><br>{{Frame|Pray}}<br><bl... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
