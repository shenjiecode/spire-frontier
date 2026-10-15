# 圆球行者 / Orb Walker

> 稳定 ID：`sts1.monster.orb_walker`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：圆球行者
- English: Orb Walker

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 3 |
| `hp_min` | 90 |
| `hp_max` | 96 |
| `ascension_json` | {"ascension_max": 102, "ascension_min": 92, "ascension_raw": "92-102", "base_max": 96, "base_min": 90, "base_raw": "90-96"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Laser | DebuffAttack3 | 10 |  | {"text": "Deals (10;11) damage. Adds a Burn into your draw pile, and another Burn into your discard pile."} |
| Claw | Attack4 | 15 |  | {"text": "Deals (15;16) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [圆球行者 / Orb Walker](../encounters/sts1_encounter_act3_easy_orb_walker.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Orb Walker | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 圆球行者 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Orb Walker", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["Initiating NL shields."] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["护盾 NL 开启。"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Strength Up"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["强化"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 102, "ascension_min": 92, "ascension_raw": "92-102", "base_max": 96, "base_min": 90, "base_raw": "90-96"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Claw` | {"effect": "Deals (15;16) damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Laser` | {"effect": "Deals (10;11) damage. Adds a Burn into your draw pile, and another Burn into your discard pile.", "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Orb Walker<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>90;96(92;102)<br>类型<br>普通<br>意图<br>灼伤打击;重击<br>初始能力<br>力量提升3（5） 17+<br>备注<br>无<br>行动<br>名称<br>效果<br>进阶2+<br>概率<br>备注<br>灼伤打击<br>造成10点伤害，并向抽牌堆与弃牌堆分别塞入一张灼伤<br>造成11点伤害，并向抽牌堆与弃牌堆分别塞入一张灼伤<br>60%<br>不能连续3回合使用<br>重击<br>造成15点伤害<br>造成16点伤害<br>40%<br>不能连续3回合使用<br>策略<br>尽量快速的去击杀圆球行者，它的力量成长十分迅速。 | `single_source` | [圆球行者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15437647&wiki_id=646570) |
| `source.infobox.description` | 90-96 | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 圆球行者 | `single_source` | [圆球行者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15437647&wiki_id=646570) |
| `source.wikitext` | {{Under Construction}}{{Enemy Infobox<br>|Name   = Orb Walker<br>|Image  = OrbWalker.png<br>|HP     = 90-96<br>|AscHP  = 92-102<br>|Powers = {{BD|Strength Up}} 3 ({{Asc|17|5}})<br>|Debut  = Act 3<br>|Type   = Normal<br>}} {{Power Infobox|Strength Up}}<br>'''Orb Walker''' is a normal [[Monsters|Enemy]] encountered exclusively in [[Act 3]]. It can also be encountered in the {{E|Mysterious Sphere}} [[Event]].<br><br>== Pattern ==<br>{{Intents Table/start|Orb Walker}}<br>{{Intents Table/row<br>|N... | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
