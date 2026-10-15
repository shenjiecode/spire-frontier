# 天罚 / Nemesis

> 稳定 ID：`sts1.monster.nemesis`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：天罚
- English: Nemesis

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 3 |
| `hp_min` | 185 |
| `hp_max` | 185 |
| `ascension_json` | {"ascension_max": 200, "ascension_min": 200, "ascension_raw": "200", "base_max": 185, "base_min": 185, "base_raw": "185"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Tri Burn | Debuff |  |  | {"text": "Adds (3;5) Burns into your discard pile."} |
| Tri Attack | Attack4 | 6 | 3 | {"text": "Deals (6×3;7×3) damage."} |
| Scythe | Attack7 | 45 |  | {"text": "Deals 45 damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Nemesis | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 天罚 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Nemesis", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 200, "ascension_min": 200, "ascension_raw": "200", "base_max": 185, "base_min": 185, "base_raw": "185"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Scythe` | {"effect": "Deals 45 damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tri Attack` | {"effect": "Deals (6×3;7×3) damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Tri Burn` | {"effect": "Adds (3;5) Burns into your discard pile.", "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Nemesis<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>185;(200;)<br>类型<br>精英<br>意图<br>灼伤;三连击;镰刀斩<br>初始能力<br>无<br>备注<br>无<br>行动模式<br>名称<br>效果<br>进阶3+<br>进阶18+<br>概率<br>灼伤<br>将3张灼伤<br>洗入弃牌堆<br>将3张灼伤<br>洗入弃牌堆<br>将3张灼伤<br>洗入弃牌堆<br>第一回合50%<br>其余回合35%<br>三连击<br>造成6x3点伤害<br>造成6x3点伤害<br>造成6x3点伤害<br>第一回合50%<br>其余回合35%<br>镰刀斩<br>造成45点伤害<br>造成45点伤害<br>造成45点伤害<br>第一回合0%<br>其余回合30%<br>三连击无法连续使用3次<br>镰刀斩无法连续使用2次<br>注意<br>天罚在偶数回合将获得一层无实体<br>尽管天罚的攻击并不会随着回合推进而强化，但如果玩家缺乏 消耗 手段，那么将会被成吨的 灼伤 所淹没，因此玩家需要避免将战斗拖得过长。<b... | `single_source` | [天罚](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436798&wiki_id=646570) |
| `source.infobox.description` | 185 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 天罚 | `single_source` | [天罚](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436798&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Nemesis<br>|Image  = Nemesis.png<br>|HP     = 185<br>|AscHP  = 200<br>|Powers = {{BD|Intangible}} every other turn<br>|Debut  = Act 3<br>|Type   = Elite<br>}} {{Power Infobox|Intangible}}<br>Nemesis is an [[Elite]] enemy found exclusively in [[Act 3]].<br><br>== Pattern ==<br>{{Intents Table/start|Nemesis}}<br>{{Intents Table/row<br>|Name   = Tri Attack<br>|Intent = Attack4<br>|Effect = Deals (6×3;{{Asc|3|7×3}}) damage.}}<br>{{Intents Table/row<br>|Name   = Tri Bu... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
