# 带壳寄生怪 / Shelled Parasite

> 稳定 ID：`sts1.monster.shelled_parasite`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：带壳寄生怪
- English: Shelled Parasite

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 2 |
| `hp_min` | 68 |
| `hp_max` | 68 |
| `ascension_json` | {"asc_hp": 70} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Double Strike | Attack3 | 6 |  | {"text": "Deals (6×2;7×2) damage."} |
| Stunned | Stunned |  |  | {"text": "Does nothing."} |
| Fell | DebuffAttack4 | 18 |  | {"text": "Deals (18;21) damage. Applies 2 Frail."} |
| Life Suck | BuffAttack3 | 10 |  | {"text": "Deals (10;12) damage. Heals HP equal to unblocked damage dealt."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Shelled Parasite | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 带壳寄生怪 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Shelled Parasite", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Double Strike` | {"effect": "Deals (6×2;7×2) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Fell` | {"effect": "Deals (18;21) damage. Applies 2 Frail.", "intent": "DebuffAttack4"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Life Suck` | {"effect": "Deals (10;12) damage. Heals HP equal to unblocked damage dealt.", "intent": "BuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Stunned` | {"effect": "Does nothing.", "intent": "Stunned"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Shelled Parasite<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>68;72(70;75)<br>类型<br>普通<br>意图<br>双击;汲取;脆弱打击<br>初始能力<br>多重护甲14<br>备注<br>无<br>行动<br>（图片未提供文字说明）<br>如果它的多层护甲被全部击破，它会被击晕，这会打断它当前的意图。<br>应对<br>由于多层护甲的存在，最好在回合中先使用高伤害攻击卡，然后在格挡被破坏后尽可能多次地攻击以破坏它的多层护甲。 | `single_source` | [带壳寄生怪](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436702&wiki_id=646570) |
| `source.infobox.description` | 68-72 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 带壳寄生怪 | `single_source` | [带壳寄生怪](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436702&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Shelled Parasite<br>|Image  = ShelledParasite.png<br>|HP     = 68-72<br>|AscHP  = 70-75<br>|Powers = {{BD|Plated Armor}} 14<br>|Debut  = Act 2<br>|Type   = Normal<br>}} {{Power Infobox|Plated Armor}}<br>'''Shelled Parasite''' is a normal [[Monsters|Enemy]] encountered exclusively in [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|Shelled Parasite}}<br>{{Intents Table/row<br>|Name   = Double Strike<br>|Intent = Attack3<br>|Effect = Deals (6×2;{{Asc|2|7×2}}... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
