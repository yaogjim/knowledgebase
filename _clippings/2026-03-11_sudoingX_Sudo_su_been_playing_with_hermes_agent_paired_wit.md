---
title: "2026-03-11_sudoingX_Sudo_su_been_playing_with_hermes_agent_paired_with"
source: "https://x.com/sudoingX/status/2030943745298878557"
author:
  - "[[@sudoingX]]"
published: 2026-03-11
created: 2026-03-11
description:
tags:
  - "x"
  - "@sudoingX"
  - "https"
  - "tok/s"
---

# Sudo su: been playing with hermes agent paired with qwen 3

**Sudo su**

been playing with hermes agent paired with qwen 3.5 dense 27B on my single 3090 since last night. there is something about this harness that caught me and i think i know what it is.

i've now run five qwen configs on consumer hardware:

35B MoE (3B active) -- 112 tok/s flat across 262K context, 1x 3090

27B dense -- 35 tok/s, zero degradation across the same range, 1x 3090

qwopus 27B (opus distilled) -- 35.7 tok/s, same architecture, different brain

80B coder -- 46 tok/s on 2x 3090s, oneshotted a 564 line particle sim

80B coder -- 1.3 tok/s on 1x 3090, bleeding through RAM because it didn't fit but it still ran

with same benchmarks. same prompts. same quant where possible. every config is documented. i know these models.

and hermes agent is the first harness that feels like it respects that work. tool calls show inline with execution time. nvidia-smi 0.2s. write\_file 0.7s. you see exactly what the agent is doing and how long each step takes. no mystery. no black box. no tool call failures so far and i've been pushing it.

most agent frameworks feel like you're watching a spinner and hoping. hermes shows the work. that transparency changes how you trust the output.

once you use it you see the UX decisions are not accidental. [@Teknium](/Teknium)

and the nous team built this like engineers who actually use their own tools. 80 skills. 29 tools. persistent memory. context compression. runs clean on a single consumer GPU.

