---
title: "2026-06-16_Huxpro_How_I_Built_Vue_Lynx_with_AI_in_Two_Weeks_我如何在两周内使"
source: "https://x.com/Huxpro/status/2036993665965416601"
author:
  - "[[@Huxpro]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#use"
  - "#lynx"
  - "x"
  - "@Huxpro"
---

# How I Built Vue Lynx with AI in Two Weeks
我如何在两周内使用 AI 构建 Vue Lynx

**Xuan Huang · 黄玄**

# How I Built Vue Lynx with AI in Two Weeks 我如何在两周内使用 AI 构建 Vue Lynx

[https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)Vue developers have wanted native for years. The

["Vue + Lynx = Vue Native"](https://x.com/danielkelly_io/status/1899746975588737407)

tweet pulled 1.7k likes. The

[Vue integration issue](https://github.com/lynx-family/lynx/issues/193)

on our repo hit 1,600 upvotes -- our biggest feature request ever. The demand was clear; the question was bandwidth.

When

[Lynx](https://lynxjs.org/) open-sourced a year ago,

[Evan You](https://x.com/youyuxi/status/1898663514581168173)

and

[Rich Harris](https://x.com/Huxpro/status/1927276405328429259)

both shouted it out, but production-quality framework integration has always demanded serious engineering bandwidth. Then projects like

[Vercel's web streams rewrite](https://vercel.com/blog/we-ralph-wiggumed-webstreams-to-make-them-10x-faster)

and

[Cloudflare's ViNext](https://blog.cloudflare.com/vinext/)

showed how solo engineers, armed with AI, can ship what used to take a team. That changed the math for me.

Vue already has the foundation: a mature Custom Renderer API. I spent a weekend on it. One ~$1,400, 37-hour hackathon. It started with a design exploration: "Can Vue's Custom Renderer even work with dual-thread code splitting, and how?" By 3am Sunday I was debugging "Tap to increment doesn't work" with Claude. By Monday morning, I had

[a working TodoMVC

一个可用的 TodoMVC](https://x.com/Huxpro/status/2028672358912086524). I couldn't resist dropping a subtle subtweet, and it immediately took off on X.

Vue 已经具备了基础：一个成熟的自定义渲染器 API。我花了一个周末来做这件事。一场约 1400 美元、持续 37 小时的黑客松活动。它始于一次设计探索：“Vue 的自定义渲染器是否能支持双线程代码分割，以及如何实现？”到周日凌晨 3 点，我正在和 Claude 一起调试“点击增量不生效”的问题。到周一早上，我已经

[一个能正常运行的 TodoMVC](https://x.com/Huxpro/status/2028672358912086524)

。我忍不住发了一条隐晦的推文，它立刻在 X 上走红。

> What have I done 我做了什么
> 
> — Xuan Huang · 黄玄
> 
> [https://x.com/Huxpro/status/2028672358912086524](https://x.com/Huxpro/status/2028672358912086524)
> 
> ![图片](https://pbs.twimg.com/profile_images/1966185663285391361/TM6shSX__x96.jpg)![Image](https://pbs.twimg.com/media/HCdJ_JSaIAEAQ5M?format=jpg&name=large)

# Introducing Vue Lynx

介绍 Vue Lynx

The next two weeks of evenings and weekends went into making it real: 160+ commits across ~180 sessions.

接下来两周的晚上和周末时间都被用来将其变为现实：160多次提交，跨越约180个会话。

```markdown
▎ Week 1 ████████████░░░░░░░░  Runtime + Toolchain
▎ Week 2 ░░░░░░░░████████████  Docs + Examples + i18n
```

I could have shipped after week one. But if you know me, you know my principle:

我本来可以在第一周结束后发货的。但如果你了解我，你就知道我的原则：

> When things actually work, you let the demos do the talking.
> 
> 当东西真正好用时，你就让演示来说话。

Check

[vue.lynxjs.org](//vue.lynxjs.org) for 20+ example apps running natively and on the web -- you can try them without leaving your browser.

检查

[vue.lynxjs.org](//vue.lynxjs.org)

以查看 20 多个原生和 Web 端运行的示例应用——你可以在不离开浏览器的情况下尝试它们。

> @Vuejs -> @Lynxjs\_org -> the Web Mind-blowing how all these demos just work. The loop is closed. @Vuejs -> @Lynxjs\_org -> 万维网 这些演示全都这么好用，太令人惊叹了！ 循环已关闭。
> 
> — Xuan Huang · 黄玄
> 
> [https://x.com/Huxpro/status/2036982983907832079](https://x.com/Huxpro/status/2036982983907832079)
> 
> ![图片](https://pbs.twimg.com/profile_images/1966185663285391361/TM6shSX__x96.jpg)![图片](https://pbs.twimg.com/amplify_video_thumb/2036981451649114112/img/9joJC_d25LWGW0D-.jpg)

We cover the full Composition API, <Transition>, <Suspense>, and ecosystem integrations including Vue Router, Pinia, Tailwind CSS, and TanStack Query. We also ported Lynx's official tutorial (Waterfall Gallery and Swiper) to showcase native components and Main Thread Script for zero-latency gestures. A HackerNews clone brings them all together.

我们涵盖了完整的组合式 API、<Transition>、<Suspense> 以及生态系统集成，包括 Vue Router、Pinia、Tailwind CSS 和 TanStack 查询。我们还移植了 Lynx 的官方教程（瀑布流画廊和 Swiper），以展示原生组件和用于零延迟手势的主线程脚本。一个 HackerNews 克隆将它们整合在一起。

## Try It Today

今日尝试

```bash
npm create vue-lynx@latest
```

It's

[open source](https://github.com/huxpro/vue-lynx), of course. If it sparked something, give it a Star! And give some love to the

[Lynx Engine](https://github.com/lynx-family/lynx)

and

[Lynx Frontend Stack](https://github.com/lynx-family/lynx-stack)

too. They are the shoulders we're standing on. I'd love for the Vue and Lynx communities to build on it together. Issues, PRs, and feedback are all welcome.

它是开源 ，当然。如果它启发了你，就给它点个星！也请给 Lynx Engine 和 Lynx 前端栈一些支持。它们是我们所依靠的肩膀。 我很乐意让 Vue 和 Lynx 社区共同基于它进行构建。问题、PR 和反馈都欢迎。

# 

# 

["Harness"](https://openai.com/index/harness-engineering/)

[Engineering](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

> You gotta use the hottest word after "AI", "vibe", and "agentic" — harness.
> 
> 你得用继‘AI’、‘vibe’和‘agentic’之后最热门的词——harness。

No humans were harmed to write code in the making of this project.

在本项目开发过程中，编写代码未造成任何人员伤害。

## Setting Up the Architecture for AI

设置 AI 架构

There were two prior community efforts. The second, from the Vue Vine maintainer

[@Shenqingchuan](https://x.com/@Shenqingchuan), went impressively far,

[even getting Main Thread Script demos running](https://x.com/Shenqingchuan/status/1996862232593129815?s=20)

. But both kept Vue on the main thread just like the Web. This works on Lynx, but it's not taking advantage of the

[dual-thread architecture](https://lynxjs.org/blog/lynx-unlock-native-for-more#use-the-main-thread-responsibly-for-interactivity)

Lynx is known for: offload the heavy framework re-rendering on background and ensuring the native UI thread non-blocking and only tapped in when needed (with Main Thread Scripts).

之前有两次社区尝试。第二次尝试来自 Vue Vine 的维护者

[@Shenqingchuan](https://x.com/@Shenqingchuan)

，取得了显著进展，

[甚至让主线程脚本（Main Thread Script）演示运行起来](https://x.com/Shenqingchuan/status/1996862232593129815?s=20)

。但两者都将 Vue 保留在主线程上，就像 Web 一样。这在 Lynx 上可行，但没有利用到

[双线程架构](https://lynxjs.org/blog/lynx-unlock-native-for-more#use-the-main-thread-responsibly-for-interactivity)

Lynx 以其著称：将繁重的框架重新渲染转移到后台，确保原生 UI 线程不阻塞，仅在需要时（通过主线程脚本）才调用。

This was the core architectural decision I validated on Day 1. In Vue Lynx, the entire Vue runs on the Background. A lightweight ShadowElement linked-list tree mirrors the native element tree in memory, and every DOM mutation gets serialized into a flat ops buffer shipped to the Main Thread in one batch per tick:

这是我在第一天验证过的核心架构决策。在 Vue Lynx 中，整个 Vue 运行在后台线程。一个轻量级的 ShadowElement 链表树在内存中镜像原生元素树，每次 DOM 变更都会被序列化为扁平的操作缓冲区，并在每帧（tick）中以一个批次发送到主线程：

```bash
┌──────────────────────────────────────────────────────┐
│ Background Thread │
│  Vue 3 runtime · reactivity · lifecycle · your code  │
└──────────────┬──────────────────────▲────────────────┘
 ops  │ │  events
 ▼ │
┌──────────────────────────────────────┴───────────────┐
│ Main Thread │
│  Native elements · layout · rendering · MTS handlers │
└──────────────────────────────────────────────────────┘
```

To keep the agent aligned with this dual-threaded architecture and not drift towards the single-threaded Web model it defaults to, I embedded all

[critical plans directly in the source tree

关键计划直接在源代码树中](https://github.com/Huxpro/vue-lynx/tree/main/plans) : design discussion notes, decision logs and post-implementation learning as cross-session context. Each new session picks up where the last left off, inheriting our architectural constraints and reasoning that shaped the code.

为了使代理与这种双线程架构保持一致，而不偏离其默认采用的单线程 Web 模型，我将所有

[关键计划直接嵌入到源代码树中](https://github.com/Huxpro/vue-lynx/tree/main/plans)

：设计讨论记录、决策日志以及实施后学习内容作为跨会话上下文 。每个新会话都会从上次结束的地方继续，继承我们架构的约束条件和塑造代码的推理过程。

## Bridging the Vue Upstream Tests

连接 Vue 上游测试

The most critical investment in any AI-driven development is feedback. Ideally, to ensure conformance with official Vue, we'd reuse Vue's upstream test suite directly. But Vue's test suite assumes a single-thread DOM. How do you run it to test a dual-thread renderer?

在任何 AI 驱动的开发中，最关键的投入是反馈。理想情况下，为确保符合官方 Vue 规范，我们会直接复用 Vue 的上游测试套件。但 Vue 的测试套件假设单线程 DOM 环境。你如何运行它来测试双线程渲染器？

Fortunately, Lynx already has the infra for

[dual-threaded testing environments](https://lynxjs.org/next/api/lynx-testing-environment/index.html#lynx-jstesting-environment). So we can rewire the suite to run through our dual-thread pipeline: BG ShadowElement -> ops buffer -> syncFlush() -> MT applyOps -> PAPI -> jsdom, then let the agent grind until no remaining failures were fixable (effectively

[Ralph Loop](https://ghuntley.com/loop/)

). The result: 852 passed out of 949 upstream tests. Every failure is accounted for in a

[skiplist](https://github.com/Huxpro/vue-lynx/blob/main/packages/upstream-tests/skiplist.json)

with documented reasons, and all turned out to be negligible. See the

[full report and skip analysis](https://github.com/Huxpro/vue-lynx/blob/main/packages/upstream-tests/README.md)

.

幸运的是，Lynx 已经具备了用于

[双线程测试环境](https://lynxjs.org/next/api/lynx-testing-environment/index.html#lynx-jstesting-environment)

。因此，我们可以重新配置测试套件，使其通过我们的双线程管道 ：BG ShadowElement → ops buffer → syncFlush() → MT applyOps → PAPI → jsdom，然后让代理持续运行直到没有剩余的故障可以修复（实际上

[Ralph Loop](https://ghuntley.com/loop/)

）。结果：949 个上游测试中通过了 852 个。每个故障都在一个

[跳跃表](https://github.com/Huxpro/vue-lynx/blob/main/packages/upstream-tests/skiplist.json)

中记录了详细原因，且所有故障都可忽略。查看

[完整报告和跳过分析](https://github.com/Huxpro/vue-lynx/blob/main/packages/upstream-tests/README.md)

.

We also added our own tests for Lynx-specific surface area such as <list> elements, bindtap events, Main Thread Scripting APIs. With the pipeline proven, I pushed further and forked the

[7GUIs benchmark

7GUIs 基准测试](https://vue.lynxjs.org/guide/7guis) from the official Vue docs as a stress test.

我们还为 Lynx 特有的界面范围添加了我们自己的测试，例如元素、bindtap 事件、主线程脚本 API。在管道验证通过后，我进一步推进并分叉了

[7GUIs 基准测试](https://vue.lynxjs.org/guide/7guis)

从官方 Vue 文档中作为压力测试。

```text
 BG Thread  ┃  Main Thread
 ┃
Vue → ShadowElement → Ops  ┃  PAPI → Lynx Engine → UI
 ┃
├─ vue runtime-core ─┤ ┃
├─── vue runtime-dom ──────╂──┤
 ├── E2E Pipeline ──╂─────────────┤
 ┃ ├── Agentic ───┤
```

## Agentic E2E Verification Loop

代理式端到端核实循环

But those classic machinery tests can't catch real UI bugs that used to require human evaluation: a misaligned CSS layout, an interaction broken on a real device. For advanced Vue features like <Transition>, <Suspense>, you need to see them run and interact to verify the behavior.

但那些传统的机械测试无法捕捉过去需要人工评估的真实 UI 缺陷：比如错位的 CSS 布局，或在真实设备上交互失效的情况。对于像 <Transition>、<Suspense> 这样的高级 Vue 特性，你需要观察它们的运行和交互以验证其行为。

With the right harnessing, writing examples isn't just demoing -- they double as workloads that the agent can evaluate automatically. I wired up two execution environments: iOS simulator via

[Lynx DevTool MCP](https://lynxjs.org/next/ai/lynx-devtool-mcp.html)/CLI/Skill, and agent-controlled browser via

[Lynx for Web](https://lynxjs.org/next/guide/start/integrate-with-existing-apps?platform=web)

. The loop is simple: run an example in both, observe and verify the output, and any regression triggers a fix. No human in the loop.

通过正确的编排，编写示例不仅仅是演示——它们还兼作代理可以自动评估的工作负载。我搭建了两个执行环境：iOS 模拟器通过

[Lynx DevTool MCP](https://lynxjs.org/next/ai/lynx-devtool-mcp.html)

/CLI/技能，和代理控制的浏览器通过

[Lynx for Web](https://lynxjs.org/next/guide/start/integrate-with-existing-apps?platform=web)

。这个流程很简单：在两者中运行示例，观察并验证输出，任何回归问题都会触发修复。无需人工介入。

```text
┌──── Fix ◀─────────────────────────────────┐
│ │
▼ │
Example ──┬──▶ iOS Simulator ───┬──▶ Evaluate
 │ (DevTool MCP) │
 │ │
 └──▶ Lynx for Web ────┘
 (agent-browser)
```

I started with Vue core features, where correctness is well-defined: the agent reads the official docs, writes an example, and checks whether the output conforms. Then I expanded scope to ecosystem integrations: Vue Router, Pinia, TanStack Query, Tailwind CSS.

我从 Vue 的核心特性开始，这些特性的正确性定义明确：工具阅读官方文档，编写示例，并检查输出是否符合要求。随后我将范围扩展到生态系统集成：Vue Router、Pinia、TanStack 查询、Tailwind CSS。

For the final exams, I tried a different approach: one I'd later learn has a name: differential evaluation: I let the agent port existing applications and verify the output against the originals. The first used the canonical Vue HackerNews implementation as ground truth, running both the Web version and the vue-lynx port with Lynx for Web side-by-side in the browser; the second used existing ReactLynx demos as reference, porting them to vue-lynx and verifying parity on the iOS Simulator via Lynx DevTool MCP. The harness doesn't need to know what "correct" looks like in the abstract. It just needs the two outputs to agree.

在期末考试中，我尝试了一种不同的方法：一种后来我才知道它的名字是 differential evaluation：我让代理移植现有应用并将输出与原始版本进行验证。第一种方法使用标准的 Vue 版 HackerNews 实现作为基准，在浏览器中并排运行 Web 版本和 vue-lynx 移植版本（使用 Lynx for Web）；第二种方法使用现有的 ReactLynx 演示作为参考，将它们移植到 vue-lynx，并通过 Lynx DevTool MCP 在 iOS 模拟器上验证等效性。这个测试框架不需要抽象地知道“正确”的样子是什么样的，只需要两个输出一致即可。

```text
| Ground Truth | Candidate | Environment |
|-----------------------|-----------------|--------------------------|
| Vue HackerNews (Web)  | vue-lynx port | Lynx Web (browser) |
| ReactLynx demos | vue-lynx port | Lynx Native (Simulator)  |


 ┌─────────────────────────────┐
 ┌────────────▶  ground truth ──▶ A │
 │ │ │ │
Input ─┤ │ Compare ──▶  Divergence
 │ │ │ │ │
 └────────────▶  Lynx (candidate)  ──▶  B │ ▼
 └─────────────────────────────┘ Fix Loop
```

## The Bill

该法案

```text
┌──────────────────────────────────────────┐
│ The Bill (at Opus rate) │
├──────────────────────────────┬───────────┤
│ Input (3.8M tokens) │ $ 57 │
│ Output (6.8M tokens) │ $ 510 │
│ Cache Write (117.9M tokens)  │ $ 2,211 │
│ Cache Read (2.5B tokens) │ $ 3,769 │
├──────────────────────────────┼───────────┤
│ TOTAL │ $ 6,547 │
└──────────────────────────────┴───────────┘
```

The numbers tell a story. Output tokens (the code and text Claude actually wrote) account for just 8% of the cost. The other 92% is comprehension: re-reading the codebase, ingesting tool outputs, re-processing conversation history across 31,700 API turns. That's 2.5 billion tokens of reading to produce 6.8 million tokens of writing -- a 370:1 ratio. This is what "agentic" actually looks like at the billing level. Was the "$6,500" API rate worth it? (Claude

[gifted me](https://x.com/Huxpro/status/2031973188440052119?s=20) the 200$ Claude Max for

[its Open Source program](https://x.com/Huxpro/status/2031973188440052119?s=20)

, thankfully)

数字讲述了一个故事。输出 token（Claude 实际编写的代码和文本）仅占成本的 8%。另外 92%的成本用于理解工作：重新阅读代码库、吸收工具输出、重新处理跨 31,700 次 API 调用轮次的对话历史。这意味着阅读了 25 亿个 token，才生成 680 万个 token 的输出——比例为 370:1。这就是“agentic”在计费层面的实际表现。 6500 美元的 API 费率值得吗？（Claude 送给我 200 美元的 Claude Max 用于其开源项目，谢天谢地）

# What's Next?

接下来是什么？

This project started as one person's nights-and-weekends effort. I'd love to explore with Vue core team how we can shape the future of Vue on native together. Personally, and on behalf of the Lynx team, we're committed to supporting its growth. Vue Lynx is pre-alpha. The architecture is solid, but Vue's API surface is large, and we haven't verified every corner of it.

这个项目最初是一个人在夜晚和周末的努力。我很想与 Vue 核心团队探讨，我们如何共同塑造 Vue 在原生平台上的未来。就我个人而言，并代表 Lynx 团队，我们致力于支持它的发展。 Vue Lynx 处于预 alpha 阶段。架构很稳固，但 Vue 的 API 表面很大，而且我们还没有验证它的每一个角落。

- Features like KeepAlive and Teleport likely need runtime adaptations.
 
 像 KeepAlive 和 Teleport 这样的特性可能需要运行时适配。
- <style scoped> and v-model on native inputs are solvable but not yet implemented.
 
 带有 scoped 属性的<style>标签和原生输入元素上的 v-model 是可解决的，但尚未实现。
- The Main Thread Script API currently reuses ReactLynx's directive-based design. A more Vue-idiomatic approach (like <script main-thread setup>) is worth exploring.
 
 主线程脚本 API 目前复用了 ReactLynx 的基于指令的设计。一种更符合 Vue 习惯用法的方法（例如 <script main-thread setup>）值得探索。
- Vue DevTools integration with Lynx DevTool app.
 
 Vue DevTools 与 Lynx DevTool 应用的集成

And beyond Vue core, there's a massive Vue ecosystem waiting for us to adapt and grow on native. The vision is simple: Vue developers should be able to ship native apps as naturally as they ship for the web today. We're not there yet, but the foundation is in place, and the path is clear. If you've read this far:

[try it

试试它](https://vue.lynxjs.org). Build something. Tell us what's missing. Oh, and Btw:

除了 Vue 核心之外，还有一个庞大的 Vue 生态系统等待我们在原生环境下适应和发展。 愿景很简单：Vue 开发者应该能够像现在发布 Web 应用一样自然地发布原生应用。我们还没达到这个目标，但基础已经打好，而且方向明确。 如果你已经看到这里：

[试试它](https://vue.lynxjs.org)

. 构建一些东西。告诉我们缺少了什么。 哦，顺便说一句：

> Fun fact: @LynxJS\_org was initially created with @vuejs 2 有趣的事实： @LynxJS\_org 最初是用 @vuejs 2创建的
> 
> — Xuan Huang · 黄玄
> 
> [https://x.com/Huxpro/status/2032279225479176229](https://x.com/Huxpro/status/2032279225479176229)
> 
> ![图片](https://pbs.twimg.com/profile_images/1966185663285391361/TM6shSX__x96.jpg)![Image](https://pbs.twimg.com/media/HDQTk_sXUAAOjH9?format=jpg&name=large)

* * *

### 热门回复

**@Mar 25** ♥ 389 · 💬 15

@Vuejs

\->

@Lynxjs\_org

\-> the Web

Mind-blowing how all these demos just work.

The loop is closed.

@Vuejs

\->

@Lynxjs\_org

\-> 万维网

这些演示全都这么好用，太令人惊叹了！

循环已关闭。

**@Mar 2** ♥ 379 · 💬 23

What have I done

我做了什么

**@Mar 12** ♥ 127 · 💬 6

Fun fact:

@LynxJS\_org

was initially created with

@vuejs

2

有趣的事实： @LynxJS\_org 最初是用 @vuejs 2创建的