# 爪击 / Claw

> 稳定 ID：`sts1.card.defect.claw`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：爪击
- English: Claw

## 卡牌属性

- 颜色：`Blue`
- 类型：`Attack`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`[]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `0.0` | Deal 3 damage. Increase the damage of ALL Claw cards by 2 this combat. | 造成3点伤害。在本场战斗中所有爪击牌的伤害增加2。 | 未保存 |
| `Upgraded` | `0.0` | Deal 5 damage. Increase the damage of ALL Claw cards by 2 this combat. | 造成5点伤害。在本场战斗中所有爪击牌的伤害增加2。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 0 | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 0 | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 3 damage.Increase the damage of ALL Claw cards by 2 this combat. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 3 damage.Increase the damage of ALL Claw cards by 2 this combat. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 5 damage.Increase the damage of ALL Claw cards by 2 this combat. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 5 damage.Increase the damage of ALL Claw cards by 2 this combat. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Claw.class", "class_sha256": "f5075bfba5c55e3f77694b1150f7b6c3261b7177186b55fb43732fa6d60e8db1", "constructor_offsets": {"damage": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 3, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Claw.class", "class_sha256": "f5075bfba5c55e3f77694b1150f7b6c3261b7177186b55fb43732fa6d60e8db1", "constructor_offsets": {"damage": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 5, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | [] | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL Increase the damage of ALL Claw cards by !M! this combat. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 在本场战斗中所有 爪击 牌的伤害增加 !M! 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Claw | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 爪击 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Gash", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 爪击<br>（图片未提供文字说明）<br>造成3点伤害。在本场战斗中所有爪击牌的伤害增加2。<br>爪击+<br>（图片未提供文字说明）<br>造成5点伤害。在本场战斗中所有爪击牌的伤害增加2。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [爪击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=474553&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Claw.png/150px-Blue-Claw.png?1c3a11", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-ClawPlus.png/150px-Blue-ClawPlus.png?5fe4a1"} | `single_source` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/3186b2789bc4cd3610b0d4bbbf498297.png"] | `single_source` | [爪击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=474553&wiki_id=646570) |
| `source.infobox.description` | Deal (3;5) damage. Increase the damage of ALL Claw cards by 2 this combat. | `single_source` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 爪击 | `single_source` | [爪击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=474553&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>|Name        = Claw<br>|Image       = Blue-Claw.png<br>|Color       = Blue<br>|Type        = Attack<br>|Rarity      = Common<br>|Cost        = 0<br>|Description = Deal (3;5) damage.<br>Increase the damage of ALL Claw cards by 2 this combat.<br>}}<br>{{C|Claw}} is a 0 {{Icon|BE}} cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|type:Attack|Attack}} Card.<br><br>== Interactions ==<br>=== Synergie... | `single_source` | [P3 wiki.gg API batch: card 15](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Sunder|Neutralize|Envenom|Predator|Go_for_the_Eyes|Follow-Up|Metallicize|Force_Field|Master_Reality|Dualcast|Chaos|Fission|Boot_Sequence|Dagger_Spray|Lesson_Learned|Claw|Darkness|Battle_Trance|Dropkick|Magnetism&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
