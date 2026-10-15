# 大脑袋 / Giant Head

> 稳定 ID：`sts1.monster.giant_head`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：大脑袋
- English: Giant Head

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 3 |
| `hp_min` | 500 |
| `hp_max` | 500 |
| `ascension_json` | {"ascension_max": 520, "ascension_min": 520, "ascension_raw": "520", "base_max": 500, "base_min": 500, "base_raw": "500"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Glare | Debuff |  |  | {"text": "Applies 1 Weak."} |
| It Is Time | Attack7 | 30 |  | {"text": "Deals (30;40) damage, increased by 5 for each time It Is Time has been used this combat up to a maximum of (60;70) damage."} |
| Count | Attack3 | 13 |  | {"text": "Deals 13 damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Giant Head | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 大脑袋 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "GiantHead", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~It~ ~is~ ~time~", "~Good~ ~Bye~", "~Tick~ ~Tock~ NL ~Tick~ ~Tock~", "~Why~ ~are~ ~you~ NL ~still~ ~here?~"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~是时候了~", "~再见~", "~滴~ ~答~ NL ~滴~ ~答~", "~为什么你~ NL ~还在这里？~"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 520, "ascension_min": 520, "ascension_raw": "520", "base_max": 500, "base_min": 500, "base_raw": "500"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Count` | {"effect": "Deals 13 damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Glare` | {"effect": "Applies 1 Weak.", "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.It Is Time` | {"effect": "Deals (30;40) damage, increased by 5 for each time It Is Time has been used this combat up to a maximum of (60;70) damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Giant Head<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>500;(520;)<br>类型<br>精英<br>意图<br>倒数;炫目;是时候了<br>初始能力<br>缓慢<br>备注<br>无<br>行动模式<br>名称<br>效果<br>进阶3+<br>倒数<br>造成13点伤害<br>造成13点伤害<br>眩目<br>给予一层<br>虚弱<br>给予一层<br>虚弱<br>是时候了<br>造成30+5*N点伤害<br>造成40+5*N点伤害<br>*N=本回合前使用“是时候了”的次数<br>前4个回合（前三个回合<br>18+<br>）各有50%的概率使用倒数或眩目，之后的回合它必定使用“是时候了”<br>“是时候了”<br>的伤害上限为60（70<br>3+<br>）<br>它会从第一个回合开始从5（4<br>18+<br>）开始倒数，倒数完后会说一句“是时候了”，即开始进行此攻击意图。<br>应对方法<br>它的高血量和稳定的攻击力使很多牌组很难将其击杀，然而因为缓慢效果，每个回合能够打出相当数量卡牌的高伤害卡组会很容... | `single_source` | [大脑袋](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436792&wiki_id=646570) |
| `source.infobox.description` | 500 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 大脑袋 | `single_source` | [大脑袋](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436792&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Giant Head<br>|Image  = GiantHead.png<br>|HP     = 500<br>|AscHP  = 520<br>|Powers = {{BD|Slow}}<br>|Debut  = Act 3<br>|Type   = Elite<br>}} {{Power Infobox|Slow}}<br>Giant Head is an [[Elite]] enemy found exclusively in [[Act 3]].<br><br>== Pattern ==<br>{{Intents Table/start|Giant Head}}<br>{{Intents Table/row<br>|Name   = Count<br>|Intent = Attack3<br>|Effect = Deals 13 damage.}}<br>{{Intents Table/row<br>|Name   = Glare<br>|Intent = Debuff<br>|Effect = Applies... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
