# 邪教徒 / Cultist

> 稳定 ID：`sts1.monster.cultist`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：邪教徒
- English: Cultist

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 1 |
| `hp_min` | 48 |
| `hp_max` | 54 |
| `ascension_json` | {"ascension_max": 56, "ascension_min": 50, "ascension_raw": "50-56", "base_max": 54, "base_min": 48, "base_raw": "48-54"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Incantation | Buff |  |  | {"text": "Gains (3;4 ; 5) Ritual."} |
| Dark Strike | Attack2 | 6 |  | {"text": "Deals 6 damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [邪教徒 / Cultist](../encounters/sts1_encounter_act1_easy_cultist.md)
- `contains_monster` → [序幕暴徒 / Exordium Thugs](../encounters/sts1_encounter_act1_hard_exordium_thugs.md) ；条件：`{"member_origin": "details", "mode": "conditional_member", "selection_rule": {"mode": "slot_alternatives", "raw": "First enemy: Louse (any) or Medium Slime (any) Second Enemy: Slaver (any), Cultist, or Looter", "slots": {"first": "Louse (any) or Medium Slime (any)", "second": "Slaver (any), Cultist, or Looter"}}}`
- `contains_monster` → [3 名邪教徒 / 3 Cultists](../encounters/sts1_encounter_act2_hard_3_cultists.md)
- `contains_monster` → [邪教徒与被拣选者 / Cultist and Chosen](../encounters/sts1_encounter_act2_hard_cultist_and_chosen.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Cultist | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 邪教徒 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Cultist", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@MY@ @POWER@ @IS@ NL @UNMATCHED!@", "@YOU@ @DO@ @NOT@ NL @BELONG@ @HERE!@", "~My~ ~powers~ NL ~were~ ~matched...~"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@我的力量@ NL @无人能及！@", "@你不属于@ NL @这里！@", "~我的力量~ NL ~有人能及啊……~"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["", "", "Incantation"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["", "", "念咒"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 56, "ascension_min": 50, "ascension_raw": "50-56", "base_max": 54, "base_min": 48, "base_raw": "48-54"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Dark Strike` | {"effect": "Deals 6 damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Incantation` | {"effect": "Gains (3;4 ; 5) Ritual.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 邪教徒（Cultist）是杀戮尖塔中一种类人型的怪物。<br>（图片未提供文字说明）<br>出现<br>（图片未提供文字说明）<br>行为<br>（图片未提供文字说明）<br>策略<br>邪教徒是玩家早期会遇到的怪物之一。此时玩家的牌组一般较弱。建议放弃过多的防御以便在下一回合击杀邪教徒，从而避免更多的战损。<br>第二阶段的3个邪教徒较为棘手，从第二回合开始就会造成增长很快的伤害，这要求玩家有快速击杀单个敌人或强大的群伤能力，如旋风斩。<br>邪教徒+被拣选者的组合则中规中矩，一般的打法是优先击杀邪教徒。<br>第三阶段的邪教徒作为觉醒者的“爪牙”出现。战斗策略仍是优先击杀邪教徒，因而群伤卡牌（如旋风斩）则颇为有效；若玩家同时亦持有地精之角，还可以反利用邪教徒以获取优势。但对于弹跳药瓶等此类随机伤害的卡牌，邪教徒则会为觉醒者分担众多伤害，因而玩家需要有针对性地选牌。<br>轶事<br>即使没有爪牙的buff，邪教徒也依然会在觉醒者死亡时逃跑。<br>因此，使用狂宴、仪式匕首等击杀觉醒者战斗中的邪教徒，也依然算作斩杀。<br>邪教徒及它们所信奉的宗教与很多事件均有关联，包括翅膀雕... | `single_source` | [邪教徒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408976&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/15/3f86b405c02a0505b115baa581aa8f74.png", "https://imgheybox.max-c.com/web/bbs/2024/08/15/98107d0510570d864acfd328bb622ace.png"] | `single_source` | [邪教徒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408976&wiki_id=646570) |
| `source.infobox.description` | 48-54 | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 邪教徒 | `single_source` | [邪教徒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408976&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>| Name   = Cultist<br>| Image  = Cultist.png<br>| HP     = 48-54<br>| AscHP  = 50-56<br>| Debut  = Act 1<br>| Type   = Normal<br>}}'''The Cultist''' is a normal [[Monsters|Enemy]] that can show up in all 3 Acts.<br><br>== Pattern ==<br>{{Intents Table/start|Cultist}}<br>{{Intents Table/row<br>| Name   = Incantation<br>| Intent = Buff<br>| Effect = Gains (3;{{Asc|2|4}} ; {{Asc|17|5}}) {{BD|Ritual}}.<br>| GivesToEnemy = Ritual<br>}}<br>{{Intents Table/row<br>| Name   = Dark S... | `single_source` | [P3 wiki.gg API batch: monster 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Slimes|Corrupt_Heart|Thieves|Thieves|Time_Eater|Snake_Plant|Chosen|Donu_and_Deca|Lagavulin|Nemesis|Centurion_and_Mystic|Spire_Shield_and_Spire_Spear|Gremlins|Spheric_Guardian|The_Guardian|Cultist|Writhing_Mass|Transient|Book_of_Stabbing|Reptomancer&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
