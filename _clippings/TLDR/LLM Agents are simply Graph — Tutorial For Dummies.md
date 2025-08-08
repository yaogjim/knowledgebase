---
title: "LLM Agents are simply Graph — Tutorial For Dummies"
source: "https://zacharyhuang.substack.com/p/llm-agent-internal-as-a-graph-tutorial"
author:
  - "[[Zachary Huang]]"
published: 2025-03-24
created: 2025-03-26
description: "Ever wondered how AI agents actually work behind the scenes?"
tags:
  - "clippings"
---
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F382ea8f1-0610-4cce-b4ef-350a9df68ee0_1050x588.png)

> *有没有想过人工智能代理在幕后是如何工作的？本指南将以最简单易懂的方式详细介绍代理系统是如何构建成简单图表的！*
> 
> *注意：这是官方 PocketFlow Agent 文档的一个超级友好的、循序渐进的版本。我们用示例和简化的解释扩展了所有概念，使其更易于理解。*

你是否到处都听说过“LLM 智能体”，但却被所有的技术术语搞得一头雾水？你不是一个人！虽然各大公司都在竞相打造像 GitHub Copilot、PerplexityAI 和 AutoGPT 这样日益复杂的人工智能智能体，但大多数解释都让它们听起来像高深莫测的科学。

好消息：它们不是。在本对初学者友好的指南中，你将学到：

- 所有人工智能代理背后惊人的简单概念
- 智能体实际上是如何做出决策的（用通俗易懂的英语！）
- 如何只用几行代码构建自己的简单代理
- 为什么大多数框架会把实际发生的事情复杂化

在本教程中，我们将使用 PocketFlow——一个仅有 100 行的微型框架，它去除了所有复杂性，向你展示智能体在幕后是如何真正工作的。与其他隐藏重要细节的框架不同，PocketFlow 让你能够一次性看到整个系统。

## 为什么使用 PocketFlow 学习智能体？

大多数智能体框架将实际发生的事情隐藏在复杂的抽象背后，这些抽象看起来令人印象深刻，但却让初学者感到困惑。PocketFlow 采用了不同的方法——它只有 100 行代码，能让你确切地看到智能体是如何工作的！

给初学者的好处：

- 清晰透明：没有神秘的黑箱或复杂的抽象概念
- 查看所有内容：整个框架可容纳在一个可读文件中
- 学习基础知识：非常适合理解智能体的实际运作方式
- 无负担：无大量依赖或供应商锁定

PocketFlow 为您提供基础知识，让您能够从头开始构建自己的理解，而不是试图去理解一个包含数千个文件的庞大框架。

## 简单的构建模块

想象一下我们的智能体系统就像一个厨房：

- 节点就像不同的烹饪工位（切菜工位、烹饪工位、摆盘工位）
- 流程就像是告诉你接下来要去哪个工位的指南
- 共享存储就像一个大台面，每个人都可以看到并使用上面的食材

在我们的厨房（智能体系统）：

1. 每个站点（节点）有三项简单的工作：
	- 准备：从台面上拿取你需要的东西（比如拿取食材）
	- 执行：做你的特殊工作（比如烹饪食材）
	- 发布：把你的成果放回台面上，告诉大家接下来要做什么（比如上菜以及决定接下来做什么菜）
2. The recipe (Flow) just tells you which station to visit based on decisions:  
	该配方（流程）只是根据决策告诉你要访问哪个工位：
	- "If the vegetables are chopped, go to the cooking station"  
		如果蔬菜切好了，就去烹饪区
	- "If the meal is cooked, go to the plating station"  
		如果饭菜做好了，就去摆盘区

Let's see how this works with our research helper!  
让我们看看这在我们的研究助手身上是如何运作的！

## What's an LLM Agent (In Human Terms)?什么是LLM 代理（用通俗易懂的话来说）？

An LLM (Large Language Model) agent is basically a smart assistant (like ChatGPT but with the ability to take actions) that can:  
一个LLM（大语言模型）智能体本质上是一个智能助手（类似于 ChatGPT，但具备采取行动的能力），它可以：

1. Think about what to do next  
	想想接下来要做什么
2. Choose from a menu of actions  
	从操作菜单中选择
3. Actually do something in the real world  
	在现实世界中真正做点事情
4. See what happened 看看发生了什么
5. Think again...再想想……

Think of it like having a personal assistant managing your tasks:  
把它想象成有一个私人助理来管理你的任务：

1. They review your inbox and calendar to understand the situation  
	他们查看你的收件箱和日程安排以了解情况
2. They decide what needs attention first (reply to urgent email? schedule a meeting?)  
	他们决定首先需要关注什么（回复紧急邮件？安排会议？）
3. They take action (draft a response, book a conference room)  
	他们采取行动（起草回复、预订会议室）
