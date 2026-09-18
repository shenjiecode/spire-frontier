# 百夫长 / Centurion

> 稳定 ID：`sts1.monster.centurion`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：百夫长
- English: Centurion

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 2 |
| `hp_min` | 76 |
| `hp_max` | 80 |
| `ascension_json` | {"ascension_max": 83, "ascension_min": 78, "base_max": 80, "base_min": 76} |
| `encounter_notes` | Split member from sts1.monster.centurion_and_mystic; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Fury | Attack4 | 6 | 3 | {"text": "Deals (6×3;7×3) damage."} |
| Slash | Attack3 | 12 |  | {"text": "Deals (12;14) damage."} |
| Protect | Defend |  |  | {"text": "Mystic gains (15;20) Block. If alone, instead gains (15;20) Block."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [百夫长与神秘术士 / Centurion and Mystic](../encounters/sts1_encounter_act2_hard_centurion_and_mystic.md)
- `has_member` → [百夫长与神秘术士 / Centurion and Mystic](sts1_monster_centurion_and_mystic.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Centurion | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 百夫长 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Centurion", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `mapping.cross_source.monster_group_member` | {"decided_by": "group_page_anchor_and_game_key", "english_anchor": "Centurion", "english_group_page": "https://slaythespire.wiki.gg/wiki/Centurion_and_Mystic", "entity_id": "sts1.monster.centurion", "game_key": "Centurion", "match": ["group_page_anchor", "official_game_key", "dedicated_chinese_article"], "zh_url": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436697&wiki_id=646570"} | `agreed` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `monster.hp.range` | {"ascension_max": 83, "ascension_min": 78, "ascension_raw": "78-83", "base_max": 80, "base_min": 76, "base_raw": "76-80"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Fury` | {"effect": {"text": "Deals (6×3;7×3) damage."}, "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Protect` | {"effect": {"text": "Mystic gains (15;20) Block. If alone, instead gains (15;20) Block."}, "intent": "Defend"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Slash` | {"effect": {"text": "Deals (12;14) damage."}, "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 怪物分布<br>行动类型<br>行动规律<br>只要可能，保护的概率是攻击的两倍。<br>不可能连续三次攻击；不可能连续三次保护。<br>神秘术士死亡后，不再保护而是连击。<br>（图片未提供文字说明） | `single_source` | [百夫长](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436697&wiki_id=646570) |
| `source.title_text` | 百夫长 | `single_source` | [百夫长](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436697&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Centurion<br>|Image  = Centurion.png<br>|HP     = 76-80<br>|AscHP  = 78-83<br>|Debut  = Act 2<br>|Type   = Normal<br>}}<br>'''Centurion''' is a normal [[Monsters|Enemy]] encountered exclusively in [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|Centurion}}<br>{{Intents Table/row<br>|Name   = Slash<br>|Intent = Attack3<br>|Effect = Deals (12;{{Asc|2|14}}) damage.<br>}}<br>{{Intents Table/row<br>|Name   = Protect<br>|Intent = Defend<br>|Effect = {{M|Mystic}... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
