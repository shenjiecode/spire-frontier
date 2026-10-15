# 飞镖 / Flechettes

> 稳定 ID：`sts1.card.silent.flechettes`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：飞镖
- English: Flechettes

## 卡牌属性

- 颜色：`Green`
- 类型：`Attack`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Hand"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 4 damage for each Skill in your hand. | 手牌中每有一张技能牌，造成4点伤害。 | 未保存 |
| `Upgraded` | `1.0` | Deal 6 damage for each Skill in your hand. | 手牌中每有一张技能牌，造成6点伤害。 | 未保存 |

## 相关条目

- `belongs_to_character` → [静默猎手 / Silent](../characters/sts1_character_silent.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Green | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 4 damage for each Skill in your hand. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 4 damage for each Skill in your hand. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 6 damage for each Skill in your hand. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 6 damage for each Skill in your hand. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/green/Flechettes.class", "class_sha256": "612b8070c277939e76ecbd3c908ea83575fadcb2aea22d38135943ceef0a5f9c", "constructor_offsets": {"damage": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 4}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/green/Flechettes.class", "class_sha256": "612b8070c277939e76ecbd3c908ea83575fadcb2aea22d38135943ceef0a5f9c", "constructor_offsets": {"damage": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 6}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Hand"] | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage for each Skill in your hand. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 手牌中每有一张技能牌，造成 !D! 点伤害。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Flechettes | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 飞镖 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Flechettes", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 飞镖<br>（图片未提供文字说明）<br>手牌中每有一张技能牌，造成4点伤害。<br>飞镖+<br>（图片未提供文字说明）<br>手牌中每有一张技能牌，造成6点伤害。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [飞镖](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494135&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Green-Flechettes.png/150px-Green-Flechettes.png?bd1600", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Green-FlechettesPlus.png/150px-Green-FlechettesPlus.png?4fb24c"} | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/749d7a1f7d2f226255e0e4740640a93c.jpg", "https://cdn.max-c.com/heybox/dailynews/img/8e388d6a9fb5977f3841c14c5b416c2b.jpg", "https://imgheybox.max-c.com/web/bbs/2024/08/22/7449077222aafa626b8cd37181e6c284.png"] | `single_source` | [飞镖](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494135&wiki_id=646570) |
| `source.infobox.description` | Deal (4;6) damage for each Skill in your hand. | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 飞镖 | `single_source` | [飞镖](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494135&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>|Name        = Flechettes<br>|Image       = Green-Flechettes.png<br>|Color       = Green<br>|Type        = Attack<br>|Rarity      = Uncommon<br>|Cost        = 1<br>|Description = Deal (4;6) damage for each Skill in your hand.<br>|Keywords    = Hand<br>}}<br>{{C|Flechettes}} is a 1{{Icon|GE}} cost {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:Attack|Attack}} card for the [[Silent]]. It deals 4 (6 if upgraded) damage, for an a... | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
