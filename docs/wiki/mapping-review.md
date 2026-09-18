# 中英文身份映射审核队列

本页由 `scripts/kb/audit_mappings.py` 从 SQLite 生成。它只提供候选排序，不会自动合并实体；确认后应通过独立审核决定写入 `inventory_mappings`。

待审核中文目录行：246；已有 confirmed 映射跳过：594。

| 类别 | 中文名 | 首选英文候选 | 分数 | 置信标记 | 备选数 | 证据提示 |
| --- | --- | --- | ---: | --- | ---: | --- |
| `character` | [故障机器人](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15589967&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `character` | [观者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15589965&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `character` | [铁甲战士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15543423&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `character` | [静默猎手](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15589144&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [关于游戏](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=530545&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [卡牌介绍](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15465872&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [卡牌奖励机制](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15715746&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [成就列表一览](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9655623&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [敌人意图](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15543865&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [每日挑战介绍](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15722655&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [自定义介绍](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15722654&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [药水介绍](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15465874&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [进入心脏战方式](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15463398&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `concept` | [进阶模式](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432040&wiki_id=646570) | — | 0 | `no_candidate` | 0 | 无 |
| `event` | [全知头骨](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408883&wiki_id=646570) | Knowing Skull | 2.667 | `low_signal` | 51 | numeric_overlap:1/3 |
| `event` | [冒险者尸体](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375140&wiki_id=646570) | Mind Bloom | 3.636 | `low_signal` | 51 | numeric_overlap:5/11 |
| `event` | [净化](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408957&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [升级神龛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408962&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [变化大转盘](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408964&wiki_id=646570) | Face Trader | 2.0 | `low_signal` | 51 | numeric_overlap:1/4 |
| `event` | [古老文字](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408867&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [吸血鬼](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408899&wiki_id=646570) | Vampires | 5.333 | `low_signal` | 51 | numeric_overlap:2/3 |
| `event` | [坠落](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408914&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [增益研究者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408876&wiki_id=646570) | Augmenter | 4.0 | `low_signal` | 51 | numeric_overlap:1/2 |
| `event` | [复制祭坛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408940&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [大图书馆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408893&wiki_id=646570) | The Woman in Blue | 5.333 | `low_signal` | 51 | numeric_overlap:4/6 |
| `event` | [大鱼](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375121&wiki_id=646570) | Big Fish | 8.0 | `weak_candidate` | 51 | numeric_overlap:3/3 |
| `event` | [实验室](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408955&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [对对碰！](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408948&wiki_id=646570) | Big Fish | 2.667 | `low_signal` | 51 | numeric_overlap:1/3 |
| `event` | [尖端设计师](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408934&wiki_id=646570) | Designer In-Spire | 5.0 | `low_signal` | 51 | numeric_overlap:5/8 |
| `event` | [巢穴](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389473&wiki_id=646570) | The Nest | 6.0 | `low_signal` | 51 | numeric_overlap:3/4 |
| `event` | [幽灵会议](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408902&wiki_id=646570) | Council of Ghosts | 6.0 | `low_signal` | 51 | numeric_overlap:3/4 |
| `event` | [心灵绽放](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408905&wiki_id=646570) | Mind Bloom | 3.0 | `low_signal` | 51 | numeric_overlap:3/8 |
| `event` | [恩洛斯](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389480&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [感知石](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408911&wiki_id=646570) | Sensory Stone | 8.0 | `weak_candidate` | 51 | numeric_overlap:5/5 |
| `event` | [换脸商](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389469&wiki_id=646570) | Face Trader | 6.0 | `low_signal` | 51 | numeric_overlap:3/4 |
| `event` | [摩艾石像](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408916&wiki_id=646570) | The Moai Head | 4.8 | `low_signal` | 51 | numeric_overlap:3/5 |
| `event` | [活墙壁](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375288&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [流浪汉的恳求](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408865&wiki_id=646570) | Pleading Vagrant | 8.0 | `weak_candidate` | 51 | numeric_overlap:1/1 |
| `event` | [牧师](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375132&wiki_id=646570) | The Cleric | 6.4 | `low_signal` | 51 | numeric_overlap:4/5 |
| `event` | [留给自己的讯息](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408938&wiki_id=646570) | Wheel of Change | 2.667 | `low_signal` | 51 | numeric_overlap:1/3 |
| `event` | [破烂软泥](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375295&wiki_id=646570) | Cursed Tome | 4.444 | `low_signal` | 51 | numeric_overlap:5/9 |
| `event` | [神圣泉水](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408932&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [神秘圆球](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408919&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [秘密传送门](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408908&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [竞技场](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15389476&wiki_id=646570) | Golden Shrine | 4.0 | `low_signal` | 51 | numeric_overlap:1/2 |
| `event` | [篝火精灵](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408945&wiki_id=646570) | Scrap Ooze | 4.8 | `low_signal` | 51 | numeric_overlap:3/5 |
| `event` | [红面具大人之墓](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408922&wiki_id=646570) | Tomb of Lord Red Mask | 4.0 | `low_signal` | 51 | numeric_overlap:1/2 |
| `event` | [翅膀雕像](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375158&wiki_id=646570) | Wing Statue | 8.0 | `weak_candidate` | 51 | numeric_overlap:4/4 |
| `event` | [老乞丐](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408870&wiki_id=646570) | Old Beggar | 8.0 | `weak_candidate` | 51 | numeric_overlap:1/1 |
| `event` | [蒙面强盗](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408886&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [蓝衣女子](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408968&wiki_id=646570) | The Woman in Blue | 5.333 | `low_signal` | 51 | numeric_overlap:6/9 |
| `event` | [蘑菇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375291&wiki_id=646570) | Masked Bandits | 4.0 | `low_signal` | 51 | numeric_overlap:1/2 |
| `event` | [蛇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375278&wiki_id=646570) | The Ssssserpent | 5.333 | `low_signal` | 51 | numeric_overlap:2/3 |
| `event` | [蜿蜒走廊](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408924&wiki_id=646570) | Winding Halls | 6.857 | `low_signal` | 51 | numeric_overlap:6/7 |
| `event` | [被遗忘的祭坛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408880&wiki_id=646570) | Forgotten Altar | 4.8 | `low_signal` | 51 | numeric_overlap:3/5 |
| `event` | [诅咒书本](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408873&wiki_id=646570) | Sensory Stone | 6.4 | `low_signal` | 51 | numeric_overlap:4/5 |
| `event` | [转化神龛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408959&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [邪恶熔炉](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408942&wiki_id=646570) | A Note For Yourself | 0.0 | `low_signal` | 51 | 无 |
| `event` | [金神像](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375147&wiki_id=646570) | Golden Idol | 6.4 | `low_signal` | 51 | numeric_overlap:4/5 |
| `event` | [金色神龛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408951&wiki_id=646570) | The Joust | 4.8 | `low_signal` | 51 | numeric_overlap:3/5 |
| `event` | [长枪决斗](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408890&wiki_id=646570) | The Joust | 5.714 | `low_signal` | 51 | numeric_overlap:5/7 |
| `event` | [闪耀之光](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375299&wiki_id=646570) | Shining Light | 6.0 | `low_signal` | 51 | numeric_overlap:3/4 |
| `event` | [陵墓](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408896&wiki_id=646570) | Sensory Stone | 3.2 | `low_signal` | 51 | numeric_overlap:2/5 |
| `event` | [高塔之心](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408927&wiki_id=646570) | Big Fish | 5.2 | `low_signal` | 51 | numeric_overlap:2/5, markers:attack |
| `event` | [黏液世界](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15375165&wiki_id=646570) | World of Goop | 6.667 | `low_signal` | 51 | numeric_overlap:5/6 |
| `mechanic` | [休息处](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15463366&wiki_id=646570) | Acts | 0.0 | `low_signal` | 19 | 无 |
| `mechanic` | [商人](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15440709&wiki_id=646570) | Acts | 0.0 | `low_signal` | 19 | 无 |
| `mechanic` | [宝箱房](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15463362&wiki_id=646570) | Acts | 0.0 | `low_signal` | 19 | 无 |
| `mechanic` | [怪物介绍](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15539744&wiki_id=646570) | Acts | 0.0 | `low_signal` | 19 | 无 |
| `mechanic` | [问号房](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15624135&wiki_id=646570) | Acts | 0.0 | `low_signal` | 19 | 无 |
| `monster` | [三机械](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408985&wiki_id=646570) | Acid Slimes | 5.733 | `low_signal` | 45 | numeric_overlap:7/15, markers:attack |
| `monster` | [乐加维林](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421614&wiki_id=646570) | Acid Slimes | 0.0 | `low_signal` | 45 | 无 |
| `monster` | [倏忽魔](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438060&wiki_id=646570) | Cultist | 4.0 | `low_signal` | 45 | numeric_overlap:2/4 |
| `monster` | [八体/甜圈](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432032&wiki_id=646570) | Donu and Deca | 10.0 | `weak_candidate` | 45 | numeric_overlap:5/10, markers:attack,block,strength |
| `monster` | [六火亡魂](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421622&wiki_id=646570) | Byrd | 8.364 | `weak_candidate` | 45 | numeric_overlap:6/11, markers:attack,strength |
| `monster` | [哨位(精英)](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421616&wiki_id=646570) | Lagavulin | 6.0 | `low_signal` | 45 | numeric_overlap:3/4 |
| `monster` | [圆球守护者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436694&wiki_id=646570) | Corrupt Heart | 1.333 | `low_signal` | 45 | numeric_overlap:1/6 |
| `monster` | [圆球行者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15437647&wiki_id=646570) | Spire Shield and Spire Spear | 6.286 | `low_signal` | 45 | numeric_overlap:4/14, markers:attack,orb |
| `monster` | [地精大块头](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421612&wiki_id=646570) | Lagavulin | 4.0 | `low_signal` | 45 | numeric_overlap:2/4 |
| `monster` | [地精小队](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411818&wiki_id=646570) | Looter | 1.0 | `low_signal` | 45 | numeric_overlap:1/8 |
| `monster` | [地精首领](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432036&wiki_id=646570) | Reptomancer | 5.556 | `low_signal` | 45 | numeric_overlap:4/9, markers:attack |
| `monster` | [塔内增生组织](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438539&wiki_id=646570) | Spire Growth | 6.0 | `low_signal` | 45 | numeric_overlap:6/12, markers:attack |
| `monster` | [大脑袋](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436792&wiki_id=646570) | Giant Head | 8.0 | `weak_candidate` | 45 | numeric_overlap:6/12, markers:attack,weak |
| `monster` | [大颚虫](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15420602&wiki_id=646570) | Jaw Worm | 5.0 | `low_signal` | 45 | numeric_overlap:5/8 |
| `monster` | [天罚](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436798&wiki_id=646570) | Spire Shield and Spire Spear | 5.429 | `low_signal` | 45 | numeric_overlap:6/14, markers:attack |
| `monster` | [奴隶主](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15417595&wiki_id=646570) | The Maw | 2.0 | `low_signal` | 45 | numeric_overlap:1/4 |
| `monster` | [奴隶头子](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432034&wiki_id=646570) | Taskmaster | 9.333 | `weak_candidate` | 45 | numeric_overlap:4/6, markers:attack,strength |
| `monster` | [守护者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421621&wiki_id=646570) | The Guardian | 13.647 | `weak_candidate` | 45 | numeric_overlap:12/17, markers:attack,block,vulnerable,weak |
| `monster` | [小黑](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438057&wiki_id=646570) | The Champ | 8.824 | `weak_candidate` | 45 | numeric_overlap:6/17, markers:attack,strength,weak |
| `monster` | [尖刺史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411793&wiki_id=646570) | Looter | 1.0 | `low_signal` | 45 | numeric_overlap:1/8 |
| `monster` | [巨口](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438054&wiki_id=646570) | The Maw | 10.0 | `weak_candidate` | 45 | numeric_overlap:4/8, markers:attack,strength,weak |
| `monster` | [带壳寄生怪](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436702&wiki_id=646570) | Looter | 3.0 | `low_signal` | 45 | numeric_overlap:1/8, markers:block |
| `monster` | [异蛇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436731&wiki_id=646570) | Acid Slimes | 7.692 | `low_signal` | 45 | numeric_overlap:6/13, markers:attack,weak |
| `monster` | [异鸟](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436744&wiki_id=646570) | Spire Shield and Spire Spear | 6.211 | `low_signal` | 45 | numeric_overlap:10/19, markers:attack |
| `monster` | [扎人的书](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432038&wiki_id=646570) | Acid Slimes | 0.0 | `low_signal` | 45 | 无 |
| `monster` | [打劫的](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421076&wiki_id=646570) | The Champ | 6.235 | `low_signal` | 45 | numeric_overlap:9/17, markers:attack |
| `monster` | [扭曲团块](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15438466&wiki_id=646570) | Taskmaster | 6.8 | `low_signal` | 45 | numeric_overlap:3/5, markers:attack |
| `monster` | [抢劫的](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421076&wiki_id=646570) | The Champ | 6.235 | `low_signal` | 45 | numeric_overlap:9/17, markers:attack |
| `monster` | [拜蛇术士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436794&wiki_id=646570) | Reptomancer | 5.692 | `low_signal` | 45 | numeric_overlap:6/13, markers:attack |
| `monster` | [收藏家](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=532023&wiki_id=646570) | The Collector | 12.267 | `weak_candidate` | 45 | numeric_overlap:8/15, markers:attack,block,strength,vulnerable |
| `monster` | [时间吞噬者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15432030&wiki_id=646570) | Bronze Automaton | 9.294 | `weak_candidate` | 45 | numeric_overlap:7/17, markers:attack,block,strength |
| `monster` | [百夫长](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436697&wiki_id=646570) | Acid Slimes | 0.0 | `low_signal` | 45 | 无 |
| `monster` | [真菌兽](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15420669&wiki_id=646570) | Chosen | 2.0 | `low_signal` | 45 | markers:vulnerable |
| `monster` | [神秘术士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436699&wiki_id=646570) | Cultist | 2.0 | `low_signal` | 45 | numeric_overlap:1/4 |
| `monster` | [第一勇士](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421632&wiki_id=646570) | The Champ | 15.333 | `weak_candidate` | 45 | numeric_overlap:14/21, markers:attack,block,strength,vulnerable,weak |
| `monster` | [腐化之心](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408990&wiki_id=646570) | Spire Shield and Spire Spear | 6.857 | `low_signal` | 45 | numeric_overlap:5/14, markers:attack,strength |
| `monster` | [虱虫](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411825&wiki_id=646570) | Looter | 1.0 | `low_signal` | 45 | numeric_overlap:1/8 |
| `monster` | [蛇花](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15436704&wiki_id=646570) | Acid Slimes | 5.5 | `low_signal` | 45 | numeric_overlap:7/16, markers:attack |
| `monster` | [被拣选者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408980&wiki_id=646570) | Acid Slimes | 0.0 | `low_signal` | 45 | 无 |
| `monster` | [觉醒者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9957006&wiki_id=646570) | The Champ | 8.0 | `weak_candidate` | 45 | numeric_overlap:8/16, markers:attack,strength |
| `monster` | [邪教徒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408976&wiki_id=646570) | Cultist | 4.0 | `low_signal` | 45 | numeric_overlap:1/4, markers:attack |
| `monster` | [酸液史莱姆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411814&wiki_id=646570) | Cultist | 4.0 | `low_signal` | 45 | numeric_overlap:2/4 |
| `monster` | [铜制机械人偶](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15421630&wiki_id=646570) | Bronze Automaton | 12.0 | `weak_candidate` | 45 | numeric_overlap:9/12, markers:attack,block,strength |
| `monster` | [高塔之盾/高塔之矛](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9959050&wiki_id=646570) | Spire Shield and Spire Spear | 9.467 | `weak_candidate` | 45 | numeric_overlap:14/15, markers:attack |
| `status` | [下回合格挡](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454362&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [不能抽牌](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454371&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [中毒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501550&wiki_id=646570) | Poison | 10.0 | `weak_candidate` | 134 | numeric_overlap:2/2, markers:poison |
| `status` | [乱战（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454327&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [人工制品](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460430&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [以手拒之（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460336&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [仪式](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460521&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:strength |
| `status` | [余像（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411811&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [你好](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448765&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [修理](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454301&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [偏差](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454375&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [先见之明（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15445492&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [免费攻击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448750&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [再生](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454295&wiki_id=646570) | Plated Armor | 8.0 | `weak_candidate` | 134 | numeric_overlap:2/2 |
| `status` | [再生（敌人）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460312&wiki_id=646570) | Artifact | 2.0 | `low_signal` | 134 | numeric_overlap:1/4 |
| `status` | [凌迟（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454315&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [凝滞](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460322&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [分裂](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460316&wiki_id=646570) | Vulnerable | 4.0 | `low_signal` | 134 | numeric_overlap:1/2 |
| `status` | [创造性AI（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447015&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [力量提升](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460325&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:strength |
| `status` | [力量（负）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460523&wiki_id=646570) | Strength | 12.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack,strength |
| `status` | [势不可当（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448770&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [勒脖（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460339&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [印记](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460347&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [双倍伤害](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447026&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [双发（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447030&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [变幻](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460304&wiki_id=646570) | Strength | 2.0 | `low_signal` | 134 | markers:strength |
| `status` | [后方攻击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460282&wiki_id=646570) | Vulnerable | 6.0 | `low_signal` | 134 | numeric_overlap:1/2, markers:attack |
| `status` | [回响形态（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447032&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [均衡（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448325&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [坚不可摧](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460306&wiki_id=646570) | Artifact | 2.0 | `low_signal` | 134 | numeric_overlap:1/4 |
| `status` | [增幅](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15411810&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [壁垒（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460434&wiki_id=646570) | Dexterity | 2.0 | `low_signal` | 134 | markers:block |
| `status` | [复制](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447028&wiki_id=646570) | Artifact | 4.0 | `low_signal` | 134 | numeric_overlap:1/2 |
| `status` | [多重护甲](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460436&wiki_id=646570) | Plated Armor | 12.0 | `weak_candidate` | 134 | numeric_overlap:2/2, markers:attack,block |
| `status` | [夜魇（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454275&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [天人](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447024&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [夹击](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454337&wiki_id=646570) | Vulnerable | 6.0 | `low_signal` | 134 | numeric_overlap:1/2, markers:attack |
| `status` | [好奇](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460286&wiki_id=646570) | Plated Armor | 4.0 | `low_signal` | 134 | numeric_overlap:2/4 |
| `status` | [如水（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448772&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [孢子云](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460318&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [尸爆术（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460345&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [幻影（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454284&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [幽魂形态（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454392&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [弹回（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454297&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [形态转换](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460310&wiki_id=646570) | Plated Armor | 3.333 | `low_signal` | 134 | numeric_overlap:1/6, markers:attack |
| `status` | [循环（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448774&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [心灵堡垒（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454270&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [必备工具（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454321&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [恶魔形态（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447019&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:strength |
| `status` | [愤怒（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=2939938&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [战歌（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15445488&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [扭动](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460333&wiki_id=646570) | Plated Armor | 2.0 | `low_signal` | 134 | markers:attack |
| `status` | [抽牌](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454356&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [抽牌减少](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454381&wiki_id=646570) | Plated Armor | 8.0 | `weak_candidate` | 134 | numeric_overlap:2/2 |
| `status` | [摆手（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454323&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [撕裂（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454310&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:strength |
| `status` | [操控现实（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454256&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [收集（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15445494&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [敏捷](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501537&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [敏捷(负)](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454365&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [敏捷下降](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454369&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [散热](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448761&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [斋戒（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454383&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [无实体](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501541&wiki_id=646570) | Plated Armor | 10.0 | `weak_candidate` | 134 | numeric_overlap:2/2, markers:attack |
| `status` | [无惧疼痛（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448741&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [无法格挡](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454385&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [无限刀刃（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448768&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [时间扭曲](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460327&wiki_id=646570) | Strength | 4.667 | `low_signal` | 134 | numeric_overlap:1/3, markers:strength |
| `status` | [易伤](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501549&wiki_id=646570) | Vulnerable | 10.0 | `weak_candidate` | 134 | numeric_overlap:2/2, markers:attack |
| `status` | [未觉醒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460329&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [机器学习（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448778&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [柔韧](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460302&wiki_id=646570) | Plated Armor | 12.0 | `weak_candidate` | 134 | numeric_overlap:2/2, markers:attack,block |
| `status` | [欧米伽（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454287&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [死亡律动](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460284&wiki_id=646570) | Plated Armor | 6.0 | `low_signal` | 134 | numeric_overlap:2/4, markers:attack |
| `status` | [残影（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15445490&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [残暴（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15446603&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [残虐](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454303&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [毒雾（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454282&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [活力](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454360&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [活动肌肉（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454396&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:strength |
| `status` | [涂毒（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447514&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [涅槃（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454279&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [消逝](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460298&wiki_id=646570) | Artifact | 2.0 | `low_signal` | 134 | numeric_overlap:1/4 |
| `status` | [混乱](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9960358&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [渎神者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15445485&wiki_id=646570) | Plated Armor | 2.667 | `low_signal` | 134 | numeric_overlap:1/3 |
| `status` | [激怒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460294&wiki_id=646570) | Strength | 4.0 | `low_signal` | 134 | numeric_overlap:1/4, markers:strength |
| `status` | [火焰吐息（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448745&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [火焰屏障（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448748&wiki_id=646570) | Strength | 12.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack,strength |
| `status` | [炸弹（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454313&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [爆发（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447009&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [爪牙](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460308&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [狂暴（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15445079&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [猛虎下山（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454299&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [生命链接](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460296&wiki_id=646570) | Vulnerable | 4.0 | `low_signal` | 134 | numeric_overlap:1/2 |
| `status` | [生气](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454397&wiki_id=646570) | Plated Armor | 6.0 | `low_signal` | 134 | numeric_overlap:2/4, markers:attack |
| `status` | [电动力学（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448326&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [疼痛戳刺](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460331&wiki_id=646570) | Plated Armor | 2.0 | `low_signal` | 134 | markers:attack |
| `status` | [盗窃](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460320&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [真言](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9960352&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [研习（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454311&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [确立基础（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448733&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [磁力（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448780&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [神气制胜（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454293&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [精准（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15440705&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [缓冲（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454354&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [缓慢](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460337&wiki_id=646570) | Plated Armor | 2.0 | `low_signal` | 134 | markers:attack |
| `status` | [缠绕](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454373&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [缠身](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454379&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [能量提升](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454358&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [脆弱](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501539&wiki_id=646570) | Weak | 8.0 | `weak_candidate` | 134 | numeric_overlap:2/2 |
| `status` | [腐化（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447013&wiki_id=646570) | Accuracy | 0.0 | `low_signal` | 134 | 无 |
| `status` | [自燃（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447011&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [自爆](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460300&wiki_id=646570) | Plated Armor | 4.667 | `low_signal` | 134 | numeric_overlap:1/3, markers:attack |
| `status` | [荆棘](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9532569&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [虔信（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447021&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [虚弱](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=501547&wiki_id=646570) | Weak | 10.0 | `weak_candidate` | 134 | numeric_overlap:2/2, markers:attack |
| `status` | [蜷身](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460290&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [计划妥当（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454325&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [跟踪锁定](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460341&wiki_id=646570) | Vulnerable | 10.0 | `weak_candidate` | 134 | numeric_overlap:2/2, markers:attack |
| `status` | [进化（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15448737&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [邪咒](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454390&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [金属化](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9534071&wiki_id=646570) | Dexterity | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:block |
| `status` | [钢笔尖（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454289&wiki_id=646570) | Plated Armor | 2.0 | `low_signal` | 134 | markers:attack |
| `status` | [锋利外甲](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460314&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [镣铐](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460343&wiki_id=646570) | Strength | 6.0 | `low_signal` | 134 | numeric_overlap:1/2, markers:strength |
| `status` | [集中](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9960350&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [集中(负)](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454367&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [雷暴（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454305&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
| `status` | [静电释放（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15454307&wiki_id=646570) | Strength | 10.0 | `weak_candidate` | 134 | numeric_overlap:1/1, markers:attack |
| `status` | [飞行](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15460288&wiki_id=646570) | Vulnerable | 5.2 | `low_signal` | 134 | numeric_overlap:2/5, markers:attack |
| `status` | [黑暗之拥（能力）](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15447017&wiki_id=646570) | Artifact | 8.0 | `weak_candidate` | 134 | numeric_overlap:1/1 |
