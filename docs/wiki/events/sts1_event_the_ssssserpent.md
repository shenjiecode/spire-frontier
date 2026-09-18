# 蛇 / The Ssssserpent

> 稳定 ID：`sts1.event.the_ssssserpent`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：蛇
- English: The Ssssserpent

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Agree | {"text": "Become Cursed - Doubt"} | {"text": "Gain 175 (150) Gold"} |
| 2 | Disagree |  | {"text": "Nothing happens. You are then given the option to"} |
| 3 | Leave |  | {"text": "."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Agree", "text": "Gain 175 (150) Gold"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Disagree", "text": "Nothing happens. You are then given the option to"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You walk into a room to find a large hole in the ground. As you approach the hole, an enormous serpent creature appears from within. NL NL ~\"Ho~ ~hooo!~ ~Hello~ ~hello!~ ~what~ ~have~ ~we~ ~got~ ~here?~ Hello adventurer, I ask a simple question. NL The most fulfilling of lives is that in which you can #y~buy~ #y~anything!~ NL Do you agree?\"", "~\"Yeeeeeeessssssssssessss!~ NL ~Thisss~ ~will~ ~all~ ~be~ ~worthhh~ ~it.~ NL ~..ssSSs.....~ ~ss...~ ~sssss....!\"~", "The serpent stares at you wi... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你走进一间房间，看见地上有一个大洞。当你靠近洞时，一条巨大的蛇形生物从里面钻了出来。 NL NL “~嚯嚯嚯！你好，你好啊！这是谁呀？~ 哎呀呀，你好冒险者，我就问一个简单的问题。 NL 最幸福的人生当然就是 #y~什么东西都能买得起~ 的土豪生活了！　 NL 你同意吗？”", "~“对～！~ NL ~这会很值～得的。~ NL ~嘶……嘶～嘶……”~", "蛇非常失望地看着你。", "蛇抬起头，往上喷出了一堆 #y金币 ！ NL 这令人震惊又有点可怕。 NL 你把 #y金币 收好，谢过蛇后，重新上路。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Agree] #gGain #g", " #gGold. #rBecome #rCursed #r- #rDoubt.", "[Disagree]", "[Continue]", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[同意] #g获得 #g", " #g金币。 #r被诅咒——疑虑。", "[反对]", "[继续]", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Ssssserpent | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 蛇～ | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Liars Game", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你走进一间房间，看见地上有一个大洞。当你靠近洞时，一条巨大的蛇形生物从里面钻了出来。“嚯嚯嚯！你好，你好啊！这是谁呀？哎呀呀，你好冒险者，我就问一个简单的问题。最幸福的人生当然就是什么东西都能买得起的土豪生活了！　你同意吗？”<br>选项<br>同意 得到 175 (进阶15以上为150) 金币。被诅咒——疑虑。“对～！这会很值～得的。嘶……嘶～嘶……”蛇抬起头，往上喷出了一堆金币！这令人震惊又有点可怕。你把金币收好，谢过蛇后，重新上路。<br>反对蛇非常失望地看着你。<br>策略<br>由于该事件仅于第一阶段出现，故其给予的诅咒疑虑将会在卡组频繁地循环，在面临精英等强力敌人时将极为不利。此外，进阶15以后其给予的金币将更少，此时占用一次删牌机会并不划算，所以大多数情况下不建议选择同意。<br>轶事<br>该事件的游戏内部名称为"Liars game"（谎言游戏，一部日本漫画），这很可能是给予的诅咒为疑虑的原因。（图片未提供文字说明） | `single_source` | [蛇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375278&wiki_id=646570) |
| `source.title_text` | 蛇 | `single_source` | [蛇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375278&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=The Ssssserpent<br>|Image=Event-Serpent.png<br>}} {{Small Card Infobox|Doubt}}<br>{{E|The Ssssserpent}} is an [[Event]] encountered exclusively in [[Act 1]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Agree}} {{TS|positive||Gain 175}} {{Asc|15|(150)}} {{TS|positive||Gold.}} {{TS|negative||Become Cursed -}} {{C|Doubt}}{{TS|negative||.}}<br><br><br><br>{{Frame|Disagree}} Nothing happens.<br><br><br><br>You are then given th... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
