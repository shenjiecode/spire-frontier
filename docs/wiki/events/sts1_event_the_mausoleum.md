# 陵墓 / The Mausoleum

> 稳定 ID：`sts1.event.the_mausoleum`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：陵墓
- English: The Mausoleum

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Open Coffin | {"text": "Become Cursed - Writhe"} | {"text": "Obtain a Relic]. 50% (100%):"} |
| 2 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Open Coffin", "text": "Obtain a Relic]. 50% (100%): Become Cursed - Writhe"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Venturing through a series of tombs, you are faced with a large sarcophagus ~studded~ ~with~ ~gems~ in the center of a circular room. NL You cannot make out the writing on the coffin, however, you do notice #p~black~ #p~fog~ seeping out from the sides.", "You push open the coffin. As you do, #p~black~ #p~fog~ spews forth and covers the entire room! Inside, you find no body, only a #y~relic.~ You take it and move onwards, #r@coughing@ #r@violently.@", "You push open the coffin. The fog dissi... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你在一系列坟墓间穿行，前方出现了一个圆形房间，中间是一口 ~镶嵌着许多宝石的~ 巨大石棺。 NL 你辨认不出石棺上的字迹，但你能注意到有 #p~黑色的雾气~ 从石棺的两侧渗透出来。", "你推开石棺，一股 #p~黑雾~ 涌了出来，淹没了整个房间！ 石棺里没有实体，只有一件 #y~遗物~ 。你拾起它重新上路， 并 #r@剧烈地咳嗽起来@ 。", "你推开石棺，雾气很快消散了。 在石棺里你找到了一具荣誉满身的士兵尸体，尸体的手还紧紧握着一件 #y遗物 ，你把东西偷了过来，离开了房间。", "你决定不去打扰被遗忘的死者，继续赶路。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Open Coffin] #gObtain #ga #gRelic. #r", "%: #rBecome #rCursed #r- #rWrithe.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[打开棺材] #g获得一件遗物。 #r", "%: #r被诅咒——苦恼。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Mausoleum | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 陵墓 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "The Mausoleum", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你在一系列坟墓间穿行，前方出现了一个圆形房间，中间是一口镶嵌着许多宝石的巨大石棺。你辨认不出石棺上的字迹，但你能注意到有黑色的雾气从石棺的两侧渗透出来。<br>选项<br>打开棺材 得到一件遗物。50%（进阶15以上为100%）：被诅咒——苦恼。结果 1：你推开石棺，一股黑雾涌了出来，淹没了整个房间！ 石棺里没有实体，只有一件遗物。你拾起它重新上路， 并剧烈地咳嗽起来。结果 2：你推开石棺，雾气很快消散了。 在石棺里你找到了一具荣誉满身的士兵尸体，尸体的手还紧紧握着一件遗物，你把东西偷了过来，离开了房间。<br>离开你决定不去打扰被遗忘的死者，继续赶路。 | `single_source` | [陵墓](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408896&wiki_id=646570) |
| `source.title_text` | 陵墓 | `single_source` | [陵墓](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408896&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=The Mausoleum<br>|Image=Event-Mausoleum.png<br>}} {{Small Card Infobox|Writhe}}<br>{{E|The Mausoleum}} is an [[Event]] found in [[Act 2]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Open Coffin}} {{TS|positive||Obtain a [[Relic]].}} {{TS|negative||50% {{Asc|15|(100%)}}: Become Cursed - {{C|Writhe}}}}<br><br>{{Frame|Leave}} Nothing happens. <br><br>== Dialogue ==<br><blockquote><div style="font-style:italic"><br>Venturing ... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
