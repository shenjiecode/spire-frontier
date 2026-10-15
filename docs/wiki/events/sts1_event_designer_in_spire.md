# 尖端设计师 / Designer In-Spire

> 稳定 ID：`sts1.event.designer_in_spire`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：尖端设计师
- English: Designer In-Spire

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2 , Act 3 - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Adjustments | {"text": "Lose 40 (50) Gold]"} | {"text": "One of the following rewards appears. * Upgrade] a card. * Upgrade] two random cards"} |
| 2 | Clean Up | {"text": "Lose 60 (75) Gold]"} | {"text": "One of the following rewards appears. * Remove a card. * Transform] two cards"} |
| 3 | Full Service | {"text": "Lose 90 (110) Gold]"} | {"text": "Remove a card, then upgrade] a random card"} |
| 4 | Punch | {"text": "Lose 3 (5) HP"} | {"text": "Lose 3 (5) HP."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Adjustments", "text": "One of the following rewards appears. * Upgrade] a card. * Upgrade] two random cards"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Clean Up", "text": "One of the following rewards appears. * Remove a card. * Transform] two cards"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Full Service", "text": "Remove a card, then upgrade] a random card"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Punch", "text": "Lose 3 (5) HP."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You discover a #g~colorful~ shop with the banner \"IN-SPIRE\" and walk in to see what's inside. NL \"No, no way. Nope. Can't let you in!\" NL NL A man with ridiculous clothing appears at the entrance to bar you.", "\"This will not do, no no. What is this style? @Disgusting!@ Are you #rbleeeeding? #p~Groooss.~ @Business??@ You a customer? Fine. ~Whaaatever.\"~ NL He lets out an exaggerated sigh and points at a list of services. NL NL The services seem fine, but you would rather punch this sm... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你发现一家 #g~五彩斑斓~ 的店，横幅上挂着大大的“尖端”两个字，就走进去想看看里面有什么。 NL “等等，别，不行。你不能进来！” NL NL 一个穿着打扮无比荒唐的男人出现在门口把你拦了下来。", "“不行不行，这怎么能行呢。哎呀，你这算是什么风格？ @令人作呕！@ 什么，你还 #r流流、流着血 ？ 哎呀 #p~好恶心啊~ 。啊？你问我是做 @什么生意@ 的？？你是顾客吗？好吧。 ~哎呀真是没办法啦。~ ” NL 他夸张地叹了一口气，伸手指向一张服务目录。 NL NL 服务内容看起来还挺正常的，但你现在一心只想对着这自我感觉良好的家伙洋洋自得的脸上一拳揍过去。", "“好啦，那下次再来哦。” NL NL ……刚刚真该一拳揍上去的。", "你一拳揍了过去，打到你的手都疼了。 NL “我的 @脸@ 啊！！ 这下我要——” NL NL 他晕了过去。呵呵，现在谁才又 #p~恶心~ 又 #r流着血 啦？"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Continue]", "[Adjustments] #rLose #r", "[Clean Up] #rLose #r", "[Full Service] #rLose #r", "[Punch] #rLose #r", " #rHP.", " #rGold. ", "#gUpgrade #g", " #grandom #gcards.", "#gUpgrade #ga #gcard.", "#gRemove #ga #gcard.", "#gTransform #g", " #gcards.", "#gRemove #ga #gcard #gand #gupgrade #ga #grandom #gcard.", "[Leave]", "Choose a Card to Upgrade", "Choose 2 Cards to Transform", "Choose a Card to Remove"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[继续]", "[小修一下] #r失去 #r", "[清洁一下] #r失去 #r", "[全套服务] #r失去 #r", "[一拳过去] #r失去 #r", " #r生命。", " #r金币。", " #g随机升级 #g", " #g张牌。", " #g升级一张牌。", " #g移除一张牌。", " #g变化 #g", " #g张牌。", " #g移除一张牌，然后随机升级一张牌。", "[离开]", "选择一张牌升级", "选择2张牌变化", "选择一张牌移除"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Designer In-Spire | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | “尖端”设计师 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Designer", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | 尖端设计师是会发生在第二阶段或第三阶段的事件。仅会在金币不少于75时出现。<br>描述<br>你发现一家五彩斑斓的店，横幅上挂着大大的“尖端”两个字，就走进去想看看里面有什么。“等等，别，不行，你不能进来！”一个穿着打扮无比荒唐的男人出现在门口把你拦了下来<br>“不行不行，这怎么能行呢，哎呀，你这算是什么风格？令人作呕！什么，你还流流，流着血？哎呀好恶心啊。啊？你问我是做什么生意的？？你是顾客吗？好吧，哎呀真是没办法啦。”他夸张地叹了一口气，伸手指向一张服务目录。服务内容看起来还挺正常的，但你现在一心指向对着这自我感觉良好的家伙得意洋洋的脸上一拳揍过去。<br>选项<br>小修一下 失去50金币。随机升级两张牌/选择升级一张牌。<br>“好啦，那下次再来哦。”...刚刚真该一拳揍上去的。<br>清洁一下 失去75金币。移除1张牌/选择变化两张牌。<br>“好啦，那下次再来哦。”...刚刚真该一拳揍上去的。<br>全套服务 失去110金币。移除一张牌，然后随机升级一张牌<br>“好啦，那下次再来哦。”...刚刚真该一拳揍上去的。<br>一拳过去 失去3点生命值（进阶15: 5点）... | `single_source` | [尖端设计师](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408934&wiki_id=646570) |
| `source.title_text` | 尖端设计师 | `single_source` | [尖端设计师](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408934&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Designer In-Spire<br>|Image=Event-Designer.png<br>}}<br>{{E|Designer In-Spire}} is a {{QueryLink|Events|shrine:Yes|shrine Event}} found in [[Act 2]] and [[Act 3]]. It will only appear if the player has at least 75 [[Gold]].<br><br>== Options ==<br>{{Frame|Adjustments}} {{TS|negative||Lose 40}} {{asc|15|(50)}} [[Gold]]{{TS|negative||.}} {{TS|positive||One of the following rewards appears.}}<br>* {{TS|positive||[[Upgrade]] a card.}}<br>* {{TS|positive||[[Upgrade]] two r... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
