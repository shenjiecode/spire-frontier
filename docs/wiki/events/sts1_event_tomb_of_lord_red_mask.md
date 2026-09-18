# 红面具大人之墓 / Tomb of Lord Red Mask

> 稳定 ID：`sts1.event.tomb_of_lord_red_mask`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：红面具大人之墓
- English: Tomb of Lord Red Mask

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 3"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Don the Red Mask |  | {"text": "Gain 222 Gold]. * The player gets to keep Red Mask afterwards. The Gold] is purely a reward for owning the relic."} |
| 2 | Leave |  | {"text": "Nothing happens. === If The Player Does Not Own Red Mask ==="} |
| 3 | Locked |  | {"text": "Requires: Red Mask"} |
| 4 | Offer: X Gold | {"text": "Lose all Gold]"} | {"text": "Obtain a Relic. * X is equal to all of the player's Gold]. * Rewards the player with Red Mask"} |
| 5 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Don the Red Mask", "text": "Gain 222 Gold]. * The player gets to keep Red Mask afterwards. The Gold] is purely a reward for owning the relic."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Leave", "text": "Nothing happens. === If The Player Does Not Own Red Mask ==="} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Locked", "text": "Requires: Red Mask"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Offer: X Gold", "text": "Obtain a Relic. * X is equal to all of the player's Gold]. * Rewards the player with Red Mask"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.5` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["A highly ornamented tomb can be seen on the other side of a floating path. Upon reaching the tomb, you notice a slot for #ygold coins with a scratched out inscription above it.", "You don the mask and the tomb starts to ~flake~ ~away...~ a secret passage! NL NL The passage is lined with countless stolen goods and mounds of #ygold!", "An opening appears in the tomb and out slides a small red mask with a note attached. \"Take from others as I have taken from you!\""] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在一条悬浮道路的尽头，你可以看见一处装饰华丽的古墓，当你到达古墓时，你看到有一个可以投放 #y金币 的开口，但上面的铭文已经被划得看不清楚了。", "你戴上面具，古墓似乎开始逐渐 ~剥离~ ……是一条密道！ NL NL 密道中有着数不清的偷来的财宝与大量的 #y金币 ！", "古墓上出现一个开口，一个小小的红面具滑了出来，旁边还有一张纸条：“如同我夺走你的东西一般，去抢夺别人的东西吧！”"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Don the Red Mask] #gGain #g222 #gGold.", "[Locked] Requires: Red Mask.", "[Offer: ", " Gold] #rLose #rall #rGold. #gObtain #ga #gRelic.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[戴上红面具] #g获得 #g222 #g金币。", "[锁定] 需要： 红面具。", "[献上: ", " 金币] #r失去所有金币。 #g获得遗物。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Tomb of Lord Red Mask | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 红面具大人之墓 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Tomb of Lord Red Mask", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在一条悬浮道路的尽头，你可以看见一处装饰华丽的古墓，当你到达古墓时，你看到有一个可以投放金币的开口，但上面的铭文已经被划得看不清楚了。<br>选项<br>戴上红面具 获得 222 金币。 需要：红面具。你戴上面具，古墓似乎开始逐渐剥离……是一条密道！密道中有着数不清的偷来的财宝与大量的金币！<br>献上：所有金币 失去所有金币。获得遗物-红面具。古墓上出现一个开口，一个小小的红面具滑了出来，旁边还有一张纸条：“如同我夺走你的东西一般，去抢夺别人的东西吧！”<br>离开<br>轶事<br>事件蒙面强盗中的强盗三人组可能在红面具大人之墓献上过金币，因为他们都戴着红面具并且和该事件一样要求玩家失去所有金币（与纸条上的字相符） | `single_source` | [红面具大人之墓](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408922&wiki_id=646570) |
| `source.title_text` | 红面具大人之墓 | `single_source` | [红面具大人之墓](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408922&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Tomb of Lord Red Mask<br>|Image=Event-RedMaskTomb.png<br>}} {{Small Relic Infobox|Red Mask}}<br>{{E|Tomb of Lord Red Mask}} is an [[Event]] found in [[Act 3]].<br><br>== Options ==<br>=== If The Player Owns {{R|Red Mask}} ===<br>{{Frame|Don the Red Mask}} {{TS|positive||Gain 222 [[Gold]].}}<br>* The player gets to keep {{R|Red Mask}} afterwards. The [[Gold]] is purely a reward for owning the relic.<br><br>{{Frame|Leave}} Nothing happens. <br><br><br><br><br><br>=== If... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
