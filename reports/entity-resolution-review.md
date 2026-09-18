# 高风险身份复核记录

复核日期：2026-09-18。范围只包括基础 Wiki、安装包本地化和两站条目身份；不读取或关联两份攻略。

本次用 wiki.gg 的 MediaWiki API 逐页核对了以下标题，并把原始 JSON 保存到 `data/raw/wiki_gg/2026-09-18/entity-review/`。API 响应的页面状态和重定向信息只用于身份判断，不能代替条目正文或游戏规则字段。

| 标题 | HTTP | 快照 SHA-256（前 64 位） |
| --- | ---: | --- |
| `Spire Heart` | 200 | `c2feb4711ac9ba247e316569decda7021adff167e9e1f9ab61b479edc1bf6a68` |
| `The Heart` | 200 | `a314714b255f123821f42465247142c2e8108040e37daa70a9bc4802f51883c5` |
| `Centurion and Mystic` | 200 | `2679130604576e5f0438f3127cb288b2107864a43e661f87651ee2dd17823817` |
| `Centurion` | 200 | `b55e291ce2fd650b8868019e7b3dd938f5fe6f7ff0f05078496e79cd1c97e755` |
| `Mystic` | 200 | `5fcc8d2cff6fdbf992de3afd0cdd7ac7f3eeba717a749842eb8a006801eabded` |

## 高塔之心 / Spire Heart

- 小黑盒候选页：[高塔之心](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408927&wiki_id=646570) 的正文描述第三幕结束、钥匙和进入第四幕的门；它与安装包 `localization/eng/events.json` / `localization/zhs/events.json` 的 `Spire Heart` 键和 `高塔之心` 名称、选项（继续/攻击/睡眠/走向门前）一致。
- 对 `https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=2&titles=Spire%20Heart...` 和 `titles=The%20Heart...` 的查询均返回 `missing: true`。因此没有可用于双源合并的英文 Wiki 实体。
- 处理决定：确认“游戏本地化条目”和“小黑盒文章”描述的是同一个事件，并写入一条 `game_local` crosswalk。由于没有独立英文 Wiki 实体，`sts1.game.candidate.event.spire_heart` 与 `sts1.candidate.zh.event.15408927` 仍分别保留为候选证据；不把它们合并到 `Corrupt Heart` 或其他事件，也不把候选晋升为原版 active Wiki 实体。

## 百夫长 / 神秘术士 / Centurion and Mystic

- wiki.gg 页面 [Centurion and Mystic](https://slaythespire.wiki.gg/wiki/Centurion_and_Mystic) 的同一正文包含两个独立的 `Enemy Infobox`、生命值、行动表和互相的组队说明。API 的 [Centurion](https://slaythespire.wiki.gg/wiki/Centurion) 与 [Mystic](https://slaythespire.wiki.gg/wiki/Mystic) 页面分别是重定向，目标为 `Centurion and Mystic#Centurion` 和 `#Mystic`。
- 安装包 `monsters.json` 的键是 `Centurion`（简中“百夫长”）和 `Healer`（显示名 `Mystic`，简中“神秘术士”），因此游戏身份粒度是两个怪物；小黑盒也有两个独立中文文章候选页。原始英文合页快照和重定向 API JSON 均保留在上述目录。
- 处理决定：已经按合页锚点建立并确认 `sts1.monster.centurion` 与 `sts1.monster.mystic` 两个独立实体；两个中文单体目录行分别映射到同一英文合页的对应锚点。组合父页只保留成员关系，不把两个怪物的生命值或行动混到父实体。

## 游戏内部关键词与状态候选

本机包导入的候选包含 33 个关键词、46 个状态/能力条目（另有少量中文来源候选）。其中既有已废弃的开发条目，也有运行时内部状态、只在图片或局部正文出现的词，以及与卡牌或状态同名的关键词。关键词、状态、卡牌是不同类别；例如 `artifact`、`strength`、`frail` 同时可能出现在关键词和状态名中，不能仅凭名称合并。

处理决定如下：

1. 标有 `DEPRECATED`、`TODO`、`UNKNOWN` 或没有对应 StS1 Wiki 条目的条目继续保留为 `sts1.game.candidate.*`，作为游戏包证据，不作为可供玩家查询的 active Wiki 实体。
2. 具有同名 active 状态或卡牌的关键词不自动合并；只有找到同类别 Wiki 条目、正文定义和游戏键三者一致时，才新增显式映射决定。
3. “机器学习（能力）”已用小黑盒 Buffs id 与本机 `Machine Learning` 本地化键确认，并记录为 game-local crosswalk；由于英文 wiki 只在 `Buffs#Draw` 下按通用效果展示，仍保留游戏候选，不强行合并为独立 wiki 状态。
4. “以手拒之（能力）”的英文效果、`Talk to the Hand` Buffs id、wiki.gg `Block Return` 锚点和本机 `BlockReturnPower` 描述一致，已合并到 `sts1.status.block_return`；中文标题作为已审核别名保留。

## 已确认的对照范围

`Sentry` 是本轮可安全合并的对照：游戏键、两站目录行和小黑盒文章范围均指向第一幕精英哨卫，已记录在 `data/decisions/mapping-decisions.monster-manual.csv`。角色四页、四个历史命名状态和其他明确一对一的合并记录在 `data/decisions/entity-merges.game-local.csv`。

这些保守决定让“能确认的身份”和“只是名称相似的候选”在数据库中保持可区分；后续补充英文条目或支持合页子实体时，可以按本记录继续重放，而无需改写既有来源快照。
