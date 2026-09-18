# 尖刺史莱姆（小） / Spike Slime (S)

> 稳定 ID：`sts1.monster.spike_slime_s`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：尖刺史莱姆（小）
- English: Spike Slime (S)

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 10 |
| `hp_max` | 14 |
| `ascension_json` | {"ascension_max": 15, "ascension_min": 11, "base_max": 14, "base_min": 10} |
| `encounter_notes` | Split member from sts1.monster.spike_slimes; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Tackle | Attack2 | 5 |  | {"text": "Deals (5;6) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [小型史莱姆 / Small Slimes](../encounters/sts1_encounter_act1_easy_small_slimes.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": [["Spike Slime(M)", "Acid Slime (S)"], ["Acid Slime (M)", "Spike Slime (S)"]], "mode": "exclusive_alternatives", "raw": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))"}}`
- `contains_monster` → [史莱姆群 / Swarm of Slimes](../encounters/sts1_encounter_act1_hard_swarm_of_slimes.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "fixed_details", "raw": "3x Spike Slime (S) and 2x Acid Slime (S)"}}`
- `has_member` → [尖刺史莱姆 / Spike Slimes](sts1_monster_spike_slimes.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Spike Slime (S) | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 尖刺史莱姆（小） | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SpikeSlime_S", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 15, "ascension_min": 11, "ascension_raw": "11-15", "base_max": 14, "base_min": 10, "base_raw": "10-14"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tackle` | {"effect": {"text": "Deals (5;6) damage."}, "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Spike Slime (S)<br>|Image  = SpikeSlimeS.png<br>|HP     = 10-14<br>|AscHP  = 11-15<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>'''Spike Slime (S)''' is a normal [[Monsters|Enemy]] that is exclusively found in Act 1.<br><br>=== Pattern ===<br>{{Intents Table/start|Spike Slime (S)}}<br>{{Intents Table/row<br>|Name   = Tackle<br>|Intent = Attack2<br>|Effect = Deals (5;{{Asc|2|6}}) damage.}}<br>{{Intents Table/end}}<br><br>=== Found With ===<br><br>===== Act 1 ===... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