![图片](https://pbs.twimg.com/media/HC5yxu4bAAADxGx?format=jpg&name=large)![图片](https://pbs.twimg.com/media/HC5yzOua8AEYBw7?format=jpg&name=large)![图片](https://pbs.twimg.com/media/HC5y1cDakAAS_EO?format=jpg&name=large)

[![视频](https://pbs.twimg.com/amplify_video_thumb/2030943377240608768/img/Fd425ah1JlkXuawL.jpg)](https://x.com/sudoingX/status/2030943745298878557)[![视频](https://pbs.twimg.com/amplify_video_thumb/2030685251157327872/img/0ttWIB8CLB9emrjD.jpg)](https://x.com/sudoingX/status/2030943745298878557)

> **@sudoingX**
> 
> okay the fuss around hermes agent is not just air. this thing has substance. installed it on a single RTX 3090 running Qwen 3.5 27B base (Q4\_K\_M, 262K context, 29-35 tok/s). fully local. my machine my data. first thing i did was tell it to discover itself. find its own model x.com/sudoingX/statu…

![引用图片](https://pbs.twimg.com/media/HC5yxu4bAAADxGx?format=jpg&name=large)![引用图片](https://pbs.twimg.com/media/HC5yzOua8AEYBw7?format=jpg&name=large)![引用图片](https://pbs.twimg.com/media/HC5y1cDakAAS_EO?format=jpg&name=large)

* * *

### 热门回复

**@Sudo su** ♥ 61 · 💬 7

for those asking what's the best model to run on a single 3090 right now. i've tested enough to have an answer.

qwen 3.5 27B dense Q4\_K\_M. 35 tok/s. 262K context. 16.7GB VRAM. no degradation.

llama server flags:

llama-server -m Qwen3.5-27B-Q4\_K\_M.gguf -ngl 99 -c 262144 -np 1

**@Sudo su** ♥ 36 · 💬 6

people ask why i ran the 80B on a single 3090 when it clearly doesn't fit.

because that's how you learn what your hardware actually does under pressure. 20 layers on GPU, rest bleeding through system RAM. 1.3 tok/s. painful. but it still generated working code.

added a second

**@Sudo su** ♥ 36 · 💬 3

the MoE runs 3x faster but only activates 3B of 35B params per token. the dense activates all 27B every token. slower but every token carries more weight.

for coding the dense wrote fewer lines but completed the task with zero intervention. MoE wrote more code but needed

**@Sudo su** ♥ 19 · 💬 1

qwopus is claude opus distilled into qwen 3.5 27B. same architecture, same speed, completely different outputs.

base qwen oneshotted octopus invaders. 1,827 lines. ran on first load. qwopus wrote more "elegant" code but left broken files and needed manual fixes.

distillation

**@Nyk** ♥ 6 · 💬 2

You got me, just downloaded hermes

---

<br>

> [!abstract]+ 对话记录
>
> 共 2 条消息

---

## 💬 对话记录

### 📋 提示词模板: 结构化

> *(已省略完整内容)*

### 🤖 AI

**主旨概括：**  
作者在单张 RTX 3090 上测试了 Hermes Agent 搭配多种 Qwen 3.5 模型后认为，**Hermes 真正突出的不是 “能跑”，而是 “透明、可靠、尊重用户调试过程”**。在本地部署、消费级硬件环境下，它把模型执行过程清楚展示出来，显著提升了可用性和信任感。

---

## 1. 作者测试了多种 Qwen 配置，硬件表现有明确结论
作者表示，自己已经在消费级硬件上跑过**5 种 Qwen 配置**，并且做了统一对比（相同提示词、尽量相同量化、都有记录）：

- **Qwen 3.5 35B MoE（每 token 激活 3B）**
  - **单张 3090**
  - **112 tok/s**
  - 在**262K 上下文**下速度基本不掉

- **Qwen 3.5 27B Dense**
  - **单张 3090**
  - **35 tok/s**
  - 同样在**262K 上下文**下几乎无性能衰减

- **Qwopus 27B（Opus 蒸馏版）**
  - **35.7 tok/s**
  - 与 27B dense 架构相同，但 “思路 / 风格” 不同

- **80B Coder**
  - **双 3090：46 tok/s**
  - 曾 “一次生成成功” 一个**564 行的粒子模拟程序**

- **80B Coder**
  - **单张 3090：1.3 tok/s**
  - 因显存不够，部分内容溢出到系统内存（RAM），但**仍然能运行并完成相同基准测试**

**一句话理解：**作者不是随便试用，而是做了比较系统的本地硬件实测。

---

## 2. Hermes Agent 最打动作者的，是 “过程可见”
作者认为，Hermes Agent 是第一个让他觉得**真正尊重这些测试和调优工作**的 agent 框架，原因在于它足够透明：

- 工具调用会**直接显示在执行流程里**
- 每一步都有**清晰耗时**
  - 例如：
    - `nvidia-smi`：**0.2 秒**
    - `write_file`：**0.7 秒**
- 用户可以明确看到：
  - agent 做了什么
  - 每一步花了多久
  - 不是 “黑箱” 操作

作者强调，很多 agent 框架给人的感觉像是：
- 只看到一个加载中的转圈
- 不知道内部到底在干什么
- 出错也不容易定位

而 Hermes 的特点是：**“把过程展示出来”**。  
这会直接改变用户对输出结果的信任方式。

**通俗例子：**  
就像让一个人帮你修电脑 ——  
- 有些工具只告诉你 “正在处理中”，你只能干等；  
- Hermes 则像边修边告诉你：“我刚检查了显卡，用了 0.2 秒；我刚写入了配置文件，用了 0.7 秒。”  
这样你更容易判断它是不是靠谱。

---

## 3. 作者认为 Hermes 的产品设计不是偶然，而是 “真正在用工具的人做出来的”
作者提到，使用一段时间后会发现，Hermes 的交互体验（UX）不是随便拼出来的，而是**懂工程、自己也真正使用这些工具的团队做出来的**。他特别点名了**@Teknium 和 Nous 团队**。

文中提到 Hermes 的一些关键能力：

- **80 个技能（skills）**
- **29 个工具（tools）**
- **持久记忆（persistent memory）**
- **上下文压缩（context compression）**
- 可以在**单张消费级 GPU**上干净运行

作者的核心态度是：  
Hermes 不只是 “功能多”，而是这些功能被组织得更清晰、更可信、更适合本地玩家和工程用户。

---

## 4. 单张 3090 上，作者给出的最佳模型推荐
在评论区，作者直接给出自己对 “单张 3090 现在最值得跑什么模型” 的答案：

- **Qwen 3.5 27B Dense Q4_K_M**
  - **35 tok/s**
  - **262K context**
  - **16.7GB 显存占用**
  - **无明显性能衰减**

并附上启动参数示例：

```bash
llama-server -m Qwen3.5-27B-Q4_K_M.gguf -ngl 99 -c 262144 -np 1
```

**结论很明确：**  
如果你只有**1 张 3090**，作者认为目前最均衡、最推荐的是**Qwen 3.5 27B Dense Q4_K_M**。

---

## 5. 作者对不同模型类型的实际观察：MoE 更快，Dense 更稳
作者还解释了为什么会同时测试**MoE**和**Dense**：

- **MoE**：
  - 速度快很多，约**3 倍**
  - 但每个 token 只激活**35B 参数中的 3B**
- **Dense**：
  - 每个 token 都激活完整**27B 参数**
  - 虽然更慢，但每个 token 的 “信息密度 / 权重” 更高

在编码任务上的体验是：

- **Dense**
  - 写的代码行数更少
  - 但能**零人工干预完成任务**

- **MoE**
  - 写的代码更多
  - 但需要更多人工修正或介入

**通俗理解：**  
MoE 像是 “写得快、铺得多”；  
Dense 像是 “写得慢一点，但更扎实”。

---

## 6. 蒸馏模型 Qwopus：风格更优雅，但稳定性不如原版
作者还比较了**Qwopus 27B**（Claude Opus 蒸馏到 Qwen 3.5 27B）与原版 Qwen：

- 两者：
  - **同架构**
  - **速度差不多**
- 但输出风格明显不同

具体案例：

- **原版 Qwen**
  - 一次生成完成了**Octopus Invaders**
  - 代码量**1,827 行**
  - **首次运行就成功**

- **Qwopus**
  - 代码风格更 “优雅”
  - 但留下了**损坏 / 不完整文件**
  - 需要**手动修复**

**作者的意思是：**  
蒸馏模型可能更有 “风格”，但不一定更适合你真正想完成的任务。  
在实际 coding 场景里，**能不能一次跑通**比 “写得漂不漂亮” 更重要。

---

## 总结
这篇文章的重点不是单纯夸模型性能，而是强调：  
**Hermes Agent 在本地 AI 工作流里，靠 “透明的执行过程 + 稳定的工具调用 + 对消费级硬件友好”，带来了比很多 agent 框架更高的可信度和可用性。**

同时，作者基于实测给出几条实用结论：

- **单张 3090 最推荐：Qwen 3.5 27B Dense Q4_K_M**
- **MoE 更快，但 Dense 在编码任务中更稳**
- **80B 即使塞不进单卡也能跑，只是会非常慢**
- **蒸馏模型不一定更实用，原版模型有时反而更能一次完成任务**

---

