# 杀戮尖塔1 视频知识学习 → 自动对局 Agent 项目方案（v2）

> 目标：基于 Qwen-MM-Plugins 的视频理解能力（omni-memory），分批学习中二少年恶魔之名的
> 杀戮尖塔1教学视频，沉淀为结构化知识库，驱动一个通过 mod 通道自动打杀戮尖塔的
> LLM Agent，并以跑局评测与日志沉淀为后续 SFT/RL 积累数据。
>
> v2 修订：视频知识为准（文字仅校对）；数值计算改为代码工具；视频分三批学习
> （游戏数据 → 卡牌认知 → 单角色实战）。

---

## 0. 范围与原则

1. 只做杀戮尖塔1。up 主的杀戮尖塔2教学不进管线。
2. **视频知识为准**。已调研文字生态：中文攻略碎片化（视频转载导读、2019 年新手文、
   站群 SEO 内容），英文 wiki 只有数据无策略区，up 主本人无文字版专栏——
   不存在与这套视频等价的成熟文字教学。文字/wiki 只用于 L0 校对，不做知识源。
3. **数值计算是代码，不是知识**。伤害/格挡/能量/启动回合代价等确定性运算
   全部实现为 agent 内置计算器工具；LLM 只做决策，不做算术。
4. 游戏操作全部走 mod 通道（JSON 协议），不做鼠标/键盘模拟。
5. 视频与提炼产物仅用于个人研究，不二次分发；自动化只跑本地对局，
   不碰每日挑战与排行榜。

---

## 1. 总体架构

```
轨道A 游戏介入层（独立工作线，先做）
  ModTheSpire + BaseMod + CommunicationMod（控制通路，JSON 协议）
  + 自定义 SpirePatch dump mod（信息增强：补盲区 + 提取游戏数据）
  + spirecomm（Python 封装）

轨道B 知识管线（分三批）
  批次一 基础数据库：游戏数据 dump + wiki 校对（非视频，零 omni 成本）
  批次二 卡牌认知：卡牌评测/遗物评测视频 → omni-memory → 增补认知层
  批次三 实战学习：战士 萌新实战(进阶5~16) → 高进阶实战 → 规则库 + 案例库
  （通用数值计算不走视频，落为代码工具；文字攻略仅校对参考）

轨道C Agent（依赖 A1 + 批次产出，随批次推进）
  spirecomm 状态 → 场景分流 → LLM 决策（知识检索 + 计算器工具）
  → 命令校验 → 执行 → 全量日志 → 评测 → 反思回写
```

---

## 2. 素材清单：中二少年恶魔之名（B站）

B站尖塔区 up。杀戮尖塔1教学体系（2026-02 查询）：

| 系列 | 总时长 | 备注 |
|---|---|---|
| 战士 超详细！！纯萌新实战教学攻略 进阶5~进阶16 | 17:15:20（20 集） | 218.7 万播放，BV1tu411V7QG |
| 战士 高进阶实战教学解说攻略 | 11:39:29 | |
| 猎人 超详细！！萌新实战教学攻略 进阶5~进阶16 | 13:11:41 | |
| 猎人 高进阶实战教学攻略 | 12:11:52 | |
| 机器人 超详细萌新实战解说攻略 进阶5~进阶16 | 12:46:00 | |
| 机器人 高进阶实战教学解说攻略 | 11:40:27 | BV1E94y1k78t（12 集） |
| 观者 进阶20 超详细萌新实战教学解说攻略 | 10:31:01 | |
| 四职业卡牌评测（战士/猎人/机器人/观者） | 合计约 5 小时 | 战士评测约 01:30:37 |
| 遗物评测 | 约 02:56:53 | 全职业共用 |
| 【攻略】如何规划一层 | 约 1 小时 | 路线规划专题 |
| 复盘/百连日记等 | 若干 | 案例库补充素材 |

- 执行时从 up 主空间页拉全集列表（部分 BV 号需逐系列补齐）；
  下载用 BBDown 或 yt-dlp（配 cookie），保留分 P 结构。
