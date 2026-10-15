# 灾祸 / Bane

> 稳定 ID：`sts1.card.silent.bane`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：灾祸
- English: Bane

## 卡牌属性

- 颜色：`Green`
- 类型：`Attack`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Poison"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 7 damage. If the enemy has Poison, deal 7 damage again. | 造成7点伤害。如果敌人有中毒状态，则再次造成7点伤害。 | 未保存 |
| `Upgraded` | `1.0` | Deal 10 damage. If the enemy has Poison, deal 10 damage again. | 造成10点伤害。如果敌人有中毒状态，则再次造成10点伤害。 | 未保存 |

## 相关条目

- `belongs_to_character` → [静默猎手 / Silent](../characters/sts1_character_silent.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Green | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 7 damage.If the enemy has Poison, deal 7 damage again. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 7 damage.If the enemy has Poison, deal 7 damage again. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 10 damage.If the enemy has Poison, deal 10 damage again. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 10 damage.If the enemy has Poison, deal 10 damage again. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/green/Bane.class", "class_sha256": "5b7417c006d18a7abf0a765ef484c764934bca024d7a4f9607a8a9f1114a244a", "constructor_offsets": {"damage": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 7}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/green/Bane.class", "class_sha256": "5b7417c006d18a7abf0a765ef484c764934bca024d7a4f9607a8a9f1114a244a", "constructor_offsets": {"damage": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 10}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Poison"] | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL If the enemy has Poison, deal !D! damage again. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 如果敌人有 中毒 状态 ，则再次造成 !D! 点伤害。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Bane | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 灾祸 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Bane", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 灾祸<br>（图片未提供文字说明）<br>​造成7点伤害。如果敌人有中毒状态，则再次造成7点伤害。<br>灾祸+<br>（图片未提供文字说明）<br>​造成10点伤害。如果敌人有中毒状态，则再次造成10点伤害。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [灾祸](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494084&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Green-Bane.png/150px-Green-Bane.png?677a95", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Green-BanePlus.png/150px-Green-BanePlus.png?4581a7"} | `single_source` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/033418ad8801b6ab2d936ba1c957666e.jpg", "https://cdn.max-c.com/heybox/dailynews/img/f700507e59e799dc46e618a23d67aaa8.jpg"] | `single_source` | [灾祸](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494084&wiki_id=646570) |
| `source.infobox.description` | Deal (7;10) damage. If the enemy has Poison, deal (7;10) damage again. | `single_source` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 灾祸 | `single_source` | [灾祸](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494084&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>| Name        = Bane<br>| Image       = Green-Bane.png<br>| Color       = Green<br>| Type        = Attack<br>| Rarity      = Common<br>| Cost        = 1<br>| Description = Deal (7;10) damage.<br>If the enemy has {{BD|Poison}}, deal (7;10) damage again.<br>| InteractsWith = Poison<br>}}<br>{{Power Infobox|Poison}}<br>{{C|Bane}} is a 1 {{Icon|GE}}-cost {{QueryLink|Cards|color:Green|Silent}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|type:Attack|Attack}} Card. I... | `single_source` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
