# 弹回 / Rebound

> 稳定 ID：`sts1.card.defect.rebound`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：弹回
- English: Rebound

## 卡牌属性

- 颜色：`Blue`
- 类型：`Attack`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`[]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 9 damage. Put the next card you play this turn on top of your draw pile. | 造成9点伤害。你在这个回合打出的下一张牌将会被放置到抽牌堆的顶部。 （只限会移入弃牌堆的牌） | 未保存 |
| `Upgraded` | `1.0` | Deal 12 damage. Put the next card you play this turn on top of your draw pile. | 造成12点伤害。你在这个回合打出的下一张牌将会被放置到抽牌堆的顶部。 （只限会移入弃牌堆的牌） | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 9 damage.Put the next card you play this turn on top of your draw pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Deal 9 damage.Put the next card you play this turn on top of your draw pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 12 damage.Put the next card you play this turn on top of your draw pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Deal 12 damage.Put the next card you play this turn on top of your draw pile. | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Rebound.class", "class_sha256": "c100919636e68888bb704a3382a2d5437d2812d1ca9fa41fe0fd767108962a43", "constructor_offsets": {"damage": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 9}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/blue/Rebound.class", "class_sha256": "c100919636e68888bb704a3382a2d5437d2812d1ca9fa41fe0fd767108962a43", "constructor_offsets": {"damage": 36}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {"damage": 12}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | [] | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | ENEMY | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. NL Put the next card you play this turn on top of your draw pile. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 NL 你在这个回合打出的下一张牌将会被放置到抽牌堆的顶部。 （只限会移入弃牌堆的牌） | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Rebound | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 弹回 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Rebound", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 弹回<br>（图片未提供文字说明）<br>造成9点伤害。你在这个回合打出的下一张牌将会被放置到抽牌堆的顶部。<br>弹回+<br>（图片未提供文字说明）<br>造成12点伤害。你在这个回合打出的下一张牌将会被放置到抽牌堆的顶部。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [弹回](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495550&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Rebound.png/150px-Blue-Rebound.png?1faa9c", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-ReboundPlus.png/150px-Blue-ReboundPlus.png?2729c7"} | `single_source` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/115de4c78ae7fb325fd41ec9059be9a2.png", "https://cdn.max-c.com/heybox/dailynews/img/77a39c8031397c26a68fb32ab999e0f3.png", "https://imgheybox.max-c.com/web/bbs/2024/08/24/4b0dac94068df3bec8eaca4a34559011.png"] | `single_source` | [弹回](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495550&wiki_id=646570) |
| `source.infobox.description` | Deal (9;12) damage. Put the next card you play this turn on top of your draw pile. | `single_source` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 弹回 | `single_source` | [弹回](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=495550&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Card Infobox<br>|Name        = Rebound<br>|Image       = Blue-Rebound.png<br>|Color       = Blue<br>|Type        = Attack<br>|Rarity      = Common<br>|Cost        = 1<br>|Description = Deal (9;12) damage.<br>Put the next card you play this turn on top of your draw pile.<br>}}<br>{{Power Infobox|Rebound}}<br>{{C|Rebound}} is a 1 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|type:Attack|Attack}} C... | `single_source` | [P3 wiki.gg API batch: card 16](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Curse_of_the_Bell|Rebound|Rainbow|Fear_No_Evil|Foresight|Mind_Blast|Doom_and_Gloom|Clash|Apparition|Recursion|Heatsinks|Finisher|Flying_Sleeves|Tantrum|Slice|Phantasmal_Killer|Sands_of_Time|Clumsy|Bane|Brilliance&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:06+00:00
