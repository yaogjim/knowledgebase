---
title: "2026-06-16_github_com_steipete_birdclaw_Stores_all_your_tweets_nicely_cl"
source: "https://github.com/steipete/birdclaw"
author:
  - "[[@amelia]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "github"
  - "@amelia"
  - "pnpm"
  - "cli"
---

# steipete/birdclaw: Stores all your tweets nicely claw-able for agents.

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/steipete/birdclaw?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[feat: add blocklist import command](/steipete/birdclaw/commit/0292aa7081d4b989d809834cb1c77f765519f0ce)

[0292aa7](/steipete/birdclaw/commit/0292aa7081d4b989d809834cb1c77f765519f0ce) ·

[39 Commits](/steipete/birdclaw/commits/main/)

 |
| 

[.github/ workflows](/steipete/birdclaw/tree/main/.github/workflows "This path skips through empty directories")

 | 

[.github/ workflows](/steipete/birdclaw/tree/main/.github/workflows "This path skips through empty directories")

 | 

[ci: stop pinning pnpm twice](/steipete/birdclaw/commit/75a737ce1d635f44cb96fcc78aaf85ed72d90d8f "ci: stop pinning pnpm twice")

 |  |
| 

[.vscode](/steipete/birdclaw/tree/main/.vscode ".vscode")

 | 

[.vscode](/steipete/birdclaw/tree/main/.vscode ".vscode")

 | 

[feat: scaffold local-first workspace](/steipete/birdclaw/commit/ccf9a5eb1314b567404139f57f0597310eee8b5a "feat: scaffold local-first workspace")

 |  |
| 

[docs](/steipete/birdclaw/tree/main/docs "docs")

 | 

[docs](/steipete/birdclaw/tree/main/docs "docs")

 | 

[feat: add blocklist import command](/steipete/birdclaw/commit/0292aa7081d4b989d809834cb1c77f765519f0ce "feat: add blocklist import command")

 |  |
| 

[playwright](/steipete/birdclaw/tree/main/playwright "playwright")

 | 

[playwright](/steipete/birdclaw/tree/main/playwright "playwright")

 | 

[feat: tighten timeline and dm layouts](/steipete/birdclaw/commit/f633bfd25329369ac4f03bc45d7616fbeae40e9e "feat: tighten timeline and dm layouts")

 |  |
| 

[public](/steipete/birdclaw/tree/main/public "public")

 | 

[public](/steipete/birdclaw/tree/main/public "public")

 | 

[feat: scaffold local-first workspace](/steipete/birdclaw/commit/ccf9a5eb1314b567404139f57f0597310eee8b5a "feat: scaffold local-first workspace")

 |  |
| 

[scripts](/steipete/birdclaw/tree/main/scripts "scripts")

 | 

[scripts](/steipete/birdclaw/tree/main/scripts "scripts")

 | 

[test: stabilize blocklist e2e harness](/steipete/birdclaw/commit/6ae6621faf4a7b729d589a27d3ca856a08bc656d "test: stabilize blocklist e2e harness")

 |  |
| 

[src](/steipete/birdclaw/tree/main/src "src")

 | 

[src](/steipete/birdclaw/tree/main/src "src")

 | 

[feat: add blocklist import command](/steipete/birdclaw/commit/0292aa7081d4b989d809834cb1c77f765519f0ce "feat: add blocklist import command")

 |  |
| 

[.gitignore](/steipete/birdclaw/blob/main/.gitignore ".gitignore")

 | 

[.gitignore](/steipete/birdclaw/blob/main/.gitignore ".gitignore")

 | 

[fix: stabilize xurl transport and dm replies](/steipete/birdclaw/commit/341c1bfda00a56a0d0d96a6814361493509c4df0 "fix: stabilize xurl transport and dm replies")

 |  |
| 

[.node-version](/steipete/birdclaw/blob/main/.node-version ".node-version")

 | 

[.node-version](/steipete/birdclaw/blob/main/.node-version ".node-version")

 | 

[feat: scaffold local-first workspace](/steipete/birdclaw/commit/ccf9a5eb1314b567404139f57f0597310eee8b5a "feat: scaffold local-first workspace")

 |  |
| 

[CHANGELOG.md](/steipete/birdclaw/blob/main/CHANGELOG.md "CHANGELOG.md")

 | 

