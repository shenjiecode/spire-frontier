# 斋戒 / Fasting

> 稳定 ID：`sts1.card.watcher.fasting`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：斋戒
- English: Fasting

别名/候选：Fasting (`en`, verified_game)

## 卡牌属性

- 颜色：`Purple`
- 类型：`Power`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Dexterity", "Strength"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `2.0` | Gain 3 Strength. Gain 3 Dexterity. Gain 1 less 1 Energyat the start of each turn. | 获得3点力量。获得3敏捷。每回合开始时少获得1点能量。 | 未保存 |
| `Upgraded` | `2.0` | Gain 4 Strength. Gain 4 Dexterity. Gain 1 less 1 Energyat the start of each turn. | 获得4点力量。获得4敏捷。每回合开始时少获得1点能量。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 2 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 2 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 3 Strength. Gain 3 Dexterity. Gain 1 less 1 Energy at the start of each turn. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Gain 3 Strength. Gain 3 Dexterity. Gain 1 less 1 Energy at the start of each turn. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 4 Strength. Gain 4 Dexterity. Gain 1 less 1 Energy at the start of each turn. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 4 Strength. Gain 4 Dexterity. Gain 1 less 1 Energy at the start of each turn. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Fasting.class", "class_sha256": "4991997e9b9898e8f1e1f878f46105cc1748c1a75dec5f212322368655b946f3", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Fasting.class", "class_sha256": "4991997e9b9898e8f1e1f878f46105cc1748c1a75dec5f212322368655b946f3", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 4}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Dexterity", "Strength"] | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Power | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | DEPRECATED | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得 !M! 点 力量 。 NL 获得 !M! 敏捷 。 NL 每回合开始时少获得1 [W] 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | DEPRECATED | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 斋戒 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_alias` | {"canonical_key": "Fasting2", "deprecated": true, "key": "Fasting", "kind": "card"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Fasting", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 斋戒<br>获得3点力量。获得3敏捷。每回合开始时少获得一点能量。<br>斋戒+<br>获得4点力量。获得4敏捷。每回合开始时少获得一点能量。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [斋戒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9958994&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-Fasting.png/150px-Purple-Fasting.png?d21a38", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-FastingPlus.png/150px-Purple-FastingPlus.png?c56077"} | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/7429b1b35cf88ccd2025b0e5c75f5690.png"] | `single_source` | [斋戒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9958994&wiki_id=646570) |
| `source.infobox.description` | Gain (3;4) Strength. Gain (3;4) Dexterity. Gain 1 less PE at the start of each turn. | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 斋戒 | `single_source` | [斋戒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9958994&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Fasting<br>|Image       = Purple-Fasting.png<br>|Color       = Purple<br>|Type        = Power<br>|Rarity      = Uncommon<br>|Cost        = 2<br>|Description = Gain (3;4) {{BD|Strength}}. <br>Gain (3;4) {{BD|Dexterity}}. <br>Gain 1 less {{Icon|PE}} at the start of each turn.<br>}}<br>{{Power Infobox|Fasting}}{{C|Fasting}} is a 2 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:Power|Po... | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
