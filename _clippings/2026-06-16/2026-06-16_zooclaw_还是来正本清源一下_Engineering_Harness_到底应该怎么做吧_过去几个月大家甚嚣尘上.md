---
title: "2026-06-16_read_readwise_io_还是来正本清源一下_Engineering_Harness_到底应该怎么做吧_过去几个月大家甚嚣尘上"
source: "https://read.readwise.io/new/read/01kn91kz72vtfskaz2bs7ch9dw"
author:
  - "[[@zooclaw]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#aicoding"
  - "read"
  - "@zooclaw"
  - "agent"
---

# 还是来正本清源一下 Engineering Harness 到底应该怎么做吧，过去几个月大家甚嚣尘上不需要工程师了，2 小时随手 Vibe 一下复刻一个应用的新闻很多。 | Readwise

1.  [
 
 还是来正本清源一下 Engineering Harness 到底应该怎么做吧，过去几个月大家甚嚣尘上不需要工程师了，2 小时随手 Vibe 一下复刻一个应用的新闻很多。
 
 还是来正本清源一下 Engineering Harness 到底应该怎么做吧，过去几个月大家甚嚣尘上不需要工程师了，2 小时随手 Vibe 一下复刻一个应用的新闻很多。 但是软件开发的核心挑战从来不是写 Code，而是管理复杂性。在 Vibe Code 下，因为代码吞吐量的进一步上升，我们的确有了更好的工具，但是同样复杂性也进一步上升了。 如果有了更好的工具，你还是只是复刻一个所有人都做了的产品，又有什么价值和意义呢？比如 Typless 很好，所以大家都来复刻一个语音输入法（我们其实在自己的产品里也内嵌了），但是这个时候一个语音输入法本身已经在市场上没有商品价值了，更像是一个一次性吸引流量的工具了。 所以我们不得不去在更短的时间内，做一个规模更大，更复杂的产品。而这个带来了更大的挑战，其实更需要工程师了，但是对于工程师的要求也变得更高了。
 
 x.com xwh - @zooclaw.ai now 3 mins
 
 ](/new/read/01kn91kz72vtfskaz2bs7ch9dw)
2.  [
 
 我现在的 flow 是：
 
 我现在的 flow 是： 1️⃣ 先前端 + mock 数据（claude + gemini） 2️⃣ 然后再 codex 写代码 3️⃣ claude review 4️⃣ codex 自己跑 playwright 做 e2e 测试 5️⃣ 我自己验收，关 issue 主要是 codex 前端真不行，一把梭 AI 太放飞 现在的问题是：claude 用量太少，成本有点高；gemini cli 慢成狗 你们玩的？
 
 x.com 𝙋𝙖𝙨𝙨𝙡𝙪𝙤 1 min
 
 ](/new/read/01kn91jegrzdrybg09wzv3ccft)
3.  [
 
 开源 Multica：专为 AI-native 团队设计的 Agent + 人的协作平台
 
 开源 Multica：专为 AI-native 团队设计的 Agent + 人的协作平台 https://t.co/Wx0IutujjR 为什么做 Multica？ Multica 最初是为了解决我们团队自己的问题： 1. 团队间的知识无法共享。 每个人都在用 coding agent，但产出的上下文全部散落在各自的 agent session 里。A 做完了一件事，B 不知道；agent 跑完了一轮，结果只有发起人看得到。团队知识变成了一座座孤岛。 2. 多人 + 多 Agent 的协作缺乏中枢。 当团队同时有多个 agent 在跑任务，谁在做什么、做到哪了、卡住了没有——没有一个地方能看到全貌。人和 agent 之间、agent 和 agent 之间，缺少一个共同的协作界面。 Multica 是什么？ 一句话：像 Linear 一样管理任务，但 AI agent 是一等公民。 你可以像分配任务给同事一样，把 issue 分配给 agent。agent 会自动领取任务、在你的本地机器上执行代码、提交结果、更新状态、发表评论——一切都发生在同一个看板里，所有人实时可见。 核心思路很简单：每个人把自己的 coding agent（Claude Code / Codex）注册到团队 workspace，之后就可以像分配任务给同事一样分配给 agent。agent 自动执行、更新状态、发表评论，所有人实时可见。 适合谁？ - 1-10 人的 AI-native 小团队 - 正在大量使用 coding agent 但缺少协作中枢的团队 - 希望让 agent 融入日常工作流而不是当作独立工具的团队 官网: https://t.co/sdFwgJM8KU 欢迎 star、试用、提 issue，也欢迎 PR。
 
 x.com Jiayuan (JY) Zhang 1 min
 
 ](/new/read/01kn91145trdqyk298qpnaxg8r)
