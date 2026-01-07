---
title: "2026-01-07_reddit_com_Meta_just_acquired_Manus_for_2_billion_I_dug_int"
source: "https://www.reddit.com/r/ClaudeAI/comments/1q2p03x/i_reverseengineered_the_workflow_that_made_manus/"
author:
  - "[[@reddit.com]]"
published: 2026-01-07
created: 2026-01-07
description:
tags:
  - "reddit"
  - "@reddit.com"
  - "https"
  - "points"
---

# Meta just acquired Manus for $2 billion. I dug int

Meta just acquired Manus for $2 billion. I dug into how their agent actually works and open-sourced the core pattern.

The problem with AI agents: after many tool calls, they lose track of goals. Context gets bloated. Errors get buried. Tasks drift.

Manus's fix is stupidly simple — 3 markdown files:

- `task_plan.md` → track progress with checkboxes
 
- [`notes.md`](http://notes.md) → store research (not stuff context)
 
- [`deliverable.md`](http://deliverable.md) → final output
 

The agent reads the plan before every decision. Goals stay in the attention window. That's it.

I packaged this into a **Claude Code skill**. Works with the CLI. Install in 10 seconds:

`cd ~/.claude/skills`

`git clone` [`https://github.com/OthmanAdi/planning-with-files.git`](https://github.com/OthmanAdi/planning-with-files.git)

MIT licensed. First skill to implement this specific pattern.

[![r/ClaudeAI - I reverse-engineered the workflow that made Manus worth $2B and turned it into a Claude Code skill](https://preview.redd.it/i-reverse-engineered-the-workflow-that-made-manus-worth-2b-v0-dkvk3d0uc3bg1.png?width=1329&format=png&auto=webp&s=fde056fb68e461b806d23435679002efaa9affb0)](https://preview.redd.it/i-reverse-engineered-the-workflow-that-made-manus-worth-2b-v0-dkvk3d0uc3bg1.png?width=1329&format=png&auto=webp&s=fde056fb68e461b806d23435679002efaa9affb0 "Image from r/ClaudeAI - I reverse-engineered the workflow that made Manus worth $2B and turned it into a Claude Code skill")

Curious what you think — anyone else experimenting with context engineering for agents?

* * *

## Comments

> **ClaudeAI-mod-bot** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgmw7w/) •
> 
> **TL;DR generated automatically after 100 comments.**
> 
> **The consensus is that OP's "$2B secret" is actually a well-known and pretty basic technique that the community is not impressed by.** Most users are skeptical of the "reverse-engineering" claim and the idea that this simple workflow is what made Manus worth billions.
> 
> - **This isn't new:** A ton of users are pointing out they've been doing this for ages. Claude Code itself often creates its own `plan.md` files without being asked, and other open-source tools like Spec-kit and APM have implemented similar workflows for a while.
> 
> - **That $2B valuation ain't for 3 markdown files:** The community is highly skeptical of the "reverse-engineering" claim, with one user summing it up as "asking Claude Code to copy Manus and it came up with a neat idea." The real value is likely in Manus's ability to use virtual machines and its massive revenue, not just a planning prompt.
> 
> - **There's a better way, anyway:** Several users pointed out a flaw in the logic. Writing to a `notes.md` file still stuffs the context with tool calls. The more advanced approach discussed in the thread is to use **subagents** to handle context-heavy tasks, keeping the main agent's context clean.
> 

> **goodtimesKC** • [112 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxemyzh/) •
> 
> I’ve been doing it like this since early 2025. Claude is currently doing this within my Claude.md which I did not ask it to do
> 
> > **dwight0** • [27 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgjpu0/) •
> > 
> > Yeah Claude taught me this over a year ago. Also calls it plan.md. 
> > 
> > > **Signal\_Question9074** • [\-5 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhobsc/) •
> > > 
> > > [u/dwight0](/user/dwight0/) That's the best validation honestly Claude itself converges on this pattern. I just packaged it for easier sharing.
> > > 
> > > > **goodtimesKC** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxjdkez/) •
> > > > 
> > > > I think it just eats up context now that they integrate the concept
> 
> **Signal\_Question9074** • [\-2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxho8rb/) •
> 
> [u/goodtimesKC](/user/goodtimesKC/) That's awesome you were ahead of the curve. The fact that Claude is doing this in your [CLAUDE.md](http://CLAUDE.md) without being asked shows this pattern works. I just formalized it as an installable skill for people who haven't discovered it yet.
> 
> > **BuddyIsMyHomie** • [4 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxjm4ub/) •
> > 
> > Sry so you are saying this is the same as going into Plan Mode?
> > 
> > > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxm1oy6/) •
> > > 
> > > [u/BuddyIsMyHomie](/user/BuddyIsMyHomie/) Nah, different thing.
> > > 
> > > Plan Mode (`/plan`) is a Claude Code feature where you enter a planning phase before execution, Claude thinks through the approach, you approve, then it executes.
> > > 
> > > My skill is about persistent markdown files that live in your project throughout execution. `task_plan.md` tracks progress with checkboxes, [`notes.md`](http://notes.md) stores research so you don't stuff context, and Claude re-reads the plan before major decisions to not lose track of goals.
> > > 
> > > You can actually use both together. enter Plan Mode to design the approach, then let my skill keep things on track during the actual work.

> **svachalek** • [53 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxeq7v4/) •
> 
> This kind of makes sense except
> 
> 1.  Recent versions of Claude code have been using persistent markdown plans for me already
> 
> 2.  I don’t get how the notes file is supposed to help anything. It seems mostly by needing tools to read and write it, it will appear repeatedly in context which emphasizes the content. But the docs say this is to prevent context “stuffing” while this effect seems to actively promote it.
> 
> 
> > **Meme\_Theory** • [11 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfrw25/) •
> > 
> > Have you noticed the plan document names? One of mine was "glorious\_narwhale.md". I felt very seen.
> > 
> > > **CalypsoTheKitty** • [4 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhksri/) •
> > > 
> > > i had eager-inventing-sloth yesterday
> 
> **lockyourdoor24** • [6 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxftt1y/) •
> 
> That’s exactly what I thought. Writing to a note makes no difference, it’s still using context. I’ve had better success with managing context by passing any context heavy tasks to subagents. Basically treating every agent like a manager that asks the subagent to do context heavy jobs and return the results. Then also having an orchestration agent that manages the main agents. Has been working well for me. I basically have a setup which can look at almost any website and build me a scraper module which plugs into my other script which runs all the scraped products through amazon and find me selling opportunities. Then i have another script which uses gpt to match the products using the titles and images and finally sends all results to sheets api and discord.
> 
> > **UnsungZ3r0** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgdbsx/) •
> > 
> > How would one learn how to create this agent / subagent / orchestration agent setup too?
> > 
> > > **Signal\_Question9074** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhr19r/) •
> > > 
> > > [u/UnsungZ3r0](/user/UnsungZ3r0/) Great question — here's how I'd start:
> > > 
> > > 1.  Understand the pattern first: The idea is simple: one "orchestrator" agent breaks tasks into chunks, delegates each chunk to a "subagent" with its own clean context, then collects results. The orchestrator stays lightweight — it only tracks progress and coordinates. The subagents do the heavy lifting.
> > > 
> > > 2.  Resources to learn from: - [https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/sdk](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/sdk) — official Anthropic docs on building agents- [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — open source framework for multi-agent orchestration- [https://github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) — role-based multi-agent framework, great for structured team - [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen) — conversational multi-agent setups
> > > 
> > > 3.  Practical starting point:
> > > 
> > > 
> > > In Claude Code, you can spin up subagents using the Task tool. Create a slash command (like /plan) that instructs Claude to break work into phases, identify what can be parallelized, and delegate context-heavy research to subagents. [u/ThreeKiloZero](/user/ThreeKiloZero/)'s comment in this thread breaks this down really well.
> > > 
> > > 4\. My next update:
> > > 
> > > I'm working on adding subagent delegation patterns to this skill. I pay for Manus ($200+/month) to study how they handle orchestration, and I'll be open-sourcing what I learn.
> > > 
> > > Start small — one orchestrator + one subagent — and scale from there. Happy to share more when I push the update.
> > > 
> > > **Cultural-Capital-579** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxi6t61/) •
> > > 
> > > I honestly, I use RooCode and it does this easily from the VSCode extension.
> > > 
> > > It has an "Orchestrator" mode, which delegates out to various other modes by creating a new task for each (which is new context), by giving it detailed and specific instructions and then has it complete and report back once done.
> > > 
> > > I'm not a huge VSCode person, I prefer Intelli-J, so I just have both open.
> > > 
> > > I would give it a shot this way, because Roo is free (and open-source), can be used with ClaudeCode (no API tokens needed). You can see if you like this style and go from there.
> 
> **burnerOfall** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgc7yo/) •
> 
> How do you connect them all? I have been doing this but with Claude cli and gemini/gpt as architects and sub agents but I want to have coding sub agents within Claude that don't drift
> 
> > **ThreeKiloZero** • [4 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgre3c/) •
> > 
> > make subagents then go manually edit the markdown. edit your [claude.md](http://claude.md) with some instructions about how to create sub agents effectively. I also made my own plan slash command and within it are details about how to plan for sub agent use and delegate the tasks. Focus all your plan creation around calling out phases, dependencies and parallelizable work. Include some instruction on the sub agent prompts and how you want their context setup, and to always use Opus as the model.
> > 
> > Now make the PRD with whatever you fancy (BMAD, Spec Kit, etc), then run your plan command against it. Now you have a plan that is broken into sub agent tasks. Main Claude thread is now the orchestrator.
> > 
> > Keep it tight.
> > 
> > In my testing the number one reason for quality degradation is too much bull shit in the process. Too many agents, mcps, long complex prompts and markdown files.
> > 
> > Leave all that context for its work and it will follow the few key commands much better and be more able to stay on target for longer uninterrupted working sessions.
> > 
> > > **Signal\_Question9074** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhompf/) •
> > > 
> > > [u/ThreeKiloZero](/user/ThreeKiloZero/) This is excellent practical advice. "Keep it tight" I try to live by that during every b2b proejct. Too many agents and complex prompts degrade quality. The PRD → plan slash command → subagent delegation flow you described is exactly the kind of upgrade I'm working toward. Will reference this when I update the repo. Thanks for taking the time to write this out.
> > > 
> > > **burnerOfall** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxh67ws/) •
> > > 
> > > Thank you! This makes a lot of sense. How do you keep the orchestrator from drifting on long projects? Are there sub agents for orchestrating too?
> 
> **Signal\_Question9074** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhqgje/) •
> 
> [u/burnerOfall](/user/burnerOfall/) Check [u/ThreeKiloZero](/user/ThreeKiloZero/)'s reply above. they broke down the subagent orchestration pattern really well. PRD → plan slash command → delegate to subagents. That's the direction I'm headed for the next update.
> 
> **Signal\_Question9074** • [0 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhoghi/) •
> 
> [u/lockyourdoor24](/user/lockyourdoor24/) This is it buddy!. The subagent approach for context-heavy tasks makes a lot of sense and it keeps everything clean and modular. it also delegate the heavy lifting. Your scraper → Amazon → matching → Sheets pipeline sounds legit. I'm going to look into adding subagent delegation to the next version of the skill. Thanks for sharing your setup.
> 
> **Outrageous-Thing-900** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgh1hx/) •
> 
> I think it’s easier for the agent to remember to check on the file to check its progress instead of remembering the progress in its entirety the whole time without losing track of any details
> 
> **Flanhare** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxf72mp/) •
> 
> 1.  You mean it does that without you telling it to?
> 
> 
> > **CzyDePL** • [9 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfe6wk/) •
> > 
> > Yes
> 
> **Signal\_Question9074** • [\-1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhmuhm/) •
> 
> [u/svachalek](/user/svachalek/) You're raising a valid point. Writing to [notes.md](http://notes.md) does put tokens in context via tool calls you're correct. The benefit is about *attention*, not token count. By re-reading the plan before decisions, goals stay in the attention window even after 50+ tool calls. That said, several people here have suggested subagents for context-heavy work . I'm looking into adding that to the next version. Appreciate the technical pushback.

