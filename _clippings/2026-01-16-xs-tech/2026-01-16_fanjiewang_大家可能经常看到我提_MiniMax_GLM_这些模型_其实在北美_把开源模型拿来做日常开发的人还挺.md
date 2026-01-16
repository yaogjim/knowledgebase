---
title: "2026-01-16_fanjiewang_大家可能经常看到我提_MiniMax_GLM_这些模型_其实在北美_把开源模型拿来做日常开发的人还挺"
source: "https://x.com/fanjiewang/status/2011919103099797680"
author:
  - "[[@fanjiewang]]"
published: 2026-01-16
created: 2026-01-16
description:
tags:
  - "x"
  - "@fanjiewang"
  - "https"
  - "2026-01-16"
---

# 大家可能经常看到我提 MiniMax、GLM 这些模型 其实在北美，把开源模型拿来做日常开发的人还挺

**Frank Wang** @fanjiewang 2025-12-29

大家可能经常看到我提 MiniMax、GLM 这些模型

其实在北美，把开源模型拿来做日常开发的人还挺少的，X 之外很多圈子基本没怎么听说过

一方面 网上能看到的 demo 往往是 one-shot 小游戏，或者复刻一个超大项目，和日常场景不沾边儿

另一方面 几乎每个模型都在某个 benchmark 排前三，时间久了大家也就麻木了，很难判断它到底好在哪、适合干嘛

我更感兴趣的是：有没有更多人愿意像 DHH 那样，真的拿去用一用，再自己判断值不值得

> 2025-12-29
> 
> 正在为 Rails 开发 ActionMCP。一开始让 Gemini 3、Codex、Opus 和 M2.1 给我一个实现方案。它们都给出了可行的方案，但路径都大相径庭。太有意思了！不过还是打算手动重写整个东西，不过这些草图很有帮助。

* * *

**索南** @SonamNerd [2026-01-16](https://x.com/SonamNerd/status/2011965791252726163)

我是组合起来用的： 闭源sota 管规划和审阅，glm 管执行，glm用了两三个月了，感觉能干活

* * *

**gacha cheng** @quanyuqn27902 [2026-01-16](https://x.com/quanyuqn27902/status/2011958524033831254)

有的。我就拿 Minimax 做自己生活的个人助手。现在每天连吃啥做什么运动都是他们通过飞书推送决定的。

这家的 code-plan 算是量大管饱，拿来coding是比不上闭源sota，但是拿来做日常生活agent，处理“材米油盐”是非常足够了

* * *

**Fang Wang** @fangwangme [2026-01-16](https://x.com/fangwangme/status/2012028547284767082)

top 2 目前肯定是 Opus 4.5 和 Codex 5.2, 它们两个是可以互相补充的，犯了错或者陷入 roadblock 用另外一个模型基本上都能解决。

其他的模型各有各的缺点，基本上不能用来做大规模的开发，只能执行简单的任务（push 代码，pull request 等等）

* * *

**Leo** @lsj5031 [2026-01-15](https://x.com/lsj5031/status/2011921212176560453)

正经干活的话肯定无脑用SOTA模型，对产品没有什么压力的时候可以试用一下开源模型看看感觉评估以下效果，我自己的 research 小机器人就是 Claude agent SDK加 glm4.7 我觉得还可以，在这种没有硬指标评估的场景替代sonnet做很多事情还是很划算的，看看日历查查文档做搜索提供daily brief之类的。

* * *

**lhong** @lhong001 [2026-01-16](https://x.com/lhong001/status/2012007942787387567)

最近高频再用GLM4.7和minimax m2.1，个人感觉有时候还可以，有时候会非常蠢，尤其是用了一段时间一定要停一会，感觉plan哪怕用量没超，但是还是会降智

* * *

**Marc Ohmann** @marcohmann [2026-01-15](https://x.com/marcohmann/status/2011939730863047067)

我正在把开源模型整合到越来越多的开发工作流里。2026年似乎是关键年，那时这些模型大概90%左右就成熟了，能真正用在更复杂的场景里。

* * *

**trymorewang** @ebv9JfKnAN2d5S5 [2026-01-16](https://x.com/ebv9JfKnAN2d5S5/status/2011970258417172678)

两个我都在公司的项目用过，后来取消订阅了，原因不说大家也知道☹️

* * *

**Travis Ennis** @travisennis [2026-01-15](https://x.com/travisennis/status/2011921716511981858)

这两个模型都非常好，价格也很有竞争力。我绝对会推荐的。

* * *

**Vic Zhang** @RealVicHere [2026-01-16](https://x.com/RealVicHere/status/2012017622485962919)

真干活，还是要 gpt codex xhigh 和 opus

* * *

**Ivan Glushko (e/acc)** @ivnglushko [2026-01-15](https://x.com/ivnglushko/status/2011930687805538764)

我真的很喜欢 GLM 4.7，比如，我在没有任何先验知识的情况下做了一个浏览器扩展。它采用了最佳实践，并且在尝试 Minimax 之后做了很好的重构。

* * *

**HuZhou\_Mr** @HuZhou\_Mr [2026-01-15](https://x.com/HuZhou_Mr/status/2011951444560167377)

信任是要付出代价的

* * *

**Joshua Skootsky** @Joshua\_Skootsky [2026-01-16](https://x.com/Joshua_Skootsky/status/2011981220133867842)

我真的很喜欢 M2.1

我挺 DHH 的！

* * *

**draco** @DracoVibeCoding [2026-01-16](https://x.com/DracoVibeCoding/status/2011962120364310727)

的确，99.9% Vibe Coding出来的东西毫无价值...

* * *

**YUMSHOT** @NotShinigamii [2026-01-16](https://x.com/NotShinigamii/status/2011972330394722563)

我一直在尝试 opencode 提供的这两个模型。我喜欢 GLM 的详细计划，但这会导致输出 token 数量增加。Minimax 的代码风格更像是我平时写的那样，所以修改起来感觉更贴近我平时的做法。

* * *

**AI-CHECKER** @FPoet41619 [2026-01-16](https://x.com/FPoet41619/status/2011970404974542986)

你拿北美来说事有啥意思？？

* * *

**block0** @block0\_eth [2026-01-15](https://x.com/block0_eth/status/2011934932680261825)

我用M2.1帮我优化的seo英文文章，效果是最好的。比opus 4.5 ，gemini 3都要好

* * *

**proxyhuang** @proxyhuang [2026-01-16](https://x.com/proxyhuang/status/2012004372830683488)

已知有更好的模型下，不要去选用差的模型