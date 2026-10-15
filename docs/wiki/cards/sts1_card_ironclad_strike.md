# 打击 / Strike

> 稳定 ID：`sts1.card.ironclad.strike`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：打击
- English: Strike

## 卡牌属性

- 颜色：`Red`
- 类型：`Attack`
- 稀有度：`Basic`
- 可获得性：`card_list`
- 标签：`[]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 6 damage. | 造成6点伤害。 | [查看图片](../../../data/assets/9d73a3b60a0a55cdc8dd7a4a9c3c0031cda98794f9586cfbf415dfd4882625b6.png) |
| `Upgraded` | `1.0` | Deal 9 damage. | 造成9点伤害。 | [查看图片](../../../data/assets/d43887998ca470818040fcf5cc0021cc8744987bb99743a2dbba8ae86ab44f05.png) |

## 相关条目

- `belongs_to_character` → [铁甲战士 / Ironclad](../characters/sts1_character_ironclad.md)

## 被哪些条目引用

- `starting_deck_contains` → [铁甲战士 / Ironclad](../characters/sts1_character_ironclad.md) ；条件：`{"quantity": 5}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Red | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.color (base)` | Red | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.color (upgrade)` | Red | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 6 damage. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 6 damage. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 9 damage. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 9 damage. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/red/Strike_Red.class", "class_sha256": "fbeab2e19185bcf13cddd474d5bd15cde76213e6d5038f4576a7cd542a172032", "constructor_offsets": {"damage": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 6}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/red/Strike_Red.class", "class_sha256": "fbeab2e19185bcf13cddd474d5bd15cde76213e6d5038f4576a7cd542a172032", "constructor_offsets": {"damage": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 9}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Basic | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.rarity (base)` | Basic | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.rarity (upgrade)` | Basic | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.tags` | [] | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags (base)` | [] | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.tags (upgrade)` | [] | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.type (base)` | Attack | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `card.type (upgrade)` | Attack | `provisional` | [Cards List | Slay the Spire 1](https://slaythespire.wiki.gg/wiki/Cards_List) |
| `game.card.description` | Deal !D! damage. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Strike | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 打击 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Strike_R", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 打击<br>造成6点伤害<br>打击+<br>造成9点伤害<br>测试画风<br>（图片未提供文字说明） | `single_source` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=404833&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Red-Strike.png/150px-Red-Strike.png?e35894", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Red-StrikePlus.png/150px-Red-StrikePlus.png?e9819c"} | `single_source` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/2a0aba174896af71965a482ad7975287.png", "https://cdn.max-c.com/heybox/dailynews/img/57720694f596f741a7c87e46347563f9.png", "https://imgheybox.max-c.com/web/bbs/2024/08/21/f8a69dd2b8ae91f10514d0b108b306b7.png"] | `single_source` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=404833&wiki_id=646570) |
| `source.infobox.description` | Deal (6;9) damage. | `single_source` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 打击 | `single_source` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=404833&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}} {{Card Infobox<br>|Name=Strike (Ironclad)<br>|DisplayName=Strike<br>|Image=Red-Strike.png<br>|Color=Red<br>|Type=Attack<br>|Rarity=Basic<br>|Cost=1<br>|Description=Deal (6;9) damage.<br>}}<br>{{C|Strike (Ironclad)|Strike}} is a 1 {{Icon|RE}}-cost {{QueryLink|Cards|color:Red|Ironclad}} {{QueryLink|Cards|rarity:Basic|Basic}} {{QueryLink|Cards|type:Attack|Attack}} Card. It deals 6 (9 if upgraded) damage.<br><br>This page is for Ironclad's version of Strike. Go here for ... | `single_source` | [P3 wiki.gg API batch: card 12](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Purity|Swift_Strike|Defend_(Silent)|Quick_Slash|Strike_(Ironclad)|Defend_(Ironclad)|Tempest|Infinite_Blades|Adrenaline|Madness|Pain|Eruption|Blade_Dance|Outmaneuver|Static_Discharge|Meteor_Strike|Infernal_Blade|Barrage|Setup|Headbutt&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
