---
title: "2025-12-29_idoubicc_分享一个很棒的开源项目_Antigravity_Tools_这是一个把_Antigravity_里面"
source: "https://x.com/idoubicc/status/2004848130693759213"
author:
  - "[[@idoubicc]]"
published: 2025-12-29
created: 2025-12-29
description:
tags:
  - "x"
  - "@idoubicc"
  - "https"
  - "antigravity"
---

# 分享一个很棒的开源项目：Antigravity Tools 这是一个把 Antigravity 里面

**idoubi** @idoubicc [2025-12-27](https://x.com/idoubicc/status/2004848130693759213)

分享一个很棒的开源项目：Antigravity Tools

这是一个把 Antigravity 里面的模型转成标准 API，给 Claude Code 等 Coding Agent 接入的智能代理项目。提供多账号管理、协议转换和智能请求调度等功能，让你能稳定、低成本地在 Claude Code、Codex 中使用 gemini / claude 系列模型。

如何使用？

1\. 访问 Antigravity Tools 代码仓库，按照指示安装 Antigravity Tools 桌面软件

2\. 在 Antigravity Tools 桌面软件添加账号，打开浏览器通过谷歌账号登录 Antigravity

3\. 在终端配置环境变量，让 Claude Code 使用自定义的 API 端点

export ANTHROPIC\_API\_KEY="sk-xxx"

export ANTHROPIC\_BASE\_URL="http://127.0.0.1:8045"

导出 ANTHROPIC\_API\_KEY="sk-xxx"

导出 ANTHROPIC\_BASE\_URL="http://127.0.0.1:8045"

4\. 打开 Claude Code 发送指令，开始使用 CC

有哪些限制？

在 Antigravity Tools 里可以添加多个 Google 账号，每个账号都有一定的 Antigravity 模型额度，如果额度不够了，可以点击切换账号，智能切换到额度足够的账号。

可以为你添加的账号升级 Antigravity 高级套餐，获得更高的额度，既能在 Antigravity 编辑器使用，也能在 Claude Code、Codex 使用，相当于一次充值，同时分配给多个编程智能体用。

可以用哪些模型？

Antigravity 免费账号主要支持的是 gemini / claude 系列模型，不支持 gpt 模型，如果在 Codex 接入，需要加一个模型映射，比如把 gpt-5-codex 映射到 gemini-3-pro-high

这个项目目前只提供桌面版软件，不支持 Web 应用，不能通过服务器部署做 API 中转站，仅供自己在本地使用，一定程度降低了对 Claude、ChatGPT 的账号依赖，仅需一个 Google 账号，即可使用 Antigravity、Claude Code、Codex、Gemini Cli 等编程智能体。

有兴趣的可以试试。👇

![Image](https://pbs.twimg.com/media/G9KmrpWbwAAZamk?format=jpg&name=large)

* * *

**idoubi** @idoubicc [2025-12-27](https://x.com/idoubicc/status/2004848269332193553)

项目地址 👇

* * *

**吕立青\_JimmyLv 2𐃏25** @Jimmy\_JingLv [2025-12-27](https://x.com/Jimmy_JingLv/status/2004924039287242976)

CC 调度 Gemini 模型还是用里面的 Claude 模型， 哈哈哈哈

* * *

**CrowdHealth** @JoinCrowdHealth

Healthcare costs are going down at CrowdHealth.

2025 Year End Results:

Single < 55 paid $1,685 ($140.42 per month) vs $1,940 ($161.67 per month) in 2024. DOWN 13%

Family of 4 paid $5,715 ($476.25 per month) vs $6,420 ($535 per month) in 2024. DOWN 11%

Singled 55+ paid $2,710

CrowdHealth 的医疗费用正在下降。

2025年年终业绩：

Single <55 支付了1,685美元（每月140.42美元），而2024年为1,940美元（每月161.67美元）。下降13%

一家四口2024年支付了5,715美元(每月476.25美元)，对比2024年的6,420美元(每月535美元)，下降了11%

55+人支付了2710美元

* * *

**黑眼圈** @i\_m\_m\_ [2025-12-27](https://x.com/i_m_m_/status/2004918987415801930)

Antigravity Tools 真不错

* * *

**UTM Grabber** @UTMGrabber [2025-12-27](https://x.com/UTMGrabber/status/2004855128390562058)

看起来是个很实用的项目！多账号管理和智能请求调度确实能大大提升使用效率，期待更多类似工具帮助开发者优化工作流程。💡

* * *

**Cactus 𝕏** @erbanku [2025-12-27](https://x.com/erbanku/status/2004909626836595106)

不是滥用就是在滥用的路上，真佩服😄

* * *

**marovole** @marovole [2025-12-27](https://x.com/marovole/status/2004938819016294507)

昨天用上的，对 Droid 支持有问题，自己 fork 了一个改了下在用

* * *

**vewin** @lawgpts [2025-12-28](https://x.com/lawgpts/status/2005139526390546747)

我自己参照老外的开源仓库也手搓了一个自己用，还是不敢放开瞎用，免得付费账号被炸了。不过这个好的一点是后端rust效率比较高。

* * *

**ZenJoy** @ZestBodhi [2025-12-28](https://x.com/ZestBodhi/status/2005119280539685114)

这工具我用了快一周月，反代 Claude Code 确实丝滑，Proxifier 代理进程后不用开 TUN，网络干净多了，编码效率直接起飞。关键点是账号得轮着来，别一天刷爆，Google 风控现在敏感得很，我备了四个号节奏控制好，目前零掉号，够重度用了🤭

* * *

**JH.** @JHVeryyellow [2025-12-29](https://x.com/JHVeryyellow/status/2005439749868400998)

This is a game changer for local AI workflows

这对本地 AI 工作流来说简直是个游戏规则改变者

* * *

**壹零柒叁** @yshc2011 [2025-12-28](https://x.com/yshc2011/status/2005285712342782147)

这个与 CLIProxyAPI项目相比有什么区别呢？

* * *

**Midnight** @MidnightNtwrk

Bybit will support NIGHT 🕛

As one of the fastest-growing global exchanges, @Bybit\_Official will help expand access for users looking to participate in the Midnight network.

This support helps introduce NIGHT and advances the mission of bringing rational privacy to Web3.

Bybit 将支持 NIGHT 🕛

作为全球增长最快的交易所之一，@Bybit\_Official 将帮助希望参与 Midnight 网络的用户扩大参与渠道。

这项支持有助于推广 NIGHT，并推进将理性隐私带入 Web3 的使命。

* * *

**不二边浪** @laughing0622 [2025-12-27](https://x.com/laughing0622/status/2004925543821836690)

我着新手都用起来了

* * *

**zac** @zac3fire [2025-12-28](https://x.com/zac3fire/status/2005176141867561128)

用上了

* * *

**金正恩** @VladimirPeng [2025-12-27](https://x.com/VladimirPeng/status/2004939296999199095)

我的Antigravity正常用都被封了一个号了，你还敢这么玩。

* * *

**币圈小新(互fo)** @kukuyidui [2025-12-28](https://x.com/kukuyidui/status/2005187687570080230)

手动点赞

* * *

**M.Zhou** @keenjack [2025-12-28](https://x.com/keenjack/status/2005095786309452275)

我最近还在考虑办理家庭网如何调取使用，会不会国内IP受限？