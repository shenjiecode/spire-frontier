# 被拣选者 / Chosen

> 稳定 ID：`sts1.monster.chosen`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：被拣选者
- English: Chosen

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 2 |
| `hp_min` | 95 |
| `hp_max` | 95 |
| `ascension_json` | {"asc_hp": 98} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Hex | DebuffStrong |  |  | {"text": "Applies Hex."} |
| Debilitate | DebuffAttack3 | 10 |  | {"text": "Deals (10;12) damage. Applies 2 Vulnerable."} |
| Drain | DebuffDefend |  |  | {"text": "Applies 3 Weak. Gain 3 Strength."} |
| Zap | Attack4 | 18 |  | {"text": "Deals (18;21) damage."} |
| Poke | Attack3 | 5 |  | {"text": "Deals (5×2;6×2) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Chosen | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 被拣选者 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Chosen", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~Suffer...~"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~挣扎吧……~"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.move.Debilitate` | {"effect": "Deals (10;12) damage. Applies 2 Vulnerable.", "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Drain` | {"effect": "Applies 3 Weak. Gain 3 Strength.", "intent": "DebuffDefend"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Hex` | {"effect": "Applies Hex.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Poke` | {"effect": "Deals (5×2;6×2) damage.", "intent": "Attack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Zap` | {"effect": "Deals (18;21) damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 被拣选者<br>怪物分布<br>（图片未提供文字说明）<br>行动类型<br>（图片未提供文字说明）<br>行动规律<br>（图片未提供文字说明）<br>玩家对策<br>邪咒对需要打出大量非攻击牌的卡组的影响非常恐怖。<br>可以利用人工制品来抵消它。<br>铁甲战士的牌中有一些能够从邪咒产生的晕眩中取得收益，如请黑暗之拥、进化、无惧疼痛、火焰吐息，甚至能利用邪咒来达成无限。<br>邪咒是向抽牌堆添加请输晕眩，当抽牌堆的牌很少时，打出非攻击牌所提高的抽到晕眩的可能性会更多。一般来说希望尽量平衡每回合抽到的晕眩，以确保稳定的防御和过牌。<br>邪咒的效果是在打出非攻击牌后触发<br>会在杂技、独门技术抽牌后触发（会导致华丽收场无法打出）<br>用非攻击牌弃掉本能反应，先触发邪咒再抽牌 | `single_source` | [被拣选者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408980&wiki_id=646570) |
| `source.infobox.description` | 95-99 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 被拣选者 | `single_source` | [被拣选者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408980&wiki_id=646570) |
| `source.wikitext` | {{Ambox<br>| title = WARNING!<br>| color = red<br>| icon = GremlinNob.png<br>| message = ''This page is under construction. Information may be wrong or incomplete.''<br>}}<br><br><br>{{Enemy Infobox<br>|Name   = Chosen<br>|Image  = Chosen.png<br>|HP     = 95-99<br>|AscHP  = 98-103<br>|Debut  = Act 2<br>|Type   = Normal<br>}}<br>{{Power Infobox|Hex}}'''The Chosen''' is a normal [[Monsters|Enemy]] encountered exclusively in [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|Chosen}}<br>{{... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
