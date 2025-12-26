---
title: "2025-12-26_shao_meng_开源推荐_Mistral_Vibe_MistralAI_开源了他们最新推出的_CLI_C"
source: "https://x.com/shao__meng/status/1998749732429246909"
author:
  - "[[@shao__meng]]"
published: 2025-12-26
created: 2025-12-26
description:
tags:
  - "x"
  - "@shao__meng"
  - "https"
  - "mistral"
---

# [开源推荐] Mistral Vibe @MistralAI 开源了他们最新推出的 CLI C

**meng shao** @shao\_\_meng [2025-12-10](https://x.com/shao__meng/status/1998749732429246909)

\[开源推荐\] Mistral Vibe: @MistralAI 开源了他们最新推出的 CLI Coding Agent「Mistral Vibe」

和 Kimi CLI 一样采用了 Python 作为主要开发语言，Agent 核心架构也是一个「观察-调整-决策-行动」的循环，模拟一个人类程序员的行为模式：先看文件结构（ls），再搜索关键词（grep），读取代码（cat），修改（vim），运行测试（make test），遇到报错看日志，再回头修改，咱们一起看看 🔽

第一阶段：构建动态上下文

在每一次循环开始前，Agent 必须“看清”当前局势。Vibe 不仅仅是把用户的聊天记录发给模型，而是构建一个结构化的 Prompt 包：

· 系统指令：定义了“你是谁”（Mistral 高级工程师）、“你的权限”（可以读写文件、运行 Shell）以及“输出格式”（必须遵循的 JSON 或 XML 结构）。

· 文件映射：这是 Vibe 的一个特点。它不会把所有代码读进去（那样会撑爆上下文），而是先生成一个精简的文件树。模型通过这个树知道 utils. py 在哪，但暂时不知道里面的内容。

· 活跃窗口：只有被 read\_file 显式打开的文件内容，才会完整进入 Context。

· 历史摘要：之前的对话如果太长，会被压缩成“摘要”，只保留关键决策点。

第二阶段：推理与决策

这是 Devstral 模型 发挥作用的时刻。模型接收上述上下文后，进行思维链推理。

· 意图识别：模型判断用户的意图是“查询”、“修改”还是“测试”。

· 工具选择：模型不直接写代码，而是生成工具调用指令。

场景举例：如果用户说“修复登录页面的 Bug”，模型不会瞎猜，而是先输出：grep("login", "src/views") 来定位代码。

· 架构特点：Vibe 这里利用了 Mistral 模型强大的 Function Calling 能力，保证输出的是结构化数据（如 JSON），而不是模糊的自然语言，确保了程序解析的稳定性。

第三阶段：原子化行动

Agent 接收到模型的指令后，Python 脚本开始执行具体的工具函数。Vibe 的工具设计非常“原子化”（Atomic），这降低了出错概率：

· view / read：查看代码，Vibe 可能会带行号读取，方便后续精准定位。

· edit / replace：这是最难的部分。Vibe 通常采用 Search & Replace Block 的方式，而不是重写整个文件。

· 容错机制：如果模型生成的“查找块”在文件中匹配不到（比如多了一个空格），Agent 会报错，并把错误扔回给循环，让模型重试。

· bash：执行终端命令。Vibe 的“杀手锏”，它允许 Agent 运行 pytest 或 linter 来验证自己的代码。

第四阶段：自我修正与反馈

· 执行结果捕获：工具执行后的 stdout 和 stderr 会被捕获。

· 闭环反馈：

· 如果 grep 没找到内容 $\\rightarrow$ 反馈给模型：“未找到，请尝试其他关键词”。

· 如果 pytest 失败 $\\rightarrow$ 反馈给模型：“测试未通过，错误堆栈如下...”。

· 模型收到反馈后，会自我反思，生成新的修正方案，进入下一次循环。

开源地址

https://github.com/mistralai/mistral-vibe…

开源地址

https://github.com/mistralai/mistralVibe…

![Image](https://pbs.twimg.com/media/G7z8LmoagAAW-K0?format=jpg&name=large)