# 奴隶头子 / Taskmaster

> 稳定 ID：`sts1.monster.taskmaster`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：奴隶头子
- English: Taskmaster

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 2 |
| `hp_min` | 54 |
| `hp_max` | 60 |
| `ascension_json` | {"ascension_max": 64, "ascension_min": 57, "ascension_raw": "57-64", "base_max": 60, "base_min": 54, "base_raw": "54-60"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Scouring Whip | DebuffAttack2 | 7 |  | {"text": "Deals 7 damage. Adds (1 Wound; 2 ; 3 Wounds) into your discard pile. (;Gains 1 Strength.)"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Taskmaster | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 奴隶头子 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SlaverBoss", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 64, "ascension_min": 57, "ascension_raw": "57-64", "base_max": 60, "base_min": 54, "base_raw": "54-60"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Scouring Whip` | {"effect": "Deals 7 damage. Adds (1 Wound; 2 ; 3 Wounds) into your discard pile. (;Gains 1 Strength.)", "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 与 蓝奴隶主 及 红奴隶主 作为第二阶段的精英同时出现<br>行动<br>造成7伤害并向你的弃牌堆加入1/2/3张伤口（进阶 0/ 3/ 18+），<br>获得1力量 18+。<br>特殊<br>奴隶头子会在二阶段的精英战（与红奴隶和蓝奴隶一起）出现，<br>以及竞技场的第二轮（与地精大块头一起）出现。 | `single_source` | [奴隶头子](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432034&wiki_id=646570) |
| `source.infobox.description` | 54-60 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 奴隶头子 | `single_source` | [奴隶头子](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432034&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Taskmaster<br>|Image  = Taskmaster.png<br>|HP     = 54-60<br>|AscHP  = 57-64<br>|Debut  = Act 2<br>|Type   = Elite<br>}}{{Small Card Infobox|Wound}}<br>Taskmaster is an [[Elite]] enemy found exclusively in [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|Taskmaster}}<br>{{Intents Table/row<br>|Name   = Scouring Whip<br>|Intent = DebuffAttack2<br>|Effect = Deals 7 damage. Adds (1 {{C|Wound}}; {{Asc|2|2}} ; {{Asc|18|3}} {{C|Wound|Wounds}}) into your discard ... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
