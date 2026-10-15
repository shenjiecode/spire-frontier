# 充电 / Charge Battery

> 稳定 ID：`sts1.card.defect.charge_battery`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：充电
- English: Charge Battery

## 卡牌属性

- 颜色：`Blue`
- 类型：`Skill`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Block", "Energy"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Gain 7 Block. Next turn, gain 1 Energy. | 获得7点格挡。在下一回合获得1点能量。 | 未保存 |
| `Upgraded` | `1.0` | Gain 10 Block. Next turn, gain 1 Energy. | 获得10点格挡。在下一回合获得1点能量。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 7 Block.Next turn, gain 1 Energy. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Gain 7 Block.Next turn, gain 1 Energy. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 10 Block.Next turn, gain 1 Energy. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 10 Block.Next turn, gain 1 Energy. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/ConserveBattery.class", "class_sha256": "de4f8244acd34d132592b5d5f1b595236e9650b3ec6fb490005c6369776a1751", "constructor_offsets": {"block": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 7}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/ConserveBattery.class", "class_sha256": "de4f8244acd34d132592b5d5f1b595236e9650b3ec6fb490005c6369776a1751", "constructor_offsets": {"block": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 10}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block", "Energy"] | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain !B! Block. NL Next turn, gain [B]. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得 !B! 点 格挡 。 NL 在下一回合获得 [B] 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Charge Battery | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 充电 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Conserve Battery", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | （图片未提供文字说明）<br>获得7点格挡。在下一回合获得一点能量。<br>充电+<br>（图片未提供文字说明）<br>获得10点格挡。在下一回合获得一点能量。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [充电](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549928&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-ChargeBattery.png/150px-Blue-ChargeBattery.png?918d86", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-ChargeBatteryPlus.png/150px-Blue-ChargeBatteryPlus.png?b35c39"} | `single_source` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/5f418160dee36302ea3a32aac9038ac7.png", "https://cdn.max-c.com/heybox/dailynews/img/cee798c7413fdc7c9f60e209e4f0253f.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/2ab198b15ca37f38a4bd706000d7d832.png"] | `single_source` | [充电](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549928&wiki_id=646570) |
| `source.infobox.description` | Gain (7;10) Block. Next turn, gain BE. | `single_source` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 充电 | `single_source` | [充电](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549928&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}} <br>{{Card Infobox<br>|Name        = Charge Battery<br>|Image       = Blue-ChargeBattery.png<br>|Color       = Blue<br>|Type        = Skill<br>|Rarity      = Common<br>|Cost        = 1<br>|Description = Gain (7;10) {{KW|Block}}.<br>Next turn, gain {{Icon|BE}}.<br>|GivesToPlayer = Energized (Defect), Block<br>|PowerGives = Energy<br>}} <br>{{Keyword Infobox|Block}} {{Power Infobox|Energized (Defect)}}<br>{{C|Charge Battery}} is a 1 {{Icon|BE}} cost {{QueryLink|Cards|c... | `single_source` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
