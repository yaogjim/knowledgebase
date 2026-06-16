---
title: "2026-06-16_jasonfried_37signals_内部沟通指南"
source: "https://x.com/jasonfried/status/2061887191517937844"
author:
  - "[[@jasonfried]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@jasonfried"
  - "work"
  - "if"
---

# 37signals 内部沟通指南

**Jason Fried**

# 37signals 内部沟通指南

我们沟通的方式、地点、原因和时机。长文本异步沟通？实时聊天？面对面？视频？口头？书面？通过电子邮件？在 Basecamp 中？我们如何让每个人都了解情况，同时又不让每个人都卷入别人的事务中？所有这些都在这里。

—

## 经验法则和一般理念

以下是我们在 37signals 与团队成员、部门内部、全公司以及公众沟通时，尽量铭记于心的一系列基本原则。这些原则并非硬性要求，但它们有助于建立界限和共同遵循的做法，以便在我们进行那件影响所有其他工作的事情（即沟通）时有所遵循。

1.  你不可能不进行沟通。不讨论房间里的大象也是一种沟通。很少有事情像清晰的沟通那样值得去学习、练习和完善。
2.  有时实时，大多数时候异步。
3.  基于长文写作的内部沟通，而非以会议、交谈和闲聊等口头交流为传统的方式，带来了令人欢迎的会议、视频会议、通话或其他会打断与被打断的实时交流机会的减少。
4.  给有意义的讨论一段有意义的时间来发展和展开。急于下判断或要求立即回应，只会增加做出错误决策的可能性。
5.  会议是最后的手段，而不是首要选择。
6.  写作能巩固，聊天会消散。重大决策始于并终于完整想法的交流，而非逐行的交锋。如果事情重要、关键或根本，就把它写下来，不要用聊天淡化它。
7.  Speaking only helps who’s in the room, writing helps everyone. This includes people who couldn’t make it, or future employees who join years from now.
8.  If your words can be perceived in different ways, they’ll be understood in the way which does the most harm.
9.  Never expect or require someone to get back to you immediately unless it’s a true emergency. The expectation of immediate response is toxic.
10.  If you have to repeat yourself, you weren’t clear enough the first time. However, if you’re talking about something brand new, you may have to repeat yourself for years before you’re heard. Pick your repeats wisely.
11.  Poor communication creates more work.
12.  Companies don’t have communication problems, they have miscommunication problems. The smaller the company, group, or team, the fewer opportunities for miscommunication.
13.  Five people in a room for an hour isn’t a one hour meeting, it’s a five hour meeting. Be mindful of the tradeoffs.
14.  Be proactive about “wait, what?” questions by providing factual context and spatial context. Factual are the things people also need to know. Spatial is where the communication happens (for example, if it’s about a specific to-do, discuss it right under the to-do, not somewhere else).
15.  Communication shouldn’t require schedule synchronization. Calendars have nothing to do with communication. Writing, rather than speaking or meeting, is independent of schedule and far more direct.
16.  “Now” is often the wrong time to say what just popped into your head. It’s better to let it filter it through the sieve of time. What’s left is the part worth saying.
17.  Ask yourself if others will feel compelled to rush their response if you rush your approach.
18.  The end of the day has a way of convincing you what you’ve done is good, but the next morning has a way of telling you the truth. If you aren’t sure, sleep on it before saying it.
19.  If you want an answer, you have to ask a question. People typically have a lot to say, but they’ll volunteer little. Automatic questions on a regular schedule help people practice sharing, writing, and communicating.
20.  Occasionally pick random words, sentences, or paragraphs and hit delete. Did it matter?
21.  Urgency is overrated, ASAP is poison.
22.  If something’s going to be difficult to hear or share, invite questions at the end. Ending without the invitation will lead to public silence but private conjecture. This is where rumors breed.
23.  Where you put something, and what you call it, matters. When titling something, lead with the most important information. Keep in mind that many technical systems truncate long text or titles.
24.  Write at the right time. Sharing something at 5pm may keep someone at work longer. You may have some spare time on a Sunday afternoon to write something, but putting it out there on Sunday may pull people back into work on the weekends. Early Monday morning communication may be buried by other things. There may not be a perfect time, but there’s certainly a wrong time. Keep that in mind when you hit send.
25.  Great news delivered on the heels of bad news makes both bits worse. The bad news feels like it’s being buried, the good news feels like it’s being injected to change the mood. Be honest with each by giving them adequate space.
26.  Time is on your side, rushing makes conversations worse.
27.  Communication is lossy, especially verbal communication. Every hearsay hop adds static and chips at fidelity. Whenever possible, communicate directly with those you’re addressing rather than passing the message through intermediaries.
28.  Ask if things are clear. Ask what you left out. Ask if there was anything someone was expecting that you didn’t cover. Address the gaps before they widen with time.
29.  Consider where you put things. The right communication in the wrong place might as well not exist at all. When someone relies on search to find something it’s often because it wasn’t where they expected something to be.
30.  Communication often interrupts, so good communication is often about saying the right thing at the right time in the right way with the fewest side effects.

## Communicating day-to-day

