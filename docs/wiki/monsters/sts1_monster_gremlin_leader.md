# 地精首领 / Gremlin Leader

> 稳定 ID：`sts1.monster.gremlin_leader`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：地精首领
- English: Gremlin Leader

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 2 |
| `hp_min` | 140 |
| `hp_max` | 148 |
| `ascension_json` | {"ascension_max": 155, "ascension_min": 145, "ascension_raw": "145-155", "base_max": 148, "base_min": 140, "base_raw": "140-148"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Stab | Attack4 | 6 | 3 | {"text": "Deals 6×3 damage."} |
| Encourage | DefendBuff |  |  | {"text": "All enemies gain (3;4 ; 5) Strength. Other enemies gain (6;10) Block."} |
| Rally! | Unknown |  |  | {"text": "Summon 2 random Gremlins]."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Gremlin Leader | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 地精首领 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "GremlinLeader", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["Don't ever give up!", "We're not done yet!", "Get em boys!", "@Retreat@ NL @Retreaaat!@", "@Ruuuuuuun!@"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["永远别放弃！", "我们还没完呢！", "小的们，给我上！", "@撤退@ NL @撤退啊！@", "@逃命哇！@"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Rally!"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["集合！"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 155, "ascension_min": 145, "ascension_raw": "145-155", "base_max": 148, "base_min": 140, "base_raw": "140-148"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Encourage` | {"effect": "All enemies gain (3;4 ; 5) Strength. Other enemies gain (6;10) Block.", "intent": "DefendBuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Rally!` | {"effect": "Summon 2 random Gremlins].", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Stab` | {"effect": "Deals 6×3 damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | （图片未提供文字说明）<br>行动<br>（图片未提供文字说明）<br>若场上没有其他敌人时：有75%的概率使用集合！，25%的概率使用三连击。<br>若场上仅1名其他敌人时：<br>若上一次行动是鼓舞，则有50%的概率使用集合！，50%的概率使用三连击。<br>若上一次行动是三连击，则有62.5%概率使用集合！，37.5%的概率使用鼓舞<br>若场上有2名其他敌人，则有有66%的概率使用鼓舞，34%的概率使用三连击。<br>策略<br>若没有足够的爆发伤害，建议先击杀其召唤的爪牙以降低其攻击的可能性。同时防止爪牙地精给予的负面状态（如胖地精）。<br>建议有限击杀威胁强的地精，如地精法师和胖地精。<br>特殊<br>本局的所有地精都带有（图片未提供文字说明）爪牙效果。<br>轶事<br>据开发者之一透露，地精头领性别为雌性。 | `single_source` | [地精首领](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432036&wiki_id=646570) |
| `source.infobox.description` | 140-148 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 地精首领 | `single_source` | [地精首领](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432036&wiki_id=646570) |
| `source.wikitext` | {{Ambox<br>| title = WARNING!<br>| color = red<br>| icon = GremlinNob.png<br>| message = ''This page is under construction. Information may be wrong or incomplete.''<br>}}<br><br><br>{{Enemy Infobox<br>|Name   = Gremlin Leader<br>|Image  = GremlinLeader.png<br>|HP     = 140-148<br>|AscHP  = 145-155<br>|Debut  = Act 2<br>|Type   = Elite<br>}}<br>'''Gremlin Leader''' is an [[Elite]] Enemy encountered exclusively in [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|Gremlin Leader}}<br>{{I... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
