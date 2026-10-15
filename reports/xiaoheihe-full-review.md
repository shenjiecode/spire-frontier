# 小黑盒全目录对照审核（2026-09-18）

数据库和聚合记录已按全目录进行覆盖检查与可确定字段修正。这里的“覆盖”表示已关联或明确记录缺口，不能等同于每条规则均完成人工验证。

## 范围与来源

- 895 篇唯一文章，1,763 条目录归属；保留多分类关系。
- 本次成功获取796篇；99篇返回 HTTP 403，使用此前快照并标记 historical_fallback，不能声称它们是当前网页内容。
- 974个 active 实体；另保留173个 candidate、10个 deprecated 审计记录。
- 47张怪物表格图已辅助查看，URL、哈希和冲突见 [图片审核记录](../data/decisions/xiao-monster-image-review.json)。不新增图片运行依赖。

## 各类覆盖

| 类别 | active记录 | 有小黑盒页面关联 |
|---|---:|---:|
| card | 370 | 370 |
| character | 4 | 4 |
| encounter | 39 | 0 |
| event | 51 | 51 |
| keyword | 22 | 0 |
| mechanic | 61 | 41 |
| monster | 71 | 70 |
| potion | 42 | 42 |
| relic | 180 | 179 |
| status | 134 | 132 |

怪物页面关联包含合页成员关系，不代表成员独立数值已核实。遭遇池、内部关键词和部分机制没有单独的小黑盒文章，已留下明确缺口。

## 已修正

- 纠正负敏捷与回合结束失去敏捷的身份混淆。
- 清理159条遗物、36条药水中文描述中的模板残留或整表混入；分离英文遗物背景文案。
- 修正基础/升级卡牌描述混用；714/722个变体可由本机官方模板与直接字节码常量生成描述，584个变体含可直接确认的数值，369张卡已有目标枚举。
- 例如：Evaluate基础格挡6、Burn升级伤害4、Third Eye升级格挡9/预见5、Bloodletting能量2/3。
- 新增36条每日/自定义模式修饰符，保留游戏ID、双语名称和效果。
- 清理青铜自动机、蛇女、收藏家混入的召唤物招式；分离抢劫者/偷窃者行动；合并史莱姆老大双语重复动作。
- 六火亡魂Divider、黑暗蜉蝣Nip、倏忽魔Attack不再用单个常数冒充公式/范围，完整公式保留在 effect_json。

## 冲突与未完成验证

皇家枕头采用游戏常量15，小黑盒遗物页写25；飞靴采用游戏显示阈值4；工具箱保留选择3张中的1张效果。原文和采用依据分别保留，不覆盖来源证据。

仍需逐条语义核验的重点：事件分支条件、怪物行动概率和进阶阈值、合页成员、仅在图片中的卡牌费用，以及动态/多次升级数值。基因算法、仪式匕首、停顿、灼热攻击共8个基础/升级变体未由通用模板自动确认。

文本差异已逐对自审，详见[自审结果](文本差异自审.md)。数字写法、同义措辞和已解释的来源差异不再作为待用户判断的数值冲突。以下统计含候选与废弃实体；状态只表示对应字段的审核层次。

| 状态 | 条数 |
|---|---:|
| match | 2854 |
| requires_semantic_review | 114 |
| not_in_source_text | 844 |
| shared_page_or_name_difference | 2 |
| equivalent_wording | 82 |
| resolved_source_difference | 42 |
| equivalent_notation | 59 |
| rule_difference_pending | 1 |
| source_annotation | 22 |
| source_editorial_error | 26 |
| renderer_corrected | 3 |
| member_specific_review_required | 25 |
| no_direct_xiao_article | 254 |

## 使用与复核

本次校验：11项回归测试通过；SQLite外键、关系表导出一致性和生成Wiki链接检查无错误。仍有同名实体及来源原文占位文字告警，不能将这些告警解释为规则核验通过。

- [SQLite主库](../data/spire.sqlite)；[数据库记录说明](../docs/数据库记录说明.md)。
- `data/records/*.jsonl`：按类别聚合的974条正式记录；`xiaoheihe_articles.jsonl`另存895篇来源文章、表格、章节。
- `xiao_field_checks` / [字段对照](xiaoheihe-field-checks.jsonl)：当前值、来源值及审核状态。
- `xiao_corrections`：修正前后值和来源。重复构建可能产生多次历史修正，不应按日志行数统计修正规则数。
- 理解字段现为35个实体、37段明确建议；来源观点单独标记，其余为null。此前两份独立攻略未引入。

```sh
python -X utf8 scripts/kb/review_xiao.py
python -X utf8 scripts/kb/apply_xiao_review.py
python -X utf8 scripts/kb/import_review_card_values.py
python -X utf8 scripts/kb/fix_review_monster_moves.py
python -X utf8 scripts/kb/review_xiao.py
python -X utf8 scripts/kb/build_records.py
python -X utf8 scripts/kb/build_wiki.py
python -X utf8 -m unittest discover -s tests -p "test_kb*.py"
python -X utf8 scripts/kb/validate_kb.py
```
