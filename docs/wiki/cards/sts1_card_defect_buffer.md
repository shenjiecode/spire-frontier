# 缓冲 / Buffer

> 稳定 ID：`sts1.card.defect.buffer`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：缓冲
- English: Buffer

## 卡牌属性

- 颜色：`Blue`
- 类型：`Power`
- 稀有度：`Rare`
- 可获得性：`card_list`
- 标签：`["Buffer"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `2.0` | Prevent the next time you would lose HP. | 阻止下一次你受到的生命值损伤。 | 未保存 |
| `Upgraded` | `2.0` | Prevent the next 2 times you would lose HP. | 阻止下2次你受到的生命值损伤。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 2 | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 2 | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Prevent the next time you would lose HP. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Prevent the next time you would lose HP. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Prevent the next 2 times you would lose HP. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Prevent the next 2 times you would lose HP. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Buffer.class", "class_sha256": "489174100e366ff927efb42f82d6c5ea84499d2e9945e6b59d5d13cd587f6e51", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 1}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Buffer.class", "class_sha256": "489174100e366ff927efb42f82d6c5ea84499d2e9945e6b59d5d13cd587f6e51", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Rare | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Buffer"] | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Power | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Prevent the next time you would lose HP. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 阻止下一次你受到的生命值损伤。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Buffer | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 缓冲 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Buffer", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 缓冲<br>（图片未提供文字说明）<br>阻止下一次你受到的生命值损伤。<br>缓冲+<br>（图片未提供文字说明）<br>阻止下两次你受到的生命值损伤。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [缓冲](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=529377&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Buffer.png/150px-Blue-Buffer.png?56d482", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-BufferPlus.png/150px-Blue-BufferPlus.png?d7a5e7"} | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/528fc3e1f9aa32f4227735f229e6069a.png", "https://cdn.max-c.com/heybox/dailynews/img/717f19c0bdc60baf250bd24f17bdf1b4.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/ff3c6e3abf562ea412f419ff88b1eadf.png"] | `single_source` | [缓冲](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=529377&wiki_id=646570) |
| `source.infobox.description` | Prevent the next (time;2 times) you would lose HP. | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 缓冲 | `single_source` | [缓冲](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=529377&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}} <br>{{Card Infobox<br>|Name        = Buffer<br>|Image       = Blue-Buffer.png<br>|Color       = Blue<br>|Type        = Power<br>|Rarity      = Rare<br>|Cost        = 2<br>|Description = Prevent the next (time;2 times) you would lose HP.<br>|GivesToPlayer = Buffer<br>}}<br>{{Power Infobox<br>|Name         = Buffer<br>|Image        = Icon Buffer.png<br>|Description  = Prevent the next X times you would lose HP.<br>|Type         = Buff<br>|Stacks       = Counter<br>|Bet... | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