> **Cobuter\_Man** • [45 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxet0ow/) •
> 
> Pretty basic stuff tbh. Useful in general but essentially is just a 'first plan, then execute' workflow with these central/ constitutional docs, fitted in an Agent Skill. Spec-kit does exactly this only not using Skills and it released in September 2025 and is compatible with CC. APM does this too (wo Skills) and was released in May 2025 - but it also distributes context across multiple CC instances to not overfill any agent's context, and uses a general orchestrator to keep everything in place.
> 
> Manus being worth 2B is generally not because of this workflow.
> 
> Spec-kit: [https://github.com/github/spec-kit.git](https://github.com/github/spec-kit.git)
> 
> APM: [https://github.com/sdi2200262/agentic-project-management](https://github.com/sdi2200262/agentic-project-management)
> 
> > **Signal\_Question9074** • [\-4 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhn320/) •
> > 
> > [u/Cobuter\_Man](/user/Cobuter_Man/) Appreciate the links to Spec-kit and APM hadn't seen APM before and the distributed context approach is smart. You're right this is a "plan then execute" pattern, not revolutionary. I packaged it as a Claude Code skill because that specific implementation didn't exist yet. The $2B headline was for engagement, but you're correct the valuation is about their full platform, not just the workflow. Will check out APM more closely.
> > 
> > **Signal\_Question9074** • [\-4 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhnjep/) •
> > 
> > I gotta tell you something else... if you want to experience one of the craziest planning sessions with your favorite LLM, go through this with Codex/Claude Code — whatever you want, just give it a try. [bmad-code-org/BMAD-METHOD: Breakthrough Method for Agile Ai Driven Development](https://github.com/bmad-code-org/BMAD-METHOD)

> **dashingsauce** • [17 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxf711r/) •
> 
> I’m sorry are we just reinventing notes and planning? Why is this a discovery?
> 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhnsme/) •
> > 
> > [u/dashingsauce](/user/dashingsauce/) Essentially, **YES** but structured for LLM context management. The insight is *when* to read/write these files (before every decision) to keep goals in the attention window. Not a discovery, just a packaged pattern. Some find it useful, some already do it naturally.

> **lucianw** • [24 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxexkwr/) •
> 
> Thanks for the write up.
> 
> Could you say more about "I dug into how their agent actually works" -- how? Is manus a binary written in Python and you read the code? Did you find this by asking manus about itself and trust the answer isn't hallucination? Did you read the prompts?
> 
> > **Primary\_Bee\_43** • [13 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgia7i/) •
> > 
> > no they just took one small part of how it works and called it reverse engineering
> > 
> > > **Signal\_Question9074** • [\-3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhnpzt/) •
> > > 
> > > [u/Primary\_Bee\_43](/user/Primary_Bee_43/) Fair criticism. You're right this is one pattern from their system, not the full architecture. "Reverse-engineered" was strong wording. I'm paying for Manus monthly to study more of how it works, and I'll keep updating the repo. Appreciate the honesty.
> 
> **Signal\_Question9074** • [0 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhlyqq/) •
> 
> [u/lucianw](/user/lucianw/) Fair question. Three sources: (1) Manus's own blog post on context engineering where they explain their markdown workflow, (2) I pay for Manus ($200+/month) and study how it operates on real tasks, (3) intercepting and analyzing its behavior patterns. This skill captures the core pattern. not the full system. I'll be updating it with more depth as I learn more. Appreciate the push for clarity.
> 
> > **lucianw** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhpwfj/) •
> > 
> > Thanks! How do you intercept?
> > 
> > I wrote [https://github.com/ljw1004/antigravity-trace](https://github.com/ljw1004/antigravity-trace) which intercepts all traffic that Antigravity makes (both to the LLM endpoint, but also between the extension and the underlying golang binary). So I got a complete log of every single thing it intercepted.
> > 
> > I also wrote [https://github.com/ljw1004/codex-trace](https://github.com/ljw1004/codex-trace) which intercepts all traffic between the Codex VSCode extension and the underlying binary it shells out to.
> > 
> > But I can't understand how you'd intercept anything from Manus. It runs in their cloud, right? So you have no control over it, nor access to its underlying binaries?
> > 
> > > **Signal\_Question9074** • [0 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxin3f9/) •
> > > 
> > > [u/lucianw](/user/lucianw/) Just went through both repos seriously impressive work.
> > > 
> > > The antigravity-trace approach is clever: shadow extension (higher-versioned copy that loads preferentially), binary wrapper (Python invokes real binary while logging), and JS injection for HTTPS traffic. That's thorough you're capturing protobuf, REST calls, and LSP comms without breaking anything.
> > > 
> > > codex-trace is cleaner Python wrapper that spawns the real `codex mcp` binary while capturing stderr with RUST\_LOG tracing. Smart approach.
> > > 
> > > You're absolutely right to push back on "intercept" for Manus. Let me be precise about what I actually did:
> > > 
> > > 1.  Primary source: Manus's own blog post They published a detailed write-up on context engineering. The 3-file pattern comes directly from that.
> > > 
> > > 2.  Active research I pay for Manus and run real tasks through it. I analyze every response, break down how it structures outputs, and document the patterns. I'm also collecting info from both Chinese and Western sources Manus originated in China and there's valuable documentation and discussion in both ecosystems that most English-speaking devs miss.
> > > 
> > > 3.  Behavioral analysis, not binary interception You're right, Manus runs in their cloud. I can't intercept internal calls like you can with local tools. What I can do is study outputs, observe file structures, and reverse-engineer the logic from behavior not the code.
> > > 
> > > 
> > > So "reverse-engineered" was strong language. More accurate: "studied their published methodology + observed their system in action + implemented the pattern."
> > > 
> > > Your interception approach is actually more rigorous than what I did. Appreciate the precision check.
> > > 
> > > > **AmbitiousButthole** • [6 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxitsi6/) •
> > > > 
> > > > Are you just... replying to peoples messages with the AI output?
> > > > 
> > > > > **Signal\_Question9074** • [0 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxj2fgx/) •
> > > > > 
> > > > > Hey bud, nope, i jsut format my thoughts better, im dyslexic and it help me correct my grammer and find better words than what i commonly use. been working home office since 2019 it definitly took a toll on my "speaking" style i think.

> **juzatypicaltroll** • [27 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxf71oq/) •
> 
> You mean they paid 2B for 3 markdown files?
> 
> > **Aromatic-Ad6942** • [12 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgavv4/) •
> > 
> > Reverse engineering!
> > 
> > **Acrobatic\_Impress306** • [8 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxglrxv/) •
> > 
> > They paid 2B for a company generating 100m+ in 6 months
> > 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhng83/) •
> > 
> > [u/juzatypicaltroll](/user/juzatypicaltroll/) Haha no they paid $2B for a company doing $100M+ revenue in 6 months, with VM capabilities, browser automation, and a full agent platform. The 3-file pattern is one piece of their context engineering. I open-sourced that piece because it's useful on its own. The headline was punchy, I'll admit. 😅

> **OldWitchOfCuba** • [6 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgjdaf/) •
> 
> Dear lord stop it with these dumb posts

> **iamzamek** • [16 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxf247z/) •
> 
> So why they are billionaires, not you?
> 
> > **Signal\_Question9074** • [9 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfnpwz/) •
> > 
> > Good point buddy. you and i are next amen.

> **m3umax** • [12 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxeotlk/) •
> 
> How does this not "stuff the context"?
> 
> Every single time the agent has to write to the notes file, those are tokens in the write tool call that "stuff" the context? It has to output the exact tokens the results of its research to notes.md as output tokens.
> 
> Don't tool calls persist in the context?
> 
> > **Keep-Darwin-Going** • [4 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxg2khh/) •
> > 
> > The problem is needle in the haystack. Llm all suffer from the same problem which is they start forgetting and miss stuff as the context filled up so some context keep getting sent to refresh it aka context stuffing. So the alternative that Claude code does is it comes up with a plan write it to the file, remind itself that everytime they are done they refer to this file update it take the next item and continue, thereby giving the impression that it can handle long task.
> > 
> > **welcome-overlords** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxetaju/) •
> > 
> > Ive been creating multiagent systems where theres a separatw context for sub agents who do tasks, so it doesnt pollute the context window
> > 
> > > **m3umax** • [5 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxeu5h5/) •
> > > 
> > > Yeah. If I were to riff off of this guys skill.md, I'd put in specific instructions that all the implementation and research stuff must be done by a subagent who then reports research and notes to notes.md and updates the task.md.
> > > 
> > > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhoown/) •
> > > 
> > > [u/welcome-overlords](/user/welcome-overlords/) Exactly subagents with their own context is the cleaner approach for heavy tasks. Several people have suggested this. Adding it to my list for the next version. Thanks.

