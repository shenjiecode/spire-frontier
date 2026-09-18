# 奴隶主 / Slavers

> 稳定 ID：`sts1.monster.slavers`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：奴隶主
- English: Slavers

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 46 |
| `hp_max` | 46 |
| `ascension_json` | {"asc_hp": 48} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Stab | Attack3 | 12 |  | {"text": "Deals (12;13) damage."} |
| Stab | Attack3 | 13 |  | {"text": "Deals (13;14) damage."} |
| Entangle | DebuffStrong |  |  | {"text": "Applies 1 Entangled."} |
| Rake | DebuffAttack2 | 7 |  | {"text": "Deals (7;8) damage. Applies (1;2) Weak."} |
| Scrape | DebuffAttack2 | 8 |  | {"text": "Deals (8;9) damage. Applies (1;2) Vulnerable."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Slaver | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 奴隶贩子 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SlaverBlue", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Rake"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["耙伤"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Entangle` | {"effect": "Applies 1 Entangled.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Rake` | {"effect": "Deals (7;8) damage. Applies (1;2) Weak.", "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Scrape` | {"effect": "Deals (8;9) damage. Applies (1;2) Vulnerable.", "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Stab` | {"effect": "Deals (12;13) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 红奴隶主<br>（图片未提供文字说明）<br>意图<br>（图片未提供文字说明）<br>第一回合必定使用刺伤。<br>之后每回合有25%的概率使用丢网，否则就一直遵循着刮伤、刮伤、刺伤的顺序进行攻击。<br>进阶 17+:行动规律有所改变，丢网前遵循着刮伤、刺伤的顺序，不再连续两回合使用刮伤。<br>蓝奴隶主<br>（图片未提供文字说明）<br>意图<br>（图片未提供文字说明）<br>进阶 17+:行动规律有所改变，不再连续两回合使用耙伤。 | `single_source` | [奴隶主](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15417595&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/17/187fffa891df8263e41dc8bfb6f2d7a9.png", "https://imgheybox.max-c.com/web/bbs/2024/08/17/2c74e4f4dd782230e9a4a167211aa01b.png"] | `single_source` | [奴隶主](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15417595&wiki_id=646570) |
| `source.infobox.description` | 46-50 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 奴隶主 | `single_source` | [奴隶主](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15417595&wiki_id=646570) |
| `source.wikitext` | = Blue Slaver =<br>{{Enemy Infobox<br>|Name   = Blue Slaver<br>|Image  = SlaverBlue.png<br>|HP     = 46-50<br>|AscHP  = 48-52<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>'''Blue Slaver''' is a normal [[Monsters|Enemy]] found in Act 1 and Act 2. They can also appear in [[Elite]] combats and {{E|The Colosseum}} [[Event]].<br><br>== Pattern ==<br>{{Intents Table/start|Blue Slaver}}<br>{{Intents Table/row<br>|Name   = Stab<br>|Intent = Attack3<br>|Effect = Deals (12;{{Asc|2|13}}) damage.}}<br... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
