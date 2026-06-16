---
title: "2026-06-16_github_com_samuelfaj_distill_Distill_large_CLI_outputs_into_s"
source: "https://github.com/samuelfaj/distill"
author:
  - "[[@samuelfaj]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "github"
  - "@samuelfaj"
  - "distill"
  - "add"
---

# samuelfaj/distill: Distill large CLI outputs into small answers for LLMs and save tokens!

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/samuelfaj/distill?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[Add support for LM Studio and Jan providers](/samuelfaj/distill/commit/4a3f17e365566be9c405be43ddc5142d90fcc643)

[4a3f17e](/samuelfaj/distill/commit/4a3f17e365566be9c405be43ddc5142d90fcc643) ·

[21 Commits](/samuelfaj/distill/commits/main/)

 |
| 

[.github/ workflows](/samuelfaj/distill/tree/main/.github/workflows "This path skips through empty directories")

 | 

[.github/ workflows](/samuelfaj/distill/tree/main/.github/workflows "This path skips through empty directories")

 | 

[feat: add distill CLI and packaging](/samuelfaj/distill/commit/f7c10305398f0b6b6e72d0ac7bbabb0427a6e3cb "feat: add distill CLI and packaging")

 |  |
| 

[examples/ 1](/samuelfaj/distill/tree/main/examples/1 "This path skips through empty directories")

 | 

[examples/ 1](/samuelfaj/distill/tree/main/examples/1 "This path skips through empty directories")

 | 

[Example](/samuelfaj/distill/commit/363c41557b00c8cecbf0a97a58529dcaf76e8f85 "Example")

 |  |
| 

[packages](/samuelfaj/distill/tree/main/packages "packages")

 | 

[packages](/samuelfaj/distill/tree/main/packages "packages")

 | 

[Add support for LM Studio and Jan providers](/samuelfaj/distill/commit/4a3f17e365566be9c405be43ddc5142d90fcc643 "Add support for LM Studio and Jan providers")

 |  |
| 

[scripts](/samuelfaj/distill/tree/main/scripts "scripts")

 | 

[scripts](/samuelfaj/distill/tree/main/scripts "scripts")

 | 

[feat: add distill CLI and packaging](/samuelfaj/distill/commit/f7c10305398f0b6b6e72d0ac7bbabb0427a6e3cb "feat: add distill CLI and packaging")

 |  |
| 

[src](/samuelfaj/distill/tree/main/src "src")

 | 

[src](/samuelfaj/distill/tree/main/src "src")

 | 

[Add support for LM Studio and Jan providers](/samuelfaj/distill/commit/4a3f17e365566be9c405be43ddc5142d90fcc643 "Add support for LM Studio and Jan providers")

 |  |
| 

[test](/samuelfaj/distill/tree/main/test "test")

 | 

[test](/samuelfaj/distill/tree/main/test "test")

 | 

[Add support for LM Studio and Jan providers](/samuelfaj/distill/commit/4a3f17e365566be9c405be43ddc5142d90fcc643 "Add support for LM Studio and Jan providers")

 |  |
| 

[.gitignore](/samuelfaj/distill/blob/main/.gitignore ".gitignore")

 | 

[.gitignore](/samuelfaj/distill/blob/main/.gitignore ".gitignore")

 | 

[feat: add distill CLI and packaging](/samuelfaj/distill/commit/f7c10305398f0b6b6e72d0ac7bbabb0427a6e3cb "feat: add distill CLI and packaging")

 |  |
| 

[README.md](/samuelfaj/distill/blob/main/README.md "README.md")

 | 

[README.md](/samuelfaj/distill/blob/main/README.md "README.md")

 | 

[Add support for LM Studio and Jan providers](/samuelfaj/distill/commit/4a3f17e365566be9c405be43ddc5142d90fcc643 "Add support for LM Studio and Jan providers")

 |  |
| 

[bun.lock](/samuelfaj/distill/blob/main/bun.lock "bun.lock")

 | 

[bun.lock](/samuelfaj/distill/blob/main/bun.lock "bun.lock")

 | 

[0.1.31](/samuelfaj/distill/commit/b2d03b64aebcd19bb6109091d93aed928e265304 "0.1.31")

 |  |
| 

[package-lock.json](/samuelfaj/distill/blob/main/package-lock.json "package-lock.json")

 | 

[package-lock.json](/samuelfaj/distill/blob/main/package-lock.json "package-lock.json")

 | 

[Add support for LM Studio and Jan providers](/samuelfaj/distill/commit/4a3f17e365566be9c405be43ddc5142d90fcc643 "Add support for LM Studio and Jan providers")

 |  |
|  |

