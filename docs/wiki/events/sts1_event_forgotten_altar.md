# 被遗忘的祭坛 / Forgotten Altar

> 稳定 ID：`sts1.event.forgotten_altar`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：被遗忘的祭坛
- English: Forgotten Altar

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Offer: Golden Idol | {"text": "Lose Golden Idol"} | {"text": "Obtain a special Relic. . * If the player does not have Golden Idol, this option is replaced with"} |
| 2 | Locked |  | {"text": "Requires: Golden Idol."} |
| 3 | Sacrifice | {"text": "Lose X HP"} | {"text": "Gain 5 Max HP. . * X is equal to 25% (35%) of the player's Max HP"} |
| 4 | Desecrate | {"text": "Become Cursed -Decay"} | {"text": "* Decay - Unplayable. At the end of your turn, take 2 damage"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Offer: Golden Idol", "text": "Obtain a special Relic. Lose Golden Idol. * If the player does not have Golden Idol, this option is replaced with"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Locked", "text": "Requires: Golden Idol."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Sacrifice", "text": "Gain 5 Max HP. Lose X HP. * X is equal to 25% (35%) of the player's Max HP."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Desecrate", "text": "Become Cursed -Decay. * Decay - Unplayable. At the end of your turn, take 2 damage."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["In front of you sits an altar to a forgotten god. NL Atop the altar sits an ornate female statue with arms outstretched. NL She calls out to you, demanding sacrifice.", "As you gently set the idol onto the altar a #bcold wind swirls throughout the room. NL The arms of the statue begin to discolor and crumble. NL NL Your #ygolden #yidol begins to dull in color and begins bleeding from its eyes. NL The bleeding never ceases.", "You stand on the altar and cut your wrists. NL As the #rblood spi... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在你面前是一个早已被遗忘的神祇的祭坛。 NL 在祭坛上方，是一尊双手伸出的精致女性雕像。 NL 她呼唤着你，要求你献上祭品。", "你小心翼翼地将金神像放到了祭坛上，一阵 #b寒风 瞬间吹过了房间。 NL 雕像的双手开始失去颜色并逐渐崩塌。 NL NL 你的 #y金神像 开始变暗，然后双眼开始流出血液。 NL 血始终也没有停止流下。", "你站在祭坛前，割开了你自己的手腕。 NL 随着 #r鲜血 涌到祭坛上，雕像的双手伸到你的面前遮住了你的双眼。 NL 一切坠入黑暗。 NL 你在一段时间后苏醒了过来，感觉自己体内有了新的潜力。", "你使劲开始砸面前的雕像，终于打破了这个房间对你施加的魔力。 NL 四周回荡起一声黑暗的恸哭，你能感觉到 #p~诅咒的魔法~ 渗入了你的骨髓。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Offer: Golden Idol] #gObtain #ga #gspecial #gRelic. #rLose #rGolden #rIdol.", "[Locked] Requires: Golden Idol.", "[Sacrifice] #gGain #g", " #gMax #gHP. #rLose #r", " #rHP.", "[Locked] Requires: Humanity.", "[Desecrate] #rBecome #rCursed #r- #rDecay."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[献上：金神像] #g获得一件特别的遗物。 #r失去金神像。", "[锁定] 需要：金神像。", "[献祭] #g获得 ", " #g点最大生命。 #r失去 #r", " #r点生命。", "[锁定] 需要：是人类。", "[亵渎] #r被诅咒——腐朽。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Forgotten Altar | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 被遗忘的祭坛 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Forgotten Altar", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在你面前是一个早已被遗忘的神祇的祭坛。在祭坛上方，是一尊双手伸出的精致女性雕像。她呼唤着你，要求你献上祭品。<br>选项<br>献上：金神像 得到一件特别的遗物。失去金神像。 需要：金神像。你小心翼翼地将金神像放到了祭坛上，一阵寒风瞬间吹过了房间。雕像的双手开始失去颜色并逐渐崩塌。你的金神像开始变暗，然后双眼开始流出血液。血始终也没有停止流下。<br>献祭 获得 5 点最大生命。失去 25%（进阶15以上为35%） 生命。你站在祭坛前，割开了你自己的手腕。随着鲜血涌到祭坛上，雕像的双手伸到你的面前遮住了你的双眼。一切坠入黑暗。你在一段时间后苏醒了过来，感觉自己体内有了新的潜力。<br>亵渎 被诅咒——腐朽。你使劲开始砸面前的雕像，终于打破了这个房间对你施加的魔力。四周回荡起一声黑暗的恸哭，你能感觉到诅咒的魔法渗入了你的骨髓。<br>策略<br>一般来说，第二层前期的战斗都会比较艰难，而若没有金神像，在这个时期遇到该事件会使情况进一步恶化。相比之下，鲜血神像能提供很不错的续航能力。因此，建议玩家在第一层遇到金神像时选择拿走。<br>轶事<b... | `single_source` | [被遗忘的祭坛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408880&wiki_id=646570) |
| `source.title_text` | 被遗忘的祭坛 | `single_source` | [被遗忘的祭坛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408880&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Forgotten Altar<br>|Image=Event-ForgottenAltar.png<br>}} {{Small Relic Infobox|Bloody Idol}} {{Small Card Infobox|Decay}}<br>{{E|Forgotten Altar}} is an [[Event]] found exclusively in [[Act 2]]. This Event is the only way to obtain {{R|Bloody Idol}}. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Offer: Golden Idol}} {{TS|positive||Obtain a special}} {{R|Bloody Idol|Relic}}{{TS|positive||.}} {{TS|negative||Lose}} {{R|Golden I... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
