# 玩家回合 / Player Turn

> 稳定 ID：`sts1.mechanic.player_turn`  
> 类别：`mechanic`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：玩家回合
- English: Player Turn

## mechanic 数据

| 字段 | 值 |
| --- | --- |
| `definition_json` | {"definition": null, "definition_en": "At the start of the player's turn, three things happen: # Energy is set to the base energy (default 3), and # A number of cards are drawn (default 5), and # Start-of-turn effects trigger. The default behavior can be changed, typically by Relics] (e.g. Fusion Hammer increases the base energy by 1; Snecko Eye increases the number of cards drawn per turn by 2). During their turn, the player may play cards or drink Potions]. Cards with an energy cost will subtract that energy from the total. All player actions are resolved immediately upon being performed. When the player presses End Turn, two things happen: # End-of-turn effects trigger. #* This generally resolves in the order relics -> buffs -> cards (e.g. Orichalcum will trigger before Plated Armor,... |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `mechanic.definition` | {"definition_en": "At the start of the player's turn, three things happen: # Energy is set to the base energy (default 3), and # A number of cards are drawn (default 5), and # Start-of-turn effects trigger. The default behavior can be changed, typically by Relics] (e.g. Fusion Hammer increases the base energy by 1; Snecko Eye increases the number of cards drawn per turn by 2). During their turn, the player may play cards or drink Potions]. Cards with an energy cost will subtract that energy f... | `single_source` | [P3 wiki.gg API batch: mechanic 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics&prop=revisions&rvprop=content|ids&rvslots=main) |
| `mechanic.definition.zh` | 回合开始时能量恢复到基础值（默认 3），抽牌（默认 5 张）并结算回合开始效果；玩家可打牌或使用药水，结束回合后结算结束效果并把手牌弃掉，再轮到敌方。 | `single_source/editorial_zh` | [P3 wiki.gg API batch: mechanic 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics&prop=revisions&rvprop=content|ids&rvslots=main) |
| `source.wikitext` | {{Sequel Disambiguation}}<br>{{Ambox<br>| title = WARNING!<br>| color = red<br>| icon = GremlinNob.png<br>| message = ''This page is under construction. Information may be wrong or incomplete.''<br>}}<br><br>== Resources ==<br><br>=== Health ===<br><blockquote> '''''Hit Points (HP):''' If you run out of HP, you die.''</blockquote><br><br>The most fundamental resource. HP can take any value from 0 to the player's maximum HP. HP is depleted by taking damage, and may be replenished at [[Map Loca... | `single_source` | [P3 wiki.gg API batch: mechanic 1](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics|Mechanics&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