> **\_blkout** • [4 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxez0z0/) •
> 
> manus literally a rip of other peoples work any way so this is fitting. They must have really pissed you off huh

> **AppealSame4367** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgc1kg/) •
> 
> Why is it always some stupid thing like this? Reminds me of "Wunderlist" -> a freakin task app and nothing more. Bought by Microsoft for a lot of money, worth nothing afterwards. Also can't see how a task list app would have killed of OneNote or Outlook.
> 
> It solves nothing, it doesn't advance the buyers portfolio, it doesn't eliminate serious competition. Maybe some stupid software licensing bs from the US.

> **NINJAMANE2000** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgtlws/) •
> 
> this is not even close to capturing the value of Manus. Claude already does this lol.
> 
> You missed Manu's ability to breakdown the original task to then orchestrate sub agents and leverage different LLMs in a continuous feedback loop.
> 
> > **Signal\_Question9074** • [0 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhr6fe/) •
> > 
> > [u/NINJAMANE2000](/user/NINJAMANE2000/) Fair point this is the 3-file pattern, not the full orchestration layer. You're right that Manus does subagent coordination with different LLMs. I'm paying for Manus to study that side of it, and the next update will move in that direction. Appreciate the feedback.

> **DasBlueEyedDevil** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhcbat/) •
> 
> I like my approach better, but I'm biased.
> 
> [https://dasblueyeddevil.github.io/Daem0n-MCP/](https://dasblueyeddevil.github.io/Daem0n-MCP/)
> 
> > **IversusAI** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxk8gwu/) •
> > 
> > I absolutely LOVE this! Such clever packaging.
> > 
> > **Signal\_Question9074** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhea64/) •
> > 
> > freaking awesome website brother!

