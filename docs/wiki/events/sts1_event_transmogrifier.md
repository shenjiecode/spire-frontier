# 转化神龛 / Transmogrifier

> 稳定 ID：`sts1.event.transmogrifier`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：转化神龛
- English: Transmogrifier

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Pray |  | {"text": "Transform a card. * Read more on Transform rules here]."} |
| 2 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Pray", "text": "Transform a card. * Read more on Transform rules here]."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Before you lies an elaborate shrine to a forgotten spirit.", "As the power of the shrine flows through you, your mind feels altered.", "You ignore the shrine."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在你面前是一个被遗忘神灵的精致神龛。", "神龛的力量涌入你，你感觉自己的内心发生了一些变化。", "你无视了神龛。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Pray] #gTransform #ga #gcard.", "[Leave]", "Select a Card to Transform."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[祈祷] #g变化一张牌。", "[离开]", "选择一张牌变化。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Transmogrifier | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 转化神龛 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Transmorgrifier", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在你面前是一个被遗忘神灵的精致神龛。<br>选项<br>祈祷 变化一张牌。神龛的力量涌入你，你感觉自己的内心发生了一些变化。<br>离开你无视了神龛。<br>轶事<br>该事件参考了卡尔文与霍布斯虎系列(Calvin in the series Calvin and Hobbes)中卡尔文用纸箱所制造机器，该机器可以把使用者变成任何所需的生物或物体。 | `single_source` | [转化神龛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408959&wiki_id=646570) |
| `source.title_text` | 转化神龛 | `single_source` | [转化神龛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408959&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Transmogrifier<br>|Image=Event-Transmogrifier.png<br>}}<br>{{E|Transmogrifier}} is a shrine [[Event]] encountered in all [[Acts]].<br><br>Shrine events appear less frequently than other events.<br><br>== Options ==<br>{{Frame|Pray}} {{KW|Transform}} {{TS|positive||a card.}}<br>* Read more on Transform rules [[Transform#Rules|here]].<br><br>{{Frame|Leave}} Nothing happens.<br><br>== Dialogue ==<br><blockquote><div style="font-style:italic"><br>Before you lies an elabor... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
