# 吸血鬼 / Vampires

> 稳定 ID：`sts1.event.vampires`  
> 类别：`event`；游戏：`sts1`；映射状态：`confirmed`

## 名称

- 中文：吸血鬼
- English: Vampires

## event 数据

| 字段 | 值 |
| --- | --- |
| `acts_json` | {"source_category": "Act 2"} |
| `room_type` | unknown |

### 选项

| # | 选项 | 条件/代价 | 结果 |
| ---: | --- | --- | --- |
| 1 | Offer: Blood Vial | {"text": "Lose Blood Vial"} | {"text": "Remove all Strikes. Receive 5 Bites. * Only present if the player has Blood Vial"} |
| 2 | Accept | {"text": "Lose X Max HP"} | {"text": "Remove all Strikes. Receive 5 Bites. . * X is equal to 30% of the player's max HP"} |
| 3 | Refuse |  | {"text": "Nothing happens. You are then given the option to"} |
| 4 | Leave |  | {"text": "."} |

## 相关条目

暂无已确认关系。

## 被哪些条目引用

暂无已确认关系。

## 来源与核对状态

字段级证据保留在 SQLite 的 `claims` 表；这里显示已采集的摘要。

| 字段 | 值 | 状态 | 来源 |
| --- | --- | --- | --- |
| `event.option.1` | {"label": "Offer: Blood Vial", "text": "Remove all Strikes. Receive 5 Bites. * Only present if the player has Blood Vial"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.2` | {"label": "Accept", "text": "Remove all Strikes. Receive 5 Bites. . * X is equal to 30% of the player's max HP"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.3` | {"label": "Refuse", "text": "Nothing happens. You are then given the option to"} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `event.option.4` | {"label": "Leave", "text": "."} | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |
| `game.event.descriptions` | ["Navigating an unlit street, you come across several hooded figures in the midst of some dark ritual. As you approach, they turn to you in eerie unison. The tallest among them bares fanged teeth and extends a long, pale hand towards you. NL ~\"Join~ ~us~ ~brother,~ ~and~ ~feel~ ~the~ ~warmth~ ~of~ ~the~ ~Spire.\"~", "Navigating an unlit street, you come across several hooded figures in the midst of some dark ritual. As you approach, they turn to you in eerie unison. The tallest among them ba... | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.descriptions` | ["在一条昏暗的街上，你遇见几个戴着兜帽的人在进行某种黑暗的仪式。当你靠近时，他们全都同时转身面对你，让你觉得十分诡异。 其中个子最高的一个微微一笑，露出了长长的尖牙，向你伸出了一只苍白而瘦长的手： NL ~“加入我们，兄弟。一起来感受高塔的温暖吧。”~", "在一条昏暗的街上，你遇见几个戴着兜帽的人在进行某种黑暗的仪式。当你靠近时，他们全都同时转身面对你，让你觉得十分诡异。 其中个子最高的一个微微一笑，露出了长长的尖牙，向你伸出了一只苍白而瘦长的手： NL ~“加入我们，姐妹。一起来感受高塔的温暖吧。”~", "高个男人抓住你的手臂将你拉了过去，他的尖牙咬进你的脖子，你感觉到一股 @黑暗的力量@ 涌入你的脖子，在你的全身 @流淌@ 。NL …… NL 不知过了多久，你醒了过来，身边空无一人。你感觉到腹中传来一阵强烈的 ~饥渴~ 。 你 #r必须进食……", "你后退一步，举起自己的武器表示警告。高个男人叹了一口气：“好吧。” 那群戴着兜帽的人就这样变化成了一团浓浓的黑雾，从你的身边飘了过去。 NL 你又是独自一人了。", "当你取出 #y小血瓶 时，那些苍白的人们震惊地倒抽了一... | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.event.options` | ["[Accept] #gRemove #gall Strikes. #gReceive #g5 Bites. #rLose #r", " #rMax #rHP.", "[Refuse]", "[Lose ", "] #gRemove #gall Strikes. #gReceive #g5 Bites.", "[Leave]"] | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.event.options` | ["[接受] #g移除所有 打击 #g牌。 #g获得5张 噬咬 #g牌。 #r失去 #r", " #r最大生命。", "[拒绝]", "[失去 ", "] #g移除所有 打击 #g牌。 #g获得5张 噬咬 #g牌。", "[离开]"] | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization.name` | Vampires(?) | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `game.localization.name` | 吸血鬼（？） | `verified_game` | [Game localization zhs/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/zhs/events.json) |
| `game.localization_key` | {"jar_sha256": "cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673", "key": "Vampires", "kind": "event", "steam_build_id": "10180494"} | `verified_game` | [Game localization eng/events.json](game://desktop-1.0.jar/cfad868ac8d65a88e71a0bf096fb09f78811e553effe0787c5309a655e081673/localization/eng/events.json) |
| `source.article_text` | （图片未提供文字说明）<br>描述<br>在一条昏暗的街上，你遇见几个戴着兜帽的人在进行某种黑暗的仪式。当你靠近时，他们全都同时转身面对你，让你觉得十分诡异。 其中个子最高的一个微微一笑，露出了长长的尖牙，向你伸出了一只苍白而瘦长的手：“加入我们，兄弟/姐妹/破碎的存在/姐妹。一起来感受高塔的温暖吧。”<br>选项<br>接受 移除所有打击牌。获得 5 张噬咬牌。失去 30% 最大生命。高个男人抓住你的手臂将你拉了过去，他的尖牙咬进你的脖子，你感觉到一股黑暗的力量涌入你的脖子，在你的全身流淌。……不知过了多久，你醒了过来，身边空无一人。你感觉到腹中传来一阵强烈的饥渴 。 你必须进食……<br>失去 小血瓶 移除所有打击牌。获得 5 张噬咬牌。当你取出小血瓶时，那些苍白的人们震惊地倒抽了一口凉气。“主人的血……主人的血！主 人 的 血！！”他们疯狂地开始反复念着这句话，而高个子男人在你面前深深地鞠了一躬：“喝下他的血，与他成为一体吧。”喊声越来越响，你喝下了小血瓶中的血液。 你的视线瞬间扭曲并很快成为了黑暗。不知过了多久，你醒了过来，身边空无一人。你感觉到腹中传来一阵强烈的饥渴。 ... | `single_source` | [吸血鬼](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408899&wiki_id=646570) |
| `source.title_text` | 吸血鬼 | `single_source` | [吸血鬼](https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=15408899&wiki_id=646570) |
| `source.wikitext` | {{Event Infobox<br>|Name=Vampires<br>|Image=Event-Vampires.png<br>}} {{Small Card Infobox|Bite}} {{Small Relic Infobox|Blood Vial}}<br>{{E|Vampires}} is an [[Event]] found exclusively in [[Act 2]].<br><br>== Options ==<br>{{Frame|Offer: Blood Vial}} {{TS|negative||Lose}} {{R|Blood Vial}}{{TS|negative||.}} <span class="positive-text"> Remove all</span> {{C|Strike (Ironclad)|Strikes}}{{TS|positive||.}} <span class="positive-text">Receive 5</span> {{C|Bite|Bites}}{{TS|positive||.}}<br>* Only pre... | `single_source` | [P3 wiki.gg API batch: event 2](https://slaythespire.wiki.gg/api.php?action=query&format=json&formatversion=1&titles=Old_Beggar|Golden_Idol_(Event)|Augmenter|Designer_In-Spire|Transmogrifier|Secret_Portal|Forgotten_Altar|The_Woman_in_Blue|The_Divine_Fountain|Tomb_of_Lord_Red_Mask|Upgrade_Shrine|Vampires|Falling|The_Nest|Council_of_Ghosts|The_Colosseum|Golden_Shrine|The_Joust|The_Library|Bonfire_Spirits&prop=revisions&rvprop=content|ids&rvslots=main) |

页面生成时间：2026-09-18T11:10:21+00:00
