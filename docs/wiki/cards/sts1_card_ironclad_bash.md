# 痛击 / Bash

> 稳定 ID：`sts1.card.ironclad.bash`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：痛击
- English: Bash

## 卡牌属性

- 颜色：`Red`
- 类型：`Attack`
- 稀有度：`Basic`
- 可获得性：`card_list`
- 标签：`["Vulnerable"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `2.0` | Deal 8 damage. Apply 2 Vulnerable. | 造成8点伤害。给予2层易伤。 | 未保存 |
| `Upgraded` | `2.0` | Deal 10 damage. Apply 3 Vulnerable. | 造成10点伤害。给予3层易伤。 | 未保存 |

## 相关条目

- `belongs_to_character` → [铁甲战士 / Ironclad](../characters/sts1_character_ironclad.md)

## 被哪些条目引用

- `starting_deck_contains` → [铁甲战士 / Ironclad](../characters/sts1_character_ironclad.md) ；条件：`{"quantity": 1}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Red | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 2 | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 2 | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 8 damage.Apply 2 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 8 damage.Apply 2 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 10 damage.Apply 3 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 10 damage.Apply 3 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/red/Bash.class", "class_sha256": "1cb0b2abd0fe4060e3ef5b6182bb48c42aa4d28375939d0feec2f0348e3696ce", "constructor_offsets": {"damage": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 8, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/red/Bash.class", "class_sha256": "1cb0b2abd0fe4060e3ef5b6182bb48c42aa4d28375939d0feec2f0348e3696ce", "constructor_offsets": {"damage": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 10, "magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Basic | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Vulnerable"] | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL Apply !M! Vulnerable. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 给予 !M! 层 易伤 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Bash | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 痛击 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Bash", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 痛击<br>（图片未提供文字说明）<br>造成8点伤害。给予2层易伤。<br>痛击+<br>（图片未提供文字说明）<br>造成10点伤害。给予3层易伤。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [痛击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408595&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Red-Bash.png/150px-Red-Bash.png?57867c", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Red-BashPlus.png/150px-Red-BashPlus.png?3df4ff"} | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/14a5380da44909db88ec40786889f9ce.png", "https://cdn.max-c.com/heybox/dailynews/img/466c54aa36f0e6c17d5911c74b011a3e.png", "https://imgheybox.max-c.com/web/bbs/2024/08/21/49c1178285c971b22f9ee28925e9c78c.png"] | `single_source` | [痛击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408595&wiki_id=646570) |
| `source.infobox.description` | Deal (8;10) damage. Apply (2;3) Vulnerable. | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 痛击 | `single_source` | [痛击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408595&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}{{Card Infobox<br>| Name        = Bash<br>| Image       = Red-Bash.png<br>| Color       = Red<br>| Type        = Attack<br>| Rarity      = Basic<br>| Cost        = 2<br>| Description = Deal (8;10) damage.<br>Apply (2;3) {{BD|Vulnerable}}.<br>| GivesToEnemy = Vulnerable<br>}}<br>{{Power Infobox|Vulnerable}}<br>{{C|Bash}} is a 2 {{Icon|RE}}-cost {{QueryLink|Cards|color:Red|Ironclad}} {{QueryLink|Cards|rarity:Basic|Basic}} {{QueryLink|Cards|type:Attack|Attack}} Card. It ... | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:07+00:00
