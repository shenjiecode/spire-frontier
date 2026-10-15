# 酸液史莱姆（中） / Acid Slime (M)

> 稳定 ID：`sts1.monster.acid_slime_m`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：酸液史莱姆（中）
- English: Acid Slime (M)

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 28 |
| `hp_max` | 32 |
| `ascension_json` | {"ascension_max": 34, "ascension_min": 29, "base_max": 32, "base_min": 28} |
| `encounter_notes` | Split member from sts1.monster.acid_slimes; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Lick | Debuff |  |  | {"text": "Applies 1 Weak."} |
| Corrosive Spit | DebuffAttack2 | 7 |  | {"text": "Deals (7;8) damage. Adds a Slimed into your discard pile."} |
| Tackle | Attack3 | 10 |  | {"text": "Deals (10;12) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [小型史莱姆 / Small Slimes](../encounters/sts1_encounter_act1_easy_small_slimes.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": [["Spike Slime(M)", "Acid Slime (S)"], ["Acid Slime (M)", "Spike Slime (S)"]], "mode": "exclusive_alternatives", "raw": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))"}}`
- `contains_monster` → [序幕暴徒 / Exordium Thugs](../encounters/sts1_encounter_act1_hard_exordium_thugs.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Louse (any) or Medium Slime (any) Second Enemy: Slaver (any), Cultist, or Looter", "slots": {"first": "Louse (any) or Medium Slime (any)", "second": "Slaver (any), Cultist, or Looter"}}}`
- `contains_monster` → [序幕野兽 / Exordium Wildlife](../encounters/sts1_encounter_act1_hard_exordium_wildlife.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `has_member` → [酸液史莱姆 / Acid Slimes](sts1_monster_acid_slimes.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Acid Slime (M) | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 酸液史莱姆（中） | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "AcidSlime_M", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Corrosive Spit", "Lick"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["腐蚀喷吐", "舔舔"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 34, "ascension_min": 29, "ascension_raw": "29-34", "base_max": 32, "base_min": 28, "base_raw": "28-32"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Corrosive Spit` | {"effect": {"text": "Deals (7;8) damage. Adds a Slimed into your discard pile."}, "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Lick` | {"effect": {"text": "Applies 1 Weak."}, "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tackle` | {"effect": {"text": "Deals (10;12) damage."}, "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Acid Slime (M)<br>|Image  = AcidSlimeM.png<br>|HP     = 28-32<br>|AscHP  = 29-34<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>'''Acid Slime (M)''' is a normal [[Monsters|Enemy]] found exclusively in Act 1.<br><br>=== Pattern ===<br>{{Intents Table/start|Acid Slime (M)}}<br>{{Intents Table/row<br>|Name   = Corrosive Spit<br>|Intent = DebuffAttack2<br>|Effect = Deals (7;{{Asc|2|8}}) damage. Adds a {{C|Slimed}} into your discard pile.}}<br>{{Intents Table/row<br>|... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
