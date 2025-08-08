---
title: "英伟达开源6亿参数ASR模型Parakeet TDT 0.6B V2"
source: "https://x.com/rohanpaul_ai/status/1920069397277774228"
author:
  - "[[@rohanpaul_ai]]"
created: 2025-05-09
description:
tags:
  - "@rohanpaul_ai #ASR #自动语音识别 #开源 #人工智能 #AI #英伟达"
---
**Rohan Paul** @rohanpaul\_ai [2025-05-07](https://x.com/rohanpaul_ai/status/1920069397277774228)

  
哇哦.. 现在你可以用一个完全开源的模型在 1 秒内转录 60 分钟的音频 🤯 @英伟达刚刚开源了 Parakeet TDT 0.6B V2，这是一个拥有 6 亿参数的自动语音识别（ASR）模型，在@huggingface Open-ASR 排行榜上以 RTFx 3380 名列前茅。它在 CC-BY-4.0 许可下开源，可供商业使用。 ⚙️ 详情

→ 该模型基于 FastConformer 编码器 + TDT 解码器构建，能够全注意力处理长达 24 分钟的音频片段，并输出带有标点、大写以及准确的单词/字符/片段时间戳的内容。

→ 在开放 ASR 排行榜上，批量大小为 128 时，它实现了 3380 的实时因子（RTFx），但性能会随音频时长和批量大小而变化。

→ 使用 128 个 A100 GPU 进行 150K 步训练，然后在 500 小时的高质量人工转录英语数据上进行微调。

→ 总训练数据跨度为 120K 小时，结合了人工标注和伪标注来源，包括 LibriSpeech、Fisher、YTC、YODAS 等。

→ 可通过 NVIDIA NeMo 获取，针对 GPU 推理进行了优化，可通过 pip install -U nemo\_toolkit\['asr'\]进行安装。

→ 与 Linux 兼容，运行在安培、布莱克韦尔、霍珀、伏特 GPU 架构上，最低需要 2GB 内存。

→ 用于训练的谷仓数据集将在 2025 年国际语音通信协会（Interspeech）会议后公开。

![Image](https://pbs.twimg.com/media/GqV07AeXcAA9klA?format=jpg&name=large)

---

**Rohan Paul** @rohanpaul\_ai [2025-05-07](https://x.com/rohanpaul_ai/status/1920069784730739130)

  
如何使用此模型：

要训练、微调模型或使用该模型进行体验，你需要安装 NVIDIA NeMo。建议在安装最新版本的 PyTorch 之后再安装它。

![Image](https://pbs.twimg.com/media/GqV1RjcXwAAsWJw?format=jpg&name=large)

---

**PDF GPT** @pdfgptsupport

  
这是我用于审查报告的最喜欢的人工智能工具。

只需上传一份报告，请求生成一份摘要，然后在几秒钟内即可获得。

它类似于 ChatGPT，但专为文档打造。

免费试用。

---

**Rohan Paul** @rohanpaul\_ai [2025-05-07](https://x.com/rohanpaul_ai/status/1920069819048620326)

---

**Rohan Paul** @rohanpaul\_ai [2025-05-07](https://x.com/rohanpaul_ai/status/1920069914800390283)

![Image](https://pbs.twimg.com/media/GqV1aC3XcAAI7e4?format=png&name=large)

---

**bhaga.sol** @BhagaTheKey [2025-05-08](https://x.com/BhagaTheKey/status/1920367390044389867)

  
罗汉，请进行设置，并将使用链接发送给我们，我有很多音频需要转录

---

**Rohan Paul** @rohanpaul\_ai [2025-05-08](https://x.com/rohanpaul_ai/status/1920490072823984380)

---

**Amit Wani** @mtwn105 [2025-05-09](https://x.com/mtwn105/status/1920680143149756697)

  
支持哪些语言

---

**Rohan Paul** @rohanpaul\_ai [2025-05-09](https://x.com/rohanpaul_ai/status/1920767563803344911)

  
英语

---

**Nabil Hunt 𝕏** @NabilHunt [2025-05-09](https://x.com/NabilHunt/status/1920762340028367354)

  
它将如何处理其中包含混合语言的音频？

---

**Rohan Paul** @rohanpaul\_ai [2025-05-09](https://x.com/rohanpaul_ai/status/1920767542928257048)

  
仅英文

---

**Thread Reader App** @threadreaderapp [2025-05-08](https://x.com/threadreaderapp/status/1920361400502747317)

  
你的推文正在疯传！#热门展开 https://threadreaderapp.com/thread/1920069397277774228.html?utm\_campaign=topunroll… 🙏🏼 @hettinga 为 🥇 展开