- **免费结构化元数据**：B站分P标题本身即高质量切段依据
  （如"进阶17 44血双药不敌三奴隶"），配合简介与置顶评论做视频切段索引。

---

## 3. 游戏介入层（轨道A）

### 3.1 控制通路

- **ModTheSpire**（CLI 启动加载 mod）+ **BaseMod**（底层 API）
- **CommunicationMod**（ForgottenArbiter，MIT）：游戏状态稳定时把完整 JSON 推给外部
  进程 stdin（手牌/抽弃牌堆/敌人意图与伤害预估/血量/能量/遗物/当前 screen），
  先握手 `ready`；外部进程回 JSON 命令：`play` / `end` / `discard` / `potion` /
  `choose` / `map` / `start` 等。SpireConfig 写 `command=` 指定外部进程。
- Python 侧用 **spirecomm**（matthewReff 维护 fork）：状态对象化 + Coordinator 收发循环。

### 3.2 信息增强通路（自研小 mod）

原版 CommunicationMod JSON 已知盲区：

- **观者 stance 字段不输出**（`GameStateConverter.java` 的 `convertPlayerToJson` 未转）；
- RNG 种子、完整牌库池、敌方未来行为等内部态缺失。

方案：SpirePatch 注解写自定义 mod 拦截内部状态，导出文件/socket
（参考 XlousMao/STS-AI-Master 的"Java Mod 数据拦截 + Protobuf"）。
该 mod 与批次一的数据 dump 共用同一套手艺。**A2 完成前观者线不启动。**

### 3.3 调试与造场景

- BaseMod console 命令：注入卡牌/遗物/金币、跳过战斗，用于构造训练与评测场景。

---

## 4. 知识管线（轨道B，三批）

### 4.1 选型：omni-memory

omni-memory（每 30 秒窗口：**画面描述 + 说话人标注逐句转写 + 非语音声音 +
归纳语义事实三元组**，保留 30s 源片段可 `replay_and_answer` 回放）优于 video-memory
（叙事图记忆，偏剧情问答）：画面与解说天然成对、语义事实即策略库雏形、
`--namespace` 可把系列内多个分 P 流式合并成一个连续记忆。

### 4.2 批次一：基础数据库（非视频，先做）

来源：自定义 SpirePatch mod dump 游戏数据 + 中文 wiki（wiki.biligame.com/sts）校对。

产出：

- `cards.json` / `relics.json` / `potions.json`：费用/类型/稀有度/升级效果/描述
- `monsters.json`：HP 区间/意图池/行为模式（作为"敌人认知"的客观底座）
- `events.json`、地图结构、进阶 5~20 逐级变化表
- **数值计算器工具集（代码）**：伤害计算（力量/易伤/虚弱）、格挡结算、
  能量规划、启动回合代价、敌人意图伤害预估——LLM 决策时直接调用

### 4.3 批次二：卡牌认知（视频第一批，约 4.5 小时）

素材：战士卡牌评测（01:30:37）+ 遗物评测（02:56:53）。

omni-memory 建记忆 → 在 L0 数据之上**增补认知字段**，形成两层合一的条目：

```
卡牌条目 = L0 客观数据（费用/效果/升级） 
         + 认知（强度评级, 适用流派, 抓取时机, 升级优先级, 协同/反例,
                出处[视频名, 时间戳, 源片段路径]）
遗物条目 = L0 客观数据 + 认知（强度评级, 出现时机价值, 路线影响, 出处）
```

- 认知以视频为准，wiki/文字攻略只做交叉校对（不一致时标注，回放源片段仲裁）。
- 本批结束即产出 agent 可用的"卡牌认知库"（战士先行，其余职业评测视频
  在扩展阶段补入）。

### 4.4 批次三：单角色实战学习（视频第二批，约 29 小时）

**选战士**：素材最全（萌新系列 20 集/17:15:20/218.7 万播放 + 高进阶 11:39:29 +
卡牌评测三件套齐），机制直白无特殊资源（观者有 stance 缺口、机器人有充能球），
首个闭环摩擦最小。

