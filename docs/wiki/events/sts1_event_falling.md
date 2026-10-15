# 坠落 / Falling

> 稳定 ID：`sts1.event.falling`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：坠落
- English: Falling

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 3"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Land | {"text": "Lose (a random Skill) * Cannot be a Skill targeted by Bottled Lightning"} | {"text": "Lose (a random Skill) * Cannot be a Skill targeted by Bottled Lightning."} |
| 2 | Channel | {"text": "Lose (a random Power) * Cannot be a Power targeted by Bottled Tornado"} | {"text": "Lose (a random Power) * Cannot be a Power targeted by Bottled Tornado."} |
| 3 | Strike | {"text": "Lose (a random Attack) * Cannot be an Attack targeted by Bottled Flame"} | {"text": "If the player somehow manages to lack even a single eligible card (e.g. they have a very small deck containing only bottled cards), then the only option listed is a special Land option that has no description"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Land", "text": "Lose (a random Skill) * Cannot be a Skill targeted by Bottled Lightning."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Channel", "text": "Lose (a random Power) * Cannot be a Power targeted by Bottled Tornado."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Strike", "text": "If the player somehow manages to lack even a single eligible card (e.g. they have a very small deck containing only bottled cards), then the only option listed is a special Land option that has no description"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["As you head upwards hopping from one floating shape to another, you slip. NL NL You begin to fall.", "While in free fall you consider your options: NL Land safely with your greatest techniques. NL Channel a Power to survive the fall. NL Strike at the wall to hang on to it.", "You land with extreme grace before continuing on.", "Harnessing and expending some of your raw power, you manage to land unhurt.", "You are able to latch on to the wall, and manage to make a short hop onto another stab... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你在悬浮在空中的平台上往上跳跃时，不慎滑了一跤。 NL NL 你开始坠落。", "在摔下的途中，你开始考虑自己有什么选择： NL 用你最好的技术安全落地。 NL 释放能力牌的力量来抵御伤害。 NL 对墙壁猛击，让自己不再下坠。", "你以优雅的姿势落地，继续前行。", "你催动自己的力量，成功在落地时避免了损伤。", "你成功挂在了墙上，一个小跳翻上了一个稳固的平台。", "你有如羽毛一般缓缓降落，安然无恙地落了地。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Continue]", "[Land] #rLose ", "[Locked] Requires: Skill Card", "[Channel] #rLose ", "[Locked] Requires: Power Card", "[Strike] #rLose ", "[Locked] Requires: Attack Card", "[Leave]", "[Land] "] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[继续]", "[落地] #r失去 ", "[锁定] 需要： 技能牌", "[释放] #r失去 ", "[锁定] 需要： 能力牌", "[猛击] #r失去 ", "[锁定] 需要： 攻击牌", "[离开]", "[落地] "] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Falling | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 坠落 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Falling", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>你在悬浮在空中的平台上往上跳跃时，不慎滑了一跤。你开始坠落。<br>在摔下的途中，你开始考虑自己有什么选择：用你最好的技术安全落地。释放能力牌的力量来抵御伤害。对墙壁猛击，让自己不再下坠。<br>选项<br>落地 失去随机一张技能牌 需要：技能牌你以优雅的姿势落地，继续前行。<br>释放 失去随机一张能力牌 需要：能力牌你催动自己的力量，成功在落地时避免了损伤。<br>猛击 失去随机一张攻击牌 需要：攻击牌你成功挂在了墙上，一个小跳翻上了一个稳固的平台。<br>特殊选项<br>假如你没有任何一张可以移除的牌，则将只有以下一个选项。<br>落地<br>你犹如羽毛一般缓缓降落，安然无恙地落了地。 | `single_source` | [坠落](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408914&wiki_id=646570) |
| `source.title_text` | 坠落 | `single_source` | [坠落](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408914&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Falling<br>|Image=Event-Falling.png<br>}}<br>{{E|Falling}} is an [[Event]] found exclusively in [[Act 3]]. <br><br>== Options ==<br>All options will randomly choose a card in the player's deck of a particular type. The option's text will explicitly tell the player which card they would lose. If the player lacks a card of a particular type, then the option relating to that type will be locked (e.g. if the player has no {{QueryLink|Cards|type:Power|Powers}} for the {{Fr... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
