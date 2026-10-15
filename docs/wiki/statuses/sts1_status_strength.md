# 力量 / Strength

> 稳定 ID：`sts1.status.strength`  
> 类别：`status`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：力量
- English: Strength

## status 数据

| 字段 | 值 |
| --- | --- |
| `polarity` | positive |
| `affects` | player |
| `stacking` | Intensity |
| `trigger_timing` | attack damage calculation |
| `removal` | end of combat or explicit effect |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Strength | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.localization.name` | 力量 | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Strength", "kind": "status", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["Increases attack damage by #b", "Decreases attack damage by #b", "."] | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["攻击伤害提升 #b", "攻击伤害降低 #b", " 。"] | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `source.article_excerpt.en` | Slay the Spire Slay the Spire 2 StrengthStack Type Intensity Increases attack damage by X. Strength is a Buff that increases the damage of Attack cards and enemy Intents. Each point of Strength increases the damage of an attack by 1. Attacks that hit multiple times, like Sword Boomerang, will apply Strength to each individual hit. Strength can be negative, reducing the damage of attacks to a minimum of 0 damage per hit. Contents 1 Sources 1.1 On Player 1.1.1 Cards 1.1.2 Relics 1.1.3 Potions 1... | `single_source` | [Strength | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Strength) |
| `source.article_text` | 力量<br>Buffs id: Strength<br>（图片未提供文字说明）<br>Buffs信息<br>效果中文描述<br>攻击伤害提升 X点 。<br>效果英文描述<br>Increases attack damage by #b.<br>类型<br>通用BUFF<br>可叠加 | `single_source` | [力量](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501526&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/20/a7f0f69f1c54783e283e0470d080f016.png"] | `single_source` | [力量](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501526&wiki_id=646570) |
| `source.infobox.description` | Increases attack damage by X. | `single_source` | [P3 wiki.gg API batch: status 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Focus|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Strength|Buffs|Strength|Debuffs|Buffs|Plated_Armor|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 力量 | `single_source` | [力量](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501526&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Power Infobox<br>|Name         = Strength<br>|Image        = Icon Strength.png<br>|Description  = Increases attack damage by X.<br>|Type         = Buff<br>|Stacks       = Intensity<br>|BetweenTurns = <br>|Cap          = <br>}}<br>{{BD|Strength}} is a [[Buff]] that increases the damage of {{QueryLink|Cards|type:Attack|Attack cards}} and  enemy [[Intent|Intents]].<br><br>Each point of {{BD|Strength}} increases the damage of an attack by 1. Attacks that hit multipl... | `single_source` | [P3 wiki.gg API batch: status 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Focus|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Strength|Buffs|Strength|Debuffs|Buffs|Plated_Armor|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | Increases attack damage by X. | `single_source` | [P3 wiki.gg API batch: status 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Focus|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Strength|Buffs|Strength|Debuffs|Buffs|Plated_Armor|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | 攻击伤害提升 X点 。 | `single_source` | [力量](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501526&wiki_id=646570) |
| `status.description.en` | Increases attack damage by #b. | `provisional` | [力量](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501526&wiki_id=646570) |
| `status.description.zh` | 攻击伤害提升 X 点。 | `provisional` | [力量](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501526&wiki_id=646570) |

页面生成时间：2026-09-18T14:55:10+00:00
