# 虱虫 / Louses

> 稳定 ID：`sts1.monster.louses`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：虱虫
- English: Louses

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 10 |
| `hp_max` | 10 |
| `ascension_json` | {"asc_hp": 11} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Grow | Buff |  |  | {"text": "Gains (3;4) Strength."} |
| Spit Web | Debuff |  |  | {"text": "Applies 2 Weak."} |
| Bite | Attack2 | 5 |  | {"text": "Deals N damage. N = Number between (5-7;6-8), chosen at the start of combat."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Louse | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 虱虫 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "FuzzyLouseDefensive", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Spit Web"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["吐网"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Bite` | {"effect": "Deals N damage. N = Number between (5-7;6-8), chosen at the start of combat.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Grow` | {"effect": "Gains (3;4) Strength.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Spit Web` | {"effect": "Applies 2 Weak.", "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 红虱虫<br>（图片未提供文字说明）<br>行为模式<br>（图片未提供文字说明）<br>进阶 17以上：其无法连续两回合使用生长,无法连续三回合使用噬咬。<br>绿虱虫<br>（图片未提供文字说明）<br>行为模式<br>（图片未提供文字说明） | `single_source` | [虱虫](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411825&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/16/de720149b3bd48677bc186a6ce7818e4.png", "https://imgheybox.max-c.com/web/bbs/2024/08/17/4b712785a230385296e199db6fb29be5.png", "https://imgheybox.max-c.com/web/bbs/2024/08/17/f04d5394833b2d7a38ae40381c4dddc3.png"] | `single_source` | [虱虫](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411825&wiki_id=646570) |
| `source.infobox.description` | 10-15 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 虱虫 | `single_source` | [虱虫](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411825&wiki_id=646570) |
| `source.wikitext` | == Red Louse ==<br>{{Enemy Infobox<br>|Name   = Red Louse<br>|Image  = RedLouse.png<br>|HP     = 10-15<br>|AscHP  = 11-16<br>|Powers = {{BD|Curl Up}} N, where N is random between 3-7 ({{Asc|7|4-8}} {{!}} {{Asc|17|9-12}})<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>{{Power Infobox|Curl Up}}<br>The '''Red Louse''' is a normal [[Monsters|Enemy]] found exclusively in Act 1.<br><br>=== Pattern ===<br>{{Intents Table/start|Red Louse}}<br>{{Intents Table/row<br>|Name   = Bite<br>|Intent = Attack... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
