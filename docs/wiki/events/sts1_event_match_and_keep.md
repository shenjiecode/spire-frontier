# 对对碰！ / Match and Keep

> 稳定 ID：`sts1.event.match_and_keep`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：对对碰！
- English: Match and Keep

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "All Acts - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Play |  | {"text": "Play a matching game for cards. Match pairs of cards to add them to your deck. There is always a pair of one Colorless card and one Curse."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Play", "text": "Play a matching game for cards. Match pairs of cards to add them to your deck. There is always a pair of one Colorless card and one Curse."} | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["\" #bTwelve cards! Match them to keep them! #bFive tries, no do-overs. NL Are you ready? Let's start!\"", "You complete the gremlin's game and look up. NL He disappeared?", "A gremlin is madly shuffling cards on a table. This monster seems to be a harmless one. You approach him out of curiosity."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["“ #b十二张牌！ #b搭对就拿走！ 五次机会，没有重来！ NL 准备好了吗？开始！”", "你完成了地精的游戏，当你抬头看时，却发现…… NL 他已经不见了？", "有一位地精正在桌子上疯狂地摆弄着一副牌，他似乎没有危害。你出于好奇接近了他。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Continue]", "[Leave]", "[Play]", "Remaining Attempts: #y"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[继续]", "[离开]", "[玩小游戏]", "剩余次数： #y"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Match and Keep! | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 对对碰！ | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Match and Keep!", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>有一位地精正在桌子上疯狂地摆弄着一副牌，他似乎没有危害。你出于好奇接近了他。十二张牌！搭对就拿走！五次机会，没有重来！准备好了吗？开始！”<br>选项<br>玩小游戏 开始玩对对碰小游戏，有 5 次机会。你完成了地精的游戏，当你抬头看时，却发现……他已经不见了？<br>注意<br>该事件供玩家配对的牌可能有：<br>一对普通牌。（颜色取决于当前职业）<br>一对罕见牌。（颜色取决于当前职业）<br>一对稀有牌。（颜色取决于当前职业）<br>一对随机诅咒。<br>一对罕见无色牌。（进阶15：以一对随机诅咒牌替代。）<br>一对当前职业的基础牌：痛击、中和、电击、暴怒<br>策略<br>如果玩家不想添加任何牌到自己牌组内，那么玩家可以选择两组并不配对的一对牌五次，从而防止添卡。<br>尽管如此，玩家仍可能第一次配对就成功并添加牌至牌组中，不过几率很小。<br>提供的稀有牌通常会对牌组有不小帮助，因此玩家可以尝试着去查看是哪张牌并决定它的去留。 | `single_source` | [对对碰！](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408948&wiki_id=646570) |
| `source.title_text` | 对对碰！ | `single_source` | [对对碰！](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408948&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Match and Keep<br>|Image=Event-MatchAndKeep.png<br>}}<br>{{E|Match and Keep}} is a shrine [[Event]] encountered in all [[Acts]].<br><br>Shrine events appear less frequently than other events.<br><br>== Options ==<br>{{Frame|Play}} <br>* Play a matching game for cards. Match pairs of cards to add them to your deck. There is always a pair of one {{QueryLink|Cards|color:Colorless|Colorless}} card and one {{QueryLink|Cards|type:Curse|Curse}}.<br><br>== Dialogue ==<br><blo... | `single_source` | [P3 wiki.gg API batch: event 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wing_Statue|Duplicator|Match_and_Keep|The_Mausoleum|A_Note_For_Yourself|Sensory_Stone|Hypnotizing_Colored_Mushrooms|Mind_Bloom|We_Meet_Again!|Big_Fish|Ancient_Writing|Shining_Light|Scrap_Ooze|Purifier|The_Ssssserpent|Pleading_Vagrant|World_of_Goop|Lab|Dead_Adventurer|The_Moai_Head&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
