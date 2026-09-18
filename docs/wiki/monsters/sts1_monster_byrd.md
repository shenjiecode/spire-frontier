# 异鸟 / Byrd

> 稳定 ID：`sts1.monster.byrd`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：异鸟
- English: Byrd

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 2 |
| `hp_min` | 25 |
| `hp_max` | 25 |
| `ascension_json` | {"asc_hp": 26} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Swoop | Attack3 | 12 |  | {"text": "Deals (12;14) damage."} |
| Peck | Attack2 | 1 |  | {"text": "Deals (1×5;1×6) damage"} |
| Headbutt | Attack1 | 3 |  | {"text": "Deals 3 damage."} |
| Caw | Buff |  |  | {"text": "Gains 1 Strength."} |
| Go Airborne | Unknown |  |  | {"text": "Gains (3;4) Flying."} |
| Stunned | Stunned |  |  | {"text": "Does nothing."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Byrd | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 异鸟 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Byrd", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@CAW!@ NL @CAAAW@", ""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@嘎！@ NL @哑！@", "击晕……"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Caw` | {"effect": "Gains 1 Strength.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Go Airborne` | {"effect": "Gains (3;4) Flying.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Headbutt` | {"effect": "Deals 3 damage.", "intent": "Attack1"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Peck` | {"effect": "Deals (1×5;1×6) damage", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Stunned` | {"effect": "Does nothing.", "intent": "Stunned"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Swoop` | {"effect": "Deals (12;14) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 异鸟<br>Monster id: Byrd<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>25;31(26;33)<br>类型<br>普通<br>意图<br>强化;连击;俯冲<br>初始能力<br>飞行3（4）<br>备注<br>无<br>行动<br>名称<br>效果<br>进阶2+<br>概率<br>备注<br>强化<br>获得1点力量<br>获得1点力量<br>第一回合：32.5%,<br>其余回合:30%<br>无法连续使用2次<br>连击<br>造成1*5点伤害<br>造成1*6点伤害<br>第一回合：62.5%,<br>其余回合:50%<br>无法连续使用3次<br>俯冲<br>造成12点伤害<br>造成14点伤害<br>第一回合:0%,<br>其余回合;20%<br>无法连续使用2次<br>当飞行被全部打破时，异鸟将会坠落并打断当前意图。<br>关于异鸟坠落后的行动请参见下文。<br>异鸟（坠落）<br>Monster id: Byrd_1<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>25;31(26;33)<br>类型<b... | `single_source` | [异鸟](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436744&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/18/a0e9c4e8e9756a1e35a4ecc74a96ed8e.png", "https://imgheybox.max-c.com/web/bbs/2024/08/18/d78fee4b9cb053952380b53731cb0d3c.png"] | `single_source` | [异鸟](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436744&wiki_id=646570) |
| `source.infobox.description` | 25-31 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 异鸟 | `single_source` | [异鸟](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436744&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Byrd<br>|Image  = Byrd.png<br>|HP     = 25-31<br>|AscHP  = 26-33<br>|Powers = {{BD|Flying}} 3 ({{Asc|17|4}})<br>|Debut  = Act 2<br>|Type   = Normal<br>}}<br>{{Power Infobox<br>|Name         = Flying<br>|Image        = Icon Flying.png<br>|Description  = Takes 50% less attack damage. Cancelled if dealt attack damage X times in one turn. Resets charges at the start of next turn if not fully removed.<br>|Type         = Buff<br>|Stacks       = Intensity<br>|BetweenTurn... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
