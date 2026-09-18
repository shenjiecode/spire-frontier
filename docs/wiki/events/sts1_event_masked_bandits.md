# 蒙面强盗 / Masked Bandits

> 稳定 ID：`sts1.event.masked_bandits`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：蒙面强盗
- English: Masked Bandits

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Pay | {"text": "Lose ALL of your Gold"} | {"text": "Lose ALL of your Gold."} |
| 2 | Fight! |  | {"text": "Starts a combat against [[#Bandits|the three bandits]] (Pointy, Romeo, and Bear). Upon winning, obtain regular card rewards, 25 - 35 Gold], and Red Mask."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Pay", "text": "Lose ALL of your Gold."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Fight!", "text": "Starts a combat against [[#Bandits|the three bandits]] (Pointy, Romeo, and Bear). Upon winning, obtain regular card rewards, 25 - 35 Gold], and Red Mask."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Hehehe.. Thanks for the #ygold! NL Oh, I love #ygold. It's so nice. NL #y~shiny~ #y~shiny~ chits they are!", "Hey #bBear, hey! NL This guy gave us all his #ygold! What a sucker, right? NL Get this, I just had to ask nicely. Who knew?! NL I certainly didn't! What a chump!", "Gang, let's all have a laugh for this wondrous occasion! NL @Hahaah@ NL @Ho@ @HOH@ ~hoho!~ NL ~Hoh!~", "Oh? You're still here? NL Did you overhear something? Didn't think so. NL #r@*snerk*@ ~...loser....~ @Hahaha@ ~haaah... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["嘿嘿嘿……谢谢你的 #y金币 啦！ NL 哎呀，我最喜欢 #y金币 了，那是多好的东西啊。 NL #y~闪闪亮的~ 小可爱们！", "喂， #b熊 ，喂！ NL 这家伙居然把他的 #y金币 全都给我们了！ 太蠢了是吧？ NL 你猜怎么着？我只是好声好气地问了一下就拿到了，谁会知道啊？！ NL 我反正是不知道！ 真是个冤大头！", "小的们，这么好的事儿，我们可得一起好好笑一笑！ NL @哈哈哈@ NL @吼吼吼@ ~嚯嚯！~ NL ~哗哈哈!~", "哦？你还在这儿呐？ NL 你有听见什么吗？没有吧。 NL #r@*噗嗤*@ ~……白痴……~ @哈哈哈@ ~哈哈~", "你遇见一群戴着巨大 #r红面具 的强盗。 NL “你好啊，留下买路钱……价格公道，只要你身上 @所有的@ #y金币 就行！ 嘿嘿嘿！”"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Pay] #rLose #rALL of your #yGold.", "[Fight!]", "[Continue]", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[付钱] #r失去所有 #y金币 。", "[战斗！]", "[继续]", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Masked Bandits | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 蒙面强盗 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Masked Bandits", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你遇见一群戴着巨大红面具的强盗。“你好啊，留下买路钱……价格公道，只要你身上所有的金币就行！ 嘿嘿嘿！”<br>选项<br>付钱 失去所有金币。嘿嘿嘿……谢谢你的金币啦！哎呀，我最喜欢金币了，那是多好的东西啊。闪闪亮的小可爱们！喂，熊，喂！这家伙居然把他的金币全都给我们了！ 太蠢了是吧？你猜怎么着？我只是好声好气地问了一下就拿到了，谁会知道啊？！我反正是不知道！ 真是个冤大头！小的们，这么好的事儿，我们可得一起好好笑一笑！哈哈哈吼吼吼嚯嚯！哗哈哈！哦？你还在这儿呐？你有听见什么吗？没有吧。*噗嗤*……白痴……哈哈哈哈哈<br>战斗<br>注：进入战斗，敌人分别是：罗密欧、熊和尖尖。胜利后除了常规的战斗奖励外，还会获得遗物：遗物-红面具。 | `single_source` | [蒙面强盗](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408886&wiki_id=646570) |
| `source.infobox.description` | 30 | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 蒙面强盗 | `single_source` | [蒙面强盗](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408886&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Masked Bandits<br>|Image=Event-MaskedBandits.png<br>}} {{Small Relic Infobox|Red Mask}}<br>{{E|Masked Bandits}} is an [[Event]] found exclusively in [[Act 2]]. This Event and {{E|Tomb of Lord Red Mask}} are the only ways to obtain {{R|Red Mask}}.<br><br>== Options ==<br>{{Frame|Pay}} {{TS|negative||Lose ALL}} of your {{TS|gold||Gold.}}<br><br><br><br><br>{{Frame|Fight!}} <br>* Starts a combat against [[#Bandits|the three bandits]] ({{M|Pointy}}, {{M|Romeo}}, and {{M|B... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
