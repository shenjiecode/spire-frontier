# 蓝衣女子 / The Woman in Blue

> 稳定 ID：`sts1.event.the_woman_in_blue`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：蓝衣女子
- English: The Woman in Blue

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Buy 1 Potion |  | {"text": "20 Gold."} |
| 2 | Buy 2 Potions |  | {"text": "30 Gold."} |
| 3 | Buy 3 Potions |  | {"text": "40 Gold."} |
| 4 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Buy 1 Potion", "text": "20 Gold."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Buy 2 Potions", "text": "30 Gold."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Buy 3 Potions", "text": "40 Gold."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["From the darkness, an arm pulls you into a small shop. As your eyes adjust, you see a pale woman in sharp clothes gesturing towards a wall of potions. NL \"Buy a potion. Now!\" she states.", "\"Good. Now leave.\" NL You exit the shop cautiously.", "#r@WHAM@ NL Her gloved fist collides with your face, nearly knocking you off your feet. NL \"Get out before I litter the floor with your guts.\" You take her word and exit with your guts still safely in your body."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["从黑暗中，一只手伸出来把你拉进了一家小店。眼睛适应了这里的亮度之后，你看见一个穿着鲜艳衣服的苍白女子正伸手展示整整一墙壁的药水。 NL “来买药水，快点！”她对你说。", "“很好，现在给我出去。” NL 你小心地离开了这家店。", "#r@砰@ NL 她戴着手套的拳头狠狠打在了你的脸上，差点就把你打翻在地。 NL “在我把你打得满地找牙之前给我滚出去。”你觉得她有可能说到做到，趁着牙齿还没事赶紧离开了这家店。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Buy 1 Potion] #y", "[Buy 2 Potions] #y", "[Buy 3 Potions] #y", " #yGold.", "[Leave]", "[Leave] #rTake #r", " #rDamage."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[买 1 瓶药水] #y", "[买 2 瓶药水] #y", "[买 3 瓶药水] #y", "  #y金币 。", "[离开]", "[离开] #r受到 #r", " #r点伤害。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Woman in Blue | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 蓝衣女子 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "The Woman in Blue", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | 需要有至少 50 金币时才会出现。<br>描述<br>从黑暗中，一只手伸出来把你拉进了一家小店。眼睛适应了这里的亮度之后，你看见一个穿着鲜艳衣服的苍白女子正伸手展示整整一墙壁的药水。“来买药水，快点！”她对你说。<br>选项<br>买 1 瓶药水 20 金币。“很好，现在给我出去。”你小心地离开了这家店。<br>买 2 瓶药水 30 金币。“很好，现在给我出去。”你小心地离开了这家店。<br>买 3 瓶药水 40 金币。“很好，现在给我出去。”你小心地离开了这家店。<br>离开（进阶15：损失等同于5%的最大生命值的血量）砰她戴着手套的拳头狠狠打在了你的脸上，差点就把你打翻在地。“在我把你打得满地找牙之前给我滚出去。”你觉得她有可能说到做到，趁着牙齿还没事赶紧离开了这家店。<br>注意<br>玩家所获得的药水种类随机，且无法选择获得哪1/2/3种将被获取。 | `single_source` | [蓝衣女子](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408968&wiki_id=646570) |
| `source.title_text` | 蓝衣女子 | `single_source` | [蓝衣女子](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408968&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=The Woman in Blue<br>|Image=Event-WomanInBlue.png<br>}}<br>{{E|The Woman in Blue}} is a shrine [[Event]] encountered in all [[Acts]].<br><br>Shrine events appear less frequently than other events.<br><br>== Options ==<br>{{Frame|Buy 1 Potion}} {{TS|gold||20 Gold.}}<br><br>{{Frame|Buy 2 Potions}} {{TS|gold||30 Gold.}}<br><br>{{Frame|Buy 3 Potions}} {{TS|gold||40 Gold.}}<br><br>{{Frame|Leave}} Nothing happens.<br><br>== Dialogue ==<br><blockquote><div style="font-style:... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
