---
title: "如何善用 Cursor 及其 12 条准则"
source: "https://x.com/hellokaton/status/1914487184423526633"
author:
  - "[[@hellokaton]]"
created: 2025-04-24
description:
tags:
  - "@hellokaton #AI开发 #Cursor #代码生成 #效率 #编程 #软件开发"
---
**katon** @hellokaton 2025-04-21

用好 Cursor = 高效、整洁的代码。

用不好 = AI 给你堆出一团乱麻的代码，够你收拾一礼拜。  
  
下面是正确使用的 12 条准则：  
  
1\. 预先定好 5-10 条明确的项目规范，让 Cursor 知道你的项目结构和约束。对于老代码库，可以试试 /generate rules。  
  
2\. 提示词要具体。像写一份简要的技术说明那样，把技术栈、功能要求和约束都讲清楚。  
  
3\. 逐个文件来做；每次处理一小部分，集中精力生成、测试和检查。  
  
4\. 先写测试，确定测试用例，然后让 AI 生成代码，直到所有测试都通过。  
  
5\. 务必检查 AI 的输出，发现问题要彻底改对，然后告诉 Cursor 这些改动，让它学习。  
  
6\. 用 @ file, @ folders, @ git 把 Cursor 的注意力范围限定在你关心的代码部分。  
  
7\. 把设计文档和任务清单放在 .cursor/ 目录里，这样 Cursor 就能充分了解接下来该做什么。  
  
8\. 如果 AI 生成的代码不对，别光解释，直接自己改。Cursor 从你的修改中学得比解释快。  
  
9\. 利用聊天历史，可以在旧提示词基础上迭代优化，不用每次都从头开始。  
  
10\. 有目的地选择不同的模型。Gemini 适合需要精确的场景，Claude 适合需要广泛理解的场景。  
  
11\. 遇到新的或不熟悉的技术栈，把文档链接粘贴进去。让 Cursor 逐行解释遇到的错误以及如何修复。  
  
12\. 大项目让它先花时间索引，可以放在晚上进行；同时限制上下文范围，保持操作流畅。  
  
掌控好结构和流程是关键 (至少目前是这样)。  
  
把 Cursor 看作一个能力很强的初级工程师——只要你指引得当，它就能快速成长、表现出色。

> 2025-04-21
> 
> Using Cursor well = fast, clean code.
> 
> Using it wrong = AI spaghetti you’ll be cleaning up all week.
> 
> Here’s how to actually use it right:
> 
> 1\. Set 5-10 clear project rules upfront so Cursor knows your structure and constraints. Try /generate rules for existing codebases.
> 
> 2\. Be  
> 善用游标 = 快速、简洁的代码。
> 
> 使用不当 = 你整个星期都要清理的人工智能乱麻。
> 
> 以下是正确使用它的方法：
> 
> 1\. 预先设置 5 到 10 条明确的项目规则，以便 Cursor 了解您的结构和约束条件。尝试为现有代码库生成规则。
> 
> 2\. 存在

---

**ColinSun** @seecolinsun [2025-04-22](https://x.com/seecolinsun/status/1914506139414466839)

我觉得第3条很重要，分解并逐个击破，否则到头来整个工程都乱七八糟，每次改动都很少崩溃

---

**katon** @hellokaton [2025-04-22](https://x.com/hellokaton/status/1914506420806189290)

是的，就像和人沟通一次说一个概念更容易准确的理解。

---

**EC Elliot** @elliotchen100 [2025-04-22](https://x.com/elliotchen100/status/1914497997616062472)

Ryo 中文很好 不过 他会依然感激你翻译