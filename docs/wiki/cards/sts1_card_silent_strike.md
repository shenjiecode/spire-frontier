# 打击 / Strike

> 稳定 ID：`sts1.card.silent.strike`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：打击
- English: Strike

## 卡牌属性

- 颜色：`Green`
- 类型：`Attack`
- 稀有度：`Basic`
- 可获得性：`card_list`
- 标签：`[]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `1.0` | Deal 6 damage. | 造成6点伤害。 | 未保存 |
| `Upgraded` | `1.0` | Deal 9 damage. | 造成9点伤害。 | 未保存 |

## 相关条目

- `belongs_to_character` → [静默猎手 / Silent](../characters/sts1_character_silent.md) 

## 被哪些条目引用

- `starting_deck_contains` → [静默猎手 / Silent](../characters/sts1_character_silent.md) ；条件：`{"quantity": 5}`

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Green | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 1 | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 1 | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 6 damage. | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Deal 6 damage. | `provisional` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=476143&wiki_id=646570) |
| `card.description (upgrade)` | Deal 9 damage. | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (upgrade)` | Deal 9 damage. | `provisional` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=476143&wiki_id=646570) |
| `card.rarity` | Basic | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | [] | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.type` | Attack | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Deal !D! damage. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 造成 !D! 点伤害。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Strike | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 打击 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Strike_G", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 打击​<br>（图片未提供文字说明）<br>造成6点伤害。<br>打击+<br>（图片未提供文字说明）<br>造成9点伤害。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=476143&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Green-Strike.png/150px-Green-Strike.png?92d9e9", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Green-StrikePlus.png/150px-Green-StrikePlus.png?800bd3"} | `single_source` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://cdn.max-c.com/heybox/dailynews/img/51d6e54eed6e3a62ccff07a3593a93eb.jpg", "https://cdn.max-c.com/heybox/dailynews/img/6c06dec3dd232e963f26a36a9223118f.jpg", "https://imgheybox.max-c.com/web/bbs/2024/08/22/88a6e7fb5edd783e1eb84d1b269ac648.png"] | `single_source` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=476143&wiki_id=646570) |
| `source.infobox.description` | Deal (6;9) damage. | `single_source` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 打击 | `single_source` | [打击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=476143&wiki_id=646570) |
| `source.wikitext` | {{Sequel Disambiguation}} <br>{{Card Infobox<br>|Name        = Strike (Silent)<br>|DisplayName = Strike<br>|Image       = Green-Strike.png<br>|Color       = Green<br>|Type        = Attack<br>|Rarity      = Basic<br>|Cost        = 1<br>|Description = Deal (6;9) damage.<br>}}<br>{{C|Strike (Silent)|Strike}} is a 1 {{Icon|GE}} cost {{QueryLink|Cards|color:Green|Silent}} {{QueryLink|Cards|rarity:Basic|Basic}} {{QueryLink|Cards|type:Attack|Attack}} Card. It deals 6 (9 if upgraded) damage.<br><br>T... | `single_source` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T04:35:44+00:00
