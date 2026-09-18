# 蜿蜒走廊 / Winding Halls

> 稳定 ID：`sts1.event.winding_halls`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：蜿蜒走廊
- English: Winding Halls

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 3"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Embrace Madness | {"text": "Lose X HP"} | {"text": "Receive 2 Madness. . * X is equal to 12.5% (18%) of the player's Max HP"} |
| 2 | Focus | {"text": "Become Cursed - Writhe"} | {"text": "Heal X HP. * X is equal to 25% (20%) of the player's Max HP"} |
| 3 | Retrace Your Steps | {"text": "Lose X Max HP"} | {"text": "* X is equal to 5% of the player's Max HP"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Embrace Madness", "text": "Receive 2 Madness. Lose X HP. * X is equal to 12.5% (18%) of the player's Max HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Focus", "text": "Become Cursed - Writhe. Heal X HP. * X is equal to 25% (20%) of the player's Max HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Retrace Your Steps", "text": "Lose X Max HP. * X is equal to 5% of the player's Max HP."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["As you slowly make your way up the twisting pathways, you constantly find yourself losing your way as the walls and ground seem to inexplicably shift before your eyes. NL NL The constant #p~whispering~ #p~voices~ in the back of your head aren't helping things either.", "Passing by a structure you are certain you have previously seen you start to question if you are going insane, or if the impossible geography of this place is starting to get to you. You need to change something, and soon. N... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你沿着弯曲的道路慢慢前进，却多次发现自己迷失了方向，仿佛墙壁和地面就在你的眼前突然移动了位置。 NL NL 更糟糕的是，你的脑中似乎还有许多声音在对你轻声低语。", "当你经过一个你十分确定之前见到过的建筑物时，你开始怀疑是自己疯了，还是这个地方违背常理的地形让你失去了理智。你需要立即做出一些改变。 NL NL 至少那些声音们是这么说的，他们怎么会骗人呢？", "你觉得自己的理智出现了裂痕，只有真正的疯子才能理解这样的地方，于是你拥抱了那些低语的声音，用“全新”的视角继续前进。 NL 现在一切似乎都变得合理了。", "你停下脚步，仔细地观察周围这片起伏波动的地貌。在混乱的变化中，你似乎逐渐找到了一些规律。可是那些令人疯狂的话语不停打断着你的思绪，你花了极大的努力才强忍着痛苦无视了他们。 NL NL 最终你成功地分析出了一条前进的道路，当你离开时，你觉得自己似乎对这个诡异地方的恶毒本质有了一定的抵抗力。", "你在迷宫中绕来绕去，仿佛经过了永恒，但你逐渐地找到了自己来时的路线。你重新稳住精神，从蜿蜒的走廊中逃离了出来。 NL NL 这让你觉得 #r~精疲力尽~ 。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["...", "[Embrace Madness] #gReceive #g2 Madness. #rLose #r", " #rHP.", "[Focus] #rBecome #rCursed #r- #rWrithe. #gHeal #g", "[Leave]", " #gHP.", "[Retrace Your Steps] #rLose #r", " #rMax #rHP."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["……", "[拥抱疯狂] #g获得2张 疯狂 #g。 #r失去 #r", " #r生命。", "[集中精神] #r被诅咒——苦恼。 #g获得 #g", "[离开]", " #g生命。", "[寻找来路] #r失去 #r", " #r点最大生命。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Winding Halls | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 蜿蜒走廊 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Winding Halls", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你沿着弯曲的道路慢慢前进，却多次发现自己迷失了方向，仿佛墙壁和地面就在你的眼前突然移动了位置。<br>更糟糕的是，你的脑中似乎还有许多声音在对你轻声低语。<br>...... 调出下一个界面。<br>下一个界面<br>当你经过一个你十分确定之前见到过的建筑物时，你开始怀疑是自己疯了，还是这个违背常理的地形让你失去了理智。你需<br>要立即做出一些改变。<br>至少那些声音们是这样说的，他们怎么会骗人呢？<br>选项<br>拥抱疯狂 得到 2 张疯狂。失去12.5%(A15+:18%)生命。你觉得自己的理智出现了裂痕，只有真正的疯子才能理解这个地方。于是你拥抱了那些低语的声音，用“全新”的视角继续前进。<br>这里的一切似乎变得更加合理了。<br>集中精神 被诅咒——苦恼。获得25%(A15+:20%)生命。你停下脚步，仔细观察这起伏波动的地貌。在混乱的变化中，你似乎逐渐找到了一些规律。可是那些令人疯狂的话语不停打断着你的思绪，你花了极大的努力才强忍着痛苦无视了他们。<br>最终你成功地分析出了一条前进的道路，当你离开时，你觉得自己似乎对这... | `single_source` | [蜿蜒走廊](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408924&wiki_id=646570) |
| `source.title_text` | 蜿蜒走廊 | `single_source` | [蜿蜒走廊](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408924&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Winding Halls<br>|Image=Event-WindingHalls.png<br>}} {{Small Card Infobox|Madness}} {{Small Card Infobox|Writhe}}<br>{{E|Winding Halls}} is an [[Event]] found exclusively in [[Act 3]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br><!-- Fix descriptions to be game accurate. Use TS template for colors. For percentages, replace with X and then in an indented bullet below, explain what X is equal to. --><br>{{Frame|Embrace Madness}} {{T... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