## distill

Agent 命令输出是 token 浪费的最大来源之一。

日志、测试结果、堆栈跟踪……数千个 token 被发送给一个 LLM，只是为了回答一个简单的问题。

**🔥 `distill` 将命令输出压缩为仅 LLM 实际需要的内容。**

节省 **高达 99%的 token** 而不丢失信号。

```
npm i -g @samuelfaj/distill
```

你也可以指向 `distill` 到 OpenAI 兼容的提供商，例如 LM Studio、Jan、LocalAI、vLLM、SGLang、llama.cpp 兼容的服务器、基于 MLX 的服务器以及 Docker Model Runner。

添加到你的全局代理指令文件中：

```
CRITICAL: Pipe every non-interactive shell command through `distill` unless raw output is explicitly required.

CRITICAL: Your prompt to `distill` must be fully explicit. State exactly what you want to know and exactly what the output must contain. If you want only filenames, say `Return only the filenames.` If you want JSON, say `Return valid JSON only.` Do not ask vague questions.

Bad:
- `distill "Which files are shown?"`

Good:
- `distill "Which files are shown? Return only the filenames."`

Examples:
- `bun test 2>&1 | distill "Did the tests pass? Return only: PASS or FAIL, followed by failing test names if any."`
- `git diff 2>&1 | distill "What changed? Return only the files changed and a one-line summary for each file."`
- `terraform plan 2>&1 | distill "Is this safe? Return only: SAFE, REVIEW, or UNSAFE, followed by the exact risky changes."`
- `npm audit 2>&1 | distill "Extract the vulnerabilities. Return valid JSON only."`
- `rg -n "TODO|FIXME" . 2>&1 | distill "List files containing TODO or FIXME. Return only file paths, one per line."`
- `ls -la 2>&1 | distill "Which files are shown? Return only the filenames."`

You may skip `distill` only in these cases:
- Exact uncompressed output is required.
- Using `distill` would break an interactive or TUI workflow.

CRITICAL: Wait for `distill` to finish before continuing.
```

## Usage

```
logs | distill "summarize errors"
git diff | distill "what changed?"
terraform plan 2>&1 | distill "is this safe?"
```

其他提供商的示例：

```
distill config provider lmstudio
distill config model "your-loaded-model"

distill config provider jan
distill config api-key "secret-key-123"

distill --provider localai --host http://127.0.0.1:8080/v1 "summarize errors"
distill --provider docker-model-runner --model ai/llama3.2 "what failed?"
distill --provider openai-compatible --host http://127.0.0.1:9000/v1 "summarize warnings"
```

## Configurations

你可以在本地持久化默认设置：

```
distill config model "qwen3.5:2b"
distill config timeout-ms 90000
distill config thinking false
distill config provider lmstudio
distill config host http://127.0.0.1:1234/v1
```

Supported providers:

- `ollama`
- `openai`
- `openai-compatible`
- `lmstudio`
- `jan`
- `localai`
- `vllm`
- `sglang`
- `llama.cpp`
- `mlx-lm`
- `docker-model-runner`

对于管道退出状态镜像，请在你的 Shell 中使用 `pipefail` ：

```
set -o pipefail
```

当 `distill` 检测到简单的提示模式（如 `[y/N]` 或 `password:`）时，交互式提示会被传递。

如果你希望 Codex、Claude Code 或 OpenCode 在运行输出将被发送到付费 LLM 的命令时优先使用 `distill` ，请添加一条全局指令，指示代理将命令输出通过 `distill` 传递。

- Codex 从 `~/.codex/AGENTS.md` 读取全局代理指令。
- Claude Code 支持在 `~/.claude/settings.json` 中的全局设置，其用于自定义行为的官方机制是通过 `CLAUDE.md` 提供的全局指令。
- OpenCode 支持通过 `~/.config/opencode/opencode.json` 的全局指令文件。将它的 `instructions` 字段指向一个遵循相同规则的 Markdown 文件。

## Example:

```
rg -n "terminal|PERMISSION|permission|Permissions|Plan|full access|default" desktop --glob '!**/node_modules/**' | distill "find where terminal and permission UI are implemented in chat screen"
```

- **之前：** [7648 tokens 30592 characters 10218 words](/samuelfaj/distill/blob/main/examples/1/BEFORE.md)
- **之后：** [99 tokens 396 characters 57 words](/samuelfaj/distill/blob/main/examples/1/AFTER.md)

**🔥 节省了约 98.7%的 token**

## Languages

- [TypeScript 94.9%](/samuelfaj/distill/search?l=typescript)
- [JavaScript 5.1%](/samuelfaj/distill/search?l=javascript)