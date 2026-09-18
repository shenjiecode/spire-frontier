# 闪耀之光 / Shining Light

> 稳定 ID：`sts1.event.shining_light`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：闪耀之光
- English: Shining Light

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Enter | {"text": "Lose X HP"} | {"text": "Upgrade 2 random cards. . * X is equal to 20% (30%) of the player's max HP"} |
| 2 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Enter", "text": "Upgrade 2 random cards. Lose X HP. * X is equal to 20% (30%) of the player's max HP."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You find a shimmering #ymass #yof #ylight encompassing the center of the room. NL NL Its ~warm~ ~glow~ and ~enchanting~ ~patterns~ invite you in.", "As you walk through the light, you notice that the light is absorbed into you. NL It's #r@scorching@ #r@hot@ ! However, the pain quickly recedes. NL You feel #binvigorated, as though you received a well deserved slap.", "You walk around it, wondering what could have been."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你发现在房间中央围绕着 #y一束很粗的光柱 。 NL NL 光柱上有着 ~温暖而闪烁的美丽花纹~ 仿佛在邀请你进入。", "你走进光柱，注意到光似乎被吸入了你的身体。 NL 这道光 #r@热得发烫@ ！ 可是痛楚很快消失了。 NL 你觉得自己 #b精神焕发 ，就像是在需要被打醒的时候被人好好地抽了一个耳光。", "你绕过光柱，虽然心中仍有些好奇如果走进去会怎么样。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Enter] #gUpgrade #g2 #grandom #gcards. #rLose #r", " #rHP.", "[Leave]", "[Locked] Requires: Upgradeable Cards"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[走进] #g随机升级 #g2 #g张牌。 #r失去 #r", " #r生命。", "[离开]", "[锁定] 需要： 可以升级的牌"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Shining Light | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 闪耀之光 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Shining Light", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你发现在房间中央围绕着一束很粗的光柱 。光柱上有着温暖而闪烁的美丽花纹仿佛在邀请你进入。<br>选项<br>走进 随机升级 2 张牌。失去（20%×最大生命值）的生命（进阶15以上为30%）。 需要：可以升级的牌你走进光柱，注意到光似乎被吸入了你的身体。这道光热得发烫！ 可是痛楚很快消失了。你觉得自己精神焕发，就像是在需要被打醒的时候被人好好地抽了一个耳光。<br>离开你绕过光柱，虽然心中仍有些好奇如果走进去会怎么样。<br>轶事<br>由于在第一阶段，玩家牌组中的打击防御有很多，所以经常会升级到打击防御等初始牌 ，因此该事件也被玩家们称为打击防御之光<br>策略<br>在本事件中可以通过SL（重开：即保存退出-继续游戏）得知强化的卡牌是什么，然后再做选择。但即使升级的是关键牌，也可能会由于消耗的血量较高而导致后面可能遭遇的精英战斗产生不利后果。 | `single_source` | [闪耀之光](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375299&wiki_id=646570) |
| `source.title_text` | 闪耀之光 | `single_source` | [闪耀之光](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375299&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Shining Light<br>|Image=Event-ShiningLight.png<br>}}<br>{{E|Shining Light}} is an [[Event]] encountered exclusively in [[Act 1]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Enter}} {{TS|positive||Upgrade 2 random cards.}} {{TS|negative||Lose X HP.}}<br>* X is equal to 20% {{Asc|15|(30%)}} of the player's max HP.<br><br><br>{{Frame|Leave}} Nothing happens.<br><br>== Dialogue ==<br><blockquote><div style="font-style:italic"... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