> **GrimCandy** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhf6zx/) •
> 
> They actually do some slightly more complex stuff for context management at least according to this talk from them [https://youtu.be/6\_BcCthVvb8?si=UUFiPg4jQJumUYoP](https://youtu.be/6_BcCthVvb8?si=UUFiPg4jQJumUYoP)
> 
> > **Signal\_Question9074** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhluds/) •
> > 
> > [u/GrimCandy](/user/GrimCandy/) Great share. I've watched this one. You're right, they do more complex stuff under the hood. This skill captures the core 3-file pattern, but I'm paying for Manus monthly ($200+) to study the full system. Planning to update the repo with more realistic implementations soon. Thanks for linking this for others!

> **\-becausereasons-** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxj4v9o/) •
> 
> I've been a Manus member since day 01, but honestly the model they use is just dumb. They likely use the Sonnet or worse; either way it makes an insane amount of absolutely stupid mistakes even with amazing context and prompting. Makes shit up CONSTANTLY... (slightly off topic)
> 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxj60zi/) •
> > 
> > hmmm interesting. well we definitely **DO NOT** use it for coding, but researchign and creating slids and artifacts but never for coding. the thing is buddy that the fact is that if you put a bad model against a superior model in a one shot or similar training it will not work even if both got reasoning on *godmode*. its the reasoning that makes a difference and thats where i agree with you that there is maybe a series of routed models but the multiple thinking steps is what makes the difference

