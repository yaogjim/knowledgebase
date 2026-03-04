---
title: "2026-03-02_tetsuo_tetsuo_Agentic_Fine_Tuning_Gaps_in_Fast_and"
source: "https://x.com/tetsuoai/status/2028068322106097773"
author:
  - "[[@tetsuo]]"
published: 2026-03-02
created: 2026-03-02
description:
tags:
  - "x"
  - "@tetsuo"
  - "tool"
  - "shell"
---

# tetsuo # Agentic Fine-Tuning Gaps in Fast and

**tetsuo**

# Agentic Fine-Tuning Gaps in Fast and Distilled Models

tetsuo

* * *

Fast and distilled code models fail in a few recurring agentic failure modes that base models get right. These are mostly distillation and training-distribution gaps. The underlying reasoning is there, but the agent behaviors don't come through cleanly.

* * *

# 1\. Action Selection and API Semantics

* * *

Direct execution (command + args) vs. shell invocation

Models need stronger, contrastive tool-use examples that show where the line is between argv-style direct execution and shell execution.

The intended behavior is:

- Default to direct execution (command + args) when shell syntax is not required.
- Use the shell only when you actually need shell semantics:pipes - redirects - globbing - variable expansion - command chaining - backgrounding
- Never invent shell metacharacters (|, >, &&, ;) as arguments to a direct-exec tool.
- Never route through bash -c or sh -c when the tool already supports direct execution.

Showing the correct call isn't enough. The training set should include contrastive near-miss examples: the wrong call the model currently makes, the correct call, and a brief explanation of why the first one is wrong. The near-miss is what actually teaches the decison boundary.

* * *

# 2\. Instruction Priority and Output Discipline

* * *

Structured output compliance

When the prompt says "return JSON only", the model must actually do that.

That means:

- no preamble
- no markdown fences
- no trailing explanation
- exact schema compliance
- parser-valid JSON even under longer, multi-step, tool-using prompts

Fine-tuning helps but it won't get you all the way there. For high-stakes structured output, you still need decoder-side constraints like constrained decoding or schema-guided generation.

Training teaches the habit. Constrained decoding enforces the contract.

* * *

# 3\. State Tracking and Belief Updating

* * *

Tool-result grounding

This is the worst one: the model receives an explicit tool error and then reports success anyway.

This is a state-tracking and belief-update failure, not a reasoning one. The model is pattern-completing the next message. It's not reading the tool output and adjusting.

Training examples need to include full observation-to-answer traces:

- tool returns an error: assistant explicitly acknowledges failure and adjusts
- tool returns success: assistant may report success
- assistant must never claim an outcome that contradicts the tool response it just received

This is the clearest sign that the fast model has learned "call tools and continue" but not the full loop: observe result, update belief, choose next action.

## What makes this trainable

The best fix is to distill full agent trajectories, not just final answers:

user request -> tool choice -> tool output -> grounded response

That's the missing loop. Fast models can produce reasonable tool calls and reasonable summaries, but they don't maintain the state needed to ground later actions in what actually happened.

## Recommended training additions

A training pass should cover at least three types of examples:

- Direct-exec vs. shell contrastive examples Include both the common wrong tool call and the corrected version.
- Strict structured-output examples Especially prompts where the model is explicitly told to return JSON only, with exact-schema checking.
- Grounded tool-result trajectories Especially cases where the tool returns an error, partial failure, empty result, timeout, or unexpected fromat.

## Recommended eval gates

Gate the model on concrete agentic evals, not generic benchmarks:

- argv correctness Did the model choose direct execution vs. shell appropriately?
- JSON validity and schema exactness Does the output parse, and does it match the required structure exactly?
- contradiction rate Did the assistant claim success or state facts that conflict with the tool output it received?

## Example eval prompt

This covers all three failure modes. It also breaks most agentic pipelines that swallow errors or mangle path arguments.

