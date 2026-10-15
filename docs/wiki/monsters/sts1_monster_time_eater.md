# 时间吞噬者 / Time Eater

> 稳定 ID：`sts1.monster.time_eater`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：时间吞噬者
- English: Time Eater

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | boss |
| `act` | Act 3 |
| `hp_min` | 456 |
| `hp_max` | 456 |
| `ascension_json` | {"ascension_max": 480, "ascension_min": 480, "ascension_raw": "480", "base_max": 456, "base_min": 456, "base_raw": "456"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Reverberate | Attack5 | 7 | 3 | {"text": "Deals (7×3;8×3) damage."} |
| Haste | Buff |  |  | {"text": "Removes all Debuffs]. Heals to 50% HP. (;Gains 32 Block.)"} |
| Ripple | DebuffDefend |  |  | {"text": "Gains 20 Block. Applies 1 Vulnerable, 1 Weak(.; and 1 Frail.)"} |
| Head Slam | DebuffAttack6 | 26 |  | {"text": "Deals (26;32) damage. Applies 1 Draw Reduction. (;Adds 2 Slimed into your discard pile.)"} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Time Eater | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 时间吞噬者 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "TimeEater", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~Ah...~ NL ~..company...~", "~Foolish..~ NL @FOOOLISH!@", "~Never....~ NL ~...liked..~ NL ~..you...~"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["~啊……~ NL ~…居然有人来了…~", "~愚蠢……~ NL @何等愚蠢！@", "~一直……~ NL ~……都不…~ NL ~…喜欢你……~"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 480, "ascension_min": 480, "ascension_raw": "480", "base_max": 456, "base_min": 456, "base_raw": "456"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Haste` | {"effect": "Removes all Debuffs]. Heals to 50% HP. (;Gains 32 Block.)", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Head Slam` | {"effect": "Deals (26;32) damage. Applies 1 Draw Reduction. (;Adds 2 Slimed into your discard pile.)", "intent": "DebuffAttack6"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Reverberate` | {"effect": "Deals (7×3;8×3) damage.", "intent": "Attack5"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Ripple` | {"effect": "Gains 20 Block. Applies 1 Vulnerable, 1 Weak(.; and 1 Frail.)", "intent": "DebuffDefend"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 时间吞噬者<br>Monster id: Time Eater<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>456;(480;)<br>类型<br>Boss<br>意图<br>时光回响;迎头痛击;时空涟漪;迎头痛击;急速逆时<br>初始能力<br>时间扭曲<br>备注<br>无<br>（图片未提供文字说明）<br>地图图标<br>能力/行动<br>进阶4以下<br>进阶4-进阶18<br>进阶19及以上<br>时间扭曲<br>每当你打出12张牌，你的回合强制结束，且时间吞噬者获得2力量<br>同前<br>同前<br>连击<br>造成7×3伤害<br>造成8×3伤害<br>同前<br>重击<br>造成26伤害，下两回合开始时抽牌数-1<br>造成32伤害，下两回合开始时抽牌数-1<br>造成32伤害，下两回合开始时抽牌数-1，将两张粘液加入弃牌堆<br>格挡<br>获得20格挡，施加1层易伤和1层虚弱<br>同前<br>获得20格挡，施加1层易伤、1层脆弱和1层虚弱<br>“愚蠢”<br>将生命值恢复至一半并移除所有负面效果<br>同前<br>将生命值恢复至一... | `single_source` | [时间吞噬者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432030&wiki_id=646570) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/fb03bb4c7e5afd5123ba2a1e3fbf3398.png", "https://imgheybox.max-c.com/web/bbs/2024/10/09/bfb7ac808390b73136cc1529a8047304.png"] | `single_source` | [时间吞噬者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432030&wiki_id=646570) |
| `source.infobox.description` | 456 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 时间吞噬者 | `single_source` | [时间吞噬者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432030&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>| Name   = Time Eater<br>| Image  = TimeEater.png<br>| Icon   = Map-TimeEater.png<br>| HP     = 456<br>| AscHP  = 480<br>| Powers = {{BD|Time Warp}}<br>| Debut  = Act 3<br>| Type   = Boss<br>}}<br>{{Power Infobox<br>| Name         = Time Warp<br>| Image        = Icon TimeWarp.png<br>| Description  = Whenever you play a certain number of cards, ends your turn and gains X {{BD|Strength}}.<br>| Type         = Buff<br>| Stacks       = Intensity<br>| BetweenTurns = <br>| Cap    ... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
