# 堆栈 / Stack

> 稳定 ID：`sts1.card.defect.stack`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：堆栈
- English: Stack

## 卡牌属性

- 颜色：`Blue`
- 类型：`Skill`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Block"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Gain Block equal to the number of cards in your discard pile. | 获得与你当前弃牌堆中牌数相等的格挡值。 | 未保存 |
| `Upgraded` | `1.0` | Gain Block equal to the number of cards in your discard pile +3. | 获得你当前弃牌堆中牌数+3的格挡值。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain Block equal to the number of cards in your discard pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Gain Block equal to the number of cards in your discard pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain Block equal to the number of cards in your discard pile+3. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain Block equal to the number of cards in your discard pile+3. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Stack.class", "class_sha256": "9b1343edea53a5d2e6bc416aa592b209029d25c5bc5bd1797883791d4b8220e7", "constructor_offsets": {"block": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 0}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Stack.class", "class_sha256": "9b1343edea53a5d2e6bc416aa592b209029d25c5bc5bd1797883791d4b8220e7", "constructor_offsets": {"block": 35}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block"] | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain Block equal to the number of cards in your discard pile. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得与你当前弃牌堆中牌数相等的 格挡 值。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Stack | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 堆栈 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Stack", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | （图片未提供文字说明）<br>获得与你当前弃牌堆数相等的格挡值。<br>堆栈+<br>（图片未提供文字说明）<br>获得与你当前弃牌堆数+3的格挡值。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [堆栈](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549931&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Stack.png/150px-Blue-Stack.png?6aa0ca", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-StackPlus.png/150px-Blue-StackPlus.png?fb1e59"} | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/708a9ad50a05dd4e4e54584587ac4342.png", "https://cdn.max-c.com/heybox/dailynews/img/90febaf35fbb83bce850984610a605a1.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/dc7cc1e089a350197c1e04e01cf775a4.png"] | `single_source` | [堆栈](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549931&wiki_id=646570) |
| `source.infobox.description` | Gain Block equal to the number of cards in your discard pile(;+3). | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 堆栈 | `single_source` | [堆栈](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=549931&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>|Name        = Stack<br>|Image       = Blue-Stack.png<br>|Color       = Blue<br>|Type        = Skill<br>|Rarity      = Common<br>|Cost        = 1<br>|Description = Gain {{KW|Block}} equal to the number of cards in your discard pile(;+3).<br>}}<br>{{Keyword Infobox|Block}}<br>{{C|Stack}} is a 1 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|type:Skill|Skill}} Card.<br><br>== Intera... | `single_source` | [P3 wiki.gg API batch: card 10](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Shiv|Discovery|Power_Through|Noxious_Fumes|Biased_Cognition|Study|Devotion|Talk_to_the_Hand|Melter|Hyperbeam|Reckless_Charge|Through_Violence|Juggernaut|Glass_Knife|Fusion|Panache|Consume|Vigilance|Rip_and_Tear|Stack&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
