# spire-scholar

从《杀戮尖塔 1》的双语 Wiki 建立可追溯的基础知识库，并为后续自动打塔 Agent 提供结构化事实。

当前知识库采用 SQLite 主库 + 自动生成的互链 Markdown Wiki；不使用 RAG 或向量召回。双主源是用户指定的[小黑盒 Wiki](https://web.xiaoheihe.cn/wiki/home?wiki_id=646570)和英文 [wiki.gg](https://slaythespire.wiki.gg/)。此前整理的两份攻略保持独立，当前不与基础 Wiki 建立关联。

## 当前知识库状态

- [双语知识 Wiki](docs/wiki/index.md)：SQLite 中有 1,121 个 StS1 实体，已生成可读页面和互链；其中 938 个为 active 实体，173 个为保留待审的 candidate 实体，10 个为保留审计轨迹的 deprecated 记录。
- 当前数据库统计：3,802 个名称、18,569 条 claims、426 条关系、938 个来源页面、21 个图片资源；生成 Wiki 共 1,127 个 Markdown 页面。纯合页父记录只保留来源和成员关系，怪物数值放在拆分后的成员页。
- 身份审核：830 条目录映射已确认，其中 828 条指向 wiki.gg、2 条保留为本机游戏本地化 crosswalk；未确认的 10 条中文目录行均为小黑盒独有的概念/说明页。未确认的游戏内部条目仍保留 candidate，不因中英文名称同时存在而晋升。
- [P1 样本报告](reports/p1-sample-report.json)：最初的纵向样本、来源快照和图片证据。
- [P0 来源审计](reports/source-audit.md)：访问方式、解析风险、许可和已保存快照。
- [P2 双源目录](docs/wiki/inventory.md)：已保存两站目录快照、分类计数和中英文待匹配清单。
- [P3 内容采集报告](reports/p3-content-report.json)：卡牌、遗物、药水、敌人、事件、状态、关键词和机制的双源文章已首轮入库，角色与概念栏目也已保存中文页面证据；未审阅的身份映射保留为候选。
- [游戏本地化导入报告](reports/game-localization-report.json)：记录本机 JAR SHA-256、Steam Build ID、卡牌/遗物/药水本地化 JSON，以及 587 条精确游戏名映射审核决定。
- [游戏本地化扩展导入报告](reports/game-localization-extended-report.json)：记录事件、怪物、状态、关键词和角色本地化；扩展决定文件累计 211 条，分批审核，不能把候选条目当成 Wiki 实体。
- [实体身份复核记录](reports/entity-resolution-review.md)：记录高塔之心、百夫长/神秘术士及游戏内部关键词/状态候选的保守处理决定。
- [实体合并审核决定](data/decisions/entity-merges.game-local.csv)：8 条已由 JAR、本地化和来源粒度核对的显式合并决定。
- [图像人工复核决定](data/decisions/mapping-decisions.image-review.csv)：4 条名称翻译不一致但经卡图/遗物图标和效果复核确认的映射。
- [中英文身份映射审核队列](docs/wiki/mapping-review.md)：基于类别、角色、数字和规则标记的候选排序，不自动合并实体。
- [审核决定说明](data/decisions/README.md)：确认映射的 CSV 格式、校验和重放命令。
- [P4 规则核验审计](docs/wiki/p4-rule-audit.md)：字段覆盖、缺失动作/分支、图标损失和许可待办。
- [三方完整性对照](reports/completeness-crosscheck.md)：wiki.gg、小黑盒和本机游戏包的目录、结构化字段、候选身份与剩余缺口。
- [结构化修复记录](reports/structured-repair-report.json)：卡牌/遗物/药水/怪物/遭遇/状态等可由已保存证据确定的修复，以及图片关联结果。
- [基础知识库建设执行计划](docs/基础知识库建设执行计划.md)：全量采集和验收规格。

## 重建样本 Wiki

在仓库根目录执行：

```powershell
$env:PYTHONIOENCODING='utf-8'
python scripts/kb/bootstrap_sample.py
python scripts/kb/discover_inventory.py
python scripts/kb/fetch_p3.py
python scripts/kb/import_game_localization.py
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.game-local.csv
python scripts/kb/import_game_extended.py
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.game-extended.csv
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.game-extended-status.csv
python scripts/kb/apply_entity_merge_decisions.py --file data/decisions/entity-merges.game-local.csv
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.monster-manual.csv
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.status-manual.csv
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.image-review.csv
python scripts/kb/repair_structured_data.py
python scripts/kb/cross_source_audit.py
python scripts/kb/build_wiki.py
python scripts/kb/audit_mappings.py
python scripts/kb/p4_audit.py
python scripts/kb/validate_kb.py
python tests/smoke_test.py
```

原始页面快照位于 `data/raw/`，必要图片位于 `data/assets/`，结构化导出位于 `data/exports/`，审核决定位于 `data/decisions/`。`discover_inventory.py` 只负责目录发现；不要在 P3 后为了刷新状态重新运行它。`fetch_p3.py` 默认采集卡牌、遗物和药水，`--all` 可采集全部已发现类别，`--refresh --languages en` 可只用已有快照重放英文解析；事件选项解析会处理嵌套 `Frame`、锁定分支和旧投影清理，原始按钮数组仍保留在游戏本地化 claims 中。`import_game_localization.py` 负责卡牌、遗物和药水；`import_game_extended.py` 负责事件、怪物、状态、关键词和角色。未核对的中英文条目会写入候选实体并明确显示 `single_source`、`provisional` 等状态，不会冒充已确认事实。`audit_mappings.py` 和 `p4_audit.py` 只生成审核报告，不改身份映射；实体合并只能通过显式 CSV 重放。两份攻略仍保持独立，`strategy_notes` 与 `strategy_links` 必须为空。

游戏介入、CommunicationMod 和确定性计算器的旧设计仍保留在[设计文档](docs/设计文档-杀戮尖塔视频学习Agent.md)，待基础知识库稳定后再接入。
