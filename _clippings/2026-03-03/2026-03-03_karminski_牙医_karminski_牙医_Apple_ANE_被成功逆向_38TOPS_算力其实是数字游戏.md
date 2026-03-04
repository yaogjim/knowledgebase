---
title: "2026-03-03_karminski_牙医_karminski_牙医_Apple_ANE_被成功逆向_38TOPS_算力其实是数字游戏"
source: "https://x.com/karminski3/status/2028287465799442770"
author:
  - "[[@karminski-牙医]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "#ANE"
  - "#CoreML"
  - "x"
  - "@karminski-牙医"
---

# karminski-牙医 Apple ANE 被成功逆向! 38TOPS 算力其实是数字游戏

**karminski-牙医**

Apple ANE 被成功逆向! 38TOPS 算力其实是数字游戏? 刚刷到博主 maderix 开源了个硬核项目: 逆向 Apple 的私有 API, 绕过 CoreML, 直接在 Apple Neural Engine (ANE) 上实现了神经网络训练! 等会? 啥是 ANE? ANE是苹果芯片内部的神经网络加速单元, M4 上目前已经是 16 核的运算单元了, 官方宣称性能有 38 TOPS. 但一直是黑盒, 你只能通过 CoreML 框架去调用, 没有任何公开接口, 没文档, 没 ISA, 啥都没. 于是这哥们把 CoreML 这层壳给扒了. 用了一些逆向手段(比如 dyld\_info 扫描, method swizzling 拦 CoreML 等), 最终逆向出了完整的编译运行流程. 最关键的是, 他还搞通了内存编译路径, 可以直接在内存里把 MIL (类似 NVIDIA 的 PTX) 编译成 ANE 二进制. (方便用ANE训练大模型了) 然后逆向的过程中发现了很多爆炸性信息: 首先ANE本质上是个卷积引擎, 不是矩阵乘法引擎. 同样的计算, 改写成卷积运算吞吐量直接翻 3 倍! (Apple 自己的 ml-ane-transformers 参考实现里就暗示了这个模式, 但从来没有明说) 第二, ANE 内部有大约 32MB 的 SRAM. (做矩阵乘法 scaling 测试发现的性能断崖推测出来了) 第三, 单个算子只能用到 ANE 峰值性能的约 30%. 因为 ANE 的 16 个核是流水线式的, 你只提交一个操作, 大部分核在空转. 得把 16-64 个操作链在一张计算图里一次性提交, 不同的核同时处理图里不同阶段的操作, 利用率才能拉满到 94%. 最后也是最炸裂的发现: "38 TOPS" 是个数字游戏. 作者用 FP16 和 INT8 跑了完全相同的操作, 吞吐量一样. 结论是 ANE 在执行 INT8 时会先反量化到 FP16 再计算, 苹果的 "38 TOPS INT8" 就是拿 19 TFLOPS FP16 乘了个2的数字游戏. 真实峰值就是 19 TFLOPS FP16. 另外个细节: ANE 有硬件级电源门控, 空闲时功耗真的是 0mW, 不是低功耗待机, 是真的完全断电零泄漏, 这电源管理真的牛X. 移动端嗷嗷友好. 当然最主要的其实还是这个过程很有学习价值, 两个blog信息量超大, 我这里写不下, 建议感兴趣的同学直接读原文 inside-the-m4-apple-neural-engine, 我这只能抛砖引玉: 项目地址: [http://github.com/maderix/ANE](http://github.com/maderix/ANE) 博客 Part 1 (逆向工程): [http://maderix.substack.com/p/inside-the-m4-apple-neural-engine…](http://maderix.substack.com/p/inside-the-m4-apple-neural-engine) 博客 Part 2 (基准测试): [http://maderix.substack.com/p/inside-the-m4-apple-neural-engine-615…](http://maderix.substack.com/p/inside-the-m4-apple-neural-engine-615) [#ANE](/hashtag/ANE?src=hashtag_click) [#CoreML](/hashtag/CoreML?src=hashtag_click) [#AppleSilicon](/hashtag/AppleSilicon?src=hashtag_click) [#NPU训练](/hashtag/NPU训练?src=hashtag_click) [#KCORES](/hashtag/KCORES?src=hashtag_click)

![图片](https://pbs.twimg.com/media/HCXssZTa0AAO4RQ?format=jpg&name=large)

* * *

### 热门回复

**@Ridge** ♥ 2.1K · 💬 40

Choose between dragon wisdom or cherry blossom renewal crafted into Ridge's patented slim design.

**@CoinTracker** ♥ 282 · 💬 14

All your crypto in one place — track your portfolio and file taxes in minutes. Try CoinTracker today.

**@ムリ** ♥ 21 · 💬 1

看这个结构基本可以看出来是为了图像的AI模型设计的 拍照视频什么的 并没有为LLM推理做什么专门优化

**@OwnYourAss** ♥ 3 · 💬 1

Apple设计好像还停留在convolution时代。有点落后了。

**@%%** ♥ 0 · 💬 1

@grok 看一下这篇文章 解释一下这是发生什么大事 对于AI来讲