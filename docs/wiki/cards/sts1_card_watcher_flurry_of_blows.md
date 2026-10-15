# 疾风连击 / Flurry of Blows

> 稳定 ID：`sts1.card.watcher.flurry_of_blows`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：疾风连击
- English: Flurry of Blows

## 卡牌属性

- 颜色：`Purple`
- 类型：`Attack`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Hand", "Stance"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `0.0` | Deal 4 damage. Whenever you change Stances, return this from the discard pile to your hand. | 造成4点伤害。你每次转换姿态时，将这张牌从弃牌堆放回你的手牌。 | 未保存 |
| `Upgraded` | `0.0` | Deal 6 damage. Whenever you change Stances, return this from the discard pile to your hand. | 造成6点伤害。你每次转换姿态时，将这张牌从弃牌堆放回你的手牌。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 0 | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 0 | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 4 damage.Whenever you change Stances, return this from the discard pile to your hand. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 4 damage.Whenever you change Stances, return this from the discard pile to your hand. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 6 damage.Whenever you change Stances, return this from the discard pile to your hand. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 6 damage.Whenever you change Stances, return this from the discard pile to your hand. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/FlurryOfBlows.class", "class_sha256": "0627d7601df4fcc1d7a00ac012cf2236227fa66c15c72b2859e1b4c16ba0f0e5", "constructor_offsets": {"damage": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 4}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/FlurryOfBlows.class", "class_sha256": "0627d7601df4fcc1d7a00ac012cf2236227fa66c15c72b2859e1b4c16ba0f0e5", "constructor_offsets": {"damage": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 6}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Hand", "Stance"] | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL Whenever you change Stances, return this from the discard pile to your hand. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 你每次转换 姿态 时，将这张牌从弃牌堆放回你的手牌。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Flurry of Blows | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 疾风连击 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "FlurryOfBlows", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 疾风连击<br>造成4点伤害。你每次转换姿态时，将这张牌从弃牌堆放回你的手牌。<br>疾风连击+<br>造成6点伤害。你每次转换姿态时，将这张牌从弃牌堆放回你的手牌。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [疾风连击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939948&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-FlurryofBlows.png/150px-Purple-FlurryofBlows.png?96dcf9", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-FlurryofBlowsPlus.png/150px-Purple-FlurryofBlowsPlus.png?cf144e"} | `single_source` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/382abef4d4debb2cd62f3e1e16791aec.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/848b47ffcc7c893a1ee75d7c7ab25e80.png"] | `single_source` | [疾风连击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939948&wiki_id=646570) |
| `source.infobox.description` | Deal (4;6) damage. Whenever you change Stances, return this from the discard pile to your hand. | `single_source` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 疾风连击 | `single_source` | [疾风连击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939948&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Flurry of Blows<br>|Image       = Purple-FlurryofBlows.png<br>|Color       = Purple<br>|Type        = Attack<br>|Rarity      = Common<br>|Cost        = 0<br>|Description = Deal (4;6) damage.<br>Whenever you change {{KW|Stance|Stances}}, return this from the discard pile to your hand.<br>|Keywords    = Hand<br>}}<br>{{C|Flurry of Blows}} is a 0 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|t... | `single_source` | [P3 wiki.gg API batch: card 17](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=TURBO|Deep_Breath|Demon_Form|Body_Slam|Catalyst|A_Thousand_Cuts|Sword_Boomerang|Bloodletting|Windmill_Strike|Nirvana|Wheel_Kick|Like_Water|Master_of_Strategy|Cleave|Pray|Tranquility|Reboot|Flurry_of_Blows|Consecrate|Secret_Technique&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
