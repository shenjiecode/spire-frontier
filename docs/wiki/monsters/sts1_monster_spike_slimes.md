# 尖刺史莱姆 / Spike Slimes

> 稳定 ID：`sts1.monster.spike_slimes`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：尖刺史莱姆
- English: Spike Slimes

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 64 |
| `hp_max` | 64 |
| `ascension_json` | {"asc_hp": 67} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Split | Unknown |  |  | {"text": "Disappears and spawns 2 Acid Slimes (M) with its current HP."} |
| Lick | Debuff |  |  | {"text": "Applies 1 Frail."} |
| Tackle | Attack3 | 10 |  | {"text": "Deals (10;12) damage."} |
| Tackle | Attack1 | 3 |  | {"text": "Deals (3;4) damage."} |
| Tackle | Attack2 | 5 |  | {"text": "Deals (5;6) damage."} |
| Flame Tackle | DebuffAttack2 | 8 |  | {"text": "Deals (8;10) damage. Adds a Slimed into your discard pile."} |
| Tackle | Attack4 | 16 |  | {"text": "Deals (16;18) damage."} |
| Corrosive Spit | DebuffAttack2 | 7 |  | {"text": "Deals (7;8) damage. Adds a Slimed into your discard pile."} |
| Lick | Debuff |  |  | {"text": "Applies 1 Weak."} |
| Corrosive Spit | DebuffAttack3 | 11 |  | {"text": "Deals (11;12) damage. Adds 2 Slimed into your discard pile."} |
| Split | Unknown |  |  | {"text": "Disappears and spawns 2 Spike Slimes (M) with its current HP."} |
| Flame Tackle | DebuffAttack4 | 16 |  | {"text": "Deals (16;18) damage. Adds 2 Slimed into your discard pile."} |
| Lick | Debuff |  |  | {"text": "Applies 2 Weak."} |
| Lick | Debuff |  |  | {"text": "Applies (2;3) Frail."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Spike Slime (L) | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 尖刺史莱姆（大） | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SpikeSlime_L", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["打断！"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Lick", "Split"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["舔舔", "分裂"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Corrosive Spit` | {"effect": "Deals (11;12) damage. Adds 2 Slimed into your discard pile.", "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Flame Tackle` | {"effect": "Deals (16;18) damage. Adds 2 Slimed into your discard pile.", "intent": "DebuffAttack4"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Lick` | {"effect": "Applies (2;3) Frail.", "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Split` | {"effect": "Disappears and spawns 2 Spike Slimes (M) with its current HP.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tackle` | {"effect": "Deals (5;6) damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 尖刺史莱姆（大）<br>（图片未提供文字说明）<br>（图片未提供文字说明）<br>出现<br>（图片未提供文字说明）<br>行动<br>（图片未提供文字说明）<br>不能连续进行三次相同的行动，进阶17+不能连续进行两次舔舔。<br>尖刺史莱姆（中）<br>（图片未提供文字说明）<br>出现<br>（图片未提供文字说明）<br>行为<br>（图片未提供文字说明）<br>不能连续进行三次相同的行动，进阶17+不能连续进行两次舔舔。<br>尖刺史莱姆（小）<br>（图片未提供文字说明）<br>出现<br>（图片未提供文字说明）<br>行为<br>（图片未提供文字说明） | `single_source` | [尖刺史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411793&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/16/03a2dfa3c9ef78b9aa1cc0bcadac1e70.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/09a1133117997dbd169aad1a8bbfc282.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/586444fb1d77045bc679492c41f0e66d.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/9d1683a3a2aec4c64b19730030e5b4db.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/bb935afb54a282bbc5177cdc5e1fd90c.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/d46008de1a545... | `single_source` | [尖刺史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411793&wiki_id=646570) |
| `source.infobox.description` | 64-70 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 尖刺史莱姆 | `single_source` | [尖刺史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411793&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{TOC limit|2}}<br>== Spike Slime (L) ==<br>{{Enemy Infobox<br>|Name   = Spike Slime (L)<br>|Image  = SpikeSlimeL.png<br>|HP     = 64-70<br>|AscHP  = 67-73<br>|Powers = {{BD|Split}}<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>{{Power Infobox|Split}}<br>'''Spike Slime (L)''' is a normal [[Monsters|Enemy]] found exclusively in Act 1.<br><br>=== Pattern ===<br>{{Intents Table/start|Spike Slime (L)}}<br>{{Intents Table/row<br>|Name   = Lick<br>|Intent = Debuff<br>... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
