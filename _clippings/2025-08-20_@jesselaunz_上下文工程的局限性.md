---
title: "上下文工程的局限性"
source: "https://x.com/jesselaunz/status/1957955834081878475"
author:
  - "[[@jesselaunz]]"
published: 2025-08-20
created: 2025-08-20
description:
tags:
  - "@jesselaunz #上下文工程  #大模型  #SubAgent"
---
**Jesse Lau 遁一子** @jesselaunz 2025-08-19

Context 越大输出性能越差，即使是号称1M窗口的Gemini，超过200k的input，出来的结果也是比较差的

我放在cc的目录也是仅需要处理的代码、小说等。

无关的东西都不会在目录下

cc的本质跟Web上输入prompt是一致的，无非是增加了context window+很多本地处理文件的工具，可以修改文件，从而能迭代改进输出效果

> 2025-08-19
> 
> 我从上下文工程方面提一点意见：如果你一下子安装73个SubAgent，也就是你每次发指令给 Claude Code，那么就要把这 73 个 SubAgent 的说明一股脑发给 Claude 模型，要知道 Claude Code 自带的工具也就 15 个左右，如果工具、SubAgent 是越多越好，那岂不是官方内置几百上千个 Agent 和工具更好？ x.com/bourneliu66/st…