# 秘密传送门 / Secret Portal

> 稳定 ID：`sts1.event.secret_portal`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：秘密传送门
- English: Secret Portal

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 3 - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Enter the Portal |  | {"text": "IMMEDIATELY travel to the boss]. * The player is put directly into combat with the Act 3 boss] at the end of the act."} |
| 2 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Enter the Portal", "text": "IMMEDIATELY travel to the boss]. * The player is put directly into combat with the Act 3 boss] at the end of the act."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Before you is a sight that seems out of place in the alien landscape around you. Strangely placed into one of the living walls of the Beyond is an enclosed stone entrance filled with a #p~swirling~ #p~magical~ #p~portal.~ NL NL You aren't sure where it leads, but maybe it could speed your journey through the Spire.", "Jumping through the portal, your sense of time and space is completely torn apart. NL NL As you reorient yourself to the new surroundings, you realize that right before you is... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在你面前有一样与周围奇异景观完全不符合的东西：在深处地区一面活墙壁上，奇怪地出现了一道石做的拱门，里面有一个 #p~旋转的魔法传送门~ 。 NL NL 你不知道它会通向哪里，但它应该能够节约你爬塔的时间。", "你跳进了传送门，瞬间失去了一切对时间与空间的感知。 NL NL 当你好不容易镇定下来时，你发现自己到达了一个新的地方，而前方正有一场苦战在等待着你。", "你觉得小心谨慎才是在这座高塔的登顶之道。你无视了传送门，继续上路。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Enter the Portal] IMMEDIATELY travel to the boss.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[进入传送门] 立即传送到Boss房间。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Secret Portal | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 秘密传送门 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SecretPortal", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在你面前有一样与周围奇异景观完全不符合的东西：在深处地区一面活墙壁上，奇怪地出现了一道石做的拱门，里面有一个旋转的魔法传送门你不知道它会通向哪里，但他应该能够节约你爬塔的时间。<br>选项<br>进入传送门 立即传送到BOSS房间<br>你跳进了传送门，瞬间失去了一切对时间与空间的感知。当你好不容易镇定下来，你发现自己到达了一个新的地方，而前方正有一场苦战等待着你。<br>离开<br>你觉得小心谨慎才是这座高塔的登顶之道。你无视了传送门，继续上路。 | `single_source` | [秘密传送门](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408908&wiki_id=646570) |
| `source.title_text` | 秘密传送门 | `single_source` | [秘密传送门](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408908&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Secret Portal<br>|Image=Event-SecretPortal.png<br>}}<br>{{E|Secret Portal}} is a shrine [[Event]] found in [[Act 3]]. It will only appear if 800 seconds (13 minutes and 20 seconds) have passed.<br><br>== Options ==<br>{{Frame|Enter the Portal}} IMMEDIATELY travel to [[Bosses#Act 3 Bosses|the boss]].<br>* The player is put directly into combat with the [[Bosses#Act 3 Bosses|Act 3 boss]] at the end of the act.<br><br><br>{{Frame|Leave}} Nothing happens.<br><br>== Dialog... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
