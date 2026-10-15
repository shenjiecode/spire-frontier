# 神秘圆球 / Mysterious Sphere

> 稳定 ID：`sts1.event.mysterious_sphere`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：神秘圆球
- English: Mysterious Sphere

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 3"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Open Sphere |  | {"text": "Fight. Reward: Rare Relic]. * The player enters combat with the 2 Orb Walkers. In addition to the Rare Relic], the combat rewards also yield 45-55 Gold], a normal card reward, and potentially a Potion] just like a normal combat."} |
| 2 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Open Sphere", "text": "Fight. Reward: Rare Relic]. * The player enters combat with the 2 Orb Walkers. In addition to the Rare Relic], the combat rewards also yield 45-55 Gold], a normal card reward, and potentially a Potion] just like a normal combat."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Jutting from the chaotic terrain around you, a bony sphere surrounds a mysterious glowing object within. NL While you are curious what lies inside, you notice some sentries keeping an eye on it.", "As soon as you strike the sphere, the sentries spring to life around you!", "No need to be greedy."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在四周混乱的地形中间，一个骨质圆球伫立在地上，似乎包裹着一样神秘的发光物体。 NL 你很好奇里面有什么东西，但你注意到圆球周围有一些哨兵正在看守。", "你刚一砸开圆球，那些看守就立即动了起来！", "做人不能太贪。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Open Sphere] #rFight. #gReward: #gRare #gRelic.", "[Leave]", "[Fight]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[打开圆球] #r战斗。 #g奖励：稀有遗物。", "[离开]", "[战斗]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Mysterious Sphere | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 神秘圆球 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Mysterious Sphere", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在四周混乱的地形中间，一个骨质圆球伫立在地上，似乎包裹着一样神秘的发光物体。你很好奇里面有什么东西，但你注意到圆球周围有一些哨兵正在看守。<br>选项<br>打开圆球 战斗。奖励：稀有遗物。你刚一砸开圆球，那些看守就立即动了起来！<br>离开<br>做人不能太贪。 | `single_source` | [神秘圆球](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408919&wiki_id=646570) |
| `source.title_text` | 神秘圆球 | `single_source` | [神秘圆球](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408919&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Mysterious Sphere<br>|Image=Event-Sphere.png<br>}}<br>{{E|Mysterious Sphere}} is an [[Event]] found exclusively in [[Act 3]].<br><br>== Options ==<br>{{Frame|Open Sphere}} {{TS|negative||Fight.}} {{TS|positive||Reward: }} {{QueryLink|Relics|rarity:Rare|Rare}} {{TS|positive||[[Relic]].}}<br>* The player enters combat with the 2 {{M|Orb Walker|Orb Walkers}}. In addition to the {{QueryLink|Relics|rarity:Rare|Rare}} [[Relic]], the combat rewards also yield 45-55 [[Gold]],... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
