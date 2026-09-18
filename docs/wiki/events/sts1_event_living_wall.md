# 活墙壁 / Living Wall

> 稳定 ID：`sts1.event.living_wall`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：活墙壁
- English: Living Wall

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Forget |  | {"text": "Remove a card from your deck."} |
| 2 | Change |  | {"text": "Transform] a card in your deck."} |
| 3 | Grow |  | {"text": "Upgrade] a card in your deck."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Forget", "text": "Remove a card from your deck."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Change", "text": "Transform] a card in your deck."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Grow", "text": "Upgrade] a card in your deck."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["As you come to a dead-end and begin to turn around, walls @slam@ @down@ from the ceiling, trapping you! NL NL Three faces materialize from the walls and speak. NL #b\"Forget #bwhat #byou #bknow, #band #bI'll #blet #byou #bgo.\" NL #p\"I #prequire #pchange #pto #psee #pa #pnew #pspace.\" NL #y\"If #yyou #ywant #yto #ypass #yme, #ythen #yyou #ymust #ygrow.\"", "Satisfied, the walls in front of you merge back into the ceiling, leaving a path forward."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你走进一条死路，正准备要回头时，四周突然有墙壁从天花板上 @哐@ 地一下 @砸了下来@ ！ NL NL 三张脸出现在墙壁上，开始对你说话： NL #b“忘记你所知道的，我就让你走。” NL #p“有所改变，我就让你看见新的道路。” NL #y“如果你想要从我这里通过，你就必须有所成长。”", "你面前的墙壁满意地缩回了天花板，你的眼前出现了道路。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Forget] #gRemove #ga #gcard #gfrom #gyour #gdeck.", "[Change] #gTransform #ga #gcard #gin #gyour #gdeck.", "[Grow] #gUpgrade #ga #gcard #gin #gyour #gdeck.", "Select a Card to Remove.", "Choose a Card to Transform.", "Choose a Card to Upgrade.", "[Leave]", "[Locked] Requires: Upgradeable Cards"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[遗忘] #g移除你牌组中的一张牌。", "[改变] #g变化你牌组中的一张牌。", "[成长] #g升级你牌组中的一张牌。", "选择一张牌移除。", "选择一张牌变化。", "选择一张牌升级。", "[离开]", "[锁定] 需要： 可以升级的牌"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Living Wall | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 活墙壁 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Living Wall", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你走进一条死路，正准备要回头时，四周突然有墙壁从天花板上哐地一下砸了下来！三张脸出现在墙壁上，开始对你说话：“忘记你所知道的，我就让你走。”“有所改变，我就让你看见新的道路。”“如果你想要从我这里通过，你就必须有所成长。”<br>选项<br>遗忘 移除你牌组中的一张牌。你面前的墙壁满意地缩回了天花板，你的眼前出现了道路。<br>改变 变化你牌组中的一张牌。你面前的墙壁满意地缩回了天花板，你的眼前出现了道路。<br>成长 升级你牌组中的一张牌。 需要：可以升级的牌<br>你面前的墙壁满意地缩回了天花板，你的眼前出现了道路。 | `single_source` | [活墙壁](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375288&wiki_id=646570) |
| `source.title_text` | 活墙壁 | `single_source` | [活墙壁](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375288&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Living Wall<br>|Image=Event-LivingWall.png<br>}}<br>{{E|Living Wall}} is an [[Event]] found exclusively in [[Act 1]]. <br><br>== Options ==<br>{{Frame|Forget}} {{TS|positive||Remove a card from your deck.}}<br><br><br><br><br>{{Frame|Change}} {{TS|positive||[[Transform]] a card in your deck.}}<br><br><br><br><br>{{Frame|Grow}} {{TS|positive||[[Upgrade]] a card in your deck.}}<br><br>== Dialogue ==<br><blockquote><br><i><br>As you come to a dead-end and begin to turn a... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