素材：战士萌新实战（进阶5~16，17:15:20）→ 战士高进阶实战（11:39:29）。

- omni-memory 建记忆（namespace 按系列合并，分 P 元数据做切段索引）
- 按决策场景提炼：
  - 选卡思路（结合批次二认知库的抓取时机）
  - 删卡时机、事件选项取舍
  - 地图路线规则（精英数量、篝火节奏、血量门槛）
  - 精英战/Boss 战对策（调用计算器验证解说中的数值判断）
  - 进阶 5~16 → 进阶 20 逐级难度应对
  - **敌人对策回填**：实战中暴露的敌人组合/意图处理经验，回填
    `monsters.json` 形成敌人认知层
- 产出两种形态：
  1. **规则条目库**：可检索的策略 markdown/JSON；
  2. **案例库**：具体局面（带时间戳与源片段），agent 遇到相似局面检索并回放核对。

### 4.5 成本模型

omni-memory 每 30 秒窗口 1 次 omni 调用（默认 `qwen3.5-omni-plus`，DashScope，
需 `DASHSCOPE_API_KEY`、`ffmpeg`/`ffprobe`、Python 3.10+；支持 `-j` 并行、
`--mode rebuild/append/resume`、`MEM_LOCAL_DIR`）。

| 批次 | 素材 | 估算调用 |
|---|---|---|
| 批次二 | 战士卡牌评测 + 遗物评测 ≈ 4.5h | ≈ 540 |
| 批次三 | 战士萌新 17:15:20 + 高进阶 11:39:29 ≈ 29h | ≈ 3,470 |
| **首轮合计** | ≈ 33.5h | **≈ 4,000** |
| （对照）四职业全量 | ≈ 100h | ≈ 12,000 |

首轮投入约为全量的 1/3。执行纪律：先 1 集试点测成本与质量（术语转写准确率
重点核对：nosl/进阶/卡牌俗名，必要时补术语词典后处理）→ 再批量。

### 4.6 扩展（验证后）

战士闭环达成验收后，按同管线复制：猎人/机器人（L0 已有，评测+实战视频补认知）；
观者等 A2 补 stance 后启动。视频角色随后降级为**权威仲裁源**：新问题先查
文字/wiki 与已有记忆，拿不准时定点建记忆并回放源片段。

---

## 5. Agent 设计（轨道C）

```
spirecomm 收 JSON state
  → 按 screen_type 分场景（战斗/选卡/地图/商店/事件/篝火/宝箱/BOSS奖励）
  → 拼上下文：游戏状态 + 知识检索（数据/认知/规则/案例）+ 本局决策摘要
  → LLM 决策（可调用数值计算器工具）
  → 命令合法性校验（对照 available_commands）
  → 执行，全量落日志
```

- 架构参考：Minhao-Zhang/slay_the_spire_agent（LangGraph + knowledge markdown +
  反思沉淀 + Web 面板），知识库换为本项目视频提炼产物。
- 评测：战士线核心指标 = 进阶20 胜率（分进阶层统计）；辅助 = 平均层数、
  血量损失曲线、败局归因（数值误判/路线失误/抓牌失误/机制未知）。
- 日志 = (state, action) 对 → SFT 数据；规模化后接 RL
  （sts_lightspeed C++ 模拟器训练，真机 CommunicationMod 终评）。
- 反思回写：败局归因结论写回知识库，形成"视频知识 → 实战检验 → 修正"闭环。

---

## 6. 执行计划