This section includes specific examples of how we apply our philosophy day-to-day across the company. Since communication often interrupts, valuing each other’s time and attention is a critical consideration. Keeping people in the loop is important, but asking them to follow along with everything is a distraction. That’s why we follow reliable, predictable methods to share the right kind of information at the right time in the right place.

Basic toolset

我们 99%的内部沟通都发生在

[Basecamp](https://basecamp.com)。这意味着所有全公司范围的讨论、社交闲聊、与项目相关的工作、想法分享、内部辩论、自动签到、状态更新、政策更新以及所有正式的决定和公告都发生在 Basecamp 中。一个单一的集中式工具将所有内容整合在一起，并为公司所有员工创建一个单一的事实来源。我们内部不使用电子邮件（但外部使用），不使用 Slack 或 Teams 等独立聊天工具，而且很少举行面对面会议。我们确实使用 Zoom 进行偶尔的两人或三人视频会议。我们偶尔会在 GitHub 上讨论拉取请求。

Automatic daily: “What did you work on today?”

Every workday at 4:30pm, Basecamp (the product) automatically asks every employee “What did you work on today?” Whatever people write up is shared with everyone in the company. Everyone’s responses are displayed on a single page, grouped by date, so anyone who’s curious about what’s happening across the company can simply read from top to bottom. And if you have a question about anything, you can comment on anyone’s “what did you work on today?” check-in to keep the conversation in context.

This routine is about loose accountability and strong reflection. Writing up what you did every day is a great way to think back about what you accomplished and how you spent your time.

Some people just jot down a few bullets. Others write multi-paragraph stories to share — and document — the thinking behind their work. There are no requirements here. We just ask everyone to write in their own style.

Automatic weekly: “What will you be working on this week?”

Every Monday morning, Basecamp automatically asks everyone “What will you be working on this week?” This is a chance for everyone to lay out the big picture of their week. It’s not about regurgitating individual tasks, or diving headlong into the minutia of the week. It’s generally just your 10,000 foot view of the week ahead. The big picture items, the general themes. It sets your mind up for the work ahead, and, collectively, it gives everyone a good sense of what’s happening across the company this week.

Automatic occasionally: “Social questions”

Every few weeks, or once a month, Basecamp will automatically ask everyone a social-style question. “What books are you reading?” Or “Try anything new lately?” Or “Anything inspire you lately?” Or “Seen any great design recently?” Or “What did you do this weekend?” These entirely optional questions are meant to shake loose some stuff that you’d love to share with everyone else, but you hadn’t had an opportunity to do so. This kind of internal communication helps grease the social gears. This is especially useful for remote teams, like ours. When we know each other a little better, we work a little better together.

← Reflect every 6 weeks: Heartbeats

Heartbeats summarize the last ~6-weeks of work for a given team, department, or individual (if that person is a department of one). They’re written by the lead of the group, and they’re meant for everyone in the company to read. They summarize the big picture accomplishments, they detail the little things that mattered, and they generally highlight the importance of the work. They’ll also shine a light on challenges and difficulties along the way. They’re a good reminder that it’s not all sunshine all the time. On balance, Heartbeats are wonderful to write, fun to read, and they help everyone — including those not directly involved with the work — reflect on jobs well done and progress well made.

→ Project every 6 weeks: Kickoffs

Kickoffs are essentially the opposites of Heartbeats. Rather than reflect, they project. They’re all about what the team plans on taking on over the next 6 weeks. Projects, initiatives, revamps, whatever it might be, if it’s on the slate, it gets summarized in the Kickoff. While Kickoffs detail specific work for a specific group, they’re also meant for full-company consumption. Like Heartbeats, they’re written by the team lead. Kickoffs are broad in scope, so they don’t cover all the details in the work ahead — the teams doing the work are the ones that wade into those weeds. We don’t want to overwhelm everyone with details that don’t matter. If anyone’s curious about something included in a Kickoff, they’re free to post a comment and ask a question.

Whenever relevant: Announcements

Occasionally we update an internal policy. Something about vacation time, or a new benefit, or reiterating that 40 hour weeks means 40 hour weeks. When we have something to announce company-wide, we don’t send an email. Email is decentralized and there’s no permanent record in a permanent place everyone can see. Instead, we post it either to the 37signals HQ message board or as a comment on an existing policy document stored in Basecamp. This means everyone sees the same thing, everyone hears the same thing, and everyone knows the same thing — including future employees who are yet to join. We now have a shared truth.

Day-to-day project work: In context

Effective communication requires context. Saying the right thing in the wrong place, or without proper detail, leads to double work and messages being missed. That’s why we spin up a separate Basecamp project for every project we work on. Everything related to that project is communicated inside that project. All the tasks, all the discussions, all the documents, all the debates, and all the decisions happen inside those walls. Everyone who needs access, has access. Every Basecamp project is a capsule of everything someone needs to know about that work project.

Further, we take spatial context seriously. If we’re discussing a specific task, we discuss it in the comment section below the task itself. If we’re talking about a specific document, we discuss it in the comments attached to the document. Communications stay attached to the thing we’re discussing. This provides the full story in one reliable place. The alternative is terrible — communication detached from the original source material, discussions all over the place, fragmented conversations missing entire chunks of time and detail, etc. Basecamp’s “everything is commentable” feature is what makes this possible for us.