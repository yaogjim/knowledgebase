---
title: "2026-06-16_github_com_teng_lin_agent_fetch_Full_content_web_fetcher_for_"
source: "https://github.com/teng-lin/agent-fetch"
author:
  - "[[@anthropic]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#16"
  - "#13"
  - "github"
  - "@anthropic"
---

# teng-lin/agent-fetch: Full-content web fetcher for AI agents — Chrome TLS fingerprinting, browser impersonation, and multi-strategy article extraction

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/teng-lin/agent-fetch?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[docs: update changelog for 0.1.5 and 0.1.6](/teng-lin/agent-fetch/commit/7632d139d5df1d8a19d23fdb2f5ae2619f151be4)

[7632d13](/teng-lin/agent-fetch/commit/7632d139d5df1d8a19d23fdb2f5ae2619f151be4) ·

[72 Commits](/teng-lin/agent-fetch/commits/main/)

 |
| 

[.github/ workflows](/teng-lin/agent-fetch/tree/main/.github/workflows "This path skips through empty directories")

 | 

[.github/ workflows](/teng-lin/agent-fetch/tree/main/.github/workflows "This path skips through empty directories")

 | 

[feat(ci): add npm publish workflow on tag push (#16)](/teng-lin/agent-fetch/commit/52b247d9cd59a0fc4b27dab6a36af1adff838faf "feat(ci): add npm publish workflow on tag push (#16)
* feat(ci): add npm publish workflow on tag push
- Add publish.yml triggered on v* tags: validates version, runs CI,
publishes to npm with provenance, creates GitHub release
- Add publishConfig for scoped public package
- Add releasing checklist to CONTRIBUTING.md
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* docs: use relative path and modern git delete syntax
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* docs: add CHANGELOG.md and update release steps with changelog section
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* fix: correct CHANGELOG release dates
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
---------
Co-authored-by: Claude Opus 4.5 <noreply@anthropic.com>")

 |  |
| 

[config](/teng-lin/agent-fetch/tree/main/config "config")

 | 

[config](/teng-lin/agent-fetch/tree/main/config "config")

 | 

[Initial commit](/teng-lin/agent-fetch/commit/4c811e4917724f947272eaa945fe039100ce7285 "Initial commit")

 |  |
| 

[scripts](/teng-lin/agent-fetch/tree/main/scripts "scripts")

 | 

[scripts](/teng-lin/agent-fetch/tree/main/scripts "scripts")

 | 

[feat: mobile API extraction for endpoints](/teng-lin/agent-fetch/commit/10d9f8de7ed26f12dca04e370d7bed825bd9b1f3 "feat: mobile API extraction for endpoints
- Rename authToken to token for consistency
- Add tokenType field to support dynamic header names
- Update mobile-extractor to use [config.tokenType] for flexible auth headers
- Support different API authentication schemes (x-access-token, authorization, etc)
Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>")

 |  |
| 

[skills/ agent-fetch](/teng-lin/agent-fetch/tree/main/skills/agent-fetch "This path skips through empty directories")

 | 

[skills/ agent-fetch](/teng-lin/agent-fetch/tree/main/skills/agent-fetch "This path skips through empty directories")

 | 

[fix: format markdown files](/teng-lin/agent-fetch/commit/9ec14ebb4bfdfb00a022dfa3fdce9e3f0c35623c "fix: format markdown files")

 |  |
| 

[src](/teng-lin/agent-fetch/tree/main/src "src")

 | 

[src](/teng-lin/agent-fetch/tree/main/src "src")

 |  |  |
| 

[.env.example](/teng-lin/agent-fetch/blob/main/.env.example ".env.example")

 | 

[.env.example](/teng-lin/agent-fetch/blob/main/.env.example ".env.example")

 | 

[Initial commit](/teng-lin/agent-fetch/commit/4c811e4917724f947272eaa945fe039100ce7285 "Initial commit")

 |  |
| 

[.gitattributes](/teng-lin/agent-fetch/blob/main/.gitattributes ".gitattributes")

 | 

[.gitattributes](/teng-lin/agent-fetch/blob/main/.gitattributes ".gitattributes")

 | 

[docs: add README badges, CI node matrix, extraction pipeline diagram …](/teng-lin/agent-fetch/commit/edbcaf506fee8fe611365fd927e57398c994b640 "docs: add README badges, CI node matrix, extraction pipeline diagram (#13)
* docs: add README badges and extraction pipeline diagram
Add npm version, Node.js version, MIT license, and CI status badges
to README. Add extraction pipeline flowchart to CONTRIBUTING.md
documenting the 8-stage fetch-and-extract workflow. Expand CI matrix
to test on Node 18, 20, 22, and 25.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* fix: drop Node 18, require >=20
Node 18 lacks the File global (added in Node 20) which undici depends
on, causing test failures. Update engines, CI matrix, and badge.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* ci: add macOS and Windows to test matrix
Run full Node version matrix (20, 22, 25) on Ubuntu. Test Node 22
on macOS and Windows to catch native binding issues (httpcloak,
better-sqlite3). 5 jobs total.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* docs: fix strategy count (7 → 9), add Nuxt and React Router
Address review feedback: update extraction strategy count from 7 to 9
across README and CONTRIBUTING.md. Add missing Nuxt payload and React
Router hydration strategies to the pipeline diagram. Fix .post-conten
typo.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* fix: enforce LF line endings for Windows CI
Prettier format:check fails on Windows because Git checks out CRLF.
Set endOfLine: "lf" in .prettierrc to normalize.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* fix: add .gitattributes to enforce LF on Windows checkout
Prettier endOfLine: "lf" catches CRLF but Git on Windows still checks
out with CRLF by default. Force LF at the Git level so format:check
passes on all platforms.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
---------
Co-authored-by: Claude Opus 4.5 <noreply@anthropic.com>")

 |  |
| 

[.gitignore](/teng-lin/agent-fetch/blob/main/.gitignore ".gitignore")

 | 

[.gitignore](/teng-lin/agent-fetch/blob/main/.gitignore ".gitignore")

 | 

[Initial commit](/teng-lin/agent-fetch/commit/4c811e4917724f947272eaa945fe039100ce7285 "Initial commit")

 |  |
| 

[.prettierrc](/teng-lin/agent-fetch/blob/main/.prettierrc ".prettierrc")

 | 

[.prettierrc](/teng-lin/agent-fetch/blob/main/.prettierrc ".prettierrc")

 | 

[docs: add README badges, CI node matrix, extraction pipeline diagram …](/teng-lin/agent-fetch/commit/edbcaf506fee8fe611365fd927e57398c994b640 "docs: add README badges, CI node matrix, extraction pipeline diagram (#13)
* docs: add README badges and extraction pipeline diagram
Add npm version, Node.js version, MIT license, and CI status badges
to README. Add extraction pipeline flowchart to CONTRIBUTING.md
documenting the 8-stage fetch-and-extract workflow. Expand CI matrix
to test on Node 18, 20, 22, and 25.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* fix: drop Node 18, require >=20
Node 18 lacks the File global (added in Node 20) which undici depends
on, causing test failures. Update engines, CI matrix, and badge.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* ci: add macOS and Windows to test matrix
Run full Node version matrix (20, 22, 25) on Ubuntu. Test Node 22
on macOS and Windows to catch native binding issues (httpcloak,
better-sqlite3). 5 jobs total.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* docs: fix strategy count (7 → 9), add Nuxt and React Router
Address review feedback: update extraction strategy count from 7 to 9
across README and CONTRIBUTING.md. Add missing Nuxt payload and React
Router hydration strategies to the pipeline diagram. Fix .post-conten
typo.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* fix: enforce LF line endings for Windows CI
Prettier format:check fails on Windows because Git checks out CRLF.
Set endOfLine: "lf" in .prettierrc to normalize.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* fix: add .gitattributes to enforce LF on Windows checkout
Prettier endOfLine: "lf" catches CRLF but Git on Windows still checks
out with CRLF by default. Force LF at the Git level so format:check
passes on all platforms.
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
---------
Co-authored-by: Claude Opus 4.5 <noreply@anthropic.com>")

 |  |
| 

[CHANGELOG.md](/teng-lin/agent-fetch/blob/main/CHANGELOG.md "CHANGELOG.md")

 | 

[CHANGELOG.md](/teng-lin/agent-fetch/blob/main/CHANGELOG.md "CHANGELOG.md")

 | 

[docs: update changelog for 0.1.5 and 0.1.6](/teng-lin/agent-fetch/commit/7632d139d5df1d8a19d23fdb2f5ae2619f151be4 "docs: update changelog for 0.1.5 and 0.1.6")

 |  |
|  |

## agent-fetch

**Full-content web fetcher for AI agents and content workflows.** Standard HTTP tools (curl, wget, or an agent's built-in web fetch) are often served truncated or different responses because servers inspect the client's network fingerprint. agent-fetch uses [browser impersonation](https://github.com/sardanioss/httpcloak) so servers respond as they would to a real browser, then runs multiple extraction strategies to pull the complete article — every paragraph, heading, and link. Also supports multi-page crawling, persistent cookies, and custom CSS selectors. Runs locally with no API keys or cloud dependencies.

Also useful for:

- **NotebookLM** can't add a URL as a source — extract the content and paste it as text
- **RAG pipelines** need clean markdown from web pages, not HTML soup or truncated summaries
- **LLM conversations** where you need the full article in context, not a 3-paragraph summary

|  | Built-in agent fetch | Cloud extraction APIs | agent-fetch |
| --- | --- | --- | --- |
| **Content** | Summary or truncation | Full (usually) | Full article text |
| **Structure** | Plain text blob | Markdown (varies) | Markdown with headings, links, lists |
| **Runs locally** | Yes | No | Yes |
| **API key required** | No | Yes | No |
| **Extraction strategies** | 1 (basic parse) | 1–2 | Multiple (Readability, JSON-LD, Next.js, RSC, WP API, text-density, CSS selectors) |
| **Open source** | N/A | Partial | Yes |

## Install

```
npm install @teng-lin/agent-fetch
```

Or run without installing:

```
npx agent-fetch https://example.com/page
```

Install the [Agent Skill](https://agentskills.io) and your agent will automatically use agent-fetch when it needs to read URLs:

```
npx skills add teng-lin/agent-fetch
```

The skill teaches agents when and how to call agent-fetch — no configuration needed.

## Quick Start

### CLI

**Getting cookies:** Export a Netscape format cookie file from your browser using the [Get cookies.txt Locally](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) Chrome extension, then pass it with `--cookie-file`. Cookies are useful for maintaining authenticated sessions or accessing content that requires login.

**Default output:**

```
Title: Page Title
Author: Author Name
Site: example.com
Published: 2025-01-26T12:00:00Z
Language: en
Fetched in 523ms
---
# Heading

Full content with **formatting**, [links](https://example.com), and structure preserved...
```

### Programmatic

```
import { httpFetch } from '@teng-lin/agent-fetch';

const result = await httpFetch('https://example.com/article');

if (result.success) {
  console.log(result.markdown); // Full article as markdown
  console.log(result.title); // "Article Title"
  console.log(result.byline); // "By John Smith"
  console.log(result.textContent); // Plain text
  console.log(result.latencyMs); // 523
}

// With options
const result2 = await httpFetch('https://slow-site.com/article', {
  timeout: 30000, // 30 second timeout (default: 20s)
  preset: 'chrome-143', // TLS preset
});
```

Crawl a site and extract articles from multiple pages with depth control:

agent-fetch runs multiple extraction strategies in parallel and picks the most complete result. No single method works for every site — modern pages use frameworks, APIs, and structured data that each require different approaches.

| Strategy | What it does | Best for |
| --- | --- | --- |
| **Readability** | Mozilla's Reader View algorithm (strict + relaxed passes) | Most pages with semantic HTML |
| **Text density** | Statistical text-to-tag ratio analysis (CETD) | Complex layouts that Readability over-trims |
| **JSON-LD** | Parses `schema.org` structured data | Sites with rich metadata |
| **Next.js** | Extracts from page props (`__NEXT_DATA__`) | Next.js sites (Pages Router) |
| **React Server Components** | Parses streaming RSC payloads | Next.js sites (App Router) |
| **WordPress REST API** | Fetches content via `/wp-json/wp/v2/` endpoints | WordPress sites (40%+ of the web) |
| **CSS selectors** | Probes semantic containers (`<article>`, `.post-content`, etc.) | Fallback for unusual layouts |

**Winner selection:** Strategies that extract 500+ characters are candidates. If text-density or RSC finds 2x more content than Readability, it wins. Otherwise, the longest result is chosen. Metadata (author, date, site name) is composed from the best source for each field across all strategies.

## Responsible Use

**Disclaimer:** This tool is intended for fetching publicly accessible web content. Users are solely responsible for:

- Complying with each website's Terms of Service and `robots.txt` directives
- Ensuring lawful use under applicable laws (including copyright, computer access, and data protection regulations)
- Obtaining necessary permissions before accessing or extracting content

The authors make no warranties about the legality of any specific use case. This tool does not grant permission to access any website or circumvent any access controls.

## License

MIT

## Releases 4

[\+ 3 releases](/teng-lin/agent-fetch/releases)

## Packages

No packages published

## Languages

- [TypeScript 97.5%](/teng-lin/agent-fetch/search?l=typescript)
- [JavaScript 2.5%](/teng-lin/agent-fetch/search?l=javascript)