---
title: 2025-09-19_@willmacaskill_mini-review of “If anyone builds it, everyone dies”
source: https://x.com/willmacaskill/status/1968759901620146427
author:
  - "[[@willmacaskill]]"
published: 2025-09-19
created: 2025-09-19
description: 
tags:
  - "@willmacaskill"
  - "#AI安全"
  - "#中文机器翻译"
  - "#超级智能"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**William MacAskill** @willmacaskill [2025-09-18](https://x.com/willmacaskill/status/1968759901620146427)

Here’s a mini-review of “If anyone builds it, everyone dies”:  
  
tl;dr: I found the book disappointing. I thought it relied on weak arguments around the evolution analogy, an implicit assumption of a future discontinuity in AI progress, conflation of “misalignment” with “catastrophic misalignment”, and that their positive proposal was not good.  
  
I had hoped to read a Yudkowsky-Soares worldview that has had meaningful updates in light of the latest developments in ML and AI safety, and that has meaningfully engaged with the scrutiny their older arguments received. I did not get that.  
  
I think if a younger version of me had read this as my first exposure to the field, I’d have either bounced off altogether (if I’d correctly assessed that the arguments are not-good), or come away with substantively the wrong strategic picture. This is a shame, because I think the risk of misaligned AI takeover is enormously important.  
  
In more detail:  
  
\*\*The evolution analogy\*\*  
  
Illustrative quote: “To extend the \[evolution\] analogy to AI: \[...\] The link between what the AI was trained for and what it ends up caring about would be complicated, unpredictable to engineers in advance, and possibly not predictable in principle.”  
  
Evolution is a fine analogy for ML if you want to give a layperson the gist of how AI training works, or to make the point that, off-distribution, you don’t automatically get what you trained for. It’s a bad analogy if you want to give a sense of alignment difficulty.  
  
Y&S argue:  
  
1\. Humans inventing and consuming sucralose (or birth control) would have been unpredictable from evolution’s perspective, and is misaligned with the goal of maximising inclusive genetic fitness.  
  
2\. The goals of a superintelligence will be similarly unpredictable, and similarly misaligned.  
  
But our training of AI is different to human evolution in ways that systematically point against reasons for pessimism.  
  
The most basic disanalogy is that evolution wasn’t trying, in any meaningful sense, to produce beings that maximise inclusive genetic fitness in off-distribution environments. But we will be doing the equivalent of that!  
  
That alone makes the evolution analogy of limited value. But there are some more substantive differences. Unlike evolution, AI developers can:  
  
\- See the behaviour of the AI in a very wide range of diverse environments, including carefully curated and adversarially-selected environments.

\- Give more fine-grained and directed shaping of individual minds throughout training, rather than having to pick among different randomly-generated genomes that produce minds.

\- Use interpretability tools to peer inside the minds they are creating to better understand them (in at least limited, partial ways).

\- Choose to train away from minds that have a general desire to replicate or grow in power (unlike for evolution, where such desires are very intensely rewarded).

(And more!)  
  
These differences sure look meaningful and helpful for training aligned AIs. A good discussion of the evolutionary analogy would have included an even-handed discussion of the disanalogies, or discussion of whether other analogies (like selective breeding, which with very blunt tools turned wolves into golden retrievers) are better; but this was lacking.  
  
\*\*Discontinuities\*\*  
  
“The engineers at Galvanic set Sable to think for sixteen hours overnight.  
  
A new sort of mind begins to think.”  
  
The classic EY AI takeover story involved a discontinuity in capabilities: AI making a “sudden, sharp, large leap in intelligence” (from “AI as a positive and negative factor”). This idea continues to appear (though to a less extreme degree) in IABIED, for example in the Sable story, where a single 16‑hour run across ~200,000 GPUs yields qualitatively new cognitive capabilities.  
  
Sudden, sharp, large leaps in intelligence now look unlikely. Things might go very fast: we might well go from AI that can automate AI R&D to true superintelligence in months or years (see Davidson and Houlden, “How quick and big would a software intelligence explosion be?"). But this is still much slower than, for example, the “days or seconds” that EY entertained in “Intelligence Explosion Microeconomics”. And I don’t see any good arguments for expecting highly discontinuous progress, rather than models getting progressively and iteratively better.  
  
In Part I of IABIED, it feels like one moment we’re talking about current models, the next we’re talking about strong superintelligence. We skip over what I see as the crucial period, where we move from the human-ish range to strong superintelligence\[1\]. This is crucial because it’s both the period where we can harness potentially vast quantities of AI labour to help us with the alignment of the next generation of models, and because it’s the point at which we’ll get a much better insight into what the first superintelligent systems will be like. The right picture to have is not “can humans align strong superintelligence”, it’s “can humans align or control AGI-”, then “can {humans and AGI-} align or control AGI” then “can {humans and AGI- and AGI} align AGI+” and so on.  
  
Elsewhere, EY argues that the discontinuity question doesn’t matter, because preventing AI takeover is still a ‘first try or die’ dynamic, so having a gradual ramp-up to superintelligence is of little or no value. I think that’s misguided. Paul Christiano puts it well: “Eliezer often equivocates between “you have to get alignment right on the first ‘critical’ try” and “you can’t learn anything about alignment from experimentation and failures before the critical try.” This distinction is very important, and I agree with the former but disagree with the latter.”  
  
(I agree with Y&S that there are major special challenges that arise once model capabilities improve. In particular, once a model realises it’s being trained or tested, it can start performing for the test, responding in ways that make it look safe rather than revealing what it would do in the wild, or masking capabilities (“sandbagging”). But, even so, the work we do before models become situationally aware – like interpretability tools that show what features the model is using, or studying how models generalise – is helpful.)  
  
\*\*Types of misalignment\*\*  
  
“We ultimately predict AIs that will not hate us, but that will have weird, strange, alien preferences that they pursue to the point of human extinction.”  
  
I think Y&S often equivocate between two different concepts under the idea of “misalignment”:  
  
1\. Imperfect alignment: The AI doesn’t always try to do what the developer/user intended it to try to do.

2\. Catastrophic misalignment: The AI tries hard to disempower all humanity, insofar as it has the opportunity.  
  
Current models are imperfectly aligned (e.g. as evidenced by alleged ChatGPT-assisted suicides). But I don’t think they’re catastrophically misaligned.  
  
I find that Y&S write and speak as if imperfect alignment entails catastrophic misalignment. But that’s just not true.  
  
To illustrate: Even suppose that all the first superintelligence terminally values is paperclips. But it’s risk-averse, in the sense that it prefers a guarantee of N resources over a 50/50 chance of 0 or 2N resources; let’s say it’s more risk-averse than the typical human being.  
  
This AI is imperfectly aligned. You could even say it's radically misaligned - it doesn’t care at all for the things that humans care about; it has weird, strange, alien preferences. But it needn’t be catastrophically misaligned: it would strongly prefer to cooperate with humans in exchange for, say, a guaranteed salary, rather than to take a risky gamble of either taking over the world or getting caught and shut off.  
  
The classic argument for expecting catastrophic misalignment is: (i) that the size of the “space” of aligned goals is small compared to the size of the “space” of misaligned goals (EY uses the language of a “narrow target” on the Hard Fork podcast, and a similar idea appears in the book.); (ii) gaining power and self-preservation is an instrumentally convergent goal, and almost all ultimate goals will result in gaining power and self-preservation as a subgoal.  
  
I don’t think that this is a good argument, because appeals to what “most” goals are like (if you can make sense of that) doesn’t tell you much about what goals are most likely. (Most directions I can fire a gun don’t hit the target; that doesn’t tell you much about how likely I am to hit the target if I’m aiming at it.) But let’s broadly accept this line of thinking for the sake of argument.  
  
Even so, it doesn’t make the risk-averse AI unlikely. The size of the space of risk-averse preferences is large compared to the size of linear-in-resources preferences, and is not small relative to the size of linear-or-superlinear-in-resources preferences. And the risk-averse AI still wants power and self-preservation, but that needn’t result in human extinction, because it prefers deals that give it a high chance of some amount of power to attempts at takeover that give it some lower chance of lots of power. We can have misalignment without catastrophic misalignment.  
  
(Maybe we won’t be able to make deals with AIs? I agree that’s a worry; but then the right response is to make sure that we can. Won’t the superintelligence have essentially a 100% chance of taking over, if it wanted to? But that’s again invoking the “discontinuous jump to godlike capabilities” idea, which I don’t think is what we’ll get).  
  
\*\*Their proposal\*\*  
  
"All over the Earth, it must become illegal for AI companies to charge ahead in developing artificial intelligence as they’ve been doing."  
  
The positive proposal is extremely unlikely to happen, could be actively harmful if implemented poorly (e.g. stopping the frontrunners gives more time for laggards to catch up, leading to more players in the race if AI development ends up resuming before alignment is solved), and distracts from the suite of concrete technical and governance agendas that we could be implementing.  
  
And, even if we’re keen on banning something, we could ban certain sorts of AI (e.g. AI trained on long horizon tasks, and/or AI with certain sorts of capabilities, and/or sufficiently agentic AI). The existence of close substitutes for agentic superintelligence could make the plan much more likely to work, just as the existence of HCFCs made banning CFCs much more viable.  
  
\*\*Other comments\*\*  
  
I was disappointed that so much of the book took the form of fiction or parables or analogies, which I find a distraction, and a poor substitute for arguments. (In my view, a much better discussion of how ASI might take over is Ryan Greenblatt’s on the 80,000 Hours podcast.)  
  
Things I liked: Y&S are very straightforward about what they believe, they state their bottom-line beliefs clearly, and they have courage in saying what they actually believe even when it doesn’t conform with orthodoxy. Even though I find the argument-from-analogy overdone, they have a great knack for telling them and the analogies to other areas of science (nuclear chain reactions, spacecraft launches, alchemy) were an enjoyable read. And EY in particular should get kudos for openly noting (especially on the podcasts I listened to) some of the ways in which the AI tech tree we’ve gotten is quite different from what he previously expected, even if I don't think that update has sufficiently propagated.  
  
\[1\] I say “strong superintelligence” because their definition - AI “exceeds every human at almost every mental task” is surprisingly low-bar, and a lower bar than what I’d call “superintelligence”. I prefer a definition where superintelligence is AI (or a team of AIs) that matches or exceeds every team of humans and AIs at almost every cognitive task. We got chess-superintelligence in the first sense in 1997, but chess-superintelligence in the second sense around 2013-2017.