# 铜制机械人偶 / Bronze Automaton

> 稳定 ID：`sts1.monster.bronze_automaton`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：铜制机械人偶
- English: Bronze Automaton

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | boss |
| `act` | Act 2 |
| `hp_min` | 300 |
| `hp_max` | 300 |
| `ascension_json` | {"ascension_max": 320, "ascension_min": 320, "ascension_raw": "320", "base_max": 300, "base_min": 300, "base_raw": "300"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| HYPER BEAM | Attack7 | 45 |  | {"text": "Deals (45;50) damage."} |
| Stunned | Unknown |  |  | {"text": "Does nothing."} |
| Boost | DefendBuff |  |  | {"text": "Gains (3;4) Strength and (9;12) Block."} |
| Spawn Orbs | Unknown |  |  | {"text": "Summons 2 Bronze Orbs."} |
| Flail | Attack3 | 7 | 2 | {"text": "Deals (7×2;8x2) damage."} |

## 相关条目

- `has_member` → [铜球 / Bronze Orb](sts1_game_candidate_monster_bronzeorb.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Bronze Automaton | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 铜制机械人偶 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "BronzeAutomaton", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["晕眩！"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["HYPER BEAM"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["超能光束"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 320, "ascension_min": 320, "ascension_raw": "320", "base_max": 300, "base_min": 300, "base_raw": "300"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Beam` | {"effect": "Deals 8 damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Boost` | {"effect": "Gains (3;4) Strength and (9;12) Block.", "intent": "DefendBuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Flail` | {"effect": "Deals (7×2;8x2) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.HYPER BEAM` | {"effect": "Deals (45;50) damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Spawn Orbs` | {"effect": "Summons 2 Bronze Orbs.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Stasis` | {"effect": "Steals a random card of the highest rarity from your draw pile (or discard pile, if the draw pile is empty). On death, returns the card to your hand.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Stunned` | {"effect": "Does nothing.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Support Beam` | {"effect": "Bronze Automaton gains 12 Block.", "intent": "Defend"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 铜制机械人偶<br>Monster id: Bronze Automaton<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>300;(320;)<br>类型<br>Boss<br>意图<br>召唤;鼓舞;双击;超能光束<br>初始能力<br>人工制品3<br>备注<br>无<br>地图图标<br>攻击方式<br>效果<br>进阶4+<br>生产球体<br>召唤两个铜球<br>同前<br>提升<br>获得9格挡，3力量<br>获得9格挡，4力量<br>连击<br>7*2伤害<br>8*2伤害<br>超能光束<br>45伤害<br>50伤害<br>*行动模式：<br>生产球体 - 连击 - 提升 - 连击 - 提升 - 超能光束 - 无行动（进阶19+，使用 提升） - （循环）<br>（图片未提供文字说明）<br>铜球<br>攻击方式<br>效果<br>凝滞<br>从牌库偷走最稀有的牌，死亡后返还<br>攻击<br>8伤害<br>防御<br>为铜制机械人偶增加12格挡<br>* 行动模式：<br>优先 凝滞，之后随机行动 | `single_source` | [铜制机械人偶](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421630&wiki_id=646570) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/263e5fae10fba4eae581f9035c0fee17.png", "https://cdn.max-c.com/heybox/dailynews/img/df5dda547db5fb764f6702dc526e4b96.png", "https://cdn.max-c.com/heybox/dailynews/img/f31d95a6f1673137fe589809b1740b05.png"] | `single_source` | [铜制机械人偶](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421630&wiki_id=646570) |
| `source.infobox.description` | 300 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 铜制机械人偶 | `single_source` | [铜制机械人偶](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421630&wiki_id=646570) |
| `source.wikitext` | {{Ambox<br>| title = WARNING!<br>| color = red<br>| icon = GremlinNob.png<br>| message = ''This page is under construction. Information may be wrong or incomplete.''<br>}}<br><br>{{Enemy Infobox<br>|Name   = Bronze Automaton<br>|Image  = BronzeAutomaton.png<br>|Icon   = Map-Automaton.png<br>|HP     = 300<br>|AscHP  = 320<br>|Powers = {{BD|Artifact}} 3<br>|Debut  = Act 2<br>|Type   = Boss<br>}}<br>'''Bronze Automaton''' is a [[Boss]] found at the end of [[Act 2]].<br><br>== Pattern ==<br>{{Int... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
