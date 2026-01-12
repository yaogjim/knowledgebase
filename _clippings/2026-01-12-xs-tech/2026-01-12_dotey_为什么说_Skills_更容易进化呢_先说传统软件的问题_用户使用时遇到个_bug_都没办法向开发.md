---
title: "2026-01-12_dotey_为什么说_Skills_更容易进化呢_先说传统软件的问题_用户使用时遇到个_bug_都没办法向开发"
source: "https://x.com/dotey/status/2010591496664207453"
author:
  - "[[@dotey]]"
published: 2026-01-12
created: 2026-01-12
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "skills"
---

# 为什么说 Skills 更容易进化呢？ 先说传统软件的问题，用户使用时遇到个 bug，都没办法向开发

**宝玉** @dotey 2026-01-11

为什么说 Skills 更容易进化呢？

先说传统软件的问题，用户使用时遇到个 bug，都没办法向开发者反馈，这个链条太长了，用户如果运气好有日志，还得把日志记录下来，或者用户专业一点，能知道怎么重现，然后这个 Bug 可能还得层层上报，先给公司，再转给 QA，QA 去验证，最后到开发，这中间稍微一点损耗就没办法重现没办法解决。

但 Agent + Skills 的组合不一样，它相当于“开发者”就在你身边，Agent 既可以帮你执行任务，又可以充当开发者的角色，遇到问题不但可以定位，还可以修复。

举个例子（参考图2）来说，我在使用某个 skill 的时候，发现这个 skill 的结果不符合预期，这时候我可以直接在当前会话告诉 agent，让它检查一下提示词或者脚本，看问题在哪，并且修复。

由于当前会话中提示词它有，输入输出它也知道，工具调用的参数、结果它都知道，本地还有所有文件，那么它可以轻易的定位到问题在哪，直接帮你修复或者优化。

还有一点，由于 skills 相关的内容都是文本文件，就是如果配合 git 做好版本管理，所有的修改操作都会被记录下来，如果有问题可以跟踪整个变更过程，而且一个人机器上的 Skills 改进了，可以共享给所有人。

> 2026-01-11
> 
> ![Image](https://pbs.twimg.com/media/G-cOPpxXgAADcSM?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G-cORsGWEAAKDOY?format=jpg&name=large) ![Article cover image](https://pbs.twimg.com/media/G-WS4jWWcAAjAHE?format=jpg&name=large)

* * *

**PutOnClothes** @madvincent4 [2026-01-12](https://x.com/madvincent4/status/2010592511161696588)

有个问题想请教宝玉老师，这样的话 skill 的共享改进有可能是 case specific 的么？比如一个改进只对当前项目有效，但是对于其他人可能起反作用，这样最后是否还是需要一个类似 QA 的完整完整流程？

* * *

**宝玉** @dotey [2026-01-12](https://x.com/dotey/status/2010593105683333349)

这其实取决于你什么策略

比如这个只是自己用，就很简单

如果是共享，那么需要有个中心版本，有专门的人或者团队维护，遇到这种问题要么融入中心版本，要么不做修复，每次各自解决

可能还有其他方案，取决于你怎么权衡

* * *

**toobe** @lwllol33 [2026-01-12](https://x.com/lwllol33/status/2010592975928303622)

像ui类的debug是不是比较难以用skills解决🤔

* * *

**在一家公司做了 10 年的前端** @tobemaster56 [2026-01-12](https://x.com/tobemaster56/status/2010592439300657408)

宝玉老师，提到的痛点太真实了，尤其桌面端的软件，反馈问题，别人说，我的机器好好的，没法复现啊，还我录视频，导出日志。甚至有可能让我进程取样。

![Image](https://pbs.twimg.com/media/G-cPJ5WXkAAvGoR?format=jpg&name=large)

* * *

**iTrustCapital** @iTrustCapital

No External Wallets or Unnecessary Risks, Just a Trusted Way to Buy & Custody Crypto.

无需外部钱包，也无不必要风险，只需一种可靠的加密货币购买与保管方式。