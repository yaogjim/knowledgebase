---
title: "MiniCPM-V 4.5 : 高刷视频理解新突破"
source: "https://x.com/aiwarts/status/1961100154746146936"
author:
  - "[[@aiwarts]]"
published: 2025-08-29
created: 2025-08-29
description:
tags:
  - "@aiwarts #高刷视频理解 #MiniCPM-V4.5 #多模态模型"
---
**卡尔的AI沃茨** @aiwarts [2025-08-28](https://x.com/aiwarts/status/1961100154746146936)

大多数多模态模型，用的都是每秒一帧的抽帧方式来理解视频。面壁现在提升了20倍，1秒20帧画面，实现了高刷视频理解 @OpenBMB

在OpenCompass上，超越了GPT-4o、Gemini-2.0-Pro 和 72B的Qwen2.5-VL。在 OmniDocBench 榜单上，MiniCPM-V 4.5的 OverallEdit、TextEdit、TableEdit 三项指标取得了通用多模态模型同级别的 SOTA

看看它的实际表现👇

（1/4）

![Image](https://pbs.twimg.com/media/Gzc6LutaYAAWRJ2?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gzc6Lu4a0AAkpMu?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/Gzc6Lu3bUAAE2dW?format=jpg&name=large)

---

**卡尔的AI沃茨** @aiwarts [2025-08-28](https://x.com/aiwarts/status/1961100159640817834)

🔗 http://github.com/OpenBMB/MiniCPM-o…

🔗 http://huggingface.co/openbmb/MiniCPM-V-4\_5…

🔗 http://modelscope.cn/models/OpenBMB/MiniCPM-V-4\_5…

---

**卡尔的AI沃茨** @aiwarts [2025-08-28](https://x.com/aiwarts/status/1961100244521013522)

先给 MiniCPM-V 4.5 一段行车记录仪的视频，让它记录下沿途所有出现过的店铺名称

MiniCPM-V 4.5 能准确识别出了那些高速掠过的招牌，甚至连一些角度刁钻的小字都捕捉到了。

（2/4）

---

**卡尔的AI沃茨** @aiwarts [2025-08-28](https://x.com/aiwarts/status/1961100306240184786)

第二个 case 是速算挑战，前段时间我还去炸鱼小学生，简单来说屏幕上会不停刷新数字、公式和符号，构成一道数学题。我们需要在炒鸡短的时间内看清题目并给出答案。

（3/4）

---

**卡尔的AI沃茨** @aiwarts [2025-08-28](https://x.com/aiwarts/status/1961100371218350580)

第三个case是快闪广告，汉堡、薯条、派、可乐等商品图片以极快的速度轮播出现。

问题是，可乐是在第几个出现的？

一个低抽帧的模型，能告诉我视频里出现了可乐，但丢失了中间的关键帧，看到的是一堆散落的素材，会搞错商品的出现顺序。高帧的MiniCPM-V

---

**Tz** @Tz\_2022 [2025-08-28](https://x.com/Tz_2022/status/1961103752796262806)

这个我落地业务还真可能用得上。。。它对显卡显存要求高么？能在16GB/24GB的家用机显卡上跑么？

---

**卡尔的AI沃茨** @aiwarts [2025-08-28](https://x.com/aiwarts/status/1961104750029701372)

8B大小vllm 24GB能跑得动