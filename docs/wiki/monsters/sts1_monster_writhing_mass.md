# 扭曲团块 / Writhing Mass

> 稳定 ID：`sts1.monster.writhing_mass`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：扭曲团块
- English: Writhing Mass

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 3 |
| `hp_min` | 160 |
| `hp_max` | 160 |
| `ascension_json` | {"ascension_max": 175, "ascension_min": 175, "ascension_raw": "175", "base_max": 160, "base_min": 160, "base_raw": "160"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Block Attack | DefendAttack4 | 15 |  | {"text": "Deals (15;16) damage. Gains 16 Block."} |
| Big Hit | Attack7 | 32 |  | {"text": "Deals (32;38) damage."} |
| Multi Hit | Attack5 | 7 | 3 | {"text": "Deals (7×3;9×3) damage."} |
| Parasite | DebuffStrong |  |  | {"text": "Permanently adds a Parasite to your deck."} |
| Debuff Attack | DebuffAttack3 | 10 |  | {"text": "Deals (10;12) damage. Applies 2 Weak and 2 Vulnerable."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [扭曲团块 / Writhing Mass](../encounters/sts1_encounter_act3_hard_writhing_mass.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Writhing Mass | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 扭曲团块 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "WrithingMass", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 175, "ascension_min": 175, "ascension_raw": "175", "base_max": 160, "base_min": 160, "base_raw": "160"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Big Hit` | {"effect": "Deals (32;38) damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Block Attack` | {"effect": "Deals (15;16) damage. Gains 16 Block.", "intent": "DefendAttack4"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Debuff Attack` | {"effect": "Deals (10;12) damage. Applies 2 Weak and 2 Vulnerable.", "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Multi Hit` | {"effect": "Deals (7×3;9×3) damage.", "intent": "Attack5"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Parasite` | {"effect": "Permanently adds a Parasite to your deck.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Writhing Mass<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>160;(175;)<br>类型<br>普通<br>意图<br>寄生;盾击;三连击;猛攻;状态攻击<br>初始能力<br>扭动<br>；<br>柔韧<br>3<br>备注<br>无<br>怪物分布<br>行动类型<br>行动规律<br>第一回合<br>连击、盾击、凋零各占1/3概率<br>新的回合<br>只要可能，寄生、重击、凋零、盾击、连击的概率之间的比例总是相当于<br>1:1:2:3:3<br>不会出现两个连续的相同的行动意图<br>一场战斗只会使用一次寄生<br>玩家对策<br>扭曲团块不会出现两个连续的相同的行动意图，如果你希望它不要执行当前意图中的行动，只需造成一次攻击伤害。<br>扭曲团块的寄生行动是能永久改变卡组的唯一外在因素（除开荒疫）。尽量使扭曲团块不要使出寄生——但也有些时候这样做并不值得。<br>通过凋零施加易伤后，重击乃至连击的伤害往往会高到难以格档。如果没有<br>人工制品<br>且不能很快结束战斗战斗，尽量使扭曲团块不要使用凋零。<b... | `single_source` | [扭曲团块](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438466&wiki_id=646570) |
| `source.infobox.description` | 160 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 扭曲团块 | `single_source` | [扭曲团块](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438466&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Writhing Mass<br>|Image  = WrithingMass.png<br>|HP     = 160<br>|AscHP  = 175<br>|Powers = {{BD|Malleable}} 4 <br> {{BD|Reactive}}<br>|Debut  = Act 3<br>|Type   = Normal<br>}}<br>{{Power Infobox|Malleable}} <br>{{Power Infobox<br>|Name         = Reactive<br>|Image        = Icon Reactive.png<br>|Description  = Upon receiving attack damage, changes its [[Intent]].<br>|Type         = Buff<br>|Stacks       = Does not stack<br>|BetweenTurns = <br>|Cap          = <br>}}... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
