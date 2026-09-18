# 换脸商 / Face Trader

> 稳定 ID：`sts1.event.face_trader`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：换脸商
- English: Face Trader

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 1 , Act 2 - Shrine"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Touch | {"text": "Lose X HP, gain 75 (50) Gold]"} | {"text": "* X is equal to 10% of the player's Max HP, rounded down"} |
| 2 | Trade |  | {"text": "50%: Good Face. 50%: Bad Face. * Receive one of the following special Relics]: ** Face of Cleric (good face) ** Ssserpent Head (good face) ** Gremlin Visage (bad face) ** N'loth's Hungry Face (bad face) ** Cultist Headpiece (neutral face)"} |
| 3 | Leave |  | {"text": "Nothing happens."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Touch", "text": "Lose X HP, gain 75 (50) Gold]. * X is equal to 10% of the player's Max HP, rounded down."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Trade", "text": "50%: Good Face. 50%: Bad Face. * Receive one of the following special Relics]: ** Face of Cleric (good face) ** Ssserpent Head (good face) ** Gremlin Visage (bad face) ** N'loth's Hungry Face (bad face) ** Cultist Headpiece (neutral face)"} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Leave", "text": "Nothing happens."} | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["You walk by an eerie statue holding several masks... NL Something behind you softly whispers, NL ~\"Stop.\"~", "You swerve around to face the statue which is now facing you! NL On closer inspection, it's not a statue but a statuesque, gaunt man. Is he even breathing? NL NL ~\"Face.~ ~Let~ ~me~ ~touch?~ ~Maybe~ ~trade?\"~", "~\"Compensation?~ ~Compensation.\"~ NL Mechanically, he cranes out a neat stack of #ygold and places it into your pouch. NL NL ~\"What~ ~a~ ~nice~ ~face.~ ~Nice~ ~face.\... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["你经过一尊举着许多不同的面具的奇怪雕像，但没走几步…… NL 你就听见身后传来一个轻柔的声音： NL ~“请留步。”~", "你回了回头，却发现那尊雕像也已经转向了你！ NL 仔细一看，原来这并不是一尊雕像，只是一个肤色如同雕像的消瘦男人……他是不是根本没有在呼吸？ NL NL ~“你的脸。~ ~让我碰碰？~ ~或者，想要交易？”~", "~“补偿吗？~ ~当然了。”~ NL 他动作机械地伸出手，将一叠 #y金币 放进了你的钱袋里。 NL NL ~“真是张好脸。~ ~啊啊，多好的脸。”~ NL 当他触碰你的脸颊时，你觉得自己的生命好像正在流失！ NL 突然之间，只见他戴着的面具掉落了下来在地上摔得粉碎。他立即尖叫起来，六只手飞快地捂住了自己的脸，这下那些面具全都摔落下来了！在这凄厉的尖叫与众多面具粉碎的声音中，你赶紧逃离了这里。 NL NL 你在不经意间瞥到了他面具下的样子：他的脸是一片完全的空白。", "~“和我？~ @和我吗？@ ~啊，当然了……~ ~可以。~ ~可以……~ ~唔嗯……”~ NL NL 你看见他的一根手臂抖动了一下，突然你的脸出现在了他的手里！似乎你的脸和... | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Touch] #rLose #r", " #gGold.", "[Trade] #g50%: #gGood #gFace. #r50%: #rBad #rFace.", "[Leave]", "[Continue]", " #rHP, #ggain #g"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[触碰] #r失去", " #g金币。", "[交易] #g50%：获得好脸。 #r50%：获得坏脸。", "[离开]", "[继续]", " #r生命， #g获得 #g"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Face Trader | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 换脸商 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "FaceTrader", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | 换脸商是会发生在第一阶段或第二阶段的事件。<br>描述<br>你经过一尊举着许多不同面具的奇怪雕像，但没走几步……你就听见身后传来一个轻柔的声音：“请留步。”你回了回头，却发现那尊雕像也已经转向了你！仔细一看，原来这并不是一尊雕像，只是一个肤色如同雕像的消瘦男人……他是不是根本没有在呼吸？“你的脸，让我碰碰？或者，想要交易？”<br>选项<br>触碰 失去10%最大生命值的生命，获得75（进阶15：50）金币<br>“补偿吗？当然了”他动作机械地伸出手来，将一叠金币放进了你的钱袋里。“真是张好脸，啊啊，多好的脸。”当他触碰你的脸颊时，你觉得自己的生命好像正在流失！突然之间，只见他带着的面具掉落了下来在地上摔得粉碎，他立即尖叫起来，六只手飞快地捂住了自己的脸，这下那些面具全都摔落下来了！在这凄厉的尖叫和众多面具粉碎的声音中，你赶紧逃离了这里。你在不经意间瞥到了他面具下的样子：他的脸是一片空白。<br>交易 50%获得好脸；50%获得坏脸。<br>“和我？和我吗？啊，当然了……可以。可以……唔嗯……”你看见他的一根手臂抖动了一下，突然你的脸出现在了他的手里！似乎你的脸和那个面具交换了... | `single_source` | [换脸商](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389469&wiki_id=646570) |
| `source.title_text` | 换脸商 | `single_source` | [换脸商](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389469&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Face Trader<br>|Image=Event-FaceTrader.png<br>}}<br>{{E|Face Trader}} is a {{QueryLink|Events|shrine:Yes|shrine Event}} found in  [[Act 1]] and [[Act 2]]. This Event is the only way to obtain {{R|Cultist Headpiece}}, {{R|Face of Cleric}}, {{R|Gremlin Visage}}, {{R|N'loth's Hungry Face}}, and {{R|Ssserpent Head}}. It is one of the events affected by {{Asc|15|Ascension}}.<br><br>== Options ==<br>{{Frame|Touch}} {{TS|negative||Lose X HP,}} {{TS|positive||gain 75 {{Asc|15... | `single_source` | [P3 wiki.gg API batch: event 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Cursed_Tome|Living_Wall|Face_Trader|Winding_Halls|N'loth|The_Cleric|Masked_Bandits|Knowing_Skull|Mysterious_Sphere|Wheel_of_Change|Ominous_Forge&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
