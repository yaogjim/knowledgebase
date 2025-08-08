---
title: "把Review修复过程放到 http://ReviewTODO.md 里，然后一件件完成"
source: "https://x.com/cholf5/status/1949743363634422135"
author:
  - "[[@cholf5]]"
created: 2025-07-29
description:
tags:
  - "@cholf5 #AI #代码审查 #程序员 #GeminiCLI #Qwen3Coder #TODO"
---
**周尔复** @cholf5 [2025-07-28](https://x.com/cholf5/status/1949743363634422135)

让 AI 交叉 Review 代码可以避免单一 AI 的思维盲区。

今天试了下效果还挺好，让 GeminiCLI 写完代码，交给 Qwen3Coder Review，生成审查报告后，再交给 Gemini 去根据 Review 报告改进代码。

![Image](https://pbs.twimg.com/media/Gw7hKi1bAAAi3t8?format=png&name=large)

---

**周尔复** @cholf5 [2025-07-28](https://x.com/cholf5/status/1949743860546195721)

Prompt:

To Qwen3: Review 整个项目的代码，发现潜在的问题，生成一份详细的 Review 报告到 http://REVIEW.md

To Gemini: http://REVIEW.md 是由另一个AI生成的 Review 报告，你觉得他说的有道理吗？

---

**周尔复** @cholf5 [2025-07-28](https://x.com/cholf5/status/1949749426081366509)

追加一个 Prompt（TODO工作流的延伸）：

把Review修复过程放到 http://ReviewTODO.md 里，然后一件件完成

![Image](https://pbs.twimg.com/media/Gw7munabIAAKhhY?format=png&name=large)

---

**周尔复** @cholf5 [2025-07-28](https://x.com/cholf5/status/1949749517043311058)

最终结果：

![Image](https://pbs.twimg.com/media/Gw7m2QbbkAAwqeP?format=png&name=large)
