---
title: "2026-02-26_Percy_Liang_Percy_Liang_These_days_I_m_much_more_excited"
source: "https://x.com/percyliang/status/2026786262737396144"
author:
  - "[[@Percy Liang]]"
published: 2026-02-26
created: 2026-02-26
description:
tags:
  - "#1"
  - "x"
  - "@Percy Liang"
  - "about"
---

# Percy Liang These days, I'm much more excited

**Percy Liang**

These days, I'm much more excited about dataset releases than model releases. Models come and go and don't compose, whereas good datasets are more enduring and can be studied, used, revised to create better models more broadly. Excited about these 155K coding agent trajectories...just SFT'ing on this data improves SWE-bench Verified massively (23% -> 59.4%).

![图片](https://pbs.twimg.com/media/HCBpyd8aAAAYkkh?format=jpg&name=large)

> **@togethercompute**
> 
> We’re open-sourcing CoderForge-Preview — 258K test-verified coding-agent trajectories (155K pass | 103K fail). Fine-tuning Qwen3-32B on the passing subset boosts SWE-bench Verified: 23.0% → 59.4% pass@1, and it ranks #1 among open-data models ≤32B parameters. Thread on the

![Square profile picture](https://pbs.twimg.com/profile_images/1982998729931042817/R88YrV4r_normal.jpg)![引用图片](https://pbs.twimg.com/media/HCBpyd8aAAAYkkh?format=jpg&name=large)

* * *

### 热门回复

**@Lucas Beyer (bl16)** ♥ 700 · 💬 27

soooo... how many papers do we think are invalidated by this? And now think about how many other bugs there must be in any re-implementations of... basically anything.

**@Mayank Mishra** ♥ 488 · 💬 11

We identified an issue with the Mamba-2 initialization in HuggingFace and FlashLinearAttention repository (dt\_bias being incorrectly initialized). This bug is related to 2 main issues: 1. init being incorrect (torch.ones) if Mamba-2 layers are used in isolation without the

**@Albert Gu** ♥ 306 · 💬 2

many papers have reported Mamba results inconsistent with what we found internally. we finally traced down the cause, which comes from wrong initializations in very popular implementations (HF and FLA) the initialization makes a huge difference - see @MayankMish98 's report!

**@Tri Dao** ♥ 251 · 💬 1

This was a wild bug hunt, weeks of effort from @MayankMish98 to track down. The wrong init of Mamba2 in many reimplementations causes the layer to decay its states too quickly, focusing in short context instead. Pretraining is mostly about getting these little things right

**@Nathan Lambert** ♥ 21 · 💬 0

Its true. The ratio of models/dataset released is totally out of wack. Many researchers should care about data more for lasting impact (in real systems).