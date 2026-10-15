# 多重释放 / Multi-Cast

> 稳定 ID：`sts1.card.defect.multi_cast`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：多重释放
- English: Multi-Cast

## 卡牌属性

- 颜色：`Blue`
- 类型：`Skill`
- 稀有度：`Rare`
- 可获得性：`card_list`
- 标签：`["Evoke"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `X` | Evoke your next Orb X times. | 激发你最右侧的充能球X次。 | 未保存 |
| `Upgraded` | `X` | Evoke your next Orb X+1 times. | 激发你最右侧的充能球X+1次。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | X | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | X | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Evoke your next Orb X times. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Evoke your next Orb X times. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Evoke your next Orb X+1 times. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Evoke your next Orb X+1 times. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/MultiCast.class", "class_sha256": "0cfcbfbe34eb73162aef9b1bd3c4ae736b7fc9cb9ad7546c80de9c94872b69b8", "constructor_offsets": {}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/MultiCast.class", "class_sha256": "0cfcbfbe34eb73162aef9b1bd3c4ae736b7fc9cb9ad7546c80de9c94872b69b8", "constructor_offsets": {}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Rare | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Evoke"] | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | NONE | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Evoke your next Orb X times. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 激发 你最右侧的充能球X次。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Multi-Cast | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 多重释放 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Multi-Cast", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 多重释放<br>（图片未提供文字说明）<br>激发你最右侧的充能球x次。<br>多重释放+<br>（图片未提供文字说明）<br>激发你最右侧的充能球x+1次。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [多重释放](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495548&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Multi-Cast.png/150px-Blue-Multi-Cast.png?386ff2", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-Multi-CastPlus.png/150px-Blue-Multi-CastPlus.png?1f7c10"} | `single_source` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/6268490088b198b9d3b92312951a88b2.png", "https://cdn.max-c.com/heybox/dailynews/img/bd153c7f0016548e4ef1fe9d074856f6.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/d60e8ce8690c57646d3fc050173220dd.png"] | `single_source` | [多重释放](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495548&wiki_id=646570) |
| `source.infobox.description` | Evoke your next Orb (X;X+1) times. | `single_source` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 多重释放 | `single_source` | [多重释放](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495548&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>|Name        = Multi-Cast<br>|Image       = Blue-Multi-Cast.png<br>|Color       = Blue<br>|Type        = Skill<br>|Rarity      = Rare<br>|Cost        = -1<br>|Description = {{KW|Evoke}} your next Orb (X;X+1) times.<br>}}<br>{{C|Multi-Cast}} is an X {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Rare|Rare}} {{QueryLink|Cards|type:Skill|Skill}} Card.<br><br>== Interactions ==<br>=== Order ===<br>* If {{KW|Plasma|Pla... | `single_source` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
