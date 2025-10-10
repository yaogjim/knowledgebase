---
title: "Browser Use v0.6.0：直接基于 CDP 运行"
source: "https://x.com/gregpr07/status/1957861004173512875"
author:
  - "[[@gregpr07]]"
published: 2025-08-20
created: 2025-08-20
description:
tags:
  - "@gregpr07 #BrowserUse #CDP #自动化 #网络自动化 #浏览器自动化"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**Gregor Zunic** @gregpr07 [2025-08-19](https://x.com/gregpr07/status/1957861004173512875)

  
Browser Use 0.6.0 不再基于 Playwright 运行 😮

我们发布了一个直接基于 CDP（Chrome DevTools 协议）的 Browser Use 新版本。

欢迎来到网络自动化的新时代。

新的 @browser\_use 是

🥷 更难被检测到（无 Playwright 泄漏）

⚡ 更快

🎯 性能更强

😮 无需 WebDriver（这是个愚蠢的要求，Playwright）

技术博客即将发布，解释我们为何这样做 👀

去试试吧 ↓

![Image](https://pbs.twimg.com/media/Gyu0xF0acAIE-ro?format=jpg&name=large)

---

**Gregor Zunic** @gregpr07 [2025-08-19](https://x.com/gregpr07/status/1957861006606016565)

---

**Lyes** @Chikor\_Zi [2025-08-19](https://x.com/Chikor_Zi/status/1957941293977391422)

  
1 - 仍然可被检测到，因为机器人检测系统追踪的是 CDP 运行时和工件，而非 Playwright。

2 - 实际上，原生 CDP 和 Playwright 之间只有个位数毫秒的差异。

3 - 你在 2 中提到了那个

4 - 你之前就可以修复那个问题，但现在你有了 CDP 工件。

你

---

**Gregor Zunic** @gregpr07 [2025-08-19](https://x.com/gregpr07/status/1957943802708258997)

  
祝 CDP 性能提升 10 倍一切顺利！

---

**Kartoon Studios** @KartoonStudios

  
卡通工作室 2025 年第二季度收益发布！

---

**TadasG** @tadasged6 [2025-08-19](https://x.com/tadasged6/status/1957862119472332983)

  
嗯……我不知道实现自己的 Chrome DevTools 协议是不是个好主意，有些地方很粗糙

使用类似 Nodriver 下载器的工具可能是个更好的选择