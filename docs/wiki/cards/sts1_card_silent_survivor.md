# 生存者 / Survivor

> 稳定 ID：`sts1.card.silent.survivor`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：生存者
- English: Survivor

## 卡牌属性

- 颜色：`Green`
- 类型：`Skill`
- 稀有度：`Basic`
- 可获得性：`card_list`
- 标签：`["Block", "Discard"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Gain 8 Block.Discard 1 card. | 获得8点格挡。丢弃一张牌。 | 未保存 |
| `Upgraded` | `1.0` | Gain 11 Block.Discard 1 card. | 获得11点格挡。丢弃一张牌。 | 未保存 |

## 相关条目

- `belongs_to_character` → [静默猎手 / Silent](../characters/sts1_character_silent.md) 

## 被哪些条目引用

- `starting_deck_contains` → [静默猎手 / Silent](../characters/sts1_character_silent.md) ；条件：`{"quantity": 1}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Green | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 8 Block.Discard 1 card. | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 8 Block.Discard 1 card. | `provisional` | [生存者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494154&wiki_id=646570) |
| `card.description (upgrade)` | Gain 11 Block.Discard 1 card. | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (upgrade)` | Gain 11 Block.Discard 1 card. | `provisional` | [生存者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494154&wiki_id=646570) |
| `card.rarity` | Basic | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block", "Discard"] | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain !B! Block. NL Discard 1 card. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得 !B! 点 格挡 。 NL 丢弃一张牌。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Survivor | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 生存者 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Survivor", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 生存者<br>（图片未提供文字说明）<br>获得8点格挡。丢弃一张牌。<br>生存者+<br>（图片未提供文字说明）<br>获得11点格挡。丢弃一张牌。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [生存者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494154&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Green-Survivor.png/150px-Green-Survivor.png?d2b86a", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Green-SurvivorPlus.png/150px-Green-SurvivorPlus.png?226e61"} | `single_source` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/1ce3788036dd8bb8a0ffd25c65de0674.jpg", "https://cdn.max-c.com/heybox/dailynews/img/d3df72c225a61098f78bd04b44e9524d.jpg", "https://imgheybox.max-c.com/web/bbs/2024/08/22/099fe622f8dc4f7e7a34abb9cedda9c8.png"] | `single_source` | [生存者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494154&wiki_id=646570) |
| `source.infobox.description` | Gain (8;11) Block. Discard 1 card. | `single_source` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 生存者 | `single_source` | [生存者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=494154&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}} <br>{{Card Infobox<br>| Name        = Survivor<br>| Image       = Green-Survivor.png<br>| Color       = Green<br>| Type        = Skill<br>| Rarity      = Basic<br>| Cost        = 1<br>| Description = Gain (8;11) {{KW|Block}}.<br>Discard 1 card.<br>| GivesToPlayer = Block, Discard<br>}}<br>{{Keyword Infobox|Block}}<br>{{C|Survivor}} is a 1 {{Icon|GE}}-cost {{QueryLink|Cards|color:Green|Silent}} {{QueryLink|Cards|rarity:Basic|Basic}} {{QueryLink|Cards|type:Skill|Skill}... | `single_source` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
