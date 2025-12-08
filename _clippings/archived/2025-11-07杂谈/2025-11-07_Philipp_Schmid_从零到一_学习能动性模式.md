---
title: "2025-11-07_Philipp_Schmid_从零到一_学习能动性模式"
source: "https://www.philschmid.de/agentic-pattern"
author:
  - "[[@Philipp Schmid]]"
published: 2025-11-07
created: 2025-11-07
description:
tags:
  - "#pattern"
  - "#workflow"
  - "philschmid"
  - "@Philipp Schmid"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# ## 从零到一：学习能动性模式

## 从零到一：学习能动性模式

May 5, 2025 16 minute read [View Code](https://github.com/philschmid/gemini-samples/blob/main/guides/agentic-pattern.ipynb)

AI 智能体。自主式人工智能。自主式架构。自主式工作流。自主式模式。智能体无处不在。但它们究竟 *是什么* ？我们又该如何构建稳健高效的自主式系统？虽然"智能体"一词被广泛使用，但其核心特征在于能够动态规划并执行任务，通常借助外部工具和记忆来实现复杂目标。

本文旨在探讨常见的设计模式。你可以将这些模式视为构建人工智能应用的蓝图或可复用模板。理解它们能为解决复杂问题、设计可扩展、模块化且适应性强的系统提供思维框架。

我们将深入探讨几种常见模式，区分更具结构性的 **工作流** 与更灵活的 **智能体模式** 。工作流通常遵循预设路径，而智能体在决策过程中拥有更高的自主权。

**为何（能动性）模式至关重要？**

- 模式为思考和设计系统提供了一种结构化的方法。
- 模式使我们能够构建并逐步提升人工智能应用的复杂度，以适应不断变化的需求。基于模式的模块化设计更易于修改和扩展。
- 模式通过提供经过验证的可重用模板，帮助管理协调多个智能体、工具和工作流程的复杂性。它们促进开发者之间的最佳实践和共同理解。

**何时（以及何时不）使用智能体？**

在深入探讨模式之前，关键是要思考 *何时* 才真正需要采用智能体方法。

- 始终优先寻求最简单的解决方案。如果你清楚解决问题的具体步骤，固定流程甚至一个简单的脚本可能比智能体更高效可靠。
- 代理系统通常以增加延迟和计算成本为代价，换取在复杂、模糊或动态任务上可能更优的性能。务必确保收益大于这些成本。
- 在处理步骤明确、定义清晰的任务时，使用 **工作流** 可确保结果的可预测性和一致性。
- 当需要灵活性、适应性和模型驱动的决策时，使用 **智能体** 。
- 保持简洁（一如既往）：即便构建智能体系统，也要追求最简洁有效的设计。过度复杂的智能体可能难以调试和管理。
- 自主性带来了固有的不可预测性和潜在错误。自主系统必须配备强大的错误记录、异常处理与重试机制，为系统（或其底层 LLM）提供自我修正的机会。

接下来，我们将探讨 3 种常见工作流模式和 4 种智能体模式。我们将通过纯 API 调用示例逐一说明，避免依赖 LangChain、LangGraph、LlamaIndex 或 CrewAI 等特定框架，以聚焦核心概念。

## Pattern Overview

我们将探讨以下模式：

- [Pattern Overview](#pattern-overview)
- [工作流：提示链](#workflow-prompt-chaining)
- [工作流：路由或交接](#workflow-routing-or-handoff)
- [工作流：并行化](#workflow-parallelization)
- [Reflection Pattern](#reflection-pattern)
- [Tool Use Pattern](#tool-use-pattern)
- [规划模式（编排器-工作者）](#planning-pattern-orchestrator-workers)
- [Multi-Agent Pattern](#multi-agent-pattern)

## 工作流：提示链

![](/static/blog/agentic-pattern/prompt-chaining.png)

一个 LLM 调用的输出会依次作为下一个 LLM 调用的输入。这种模式将任务分解为固定的步骤序列，每一步都由一个 LLM 调用处理前一步的输出结果。它适用于那些能够清晰拆分为可预测、顺序性子任务的工作场景。

Use Cases:

- 生成结构化文档：LLM 1 创建大纲，LLM 2 根据标准验证大纲，LLM 3 基于验证后的大纲撰写内容。
- 多步骤数据处理：提取信息、进行转换，然后进行总结。
- 根据精选输入生成新闻简报。

```python
import os

from google import genai

 

# Configure the client (ensure GEMINI_API_KEY is set in your environment)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

 

# --- Step 1: Summarize Text ---

original_text = "Large language models are powerful AI systems trained on vast amounts of text data. They can generate human-like text, translate languages, write different kinds of creative content, and answer your questions in an informative way."

prompt1 = f"Summarize the following text in one sentence: {original_text}"

 

# Use client.models.generate_content

response1 = client.models.generate_content(

 model='gemini-2.0-flash',

 contents=prompt1

)

summary = response1.text.strip()

print(f"Summary: {summary}")

 

# --- Step 2: Translate the Summary ---

prompt2 = f"Translate the following summary into French, only return the translation, no other text: {summary}"

 

# Use client.models.generate_content

response2 = client.models.generate_content(

 model='gemini-2.0-flash',

 contents=prompt2

)

translation = response2.text.strip()

print(f"Translation: {translation}")
```

## Workflow: Routing

![](/static/blog/agentic-pattern/routing-or-handoff.png)

初始的 LLM 充当路由器，对用户输入进行分类并将其引导至最合适的专门任务或 LLM。这种模式实现了关注点分离，允许单独优化各个下游任务（使用专门的提示、不同模型或特定工具）。它通过为简单任务使用较小模型来提高效率并可能降低成本。当任务被路由时，所选代理将“接管”完成责任。

Use Cases:

- 客户支持系统：将查询转接至专门处理账单、技术支持或产品信息的客服专员。
- 分层 LLM 使用策略：将简单查询路由至更快速、经济的模型（如 Llama 3.1 8B），而将复杂或非常规问题分配给性能更强的模型（如 Gemini 1.5 Pro）。
- 内容生成：将博客文章、社交媒体更新或广告文案的请求路由至不同的专业提示/模型。

```python
import os

import json

from google import genai

from pydantic import BaseModel

import enum

 

# Configure the client (ensure GEMINI_API_KEY is set in your environment)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

 

# Define Routing Schema

class Category(enum.Enum):

 WEATHER = "weather"

 SCIENCE = "science"

 UNKNOWN = "unknown"

 

class RoutingDecision(BaseModel):

 category: Category

 reasoning: str

 

# Step 1: Route the Query

user_query = "What's the weather like in Paris?"

# user_query = "Explain quantum physics simply."

# user_query = "What is the capital of France?"

 

prompt_router = f"""

Analyze the user query below and determine its category.

Categories:

- weather: For questions about weather conditions.

- science: For questions about science.

- unknown: If the category is unclear.

 

Query: {user_query}

"""

 

# Use client.models.generate_content with config for structured output

response_router = client.models.generate_content(

 model= 'gemini-2.0-flash-lite',

 contents=prompt_router,

 config={

 'response_mime_type': 'application/json',

 'response_schema': RoutingDecision,

 },

)

print(f"Routing Decision: Category={response_router.parsed.category}, Reasoning={response_router.parsed.reasoning}")

 

# Step 2: Handoff based on Routing

final_response = ""

if response_router.parsed.category == Category.WEATHER:

 weather_prompt = f"Provide a brief weather forecast for the location mentioned in: '{user_query}'"

 weather_response = client.models.generate_content(

 model='gemini-2.0-flash',

 contents=weather_prompt

 )

 final_response = weather_response.text

elif response_router.parsed.category == Category.SCIENCE:

 science_response = client.models.generate_content(

 model="gemini-2.5-flash-preview-04-17",

 contents=user_query

 )

 final_response = science_response.text

else:

 unknown_response = client.models.generate_content(

 model="gemini-2.0-flash-lite",

 contents=f"The user query is: {prompt_router}, but could not be answered. Here is the reasoning: {response_router.parsed.reasoning}. Write a helpful response to the user for him to try again."

 )

 final_response = unknown_response.text

print(f"\nFinal Response: {final_response}")
```

## 工作流：并行化

![](/static/blog/agentic-pattern/parallelization.png)

任务被分解为多个独立的子任务，由多个 LLM 并行处理，并将它们的输出进行聚合。这种模式利用并发性处理任务。初始查询（或其部分内容）通过不同的提示/目标并行发送给多个 LLM。当所有分支都完成后，它们各自的结果被收集起来，传递给最终的聚合器 LLM，由该 LLM 将这些结果合成为最终响应。如果子任务之间没有依赖关系，这种方法可以降低延迟；或者通过多数表决、生成多样化选项等技术来提高质量。

Use Cases:

- 采用查询分解的 RAG：将复杂查询拆分为子查询，并行执行各子查询的检索，并综合结果。
- 分析大型文档：将文档划分为多个部分，并行总结每个部分，然后合并摘要。
- 生成多重视角：向多个 LLMs 提出相同问题，但使用不同角色提示词，并汇总它们的回答。
- 对数据的映射-归约式操作。

```python
import os

import asyncio

import time

from google import genai

 

# Configure the client (ensure GEMINI_API_KEY is set in your environment)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

 

async def generate_content(prompt: str) -> str:

 response = await client.aio.models.generate_content(

 model="gemini-2.0-flash",

 contents=prompt

 )

 return response.text.strip()

 

async def parallel_tasks():

 # Define Parallel Tasks

 topic = "a friendly robot exploring a jungle"

 prompts = [

 f"Write a short, adventurous story idea about {topic}.",

 f"Write a short, funny story idea about {topic}.",

 f"Write a short, mysterious story idea about {topic}."

 ]

 # Run tasks concurrently and gather results

 start_time = time.time()

 tasks = [generate_content(prompt) for prompt in prompts]

 results = await asyncio.gather(*tasks)

 end_time = time.time()

 print(f"Time taken: {end_time - start_time} seconds")

 

 print("\n--- Individual Results ---")

 for i, result in enumerate(results):

 print(f"Result {i+1}: {result}\n")

 

 # Aggregate results and generate final story

 story_ideas = '\n'.join([f"Idea {i+1}: {result}" for i, result in enumerate(results)])

 aggregation_prompt = f"Combine the following three story ideas into a single, cohesive summary paragraph:{story_ideas}"

 aggregation_response = await client.aio.models.generate_content(

 model="gemini-2.5-flash-preview-04-17",

 contents=aggregation_prompt

 )

 return aggregation_response.text

 

 

result = await parallel_tasks()

print(f"\n--- Aggregated Summary ---\n{result}")
```

## Reflection Pattern

![](/static/blog/agentic-pattern/reflection.png)

智能体评估自身输出，并利用该反馈迭代优化其响应。这种模式也被称为评估器-优化器，采用自我修正循环：初始 LLM 生成响应或完成任务后，第二个 LLM 步骤（或使用不同提示的同一 LLM）充当反射器或评估器，根据需求或期望质量评判初始输出。该评判意见（反馈）随后被回传，促使 LLM 生成优化后的输出。此循环可重复进行，直至评估器确认需求已满足或获得令人满意的输出。

Use Cases:

- 代码生成：编写代码，执行代码，利用错误信息或测试结果作为反馈来修复缺陷。
- 写作与润色：生成初稿，反思其清晰度与语气，然后进行修改。
- 复杂问题解决：制定计划、评估其可行性，并根据评估结果进行优化。
- 信息检索：在呈现答案前，先搜索信息并使用评估器 LLM 来检查是否已找到所有必需的细节。

```python
import os

import json

from google import genai

from pydantic import BaseModel

import enum

 

# Configure the client (ensure GEMINI_API_KEY is set in your environment)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

 

class EvaluationStatus(enum.Enum):

 PASS = "PASS"

 FAIL = "FAIL"

 

class Evaluation(BaseModel):

 evaluation: EvaluationStatus

 feedback: str

 reasoning: str

 

# --- Initial Generation Function ---

def generate_poem(topic: str, feedback: str = None) -> str:

 prompt = f"Write a short, four-line poem about {topic}."

 if feedback:

 prompt += f"\nIncorporate this feedback: {feedback}"

 

 response = client.models.generate_content(

 model='gemini-2.0-flash',

 contents=prompt

 )

 poem = response.text.strip()

 print(f"Generated Poem:\n{poem}")

 return poem

 

# --- Evaluation Function ---

def evaluate(poem: str) -> Evaluation:

 print("\n--- Evaluating Poem ---")

 prompt_critique = f"""Critique the following poem. Does it rhyme well? Is it exactly four lines? 

Is it creative? Respond with PASS or FAIL and provide feedback.

 

Poem:

{poem}

"""

 response_critique = client.models.generate_content(

 model='gemini-2.0-flash',

 contents=prompt_critique,

 config={

 'response_mime_type': 'application/json',

 'response_schema': Evaluation,

 },

 )

 critique = response_critique.parsed

 print(f"Evaluation Status: {critique.evaluation}")

 print(f"Evaluation Feedback: {critique.feedback}")

 return critique

 

# Reflection Loop 

max_iterations = 3

current_iteration = 0

topic = "a robot learning to paint"

 

# simulated poem which will not pass the evaluation

current_poem = "With circuits humming, cold and bright,\nA metal hand now holds a brush"

 

while current_iteration < max_iterations:

 current_iteration += 1

 print(f"\n--- Iteration {current_iteration} ---")

 evaluation_result = evaluate(current_poem)

 

 if evaluation_result.evaluation == EvaluationStatus.PASS:

 print("\nFinal Poem:")

 print(current_poem)

 break

 else:

 current_poem = generate_poem(topic, feedback=evaluation_result.feedback)

 if current_iteration == max_iterations:

 print("\nMax iterations reached. Last attempt:")

 print(current_poem)
```

## Tool Use Pattern

![](/static/blog/agentic-pattern/tool-use.png)

大语言模型具备调用外部函数或 API 的能力，使其能与外部世界交互、获取信息或执行操作。这种模式常被称为函数调用，是当前认知度最高的模式。系统会向大语言模型提供可用工具（函数、API、数据库等）的定义（名称、描述、输入模式）。根据用户查询，大语言模型可通过生成符合预定模式的结构化输出（如 JSON）来决定调用一个或多个工具。该输出用于执行实际的外部工具/函数，并将结果返回给大语言模型。随后大语言模型利用该结果生成最终响应返回给用户。这极大地扩展了大语言模型超越其训练数据范围的能力边界。

Use Cases:

- 通过日历 API 预约安排。
- 通过金融 API 获取实时股价。
- 在向量数据库中搜索相关文档（RAG）。
- 控制智能家居设备。
- 执行代码片段。

```python
import os

from google import genai

from google.genai import types

 

# Configure the client (ensure GEMINI_API_KEY is set in your environment)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

 

# Define the function declaration for the model

weather_function = {

 "name": "get_current_temperature",

 "description": "Gets the current temperature for a given location.",

 "parameters": {

 "type": "object",

 "properties": {

 "location": {

 "type": "string",

 "description": "The city name, e.g. San Francisco",

 },

 },

 "required": ["location"],

 },

}

 

# Placeholder function to simulate API call

def get_current_temperature(location: str) -> dict:

 return {"temperature": "15", "unit": "Celsius"}

 

# Create the config object as shown in the user's example

# Use client.models.generate_content with model, contents, and config

tools = types.Tool(function_declarations=[weather_function])

contents = ["What's the temperature in London right now?"]

response = client.models.generate_content(

 model='gemini-2.0-flash',

 contents=contents,

 config = types.GenerateContentConfig(tools=[tools])

)

 

# Process the Response (Check for Function Call)

response_part = response.candidates[0].content.parts[0]

if response_part.function_call:

 function_call = response_part.function_call

 print(f"Function to call: {function_call.name}")

 print(f"Arguments: {dict(function_call.args)}")

 

 # Execute the Function

 if function_call.name == "get_current_temperature": 

 # Call the actual function

 api_result = get_current_temperature(*function_call.args)

 # Append function call and result of the function execution to contents

 follow_up_contents = [

 types.Part(function_call=function_call),

 types.Part.from_function_response(

 name="get_current_temperature",

 response=api_result

 )

 ]

 # Generate final response

 response_final = client.models.generate_content(

 model="gemini-2.0-flash",

 contents=contents + follow_up_contents,

 config=types.GenerateContentConfig(tools=[tools])

 )

 print(response_final.text)

 else:

 print(f"Error: Unknown function call requested: {function_call.name}")

else:

 print("No function call found in the response.")

 print(response.text)
```

## 规划模式（协调者-工作者）

![](/static/blog/agentic-pattern/planning.png)

中央规划型 LLM 将复杂任务分解为动态子任务列表，随后将这些子任务分配给专业的工作代理（通常借助工具调用）执行。该模式通过生成初始规划方案，旨在解决需要多步推理的复杂问题。该规划基于用户输入动态生成，子任务被分配给"工作代理"执行——若依赖关系允许，可并行处理。"协调器"或"合成器"LLM 负责收集工作代理的执行结果，评估整体目标是否达成，进而合成最终输出或在必要时启动重新规划流程。这种模式有效分散了单次 LLM 调用的认知负荷，提升推理质量，减少错误率，并支持工作流的动态调整。与路由模式的核心差异在于：规划器生成的是 *多步骤方案* 而非仅选择单一步骤。

Use Cases:

- 复杂的软件开发任务：将“构建一个功能”分解为规划、编码、测试和文档编写等子任务。
- 研究与报告生成：规划文献检索、数据提取、分析及报告撰写等步骤。
- 多模态任务：涉及图像生成、文本分析和数据整合的步骤规划。
- 执行复杂的用户请求，例如“规划一次为期三天的巴黎之旅，在我的预算内预订机票和酒店。”

```python
import os

from google import genai

from pydantic import BaseModel, Field

from typing import List

 

# Configure the client (ensure GEMINI_API_KEY is set in your environment)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

 

# Define the Plan Schema

class Task(BaseModel):

 task_id: int

 description: str

 assigned_to: str = Field(description="Which worker type should handle this? E.g., Researcher, Writer, Coder")

 

class Plan(BaseModel):

 goal: str

 steps: List[Task]

 

# Step 1: Generate the Plan (Planner LLM)

user_goal = "Write a short blog post about the benefits of AI agents."

 

prompt_planner = f"""

Create a step-by-step plan to achieve the following goal. 

Assign each step to a hypothetical worker type (Researcher, Writer).

 

Goal: {user_goal}

"""

 

print(f"Goal: {user_goal}")

print("Generating plan...")

 

# Use a model capable of planning and structured output

response_plan = client.models.generate_content(

 model='gemini-2.5-pro-preview-03-25',

 contents=prompt_planner,

 config={

 'response_mime_type': 'application/json',

 'response_schema': Plan,

 },

)

 

# Step 2: Execute the Plan (Orchestrator/Workers - Omitted for brevity) 

for step in response_plan.parsed.steps:

 print(f"Step {step.task_id}: {step.description} (Assignee: {step.assigned_to})")
```

## Multi-Agent Pattern

![](/static/blog/agentic-pattern/multi-agent.png) 协调者、管理者模式 %% 群体智能模式

多个独立智能体各司其职，分别承担特定角色、身份或专业领域，共同协作实现统一目标。该模式采用自主或半自主智能体，每个智能体可能具备独特职能（如项目经理、程序员、测试员、评审员）、专业知识或专用工具权限。它们通过交互协作达成目标，通常由中央"协调者"或"管理者"智能体（如图中 PM 角色）统筹调度，或采用交接逻辑——即某个智能体将控制权移交至另一智能体。

Use Cases:

- 模拟不同 AI 角色间的辩论或头脑风暴。
- 涉及规划、编码、测试和部署的智能体复杂软件创建。
- 运行虚拟实验或模拟，其中包含代表不同参与者的智能体。
- 协作写作或内容创作流程。

注意：以下示例展示了如何使用多智能体模式，包含任务交接逻辑和结构化输出。建议参考 [LangGraph 多智能体集群](https://github.com/langchain-ai/langgraph-swarm-py) 或 [Crew AI](https://www.crewai.com/open-source) 进行深入了解。

```python
from google import genai

from pydantic import BaseModel, Field

 

# Configure the client (ensure GEMINI_API_KEY is set in your environment)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

 

# Define Structured Output Schemas

class Response(BaseModel):

 handoff: str = Field(default="", description="The name/role of the agent to hand off to. Available agents: 'Restaurant Agent', 'Hotel Agent'")

 message: str = Field(description="The response message to the user or context for the next agent")

 

# Agent Function

def run_agent(agent_name: str, system_prompt: str, prompt: str) -> Response:

 response = client.models.generate_content(

 model='gemini-2.0-flash',

 contents=prompt,

 config = {'system_instruction': f'You are {agent_name}. {system_prompt}', 'response_mime_type': 'application/json', 'response_schema': Response}

 )

 return response.parsed

 

 

# Define System Prompts for the agents

hotel_system_prompt = "You are a Hotel Booking Agent. You ONLY handle hotel bookings. If the user asks about restaurants, flights, or anything else, respond with a short handoff message containing the original request and set the 'handoff' field to 'Restaurant Agent'. Otherwise, handle the hotel request and leave 'handoff' empty."

restaurant_system_prompt = "You are a Restaurant Booking Agent. You handle restaurant recommendations and bookings based on the user's request provided in the prompt."

 

# Prompt to be about a restaurant

initial_prompt = "Can you book me a table at an Italian restaurant for 2 people tonight?"

print(f"Initial User Request: {initial_prompt}")

 

# Run the first agent (Hotel Agent) to force handoff logic

output = run_agent("Hotel Agent", hotel_system_prompt, initial_prompt)

 

# simulate a user interaction to change the prompt and handoff

if output.handoff == "Restaurant Agent":

 print("Handoff Triggered: Hotel to Restaurant")

 output = run_agent("Restaurant Agent", restaurant_system_prompt, initial_prompt)

elif output.handoff == "Hotel Agent":

 print("Handoff Triggered: Restaurant to Hotel")

 output = run_agent("Hotel Agent", hotel_system_prompt, initial_prompt)

 

print(output.message)
```

## 组合与定制这些模式

重要的是要明白，这些模式并非固定规则，而是灵活的建筑模块。现实中的智能体系统常常融合多种模式的元素。一个规划型智能体可能会运用工具使用模式，而其下属可能采用反思机制。多智能体系统内部或许会通过路由模式进行任务分配。

任何 LLM 应用成功的关键，尤其是复杂的智能体系统，在于实证评估。定义指标、衡量性能、识别瓶颈或故障点，并持续迭代优化设计。切忌过度工程化。