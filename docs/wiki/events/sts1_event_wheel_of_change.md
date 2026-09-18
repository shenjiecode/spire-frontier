# 变化大转盘 / Wheel of Change

> 稳定 ID：`sts1.event.wheel_of_change`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：变化大转盘
- English: Wheel of Change

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Play | {"text": "Become Cursed - Decay ** Remove a card from your deck"} | {"text": "Spin a wheel containing the following \"prizes\" (clockwise starting at 12 o'clock in the image): ** Take 10% (15%) of your Max HP as damage. ** Gain Gold] ** Gain a random Relic] ** Heal to full HP **"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Play", "text": "Spin a wheel containing the following \"prizes\" (clockwise starting at 12 o'clock in the image): ** Take 10% (15%) of your Max HP as damage. ** Gain Gold] ** Gain a random Relic] ** Heal to full HP **"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You come upon a dapper looking, cheery gremlin. NL \"It's time to spin the wheel! Are you ~R~ ~E~ ~A~ ~D~ ~Y~ ~?~ Of course you are!\"", "\"You win some #yGOLD! NL YAY!!!!\"", "\"Ah, a #ggift! NL Enjoy!\"", "\"Oooh, a free #gHeal for you!\"", "\"Looks like you won a #pCurse! NL That's not good. NL Oh well! Better luck next time!\"", "\"Ohh, the power of #r~darkness...~ NL Choose a card to remove from your deck!\"", "\"Uh oh! NL You lose!\" NL You spot him readying a shiv...", "You slash at ... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你见到一位穿着帅气、满面笑容的地精。 NL “是时候转动转盘了！ ~你准备好了吗？~ 你当然准备好了！”", "“你赢得了一些 #y金币 ！ NL 噢耶！！！”", "“啊，一件 #g礼物 ！ NL 请收下吧！”", "“哦哦，一次免费的 #g回复 ！”", "“看起来你赢得了一个 #p诅咒 ！ NL 这就比较糟糕啦。 NL 好吧！那么祝你下次好运啦！”", "“哦哦， #r~黑暗的力量……~ NL 在你的牌组中选择一张移除吧！”", "“呃欧！ NL 你输了！” NL 你看见他拿出了一把小刀……", "你向这个疯子地精砍了过去，但他的速度太快了！ NL 你被他的小刀砍中了几次。 NL “代价已经付清！！” NL 他说着就和转盘一起在烟雾中消失了。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Play]", "[Prize!] YAY!!!!", "[Prize!] #gObtain #ga #gRelic.", "[Prize!] #gHeal #gto #gfull #ghealth.", "[Prize?] #rCurse #r- #rDecay.", "[Prize!] #gRemove #ga #gcard #gfrom #gyour #gdeck.", "[Prize?] #rLose #r", " #rHP.", "[Leave]", "Select a Card to Remove."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[玩小游戏]", "[奖品！] 耶！！！", "[奖品！] #g获得遗物。", "[奖品！] #g回复所有生命。", "[奖品？] #r诅咒——腐朽。", "[奖品！] #g从你的牌组中移除一张牌。", "[奖品？] #r失去 #r", " #r生命。", "[离开]", "选择一张牌移除。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Wheel of Change | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 变化大转盘 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Wheel of Change", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你见到一位穿着帅气、满面笑容的地精。“是时候转动转盘了！你准备好了吗？你当然准备好了！”<br>选项<br>玩小游戏随机获得奖品<br>奖品<br>金币“你赢得了一些金币！噢耶！！！”<br>注：在第一阶段获得 100 金币，在第二阶段获得 200 金币，在第三阶段获得 300 金币。<br>遗物“啊，一件礼物！请收下吧！”<br>回复所有生命“哦哦，一次免费的回复！”<br>诅咒——腐朽“看起来你赢得了一个诅咒！这就比较糟糕啦。好吧！那么祝你下次好运啦！”<br>从你的牌组中移除一张牌“哦哦，黑暗的力量……在你的牌组中选择一张移除吧！”<br>失去 10% 生命“呃欧！你输了！”你看见他拿出了一把小刀……你向这个疯子地精砍了过去，但他的速度太快了！你被他的小刀砍中了几次。“代价已经付清！！” | `single_source` | [变化大转盘](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408964&wiki_id=646570) |
| `source.title_text` | 变化大转盘 | `single_source` | [变化大转盘](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408964&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Wheel of Change<br>|Image=Event-SpinTheWheel.png<br>}}<br>{{E|Wheel of Change}} is a shrine [[Event]] found in all [[Acts]].<br><br>Shrine events appear less frequently than other acts.<br>{{Clear}}<br>== Options ==<br><div style="float:right; display:flex; flex-direction:row; gap:10px; margin:0 0 10px 10px;"><br>[[File:SpinButton.png|100px|thumb|Spin Button.]]<br>[[File:WheelArrow.png|100px|thumb|Wheel arrow.]]<br>[[File:Wheel.png|250px|thumb|Wheel.]]<br></div><br>{{... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
