# 史莱姆老大 / Slime Boss

> 稳定 ID：`sts1.monster.slime_boss`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：史莱姆老大
- English: Slime Boss

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | boss |
| `act` | Act 1 |
| `hp_min` | 140 |
| `hp_max` | 140 |
| `ascension_json` | {"ascension_max": 150, "ascension_min": 150, "ascension_raw": "150", "base_max": 140, "base_min": 140, "base_raw": "140"} |
| `encounter_notes` | Chinese article shows 140;(150;) and a 4+/19+ action table; retain raw text in claims. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Slam | Attack7 | 35 |  | {"text": "Deals (35;38) damage."} |
| Preparing | Unknown |  |  | {"text": "Does nothing."} |
| Split | Unknown |  |  | {"text": "Disappears and spawns 1 Acid Slime (L) and 1 Spike Slime (L) with its current HP."} |
| Goop Spray | DebuffStrong |  |  | {"text": "Adds (3;5) Slimed into your discard pile."} |
| 准备 | buff |  |  | {} |
| 史莱姆撞击 | attack | 35 | 1 | {"a4_plus_damage": 38} |
| 黏液喷射 | debuff |  |  | {"a19_plus_count": 5, "add_to_discard": "Slimed", "count": 3} |
| 分裂 | special |  |  | {"condition": "current_hp_below_half", "summons": ["Large Spike Slime", "Large Acid Slime"]} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [第一幕：史莱姆老大 / Exordium: Slime Boss](../encounters/sts1_encounter_exordium_slime_boss.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Slime Boss | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 史莱姆老大 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SlimeBoss", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~Slime...~ NL #r~CRUSH!!!~", ""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~史莱姆……~ NL #r~撞~ #r~击~ #r~！！~", "打断！"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Slam", "Preparing", "Split", "Goop Spray"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["猛撞", "准备", "分裂", "黏液喷射"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.ascension` | 150 | `provisional` | [史莱姆老大](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570) |
| `monster.hp.base` | 140 | `provisional` | [史莱姆老大](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570) |
| `monster.hp.range` | {"ascension_max": 150, "ascension_min": 150, "ascension_raw": "150", "base_max": 140, "base_min": 140, "base_raw": "140"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Goop Spray` | {"effect": "Adds (3;5) Slimed into your discard pile.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Preparing` | {"effect": "Does nothing.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Slam` | {"effect": "Deals (35;38) damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Split` | {"effect": "Disappears and spawns 1 Acid Slime (L) and 1 Spike Slime (L) with its current HP.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.slime.damage` | 35 | `provisional` | [史莱姆老大](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570) |
| `monster.move.slime.damage_a4_plus` | 38 | `provisional` | [史莱姆老大](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570) |
| `monster.move.slime_count` | 3 | `provisional` | [史莱姆老大](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570) |
| `monster.move.slime_count_a19_plus` | 5 | `provisional` | [史莱姆老大](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570) |
| `source.article_excerpt.en` | Slime BossHP 140150 9Debut Act 1Powers Split SplitStack Type Does not stack When its HP is at or below 50%, it will split into 2 smaller Slimes with its current HP. Slimed 1 Energy - Status Exhaust. Slime Boss is a Boss that can appear at the end of Act 1 or the Act 3 event Mind Bloom. Pattern[edit | edit source] Name Intent Effect Goop Spray Adds 3 Slimed into your discard pile. Adds 5 19 Slimed into your discard pile. Preparing Does nothing. Slam Deals 35 damage. Deals 38 4 damage. Split Di... | `single_source` | [Slime Boss | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Slime_Boss) |
| `source.article_text` | 史莱姆老大<br>Monster id: Slime Boss<br>怪物信息<br>生命值<br>140;(150;)<br>类型<br>Boss<br>意图<br>黏液喷射;准备;史莱姆撞击;分裂<br>初始能力<br>分裂<br>备注<br>无<br>地图图标<br>攻击方式<br>效果<br>进阶4+<br>进阶19+<br>粘液<br>向弃牌堆放置3张粘液<br>向弃牌堆放置3张粘液<br>向弃牌堆放置5张粘液<br>准备<br>无<br>无<br>无<br>撞击<br>35伤害<br>38伤害<br>38伤害<br>分裂<br>当前低于半血时，会分裂成 尖刺史莱姆（大）和毒液史莱姆（大）<br>同前<br>同前<br>* 行为模式：<br>粘液 - 准备 - 撞击 （循环） | `single_source` | [史莱姆老大](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/8395e149d8d2b6b1322df8bce6e93fde.png"] | `single_source` | [史莱姆老大](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570) |
| `source.infobox.description` | 140 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 史莱姆老大 | `single_source` | [史莱姆老大](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=531529&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Slime Boss<br>|Image  = SlimeBoss.png<br>|Icon   = Map-SlimeBoss.png<br>|HP     = 140<br>|AscHP  = 150<br>|Powers = {{BD|Split}}<br>|Debut  = Act 1<br>|Type   = Boss<br>}} {{Power Infobox|Split}}{{Small Card Infobox|Slimed}}<br>'''Slime Boss''' is a [[Boss]] that can appear at the end of [[Act 1]] or the [[Act 3]] event {{E|Mind Bloom}}.<br><br>== Pattern ==<br>{{Intents Table/start|Slime Boss}}<br>{{Intents Table/row<br>|Name   = Goop Spray<br>|Intent = DebuffStr... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
