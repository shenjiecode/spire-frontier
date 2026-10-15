# 防御 / Defend

> 稳定 ID：`sts1.card.ironclad.defend`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：防御
- English: Defend

## 卡牌属性

- 颜色：`Red`
- 类型：`Skill`
- 稀有度：`Basic`
- 可获得性：`card_list`
- 标签：`["Block"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Gain 5 Block. | 获得5点格挡。 | 未保存 |
| `Upgraded` | `1.0` | Gain 8 Block. | 获得8点格挡。 | 未保存 |

## 相关条目

- `belongs_to_character` → [铁甲战士 / Ironclad](../characters/sts1_character_ironclad.md)

## 被哪些条目引用

- `starting_deck_contains` → [铁甲战士 / Ironclad](../characters/sts1_character_ironclad.md) ；条件：`{"quantity": 4}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Red | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 5 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Gain 5 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 8 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 8 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/red/Defend_Red.class", "class_sha256": "6ab4a01175dd549360e1bb426bdf107c62f6328e05c61b5947e07d1fef72a65b", "constructor_offsets": {"block": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 5}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/red/Defend_Red.class", "class_sha256": "6ab4a01175dd549360e1bb426bdf107c62f6328e05c61b5947e07d1fef72a65b", "constructor_offsets": {"block": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 8}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Basic | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block"] | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain !B! Block. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得 !B! 点 格挡 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Defend | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 防御 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Defend_R", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 防御<br>（图片未提供文字说明）<br>获得5点格挡。<br>防御+<br>（图片未提供文字说明）<br>获得8点格挡。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [防御](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408683&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Red-Defend.png/150px-Red-Defend.png?c0245b", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Red-DefendPlus.png/150px-Red-DefendPlus.png?7a7e56"} | `single_source` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/21/ed85a27dc13488141de37bbaec90a52d.png"] | `single_source` | [防御](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408683&wiki_id=646570) |
| `source.infobox.description` | Gain (5;8) Block. | `single_source` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 防御 | `single_source` | [防御](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408683&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>| Name        = Defend (Ironclad)<br>| DisplayName = Defend<br>| Image       = Red-Defend.png<br>| Color       = Red<br>| Type        = Skill<br>| Rarity      = Basic<br>| Cost        = 1<br>| Description = Gain (5;8) {{KW|Block}}.<br>| GivesToPlayer = Block<br>}}<br>{{Keyword Infobox|Block}}<br>{{C|Defend (Ironclad)|Defend}} is a 1 {{Icon|RE}}-cost {{QueryLink|Cards|color:Red|Ironclad}} {{QueryLink|Cards|rarity:Basic|Basic}} {{QueryLink|Cards|ty... | `single_source` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