4. They observe the result (did someone reply? was the room available?)  
	他们观察结果（有人回复了吗？房间有空吗？）
5. They plan the next task based on what happened  
	他们根据已发生的事情来规划下一项任务

## The Big Secret: Agents Are Just Simple Graphs!重大秘密：智能体只是简单的图！

Here's the mind-blowing truth about agents that frameworks overcomplicate:  
以下是关于代理的令人震惊的真相，即框架将其过度复杂化了：

![Agents Are Just Simple Graphs](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6155038-4ec0-4f88-b44a-2fd596de3a32_800x379.jpeg)

就是这样！每个智能体都只是一个具有以下内容的图：

1. 一个分支到不同操作的决策节点
2. 执行特定任务的操作节点
3. 一个结束流程的终结节点
4. 将所有内容连接在一起的边缘
5. 将执行带回决策节点的循环

无需复杂的数学，无需神秘的算法——只有节点和箭头！其他一切都只是细节。如果你深入挖掘，就会在过于复杂的框架中发现这些隐藏的图：

- OpenAI 智能体：有关图中工作流程，请查看 run.py#L119 。
- Pydantic 代理：\_agent\_graph.py#L779 以图形方式组织步骤。
- Langchain: agent\_iterator.py#L174 展示了循环结构。
- LangGraph：基于图的方法请参考 agent.py 文件的第 56 行。

让我们通过一个简单的例子来看看这个图表实际上是如何工作的。

## 让我们构建一个超级简单的研究代理

想象一下，我们想要构建一个能够搜索网页并回答问题的人工智能助手——类似于 Perplexity AI 这样的工具，但要简单得多。我们希望我们的智能体能够：

1. 从用户读取一个问题
2. 决定是否需要搜索信息
3. 如有需要，可在网上查找相关内容
4. 有足够信息后再给出答案

让我们将我们的智能体分解为各个“工作站”，每个工作站处理一项特定任务。可以将这些工作站想象成装配线上的工人——每个都有自己特定的任务。

这是我们研究代理的简单示意图：

![Diagram of our research agent](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84ba6ab0-1c4f-449e-acd2-b2b3f55ddfe2_800x423.jpeg)

在此图表中：

1. “决定行动”是我们的“思维站”，智能体在这里决定下一步做什么
2. SearchWeb 是我们的“研究站”，智能体在那里查找信息
3. AnswerQuestion 是我们的“回答站”，客服人员在此生成最终答案

## 在我们编码之前：让我们来看一个示例

想象一下，你问我们的智能体：“谁赢得了 2023 年超级碗？”

以下是一步步将会发生的情况：

1. 决定行动站：
	- 查看内容：你的问题以及我们目前所了解的情况（目前尚无任何信息）
	- 想：“我不知道谁赢得了 2023 年超级碗，我需要搜索一下”
	- 决定：搜索“2023 年超级碗冠军”
	- 传递至：搜索网站
2. 搜索网站：
	- 查看：搜索查询“2023 年超级碗冠军”
	- 功能：在互联网上进行搜索（假设它找到“堪萨斯城酋长队获胜”）
	- 保存：我们共享台面上的搜索结果
	- 传递至：返回“决定行动”工作站
3. 决定行动站（第二次）：
	- 查看内容：您的问题以及我们目前所了解的信息（搜索结果）
	- 心想：“太棒了，现在我知道酋长队赢得了 2023 年超级碗”
	- 决定：我们有足够的信息来回答
	- 传递至：回答问题站
4. 回答问题站：
	- 查看内容：您的问题以及我们所有的研究
	- 功能：使用所有信息创建一个友好的答案
	- 保存：最终答案
	- 完成：任务已完成！

这正是我们的代码要做的——只是用编程语言表达出来。

让我们一个一个地建造这些站点，然后将它们连接在一起！

### 步骤 1：构建我们的第一个节点：DecideAction 🤔

“DecideAction”节点就像是我们智能体的“大脑”。它的工作很简单：

1. 查看这个问题以及我们目前收集到的任何信息
2. 决定我们是否需要搜索更多信息，或者我们现在是否可以回答

让我们一步一步来构建它：

```markup
class DecideAction(Node):
    def prep(self, shared):
        # Think of "shared" as a big notebook that everyone can read and write in
        # It's where we store everything our agent knows

        # Look for any previous research we've done (if we haven't searched yet, just note that)
        context = shared.get("context", "No previous search")

        # Get the question we're trying to answer
        question = shared["question"]

        # Return both pieces of information for the next step
        return question, context
```

首先，我们创建了一个用于收集信息的 `prep` 方法。可以把 `prep` 想象成厨师在烹饪前收集食材的过程。它所做的只是查看我们已经知道的内容（我们的“上下文”）以及我们试图回答的问题。

现在，让我们构建“思考”部分：

