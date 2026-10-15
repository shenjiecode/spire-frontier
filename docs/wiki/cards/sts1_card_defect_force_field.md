# 力场 / Force Field

> 稳定 ID：`sts1.card.defect.force_field`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：力场
- English: Force Field

## 卡牌属性

- 颜色：`Blue`
- 类型：`Skill`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Block", "Energy"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `4.0` | Costs 1 less 1 Energyfor each Power card played this combat. Gain 12 Block. | 你在本场战斗中每打出一张能力牌，耗能就减少1点能量。获得12点格挡。 | 未保存 |
| `Upgraded` | `4.0` | Costs 1 less 1 Energyfor each Power card played this combat. Gain 16 Block. | 你在本场战斗中每打出一张能力牌，耗能就减少1点能量。获得16点格挡。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 4 | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 4 | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Costs 1 less 1 Energy for each Power card played this combat.Gain 12 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Costs 1 less 1 Energy for each Power card played this combat.Gain 12 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Costs 1 less 1 Energy for each Power card played this combat.Gain 16 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Costs 1 less 1 Energy for each Power card played this combat.Gain 16 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/ForceField.class", "class_sha256": "ea0d9d09f12c6b9beda2209d7374bf75ba00358ff5a2d57ce13bc0e55d27dec1", "constructor_offsets": {"block": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 12}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/ForceField.class", "class_sha256": "ea0d9d09f12c6b9beda2209d7374bf75ba00358ff5a2d57ce13bc0e55d27dec1", "constructor_offsets": {"block": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 16}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block", "Energy"] | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Costs 1 less [B] for each Power card played this combat. NL Gain !B! Block. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 你在本场战斗中每打出一张能力牌，耗能就减少1 [B] 。 NL 获得 !B! 点 格挡 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Force Field | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 力场 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Force Field", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | （图片未提供文字说明）<br>你在本场战斗中每打出一张能力牌，耗能就减少1点，获得12点格挡。<br>力场+<br>（图片未提供文字说明）<br>你在本场战斗中每打出一张能力牌，耗能就减少1点，获得16点格挡。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [力场](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549944&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-ForceField.png/150px-Blue-ForceField.png?951714", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-ForceFieldPlus.png/150px-Blue-ForceFieldPlus.png?c8ca4c"} | `single_source` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/ed0050bad9b7f408c33c5d13d8877349.png", "https://cdn.max-c.com/heybox/dailynews/img/fee53a60c893d3b137a7b5a20b53559b.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/baf0026dced05939ecf88450491966fe.png"] | `single_source` | [力场](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549944&wiki_id=646570) |
| `source.infobox.description` | Costs 1 less BE for each Power card played this combat. Gain (12;16) Block. | `single_source` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 力场 | `single_source` | [力场](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549944&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Force Field<br>|Image       = Blue-ForceField.png<br>|Color       = Blue<br>|Type        = Skill<br>|Rarity      = Uncommon<br>|Cost        = 4<br>|Description = Costs 1 less {{Icon|BE}} for each Power card played this combat.<br>Gain (12;16) {{KW|Block}}.<br>|Keywords    = Energy<br>}}<br>{{Keyword Infobox|Block}}<br>{{C|Force Field}} is a 4 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|t... | `single_source` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
