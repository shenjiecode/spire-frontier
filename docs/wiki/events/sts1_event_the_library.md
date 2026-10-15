# 大图书馆 / The Library

> 稳定 ID：`sts1.event.the_library`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：大图书馆
- English: The Library

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Read |  | {"text": "Choose 1 of 20 cards to add to your deck."} |
| 2 | Sleep |  | {"text": "Heal X HP. * X is equal to 33% (20%) of the player's Max HP."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Read", "text": "Choose 1 of 20 cards to add to your deck."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Sleep", "text": "Heal X HP. * X is equal to 33% (20%) of the player's Max HP."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You come across an ornate building which appears abandoned. NL A plaque that has been torn free from a wall is on the floor. It reads, #b\"THE #bLIBRARY\". NL Inside, you find countless rows of scrolls, manuscripts, and books. NL You pick one and cozy yourself into a chair for some quiet time.", "Reading is for chumps. NL You doze off in a comfy chair instead. NL ~Zzz...~ ~zzz...~ ~..Zz....~ NL You wake up feeling refreshed.", "The story is about an insect-controlling teenage girl who aspir... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你经过一栋被遗弃的华美建筑物。 NL 墙上的标牌掉在了地上，上面写着 #b“大图书馆” 几个大字。 NL 你走进建筑物中，看见了无数卷轴、手稿和书籍。 NL 你拿起一本，舒服地坐在沙发椅上看了好一会儿。", "傻子才读书呢。 NL 你在沙发椅上打了个盹儿。 NL ~Zzz...~ ~zzz...~ ~..Zz....~ NL 醒来后，你觉得神清气爽。", "这本书是关于一个被昆虫控制的想当英雄的少女的。书中有许多关于超能力、战术和不同视角的内容，极有创意。 NL 读完书，你觉得心满意足。", "这本书是关于一个在群星旅行，最后落难在一个荒芜陌生星球上的男人的。 他依靠着智慧、幸运、坚韧不拔和用来维系自己理性的一点幽默感，最终成功返回了故乡。 NL 读来令人神往。", "这本书是关于一个巨大的废弃地下建筑的，地上的环境已经无法生存，小说的内容充满了阴谋、洗脑和不公。你开始思考是否在高塔中也存在着类似的关系网。 NL 读得让人心里发毛。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Read] #gChoose #g1 #gof #g20 #gcards #gto #gadd #gto #gyour #gdeck.", "[Sleep] #gHeal #g", " #gHP.", "[Leave]", "Add a card to your deck."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[阅读] #g从 #g20 #g张牌中选择一张加入你的牌组。", "[睡觉]  #g回复 #g", " #g点生命。", "[离开]", "选择一张牌加入牌组。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Library | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 大图书馆 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "The Library", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你经过一栋被遗弃的华美建筑物。墙上的标牌掉在了地上，上面写着“大图书馆”几个大字。你走进建筑物中，看见了无数卷轴、手稿和书籍。你拿起一本，舒服地坐在沙发椅上看了好一会儿。<br>选项<br>阅读 从 20 张牌中选择一张加入你的牌组。结果 1：这本书是关于一个被昆虫控制的想当英雄的少女的。书中有许多关于超能力、战术和不同视角的内容，极有创意。读完书，你觉得心满意足。结果 2：这本书是关于一个在群星旅行，最后落难在一个荒芜陌生星球上的男人的。 他依靠着智慧、幸运、坚韧不拔和用来维系自己理性的一点幽默感，最终成功返回了故乡。读来令人神往。结果 3：这本书是关于一个巨大的废弃地下建筑的，地上的环境已经无法生存，小说的内容充满了阴谋、洗脑和不公。你开始思考是否在高塔中也存在着类似的关系网。读得让人心里发毛。<br>睡觉 回复 33%（进阶15以上为20%） 生命。傻子才读书呢。你在沙发椅上打了个盹儿。Zzz...zzz.....Zz....醒来后，你觉得神清气爽。 | `single_source` | [大图书馆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408893&wiki_id=646570) |
| `source.title_text` | 大图书馆 | `single_source` | [大图书馆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408893&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=The Library<br>|Image=Event-Library.png<br>}}<br>{{E|The Library}} is an [[Event]] found exclusively in [[Act 2]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Read}} {{TS|positive||Choose 1 of 20 cards to add to your deck.}}<br><br><br><br><br>{{Frame|Sleep}} {{TS|positive||Heal X HP.}}<br>* X is equal to 33% {{Asc|15|(20%)}} of the player's Max HP.<br><br>== Dialogue ==<br><blockquote><div style="font-style:italic"><br>Yo... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
