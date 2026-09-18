# 恩洛斯 / N'loth

> 稳定 ID：`sts1.event.n_loth`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：恩洛斯
- English: N'loth

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2 - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Offer: Relic A | {"text": "Lose this relic"} | {"text": "Obtain a special relic"} |
| 2 | Offer: Relic B | {"text": "Lose this relic"} | {"text": "Obtain a special relic. * Rewards the player with N'loth's Gift"} |
| 3 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Offer: Relic A", "text": "Obtain a special relic"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Offer: Relic B", "text": "Obtain a special relic. * Rewards the player with N'loth's Gift"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["An odd creature with a hunched back sprouting several tentacles is scrounging through a pile of trash and debris in front of you. As you approach, he shuffles towards you in a non-threatening manner. NL \"N'loth hungry. Feed N'loth.\"", "Holding the #yrelic out towards him, N’loth snatches it out of your hand with his tentacles, dislocates his jaw, and slurps down your offer in one quick gulp. NL He gives you a large, toothy grin as more tentacles appear from behind his cloak, these ones br... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["一个驼着背、背后长出几条触手的奇怪生物正在你面前的垃圾堆和废墟里来回地翻找些什么。当你靠近时，他可怜巴巴地拖着脚走到了你面前。 NL “恩洛斯好饿，喂喂恩洛斯。”", "你把 #y遗物 递给恩洛斯，他用触手一把将东西抓过去，大张开嘴，一口就啊呜吞了下去。 NL 他露齿一笑，斗篷后面似乎出现了更多触手，簇拥着拿出了一个看起来非常整洁的小盒子。他把盒子硬是塞给了你。", "你摇摇头，恩洛斯的背驼得更深了，他叹了口气，灰溜溜地跑了。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Offer: ", "] #rLose #rthis #rrelic. #gObtain #ga #gspecial #grelic.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[交出： ", "] #r失去这件遗物。 #g获得一件特别的遗物。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | N'loth | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 恩洛斯 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "N'loth", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>一个驼着背、背后长出几条触手的奇怪生物正在你面前的垃圾堆和废墟里来回地翻找些什么。当你靠近时，他可怜巴巴地拖着脚走到了你面前。“恩洛斯好饿，喂喂恩洛斯。<br>选项<br>[交出：某件遗物] 失去这件遗物。获得一件特别的遗物。你把遗物递给恩洛斯，他用触手一把将东西抓过去，大张开嘴，一口就啊呜吞了下去。他露齿一笑，斗篷后面似乎出现了更多触手，簇拥着拿出了一个看起来非常整洁的小盒子。他把盒子硬是塞给了你。<br>可能索要任何类型遗物；交出「获得时生效的遗物」（如药水腰带） 不会使其效果消失<br>[交出：另一件遗物] 失去这件遗物。获得一件特别的遗物。同上<br>离开<br>你摇摇头，恩洛斯的背驼得更深了，他叹了口气，灰溜溜地跑了。 | `single_source` | [恩洛斯](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389480&wiki_id=646570) |
| `source.title_text` | 恩洛斯 | `single_source` | [恩洛斯](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389480&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=N'loth<br>|Image=Event-Nloth.png<br>}} {{Small Relic Infobox|N'loth's Gift}}<br>{{E|N'loth}} is a {{QueryLink|Events|shrine:Yes|shrine Event}} found exclusively in [[Act 2]]. It will only appear if the player has at least 2 [[Relics]]. This Event is the only way to obtain {{R|N'loth's Gift}}.<br><br>== Options ==<br>'''Note:''' "Relic A" and "Relic B" will be randomly chosen from the player's currently held [[Relics]].<br><br><br><br>{{Frame|Offer: Relic A}} {{TS|nega... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
