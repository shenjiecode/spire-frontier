# spire-scholar

从《杀戮尖塔1》教学视频中学习策略知识，构建可自动打塔的 LLM Agent。

- **知识源**：B站 up 主「中二少年恶魔之名」的杀戮尖塔1教学系列（视频知识为准，
  wiki/文字仅校对）。视频理解基于 [Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins)
  的 omni-memory 能力，分批学习：游戏数据 → 卡牌认知 → 单角色实战。
- **游戏介入**：ModTheSpire + BaseMod + CommunicationMod（JSON 协议控制）+
  自研 SpirePatch 数据 dump mod（信息增强），零鼠标模拟。
- **数值计算**：确定性运算（伤害/格挡/能量/启动回合代价）实现为 agent 内置
  计算器工具，LLM 只做决策不做算术。
- **目标**：进阶20 分职业胜率评测；跑局日志沉淀 (state, action) 数据，
  供后续 SFT / RL（sts_lightspeed 模拟器）训练。

完整设计见 [docs/设计文档-杀戮尖塔视频学习Agent.md](docs/设计文档-杀戮尖塔视频学习Agent.md)。

## 状态

🚧 设计阶段。三条轨道：

| 轨道 | 内容 | 状态 |
|---|---|---|
| A 游戏介入层 | CommunicationMod 跑通 + SpirePatch dump mod | 未开始 |
| B 知识管线 | 数据库 → 卡牌认知 → 战士实战（分批） | 未开始 |
| C Agent | spirecomm + LLM 决策 + 评测闭环 | 未开始 |
