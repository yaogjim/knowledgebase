---
title: "2026-03-03_AlexZ_AlexZ_这个_skill_解决的是_AI_coding_agent_估算工时时的人类时"
source: "https://x.com/blackanger/status/2022994268810518786"
author:
  - "[[@AlexZ]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@AlexZ"
  - "agent"
  - "https"
---

# AlexZ 这个 skill 解决的是 AI coding agent 估算工时时的人类时

**AlexZ**

这个 skill 解决的是 AI coding agent 估算工时时的"人类时间锚定"问题。 agent 从训练数据中吸收了大量人类开发者的经验（"这个功能要 2-3 天"），导致它严重高估自己完成任务所需的时间。 skill 的核心思路是强制 agent 用自己的原生操作单位"round"（一次工具调用循环：思考→写码→执行→验证→修复）来估算，先把任务拆成模块、给每个模块估 round 数、乘以风险系数，最后才换算成人类的分钟数。 这样一个人类觉得要"几天"的项目，agent 能准确估出"31 rounds ≈ 1.5-2 小时"。 考虑到昨天给的「闪念/凝视/深思」太抽象，AI 不容易理解，所以使用了 "轮（round）"。 Skill 封装好了：[https://github.com/ZhangHanDong/agent-estimation…](https://github.com/ZhangHanDong/agent-estimation)

![图片](https://pbs.twimg.com/media/HBMej6ha4AAmEDQ?format=jpg&name=large)![图片](https://pbs.twimg.com/media/HBMej6kaQAE-EGk?format=jpg&name=large)

> **@blackanger**
> 
> 众所周知， 像 Claude Code 这种 Agent 给你评估工作任务，它都会按人类的常规工作时间预估。 本来一小时能完成的，它会跟你说大概需要一周。 为了让它精确评估工作量，我建议你和你的 Agent 做如下约定： 请你评估工作量以“深思”（Deep Thinks），为时间计量单位，而不是人类工作时间。 ∙1

* * *

### 热门回复

**@Outshine** ♥ 0 · 💬 1

有用，给领导报工时可以参考了

**@learner** ♥ 1 · 💬 0

“深思”这个单位挺妙，本质是把估算从“日历时间”换成“迭代次数/检查点”。 我更偏好让 Agent 输出：步骤+每步产物+风险点，最后再给一个区间估算，基本就不会虚高了。

**@Snslas** ♥ 0 · 💬 0

我都不在乎工時直接選最好的做，反正都是 AI 做我只在乎訂閱額度還夠不夠

**@Tamiko\_黎子** ♥ 0 · 💬 0

跟“天上一天，地上一年”一样，把ai估的时间换算一下除以24就好了，一天就是一个小时（其实还有点富裕量）

**@Kinesis Money** ♥ 0 · 💬 0

Join thousands of customers earning gold every month.