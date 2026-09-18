# 酸液史莱姆 / Acid Slimes

> 稳定 ID：`sts1.monster.acid_slimes`  
> 类别：`monster`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：酸液史莱姆
- English: Acid Slimes

## monster 合页上下文

本页对应来源中的组合页，只保留来源正文和 `has_member` 关系。生命值与行动请查看下方成员页面；不会把某个成员的数值投影到父页。

| 字段 | 值 |
| --- | --- |
| `encounter_notes` | Grouped wiki page only; structured HP/actions live on its has_member child entities. |

## 相关条目

- `has_member` → [酸液史莱姆（大） / Acid Slime (L)](sts1_monster_acid_slime_l.md)
- `has_member` → [酸液史莱姆（中） / Acid Slime (M)](sts1_monster_acid_slime_m.md)
- `has_member` → [酸液史莱姆（小） / Acid Slime (S)](sts1_monster_acid_slime_s.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Acid Slime (L) | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 酸液史莱姆（中） | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "AcidSlime_S", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Corrosive Spit", "Lick"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["腐蚀喷吐", "舔舔"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 73, "ascension_min": 67, "ascension_raw": "67-73", "base_max": 70, "base_min": 64, "base_raw": "64-70"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Corrosive Spit` | {"effect": "Deals (11;12) damage. Adds 2 Slimed into your discard pile.", "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Flame Tackle` | {"effect": "Deals (16;18) damage. Adds 2 Slimed into your discard pile.", "intent": "DebuffAttack4"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Lick` | {"effect": "Applies (2;3) Frail.", "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Split` | {"effect": "Disappears and spawns 2 Spike Slimes (M) with its current HP.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tackle` | {"effect": "Deals (5;6) damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 酸液史莱姆（大）<br>（图片未提供文字说明）<br>怪物分布<br>（图片未提供文字说明）<br>行动类型<br>（图片未提供文字说明）<br>行动规律<br>（图片未提供文字说明）<br>进阶17以下<br>只要可能，腐蚀喷吐、重击、舔舔的权重为3:4:3。<br>不可能连续进行两次重击，其余行动不可能连续进行三次。<br>进阶 17以上<br>只要可能，腐蚀喷吐、重击、舔舔的权重为4:3:3。<br>不可能连续进行两次舔舔，其余行动不可能连续进行三次。<br>酸液史莱姆（中）<br>（图片未提供文字说明）<br>怪物分布<br>（图片未提供文字说明）<br>行动类型<br>（图片未提供文字说明）<br>行动规律<br>（图片未提供文字说明）<br>进阶17以下<br>只要可能，腐蚀喷吐、重击、舔舔的权重为3:4:3。<br>不可能连续进行两次重击，其余行动不可能连续进行三次。<br>进阶 17以上<br>只要可能，腐蚀喷吐、重击、舔舔的权重为4:4:2。<br>不可能连续进行两次舔舔，其余行动不可能连续进行三次。<br>酸液史莱姆（小）<br>（图片未提供文字说明）<br>... | `single_source` | [酸液史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411814&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/16/0286d9ec4dab15fbbfd5833ae036db06.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/029675d0d6b21a2b0ea45fa4b9f37c81.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/2c480220fffeea895acb8cd44435b504.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/687cb53e08d77166f7953bc8360dcca2.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/773473d54cfe0617da30116cce0691e7.png", "https://imgheybox.max-c.com/web/bbs/2024/08/16/af0d96c24b9b7... | `single_source` | [酸液史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411814&wiki_id=646570) |
| `source.infobox.description` | 64-70 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 酸液史莱姆 | `single_source` | [酸液史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411814&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{TOC limit|2}}<br>== Spike Slime (L) ==<br>{{Enemy Infobox<br>|Name   = Spike Slime (L)<br>|Image  = SpikeSlimeL.png<br>|HP     = 64-70<br>|AscHP  = 67-73<br>|Powers = {{BD|Split}}<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>{{Power Infobox|Split}}<br>'''Spike Slime (L)''' is a normal [[Monsters|Enemy]] found exclusively in Act 1.<br><br>=== Pattern ===<br>{{Intents Table/start|Spike Slime (L)}}<br>{{Intents Table/row<br>|Name   = Lick<br>|Intent = Debuff<br>... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
