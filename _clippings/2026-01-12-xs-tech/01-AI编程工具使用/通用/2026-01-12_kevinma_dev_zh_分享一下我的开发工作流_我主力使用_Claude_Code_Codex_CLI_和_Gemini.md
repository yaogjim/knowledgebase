---
title: "2026-01-12_kevinma_dev_zh_分享一下我的开发工作流_我主力使用_Claude_Code_Codex_CLI_和_Gemini"
source: "https://x.com/kevinma_dev_zh/status/2006044914627535187"
author:
  - "[[@kevinma_dev_zh]]"
published: 2026-01-12
created: 2026-01-12
description:
tags:
  - "x"
  - "@kevinma_dev_zh"
  - "https"
  - "2025-12-31"
---

# 分享一下我的开发工作流，我主力使用 Claude Code, Codex CLI 和 Gemini

**Kevin Ma** @kevinma\_dev\_zh 2025-12-29

分享一下我的开发工作流，我主力使用 Claude Code, Codex CLI 和 Gemini CLI，组成一个开发团队。

Claude Code 写代码快，小任务一把梭没问题。但任务一大，几乎必定有 Bug。让它自己改，改着改着容易绕进去。

所以我让 Codex 来 Review。

现在无论是技术方案还是代码实现，我都习惯交叉评审。就像人类团队里，代码写完要有人 Review 一样。

我一般是让 Gemini 做 planning，输出设计文档；Claude Code review 这个 plan，然后负责执行；Codex 依据 planning doc，review 代码并优化。

这个工作流目前还是很好使的，好几次重构都是一把过，省了不少来回改的时间。

UI 的调整就简单了，直接让 Claude Code 处理，不用这么复杂的流程。

我用 Gemini 做 planning，单纯是我更适应它的文字风格。Codex 的输出读起来太累，Claude Code 写文档又臭又长。所以规划这块我喜欢交给 Gemini，跟它聊起来比较舒服。

一个 AI 开发团队基本上就这三个模型了。像我们人类团队一样，相互讨论和 Review，然后由人负责把关技术设计，拍板最终方案。

我现在一个终端窗口，就把他们都放进去了。用 tmux 管理，能随时在三个 agent 窗口、nvim 和一个运行服务的窗口之间随意切换。想找谁聊就切到谁那边。

共享上下文有时要复制粘贴一下，命令倒也能解决，不过更多时候还是靠写文档来同步信息。不算特别优雅，但够用了。

> 2025-12-29
> 
> Claude Code 觉得完美的代码, Codex review 出无数的 Bug ... 重点是, 贴给 Claude, 一个劲说对对对,确实有这个问题...... 这可咋搞

* * *

