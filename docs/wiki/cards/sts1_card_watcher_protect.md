# 护身 / Protect

> 稳定 ID：`sts1.card.watcher.protect`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：护身
- English: Protect

## 卡牌属性

- 颜色：`Purple`
- 类型：`Skill`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Block", "Retain"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `2.0` | Retain. Gain 12 Block. | 保留。获得12点格挡。 | 未保存 |
| `Upgraded` | `2.0` | Retain. Gain 16 Block. | 保留。获得16点格挡。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 2 | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 2 | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Retain.Gain 12 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Retain.Gain 12 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Retain.Gain 16 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Retain.Gain 16 Block. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Protect.class", "class_sha256": "559fd1ad835e2f7a2798211ab2050df51f5f7fff590b7b740c5f2fa601c73a28", "constructor_offsets": {"block": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 12}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Protect.class", "class_sha256": "559fd1ad835e2f7a2798211ab2050df51f5f7fff590b7b740c5f2fa601c73a28", "constructor_offsets": {"block": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 16}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block", "Retain"] | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Retain. NL Gain !B! Block. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` |  保留 。 NL 获得 !B! 点 格挡 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Protect | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 护身 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Protect", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 护身<br>保留。获得12点格挡。<br>护身+<br>保留。获得16点格挡。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [护身](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9537855&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-Protect.png/150px-Purple-Protect.png?416cf1", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-ProtectPlus.png/150px-Purple-ProtectPlus.png?6b69fa"} | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/64bb2fd15860218b25ebbcbe9d64a4e6.png", "https://cdn.max-c.com/heybox/dailynews/img/a11163684cb79bf0d44b1e50074a83ba.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/4d537fb70586d98f07253e1ca92900d7.png"] | `single_source` | [护身](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9537855&wiki_id=646570) |
| `source.infobox.description` | Retain. Gain (12;16) Block. | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 护身 | `single_source` | [护身](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9537855&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Protect<br>|Image       = Purple-Protect.png<br>|Color       = Purple<br>|Type        = Skill<br>|Rarity      = Common<br>|Cost        = 2<br>|Description = {{KW|Retain}}.<br>Gain (12;16) {{KW|Block}}.<br>}}<br>{{C|Protect}} is a 2 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|type:Skill|Skill}} Card. It gives 12 (16 if upgraded) {{KW|Block}}. It has {{KW|Retain}}, meaning it will not be di... | `single_source` | [P3 wiki.gg API batch: card 18](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Watcher)|Disarm|Nightmare|Flex|Coolheaded|Seeing_Red|Compile_Driver|Entrench|Bash|Defragment|Blizzard|Electrodynamics|Writhe|Protect|Self_Repair|Parasite|Sanctity|Bludgeon|Mayhem|Wild_Strike&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