[CHANGELOG.md](/steipete/birdclaw/blob/main/CHANGELOG.md "CHANGELOG.md")

 | 

[feat: add blocklist import command](/steipete/birdclaw/commit/0292aa7081d4b989d809834cb1c77f765519f0ce "feat: add blocklist import command")

 |  |
|  |

## birdclaw

`birdclaw` is a local-first X workspace: archive import, cached live reads, focused triage, and reply flows in one local web app + CLI.

Status: WIP. Real and usable. Not done. Expect schema churn, transport gaps, and rough edges while the core settles.

- keeps your X data in local SQLite
- stores media and avatar cache under `~/.birdclaw`
- imports archives when you have them
- still works when you do not
- gives you a clean local UI for home, mentions, DMs, inbox, and blocks
- exposes scriptable JSON for agents and automation

- one shared SQLite DB for multiple accounts
- FTS5 search over tweets and DMs
- archive autodiscovery on macOS
- archive import for tweets, likes, profiles, and full DMs
- profile hydration from live X metadata
- local avatar cache
- local media cache root under `~/.birdclaw`

### Web UI

- `Home` timeline
- `Mentions` queue
- `DMs` workspace with two-column layout
- `Inbox` for mixed mention + DM triage
- `Blocks` for local blocklist maintenance
- constrained timeline lane instead of full-width dashboard UI
- tweet expansion with URLs, inline images, quoted tweets, replies, and profile hover cards
- sender bio and influence context in the DM detail header
- system / light / dark theme switcher with animated transition

- replied / unreplied filters for timelines
- DM filters by participant, followers, and derived influence score
- AI-ranked inbox for mentions + DMs
- OpenAI scoring hook for low-signal filtering
- cached live mentions export in `xurl` -compatible JSON
- live profile-reply inspection for borderline AI/slop triage

### Actions

- post tweets
- reply to tweets
- reply to DMs
- add / remove local blocks
- add / remove local mutes
- sync remote blocks through `xurl` when available

### Safety

- local-first by default
- tests disable live writes
- CI disables live writes
- app has no auth layer because it is a local-only tool

- broader resumable live sync beyond the targeted paths already wired
- fuller media fetch pipeline
- richer multi-account UX
- more complete transport coverage
- more archive edge-case handling

If you need polished product-grade sync parity today, this is not there yet.

## Screens

- `Home`: read and reply without fighting the main X timeline
- `Mentions`: work the reply queue with clean filters
- `DMs`: triage by sender context, follower count, and influence
- `Inbox`: let heuristics / OpenAI float likely-important items
- `Blocks`: maintain a local-first account-scoped blocklist

## Storage

Default root:

```
~/.birdclaw
```

Important paths:

- DB: `~/.birdclaw/birdclaw.sqlite`
- media cache: `~/.birdclaw/media`
- avatar cache: `~/.birdclaw/media/thumbs/avatars`
- Playwright test home: `.playwright-home`

Override the root:

```
export BIRDCLAW_HOME=/path/to/custom/root
```

## Requirements

- Node `24.12.0`
- `pnpm`
- macOS recommended for Spotlight archive discovery
- `xurl` optional for live reads / writes
- OpenAI API key optional for inbox scoring

## Install

```
fnm use
pnpm install
```

## Run

```
pnpm dev
```

Open:

```
http://localhost:3000
```

## Quick Start

Initialize local state:

```
pnpm cli init
pnpm cli auth status --json
pnpm cli db stats --json
```

Find and import an archive:

```
pnpm cli archive find --json
pnpm cli import archive --json
pnpm cli import archive ~/Downloads/twitter-archive-2025.zip --json
pnpm cli import hydrate-profiles --json
```

Start the app:

```
pnpm dev
```

## CLI Highlights

```
pnpm cli search tweets "local-first" --json
pnpm cli search tweets "sync engine" --limit 20 --json
```

Default `birdclaw` mode returns normalized items with `text`, `plainText`, `markdown`, author metadata, and canonical URLs:

```
pnpm cli mentions export "agent" --unreplied --limit 10
```

`xurl` mode returns `xurl` -compatible `data/includes/meta`, but cached locally so repeat reads do not keep spending API calls:

