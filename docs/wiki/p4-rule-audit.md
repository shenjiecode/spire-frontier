# P4 机制与规则核验审计

生成时间：2026-09-18T11:10:23+00:00。状态：`audit_pending_review`。

此页只报告字段覆盖和待核验项，不把缺失数据补成 0，也不把候选身份当作双语事实。纯合页父记录只保留来源和成员关系，怪物数值按成员页统计。

## 字段覆盖

| 类别 | 条目数 | 必备字段齐全 |
| --- | ---: | ---: |
| `card` | 422 | 370 |
| `relic` | 180 | 180 |
| `potion` | 42 | 42 |
| `monster` | 64 | 62 |
| `event` | 55 | 51 |
| `status` | 181 | 181 |
| `keyword` | 55 | 55 |
| `mechanic` | 25 | 25 |

## 待处理数量

| 项目 | 数量 |
| --- | ---: |
| `possible_energy_icon_loss` | 0 |
| `raw_placeholder_claims` | 1981 |
| `unknown_image_licence_assets` | 21 |
| `candidate_entities` | 173 |
| `confirmed_inventory_mappings` | 830 |
| `candidate_inventory_mappings` | 0 |
| `strategy_notes` | 0 |
| `strategy_links` | 0 |

## 未完成字段清单

### inventory_not_parsed（0）
无。
### cards_without_base_variant（52）
- `Allocate` (`candidate`)
- `sts1.game.candidate.card.awakenedstrike` (`candidate`)
- `Axe Kick` (`candidate`)
- `sts1.game.candidate.card.bigbrain` (`candidate`)
- `Blaster` (`candidate`)
- `sts1.game.candidate.card.blessed` (`candidate`)
- `sts1.game.candidate.card.brillianceaura` (`candidate`)
- `Calm` (`candidate`)
- `Causality` (`candidate`)
- `Clarity` (`candidate`)
- `Cleanse Evil` (`candidate`)
- `sts1.game.candidate.card.crescentkick` (`candidate`)
- `sts1.game.candidate.card.discipline` (`candidate`)
- `Energy Pulse` (`candidate`)
- `sts1.game.candidate.card.experienced` (`candidate`)
- `sts1.game.candidate.card.flamemastery` (`candidate`)
- `sts1.game.candidate.card.flare` (`candidate`)
- `sts1.game.candidate.card.flick` (`candidate`)
- `sts1.game.candidate.card.flicker` (`candidate`)
- `sts1.game.candidate.card.flow` (`candidate`)
- `sts1.game.candidate.card.flowstate` (`candidate`)
- `Flux Capacitor` (`candidate`)
- `sts1.game.candidate.card.furyaura` (`candidate`)
- `Hide` (`candidate`)
- `sts1.game.candidate.card.letfatedecide` (`candidate`)
- `Mastery` (`candidate`)
- `sts1.game.candidate.card.metaphysics` (`candidate`)
- `sts1.game.candidate.card.palmthatrestrains` (`candidate`)
- `Peace` (`candidate`)
- `sts1.game.candidate.card.perfectedform` (`candidate`)
- `sts1.game.candidate.card.polymath` (`candidate`)
- `sts1.game.candidate.card.prediction` (`candidate`)
- `sts1.game.candidate.card.punishment` (`candidate`)
- `sts1.game.candidate.card.retreatinghand` (`candidate`)
- `sts1.game.candidate.card.retribution` (`candidate`)
- `sts1.game.candidate.card.serenity` (`candidate`)
- `sts1.game.candidate.card.shield` (`candidate`)
- `sts1.game.candidate.card.soothingaura` (`candidate`)
- `sts1.game.candidate.card.stepandstrike` (`candidate`)
- `sts1.game.candidate.card.sublimeslice` (`candidate`)
- `sts1.game.candidate.card.survey` (`candidate`)
- `sts1.game.candidate.card.swipe` (`candidate`)
- `sts1.game.candidate.card.thwack` (`candidate`)
- `sts1.game.candidate.card.torrent` (`candidate`)
- `Transcendence` (`candidate`)
- `Truth` (`candidate`)
- `Unraveling` (`candidate`)
- `sts1.game.candidate.card.wardaura` (`candidate`)
- `sts1.game.candidate.card.waveofthehand2` (`candidate`)
- `sts1.game.candidate.card.windup` (`candidate`)
- `Wisdom` (`candidate`)
- `Wrath` (`candidate`)
### monsters_without_moves（2）
- `sts1.candidate.zh.monster.15436697` (`deprecated`)
- `sts1.candidate.zh.monster.15436699` (`deprecated`)
### events_without_options（4）
- `sts1.candidate.zh.event.15408927` (`candidate`)
- `Proceed Screen` (`candidate`)
- `Spire Heart` (`candidate`)
- `Thinking with Puddles` (`candidate`)

## 数值与提取检查

- 升级后固定 0 费变体：95 条。
- X 费变体：20 条。
- 可能的能量图标文本损失和原始图片占位词仍保留在报告中，需对照源图复核。

详细 JSON：[p4-rule-audit.json](../../reports/p4-rule-audit.json)
