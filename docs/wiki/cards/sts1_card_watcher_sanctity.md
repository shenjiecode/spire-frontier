# 圣洁 / Sanctity

> 稳定 ID：`sts1.card.watcher.sanctity`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：圣洁
- English: Sanctity

## 卡牌属性

- 颜色：`Purple`
- 类型：`Skill`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Block", "Draw"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Gain 6 Block. If the last card played this combat was a Skill, draw 2 cards. | 获得6点格挡。如果本场战斗中打出的上一张牌是技能牌，抽2张牌。 | 未保存 |
| `Upgraded` | `1.0` | Gain 9 Block. If the last card played this combat was a Skill, draw 2 cards. | 获得9点格挡。如果本场战斗中打出的上一张牌是技能牌，抽2张牌。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 6 Block. If the last card played this combat was a Skill, draw 2 cards. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Gain 6 Block. If the last card played this combat was a Skill, draw 2 cards. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 9 Block. If the last card played this combat was a Skill, draw 2 cards. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Gain 9 Block. If the last card played this combat was a Skill, draw 2 cards. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Sanctity.class", "class_sha256": "ca410fabb8657705eae8dcf19ac0a5fe712007b387018022999be50fae35c798", "constructor_offsets": {"block": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 6, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Sanctity.class", "class_sha256": "ca410fabb8657705eae8dcf19ac0a5fe712007b387018022999be50fae35c798", "constructor_offsets": {"block": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 9, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block", "Draw"] | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain !B! Block. NL If the last card played this combat was a Skill, draw !M! cards. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得 !B! 点 格挡 。 NL 如果本场战斗中打出的上一张牌是技能牌，抽 !M! 张牌。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Sanctity | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 圣洁 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Sanctity", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 获得6点格挡。如果本场战斗中打出的上一张牌是技能牌，抽2张牌<br>获得9点格挡。如果本场战斗中打出的上一张牌是技能牌，抽2张牌。<br>测试画风 | `single_source` | [圣洁](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667088&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-Sanctity.png/150px-Purple-Sanctity.png?3bfcb1", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-SanctityPlus.png/150px-Purple-SanctityPlus.png?1e633c"} | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/6c8e4c945f08316d8be6d432630a334a.png"] | `single_source` | [圣洁](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667088&wiki_id=646570) |
| `source.infobox.description` | Gain (6;9) Block. If the last card played this combat was a Skill, draw 2 cards. | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 圣洁 | `single_source` | [圣洁](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667088&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Sanctity<br>|Image       = Purple-Sanctity.png<br>|Color       = Purple<br>|Type        = Skill<br>|Rarity      = Uncommon<br>|Cost        = 1<br>|Description = Gain (6;9) {{KW|Block}}. <br>If the last card played this combat was a Skill, draw 2 cards.<br>|Keywords    = Draw<br>}}<br>{{C|Sanctity}} is a 1 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:Attack|Attack}} Card. It gives ... | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
