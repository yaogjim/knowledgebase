---
title: ""
source: "https://x.com/pradeep24/status/2021319785947316490"
author: ""
created: 2026-02-13 17:55:47
date: 2026-02-13 17:55:47
description: ""
tags: ""
---
是一个

插件，它允许你的代理浏览通常会阻止自动化的网站——X、Product Hunt、Amazon 以及更多网站。它是从

，在那里它支持我们的服务器端网页浏览。

它是一个基于

无头浏览器服务器构建的，一个在 C++ 层面而非在 JavaScript 中伪装浏览器指纹的 Firefox 分支。这使其比标准无头浏览器更有可能通过检测系统。

如果你的 OpenClaw 部署在 Mac Mini 上，内置的浏览器工具会驱动一个真实的浏览器窗口，网站会像对待普通浏览器一样正常处理它。在 VPS 或远程服务器上，你只能使用无头 Chrome 或原始 HTTP 请求——这两种方式通常都会被屏蔽。Camofox 针对远程服务器解决了这个问题，并且对于代理工作流来说，它比桌面浏览更快。

```
openclaw plugins install @askjo/camofox-browser
```

公开工具：camofox\_create\_tab、camofox\_snapshot、camofox\_click、camofox\_type、camofox\_navigate、camofox\_scroll、camofox\_screenshot。

Playwright 和 Puppeteer 在协作网站上运行良好。将它们指向 Google、Amazon 或任何由 Cloudflare 防护的网站时，请求不会被速率限制——而是直接被拒绝。

检测系统通过数百个维度对浏览器进行指纹识别，这些维度包括 WebGL 渲染器字符串、AudioContext 采样率、navigator 硬件并发数、屏幕几何参数、WebRTC IP 泄漏、电池 API 特性以及语音合成声音等。

标准解决方案是使用隐身插件：修补 navigator.webdriver、覆盖一些属性。这种方法在补丁本身成为指纹信号之前一直有效——而面对强大的检测系统时，它就会（成为指纹信号）。

根本问题： 你在 JavaScript 中重写的任何属性都可以在 JavaScript 中被检查。 属性描述符、原型链以及函数 toString() 都会暴露重写的信息。

当 JavaScript 调用导航器.硬件并发数时，它由 Firefox 中的 C++实现支持。在 JavaScript 中覆盖该属性后，网页可以检测到差异——属性描述符看起来不正确，原型不匹配，函数不是原生的。修改 C++返回路径后，JavaScript 会将伪造的值视为真实值。

> 在 Camoufox 中，数据在 C++实现层面被拦截，因此这些修改无法通过 JavaScript 检查被检测到。

camofox-browser 将该引擎封装到一个为编程用途设计的 REST API 中。

这些补丁遵循一个简单的模式：检查配置，如果设置了，则返回伪造的值，否则退回到正常实现。来自

：

```
double nsGlobalWindowInner::GetInnerWidth(ErrorResult& aError) {
  if (auto value = MaskConfig::GetDouble("window.innerWidth"))
    return value.value();
  FORWARD_TO_OUTER_OR_THROW(GetInnerWidthOuter, (aError), aError, 0);
}
```

该模式涵盖窗口几何形状、navigator 字段、屏幕详情、WebGL 参数（通过 GPU 指纹

）、WebRTC IP 伪装（

）、音频指纹、自动批准的地理位置、电池 API 以及语音合成声音。

Camoufox 还包含基于贝塞尔曲线的鼠标轨迹，这些轨迹在 MouseTrajectories.hpp 中实现 — 因为检测系统越来越多地评估你如何交互，而不仅仅是你发送的内容。

在 JavaScript 看到它之前，所有这些都在 C++中被拦截。

谷歌的一个搜索结果页面大约是 500KB 的 HTML。同一页面的可访问性树大约是 5KB。当使用者是具有上下文窗口的大型语言模型（LLM）时，这种 100 倍的缩减就很重要了。

-   无障碍快照而不是 HTML
    
-   元素引用 (e1, e2, e3) 而不是脆弱的选择器
    
-   针对常见网站的宏（@google\_search、@youtube\_search、@amazon\_search）
    

```
# Create tab, get snapshot, click by ref
curl -X POST http://localhost:9377/tabs \
  -d '{"userId": "agent1", "sessionKey": "task1", "url": "https://google.com"}'

curl "http://localhost:9377/tabs/TAB_ID/snapshot?userId=agent1"

curl -X POST http://localhost:9377/tabs/TAB_ID/click \
  -d '{"userId": "agent1", "ref": "e3"}'
```

这仍然是整个难题中最棘手的部分。大多数反机器人系统会检查你的 IP 是住宅 IP 还是数据中心 IP，而数据中心 IP 段都有完善的记录。你可以通过使用 ISP 代理或住宅代理来规避这个问题，但这是一种不稳定的基础设施操作。Camofox 在这里并不总是成功，但你的成功率比直接使用 Playwright 要高。

我们在

中解决了这个问题，通过构建一个本地的 Safari 驱动的栈——你的真实浏览器、真实 IP、真实 Cookie。它效果很好，但代价是 WebView 特有的拦截。没有万能药。

C++伪装处理浏览器身份，而非 IP 身份。大多数反机器人系统会同时关联这两者：来自 100 个 IP 的相同指纹看起来很奇怪；来自同一个 IP 的 100 个指纹也看起来很奇怪。随 IP 轮换指纹，在会话内保持稳定。Camoufox 通过环境变量按会话配置指纹，这与隔离的代理会话非常匹配。

npm install \# 或来自源 git clone https://github.com/jo-inc/camofox-browser cd camofox-browser && npm 安装 && npm 启动 curl http://localhost:9377/health

```
# Create tab, get snapshot, click by ref
curl -X POST http://localhost:9377/tabs \
  -d '{"userId": "agent1", "sessionKey": "task1", "url": "https://google.com"}'

curl "http://localhost:9377/tabs/TAB_ID/snapshot?userId=agent1"

curl -X POST http://localhost:9377/tabs/TAB_ID/click \
  -d '{"userId": "agent1", "ref": "e3"}'
```

该仓库采用 MIT 许可证授权，仍处于早期阶段——会有缺陷。欢迎贡献，如果你遇到任何问题，

。我们希望 OpenClaw 社区觉得它有用。