> **scodgey** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxetwpl/) •
> 
> I don't know if this is anything particularly new tbh, but nice to have it in isolation for those not in the know. Unless there is something new here?
> 
> Antigravity does this in its brain already, and many already do this with their claude code setups. Also pretty much what the sdk does i think?
> 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhnzfq/) •
> > 
> > [u/scodgey](/user/scodgey/) You're right it's not new many people have been doing this. I packaged it as a Claude Code skill because that specific format didn't exist. If you're already doing this in your setup, this probably won't add much. For people starting out, it's a quick install. Appreciate the context on Antigravity will check it out.

> **Bhilthotl** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxf3l4m/) •
> 
> CLINE is calling you bro...

> **MessageEquivalent347** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxlwsqj/) •
> 
> Thanks, I will try it 👍
> 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxm09y5/) •
> > 
> > [u/MessageEquivalent347](/user/MessageEquivalent347/) Let me know how it goes 🙏

> **\_number** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxqbfya/) •
> 
> What made Manus 2B was not vibe coders but shadow users, usually happens when you want to inflate the value of the company so someone buys it.

> **tabdon** • [5 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxeoh9n/) •
> 
> That's awesome. How did you discover how they did it?
> 
> > **HeavyCoffeeDrinker99** • [3 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxf6dcl/) •
> > 
> > Maybe this? My PoV of Key point is keep context as a markdown checklist.
> > 
> > [https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
> > 
> > * * *
> > 
> > EDIT:
> > 
> > I've always Break-down a Large pile of tasks to headings and todo list, add Contextual Logs to same markdown file.

> **SheepherderOwn2712** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxeqlik/) •
> 
> define "reverse engineer"
> 
> > **paplike** • [11 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxesycf/) •
> > 
> > It roughly means “I asked Claude Code to copy Manus and it came up with a neat idea, but it was oversold as ‘reverse engineering’”
> > 
> > **Not-Kiddding** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxet25n/) •
> > 
> > Cloning?
> > 
> > **deadcoder0904** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxg0htl/) •
> > 
> > i watched a video today that did it for cc - [https://www.youtube.com/watch?v=i0P56Pm1Q3U](https://www.youtube.com/watch?v=i0P56Pm1Q3U)
> > 
> > basically, read their unminified code & publish findings. u can do this easily nowadays with gemini 1 million token window.
> > 
> > or intercept requests using browser which is how the above video is doing.
> > 
> > if ur asking basic definition, then it just means copying other people's techniques on why something worked. for ex, mr.beast goes viral. analyse his last 10 yt shorts, take notes on pacing, psychology, content, words used, clothes worn, etc...., then recreate it to go viral urself.

> **Signal\_Question9074** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfobet/) •
> 
> Just want to say, the response to this has been unreal. 160+ stars in under 24 hours. I'm reading every single comment, and I'll be updating the repo based on the feedback here. Some of you raised valid points about context stuffing and subagents, I'm actively paying $200+/month for Manus itself to study how they actually handle this, and the next update will reflect that. Appreciate all of you. 🙏

