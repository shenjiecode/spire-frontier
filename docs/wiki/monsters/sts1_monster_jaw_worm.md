# 大颚虫 / Jaw Worm

> 稳定 ID：`sts1.monster.jaw_worm`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：大颚虫
- English: Jaw Worm

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 40 |
| `hp_max` | 44 |
| `ascension_json` | {"ascension_max": 46, "ascension_min": 42, "ascension_raw": "42-46", "base_max": 44, "base_min": 40, "base_raw": "40-44"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Chomp | Attack3 | 11 |  | {"text": "Deals (11;12) damage."} |
| Thrash | DefendAttack2 | 7 |  | {"text": "Deals 7 damage. Gains 5 Block."} |
| Bellow | DefendBuff |  |  | {"text": "Gains (3;4 ; 5) Strength. Gains (6;9) Block."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [大颚虫 / Jaw Worm](../encounters/sts1_encounter_act1_easy_jaw_worm.md)
- `contains_monster` → [序幕野兽 / Exordium Wildlife](../encounters/sts1_encounter_act1_hard_exordium_wildlife.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `contains_monster` → [大颚虫群 / Jaw Worm Horde](../encounters/sts1_encounter_act3_hard_jaw_worm_horde.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "3x Jaw Worms (that start combat with the effects of Bellow) Bellow: On Ascension 0 onwards: Gain 3 Strength and 6 Block On Ascension 2 onwards: Gain 4 Strength and 6 Block On Ascension 17 onwards: Gain 5 Strength and 9 Block"}}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Jaw Worm | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 大颚虫 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "JawWorm", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Bellow", "Thrash"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["咆哮", "抽打"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 46, "ascension_min": 42, "ascension_raw": "42-46", "base_max": 44, "base_min": 40, "base_raw": "40-44"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Bellow` | {"effect": "Gains (3;4 ; 5) Strength. Gains (6;9) Block.", "intent": "DefendBuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Chomp` | {"effect": "Deals (11;12) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Thrash` | {"effect": "Deals 7 damage. Gains 5 Block.", "intent": "DefendAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 大颚虫<br>（图片未提供文字说明）<br>怪物分布<br>（图片未提供文字说明）<br>行动类型<br>（图片未提供文字说明）<br>行动规律<br>（图片未提供文字说明）<br>在第一阶段：塔底中<br>第一回合必定使用重击<br>之后有45%概率使用咆哮,30%概率使用盾击，25%概率使用重击<br>不可能连续三次盾击；不可能连续两次重击；不可能连续两次咆哮<br>在第三阶段：深处中<br>所有的大颚虫起始获得3/4/5力量和6/6/9点护甲，相当于一次咆哮的效果。<br>其第一回合未必使用重击，而是参照第一阶段的规律进行攻击。<br>轶事<br>其名称和外观在一定程度上，与巨口有着某些关联。 | `single_source` | [大颚虫](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15420602&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/17/b3c5196e64cb7bf126759dea13a1bbd6.png"] | `single_source` | [大颚虫](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15420602&wiki_id=646570) |
| `source.infobox.description` | 40-44 | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 大颚虫 | `single_source` | [大颚虫](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15420602&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>| Name   = Jaw Worm<br>| Image  = JawWorm.png<br>| HP     = 40-44<br>| AscHP  = 42-46<br>| Debut  = Act 1<br>| Type   = Normal<br>}}<br>{{Enemy Infobox<br>| Name   = Jaw Worm (Hard)<br>| Image  = JawWorm.png<br>| HP     = 40-44<br>| AscHP  = 42-46<br>| Powers = {{BD|Strength}} 3 ({{Asc|2|4}}/{{Asc|17|5}})<br> {{BD|Block}}  6 ({{Asc|17|9}})<br>| Debut  = Act 3<br>| Type   = Normal<br>}}<br>'''Jaw Worm''' is a normal [[Monsters|Enemy]] that can show up in Act 1, and has a har... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
