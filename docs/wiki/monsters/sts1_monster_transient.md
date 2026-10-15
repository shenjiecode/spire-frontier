# 倏忽魔 / Transient

> 稳定 ID：`sts1.monster.transient`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：倏忽魔
- English: Transient

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 3 |
| `hp_min` | 999 |
| `hp_max` | 999 |
| `ascension_json` | {"base_max": 999, "base_min": 999, "base_raw": "999"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Attack | Attack7 |  |  | {"text": "Deals (20+N; 30+N) damage. N = Current turn, multiplied by 10."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [倏忽魔 / Transient](../encounters/sts1_encounter_act3_hard_transient.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Transient | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 倏忽魔 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Transient", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"base_max": 999, "base_min": 999, "base_raw": "999"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Attack` | {"effect": "Deals (20+N; 30+N) damage. N = Current turn, multiplied by 10.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Transient<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>999;(999;)<br>类型<br>普通<br>意图<br>猛攻<br>初始能力<br>消逝5(6) 17+;变幻<br>备注<br>无<br>行动模式<br>其中，N=本场战斗的回合数<br>· 如果玩家通过非常规手段清除了倏忽魔的消逝，它不会在回合结束时死亡且伤害会持续增长下去。<br>相关成就<br>若在倏忽魔消逝前将其击杀，可获得倏忽即逝成就 | `single_source` | [倏忽魔](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438060&wiki_id=646570) |
| `source.infobox.description` | 999 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 倏忽魔 | `single_source` | [倏忽魔](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438060&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Transient<br>|Image  = Transient.png<br>|HP     = 999<br>|Powers = {{BD|Fading}} 5 ({{Asc|17|6}}) <br> {{BD|Shifting}}<br>|Debut  = Act 3<br>|Type   = Normal<br>}} {{Power Infobox|Fading}} {{Power Infobox|Shifting}}<br>The Transient is a normal [[Monsters|Enemy]] found exclusively in [[Act 3]].<br><br>== Pattern ==<br>{{Intents Table/start|Transient}}<br>{{Intents Table/row<br>|Name   = Attack<br>|Intent = Attack7<br>|Effect = Deals (20+N; {{Asc|2|30+N}}) damage. ... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
