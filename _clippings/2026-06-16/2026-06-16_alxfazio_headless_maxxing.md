---
title: "2026-06-16_alxfazio_headless_maxxing"
source: "https://x.com/alxfazio/status/2032556496781779302"
author:
  - "[[@alxfazio]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@alxfazio"
  - "codex"
  - "exec"
---

# headless maxxing

**alex fazio**

# headless maxxing

In this article, I’ll walk through how to wrap codex exec for your agentic apps. codex exec "your query" (short alias: codex e "your query") is the dedicated command for headless/scriptable use cases: non-interactive execution, streams progress to stderr, outputs only the final agent message to stdout, then exits.

# Context

If you’ve used the Codex interactive TUI, you already know what the agent can do. codex exec is how you put that same agent into your scripts and CI pipelines. It streams progress to stderr while outputting only the final agent message to stdout. By default it runs in a read-only sandbox, requires a Git repository, and authenticates via CODEX\_API\_KEY.

# Wrapping the CLI

This all comes down to codex exec (or codex e). It’s a one-shot invocation of the CLI that runs the agent, streams progress to stderr, and pipes the final result to stdout. Everything in this article is derived from testing 66 flag combinations against Codex CLI v0.114.0, so the behaviors described here are verified against the actual CLI.

# The State Machine

codex exec can be thought of as a state machine with two independent dimensions that combine orthogonally:

The first dimension is output format, which controls what comes out of stdout.

