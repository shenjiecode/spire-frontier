# 足跟勾 / Heel Hook

> 稳定 ID：`sts1.card.silent.heel_hook`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：足跟勾
- English: Heel Hook

## 卡牌属性

- 颜色：`Green`
- 类型：`Attack`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Draw", "Energy", "Weak"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 5 damage. If the enemy has Weak, gain 1 Energyand draw 1 card. | 造成5点伤害。如果敌人有虚弱状态，获得1点能量并且抽1张牌。 | 未保存 |
| `Upgraded` | `1.0` | Deal 8 damage. If the enemy has Weak, gain 1 Energyand draw 1 card. | 造成8点伤害。如果敌人有虚弱状态，获得1点能量并且抽1张牌。 | 未保存 |

## 相关条目

- `belongs_to_character` → [静默猎手 / Silent](../characters/sts1_character_silent.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Green | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 5 damage. If the enemy has Weak, gain 1 Energy and draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 5 damage. If the enemy has Weak, gain 1 Energy and draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 8 damage. If the enemy has Weak, gain 1 Energy and draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 8 damage. If the enemy has Weak, gain 1 Energy and draw 1 card. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/green/HeelHook.class", "class_sha256": "0fd9629bc5661178b190a5be765c2213ddc5a01fbda4947433b7777befbe6310", "constructor_offsets": {"damage": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 5}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/green/HeelHook.class", "class_sha256": "0fd9629bc5661178b190a5be765c2213ddc5a01fbda4947433b7777befbe6310", "constructor_offsets": {"damage": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 8}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Draw", "Energy", "Weak"] | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL If the enemy has Weak, NL gain [G] and NL draw 1 card. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 如果敌人有 虚弱 状态 ， NL 获得 [G] 并且 NL 抽1张牌。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Heel Hook | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 足跟勾 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Heel Hook", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 足跟勾<br>（图片未提供文字说明）<br>造成5点伤害。如果敌人有虚弱状态，获得能量并且抽1张牌。<br>足跟勾+<br>（图片未提供文字说明）<br>造成8点伤害。如果敌人有虚弱状态，获得能量并且抽1张牌。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [足跟勾](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494130&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Green-HeelHook.png/150px-Green-HeelHook.png?c4924c", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Green-HeelHookPlus.png/150px-Green-HeelHookPlus.png?3c170c"} | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/b1d6eef7c17c8317ec6033044a51db0f.jpg", "https://cdn.max-c.com/heybox/dailynews/img/fb3ef88d376c87773490459703577d63.jpg", "https://imgheybox.max-c.com/web/bbs/2024/08/22/a3e452a4b6af2a6199007c028588a44a.png"] | `single_source` | [足跟勾](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494130&wiki_id=646570) |
| `source.infobox.description` | Deal (5;8) damage. If the enemy has Weak, gain GE and draw 1 card. | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 足跟勾 | `single_source` | [足跟勾](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494130&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Heel Hook<br>|Image       = Green-HeelHook.png<br>|Color       = Green<br>|Type        = Attack<br>|Rarity      = Uncommon<br>|Cost        = 1<br>|Description = Deal (5;8) damage. <br>If the enemy has {{BD|Weak}}, <br>gain {{Icon|GE}} and draw 1 card.<br>|Keywords    = Draw, Energy<br>}}<br>{{C|Heel Hook}} is a 1 {{Icon|GE}}-cost {{QueryLink|Cards|color:Green|Silent}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:Attack|Attack}} Card. It ... | `single_source` | [P3 wiki.gg API batch: card 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Bullseye|Corruption|Expunger|Wave_of_the_Hand|Panic_Button|Scrape|Indignation|Cut_Through_Fate|Hemokinesis|Deflect|Sadistic_Nature|Evaluate|Buffer|Tools_of_the_Trade|Wallop|Blasphemy|Ball_Lightning|Bite|Heel_Hook|Die_Die_Die&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
