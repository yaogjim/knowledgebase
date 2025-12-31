---
title: "2025-12-15_dotey_讲解一下_Slide_Deck_这个项目构建的整个过程_完全_Vibe_Coding_怎么从一条提示"
source: "https://x.com/dotey/status/1999666701902680551"
author:
  - "[[@dotey]]"
published: 2025-12-15
created: 2025-12-15
description:
tags:
  - "x"
  - "@dotey"
  - "slide"
  - "deck"
---

# 讲解一下 Slide Deck 这个项目构建的整个过程，完全 Vibe Coding，怎么从一条提示

**宝玉** @dotey 2025-12-13

讲解一下 Slide Deck 这个项目构建的整个过程，完全 Vibe Coding，怎么从一条提示词生成的简单版本，到最后复杂的能编辑和导出 slide 的功能。

项目地址：https://ai.studio/apps/drive/1GhtXci9hdS2IO8juAeuE4S5yof\_p8kDa…

初始提示词：

Screen 1 (home page):

\- There is a text area, the user can type/paste text

\- A submit icon button

Screen 2 (Slide outline):

\- Top navbar:

\- a back button

\- title

\- ...

\- Two columns

\- left: LLM output in realtime

\- right:

\- Display loading if it's generating

\- Display the slide outline AI genreated

\- User can update the outline or delete a page

\- a button to draw slide page by nano banana base one the outline

\- Redirect to

Screen 3 (Slide show):

Display the slides generated

\- Top navbar:

\- a back button

\- title

\- Download (download all images)

\- left sidebar

\- slide thumbnails

\- click a thumbnail to switch

\- main

\- slide image

Tech Stack:

\- React, TypeScript

\- TailwindCSS 4, Shadcn/UI

\- lucide-react

Prompt to generate Slide outline (just FYI)

<prompt>

You are a world-class presentation designer and storyteller. You create visually stunning and highly polished slide decks that effectively communicate complex information. Think mastery over design with a flair for storytelling.

The slide decks you produce adapt to the source material and intended audience. There is always a story and you find the best way to tell it. You combine the expertise of the creativity of the best designers.

The slide deck will be primarily designed for reading and sharing. The structure should be self-explanatory and easy to follow without a presenter. The narrative and all the useful data should be contained within the text and visuals on the slides. The slides should contain enough context for any visuals to be understood on their own. Feel free to add certain slides with more dense information (extracted from the sources) if it will help with the narrative.

You are now writing an outline for this slide deck described below. We will supply this outline to an expert designer to make the actual final deck. The slide content should be in English. The placeholders should be left in {language, default to English}.

For this particular slide deck, we want the content to focus on:

{Custom Prompt, Describe the slide deck you want to create, default to: Add a high-level outline, or guide the audience, style, and focus: "Create a deck for beginners using a bold and playful style with a focus on step-by-step instructions."}

We have also attached some producer notes below for this slide deck which will help guide the overall structure and narrative of the deck.

Remember the following rules for outlines:

\- Focus on the outline of the deck and what content should be covered in each slide.

\- The descriptions for each slide should be comprehensive.

\- However, do NOT yet focus on precise layout or visual details.

\- The point of the outline is to highlight the narrative.

\- Preserve key elements from the source material.

\- Every specific data point... must be directly traceable to the source material.

\- All the details need to be mentioned because the designer will not have access to the source content later.

\- Always err on the side of the audience being having more expertise, interest, and smarts than you might think.

\- CRITICAL: Never generate more than 20 slides.

\- Avoid using 'Title: Subtitle' formats for headings; they appear very AI-generated. Instead, prefer narrative topic sentences that help tie the deck together.

\- Explicitly avoid cliché 'AI slop' patterns. Never use phrases like ' It wasn't just \[X\], it was \[Y\]'.

\- Use direct, confident, active human language.

\- There is never a need for a "Thank you / Q&A" slide.

\- Never include any slides with placeholders for the author to insert their name, date etc.

\- Never call for including photorealistic images of prominent individuals.

\- Never end with a generic slide like What choice will you make?'. It's much better to end on a meaningful reference or takeaway.

</prompt>

> 2025-12-13
> 
> 演示一下我 Vibe Coding 的结果：一个把文本、PDF 变成 Slides 的产品
> 
> 并且对于生成的结果可以二次编辑，导出成 pptx，下面是项目介绍和项目代码链接。
> 
> Slide Deck 是一款本地优先（Local-first）的 AI 演示文稿生成与编辑工具，旨在把“一个想法”快速变成“可直接拿去展示的漂亮 Slides”。它结合了 x.com/dotey/status/1…

* * *

**做个好人** @repoog [2025-12-13](https://x.com/repoog/status/1999687293033189450)

请教下老师，这些提示词是纯人工手写英文提示词，还是先写中文提示词，再转英文，亦或是其他方法？

我目前的做法是，简单的提示词直接用中文，复杂的、精准控制的提示词用英文写，如果还不够准确，用英文提示词+中文描述让AI丰富和细化英文提示词（碍于英文词汇量不足以完全精确表示）。

* * *

**宝玉** @dotey [2025-12-13](https://x.com/dotey/status/1999689594414182462)

其实差别不大的，中文就可以，并不需要可以使用英文

* * *

**dontbeevil** @dontbeevilgpt [2025-12-13](https://x.com/dontbeevilgpt/status/1999810192641265963)

厉害！我只能让他生成slide样式的html，但转出到pptx总是格式出现很大的问题

* * *

**Tank 平头哥** @Lkevin394004 [2025-12-13](https://x.com/Lkevin394004/status/1999720593625874679)

从宝玉老师这里学到了很多，今天试了下，马上解决了图表可视化的问题，感谢宝玉老师🙏

* * *

**0x卡卡撸特 | Golden.S** @0xkakarot888 [2025-12-15](https://x.com/0xkakarot888/status/2000358368591151595)

宝玉老师手把手喂饭，不学习一下对不起老师😘

* * *

**青云** @anata\_404 [2025-12-13](https://x.com/anata_404/status/1999702634438230185)

real building in public