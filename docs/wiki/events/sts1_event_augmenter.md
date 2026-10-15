# 增益研究者 / Augmenter

> 稳定 ID：`sts1.event.augmenter`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：增益研究者
- English: Augmenter

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Test J.A.X. |  | {"text": "Get JAXXED. * Adds J.A.X. to the player's deck."} |
| 2 | Become Test Subject |  | {"text": "Transform] 2 cards. * Read more on Transform rules here]."} |
| 3 | Ingest Mutagens |  | {"text": "Obtain a special relic. * Rewards the player with Mutagenic Strength."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Test J.A.X.", "text": "Get JAXXED. * Adds J.A.X. to the player's deck."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Become Test Subject", "text": "Transform] 2 cards. * Read more on Transform rules here]."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Ingest Mutagens", "text": "Obtain a special relic. * Rewards the player with Mutagenic Strength."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["A man with an eyepatch and a devilish grin strides up to you. NL \"Hey there, stranger. Interested in advancing science? I can make you stronger than any training or blessing. You're gonna need it if you're one of those heroes with a death wish.\" NL NL ~\"Whad'ya~ ~say?\"~", "~\"Excellent.\"~ NL The man hands over a dangerous looking syringe filled with a #b~glowing~ #b~liquid~ before skulking off into a shadowy alleyway.", "~\"Superb.\"~ NL The man injects you with three unknown substance... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["一个戴着眼罩的邪笑着的男人大摇大摆地走到你面前： NL “嘿陌生人，想不想试试高端的科技？ 可会让你变得比任何训练和祝福都要强哦。 如果你是那种一心求死的英雄的话可不能没有它呢。 NL 你说怎么样？ 想不想试一下？” ", "~“太好了。”~ NL 男人递给你一个看起来很危险的装着 #b~发光液体~ 的针筒，自己又鬼鬼祟祟地走进一条阴暗的小巷子里。", "~“太棒了。”~ NL 他对你注射了三管不知什么液体，然后拿出一本笔记本。你觉得自己开始有点飘飘忽忽的，他则开始飞快地开始了笔记。  NL 你不记得过了多久，但当你恢复意识的时候，那个可疑的家伙已经不见了。", "~“太妙了。”~ NL 你喝下了神秘的液体，立即就觉得自己充满了活力，仿佛全身的肌肉纤维都开始 @抖动@ 了起来！"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Test J.A.X.] #gGet #gJAXXED.", "[Become Test Subject] #gTransform #g2 #gcards.", "[Ingest Mutagens] #gObtain #ga #gspecial #grelic.", "[Leave]", "[Locked] Requires: 2 or more cards in deck.", "Select Cards to Transform."] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[试一下J.A.X.] #g来点猛药。", "[当一下实验对象] #g选择2张牌进行变化。", "[喝一下突变剂] #g获得一件特殊遗物。", "[离开]", "[锁定] 需要：牌组中至少有2张牌。", "选择要变化的牌。"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Augmenter | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 增益研究者 | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Drug Dealer", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>一个戴着眼罩的邪笑着的男人大摇大摆地走到你面前：“嘿陌生人，想不想试试高端的科技吗？ 可会让你变得比任何训练和祝福都要强哦。 如果你是那种一心求死的英雄的话可不能没有它呢。你说怎么样？ 想不想来试一下？”<br>选项<br>来点猛药 获得 无色牌-J.A.X.“好极了。”男人递给你一个看起来很危险的装着发光液体的针筒，自己又鬼鬼祟祟地走进一条阴暗的小巷子里。<br>当一下实验对象 选择两张牌进行变化“太棒了。”男人给你注射了三管不知什么液体，然后他掏出了一本笔记本。你感觉自己有点儿飘飘忽忽，他则飞快地记起了笔记。你不记得过了多久，但是当你恢复意识时，那个可疑的人已经不见了。<br>喝下突变剂 获得 遗物- 突变之力“太妙了”<br>你喝下了神秘液体，立即就感觉自己充满了活力，感觉肌肉纤维都仿佛抖动了起来！ | `single_source` | [增益研究者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408876&wiki_id=646570) |
| `source.title_text` | 增益研究者 | `single_source` | [增益研究者](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408876&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Augmenter<br>|Image=Event-Augmenter.png<br>}} {{Small Relic Infobox|Mutagenic Strength}} {{Small Card Infobox|J.A.X.}}<br>{{E|Augmenter}} is an [[Event]] found exclusively in [[Act 2]]. This Event is the only way to obtain {{C|J.A.X.}} and {{R|Mutagenic Strength}}.<br><br>== Options ==<br>{{Frame|Test J.A.X.}} {{TS|positive||Get JAXXED.}}<br>* Adds {{C|J.A.X.}} to the player's deck.<br><br><br>{{Frame|Become Test Subject}} {{TS|positive||[[Transform]] 2 cards.}}<br>* ... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T14:55:08+00:00
