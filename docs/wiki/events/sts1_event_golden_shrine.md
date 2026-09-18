# 金色神龛 / Golden Shrine

> 稳定 ID：`sts1.event.golden_shrine`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：金色神龛
- English: Golden Shrine

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Pray |  | {"text": "Gain 100 Gold."} |
| 2 | Desecrate | {"text": "Become Cursed - Regret; lose HP equal to the number of cards in your hand"} | {"text": "Gain 275 Gold. . * Regret - Unplayable. At the end of your turn,"} |
| 3 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Pray", "text": "Gain 100 Gold."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Desecrate", "text": "Gain 275 Gold. Become Cursed - Regret. * Regret - Unplayable. At the end of your turn, lose HP equal to the number of cards in your hand."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Before you lies an elaborate shrine to an ancient spirit. ", "As your hand touches the shrine, #ygold rains from the ceiling ~showering~ ~you~ ~in~ ~riches.~ ", "Each time you strike the shrine, #ygold pours forth again and again! NL NL As you pocket the riches, something #rweighs #rheavily #ron #ryou.", "You ignore the shrine."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在你面前是一座古老神灵的精巧神龛。", "当你的手触碰神龛时，天空中开始掉落 #y金币 ， ~赚钱了！~", "你每攻击一次神龛，就有更多的 #y金币 掉落出来！ NL NL 当你收起所有钱时，心中有了一种 #r沉重的感觉 。", "你无视了神龛。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Pray] #gGain #g", " #gGold.", "[Desecrate] #gGain #g275 #gGold. #rBecome #rCursed #r- #rRegret.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[祈祷] #g获得 #g", " #g金币。", "[亵渎] #g获得 #g275 #g金币。 #r被诅咒——悔恨。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Golden Shrine | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 金色神龛 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Golden Shrine", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在你面前是一座古老神灵的精巧神龛。<br>选项<br>祈祷 获得 100 金币。（进阶15:50金币）<br>当你的手触碰神龛时，天空中开始掉落金币，赚钱了！<br>亵渎 获得 250 金币。被诅咒——悔恨。你每攻击一次神龛，就有更多的金币掉落出来！当你收起所有钱时，心中有了一种沉重的感觉。<br>离开你无视了神龛。<br>注意<br>金神像无法增加此事件给予的金币数目。 | `single_source` | [金色神龛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408951&wiki_id=646570) |
| `source.title_text` | 金色神龛 | `single_source` | [金色神龛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408951&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Golden Shrine<br>|Image=Event-GoldenShrine.png<br>}} {{Small Card Infobox|Regret}}<br>{{E|Golden Shrine}} is a {{QueryLink|Events|shrine:Yes|shrine Event}} encountered in all [[Acts]].<br><br>== Options ==<br>{{Frame|Pray}} {{TS|positive||Gain 100 Gold.}}<br><br>{{Frame|Desecrate}} {{TS|positive||Gain 275 Gold.}} {{TS|negative||Become Cursed -}} {{C|Regret}}.<br>* {{C|Regret}} - {{KW|Unplayable}}. At the end of your turn, lose HP equal to the number of cards in your h... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
