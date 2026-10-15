# 警惕 / Vigilance

> 稳定 ID：`sts1.card.watcher.vigilance`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：警惕
- English: Vigilance

## 卡牌属性

- 颜色：`Purple`
- 类型：`Skill`
- 稀有度：`Basic`
- 可获得性：`card_list`
- 标签：`["Block", "Calm"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `2.0` | Gain 8 Block. Enter Calm. | 获得8点格挡。进入平静。 | 未保存 |
| `Upgraded` | `2.0` | Gain 12 Block. Enter Calm. | 获得12点格挡。进入平静。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

- `starting_deck_contains` → [观者 / Watcher](../characters/sts1_character_watcher.md) ；条件：`{"quantity": 1}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 2 | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 2 | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 8 Block. Enter Calm. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Gain 8 Block. Enter Calm. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 12 Block. Enter Calm. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 12 Block. Enter Calm. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Vigilance.class", "class_sha256": "93753eda12435ccc87dda52065b9758aa29e00dd29ca2b8f6708dac22dade247", "constructor_offsets": {"block": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 8}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Vigilance.class", "class_sha256": "93753eda12435ccc87dda52065b9758aa29e00dd29ca2b8f6708dac22dade247", "constructor_offsets": {"block": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 12}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Basic | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block", "Calm"] | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain !B! Block. NL Enter Calm. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得 !B! 点 格挡 。 NL 进入 平静 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Vigilance | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 警惕 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Vigilance", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 警惕<br>获得8点格挡。进入平静。<br>警惕+<br>获得12点格挡。进入平静。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [警惕](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2988176&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-Vigilance.png/150px-Purple-Vigilance.png?d30995", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-VigilancePlus.png/150px-Purple-VigilancePlus.png?a94e16"} | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/1115d40e127509057d691ebc8357720c.png", "https://cdn.max-c.com/heybox/dailynews/img/821ddbe0c53acdec54939e1c0d0b5083.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/3f716980f4f398f80d1de745c95efb9e.png"] | `single_source` | [警惕](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2988176&wiki_id=646570) |
| `source.infobox.description` | Gain (8;12) Block. Enter Calm. | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 警惕 | `single_source` | [警惕](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2988176&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>| Name        = Vigilance<br>| Image       = Purple-Vigilance.png<br>| Color       = Purple<br>| Type        = Skill<br>| Rarity      = Basic<br>| Cost        = 2<br>| Description = Gain (8;12) {{KW|Block}}. <br>Enter {{KW|Calm}}.<br>| GivesToPlayer = Block, Calm<br>}}<br>{{Keyword Infobox|Calm}} {{Keyword Infobox|Block}}<br>{{C|Vigilance}} is a 2 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Basic|Basic}} {{QueryLink|Cards|type:Skill|Ski... | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
