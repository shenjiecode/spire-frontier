# 竞技场 / The Colosseum

> 稳定 ID：`sts1.event.the_colosseum`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：竞技场
- English: The Colosseum

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Fight |  | {"text": "The player enters a fight with a Blue Slaver and Red Slaver. This fight gives no rewards. After the fight ends, a choice has to be made:"} |
| 2 | COWARDICE |  | {"text": "Escape."} |
| 3 | VICTORY |  | {"text": "A powerful fight with many rewards. * The player enters a fight with Taskmaster and Gremlin Nob. * The rewards are 100 Gold], 1 Rare Relic], 1 Uncommon Relic], a card reward, and sometimes a Potion]."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Fight", "text": "The player enters a fight with a Blue Slaver and Red Slaver. This fight gives no rewards. After the fight ends, a choice has to be made:"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "COWARDICE", "text": "Escape."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "VICTORY", "text": "A powerful fight with many rewards. * The player enters a fight with Taskmaster and Gremlin Nob. * The rewards are 100 Gold], 1 Rare Relic], 1 Uncommon Relic], a card reward, and sometimes a Potion]."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["@Thwack!!!@ NL .. NL ...... NL ... NL ~You~ ~were~ ~knocked~ ~unconscious...~", "~Groggy~ and with a @throbbing@ head, you awaken to find yourself thrown in the center of a massive stadium with an overflowing audience of #bSlavers, #pCultists, and other denizens of the City! NL ", " NL An armored giant with a #ygolden #ycrown bellows at you from atop, NL @\"WE@ @NOW@ @BEGIN@ @THE@ @", "TH@ @COMBAT!!!!\"@ NL A gate on the opposite side opens...", "@\"WELL@ @DONE,@ @WEAKLING!\"@ NL The giant ... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["@哐！！！@ NL … NL ……… NL …… NL ~你被~ ~打晕了~ ~……~", "你悠悠醒转， 脑袋还 @疼得厉害@ ，脚也 ~站不太稳~ 。你发现自己正处于一座巨大竞技场的中央，观众席上挤满了 #b奴隶贩子 、 #p邪教徒 和城市区的其他居民们！ NL ", " NL 一个头戴 #y金冠 的重甲巨人伫立在上方，他对你咆哮： NL @“那么现在，就让我们开始第@ @", "@ @轮战斗！！！！”@ NL 在你对面的那道大门缓缓打开了……", "@“打得不错，弱者啊！”@ NL 那名巨人假装鼓了鼓掌，用夸张的手势开始鼓动起观众们。 NL #y~金币~ ~和~ #y~彩纸~ ~从天而降~ ~撒落在你身旁！~ NL @“接下来才是真正的挑战！！”@ NL NL 上一场战斗在竞技场的围墙上留下了一个小小缺口，你完全有机会在众人们没留意时从那里逃出去。 NL 你想要留下来继续战斗吗？"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Continue]", "[Fight]", "[COWARDICE] Escape.", "[VICTORY] A powerful fight with many rewards."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[继续]", "[战斗]", "[怂了] 逃跑。", "[战斗到底] 进行一场艰难的战斗，赢得众多奖赏。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | The Colosseum | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 竞技场 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Colosseum", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>哐！！！…………………你被打晕了……你悠悠醒转，脑袋还疼得厉害，脚也站不太稳，你发现自己正处于一座巨大竞技场的中央，观众席上挤满了奴隶贩子、邪教徒和城市区的其它居民们！一个头戴金冠的重甲巨人伫立在上方，他对你咆哮：“那么现在，就让我们开始第4200轮战斗！！！！”在你对面的大门缓缓打开了……<br>（强制开始第一场战斗，敌方为蓝奴隶主和红奴隶主各一。）<br>（战斗结束后：）<br>“打得不错，弱者啊！”那名巨人假装鼓了鼓掌，用夸张的手势开始鼓动起观众们。金币和彩纸从天而降洒落在你身旁！“接下来才是真正的挑战！！”上一场战斗在竞技场的围墙上留下了一个小小的缺口，你完全有机会在众人们没留意时从那里逃出去你想要留下来继续战斗吗？<br>选项<br>怂了 逃跑（避免下一场战斗） 备注：（调出地图界面，继续行进）<br>继续 开始一场艰难的战斗，赢得众多奖赏 备注：（与奴隶头子和地精大块头进行战斗，胜利后获得100金币，一个随机稀有遗物，一个随机罕见遗物和一组卡牌） | `single_source` | [竞技场](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389476&wiki_id=646570) |
| `source.title_text` | 竞技场 | `single_source` | [竞技场](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389476&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=The Colosseum<br>|Image=Event-Colosseum.png<br>}}<br>{{E|The Colosseum}} is an [[Event]] found exclusively in [[Act 2]]. It is one of the events affected by {{Asc|15|Ascension}}. It only appears after the guaranteed [[Map Locations#Treasure Room|Treasure Room]] on the 6th floor of the City.<br><br>== Options ==<br>{{Frame|Fight}}<br>* The player enters a fight with a {{M|Blue Slaver}} and {{M|Red Slaver}}. This fight gives no rewards.<br><blockquote><br>After the figh... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
