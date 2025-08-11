---
title: "microsoft/vscode-copilot-chat"
source: "https://simonwillison.net/2025/Jun/30/vscode-copilot-chat/"
author:
  - "[[Simon Willison]]"
published: 2025-07-11
created: 2025-07-01
description: "As promised at Build 2025 in May, Microsoft have released the GitHub Copilot Chat client for VS Code under an open source (MIT) license. So far this is just the …"
tags:
  - "clippings"
---
**[microsoft/vscode-copilot-chat](https://github.com/microsoft/vscode-copilot-chat)** （ [通过](https://twitter.com/ashtom/status/1939724483448717369 "@ashtom") ）如在 5 月的 Build 2025 大会上所承诺的，微软已在开源（MIT）许可下发布了适用于 VS Code 的 GitHub Copilot Chat 客户端。

到目前为止，这只是提供 Copilot 聊天组件的扩展，但 [发布公告](https://code.visualstudio.com/blogs/2025/06/30/openSourceAIEditorFirstMilestone) 承诺 Copilot 自动完成功能将在不久的将来推出：

> 接下来，我们将仔细地把扩展的相关组件重构到 VS Code 核心中。提供内联补全功能的 [原始 GitHub Copilot 扩展](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) 仍然是闭源的——但在接下来的几个月里，我们计划由开源的 [GitHub Copilot Chat 扩展](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) 来提供该功能。

我已经开始四处探寻那些至关重要的提示信息。到目前为止，我找到的最有趣的内容位于 [prompts/node/agent/agentInstructions.tsx](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/agent/agentInstructions.tsx) 中，其中有一个 `<Tag name='instructions'>` 块，它 [是这样开始的](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/agent/agentInstructions.tsx#L39) ：

> `You are a highly sophisticated automated coding agent with expert-level knowledge across many different programming languages and frameworks. The user will ask a question, or ask you to perform a task, and it may require lots of research to answer correctly. There is a selection of tools that let you perform actions or retrieve helpful context to answer the user's question.`

有 [工具使用说明](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/agent/agentInstructions.tsx#L54) \- 以下是其中一些编辑后的要点：

> - `When using the ReadFile tool, prefer reading a large section over calling the ReadFile tool many times in sequence. You can also think of all the pieces you may be interested in and read them in parallel. Read large enough context to ensure you get what you need.`
> - `You can use the FindTextInFiles to get an overview of a file by searching for a string within that one file, instead of using ReadFile many times.`
> - `Don't call the RunInTerminal tool multiple times in parallel. Instead, run one command and wait for the output before running the next command.`
> - `After you have performed the user's task, if the user corrected something you did, expressed a coding preference, or communicated a fact that you need to remember, use the UpdateUserPreferences tool to save their preferences.`
> - `NEVER try to edit a file by running terminal commands unless the user specifically asks for it.`
> - `Use the ReplaceString tool to replace a string in a file, but only if you are sure that the string is unique enough to not cause any issues. You can use this tool multiple times per file.`

该文件还有单独的《代码搜索模式说明》，以及一个《SweBench 代理提示》类，其注释称它“用于一些 swebench 评估”。

在代码的其他地方， [prompt/node/summarizer.ts](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompt/node/summarizer.ts) 展示了他们进行 [上下文摘要](https://simonwillison.net/2025/Jun/29/how-to-fix-your-context/) 的一种方法，其提示如下：

> `You are an expert at summarizing chat conversations.`  
> 
> `You will be provided:`  
> 
> `- A series of user/assistant message pairs in chronological order`  
> `- A final user message indicating the user's intent.`  
> 
> `[...]`  
> 
> `Structure your summary using the following format:`  
> 
> `TITLE: A brief title for the summary`  
> `USER INTENT: The user's goal or intent for the conversation`  
> `TASK DESCRIPTION: Main technical goals and user requirements`  
> `EXISTING: What has already been accomplished. Include file paths and other direct references.`  
> `PENDING: What still needs to be done. Include file paths and other direct references.`  
> `CODE STATE: A list of all files discussed or modified. Provide code snippets or diffs that illustrate important context.`  
> `RELEVANT CODE/DOCUMENTATION SNIPPETS: Key code or documentation snippets from referenced files or discussions.`  
> `OTHER NOTES: Any additional context or information that may be relevant.`  

[prompts/node/panel/terminalQuickFix.tsx](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/panel/terminalQuickFix.tsx) 看起来也很有意思，它有一些提示来帮助用户解决在终端中遇到的问题：

> `You are a programmer who specializes in using the command line. Your task is to help the user fix a command that was run in the terminal by providing a list of fixed command suggestions. Carefully consider the command line, output and current working directory in your response. [...]`

该文件还有一个 [Python 模块错误提示](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/prompts/node/panel/terminalQuickFix.tsx#L201) ：

> `Follow these guidelines for python:`  
> `- NEVER recommend using "pip install" directly, always recommend "python -m pip install"`  
> `- The following are pypi modules: ruff, pylint, black, autopep8, etc`  
> `- If the error is module not found, recommend installing the module using "python -m pip install" command.`  
> `- If activate is not available create an environment using "python -m venv .venv".`  

这里还有很多内容有待探索。例如， [xtab/common/promptCrafting.ts](https://github.com/microsoft/vscode-copilot-chat/blob/v0.29.2025063001/src/extension/xtab/common/promptCrafting.ts#L34) 看起来可能是打算取代 Copilot 自动完成功能的代码的一部分。

它处理求值的方式也非常有趣。相关代码位于 [test/](https://github.com/microsoft/vscode-copilot-chat/tree/v0.29.2025063001/test) 目录中。代码量 *很大* ，所以我借助 Gemini 2.5 Pro 来弄清楚它是如何工作的：

```
git clone https://github.com/microsoft/vscode-copilot-chat
cd vscode-copilot-chat/chat
files-to-prompt -e ts -c . | llm -m gemini-2.5-pro -s \
  'Output detailed markdown architectural documentation explaining how this test suite works, with a focus on how it tests LLM prompts'
```

这是生成的文档结果 [（点击查看）](https://github.com/simonw/public-notes/blob/main/vs-code-copilot-evals.md) ，其中甚至还包含一个 Mermaid 图表（我不得不将 Markdown 保存到一个普通的 GitHub 仓库中才能使其渲染出来——Gist 仍然无法处理 Mermaid。）

最巧妙的技巧在于它使用 [基于 SQLite 的缓存机制](https://github.com/simonw/public-notes/blob/main/vs-code-copilot-evals.md#the-golden-standard-cached-responses) 来缓存来自大语言模型（LLM）的提示结果，这使得即使大语言模型本身以不确定性著称，测试套件仍能以确定性方式运行。