# 耗尽 / Consume

> 稳定 ID：`sts1.card.defect.consume`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：耗尽
- English: Consume

## 卡牌属性

- 颜色：`Blue`
- 类型：`Skill`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Focus", "Orb"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `2.0` | Gain 2 Focus. Lose 1 Orb slot. | 获得2点集中。失去1个充能球栏位。 | 未保存 |
| `Upgraded` | `2.0` | Gain 3 Focus. Lose 1 Orb slot. | 获得3点集中。失去1个充能球栏位。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 2 | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 2 | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 2 Focus.Lose 1 Orb slot. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Gain 2 Focus.Lose 1 Orb slot. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 3 Focus.Lose 1 Orb slot. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 3 Focus.Lose 1 Orb slot. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Consume.class", "class_sha256": "ad8b341b2ec852ade3bdde17acfd4d86cdc6ac06ff8487a6c1c48abdef8715dd", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Consume.class", "class_sha256": "ad8b341b2ec852ade3bdde17acfd4d86cdc6ac06ff8487a6c1c48abdef8715dd", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Focus", "Orb"] | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain !M! Focus. NL Lose 1 Orb slot. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得 !M! 点 集中 。 NL 失去 1 个充能球栏位。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Consume | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 耗尽 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Consume", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 耗尽<br>（图片未提供文字说明）<br>获得两点集中。失去一个充能球栏位。<br>耗尽+<br>（图片未提供文字说明）<br>获得3点集中。失去一个充能球栏位。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [耗尽](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549935&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Consume.png/150px-Blue-Consume.png?7a67ba", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-ConsumePlus.png/150px-Blue-ConsumePlus.png?bf5afe"} | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/a7221caf29b9bf961f77dea76c45c401.png", "https://cdn.max-c.com/heybox/dailynews/img/ef9cbe6e5406cc25ec4b46b157842272.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/9841419375979af2ab80d53eed52156f.png"] | `single_source` | [耗尽](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549935&wiki_id=646570) |
| `source.infobox.description` | Gain (2;3) Focus. Lose 1 Orb Slot. | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 耗尽 | `single_source` | [耗尽](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549935&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Consume<br>|Image       = Blue-Consume.png<br>|Color       = Blue<br>|Type        = Skill<br>|Rarity      = Uncommon<br>|Cost        = 2<br>|Description = Gain (2;3) {{BD|Focus}}.<br>Lose 1 {{KW|Orb Slot}}.<br>|GivesToPlayer = Focus, Orb Slot<br>}}<br>{{Power Infobox|Focus}} {{Keyword_Infobox|Orb Slot}}<br>{{C|Consume}} is a 2 {{Icon|BE}} cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:Skill|Skill}... | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