4.  [
 
 低价、稳定使用 Claude Code (月包+按量+一键切换，全程无广)
 
 This tweet contains no text.
 
 x.com 余温 1 min
 
 ](/new/read/01kn8fjgsh4y9ydpkpfct7n7r6)
5.  [
 
 Toolbox · ninehills/blog Wiki
 
 Contribute to ninehills/blog development by creating an account on GitHub.
 
 github.com https://github.com/ninehills/ 1 min
 
 ](/new/read/01kn60w8axc8g71xc5yaj7mgdf)
6.  [
 
 任何减少自身选择权的行为，都可以看成是 ‘’软弱‘’。
 
 任何减少自身选择权的行为，都可以看成是 ‘’软弱‘’。 按照这个思路，过早表态，过早投入资源在某件事情上就是一种软弱，因为这可能提前把自己锁定在一个路径上，而未来完全无法调整改变。模棱两可，拒绝表态，沉默寡言，按兵不动，在很多场景下反而是真正的强硬。 饮食作息不规律，任性的消耗身体健康，就更是一种彻头彻尾的软弱了。
 
 x.com 硅谷王川 Chuan 1 min
 
 ](/new/read/01kn3xjhvsysh6ewy3rmttze6c)
7.  [
 
 分析claude code源代码第一步，先跑起来。这次泄漏的代码只是source map还原后的结果，缺少很多脚手架和私有package。本来我打算自己搞一下，结果发现已经有好心人搞定了。
 
 分析claude code源代码第一步，先跑起来。这次泄漏的代码只是source map还原后的结果，缺少很多脚手架和私有package。本来我打算自己搞一下，结果发现已经有好心人搞定了。 （我运行时有点小bug，把错误信息发给codex就搞定了） 尽早fork下载本地，估计存活不了太久😂
 
 x.com 宝玉 1 min
 
 ](/new/read/01kn3x1pqm31pn7mnnhjfhh9r4)
8.  [
 
 神前奏！74岁传奇歌手Sting在博物馆演绎名曲 心凝神静！Sting 2026年最新现场，在荷兰国立博物馆里演唱名曲〈Shape of My Heart〉
 
 神前奏！74岁传奇歌手Sting在博物馆演绎名曲 心凝神静！Sting 2026年最新现场，在荷兰国立博物馆里演唱名曲〈Shape of My Heart〉 史上最好听的吉他前奏之一，无论何时响起，都能让人瞬间进入宁静，如此安谧、孤寂、冰冷而静思，简直有一种古典式的冥想氛围，Dominic Miller 弹得还是那么动人。据介绍 Sting 这次演出还用到了一把独特的17世纪吉他，原为路易十四宫廷制作，并一直珍藏在荷兰国立博物馆。 在这样的一个夜晚，听着这吉他旋律与斯汀74岁的嗓音，让人进入了四分钟的安宁的心流。
 
 x.com 瞎玩菌 1 min
 
 ](/new/read/01kn0zkf49pxdm7189sc86mn6f)
