---
title: "2026-02-27_Mastra_Mastra_The_coding_agent_that_never_compacts"
source: "https://x.com/mastra/status/2026711011869233397"
author:
  - "[[@Mastra]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "x"
  - "@Mastra"
  - "mastra"
  - "agent"
---

# Mastra # The coding agent that never compacts

**Mastra**

# The coding agent that never compacts

If you’ve used a coding agent, you know the pain. You’re hours into a complex feature. The agent understands your codebase. It remembers every decision. It knows exactly where you are. Then it hits the context window limit and compacts. Suddenly it feels like you’re talking to a stranger.

[Mastra Code](https://code.mastra.ai/)

is a TUI coding agent that never forgets. It’s powered by observational memory, which watches your conversation, generates observations, and reflects on them to compress context without compacting and losing important information.

About half the team at Mastra already use it as a daily driver. I’ve had a session running for months, and it maintains useful knowledge without losing what it learned.

0:15 / 0:58

0:43

## 

Installation

Install mastracode globally with your package manager of choice:

bash

```bash
npm install -g mastracode
```

If you prefer not to install packages globally, you can use npx:

bash

```bash
npx mastracode
```

## 

Features

Like most coding agents, Mastra Code has a plan mode for researching and mapping out changes, and a build mode for executing them. It also includes:

- LSP integration
 
- AST-aware code editing
 
- Shell execution, search, navigation, and web search via Claude tools or Tavily
 
- Subagents, including different models from the main agent
 
- Skills support, with sandbox support in progress
 
- OAuth for Claude Max (Anthropic) and ChatGPT Plus (OpenAI)
 
- Standard API key support for other providers
 
- Project-scoped conversations via git remote or path that persist across sessions
 
- Worktree support
 
- Multi-model support across the 1,800 models available through Mastra’s model router
 
- Tool approval and permission controls for agent directory and git access, plus YOLO mode
 
- Slash commands like /new, /threads, /models, /cost, and /settings
 
- Keyboard shortcuts such as Ctrl+T for thinking and Ctrl+E for expand or collapse
 
- Message steering and queueing
 
- Real-time streaming of chat responses and tool outputs
 

## 

Under the hood

Mastra Code is built using:

- Mastra: Which handles orchestration, memory, and storage. It uses the framework’s Agent, Memory, Workspace, Tools, Model Router, and MCP primitives.
 
- pi-tui: That powers the terminal experience, including streaming responses, markdown rendering, and interactive components like the model picker and thread browser.
 
- ast-grep: Which gives us structure-aware code edits. Instead of chaining search-and-replace calls, the agent writes one AST rule that handles them all at once, resulting in fewer tool calls, fewer tokens, and faster edits.
 
- LibSQL: That keeps threads, messages, token usage, and observational memory in SQLite on your machine, so nothing leaves your local development environment.
 

## 

What it’s like to use day to day

It runs directly in your terminal, with no browser or IDE plugin, so you just install it and start working. With most coding agents, you start thinking about the context window, splitting work across threads, or dumping notes to disk before compaction hits. With Mastra Code, you don’t have to. There’s no compaction pause and no noticeable degradation, even with long-running sessions.

> No compaction! Even with 1M context window compaction took like 3 minutes. With Mastra Code I don't notice any degradation, I don't curse into the air, I stopped yelling COMPACTION, and my mental health is better for it. —
> 
> [Abhi Aiyer](https://x.com/abhiaiyer)

You can throw anything at it, from planning and brainstorming to web or code research, writing features, and fixing bugs. Over time, the difference becomes clear. Memory stops being something you manage and fades into the background so you can stay focused on building.

> I don't worry about the conversation length or multiple threads for anything. I just keep rolling and it keeps going. —
> 
> [Daniel Lew](https://mastra.ai/authors/daniel-lew)

After a few days or weeks, you realize you are no longer tracking context windows or restructuring work to avoid compaction. Observational memory quietly retains what matters as sessions grow. Once you experience that, it is hard to go back.

## 

Get started

Ready to try it for yourself? Dive into the

[Mastra Code docs](https://code.mastra.ai/)

and start building with a coding agent that never forgets.