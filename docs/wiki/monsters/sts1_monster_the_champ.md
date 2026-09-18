# 第一勇士 / The Champ

> 稳定 ID：`sts1.monster.the_champ`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：第一勇士
- English: The Champ

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | boss |
| `act` | Act 2 |
| `hp_min` | 420 |
| `hp_max` | 420 |
| `ascension_json` | {"ascension_max": 440, "ascension_min": 440, "ascension_raw": "440", "base_max": 420, "base_min": 420, "base_raw": "420"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Gloat | Buff |  |  | {"text": "Gains (2;3 ; 4) Strength."} |
| Anger | Buff |  |  | {"text": "Removes all Debuffs]. Gains (6;9 ; 12) Strength."} |
| Taunt | Unknown |  |  | {"text": "Applies 2 Weak and 2 Vulnerable."} |
| Defensive Stance | DefendBuff |  |  | {"text": "Gains (15;18 ; 20) Block and (5;6 ; 7) Metallicize."} |
| Execute | Attack7 | 10 | 2 | {"text": "Deals 10×2 damage."} |
| Face Slap | DebuffAttack3 | 12 |  | {"text": "Deals (12;14) damage. Applies 2 Frail and 2 Vulnerable"} |
| Heavy Slash | Attack4 | 16 |  | {"text": "Deals (16;18) damage."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | The Champ | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 第一勇士 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Champ", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["You call that a weapon?", "Come at me!", "Do your worst! NL @HAHAHA!@", "Have a free shot! NL Futile weakling!", "~You've~ ~done~ ~it~ ~now...~", "@DEFEAT??@ NL @IMPOSSIBLE!!@", "~DIE~ ~.~ ~.~ ~.~", "Face my wrath!", "@THAT'S@ NL @MY@ @BELT!!@"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["你管这叫武器？", "来和我战啊！", "有什么招数尽管上！ NL @哈哈哈！@", "来啊我让你打！ NL 没用的弱者！", "~你惹火我了……~", "@败北？@ NL @不可能的！！@ ", "~去~ ~死~ ~。。。~", "接受我的怒火吧！", "@那是@ NL @我的@ @腰带！！@"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | ["Defensive Stance", "Execute", "Face Slap"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | ["防御态势", "处决", "打脸"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 440, "ascension_min": 440, "ascension_raw": "440", "base_max": 420, "base_min": 420, "base_raw": "420"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Anger` | {"effect": "Removes all Debuffs]. Gains (6;9 ; 12) Strength.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Defensive Stance` | {"effect": "Gains (15;18 ; 20) Block and (5;6 ; 7) Metallicize.", "intent": "DefendBuff"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Execute` | {"effect": "Deals 10×2 damage.", "intent": "Attack7"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Face Slap` | {"effect": "Deals (12;14) damage. Applies 2 Frail and 2 Vulnerable", "intent": "DebuffAttack3"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Gloat` | {"effect": "Gains (2;3 ; 4) Strength.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Heavy Slash` | {"effect": "Deals (16;18) damage.", "intent": "Attack4"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Taunt` | {"effect": "Applies 2 Weak and 2 Vulnerable.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | 第一勇士<br>Monster id: The Champ<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>420;(440;)<br>类型<br>Boss<br>意图<br>防御态势;打脸;挑衅;重斩;强化;爆发;处刑<br>初始能力<br>无<br>备注<br>无<br>地图图标<br>攻击方式<br>效果<br>进阶4+<br>进阶9+<br>进阶19+<br>防御姿态<br>获得15格挡，金属化5<br>同前<br>获得18格挡，金属化6<br>获得20格挡，金属化7<br>打脸<br>12伤害，造成两回合破甲、易伤<br>14伤害，造成两回合破甲、易伤<br>同前<br>同前<br>嘲讽<br>造成两回合易伤、虚弱<br>同前<br>同前<br>同前<br>普攻<br>16伤害<br>18伤害<br>同前<br>同前<br>注视<br>获得2力量<br>获得3力量<br>获得3力量<br>获得4力量<br>处刑<br>造成10*2伤害<br>同前<br>同前<br>同前<br>发怒<br>移除所有debuff，增加6力量<br>移除所有debuff，增... | `single_source` | [第一勇士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421632&wiki_id=646570) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/406b07b48054870f523ced2f06794402.png", "https://cdn.max-c.com/heybox/dailynews/img/9dacb9083c8597f4c0c6ff0aa859e4c1.png"] | `single_source` | [第一勇士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421632&wiki_id=646570) |
| `source.infobox.description` | 420 | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 第一勇士 | `single_source` | [第一勇士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421632&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = The Champ<br>|Image  = Champ.png<br>|Icon   = Map-Champ.png<br>|HP     = 420<br>|AscHP  = 440<br>|Debut  = Act 2<br>|Type   = Boss<br>}}<br>The Champ is a [[Boss]] found at the end of [[Act 2]].<br><br>== Pattern ==<br>{{Intents Table/start|The Champ}}<br>{{Intents Table/row<br>|Name   = Heavy Slash<br>|Intent = Attack4<br>|Effect = Deals (16;{{Asc|4|18}}) damage.}}<br>{{Intents Table/row<br>|Name   = Face Slap<br>|Intent = DebuffAttack3<br>|Effect = Deals (12;{{A... | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