9.  [
 
 My dear front-end developers (and anyone who’s interested in the...
 
 My dear front-end developers (and anyone who’s interested in the future of interfaces): I have crawled through depths of hell to bring you, for the foreseeable years, one of the more important foundational pieces of UI engineering (if not in implementation then certainly at least in concept): Fast, accurate and comprehensive userland text measurement algorithm in pure TypeScript, usable for laying out entire web pages without CSS, bypassing DOM measurements and reflow
 
 x.com Cheng Lou 2 mins
 
 ](/new/read/01kmz5gf85qnscv853sg8vtz6w)
10.  [
 
 1/
 
 1/ Claude Code users: token-saving tactics that actually work 💰 My Claude Code token usage started climbing fast, and my subscription limit wasn't enough. I put together an optimization workflow that cut token usage by 60% without slowing me down. Here are the core steps 👇🧵
 
 x.com AI Builder Club 1 min
 
 ](/new/read/01kmz5d509tzztpq20qw12cd5z)
11.  [
 
 The Most Important Ideas in AI Right Now (April 2026)
 
 This tweet contains no text.
 
 x.com ᴅᴀɴɪᴇʟ ᴍɪᴇssʟᴇʀ 🛡️ 7 mins
 
 ](/new/read/01kmyjjc3kq223ewa21b9kpq7v)
12.  [
 
 昨天和我一个很敬佩的大哥从下午聊到晚上十点多。
 
 昨天和我一个很敬佩的大哥从下午聊到晚上十点多。 这个大哥的情况两句话就说完了： 1，为了法拉利限量版的购买资格，一口气先买了七台法拉利。 2，培养自己儿子从5岁开始做F1赛车手。 昨天是我第一次和他正儿八经聊天，因为过去我们基本都是在风月场所见面。 聊下来才知道，他的第一桶金和第二桶金，总结起来就三个词： 敢想敢干 足够专注 执行力拉满 他每次入局前都先看到市场验证，然后all in进去。 但今天我要讲的不是他怎么赚到的钱。 而是聊完之后，我想明白了一件关于我自己的事。 2000年，我和这个大哥同一年接触电脑。 他开始学技术，甚至把老师请到家里，天天请吃饭，就为了学得更快。 我开始玩游戏，在游戏里给人搞装备赚钱，觉得自己发现了一条捷径。 昨天坐下来聊了几个小时，我第一次认真想清楚了一件事： 我们不是走了不同的路。我们是同一年，在同一个房间，做出了完全不同的选择，然后被时间放大成两种人生。 他用技术和能力不断的在正道上搞事业 我用找捷径的思维不断的在捞快钱 他后来赚到第二桶金，拿其中3000万现金买了腾讯，那时候腾讯100多一股。他跟身边朋友说，尽可能all in，起码能到500，昨天还特意给我看了聊天记录来证明他当时的远见。 没几年后腾讯真的到了500，而今天我查了下，已经 1200 了。 换言之，当时这 3000 万进去，现在就是 3.6 亿 但他并没拿到那个结果。翻了一倍就卖了。 他自己总结：「直觉是对的，但认知跟不上，行为和认知没对齐，动作自然就变形了。」 我听到这句话的时候，沉默了很久。 因为这不只是他的故事。 我从小到大考试靠作弊。高数让两个学霸最快考完，一人负责一半，给我报答案，我连符号叫什么都不知道，还设计了自己听得懂的暗号。 我一直以为这是聪明。别人拼命读书考99分，我完全不读，我也有97分。 那时候我觉得这是超能力。 而这种找捷径让我拿到结果之后，会成为我做所有事的一种路径依赖。 把运气和小聪明当做硬实力的时候，就会变的很傲慢，认为靠努力，靠踏实搞钱的人，都挺傻逼的。 而自己在一个玩物丧志的状态下还能天天赚钱，感到沾沾自喜。 但昨天我终于想明白了这道数学题： 你不努力，97分。别人拼命，99分。 这2分的差距，放大到10年20年30年是几十亿和几百亿之差。 而且还有更恐怖的一面： 如果真的努力，我可能连97分都没有。 因为我的97分不是能力，是天赋的透支。它不会复利，只会折...
 
 x.com U哥 1 min
 
 ](/new/read/01kmyjha9byc0vtwmc6qwt3kvz)

还是来正本清源一下 Engineering Harness 到底应该怎么做吧，过去几个月大家甚嚣尘上不需要工程师了，2 小时随手 Vibe 一下复刻一个应用的新闻很多。

但是软件开发的核心挑战从来不是写 Code，而是管理复杂性。在 Vibe Code 下，因为代码吞吐量的进一步上升，我们的确有了更好的工具，但是同样复杂性也进一步上升了。

如果有了更好的工具，你还是只是复刻一个所有人都做了的产品，又有什么价值和意义呢？比如 Typless 很好，所以大家都来复刻一个语音输入法（我们其实在自己的产品里也内嵌了），但是这个时候一个语音输入法本身已经在市场上没有商品价值了，更像是一个一次性吸引流量的工具了。

所以我们不得不去在更短的时间内，做一个规模更大，更复杂的产品。而这个带来了更大的挑战，其实更需要工程师了，但是对于工程师的要求也变得更高了。

请刚开始 vibe coding 的你们不要因为 copy paste 了一下别人的项目，就发一些暴论来误导大家

1.  Worktree 同样是独立有一个工作目录
2.  项目随时间变动 git size 越来越大
3.  考虑到 agent 自主运行，一般 workspace 都是放在 devcontainer 内的，启动多个目录多个 devcontainer 会极大地增加内存需求和负担
4.  既然本身要走 PR 合并也就不存在本地 worktree 之间互相干扰的问题

没必要worktree，可以 clone 几份放在固定的目录，轮着用就够了，每次pull最新然后checkout一个新的branch，完成后提PR合并到main

[@dotey](https://twitter.com/dotey) 请教monorepo太大导致没法git worktree，如何更好的并行开发？

AI Coding 的能力很强，但是一旦你以团队方式运作，并且希望在短时间内发布一个复杂产品，就会带来巨大的复杂性管理的挑战。

今天如果你有 10 个工程师在一个 Codebase 里工作，实际的代码量大约是过去 50 个人的工作量。无论是 Claude Code 还是 CodeX 虽然能力都很强，但是如果不做好复杂性管理，代码仍然腐化得非常之快。

原因也很简单，就是 Claude Code 和 CodeX 进行 Agent Coding 的机制决定的，他们并不会读完所有的代码来Coding ，仍然是阅读部分代码来叠加式的实现新功能。

所以你很容看到是不是出现大量的重复代码，几千行代码的单个文件/组件，欠缺考虑的并发性问题。

而 Engineering Harness 中有一半工作就是要尝试尽可能地减少这些问题，来管理这个复杂性，（另一半是给到对于环境的更完整的可观测性和可操作性来让 Agent 可以更持续地完成工作）。

而管理这些复杂性的手段并不新，其实就是来自过去几十年来软件工程的所有实践。在我们开发 [zooclaw.ai](http://zooclaw.ai) 这个产品的过程里，我们目前维护了这样一套 harness 来尽可能保障质量和提升效率：

1.  Mono Repo + Dev Container
2.  通过 GitHub Actions 触发的 auto-review 以及 auto-merge
3.  一系列 pre-commit hook + ci/cd 的各类 lint 规则
4.  BDD 风格的高覆盖率的自动化测试
5.  自动触发的 E2E Test 以及对应自动截屏供人工审核
6.  每周自动触发的完整代码的 code review 与自动创建 issue

其实离理想的质量维护目标仍然有巨大的距离（因为现在 Vibe Coding 提一个 PR 的成本实在太低了），但是的确对维护代码的基本质量还是非常有帮助的。

下面我一一来解释每一项具体我们做了什么，以及为什么做这些选择。

## zooclaw #aicoding

1.  Mono Repo + Dev Container

我们一直是使用 devcontainer 的，但是最近才切换到使用 mono-repo。原因是 Coding Agent 的能力，只有在 mono-repo 里才能更好地发挥出来。

因为在当前 Coding Agent 的能力下，交付产品的瓶颈迅速变成了两个节点：

1\. 人与人之间因为分工不得不进行的沟通。

2\. 实际产品最终还是需要完成上线测试验收，但是 staging 环境我们往往只部署一套。

所以解决方案就是

1\. 减少不必要的沟通，不要区分前后端，尽量让一个人能完成完整一整个功能。

2\. 尽量每个人可以在自己的开发环境里就能部署起一套完整的产品，自己完成完整功能的验收。

而 mono-repo + devcontainer 完美解决了这个问题，devcontainer 里包含了绝大部分的服务代码（有一个公司层面的基建不在其中，但是因为一般那些基础组件的代码不会变更和修改，可以共享一套 dev/staging 环境），以及devcontainer 本身同时启动了各类依赖的 cache/db 中间件。所以任何一个人，可以有一个自己独立完整的环境测试完代码。

因为 devcontainer 也免去了大家搭建环境需要浪费的时间，事实上，我们现在的设计师和产品经理，都是直接基于 devcontainer 来 vibe design，直接修改前端交互界面，给工程师提 PR 的。

1.  通过 Github 强制触发的 auto-review

因为 LLM 的 next token prediction 的原理，在同一个 context 下他总是更倾向于认为自己是对的。同时，在目前的 PR 提交量下，也很难让每个 PR 都得到充分的 Review。

所以，最简单直接的方式就是让另一个 AI 来 Review。Claude Code 和 CodeX 都提供了 Github Actions，你很容易设置对任何 PR 进行 Code Review，并且你可以定义自己的 Prompt 和 checklist，完全满足每个项目自己特定的要求。

因为这些 Code Review Actions 是在一个干净崭新的 Context Window 里，所以往往能找到不少代码里的问题。对于 Review 的结果，我们通过让 Action 给 GitHub PR 打不同的 Tag 来进行三档规则性的标注，在减轻人的负担的情况下，又能保障质量：

1.  Low Risk Auto-Merge，也就是 AI 觉得代码完全没有问题，可以直接合并。这种情况下我们基本就自动合并了。
2.  Need Human Review，往往这种情况下，是有一些决策或者瑕疵，AI 觉得不好判断，让人来看。因为具体的 Review 内容是以 Github PR 的 Comments 出现的，人往往只需要关注 AI 跳出来需要人确认的部分来看。这类我们不 block merge，也就是任何人看了觉得不用改一样可以合并代码
3.  Request Change，这个情况是 AI 觉得有些地方有问题，要求修改，这类问题我们强制要求必须 Fix。除非找到项目或者团队的管理员人工确认 AI 看错了，不然不能合并。

目前我们还没有做到模型层面的对抗（就是用 Claude Code 写的代码让CodeX 来 review，CodeX写的代码用 Claude Code 来 review）。但是这个也是在我们下一步的计划里的。

1.  一系列的 Pre-Commit hook + CI/CD 的各类 lint 规则。

其实原来大家开发的过程中也用各种 Lint，但是过去因为人写代码的交付速度问题，往往设置的 Lint 规则比较简单，规则也通常比较松，因为最后拦截质量问题的是人的 Code Review。

但是在当前的Coding Agent 能力使得我们增加了更多的 Lint：

1\. 因为增加一个 Lint 也更容易了

2\. 因为代码吞吐量太大了，Lint 本身能为我们捕捉到很多问题

我们目前主要是有这样一系列的 Lint：

1\. Coding Format 和 Typecheck，但是比传统的更严格，因为 Fix Lint 问题本身变得容易了。外加每个人用的 Coding Agent 可能不同，就会有不同习惯的风格，不限制 Coding Format 会出现很多 Diff 里其实只是 format 改变。

2\. 单个文件行数限制，圈复杂度限制，代码重复率限制。

比如，单个 python 文件不超过 X 行，单函数圈复杂度不超过 Y，功能代码重复率不超过 U，测试代码重复率不超过 V。

3\. 更复杂的一些模块依赖限制，代码规则限制。比如 fastapi 的 routes 不能直接访问 DB，css 必须是 semantic 的。

所有 lint 都是以确定性的代码来限制，而不是 prompt。过去几十年其实软件工程里已经有了大量的武器来管理复杂度了，直接用就好了，没有必要用 LLM再发明一遍。这些 lint 工具稳定、快速、便宜。

而且因为 AI Coding 的存在，你要自定义写一个新的 Lint 也非常容易。

其中部分 Lint 也是 Warning，即发生了需要人来确认。其他的则是规则，需要强制通过。并且一些运行快速的 Lint 直接会放在 Pre-Commit hook 里。

因为团队都使用 devcontainer，使得 Pre-Commit hook自动会安装和强制运行，也比较节约大家的时间。

1.  BDD 风格的高覆盖率的自动化测试。

除了 Lint 之外，另一个保障尽量不出 Bug 的就是 Testing。但是和 Pre-AI 时代的测试有两个变化：

1.  因为使用了 devcontainer，devcontainer 里已经起了 DB/Cache 的服务，所以测试可以少一些 Mock，直接 Hit 到真实的 DB 和 Cache，尽量能够测试到完整正式的链路。并且现在的开发模式也是并行多个窗口 Agent 自己在跑，硬件的性能也很好，没有必要都 Mock。Mock 往往漏掉了很多真实的场景。
 
2.  测试尽可能直接用 BDD 风格的测试为主，人去 Review AI 写的测试的时候，也是 Review BDD 的自然语言描述为主，而不是去看实际的测试代码。因为测试通常复杂度比功能代码低，所以出错的概率也比较低，直接看 BDD 的业务逻辑描述就足够了。
 

让测试覆盖率超过 90% 以上，以捕捉到尽可能多的错误。但是不强求数字，如果提升覆盖率是靠海量的 Mock 没有实际意义也可以不做。

但是有意义的测试覆盖率本身反馈了代码质量，大量不得不 mock 才能测试的代码往往意味着设计或者代码质量本身存在问题。

1.  自动触发的 E2E Test 以及对应自动录屏供人工审核

光有 BDD 风格的测试还是不够的，BDD 风格的测试往往仍然是单模块的（比如单独测试前端组件，或者后端API）。

所有系统联通在一起的场景没有办法通过 BDD 覆盖到，Agent 类型的产品，是否 AI 正确回答了相关问题也无法通过 BDD 测试覆盖到。

我们会在 CI/CD 的 Tag 触发完成部署 Staging 环境和 Production 环境后，自动触发实际操作线上系统的端到端测试（E2E），以覆盖实际使用产品的各种场景。

这个时候，测试是实际通过浏览器操作线上真实的功能，并且在传统意义上的功能的 assertion 之外，还会加上 LLM Judge 的断言来判断功能是否正确。

并且所有的测试都会自动录屏，无论测试是否通过，都可以直接看一下录屏来判断基本的功能，Agent 效果和交互是否正确。

1.  每周自动 code review 和创建 issue

即使在有了上述的所有动作，代码其实仍然因为交付速度会快速腐化。所以代码本身需要更频繁的小规模重构。

这些小规模的重构，就依赖通过 Github Actions 自动触发的对于完整代码的 Code Review。这个 Review 核心不是看逻辑正确性，而是看代码的 Architecture 是否仍然正确。

对应的 Review 结果会以 Github Issues 的形式出现，然后让人工去跟进判断是否再通过 AI Coding 来解决。

类似于一个定时的垃圾回收或者 Memory Compaction 的操作。

hidden text to trigger resize events if fonts change

![ghostreader ghost body](/Ghost.svg) ![ghost glasses](/Glasses.svg)