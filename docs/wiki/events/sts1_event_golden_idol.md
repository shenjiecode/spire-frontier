# 金神像 / Golden Idol

> 稳定 ID：`sts1.event.golden_idol`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：金神像
- English: Golden Idol

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Take |  | {"text": "Obtain Golden Idol. Trigger a trap."} |
| 2 | Outrun | {"text": "Become Cursed - Injury"} | {"text": "Become Cursed - Injury."} |
| 3 | Smash |  | {"text": "Take X Damage. * X is equal to 25% (35%) of the player's Max HP."} |
| 4 | Hide | {"text": "Lose X Max HP"} | {"text": "* X is equal to 8% (10%) of the player's Max HP"} |
| 5 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Take", "text": "Obtain Golden Idol. Trigger a trap."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Outrun", "text": "Become Cursed - Injury."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Smash", "text": "Take X Damage. * X is equal to 25% (35%) of the player's Max HP."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Hide", "text": "Lose X Max HP. * X is equal to 8% (10%) of the player's Max HP."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.5` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You come across an inconspicuous pedestal with a #yshining #ygold #yidol sitting peacefully atop. It looks incredibly valuable. NL NL You sure don't see any traps nearby.", "As you grab the Idol and stow it away, a giant boulder smashes through the ceiling into the ground next to you. NL You realize that the floor is slanted downwards as the boulder starts to roll towards you.", "@RUUUUUUUUUUN!@ NL You barely leap into a side passageway as the boulder rushes by. Unfortunately it feels like ... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在一个不引人注意的小高台上，你发现了一个 #y闪闪发光的金神像 安然放置在上面，看起来非常值钱。 NL NL 周围看起来完全没有什么陷阱的样子。", "你拿住金神像放入囊中，突然天花板上一块巨大的圆石掉到了你身边的地上。 NL 石头开始向你滚来，你这才发现地面有一点倾斜。", "@快跑！@ NL 你勉强在石头碾到你之前跳进了旁边的一条小路，不幸的是你似乎扭伤了关节。", "你用尽全力向巨石发起了攻击。尘埃落定之后，你可以寻找安全的出路。", "@咕叽！@ NL 巨石滚过时压到了你一点，但看起来你并没有大碍，可以离开了。", "没有比这更明显的陷阱了吧。 NL 你决定还是不要去碰高台上的东西了。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Take] #gObtain #gGolden #gIdol. #rTrigger #ra #rtrap.", "[Leave]", "[Outrun] #rBecome #rCursed #r- #rInjury.", "[Smash] #rTake #r", " #rDamage.", "[Hide] #rLose #r", " #rMax #rHP."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[拿走] #g获得金神像。 #r触发一个陷阱。", "[离开]", "[逃跑] #r被诅咒——受伤。", "[砸烂] #r受到 #r", " #r点伤害。", "[躲藏] #r失去 #r", " #r最大生命。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Golden Idol | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 金神像 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Golden Idol", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在一个不引人注意的小高台上，你发现了一个闪闪发光的金神像安然放置在上面，看起来非常值钱。周围看起来完全没有什么陷阱的样子。<br>选项<br>拿走 得到金神像。触发一个陷阱。你拿住金神像放入囊中，突然天花板上一块巨大的圆石掉到了你身边的地上。石头开始向你滚来，你这才发现地面有一点倾斜。<br>逃跑 被诅咒——受伤。<br>快跑！你勉强在石头碾到你之前跳进了旁边的一条小路，不幸的是你似乎扭伤了关节。<br>砸烂 失去 25% 生命（进阶15以上为35%）。<br>你用尽全力向巨石发起了攻击。尘埃落定之后，你可以寻找安全的出路。<br>躲藏 失去 8% 最大生命（进阶15以上为10%）。<br>咕叽！巨石滚过时压到了你一点，但看起来你并没有大碍，可以离开了。<br>离开没有比这更明显的陷阱了吧。你决定还是不要去碰高台上的东西了。<br>策略<br>除开金神像本身较为强力的效果，其在第二阶段的被遗忘的祭坛事件中可以避免献祭的巨额的血量损失，或者亵渎获得诅咒的选项，以免对接下来的战斗产生较大影响。<br>选择“躲藏”一般为最优选项，因为“逃跑”获... | `single_source` | [金神像](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375147&wiki_id=646570) |
| `source.title_text` | 金神像 | `single_source` | [金神像](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375147&wiki_id=646570) |
| `source.wikitext` | {{Ambox<br>| color = brown<br>| icon = Necronomicon.png<br>| message = ''This is information about the Event called '''Golden Idol''' in Slay the Spire. For the Golden Shrine event, see [[Golden Shrine]]. For the relic of the same name, see [[Golden Idol (Relic)]].''}}<br>{{Event Infobox<br>|Name=Golden Idol<br>|Image=Event-GoldenIdol.png<br>}} {{Small Relic Infobox|Golden Idol}} {{Small Card Infobox|Injury}}<br>{{E|Golden Idol}} is an [[Event]] found exclusively in [[Act 1]].  It is one of t... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
