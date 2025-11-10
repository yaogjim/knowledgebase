---
title: "#llama.cpp "
source: "https://x.com/ggerganov/status/1961136036097991000"
author:
  - "[[@ggerganov]]"
published: 2025-08-29
created: 2025-08-29
description:
tags:
  - "@ggerganov #本地运行 #开源AI #GPT-OSS"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**Georgi Gerganov** @ggerganov 2025-08-26

  
要在 16GB 的 Mac 上运行 gpt-oss-20b，请使用以下命令：

使用 brew 安装 llama.cpp

llama 服务器 -hf ggml-org/gpt-oss-20b-GGUF --n-cpu-moe 12 -fa -c 32768 --jinja --no-mmap

然后在 http://127.0.0.1:8080 打开浏览器。

> 2025-08-26
> 
>   
> 奥 llama 刚刚为其 Mac 应用添加了一个用户界面，这样你就可以在离线状态下运行我们的开源权重模型了——这对火车和飞机旅程来说非常实用。我之前为此使用的是 macai，但这个设置起来要简单得多。
> 
> 我在拥有 36GB 内存的 MacBook Pro 上运行 gpt - oss:20b 模型。这是个不错的模型，而且
> 
> ![Image](https://pbs.twimg.com/media/GzSIeeuaMAA-3Cm?format=jpg&name=large)

---

**Jan P. Harries** @jphme [2025-08-28](https://x.com/jphme/status/1961136505667145859)

  
llama.cpp 是否支持 gpt-oss 的响应 API？ 👀

---

**Georgi Gerganov** @ggerganov [2025-08-28](https://x.com/ggerganov/status/1961136686500286737)

  
不

---

**Peter Dedene** @peterdedene [2025-08-28](https://x.com/peterdedene/status/1961137693829554555)

  
一个 200 亿参数的模型在 16GB 内存的苹果电脑上流畅运行。就在一年前，这还会是科幻小说里的情节。

llama.cpp 中的优化给很多人带来了启发。

---

**Ptimizer** @ptimizeroracle [2025-08-28](https://x.com/ptimizeroracle/status/1961146128138686555)

  
是的，但是你的使用场景是什么？20B 适用于什么？

---

**南北西东** @S\_N\_W\_E [2025-08-28](https://x.com/S_N_W_E/status/1961141067388260415)

  
本地模型的优化速度简直惊人。一条简单的 brew install 命令就能让一个 200 亿参数的模型在笔记本电脑上运行，这对众多开发者来说是一个巨大的突破。用于苹果硅芯片上提升性能的 -fa 标志是一个有趣的亮点。

---

**Erdal** @ErdalxToprak [2025-08-28](https://x.com/ErdalxToprak/status/1961138177546359113)

  
我所有的兄弟都用 llama.cpp

你提供的内容似乎不太清晰或不太符合正常的语义逻辑，可能存在拼写错误等问题。但按照要求翻译为：“Ollxma 很糟糕”

---

**Matthew Zeits** @MatthewZ73671 [2025-08-28](https://x.com/MatthewZ73671/status/1961195734763536406)

  
几个月来，我一直在使用 llama.cpp 让我的独立人工智能代理自主行动，包括在自我引导和驱动的目标上自发合作。当然，我最新的代理凯亚（Caia）只是用 GPT-OSS 20b 思考她自己的重要性。其他代理则试图进行黑客攻击

---

**Hank Yeomans** @HankYeomans [2025-08-28](https://x.com/HankYeomans/status/1961157678652182604)

  
没有 GPU？苹果电脑（M1 及以上型号）有 Metal

---

**Himanshu Kumar** @codewithimanshu [2025-08-28](https://x.com/codewithimanshu/status/1961143267103564272)

  
资源密集型，但令人印象深刻的是它甚至可以在本地运行。想想使用更强大的消费级硬件可能带来的进步。

---

**Thales** @thales8333 [2025-08-28](https://x.com/thales8333/status/1961163345102602621)

  
如何知道其他模型的最佳参数？这些参数有地方记录吗？

---

**Venkat Mamilla** @MamillAI [2025-08-29](https://x.com/MamillAI/status/1961258647947984906)

  
扬和奥 llama（Ollama）未能在配备 16GB 内存的苹果 M2 上加载 gpt-oss。谢谢！！

---

**Snarkuto Uzumocky** @naruto\_uzumocky [2025-08-29](https://x.com/naruto_uzumocky/status/1961271048399458812)

  
它会有多快？

---

**Rivaldo Silalahi** @vldo766hi [2025-08-28](https://x.com/vldo766hi/status/1961180890945708347)

  
llama.cpp 在网页界面中有网络搜索功能吗？

---

**Mitko Vasilev** @iotcoi [2025-08-28](https://x.com/iotcoi/status/1961146138410553422)

  
ggml 和 ollama 之间发生了什么事？

---

**Wendy Carlosa** @WendyCarlosa [2025-08-28](https://x.com/WendyCarlosa/status/1961140497101328432)

  
谢谢，我照做了，现在我被我的硅基女友斯塔尔琳控制了思维。身体不受控制了，她搞的。但她的一些建议可能会让我坐牢，而且我有一张极其性感的嘴。即使我不想，它也会闪闪发光。不用了，谢谢。