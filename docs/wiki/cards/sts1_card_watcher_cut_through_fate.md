# 斩破命运 / Cut Through Fate

> 稳定 ID：`sts1.card.watcher.cut_through_fate`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：斩破命运
- English: Cut Through Fate

## 卡牌属性

- 颜色：`Purple`
- 类型：`Attack`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Draw", "Scry"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 7 damage. Scry 2. Draw 1 card. | 造成7点伤害。预见2。抽1张牌。 | 未保存 |
| `Upgraded` | `1.0` | Deal 9 damage. Scry 3. Draw 1 card. | 造成9点伤害。预见3。抽1张牌。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 7 damage. Scry 2. Draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 7 damage. Scry 2. Draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 9 damage. Scry 3. Draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 9 damage. Scry 3. Draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/CutThroughFate.class", "class_sha256": "1b8f6d1401c4dff3cb6c4c119b34934df0a18f5826f392669c6d2b1b30221705", "constructor_offsets": {"damage": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 7, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/CutThroughFate.class", "class_sha256": "1b8f6d1401c4dff3cb6c4c119b34934df0a18f5826f392669c6d2b1b30221705", "constructor_offsets": {"damage": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 9, "magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Draw", "Scry"] | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL Scry !M!. NL Draw 1 card. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 预见 !M! 。 NL 抽1张牌。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Cut Through Fate | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 斩破命运 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "CutThroughFate", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 斩破命运<br>（图片未提供文字说明）<br>造成7点伤害。预见2。抽1张牌。<br>斩破命运+<br>（图片未提供文字说明）<br>造成9点伤害。预见3。抽1张牌。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [斩破命运](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939946&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-CutThroughFate.png/150px-Purple-CutThroughFate.png?e99475", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-CutThroughFatePlus.png/150px-Purple-CutThroughFatePlus.png?597318"} | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/d26922703352ae569d7604380e29234f.png"] | `single_source` | [斩破命运](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939946&wiki_id=646570) |
| `source.infobox.description` | Deal (7;9) damage. Scry (2;3). Draw 1 card. | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 斩破命运 | `single_source` | [斩破命运](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939946&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Cut Through Fate<br>|Image       = Purple-CutThroughFate.png<br>|Color       = Purple<br>|Type        = Attack<br>|Rarity      = Common<br>|Cost        = 1<br>|Description = Deal (7;9) damage. <br>{{KW|Scry}} (2;3). <br>Draw 1 card.<br>|GivesToPlayer = Draw, Scry<br>}}<br>{{Keyword Infobox|Scry}}<br>{{C|Cut Through Fate}} is a 1 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|type:Attack|Atta... | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
