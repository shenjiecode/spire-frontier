# 坚韧 / Perseverance

> 稳定 ID：`sts1.card.watcher.perseverance`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：坚韧
- English: Perseverance

## 卡牌属性

- 颜色：`Purple`
- 类型：`Skill`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Block", "Retain"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Retain. Gain 5 Block. When Retained, increase its Block by 2 this combat. | 保留。获得5点格挡。每当这张牌被保留时，将其在本场战斗的格挡增加2点。 | 未保存 |
| `Upgraded` | `1.0` | Retain. Gain 7 Block. When Retained, increase its Block by 3 this combat. | 保留。获得7点格挡。每当这张牌被保留时，将其在本场战斗的格挡增加3点。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Retain.Gain 5 Block.Whenever this card is Retained, increase its Block by 2. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Retain.Gain 5 Block.Whenever this card is Retained, increase its Block by 2. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Retain.Gain 7 Block.Whenever this card is Retained, increase its Block by 3. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Retain.Gain 7 Block.Whenever this card is Retained, increase its Block by 3. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Perseverance.class", "class_sha256": "4d0dfc1f497bc85c9a5d2bc55b4ec735ad1eaab3058bff00184380861bfc7de0", "constructor_offsets": {"block": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 5, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Perseverance.class", "class_sha256": "4d0dfc1f497bc85c9a5d2bc55b4ec735ad1eaab3058bff00184380861bfc7de0", "constructor_offsets": {"block": 35, "magic_number": 40}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"block": 7, "magic_number": 3}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block", "Retain"] | `provisional` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Retain. NL Gain !B! Block. NL When Retained, increase its Block by !M! this combat. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` |  保留 。 NL 获得 !B! 点 格挡 。 NL 每当这张牌被 保留 时，将其在本场战斗的格挡增加 !M! 点。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Perseverance | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 坚韧 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Perseverance", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 保留。获得5点格挡。每当这张牌被保留时，将其在本场战斗的格挡增加2点<br>保留。获得7点格挡。每当这张牌被保留时，将其在本场战斗的格挡增加3点<br>测试画风<br>（图片未提供文字说明） | `single_source` | [坚韧](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667090&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-Perseverance.png/150px-Purple-Perseverance.png?609ea2", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-PerseverancePlus.png/150px-Purple-PerseverancePlus.png?49c770"} | `single_source` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/52070dd189b70441e2f510fec69df210.png"] | `single_source` | [坚韧](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667090&wiki_id=646570) |
| `source.infobox.description` | Retain. Gain (5;7) Block. Whenever this card is Retained, increase its Block by (2;3). | `single_source` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 坚韧 | `single_source` | [坚韧](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667090&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Perseverance<br>|Image       = Purple-Perseverance.png<br>|Color       = Purple<br>|Type        = Skill<br>|Rarity      = Uncommon<br>|Cost        = 1<br>|Description = {{KW|Retain}}.<br>Gain (5;7) {{KW|Block}}.<br>Whenever this card is {{KW|Retain|Retained}}, increase its {{KW|Block}} by (2;3).<br>}}<br>{{Keyword Infobox|Retain}} {{Keyword Infobox|Block}}<br>{{C|Perseverance}} is a 1 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|... | `single_source` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
