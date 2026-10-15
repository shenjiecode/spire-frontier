# 拜蛇术士 / Reptomancer

> 稳定 ID：`sts1.monster.reptomancer`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：拜蛇术士
- English: Reptomancer

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | elite |
| `act` | Act 3 |
| `hp_min` | 180 |
| `hp_max` | 190 |
| `ascension_json` | {"ascension_max": 200, "ascension_min": 190, "ascension_raw": "190-200", "base_max": 190, "base_min": 180, "base_raw": "180-190"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Spawn Dagger | Unknown |  |  | {"text": "Summons (1 Dagger;2 Daggers) (up to a maximum of 4)."} |
| Big Bite | Attack7 | 30 |  | {"text": "Deals (30;34) damage."} |
| Snake Strike | DebuffAttack6 | 13 | 2 | {"text": "Deals (13×2;16×2) damage. Applies 1 Weak."} |

## 相关条目

- `has_member` → [匕首 / Dagger](sts1_game_candidate_monster_dagger.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Reptomancer | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 拜蛇术士 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Reptomancer", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 200, "ascension_min": 190, "ascension_raw": "190-200", "base_max": 190, "base_min": 180, "base_raw": "180-190"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Big Bite` | {"effect": "Deals (30;34) damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Explode` | {"effect": "Deals 25 damage. Dies", "intent": "Attack6"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Snake Strike` | {"effect": "Deals (13×2;16×2) damage. Applies 1 Weak.", "intent": "DebuffAttack6"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Spawn Dagger` | {"effect": "Summons (1 Dagger;2 Daggers) (up to a maximum of 4).", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Wound` | {"effect": "Deals 9 damage. Adds a Wound into your discard pile.", "intent": "DebuffAttack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 拜蛇术士<br>Monster id: Reptomancer<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>180;190(190;200)<br>类型<br>精英<br>意图<br>召唤;重击;连击<br>初始能力<br>无<br>备注<br>战斗开始时拥有两个匕首协助作战<br>怪物分布<br>（图片未提供文字说明）<br>行动类型<br>名称<br>效果<br>进阶3+<br>进阶18+<br>召唤<br>生成1匕首作为爪牙<br>生成1匕首作为爪牙<br>生成2匕首作为爪牙<br>重击<br>造成30点伤害<br>造成34点伤害<br>造成34点伤害<br>连击<br>造成13x2点伤害<br>给予1层虚弱<br>造成16x2点伤害<br>给予1层虚弱<br>造成16x2点伤害<br>给予1层虚弱<br>行动规律<br>（图片未提供文字说明）<br>未连续多次使用相同行动时，三个行动的权重均等，除非：<br>场上有四只匕首时不会召唤，召唤的权重转移给连击。<br>连击、重击不会连续两次<br>召唤不会连续三次<br>匕首<br>Monster id:... | `single_source` | [拜蛇术士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436794&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/18/738a5ac2e71e85ba30256670e754bc1d.png", "https://imgheybox.max-c.com/web/bbs/2024/08/18/89bd33588c5a04ce3cb1a2149960c263.png", "https://imgheybox.max-c.com/web/bbs/2024/08/18/8a35a52d39bc9ad755df6ab27346b26e.png", "https://imgheybox.max-c.com/web/bbs/2024/08/31/14ebeb5ec9466d0ea4e9b64744bbb97a.png", "https://imgheybox.max-c.com/web/bbs/2024/08/31/239420667ffd8d03b5ffa49da7df515e.png"] | `single_source` | [拜蛇术士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436794&wiki_id=646570) |
| `source.infobox.description` | 180-190 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 拜蛇术士 | `single_source` | [拜蛇术士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436794&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Reptomancer<br>|Image  = Reptomancer.png<br>|HP     = 180-190<br>|AscHP  = 190-200<br>|Debut  = Act 3<br>|Type   = Elite<br>}}<br>Reptomancer is an [[Elite]] enemy found exclusively in [[Act 3]].<br><br>== Pattern ==<br>{{Intents Table/start|Reptomancer}}<br>{{Intents Table/row<br>|Name   = Spawn Dagger<br>|Intent = Unknown<br>|Effect = Summons (1 {{M|Dagger}};{{Asc|18|2}} {{M|Dagger|Daggers}}) (up to a maximum of 4).}}<br>{{Intents Table/row<br>|Name   = Big Bite... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