```markup
def exec(self, inputs):
        # This is where the magic happens - the LLM "thinks" about what to do
        question, context = inputs

        # We ask the LLM to decide what to do next with this prompt:
        prompt = f"""
### CONTEXT
You are a research assistant that can search the web.
Question: {question}
Previous Research: {context}

### ACTION SPACE
[1] search
  Description: Look up more information on the web
  Parameters:
    - query (str): What to search for

[2] answer
  Description: Answer the question with current knowledge
  Parameters:
    - answer (str): Final answer to the question

## NEXT ACTION
Decide the next action based on the context and available actions.
Return your response in this format:

\`\`\`yaml
thinking: |
    <your step-by-step reasoning process>
action: search OR answer
reason: <why you chose this action>
search_query: <specific search query if action is search>
\`\`\`"""

        # Call the LLM to make a decision
        response = call_llm(prompt)

        # Pull out just the organized information part from the LLM's answer
        # (This is like finding just the recipe part of a cooking video)
        yaml_str = response.split("\`\`\`yaml")[1].split("\`\`\`")[0].strip()
        decision = yaml.safe_load(yaml_str)  # Convert the text into a format our program can use

        return decision
```

`exec` 方法是实际进行“思考”的地方。可以把它想象成厨师烹饪食材的过程。在这里，我们：

1. 创建一个向LLM解释当前情况的提示
2. 请LLM决定是进行搜索还是回答
3. 解析响应以获得明确的决策

最后，让我们保存该决策并告知流程接下来要做什么：

```markup
def post(self, shared, prep_res, exec_res):
        # If the LLM decided to search, save the search query
        if exec_res["action"] == "search":
            shared["search_query"] = exec_res["search_query"]

        # Return which action to take - this tells our flow where to go next!
        return exec_res["action"]  # Will be either "search" or "answer"
```

`post` 方法是我们保存结果并决定下一步操作的地方。可以把它想象成厨师上菜并决定接下来准备什么菜肴。如果需要，我们会保存搜索查询，然后返回 “搜索” 或 “答案”，以告诉我们的流程接下来访问哪个节点。

### 步骤 2：构建我们的第二个节点：SearchWeb 🔍

SearchWeb 节点是我们的“研究员”。它唯一的任务是：

1. 输入一个搜索查询
2. 查找它（在这个简单的示例中，我们将伪造结果）
3. 保存它找到的内容
4. 告诉智能体决定如何处理这条新信息

让我们构建它：

```markup
class SearchWeb(Node):
    def prep(self, shared):
        # Simply get the search query we saved earlier
        return shared["search_query"]
```

这里的 `prep` 方法只是获取由 DecideAction 节点保存的搜索查询。

```markup
def exec(self, search_query):
        # This is where we'd connect to Google to search the internet
        # Set up our connection to Google
        search_client = GoogleSearchAPI(api_key="GOOGLE_API_KEY")

        # Set search parameters
        search_params = {
            "query": search_query,
            "num_results": 3,
            "language": "en"
        }

        # Make the API request to Google
        results = search_client.search(search_params)

        # Format the results into readable text
        formatted_results = f"Results for: {search_query}\n"

        # Process each search result
        for result in results:
            # Extract the title and snippet from each result
            formatted_results += f"- {result.title}: {result.snippet}\n"

        return formatted_results
```

`exec` 方法连接到搜索 API，发送查询并格式化结果。在实际实现中，你需要注册一个搜索 API 服务，如 Google 自定义搜索 API，并获取你自己的 API 密钥。

```markup
def post(self, shared, prep_res, exec_res):
        # Store the search results in our shared whiteboard
        previous = shared.get("context", "")
        shared["context"] = previous + "\n\nSEARCH: " + shared["search_query"] + "\nRESULTS: " + exec_res

        # Always go back to the decision node after searching
        return "decide"
```

`post` 方法通过将搜索结果添加到共享上下文来保存它们。然后它返回 “decide” 以告知我们的流程返回 DecideAction 节点，以便它可以思考如何处理这些新信息。

### 步骤 3：构建我们的第三个节点：AnswerQuestion 💬

AnswerQuestion 节点是我们的“响应器”。它的工作很简单，就是：

1. 获取我们收集到的所有信息
2. 创建一个友好、有用的回答
3. 把那个答案留给用户

让我们构建它：

```markup
class AnswerQuestion(Node):
    def prep(self, shared):
        # Get both the original question and all the research we've done
        return shared["question"], shared.get("context", "")
```

`prep` 方法收集了原始问题以及我们收集到的所有研究内容。

```markup
def exec(self, inputs):
        question, context = inputs
        # Ask the LLM to create a helpful answer based on our research
        prompt = f"""
### CONTEXT
Based on the following information, answer the question.
Question: {question}
Research: {context}

## YOUR ANSWER:
Provide a comprehensive answer using the research results.
"""
        return call_llm(prompt)
```