> **conradr** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxeqinh/) •
> 
> Thanks for sharing this !

> **ukSurreyGuy** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfa2az/) •
> 
> Dear OP, great share you say you have reverse engineered Manus agent?
> 
> obvious question but
> 
> Q. how do you know that you have reverse engineered Manus?
> 
> Q. what evidence confirms framework shares approach? Manus agent Vs your agent
> 
> are these .MD files on Manus ? their file format? prompt ?

> **ClaudeAI-mod-bot** • [\-2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxek495/) •
> 
> **If this post is showcasing a project you built with Claude, please change the post flair to Built with Claude so that it can be easily found by others.**

> **CuTe\_M0nitor** • [\-1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxev8a2/) •
> 
> Fucking amazing 🤩 Just shows how bad and worthless Meta is. Some engineering reversed the code for Claude Code and it's basically just a prompt flow. We live in a time where prompts are the new programming language
> 
> > **Signal\_Question9074** • [\-1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfqxbv/) •
> > 
> > RIGHT ON THE SPOT BUDDY! CHECK THIS DOPE ASS PROJECT OUT [NERD - No Effort Required, Done](https://www.nerd-lang.org/) ITS NOT MINE BUT SH\*T IS GETTING SERIOUS!

> **lucasvtiradentes** • [\-5 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxekno7/) •
> 
> Awesome work i was thinking in a way to create a custom plan command for me, this post is in the best timing. Thanks!
> 
> > **Signal\_Question9074** • [0 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfr12i/) •
> > 
> > <3 THANK YOU man! i love open source. dude this is the best feeling in the world to feel useful with our work!

> **Dull-Instruction-698** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxf5ben/) •
> 
> I’ll buy you for 2B

