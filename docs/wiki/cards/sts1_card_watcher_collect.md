# 收集 / Collect

> 稳定 ID：`sts1.card.watcher.collect`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：收集
- English: Collect

## 卡牌属性

- 颜色：`Purple`
- 类型：`Skill`
- 稀有度：`Uncommon`
- 可获得性：`card_list`
- 标签：`["Exhaust", "Hand"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `X` | Put a Miracle+ into your hand at the start of your next X turns. Exhaust. | 在你的下X个回合开始时，增加一张奇迹+ 到你的手牌。消耗。 | 未保存 |
| `Upgraded` | `X` | Put a Miracle+ into your hand at the start of your next X+1 turns. Exhaust. | 在你的下X+1个回合开始时，增加一张奇迹+ 到你的手牌。消耗。 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | X | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | X | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Put a Miracle+ into your hand at the start of your next X turns. Exhaust | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (base)` | Put a Miracle+ into your hand at the start of your next X turns. Exhaust | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Put a Miracle+ into your hand at the start of your next X+1 turns. Exhaust | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.description (upgrade)` | Put a Miracle+ into your hand at the start of your next X+1 turns. Exhaust | `provisional` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Collect.class", "class_sha256": "75d3983ed3c6d868ce8131054e2048a2f421a8881311df07bf32ea69507ce179", "constructor_offsets": {}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Collect.class", "class_sha256": "75d3983ed3c6d868ce8131054e2048a2f421a8881311df07bf32ea69507ce179", "constructor_offsets": {}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Uncommon | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Exhaust", "Hand"] | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Put a *Miracle+ into your hand at the start of your next X turns. NL Exhaust. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 在你的下X个回合开始时，增加一张 *奇迹+ 到你的手牌。 NL 消耗 。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Collect | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 收集 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Collect", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 在你的下X个回合开始时，增加一张奇迹+到你的手牌。消耗<br>在你的下X+1个回合开始时，增加一张奇迹+到你的手牌。消耗。<br>测试画风<br>（图片未提供文字说明） | `single_source` | [收集](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667096&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-Collect.png/150px-Purple-Collect.png?66ab93", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-CollectPlus.png/150px-Purple-CollectPlus.png?562abf"} | `single_source` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/3fb47661eabad459b5e337fccd1bdf42.png"] | `single_source` | [收集](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667096&wiki_id=646570) |
| `source.infobox.description` | Put a Miracle+ into your hand at the start of your next (X;X+1) turns. Exhaust | `single_source` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 收集 | `single_source` | [收集](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9667096&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Collect<br>|Image       = Purple-Collect.png<br>|Color       = Purple<br>|Type        = Skill<br>|Rarity      = Uncommon<br>|Cost        = -1<br>|Description = Put a {{C|Miracle|Miracle+}} into your hand at the start of your next (X;X+1) turns. {{KW|Exhaust}}<br>|GivesToPlayer = Exhaust<br>}}<br>{{Power Infobox|Collect}} {{Small Card Infobox|Miracle}}<br>{{C|Collect}} is an X {{Icon|PE}} cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Un... | `single_source` | [P3 wiki.gg API batch: card 5](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=True_Grit|Signature_Move|Shrug_It_Off|Blood_for_Blood|Empty_Mind|Machine_Learning|All-Out_Attack|Thunder_Strike|Second_Wind|Strike_(Silent)|Grand_Finale|Collect|Immolate|Omega|Regret|Feed|Safety|Glacier|Deadly_Poison|Burning_Pact&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
