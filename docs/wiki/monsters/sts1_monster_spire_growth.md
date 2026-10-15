# 塔内增生组织 / Spire Growth

> 稳定 ID：`sts1.monster.spire_growth`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：塔内增生组织
- English: Spire Growth

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 3 |
| `hp_min` | 170 |
| `hp_max` | 170 |
| `ascension_json` | {"ascension_max": 190, "ascension_min": 190, "ascension_raw": "190", "base_max": 170, "base_min": 170, "base_raw": "170"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Constrict | DebuffStrong |  |  | {"text": "Applies (10;12) Constricted."} |
| Smash | Attack5 | 22 |  | {"text": "Deals (22;25) damage."} |
| Quick Tackle | Attack4 | 16 |  | {"text": "Deals (16;18) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [塔内增生组织 / Spire Growth](../encounters/sts1_encounter_act3_hard_spire_growth.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Spire Growth | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 塔内增生组织 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Serpent", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 190, "ascension_min": 190, "ascension_raw": "190", "base_max": 170, "base_min": 170, "base_raw": "170"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Constrict` | {"effect": "Applies (10;12) Constricted.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Quick Tackle` | {"effect": "Deals (16;18) damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Smash` | {"effect": "Deals (22;25) damage.", "intent": "Attack5"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Spire Growth<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>170;(190;)<br>类型<br>普通<br>意图<br>打击;粉碎;缠绕<br>初始能力<br>无<br>备注<br>无<br>行动模式<br>它的行动会受玩家目前状态影响：<br>如果玩家没有被缠绕，则它有50%的几率使用缠绕，50%的几率使用打击。<br>17-<br>:如果玩家已被缠绕或上一回合使用了缠绕，则有50%几率使用打击，50%几率使用粉碎。<br>17+<br>:它将必定在第一回合使用缠绕。如果玩家没有被缠绕并且上一回合没有使用缠绕，它也必定使用缠绕<br>它不能连续使用任何一次攻击3次。<br>名称<br>效果<br>进阶2+<br>进阶17+<br>打击<br>造成16点伤害<br>造成18点伤害<br>造成18点伤害<br>粉碎<br>造成22点伤害<br>造成25点伤害<br>造成25点伤害<br>缠绕<br>给予玩家10点缠绕<br>给予玩家10点缠绕<br>给予玩家12点缠绕 | `single_source` | [塔内增生组织](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438539&wiki_id=646570) |
| `source.infobox.description` | 170 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 塔内增生组织 | `single_source` | [塔内增生组织](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438539&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Spire Growth<br>|Image  = SpireGrowth.png<br>|HP     = 170<br>|AscHP  = 190<br>|Debut  = Act 3<br>|Type   = Normal<br>}}<br>{{Power Infobox|Constricted}}<br>Spire Growth is a normal [[Monsters|Enemy]] found exclusively in [[Act 3]].<br><br>== Pattern ==<br>{{Intents Table/start|Spire Growth}}<br>{{Intents Table/row<br>|Name   = Constrict<br>|Intent = DebuffStrong<br>|Effect = Applies (10;{{Asc|2|12}}) {{BD|Constricted}}.}}<br>{{Intents Table/row<br>|Name   = Quick... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
