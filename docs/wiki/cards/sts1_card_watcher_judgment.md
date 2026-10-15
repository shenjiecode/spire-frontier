# 审判 / Judgment

> 稳定 ID：`sts1.card.watcher.judgment`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：审判
- English: Judgment

## 卡牌属性

- 颜色：`Purple`
- 类型：`Skill`
- 稀有度：`Rare`
- 可获得性：`card_list`
- 标签：`[]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | If the enemy has 30 or less HP, set their HP to 0. | 如果目标敌人的生命值小于等于30点，则将其生命值变为0。 | 未保存 |
| `Upgraded` | `1.0` | If the enemy has 40 or less HP, set their HP to 0. | 如果目标敌人的生命值小于等于40点，则将其生命值变为0。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | If the enemy has 30 or less HP, set their HP to 0. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | If the enemy has 30 or less HP, set their HP to 0. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | If the enemy has 40 or less HP, set their HP to 0. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | If the enemy has 40 or less HP, set their HP to 0. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Judgement.class", "class_sha256": "a9c3cb0eb1fb1fccff7c96c00b2db94d95e492b63be313830b28d68270bf6de0", "constructor_offsets": {"magic_number": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 30}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Judgement.class", "class_sha256": "a9c3cb0eb1fb1fccff7c96c00b2db94d95e492b63be313830b28d68270bf6de0", "constructor_offsets": {"magic_number": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 40}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Rare | `provisional` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | [] | `provisional` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | If the enemy has !M! or less HP, set their NL HP to 0. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 如果目标敌人的生命值小于等于 !M! 点， NL 则将其生命值变为0。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Judgment | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 审判 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Judgement", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 如果目标敌人的生命值小于等于30点，则将其生命值变为0<br>如果目标敌人的生命值小于等于40点，则将其生命值变为0.<br>测试画风<br>（图片未提供文字说明） | `single_source` | [审判](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667108&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-Judgment.png/150px-Purple-Judgment.png?85579e", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-JudgmentPlus.png/150px-Purple-JudgmentPlus.png?1bc501"} | `single_source` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/8a9253d514b8a0e457afdefa20dc3861.png"] | `single_source` | [审判](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667108&wiki_id=646570) |
| `source.infobox.description` | If the enemy has (30;40) or less HP, set their HP to 0. | `single_source` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 审判 | `single_source` | [审判](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667108&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Judgment<br>|Image       = Purple-Judgment.png<br>|Color       = Purple<br>|Type        = Skill<br>|Rarity      = Rare<br>|Cost        = 1<br>|Description = If the enemy has (30;40) or less HP, set their HP to 0.<br>}}<br>{{C|Judgment}} is a 1 {{Icon|PE}} cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Rare|Rare}} {{QueryLink|Cards|type:Skill|Skill}} Card. It deals no damage, but if the target has less than 30 (40 if upgraded) HP, it wil... | `single_source` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
