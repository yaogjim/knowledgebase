---
title: "马天翼 on X: "OpenCode 和 oh-my-opencode 简单科普" / X"
source: "https://x.com/fkysly/status/2008216983628902879"
author: ""
created: 2026-01-07 09:50:18
date: 2026-01-07 09:50:18
description: ""
tags: ""
---
有些人还不知道 OpenCode 是干啥的。OpenCode 就是 Claude Code 的开源平替版本。

[

![Image](https://pbs.twimg.com/media/G96c4MTb0AAr5PU?format=jpg&name=medium)



](https://x.com/fkysly/article/2008216983628902879/media/2008214973043167232)

基础功能上，Claude Code 能做到的，OpenCode 也差不多，而且很容易追上。那么 OpenCode 的独家好处有哪些呢？主要有3个：

1\. 自由的接入你已经购买过的模型 API，比如你已经有了一些第三方的 API，都可以想怎么接入怎么接入。（虽然 Claude Code 也能折腾一下接入第三方 API，但是毕竟不如 OpenCode 自由、开箱即用）。OpenCode 本身也有个叫 Zen 的模型提供服务，就是官方编程大模型精选集，你可以直接付费订阅他们的 API 服务，All-In-One省心了。

[

![Image](https://pbs.twimg.com/media/G96c_H0bcAE00DD?format=jpg&name=medium)



](https://x.com/fkysly/article/2008216983628902879/media/2008215092098461697)

2\. 混合用不同模型的多 Agents。这点听起来有点绕，实际理解起来很容易。基于第一点，假设你有 OpenAI 的 API和 Gemini API，因为 OpenCode 随便你用，那你就可以用 OpenAI 的 API 搞一个 Agent，然后再同时用 Gemini API 再搞一个 Agent，让第一个 Agent 调用第二个 Agent，形成混合多个不同模型的多个 Agents 共同协作。这点是 Claude Code 目前做不到的，Claude Code 只能多 Agents 协作，但是不能混合不同模型的。

当然，OpenCode 也是有点配置门槛的，所以，网友们整了一个 oh my opencode 项目，

。

[

![Image](https://pbs.twimg.com/media/G96djawbcAAbks4?format=jpg&name=medium)



](https://x.com/fkysly/article/2008216983628902879/media/2008215715657248768)

这玩意，好多人第一反应是为什么叫 oh my xxx。其实对很多用 zsh shell 工具的人来说就是一个梗，因为 zsh 工具对应有一个 oh my zsh，可以帮你自动傻瓜式配置好 zsh，支持很多强大好用的功能，做到开箱即用。那么，对应的 oh my opencode，也是一个开箱即用，帮你傻瓜化配置好 opencode，特别是上面提到的帮你配置好一系列的混合使用的 Agents （不过这个数量很多，Tokens 消耗也很快。） 总而言之，OpenCode 是 Claude Code 的开源平替。 如果你只是希望体验一下 OpenCode，在 OpenCode 里用一些量大便宜的国产模型，可以参考我的另外一篇讲目前值得冲的国产 Coding 模型：