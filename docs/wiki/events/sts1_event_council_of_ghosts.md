# 幽灵会议 / Council of Ghosts

> 稳定 ID：`sts1.event.council_of_ghosts`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：幽灵会议
- English: Council of Ghosts

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Accept | {"text": "Lose X Max HP"} | {"text": "Receive 5 (3) Apparitions. . * X is equal to 50% of the player's Max HP, rounded up"} |
| 2 | Refuse |  | {"text": "Nothing happens. You are then given the option to"} |
| 3 | Leave |  | {"text": "."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Accept", "text": "Receive 5 (3) Apparitions. Lose X Max HP. * X is equal to 50% of the player's Max HP, rounded up."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Refuse", "text": "Nothing happens. You are then given the option to"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["As you continue your ascent, #p~thick~ #p~black~ #p~smoke~ begins to billow out of the ground and walls around you, coalescing into three masked forms that start to speak. NL NL ~\"Another~ ~puppet~ ~of~ #y~Neow~ ~I~ ~think.\"~ NL #r@\"AGREED!@ #r@SHE@ #r@ALWAYS@ #r@MAKES@ #r@THE@ #r@FUNNEST@ #r@TOYS!\"@ NL NL You notice an over-sized grin as the third addresses you. NL \"Ignore the others... Would you like a taste of our #y~power?\"~ ", "", "#y\"Excellent!\" NL As the ghostly shape speaks,... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在你向上攀升时，突然四周的墙壁和地面开始冒出 #p~浓重的黑烟~ ，逐渐聚成了三个戴着面具的形状，它们交头接耳地说起话来。 ~“看来这又是一个~ #y~涅奥~ ~的玩偶。”~ NL #r@“我看也是！@ #r@她总能做出最有趣的玩具！”@ NL NL 你注意到第三个存在有着巨大的嘴，它露出了一个大到夸张的微笑对你说： NL “别管那两个家伙……总之，你想不想尝试一下我们的 #y~力量~ 呢？” ", "", "#y“好极了！” NL 那个幽灵鬼影的话音刚落，你就看见它本已硕大的嘴张开得越来越大，从中涌出更多 #p~浓重的黑烟~ 笼罩了整个房间。你什么也看不见，也无法呼吸…… NL NL 就在你快要失去意识的时候，烟雾的感觉突然消失了。 NL NL 不管那三个东西是什么存在，它们现在已经不在了。你重新上路，但总觉得自己的内心变得有些 #b空洞 。", "“真令人失望……” NL ~“反正你迟早会成为我们的一员。”~  NL #r@“哈哈@ #r@哈哈哈哈！”@ NL NL 那些幽影消散了，只留下这令人不安的大笑声在你耳中回荡。", ""] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Accept] #gReceive #g5 Apparition. #rLose #r", " #rMax #rHP.", "[Refuse]", "[Accept] #gReceive #g3 Apparition. #rLose #r", "", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[接受] #g获得5张 灵体 #g牌。 #r失去 #r", " #r最大生命。", "[拒绝]", "[接受] #g获得3张 灵体 #g牌。 #r失去 #r", "", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Council of Ghosts | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 幽灵议会 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Ghosts", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在你向上攀升时，突然四周的墙壁和地面开始出浓重的黑烟，逐渐聚成了三个戴着面具的形状，它们交头接耳地说起话来。“看来这又是一个涅奥的玩偶。”“我看也是!她总能做出最有趣的玩具!”你注意到第三个存在有着巨大的嘴，它露出了一个大到夸张的微笑对你说:“别管那两个家伙....总之你想不想尝试一下我们的力量呢?”<br>选项<br>接受 获得5张灵体牌（进阶15+:3张）。失去50%的最大生命值。<br>“好极了!”那个幽灵鬼影的话音刚落，你就看见它本已硕大的嘛张开得越来越大，从中涌出更多浓重的黑烟笼罩了整个房间。你什么也看不见，也无法呼吸.....就在你快要失去意识的时候，烟雾的感觉突然消失了。不管那三个东西是什么存在，它们现在已经不在了。你重新上路，但总觉得自己的内心变得有些空洞。<br>拒绝 (无实质影响)。<br>“真令人失望....”“反正你迟早会成为我们的一员。”“哈哈哈哈哈哈!”那些幽影消散了，只留下这令人不安的大笑声在你耳中回荡。<br>轶事<br>此事件中出现的幽灵可能是先前被涅奥派出的冒险者死去后的灵魂（从它们称角色为“涅奥的玩偶... | `single_source` | [幽灵会议](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408902&wiki_id=646570) |
| `source.title_text` | 幽灵会议 | `single_source` | [幽灵会议](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408902&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Council of Ghosts<br>|Image=Event-Ghosts.png<br>}} {{Small Card Infobox|Apparition}}<br>{{E|Council of Ghosts}} is an event found exclusively in [[Act 2]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Accept}} {{TS|positive||Receive 5}} {{Asc|15|(3)}} {{C|Apparition|Apparitions}}. {{TS|negative||Lose X Max HP.}}<br>* X is equal to 50% of the player's Max HP, rounded up.<br><br>{{Frame|Refuse}} Nothing happens.<br><br><br><b... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
