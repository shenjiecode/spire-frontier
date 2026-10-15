# 抽牌 / Draw

> 稳定 ID：`sts1.status.draw`  
> 类别：`status`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：抽牌
- English: Draw

## status 数据

| 字段 | 值 |
| --- | --- |
| `polarity` | neutral |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Draw | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.localization.name` | 抽牌 | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Draw", "kind": "status", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["At the start of your turn, draw #b", " additional card.", " less card.", " additional cards.", " less cards."] | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["#b", " 张额外抽牌，在每个回合开始时。", " 张减少抽牌，在每个回合开始时。", " 张额外抽牌，在每个回合开始时。", " 张减少抽牌，在每个回合开始时。"] | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `source.article_text` | 抽牌<br>Buffs id: Draw Card<br>（图片未提供文字说明）<br>Buffs信息<br>效果中文描述<br>下回合抽 X 张牌。<br>效果英文描述<br>Draw X additional card(s) next turn.<br>类型<br>玩家BUFF<br>可叠加 | `single_source` | [抽牌](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454356&wiki_id=646570) |
| `source.title_text` | 抽牌 | `single_source` | [抽牌](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454356&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation|1}}{{Ambox|title=WARNING| style="text-align:center; font-weight:bold;" ||color=red|icon=GremlinNob.png|message=''This page is under construction. Information may be wrong or incomplete.''}}{{#setmainimage:Intent_Buff.png|quiet}}<br>{{TOC limit|2}}<br>See also: [[Debuffs]]<br><br>== Stack Types ==<br>{{Hatnote|'''Note:''' These terms are not officially used by the game and are used by the wiki for better classification and description of their behavior.}}<br>* '''Intens... | `single_source` | [P3 wiki.gg API batch: status 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Focus|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Strength|Buffs|Strength|Debuffs|Buffs|Plated_Armor|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | Draw X additional card(s) next turn. | `single_source` | [P3 wiki.gg API batch: status 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Focus|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Strength|Buffs|Strength|Debuffs|Buffs|Plated_Armor|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | 下回合抽 X 张牌。 | `single_source` | [抽牌](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454356&wiki_id=646570) |

页面生成时间：2026-09-18T14:55:10+00:00
