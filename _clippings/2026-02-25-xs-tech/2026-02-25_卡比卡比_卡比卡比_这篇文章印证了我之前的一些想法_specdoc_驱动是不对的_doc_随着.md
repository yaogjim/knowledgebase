---
title: "2026-02-25_卡比卡比_卡比卡比_这篇文章印证了我之前的一些想法_specdoc_驱动是不对的_doc_随着"
source: "https://x.com/jakevin7/status/2026238245609365939"
author:
  - "[[@卡比卡比]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@卡比卡比"
  - "ai"
  - "agent"
---

# 卡比卡比 这篇文章印证了我之前的一些想法： - specdoc 驱动是不对的，doc 随着

**卡比卡比**

这篇文章印证了我之前的一些想法： - spec/doc 驱动是不对的，doc 随着代码的增加非常容易过失，spec 这种硬约束容易误导 agent。设计文档、架构图、onboarding wviki--几乎一写出来就过时了。 - 应该是描述需求，让 agent 起草 spec，再拆分 task - 进行实时的review，遇到了哪些原计划没考虑的约束及时反馈。 - 文章里没提到的一点是，代码文档很重要。代码文档本身可以作为一个渐进式的知识系统。 - 架构要作为软性约束，不要用文档做硬性约束。

* * *

### 热门回复

**@玩个锤子** ♥ 208 · 💬 17

由于某 a 字母开头的公司实在是不当人，然后我们捣鼓了一下 codex 转 claude code。 然后一不小心就搞好了，思考，调用 tool，缓存都没问题～ 只需要在 packyapi 中将令牌分组切换到 cxtocc 中即可开始使用～ 此分组仅 0.25 倍，便宜的和不要钱一样

**@Yuhang** ♥ 157 · 💬 10

一觉醒来，Claude 官方推出了 Remote Control，Cloudflare 重写了 Next.js，Cursor 支持了 Cloud computers，Notion 发布了 Custom Agents

**@0xMartin | St₳ke with** ♥ 6 · 💬 2

如果spec是硬约束，那交付物就应该是spec而不是代码，代码只是spec通过agent编译后的产物了

**@卡比卡比** ♥ 6 · 💬 2

表述可能让人误解了。我的意思是很多人希望拿 spec 作为硬约束，让 spec 产出稳定的成果，sped 在人类编码时代是这样的对吧。 但是这在 AI Agent 时代是行不通的，spec 对于 AI 的约束里很低，不能寄托spec像人类时代一样发挥硬约束。

**@Bhe hontyu** ♥ 4 · 💬 0

spec就应该是 ai 沟通并填充的，但是你一开始反对的spec驱动并不成立，spec并不可能一上来就是对的，需要调整并不影响spec驱动这个大前提