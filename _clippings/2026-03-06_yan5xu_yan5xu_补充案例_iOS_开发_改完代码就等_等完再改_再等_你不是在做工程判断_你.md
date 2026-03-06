---
title: "2026-03-06_yan5xu_yan5xu_补充案例_iOS_开发_改完代码就等_等完再改_再等_你不是在做工程判断_你"
source: "https://x.com/yan5xu/status/2029804807595380821"
author:
  - "[[@yan5xu]]"
published: 2026-03-06
created: 2026-03-06
description:
tags:
  - "x"
  - "@yan5xu"
  - "ios"
  - "claude"
---

# yan5xu 补充案例 iOS 开发：改完代码就等，等完再改，再等 你不是在做工程判断——你

**yan5xu**

补充案例 iOS 开发：改完代码就等，等完再改，再等

你不是在做工程判断——你是在当 Xcode 和 CI 之间的人肉轮询器。改一行代码，Cmd+U 等 3 分钟编译，盯着进度条看测试跑完，红了点进去翻失败原因，切到 CI 网页再翻一遍日志，切到 Crashlytics 看崩溃堆栈。

真正写代码可能只占你 30% 的时间，剩下 70% 你在等、在翻、在来回切换窗口搬运信息。

发版前的回归更绝——打开模拟器，手动点 20 分钟核心流程，祈祷别出 bug。

Agent 介入之后

Claude Code 跑在你的 Mac 上，跟你用同一套开发环境。核心是两个工具：

idb（Meta 开源，iOS 自动化 CLI）——管模拟器、装 App、操作 GUI、跑测试、截图 gemini-vision——截图后"看懂"界面，验证布局、文字、图片是否正常 你改完一个网络层的 bug，保存文件，随手说一句"跑一下相关测试"。

它先看你改了哪些文件，发现改了 NetworkService.swift，知道关联的测试是 NetworkTests，不跑全量，只跑相关的。你继续写下一个功能。两分钟后它告诉你：

"14 个 pass，2 个 fail。testTokenRefresh 失败：你改了请求头格式但 mock 里的 expected header 没同步更新。要我改？"

你说"改"。它更新 mock，再跑一遍，全绿，帮你提交。

发版回归更爽。 你说"跑一遍回归"，去倒杯咖啡。

它用 idb 接管整个流程——启动干净模拟器，装最新编译的 App，然后像人一样操作：读取界面上所有元素的位置，点登录，输账号，一步步走完登录→首页→搜索→加购→下单→支付。每一步操作后截图，用 gemini-vision 验收：

"登录页正常，首页商品列表渲染完整，下单页价格和地址显示正确，支付页可用。"

传统 XCUITest 只能验证"元素存不存在"，这套能验证"界面看起来对不对"——文字截断、布局错位这些人眼才能发现的问题，现在也能捕获。而且不需要提前写测试代码。

跑完它告诉你：

"8 条核心流程全部通过。第 5 条'下单流程'比上个版本慢了 1.2 秒，建议排查。"

Crash 日志丢进去，秒出结论：

"崩溃在 CartViewController.swift:142，强解包了一个 nil 的 selectedItem。从后台回来时被释放了。建议改成 guard let。要我改？"

怎么搭

\# idb（Meta 出品的 iOS 自动化 CLI） brew install idb-companion pip install fb-idb idb list-targets # 验证：能看到可用模拟器 然后在 iOS 项目根目录创建 CLAUDE.md，告诉 Agent 四件事： 项目结构（workspace、scheme、测试 target） 文件和测试的映射关系（改了哪个文件跑哪个测试） 回归测试的核心流程步骤

commit message 规范 cd ~/your-ios-project claude # "跑一下相关测试" # "跑一遍回归" # "帮我看看这个 crash" 每天省下的不只是 1-2 小时，是被反复打断的专注力。 你可以连续写两小时代码不中断——因为有人替你盯着。 它还会越来越好。 每次你指定"这次改动跑这些测试"，它会建议更新映射表。几周后它越来越精准地知道该跑哪些测试。每次回归走过的 idb 操作序列，会固化成 CLAUDE.md 里的标准流程。下次回归直接按流程走，不需要重新探索界面。

* * *

### 热门回复

**@David Protein** ♥ 45 · 💬 8

David designs tools to increase muscle and decrease fat. At 75% calories from protein, David delivers the highest protein-to-calorie ratio of any leading bar on the market

**@yan5xu** ♥ 12 · 💬 0

补充案例 一个人扛海外运营，跨时区 24 小时响应 你不是在做运营，你是在当一个跨时区的人肉路由器——凌晨 3 点欧洲客户发的邮件要等你早上 9 点起来才能转，而他已经在等了 6 小时。你的瓶颈不是能力，是你的生物钟。 你现在怎么处理的 客户消息这条线：早上起来打开 Gmail 和

**@青云** ♥ 0 · 💬 0

最近在学习 iOS 开发，谢谢分享经验(^^)