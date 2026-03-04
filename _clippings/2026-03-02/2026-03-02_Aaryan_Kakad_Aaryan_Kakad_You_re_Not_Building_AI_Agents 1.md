---
title: "2026-03-02_Aaryan_Kakad_Aaryan_Kakad_You_re_Not_Building_AI_Agents"
source: "https://x.com/aaryan_kakad/status/2028186694932214187"
author:
  - "[[@Aaryan Kakad]]"
published: 2026-03-02
created: 2026-03-02
description:
tags:
  - "x"
  - "@Aaryan Kakad"
  - "agents"
  - "agent"
---

# Aaryan Kakad # You're Not Building AI Agents.

**Aaryan Kakad**

# You're Not Building AI Agents. You're Building LLM Wrappers.

Before you think this is an AI slop article. Let me introduce myself.

Aaryan here ~ a 19 year old who's been self learning ML and Agentic AI for over a year now. No CS degree. No bootcamp.

Most people are getting "agents" wrong. They see them as "LLM WRAPPERS" with some extra steps.

They are much more than that if used like they were designed to be used.

This is what agents actually are when you stop wrapping and start architecting.

* * *

## What are AI agents and what problem do they solve?

In simple words, AI agents are semi or fully autonomous systems that use LLMs to perceive, reason, plan, adapt and act on their own.

But why do we really need them?

LLMs don't have proper memory management, they don't have the ability to plan and act on their own.

Humans can use them to become informed and then act using that info.

But agents can do all of them permissionlessly.

* * *

## What are the key features of an AI agent?

- It reasons, uses logic and available information to draw conclusions, make inferences, and solve problems.
- It acts, performs tasks based on decisions, plans or external inputs. This includes physical action in the case of embodied AI, digital actions like sending messages, updating data, etc.
- It observes, gathers essential information about the environment or situation.
- It plans, develops a strategic plan to achieve goals.
- It collaborates, works effectively with humans or other AI agents.
- It self-refines, some of the agents have the ability to self improve, these are the ELITE TIER agents, the capacity to self improve and learn from experience and feedbacks is the hallmark of an advanced AI agent.

* * *

## What is the difference between a "LLM Wrapper" and an actual AI agent?

There is one major difference between a wrapper and agent, HARDCODING.

Some people just create .md files and write code to generate LLM queries. That is a pure LLM wrapper.

That's just a prompt. You could paste it directly into a LLM and get the same result.

But agents are different.

In agents, we write tools that could be helpful in getting to our final output, and we don't HARDCODE stuff, we give the LLM and the agent, the freedom to choose tools it wants to use whenever needed.

I learned this the hard way.

People criticized me for months, because all I was doing was writing a single function that had LLM queries with some comprehensive prompts, thats it.

That was more like a workflow rather than agent.

Agency is having the ability to act, reason, plan, collaborate and do stuff on its own autonomously or semi-autonomously.

Here's a real world example:

Wrapper: 'Here's the user's email, write a reply.' → LLM outputs reply. Done.

Agent: 'Handle this email.' → Agent reads it, checks your calendar, drafts a reply, schedules a follow-up, sends it. You never touched it.

* * *

The agentic loop - this is what separates a wrapper from an agent.

## How to actually architect an AI agent?

Most agents follow the loop of - perceive, plan, act, observe, self improve and repeat as shown in the above image.

What are tools and how do they make an agent better?

Tools are decorated functions that help the agent in getting access to external data sources.

For example, if you want to build a weather agent, you need access to the live weather data, and tools help agents in accessing that data using some APIs or MCPs.

Their one major benefit is that they let agents gather enough information/context before taking decisions.

One more example is, if you want to build a research agent, you need to do some web scraping, scrape data from some verified sources.

To scrape such data, we can write web search tools for it using tools like @firecrawl, Serper, etc.

What is memory and how does it make an agent better?

Memory is storing required data. That's it.

In agents, there are two types of memories:

1.  Long term memory: the data you need throughout your agent's life.
2.  Short term memory: the data you need for some specific situations.

How do they make an agent better?

Modern LLMs are not so good at memory, the maximum context window we have is 1M, which is still good but agents can have infinite data stored using RAG.

Retrieval Augmented Generation.

Its a process - that includes - ingesting data, dividing them into chunks, converting them into vector embeddings (suitable for vector search), and then retrieving relevant data.

It retrieves relevant data using vector search - calculating the difference between vectors - the lesser the difference, the more relevant the chunk is. And the most relevant chunk is then used.

That's it.

Tools give your agent reach. Memory gives it context. The loop gives it autonomy. Put all three together and you stop building wrappers forever.

And most importantly, LLM is the brain of your agent, it chooses what tools to use, what data from the memory to use, everything.

So, the better model you use, the better results you get.

* * *

The one major difference between wrappers and agents is HARDCODING.

Agents are the next big thing - especially enterprise agents. They won't just reduce costs. They'll make the cost-per-output of an entire team look embarrassing.

You now have the full picture. Tools, memory, the loop, the LLM as the brain. Now go and actually build something.

I'm Aaryan. I write about ML, AI, specifically Agentic AI from the perspective of someone actually building it - not theorizing about it. Find me at @aaryan\_kakad.