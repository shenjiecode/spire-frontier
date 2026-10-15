# 牧师 / The Cleric

> 稳定 ID：`sts1.event.the_cleric`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：牧师
- English: The Cleric

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Heal |  | {"text": "35 Gold]: Heal X HP. * X is equal to 25% of the player's Max HP, rounded down."} |
| 2 | Purify |  | {"text": "50 (75) Gold]: Remove a card from your deck."} |
| 3 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Heal", "text": "35 Gold]: Heal X HP. * X is equal to 25% of the player's Max HP, rounded down."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Purify", "text": "50 (75) Gold]: Remove a card from your deck."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["A strange blue humanoid with a golden helm(?) approaches you with a huge smile. NL @\"Hello@ @friend!@ I am #bCleric! Are you interested in my services?!\" the creature shouts, loudly.", "A warm golden light envelops your body and dissipates. NL The creature grins. \"Cleric best healer. @Have@ @a@ @good@ @day!\"@", "A cold blue flame envelops your body and dissipates. NL The creature grins. \"Cleric talented. @Have@ @a@ @good@ @day!\"@", "You don't trust this #b\"Cleric\", so you leave."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["一个戴着金头盔（？）的奇怪蓝色人形生物脸上带着大大的微笑走到了你面前。 NL “ @你好啊朋友！@ 我是 #b牧师 ！你想不想试试我的服务呐？！”那个生物大声喊叫起来。", "一道温暖的金光笼罩了你然后消散了。 NL 那个生物咧嘴一笑：“牧师最强奶妈。那么 @祝你愉快啦！@ ”", "一道寒冷的蓝色火焰笼罩了你然后消散了。 NL 那个生物咧嘴一笑：“牧师就是能干。那么 @祝你愉快啦！@ ”", "你完全不相信这个 #b“牧师” ，就这样走开了。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Heal] #y35 #yGold: #gHeal #g", "[Locked] Requires: ", " Gold.", "[Purify] #y", " #yGold: #gRemove #ga #gcard #gfrom #gyour #gdeck.", "[Locked] Requires: 50 Gold.", "[Leave]", "Select a Card to Remove.", " #gHP."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[治疗] #y35 #y金币 ： #g回复 #g", "[锁定] 需要： ", " 金币。", "[净化] #y", " #y金币 : #g从你的牌组中 #g移除一张牌。", "[锁定] 需要： 50 金币。", "[离开]", "选择一张牌移除。", "。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Cleric | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 牧师 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "The Cleric", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>一个戴着金头盔（？）的奇怪蓝色人形生物脸上带着大大的微笑走到了你面前。“你好啊朋友！我是牧师！你想不想试试我的服务呐？！”那个生物大声喊叫起来。<br>选项<br>治疗 35 金币：回复 25% 生命。 需要：35 金币。一道温暖的金光笼罩了你然后消散了。那个生物咧嘴一笑：“牧师最强奶妈。那么祝你愉快啦！”<br>净化 50 (进阶15：75) 金币：从你的牌组中移除一张牌。 需要：50(进阶15：75) 金币。一道寒冷的蓝色火焰笼罩了你然后消散了。那个生物咧嘴一笑：“牧师就是能干。那么祝你愉快啦！”<br>离开你完全不相信这个“牧师”，就这样走开了。<br>轶事<br>牧师和老乞丐事件是唯二会出现“牧师”的地方。 | `single_source` | [牧师](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375132&wiki_id=646570) |
| `source.title_text` | 牧师 | `single_source` | [牧师](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375132&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=The Cleric<br>|Image=Event-Cleric.png<br>}}<br>{{E|The Cleric}} is a {{QueryLink|Events|shrine:Yes|shrine Event}} found exclusively in [[Act 1]]. It is one of the events affected by {{Asc|15|Ascension}}. It can only be encountered if the player has at least 35 [[Gold]]; enough to afford at least one of the options.<br><br>== Options ==<br>{{Frame|Heal}} {{TS|gold||35 [[Gold]]:}} {{TS|positive||Heal X HP.}}<br>* X is equal to 25% of the player's Max HP, rounded down.<b... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
