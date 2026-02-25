---
title: "2026-02-25_艾略特_艾略特_Vibe_Marketing_Agent_从_0_到_1_实战_前两天看了这个"
source: "https://x.com/elliotchen100/status/2021391269818429705"
author:
  - "[[@艾略特]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@艾略特"
  - "skill"
  - "lead"
---

# 艾略特 # Vibe Marketing Agent 从 0 到 1 实战 前两天看了这个

**艾略特**

# Vibe Marketing Agent 从 0 到 1 实战

前两天看了这个 Vibe Marketing 的实战视频，核心是用 Claude Code + MCP + Skills，在一个 CLI 里从 0 到 1 搭一整套营销系统。​

[

![Image](https://pbs.twimg.com/media/HA1qyE8aUAALuNV?format=jpg&name=medium)


](/elliotchen100/article/2021391269818429705/media/2021389216312348672)

youtube 上面为数不多讲 Vibe Marketing 的实战视频

[@gregisenberg](https://x.com/@gregisenberg)

的油管频道最近很高产，各种爆款视频都有。之前请 Claude Code 作者老鲍的那期，被 OpenClaw 的热度压了一头，他后面也第一时间补拍了 OpenClaw 的视频

​但这阵子所有视频里，我个人最喜欢的还是这期 Vibe Marketing。毕竟我们玩 Vibe Coding 很久了，Vibe Marketing 才是真正能「落地赚钱」的那一块。

昨天通勤的时候，我把视频完整看了一遍，随手记了些要点。

## 

​整体方法论

先别急着乱 prompt，一上来至少花一小时做深度研究：用 Perplexity MCP、Firecrawl、Playwright 把市场、竞品、空白点和所有素材抓干净，再动笔写任何文案或页面，这是避免 AI slop 的前提。​

把「Skills」当成给模型的操作手册：比如定位 skill、直效文案 skill、前端设计 skill、Lead Magnet skill、Orchestrator skill，把自己的专业框架和审美写进 skill，让模型只负责执行，这样输出会稳定贴近专家水准。

## 

实战：从虚构代理到完整 Funnel

案例选的是「给年营收 200–1000 万美元的无聊本地生意（plumber / HVAC 等）做 AI 营销代理」。先用定位 skill 列一堆角度，再让一个任务型 agent 扮演 Greg 出来拍板，最后收敛到「Boring Money」这种反传统代理叙事。

​在研究和定位打牢的基础上，用直效文案 skill 写首页文案，再用 Playwright MCP 抓竞品截图，配合 Anthropic 的前端设计 skill 生出一个不带「AI 审美」的落地页（反紫渐变、反可爱 emoji），把差异点、价格锚点、创始人故事都讲清楚。

## 

Lead Magnet 与转化机制

Orchestrator skill 负责判断「下一步该干嘛」，它会意识到你缺的是 Lead Magnet、邮件序列和流量策略，然后自动调 Lead Magnet skill 生成多个创意，再打分挑一个最稳的，比如「5 分钟营销体检清单」这种工具型诱饵。

​Claude Code 直接把这份体检清单做成网页右下角的弹出问卷组件，而不是去接第三方表单。问题覆盖响应速度、自动跟进、报价到成交转化、评论系统等，填完给一个评分和诊断，同时收邮箱、顺势引导预约电话。

​

## 

流量与内容系统

用 Keyword Research skill 做底层关键词和城市场景分析，找「能快速打下来的」长尾程序化 SEO 机会，比如「HVAC marketing in Phoenix」。再用 SEO 内容 skill 批量生成本地化长文，把前面做好的 Lead Magnet 全部嵌进去。

​用 DTC Ads skill 借鉴消费品直效广告的结构和钩子，设计一整套广告策略，然后用 Remotion 在终端里程序化生成多尺寸视频广告（横、竖、方），支持自定义字体、配色和素材图，一次 prompt 就能打出几十条创意做测试。

​

## 

工具栈与成本

整个 MCP/工具栈刻意保持「很瘦」：Perplexity 做研究，Firecrawl 抓取并结构化网页，Playwright 做浏览器自动化和竞品截图，Glyph / Nano Banana Pro 生静态图，Remotion 生视频，尽量不装一堆用不到的 MCP。

整场实战几乎都在 Claude Code 这一个环境里完成：研究、技能调用、文案、设计、SEO、广告到部署脚本一条龙。他提到自己用的是 Claude Code 的 200 美元/月封顶套餐，日常高强度的「vibe coding + vibe marketing」也没把配额用满。

## 

具体实施步骤

1.  研究：把市场和竞品掏干净
 

- 用 Perplexity MCP 做深度调研：行业现状、目标客群（比如年营收 200–1000 万美金的 plumber/HVAC）、主流报价、常见痛点。​​
 
- 用 Firecrawl 抓取头部和细分对手的网站，把他们的定位、offer、价格结构和案例结构化出来。​
 
- 用 Playwright 做自动化浏览和截图，把典型 landing page/广告创意批量存好，方便后面做差异化。​​
 

2\. 定位 + Skills：把“脑子里的方法”固化下来

- 写一个 Positioning Skill：明确你要服务的细分（如「Boring Money」本地生意）、他们讨厌什么代理话术、你解决什么具体结果。​
 
- 写 Direct Response Copy / Landing Page Skill：把你一套成型的直效文案结构写进去（主标题、承诺、证明、报价、FAQ、创始人故事等）。​​
 
- 写 Orchestrator Skill：约定「先研究→再定位→再文案→再设计→再 Lead Magnet→再流量」，让它负责检查现在缺哪一块、调用哪个 skill。​
 

3\. 页面与 Lead Magnet：搭好转化骨架

- 在 Claude Code 里用定位 skill + 文案 skill 生成首页/主着陆页文案，然后参考竞品截图，用前端设计 skill 出一个不“AI 审美”的设计稿。​
 
- 用 Playwright MCP 或自己的前端脚本实际把页面搭出来（哪怕是简单 Tailwind/Next.js 模板），先确保能跑。​​
 
- 让 Orchestrator Skill 检查「漏了什么」，通常会发现需要 Lead Magnet、邮件序列、预约流。​
 
- 用 Lead Magnet Skill 生成 3–5 个诱饵创意（如「5 分钟营销体检清单」），评分选一个，然后在 Claude Code 里把它直接做成悬浮问卷组件：问题、评分逻辑、邮件收集、预约按钮一次写好。​
 

4\. 流量与内容系统：让漏斗真正跑起来

- 用 Keyword Research Skill 针对目标城市/行业做长尾关键词表，标记“容易赢 + 有商业意图”的词。​​
 
- 用 SEO 内容 Skill 为这些关键词批量生成本地长文，每篇都嵌入你的 Lead Magnet 和预约 CTA。​
 
- 用 DTC Ads Skill 设计一套吸客广告脚本和文案，再用 Remotion 在 CLI 里程序化生成多尺寸视频/图像广告，导出后丢进你常用的 Ads 平台做小预算测试。​​
 
- 建一个简单的「反馈–迭代循环」：每周看一次哪些关键词/广告带来表单和电话，把表现好的那批交给 Orchestrator Skill，自动建议下一步优化（加预算、复用创意、扩展相邻关键词等）。​
 

原视频在这：

[https://www.youtube.com/watch?v=fVUlrpaWNxg](https://www.youtube.com/watch?v=fVUlrpaWNxg)