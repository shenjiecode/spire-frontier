# 双源目录（P2）

生成时间：2026-09-17T16:27:41+00:00。本页只记录两站目录发现结果，不把未核对的中文/英文条目合并为正式实体。

- [目录 CSV](../../data/exports/inventory.csv)
- [目录 JSONL](../../data/exports/inventory.jsonl)
- [中英文映射清单](../../data/exports/name_mapping.csv)

## 目录数量

| 来源 | 语言 | 类别 | 状态 | 数量 |
| --- | --- | --- | --- | ---: |
| `wiki_gg` | `en` | `card` | `discovered` | 370 |
| `wiki_gg` | `en` | `event` | `discovered` | 51 |
| `wiki_gg` | `en` | `keyword` | `discovered` | 25 |
| `wiki_gg` | `en` | `mechanic` | `discovered` | 19 |
| `wiki_gg` | `en` | `monster` | `discovered` | 45 |
| `wiki_gg` | `en` | `potion` | `discovered` | 42 |
| `wiki_gg` | `en` | `relic` | `discovered` | 180 |
| `wiki_gg` | `en` | `relic` | `excluded` | 13 |
| `wiki_gg` | `en` | `status` | `discovered` | 134 |
| `xiaoheihe` | `zh-CN` | `card` | `discovered` | 370 |
| `xiaoheihe` | `zh-CN` | `character` | `discovered` | 4 |
| `xiaoheihe` | `zh-CN` | `concept` | `discovered` | 10 |
| `xiaoheihe` | `zh-CN` | `event` | `discovered` | 52 |
| `xiaoheihe` | `zh-CN` | `mechanic` | `discovered` | 5 |
| `xiaoheihe` | `zh-CN` | `monster` | `discovered` | 45 |
| `xiaoheihe` | `zh-CN` | `potion` | `discovered` | 42 |
| `xiaoheihe` | `zh-CN` | `relic` | `discovered` | 179 |
| `xiaoheihe` | `zh-CN` | `status` | `discovered` | 133 |

## 读取说明

- wiki.gg 的卡牌、遗物、药水和事件列表使用页面结构化盒子；普通敌人、精英和 Boss 使用各自页面的图鉴图像链接。
- 小黑盒目录来自用户指定 Wiki 的动态首页 JSON；原始响应已保存到 `data/raw/xiaoheihe/`，文章正文仍需在后续阶段逐项抓取。
- wiki.gg 遗物清单中的 `Blight` 条目被标记为 `excluded`（StS2 范围），没有写入基础实体。
- 日常挑战、职业打法、常见问题和百科维护栏目不属于当前基础 Wiki；它们的排除数量写在 P2 报告中。
- `confirmed` 映射只复制 P1 中已经审阅的实体；`unmatched_*` 是待核查项，不能当作缺少对应条目的结论。

## 报告

- [P2 目录报告](../../reports/p2-inventory-report.json)
- 当前发现 1706 条有效目录记录，7 对已审阅映射。
