# 牌堆 / Card Piles

> 稳定 ID：`sts1.mechanic.card_piles`  
> 类别：`mechanic`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：牌堆
- English: Card Piles

## mechanic 数据

| 字段 | 值 |
| --- | --- |
| `definition_json` | {"definition": null, "definition_en": "There are three piles in which cards may reside when not in the player's hand. * Draw Pile: The pile from which cards are drawn at the start of the turn. The draw pile is populated at the start of combat with all the cards from the player's deck. Attempting to draw a card when the draw pile is empty triggers a shuffle (see below). * Discard Pile: The pile to which most cards are sent after playing. When a shuffle is triggered, all cards from the discard pile are shuffled into the draw pile. Certain cards do not enter the discard pile after being played: Exhaust] cards instead enter the exhaust pile, while Powers cards disappear entirely. * Exhaust Pile: The pile in which cards that have been Exhausted] reside. There is no way to recover cards from ... |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `mechanic.definition` | {"definition_en": "There are three piles in which cards may reside when not in the player's hand. * Draw Pile: The pile from which cards are drawn at the start of the turn. The draw pile is populated at the start of combat with all the cards from the player's deck. Attempting to draw a card when the draw pile is empty triggers a shuffle (see below). * Discard Pile: The pile to which most cards are sent after playing. When a shuffle is triggered, all cards from the discard pile are shuffled in... | `single_source` | [P3 wiki.gg API batch: mechanic 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics&prop=revisions&rvprop=content|ids&rvslots=main) |
| `mechanic.definition.zh` | 牌不在手牌中时位于抽牌堆、弃牌堆或消耗牌堆。抽牌堆抽空会把弃牌堆洗回；消耗的牌在本场战斗结束前不能正常取回。 | `single_source/editorial_zh` | [P3 wiki.gg API batch: mechanic 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Ambox<br>| title = WARNING!<br>| color = red<br>| icon = GremlinNob.png<br>| message = ''This page is under construction. Information may be wrong or incomplete.''<br>}}<br><br>== Resources ==<br><br>=== Health ===<br><blockquote> '''''Hit Points (HP):''' If you run out of HP, you die.''</blockquote><br><br>The most fundamental resource. HP can take any value from 0 to the player's maximum HP. HP is depleted by taking damage, and may be replenished at [[Map Loca... | `single_source` | [P3 wiki.gg API batch: mechanic 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
