# 神圣泉水 / The Divine Fountain

> 稳定 ID：`sts1.event.the_divine_fountain`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：神圣泉水
- English: The Divine Fountain

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Drink |  | {"text": "Remove all Curses from your deck."} |
| 2 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Drink", "text": "Remove all Curses from your deck."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You come across #b~shimmering~ #b~water~ flowing endlessly from a fountain on a nearby wall.", "As you drink the #b~water,~ you feel a #pdark #pgrasp loosen.", "Unsure of the nature of this water, you continue on your way, parched."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你经过墙壁上的一处饮水池，里面流淌着源源不断 #b~闪着光的水~ 。", "你喝下 #b~水~ 后，感觉到身体中不再有 #p黑暗的束缚 。", "你仍然不知道这水从何而来，但解渴之后，你重新踏上了旅程。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Drink] #gRemove #gall #gCurses #gfrom #gyour #gdeck.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[喝水] #g移除所有诅咒牌。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Divine Fountain | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 神圣泉水 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Fountain of Cleansing", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你经过墙壁上的一处饮水池，里面流淌着源源不断闪着光的水。<br>选项<br>喝水 移除所有诅咒牌。喝下水后，感觉到身体中不再有黑暗的束缚。<br>离开你仍然不知道这水从何而来，但解渴之后，你重新踏上了旅程。<br>注意<br>该事件仅能在玩家目前牌组中至少含有一张诅咒才能遇到（不可移除的诅咒除外）。 | `single_source` | [神圣泉水](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408932&wiki_id=646570) |
| `source.title_text` | 神圣泉水 | `single_source` | [神圣泉水](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408932&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Divine Fountain<br>|Image=Event-DivineFountain.png<br>}}<br>{{E|The Divine Fountain}} is a shrine [[Event]] found in all [[Acts]]. This event can only appear if you have a {{QueryLink|Cards|type:Curse|Curse}} in your deck.<br><br>Shrine events appear less frequently than other events.<br><br>== Options ==<br>{{Frame|Drink}} {{TS|positive||Remove all}} {{QueryLink|Cards|type:Curse|Curses}} {{TS|positive||from your deck.}}<br><br>{{Frame|Leave}} Nothing happens.<br><br>... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
