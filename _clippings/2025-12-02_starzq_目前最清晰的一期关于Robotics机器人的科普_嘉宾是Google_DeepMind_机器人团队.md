---
title: "2025-12-02_starzq_目前最清晰的一期关于Robotics机器人的科普_嘉宾是Google_DeepMind_机器人团队"
source: "https://x.com/starzq/status/1995396644502942187"
author:
  - "[[@starzq]]"
published: 2025-12-02
created: 2025-12-02
description:
tags:
  - "x"
  - "@starzq"
  - "2025-12-01"
  - "https"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 目前最清晰的一期关于Robotics机器人的科普，嘉宾是Google DeepMind 机器人团队

**Star@Day1Global Podcast** @starzq 2025-11-28

目前最清晰的一期关于Robotics/机器人的科普，嘉宾是Google DeepMind 机器人团队的技术负责人Tan Jie

最大感受是，如果要投资机器人，Google是一个重要的Beta

几个takeaways：

1\. 机器人领域目前面临最大的问题是“如何能够获得高质量、大规模的数据”，现在的数据量完全没有办法喂饱模型的能力

2\. 从 Scaling Law 出发，「生成式模型的仿真」更可行. Google现在主要用真实数据训练，但成本很高，覆盖度有限. 如果要满足 Scaling Law, 嘉宾认为「生成式模型的仿真」更可行（by VEO、Sora 2 这样的视频生成模型），通过完全遥操的数据来解决机器人问题可能性非常低。传统物理模拟仿真会慢慢地被生成式模型的仿真所取代

3\. 「比如我要生成任意场景，在传统的仿真里面，你需要有人建模，建完模以后就像做游戏一样，需要很多designer把所有的场景、所有的资产拼在一块，这就非常困难。但是我要500个家庭场景的视频，你只要500个不同的prompt」（让我想到 Alpha Go 第二版，不再是学习人类的数据，而是自己跟自己对战来提升）

4\. 我觉得所有的视频生成模型的进展都会让机器人领域感到非常兴奋，因为这就是一个新的仿真或者新的world model. 世界模型的定义是：如果给上前一帧，再给上机器人的动作，你可以预测下一帧。世界模型就是Vision-Language-Vision，vision和language in，生成下一帧的图像。

5\. 如果你有灵巧手，触觉就非常重要。之所以前面觉得触觉不重要，是受限于硬件，我们现在还处于夹爪时代

6\. Gemini非常非常的强大。它有一个非常强的vision encoder（视觉编码器），那个vision encoder已经见过了全世界所有互联网上的数据（假设），我们就发觉visual generalization comes for free。我们不需要做任何的研究，它的visual generalization就已经特别好。

7\. 中国的大环境和文化和硅谷还是不太一样的。在硅谷，大家会有一个信念，就是哪怕你并没有做出什么初期的结果，只要大家相信一个东西，还是愿意花时间、花精力、花钱上去做的，可以很长，比如十年。在大模型时代，你真的需要烧很多钱才能看到结果。很多时候，你要看到scaling law，比如在robotics上你需要几万小时的数据。但是很多国内的企业家、投资人也好，他们希望的是“我先给你一点点钱，你采十几个小时数据，给我看结果不错，我再给你继续投资或投算力”。

8\. 当一个generalist真正成型，specialist很难生存。因为我一个机器人可以做你的事情，但我还可以做100个其他不同的事情。

9\. 当我有一个人形机器人，它能够像人一样或者超越人的智能，那么的确，我不需要车来自动驾驶了，我可以有个机器人来做自动驾驶

10\. Gemini Robotics 1.5最重要的两点，一个是加入了thinking，另一个是跨具身迁移（motion transfer）。在我有训练数据的机器人里面，虽然我没有见过这个task，但这个task是别人见过的，我就能做那个任务。

11\. 机器人的发展有这么几个阶段：automation（自动化）、teleoperated robot（远程操控机器人）、generalist（通才）、superhuman capability（超人能力）。因为强化学习，因为机器人它可能有碳基生物所没有的一些存储、power density之类的，它可能在很多领域会超越人类的智能和体能。那可能是最后一个stage

12\. 我们为什么要做通用的人形机器人？嘉宾认为这是一个比较形而上的话题。可能会有一个大佬，他可能是Elon Musk，可能是Steve Jobs，一个visionary（有远见）的人，他灌输了一个概念，说“通用人形机器人是最终局的解决方案”。当一个大佬发话以后，就会有很多follower（追随者）、很多钱和很多talent（人才）进来，最后就促使这一条路径成了真正被解决的路径。

同时，大语言模型也证明了，如果你做specialized model（专有模型）——以前的语言模型通常都是specialized model，比如你做英到中的翻译是一个model，做VQA（Visual Question Answering，视觉问答）是另外一个model——但后来你发现，当你真正有一个generalist model（通用模型）的时候，那些specialized model（专有模型）就完全不能与之竞争。

13\. 一个有使命感的人，影响他跳槽不一定是钱，他不会容忍说“I’m on a wrong ship”

> 2025-11-28
> 
> 很前沿、hardcore的一集（关于robotics），嘉宾是Google DeepMind 机器人团队的技术负责人谭捷。可以从中了解：Google Robotics团队是怎么思考与工作的？我们也聊了聊这几年Google的研究文化变化🤖
> 
> 一些takeaways：
> 
> 1/机器人基座大模型最近几年的发展，主要依赖于多模态大模型，但多模态模型缺少robot

* * *

**Star@Day1Global Podcast** @starzq [2025-12-01](https://x.com/starzq/status/1995396656523817427)

播客中提到的 Dyna 机器人折叠衣服的视频

> 2025-09-29
> 
> Wrapped Day-1 at @corl\_conf - our booth was buzzing all day, and this is why. ⬇️
> 
> Here’s a timelapse of Dynasaur folding continuously, shrugging off every interruption researchers threw at it.
> 
> It’s thrilling to see the crowd erupt in applause after the robot nails a flawless

* * *

**Crazyox｜爱看腹肌版** @crazyox [2025-12-01](https://x.com/crazyox/status/1995412903554662780)

数据才是机器人发展的瓶颈啊，看来谷歌有先发优势！

* * *

**子敬Σ** @zijing [2025-12-01](https://x.com/zijing/status/1995583291303571694)

感觉人形机器人离真正家用还有很长的路要走

* * *

**JaazzMiin.sol** @Jaazzmiiin [2025-12-01](https://x.com/Jaazzmiiin/status/1995398099641254281)

生成式仿真太猛，数据瓶颈迎刃而解

* * *

**Eden** @Web3Eden01 [2025-12-01](https://x.com/Web3Eden01/status/1995412345024364952)

当我有一个人形机器人

我就让它来给我炒菜🧐

* * *

**Ozi** @0xOziii [2025-12-01](https://x.com/0xOziii/status/1995593311453938159)

i feel like robotics is still so early but the potential is insane