![Image](https://pbs.twimg.com/media/HDUQTGrWMAAnkCv?format=png&name=large)

The second dimension is permission level, which controls what the agent is allowed to do.

![Image](https://pbs.twimg.com/media/HDUQZJ2X0AA0ssC?format=png&name=large)

Any output format works with any sandbox mode. Unlike interactive mode, there is no bidirectional streaming — input is provided upfront and output flows one way.

One wrinkle: --full-auto is a hard override that always locks the sandbox to workspace-write. If you pass --full-auto --sandbox danger-full-access, the explicit --sandbox flag is silently ignored. To get full access, use --sandbox danger-full-access directly (or --yolo).

## Gotchas

- codex exec requires a Git repository (or trusted directory) by default. Use --skip-git-repo-check to override.
- Stderr streams progress; stdout contains only the final result. Don’t mix them up when piping.
- CODEX\_API\_KEY only works with codex exec, not other commands.

# Basic Usage Patterns

## Getting Data IN: Input Methods

There are multiple ways to feed a prompt into codex exec:

1.  Command Line Argument (Most Common)

```bash
codex exec "explain this function in main.py"
# or short alias:
codex e "explain this function in main.py"
```

1.  Stdin Pipe (Pipe content from another command:)

```bash
# Read prompt entirely from stdin (use - or omit the argument):
cat logs.txt | codex exec -

# Pipe a file and include instructions in the same stream:
(echo "Review this code for bugs:"; cat file.py) | codex exec -
```

1.  Stdin Redirect (Read from a file:)

```text
codex exec < prompt.txt
```

1.  Here-Doc (Multi-line Prompts, perfect for complex prompts with formatting)

```bash
codex exec <<EOF
You are a code reviewer. Review this code:

def add(a, b):
 return a + b

Focus on: error handling, edge cases, documentation.
EOF
```

1.  Image Input (Attach screenshots or design specs — prompt must come before the image flag)

```text
# Single image
codex exec "Explain this error" -i screenshot.png

# Multiple images
codex exec "Summarize these diagrams" --image img1.png,img2.jpg
```

## Combining Input Methods

Stdin is only read when no prompt argument is provided (or when - is used). To combine context with instructions, concatenate them into a single stdin stream:

```bash
# File content + instruction via stdin
(echo "Review this code for bugs:"; cat file.py) | codex exec -

# Git diff + task via stdin
(echo "Write a commit message for these changes:"; git diff HEAD~3) | codex exec -

# Prompt argument + image attachment
codex exec "fix the security issues" -i screenshot.png
```

# Getting Data OUT: Output Methods

There are 2 output formats plus a file-capture flag:

1: Text Output (Default, human-readable, plain text)

```bash
# To terminal (progress on stderr, result on stdout)
codex exec "summarize the repository structure"

# Capture to variable (only gets stdout = final message)
response=$(codex exec "What is 2+2?")
echo "$response"

# Save to file
codex exec "Write a haiku" > haiku.txt

# Pipe to another command
codex exec "generate release notes for the last 10 commits" | tee release-notes.md
```

2: JSON Lines Output (Machine-Readable)

JSONL event stream via --json (or --experimental-json):

```bash
codex exec --json "summarize the repo structure" | jq
```

Returns newline-delimited JSON events with these event types:

![Image](https://pbs.twimg.com/media/HDURRK3WYAEC2Px?format=jpg&name=large)

Sample event stream:

```json
{"type":"thread.started","thread_id":"019ce6ce-65fd-7530-8e6b-9ccce0436091"}
{"type":"turn.started"}
{"type":"item.completed","item":{"id":"item_0","type":"agent_message","text":"PING"}}
{"type":"turn.completed","usage":{"input_tokens":8497,"cached_input_tokens":8448,"output_tokens":51}}
```

By default, reasoning items are hidden from the JSONL stream. To include them (when using model\_reasoning\_summary):

```text
codex exec --json -c model_reasoning_summary=detailed -c hide_agent_reasoning=false "complex task"
```

This adds item.completed events with "type": "reasoning" before the agent message.

Extract fields with jq:

```bash
# Get just agent messages
codex exec --json "What is 2+2?" | jq 'select(.type == "item.completed") | .item.text'

# Get token usage from turn completion
codex exec --json "Hello" | jq 'select(.type == "turn.completed") | .usage'
```

Parse in real-time:

```bash
codex exec --json "Write a story" | \
  while IFS= read -r line; do
 text=$(echo "$line" | jq -r 'select(.type == "item.completed") | .item.text // empty' 2>/dev/null)
 [ -n "$text" ] && printf "%s" "$text"
  done
```

Or in Node.js:

```javascript
const readline = require("readline");

for await (const line of readline.createInterface({ input: process.stdin })) {
  const event = JSON.parse(line);
  if (event.type === "item.completed" && event.item?.text) {
 process.stdout.write(event.item.text);
  }
}
```

## Input/Output Combination Matrix

![Image](https://pbs.twimg.com/media/HDUSrIQXcAAh0UH?format=jpg&name=large)

## Structured Output with JSON Schema

This is the killer feature for data extraction. Define a JSON Schema file for structured responses via --output-schema:

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json
```

Example schema file (schema.json). Fair warning: the OpenAI API enforces strict mode, so every object must include additionalProperties: false and requiredmust list all properties. I burned two attempts figuring this out before the third one worked:

```bash
{
  "type": "object",
  "properties": {
 "answer": { "type": "string" },
 "confidence": { "type": "number" }
  },
  "required": ["answer", "confidence"],
  "additionalProperties": false
}
```

The final message conforms to the schema and is written to the specified file (via -o) while still appearing on stdout. Note that -o always captures plain text. When combined with --json, stdout gets the JSONL event stream while the file gets only the final agent message. This makes -o useful for extracting the result while streaming JSONL events to stdout for monitoring.

## Tool Configuration

By default, Codex exec has access to a shell tool and file operations. You can get pretty granular with tool configuration via config.toml:

Disable Shell Tool (Pure LLM)

```bash
codex exec -c features.shell_tool=false "analyze this code"
# or equivalently:
codex exec --disable shell_tool "analyze this code"
```

The --enable and --disable flags are shortcuts for -c features.<name>=true/false.

Or set defaults in ~/.codex/config.toml:

```yaml
[features]
shell_tool = false
```

Per-App Tool Control

In config.toml, enable/disable specific MCP apps and their individual tools:

```yaml
[apps._default]
enabled = false

[apps.my_tool]
enabled = true

[apps.my_tool.tools.dangerous_action]
enabled = false
```

Web Search

The interactive --search flag does not work with codex exec. To enable web search in exec mode, use the config key:

```bash
codex exec -c web_search=live "what is the latest version of React?"
```

Values: disabled | cached | live (default: cached).

MCP Server Configuration

```yaml
[mcp_servers.my_server]
enabled = true
command = "npx"
args = ["-y", "my-mcp-server"]
enabled_tools = ["safe_tool_1", "safe_tool_2"]
disabled_tools = ["dangerous_tool"]
required = true
```

## Permission Modes

Autonomous execution hinges on two things: sandbox policy and approval policy.

Sandbox modes (--sandbox or -s):

![Image](https://pbs.twimg.com/media/HDUTQKNbsAAVPsH?format=jpg&name=large)

In exec mode, approval is always never because there is no interactive user to prompt. The --full-auto docs describe it as on-request, but exec mode collapses this to never automatically.

Convenience flags:

```bash
# Workspace-write sandbox + auto-approval (recommended for local automation)
codex exec --full-auto "your task here"

# Bypass everything — only use in isolated CI runners
codex exec --dangerously-bypass-approvals-and-sandbox "your task here"

# or equivalently:
codex exec --yolo "your task here"
```

For CI/CD Pipelines

```bash
codex exec --full-auto \
  "Read repo, run tests, identify minimal fix, implement only that change, stop."
```

Additional writable directories:

```bash
codex exec --full-auto --add-dir /tmp/output "generate reports"
```

Sandbox Fine-Tuning

```bash
# Enable outbound network access within workspace-write sandbox
codex exec --full-auto -c sandbox_workspace_write.network_access=true "fetch and summarize this API"

# Remove /tmp from writable paths
codex exec --full-auto -c sandbox_workspace_write.exclude_slash_tmp=true "process these files"
```

## Session Management

Ephemeral Sessions (No Disk Storage)

\--ephemeral prevents saving session rollout files to disk:

```bash
codex exec --ephemeral "triage this repository and suggest next steps"
```

Resume Previous Sessions

Continue a previous session with new instructions:

```bash
# Resume most recent session
codex exec resume --last "fix the race conditions you found"

# Resume a specific session by ID
codex exec resume 0199a213-81c0-7800-8aa1-bbab2a035a53

# Resume with a follow-up prompt
codex exec resume --last "now write tests for those fixes"
```

Continue Most Recent

```bash
codex exec resume --last "follow up question"
```

## Code Review

codex exec review is a dedicated subcommand for automated code review. It requires a git repository and one of:

```bash
# Review uncommitted changes
codex exec review --uncommitted

# Review changes against a branch
codex exec review --base main

# Review a specific commit
codex exec review --commit abc123
```

It produces structured review comments with severity levels (P1-P4), file paths, and line ranges. I was genuinely surprised by how useful this is; it caught a leftover test heading I’d accidentally left in a file.

## Custom System Prompts

Replace Entirely

Use model\_instructions\_file in config.toml to replace the built-in instructions (instead of AGENTS.md):

```yaml
model_instructions_file = "./my-instructions.md"
```

Append to Default (Recommended)

Use developer\_instructions in config.toml to inject additional instructions without replacing the defaults:

```yaml
developer_instructions = "IMPORTANT: Always respond in bullet points. Focus on security."
```

Or use an AGENTS.md file in the project root — Codex automatically reads it as additional context.

## Custom Agents

Configure multi-agent collaboration via config.toml:

```yaml
[features]
multi_agent = true

[agents]
max_threads = 6
max_depth = 1

[agents.reviewer]
description = "Code reviewer that focuses on security and performance"
```

## Model Selection

Basic Model Choice

```bash
# Recommended flagship model
codex exec --model gpt-5.4 "complex task"

# Industry-leading coding model
codex exec --model gpt-5.3-codex "standard task"

# Text-only near-instant research preview (ChatGPT Pro only)
codex exec --model gpt-5.3-codex-spark "quick question"
```

Or set a default in ~/.codex/config.toml:

```yaml
model = "gpt-5.4"
```

Reasoning Control

```bash
# Control reasoning effort
codex exec -c model_reasoning_effort=high "complex debugging task"

# Control reasoning summary detail
codex exec -c model_reasoning_summary=detailed "explain this architecture"
```

## No Bidirectional Streaming

codex exec does not support bidirectional streaming. It is a one-shot command: input is provided upfront (via argument, stdin, or here-doc), and output flows one way. For real-time interactive use cases, use the interactive TUI mode (codex) instead.

# Putting It All Together

Production Agentic Wrapper

```bash
#!/bin/bash
# agentic-codex.sh - Production wrapper for autonomous execution

TASK="$1"

codex exec \
  --model gpt-5.4 \
  --full-auto \
  --ephemeral \
  --json \
  --output-schema ./task-schema.json \
  -o ./result.json \
  "$TASK"

# Extract structured output
success=$(jq -r '.success' ./result.json)
summary=$(jq -r '.summary' ./result.json)

echo "Task: $success"
echo "Summary: $summary"
```

Chatbot Wrapper

```typescript
import { execSync } from "child_process";

function chat(prompt: string, model = "gpt-5.4"): string {
  const result = execSync(`codex exec --model ${model} --ephemeral`, {
 input: prompt,
 encoding: "utf-8",
  });
  return result;
}

const response = chat("What is the meaning of life?");
console.log(response);
```

Data Extraction Pipeline

```typescript
import { execSync, ExecSyncOptionsWithStringEncoding } from "child_process";
import { writeFileSync } from "fs";

const SCHEMA = {
  type: "object",
  properties: {
 entities: { type: "array", items: { type: "string" } },
 sentiment: { enum: ["positive", "negative", "neutral"] },
 summary: { type: "string" },
  },
  required: ["entities", "sentiment", "summary"],
};

writeFileSync("./extract-schema.json", JSON.stringify(SCHEMA));

function extract(text: string) {
  execSync(
 `codex exec --model gpt-5.4 --ephemeral --output-schema ./extract-schema.json -o ./extracted.json`,
 {
 input: `Extract entities, sentiment, and summary from: ${text}`,
 encoding: "utf-8",
 } as ExecSyncOptionsWithStringEncoding,
  );
  return JSON.parse(require("fs").readFileSync("./extracted.json", "utf-8"));
}

const info = extract("I love this new iPhone! Apple really outdid themselves.");
console.log(info); // { entities: ['iPhone', 'Apple'], sentiment: 'positive', ... }
```

## Quick Reference

![Image](https://pbs.twimg.com/media/HDUVeuUXcAAvb0q?format=png&name=large)

## Gotchas

I/O

codex exec requires a Git repository (or trusted directory) by default; use --skip-git-repo-check to override. Progress streams to stderr, only the final message goes to stdout. Stdin is only read when no prompt argument is provided (or when - is used), so you cannot combine a prompt argument with piped stdin content. Image flags (-i / --image) must come after the prompt argument. There is no bidirectional streaming; use the interactive TUI for real-time chat.

Structured output

\--output-schema accepts a file path, so write your schema to a file first. The schema must use strict mode: additionalProperties: false and all properties in required.

Permissions and safety

\--yolo bypasses ALL safety; only use in isolated CI runners with no sensitive access. Required MCP servers (required = true) cause exit with error if they fail to initialize. --search does not work with codex exec (returns “unexpected argument”); use -c web\_search=live instead.

Auth and environment

CODEX\_API\_KEY overrides stored auth and only works with codex exec. OPENAI\_API\_KEY is silently ignored when ~/.codex/auth.json has valid credentials, so use CODEX\_API\_KEY for exec-mode auth override. OPENAI\_BASE\_URL redirects API calls (useful for proxies and custom endpoints). CODEX\_HOME redirects all config, auth, and session storage away from ~/.codex.

Sessions

Resuming an ephemeral session silently creates a new session instead of erroring, because the original session was never persisted.

The two-dimensional state machine (output format x sandbox level) keeps things simple, and the -c config overrides let you reach everything else without touching config.toml. If you’re building agentic apps on top of Codex, start with --full-auto --json and layer on --output-schema when you need structured data. That covers 90% of use cases.

> Codex CLI version: 0.114.0 | Tested: 2026–03–13

## References

- [Codex CLI Reference (Command Line Options)](https://developers.openai.com/codex/cli/reference)
 
- [Codex CLI Features](https://developers.openai.com/codex/cli/features)
 
- [Codex Non-Interactive Mode](https://developers.openai.com/codex/noninteractive/)
 
- [Codex Configuration Reference](https://developers.openai.com/codex/config-reference/)
 
- [Codex Sandboxing Concepts](https://developers.openai.com/codex/concepts/sandboxing/)
 
- [Codex Authentication](https://developers.openai.com/codex/auth/)
 
- [Codex Models](https://developers.openai.com/codex/models/)
 
- [Codex Config Basics](https://developers.openai.com/codex/config-basic/)