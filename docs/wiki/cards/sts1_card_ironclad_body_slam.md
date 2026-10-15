# 全身撞击 / Body Slam

> 稳定 ID：`sts1.card.ironclad.body_slam`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：全身撞击
- English: Body Slam

## 卡牌属性

- 颜色：`Red`
- 类型：`Attack`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Block"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal damage equal to your Block. | 造成你当前格挡值的伤害。 | [查看图片](../../../data/assets/7fb9cf88aa86a19719869134b1ee6187d7c51ad15118c0d2516ba160d29af0b0.png) |
| `Upgraded` | `0.0` | Deal damage equal to your Block. | 造成你当前格挡值的伤害。 | [查看图片](../../../data/assets/553267f0c3d5cbd40d171449a40b815397c036a65232722cc0f8fdbc5ad2d541.png) |

## 相关条目

- `belongs_to_character` → [铁甲战士 / Ironclad](../characters/sts1_character_ironclad.md)
- `uses_mechanic` → [格挡 / Block](../mechanics/sts1_mechanic_block.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Red | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.color (base)` | Red | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.color (upgrade)` | Red | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 0 | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal damage equal to your Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal damage equal to your Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal damage equal to your Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal damage equal to your Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/red/BodySlam.class", "class_sha256": "0ee8eed2dfd4d9ed5c0120a431aef266dd39f087896a3f9366695147e10faaca", "constructor_offsets": {"damage": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 0}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/red/BodySlam.class", "class_sha256": "0ee8eed2dfd4d9ed5c0120a431aef266dd39f087896a3f9366695147e10faaca", "constructor_offsets": {"damage": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 0}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.rarity (base)` | Common | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.rarity (upgrade)` | Common | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.tags` | ["Block"] | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags (base)` | ["Block"] | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.tags (upgrade)` | ["Block"] | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.type (base)` | Attack | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.type (upgrade)` | Attack | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `game.card.description` | Deal damage equal to your Block. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成你当前 格挡 值的伤害。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Body Slam | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 全身撞击 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Body Slam", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 全身撞击<br>（图片未提供文字说明）<br>造成你当前格挡值的伤害。<br>全身撞击+<br>（图片未提供文字说明）<br>造成你当前格挡值的伤害。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [全身撞击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408598&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Red-BodySlam.png/150px-Red-BodySlam.png?79afd3", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Red-BodySlamPlus.png/150px-Red-BodySlamPlus.png?323936"} | `single_source` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/8f55281f8ab94da1df856bf7de0357f3.png", "https://cdn.max-c.com/heybox/dailynews/img/9f710fd7f61956a92650fe48d6aa26cf.png", "https://imgheybox.max-c.com/web/bbs/2024/08/21/c5526ebef973f76ff23577081203144c.png"] | `single_source` | [全身撞击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408598&wiki_id=646570) |
| `source.infobox.description` | Deal damage equal to your Block. | `single_source` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 全身撞击 | `single_source` | [全身撞击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408598&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>| Name        = Body Slam<br>| Image       = Red-BodySlam.png<br>| Color       = Red<br>| Type        = Attack<br>| Rarity      = Common<br>| Cost        = 1<br>| CostPlus    = 0<br>| Description = Deal damage equal to your {{KW|Block}}.<br>| InteractsWith = Block<br>}}<br>{{Keyword Infobox|Block}}<br>{{C|Body Slam}} is a 1 (0 if upgraded) {{Icon|RE}}-cost {{QueryLink|Cards|color:Red|Ironclad}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink... | `single_source` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
