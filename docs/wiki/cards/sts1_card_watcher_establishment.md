# 确立基础 / Establishment

> 稳定 ID：`sts1.card.watcher.establishment`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：确立基础
- English: Establishment

## 卡牌属性

- 颜色：`Purple`
- 类型：`Power`
- 稀有度：`Rare`
- 可获得性：`card_list`
- 标签：`["Innate", "Retain"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Whenever a card is Retained, reduce its cost by 1 this combat. | 每当有卡牌被保留时，将其在本场战斗的耗能减少1。 | 未保存 |
| `Upgraded` | `1.0` | Innate. Whenever a card is Retained, reduce its cost by 1 this combat. | 固有。每当有卡牌被保留时，将其在本场战斗的耗能减少1。 | 未保存 |

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
| `card.description (base)` | Whenever a card is Retained, lower its cost by 1. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Whenever a card is Retained, lower its cost by 1. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Innate. Whenever a card is Retained, lower its cost by 1. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Innate. Whenever a card is Retained, lower its cost by 1. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Establishment.class", "class_sha256": "478d4f10f40f1008af257a0d51468e5dcad4e10327a8b431bfcabe9e746e4c44", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 1}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Establishment.class", "class_sha256": "478d4f10f40f1008af257a0d51468e5dcad4e10327a8b431bfcabe9e746e4c44", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 1}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Rare | `provisional` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Innate", "Retain"] | `provisional` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Power | `provisional` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Whenever a card is Retained, reduce its cost by !M! this combat. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 每当有卡牌被 保留 时，将其在本场战斗的耗能减少 !M! 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Establishment | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 确立基础 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Establishment", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 确立基础<br>每当有卡牌被保留时，将其在本场战斗的耗能减少1。<br>确立基础+<br>固有。每当有卡牌被保留i时，将其在本场战斗的耗能减少1。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [确立基础](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9958989&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-Establishment.png/150px-Purple-Establishment.png?9c0ea0", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-EstablishmentPlus.png/150px-Purple-EstablishmentPlus.png?28bfa4"} | `single_source` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/dcaa8b67bb2056adc7f009699138aace.png"] | `single_source` | [确立基础](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9958989&wiki_id=646570) |
| `source.infobox.description` | (;Innate. )Whenever a card is Retained, lower its cost by 1. | `single_source` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 确立基础 | `single_source` | [确立基础](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9958989&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Establishment<br>|Image       = Purple-Establishment.png<br>|Color       = Purple<br>|Type        = Power<br>|Rarity      = Rare<br>|Cost        = 1<br>|Description = (;{{KW|Innate}}. )Whenever a card is {{KW|Retain|Retained}}, lower its cost by 1.<br>}}<br>{{Power Infobox|Establishment}}{{Keyword Infobox|Retain}}<br>{{C|Establishment}} is a 1 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Rare|Rare}} {{QueryLink|Cards|type:... | `single_source` | [P3 wiki.gg API batch: card 7](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Jack_of_All_Trades|Piercing_Wail|Intimidate|Rushdown|Empty_Fist|Establishment|Judgment|Double_Tap|Rampage|Ghostly_Armor|Amplify|Panacea|Void|Dodge_and_Roll|J.A.X.|Crescendo|Riddle_with_Holes|Recycle|Skewer|Thinking_Ahead&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
