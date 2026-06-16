---
title: "2026-06-16_michaellivs_com_A_thousand_ways_to_sandbox_an_agent"
source: "https://michaellivs.com/blog/sandbox-comparison-2026"
author:
  - "[[@anthropic]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "michaellivs"
  - "@anthropic"
  - "https"
  - "sandbox"
---

# A thousand ways to sandbox an agent

/ Article

Okay, I lied. There are three.

Sandboxing isn’t about restricting agents. It’s what lets you give them bash instead of building fifty tools.

In my post on [Claude Code’s architecture](/blog/architecture-behind-claude-code/), I broke down the four primitives: read, write, edit, bash. Bash is the one that scales. One interface, infinite capability. The agent inherits grep, curl, Python, the entire unix toolkit. But unrestricted bash is a liability. So you sandbox it.

Everyone who ships agents lands on the same three solutions.

## The three approaches

### 1\. Simulated environments

No real OS at all. Your agent *thinks* it’s running shell commands, but it’s all happening in JavaScript or WASM.

[Vercel’s just-bash](https://github.com/vercel-labs/just-bash) is the canonical example. It’s a TypeScript implementation of bash with an in-memory virtual filesystem. Supports 40+ standard Unix utilities: cat, grep, sed, jq, curl (with URL restrictions). No syscalls. Works in the browser.

```typescript
import { Bash, InMemoryFs } from "just-bash";

const fs = new InMemoryFs();

const bash = new Bash({ fs });

await bash.exec('echo "hello" > test.txt');

const result = await bash.exec('cat test.txt');

// result.stdout === "hello\n"
```

Startup is instant (<1ms). There’s no container, no VM, no kernel.

I’ve been impressed by how far you can push this. just-bash supports custom command definitions, so I was able to wire in my own CLIs and even DuckDB. For most agent workflows, it covers what you actually need. The trade-off: no real binaries, no native modules, no GPU. If your agent needs `ffmpeg` or `numpy`, this won’t work.

There’s also [Amla Sandbox](https://github.com/amlalabs/amla-sandbox), which takes a different angle: QuickJS running inside WASM with capability-based security. First run is ~300ms (WASM compilation), subsequent runs ~0.5ms. It supports [code mode](https://www.anthropic.com/engineering/code-execution-with-mcp), where agents write scripts that orchestrate tools instead of calling them one by one, with a constraint DSL for parameter validation.

And [AgentVM](https://github.com/deepclause/agentvm), a full Alpine Linux VM compiled to WASM via [container2wasm](https://github.com/aspect-build/container2wasm). Experimental, but interesting: real Linux, no Docker daemon, runs in a worker thread.

**When to use:** Your agent manipulates text and files. You want instant startup. You don’t need real binaries.

### 2\. OS-level isolation (containers)

This is the workhorse. Use Linux namespaces, cgroups, and seccomp to isolate a process. The agent runs real code against a real (or real-ish) kernel, but can’t escape the box.

The spectrum here ranges from lightweight process isolation to full userspace kernels:

**OS primitives (lightest).**[Anthropic’s sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) uses [bubblewrap](https://github.com/containers/bubblewrap) on Linux and Seatbelt on macOS. No containers at all, just OS-level restrictions on a process. Network traffic routes through a proxy that enforces domain allowlists. This is what Claude Code uses locally.

OpenAI’s Codex CLI takes a similar approach: [Landlock](https://docs.kernel.org/security/landlock.html) + seccomp on Linux, Seatbelt on macOS, restricted tokens on Windows. Network disabled by default, writes limited to the active workspace.

**Docker/containers.**[LLM-Sandbox](https://github.com/vndee/llm-sandbox) wraps Docker, Kubernetes, or Podman. You get real isolation with real binaries, but you need a container runtime. Supports Python, JavaScript, Java, C++, Go, R. Has interactive sessions that maintain interpreter state.

```python
from llm_sandbox import SandboxSession

with SandboxSession(lang="python", keep_template=True) as session:

 result = session.run("print('hello world')")
```

**gVisor (strongest container-ish option).** A userspace kernel written in Go that intercepts syscalls. Your container thinks it’s talking to Linux, but it’s talking to gVisor. I [reverse-engineered Claude’s web sandbox](/blog/sandboxed-execution-environment). The `runsc` hostname gives it away. Google uses this for Cloud Run; Anthropic uses it for Claude on the web.

**When to use:** You need real binaries. You’re running in the cloud. You want the ecosystem (Docker images, k8s, etc).

### 3\. MicroVMs

True VM-level isolation. Each agent gets its own kernel, its own memory space, hardware-enforced boundaries.

[Firecracker](https://firecracker-microvm.github.io/) is the standard. AWS built it for Lambda. Boots in ~125ms with ~5MB memory overhead. The catch: needs KVM access, which means bare metal or nested virtualization. Operationally heavier than containers.

[E2B](https://e2b.dev) runs on Firecracker (they’ve since [moved to Cloud Hypervisor](https://e2b.dev/blog), same idea). Cold start under 200ms. 200M+ sandboxes served. SOC 2 compliant.

```python
from e2b import Sandbox

sandbox = Sandbox()

sandbox.commands.run("echo 'Hello World!'")

sandbox.close()
```

[Fly Sprites](https://fly.io/blog/code-and-let-live/) takes a different philosophy. Instead of ephemeral sandboxes, they give you persistent Linux VMs that sleep when idle. Create in 1-2 seconds, checkpoint in ~300ms, restore instantly. Storage is durable (100GB, backed by object storage via a [JuiceFS](https://juicefs.com/docs/community/introduction/) -inspired architecture). As Kurt Mackey [puts it](https://fly.io/blog/code-and-let-live/): “You’re not helping the agent by giving it a container. They don’t want containers.”

```bash
# Create a sprite

sprite create my-dev-env

# SSH in

sprite ssh my-dev-env

# Checkpoint and restore

sprite checkpoint my-dev-env

sprite restore my-dev-env --checkpoint cp_abc123
```

[Daytona](https://www.daytona.io/) shares the persistent, stateful philosophy. Programmatic sandboxes that agents can start, pause, fork, snapshot, and resume on demand. Sub-90ms cold start. Supports Computer Use (desktop automation on Linux/macOS/Windows). Multi-cloud and self-hosted deployment. “Infrastructure built for agents, not humans.”

[Cloudflare Sandbox](https://developers.cloudflare.com/sandbox/) runs containers on Cloudflare’s edge infrastructure. Full Linux environment, integrates with Workers, can mount R2/S3 storage. Good if you’re already in the Cloudflare ecosystem.

[Modal](https://modal.com/docs/guide/sandbox) lets you define containers at runtime and spawn them on-demand. Sandboxes can run for up to 24 hours. Good for batch workloads and reinforcement learning.

**When to use:** You need the strongest isolation. You’re a platform selling security as a feature. You have the operational capacity.

## The browser is also a sandbox

Paul Kinlan makes an [interesting argument](https://aifoc.us/the-browser-is-the-sandbox/): browsers have 30 years of security infrastructure for running untrusted code. The File System Access API creates a chroot-like environment. Content Security Policy restricts network access. WebAssembly runs in isolated workers.

His demo app, Co-do, lets users select folders, configure AI providers, and request file operations, all within browser sandbox constraints.

The browser isn’t a general solution (no shell, limited to JS/WASM), but for certain use cases it’s zero-setup isolation that works everywhere.

## What the CLI agents actually use

| Agent | Linux | macOS | Windows | Network |
| --- | --- | --- | --- | --- |
| [Claude Code](https://github.com/anthropics/claude-code) | bubblewrap | Seatbelt | WSL2 (bubblewrap) | Proxy with domain allowlist |
| [Codex CLI](https://developers.openai.com/codex/security/) | Landlock + seccomp | Seatbelt | Restricted tokens | Disabled by default |

Both landed on the same pattern: OS-level primitives, no containers, network through a controlled channel.

Claude Code’s sandbox is [open-sourced](https://github.com/anthropic-experimental/sandbox-runtime). Codex’s implementation is proprietary but [well-documented](https://developers.openai.com/codex/security/). Both let you test the sandbox directly:

```bash
# Claude Code

npx @anthropic-ai/sandbox-runtime <command>

# Codex

codex sandbox linux [--full-auto] <command>

codex sandbox macos [--full-auto] <command>
```

The key insight from both: network isolation matters as much as filesystem isolation. Without network control, a compromised agent can exfiltrate `~/.ssh`. Without filesystem control, it can backdoor your shell config to get network access later.

## What the cloud services use

| Service | Technology | Cold Start | Persistence |
| --- | --- | --- | --- |
| [Claude Web](/blog/sandboxed-execution-environment) | gVisor | ~500ms | Session-scoped |
| [ChatGPT containers](https://simonwillison.net/2026/Jan/26/chatgpt-containers/) | Proxy-gated containers | N/A | Session-scoped |
| [E2B](https://e2b.dev) | Firecracker/Cloud Hypervisor | ~200ms | Up to 24h |
| [Fly Sprites](https://fly.io/blog/code-and-let-live/) | Full VMs | 1-2s | Persistent |
| [Daytona](https://www.daytona.io/) | Stateful sandboxes | <90ms | Persistent |
| [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) | Firecracker | ~125ms | Ephemeral |
| [Cloudflare Sandbox](https://developers.cloudflare.com/sandbox/) | Containers | Fast | Configurable |
| [Modal](https://modal.com/docs/guide/sandbox) | Containers | Variable | Up to 24h |

Simon Willison recently [explored ChatGPT’s container environment](https://simonwillison.net/2026/Jan/26/chatgpt-containers/). It now supports bash directly, multiple languages (Node, Go, Java, even Swift), and package installation through a proxy. Downloads come from Azure (Des Moines, Iowa) with a custom user-agent.

## The E2B lesson

E2B built Firecracker-based sandboxes three years ago, long before agents went mainstream. Solid API, 200M+ sandboxes served, SOC 2 compliant. The product was ready. The market wasn’t.

By the time agents hit mainstream, a dozen competitors had emerged. Fly Sprites, Modal, Cloudflare, Vercel. E2B’s early-mover advantage dissolved into a crowded field.

There’s a positioning lesson here. “Cloud sandboxes for agents” describes what E2B *is*. Fly’s framing, “your agent gets a real computer”, describes what it *enables*. One is a feature. The other is a benefit.

If you’re building in this space: don’t describe the box. Describe what happens when the agent gets out of it.

## The open-source landscape

A wave of new projects are tackling this space:

| Project | Approach | Status |
| --- | --- | --- |
| [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) | bubblewrap/Seatbelt | Production (Claude Code) |
| [just-bash](https://github.com/vercel-labs/just-bash) | Simulated bash | Production |
| [llm-sandbox](https://github.com/vndee/llm-sandbox) | Docker/K8s/Podman wrapper | Active |
| [amla-sandbox](https://github.com/amlalabs/amla-sandbox) | WASM (QuickJS) | Active |
| [agentvm](https://github.com/deepclause/agentvm) | WASM (container2wasm) | Experimental |

If you’re building an agent and need sandboxing, start with one of these before rolling your own.

## How to pick

| Use case | Approach | Go-to option |
| --- | --- | --- |
| CLI tool on user’s machine | OS primitives | [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) |
| CLI agent in the cloud | Full VMs | [Fly Sprites](https://sprites.dev) |
| Web agent, simple setup | Containers (gVisor) | Standard Kubernetes |
| Web agent, max isolation | MicroVMs | [E2B](https://e2b.dev), [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) |
| Text/file manipulation only | Simulated | [just-bash](https://github.com/vercel-labs/just-bash) |
| Already on Cloudflare | Containers | [Cloudflare Sandbox](https://developers.cloudflare.com/sandbox/) |
| Batch/RL workloads | Containers | [Modal](https://modal.com/docs/guide/sandbox) |
| Browser-based agent | Browser sandbox | CSP + File System Access API |

**Building a CLI tool?** Use OS-level primitives. Users won’t install Docker for a CLI. Fork [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) or study [Codex’s approach](https://developers.openai.com/codex/security/).

**Running agents in the cloud?**

- Need simplicity? gVisor works in standard Kubernetes.
- Need persistence and statefulness? Fly Sprites or Daytona give you real computers that can snapshot/fork/resume.
- Need maximum isolation? Firecracker (E2B, Vercel).
- Already on Cloudflare? Use their sandbox.

**Agent just processes text and files?**[just-bash](https://github.com/vercel-labs/just-bash). Zero overhead, instant startup, works in the browser.

**Building a platform where security is the product?** MicroVMs. The operational overhead is worth it when isolation is what you’re selling.

**Prototyping quickly?** Simulated environments have the best DX. No containers to manage, no images to build, instant feedback.

## What’s next

A thousand ways to sandbox an agent. Three that actually matter.

Most agents don’t need Firecracker. They need grep and a filesystem. Start with [just-bash](https://github.com/vercel-labs/just-bash) or [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime). You can always escalate later.

The sandbox isn’t the constraint. It’s the permission slip. Pick one and let your agent loose.