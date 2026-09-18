# 摩艾石像 / The Moai Head

> 稳定 ID：`sts1.event.the_moai_head`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：摩艾石像
- English: The Moai Head

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 3"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Jump Inside | {"text": "Lose X Max HP; Lose Golden Idol"} | {"text": "Heal to full HP. . * X is equal to 12.5% (18%) of the player's Max HP. Offer: Golden Idol Receive 333 Gold]. . * If the player lacks Golden Idol, this option is replaced with"} |
| 2 | Locked |  | {"text": "Requires: Golden Idol."} |
| 3 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Jump Inside", "text": "Heal to full HP. Lose X Max HP. * X is equal to 12.5% (18%) of the player's Max HP. Offer: Golden Idol Receive 333 Gold]. Lose Golden Idol. * If the player lacks Golden Idol, this option is replaced with"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Locked", "text": "Requires: Golden Idol."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You stumble across something that feels *very* out of place. Before you, an enormous stony head emerges from a large wall segment that does not shift and change like the rest of this area. NL The head's mouth is wide open, and it reveals large intimidating teeth stained red with blood. The surface of the statue is riddled with pictographs that seem to indicate people throwing themselves into the mouth of this head and being devoured. Why would anyone do that?", "At first when you step up in... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你遇到了一个和四周*完全不搭*的东西。在你面前有一道与周围不同，没有在移动和变化的墙壁，一个巨大的石制头像从墙壁上凸出来。 NL 石像的嘴大张着，里面有许多巨大的染着血迹的牙齿。石像表面上写着许多象形文字，似乎是说有许多人会自己跳进嘴里被石像吞噬。为什么会有人这样做呢？", "你踏进石像的嘴，一开始什么也没发生。正当你觉得自己有点犯傻的时候，上方巨大的臼齿突然砸了下来，将你整个碾碎了。 NL @黑暗。@ NL 一段时间后，你在黑暗中见到一线光明，并听见了轰隆作响的声音，你这才反应过来那是石像的牙齿重新缓慢地升了上去。 NL NL NL 你满心困惑地走了出来。", "巨大的臼齿轰然砸下，将金神像碾成了粉末，你下意识地往后跳了一步。当巨齿重新上升时，嘴中不断涌出 #y金币 ，你赶紧把钱捡了起来。", "你离开了这里，但心里还是有一些好奇。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Jump Inside] #gHeal #gto #gfull #gHP. #rLose #r", " #rMax #rHP.", "[Offer: Golden Idol] #gGain #g333 #gGold. #rLose #rGolden #rIdol.", "[Locked] Requires: Golden Idol.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[跳进去]  #g回复所有生命。 #r失去 #r", " #r最大生命。", "[献上：金神像] #g获得 #g333 #g金币。 #r失去金神像。", "[锁定] 需要：金神像。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Moai Head | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 摩艾石像 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "The Moai Head", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | 有金神像或者生命少于 50% 的时候可能会遇上<br>描述<br>你遇到了一个和四周*完全不搭*的东西。在你面前有一道与周围不同，没有在移动和变化的墙壁，一个巨大的石制头像从墙壁上凸出来。石像的嘴大张着，里面有许多巨大的染着血迹的牙齿。石像表面上写着许多象形文字，似乎是说有许多人会自己跳进嘴里被石像吞噬。为什么会有人这样做呢？<br>选项<br>跳进去 回复所有生命。失去 12.5% （进阶15或以上为18%）最大生命。你踏进石像的嘴，一开始什么也没发生。正当你觉得自己有点犯傻的时候，上方巨大的臼齿突然砸了下来，将你整个碾碎了。黑暗。一段时间后，你在黑暗中见到一线光明，并听见了轰隆作响的声音，你这才反应过来那是石像的牙齿重新缓慢地升了上去。你满心困惑地走了出来。<br>献上：金神像 得到 333 金币。失去金神像。 需要：金神像。巨大的臼齿轰然砸下，将金神像碾成了粉末，你下意识地往后跳了一步。当巨齿重新上升时，嘴中不断涌出金币，你赶紧把钱捡了起来。<br>离开你离开了这里，但心里还是有一些好奇。 | `single_source` | [摩艾石像](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408916&wiki_id=646570) |
| `source.title_text` | 摩艾石像 | `single_source` | [摩艾石像](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408916&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=The Moai Head<br>|Image=Event-MoaiHead.png<br>}} {{Small Relic Infobox|Golden Idol}}<br>{{E|The Moai Head}} is an [[Event]] found in [[Act 3]]. It is one of the events affected by {{Asc|15|Ascension}}. It can only be encountered if the player either has {{R|Golden Idol}}, or their HP is at or below 50%.<br><br>== Options ==<br><!-- Fix descriptions to be game-accurate. Use TS colors for positive and negative effects. Put any extra information in indented bullet points... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
