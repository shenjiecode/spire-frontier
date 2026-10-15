# 祭品 / Offering

> 稳定 ID：`sts1.card.ironclad.offering`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：祭品
- English: Offering

## 卡牌属性

- 颜色：`Red`
- 类型：`Skill`
- 稀有度：`Rare`
- 可获得性：`card_list`
- 标签：`["Draw", "Energy", "Exhaust", "Lose", "HP"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `0.0` | Lose 6 HP. Gain 2 Energy. Draw 3 cards. Exhaust. | 失去6点生命。获得2点能量。抽3张牌。消耗。 | 未保存 |
| `Upgraded` | `0.0` | Lose 6 HP. Gain 2 Energy. Draw 5 cards. Exhaust. | 失去6点生命。获得2点能量。抽5张牌。消耗。 | 未保存 |

## 相关条目

- `belongs_to_character` → [铁甲战士 / Ironclad](../characters/sts1_character_ironclad.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Red | `provisional` | [P3 wiki.gg API batch: card 14](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Dazed|Prostrate|Calculated_Gamble|Core_Surge|Bouncing_Flask|Reach_Heaven|Sever_Soul|Reinforced_Body|Footwork|Genetic_Algorithm|Cloak_and_Dagger|Empty_Body|Seek|Rage|Defend_(Defect)|Pressure_Points|Streamline|Equilibrium|Offering|Anger&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 0 | `provisional` | [P3 wiki.gg API batch: card 14](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Dazed|Prostrate|Calculated_Gamble|Core_Surge|Bouncing_Flask|Reach_Heaven|Sever_Soul|Reinforced_Body|Footwork|Genetic_Algorithm|Cloak_and_Dagger|Empty_Body|Seek|Rage|Defend_(Defect)|Pressure_Points|Streamline|Equilibrium|Offering|Anger&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 0 | `provisional` | [P3 wiki.gg API batch: card 14](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Dazed|Prostrate|Calculated_Gamble|Core_Surge|Bouncing_Flask|Reach_Heaven|Sever_Soul|Reinforced_Body|Footwork|Genetic_Algorithm|Cloak_and_Dagger|Empty_Body|Seek|Rage|Defend_(Defect)|Pressure_Points|Streamline|Equilibrium|Offering|Anger&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Lose 6 HP.Gain 2 Energy.Draw 3 cards.Exhaust. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Lose 6 HP.Gain 2 Energy.Draw 3 cards.Exhaust. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Lose 6 HP.Gain 2 Energy.Draw 5 cards.Exhaust. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Lose 6 HP.Gain 2 Energy.Draw 5 cards.Exhaust. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/red/Offering.class", "class_sha256": "ae957b4a1b3959292310a32004561d46b57cb4580acca41e5544a69038245281", "constructor_offsets": {"magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/red/Offering.class", "class_sha256": "ae957b4a1b3959292310a32004561d46b57cb4580acca41e5544a69038245281", "constructor_offsets": {"magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 5}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Rare | `provisional` | [P3 wiki.gg API batch: card 14](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Dazed|Prostrate|Calculated_Gamble|Core_Surge|Bouncing_Flask|Reach_Heaven|Sever_Soul|Reinforced_Body|Footwork|Genetic_Algorithm|Cloak_and_Dagger|Empty_Body|Seek|Rage|Defend_(Defect)|Pressure_Points|Streamline|Equilibrium|Offering|Anger&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Draw", "Energy", "Exhaust", "Lose", "HP"] | `provisional` | [P3 wiki.gg API batch: card 14](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Dazed|Prostrate|Calculated_Gamble|Core_Surge|Bouncing_Flask|Reach_Heaven|Sever_Soul|Reinforced_Body|Footwork|Genetic_Algorithm|Cloak_and_Dagger|Empty_Body|Seek|Rage|Defend_(Defect)|Pressure_Points|Streamline|Equilibrium|Offering|Anger&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 14](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Dazed|Prostrate|Calculated_Gamble|Core_Surge|Bouncing_Flask|Reach_Heaven|Sever_Soul|Reinforced_Body|Footwork|Genetic_Algorithm|Cloak_and_Dagger|Empty_Body|Seek|Rage|Defend_(Defect)|Pressure_Points|Streamline|Equilibrium|Offering|Anger&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Lose 6 HP. NL Gain [R] [R]. NL Draw !M! cards. NL Exhaust. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 失去 6 点生命。 NL 获得 [R] [R] 。 NL 抽 !M! 张牌。 NL 消耗 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Offering | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 祭品 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Offering", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 祭品<br>（图片未提供文字说明）<br>失去6点生命。获得两点能量。抽3张牌。消耗。<br>祭品+<br>（图片未提供文字说明）<br>失去6点生命。获得两点能量。抽5张牌。消耗。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [祭品](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=412556&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Red-Offering.png/150px-Red-Offering.png?39a0a3", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Red-OfferingPlus.png/150px-Red-OfferingPlus.png?b1af06"} | `single_source` | [P3 wiki.gg API batch: card 14](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Dazed|Prostrate|Calculated_Gamble|Core_Surge|Bouncing_Flask|Reach_Heaven|Sever_Soul|Reinforced_Body|Footwork|Genetic_Algorithm|Cloak_and_Dagger|Empty_Body|Seek|Rage|Defend_(Defect)|Pressure_Points|Streamline|Equilibrium|Offering|Anger&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/21/82cfad43e9ebfa9bebf9492f2222c6e0.png"] | `single_source` | [祭品](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=412556&wiki_id=646570) |
| `source.infobox.description` | Lose 6 HP. Gain 能量 能量. Draw (3;5) cards. Exhaust. | `single_source` | [P3 wiki.gg API batch: card 14](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Dazed|Prostrate|Calculated_Gamble|Core_Surge|Bouncing_Flask|Reach_Heaven|Sever_Soul|Reinforced_Body|Footwork|Genetic_Algorithm|Cloak_and_Dagger|Empty_Body|Seek|Rage|Defend_(Defect)|Pressure_Points|Streamline|Equilibrium|Offering|Anger&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 祭品 | `single_source` | [祭品](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=412556&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>| Name        = Offering<br>| Image       = Red-Offering.png<br>| Color       = Red<br>| Type        = Skill<br>| Rarity      = Rare<br>| Cost        = 0<br>| Description = Lose 6 HP.<br>Gain {{Icon|RE}} {{Icon|RE}}.<br>Draw (3;5) cards.<br>{{KW|Exhaust}}.<br>| GivesToPlayer = Lose HP, Energy, Exhaust, Draw<br>}}<br>{{Keyword Infobox|Energy}} {{Keyword Infobox|Exhaust}}<br>{{C|Offering}} is a 0 {{Icon|RE}}-cost {{QueryLink|Cards|color:Red|Ironcla... | `single_source` | [P3 wiki.gg API batch: card 14](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Dazed|Prostrate|Calculated_Gamble|Core_Surge|Bouncing_Flask|Reach_Heaven|Sever_Soul|Reinforced_Body|Footwork|Genetic_Algorithm|Cloak_and_Dagger|Empty_Body|Seek|Rage|Defend_(Defect)|Pressure_Points|Streamline|Equilibrium|Offering|Anger&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
