---
title: "2026-06-16_unknown_Cog认知架构与长期记忆系统解析"
source: "omnisun://digest/1774576316328"
author:
  - "[[@anthropic]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#domain"
  - "@anthropic"
  - "claude"
  - "memory"
---

# Cog认知架构与长期记忆系统解析

# marciopuga/cog: Cognitive architecture for Claude Code — persistent memory, self-reflection, and foresight

https://github.com/marciopuga/cog

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/marciopuga/cog?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

and

[docs: clarify that the architecture evolves, not the model](/marciopuga/cog/commit/65e5043c6fcc58924648960d0e54240380acbbd4)

[65e5043](/marciopuga/cog/commit/65e5043c6fcc58924648960d0e54240380acbbd4) ·

[8 Commits](/marciopuga/cog/commits/main/)

 |
| 

[.claude](/marciopuga/cog/tree/main/.claude ".claude")

 | 

[.claude](/marciopuga/cog/tree/main/.claude ".claude")

 | 

[feat(pipeline): add Unix toolbox orientation to pipeline skills](/marciopuga/cog/commit/d5e9e4333d917713283d528c698b89d8d798729b "feat(pipeline): add Unix toolbox orientation to pipeline skills
- Add Orientation sections to housekeeping, reflect, evolve with shell
commands (find -mtime, grep -c, git diff, wc -c) for efficient scoping
- Update CLAUDE.md memory retrieval to use domain-scoped L0 grep
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[memory](/marciopuga/cog/tree/main/memory "memory")

 | 

[memory](/marciopuga/cog/tree/main/memory "memory")

 | 

[feat: scalable entities & patterns architecture](/marciopuga/cog/commit/d47510b0f66cef9ad8427ce13f535719adba9051 "feat: scalable entities & patterns architecture
- Entity format: 3-line compact registry (### Name / key facts / status+links)
Heavy entries promoted to thread files. Cross-domain pointers for shared entities.
- Pattern satellites: core patterns.md cap reduced from 110→70 lines (5.5KB).
Domain-specific patterns go in satellite files loaded only by owning skill.
- Reflect: pattern routing rules, entity format enforcement (step 3b)
- Housekeeping: entity registry enforcement (step 5b), glacier inactive entities
- Evolve: scorecard metrics for pattern distribution + entity compression ratio
- README: updated entity example to 3-line format
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[.gitignore](/marciopuga/cog/blob/main/.gitignore ".gitignore")

 | 

[.gitignore](/marciopuga/cog/blob/main/.gitignore ".gitignore")

 | 

[feat: initial cog release — cognitive architecture for Claude Code](/marciopuga/cog/commit/1dd881975b77419c68fbcb06039bca97a5b892b0 "feat: initial cog release — cognitive architecture for Claude Code
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[CLAUDE.md](/marciopuga/cog/blob/main/CLAUDE.md "CLAUDE.md")

 | 

[CLAUDE.md](/marciopuga/cog/blob/main/CLAUDE.md "CLAUDE.md")

 | 

[feat(pipeline): add Unix toolbox orientation to pipeline skills](/marciopuga/cog/commit/d5e9e4333d917713283d528c698b89d8d798729b "feat(pipeline): add Unix toolbox orientation to pipeline skills
- Add Orientation sections to housekeeping, reflect, evolve with shell
commands (find -mtime, grep -c, git diff, wc -c) for efficient scoping
- Update CLAUDE.md memory retrieval to use domain-scoped L0 grep
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[LICENSE](/marciopuga/cog/blob/main/LICENSE "LICENSE")

 | 

[LICENSE](/marciopuga/cog/blob/main/LICENSE "LICENSE")

 | 

[feat: initial cog release — cognitive architecture for Claude Code](/marciopuga/cog/commit/1dd881975b77419c68fbcb06039bca97a5b892b0 "feat: initial cog release — cognitive architecture for Claude Code
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[README.md](/marciopuga/cog/blob/main/README.md "README.md")

 | 

[README.md](/marciopuga/cog/blob/main/README.md "README.md")

 | 

[docs: clarify that the architecture evolves, not the model](/marciopuga/cog/commit/65e5043c6fcc58924648960d0e54240380acbbd4 "docs: clarify that the architecture evolves, not the model
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
|  |

## Cog

A plain-text cognitive architecture for Claude Code — simple by design, so the model can reason over its own memory with the same Unix tools (`grep`, `find`, `git diff`) it already knows.

**[Documentation](https://lab.puga.com.br/cog)** | **[Why Text](https://lab.puga.com.br/cog/#/why-text)** | **[Credits & Inspiration](https://lab.puga.com.br/cog/#/credits)**

Cog is a set of conventions — not code — that teach Claude Code how to build and maintain its own memory. You define the rules in plain text. Claude scaffolds the structure and follows them. The filesystem is the interface.

There is no server, no runtime, no application code. `CLAUDE.md` contains the conventions — how to tier memory, when to condense, how to route queries, when to archive. The skill files (`.claude/commands/*.md`) teach Claude specific workflows: reflection, foresight, housekeeping, self-evolution. Claude reads these instructions and follows them to organize, maintain, and grow a persistent knowledge base across sessions.

Everything is plain text [by design](https://lab.puga.com.br/cog/#/why-text). Not as a compromise — because plain text is what makes this work. Memory files are just markdown, which means Claude can `grep` for patterns, `find` what changed, `wc` to check file sizes, and `git diff` to see what the last pipeline run touched. The same Unix tools that make Linux powerful make Cog's memory observable and maintainable.

Cog is a learning tool — an experiment in watching how a memory architecture evolves when given clear conventions and self-observation capabilities. You set the rules, Claude scaffolds the structure, and the pipeline skills refine the conventions over time. The model doesn't evolve — it follows whatever rules it finds. The rules are what change. Every decision is visible. Every rule is editable. Every change is in the git log.

## Quick Start

Requires [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).

```
git clone https://github.com/marciopuga/cog
cd cog
```

Open the project in Claude Code, then:

```
/setup
```

Cog will ask about your life and work — company, side projects, what you want to track. From that conversation, it generates everything: domain manifest, memory directories, skill files, and routing table.

That's it. Start talking.

### Permissions

Cog ships with `.claude/settings.json` that pre-approves the tools it needs — file reads, writes, edits, search, and git operations. When you first open the project, Claude Code will ask you to accept these project-level permissions. Say yes once and you won't be interrupted again.

If you'd rather review everything manually, delete `.claude/settings.json` and Claude Code will prompt for each operation individually.

`CLAUDE.md` defines the conventions below. Claude reads them at the start of every session and follows them to decide where to store facts, when to condense, how to route queries, and when to archive. The `memory/` directory is the state that emerges from following these rules over time.

### Three-Tier Memory

```
memory/
├── hot-memory.md ← Always loaded. <50 lines. What matters right now.
├── personal/ ← Warm. Loaded when relevant.
│ ├── hot-memory.md
│ ├── observations.md ← Append-only event log
│ ├── action-items.md ← Tasks with due dates
│ ├── entities.md ← People, places, things
│ └── ...
├── work/acme/ ← Your work domain (created by /setup)
│ └── ...
└── glacier/ ← Cold. Archived, indexed, retrieved on demand.
 └── index.md
```

- **Hot**: Loaded every conversation. Current state, top priorities.
- **Warm**: Domain-specific files loaded when a skill activates.
- **Glacier**: YAML-frontmattered archives. Searched via `glacier/index.md`.

Here's what builds up over time. None of this is pre-filled — it emerges from your conversations.

**`memory/hot-memory.md`** — the 30,000-foot view:

```
# Hot Memory
<!-- L0: Current priorities, active situations, system notes -->

## Identity
- Software engineer at Acme Corp, 2 kids, based in Melbourne
- Side project: open-source CLI tools

## Watch
- Performance review cycle opens next week — prep doc started [[work/acme/action-items]]
- Kid's speech therapy showing progress — 3 new words this month [[personal/health]]

## System
- /reflect found 3 observation clusters ready to promote to patterns
```

**`memory/personal/observations.md`** — raw events, append-only:

**`memory/work/acme/entities.md`** — compact 3-line registry:

```
### Sarah Chen (Engineering Manager)
- Direct report to VP Eng | Joined Jan 2025 | Runs platform team | Prefers async over meetings
- status: active | last: 2026-03-10
```

Heavy entries get promoted to thread files — the entity stub just links: `→ [[work/acme/sarah-chen]]`.

### Progressive Condensation

Two processes:

**Condensation:** observations → patterns → hot-memory. Each layer is smaller and more actionable than the one below.

**Archival:** old observations → glacier. Indexed, retrievable, out of the way.

Nothing is deleted — it moves to the right place.

When a topic keeps coming up across observations, Cog raises it into a **thread** — a read-optimized synthesis file that pulls scattered fragments into a coherent narrative.

Every thread has the same spine:

- **Current State** — what's true right now (rewrite freely)
- **Timeline** — dated entries, append-only, full detail preserved
- **Insights** — patterns, learnings, what's different this time

A thread gets raised when a topic appears in 3+ observations across 2+ weeks, or when you say "raise X" or "thread X". Threads grow long — that's the point. The texture is the value. One file forever, never condensed.

Fragments (observations) never move. Threads reference them via wiki-links.

See the full [Thread Framework documentation](https://lab.puga.com.br/cog/#/memory) for details.

Every memory file has a one-line summary: `<!-- L0: what's in this file -->`. This is the first tier of a three-level retrieval protocol:

- **L0** — one-line summary. Decides whether to open a file at all.
- **L1** — section header scan. Identifies which part of a long file to read.
- **L2** — full file read. Used when the full context is needed.

Scan L0s first, confirm relevance, use L1 for long files, read only what's needed.

Each fact lives in one canonical file. `entities.md` owns people. `action-items.md` owns tasks. `hot-memory.md` holds pointers — not the authoritative version of any fact. Other files reference with `[[wiki-links]]` instead of copying.

### Wiki-Links

Files cross-reference each other with `[[domain/filename]]` links. A link index is auto-generated by `/housekeeping` so you can discover what connects to what.

### Domain Registry

Domains are areas of your life — personal, work, side projects. Each domain gets its own memory directory and slash command.

```
/setup → conversational → domains.yml → directories + skills + routing
```

| Type | Purpose | Examples |
| --- | --- | --- |
| `personal` | Personal life | Always created |
| `work` | Day job | `/acme`, `/google` |
| `side-project` | Ventures, hobbies | `/myapp`, `/substack` |
| `system` | Cog internals | Auto-created (`cog-meta`) |

## Skills

Built-in skills in `.claude/commands/`:

| Skill | What it does |
| --- | --- |
| `/setup` | Conversational domain setup |
| `/personal` | Family, health, calendar, day-to-day |
| `/reflect` | Mine conversations, extract patterns, condense |
| `/evolve` | Audit memory architecture, propose rule changes |
| `/foresight` | Cross-domain strategic nudge |
| `/scenario` | Decision simulation with timeline overlay |
| `/housekeeping` | Archive, prune, link audit, glacier index |
| `/history` | Deep search across memory files |
| `/explainer` | Writing and explanation (Atkins + Montaigne method) |
| `/humanizer` | Remove AI patterns from text |

Domain skills (`/work`, `/sideproject`, etc.) are auto-generated by `/setup`.

## Pipeline

Cog includes pipeline skills that maintain memory health over time. Run them manually:

```
/housekeeping # Archive stale data, prune hot-memory, rebuild indexes
/reflect # Mine recent work, condense patterns, detect threads
/evolve # Audit architecture, check rule effectiveness
/foresight # Cross-domain scan, surface one strategic nudge
```

Or automate with scheduling:

**Claude Code** has built-in task scheduling — use `/loop` or cron to run pipeline skills on a recurring basis:

```
# Example: nightly housekeeping + reflect via cron
0 23 * * * cd /path/to/cog && claude -p "$(cat .claude/commands/housekeeping.md)"
0 0  * * * cd /path/to/cog && claude -p "$(cat .claude/commands/reflect.md)"
```

**[Cowork](https://claude.com/product/cowork)** sessions can also run pipeline skills. Open Cog in Cowork and ask it to run `/housekeeping` or `/reflect` — it has full file access and can maintain memory as part of a longer autonomous session.

The pipeline is optional. Cog works without it — but running it regularly keeps memory clean and surfaces insights you'd miss.

## Architecture

Cog's architecture lives entirely in instructions — `CLAUDE.md` for conventions and `.claude/commands/*.md` for workflows. There is no application code. The instructions define how memory is structured, how queries are routed, and how the system maintains itself. Claude reads these files and acts on them. The `memory/` directory is just the state that accumulates.

This makes Cog interface-agnostic. It works with:

- **[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)** (terminal) — native. Just open the project.
- **[Cowork](https://claude.com/product/cowork)** — Claude Desktop's agentic mode. Point it at `memory/` and it inherits everything. Great for heavy document generation and long autonomous workflows.
- **Any Claude-powered tool** that reads `CLAUDE.md` and has file access.

The memory system is the same everywhere — markdown files with conventions. The interface just determines how context is loaded.

## Connecting Tools

Cog becomes significantly more powerful when connected to external tools via MCP (Model Context Protocol). In Claude Code or Cowork, you can connect services like:

- **Google Calendar** — schedule awareness, meeting prep, time-blocking
- **Gmail** — email drafting, inbox triage, follow-up tracking
- **Slack** — team context, message drafting, channel monitoring
- **GitHub** — PR reviews, issue tracking, codebase awareness
- **Linear/Jira** — project tracking, sprint context
- **Notion/Obsidian** — extended knowledge base, note sync

When tools are connected, Cog's skills can use them automatically. `/foresight` checks your calendar before surfacing nudges. `/reflect` can reference Slack threads. `/personal` can draft emails. The memory layer gives these tools something they don't have alone: context that persists and compounds.

**To connect tools in Cowork**, add MCP servers in your Cowork settings. Each tool appears as a set of functions Cog can call alongside its memory operations — no code changes needed.

The combination of persistent memory + connected tools is where Cog stops being a note-taking system and starts being a cognitive layer. Memory without action is a diary. Memory with tools is an agent.

## Credits

Cog is a synthesis of ideas from research, open-source systems, and knowledge management traditions.

**Research**: [RLM](https://arxiv.org/abs/2512.24601) (recursive memory hierarchy) | [A-MEM](https://arxiv.org/abs/2502.12110) (bi-directional back-linking) | [OpenViking](https://github.com/volcengine/OpenViking) (L0/L1/L2 tiered context loading)

**Systems**: [Zep/Graphiti](https://github.com/getzep/graphiti) (temporal validity) | [Mem0](https://github.com/mem0ai/mem0) (contradiction detection) | [Claude Memory](https://docs.anthropic.com/en/docs/claude-code/memory) (file-based architecture validation)

**Traditions**: [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten) (thread framework) | [SSOT](https://en.wikipedia.org/wiki/Single_source_of_truth) (canonical fact storage)

**Platform**: [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) (Anthropic)

See the [full credits page](https://lab.puga.com.br/cog/#/credits) for how each idea shaped Cog's design.

## Citation

If Cog influences your work — whether you fork it, adapt the patterns, or reference the architecture — a mention goes a long way:

```
Cog: Cognitive Architecture for Claude Code
https://github.com/marciopuga/cog
Marcio Puga, 2026
```

BibTeX for academic use:

```
@software{puga2026cog,
  author = {Puga, Marcio},
  title = {Cog: Cognitive Architecture for Claude Code},
  year = {2026},
  url = {https://github.com/marciopuga/cog},
  note = {Persistent memory, self-reflection, and foresight for AI agents}
}
```

## License

MIT

## Releases

No releases published

## Packages

No packages published

* * *

# Cog — Cognitive Architecture for Claude Code

https://lab.puga.com.br/cog/

* * *

Explore

[](#/architecture)

[Architecture](#/architecture)

[

No server, no runtime — just conventions Claude follows. Skills, domains, routing.

](#/architecture)

[](#/memory)

[Memory](#/memory)

[

Three tiers: desk, filing cabinet, deep storage. How Cog remembers without reading everything.

](#/memory)

[](#/cowork)

[Cowork](#/cowork)

[

How Cowork sessions inherit persistent memory from Cog

](#/cowork)

[](#/pipeline)

[Pipeline](#/pipeline)

[

REM sleep for an AI — nightly consolidation, pattern extraction, self-improvement

](#/pipeline)

[](#/journal)

[Origins](#/journal)

[

Development journal — how the architecture evolved from first boot to release

](#/journal)

[](#/why-text)

[Why Text](#/why-text)

[

Why plain text, not a database — and why that makes the cognition legible

](#/why-text)

[](#/credits)

[Credits](#/credits)

[

Research, systems, and ideas that shaped Cog's design

](#/credits)

* * *

<table><tbody><tr><td><strong>Interfaces</strong></td><td>Claude Code, Cowork, any Claude tool with file access</td></tr><tr><td><strong>Engine</strong></td><td>CLAUDE.md conventions — works with any Claude session</td></tr><tr><td><strong>Skills</strong></td><td>11 built-in + auto-generated domain skills from manifest</td></tr><tr><td><strong>Memory</strong></td><td>Three-tier (hot/warm/glacier), L0-indexed, domain-based</td></tr><tr><td><strong>Pipeline</strong></td><td>5 skills: housekeeping → reflect → evolve → foresight → scenarios</td></tr><tr><td><strong>Source</strong></td><td><a href="https://github.com/marciopuga/cog">github.com/marciopuga/cog</a></td></tr></tbody></table>

* * *

# Cog — Cognitive Architecture for Claude Code

https://lab.puga.com.br/cog/#/pipeline

## Pipeline

When you sleep, your brain doesn't shut off. It replays the day's events, strengthens the connections that matter, discards the noise, and reorganises everything into long-term memory. That's REM sleep — and Cog's pipeline is the AI equivalent.

Without maintenance, a memory system decays. Facts go stale. Summaries drift from their sources. Patterns emerge that no single conversation notices. The pipeline runs nightly to consolidate, reflect, and evolve — so every new session starts cleaner than the last.

| Stage | Role | What it does |
| --- | --- | --- |
| [Housekeeping](#/pipeline/housekeeping) | Janitor | Archive stale data, prune broken links, rebuild indexes |
| [Reflect](#/pipeline/reflect) | Therapist | Mine conversations for patterns, detect contradictions, raise threads |
| [Evolve](#/pipeline/evolve) | Architect | Audit the memory architecture itself, rewrite rules that aren't working |
| [Foresight](#/pipeline/foresight) | Strategist | Cross-domain strategic nudge — what should you be thinking about tomorrow? |

Each step feeds the next. Zero overlap — one owner per job.

The pipeline was introduced incrementally: scheduler on [Day 2](#/journal/scheduler-and-domains), reflection on [Day 6](#/journal/the-architecture-day), evolve on [Day 12](#/journal/evolve-pipeline), foresight and scenarios on [Day 23](#/journal/strategic-foresight). The [domain registry](#/journal/domain-registry) made the pipeline domain-agnostic — stages discover domains from `domains.yml` instead of hardcoded paths.

## Design Principle

**"Seeing ≠ owning."** When a pipeline step spots an issue outside its domain, it routes the issue — it doesn't adopt it. Housekeeping cleans; if it finds a pattern, it notes it for Reflect. Evolve changes rules; if it finds stale content, it routes to Housekeeping.

This prevents scope creep and keeps each stage focused.

## Scheduling

The pipeline is manual-first — run any skill as a slash command whenever you want. But for best results, automate it.

### Claude Code

Use cron to spawn one-shot Claude processes:

```bash
# Nightly maintenance
0 23 * * * cd /path/to/cog && claude -p "$(cat .claude/commands/housekeeping.md)"
0 0  * * * cd /path/to/cog && claude -p "$(cat .claude/commands/reflect.md)"

# Weekly architecture audit
0 1  * * 0 cd /path/to/cog && claude -p "$(cat .claude/commands/evolve.md)"

# Daily strategic nudge
0 7  * * * cd /path/to/cog && claude -p "$(cat .claude/commands/foresight.md)"
```

### Cowork

Open Cog in a [Cowork](https://claude.com/product/cowork) session and ask it to run pipeline skills as part of a longer autonomous workflow. Cowork has full file access and can chain multiple stages together — useful for a full maintenance pass in one session.

Stages

[](#/pipeline/housekeeping)

[23:00 — Janitor](#/pipeline/housekeeping)

[

Housekeeping

Clean, archive, sync, surface accountability

](#/pipeline/housekeeping)

[](#/pipeline/reflect)

[00:00 + 14:00 — Therapist](#/pipeline/reflect)

[

Reflect

Introspect, mine journals, fix contradictions, condense

](#/pipeline/reflect)

[](#/pipeline/evolve)

[01:00 — Architect](#/pipeline/evolve)

[

Evolve

Audit rules, prompt weight, system design

](#/pipeline/evolve)

[](#/pipeline/foresight)

[07:00 — Strategist](#/pipeline/foresight)

[

Foresight

Scan broadly, connect dots, look forward

](#/pipeline/foresight)

[](#/pipeline/scenarios)

[On demand — Simulator](#/pipeline/scenarios)

[

Scenarios

Model decisions, generate branches, track outcomes

](#/pipeline/scenarios)

* * *

# Cog — Cognitive Architecture for Claude Code

https://lab.puga.com.br/cog/#/architecture

## Architecture

Cog is simple by design. Everything is plain text — markdown conventions and memory files — so Claude Code can reason over its own memory with the same Unix tools it already knows: `grep` for patterns, `find` for changes, `git diff` for history.

This isn't a framework to install. It's a set of conventions that Claude follows to scaffold and maintain a persistent memory system. You define the rules, Claude builds the structure, and you can observe every decision the model makes about how to organize its own knowledge.

## How It Works

Cog has no server, no runtime, no daemon. It's a project directory with conventions.

```
Open the project in Claude Code → Claude reads CLAUDE.md
 → memory/ is available as persistent storage
 → skills route conversations via slash commands
 → memory files update as you work
```

When you open a Cog project, Claude reads `CLAUDE.md` — the instruction set that defines persona, memory rules, domain routing, and skill behaviors. The `memory/` directory is the persistent knowledge base. Skills are markdown prompt files in `.claude/commands/`. That's the entire system.

No process to start. No session to manage. No infrastructure to maintain.

## Interface Agnostic

Cog's memory is just markdown files. Any Claude-powered tool with file access can use it:

- **Claude Code** — the primary interface. Terminal-native, skill routing via slash commands, real-time memory updates.
- **Cowork** — Claude Desktop's agentic mode. Point it at `memory/` and it inherits everything. Good for heavy document generation, multi-file research, long autonomous workflows. See [Using Cog with Cowork](#/cowork).
- **Any future Claude tool** — if it can read and write files, it can use Cog's memory.

The interface determines how context is loaded and how you interact. The memory system doesn't care — it's files on disk.

## Skills

Slash commands route conversations to the right domain and behavior. Each skill is a markdown prompt file in `.claude/commands/` that tells Claude what files to load and how to behave.

**Built-in skills** ship with every Cog instance:

| Skill | Domain |
| --- | --- |
| `/personal` | Family, health, calendar, day-to-day |
| `/explainer` | Writing, explanation, long-form |
| `/humanizer` | Rewrite AI text in human voice |
| `/reflect` | Self-improvement, conversation mining |
| `/evolve` | Systems architecture audit |
| `/history` | Deep memory search, recall |
| `/foresight` | Cross-domain strategic nudge |
| `/scenario` | Decision simulation, branch modeling |
| `/housekeeping` | Memory maintenance, archival |
| `/setup` | Bootstrap domains from manifest |

**Domain skills** are auto-generated from `memory/domains.yml` — add a domain to the manifest, run `/setup`, and Cog creates the skill file, memory directories, and routing rules. No code changes needed. See the [journal entry](#/journal/domain-registry) for the full story.

Skills handle their own memory loading. The main instruction set doesn't duplicate that logic — it provides the routing table so Cog knows where to look.

## Domain Registry

All memory domains are defined in a single YAML manifest (`memory/domains.yml`). The manifest is the **single source of truth** for domain structure — pipeline skills and the routing table all read from it.

```yaml
domains:
  - id: work
 path: work/acme
 type: work
 label: "Day job at Acme Corp"
 triggers: [acme, work, colleagues, projects]
 files: [hot-memory, action-items, entities, projects, dev-log, observations]
```

Each domain has a type (`personal`, `work`, `side-project`, `system`) that determines how the pipeline treats it. Work and side-project domains are automatically included in foresight scans. Domains can have subdomains for focused sub-topics.

The `/setup` skill reads the manifest and generates:

- Memory directories with starter files (hot-memory, observations, action-items, entities)
- Domain command files from `.claude/commands/_templates/domain.md`
- Updated routing table in `CLAUDE.md`

Running `/setup` is idempotent — it creates what's missing, regenerates command files from the template, and leaves everything else alone.

## Design Principles

**Simpler always wins.** Every architecture decision that survived is the simpler option. Feature velocity comes from removing complexity, not adding it. When two approaches solve the same problem, the one with fewer moving parts wins.

**Data transformation is the superpower.** The system is optimized for turning unstructured input into structured, actionable output:

- Voice note while working → entity profile update
- Photo of a document → structured tracking file
- PDF from a specialist → session notes with goals and observations
- Scattered conversation fragments → synthesized thread with narrative arc

* * *

# Cog — Cognitive Architecture for Claude Code

https://lab.puga.com.br/cog/#/memory

## Memory

## The Core Idea

Cog's memory design draws from the RLM paper (arxiv 2512.24601).

> Memory as environment, not input.

Cog doesn't try to load everything it knows into every conversation. Instead, it structures memory into three tiers — like an office:

- **Hot memory** is your desk. The 30,000-ft view of your current state — top priorities, active projects, what matters right now. Loaded into every conversation automatically. (~25 lines, cross-domain.)
- **Warm memory** is the filing cabinet across the room. Domain-specific files that only get pulled when a skill activates. Ask about your Python project and it walks over to that cabinet — it doesn't pull your grocery list.
- **Glacier** is deep storage across town. Historical archives, indexed with metadata so they're searchable without reading the full contents. Out of the way, but never lost.

The result: Cog can have hundreds of files across dozens of domains and still load only what's relevant — without reading everything up front.

## Progressive Condensation

Two processes:

**Condensation** compresses raw data into increasingly actionable layers:

```
Raw events (voice, photos, PDFs, conversation fragments)
 ↓ capture fast, timestamp, tag
Observations (append-only, per-domain)
 ↓ when 3+ observations cluster on a theme
Patterns (edit-in-place, distilled rules)
 ↓ when active or urgent
Hot Memory (rewrite-freely, ~25 lines cross-domain)
```

**Archival** moves stale data to cold storage:

```
Observations → Glacier (indexed, retrievable on demand)
```

Nothing is ever lost. Active working memory stays lean.

## File Types

| Type | Purpose | Edit Mode | Loaded When |
| --- | --- | --- | --- |
| `hot-memory.md` | Top-of-mind per domain | Rewrite freely | Every conversation (in system prompt) |
| `observations.md` | Timestamped events | Append only | When skill activates or search hits |
| `entities.md` | People, places, things | Edit in place | When someone/something is mentioned |
| `action-items.md` | Tasks and deadlines | Edit in place | Briefings, triage, when relevant |
| `patterns.md` | Distilled rules | Edit in place | Self-improvement, when behaviour repeats |
| Thread files | Deep single-topic synthesis | Current state: rewrite. Timeline: append | When topic comes up |
| `glacier/` | Archived data | Read only | Only via explicit search |

## Domain Structure

Every domain follows the same anatomy — a directory with standard file types. Domains are defined in `memory/domains.yml` (the [domain registry](#/architecture#domain-registry)) and created by the `/setup` skill:

```
memory/
  domains.yml # Manifest — SSOT for all domains
  hot-memory.md # Cross-domain top-of-mind
  personal/ # hot-memory, observations, action-items, entities, ...
  work/
 <your-job>/ # Same structure — one dir per domain
 <side-project>/
  cog-meta/ # Cog self-knowledge
  glacier/ # Archived data by domain
```

Each domain lists its files in the manifest. The pipeline skills all discover domains from this file — no hardcoded paths.

## The Memory Router

Instead of loading all memory into context, Cog gets a **routing index** — a compact map of what exists and where.

Cog uses L0 headers and CLAUDE.md routing conventions to navigate the memory directory. Rather than loading every file, Claude reads the routing table and navigates to the right files based on query type:

- "What's on today?" → `personal/calendar.md`
- "Who's on my team?" → `work/<domain>/entities.md`
- "How's the typing going?" → `personal/keyboard-typing.md` (thread)
- "Update my action items" → domain-specific `action-items.md`

The router means Cog can have hundreds of files across dozens of domains and still know exactly where to look — without reading everything up front.

> Inspired by [OpenViking](https://github.com/volcengine/OpenViking) (ByteDance), which uses L0/L1/L2 tiered loading to reduce token cost and improve routing accuracy.

Think of it like browsing a library. You read the spine of the book to see the title. If it looks relevant, you open it and check the table of contents. Only then do you turn to the chapter you need.

Every memory file has a one-line **L0 summary** near the top — a quick answer to "what would I find if I read this file?" (max 80 characters):

```markdown
# Personal — Entities
<!-- L0: Key people — family, friends, professionals, with bios and key details -->
```

Three-tier loading in practice:

- **L0** — read the spine. One-line summaries across all files (~100 tokens total) for routing decisions
- **L1** — check the table of contents. Domain files loaded when a skill activates or the router selects them
- **L2** — read the chapter. Threads and deep context loaded only when needed

L0 headers are maintained by the pipeline: [Housekeeping](#/pipeline/housekeeping) scans for missing headers, [Reflect](#/pipeline/reflect) preserves them when reorganising. See the [journal entry](#/journal/l0-progressive-loading) for the full story.

#### Grep-Based Retrieval

For pipeline skills, the recommended way to access L0 summaries is a direct grep rather than reading INDEX.md:

```bash
grep -rn "<!-- L0:" memory/{domain}/
```

This extracts every L0 header in a domain with one shell command — no file reads required. Pipeline skills use this as part of a [shell orientation pass](#/journal/unix-toolbox-orientation) that scopes work before loading any files. INDEX.md files remain useful as a human-readable reference, but for programmatic routing, grep is faster and cheaper.

## Memory Intelligence

Three research-informed improvements adopted on [Day 23](#/journal/memory-intelligence) after surveying 12 LLM memory systems:

**Bi-directional back-linking** (inspired by A-MEM, NeurIPS 2025) — When writing to file A and linking to file B, Cog also updates file B to link back to A. The knowledge graph stays connected in both directions, not just forward references.

**Temporal validity on entities** (inspired by Zep/Graphiti) — When facts change in entity files, the old value is preserved with `since/until` dates and strikethrough:

```
Role: ~~Senior Engineer (since 2023-01, until 2024-12)~~
 → Creative Technologist (since 2024-12)
```

This preserves how understanding evolved — important for a personal AI that tracks real people across years.

**Contradiction detection** (inspired by Mem0) — A systematic consistency sweep runs every [Reflect](#/pipeline/reflect) pass. For each domain's hot-memory, reflect verifies factual claims against canonical sources. Resolution: canonical file always wins; more recent wins; more specific wins over summary. Health dates and family-sensitive facts are flagged for user review, not auto-fixed.

## Threads — The Zettelkasten Layer

Threads are **read-optimised synthesis files**. While observations capture raw events (write-optimised), threads pull related fragments into a coherent narrative.

Every thread has the same spine:

- **Current State** — what's true right now (rewrite freely, always current)
- **Timeline** — dated entries, append-only, full detail preserved (never condensed)
- **Insights** — learnings, patterns, what's different this time

### What Does "Raise" Mean?

"Raise" is the verb for creating or updating a thread. When triggered:

1.  **Search fragments** — Cog searches observations and memory files for all references
2.  **Synthesise** — extract the narrative arc
3.  **Write the thread** — create or update with the Current State → Timeline → Insights spine
4.  **Link** — thread references source fragments via wiki-links

### Graduation

A thread gets raised when:

- A topic appears in **3+ observations across 2+ weeks**
- The user explicitly says "raise X" or "thread X"
- Scattered fragments no longer serve the topic well

### Rules

- **One file forever** — threads grow long, they don't split or condense
- **Texture is the value** — every entry keeps its full detail, quotes, and dates
- **Fragments never move** — threads reference them, don't replace them
- **Current State is always current** — rewrite it freely as things change

## SSOT

**Single Source of Truth.** Each fact lives in ONE canonical file. Other files reference via wiki-links, never copy.

- Action items → `action-items.md`
- Calendar → `calendar.md`
- People → `entities.md`
- Health → `health.md`

When a canonical file updates, hot-memory adjusts its framing but never duplicates the data.

* * *

# Cog — Cognitive Architecture for Claude Code

https://lab.puga.com.br/cog/#/cowork

## Using Cog with Cowork

[Cowork](https://claude.com/product/cowork) is Claude Desktop's agentic mode — it executes multi-step tasks autonomously with direct file system access. Its biggest limitation: **no memory between sessions**. Every session starts blank.

Cog's memory is entirely file-based. Cowork reads files. That's the integration — no API, no plugin, no configuration. Point Cowork at `memory/` and it inherits everything Cog knows.

## What Cowork Gets

When Cowork reads Cog's memory files, it picks up:

- **`hot-memory.md`** — identity, active situations, what matters right now
- **`*/entities.md`** — people, places, things with structured bios
- **`*/action-items.md`** — tasks with deadlines, priorities, domains
- **`*/observations.md`** — timestamped raw events and notes
- **Thread files** — deep synthesis on ongoing topics (health, family, career)

This turns Cowork from amnesiac to contextual. No need to explain your situation from scratch — Cowork already knows the family structure, work context, active projects, and preferences.

## How to Use It

Reference Cog's memory directly in a Cowork session:

```
Read my memory files in memory/ and then:
- Build a timeline of [topic] from my thread files
- Synthesise my action items into a prioritised spreadsheet
- Research [topic] using my entities and observations as context
```

Or more targeted:

```
Read memory/hot-memory.md for context about me,
then memory/personal/entities.md for family details.
Create a birthday planning doc for the next upcoming birthday.
```

| Task | Cog (Claude Code) | Cowork (Desktop) |
| --- | --- | --- |
| Quick capture (text, commands) | Yes | — |
| Real-time memory updates | Yes | — |
| Proactive nudges via /foresight | Yes | — |
| Calendar queries (via MCP) | Yes | — |
| Skill routing via slash commands | Yes | — |
| Heavy document generation | — | Yes |
| Multi-file research synthesis | — | Yes |
| Spreadsheets with formulas | — | Yes |
| Presentations and deliverables | — | Yes |
| Long autonomous workflows | — | Yes |

Cog is the persistent brain — always remembering, always routing. Cowork is the workshop — heavy lifting with full context.

Cowork can also **write** back to Cog's memory. A Cowork session that produces research or analysis can save structured output to `memory/` — observations, entity updates, or new threads. Cog's [pipeline skills](#/pipeline) pick up the changes and integrate them on the next run.

```
After your analysis, append findings to
memory/personal/observations.md
using the format: ### YYYY-MM-DD — [topic]\n- finding 1\n- finding 2
```

Two-way loop: Cog captures and structures daily life. Cowork does deep work informed by that structure. Results flow back into memory for future conversations.