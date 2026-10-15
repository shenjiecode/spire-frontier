# 巢穴 / The Nest

> 稳定 ID：`sts1.event.the_nest`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：巢穴
- English: The Nest

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Smash and Grab |  | {"text": "Obtain 99 (50) Gold."} |
| 2 | Stay in Line | {"text": "Lose 6 HP"} | {"text": "Obtain Ritual Dagger"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Smash and Grab", "text": "Obtain 99 (50) Gold."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Stay in Line", "text": "Obtain Ritual Dagger"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["A long line of #b~hooded~ #b~figures~ can be seen entering NL an #punassuming #pcathedral.", "Naturally, you join the line and are quickly surrounded by #rCultists! NL They ignore you as they gleefully @chant@ and ~wave~ their weapons around. NL NL #r@\"MURDER!!@ #r@MURDER@ #r@MURDER!!\"@ NL #b~\"CAW~ #b~CAW~ #b~CAAAAAWWW!\"~ NL #r@\"MURDER!@ #r@MURDER@ #r@MUURDER!!\"@ NL #b~\"CAAW~ #b~CAW~ #b~CAAAAAAWW!!\"~ NL NL You eye a #yDonation #yBox...", "You decide to stay in line (out of fear) to ... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你看见一长串 #b~戴着兜帽的人们~ 正鱼贯走进一座 #p看起来没什么特别的大教堂。", "于是你理所当然地加入了队伍里，很快你的周围就站满了 #r邪教徒 ！ NL 他们似乎没有发现你，只是兴奋地 ~挥舞着~ 自己的武器并喜悦地 @呼喊@ 着些什么。 NL NL #r@“杀！@ #r@杀～@ #r@杀杀杀！！”@ NL #b~“咔～~ #b~咔～~ #b~咔—咔！”~ NL #r@“杀！@ #r@杀～@ #r@杀杀杀！！”@ NL #b~“咔～~ #b~咔～~ #b~咔—咔！”~ NL NL 你看到前面有一个 #y捐款箱 ……", "你（可能是出于害怕）决定留在队列中，看看究竟会发生什么。 NL NL 最终你到达了队伍的最前，与教徒的领袖面对面。 一名身着华服的邪教徒交给你一把 #y华丽的匕首 。 你照着之前所有人的样子，用匕首在自己的手臂上划开了一道口子，让鲜血滴入了下方一个形状奇怪的碗。 NL NL 邪教徒们开始对你 @大喊@ @大叫@ ！ NL NL #b~“咔～~ #b~咔～~ #b~咔——咔！”~ NL NL 你也跟着喊了起来。为什么不呢？", "他们甚至完全没有注... | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Stay in Line] #gObtain Ritual Dagger. #rLose #r", " #rHP.", "[Smash and Grab] #gObtain #g", " #gGold.", "[Leave]", "[Continue]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[留在队伍中] #g获得 仪式匕首 #g。 #r失去 #r", " #r生命。", "[抢了钱就跑] #g获得 #g", " #g金币。", "[离开]", "[继续]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Nest | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 巢穴 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Nest", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你看到一长串戴着兜帽的人们正鱼贯走进一座看起来没什么特别的大教堂于是你理所当然地加入了队伍里，很快你的周围就站满了邪教徒！他们似乎没有发现你，只是兴奋地挥舞着自己的武器并喜悦地呼喊着些什么。“杀！杀~杀杀杀！！”“咔~咔~咔-咔！”“杀！杀~杀杀杀！！”“咔~咔~咔-咔！”你看到前面有一个捐款箱。<br>选项<br>抢了钱就跑 获得99金币（进阶15以上为50金币 ）<br>他们甚至完全没有注意到你的行动。<br>留在队伍中 获得仪式匕首，失去6生命。<br>你（可能是出于害怕），决定留在队列中，看看究竟会发生什么最终你到达了队伍的最前，与教徒的领袖面对面，一名身着华服的邪教徒交给你一把华丽的匕首。你照着之前所有人的样子，用匕首在自己手臂上划开了一道口子，让鲜血滴入了下方一个形状奇怪的碗邪教徒们开始对你大喊大叫！“咔~咔~咔-咔！”你也跟着喊了起来，为什么不呢？ | `single_source` | [巢穴](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389473&wiki_id=646570) |
| `source.title_text` | 巢穴 | `single_source` | [巢穴](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389473&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=The Nest<br>|Image=Event-TheNest.png<br>}} {{Small Card Infobox|Ritual Dagger}}<br>{{E|The Nest}} is an event found exclusively in [[Act 2]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Smash and Grab}} {{TS|positive||Obtain 99 {{Asc|15|(50)}} Gold.}}<br><br><br><br><br>{{Frame|Stay in Line}} {{TS|positive||Obtain {{C|Ritual Dagger}}.}} {{TS|negative||Lose 6 HP.}}<br><br>== Dialogue ==<br><blockquote><div style="font-style... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
