# 守护者 / The Guardian

> 稳定 ID：`sts1.monster.the_guardian`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：守护者
- English: The Guardian

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | boss |
| `act` | Act 1 |
| `hp_min` | 240 |
| `hp_max` | 240 |
| `ascension_json` | {"ascension_max": 250, "ascension_min": 250, "ascension_raw": "250", "base_max": 240, "base_min": 240, "base_raw": "240"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Charging Up | Defend |  |  | {"text": "Gains 9 Block."} |
| Whirlwind | Attack5 | 5 | 4 | {"text": "Deals 5×4 damage."} |
| Defensive Mode | Buff |  |  | {"text": "Gains (3;4) Sharp Hide."} |
| Roll Attack | Attack2 | 9 |  | {"text": "Deals (9;10) damage."} |
| Vent Steam | DebuffStrong |  |  | {"text": "Applies 2 Weak and 2 Vulnerable."} |
| Twin Slam | Attack4 | 8 | 2 | {"text": "Deals 8×2 damage. Loses Sharp Hide. Gains (30;35 ; 40) Mode Shift, increased by 10 for each time Mode Shift triggered this combat."} |
| Fierce Bash | Attack7 | 32 |  | {"text": "Deals (32;36) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | The Guardian | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 守护者 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "TheGuardian", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["#b~..COOLING...~ NL #b~...DOWN...~", "Defending...", "#r@DESTROY@ NL #r@DESTROY@ NL #r@DESTROY@", "#r@DANGER@ NL #r@DANGER@ NL #r@DANGER@"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["#b~冷却……~ NL #b~…中…~", "防御……", "#r@摧毁@ NL #r@摧毁@ NL #r@摧毁@", "#r@危险@ NL #r@危险@ NL #r@危险@"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Defensive Mode", "Fierce Bash", "Roll", "Twin Slam", "Whirlwind", "Charging Up", "Vent Steam"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["防御模式", "猛烈痛击", "滚动", "双斩", "旋风", "蓄能", "蒸汽喷射"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 250, "ascension_min": 250, "ascension_raw": "250", "base_max": 240, "base_min": 240, "base_raw": "240"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Charging Up` | {"effect": "Gains 9 Block.", "intent": "Defend"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Defensive Mode` | {"effect": "Gains (3;4) Sharp Hide.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Fierce Bash` | {"effect": "Deals (32;36) damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Roll Attack` | {"effect": "Deals (9;10) damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Twin Slam` | {"effect": "Deals 8×2 damage. Loses Sharp Hide. Gains (30;35 ; 40) Mode Shift, increased by 10 for each time Mode Shift triggered this combat.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Vent Steam` | {"effect": "Applies 2 Weak and 2 Vulnerable.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Whirlwind` | {"effect": "Deals 5×4 damage.", "intent": "Attack5"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 守护者<br>Monster id: Guardian<br>怪物信息<br>生命值<br>240;(250;)<br>类型<br>Boss<br>意图<br>蓄能;迎头痛击;蒸汽喷射;旋风斩<br>初始能力<br>形态转换30(35) 4+/(40) 19+<br>备注<br>无<br>（图片未提供文字说明）<br>地图图标<br>攻击模式：<br>攻击方式<br>效果<br>进阶4+<br>充能<br>获得9点格挡<br>获得9点格挡<br>猛烈痛击<br>32伤害<br>36伤害<br>蒸汽喷射<br>造成两回合 虚弱 和 易伤<br>同前<br>旋风斩<br>5*4伤害<br>5*4伤害<br>防御模式：<br>攻击方式<br>效果<br>进阶4+<br>进阶19+<br>防御模式<br>获得反甲3<br>获得反甲3<br>获得反甲4<br>滚动<br>9伤害<br>10伤害<br>10伤害<br>双斩<br>8*2伤害，移除反甲，切换回攻击模式<br>同前<br>同前<br>*<br>备注：受到伤害时，会减少模式转变值，减为0时，会立即切换为防御模式；重新切换回攻击模式... | `single_source` | [守护者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421621&wiki_id=646570) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/14699c7ca4778ed3dc0e4d30c235b5e4.png", "https://cdn.max-c.com/heybox/dailynews/img/56d0551a25b537b950ba54d3a719ba2b.png"] | `single_source` | [守护者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421621&wiki_id=646570) |
| `source.infobox.description` | 240 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 守护者 | `single_source` | [守护者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421621&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = The Guardian<br>|Image  = TheGuardian.png<br>|Icon   = Map-Guardian.png<br>|HP     = 240<br>|AscHP  = 250<br>|Powers = {{BD|Mode Shift}} 30 ({{Asc|9|35}} {{!}} {{Asc|19|40}})<br>|Debut  = Act 1<br>|Type   = Boss<br>}} {{Power Infobox|Mode Shift}} {{Power Infobox|Sharp Hide}}<br>'''The Guardian''' is a [[Boss]] that can appear at the end of [[Act 1]] or the [[Act 3]] event {{E|Mind Bloom}}.<br><br>== Pattern ==<br>{{Intents Table/start|The Guardian}}<br>{{Intents T... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
