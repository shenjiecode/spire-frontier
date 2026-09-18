# 反冲机 / Repulsor

> 稳定 ID：`sts1.monster.repulsor`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：反冲机
- English: Repulsor

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 3 |
| `hp_min` | 29 |
| `hp_max` | 35 |
| `ascension_json` | {"ascension_max": 38, "ascension_min": 31, "base_max": 35, "base_min": 29} |
| `encounter_notes` | Split member from sts1.monster.shapes; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Attack | Attack3 | 11 |  | {"text": "Deals (11;13) damage."} |
| Daze | Debuff |  |  | {"text": "Adds 2 Dazed into your draw pile."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [3 个三机械 / 3 Shapes](../encounters/sts1_encounter_act3_easy_3_shapes.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 3, "mode": "sample_without_replacement", "pool": ["2x Repulsor", "2x Exploder", "2x Spiker"], "raw": "3 Shapes chosen from [2x Repulsor, 2x Exploder, 2x Spiker]"}}`
- `contains_monster` → [4 个三机械 / 4 Shapes](../encounters/sts1_encounter_act3_hard_4_shapes.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 4, "mode": "sample_without_replacement", "pool": ["2x Repulsor", "2x Exploder", "2x Spiker"], "raw": "4 Shapes chosen from [2x Repulsor, 2x Exploder, 2x Spiker]"}}`
- `contains_monster` → [圆球守护者 + 2 个三机械 / Spheric Guardian + 2 Shapes](../encounters/sts1_encounter_act3_hard_spheric_guardian_2_shapes.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"choose_count": 2, "mode": "independent_choices", "raw": "2 Shapes are independently chosen with equal probability and 1 Spheric Guardian"}}`
- `has_member` → [三机械 / Shapes](sts1_monster_shapes.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Repulsor", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `monster.hp.range` | {"ascension_max": 38, "ascension_min": 31, "ascension_raw": "31-38", "base_max": 35, "base_min": 29, "base_raw": "29-35"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Attack` | {"effect": {"text": "Deals (11;13) damage."}, "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Daze` | {"effect": {"text": "Adds 2 Dazed into your draw pile."}, "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Repulsor<br>|Image  = Repulsor.png<br>|HP     = 29-35<br>|AscHP  = 31-38<br>|Debut  = Act 3<br>|Type   = Normal<br>}}<br>{{Small Card Infobox|Dazed}}<br>Repulsor repeatedly gives the player {{C|Dazed}}.<br><br>=== Pattern ===<br>{{Intents Table/start|Repulsor}}<br>{{Intents Table/row<br>|Name   = Daze<br>|Intent = Debuff<br>|Effect = Adds 2 {{C|Dazed}} into your draw pile.}}<br>{{Intents Table/row<br>|Name   = Attack<br>|Intent = Attack3<br>|Effect = Deals (11;{{A... | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
