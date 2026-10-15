# 粉碎关节 / Crush Joints

> 稳定 ID：`sts1.card.watcher.crush_joints`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：粉碎关节
- English: Crush Joints

## 卡牌属性

- 颜色：`Purple`
- 类型：`Attack`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Vulnerable"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 8 damage. If the last card played this combat was a Skill, apply 1 Vulnerable. | 造成8点伤害。如果本场战斗中打出的上一张牌是技能牌，给予1层易伤。 | 未保存 |
| `Upgraded` | `1.0` | Deal 10 damage. If the last card played this combat was a Skill, apply 2 Vulnerable. | 造成10点伤害。如果本场战斗中打出的上一张牌是技能牌，给予2层易伤。 | 未保存 |

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
| `card.description (base)` | Deal 8 damage.If the last card played this combat was a Skill, apply 1 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 8 damage.If the last card played this combat was a Skill, apply 1 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 10 damage.If the last card played this combat was a Skill, apply 2 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 10 damage.If the last card played this combat was a Skill, apply 2 Vulnerable. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/CrushJoints.class", "class_sha256": "cfe94ee749ffe569bfec1aa8f68ccf5662a92184e6eeba4898dfc1a9c8a106e1", "constructor_offsets": {"damage": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 8, "magic_number": 1}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/CrushJoints.class", "class_sha256": "cfe94ee749ffe569bfec1aa8f68ccf5662a92184e6eeba4898dfc1a9c8a106e1", "constructor_offsets": {"damage": 36, "magic_number": 41}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 10, "magic_number": 2}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Vulnerable"] | `provisional` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL If the last card played this combat was a Skill, apply !M! Vulnerable. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 如果本场战斗中打出的上一张牌是技能牌，给予 !M! 层 易伤 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Crush Joints | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 粉碎关节 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "CrushJoints", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 粉碎关节<br>造成8点伤害。如果本场战斗中打出的上一张牌是技能牌，给予1层易伤。<br>粉碎关节+<br>造成10点伤害。如果本场战斗中打出的上一张牌是技能牌，给予2层易伤。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [粉碎关节](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939950&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-CrushJoints.png/150px-Purple-CrushJoints.png?a02aaa", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-CrushJointsPlus.png/150px-Purple-CrushJointsPlus.png?17254e"} | `single_source` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/2d2679c0289a15031cfb86fdff258c7c.png", "https://cdn.max-c.com/heybox/dailynews/img/333b87555ed24c24e83f66dae3a4aee9.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/5c759be39964eaf00e5a78156dd1ec1e.png"] | `single_source` | [粉碎关节](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939950&wiki_id=646570) |
| `source.infobox.description` | Deal (8;10) damage. If the last card played this combat was a Skill, apply (1;2) Vulnerable. | `single_source` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 粉碎关节 | `single_source` | [粉碎关节](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939950&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Crush Joints<br>|Image       = Purple-CrushJoints.png<br>|Color       = Purple<br>|Type        = Attack<br>|Rarity      = Common<br>|Cost        = 1<br>|Description = Deal (8;10) damage.<br>If the last card played this combat was a {{QueryLink|Cards|type:Skill|Skill}}, apply (1;2) {{BD|Vulnerable}}.<br>|GivesToEnemy = Vulnerable<br>}}<br>{{C|Crush Joints}} is a 1 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Common|Common}}... | `single_source` | [P3 wiki.gg API batch: card 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Carnage|Warcry|Chill|Apotheosis|Double_Energy|Secret_Weapon|Perseverance|Wreath_of_Flame|Crush_Joints|Deva_Form|Hand_of_Greed|Forethought|Caltrops|Storm_of_Steel|Acrobatics|Skim|Good_Instincts|White_Noise|Spot_Weakness|Well-Laid_Plans&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
