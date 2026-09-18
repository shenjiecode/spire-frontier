# 觉醒者 / Awakened One

> 稳定 ID：`sts1.monster.awakened_one`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：觉醒者
- English: Awakened One

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | boss |
| `act` | Act 3 |
| `hp_min` | 300 |
| `hp_max` | 300 |
| `ascension_json` | {"ascension_max": 320, "ascension_min": 320, "ascension_raw": "320", "base_max": 300, "base_min": 300, "base_raw": "300"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Tackle | Attack7 | 10 | 3 | {"text": "Deals 10×3 damage."} |
| Rebirth | Unknown |  |  | {"text": "Heals to full HP. Removes all Debuffs]. Loses Curiosity."} |
| Soul Strike | Attack5 | 6 | 4 | {"text": "Deals 6×4 damage."} |
| Slash | Attack5 | 20 |  | {"text": "Deals 20 damage."} |
| Sludge | DebuffAttack4 | 18 |  | {"text": "Deals 18 damage. Adds a Void into your draw pile."} |
| Dark Echo | Attack7 | 40 |  | {"text": "Deals 40 damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Awakened One | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 觉醒者 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "AwakenedOne", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~Grr~ ~.~ ~.~ ~.~", "~No~ ~.~ ~.~ ~.~ ~no~ ~.~ ~.~ NL ~.~ ~.~ ~no~ ~.~ ~.~ ~.~"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~咕嗷。。。~", "~不。。。不。。~ NL ~。。不。。。~"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Soul Strike", "Dark Echo", "Cleanse", "Sludge"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["灵魂攻击", "黑暗回音", "净化", "污泥"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 320, "ascension_min": 320, "ascension_raw": "320", "base_max": 300, "base_min": 300, "base_raw": "300"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Dark Echo` | {"effect": "Deals 40 damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Rebirth` | {"effect": "Heals to full HP. Removes all Debuffs]. Loses Curiosity.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Slash` | {"effect": "Deals 20 damage.", "intent": "Attack5"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Sludge` | {"effect": "Deals 18 damage. Adds a Void into your draw pile.", "intent": "DebuffAttack4"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Soul Strike` | {"effect": "Deals 6×4 damage.", "intent": "Attack5"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tackle` | {"effect": "Deals 10×3 damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 觉醒者<br>觉醒前：<br>Monster id: AwakenedOne<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>300;(320;)<br>类型<br>Boss<br>意图<br>劈斩;灵魂打击;重生<br>初始能力<br>再生（敌人）<br>10（15） 19+<br>;好奇<br>1(2) 19+<br>备注<br>战斗开始时，获得4<br>力量<br>4+<br>;战斗伊始时拥有2个邪教徒协助参战。<br>地图图标<br>战斗开始时​额外有两个邪教徒（咔咔）参加战斗，觉醒者死亡时若咔咔仍存活将会自动撤退；进阶4及以上战斗开始时获得2力量。<br>觉醒前意图：<br>能力/行动<br>进阶4以下<br>进阶4-进阶18<br>进阶19及以上<br>好奇<br>每打出一张能力牌，觉醒者获得1力量<br>同前<br>每打出一张能力牌，觉醒者获得2力量<br>再生<br>回合结束后回复10生命<br>同前<br>回合结束后回复15生命<br>重击<br>造成20伤害<br>同前<br>同前<br>灵魂打击<br>造成6×4伤害<br>同前<br>同前... | `single_source` | [觉醒者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9957006&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/18/08536ee75f4702d13fb40e6673b34c29.png", "https://imgheybox.max-c.com/web/bbs/2024/08/18/55626173dba3f830b6f020b595398ac5.png"] | `single_source` | [觉醒者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9957006&wiki_id=646570) |
| `source.infobox.description` | 300 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 觉醒者 | `single_source` | [觉醒者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9957006&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Awakened One<br>|Image  = AwakenedOne.png<br>|Icon   = Map-Awakened.png<br>|HP     = 300<br>|AscHP  = 320<br>|Powers = {{BD|Regenerate}} 10 ({{Asc|19|15}}) <br> {{BD|Curiosity}} 1 ({{Asc|19|2}}) <br> ({{BD|Strength}} 2 {{Asc|4}})<br>|Debut  = Act 3<br>|Type   = Boss<br>}} {{Power Infobox|Curiosity}} {{Power Infobox|Regenerate}} {{Power Infobox|Unawakened}}<br>The Awakened One is a [[Boss]] found at the end of [[Act 3]].<br><br>== Pattern ==<br>{{Intents Table/star... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
