# 哨位(精英) / Sentry

> 稳定 ID：`sts1.monster.sentry`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：哨位(精英)
- English: Sentry

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 38 |
| `hp_max` | 42 |
| `ascension_json` | {"ascension_max": 45, "ascension_min": 39, "ascension_raw": "39-45", "base_max": 42, "base_min": 38, "base_raw": "38-42"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Bolt | Debuff |  |  | {"text": "Adds (2;3) Dazed into your discard pile."} |
| Beam | Attack2 | 9 |  | {"text": "Deals (9;10) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [哨卫与圆球守护者 / Sentry and Spheric Guardian](../encounters/sts1_encounter_act2_hard_sentry_and_spheric_guardian.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Sentry | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 哨卫 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Sentry", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Disintegrate"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["粉碎"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 45, "ascension_min": 39, "ascension_raw": "39-45", "base_max": 42, "base_min": 38, "base_raw": "38-42"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Beam` | {"effect": "Deals (9;10) damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Bolt` | {"effect": "Adds (2;3) Dazed into your discard pile.", "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | （图片未提供文字说明）<br>分布<br>你可以在第一阶段塔底的精英战中，遇到三个一组的哨卫；或者在第二阶段城市（后期的）的普通战斗中，遇到与圆球守护者搭档的单个哨卫。<br>行动<br>哨卫的意图是固定且交替进行的。<br>（图片未提供文字说明）<br>如果你遭遇的是精英战中三个一组的哨卫，那么第一回合时，两侧的两个哨卫会使用螺旋催眠，而中间的哨卫会使用激光；<br>第二回合时，它们将切换行动：两侧的哨卫使用激光，中间的哨卫使用螺旋催眠。以此类推。<br>如果你遭遇的是普通战斗中单个的哨卫，那么这个哨卫第一回合会使用螺旋催眠。<br>策略<br>鉴于精英战中两侧的哨卫总是同步行动，因此推荐集中火力击杀第一个或者第三个哨卫，以免你需要想办法在游戏前期去阻挡足足18（或20）点伤害。<br>哨卫会在你的牌组中加入大量状态牌，这使得战士的请火焰吐息在对战哨卫时有相当不错的效果。<br>如果使用大牌组与哨卫进行战斗，有利于使晕眩影响你的抽牌之前结束战斗。但这很可能会令你无法及时抽到关键牌，从而扰乱你的战斗节奏。此外，在第一阶段塔底就成功构筑大牌组不太现实。<br>由于哨卫在战斗开始时自... | `single_source` | [哨位(精英)](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421616&wiki_id=646570) |
| `source.infobox.description` | 38-42 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 哨位(精英) | `single_source` | [哨位(精英)](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421616&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Sentry<br>|Image  = Sentry.png<br>|HP     = 38-42<br>|AscHP  = 39-45<br>|Powers = {{BD|Artifact}} 1<br>|Debut  = Act 1<br>|Type   = Elite<br>}}{{Power Infobox|Artifact}}{{Small Card Infobox|Dazed}}<br>'''Sentry''' is an [[Elite]] found in [[Act 1]] in groups of three. In [[Act 2]], a Sentry can be fought as a common [[Slay the Spire Wiki/Enemies|Enemy]].<br>== Pattern ==<br>{{Intents Table/start|Sentry}}<br>{{Intents Table/row<br>|Name   = Bolt<br>|Intent = Debuff... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
