---
title: "2026-06-16_techtrenches_dev_The_West_Forgot_How_to_Build_Now_It_s_Forgetting_C"
source: "https://techtrenches.dev/p/the-west-forgot-how-to-make-things"
author:
  - "[[@techtrenches.dev]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "techtrenches"
  - "@techtrenches.dev"
  - "years"
  - "production"
---

# The West Forgot How to Build. Now It's Forgetting Code

[

![](https://substackcdn.com/image/fetch/$s_!8_UF!)

](https://substackcdn.com/image/fetch/$s_!8_UF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff32f29d9-18d6-448b-9b03-54c5711e5871_1600x1000.png)

In 2023, Raytheon’s president stood at the Paris Air Show and described what it took to [restart Stinger](https://www.defenseone.com/business/2023/06/raytheon-calls-retirees-help-restart-stinger-missile-production/388067/) missile production. They brought back engineers in their 70s to teach younger workers how to build a missile from paper schematics drawn during the Carter administration. Test equipment had been sitting in warehouses for years. The nose cone still had to be attached by hand, exactly as it was forty years ago.

The Pentagon hadn’t bought a new Stinger in twenty years. Then Russia invaded Ukraine, and suddenly everyone needed them. The production line was shut down. The electronics were obsolete. The seeker component was out of production. An order placed in May 2022 wouldn’t deliver until 2026. Four years. Not because of money. Because the people who knew how to build them retired a decade earlier and nobody replaced them.

I run engineering teams in Ukraine. My people lived the other side of this equation. Not the factory floor. The receiving end. While Raytheon was struggling to restart production from forty-year-old blueprints, the US was shipping thousands of Stingers to Ukraine. RTX CEO Greg Hayes: ten months of war burned through thirteen years’ worth of Stinger production. I’ve seen this pattern before. It’s happening in my industry right now.

## A Million Shells Nobody Could Make

In March 2023, the EU promised Ukraine one million artillery shells within twelve months. European production capacity sat at 230,000 shells per year. Ukraine was consuming 5,000 to 7,000 rounds per day. Anyone with a calculator could see this wouldn’t work.

By the deadline, Europe delivered about half. Macron called the original promise reckless. An [investigation](https://www.ftm.eu/articles/who-pays-for-ukraine-s-155mm-grenade) by eleven media outlets across nine countries found actual production capacity was roughly one-third of official EU claims. The million-shell mark wasn’t hit until December 2024, nine months late.

It wasn’t one bottleneck. It was all of them. France had halted domestic propellant production in 2007. Seventeen years of nothing. Europe’s single major TNT producer was in Poland. Germany had two days of ammunition stored. A Nammo plant in Denmark was shut down in 2020 and had to be restarted from scratch. The entire continent’s defense industry had been optimized for making small batches of expensive custom products. Nobody planned for volume. Nobody planned for crisis.

The U.S. wasn’t much better. One plant in Scranton, one facility in Iowa for explosive fill, no domestic TNT production since 1986. Billions of investment later, production still hadn’t hit half the target.

## Consolidate or Die

This wasn’t an accident. In 1993, the Pentagon told defense CEOs to consolidate or die. Fifty-one major defense contractors collapsed into five. Tactical missile suppliers went from thirteen to three. Shipbuilders from eight to two. The workforce fell from 3.2 million to 1.1 million. A 65% cut.

The ammunition supply chain had single points of failure everywhere. One manufacturer for 155mm shell casings, sitting in Coachella, California, on the San Andreas Fault. One facility in Canada for propellant charges. Optimized for minimum cost with zero margin for surge. On paper, efficient. In practice, one bad day away from collapse.

## When Knowledge Dies, It Stays Dead

Then there’s Fogbank. A classified material used in nuclear warheads. Produced from 1975 to 1989, then the facility was shut down. When the government needed to reproduce it for a warhead life extension program in 2000, they discovered they couldn’t. A [GAO report](https://en.wikipedia.org/wiki/Fogbank) found that almost all staff with production expertise had retired, died, or left the agency. Few records existed.

After spending an additional $69 million and years of reverse engineering, they finally produced viable Fogbank. Then discovered the new batch was too pure. The original had contained an unintentional impurity that was critical to its function. That fact existed nowhere in any document. Only the workers who made the original batch knew it, and they had retired years earlier.

A nuclear weapons program lost the ability to make a material it invented. The knowledge existed only in people, and the people were gone.

## The Same Playbook

I read the Fogbank story and recognized it immediately. Not the nuclear material. The pattern. Build capability over decades. Find a cheaper substitute. Let the human pipeline atrophy. Enjoy the savings. Then watch it all collapse when a crisis demands what you optimized away.

In defense, the substitute was the peace dividend. In software, it’s AI.

I wrote about the [talent pipeline collapse](https://techtrenches.substack.com/p/ai-wont-save-us-from-the-talent-crisis) before. The hiring numbers and the junior-to-senior problem are documented. So is the [comprehension crisis](https://techtrenches.dev/p/the-comprehension-extinction-ai-isnt). What I didn’t have was the right historical parallel. Now I do.

And it tells you something the hiring data doesn’t: how long rebuilding actually takes.

## Rebuilding Takes Years. Always.

Every major defense production ramp-up took three to five years for simple systems. Five to ten for complex ones. Stinger: thirty months minimum from order to delivery. Javelin: four and a half years to less than double production. 155mm shells: four years and still not at target despite five billion dollars invested. France only restarted propellant production in 2024, seventeen years after shutting it down.

Money was never the constraint. Knowledge was. [RAND found](https://www.rand.org/content/dam/rand/pubs/monographs/2007/RAND_MG608.1.pdf) that 10% of technical skills for submarine design need ten years of on-the-job experience to develop, sometimes following a PhD. Apprenticeships in defense trades take two to four years, with five to eight years to reach supervisory competence.

Now map that onto software. A junior developer needs three to five years to become a competent mid-level engineer. Five to eight years to become senior. Ten or more to become a principal or architect. That timeline can’t be compressed by throwing money at it. It can’t be compressed by AI either.

A [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) randomized controlled trial found that experienced developers using AI coding tools actually took 19% longer on real-world open source tasks. Before starting, they predicted AI would make them 24% faster. The gap between prediction and reality was 43 percentage points. When researchers tried to run a follow-up, a significant share of developers refused to participate if it meant working without AI. They couldn’t imagine going back.

## The Bill Always Comes Due

The software industry is in year three of the same optimization. [Salesforce said](https://sfstandard.com/2025/02/27/salesforce-marcbenioff-layoffs-tech-agents/) it won’t hire more software engineers in 2025. A LeadDev survey found 54% of engineering leaders believe AI copilots will reduce junior hiring long-term. A [CRA survey](https://cra.org/crn/2025/10/cerp-pulse-survey-a-snapshot-of-2025-undergraduate-computing-enrollment-patterns/) of university computing departments found 62% reported declining enrollment this year.

I see it in code review. Review is now the bottleneck. AI generates code fast. Humans review it slow. The industry’s answer is predictable: let AI review AI’s code. I’m not doing that. I’ve reworked our pull request templates instead. Every PR now has to explain what changed, why, what type of change it is, screenshots of before and after. Structured context so the reviewer isn’t guessing. I’m adding dedicated reviewers per project. More eyes, more chances to catch what the model missed.

But even that doesn’t solve the deeper problem. The skills you need to be effective now are different. Technical expertise alone isn’t enough anymore. You need people who can take ownership, communicate tradeoffs, push back on bad suggestions from a machine that sounds very confident. Leadership qualities. Our last hiring round tells you how rare that is: 2,253 candidates, 2,069 disqualified, 4 hired. A 0.18% conversion rate. The combination of technical skill and the judgment to know when the AI is wrong barely exists in the market anymore.

We document everything. Site Books, SDDs, RVS reports, boilerplate modules with full coverage. It works today, because the people reading those docs have the engineering expertise to act on them. What happens when they don’t? Honestly, I don’t know. Maybe AI in five years is good enough that it won’t matter. Maybe the problem stays manageable. I can’t predict the capabilities of models in 2031.

But crises don’t send calendar invites. Nobody expected a full-scale land war in Europe in 2022. The defense industry had thirty years to prepare and didn’t. Even Fogbank had records. They weren’t enough without the people who understood what they meant.

Five to ten years from now, we’ll need senior engineers. People who understand systems end to end, who can debug distributed failures at 2 AM, who carry institutional knowledge that exists nowhere in the codebase. Those engineers don’t exist yet because we’re not creating them. The juniors who should be learning right now are either not being hired or developing what a DoD-funded workforce study calls “AI-mediated competence.” They can prompt an AI. They can’t tell you what the AI got wrong.

It’s Fogbank for code. When juniors skip debugging and skip the formative mistakes, they don’t build the tacit expertise. And when my generation of engineers retires, that knowledge doesn’t transfer to the AI.

It just disappears.

The West already made this mistake once. The bill came due in Ukraine.

I know how this sounds. I know I’ve written about the talent pipeline before. The defense example isn’t about repeating the argument. It’s about showing what happens if the industry’s expectations don’t work out. Stinger, Javelin, Fogbank, a million shells nobody could make. That’s the cost of betting wrong on optimization. We’re making the same bet with software engineering right now.

Maybe AI gets good enough, and the bet pays off. Maybe it doesn’t. The defense industry thought peace would last forever, too.