# 破烂软泥 / Scrap Ooze

> 稳定 ID：`sts1.event.scrap_ooze`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：破烂软泥
- English: Scrap Ooze

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Reach Inside | {"text": "Lose 3 (5) HP"} | {"text": "25% chance to find a Relic]. * If you fail to find a Relic], you can try again until you find one. Each time you fail, the HP loss is increased by 1 and the chance to gain a Relic increases by 10%"} |
| 2 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Reach Inside", "text": "Lose 3 (5) HP. 25% chance to find a Relic]. * If you fail to find a Relic], you can try again until you find one. Each time you fail, the HP loss is increased by 1 and the chance to gain a Relic increases by 10%."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["As you walk into the room you hear a ~gurgling~ and the @grinding@ of metals. Before you is a slime-like creature that ate too much scrap for its own good. From the center of the creature you see glints of strange light, perhaps something magical? It looks like you can get some #ytreasure if you just reach inside its... opening. However, the acid and sharp objects may #rhurt.", "#r@Ouch!@ NL All you find is corroded metal and a bit of #r@burning@ #r@pain.@ NL However, you're still convinced... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你刚走进房间，就听见奇怪的 ~咕嘟声~ 和金属的 @摩擦声@ 。在你面前的是一个史莱姆状的生物，它显然是吃了太多的破铜烂铁，消化不良了。 你在这个生物的中央见到了奇怪的光芒，或许是什么有魔法的物品？看起来只要你愿意把手伸进这东西的……开口，你就能得到什么 #y财宝 。当然，酸液和尖锐的破烂有可能会让你 #r受伤。", "#r@啊呀！@ NL 你找到的只是已被腐蚀的金属和一点 #r@灼伤的疼痛@ 。 NL 可是你还是很确定，里面一定有一件 #y遗物 ……", "#g成功！ NL 在金属和酸液之中翻找了好久，你终于抓住了一件 #y遗物 把它拉了出来。 NL 你从黏液中抽回手来，虽然 #r受了点伤 ，但至少东西拿到了。", "你决定离开这个地方。 NL 史莱姆并不在意，接着慢慢消化它的美餐。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Reach Inside] #rLose #r", " #rHP. #g", "%: #gFind #ga #gRelic.", "[Leave]", "[Deeper] #rLose #r"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[伸手进去] #r失去 #r", " #r生命。 #g", "%: #g找到一件遗物。", "[离开]", "[接着往里伸] #r失去 #r"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Scrap Ooze | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 破烂软泥 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Scrap Ooze", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你刚走进房间，就听见奇怪的咕嘟声和金属的摩擦声。在你面前的是一个史莱姆状的生物，它显然是吃了太多的破铜烂铁，消化不良了。 你在这个生物的中央见到了奇怪的光芒，或许是什么有魔法的物品？看起来只要你愿意把手伸进这东西的……开口，你就能得到什么财宝。当然，酸液和尖锐的破烂有可能会让你受伤。<br>选项<br>伸手进去 失去 3 (进阶15以上为5) 生命。25%：找到一件遗物。<br>结果 1：啊呀！你找到的只是已被腐蚀的金属和一点灼伤的疼痛。可是你还是很确定，里面一定有一件遗物……<br>结果 2：成功！在金属和酸液之中翻找了好久，你终于抓住了一件遗物把它拉了出来。你从黏液中抽回手来，虽然受了点伤，但至少东西拿到了。<br>接着往里伸 失去 3 (进阶15以上为5) + ( 1 × 之前尝试的次数) 生命。25% + ( 10 × 之前尝试的次数)%：找到一件遗物。<br>离开你决定离开这个地方。史莱姆并不在意，接着慢慢消化它的美餐。<br>伤害与获得遗物的概率<br>图片来自wiki<br>想要获得遗物平均会损失 11.34(进阶15以上为... | `single_source` | [破烂软泥](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375295&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/13/5818e064f4d39218d57dc68a16219152.jpeg"] | `single_source` | [破烂软泥](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375295&wiki_id=646570) |
| `source.title_text` | 破烂软泥 | `single_source` | [破烂软泥](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375295&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Scrap Ooze<br>|Image=Event-ScrapOoze.png<br>}}<br>{{E|Scrap Ooze}} is an event found exclusively in [[Act 1]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Reach Inside}} {{TS|negative||Lose 3}} {{Asc|15|(5)}} {{TS|negative||HP.}} {{TS|positive||25% chance to find a [[Relic]].}}<br>* If you fail to find a [[Relic]], you can try again until you find one. Each time you fail, the HP loss is increased by 1 and the chance to gai... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
