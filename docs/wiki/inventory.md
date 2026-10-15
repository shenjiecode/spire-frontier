# 双源目录与身份审核视图（P2）

生成时间：2026-09-18T14:55:10+00:00。本页由当前 SQLite 目录重建；目录发现、文章采集和身份确认仍是不同层级。

- [目录 CSV](../../data/exports/inventory.csv)
- [目录 JSONL](../../data/exports/inventory.jsonl)
- [中英文映射清单](../../data/exports/name_mapping.csv)

## 目录数量

| 来源 | 语言 | 类别 | 状态 | 数量 |
| --- | --- | --- | --- | ---: |
| `game_local` | `en` | `event` | `parsed` | 1 |
| `game_local` | `en` | `status` | `parsed` | 1 |
| `wiki_gg` | `en` | `card` | `parsed` | 370 |
| `wiki_gg` | `en` | `character` | `parsed` | 4 |
| `wiki_gg` | `en` | `event` | `parsed` | 51 |
| `wiki_gg` | `en` | `keyword` | `parsed` | 25 |
| `wiki_gg` | `en` | `mechanic` | `parsed` | 24 |
| `wiki_gg` | `en` | `monster` | `parsed` | 45 |
| `wiki_gg` | `en` | `potion` | `parsed` | 42 |
| `wiki_gg` | `en` | `relic` | `excluded` | 13 |
| `wiki_gg` | `en` | `relic` | `parsed` | 180 |
| `wiki_gg` | `en` | `status` | `parsed` | 134 |
| `xiaoheihe` | `zh-CN` | `card` | `parsed` | 370 |
| `xiaoheihe` | `zh-CN` | `character` | `parsed` | 4 |
| `xiaoheihe` | `zh-CN` | `concept` | `parsed` | 10 |
| `xiaoheihe` | `zh-CN` | `event` | `parsed` | 52 |
| `xiaoheihe` | `zh-CN` | `mechanic` | `parsed` | 5 |
| `xiaoheihe` | `zh-CN` | `monster` | `parsed` | 45 |
| `xiaoheihe` | `zh-CN` | `potion` | `parsed` | 42 |
| `xiaoheihe` | `zh-CN` | `relic` | `parsed` | 179 |
| `xiaoheihe` | `zh-CN` | `status` | `parsed` | 133 |

## 读取说明

- wiki.gg 的目录按 StS1 范围保存；小黑盒目录来自用户指定 Wiki 的公开首页 JSON，文章快照保存在 `data/raw/`。
- `confirmed` 映射是经过英文 Wiki、中文文章和/或本机游戏本地化核对的身份关系；`candidate` 只表示待审线索。
- 目录行不等于规则事实。规则字段要看对应实体页的 claims、来源和验证状态。

## 当前审核计数

- 有效目录行：1717；排除目录行：13。
- 已确认身份映射：830；候选映射：0。
- [身份审核队列](mapping-review.md)；[三方完整性对照](../../reports/completeness-crosscheck.md)。
