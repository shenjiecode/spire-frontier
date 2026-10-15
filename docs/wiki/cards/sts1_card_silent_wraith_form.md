# 幽魂形态 / Wraith Form

> 稳定 ID：`sts1.card.silent.wraith_form`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：幽魂形态
- English: Wraith Form

## 卡牌属性

- 颜色：`Green`
- 类型：`Power`
- 稀有度：`Rare`
- 可获得性：`card_list`
- 标签：`["Dexterity", "(Negative)", "Intangible", "Wraith", "Form"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `3.0` | Gain 2 Intangible. At the end of your turn, lose 1 Dexterity. | 获得2层无实体。在每回合结束时失去1点敏捷。 | 未保存 |
| `Upgraded` | `3.0` | Gain 3 Intangible. At the end of your turn, lose 1 Dexterity. | 获得3层无实体。在每回合结束时失去1点敏捷。 | 未保存 |

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
| `card.description (base)` | Gain 2 Intangible.At the end of your turn, lose 1 Dexterity. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Gain 2 Intangible.At the end of your turn, lose 1 Dexterity. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 3 Intangible.At the end of your turn, lose 1 Dexterity. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 3 Intangible.At the end of your turn, lose 1 Dexterity. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/green/WraithForm.class", "class_sha256": "7811d82f1f86a82d8eb52df2376d990085c8e76001b0a4894cfa4a994006cbdf", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/green/WraithForm.class", "class_sha256": "7811d82f1f86a82d8eb52df2376d990085c8e76001b0a4894cfa4a994006cbdf", "constructor_offsets": {"magic_number": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Rare | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Dexterity", "(Negative)", "Intangible", "Wraith", "Form"] | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Power | `provisional` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain !M! Intangible. NL At the end of your turn, lose 1 Dexterity. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得 !M! 层 无实体 。 NL 在每回合结束时失去1点 敏捷 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Wraith Form | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 幽魂形态 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Wraith Form v2", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 幽魂形态<br>（图片未提供文字说明）<br>获得2层无实体。在每回合结束时失去1点敏捷。<br>幽魂形态+<br>（图片未提供文字说明）<br>获得3层无实体。在每回合结束时失去1点敏捷。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [幽魂形态](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495067&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Green-WraithForm.png/150px-Green-WraithForm.png?5c500b", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Green-WraithFormPlus.png/150px-Green-WraithFormPlus.png?7a61df"} | `single_source` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/88930d22a8d658c9b2bc11a807cf1272.jpg", "https://cdn.max-c.com/heybox/dailynews/img/e68977c30a07ed225eee7b65a331d06a.jpg", "https://imgheybox.max-c.com/web/bbs/2024/08/22/2ea08b912c6bd35314408ecc98f5c6a2.png"] | `single_source` | [幽魂形态](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495067&wiki_id=646570) |
| `source.infobox.description` | Gain (2;3) Intangible. At the end of your turn, lose 1 Dexterity. | `single_source` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 幽魂形态 | `single_source` | [幽魂形态](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495067&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>| Name        = Wraith Form<br>| Image       = Green-WraithForm.png<br>| Color       = Green<br>| Type        = Power<br>| Rarity      = Rare<br>| Cost        = 3<br>| Description = Gain (2;3) {{BD|Intangible}}.<br>At the end of your turn, lose 1 {{BD|Dexterity}}.<br>| GivesToPlayer = Intangible, Wraith Form<br>| PowerGives = Dexterity (Negative)<br>}} <br>{{Power Infobox|Intangible}}<br>{{Power Infobox<br>| Name         = Wraith Form<br>| Image ... | `single_source` | [P3 wiki.gg API batch: card 8](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Wish|Charge_Battery|Berserk|Blind|Dark_Embrace|Cold_Snap|Auto-Shields|Wraith_Form|Violence|Flying_Knee|Tactician|Simmering_Fury|Pummel|Sentinel|Dual_Wield|Creative_AI|Eviscerate|Chrysalis|Brutality|Uppercut&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
