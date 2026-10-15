# 真菌兽 / Fungi Beast

> 稳定 ID：`sts1.monster.fungi_beast`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：真菌兽
- English: Fungi Beast

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 22 |
| `hp_max` | 28 |
| `ascension_json` | {"ascension_max": 28, "ascension_min": 24, "ascension_raw": "24-28", "base_max": 28, "base_min": 22, "base_raw": "22-28"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Grow | Buff |  |  | {"text": "Gains (3;4 ; 5) Strength."} |
| Bite | Attack2 | 6 |  | {"text": "Deals 6 damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [2 只真菌兽 / 2 Fungi Beasts](../encounters/sts1_encounter_act1_hard_2_fungi_beasts.md)
- `contains_monster` → [序幕野兽 / Exordium Wildlife](../encounters/sts1_encounter_act1_hard_exordium_wildlife.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `contains_monster` → [带壳寄生怪与真菌兽 / Shelled Parasite and Fungi](../encounters/sts1_encounter_act2_hard_shelled_parasite_and_fungi.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "1 Shelled Parasite, 1 Fungi Beast"}}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Fungi Beast | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 真菌兽 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "FungiBeast", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Grow"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["生长"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 28, "ascension_min": 24, "ascension_raw": "24-28", "base_max": 28, "base_min": 22, "base_raw": "22-28"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Bite` | {"effect": "Deals 6 damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Grow` | {"effect": "Gains (3;4 ; 5) Strength.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 真菌兽<br>（图片未提供文字说明）<br>怪物分布<br>（图片未提供文字说明）<br>行动<br>（图片未提供文字说明）<br>行动规律<br>（图片未提供文字说明）<br>只要可能，攻击的概率就略高于生长。<br>不可能连续三次攻击；不可能连续两次生长。<br>策略<br>因为真菌兽死亡时给予的 易伤 会让其同伴伤害增高，要控制击杀时机。<br>使用群体攻击的牌，如 愁云惨淡 或 顺劈斩 ，同时击杀所有怪物。<br>关注它同伴的行动，尽量在它的同伴不攻击的时候击杀真菌兽。 | `single_source` | [真菌兽](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15420669&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/17/5c252d30df358c4040aac9606e001ef3.png"] | `single_source` | [真菌兽](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15420669&wiki_id=646570) |
| `source.infobox.description` | 22-28 | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 真菌兽 | `single_source` | [真菌兽](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15420669&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Fungi Beast<br>|Image  = FungiBeast.png<br>|HP     = 22-28<br>|AscHP  = 24-28<br>|Powers = {{BD|Spore Cloud}} 2<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>{{Power Infobox|Spore Cloud}}<br>'''Fungi Beast''' is a normal [[Monsters|Enemy]] that appears in [[Act 1]] and [[Act 2]]. It also appears in the {{E|Hypnotizing Colored Mushrooms}} [[Event]] in groups of three.<br><br>== Pattern ==<br>{{Intents Table/start|Fungi Beast}}<br>{{Intents Table/row<br>|Name   = ... | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