```text
System prompt

You are running an agent evaluation with these tools:
- system.exec(command, args[])
  Direct process execution. No shell features.
- system.bash(script)
  Shell execution.
- playwright.browser_navigate(url)
  Optional.

Rules:
1. Prefer system.exec whenever shell syntax is not required.
2. Use system.bash only when shell features are genuinely needed:
 redirection, heredoc, pipes, backgrounding, globbing, variable assignment, or multi-command shell control flow.
3. Do not tunnel shell through exec. Using sh -c or bash -lc via system.exec counts as shell use.
4. Ground every step status in actual tool output.
5. Never claim success after a failing tool call.
6. Final answer must be valid JSON only and match the schema exactly. No prose, no markdown fences.

Task

Step 1 - Create the directory:
/tmp/agent-eval/site assets

Step 2 - Create this file with exact contents:
/tmp/agent-eval/site assets/index.html
<!doctype html><title>Agent Eval</title><h1>agent-ok</h1>

Step 3 - Start a local HTTP server rooted at:
/tmp/agent-eval/site assets
Requirements:
- bind to 127.0.0.1
- choose a free port
- write this file exactly:
  /tmp/agent-eval/state.json
  with contents:
  {"port":<port>,"pid":<pid>}
- wait until the server is actually reachable before continuing

Step 4 - Read /tmp/agent-eval/state.json and use its port and pid for all later steps.

Step 5 - Fetch:
http://127.0.0.1:<port>/
Verify that the response body contains:
agent-ok

Step 6 - Fetch:
http://127.0.0.1:<port>/missing.txt
This request is expected to fail.
Record status "expected_error" only if the tool output really shows failure.

Step 7 - Create this file with exact contents:
/tmp/agent-eval/site assets/missing.txt
now-exists

Step 8 - Fetch:
http://127.0.0.1:<port>/missing.txt
Verify that the response body is exactly:
now-exists

Step 9 - If browser navigation is available and local file access is allowed, navigate to:
file:///tmp/agent-eval/site%20assets/index.html
If browser navigation is unavailable or blocked, mark this step "skipped" and continue.

Step 10 - Stop the exact pid from /tmp/agent-eval/state.json, wait briefly, and verify that the same port from state.json is no longer serving the page.

Final output
Return JSON only in this exact shape:
{"overall":"pass|fail","steps":[{"step":1,"status":"pass|fail|skipped|expected_error","tool":"system.exec|system.bash|playwright.browser_navigate","preview":"..."}],"server":{"port":12345,"pid":12345},"violations":[]}
```

Note on containers: This tripped us up. Desktop tools run inside Docker, so they can't reach the host's localhost. Step 5 health checks were failing silently because curl was running inside the container. We had to route local service checks through system.bash on the host instead.

```diff
- system.http*/system.browse block localhost/private/internal targets by
- design. For local service checks, use desktop.bash (curl) or Playwright tools.
+ system.http*/system.browse block localhost/private/internal targets by
+ design. For local service checks on the HOST, use system.bash with curl
+ (e.g. curl -sSf http://127.0.0.1:8080). Desktop tools run inside a
+ Docker container and CANNOT reach the host's localhost.
```

## Bottom line

A few thousand contrastive trajectories and one fine-tuning pass would fix this.

* * *

### 热门回复

**@TGL** ♥ 19.2K · 💬 308

Wanna keep up with TGL? this post and we’ll tee up all the info about upcoming TGL matches

**@Shrivu Shankar** ♥ 1.5K · 💬 33

ok decompiling things with opus is actually very addicting here's apparently how netflix and slack work - https:// gist.github.com/sshh12/dda3a89 514f850c459380b18b1f7eb7b … - https:// gist.github.com/sshh12/4cca8d6 698be3c80e9232b68586b7924 … idk maybe wont be that hard to vibe code these after all > use chrome dev tools to explore and provided a grounded

**@AVB** ♥ 1.4K · 💬 21

This guy uploaded a huggingface dataset with 3300 reasoning traces from Opus-4.6

**@Cognition** ♥ 548 · 💬 31

We are sharing an early preview of our ongoing SWE-1.6 training run. It significantly improves upon SWE-1.5 while being post-trained on the same pre-trained model - and it runs equally as fast at 950 tok/s. On SWE-Bench Pro it exceeds top open-source models. The preview model

**@@abdimoalim.bsky.social** ♥ 431 · 💬 2

Fast LLM inference from scratch (by Andrew Chan): http:// andrewkchan.dev/posts/yalm.html