# 三机械 / Shapes

> 稳定 ID：`sts1.monster.shapes`  
> 类别：`monster`；游戏：`sts1`；映射状态：`provisional`

## 名称

- 中文：三机械
- English: Shapes

## monster 合页上下文

本页对应来源中的组合页，只保留来源正文和 `has_member` 关系。生命值与行动请查看下方成员页面；不会把某个成员的数值投影到父页。

| 字段 | 值 |
| --- | --- |
| `encounter_notes` | Grouped wiki page only; structured HP/actions live on its has_member child entities. |

## 相关条目

- `has_member` → [爆炸机 / Exploder](sts1_monster_exploder.md)
- `has_member` → [反冲机 / Repulsor](sts1_monster_repulsor.md)
- `has_member` → [钉刺机 / Spiker](sts1_monster_spiker.md)

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `game.localization.name` | Exploder | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.localization.name` | 反冲机 | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Spiker", "kind": "monster", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.dialog` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization eng/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/monsters.json) |
| `game.monster.moves` | [""] | `verified_game` | [Game localization zhs/monsters.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/monsters.json) |
| `monster.hp.range` | {"ascension_max": 35, "ascension_min": 30, "ascension_raw": "30-35", "base_max": 30, "base_min": 30, "base_raw": "30"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Attack` | {"effect": "Deals (9;11) damage.", "intent": "Attack2"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Buff Thorns` | {"effect": "Gains 2 Thorns.", "intent": "Buff"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Daze` | {"effect": "Adds 2 Dazed into your draw pile.", "intent": "Debuff"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `monster.move.Explode` | {"effect": "Deals 30 damage. Dies.", "intent": "Unknown"} | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.article_text` | （图片未提供文字说明）<br>钉刺机<br>（图片未提供文字说明）<br>它初始携带3点<br>荆棘<br>，在进阶2以上改为4点，在进阶17以上改为7点。<br>行动模式<br>名称<br>效果<br>进阶2+<br>概率<br>备注<br>切割<br>造成7点伤害<br>造成9点伤害<br>50%<br>不会连续使用两次<br>荆棘<br>获得2点<br>荆棘<br>获得2点<br>荆棘<br>50%<br>在一场战斗中不会使用超过6次<br>应对方法<br>最好能在荆棘点数较低时，用单次伤害较高的牌将其秒杀，如<br>重锤<br>，<br>重刃<br>，<br>华丽收场<br>。<br>由于<br>荆棘<br>是按照受到攻击的次数进行反伤，不推荐使用多段伤害的卡牌，如<br>连续拳<br>，<br>恶魔之焰<br>，<br>雷霆打击<br>。<br>非攻击伤害（如战士的<br>火焰屏障<br>、猎人的<br>中毒<br>和机器人的闪电充能球）不会受到反弹伤害。<br>爆炸机<br>（图片未提供文字说明）<br>行动模式<br>名称<br>效果<br>进阶2+<br>备注<b... | `single_source` | [三机械](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408985&wiki_id=646570) |
| `source.image_urls` | ["https://imgheybox.max-c.com/web/bbs/2024/08/15/a6c58faeb06160c8e7da87f14186e6a9.png", "https://imgheybox.max-c.com/web/bbs/2024/08/15/e3c5ca3773d91a976ffbdaf58e8c70f1.png", "https://imgheybox.max-c.com/web/bbs/2024/08/15/e7a6d336aa36e0f25a5b8c56c8130322.png"] | `single_source` | [三机械](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408985&wiki_id=646570) |
| `source.infobox.description` | 30 | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.title_text` | 三机械 | `single_source` | [三机械](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408985&wiki_id=646570) |
| `source.wikitext` | The Shapes are a group of enemies encountered in [[Act 3]].<br><br>== Exploder ==<br>{{Enemy Infobox<br>|Name   = Exploder<br>|Image  = Exploder.png<br>|HP     = 30<br>|AscHP  = 30-35<br>|Powers = {{BD|Explosive}} 3<br>|Debut  = Act 3<br>|Type   = Normal<br>}}<br>{{Power Infobox|Explosive}}<br>Exploders explode. Profound knowledge.<br><br>=== Pattern ===<br>{{Intents Table/start|Exploder}}<br>{{Intents Table/row<br>|Name   = Attack<br>|Intent = Attack2<br>|Effect = Deals (9;{{Asc|2|11}}) dama... | `single_source` | [P3 wiki.gg API batch: monster 3](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=The_Maw|Fungi_Beast|Orb_Walker|Shapes|The_Champ&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:09+00:00
