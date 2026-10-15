# 长枪决斗 / The Joust

> 稳定 ID：`sts1.event.the_joust`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：长枪决斗
- English: The Joust

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2 - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Murderer |  | {"text": "Bet 50 Gold - 70%: win 100 Gold."} |
| 2 | Owner |  | {"text": "Bet 50 Gold - 30%: win 250 Gold. There is no option to avoid betting."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Murderer", "text": "Bet 50 Gold - 70%: win 100 Gold."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Owner", "text": "Bet 50 Gold - 30%: win 250 Gold. There is no option to avoid betting."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["As you make your way through the large buildings you come across a long narrow bridge and spot knights on either side, facing one another. You approach... NL @\"Halt!\"@ NL NL A knight forcefully gestures you to stop with its giant lance.", "\"Today is the day I must settle the score with the #rmurderer of my beloved pet, #yNoodles. Until then, you may not pass. NL NL Fellow witness, why don't you #bbet on who you think will emerge victorious?\"", "\"I can't believe you're betting against #... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你在巨大的建筑物间穿行时，遇见了一条长长的窄桥，两头似乎都有一名骑士彼此对望着。你走上前去…… NL @“停步！”@ NL NL 一名骑士用手中的长枪对你比划着，强硬地让你停下。", "“今天是我为我心爱的宠物 #y面条 报仇的日子，就是前面这个人谋杀了它！ 在我们的决斗结束之前，你不能经过这里。 NL NL 决斗的见证者啊，你为什么不 #b赌一赌 最后谁会获得胜利呢？”", "“真不敢相信，你竟然觉得 #y面条 的仇报不了！” NL NL 骑士愤怒地盖上自己的面具，向着前方的宿敌冲了过去。", "“ #y面条 啊，给我力量！” NL NL 骑士盖上了自己的面具，向前冲去。", "NL #y@*哐啷*！！@ #r@*铛！！*@ NL NL #g@*砰！！*@", "看来是杀宠凶手死了。 NL NL ", "看来是宠物主人死了。 NL NL ", "你 #g赌赢了 。虽然你还是搞不太清楚情况，但有得赚就好，你收下钱离开了这里。", "你 #r赌输了 。但至少被长枪捅穿的人不是你。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Continue]", "[Murderer] #yBet #y", " #yGold - #g70%: #gwin #g", " #gGold.", "[Owner] #yBet #y", " #yGold - #g30%: #gwin #g", "[Watch]", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[继续]", "[凶手] #y赌 #y", "  #y金币 —— #g70%: #g赢得 #g", " #g金币。", "[主人] #y赌 #y", "  #y金币 —— #g30%: #g赢得 #g", "[观战]", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Joust | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 长枪决斗 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "The Joust", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | 需要有至少 50 金币时才会出现<br>描述<br>你在巨大的建筑物间穿行时，遇见了一条长长的窄桥，两头似乎都有一名骑士彼此对望着。你走上前去……“停步！”一名骑士用手中的长枪对你比划着，强硬地让你停下。“今天是我为我心爱的宠物面条报仇的日子，就是前面这个人谋杀了它！ 在我们的决斗结束之前，你不能经过这里。决斗的见证者啊，你为什么不赌一赌最后谁会获得胜利呢？”<br>选项<br>凶手 赌 50 金币——70%：赢得 100 金币。“真不敢相信，你竟然觉得面条的仇报不了！”骑士愤怒地盖上自己的面具，向着前方的宿敌冲了过去。*哐啷*！！ *铛！！**砰！！*结果 1：看来是杀宠凶手死了。<br>你赌输了。但至少被长枪捅穿的人不是你。结果 2：看来是宠物主人死了。你赌赢了。虽然你还是搞不太清楚情况，但有得赚就好，你收下钱离开了这里。<br>主人 赌 50 金币——30%：赢得 250 金币。“面条啊，给我力量！”骑士盖上了自己的面具，向前冲去。*哐啷*！！ *铛！！**砰！！*结果 1：看来是杀宠凶手死了。<br>你赌赢了。虽然你还是搞不太清楚情况，但有得赚就好，你收下钱离开了这里。结... | `single_source` | [长枪决斗](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408890&wiki_id=646570) |
| `source.title_text` | 长枪决斗 | `single_source` | [长枪决斗](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408890&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=The Joust<br>|Image=Event-Joust.png<br>}}<br>{{E|The Joust}} is a shrine [[Event]] found in [[Act 2]]. This event can only be encountered with more than 50 [[Gold]].<br><br>== Options ==<br>{{Frame|Murderer}} {{TS|gold||Bet 50 Gold}} - {{TS|positive||70%: win 100 Gold.}}<br><br>{{Frame|Owner}} {{TS|gold||Bet 50 Gold}} - {{TS|positive||30%: win 250 Gold.}}<br><br>There is no option to avoid betting.<br><br>== Dialogue ==<br><blockquote><div style="font-style:italic"><b... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
