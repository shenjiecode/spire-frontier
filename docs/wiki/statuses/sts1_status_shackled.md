# 镣铐 / Shackled

> 稳定 ID：`sts1.status.shackled`  
> 类别：`status`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：镣铐
- English: Shackled

## status 数据

| 字段 | 值 |
| --- | --- |
| `polarity` | negative |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Shackled | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.localization.name` | 镣铐 | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Shackled", "kind": "status", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["At the end of its turn, gains #b", " #yStrength."] | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["在其回合结束时回复 #b", " 点 #y力量 。"] | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `source.article_text` | 镣铐<br>Buffs id: Shackled<br>（图片未提供文字说明）<br>Buffs信息<br>效果中文描述<br>在其回合结束时回复 X 点 力量 。<br>效果英文描述<br>Increases the effectiveness of Orbs by X.<br>类型<br>敌方Debuff<br>可叠加<br>注意<br>所有“使敌人在本回合内失去x力量”的效果实际均为同时赋予敌人x层力量（负）与x层镣铐。<br>漏洞&策略<br>镣铐被错误地判定为减益效果，这使得它能够被一些敌人（如时间吞噬者和觉醒者）的“移除所有减益”的行动所移除。<br>因此，如果这些敌人原本拥有力量，在它们即将移除减益的回合使用“使敌人在本回合内失去x力量”的效果会让它们的力量在移除减益后降低x点（如果不足x点，则降低至0点，因为力量（负）同样是减益效果） | `single_source` | [镣铐](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460343&wiki_id=646570) |
| `source.title_text` | 镣铐 | `single_source` | [镣铐](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460343&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Template:Under Construction}}<br>{{#setmainimage:Intent_Debuff.png|quiet}}<br>{{TOC limit|2}}<br>See also: [[Buffs]]<br><br>== Stack Types ==<br>{{Hatnote|'''Note:''' These terms are not officially used by the game and are used by the wiki for better classification and description of their behavior.}}<br>* '''Intensity Debuffs''' are more effective depending on how many stacks of the debuffs you have. These debuffs typically are either permanent for the combat e... | `single_source` | [P3 wiki.gg API batch: status 4](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Buffs|Buffs|Debuffs|Buffs|Debuffs|Buffs|Dexterity|Vulnerable|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Weak|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | Increases the effectiveness of Orbs by X. | `single_source` | [P3 wiki.gg API batch: status 4](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Buffs|Buffs|Debuffs|Buffs|Debuffs|Buffs|Dexterity|Vulnerable|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Weak|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | 在其回合结束时回复 X 点 力量 。 | `single_source` | [镣铐](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460343&wiki_id=646570) |

页面生成时间：2026-09-18T11:10:22+00:00
