# 大鱼 / Big Fish

> 稳定 ID：`sts1.event.big_fish`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：大鱼
- English: Big Fish

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Banana |  | {"text": "Heal 1/3 of your max HP. * If the player's HP is not divisble by 3, the HP gain is rounded down."} |
| 2 | Donut |  | {"text": "Max HP +5. * Like all HP gain, the extra hit points are healed when you get them."} |
| 3 | Box | {"text": "Become Cursed - Regret"} | {"text": "Obtain a Relic]. . * The Relic is a randomly selected Common, Uncommon, or Rare Relic. You are then given the option to"} |
| 4 | Leave |  | {"text": "."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Banana", "text": "Heal 1/3 of your max HP. * If the player's HP is not divisble by 3, the HP gain is rounded down."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Donut", "text": "Max HP +5. * Like all HP gain, the extra hit points are healed when you get them."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Box", "text": "Obtain a Relic]. Become Cursed - Regret. * The Relic is a randomly selected Common, Uncommon, or Rare Relic. You are then given the option to"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Leave", "text": "."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["As you make your way down a long corridor you see a #ybanana, a #ydonut, and a #ybox ~floating~ about. No... upon closer inspection they are tied to strings coming from holes in the ceiling. There is a quiet @cackling@ from above as you approach the objects. NL What do you do?", "You eat the #ybanana. It is nutritious and slightly #bmagical, healing you.", "You eat the #ydonut. It really hits the spot! Your Max HP increases.", "", "You grab the box. Inside you find a #yrelic!", " NL However... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["当你走过一条长廊时，你看见空中 ~漂浮~ 着 #y一根香蕉 ， #y一个甜甜圈 ， 和 #y一个盒子 。 不……仔细一看，它们都是被用绳子系着，从天花板上的几个洞里悬挂下来的。你在接近这几样东西时，上方似乎传来一阵 @咯咯@ 的笑声。 NL 你会怎么做？", "你吃下了 #y香蕉，它很有营养，似乎还有些 #b魔法 ，回复了你的生命。", "你吃下了 #y甜甜圈 ，真是太好吃了！你的最大生命值增加了。", "", "你抓住了盒子，在里面找到了一个 #y遗物 ！", " NL 可是，你真的很想吃那个甜甜圈…… NL 你的心中充满了 ~悲伤~ ，尤其是一份 #r悔恨 。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Banana] #gHeal #g", " #gHP.", "[Donut] #gMax #gHP #g+", ".", "[Box] #gObtain #ga #gRelic. #rBecome #rCursed #r- #rRegret.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[香蕉]  #g回复  #g", " #g生命。", "[甜甜圈] #g最大生命值 #g+", " #g。", "[盒子] #g获得一件遗物。 #r被诅咒——悔恨。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Big Fish | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 大鱼 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Big Fish", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述当你走过一条长廊时，你看见空中漂浮着一根香蕉，一个甜甜圈，和一个盒子。 不……仔细一看，它们都是被用绳子系着，从天花板上的几个洞里悬挂下来的。你在接近这几样东西时，上方似乎传来一阵咯咯的笑声。<br>选项<br>香蕉 回复最大生命值的1/3。你吃下了香蕉，它很有营养，似乎还有些魔法，回复了你的生命。 备注：如果玩家的最大生命值不能被3整除，那么回复的生命值会向下取整。<br>甜甜圈 最大生命值 +5。<br>你吃下了甜甜圈，真是太好吃了！你的最大生命值增加了。 备注：正如大多数增加最大生命值的效果一样，增加5点最大生命值的同时也会回复5点生命值<br>盒子 获得一件遗物。被诅咒——悔恨。你抓住了盒子，在里面找到了一个遗物！可是，你真的很想吃那个甜甜圈……你的心中充满了悲伤，尤其是一份悔恨。 备注：遗物可以是任意稀有度。错过的遗物可以在下一个精英或给予遗物的事件获得。 | `single_source` | [大鱼](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375121&wiki_id=646570) |
| `source.title_text` | 大鱼 | `single_source` | [大鱼](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375121&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Big Fish<br>|Image=Event-BigFish.png<br>}} {{Small Card Infobox|Regret}}<br>{{E|Big Fish}} is an event found exclusively in [[Act 1]].<br><br>== Options ==<br>{{Frame|Banana}} {{TS|positive||Heal 1/3 of your max HP.}}<br>* If the player's HP is not divisble by 3, the HP gain is rounded down.<br><br><br>{{Frame|Donut}} {{TS|positive||Max HP +5.}}<br>* Like all HP gain, the extra hit points are healed when you get them.<br><br><br>{{Frame|Box}} {{TS|positive||Obtain a [... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
