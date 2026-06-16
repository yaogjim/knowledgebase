---
title: "2026-06-16_github_com_truefoundry_tfy_voice_analyser_agent_Voice_call_an"
source: "https://github.com/truefoundry/tfy-voice-analyser-agent"
author:
  - "[[@anthropic]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#1"
  - "github"
  - "@anthropic"
  - "linear"
---

# truefoundry/tfy-voice-analyser-agent: Voice call analyzer using DeepAgents + TFY AI Gateway + Linear MCP

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/truefoundry/tfy-voice-analyser-agent?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

and

[Limit Linear issue creation to top 2 action items (](/truefoundry/tfy-voice-analyser-agent/commit/d57e02ed88bd4921767cad296aaf5eecb7974819)[#1](https://github.com/truefoundry/tfy-voice-analyser-agent/pull/1)[)](/truefoundry/tfy-voice-analyser-agent/commit/d57e02ed88bd4921767cad296aaf5eecb7974819)

[d57e02e](/truefoundry/tfy-voice-analyser-agent/commit/d57e02ed88bd4921767cad296aaf5eecb7974819) ·

[4 Commits](/truefoundry/tfy-voice-analyser-agent/commits/main/)

 |
| 

[.env.example](/truefoundry/tfy-voice-analyser-agent/blob/main/.env.example ".env.example")

 | 

[.env.example](/truefoundry/tfy-voice-analyser-agent/blob/main/.env.example ".env.example")

 | 

[Limit Linear issue creation to top 2 action items (](/truefoundry/tfy-voice-analyser-agent/commit/d57e02ed88bd4921767cad296aaf5eecb7974819 "Limit Linear issue creation to top 2 action items (#1)
* Limit Linear issue creation to top 2 action items, return ticket links
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: change 'exactly 2' to 'up to 2' issues, update sub-agent description
Addresses PR review comments — avoids fabricated tickets when fewer
than 2 action items exist.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: add LINEAR_TEAM env var — required by Linear MCP for issue creation
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: instruct LLM to use real markdown in Linear issue descriptions
Prevents literal \n appearing in Linear ticket bodies.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
---------
Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")[#1](https://github.com/truefoundry/tfy-voice-analyser-agent/pull/1)[)](/truefoundry/tfy-voice-analyser-agent/commit/d57e02ed88bd4921767cad296aaf5eecb7974819 "Limit Linear issue creation to top 2 action items (#1)
* Limit Linear issue creation to top 2 action items, return ticket links
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: change 'exactly 2' to 'up to 2' issues, update sub-agent description
Addresses PR review comments — avoids fabricated tickets when fewer
than 2 action items exist.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: add LINEAR_TEAM env var — required by Linear MCP for issue creation
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: instruct LLM to use real markdown in Linear issue descriptions
Prevents literal \n appearing in Linear ticket bodies.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
---------
Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
| 

[.gitignore](/truefoundry/tfy-voice-analyser-agent/blob/main/.gitignore ".gitignore")

 | 

[.gitignore](/truefoundry/tfy-voice-analyser-agent/blob/main/.gitignore ".gitignore")

 | 

[Remove DEMO.md from tracking, add to.gitignore](/truefoundry/tfy-voice-analyser-agent/commit/a1f8a89dc628965da2e70f2a71856808af1f30a2 "Remove DEMO.md from tracking, add to .gitignore
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
| 

[README.md](/truefoundry/tfy-voice-analyser-agent/blob/main/README.md "README.md")

 | 

[README.md](/truefoundry/tfy-voice-analyser-agent/blob/main/README.md "README.md")

 | 

[Fix.env.example URLs, add model customization note to README](/truefoundry/tfy-voice-analyser-agent/commit/493059cb1e8b6bcec43505c542d17ba086b12efc "Fix .env.example URLs, add model customization note to README
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
| 

[agent.py](/truefoundry/tfy-voice-analyser-agent/blob/main/agent.py "agent.py")

 | 

[agent.py](/truefoundry/tfy-voice-analyser-agent/blob/main/agent.py "agent.py")

 | 

[Limit Linear issue creation to top 2 action items (](/truefoundry/tfy-voice-analyser-agent/commit/d57e02ed88bd4921767cad296aaf5eecb7974819 "Limit Linear issue creation to top 2 action items (#1)
* Limit Linear issue creation to top 2 action items, return ticket links
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: change 'exactly 2' to 'up to 2' issues, update sub-agent description
Addresses PR review comments — avoids fabricated tickets when fewer
than 2 action items exist.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: add LINEAR_TEAM env var — required by Linear MCP for issue creation
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: instruct LLM to use real markdown in Linear issue descriptions
Prevents literal \n appearing in Linear ticket bodies.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
---------
Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")[#1](https://github.com/truefoundry/tfy-voice-analyser-agent/pull/1)[)](/truefoundry/tfy-voice-analyser-agent/commit/d57e02ed88bd4921767cad296aaf5eecb7974819 "Limit Linear issue creation to top 2 action items (#1)
* Limit Linear issue creation to top 2 action items, return ticket links
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: change 'exactly 2' to 'up to 2' issues, update sub-agent description
Addresses PR review comments — avoids fabricated tickets when fewer
than 2 action items exist.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: add LINEAR_TEAM env var — required by Linear MCP for issue creation
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
* Fix: instruct LLM to use real markdown in Linear issue descriptions
Prevents literal \n appearing in Linear ticket bodies.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
---------
Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
| 

[langgraph.json](/truefoundry/tfy-voice-analyser-agent/blob/main/langgraph.json "langgraph.json")

 | 

[langgraph.json](/truefoundry/tfy-voice-analyser-agent/blob/main/langgraph.json "langgraph.json")

 | 

[Initial commit: Voice Call Analyzer with DeepAgents + TFY AI Gateway …](/truefoundry/tfy-voice-analyser-agent/commit/5b076dd056264ccb9b1831092ac8950aab7bf2a7 "Initial commit: Voice Call Analyzer with DeepAgents + TFY AI Gateway + Linear MCP
3 sub-agents (sentiment, action items, coaching) running in parallel on
different LLMs (Gemini Flash, Claude Sonnet, GPT-5 Mini) routed through
TrueFoundry AI Gateway. Action items auto-created as Linear issues via
TFY MCP Gateway.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
| 

[pyproject.toml](/truefoundry/tfy-voice-analyser-agent/blob/main/pyproject.toml "pyproject.toml")

 | 

[pyproject.toml](/truefoundry/tfy-voice-analyser-agent/blob/main/pyproject.toml "pyproject.toml")

 | 

[Initial commit: Voice Call Analyzer with DeepAgents + TFY AI Gateway …](/truefoundry/tfy-voice-analyser-agent/commit/5b076dd056264ccb9b1831092ac8950aab7bf2a7 "Initial commit: Voice Call Analyzer with DeepAgents + TFY AI Gateway + Linear MCP
3 sub-agents (sentiment, action items, coaching) running in parallel on
different LLMs (Gemini Flash, Claude Sonnet, GPT-5 Mini) routed through
TrueFoundry AI Gateway. Action items auto-created as Linear issues via
TFY MCP Gateway.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
| 

[sample\_transcript.txt](/truefoundry/tfy-voice-analyser-agent/blob/main/sample_transcript.txt "sample_transcript.txt")

 | 

[sample\_transcript.txt](/truefoundry/tfy-voice-analyser-agent/blob/main/sample_transcript.txt "sample_transcript.txt")

 | 

[Initial commit: Voice Call Analyzer with DeepAgents + TFY AI Gateway …](/truefoundry/tfy-voice-analyser-agent/commit/5b076dd056264ccb9b1831092ac8950aab7bf2a7 "Initial commit: Voice Call Analyzer with DeepAgents + TFY AI Gateway + Linear MCP
3 sub-agents (sentiment, action items, coaching) running in parallel on
different LLMs (Gemini Flash, Claude Sonnet, GPT-5 Mini) routed through
TrueFoundry AI Gateway. Action items auto-created as Linear issues via
TFY MCP Gateway.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
|  |

Analyze voice call transcripts with 3 AI sub-agents running in parallel — each on a different LLM, all routed through one [TrueFoundry AI Gateway](https://www.truefoundry.com/ai-gateway). Action items are auto-created as [Linear](https://linear.app) issues via TrueFoundry MCP Gateway.

🚀 [Sign up for TrueFoundry](https://www.truefoundry.com/register)  ·  📖 [AI Gateway docs](https://docs.truefoundry.com/docs/ai-gateway)  ·  🤖 [DeepAgents](https://github.com/langchain-ai/deepagents)

* * *

## Architecture

```
load_transcript()
 │
 Planner Agent (Claude Sonnet 4.6)
 │
 ┌────────────┼────────────┐
 │ │ │
 Sentiment Action Items Coach
  (Gemini 3 (Claude 4.6 + (GPT-5
 Flash) Linear MCP) Mini)
 │ │ │
 └────────────┼────────────┘
 │
 Combined Report
```

**3 LLMs, 1 API endpoint** — TFY AI Gateway handles model routing, auth, rate limiting, and observability.

* * *

## Quick Start

```
git clone <repo-url> && cd tfy-voice-analyser-agent
uv sync
cp .env.example .env
```

Fill in your credentials in `.env`:

```
# TFY AI Gateway (required)
TFY_GATEWAY_URL=https://gateway.truefoundry.ai
TFY_API_KEY=tfy-...

# Linear project name (optional)
LINEAR_PROJECT=

# TFY MCP Gateway for Linear (optional — skips issue creation if not set)
TFY_MCP_GATEWAY_URL=https://gateway.truefoundry.ai/your-org/mcp/linear/server
TFY_MCP_GATEWAY_KEY=tfy-...
```

Start the server:

```
langgraph dev --port 8888
```

This gives you:

- **API**: [http://localhost:8888](http://localhost:8888)
- **Studio**: [https://smith.langchain.com/studio/?baseUrl=http://localhost:8888](https://smith.langchain.com/studio/?baseUrl=http://localhost:8888)
- **Docs**: [http://localhost:8888/docs](http://localhost:8888/docs)

* * *

1.  Loads a sample support call transcript (~8 min call)
2.  Spawns **3 sub-agents in parallel**, each on a different LLM via Gateway:
 - **Sentiment Analyzer** (Gemini Flash) — tone, emotional arc, CSAT score
 - **Action Items Creator** (Claude Sonnet) — extracts items + creates Linear issues via MCP
 - **Call Coach** (GPT-5 Mini) — strengths, improvements, suggested phrases
3.  Combines outputs into a single report
4.  Returns the report with links to created Linear issues

* * *

## Customizing Models

Model names in `agent.py` must match what's registered on your TFY AI Gateway. Update these to match your setup:

```
llm("flash/gemini-3-flash") # sentiment
llm("bedrock/global.anthropic.claude-sonnet-4-6") # action items + planner
llm("openai-main/gpt-5-mini") # coaching
```

* * *

## Files

```
agent.py — the whole thing (~130 lines)
langgraph.json — graph config for langgraph dev
sample_transcript.txt — sample support call for demo
pyproject.toml — dependencies
.env.example — credential template
```

* * *

| Component | What | Why |
| --- | --- | --- |
| [DeepAgents](https://github.com/langchain-ai/deepagents) | Multi-agent orchestration with parallel sub-agents | Planning, delegation, combining results |
| [TFY AI Gateway](https://www.truefoundry.com/ai-gateway) | Single endpoint routing to 3 different LLMs | Model routing, cost control, observability |
| [TFY MCP Gateway](https://docs.truefoundry.com/docs/mcp) | Linear issue creation via MCP protocol | Secure tool access with auth + audit |

## Releases

No releases published

## Packages

No packages published

## Languages

- [Python 100.0%](/truefoundry/tfy-voice-analyser-agent/search?l=python)