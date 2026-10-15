# 刮削 / Scrape

> 稳定 ID：`sts1.card.defect.scrape`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：刮削
- English: Scrape

## 卡牌属性

- 颜色：`Blue`
- 类型：`Attack`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Discard", "Draw"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 7 damage. Draw 4 cards. Discard all cards drawn this way that do not cost 0. | 造成7伤害。抽4张牌。丢弃抽到的牌中耗能不为0的牌。 | 未保存 |
| `Upgraded` | `1.0` | Deal 10 damage. Draw 5 cards. Discard all cards drawn this way that do not cost 0. | 造成10伤害。抽5张牌。丢弃抽到的牌中耗能不为0的牌。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 7 damage.Draw 4 cards.Discard all cards drawn this way that do not cost 0. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 7 damage.Draw 4 cards.Discard all cards drawn this way that do not cost 0. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 10 damage.Draw 5 cards.Discard all cards drawn this way that do not cost 0. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 10 damage.Draw 5 cards.Discard all cards drawn this way that do not cost 0. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Scrape.class", "class_sha256": "f4e87fef597c6d0d15388c3443df7da1615238bd13f4d09e4b0469af37e42bd6", "constructor_offsets": {"damage": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 7, "magic_number": 4}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Scrape.class", "class_sha256": "f4e87fef597c6d0d15388c3443df7da1615238bd13f4d09e4b0469af37e42bd6", "constructor_offsets": {"damage": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 10, "magic_number": 5}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Discard", "Draw"] | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL Draw !M! cards. NL Discard all cards drawn this way that do not cost 0. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 伤害。 NL 抽 !M! 张牌。 NL 丢弃抽到的牌中耗能不为0的牌。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Scrape | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 刮削 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Scrape", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 刮削<br>（图片未提供文字说明）<br>造成7点伤害。抽4张牌。丢弃抽到的牌中耗能不为0的牌。<br>刮削+<br>（图片未提供文字说明）<br>造成10点伤害。抽5张牌。丢弃抽到的牌中耗能不为0的牌。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [刮削](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495546&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Scrape.png/150px-Blue-Scrape.png?55c313", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-ScrapePlus.png/150px-Blue-ScrapePlus.png?77b9d5"} | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/49ce28b571e06cb10a10c0c913bff2eb.jpg", "https://cdn.max-c.com/heybox/dailynews/img/9a8c39cb95574dc03298f57d9818574d.jpg", "https://imgheybox.max-c.com/web/bbs/2024/08/24/18cec393e86f08c7a6ea2a976dc37ca6.png"] | `single_source` | [刮削](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495546&wiki_id=646570) |
| `source.infobox.description` | Deal (7;10) damage. Draw (4;5) cards. Discard all cards drawn this way that do not cost 0. | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 刮削 | `single_source` | [刮削](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495546&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>|Name        = Scrape<br>|Image       = Blue-Scrape.png<br>|Color       = Blue<br>|Type        = Attack<br>|Rarity      = Uncommon<br>|Cost        = 1<br>|Description = Deal (7;10) damage.<br>Draw (4;5) cards.<br>Discard all cards drawn this way that do not cost 0.<br>|Keywords    = Draw, Discard<br>}}<br>{{C|Scrape}} is a 1 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:... | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
