# 小黑 / Darkling

> 稳定 ID：`sts1.monster.darkling`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：小黑
- English: Darkling

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 3 |
| `hp_min` | 48 |
| `hp_max` | 56 |
| `ascension_json` | {"ascension_max": 59, "ascension_min": 50, "ascension_raw": "50-59", "base_max": 56, "base_min": 48, "base_raw": "48-56"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Reincarnate | Buff |  |  | {"text": "Revives with 50% HP."} |
| Harden | Defend |  |  | {"text": "Gains 12 Block(.; and 2 Strength.)"} |
| Regrowing... | Unknown |  |  | {"text": "Does nothing."} |
| Nip | Attack2 |  |  | {"text": "Deals N damage. N = Number between (7-11;9-13), chosen at the start of combat."} |
| Chomp | Attack4 | 8 | 2 | {"text": "Deals (8×2;9×2) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [3 只小黑 / 3 Darklings](../encounters/sts1_encounter_act3_easy_3_darklings.md)
- `contains_monster` → [3 只小黑 / 3 Darklings](../encounters/sts1_encounter_act3_hard_3_darklings.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Darkling | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 小黑 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Darkling", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["Regrowing..."] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["重生中……"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Chomp! Chomp!"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["啊呜！啊呜！"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 59, "ascension_min": 50, "ascension_raw": "50-59", "base_max": 56, "base_min": 48, "base_raw": "48-56"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Chomp` | {"effect": "Deals (8×2;9×2) damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Harden` | {"effect": "Gains 12 Block(.; and 2 Strength.)", "intent": "Defend"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Nip` | {"effect": "Deals N damage. N = Number between (7-11;9-13), chosen at the start of combat.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Regrowing...` | {"effect": "Does nothing.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Reincarnate` | {"effect": "Revives with 50% HP.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Darkling<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>48;56(50;59)<br>类型<br>普通<br>意图<br>重击;双击;硬化;重生;再生<br>初始能力<br>生命链接<br>备注<br>无<br>行动类型<br>行动<br>意图类型<br>效果<br>效果（进阶2+）<br>折叠效果（进阶17+）<br>单击<br>攻击<br>造成7～11伤害<br>造成9～13伤害<br>造成9～13伤害<br>双击<br>攻击<br>造成8伤害2次<br>造成9伤害2次<br>造成9伤害2次<br>防御<br>格档<br>获得12格档<br>获得12格档<br>获得12格档获得2力量<br>生命链接<br>强化<br>重生至一半的生命值获得生命链接<br>重生至一半的生命值获得生命链接<br>重生至一半的生命值获得生命链接<br>对于同一只小黑，其单击伤害在一场战斗中是固定的，在战斗开始时已确定。<br>由于生命链接，只要场上仍有其他小黑，被杀死的小黑会进入不可选中状态，本回合不作任何行动，但下回合将重生至一半的生命值。重... | `single_source` | [小黑](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438057&wiki_id=646570) |
| `source.infobox.description` | 48-56 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 小黑 | `single_source` | [小黑](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438057&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Darkling<br>|Image  = Darkling.png<br>|HP     = 48-56<br>|AscHP  = 50-59<br>|Powers = {{BD|Life Link}}<br>|Debut  = Act 3<br>|Type   = Normal<br>}} <br>{{Power Infobox<br>|Name         = Life Link<br>|Image        = Icon LifeLink.png<br>|Description  = If other {{M|Darkling|Darklings}} are still alive, revives in 2 turns.<br>|Type         = Buff<br>|Stacks       = Does not stack<br>|BetweenTurns = <br>|Cap          = <br>}}<br>Darkling is a normal [[Monsters|Enemy... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
