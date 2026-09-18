# 神秘术士 / Mystic

> 稳定 ID：`sts1.monster.mystic`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：神秘术士
- English: Mystic

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 2 |
| `hp_min` | 48 |
| `hp_max` | 56 |
| `ascension_json` | {"ascension_max": 58, "ascension_min": 50, "base_max": 56, "base_min": 48} |
| `encounter_notes` | Split member from sts1.monster.centurion_and_mystic; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Heal | Buff |  |  | {"text": "All enemies heal (16;20) HP."} |
| Buff | Buff |  |  | {"text": "All enemies gain (2;3 ; 4) Strength."} |
| Attack | DebuffAttack2 | 8 |  | {"text": "Deals (8;9) damage. Applies 2 Frail."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [百夫长与神秘术士 / Centurion and Mystic](../encounters/sts1_encounter_act2_hard_centurion_and_mystic.md)
- `has_member` → [百夫长与神秘术士 / Centurion and Mystic](sts1_monster_centurion_and_mystic.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Mystic | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 神秘术士 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Healer", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `mapping.cross_source.monster_group_member` | {"decided_by": "group_page_anchor_and_game_key", "english_anchor": "Mystic", "english_group_page": "https://slaythespire.wiki.gg/wiki/Centurion_and_Mystic", "entity_id": "sts1.monster.mystic", "game_key": "Healer", "match": ["group_page_anchor", "official_game_key", "dedicated_chinese_article"], "zh_url": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436699&wiki_id=646570"} | `agreed` | [Monsters | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Monsters) |
| `monster.hp.range` | {"ascension_max": 58, "ascension_min": 50, "ascension_raw": "50-58", "base_max": 56, "base_min": 48, "base_raw": "48-56"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Attack` | {"effect": {"text": "Deals (8;9) damage. Applies 2 Frail."}, "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Buff` | {"effect": {"text": "All enemies gain (2;3 ; 4) Strength."}, "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Heal` | {"effect": {"text": "All enemies heal (16;20) HP."}, "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | （图片未提供文字说明）<br>怪物分布<br>（图片未提供文字说明）<br>行动类型<br>（图片未提供文字说明）<br>行动规律<br>（图片未提供文字说明）<br>如果有人受伤，必定使用治疗。但不会连续使用三次。<br>只要可能，强化的概率略高于脆弱打击<br>进阶 3以下<br>不可能连续使用三次脆弱打击；不可能连续使用三次强化。<br>进阶 17+<br>脆弱打击后必定强化；不可能连续使用三次强化。 | `single_source` | [神秘术士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436699&wiki_id=646570) |
| `source.title_text` | 神秘术士 | `single_source` | [神秘术士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436699&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Mystic<br>|Image  = Healer.png<br>|HP     = 48-56<br>|AscHP  = 50-58<br>|Debut  = Act 2<br>|Type   = Normal<br>}}<br>'''Mystic''' is a normal [[Monsters|Enemy]] encountered exclusively in [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|Mystic}}<br>{{Intents Table/row<br>|Name   = Attack<br>|Intent = DebuffAttack2<br>|Effect = Deals (8;{{Asc|2|9}}) damage. Applies 2 {{BD|Frail}}.<br>|GivesToPlayer = Frail<br>}}<br>{{Intents Table/row<br>|Name   = Buff<br>|... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
