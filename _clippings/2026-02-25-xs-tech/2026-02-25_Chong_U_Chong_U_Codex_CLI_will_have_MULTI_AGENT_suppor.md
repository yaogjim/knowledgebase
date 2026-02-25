---
title: "2026-02-25_Chong_U_Chong_U_Codex_CLI_will_have_MULTI_AGENT_suppor"
source: "https://x.com/chongdashu/status/2023913841529065892"
author:
  - "[[@Chong-U]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@Chong-U"
  - "agents"
---

# Chong-U Codex CLI will have MULTI-AGENT suppor

**Chong-U**

Codex CLI will have MULTI-AGENT support in 0.123.0 Here's how it will work: → 1. Add \`multi\_agent=true\` in ~/codex/config.toml under \[features\] → 2. Toggle with \`/experimental\` → 3. Three built-in agents (default, explorer, worker) → 4. Define your own agents \`\`\` \[agents.researcher\] description = "Research-focused role." config\_file = "~/.codex/agents/researcher.toml" model = "gpt-5.3-codex" model\_reasoning\_effort = "high" web\_search = "live" sandbox\_mode = "read-only" developer\_instructions = """ You are the researcher agent. - Gather evidence from primary sources. - Return links, findings, and uncertainty. - Do not edit files. """ \`\`\` → 5. Run more agent threads per session (default: 6) \`\`\` \[agents\] max\_threads = 6 Notes: → OAI released 0.122.0 - but rolled it back! → I built it from source (so you don't have)

[![视频](https://pbs.twimg.com/amplify_video_thumb/2023913750852497408/img/P3In8y5I4A1yIXKH.jpg)](https://x.com/chongdashu/status/2023913841529065892)

* * *

### 热门回复

**@Cursor** ♥ 5.7K · 💬 282

Cursor now shows you demos, not diffs. Agents can use the software they build and send you videos of their work.

**@Boris Cherny** ♥ 3.8K · 💬 202

We shipped Claude Code as a research preview a year ago today. Developers have used it to build weekend projects, ship production apps, write code at the world's largest companies, and help plan a Mars rover drive. We built it, and you showed us what it was for.

**@Opopop** ♥ 151 · 💬 0

Want the perfect pop? Grab the Discovery Kit Today

**@CoreWeave** ♥ 60 · 💬 0

Only CoreWeave Cloud gives you access to the latest GPUs, 99.9% data availability at exabyte scale, and continuous visibility across compute, storage, and networking. We help teams iterate faster and deploy AI workloads more efficiently. Ready for Anything, Ready for AI

**@Chong-U** ♥ 3 · 💬 2

\*0.103.0 not 0.123.0