# 格挡返还 / Block Return

> 稳定 ID：`sts1.status.block_return`  
> 类别：`status`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：格挡返还
- English: Block Return

别名/候选：以手拒之（能力） (`zh-CN`, agreed)

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
| `game.localization.name` | Block Return | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.localization.name` | 格挡返还 | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "BlockReturnPower", "kind": "status", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["When attacked, you gain #b", " #yBlock."] | `verified_game` | [Game localization eng/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/powers.json) |
| `game.status.descriptions` | ["当被你攻击时，你获得 #b", " 点 #y格挡 。"] | `verified_game` | [Game localization zhs/powers.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/powers.json) |
| `mapping.cross_source.status` | {"english_url": "https://slaythespire.wiki.gg/wiki/Debuffs#block_return", "game_key": "BlockReturnPower", "match": ["xiaoheihe_buff_id", "wiki_gg_buff_anchor", "game_local_description"], "target_entity_id": "sts1.status.block_return", "target_name": "Block Return", "zh_article_id": "15460336", "zh_url": "https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460336&wiki_id=646570"} | `agreed` | [Debuffs | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Debuffs) |
| `source.article_text` | 以手拒之<br>Buffs id: Talk to the Hand<br>（图片未提供文字说明）<br>Buffs信息<br>效果中文描述<br>每当玩家攻击敌人时，获得X点格挡<br>效果英文描述<br>Whenever you attack this enemy,gain X Block.<br>类型<br>敌方Debuff<br>可叠加<br>策略<br>攻击拥有以手拒之的敌人，并且造成伤害（被格挡的伤害也会计入次数）可以令玩家获得等同于层数的格挡。因此，用多段攻击（如发泄或诸神之黄昏等）搭配以手拒之，可以将收益最大化。<br>轶事<br>若玩家通过非常规手段令自身获得以手拒之，那么当玩家受到伤害时，立即获得等同于层数的格挡 | `single_source` | [以手拒之（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460336&wiki_id=646570) |
| `source.title_text` | 以手拒之（能力） | `single_source` | [以手拒之（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460336&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Template:Under Construction}}<br>{{#setmainimage:Intent_Debuff.png|quiet}}<br>{{TOC limit|2}}<br>See also: [[Buffs]]<br><br>== Stack Types ==<br>{{Hatnote|'''Note:''' These terms are not officially used by the game and are used by the wiki for better classification and description of their behavior.}}<br>* '''Intensity Debuffs''' are more effective depending on how many stacks of the debuffs you have. These debuffs typically are either permanent for the combat e... | `single_source` | [P3 wiki.gg API batch: status 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Focus|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Strength|Buffs|Strength|Debuffs|Buffs|Plated_Armor|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | Whenever you attack this enemy,gain X Block. | `single_source` | [P3 wiki.gg API batch: status 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Focus|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Buffs|Strength|Buffs|Strength|Debuffs|Buffs|Plated_Armor|Buffs|Buffs|Buffs|Buffs|Buffs&prop=revisions&rvprop=content|ids&rvslots=main) |
| `status.description` | 每当玩家攻击敌人时，获得X点格挡 | `single_source` | [以手拒之（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460336&wiki_id=646570) |

页面生成时间：2026-09-18T11:10:22+00:00
