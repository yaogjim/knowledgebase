---
title: "2026-01-07_github_com_matthewod11_stack_opened_this_issue_on_12220"
source: "https://github.com/anthropics/claude-code/issues/12836#issuecomment-3712095954"
author:
  - "[[@mpiroc]]"
published: 2026-01-07
created: 2026-01-07
description:
tags:
  - "#249"
  - "#how"
  - "github"
  - "@mpiroc"
---

# matthewod11-stack opened this issue on 12220

**matthewod11-stack** opened this issue on 12/2/2025

## Summary

Claude Code loads all tool definitions upfront at session start, which consumes significant context tokens - especially for users with multiple MCP servers, plugins, and agents configured. Anthropic has released beta features specifically designed to address this: **Tool Search Tool** and **Programmatic Tool Calling**.

These are documented at: [https://www.anthropic.com/engineering/advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use)

## Feature Request

Add support for the following API betas in Claude Code:

### 1\. Tool Search Tool (`tool-search-2025-04-15`)

Allow tools to be marked with `defer_loading: true` so they remain discoverable without consuming context tokens at session start. Claude would discover relevant tools on-demand via a search mechanism.

**Reported benefits:**

- 85% reduction in token usage while maintaining full tool access
- Significant accuracy improvements (Opus 4: 49% → 74%, Opus 4.5: 79.5% → 88.1%)

### 2\. Programmatic Tool Calling (`programmatic-tool-use-2025-04-15`)

Allow Claude to orchestrate multiple tools through code execution rather than individual API round-trips, with only final results entering context.

**Reported benefits:**

- 37% token reduction on complex multi-tool tasks
- Eliminates inference overhead from multiple round-trips

## Use Case

Users with extensive setups (multiple MCP servers like filesystem, github, puppeteer, brave-search, plus plugins with agents/skills/commands) are paying a substantial token cost on every session. These betas would allow:

1.  MCP server tools to defer loading until actually needed
2.  Plugin-defined tools/agents to use deferred discovery
3.  Complex multi-tool workflows to execute more efficiently

## Proposed Implementation

- Add configuration options (perhaps in `settings.json` or `.claude/settings.json`) to enable these betas for users who want them
- Support `defer_loading` flag in MCP server tool configurations
- Support `allowed_callers` for programmatic tool execution

## Additional Context

Users with API/developer platform accounts already have access to these betas when using the API directly - this would bring that capability to Claude Code.

**dknoodle** commented on 12/4/2025

For the love of God, PLEASE!

**vmihalis** commented on 12/4/2025

pls anthropic

**ejmockler** commented on 12/4/2025

tool search with RAG sounds promising, but tf-idf still works. just implemented a search-inspect-query pattern to deal with 100+ tools/query endpoints.. tf-idf is lightweight!

[gyorilab/indra\_cogex#249](https://github.com/gyorilab/indra_cogex/pull/249)

**mpiroc** commented on 12/5/2025

[My most frequently-used MCP server](https://devrev.ai/docs/product/remote-mcp) has ~20-30 tools that consume 73.9k tokens of context. 53k of that is consumed by 3 tools that I never use. The authors are working on a fix, but the ability to configure `defer_loading` or even completely disable them (right now, disabling tools doesn't prevent them from being loaded into context) myself without waiting for the authors would be a lifesaver!

**michabbb** commented on 12/5/2025

If you want to filter unused tools inside your mcp server, there's always something like [https://github.com/TBXark/mcp-proxy](https://github.com/TBXark/mcp-proxy) that works pretty well

**amondnet** commented on 12/5/2025

I am implementing this feature using MCP. [https://github.com/pleaseai/mcp-gateway](https://github.com/pleaseai/mcp-gateway)

**michabbb** commented on 12/5/2025

Also, if someone is interested in saving tokens: [https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/#how-the-mcp-toolkit-works](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/#how-the-mcp-toolkit-works)

**ysong2123** commented on 12/5/2025

[@mpiroc](https://github.com/mpiroc) may I know tool search tool and programatic tool calling enabled in which Claude Code version? 2.0.36 work?

**nimto** commented on 12/7/2025

I'm really looking forward to it. I hope it will be supported in the Claude Code CLI as well.

**dleen** commented on 12/31/2025

Is mcp-cli the intended future for programmatic tool calling or is there another solution in the works?

**rcdailey** commented on 12/31/2025

Feedback on `ENABLE_TOOL_SEARCH` with custom agents:

To assign specific MCP tools to an agent, you must also include `MCPSearch` in the tools list:

```yaml
tools: MCPSearch, mcp__octocode__githubSearchCode, mcp__octocode__githubGetFileContent
```

This is undocumented (discovered via trial and error). The agent works, but inefficiently: it calls MCPSearch first to fetch tool docs before using them.

**Suggested behavior:**

1.  Specify tools *without* `MCPSearch` (e.g. `tools: mcp__octocode__githubSearchCode`)
2.  Automatically load tool definitions into the agent context for each listed tool
3.  Agent uses tools directly without the MCPSearch lookup step

This would be more performant and hide the MCP optimization implementation detail from agent configuration. Tools not listed would continue to be optimized away as usual (not consuming tokens).

**shostako** commented on 12/31/2025

## How to persist `ENABLE_TOOL_SEARCH`

For those who discovered this env var works - here's how to make it permanent across sessions:

### Windows (PowerShell)

```powershell
# Add to $PROFILE
$env:ENABLE_TOOL_SEARCH = "true"
```

### macOS / Linux / WSL

```shell
# Add to ~/.zshrc or ~/.bashrc
export ENABLE_TOOL_SEARCH=true
```

**Important**: After adding, open a **new terminal** and start Claude Code from there. Verify with `/context` - you should see "loaded on-demand" next to MCP tools.

[![Image](https://private-user-images.githubusercontent.com/131621616/531183735-61cc80f1-fb70-424e-b0fd-7a961fce54ca.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc3NTAwMTcsIm5iZiI6MTc2Nzc0OTcxNywicGF0aCI6Ii8xMzE2MjE2MTYvNTMxMTgzNzM1LTYxY2M4MGYxLWZiNzAtNDI0ZS1iMGZkLTdhOTYxZmNlNTRjYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwN1QwMTM1MTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lOWRhZGMxMzFjYzdjZDM5ZTcwYzQ3NjRkZjYzZDE2ZjFiMDUwMmE0YzYzOTRjZGI4YWMwM2NlY2UxNjEyMDhjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.TYsWkkvZ41JKUk0mCVaAhtgh1wkv3sYW4wrHppNThQE)](https://private-user-images.githubusercontent.com/131621616/531183735-61cc80f1-fb70-424e-b0fd-7a961fce54ca.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc3NTAwMTcsIm5iZiI6MTc2Nzc0OTcxNywicGF0aCI6Ii8xMzE2MjE2MTYvNTMxMTgzNzM1LTYxY2M4MGYxLWZiNzAtNDI0ZS1iMGZkLTdhOTYxZmNlNTRjYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwN1QwMTM1MTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lOWRhZGMxMzFjYzdjZDM5ZTcwYzQ3NjRkZjYzZDE2ZjFiMDUwMmE0YzYzOTRjZGI4YWMwM2NlY2UxNjEyMDhjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.TYsWkkvZ41JKUk0mCVaAhtgh1wkv3sYW4wrHppNThQE)

**jasonswearingen** commented on 1/4/2026

[@shostako](https://github.com/shostako) just add it to your `.claude/settings.json`

```json
{
  "env" : {
 "ENABLE_TOOL_SEARCH": "true"
  }
}
```

**Calebperez23** commented on 1/4/2026

We’ve been measuring a persistent state substrate that ends up cheaper than RAG-by-default under equivalent workloads, while also materially reducing frontend and tool-loading overhead.

We’re still validating results and not publishing details yet, but it’s changing how we think about where inference cost actually accrues—especially in long-running or agentic setups where retrieval and compaction start behaving like cost multipliers.

**uje-m** commented on 1/5/2026

> We’ve been measuring a persistent state substrate that ends up cheaper than RAG-by-default under equivalent workloads, while also materially reducing frontend and tool-loading overhead.
> 
> We’re still validating results and not publishing details yet, but it’s changing how we think about where inference cost actually accrues—especially in long-running or agentic setups where retrieval and compaction start behaving like cost multipliers.

Interesting. Would love to see the details

**MoogyG** commented on 1/5/2026

Based on my tests, the feature is not production-ready. CC no longer proactively uses certain MCPs.

**konarkm** commented on 1/6/2026

> Based on my tests, the feature is not production-ready. CC no longer proactively uses certain MCPs.

Depending on how the search is already being done, I wonder if this could be largely remedied by the search query (and handling) be what the model "wants to do" rather than a search for specific tools and their definitions. I believe Rube/Composio does something similar, and it allows for a smarter search. Just have a cheap model equipped with more context of the enabled tools handle the query and return whatever's relevant.

**Calebperez23** commented on 1/6/2026

Appreciate the interest.

We’re still in the middle of longer-horizon runs and cross-checking results under a few different baseline assumptions, so we’re intentionally not sharing implementation details yet.

What’s been most surprising so far isn’t any single optimization, but where the cost ends up accruing once sessions persist and tool/search behavior compounds over time. Some of the early ratios only stabilize after hours-long runs, which makes short benchmarks pretty misleading.

In a few workloads, marginal token overhead appears to compress by multiples rather than percentages once state persists—but the exact range is baseline-dependent, so we’re finishing validation before publishing ratios.

We’ll share more once the data is locked and reproducible under independent assumptions—but for now we’re focused on finishing validation rather than expanding scope.