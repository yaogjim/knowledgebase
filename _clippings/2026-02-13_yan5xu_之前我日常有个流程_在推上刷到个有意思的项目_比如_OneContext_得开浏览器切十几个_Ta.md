---
title: "2026-02-13_yan5xu_之前我日常有个流程_在推上刷到个有意思的项目_比如_OneContext_得开浏览器切十几个_Ta"
source: "https://x.com/yan5xu/status/2021040717477601524"
author:
  - "[[@yan5xu]]"
published: 2026-02-13
created: 2026-02-13
description:
tags:
  - "x"
  - "@yan5xu"
  - "https"
  - "2026-02-10"
---

# 之前我日常有个流程：在推上刷到个有意思的项目（比如 OneContext），得开浏览器切十几个 Ta

**yan5xu** @yan5xu [2026-02-10](https://x.com/yan5xu/status/2021040717477601524)

之前我日常有个流程：在推上刷到个有意思的项目（比如 OneContext），得开浏览器切十几个 Tab 搜评价、翻源码，最后还要手动切到 Note 做记录，或者发微信提醒自己。

这套逻辑在 PC 上勉强能跑，在手机上就是灾难。App 频繁切换导致心智加载极慢，且手机端缺乏拉源码、深度审计的工程环境，思路经常在这些低效操作里被打断。

在 Epiral 或者类似 openclaw 架构下，这个流程被彻底重构了：

现在不用我主动去刷噪音，Agent 每小时会自动巡检多维信源，把脱水后的增量推送给我。我在手机上发现目标，只需要丢一句「对 XX 开启深度调研」，剩下的就交给后台。

Agent 会开启一个独立 Topic，在配置好的浏览器里静默抓取，并行执行源码审计、对冲观点、生成对标分析。我甚至不需要保持手机在线。

最核心的价值是「研究即记录」。以前调研完还得搬运到笔记里，现在所有调研轨迹和结论天然就沉淀成了系统的长期资产。

这本质上是把执行权剥离给了后台 OS，手机从一个低效的生产工具，变成了纯粹的指挥入口。这种跨设备心智的一致性，才叫 Agentic 工作流。

![Image](https://pbs.twimg.com/media/HAwtzGjaAAMlVGw?format=jpg&name=large)

* * *

**LotusDecoder** @LotusDecoder [2026-02-10](https://x.com/LotusDecoder/status/2021069105181360567)

🤯🤯🤯

* * *

**flyisland** @flyisland [2026-02-10](https://x.com/flyisland/status/2021043612650557672)

赞「研究即记录」，这也是我打算做的！期待能分享你的OpenClaw配置

* * *

**yan5xu** @yan5xu [2026-02-10](https://x.com/yan5xu/status/2021065176511021394)

😂我这个是自己搓的 agent 不是 openclaw

* * *

**Pirate Code** @Code2Pirate [2026-02-11](https://x.com/Code2Pirate/status/2021505420674859118)

大佬，基于 pi agent 二开的嘛？ 额外加了哪些东西呢

* * *

**Hannah | atypica.ai** @hannah\_builds [2026-02-10](https://x.com/hannah_builds/status/2021176800424919415)

研究即记录”这个概括太精准了！把手机从低效工具变成指挥入口，这才是 Agentic 工作流的终极形态啊 🤯 刚才私信您了个合作邀约，辛苦看看~