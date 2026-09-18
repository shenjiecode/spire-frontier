# 老乞丐 / Old Beggar

> 稳定 ID：`sts1.event.old_beggar`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：老乞丐
- English: Old Beggar

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Offer Gold |  | {"text": "75 Gold]: Remove a card from your deck."} |
| 2 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Offer Gold", "text": "75 Gold]: Remove a card from your deck."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["An old beggar cloaked in fur reaches his hands out towards you as you pass. \"Spare some coin, child?\"", "The beggar looks to the floor as you pass. NL \"You will never make a difference... You never do.\"", "The beggar takes off its cloak to reveal that he is #bCleric! NL @\"You@ @are@ @a@ @kind@ @soul.@ @Receive@ @my@ @purification!\"@ he screams. NL You are unsure if he is grateful or mad.", "@\"I@ @hope@ @you@ @do@ @better@ @this@ @time,@ @friend!\"@ he shouts. NL Wondering what was im... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["一个裹着毛衣的老乞丐在你经过时向你伸出了双手，他对你说：“施舍点钱吧，孩子？”", "乞丐在你经过时低头看着地板，喃喃自语： NL “你永远也成就不了什么事情的……永远不会。”", "乞丐突然脱下了外套，原来他是 #b牧师 ！ NL @“你真是个善良的人，接受我的净化吧！”@ 他大声叫起来。 NL 老实说你有点不知道他是在开心还是在生气。", "@“希望你这次能做得更好啊，朋友！”@ 他冲你喊着。 NL 你玩味着这句话中暗藏的意思，继续向前出发。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Offer Gold] #y", " #yGold: #gRemove #ga #gcard #gfrom #gyour #gdeck.", "[Locked] Requires: ", " Gold.", "[Continue]", "[Leave]", "Select a Card to Remove."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[给金币] #y", "  #y金币： #g从你的牌组中移除一张牌。", "[锁定] 需要： ", " 金币。", "[继续]", "[离开]", "选择一张牌移除。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Old Beggar | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 老乞丐 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Beggar", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | 至少有75金币时才会出现。（图片未提供文字说明）<br>描述<br>一个裹着毛衣的老乞丐在你经过时向你伸出了双手，他对你说：“施舍点钱吧，孩子？”<br>选项<br>给金币 失去75 金币：从你的牌组中移除一张牌。 需要：75 金币。乞丐突然脱下了外套，原来他是牧师！<br>“你真是个善良的人，接受我的净化吧！”他大声叫起来。老实说你有点不知道他是在开心还是在生气。<br>“希望你这次能做得更好啊，朋友！”他冲你喊着。你玩味着这句话中暗藏的意思，继续向前出发。<br>离开乞丐在你经过时低头看着地板，喃喃自语：“你永远也成就不了什么事情的……永远不会。”<br>轶事<br>“希望你这次能做得更好”可能暗指角色每次在攀爬尖塔失败后，都会被涅奥复活、清除记忆并送回塔底。 | `single_source` | [老乞丐](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408870&wiki_id=646570) |
| `source.title_text` | 老乞丐 | `single_source` | [老乞丐](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408870&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Old Beggar<br>|Image=Event-Beggar.png<br>}}<br>{{E|Old Beggar}} is an [[Event]] found exclusively in [[Act 2]]. It will only appear if the player has at least 75 [[Gold]].<br><br>== Options ==<br>{{Frame|Offer Gold}} {{TS|gold||75 [[Gold]]:}} {{TS|positive||Remove a card from your deck.}} <br><br><br><br><br>{{Frame|Leave}} Nothing happens.<br><br>== Dialogue ==<br><blockquote><div style="font-style:italic"><br>An old beggar cloaked in fur reaches his hands out toward... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
