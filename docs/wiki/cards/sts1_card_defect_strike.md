# 打击 / Strike

> 稳定 ID：`sts1.card.defect.strike`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：打击
- English: Strike

## 卡牌属性

- 颜色：`Blue`
- 类型：`Attack`
- 稀有度：`Basic`
- 可获得性：`card_list`
- 标签：`[]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 6 damage. | ​ 造成6伤害。 | 未保存 |
| `Upgraded` | `1.0` | Deal 9 damage. | ​​​​造成9点伤害。 | 未保存 |

## 相关条目

- `belongs_to_character` → [故障机器人 / Defect](../characters/sts1_character_defect.md)

## 被哪些条目引用

- `starting_deck_contains` → [故障机器人 / Defect](../characters/sts1_character_defect.md) ；条件：`{"quantity": 4}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Blue | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 6 damage. | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 6 damage. | `provisional` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=412596&wiki_id=646570) |
| `card.description (upgrade)` | Deal 9 damage. | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (upgrade)` | Deal 9 damage. | `provisional` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=412596&wiki_id=646570) |
| `card.rarity` | Basic | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | [] | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Strike | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 打击 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Strike_B", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 打击<br>​（图片未提供文字说明）<br>造成6伤害。<br>打击+<br>（图片未提供文字说明）<br>​​​​造成9点伤害。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=412596&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Blue-Strike.png/150px-Blue-Strike.png?56b660", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Blue-StrikePlus.png/150px-Blue-StrikePlus.png?4c5abe"} | `single_source` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/23/7c082b20a7695577b063377866952fa4.png"] | `single_source` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=412596&wiki_id=646570) |
| `source.infobox.description` | Deal (6;9) damage. | `single_source` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 打击 | `single_source` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=412596&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation|1|1}} <br>{{Card Infobox<br>|Name        = Strike (Defect)<br>|DisplayName = Strike<br>|Image       = Blue-Strike.png<br>|Color       = Blue<br>|Type        = Attack<br>|Rarity      = Basic<br>|Cost        = 1<br>|Description = Deal (6;9) damage.<br>}}<br>{{C|Strike (Defect)|Strike}} is a 1 {{Icon|BE}}-cost {{QueryLink|Cards|color:Blue|Defect}} {{QueryLink|Cards|rarity:Basic|Basic}} {{QueryLink|Cards|type:Attack|Attack}} Card. It deals 6 (9 if upgraded) damage.<br><br>... | `single_source` | [P3 wiki.gg API batch: card 19](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Strike_(Defect)|Normality|Survivor|Vault|Just_Lucky|Battle_Hymn|Terror|Multi-Cast|Live_Forever|Sucker_Punch&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:20+00:00
