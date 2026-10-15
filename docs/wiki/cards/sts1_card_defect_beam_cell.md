# 光束射线 / Beam Cell

> 稳定 ID：`sts1.card.defect.beam_cell`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：光束射线
- English: Beam Cell

## 卡牌属性

- 颜色：`Blue`
- 类型：`Attack`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Vulnerable"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `0.0` | Deal 3 damage. Apply 1 Vulnerable. | 造成3点伤害。给予1层易伤。 | 未保存 |
| `Upgraded` | `0.0` | Deal 4 damage. Apply 2 Vulnerable. | 造成4点伤害。给予2层易伤。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 0 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 0 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 3 damage.Apply 1 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 3 damage.Apply 1 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 4 damage.Apply 2 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 4 damage.Apply 2 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/BeamCell.class", "class_sha256": "559dec7c944c640b61835ca19c025a9a87f94cfddb414e89f0290c8e40d25ee1", "constructor_offsets": {"damage": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 3, "magic_number": 1}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/BeamCell.class", "class_sha256": "559dec7c944c640b61835ca19c025a9a87f94cfddb414e89f0290c8e40d25ee1", "constructor_offsets": {"damage": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 4, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Vulnerable"] | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL Apply !M! Vulnerable. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 给予 !M! 层 易伤 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Beam Cell | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 光束射线 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Beam Cell", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 光束射线<br>（图片未提供文字说明）<br>造成3点伤害，给予1层易伤。<br>光束射线+<br>（图片未提供文字说明）<br>造成4点伤害，给予2层易伤。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [光束射线](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495545&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-BeamCell.png/150px-Blue-BeamCell.png?9e8857", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-BeamCellPlus.png/150px-Blue-BeamCellPlus.png?3b882d"} | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/0ee5c38d3dc431c790f27143463ef4a5.png", "https://cdn.max-c.com/heybox/dailynews/img/7d16844d533c59e4f2177fbfaa4b0e08.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/602c0c4ffa527f56271bf317326bd185.png"] | `single_source` | [光束射线](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495545&wiki_id=646570) |
| `source.infobox.description` | Deal (3;4) damage. Apply (1;2) Vulnerable. | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 光束射线 | `single_source` | [光束射线](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495545&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>|Name        = Beam Cell<br>|Image       = Blue-BeamCell.png<br>|Color       = Blue<br>|Type        = Attack<br>|Rarity      = Common<br>|Cost        = 0<br>|Description = Deal (3;4) damage.<br>Apply (1;2) {{BD|Vulnerable}}.<br>|GivesToEnemy = Vulnerable<br>}}<br>{{Power Infobox|Vulnerable}}<br>{{C|Beam Cell}} is a 0 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|type:Attack|Attac... | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
