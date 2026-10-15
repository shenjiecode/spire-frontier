# 内脏切除 / Eviscerate

> 稳定 ID：`sts1.card.silent.eviscerate`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：内脏切除
- English: Eviscerate

## 卡牌属性

- 颜色：`Green`
- 类型：`Attack`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Discard", "Energy"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `3.0` | Costs 1 less 1 Energyfor each card discarded this turn. Deal 7 damage 3 times. | 你在这个回合内每丢弃一张牌，耗能就减少1点能量。造成7点伤害三次。 | 未保存 |
| `Upgraded` | `3.0` | Costs 1 less 1 Energyfor each card discarded this turn. Deal 9 damage 3 times. | 你在这个回合内每丢弃一张牌，耗能就减少1点能量。造成9点伤害三次。 | 未保存 |

## 相关条目

- `belongs_to_character` → [静默猎手 / Silent](../characters/sts1_character_silent.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Green | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 3 | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 3 | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Costs 1 less 1 Energy for each card discarded this turn.Deal 7 damage 3 times. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Costs 1 less 1 Energy for each card discarded this turn.Deal 7 damage 3 times. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Costs 1 less 1 Energy for each card discarded this turn.Deal 9 damage 3 times. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Costs 1 less 1 Energy for each card discarded this turn.Deal 9 damage 3 times. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/green/Eviscerate.class", "class_sha256": "163a16e941396775e861e5983fdae5dc12097acb6628c824f6cfbf849db25ecb", "constructor_offsets": {"damage": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 7}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/green/Eviscerate.class", "class_sha256": "163a16e941396775e861e5983fdae5dc12097acb6628c824f6cfbf849db25ecb", "constructor_offsets": {"damage": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 9}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Discard", "Energy"] | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Costs 1 less [G] NL for each card discarded this turn. NL Deal !D! damage 3 times. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 你在这个回合内每丢弃一张牌，耗能就减少1 [G] 。 NL 造成 !D! 点伤害三次。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Eviscerate | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 内脏切除 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Eviscerate", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 内脏切除<br>（图片未提供文字说明）<br>你在这个回合内每丢弃一张牌，耗能就减少1能量。造成7点伤害三次。<br>内脏切除+<br>（图片未提供文字说明）<br>你在这个回合内每丢弃一张牌，耗能就减少1能量。造成9点伤害三次。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [内脏切除](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494111&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Green-Eviscerate.png/150px-Green-Eviscerate.png?a319fb", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Green-EvisceratePlus.png/150px-Green-EvisceratePlus.png?d28036"} | `single_source` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/2352ed1bcc741eda63afcbbc1f7e7c91.jpg", "https://cdn.max-c.com/heybox/dailynews/img/738beb8494ff9987dee7b94d7b0e0f08.jpg", "https://imgheybox.max-c.com/web/bbs/2024/08/22/e9290fd0f0da6ed2bd1e2dde464b44bf.png"] | `single_source` | [内脏切除](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494111&wiki_id=646570) |
| `source.infobox.description` | Costs 1 less GE for each card discarded this turn. Deal (7;9) damage 3 times. | `single_source` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 内脏切除 | `single_source` | [内脏切除](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494111&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>| Name        = Eviscerate<br>| Image       = Green-Eviscerate.png<br>| Color       = Green<br>| Type        = Attack<br>| Rarity      = Uncommon<br>| Cost        = 3<br>| Description = Costs 1 less {{Icon|GE}} for each card discarded this turn.<br>Deal (7;9) damage 3 times.<br>| GivesToPlayer = Discard, Energy<br>}}<br>{{C|Eviscerate}} is a 3 {{Icon|GE}}-cost {{QueryLink|Cards|color:Green|Silent}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:Attack|At... | `single_source` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
