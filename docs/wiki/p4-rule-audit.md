# P4 机制与规则核验审计

生成时间：2026-09-18T04:35:57+00:00。状态：`audit_pending_review`。

此页只报告字段覆盖和待核验项，不把缺失数据补成 0，也不把候选身份当作双语事实。

## 字段覆盖

| 类别 | 条目数 | 必备字段齐全 |
| --- | ---: | ---: |
| `card` | 422 | 370 |
| `relic` | 180 | 178 |
| `potion` | 42 | 42 |
| `monster` | 61 | 44 |
| `event` | 55 | 51 |
| `status` | 182 | 182 |
| `keyword` | 55 | 22 |
| `mechanic` | 25 | 25 |

## 待处理数量

| 项目 | 数量 |
| --- | ---: |
| `possible_energy_icon_loss` | 0 |
| `raw_placeholder_claims` | 1979 |
| `unknown_image_licence_assets` | 21 |
| `candidate_entities` | 186 |
| `confirmed_inventory_mappings` | 816 |
| `candidate_inventory_mappings` | 0 |
| `strategy_notes` | 0 |
| `strategy_links` | 0 |

## 未完成字段清单

### inventory_not_parsed（0）
无。
### cards_without_base_variant（52）
- `Allocate` (`candidate`)
- `DEPRECATED Awakened Strike` (`candidate`)
- `Axe Kick` (`candidate`)
- `DEPRECATED Big Brain` (`candidate`)
- `Blaster` (`candidate`)
- `DEPRECATED Blessed` (`candidate`)
- `DEPRECATED Brilliance Aura` (`candidate`)
- `Calm` (`candidate`)
- `Causality` (`candidate`)
- `Clarity` (`candidate`)
- `Cleanse Evil` (`candidate`)
- `DEPRECATED Crescent Kick` (`candidate`)
- `DEPRECATED Discipline` (`candidate`)
- `Energy Pulse` (`candidate`)
- `DEPRECATED Experienced` (`candidate`)
- `DEPRECATED Flame Mastery` (`candidate`)
- `DEPRECATED Flare` (`candidate`)
- `DEPRECATED Flick` (`candidate`)
- `DEPRECATED Flicker` (`candidate`)
- `DEPRECATED Flow` (`candidate`)
- `DEPRECATED Flow State` (`candidate`)
- `Flux Capacitor` (`candidate`)
- `DEPRECATED Fury Aura` (`candidate`)
- `Hide` (`candidate`)
- `DEPRECATED Let Fate Decide` (`candidate`)
- `Mastery` (`candidate`)
- `DEPRECATED` (`candidate`)
- `DEPRECATED Restraining Palm` (`candidate`)
- `Peace` (`candidate`)
- `DEPRECATED Perfected Form` (`candidate`)
- `DEPRECATED Polymath` (`candidate`)
- `DEPRECATED Prediction` (`candidate`)
- `DEPRECATED Punishment` (`candidate`)
- `DEPRECATED Retreating Hand` (`candidate`)
- `DEPRECATED Retribution` (`candidate`)
- `DEPRECATED Serenity` (`candidate`)
- `DEPRECATED Shield` (`candidate`)
- `DEPRECATED Soothing Aura` (`candidate`)
- `DEPRECATED Step and Strike` (`candidate`)
- `DEPRECATED Sublime Slice` (`candidate`)
- `DEPRECATED Survey` (`candidate`)
- `DEPRECATED Swipe` (`candidate`)
- `DEPRECATED Thwack` (`candidate`)
- `DEPRECATED Torrent` (`candidate`)
- `Transcendence` (`candidate`)
- `Truth` (`candidate`)
- `Unraveling` (`candidate`)
- `DEPRECATED Ward Aura` (`candidate`)
- `DEPRECATED` (`candidate`)
- `DEPRECATED Windup` (`candidate`)
- `Wisdom` (`candidate`)
- `Wrath` (`candidate`)
### monsters_without_moves（17）
- `sts1.candidate.zh.monster.15436697` (`candidate`)
- `sts1.candidate.zh.monster.15436699` (`candidate`)
- `Apology Slime` (`candidate`)
- `Bear` (`candidate`)
- `Pointy` (`candidate`)
- `Romeo` (`candidate`)
- `Orb` (`candidate`)
- `Centurion` (`candidate`)
- `Dagger` (`candidate`)
- `Fire Orb` (`candidate`)
- `Flame Bruiser` (`candidate`)
- `Mystic` (`candidate`)
- `HexaghostBody` (`candidate`)
- `HexaghostOrb` (`candidate`)
- `Puppeteer` (`candidate`)
- `TheGuardianOrb` (`candidate`)
- `Torch Head` (`candidate`)
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
