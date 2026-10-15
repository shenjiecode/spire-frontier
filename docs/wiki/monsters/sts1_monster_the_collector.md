# 收藏家 / The Collector

> 稳定 ID：`sts1.monster.the_collector`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：收藏家
- English: The Collector

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | boss |
| `act` | Act 2 |
| `hp_min` | 282 |
| `hp_max` | 282 |
| `ascension_json` | {"ascension_max": 300, "ascension_min": 300, "ascension_raw": "300", "base_max": 282, "base_min": 282, "base_raw": "282"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Buff | DefendBuff |  |  | {"text": "All enemies gain (3;4 ; 5) Strength. Gains (15;18 ; 23) Block."} |
| Mega Debuff | DebuffStrong |  |  | {"text": "Applies (3;5) Weak, (3;5) Vulnerable and (3;5) Frail."} |
| Fireball | Attack4 | 18 |  | {"text": "Deals (18;21) damage."} |
| Spawn | Unknown |  |  | {"text": "Summons up to 2 Torch Heads."} |

## 相关条目

- `has_member` → [火炬头 / Torch Head](sts1_game_candidate_monster_torchhead.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | The Collector | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 收藏家 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "TheCollector", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@You@ @are@ @mine!@"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@你是我的了！@"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 300, "ascension_min": 300, "ascension_raw": "300", "base_max": 282, "base_min": 282, "base_raw": "282"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Buff` | {"effect": "All enemies gain (3;4 ; 5) Strength. Gains (15;18 ; 23) Block.", "intent": "DefendBuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Fireball` | {"effect": "Deals (18;21) damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Mega Debuff` | {"effect": "Applies (3;5) Weak, (3;5) Vulnerable and (3;5) Frail.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Spawn` | {"effect": "Summons up to 2 Torch Heads.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tackle` | {"effect": "Deals 7 damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 收藏家<br>Monster id: The Collector<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>282;(300;)<br>类型<br>Boss<br>意图<br>强化;火球;究极减益;召唤<br>初始能力<br>无<br>备注<br>无<br>地图图标<br>攻击方式<br>效果<br>进阶4+<br>进阶19+<br>防御buff<br>获得15格挡，所有敌人获得3力量<br>获得18格挡，所有敌人获得4力量<br>获得23格挡，所有敌人获得5力量<br>火球<br>18伤害<br>21伤害<br>同前<br>大型debuff<br>造成三回合虚弱、易伤、破甲<br>同前<br>造成五回合虚弱、易伤、破甲<br>召唤<br>将场上火炬头数量补充至两个<br>同前<br>同前<br>* 行动模式：<br>第一回合一定会使用 召唤；并且总是会在第四回合使用 大型debuff。如果一个火炬头被消灭，Boss有25%重新 召唤，45%火球，30%防御buff。如果两个火炬头均存活，70%火球，30%防御buff。不会连续两次 防御buff，不会连续... | `single_source` | [收藏家](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=532023&wiki_id=646570) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/0857c3fca2b4abf9f7547bd20b211192.png", "https://cdn.max-c.com/heybox/dailynews/img/74b941f4f915f59e3ef5c8ebf96b9507.png", "https://cdn.max-c.com/heybox/dailynews/img/e2c49fd273f03420f8db5c56ca63dfcc.png"] | `single_source` | [收藏家](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=532023&wiki_id=646570) |
| `source.infobox.description` | 282 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 收藏家 | `single_source` | [收藏家](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=532023&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = The Collector<br>|Image  = TheCollector.png<br>|Icon   = Map-Collector.png<br>|HP     = 282<br>|AscHP  = 300<br>|Debut  = Act 2<br>|Type   = Boss<br>}}<br>The Collector is a [[Boss]] found at the end of [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|The Collector}}<br>{{Intents Table/row<br>|Name   = Spawn<br>|Intent = Unknown<br>|Effect = Summons up to 2 {{M|Torch Head|Torch Heads}}.}}<br>{{Intents Table/row<br>|Name   = Fireball<br>|Intent = Attack4<br... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
