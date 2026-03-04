---
title: "2026-03-02_Michael_Truell_Michael_Truell_The_third_era_of_AI_software"
source: "https://x.com/mntruell/status/2026736314272591924"
author:
  - "[[@Michael Truell]]"
published: 2026-03-02
created: 2026-03-02
description:
tags:
  - "x"
  - "@Michael Truell"
  - "agents"
  - "work"
---

# Michael Truell # The third era of AI software

**Michael Truell**

# The third era of AI software development

When we started building Cursor a few years ago, most code was written one keystroke at a time. Tab autocomplete changed that and opened the first era of AI-assisted coding.

Then agents arrived, and developers shifted to directing agents through synchronous prompt-and-response loops. That was the second era. Now a third era is arriving. It is defined by agents that can tackle larger tasks independently, over longer timescales, with less human direction.

As a result, Cursor is no longer primarily about writing code. It is about helping developers build the factory that creates their software. This factory is made up of fleets of agents that they interact with as teammates: providing initial direction, equipping them with the tools to work independently, and reviewing their work.

Many of us at Cursor are already working this way. More than one-third of the PRs we merge are now created by agents that run on their own computers in the cloud. A year from now, we think the vast majority of development work will be done by these kinds of agents.

# From Tab to agents

Tab excelled at identifying where low-entropy, repetitive work could be automated. For nearly two years, it produced significant leverage.

Then the models improved. Agents could hold more context, use more tools, and execute longer sequences of actions. Developer habits began to shift, slowly through the summer, then rapidly over the last few months.

The transformation has been so complete that today, many Cursor users never touch the tab key. In March 2025, we had roughly 2.5x as many Tab users as agent users. Now, that is flipped: we now have 2x as many agent users as Tab users and agent usage in Cursor has surged.

Agent usage in Cursor has grown over 15x in the last year.

But already this shift is giving way to something bigger. The Tab era lasted nearly two years. The second era, in which most work is done with synchronous agents, may not last one.

# Cloud agents and artifacts

Compared to Tab, synchronous agents work further up the stack. They handle tasks that require context and judgment, but still keep the developer in the loop at every step. But this form of real-time interaction, combined with the fact that synchronous agents compete for resources on the local machine, means it is only practical to work with a few at a time.

Cloud agents remove both constraints. Each runs on its own virtual machine, allowing a developer to hand off a task and move on to something else. The agent works through it over hours, iterating and testing until it is confident in the output, and returns with something quickly reviewable: logs, video recordings, and live previews rather than diffs.

This makes running agents in parallel practical, because artifacts and previews give you enough context to evaluate output without reconstructing each session from scratch. The human role shifts from guiding each line of code to defining the problem and setting review criteria.

# The shift is underway inside Cursor

Thirty-five percent of the PRs we merge internally at Cursor are now created by agents operating autonomously in cloud VMs. We see the developers adopting this new way of working as characterized by three traits:

1.  Agents write almost 100% of their code.
2.  They spend their time breaking down problems, reviewing artifacts / code, and giving feedback.
3.  They spin up multiple agents simultaneously instead of handholding one to completion.

There is a lot of work left before this approach becomes standard in software development. At industrial scale, a flaky test or broken environment that a single developer can work around turns into a failure that interrupts every agent run. More broadly, we still need to make sure agents can operate as effectively as possible, with full access to tools and context they need.

We think yesterday's launch is an initial but important step in that direction.

* * *

### 热门回复

**@ModRetro** ♥ 591 · 💬 0

Chromatic is the ultimate tribute to the Game Boy®. It has a rock solid, cool-touch metal shell and a pixel-perfect, sunlight-readable display. Play original Game Boy and Game Boy Color cartridges, plus 20+ new games made for Chromatic, with more on the way

**@nick woodward** ♥ 483 · 💬 8

Fuck, can we get the 140 character limit back please, for the love of god

**@sudheer singh** ♥ 330 · 💬 14

The part nobody talks about in the "third era": the skill ceiling for reviewing AI-generated code is actually higher than writing it yourself. You need to understand the code well enough to spot subtle bugs in patterns you didn't choose. Most teams aren't ready for that shift.

**@Heikki Hämäläinen** ♥ 26 · 💬 10

Do you think that PR driven workflow will stay relevant in the agentic era?

**@cole murray** ♥ 32 · 💬 1

we agree and are driving the open source version of it: