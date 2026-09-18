# 我们又见面了！ / We Meet Again!

> 稳定 ID：`sts1.event.we_meet_again`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：我们又见面了！
- English: We Meet Again!

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | ? |
| `appearance_condition_json` | {"source": "article", "status": "needs_cross-check"} |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | 给他药水 | {"cost": "one_random_potion", "locked_if": "no_potion"} | {"reward": "one_random_relic"} |
| 1 | Give Potion | {"text": "Lose a chosen potion"} | {"text": "Obtain a Relic. * The event will randomly choose a potion upon entry and tell you which one was selected. You will be unable to drink or discard that potion until you leave the event's floor"} |
| 2 | 给他金币 | {"cost": "X_gold_between_50_and_current", "locked_if": "gold_less_than_50"} | {"reward": "one_random_relic"} |
| 2 | Give Gold | {"text": "Lose Gold"} | {"text": "Obtain a Relic. * The amount of Gold] lost is between 50 and 150 (or your current amount of Gold])"} |
| 3 | 给他卡牌 | {"cost": "one_random_non_basic_non_curse_card", "locked_if": "deck_has_no_eligible_card"} | {"reward": "one_random_relic"} |
| 3 | Give Card | {"text": "Lose a chosen card"} | {"text": "Obtain a Relic. * The chosen card will not be Basic or a Curse"} |
| 4 | 攻击 | {"cost": null} | {"result": "leave_without_combat"} |
| 4 | Attack |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Give Potion", "text": "Lose a chosen potion. Obtain a Relic. * The event will randomly choose a potion upon entry and tell you which one was selected. You will be unable to drink or discard that potion until you leave the event's floor."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Give Gold", "text": "Lose Gold. Obtain a Relic. * The amount of Gold] lost is between 50 and 150 (or your current amount of Gold])."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Give Card", "text": "Lose a chosen card. Obtain a Relic. * The chosen card will not be Basic or a Curse."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Attack", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["\"We meet again!\" NL A cheery disheveled fellow approaches you gleefully. You do not know this man. NL NL \"It's me, #yRanwid! Have any goods for me today? The usual? A fella like me can't make it alone, you know?\" NL You eye him suspiciously and consider your options...", "\"Exquisite! Was feeling parched.\" NL #b~Glup~ #b~glup~ #b~glup~ NL NL He downs the potion in one go and lets out a satisfied @burp.@", "\"Magnificent! This will be quite handy if I run into those #rmask #rwearing #rh... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["“我们又见面了！” NL 一个蓬头垢面的男子欢快地出现在你面前向你问好。你不认识这个男人。 NL NL “是我， #y兰伟德 啊！所以今天有什么好东西给我吗？和往常一样？哎呀呀，像我这样的人，独自一个可实在不好混啊，对不对？” NL 你满腹狐疑地打量着他，开始思考应该怎么做……", "“太好了！我正口渴呢。” NL #b~咕嘟~ #b~咕嘟~ #b~咕嘟~ NL NL 他一口气喝完了药水，满意地打了一个 @饱嗝@ 。", "“太棒了！之后要是再遇见那些 #r戴面具的流氓 ，这一定会很有用的。”", "“有意思！我会回去好好研究的。”", "“ @啊！！@ 哎呀你这人有时真是老混蛋了！” NL 他飞快地跑开了。", "  NL NL 他在自己身上的众多口袋里摸索了半天…… NL “看我今天为你准备了什么！给你给你！”"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Give Potion] #rLose ", "[Locked] Requires: Potion.", "[Give Gold] #rLose #r", "[Locked] Requires: At least 50 Gold.", "[Give Card] #rLose ", "[Locked] Requires: Card.", ". #gObtain #ga #gRelic.", "[Attack]", "[Leave]", " #rGold"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[给他药水] #r失去 ", "[锁定] 需要：药水。", "[给他金币] #r失去 #r", "[锁定] 需要：至少50金币。", "[给他卡牌] #r失去 ", "[锁定] 需要：卡牌。", "。 #g获得一件遗物。", "[攻击]", "[离开]", " #r金币"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | We Meet Again! | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 我们又见面了！ | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "WeMeetAgain", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_excerpt.en` | We Meet Again! We Meet Again! is a shrine Event found in all Acts. Shrine events appear less frequently than other events. Options[edit | edit source] [Give Potion] Lose a chosen potion. Obtain a Relic. The event will randomly choose a potion upon entry and tell you which one was selected. You will be unable to drink or discard that potion until you leave the event's floor. [Give Gold] Lose Gold. Obtain a Relic. The amount of Gold lost is between 50 and 150 (or your current amount of Gold). [... | `single_source` | [We Meet Again! | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/We_Meet_Again!) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>“我们又见面了！”一个蓬头垢面的男子欢快地出现在你面前向你问好，你不认识这个男人。“是我，兰伟德啊！所以今天有什么好东西给我吗？和往常一样？哎呀呀，像我这样的人，独自一个可实在不好混啊，对不对？”你满腹狐疑地打量着他，开始思考应该怎么做……<br>选项<br>给他药水 失去X药水。获得一件遗物。<br>“太好了！我正口渴呢。”咕嘟咕嘟咕嘟他一口气喝完了药水，满意地打了个饱嗝。他在自己身上的众多口袋摸索了半天……“看我今天为你准备了什么！给你给你！”<br>给他金币 失去X金币。获得一件遗物<br>“太棒了！之后要是再遇见那些戴面具的流氓，这一定会很有用的。”他在自己身上的众多口袋摸索了半天……“看我今天为你准备了什么！给你给你！”<br>给他卡牌 失去X卡牌。获得一件遗物“有意思！我会回去好好研究的”他在自己身上的众多口袋摸索了半天……“看我今天为你准备了什么！给你给你！”<br>攻击 调出地图界面，继续行进“啊！！哎呀你这人有时真是老混蛋了！”他飞快地跑开了。<br>注意<br>“给他药水”选项将会从玩家的药水槽位中预先随机选择一个药水... | `single_source` | [我们又见面了！](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408930&wiki_id=646570) |
| `source.title_text` | （图片未提供文字说明） | `single_source` | [我们又见面了！](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408930&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=We Meet Again!<br>|Image=Event-WeMeetAgain.png<br>}}<br>{{E|We Meet Again!}} is a shrine [[Event]] found in all [[Acts]].<br><br>Shrine events appear less frequently than other events.<br><br>== Options ==<br>{{Frame|Give Potion}} {{TS|negative||Lose a chosen potion.}} {{TS|positive||Obtain a Relic.}}<br>* The event will randomly choose a potion upon entry and tell you which one was selected. You will be unable to drink or discard that potion until you leave the event... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