```
pnpm cli mentions export --mode xurl --limit 5
pnpm cli mentions export --mode xurl --refresh --limit 5
pnpm cli mentions export "courtesy" --mode xurl --limit 5
```

Notes:

- `--refresh` forces a live fetch
- `--cache-ttl <seconds>` tunes freshness
- filters still work in `xurl` mode; filtered payloads are rebuilt from the local canonical store after sync

```
pnpm cli search dms "prototype" --json
pnpm cli search dms "layout" --min-followers 1000 --min-influence-score 120 --sort influence --json
pnpm cli dms list --unreplied --min-followers 500 --min-influence-score 90 --sort influence --json
```

### AI inbox

```
pnpm cli inbox --json
pnpm cli inbox --kind dms --limit 10 --json
pnpm cli inbox --score --hide-low-signal --limit 8 --json
```

### Blocklist

```
pnpm cli blocks list --account acct_primary --json
pnpm cli blocks import ~/triage/blocklist.txt --account acct_primary --json
pnpm cli blocks add @amelia --account acct_primary --json
pnpm cli blocks remove @amelia --account acct_primary --json
pnpm cli ban @amelia --account acct_primary --json
pnpm cli unban @amelia --account acct_primary --json
```

Notes:

- block/unblock tries `xurl` first
- if X rejects `xurl` OAuth2 block writes, birdclaw falls back to the X web cookie session (`auth_token` + `ct0`) when available
- `blocks import` accepts newline-delimited blocklists with comments and markdown bullets

```
pnpm cli profiles replies @jpctan --limit 12 --json
```

Notes:

- for the "unsure if AI" case
- scans recent authored tweets, excludes retweets, keeps replies
- useful for spotting repeated generic praise, abstraction soup, or cross-thread templated cadence

### Mutes

```
pnpm cli mutes list --account acct_primary --json
pnpm cli mute @amelia --account acct_primary --json
pnpm cli unmute @amelia --account acct_primary --json
```

```
pnpm cli compose post "Ship local software."
pnpm cli compose reply tweet_004 "On it."
pnpm cli compose dm dm_003 "Send it over."
```

## Typical Workflow

1.  import your archive if you have one
2.  hydrate imported profiles from live X metadata
3.  use `Home` for reading
4.  use `Mentions` for reply triage
5.  use `DMs` for high-context conversation work
6.  use `Inbox` when you want AI help cutting noise
7.  use CLI exports when agents need stable JSON

## Live Transport

Current preference:

- `xurl` first

Without `xurl`, `birdclaw` still works in local/archive mode.

Check transport:

```
pnpm cli auth status --json
```

## Architecture

- SQLite is the canonical local truth
- archive import and live transport should converge on the same model
- CLI and web UI share the same normalized core
- AI ranking is layered on top of local data, not the source of truth

## Testing

```
fnm exec --using 24.12.0 pnpm check
fnm exec --using 24.12.0 pnpm test
fnm exec --using 24.12.0 pnpm coverage
fnm exec --using 24.12.0 pnpm build
fnm exec --using 24.12.0 pnpm e2e
```

Current bar:

- branch coverage above `80%`
- Playwright coverage for core UI flows

## CI

GitHub Actions runs:

- `pnpm check`
- `pnpm coverage`
- `pnpm build`
- `pnpm e2e`

Workflow: [ci.yml](/steipete/birdclaw/blob/main/Users/steipete/Projects/birdclaw/.github/workflows/ci.yml)

## Docs

- [spec.md](/steipete/birdclaw/blob/main/Users/steipete/Projects/birdclaw/docs/spec.md)
- [cli.md](/steipete/birdclaw/blob/main/Users/steipete/Projects/birdclaw/docs/cli.md)
- [data-architecture.md](/steipete/birdclaw/blob/main/Users/steipete/Projects/birdclaw/docs/data-architecture.md)

## Releases

No releases published

## Packages

No packages published

## Contributors 1

- [**steipete** Peter Steinberger](https://github.com/steipete)

## Languages

- [TypeScript 96.1%](/steipete/birdclaw/search?l=typescript)
- [JavaScript 3.3%](/steipete/birdclaw/search?l=javascript)
- [CSS 0.6%](/steipete/birdclaw/search?l=css)