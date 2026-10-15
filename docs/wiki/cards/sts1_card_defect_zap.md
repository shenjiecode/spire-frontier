# 电击 / Zap

> 稳定 ID：`sts1.card.defect.zap`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：电击
- English: Zap

别名/候选：电击 (`zh-CN`, unverified)

## 卡牌属性

- 颜色：`Blue`
- 类型：`Skill`
- 稀有度：`Basic`
- 可获得性：`card_list`
- 标签：`["Channel", "Lightning"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Channel 1 Lightning. | 生成1个闪电充能球。 | [查看图片](../../../data/assets/9ec5e40be2b937291c68b9fcefe703ea12feb425c17d427a7d10fec425ea199f.png) |
| `Upgraded` | `0.0` | Channel 1 Lightning. | 生成1个闪电充能球。 | [查看图片](../../../data/assets/bfd04d129282b2da72cc73c9ee3a4d7b774c370c403488db04f47114462f4499.png) |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

- `starting_deck_contains` → [故障机器人 / Defect](../characters/sts1_character_defect.md) ；条件：`{"quantity": 1}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.color (base)` | Blue | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.color (upgrade)` | Blue | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 0 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Channel 1 Lightning. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Channel 1 Lightning. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Channel 1 Lightning. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Channel 1 Lightning. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Zap.class", "class_sha256": "524820d2a3fc6a6d5d0f094f7ff938f7e55587397301fdddedeeccb68c15c573", "constructor_offsets": {"magic_number": 45}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 1}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Zap.class", "class_sha256": "524820d2a3fc6a6d5d0f094f7ff938f7e55587397301fdddedeeccb68c15c573", "constructor_offsets": {"magic_number": 45}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 1}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Basic | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.rarity (base)` | Basic | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.rarity (upgrade)` | Basic | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.tags` | ["Channel", "Lightning"] | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags (base)` | ["Channel", "Lightning"] | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.tags (upgrade)` | ["Channel", "Lightning"] | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.type (base)` | Skill | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.type (upgrade)` | Skill | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `game.card.description` | Channel !M! Lightning. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 生成 !M! 个 闪电 充能球。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Zap | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 电击 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Zap", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | （图片未提供文字说明）<br>生成一个闪电充能球。<br>电击+<br>（图片未提供文字说明）<br>生成一个闪电充能球。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [电击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549930&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Zap.png/150px-Blue-Zap.png?d47181", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-ZapPlus.png/150px-Blue-ZapPlus.png?f090a7"} | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/13b72ebe1d0903dbf097fb684f941fb8.png", "https://cdn.max-c.com/heybox/dailynews/img/b1cdb5b53af3dbf71d38dbfa733221b9.png", "https://imgheybox.max-c.com/web/bbs/2024/08/23/931945aa6186ed95b1ab3adb5d83c60b.png"] | `single_source` | [电击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549930&wiki_id=646570) |
| `source.infobox.description` | Channel 1 Lightning. | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 电击 | `single_source` | [电击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549930&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>| Name        = Zap<br>| Image       = Blue-Zap.png<br>| Color       = Blue<br>| Type        = Skill<br>| Rarity      = Basic<br>| Cost        = 1<br>| CostPlus    = 0<br>| Description = {{KW|Channel}} 1 {{KW|Lightning}}.<br>| GivesToPlayer = Channel, Lightning<br>}}<br>{{Keyword Infobox|Channel}}<br>{{Keyword Infobox|Lightning}}<br>{{C|Zap}} is a 1 (0 if upgraded) {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Ba... | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
