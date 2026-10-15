# 扫荡射线 / Sweeping Beam

> 稳定 ID：`sts1.card.defect.sweeping_beam`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：扫荡射线
- English: Sweeping Beam

## 卡牌属性

- 颜色：`Blue`
- 类型：`Attack`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Draw"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 6 damage to ALL enemies. Draw 1 card. | 对所有敌人造成6点伤害。抽1张牌。 | 未保存 |
| `Upgraded` | `1.0` | Deal 9 damage to ALL enemies. Draw 1 card. | 对所有敌人造成9点伤害。抽1张牌。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shame|Perfected_Strike|Pommel_Strike|Alchemize|Shockwave|Overclock|Accuracy|Alpha|Ritual_Dagger|Carve_Reality|Slimed|Bullet_Time|Poisoned_Stab|Inner_Peace|Pride|Thunderclap|Mental_Fortress|Sweeping_Beam|Searing_Blow|Flame_Barrier&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shame|Perfected_Strike|Pommel_Strike|Alchemize|Shockwave|Overclock|Accuracy|Alpha|Ritual_Dagger|Carve_Reality|Slimed|Bullet_Time|Poisoned_Stab|Inner_Peace|Pride|Thunderclap|Mental_Fortress|Sweeping_Beam|Searing_Blow|Flame_Barrier&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shame|Perfected_Strike|Pommel_Strike|Alchemize|Shockwave|Overclock|Accuracy|Alpha|Ritual_Dagger|Carve_Reality|Slimed|Bullet_Time|Poisoned_Stab|Inner_Peace|Pride|Thunderclap|Mental_Fortress|Sweeping_Beam|Searing_Blow|Flame_Barrier&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 6 damage to ALL enemies.Draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 6 damage to ALL enemies.Draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 9 damage to ALL enemies.Draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 9 damage to ALL enemies.Draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/SweepingBeam.class", "class_sha256": "1fec0258372e41ff74890ab5e4e1c66d916c6f28a87dcd7c47c4252694ae6e91", "constructor_offsets": {"damage": 36, "magic_number": 46}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 6, "magic_number": 1}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/SweepingBeam.class", "class_sha256": "1fec0258372e41ff74890ab5e4e1c66d916c6f28a87dcd7c47c4252694ae6e91", "constructor_offsets": {"damage": 36, "magic_number": 46}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 9, "magic_number": 1}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shame|Perfected_Strike|Pommel_Strike|Alchemize|Shockwave|Overclock|Accuracy|Alpha|Ritual_Dagger|Carve_Reality|Slimed|Bullet_Time|Poisoned_Stab|Inner_Peace|Pride|Thunderclap|Mental_Fortress|Sweeping_Beam|Searing_Blow|Flame_Barrier&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Draw"] | `provisional` | [P3 wiki.gg API batch: card 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shame|Perfected_Strike|Pommel_Strike|Alchemize|Shockwave|Overclock|Accuracy|Alpha|Ritual_Dagger|Carve_Reality|Slimed|Bullet_Time|Poisoned_Stab|Inner_Peace|Pride|Thunderclap|Mental_Fortress|Sweeping_Beam|Searing_Blow|Flame_Barrier&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ALL_ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shame|Perfected_Strike|Pommel_Strike|Alchemize|Shockwave|Overclock|Accuracy|Alpha|Ritual_Dagger|Carve_Reality|Slimed|Bullet_Time|Poisoned_Stab|Inner_Peace|Pride|Thunderclap|Mental_Fortress|Sweeping_Beam|Searing_Blow|Flame_Barrier&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage to ALL enemies. NL Draw !M! card. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 对所有敌人造成 !D! 点伤害。 NL 抽 !M! 张牌。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Sweeping Beam | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 扫荡射线 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Sweeping Beam", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 扫荡射线<br>（图片未提供文字说明）<br>对所有敌人造成6点伤害。抽一张牌。<br>扫荡射线+<br>（图片未提供文字说明）<br>对所有敌人造成9点伤害。抽一张牌。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [扫荡射线](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495530&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-SweepingBeam.png/150px-Blue-SweepingBeam.png?7209f1", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-SweepingBeamPlus.png/150px-Blue-SweepingBeamPlus.png?84fa00"} | `single_source` | [P3 wiki.gg API batch: card 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shame|Perfected_Strike|Pommel_Strike|Alchemize|Shockwave|Overclock|Accuracy|Alpha|Ritual_Dagger|Carve_Reality|Slimed|Bullet_Time|Poisoned_Stab|Inner_Peace|Pride|Thunderclap|Mental_Fortress|Sweeping_Beam|Searing_Blow|Flame_Barrier&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/f99f1385163c1e171ad09a8fe09d8442.png"] | `single_source` | [扫荡射线](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495530&wiki_id=646570) |
| `source.infobox.description` | Deal (6;9) damage to ALL enemies. Draw 1 card. | `single_source` | [P3 wiki.gg API batch: card 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shame|Perfected_Strike|Pommel_Strike|Alchemize|Shockwave|Overclock|Accuracy|Alpha|Ritual_Dagger|Carve_Reality|Slimed|Bullet_Time|Poisoned_Stab|Inner_Peace|Pride|Thunderclap|Mental_Fortress|Sweeping_Beam|Searing_Blow|Flame_Barrier&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 扫荡射线 | `single_source` | [扫荡射线](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495530&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>|Name        = Sweeping Beam<br>|Image       = Blue-SweepingBeam.png<br>|Color       = Blue<br>|Type        = Attack<br>|Rarity      = Common<br>|Cost        = 1<br>|Description = Deal (6;9) damage to ALL enemies.<br>Draw 1 card.<br>|Keywords    = Draw<br>}}<br>{{C|Sweeping Beam}} is a 1 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|type:Attack|Attack}} Card.<br><br>== Update His... | `single_source` | [P3 wiki.gg API batch: card 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shame|Perfected_Strike|Pommel_Strike|Alchemize|Shockwave|Overclock|Accuracy|Alpha|Ritual_Dagger|Carve_Reality|Slimed|Bullet_Time|Poisoned_Stab|Inner_Peace|Pride|Thunderclap|Mental_Fortress|Sweeping_Beam|Searing_Blow|Flame_Barrier&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
