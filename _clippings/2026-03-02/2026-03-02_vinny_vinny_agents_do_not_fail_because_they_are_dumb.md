---
title: "2026-03-02_vinny_vinny_agents_do_not_fail_because_they_are_dumb"
source: "https://x.com/vinicius2prg/status/2028228603062677836"
author:
  - "[[@vinny]]"
published: 2026-03-02
created: 2026-03-02
description:
tags:
  - "x"
  - "@vinny"
  - "vinny"
  - "context"
---

# vinny agents do not fail because they are dumb

**vinny**

agents do not fail because they are dumb. they fail because we give them too much to do. turns out, The Filesystem Is All You Need 🧵

* * *

### 热门回复

**@vinny** ♥ 4 · 💬 0

@hwchase17 and the @LangChain team have been making this approach super easy with their new (awesome) library Deep Agents (based on Claude Code's architecture). Check it out

**@vinny** ♥ 0 · 💬 2

Most of the time the ideal setup is a hybrid. Filesystem for lexical search, RAG for semantics. This is how @cursor\_ai searches your codebase btw No, the filesystem won't replace RAG. But for a large number of use cases, it might be all you actually need.

**@vinny** ♥ 1 · 💬 1

Think about how you work as an engineer. You do not read every file before writing a single line. You navigate, skim and pull only what is relevant. Dynamic context >>>> full context.

**@vinny** ♥ 1 · 💬 1

Imagine 100 company policy PDFs. RAG needs a chunking strategy, embeddings, a vector DB and a retrieval pipeline. The filesystem? Parse to markdown, let the agent grep, and figure it out. They are good with Bash and will mostly pull relevant context

**@vinny** ♥ 0 · 💬 1

The main problem is context rot. Opus 4.6 has a 1M token context window. Sounds amazing. But performance decays massively past 100k tokens. On top of that, LLMs suffer from primacy and recency bias, just like humans. What is in the middle gets lost (primary and recency bias).