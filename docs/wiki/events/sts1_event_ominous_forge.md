# 邪恶熔炉 / Ominous Forge

> 稳定 ID：`sts1.event.ominous_forge`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：邪恶熔炉
- English: Ominous Forge

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Forge |  | {"text": "Upgrade a card in your deck."} |
| 2 | Rummage | {"text": "Become Cursed - Pain; lose 1 HP whenever you play another card"} | {"text": "Obtain a special relic. . * Warped Tongs - At the start of your turn, Upgrade a random card in your hand for the rest of combat. * Pain - Unplayable. While in hand,"} |
| 3 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Forge", "text": "Upgrade a card in your deck."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Rummage", "text": "Obtain a special relic. . * Warped Tongs - At the start of your turn, Upgrade a random card in your hand for the rest of combat. * Pain - Unplayable. While in hand,"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You duck into a small hut. Inside, you find what appears to be a forge. The smithing tools are covered with dust, yet a fire roars inside the furnace. You feel on edge...", "You decide to put the forge to use and... NL #y@CLANG@ #y@CLAAANG@ #y@CLANG!@ NL ...improve your arsenal!", "You decide to see if you can find anything of use. After uncovering tarps, looking through boxes, and checking nooks and crannies, you find a dust covered #y~relic!~ ", "As you go through the finishing touches, t... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你钻进一个小屋，在里面似乎有一个锻造熔炉，旁边的铁匠工具都已经布满了灰尘，可是炉中的火却仍然熊熊燃烧。你觉得有些不安……", "你决定好好利用这个熔炉…… NL #y@铛@ #y@铛@ #y@铛！@ NL ……来强化你的卡牌！", "你决定看看能不能找到什么其他有用的东西。在掀开不少盖布、翻开不少箱子和在角落四处搜寻之后，你找到了一个满是灰尘的 #y~遗物~ ！", "在锻造快要完成的时候，熔炉中的火焰突然蹿到了你的手臂上， #r@烧伤@ 了你……", " NL NL 拿走遗物离开时，你突然感觉到一阵挥之不去的 #r~剧烈疼痛~ ，或许是你的行为惊动了什么恶灵？", "看来没什么能用上的东西，你从来路退了出去。熔炉中的火焰在墙上投射下了 #p~诡异的影子~ ……"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Forge] #gUpgrade #ga #gcard #gin #gyour #gdeck.", "[Rummage] #gObtain #ga #gspecial #gRelic. #rBecome #rCursed #r- #rPain.", "[Leave]", "Choose a Card to Upgrade", "[Locked] Requires: Upgradeable Cards"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[锻造] #g升级你牌组中的一张牌。", "[翻查] #g获得一件特别遗物。 #r被诅咒——疼痛。", "[离开]", "选择一张牌升级", "[锁定] 需要： 可以升级的牌"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Ominous Forge | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 邪恶熔炉 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Accursed Blacksmith", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你钻进一个小屋，在里面似乎有一个锻造熔炉，旁边的铁匠工具都已经布满了灰尘，可是炉中的火却仍然熊熊燃烧。你觉得有些不安……<br>选项<br>锻造 升级一张牌。] 需要：可以升级的牌你决定好好利用这个熔炉……铛 铛 铛！……来强化你的卡牌!<br>翻查 获得一件特别的遗物：弯曲铁钳。被诅咒——疼痛。你决定看看能不能找到什么其他有用的东西。在掀开不少盖布、翻开不少箱子和在角落四处搜寻之后，你找到了一个满是灰尘的遗物！在你离开小屋时，你感觉到了一阵挥之不去的疼痛，或许是你的行为惊扰了什么恶灵？<br>离开看来没什么能用上的东西，你从来路退了出去。熔炉中的火焰在墙上投射下了诡异的影子……<br>策略<br>该事件最通常的选项为“锻造”，此选项除了获得不到遗物弯曲铁钳以外，没有任何的副作用与代价。<br>如果玩家能够抵御诅咒，亦或是前方不远处即为商店且金币足够，并且身上并没有亟待升级的牌，那么弯曲铁钳或许是个好选择。同时，灼热攻击受到该遗物的增益很大，同时疼痛和撕裂也会产生强大的协同作用。 | `single_source` | [邪恶熔炉](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408942&wiki_id=646570) |
| `source.title_text` | 邪恶熔炉 | `single_source` | [邪恶熔炉](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408942&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Ominous Forge<br>|Image=Event-OminousForge.png<br>}} {{Small Relic Infobox|Warped Tongs}} {{Small Card Infobox|Pain}}<br>{{E|Ominous Forge}} is a shrine [[Event]] encountered in all [[Acts]].<br><br>== Options ==<br>{{Frame|Forge}} {{TS|positive||Upgrade a card in your deck.}}<br><br><br><br>{{Frame|Rummage}} {{TS|positive||Obtain a special relic.}} {{TS|negative||Become Cursed -}} {{C|Pain}}.<br>* {{R|Warped Tongs}} - At the start of your turn, {{KW|Upgrade}} a rando... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
