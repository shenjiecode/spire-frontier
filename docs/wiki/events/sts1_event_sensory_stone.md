# 感知石 / Sensory Stone

> 稳定 ID：`sts1.event.sensory_stone`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：感知石
- English: Sensory Stone

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 3"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Recall |  | {"text": "Add 1 Colorless card to your deck."} |
| 2 | Recall | {"text": "Lose 5 HP"} | {"text": "Add 2 Colorless cards to your deck"} |
| 3 | Recall | {"text": "Lose 10 HP"} | {"text": "Add 3 Colorless cards to your deck"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Recall", "text": "Add 1 Colorless card to your deck."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Recall", "text": "Add 2 Colorless cards to your deck"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Recall", "text": "Add 3 Colorless cards to your deck"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Navigating through the Beyond, you discover a #bglowing #btesseract @spinning@ and ~shifting~ gently in the air.", "You touch it. NL NL A #r@sharp@ #r@pain@ flows through you, followed by vivid flashes of a distant memory. NL ...whose memories are these?", "#r~FEAR.~ NL NL A demonic creature towers above you, wings spread wide as it howls with laughter. Dead bodies of a tribe surround you while the village is engulfed in terrible #p~dark~ #p~flames.~ NL NL The demon calls out, taunting you.... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你在高塔深处前进时，你遇到一个悬浮在空中缓慢 @旋转@ 且 ~变幻~ 着的 #b发光超立方体 。", "你触碰了超立方体。 NL NL 你浑身感到一股 #r@剧烈的疼痛@ ，然后一段遥远的回忆清晰地闪现在你脑中。 NL ……这是谁的记忆？", "#r~恐惧。~ NL NL 一个恶魔般的生物耸立在你上方，它的双翅张开，放声大笑。你的周围是数不尽的同族们的尸体，整个村庄已被可怕的 #p~黑色火焰~ 吞没殆尽。 NL NL 恶魔嘲笑着你： NL NL “ #r@这下你确实成为最强的了！@ #r@哈哈哈……呵呵呵……@ #r@哈哈哈哈哈！！@ ” NL NL 它的笑声没有停止，永远回荡在你的耳中…… ", "#g~凯旋。~ NL NL 月光之下，一具 #p~幽灵般生物~ 的遗骸慢慢没入了你面前的泥土中，让人看不真切。你已向姐妹们证明了自己的实力。 NL NL 你以胜者的姿态静静伫立着，周围的人们隆重地将 #y那个生物的头骨 放置在你的头上，仪式完成了。 NL NL 你向着一座高塔出发……", "#b~混乱。~ NL NL #y[目标] #g必须维系 #g平衡 NL #y[定义] #g... | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Recall] #gAdd #g1 #gColorless #gcard #gto #gyour #gdeck.", "[Recall] #gAdd #g2 #gColorless #gcards #gto #gyour #gdeck. #rLose #r", "[Recall] #gAdd #g3 #gColorless #gcards #gto #gyour #gdeck. #rLose #r", " #rHP.", "[Leave]", "[Interact]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[回忆] #g在你的牌组中加入 #g1 #g张无色牌。", "[回忆] #g在你的牌组中加入 #g2 #g张无色牌。 #r失去 #r", "[回忆] #g在你的牌组中加入 #g3 #g张无色牌。 #r失去 #r", " #r点生命。", "[离开]", "[交互]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Sensory Stone | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 感知石 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SensoryStone", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你在高塔深处前进时，你遇到一个悬浮在空中缓慢旋转且变幻着的发光超立方体。你触碰了超立方体你浑身感到一股剧烈的疼痛,然后一段遥远的回忆清晰地闪现在你的脑中……这是谁的记忆？<br>选项<br>回忆 在你的牌组中加入1张无色牌<br>凯旋月光之下，一具幽灵般的生物的遗骸慢慢没入了你面前的泥土中，让人看不真切，你已向姐妹们证明了自己的实力。你以胜者的姿态静静伫立着，周围的人们隆重地将那个生物的头骨放置在你的头上，仪式完成了。你向着一座高塔出发……<br>交互 在你的牌组中加入2张无色牌。失去5点生命。<br>恐惧一个恶魔般的生物耸立在你上方，它的双翅张开，放声大笑。你的周围是数不尽的同族的尸体，整个村庄已被可怕的黑色火焰吞没殆尽。恶魔嘲笑着你：“这下你确实成为最强的了，哈哈哈……呵呵呵……哈哈哈哈哈！！”'他的笑声没有停止，永远回荡在你的耳中……<br>交互 在你的牌组中加入3张无色牌。失去10点生命。<br>混乱[目标]必须维系平衡[定义]平衡[错误]无法检索到平衡[定义]平衡[错误]无法检索到平衡[警告]巨大物体正在靠近“我……是……涅奥…... | `single_source` | [感知石](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408911&wiki_id=646570) |
| `source.title_text` | 感知石 | `single_source` | [感知石](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408911&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Sensory Stone<br>|Image=Event-SensoryStone.png<br>}}<br>{{E|Sensory Stone}} is an [[Event]] found exclusively in [[Act 3]]. <br><br>== Options ==<br>{{Frame|Recall}} {{TS|positive||Add 1 {{QueryLink|Cards|color:Colorless|Colorless}} card to your deck.}}<br><br>{{Frame|Recall}} {{TS|positive||Add 2 {{QueryLink|Cards|color:Colorless|Colorless}} cards to your deck.}} {{TS|negative||Lose 5 HP.}}<br><br>{{Frame|Recall}} {{TS|positive||Add 3 {{QueryLink|Cards|color:Colorles... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
