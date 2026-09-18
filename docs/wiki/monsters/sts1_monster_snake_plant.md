# 蛇花 / Snake Plant

> 稳定 ID：`sts1.monster.snake_plant`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：蛇花
- English: Snake Plant

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 2 |
| `hp_min` | 75 |
| `hp_max` | 79 |
| `ascension_json` | {"ascension_max": 82, "ascension_min": 78, "ascension_raw": "78-82", "base_max": 79, "base_min": 75, "base_raw": "75-79"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Chomp Chomp | Attack5 | 7 | 3 | {"text": "Deals (7×3;8×3) damage."} |
| Enfeebling Spores | DebuffStrong |  |  | {"text": "Applies 2 Frail and 2 Weak."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [蛇花 / Snake Plant](../encounters/sts1_encounter_act2_hard_snake_plant.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Snake Plant | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 蛇花 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "SnakePlant", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Enfeebling Spores"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["虚弱孢子"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 82, "ascension_min": 78, "ascension_raw": "78-82", "base_max": 79, "base_min": 75, "base_raw": "75-79"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Chomp Chomp` | {"effect": "Deals (7×3;8×3) damage.", "intent": "Attack5"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Enfeebling Spores` | {"effect": "Applies 2 Frail and 2 Weak.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: Snake Plant<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>75;79(78;82)<br>类型<br>普通<br>意图<br>虚弱孢子；噬咬<br>初始能力<br>柔韧<br>3<br>备注<br>无<br>怪物分布<br>编号<br>组合<br>位置<br>概率<br>1<br>蛇花<br>第二阶段：城市<br>强怪池<br>21%<br>行动类型<br>名称<br>效果<br>进阶2+<br>进阶17+<br>虚弱孢子<br>给予2层虚弱和2层破防<br>给予2层虚弱和2层破防<br>给予2层虚弱和2层破防<br>噬咬<br>造成7点伤害3次<br>造成8点伤害3次<br>造成8点伤害3次<br>行动规律<br>（图片未提供文字说明）<br>在进阶17以下<br>只要可能，噬咬的概率是虚弱孢子的两倍<br>不可能连续两次虚弱孢子；不可能连续三次噬咬<br>在进阶17及以上<br>总是进行两次噬咬一次虚弱孢子的循环。虚弱孢子的首次使用有35%（约1/3）的概率在第一回合，23%（约1/4）的概率在第二回合，42%（约2/5... | `single_source` | [蛇花](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436704&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/18/b64ca9585434402fd5aa9db2702ceeda.png", "https://imgheybox.max-c.com/web/bbs/2024/08/18/eb067839e1353858badc8a722e8009fd.png"] | `single_source` | [蛇花](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436704&wiki_id=646570) |
| `source.infobox.description` | 75-79 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 蛇花 | `single_source` | [蛇花](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436704&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = Snake Plant<br>|Image  = SnakePlant.png<br>|HP     = 75-79<br>|AscHP  = 78-82<br>|Powers = {{BD|Malleable}} 3<br>|Debut  = Act 2<br>|Type   = Normal<br>}} {{Power Infobox|Malleable}}<br>Snake Plant is a normal [[Monsters|Enemy]] found only in [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|Snake Plant}}<br>{{Intents Table/row<br>|Name   = Chomp Chomp<br>|Intent = Attack5<br>|Effect = Deals (7×3;{{Asc|2|8×3}}) damage.}}<br>{{Intents Table/row<br>|Name   = ... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
