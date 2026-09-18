# 易伤 / Vulnerable

> 稳定 ID：`sts1.status.vulnerable`  
> 类别：`status`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：易伤
- English: Vulnerable

## status 数据

| 字段 | 值 |
| --- | --- |
| `polarity` | negative |
| `affects` | player or enemy |
| `stacking` | additive |
| `trigger_timing` | attack damage calculation |
| `removal` | turn/explicit effect |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Vulnerable | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.localization.name` | 易伤 | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Vulnerable", "kind": "status", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["Receive #b", "% more damage from #yAttacks for #b", " turn.", " turns."] | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["从 #y攻击 受到的伤害增加 #b", "% 。持续时间 #b", " 回合。", " 回合。"] | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `source.article_text` | 易伤<br>Buffs id: Vulnerable<br>（图片未提供文字说明）<br>Buffs信息<br>效果中文描述<br>从 攻击 受到的伤害增加 50% .持续 X 回合。<br>效果英文描述<br>Receive 50% more damage from Attacks for #b turn(s).<br>类型<br>通用Debuff<br>可叠加<br>注意<br>易伤只影响“从攻击受到的伤害”。<br>对于我方，只影响直接由敌人的攻击类意图造成的伤害；对于敌方，只影响直接由攻击牌造成的伤害。 | `single_source` | [易伤](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501549&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/20/954c0cf73b38c727ae72b60d2d457cb6.png"] | `single_source` | [易伤](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501549&wiki_id=646570) |
| `source.infobox.description` | Receive 50% more damage from Attacks for X turns. | `single_source` | [P3 wiki.gg API batch: status 4](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Buffs|Buffs|Debuffs|Buffs|Debuffs|Buffs|Dexterity|Vulnerable|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Weak|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 易伤 | `single_source` | [易伤](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501549&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Power Infobox<br>|Name         = Vulnerable<br>|Image        = Icon Vulnerable.png<br>|Description  = Receive 50% more damage from Attacks for X turns.<br>|Type         = Debuff<br>|Stacks       = Duration<br>|BetweenTurns = <br>|Cap          = <br>}}<br>{{BD|Vulnerable}} is a [[Debuff]] that increases the damage of {{QueryLink|Cards|type:Attack|Attack cards}} and  enemy [[Intent|Intents]] by 50% (typically).<br><br>Each point of {{BD|Vulnerable}} increases how ... | `single_source` | [P3 wiki.gg API batch: status 4](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Buffs|Buffs|Debuffs|Buffs|Debuffs|Buffs|Dexterity|Vulnerable|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Weak|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | Receive 50% more damage from Attacks for X turns. | `single_source` | [P3 wiki.gg API batch: status 4](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Buffs|Buffs|Debuffs|Buffs|Debuffs|Buffs|Dexterity|Vulnerable|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Weak|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:45+00:00
