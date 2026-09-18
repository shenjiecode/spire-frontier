# 尖刺史莱姆（中） / Spike Slime (M)

> 稳定 ID：`sts1.monster.spike_slime_m`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：尖刺史莱姆（中）
- English: Spike Slime (M)

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 28 |
| `hp_max` | 32 |
| `ascension_json` | {"ascension_max": 34, "ascension_min": 29, "base_max": 32, "base_min": 28} |
| `encounter_notes` | Split member from sts1.monster.spike_slimes; source section retains group-page context. |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Flame Tackle | DebuffAttack2 | 8 |  | {"text": "Deals (8;10) damage. Adds a Slimed into your discard pile."} |
| Lick | Debuff |  |  | {"text": "Applies 1 Frail."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [小型史莱姆 / Small Slimes](../encounters/sts1_encounter_act1_easy_small_slimes.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"alternatives": [["Spike Slime(M)", "Acid Slime (S)"], ["Acid Slime (M)", "Spike Slime (S)"]], "mode": "exclusive_alternatives", "raw": "Either (Spike Slime(M) + Acid Slime (S)) or (Acid Slime (M) + Spike Slime (S))"}}`
- `contains_monster` → [序幕暴徒 / Exordium Thugs](../encounters/sts1_encounter_act1_hard_exordium_thugs.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Louse (any) or Medium Slime (any) Second Enemy: Slaver (any), Cultist, or Looter", "slots": {"first": "Louse (any) or Medium Slime (any)", "second": "Slaver (any), Cultist, or Looter"}}}`
- `contains_monster` → [序幕野兽 / Exordium Wildlife](../encounters/sts1_encounter_act1_hard_exordium_wildlife.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Fungi Beast or Jaw Worm Second Enemy: Louse (any) or Medium Slime (any)", "slots": {"first": "Fungi Beast or Jaw Worm", "second": "Louse (any) or Medium Slime (any)"}}}`
- `has_member` → [尖刺史莱姆 / Spike Slimes](sts1_monster_spike_slimes.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Spike Slime (M) | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 尖刺史莱姆（中） | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SpikeSlime_M", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Lick"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["舔舔"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 34, "ascension_min": 29, "ascension_raw": "29-34", "base_max": 32, "base_min": 28, "base_raw": "28-32"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Flame Tackle` | {"effect": {"text": "Deals (8;10) damage. Adds a Slimed into your discard pile."}, "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Lick` | {"effect": {"text": "Applies 1 Frail."}, "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Spike Slime (M)<br>|Image  = SpikeSlimeM.png<br>|HP     = 28-32<br>|AscHP  = 29-34<br>|Debut  = Act 1<br>|Type   = Normal<br>}}<br>'''Spike Slime (M)''' is a normal [[Monsters|Enemy]] found exclusively in Act 1.<br><br>=== Pattern ===<br>{{Intents Table/start|Spike Slime (M)}}<br>{{Intents Table/row<br>|Name   = Lick<br>|Intent = Debuff<br>|Effect = Applies 1 {{BD|Frail}}.}}<br>{{Intents Table/row<br>|Name   = Flame Tackle<br>|Intent = DebuffAttack2<br>|Effect = D... | `single_source` | [P3 wiki.gg API batch: monster 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sentry|Giant_Head|Bronze_Automaton|The_Collector|Shelled_Parasite|Jaw_Worm|Slime_Boss|Gremlin_Leader|Louses|Taskmaster|Darkling|Byrd|Slimes|Sentry|Slavers|Awakened_One|Hexaghost|Snecko|Spire_Growth|Gremlin_Nob&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
