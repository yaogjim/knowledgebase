---
title: "使用 ggml-org/gpt-oss-20b在macOS上本地运行LLaMA"
source: "https://x.com/simonw/status/1957880963666702466"
author:
  - "[[@simonw]]"
published: 2025-08-20
created: 2025-08-20
description:
tags:
  - "@simonw #llama #LLM #苹果硅 #macos #AI"
---
**Simon Willison** @simonw 2025-08-19

  
在 macOS 上开始使用一个不错的本地 LLM（如果你有大约 12GB 的可用磁盘空间和内存）的最快方法之一是——使用 llama - server 和 gpt - oss - 20b：

使用 brew 安装 llama.cpp

llama 服务器 -hf ggml-org/gpt-oss-20b-GGUF

\--ctx-size 0 --jinja -ub 2048 -b 2048 -ngl 99 -fa （此内容看起来像是特定命令行参数，直接保留英文原样也是常见做法，若强行翻译会失去其专业性和准确性，以下是勉强翻译）

\--上下文大小 0 --金贾 -上边界 2048 -边界 2048 -非图形层 99 -文件格式相关（这里的“jinja”和“fa”等可能是特定领域未明确的术语，翻译可能不准确）

> 2025-08-19
> 
>   
> 使用 gpt-oss 搭配 llama.cpp 的终极指南
> 
> \- 可在任何设备上运行
> 
> \- 支持英伟达、苹果、AMD 等
> 
> \- 支持高效的 CPU 卸载
> 
> \- 当今最轻量级的推理堆栈
> 
> https://github.com/ggml-org/llama.cpp/discussions/15396…
> 
> ![Screenshot of a chat interface with filename ](https://pbs.twimg.com/media/GyvKRJMa0AA_Caj?format=jpg&name=large)

---

**Simon Willison** @simonw [2025-08-19](https://x.com/simonw/status/1957881073159094452)

  
我的博客上有更多笔记

---

**accelerate(e/acc)** @EAccelerate\_42 [2025-08-19](https://x.com/EAccelerate_42/status/1957883338779422960)

  
不行，对于苹果硅芯片来说，mlx 是唯一有意义的方式，它快 50%到 80%

---

**Simon Willison** @simonw [2025-08-19](https://x.com/simonw/status/1957888893908656379)

  
在我的 Mac 上，这些 GGUF 格式文件的处理速度是每秒 82 个 token。我试过的 MLX 格式文件，其处理速度是每秒 62 个 token，但它是 8 位量化的，而且文件大得多（22GB）

gpt-oss 针对 MXFP4 进行了优化，而我认为 MLX 尚不支持该功能

---

**kevin** @kswzzl [2025-08-19](https://x.com/kswzzl/status/1957898542338527272)

  
感谢这篇博客文章。我认为 llama - server 默认端口是 8080，而不是 8000。