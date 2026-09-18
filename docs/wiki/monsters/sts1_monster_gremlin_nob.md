# 地精大块头 / Gremlin Nob

> 稳定 ID：`sts1.monster.gremlin_nob`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：地精大块头
- English: Gremlin Nob

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 1 |
| `hp_min` | 82 |
| `hp_max` | 82 |
| `ascension_json` | {"asc_hp": 85} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Skull Bash | DebuffAttack2 | 6 |  | {"text": "Deals (6;8) damage. Applies 2 Vulnerable."} |
| Bellow | Buff |  |  | {"text": "Gains (2;3) Enrage."} |
| Bull Rush | Attack3 | 14 |  | {"text": "Deals (14;16) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Gremlin Nob | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 地精大块头 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "GremlinNob", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@RRrroohrrRGHHhhh!!@"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@啊嗷嗷呜嗷！！@"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Skull Bash", "Bull Rush"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["颅骨重击", "蛮牛冲撞"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Bellow` | {"effect": "Gains (2;3) Enrage.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Bull Rush` | {"effect": "Deals (14;16) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Skull Bash` | {"effect": "Deals (6;8) damage. Applies 2 Vulnerable.", "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 行为<br>进阶 18+：第二回合必定是颅骨重击，随后第三回合必定使用蛮牛冲撞，此后一直重复该顺序。<br>轶事<br>地精大块头的模型参考了“战锤40K”中的“Ork Nob”。<br>根据地精之角的文字描述，地精大块头会一直保持生长，直到死亡为止。<br>事件竞技场的第二轮战斗原本是由两只地精大块头组成的，但在2019年1月17日时修改为了一个面具大师和地精大块头。<br>（图片未提供文字说明） | `single_source` | [地精大块头](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421612&wiki_id=646570) |
| `source.infobox.description` | 82-86 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 地精大块头 | `single_source` | [地精大块头](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421612&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>| Name   = Gremlin Nob<br>| Image  = GremlinNob.png<br>| HP     = 82-86<br>| AscHP  = 85-90<br>| Debut  = Act 1<br>| Type   = Elite<br>}} <br>{{Power Infobox<br>| Name         = Enrage<br>| Image        = Icon Anger.png<br>| Description  = Whenever you play a {{QueryLink|Cards|type:Skill|Skill}} card, gains X {{BD|Strength}}.<br>| Type         = Buff<br>| Stacks       = Intensity<br>| BetweenTurns = <br>| Cap          = <br>| GivesToEnemy = Strength<br>}}<br>'''Gremlin Nob'... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
