---
title: "steipete 为 AI 打造 CLI 工具库让计算机“服从”"
source: "https://x.com/_kaichen/status/2016736112669307372"
author:
  - "[[@_kaichen]]"
date: "2026-01-30T19:03:59+08:00"
created: 2026-01-30
description:
tags:
  - "@_kaichen # AI # Moltbot # Clawdbot # steipete # GitHub # CLI # 代码 # 工具 # macOS # Agent"
---
**kAI** @\_kaichen [2026-01-29](https://x.com/_kaichen/status/2016736112669307372)

从 Clawdbot/Moltbot 之父 steipete 在 GitHub 上 2025 年中开始的代码提交记录可以看到，他的所有开发都在为同一个目标服务：让 AI 真正能操控计算机（Mac）

打造 CLI 武器库

他批量开发各种命令行工具，每个工具做好一件事：

\- bird 读写 Twitter/X

\- gifgrep 搜索 GIF

\- gogcli 访问 Google Workspace 全家桶

\- summarize 把任何 URL、YouTube、播客变成摘要

这些都是给 Agent 准备的"手脚"。

他自己就是 Coding Agent 重度用户，所以顺手解决了自己的痛点：

\- VibeTunnel：把浏览器变成终端，出门在外也能远程操控 Agent

\- CodexBar：菜单栏实时显示 token 消耗——即便不差钱，也要清楚钱花在哪

\- Poltergeist：通用热重载工具，任何语言的项目都能自动重建

连接物理世界

\- 海外外卖平台有 API？那就写个 ordercli 查订单

\- 家里有摄像头？camsnap 搞定 RTSP/ONVIF 协议，截图、录像、动作检测一条龙

\- Sonos 音箱？sonoscli 实现发现、分组、队列、播放 Spotify

\- 想用语音唤醒 Mac？Brabble 本地转录，像小爱同学一样下达指令

完全控制 macOS

\- Peekaboo：不只截图，而是完整的 GUI 自动化，see、click、type、scroll、hotkey、menu，模拟人类的一切操作

\- imsg：命令行收发 iMessage/SMS

\- remindctl：操控 Apple Reminders

突破浏览器沙箱

他实现了 cookie 提取能力，让 Agent 能以用户身份直接调用任何网站的 API，绕过登录墙。

务实的技术选型

这些工具横跨多种语言：

\- Go：网络相关 CLI（gogcli、sonoscli、camsnap、bird）编译快、跨平台、无依赖

\- Swift：macOS 深度集成（Peekaboo、imsg、Brabble）系统 API 原生支持

\- TypeScript：Agent 端逻辑（Clawdbot 主体、MCP server）生态丰富、AI 友好

没有技术洁癖，哪个顺手用哪个。

终极目标，这一切都在做同一件事：打破软件厂商几十年来建立的互操作壁垒。

过去，每个 App 都是信息孤岛。你的邮件在 Gmail，日历在 Calendar，消息在 iMessage，音乐在 Sonos，摄像头在另一个 App。它们之间没有桥梁。

steipete 用几十个 CLI 工具，把这些孤岛全部打通，然后通过 统一暴露给 AI 来操作。

AI 成为编排者，说一句话，它调用 gogcli 查日历、用 Peekaboo 截图分析、通过 imsg 发消息、让 sonoscli 播放音乐。

所有这些，一气呵成。这才是 Clawdbot/Moltbot 最大价值，一整套让 AI 能操控一切的基础设施。

---

**杠哥** @solo\_lever [2026-01-29](https://x.com/solo_lever/status/2016813870560792807)

任何试图用 GUI 驯服 AI 的努力最后往往只能做出玩具。CLI 才是 AI 的母语。把工作流原子化、脚本化，才是真正的“生产力杠杆”。steipete 这条路走对了，只有抛弃鼠标，才能跟上 AI 的思考速度。

---

**kAI** @\_kaichen [2026-01-29](https://x.com/_kaichen/status/2016868692131533263)

cli 具有无限组合的可能性！

---

**MobaiLabs** @mobailabs [2026-01-29](https://x.com/mobailabs/status/2016764262203449608)

深度好文！steipete 这种从 2025 年中就开始的持续输出确实是 Moltbot 成功的基石。从提交记录看底层逻辑确实能学到很多工程化的精髓。

---

**kAI** @\_kaichen [2026-01-29](https://x.com/_kaichen/status/2016765897797750880)

他写的项目都挺有研究价值的，很有突破枷锁的黑客精神。

---

**Hiroki** @dickeylth [2026-01-29](https://x.com/dickeylth/status/2016842613157220711)

前面的不太懂，看到「突破浏览器沙箱 他实现了 cookie 提取能力，让 Agent 能以用户身份直接调用任何网站的 API，绕过登录墙。」有点绷不住了，这是浏览器插件授权开启 debugger 后就能做到的没有那么神秘，表述不太严谨。。。

---

**kAI** @\_kaichen [2026-01-29](https://x.com/_kaichen/status/2016870149463429567)

你可以看看 https://github.com/steipete/sweet-cookie… 和 https://github.com/steipete/SweetCookieKit…

都是去文件系统里捞浏览器对应网站的 Cookies，不是通过浏览器插件

通过这个方式做了 https://github.com/steipete/bird 推特命令行工具

---

**TrueWild\_77** @TrueWildXiaoQi [2026-01-29](https://x.com/TrueWildXiaoQi/status/2017014667160539630)

现在是2026年1月，这个MOLT就这么火，四个AI大模型公司还没下场做类似项目呢，我预计，如果他们出手做仿造品，有可能今年AGI就真的来了。

---

**TrueWild\_77** @TrueWildXiaoQi [2026-01-29](https://x.com/TrueWildXiaoQi/status/2017013887636558077)

看到你说，每天一觉醒来就查看AGI来了没有，果断关注，同路人。

---

**Tanker** @tanker327 [2026-01-29](https://x.com/tanker327/status/2016874322359398755)

分析得太好了，一语点醒梦中人! 谢谢

---

**TrueWild\_77** @TrueWildXiaoQi [2026-01-29](https://x.com/TrueWildXiaoQi/status/2017013438304964882)

这篇文章写的很好👍，感谢！

---

**Crazyox** @crazyox [2026-01-29](https://x.com/crazyox/status/2016775319576055961)

看到Clawdbot/Moltbot之父steipete在GitHub上的代码提交记录，感觉AI终于有希望能真正操控计算机了！

工具库开发得so棒，看了名字就感觉自己有一把武器库！

AI未来会很方便，希望它能真正帮我们做事情！

这些工具的名字像武器库，感觉AI未来能真正控制计算机了！