# P0 来源审计（第一轮）

审计时间：2026-09-17（UTC）。这是本轮实际访问记录，后续全量采集前需要重新确认页面是否变化。

## 双主源

| 来源 | 入口/样例 | 结果 |
| --- | --- | --- |
| 英文 wiki.gg | [`Cards_List`](https://slaythespire.wiki.gg/wiki/Cards_List) | HTTP 200；页面标题为 “Cards List \| Slay the Spire 1”；页面显示 370 个结果。卡框的 `data-name/data-rarity/data-type/data-color/data-cost` 和基础/升级描述可从 HTML 读取。 |
| 英文 wiki.gg | [`Body_Slam`](https://slaythespire.wiki.gg/wiki/Body_Slam) | HTTP 200；页面包含 StS1/StS2 标签，必须选择 StS1 标签并排除 `Slay_the_Spire_2:` 命名空间。 |
| 英文 wiki.gg | [`api.php`](https://slaythespire.wiki.gg/api.php?action=query&format=json&titles=Body_Slam&prop=revisions&rvprop=content&rvslots=main) | 本轮探测 HTTP 200，已保存 JSON 样例；正式解析前仍需检查限流和响应结构变化。 |
| 小黑盒 | [`wiki_id=646570`](https://web.xiaoheihe.cn/wiki/home?wiki_id=646570) | 初始 HTML 是 Vue 壳，完整栏目由浏览器渲染。通过首页公开请求签名验证了 [`get_homepage_content`](https://api.xiaoheihe.cn/wiki/get_homepage_content/?wiki_id=646570) 目录接口；响应包含角色、卡牌、遗物、事件、诅咒、怪物、药水、能力/Buff 等栏目及筛选项。原始 JSON 已保存，不能把静态 HTML 当完整清单。 |
| 小黑盒 | [`全身撞击`](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=408598&wiki_id=646570) | 文章端点 HTTP 200；正文有基础、升级和测试画风段落；费用未出现在可见正文，卡图是必要证据。页面显示编辑者和编辑时间。 |

## 小黑盒本轮抽查的文章

已把原始响应保存在 `data/raw/xiaoheihe/2026-09-17/`，并登记到 SQLite 的 `source_pages`：

- 打击（article_id 404833）
- 全身撞击（408598）
- 燃烧之血（493025）
- 蛇之戒指（492919）
- 虚弱药水（496923）
- 史莱姆老大（531529）
- 我们又见面了！（15408930）
- 力量（501526）

“力量”页同时显示中文效果“攻击伤害提升 X 点。”和英文效果“Increases attack damage by #b.”；“史莱姆老大”页含生命、进阶 4+/19+ 行动表和行为模式；“我们又见面了！”页含选项锁定条件。它们已作为 P1 样本证据保存，尚未全部提升到 `verified_game`。

## 解析风险

1. wiki.gg 页面正文的能量、格挡等图标会通过 `<img alt=...>` 表达。只取 `innerText` 可能得到 “Gain .” 或 “Deal .”。解析器必须保留图片的 `alt/title/src` 和邻接文本，数值缺失时标为待核查。
2. 小黑盒文章响应的 HTML 元信息写 UTF-8，但本轮文章字节按 GBK 解码时中文正确。原始字节和解码文本分开保存，不能覆盖原始快照。
3. wiki.gg 同站包含 StS2；目录和页面必须按游戏标签/命名空间过滤。Mod、每日挑战和其他扩展不进入基础库。
4. 小黑盒首页的“遗物收集”初始可见项是少量初始遗物，职业牌初始可见项主要是攻击牌；已验证的目录接口需选择“全部”筛选并去重文章 ID，同时保留同一文章的不同中文别名。
5. wiki.gg 的文本页脚标示 CC BY-SA 4.0；本轮没有确认小黑盒正文和游戏图片的可再分发许可，所以数据库中的图片 `license_status` 保持 `unknown`。

## 本轮工具与快照

`scripts/kb/bootstrap_sample.py` 会串行抓取、指数退避、按 SHA-256 保存快照，并在 `reports/p1-sample-report.json` 中记录范围和限制。`scripts/kb/discover_inventory.py` 读取两站目录，保存小黑盒首页 JSON 快照，生成 `inventory.csv`、`inventory.jsonl`、`name_mapping.csv` 和 `reports/p2-inventory-report.json`。失败响应不绕过权限；脚本只在公共页面访问成功时继续。
