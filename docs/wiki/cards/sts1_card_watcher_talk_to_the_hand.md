# 以手拒之 / Talk to the Hand

> 稳定 ID：`sts1.card.watcher.talk_to_the_hand`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：以手拒之
- English: Talk to the Hand

## 卡牌属性

- 颜色：`Purple`
- 类型：`Attack`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Block", "Exhaust"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 5 damage. Whenever you attack this enemy, gain 2 Block. Exhaust. | 造成5点伤害。每当目标敌人受到攻击时，你获得2点格挡。消耗。 | 未保存 |
| `Upgraded` | `1.0` | Deal 7 damage. Whenever you attack this enemy, gain 3 Block. Exhaust. | 造成7点伤害。每当目标敌人受到攻击时，你获得3点格挡。消耗。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 5 damage. Whenever you attack this enemy, gain 2 Block. Exhaust. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 5 damage. Whenever you attack this enemy, gain 2 Block. Exhaust. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 7 damage. Whenever you attack this enemy, gain 3 Block. Exhaust. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 7 damage. Whenever you attack this enemy, gain 3 Block. Exhaust. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/TalkToTheHand.class", "class_sha256": "8efaacb0f8aaa5291727e71b0345b6fe82a46a89999e81486b8e52f7a2e58371", "constructor_offsets": {"damage": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 5, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/TalkToTheHand.class", "class_sha256": "8efaacb0f8aaa5291727e71b0345b6fe82a46a89999e81486b8e52f7a2e58371", "constructor_offsets": {"damage": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 7, "magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block", "Exhaust"] | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL Whenever you attack this enemy, gain !M! Block. NL Exhaust. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 每当目标敌人受到攻击时，你获得 !M! 点格挡。 NL 消耗 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Talk to the Hand | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 以手拒之 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "TalkToTheHand", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 以手拒之<br>造成5点伤害。每当目标敌人受到攻击时，你获得2点格挡。消耗。<br>以手拒之+<br>造成7点伤害。每当目标敌人受到攻击时，你获得3点格挡。消耗。<br>会被人工制品抵消。<br>​<br>测试画风<br>（图片未提供文字说明） | `single_source` | [以手拒之](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939954&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-TalktotheHand.png/150px-Purple-TalktotheHand.png?3f7237", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-TalktotheHandPlus.png/150px-Purple-TalktotheHandPlus.png?b60e29"} | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/05915288e0f710ae60c8c1d5d38ac735.png", "https://cdn.max-c.com/heybox/dailynews/img/f73a4abdcf2aae032f6533940a8a2e6e.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/13a32a18fc8c5549703ecd303a495fb5.png"] | `single_source` | [以手拒之](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939954&wiki_id=646570) |
| `source.infobox.description` | Deal (5;7) damage. Whenever you attack this enemy, gain (2;3) Block. Exhaust. | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 以手拒之 | `single_source` | [以手拒之](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939954&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Talk to the Hand<br>|Image       = Purple-TalktotheHand.png<br>|Color       = Purple<br>|Type        = Attack<br>|Rarity      = Uncommon<br>|Cost        = 1<br>|Description = Deal (5;7) damage. Whenever you attack this enemy, gain (2;3) {{KW|Block}}. <br>{{KW|Exhaust}}.<br>}}<br>{{Power Infobox|Block Return}} {{Keyword Infobox|Block}} {{Keyword Infobox|Exhaust}}<br>{{C|Talk to the Hand}} is a 1 {{Icon|PE}} cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryL... | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