**Rainman** @0xdeusyu [2025-12-30](https://x.com/0xdeusyu/status/2006061442114670645)

我主力使用两个，cc 和codex，跟你一样codex review

* * *

**Kevin Ma** @kevinma\_dev\_zh [2025-12-31](https://x.com/kevinma_dev_zh/status/2006165711350030679)

codex 靠谱

* * *

**古拉** @lishali12345 [2025-12-31](https://x.com/lishali12345/status/2006514176706122102)

Hi，看到这样的分享很欣喜，也是自己最近在学习的。想请教一下您的工作流中，在tmux中切换不同的agent时，如何让上一个节点的输出成为下一个节点的输入呢？例如Gemini的planning结果如何自动化给到Claude Code去执行，Claude Code执行后生成的代码如何自动给到Codex去Review呢？

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-01](https://x.com/kevinma_dev_zh/status/2006601748220408051)

写到文档中，或者复制粘贴

* * *

**Voyager | 舟行** @utopiazh [2025-12-31](https://x.com/utopiazh/status/2006308723732717702)

挺好的组合，回头也试试。

现在一般是一个项目固定一个模型，除非它陷入泥潭，找个对头来救火。

单项目里，Gemini的文档确实不错，但它自己执行的时候碰到问题有时会去改文档，而且变动还挺大😅

Claude倒是会照着文档执行的挺好，当然文档也是它自己写的，写的时候埋了挺多代码进去。

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-01](https://x.com/kevinma_dev_zh/status/2006601457009901771)

至少两个模型工具，相互 Review 比较可靠，我只用 Gemini 写文档，不让它写代码，执行准确度不如Claude code

* * *

**Rix** @SuperL46156688 [2025-12-31](https://x.com/SuperL46156688/status/2006251671329112187)

我现在主用gemini cli，cc辅助执行复杂任务，codex有必要上吗？大佬选择codex来review出于什么考虑？

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-01](https://x.com/kevinma_dev_zh/status/2006715588652183664)

codex很有必要，感觉它的逻辑强一些，思考地多一些，我重构和 Code Review 都用它，给的使用量大，缺点就是慢。

* * *

**Max** @venmax [2025-12-31](https://x.com/venmax/status/2006193074238882188)

gemini写计划大而全，但是会缺少很多细节

* * *

**Kevin Ma** @kevinma\_dev\_zh [2025-12-31](https://x.com/kevinma_dev_zh/status/2006193552867614807)

所以我先关注全局的，然后深入细节，再让其它的来 Review。一开始太多细节，有点受不了

* * *

**小岛哥** @findnewland2000 [2025-12-31](https://x.com/findnewland2000/status/2006174735508607081)

chatgpt+cursor如何？

ChatGPT + Cursor 怎么样？

* * *

**Kevin Ma** @kevinma\_dev\_zh [2025-12-31](https://x.com/kevinma_dev_zh/status/2006180827990810829)

我现在不用 cursor 了，我看挺多人这么用也是可以的，看个人习惯

* * *

**Sansi** @3an3i [2025-12-31](https://x.com/3an3i/status/2006182373780578388)

为啥用 gemini 做 plan ，很亮眼吗

* * *

**Kevin Ma** @kevinma\_dev\_zh [2025-12-31](https://x.com/kevinma_dev_zh/status/2006196698352431209)

claude 喜欢上来就聊细节，codex 写的东西有点八股文阅读起来难受。

gemini 的风格正好适合我，先全局聊，然后再深入细节，最后写完文档再给另外两个工具进行 review 补充细节。

* * *

**Warning** @WarningDD [2025-12-31](https://x.com/WarningDD/status/2006321225300353426)

国内怎么使用 Claude Code？有没有避免封号的办法

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-01](https://x.com/kevinma_dev_zh/status/2006715264080187566)

稳定的梯子，Google play/iOS 内购，我从来没遇到过封号，内购稳定但缺点就是费用会多一点。

* * *

**Hudie** @Hudie [2025-12-31](https://x.com/Hudie/status/2006169351498478003)

兄弟，3个都付费么？我目前主力cc

* * *

**Kevin Ma** @kevinma\_dev\_zh [2025-12-31](https://x.com/kevinma_dev_zh/status/2006176074565128227)

都付费的，这三家基本上是日常必备模型和工具了。Gemini 免费也可以有额度用

* * *

**前端輕鬆聊** @fetalkpodcast [2025-12-31](https://x.com/fetalkpodcast/status/2006262360261157337)

我是用 gemini 做 planning 和開發因為速度快，然後用 Codex 做最後 review 和其他與 edge cases

* * *

**Kevin Ma** @kevinma\_dev\_zh [2025-12-31](https://x.com/kevinma_dev_zh/status/2006263252196757526)

咱们 Codex 的用法差不多，但是 Gemini CLI 写代码的话不太靠谱，它经常会操作文件失败.

* * *

**ByeBye178** @ByeFly178 [2025-12-31](https://x.com/ByeFly178/status/2006343251780088226)

哪个模型 对win64 驱动开发帮助大呢?我用claude开发一个内核rootkit程序 一堆bug 我是反复审查 累死我了

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-01](https://x.com/kevinma_dev_zh/status/2006715760417403361)

这个还真不了解，可能需要你多尝试下

* * *

**sherlock** @xingyu\_liao [2025-12-31](https://x.com/xingyu_liao/status/2006211861373505733)

之前我也是在 Codex 和 Claude Code 之间协同，但我发现 Context 管理非常麻烦。

所以我现在用了 @droid 可以在 session 里面切换模型，我觉得更方便一些

* * *

**Justin** @dstjustinit [2025-12-31](https://x.com/dstjustinit/status/2006295245047341353)

我是用cursor產生詳細文檔跟規格，給Claude產程式碼，前端給Gemini，修bug回到cursor

* * *

**Zephyr** @Zephyr0715 [2025-12-31](https://x.com/Zephyr0715/status/2006204586739261688)

目前claude code 唯一的选择，codex 5.1拉胯后就没用过。在代码几乎全部AI的时代，code review 确实是刚需了

* * *

**milk** @Mmilk100 [2025-12-31](https://x.com/Mmilk100/status/2006180511442522219)

gemini 写 plan 倒是没想到，我试试