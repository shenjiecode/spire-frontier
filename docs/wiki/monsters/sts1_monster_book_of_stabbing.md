# 扎人的书 / Book of Stabbing

> 稳定 ID：`sts1.monster.book_of_stabbing`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：扎人的书
- English: Book of Stabbing

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 2 |
| `hp_min` | 160 |
| `hp_max` | 164 |
| `ascension_json` | {"ascension_max": 172, "ascension_min": 168, "ascension_raw": "168-172", "base_max": 164, "base_min": 160, "base_raw": "160-164"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Big Stab | Attack5 | 21 |  | {"text": "Deals (21;24) damage."} |
| Multi Stab | Attack3 | 6 |  | {"text": "Deals (6×N;7×N) damage. (N = Number of times Multi Stab was used this combat, plus 2.; On , N = Current turn, plus 1.)"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Book of Stabbing | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 扎人的书 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "BookOfStabbing", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 172, "ascension_min": 168, "ascension_raw": "168-172", "base_max": 164, "base_min": 160, "base_raw": "160-164"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Big Stab` | {"effect": "Deals (21;24) damage.", "intent": "Attack5"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Multi Stab` | {"effect": "Deals (6×N;7×N) damage. (N = Number of times Multi Stab was used this combat, plus 2.; On , N = Current turn, plus 1.)", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | （图片未提供文字说明）<br>它战斗开始时自带疼痛戳刺效果。<br>行为<br>（图片未提供文字说明） | `single_source` | [扎人的书](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432038&wiki_id=646570) |
| `source.infobox.description` | 160-164 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 扎人的书 | `single_source` | [扎人的书](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432038&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Book of Stabbing<br>|Image  = BookOfStabbing.png<br>|HP     = 160-164<br>|AscHP  = 168-172<br>|Powers = {{BD|Painful Stabs}}<br>|Debut  = Act 2<br>|Type   = Elite<br>}} {{Power Infobox|Painful Stabs}}<br>Book of Stabbing is an [[Elite]] enemy found exclusively in [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|Book of Stabbing}}<br>{{Intents Table/row<br>|Name   = Multi Stab<br>|Intent = Attack3<br>|Effect = Deals (6×N;{{Asc|3|7×N}}) damage. (N = Number o... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