```
轨道A（先做）
  A1 ModTheSpire+BaseMod+CommunicationMod 跑通，spirecomm 规则 agent 打完一局
                                                      【验收：自动通关一层】
  A2 SpirePatch dump mod → 批次一数据四件套 + 补 stance 【验收：观者局 stance 可读】

轨道B（批次推进）
  B1 批次一：数据 dump + wiki 校对 + 数值计算器代码      【验收：四件套 JSON 通过抽查】
  B2 omni-memory 单集试点（战士卡牌评测 EP1）           【验收：单集成本+术语转写质量报告】
  B3 批次二：战士卡牌评测 + 遗物评测 → 认知库           【验收：逐卡/逐遗物条目人工抽查】
  B4 批次三：战士萌新(20集) → 高进阶 → 规则库+案例库    【按 B2 成本决定批量策略】

轨道C（依赖 A1+B1；随批次增强）
  C1 决策骨架 + B1 数据 + 计算器（暂无认知库）          【验收：进阶低层稳定通关】
  C2 接入 B3 认知库                                     【验收：选卡质量对比 C1 有提升】
  C3 接入 B4 规则库+案例库                              【验收：进阶20 批量对局报告】
  C4 日志 (state,action) 沉淀 + 反思回写                【验收：败局归因库、SFT 数据集】
```

依赖：A1 ∥ B1 → B2 → B3/B4；A2 阻塞观者一切工作；
C1 只依赖 A1+B1（可最早启动验证管线）。

---

## 7. 风险与注意事项

| 风险 | 应对 |
|---|---|
| omni-memory 批量成本超预算 | B2 单集试点先行；分 P 标题元数据做切段索引降低无效窗口 |
| 术语转写错误（nosl/卡牌俗名） | B2 重点核对；建术语词典做后处理；认知条目回放源片段复核 |
| CommunicationMod 年久（2019~2021） | 社区 fork 仍维护；盲区由自研 SpirePatch mod 兜底 |
| 观者 stance 缺失 | A2 必做项，阻塞观者线（本方案观者列扩展期，不阻塞主线） |
| B站下载与版权 | 仅个人学习，不二次分发、不公开传播提炼产物原文 |
| 游戏自动化边界 | 只跑本地对局；不用于每日挑战、排行榜等在线场景 |
| 战士闭环不达标即扩展 | 纪律：C3 验收通过前不启动其他职业视频批次 |

---

## 8. 参考资料

**视频理解**
- Qwen-MM-Plugins: https://github.com/QwenLM/Qwen-MM-Plugins
  （能力=skill+MCP；omni-memory / video-memory / core / api；依赖 uvx、ffmpeg；
  API key：`DASHSCOPE_API_KEY`；配置文件 `~/.qwen-mm-plugins/config`）
- omni-memory SKILL: `src/capabilities/omni-memory/skill/SKILL.md`
- B站搜索页: https://search.bilibili.com/all?keyword=中二少年恶魔之名

**游戏介入**
- CommunicationMod: https://github.com/ForgottenArbiter/CommunicationMod
- ModTheSpire: https://github.com/kiooeht/ModTheSpire
- BaseMod: https://github.com/daviscook477/BaseMod
- spirecomm（维护 fork）: https://github.com/matthewReff/spirecomm
- STS-AI-Master（PPO/数据拦截参考）: https://github.com/XlousMao/STS-AI-Master
- sts_lightspeed（C++ 模拟器）: https://github.com/gamerpuppy/sts_lightspeed

**Agent 架构参考**
- slay_the_spire_agent: https://github.com/Minhao-Zhang/slay_the_spire_agent

**下载与资料**
- BBDown: https://github.com/nilaoda/BBDown ；yt-dlp: https://github.com/yt-dlp/yt-dlp
- 中文 wiki（仅校对用）: https://wiki.biligame.com/sts
- B站 API 文档: https://github.com/SocialSisterYi/bilibili-API-collect

**文字生态调研结论（2026-02）**
- 中文：233乐园帖子多为视频转载导读；传统媒体攻略停在 2019 新手层面；
  happylx/spireofchaos 等为站群 SEO 内容；NGA/贴吧碎片化且有登录墙。
- 英文：fandom 与 wiki.gg 卡牌页仅数据无策略区；系统性讨论散落
  reddit 周讨论帖与 Steam 指南（部分已删）。
- 结论：无等价成熟文字教学，视频知识为准。
