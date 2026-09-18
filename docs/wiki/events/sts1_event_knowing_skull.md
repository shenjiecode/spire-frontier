# 全知头骨 / Knowing Skull

> 稳定 ID：`sts1.event.knowing_skull`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：全知头骨
- English: Knowing Skull

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2 - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | A Pick Me Up? | {"text": "Lose X HP; lose HP and this option's HP loss is still increased by 1 even though no potion is obtained"} | {"text": "Get a Potion]. . * A random Potion] is immediately added to the player's left-most empty potion slot. * The player is able to select this option even if all their potion slots are full or if they possess Sozu. They still"} |
| 2 | Riches? | {"text": "Lose X HP"} | {"text": "Gain 90 Gold]"} |
| 3 | Success? | {"text": "Lose X HP"} | {"text": "Get a Colorless card. . * A random Uncommon Colorless card is added to the player's deck"} |
| 4 | How do I leave? | {"text": "Lose X HP"} | {"text": "* This event repeats until this option is chosen"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "A Pick Me Up?", "text": "Get a Potion]. Lose X HP. * A random Potion] is immediately added to the player's left-most empty potion slot. * The player is able to select this option even if all their potion slots are full or if they possess Sozu. They still lose HP and this option's HP loss is still increased by 1 even though no potion is obtained."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Riches?", "text": "Gain 90 Gold]. Lose X HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Success?", "text": "Get a Colorless card. Lose X HP. * A random Uncommon Colorless card is added to the player's deck."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "How do I leave?", "text": "Lose X HP. * This event repeats until this option is chosen."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You find yourself in an old, decorated chamber. In the center of the room, a large skull sits atop an ornate pedestal. As you approach, the skull #g@bursts@ #g@into@ #g@flames@ and turns to face you.", "\"WHAT IS IT YOU SEEK? WHAT IS IT YOU OFFER?\" NL In sync with its final words, the door behind you @slams@ @shut.@", " NL NL \"ANYTHING ELSE?\"", " ", "\"DRINK UP!\" NL You obtain a potion.", "\"PERHAPS THIS WILL HELP?\" NL You obtain a card.", "\"YOU MORTALS NEVER CHANGE. IT IS DONE.\" NL ... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你发现自己在一个古老的有装饰的房间里，在房间正中央，有一个巨大的头骨被放在精致的高台上，在你靠近时，头骨 #g@迸发出火焰@ 转向了你。", "“你想寻找什么？你会献出什么？” NL 它的话音刚落，你背后的门就 @砰地关上了@ 。", " NL NL “还有没有别的” ", " ", "“喝了吧！” NL 你获得一瓶药水。", "“说不定这个能行？” NL 你获得一张牌。", "“你们这些人类真是从来都不会变。愿望达成了。” NL #y金币 开始从上空不断落下！", "“看你背后，人类。” NL 你回头一瞥，果然，有一扇门在哪里。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Continue]", " #rHP.", "[Information?] #gReveal #gthe #gBoss. #rLose #r", "[Success?] #gGet #ga #gColorless #gCard. #rLose #r", "[A Pick Me Up?] #gGet #ga #gPotion. #rLose #r", "[Riches?] #gGain #g", " #gGold. #rLose #r", "[How do I leave?] #rLose #r", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[继续]", " #r生命。", "[信息？] #g告知 #gBoss #g身份。 #r失去 #r", "[成功？] #g获得一张无色牌。 #r失去 #r", "[来点喝的？] #g获得一瓶药水。 #r失去 #r", "[财富？] #g获得 #g", " #g金币。 #r失去 #r", "[我要怎么离开？] #r失去 #r", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Knowing Skull | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 全知头骨 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Knowing Skull", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | 需要剩余生命高于 12 时才会出现<br>描述<br>你发现自己在一个古老的有装饰的房间里，在房间正中央，有一个巨大的头骨被放在精致的高台上，在你靠近时，头骨迸发出火焰转向了你。“你想寻找什么？你会献出什么？”它的话音刚落，你背后的门就砰地关上了。<br>选项<br>来点喝的？ 得到一瓶药水。失去 （6+选择该选项次数） 生命。“喝了吧！”你得到一瓶药水。“还有没有别的”<br>财富？ 获得 90 金币。失去 （6+选择该选项次数） 生命。“你们这些人类真是从来都不会变。愿望达成了。”“还有没有别的”金币开始从上空不断落下！<br>成功？ 得到一张无色牌。失去 （6+选择该选项次数） 生命。“说不定这个能行？”你得到一张牌。“还有没有别的”<br>注：无色牌珍稀度为罕见。<br>我要怎么离开？ 失去 6 生命。“看你背后，人类。”你回头一瞥，果然，有一扇门在哪里。 | `single_source` | [全知头骨](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408883&wiki_id=646570) |
| `source.title_text` | 全知头骨 | `single_source` | [全知头骨](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408883&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Knowing Skull<br>|Image=Event-KnowingSkull.png<br>}}<br>{{E|Knowing Skull}} is a {{QueryLink|Events|shrine:Yes|shrine Event}} found exclusively in [[Act 2]]. It will only appear if the player has at least 13 HP; guaranteeing they can select at least 1 option and leave the event without dying.<br><br>== Options ==<br>The following options are presented to the player until they decide to leave the event. X is equal to 10% of the player's Max HP (minimum of 6 HP) plus th... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
