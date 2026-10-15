# 停顿 / Halt

> 稳定 ID：`sts1.card.watcher.halt`  
> 类别：`card`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：停顿
- English: Halt

## 卡牌属性

- 颜色：`Purple`
- 类型：`Skill`
- 稀有度：`Common`
- 可获得性：`card_list`
- 标签：`["Block", "Wrath"]`

## 变体

| 变体 | 费用 | 英文效果 | 中文效果 | 图片 |
| --- | --- | --- | --- | --- |
| `Base` | `0.0` | Gain 3 Block. If you are in Wrath, gain 9 additional Block. | 获得3点格挡。愤怒：获得额外9点格挡 | 未保存 |
| `Upgraded` | `0.0` | Gain 4 Block. If you are in Wrath, gain 14 additional Block. | 获得4点格挡。愤怒：获得额外14点格挡 | 未保存 |

## 相关条目

- `belongs_to_character` → [观者 / Watcher](../characters/sts1_character_watcher.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `card.color` | Purple | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (base)` | 0 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.cost (upgrade)` | 0 | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 3 Block. If you are in Wrath, gain 9 additional Block. | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (base)` | Gain 3 Block. If you are in Wrath, gain 9 additional Block. | `provisional` | [停顿](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9666208&wiki_id=646570) |
| `card.description (upgrade)` | Gain 4 Block. If you are in Wrath, gain 14 additional Block. | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.description (upgrade)` | Gain 4 Block. If you are in Wrath, gain 14 additional Block. | `provisional` | [停顿](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9666208&wiki_id=646570) |
| `card.game_values (base)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Halt.class", "class_sha256": "4234cd5c3de8e808a279ea78140a16ee33073907ca27f2f38469283748e5353f", "constructor_offsets": {}, "dynamic_upgrade_fields": [], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.game_values (upgrade)` | {"class_name": "com/megacrit/cardcrawl/cards/purple/Halt.class", "class_sha256": "4234cd5c3de8e808a279ea78140a16ee33073907ca27f2f38469283748e5353f", "constructor_offsets": {}, "dynamic_upgrade_fields": ["block"], "scope": "unmodified static base values; conditions/multipliers are in descriptions", "source_page_id": "game.review.classes.22313d2c8d8b3741", "values": {}} | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.rarity` | Common | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.tags` | ["Block", "Wrath"] | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `card.target` | SELF | `verified_game` | [Installed game constructor/upgrade bytecode](game-local://cfad868ac8d65a88/review-class-evidence/22313d2c8d8b37414e828a97697d2be7b85232aa05e079275b1f83f08f4ab8a0) |
| `card.type` | Skill | `provisional` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.card.description` | Gain !B! Block. NL If you are in Wrath, gain !M! additional Block. | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.card.description` | 获得 !B! 点 格挡 。 NL 愤怒 ：获得 !M! 点额外格挡。 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization.name` | Halt | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `game.localization.name` | 停顿 | `verified_game` | [Game localization zhs/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/cards.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Halt", "kind": "card", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/cards.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/cards.json) |
| `source.article_text` | 获得3点格挡。愤怒：获得额外9点格挡<br>获得4点格挡。愤怒：获得额外14点格挡<br>测试画风 | `single_source` | [停顿](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9666208&wiki_id=646570) |
| `source.image_urls` | {"base": "https://slaythespire.wiki.gg/images/thumb/Purple-Halt.png/150px-Purple-Halt.png?d5ffd0", "upgrade": "https://slaythespire.wiki.gg/images/thumb/Purple-HaltPlus.png/150px-Purple-HaltPlus.png?ff6c7c"} | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/24/0c8d0d4b9416d5a7d60646e9348d8a45.png"] | `single_source` | [停顿](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9666208&wiki_id=646570) |
| `source.infobox.description` | Gain (3;4) Block. If you are in Wrath, gain (9;14) additional Block. | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 停顿 | `single_source` | [停顿](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9666208&wiki_id=646570) |
| `source.wikitext` | {{Card Infobox<br>|Name        = Halt<br>|Image       = Purple-Halt.png<br>|Color       = Purple<br>|Type        = Skill<br>|Rarity      = Common<br>|Cost        = 0<br>|Description = Gain (3;4) {{KW|Block}}. <br>If you are in {{KW|Wrath}}, gain (9;14) additional {{KW|Block}}.<br>}}<br>{{Keyword Infobox|Block}} {{Keyword Infobox|Wrath}}<br>{{C|Halt}} is a 0 {{Icon|PE}}-cost {{QueryLink|Cards|color:Purple|Watcher}} {{QueryLink|Cards|rarity:Common|Common}} {{QueryLink|Cards|type:Skill|Skill}} C... | `single_source` | [P3 wiki.gg API batch: card 13](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Storm|Sash_Whip|Flechettes|Fame_and_Fortune|Fasting|Inflame|Halt|Insight|Zap|Ragnarok|Clothesline|Twin_Strike|Burst|Combust|Scrawl|Loop|Miracle|Beam_Cell|Foreign_Influence|FTL&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
