# 暴雪 / Blizzard

> 稳定 ID：`sts1.card.defect.blizzard`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：暴雪
- English: Blizzard

## 卡牌属性

- 颜色：`Blue`
- 类型：`Attack`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Channel", "Frost"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal damage equal to 2 times the number of Frost Channeled this combat to ALL enemies. | 对所有敌人造成你在本场战斗中生成过的冰霜充能球总数2倍的伤害。 | 未保存 |
| `Upgraded` | `1.0` | Deal damage equal to 3 times the number of Frost Channeled this combat to ALL enemies. | 对所有敌人造成你在本场战斗中生成过的冰霜充能球总数3倍的伤害。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal damage equal to 2 times the number of Frost Channeled this combat to ALL enemies. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal damage equal to 2 times the number of Frost Channeled this combat to ALL enemies. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal damage equal to 3 times the number of Frost Channeled this combat to ALL enemies. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal damage equal to 3 times the number of Frost Channeled this combat to ALL enemies. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Blizzard.class", "class_sha256": "987ee4ba3fc7bdcf690114eb26b25943868a73f861092934853f976e06464919", "constructor_offsets": {"damage": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 0, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Blizzard.class", "class_sha256": "987ee4ba3fc7bdcf690114eb26b25943868a73f861092934853f976e06464919", "constructor_offsets": {"damage": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 0, "magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Channel", "Frost"] | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ALL_ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal damage equal to !M! times the number of Frost Channeled this combat to ALL enemies. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 对所有敌人造成你在本场战斗中 生成 过的 冰霜 充能球总数 !M! 倍的伤害。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Blizzard | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 暴雪 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Blizzard", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 暴雪<br>（图片未提供文字说明）<br>对所有敌人造成你在本回合战斗中生成过的冰霜充能球总数2倍的伤害。<br>暴雪+<br>（图片未提供文字说明）<br>对所有敌人造成你在本回合战斗中生成过的冰霜充能球总数3倍的伤害<br>测试画风<br>（图片未提供文字说明） | `single_source` | [暴雪](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495632&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Blizzard.png/150px-Blue-Blizzard.png?c25d27", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-BlizzardPlus.png/150px-Blue-BlizzardPlus.png?c10c87"} | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/35639ea2f0cea7cf29c9d67c618035b6.png", "https://cdn.max-c.com/heybox/dailynews/img/4cd4996092c2a6d8d6b1dc0b156b74d4.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/f62bde5be7fea0df517455764775edce.png"] | `single_source` | [暴雪](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495632&wiki_id=646570) |
| `source.infobox.description` | Deal damage equal to (2;3) times the number of Frost Channeled this combat to ALL enemies. | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 暴雪 | `single_source` | [暴雪](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495632&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Blizzard<br>|Image       = Blue-Blizzard.png<br>|Color       = Blue<br>|Type        = Attack<br>|Rarity      = Uncommon<br>|Cost        = 1<br>|Description = Deal damage equal to (2;3) times the number of {{KW|Frost}} {{KW|Channel|Channeled}} this combat to ALL enemies.<br>|InteractsWith = Channel, Frost<br>}}<br>{{C|Blizzard}} is a 1 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:Atta... | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
