# 审核决定

`mapping-review.csv` 是自动生成的候选排序，不能直接当作事实。人工对照两站原文后，把确认的行复制到 `mapping-decisions.csv`（字段见 `mapping-decisions.template.csv`）。本机游戏包导入器生成 `mapping-decisions.game-local.csv`（卡牌/遗物/药水）和 `mapping-decisions.game-extended.csv`（事件/怪物/状态等）：只有英文目录名、简体中文目录名、类别/角色和游戏本地化条目同时精确对应的行才会进入这些文件，证据中保留 JAR SHA-256、Steam Build ID 和本地化 JSON 页面 ID。

`mapping-decisions.game-extended-status.csv` 和 `mapping-decisions.status-manual.csv` 记录状态名称的显式校正；`mapping-decisions.monster-manual.csv` 记录来源粒度和图片/正文范围均核对过的怪物映射。`mapping-decisions.source-crosswalk.csv` 记录高塔之心、机器学习与以手拒之的三条跨源复核；前两条只确认到本机游戏本地化键，后一条合并到 `Block Return`。`entity-merges.game-local.csv` 是候选实体到 active 实体的独立合并决定，不能用普通目录映射代替。高塔之心、百夫长/神秘术士和游戏内部候选的处理理由见 `reports/entity-resolution-review.md`。
需要名称翻译不一致的条目时，图像/效果人工复核写入 `mapping-decisions.image-review.csv`，证据保留图片 URL、下载内容哈希和复核理由；它与游戏包自动决定分开重放。

```powershell
$env:PYTHONIOENCODING='utf-8'
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.csv
python scripts/kb/fetch_p3.py --refresh --languages zh-CN --kinds card,relic,potion,event,monster,status,mechanic
python scripts/kb/audit_mappings.py
python scripts/kb/build_wiki.py
python scripts/kb/validate_kb.py
```

Cross-source rows in `mapping-decisions.source-crosswalk.csv` are replayed by `scripts/kb/repair_structured_data.py` (the quality supplement is idempotent); rerun that command before rebuilding the Wiki after a fresh import.

导入已安装游戏的第三来源（默认路径为 Steam 的 `desktop-1.0.jar`）：

```powershell
$env:PYTHONIOENCODING='utf-8'
python scripts/kb/import_game_localization.py
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.game-local.csv
python scripts/kb/import_game_extended.py
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.game-extended.csv
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.game-extended-status.csv
python scripts/kb/apply_entity_merge_decisions.py --file data/decisions/entity-merges.game-local.csv
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.monster-manual.csv
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.status-manual.csv
python scripts/kb/apply_mapping_decisions.py --file data/decisions/mapping-decisions.image-review.csv
```

游戏包中未能唯一对应 wiki 的本地化条目会保留为 `sts1.game.candidate.*`，不会因为同时存在中英文名称就自动晋升为 wiki 实体。英文合页下的独立锚点也必须保留来源粒度，不能把多个怪物折叠到一个合页实体。

脚本会检查中英文语言、类别、卡牌角色和确认映射的一对一约束，并在一个事务中写入 `inventory_mappings`。没有 `rationale` 的确认行会被拒绝。`candidate`、`conflict`、`rejected` 可以先记录为审核结论，但不会合并实体。

不要重新运行 `discover_inventory.py` 来刷新 P3 状态；它会重建目录行。攻略文档不属于本审核范围。
