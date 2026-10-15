# 虚弱 / Weak

> 稳定 ID：`sts1.status.weak`  
> 类别：`status`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：虚弱
- English: Weak

## status 数据

| 字段 | 值 |
| --- | --- |
| `polarity` | negative |
| `affects` | player or enemy |
| `stacking` | Duration |
| `trigger_timing` | attack damage calculation |
| `removal` | turn/explicit effect |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

- `applies_status` → [虚弱药水 / Weak Potion](../potions/sts1_potion_weak.md)

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Weakened | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.localization.name` | 虚弱 | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Weakened", "kind": "status", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["#yAttacks deal #b", "% less damage for #b", " turn.", " turns."] | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | [" #y攻击 造成的伤害减少 #b", "% 。持续时间 #b", " 回合。", " 回合。"] | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `source.article_text` | 虚弱<br>Buffs id: Weak<br>（图片未提供文字说明）<br>Buffs信息<br>效果中文描述<br>攻击 造成的伤害减少 25% 。持续时间 X 回合。<br>效果英文描述<br>Attacks deal 25% less damage for X turn(s).<br>类型<br>通用Debuff<br>可叠加 | `single_source` | [虚弱](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501547&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/20/ef750abfa9826530f73df3fce98718a5.png"] | `single_source` | [虚弱](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501547&wiki_id=646570) |
| `source.infobox.description` | Attacks deal 25% less damage for X turns. | `single_source` | [P3 wiki.gg API batch: status 4](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Buffs|Buffs|Debuffs|Buffs|Debuffs|Buffs|Dexterity|Vulnerable|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Weak|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 虚弱 | `single_source` | [虚弱](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501547&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}} <br>{{Power Infobox<br>|Name         = Weak<br>|Image        = Icon Weak.png<br>|Description  = Attacks deal 25% less damage for X turns.<br>|Type         = Debuff<br>|Stacks       = Duration<br>|BetweenTurns = <br>|Cap          = <br>}}<br>{{BD|Weak}} is a [[Debuff]] that reduces the damage of {{QueryLink|Cards|type:Attack|Attack}} cards and enemy [[Intent|Intents]] by 25% (typically).<br><br>Each point of {{BD|Weak}} increases how many turns the debuff is active fo... | `single_source` | [P3 wiki.gg API batch: status 4](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Buffs|Buffs|Debuffs|Buffs|Debuffs|Buffs|Dexterity|Vulnerable|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Weak|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | Attacks deal 25% less damage for X turns. | `single_source` | [P3 wiki.gg API batch: status 4](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Buffs|Buffs|Debuffs|Buffs|Debuffs|Buffs|Dexterity|Vulnerable|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Weak|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | 攻击 造成的伤害减少 25% 。持续时间 X 回合。 | `single_source` | [虚弱](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501547&wiki_id=646570) |

页面生成时间：2026-09-18T14:55:10+00:00
