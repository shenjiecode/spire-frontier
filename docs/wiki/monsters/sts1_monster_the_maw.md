# 巨口 / The Maw

> 稳定 ID：`sts1.monster.the_maw`  
> 类别：`monster`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：巨口
- English: The Maw

## monster 数据

| 字段 | 值 |
| --- | --- |
| `category` | normal |
| `act` | Act 3 |
| `hp_min` | 300 |
| `hp_max` | 300 |
| `ascension_json` | {"base_max": 300, "base_min": 300, "base_raw": "300"} |

### 行动

| 名称 | 意图 | 伤害 | 次数 | 效果 |
| --- | --- | ---: | ---: | --- |
| Slam | Attack6 | 25 |  | {"text": "Deals (25;30) damage."} |
| Drool | Buff |  |  | {"text": "Gains (3;5) Strength."} |
| Roar | DebuffStrong |  |  | {"text": "Applies (3;5) Weak and (3;5) Frail."} |
| Nom Nom | Attack2 | 5 |  | {"text": "Deals 5×N damage. N = Current turn, divided by two (rounded up)."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `contains_monster` → [巨口 / The Maw](../encounters/sts1_encounter_act3_hard_the_maw.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | The Maw | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 巨口 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Maw", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@RRrrohrrRGHhh!!@"] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | ["@呜嗷嗷啊嗷！！@"] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"base_max": 300, "base_min": 300, "base_raw": "300"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Drool` | {"effect": "Gains (3;5) Strength.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Nom Nom` | {"effect": "Deals 5×N damage. N = Current turn, divided by two (rounded up).", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Roar` | {"effect": "Applies (3;5) Weak and (3;5) Frail.", "intent": "DebuffStrong"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Slam` | {"effect": "Deals (25;30) damage.", "intent": "Attack6"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | Monster id: The Maw<br>（图片未提供文字说明）<br>怪物信息<br>生命值<br>300;(300;)<br>类型<br>普通<br>意图<br>咆哮;强化;猛击;连击<br>初始能力<br>无<br>备注<br>无<br>行动模式<br>名称<br>效果<br>效果（进阶3+）<br>效果（进阶17+）<br>咆哮<br>给予3层<br>脆弱<br>与<br>虚弱<br>给予3层<br>脆弱<br>与<br>虚弱<br>给予5层<br>脆弱<br>与<br>虚弱<br>强化<br>获得3点<br>力量<br>获得3点<br>力量<br>获得5点<br>力量<br>猛击<br>造成25点伤害<br>造成30点伤害<br>造成30点伤害<br>连击<br>造成5*n点伤害<br>造成5*n点伤害<br>造成5*n点伤害<br>其中，n=本次战斗使用连击的次数+1。<br>巨口的攻击机制比较复杂，可以归纳成以下几点：<br>首回合必定使用咆哮，且本场战斗只会使用一次<br>第二回合有50%的几率使用猛击，50%的几率使用连击<br>之后的攻击会由上个回合的行动... | `single_source` | [巨口](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438054&wiki_id=646570) |
| `source.infobox.description` | 300 | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 巨口 | `single_source` | [巨口](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438054&wiki_id=646570) |
| `source.wikitext` | {{Enemy Infobox<br>|Name   = The Maw<br>|Image  = Maw.png<br>|HP     = 300<br>|Debut  = Act 3<br>|Type   = Normal<br>}}<br>The Maw is a normal [[Monsters|Enemy]] found exclusively in [[Act 3]].<br><br>== Pattern ==<br>{{Intents Table/start|The Maw}}<br>{{Intents Table/row<br>|Name   = Roar<br>|Intent = DebuffStrong<br>|Effect = Applies (3;{{Asc|17|5}}) {{BD|Weak}} and (3;{{Asc|17|5}}) {{BD|Frail}}.}}<br>{{Intents Table/row<br>|Name   = Slam<br>|Intent = Attack6<br>|Effect = Deals (25;{{Asc|2|... | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
