---
title: "2025-11-05_karminski3_llama_cpp_终于要砸_Ollama_饭碗了_llama_cpp_是一个C_实现的大模型推"
source: "https://x.com/karminski3/status/1985864385055826342"
author:
  - "[[@karminski3]]"
published: 2025-11-05
created: 2025-11-05
description:
tags:
  - "x"
  - "@karminski3"
  - "https"
  - "pbs"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# llama.cpp 终于要砸 Ollama 饭碗了！ llama.cpp 是一个C++实现的大模型推

**karminski-牙医** @karminski3 [2025-11-05](https://x.com/karminski3/status/1985864385055826342)

llama.cpp 终于要砸 Ollama 饭碗了！

llama.cpp 是一个C++实现的大模型推理引擎，而ollama是在llama.cpp基础上套了个网页界面。当然 llama.cpp 之前也是有网页界面的，不过做得很简陋。但是今天迎来了大更新，给大家捋一捋：

首先多模态支持做得非常好了，图片，声音，PDF都可以输入了（还差个视频），然后支持混合输入，比如拖进去一个代码文件，再粘贴一段代码也是OK的。

PDF还可以实现转换，如果模型支持直接输入图片效果好可以把PDF转成图片。

界面上也支持修改之前的prompt然后重新生成，以及并行运行多个聊天（图片处理也可以并行）。

以及还有个我最喜欢的功能，url可以直接输入文本当作prompt查询。这个功能的好处是，可以直接在浏览器里 @ llamacpp 就能对话了(chrome 可以配置一下)，省去了再输入URL。

还有个最方便的功能——可以在设置里面指定一个JSON格式，然后大模型的输出就全是在这个JSON格式了！非常适合批量格式转换/数据清洗任务！

这还只是一小部分，更多细节见更新页面：http://github.com/ggml-org/llama.cpp/discussions/16938…

总之我觉得可以淘汰掉其它大模型客户端了

![Screenshot of a macOS application window displaying the llama.cpp web interface in a browser, with green annotations highlighting features: server status showing 0/1 loaded and 0 requests, file upload options for images, text files, and other files, a chat input area with a prompt in Chinese about compiling llama.cpp, and a black background with white Chinese text at the bottom reading 11ama.cpp and a question about compiling 011ama.](https://pbs.twimg.com/media/G4807DrbQAEf-jP?format=png&name=large)

* * *

**karminski-牙医** @karminski3 [2025-11-05](https://x.com/karminski3/status/1985864389598273934)

更新细节 1

![Image](https://pbs.twimg.com/media/G481GJhbgAEbO2f?format=png&name=large) ![Image](https://pbs.twimg.com/media/G481GMDbQAAb3RQ?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G481GJpbQAAhQ1r?format=png&name=large) ![Image](https://pbs.twimg.com/media/G481GJza0AAO_cu?format=png&name=large)

* * *

**karminski-牙医** @karminski3 [2025-11-05](https://x.com/karminski3/status/1985864394123981181)

更新细节 2

![Image](https://pbs.twimg.com/media/G481ICCbQAEaRj9?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G481H_la4AAsRvm?format=jpg&name=large)

* * *

**ElevenLabs** @elevenlabsio

Translate audio and video while preserving the emotion, timing, tone, and unique characteristics of each speaker.

在翻译音视频时，保持每位发言者的情感、节奏、语调和独特个性。