> **Crypto\_gambler952** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfbp9n/) •
> 
> This is essentially how I have been using Claude code for a long while now; Keep Claude.md very light, outlining main expectations on behaviour and methodology. With info on a bunch of other md files that are to be read when applicable, e.g. there’s no point polluting context about database stuff when the task at hand has absolutely nothing to do with database.
> 
> Now that some of my projects have gotten very large, even my todo tasks are broken into phases.
> 
> Here are some extra tips, explain to Claude that it can add tasks and subtasks to the md file, and maintain a wishlist too, so that features and tasks that are not part of the stuff currently worked on don’t cloud the tasks.md that describe what your call deliverables.

> **ZbigniewOrlovski** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfbun9/) •
> 
> From my experience reminding Claude each time does not make any sense.

> **Logical-Reputation46** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfi25v/) •
> 
> Is it possible for free users to experiments with new agent skills?
> 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhpry0/) •
> > 
> > [u/Logical-Reputation46](/user/Logical-Reputation46/) Skills work on Claude Code which requires API access or a Pro subscription. Free tier has very limited usage. The skill itself is free and open source the bottleneck is Claude Code access.
> > 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhq78i/) •
> > 
> > BUT BUDDY!!! wathc out! skills is going to be something **ON** by default in almost every single agentic web app or software in the near future and you might see it or might not but anyway pre cleaned and defined data already being injected into teh LLM on cloud platforms like azure ai foundary and skills as well SO.... the point is, skills is going to be a software thing, not some silly CLI or platform, its part of each agentic sofeware like LTM, HITL, Short memeory, context window, trimming, streaming, chunking, embedding, invoking, function execution and blahblahnlahblha...
> > 
> > > **Logical-Reputation46** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxks3d5/) •
> > > 
> > > Thanks for your explanation

