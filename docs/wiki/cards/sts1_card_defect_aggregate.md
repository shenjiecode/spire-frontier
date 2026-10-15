# 汇集 / Aggregate

> 稳定 ID：`sts1.card.defect.aggregate`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：汇集
- English: Aggregate

## 卡牌属性

- 颜色：`Blue`
- 类型：`Skill`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Energy"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Gain 1 Energyfor every 4 cards in your draw pile. | 你的抽牌堆中每有4张牌，获得1点能量。 | 未保存 |
| `Upgraded` | `1.0` | Gain 1 Energyfor every 3 cards in your draw pile. | 你的抽牌堆中每有3张牌，获得1点能量。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 9](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Malaise|Escape_Plan|Corpse_Explosion|Capacitor|Crippling_Cloud|After_Image|Sneaky_Strike|Blur|Iron_Wave|Wound|Trip|Exhume|Weave|Expertise|Aggregate|Leap|Flash_of_Steel|Whirlwind|Leg_Sweep|Metamorphosis&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 9](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Malaise|Escape_Plan|Corpse_Explosion|Capacitor|Crippling_Cloud|After_Image|Sneaky_Strike|Blur|Iron_Wave|Wound|Trip|Exhume|Weave|Expertise|Aggregate|Leap|Flash_of_Steel|Whirlwind|Leg_Sweep|Metamorphosis&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 9](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Malaise|Escape_Plan|Corpse_Explosion|Capacitor|Crippling_Cloud|After_Image|Sneaky_Strike|Blur|Iron_Wave|Wound|Trip|Exhume|Weave|Expertise|Aggregate|Leap|Flash_of_Steel|Whirlwind|Leg_Sweep|Metamorphosis&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 1 Energy for every 4 cards in your draw pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Gain 1 Energy for every 4 cards in your draw pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 1 Energy for every 3 cards in your draw pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 1 Energy for every 3 cards in your draw pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Aggregate.class", "class_sha256": "148de223589731c3943113a03fd602a4735b680b0e801229596ffa6dbf850ae7", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 4}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Aggregate.class", "class_sha256": "148de223589731c3943113a03fd602a4735b680b0e801229596ffa6dbf850ae7", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 9](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Malaise|Escape_Plan|Corpse_Explosion|Capacitor|Crippling_Cloud|After_Image|Sneaky_Strike|Blur|Iron_Wave|Wound|Trip|Exhume|Weave|Expertise|Aggregate|Leap|Flash_of_Steel|Whirlwind|Leg_Sweep|Metamorphosis&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Energy"] | `provisional` | [P3 wiki.gg API batch: card 9](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Malaise|Escape_Plan|Corpse_Explosion|Capacitor|Crippling_Cloud|After_Image|Sneaky_Strike|Blur|Iron_Wave|Wound|Trip|Exhume|Weave|Expertise|Aggregate|Leap|Flash_of_Steel|Whirlwind|Leg_Sweep|Metamorphosis&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 9](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Malaise|Escape_Plan|Corpse_Explosion|Capacitor|Crippling_Cloud|After_Image|Sneaky_Strike|Blur|Iron_Wave|Wound|Trip|Exhume|Weave|Expertise|Aggregate|Leap|Flash_of_Steel|Whirlwind|Leg_Sweep|Metamorphosis&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain [B] for every !M! cards in your draw pile. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 你的抽牌堆中每有 !M! 张牌，获得一点 [B] 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Aggregate | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 汇集 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Aggregate", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | （图片未提供文字说明）<br>你的抽牌堆中每有4张牌，获得一点能量。<br>汇集+<br>（图片未提供文字说明）<br>你的抽牌堆中每有3张牌，获得一点能量。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [汇集](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549937&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Aggregate.png/150px-Blue-Aggregate.png?160957", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-AggregatePlus.png/150px-Blue-AggregatePlus.png?6d0a5c"} | `single_source` | [P3 wiki.gg API batch: card 9](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Malaise|Escape_Plan|Corpse_Explosion|Capacitor|Crippling_Cloud|After_Image|Sneaky_Strike|Blur|Iron_Wave|Wound|Trip|Exhume|Weave|Expertise|Aggregate|Leap|Flash_of_Steel|Whirlwind|Leg_Sweep|Metamorphosis&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/91e90b06962b157ab0a4d9fc5526fcfb.jpg", "https://cdn.max-c.com/heybox/dailynews/img/e51842d26857b31a62b3edd9f330b6ed.jpg", "https://imgheybox.max-c.com/web/bbs/2024/08/24/dd8c3de91be1a143e6463bfcec16fb81.png"] | `single_source` | [汇集](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549937&wiki_id=646570) |
| `source.infobox.description` | Gain BE for every (4;3) cards in your draw pile. | `single_source` | [P3 wiki.gg API batch: card 9](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Malaise|Escape_Plan|Corpse_Explosion|Capacitor|Crippling_Cloud|After_Image|Sneaky_Strike|Blur|Iron_Wave|Wound|Trip|Exhume|Weave|Expertise|Aggregate|Leap|Flash_of_Steel|Whirlwind|Leg_Sweep|Metamorphosis&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 汇集 | `single_source` | [汇集](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549937&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>| Name        = Aggregate<br>| Image       = Blue-Aggregate.png<br>| Color       = Blue<br>| Type        = Skill<br>| Rarity      = Uncommon<br>| Cost        = 1<br>| Description = Gain {{Icon|BE}} for every (4;3) cards in your draw pile.<br>| GivesToPlayer = Energy<br>}}<br>{{C|Aggregate}} is a 1 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:Skill|Skill}} Card. It gives 1 {{Icon|BE}} '''Energy''' f... | `single_source` | [P3 wiki.gg API batch: card 9](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Malaise|Escape_Plan|Corpse_Explosion|Capacitor|Crippling_Cloud|After_Image|Sneaky_Strike|Blur|Iron_Wave|Wound|Trip|Exhume|Weave|Expertise|Aggregate|Leap|Flash_of_Steel|Whirlwind|Leg_Sweep|Metamorphosis&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