`exec` 方法要求LLM根据我们的研究创建一个有用的答案。

```markup
def post(self, shared, prep_res, exec_res):
        # Save the answer in our shared whiteboard
        shared["answer"] = exec_res

        # We're done! No need to continue the flow.
        return "done"
```

`post` 方法保存最终答案并返回 “完成” 以表明我们的流程已完成。

### 步骤 4：将所有内容连接在一起！ 🔄

现在到了有趣的部分——我们需要将所有节点连接在一起，以创建一个可运行的智能体！

```markup
# First, create instances of each node
decide = DecideAction()
search = SearchWeb()
answer = AnswerQuestion()

# Now connect them together - this is where the magic happens!
# Each connection defines where to go based on the action returned by post()

# If DecideAction returns "search", go to SearchWeb
decide - "search" >> search

# If DecideAction returns "answer", go to AnswerQuestion
decide - "answer" >> answer

# After SearchWeb completes, go back to DecideAction
search - "decide" >> decide

# Create our flow, starting with the DecideAction node
flow = Flow(start=decide)
```

就是这样！我们已经将节点连接成一个完整的流程，该流程可以：

1. 首先决定要做什么
2. 如有需要，请搜索信息
3. 循环返回以确定我们是否需要更多信息
4. 准备好时再回答问题

把它想象成一个流程图，其中每个框都是一个节点，箭头表示根据沿途做出的决策下一步要去往何处。

### 让我们运行我们的代理！🚀

现在让我们看看我们的智能体是如何运行的：

```markup
# Create a shared whiteboard with just a question
shared = {"question": "What is the capital of France?"}

# Run our flow!
flow.run(shared)

# Print the final answer
print(shared["answer"])
```

以下是我们的智能体运行时会发生的情况：

#### 第一轮：初步决定 🤔

首先，我们的智能体思考这个问题：

```markup
thinking: |
  The question is asking about the capital of France. I don't have any prior search results to work with.
  To answer this question accurately, I should search for information about France's capital.
action: search
reason: I need to look up information about the capital of France
search_query: capital of France
```

我们的智能体判定它目前掌握的信息还不够，所以它需要搜索信息。

#### 第二轮：在网络上搜索🔍

SearchWeb 节点现在搜索“法国首都”并获得以下结果：

```markup
Results for: capital of France
- The capital of France is Paris
- Paris is known as the City of Light
```

它将这些结果保存到我们的共享上下文中。

#### 第三轮：最终决定🤔

我们的智能体再次查看这个问题，但现在它有了一些搜索结果：

```markup
thinking: |
  Now I have search results that clearly state "The capital of France is Paris".
  This directly answers the question, so I can provide a final answer.
action: answer
reason: I now have the information needed to answer the question
```

这次，我们的智能体判定它有足够的信息来回答！

#### 第四轮：回答问题💬

最后，“回答问题”节点生成一个有用的回复：

```markup
The capital of France is Paris, which is also known as the City of Light.
```

然后我们就完成了！我们的智能体已成功：

1. 意识到需要搜索信息
2. 执行了一次搜索
3. 决定它已经有足够的信息了
4. 生成了一个有用的答案

### 全过程可视化：

![The Whole Process Visualized](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34da5ff1-228a-4725-9037-95f9d6931e34_800x552.jpeg)

### 深入探索：探究代码及其他方面

如果你有一定的技术基础，并且想阅读或试验本教程的完整代码，你可以在这里找到它！

你还可以通过查看这些代码片段，了解这种相同的循环和分支模式在更大的框架中是如何出现的：

- OpenAI 智能体：有关图中工作流程，请查看 run.py#L119 。
- Pydantic 代理：\_agent\_graph.py#L779 以图形方式组织步骤。
- Langchain: agent\_iterator.py#L174 展示了循环结构。
- LangGraph：基于图的方法请参考 agent.py 文件的第 56 行。

## 结论：理解智能体的秘诀

现在你知道秘密了——LLM 特工只是带有分支的循环：

1. 思考当前状态
2. 通过从多个选项中选择一个操作进行分支
3. 执行所选操作
4. 从该操作中获取结果
5. 回头再思考

“思考”发生在提示（我们向LLM询问的内容）中，“分支”是指智能体在可用工具之间进行选择的时候，而“执行”则发生在我们调用外部函数时。其他一切都只是管道工作！

下次当你看到一个有成千上万行代码的复杂代理框架时，记住这个简单的模式，然后问问自己：“这个系统中的决策分支和循环在哪里？”

有了这些知识，无论任何智能体系统表面上看起来多么复杂，你都能够理解它。

*想了解更多关于构建简单智能体的信息吗？在 GitHub 上查看 PocketFlow！*