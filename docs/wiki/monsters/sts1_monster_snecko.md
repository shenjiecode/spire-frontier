# 异蛇 / Snecko

> 稳定 ID：`sts1.monster.snecko`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：异蛇
- English: Snecko

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 2 |
| `hp_min` | 114 |
| `hp_max` | 120 |
| `ascension_json` | {"ascension_max": 125, "ascension_min": 120, "ascension_raw": "120-125", "base_max": 120, "base_min": 114, "base_raw": "114-120"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Perplexing Glare | DebuffStrong |  |  | {"text": "Applies Confused."} |
| Bite | Attack4 | 15 |  | {"text": "Deals (15;18) damage."} |
| Tail Whip | DebuffAttack2 | 8 |  | {"text": "Deals (8;10) damage. Applies 2 Vulnerable(.; and 2 Weak)."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [异蛇 / Snecko](../encounters/sts1_encounter_act2_hard_snecko.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Snecko | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 异蛇 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Snecko", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Perplexing Glare", "Tail Whip", "Bite"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["困惑瞪视", "扫尾", "噬咬"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 125, "ascension_min": 120, "ascension_raw": "120-125", "base_max": 120, "base_min": 114, "base_raw": "114-120"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Bite` | {"effect": "Deals (15;18) damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Perplexing Glare` | {"effect": "Applies Confused.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tail Whip` | {"effect": "Deals (8;10) damage. Applies 2 Vulnerable(.; and 2 Weak).", "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Snecko<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>114;120(120;125)<br>类型<br>普通<br>意图<br>困惑瞪视;扫尾;噬咬<br>初始能力<br>无<br>备注<br>无<br>行动<br>名称<br>效果<br>进阶2+<br>进阶17+<br>备注<br>困惑<br>瞪视<br>施加1层混乱<br>施加1层混乱<br>施加1层混乱<br>首回合必定使用，每场战斗只能使用一次<br>扫尾<br>造成8点伤害，<br>施加2层易伤<br>造成10点伤害,施加2层易伤<br>造成10点伤害,施加2层易伤、虚弱<br>噬咬<br>造成15点伤害<br>造成18点伤害<br>造成18点伤害<br>不能连续使用3次<br>应对<br>由于困惑瞪视只会使用一次，可以使用<br>人工制品<br>抵消<br>混乱<br>效果。<br>混乱效果并不只有坏处，有时，它会将高能量的卡牌的能量需求减少，这可能会对你有很大帮助。<br>轶事<br>据统计，蛇（大多为异蛇）是游戏中出现次数最多的动物。 | `single_source` | [异蛇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436731&wiki_id=646570) |
| `source.infobox.description` | 114-120 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 异蛇 | `single_source` | [异蛇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436731&wiki_id=646570) |
| `source.wikitext` | {{Ambox<br>| title = WARNING!<br>| color = red<br>| icon = GremlinNob.png<br>| message = ''This page is under construction. Information may be wrong or incomplete.''<br>}}<br><br><br>{{Enemy Infobox<br>|Name   = Snecko<br>|Image  = Snecko.png<br>|HP     = 114-120<br>|AscHP  = 120-125<br>|Debut  = Act 2<br>|Type   = Normal<br>}}<br>{{Power Infobox|Confused}}<br>'''Snecko''' is a normal [[Monsters|Enemy]] encountered exclusively in [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|Snecko... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
