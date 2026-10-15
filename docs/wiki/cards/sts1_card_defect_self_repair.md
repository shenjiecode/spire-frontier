# 自我修复 / Self Repair

> 稳定 ID：`sts1.card.defect.self_repair`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：自我修复
- English: Self Repair

## 卡牌属性

- 颜色：`Blue`
- 类型：`Power`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`[]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | At the end of combat, heal 7 HP. | 在战斗结束时，回复7点生命。 | 未保存 |
| `Upgraded` | `1.0` | At the end of combat, heal 10 HP. | 在战斗结束时，回复10点生命。 | 未保存 |

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
| `card.description (base)` | At the end of combat, heal 7 HP. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | At the end of combat, heal 7 HP. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | At the end of combat, heal 10 HP. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | At the end of combat, heal 10 HP. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/SelfRepair.class", "class_sha256": "2f23b9d86343efb9ac3fe5258f9b9b047f4d8c7277f9035b8615c30e4d5467c5", "constructor_offsets": {"magic_number": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 7}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/SelfRepair.class", "class_sha256": "2f23b9d86343efb9ac3fe5258f9b9b047f4d8c7277f9035b8615c30e4d5467c5", "constructor_offsets": {"magic_number": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"magic_number": 10}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | [] | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Power | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | At the end of combat, heal !M! HP. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 在战斗结束时，回复 !M! 点生命。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Self Repair | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 自我修复 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Self Repair", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 自我修复<br>（图片未提供文字说明）<br>在战斗结束时，回复7点生命。<br>自我修复+<br>（图片未提供文字说明）<br>在战斗结束时，回复10点生命。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [自我修复](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=545762&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-SelfRepair.png/150px-Blue-SelfRepair.png?6d5701", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-SelfRepairPlus.png/150px-Blue-SelfRepairPlus.png?811307"} | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/38218a160a8594f544f396de33aedf4b.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/7a3a20773b155e563fc2bd2e2b56f3bf.png"] | `single_source` | [自我修复](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=545762&wiki_id=646570) |
| `source.infobox.description` | At the end of combat, heal (7;10) HP. | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 自我修复 | `single_source` | [自我修复](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=545762&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Self Repair<br>|Image       = Blue-SelfRepair.png<br>|Color       = Blue<br>|Type        = Power<br>|Rarity      = Uncommon<br>|Cost        = 1<br>|Description = At the end of combat, heal (7;10) HP.<br>}}<br>{{Power Infobox|Repair}}{{C|Self Repair}} is a 1 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Uncommon|Uncommon}} {{QueryLink|Cards|type:Power|Power}} Card. It gives 7 (10 if upgraded) {{BD|Repair}}, which will heal you ... | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
