# 覆盖与缺口

本页由 SQLite 生成，时间：2026-09-18T04:35:46+00:00。当前已完成 P3 首轮双源内容采集；卡牌、遗物、药水已进入结构化字段，角色/敌人/事件/状态/关键词/机制已保存正文并完成保守字段解析，身份映射和人工抽检仍需继续。P2 双源目录单独统计，目录发现不等于事实核验完成。

## 当前数量

实体共 1054 个（active 868，candidate 186）；名称 3751 个，claims 17606 条，关系 324 条，来源页面 933 个，图片资源 21 个。当前生成目录包含约 1876 个 Markdown 页面。

| 实体类别 | 数量 |
| --- | ---: |
| `card` | 422 |
| `character` | 4 |
| `concept` | 10 |
| `encounter` | 1 |
| `event` | 55 |
| `keyword` | 55 |
| `mechanic` | 25 |
| `monster` | 61 |
| `potion` | 44 |
| `relic` | 195 |
| `status` | 182 |

## P2 双源目录

| 来源 | 语言 | 类别 | 状态 | 数量 |
| --- | --- | --- | --- | ---: |
| `wiki_gg` | `en` | `card` | `parsed` | 370 |
| `wiki_gg` | `en` | `event` | `parsed` | 51 |
| `wiki_gg` | `en` | `keyword` | `parsed` | 25 |
| `wiki_gg` | `en` | `mechanic` | `parsed` | 19 |
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

P2 当前保存 1719 条目录行，已生成 816 条确认映射记录；其余身份仍需逐项审阅或保留为候选。

## P3 内容采集

- [P3 内容采集报告](../../reports/p3-content-report.json)
- 卡牌：英文 370，中文 370 条文章已采集并解析；未确认身份保留为候选实体。
- 遗物：英文 180，中文 179 条文章已采集并解析；未确认身份保留为候选实体。
- 药水：英文 42，中文 42 条文章已采集并解析；未确认身份保留为候选实体。
- 敌人：英文 45，中文 45 条文章已采集并解析；未确认身份保留为候选实体。
- 事件：英文 51，中文 52 条文章已采集并解析；未确认身份保留为候选实体。
- 状态：英文 134，中文 133 条文章已采集并解析；未确认身份保留为候选实体。
- 关键词：英文 25，中文 0 条文章已采集并解析；未确认身份保留为候选实体。
- 机制：英文 19，中文 5 条文章已采集并解析；未确认身份保留为候选实体。
- 角色：英文 0，中文 4 条文章已采集并解析；未确认身份保留为候选实体。
- 概念：英文 0，中文 10 条文章已采集并解析；未确认身份保留为候选实体。

## 游戏包第三来源

- [游戏本地化导入报告](../../reports/game-localization-report.json)
- Steam Build ID：`10180494`；JAR SHA-256：`cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673`。
  - `card`：本地化条目 423，已唯一对应现有实体 373，保留候选 50。
  - `potion`：本地化条目 45，已唯一对应现有实体 43，保留候选 2。
  - `relic`：本地化条目 195，已唯一对应现有实体 180，保留候选 15。
  - 本批精确游戏名映射审核决定：587 条。
- [游戏本地化扩展导入报告](../../reports/game-localization-extended-report.json)
  - `character`：本地化条目 4，已唯一对应现有实体 4，保留候选 0。
  - `event`：本地化条目 54，已唯一对应现有实体 51，保留候选 3。
  - `keyword`：本地化条目 48，已唯一对应现有实体 15，保留候选 33。
  - `monster`：本地化条目 72，已唯一对应现有实体 57，保留候选 15。
  - `status`：本地化条目 178，已唯一对应现有实体 132，保留候选 46。
  - 本次重放无新增决定，保留已有审核 CSV；扩展决定文件累计 211 条。
- 两批本地化导入共记录 798 条目录映射决定；实体合并另由显式 CSV 控制，未确认身份仍保留候选。

## 高风险身份复核

- [实体身份复核记录](../../reports/entity-resolution-review.md)

## 身份审核

- [中英文身份映射审核队列](mapping-review.md)
- [审核队列 CSV](../../data/decisions/mapping-review.csv)
- [审核队列 JSON](../../reports/mapping-review.json)

## P4 规则核验

- [P4 机制与规则核验审计](p4-rule-audit.md)
- [P4 审计 JSON](../../reports/p4-rule-audit.json)

## 状态解释

- `single_source`：只有一站提供或当前只采集到一站。
- `provisional`：已选择一个候选值，但尚未由第二来源或游戏数据确认。
- `conflict`：来源值存在差异，保留双方证据。
- `verified_game`：由本地游戏数据或可复现实验核实。

## 当前缺口

- 中英文大多数条目尚未完成身份审阅；候选实体不能当作双语确认事实。
- wiki.gg 能量图标和小黑盒图片承载的数值仍需视觉/字段交叉核对。
- 图片许可目前均标为 `unknown`，不自动将网页文本许可扩展到游戏图片。
- 当前已发现的双源目录行均已完成首轮文章采集；后续重点是字段级抽检和身份映射，而不是重复抓取。
- 未解决映射、冲突字段和复杂机制必须继续补齐，不能用模型记忆填充。
- 两份攻略保持独立；当前策略表为空，基础 Wiki 不生成攻略关联。