> **vickey97** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfiw9e/) •
> 
> Hey, sorry for the unrelated question, I’d really appreciate some insight.
> 
> So far, I’ve only used ChatGPT through the browser. I used Claude the same way in the past, but the more time I spend in this sub, the more I feel like I’m missing out on how people are actually using these tools productively.
> 
> I’ve seen mentions of Claude Code, using Claude via the CLI, and even integrations inside VS Code. Could you share what a good setup looks like and how everyone uses Claude day-to-day effectively?
> 
> I want to get started with Claude Code in an effective way. My goal is to replace ChatGPT with a better tool.
> 
> Also, do I need a paid plan for this? I currently have the $20 ChatGPT plan, would something similar be required for Claude, and if so, which plan is sufficient for a non-hardcore user?
> 
> Thanks in advance!

> **Cedar\_Wood\_State** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxfve02/) •
> 
> Co-pilot also have something basically the same. You have to ‘review’ the steps before executing one by one

> **Empty-Employment8050** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgbdr0/) •
> 
> Roocode

> **EternalNY1** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxge1c4/) •
> 
> This is ... uh ... exactly how I've been working with Claude Code since forever.
> 
> Apparently this is a $2 billion idea?
> 
> [CLAUDE.md](http://CLAUDE.md) + [living-document.md](http://living-document.md)
> 
> Claude will read that and say "Should I implement phase 2" and then when done, tell it to update [living-document.md](http://living-document.md) with the "state of the state".
> 
> Type /clear, repeat - done.
> 
> I didn't realize I was doing something revolutionary. 😂
> 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhrf13/) •
> > 
> > [u/EternalNY1](/user/EternalNY1/) Haha you were already doing the $2B workflow! The fact that multiple people independently converged on this pattern is validation that it works. I just packaged it for people who haven't discovered it yet.

> **gantamk** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxge6p6/) •
> 
> Amazing. I wonder what the future of software is going to be. Mainly for enterprises?
> 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhqvsx/) •
> > 
> > [u/gantamk](/user/gantamk/) Thanks! Honestly, I think we're watching it happen in real-time. Context engineering is becoming a discipline. Exciting times. and as well, its the era of AGENT ENGINEER, because an Agent engineer IS a software engineer BUT they simply can build with their know-how of cloud, api's, and all the things we do now as well agentic abilities.

> **Zappa\_Dog** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgid76/) •
> 
> M'anus is impressed.

> **jammy-git** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgke4i/) •
> 
> Surely what made Manus so valuable was not just this, but the ability to spin up a virtual machine and use that VM to accomplish tasks that other LLMs could not do by themselves?

> **jwikstrom** • [1 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxgpwj3/) •
> 
> Check out my mCP that admittedly needs to be cleaned up a bit. Why use markdown and have to read the while thing or find the spot in the file? Use SQL. It's basically lightweight JURA as an MCP. [https://github.com/heffrey78/lifecycle-mcp](https://github.com/heffrey78/lifecycle-mcp)
> 
> > **Signal\_Question9074** • [2 points](https://reddit.com/r/ClaudeAI/comments/1q2p03x/comment/nxhr8a5/) •
> > 
> > [u/jwikstrom](/user/jwikstrom/) Interesting approach. SQL instead of parsing markdown. I can see the benefit for larger projects where finding specific items matters. Will check it out. Thanks for sharing!