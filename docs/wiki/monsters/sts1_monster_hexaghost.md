# 六火亡魂 / Hexaghost

> 稳定 ID：`sts1.monster.hexaghost`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：六火亡魂
- English: Hexaghost

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | boss |
| `act` | Act 1 |
| `hp_min` | 250 |
| `hp_max` | 250 |
| `ascension_json` | {"ascension_max": 264, "ascension_min": 264, "ascension_raw": "264", "base_max": 250, "base_min": 250, "base_raw": "250"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Inferno | DebuffAttack5 | 2 | 6 | {"text": "Deals (2×6;3×6) damage. Adds 3 Burns+ into your discard pile. Upgrades all Burns. For the rest of combat, any Burn created by Sear will be upgraded."} |
| Activate | Unknown |  |  | {"text": "Does nothing."} |
| Divider | Attack7 | 1 | 6 | {"text": "Deals (N+1)×6 damage. N = Player's HP at the start of the turn, divided by 12 (rounded down)."} |
| Inflame | DefendBuff |  |  | {"text": "Gains 12 Block and (2;3) Strength."} |
| Sear | DebuffAttack2 | 6 |  | {"text": "Deals 6 damage. Adds (1;2) Burns into your discard pile."} |
| Tackle | Attack3 | 5 | 2 | {"text": "Deals (5×2;6×2) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Hexaghost | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 六火亡魂 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Hexaghost", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["Inflame", "Sear", "Inferno"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["高热", "灼烧", "地狱火"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 264, "ascension_min": 264, "ascension_raw": "264", "base_max": 250, "base_min": 250, "base_raw": "250"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Activate` | {"effect": "Does nothing.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Divider` | {"effect": "Deals (N+1)×6 damage. N = Player's HP at the start of the turn, divided by 12 (rounded down).", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Inferno` | {"effect": "Deals (2×6;3×6) damage. Adds 3 Burns+ into your discard pile. Upgrades all Burns. For the rest of combat, any Burn created by Sear will be upgraded.", "intent": "DebuffAttack5"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Inflame` | {"effect": "Gains 12 Block and (2;3) Strength.", "intent": "DefendBuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Sear` | {"effect": "Deals 6 damage. Adds (1;2) Burns into your discard pile.", "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tackle` | {"effect": "Deals (5×2;6×2) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 六火亡魂<br>Monster id: Hexaghost<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>250;(264;)<br>类型<br>Boss<br>意图<br>准备;地狱火;双击;灼烧;高热;地狱火_1<br>初始能力<br>无<br>备注<br>无<br>地图图标<br>攻击方式<br>效果<br>进阶4+<br>进阶19+<br>启动<br>无<br>无<br>无<br>火带<br>X*6伤害，X=(当前生命 / 12)+1<br>同前<br>同前<br>地狱火<br>2*6伤害，向弃牌堆放置3张灼烧。升级所有灼烧<br>3*6伤害， 向弃牌堆放置3张灼烧。升级所有灼烧<br>同前<br>烧焦<br>6伤害，向弃牌堆放置1张灼烧<br>同前<br>6伤害，向弃牌堆放置2张灼烧<br>双击<br>5*2伤害<br>6*2伤害<br>同前<br>高热<br>获得12点防御，2力量<br>同前<br>获得12点防御，3力量<br>* 备注：地狱火会在第二次发动时升级所有灼烧，并使之后的灼烧均升级为灼烧+<br>* 行为模式：<br>（启动 - 火带... | `single_source` | [六火亡魂](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421622&wiki_id=646570) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/cd1cad8ee1524095a021dde6d0ea9154.png", "https://cdn.max-c.com/heybox/dailynews/img/ee5b22b40d6d38468f301df0dac3e7f4.png"] | `single_source` | [六火亡魂](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421622&wiki_id=646570) |
| `source.infobox.description` | 250 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 六火亡魂 | `single_source` | [六火亡魂](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421622&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Hexaghost<br>|Image  = Hexaghost.png<br>|Icon   = Map-Hexaghost.png<br>|HP     = 250<br>|AscHP  = 264<br>|Debut  = Act 1<br>|Type   = Boss<br>}} {{M|Hexaghost}} is a [[Boss]] that can appear at the end of [[Act 1]] or the [[Act 3]] event {{E|Mind Bloom}}.<br><br>== Pattern ==<br>{{Intents Table/start|Hexaghost}}<br>{{Intents Table/row<br>|Name   = Activate<br>|Intent = Unknown<br>|Effect = Does nothing.}}<br>{{Intents Table/row<br>|Name   = Divider<br>|Intent = At... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
