# 心灵绽放 / Mind Bloom

> 稳定 ID：`sts1.event.mind_bloom`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：心灵绽放
- English: Mind Bloom

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 3"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | I am War |  | {"text": "Boss]] from Act 1. Obtain a Rare Relic]. * The boss is selected at random. It can be the same boss that the player actually fought in Act 1], or one of the two that they did not encounter. * In addition to the Boss dropping a Rare Relic], it also drops normal combat rewards and 50 (25) Gold]."} |
| 2 | I am Awake | {"text": "You can no longer heal"} | {"text": "Upgrade] all cards. . * Obtain Mark of the Bloom"} |
| 3 | I am Rich | {"text": "Cursed - 2 Normality"} | {"text": "Gain 999 Gold]. . * This option only appears on floors 35 to 40"} |
| 4 | I am Healthy | {"text": "Cursed - Doubt"} | {"text": "Heal to full HP. . * This option replaces"} |
| 5 | I am Rich |  | {"text": "on floor 41 and above."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "I am War", "text": "Boss]] from Act 1. Obtain a Rare Relic]. * The boss is selected at random. It can be the same boss that the player actually fought in Act 1], or one of the two that they did not encounter. * In addition to the Boss dropping a Rare Relic], it also drops normal combat rewards and 50 (25) Gold]."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "I am Awake", "text": "Upgrade] all cards. You can no longer heal. * Obtain Mark of the Bloom."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "I am Rich", "text": "Gain 999 Gold]. Cursed - 2 Normality. * This option only appears on floors 35 to 40."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "I am Healthy", "text": "Heal to full HP. Cursed - Doubt. * This option replaces"} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.5` | {"label": "I am Rich", "text": "on floor 41 and above."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["While walking and traversing through the chaos of the Spire, your thoughts suddenly begin to feel very... #p~real...~ NL NL Imaginings of #rmonsters and #yriches begin to manifest themselves into reality. NL The sensation is quickly fleeting. What do you do?", "Can it really be this easy?", "Everything makes sense now. NL The lack of memories, the ascent, the #yAncient #yOne. NL NL This is the way it always was. NL This is the way it always will be. NL All will be forgotten again soon..."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你在高塔的混沌深处不断攀行，不知不觉间，你愕然发现自己的思绪开始变得非常…… #p~真实……~ NL NL 各种 #r怪物 与 #y财宝 的影像开始有了实体。 NL 这些感觉稍纵即逝，你准备怎么做？", "真的有这么简单的事吗？", "一切都明白了。 NL 失去的记忆、不断的攀登、那个 #y先古之民 。 NL NL 这是一切事物原本的样子， NL 也是一切事物将有的样子。 NL 很快，这一切又会被再次遗忘……"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[I am War] #rFight #ra #rBoss #rfrom #rAct #r1. #gObtain #ga #gRare #gRelic.", "[I am Rich] #gGain #g999 #gGold. #rCursed #r- #r2 #rNormality.", "[I am Healthy] #gHeal #gto #gfull #gHP. #rCursed #r- #rDoubt.", "[I am Awake] #gUpgrade #gall #gCards. #rYou #rcan #rno #rlonger #rheal.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[我必凯旋] #r与一名第一阶段的 #rBoss #r战斗。 #g获得一件稀有遗物。", "[我将富有] #g获得 #g999 #g金币。 #r被诅咒—— #r2 #r张凡庸。", "[我无伤痛] #g回复所有生命. #r被诅咒——疑虑。", "[我已觉醒] #g升级所有牌。 #r你无法再回复生命。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Mind Bloom | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 心灵绽放 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "MindBloom", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你在高塔的混沌深处不断攀行，不知不觉间，你愕然发现者自己的思绪开始变得非常……真实……各种怪物和财宝的影响开始有了实体。这些感觉稍纵即逝，你准备怎么做？<br>选项<br>我必凯旋 与一名第一阶段的BOSS战斗。获得一件稀有遗物<br>我已觉醒 升级所有牌。你无法再回复生命<br>一切都明白了。失去的记忆、不断地攀登、那个先古之民。这是一切事物原本的样子。也是一切事物将有的样子。很快，这一切又会被再次遗忘。<br>我将富有 获得999金币。被诅咒——2张凡庸<br>真的有这么简单的事吗？<br>我无伤痛 恢复所有生命。被诅咒——疑虑<br>真的有这么简单的事吗？<br>特殊<br>我将富有 选项只会在40层之前遇到 心灵绽放 才会出现，否则其将被替换成 我无伤痛 。<br>我必凯旋 中的稀有遗物并非立刻获得，而是在与BOSS的战斗完成后以掉落物的方式由玩家来拾取。<br>我已觉醒 中“你无法再回复生命”的实际效果为获得绽放印记<br>这会使蜥蜴尾巴和瓶中精灵无法为你回复生命值而失效。<br>这意味着如果你通过某种方式失去绽放印记（如事件恩... | `single_source` | [心灵绽放](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408905&wiki_id=646570) |
| `source.title_text` | 心灵绽放 | `single_source` | [心灵绽放](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408905&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Mind Bloom<br>|Image=Event-MindBloom.png<br>}} {{Small Relic Infobox|Mark of the Bloom}} {{Small Card Infobox|Normality}} {{Small Card Infobox|Doubt}}<br>{{E|Mind Bloom}} is an [[Event]] found exclusively in [[Act 3]]. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|I am War}} {{TS|negative||Fight a [[Bosses#Act 1 Bosses|Boss]] from Act 1.}} {{TS|positive||Obtain a {{QueryLink|Relics|rarity:Rare|Rare}} [[Relic]].}}<br>* The bo... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
