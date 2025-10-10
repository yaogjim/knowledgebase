---
title: "Build a Deep Research Agent: $1 Alternative to $200 OpenAI's Tool"
source: "https://www.analyticsvidhya.com/blog/2025/02/build-your-own-deep-research-agent/"
author:
  - "[[Dipanjan (DJ) Sarkar]]"
published: 2025-02-05
created: 2025-03-26
description: "Build your own Deep Research & Report Generation Agent for under $1! A hands-on guide to creating an OpenAI Deep Research alternative."
tags:
  - "clippings"
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
## 构建一个深度研究代理：200 美元 OpenAI 工具的 1 美元替代品

最后更新时间：2025 年 2 月 26 日

如今，智能 AI 系统风靡一时！它们简直就是在 for 循环中与某些提示和工具相连的LLMs，可以为你自动执行任务。然而，你也可以构建可靠的逐步工作流程，在LLM为你解决问题时引导它变得更加可靠。最近在 2025 年 2 月，OpenAI 推出了深度研究，这是一个可以接收用户主题、自动进行一系列搜索并将其编译成一份不错报告的智能体。然而，它仅在其 200 美元的专业计划中可用。在这里，我将向你展示一个逐步的实践指南，教你如何使用 LangGraph 以不到一美元的成本构建自己的深度研究和报告生成智能体！

## OpenAI 深度研究简报

OpenAI 于 2025 年 2 月 2 日推出了深度研究功能，该功能已作为其 ChatGPT 产品的一项附加功能推出。他们将此称为一种新的智能体能力，它可以针对用户提出的复杂任务或查询在互联网上进行多步骤研究。他们声称，它能在几十分钟内完成人类需要花费数小时才能完成的任务。

![OpenAI DeepSearch](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/image.gif)

深度研究进行中 – 来源：OpenAI

深度研究是 OpenAI 当前的智能体人工智能产品，它可以为你自主完成工作。你通过提示向它给出一项任务或主题，ChatGPT 会查找、分析并综合数百个在线资源，以生成一份研究分析师水平的全面报告。它由即将推出的针对网页浏览和数据分析进行了优化的 OpenAI o3 模型版本提供支持，利用推理来搜索、解释和分析互联网上大量的文本、图像和 PDF 文件，最终编制出一份结构良好的报告。

个性化生成式人工智能学习路径 2025✨专为您打造！

新功能 Beta

[View original](https://www.analyticsvidhya.com/learning-path/chat/?article_id=219774&utm_source=blog_banner)

不过，这确实有一些限制，因为只有订阅了 200 美元的 ChatGPT 专业版才能使用它。这就是我自己的智能 AI 系统发挥作用的地方，它可以进行深入研究，并在不到一美元的成本下生成一份不错的综合报告。让我们开始吧！

## 深度研究与结构化报告生成规划智能 AI 系统架构

下图展示了我们系统的整体架构，我们将使用 LangChain 的 LangGraph 开源框架来实现该架构，以便轻松且可控地构建有状态的智能系统。

![Deep Research & Structured Report Generation Planning Agentic AI System Architecture](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T160939.851.webp)

深度研究与报告生成人工智能代理 - 来源：作者

为上述系统提供动力的关键组件包括：

- 一个强大的、擅长推理的大语言模型。我们正在使用价格不算超级昂贵且速度快的 GPT-4o，不过，你甚至可以使用像 Llama 3.2 这样的LLMs或其他开源替代方案。
- 用于构建我们的智能系统的 LangGraph，因为它是一个出色的框架，用于构建基于循环图的系统，该系统可以在整个工作流程中维护状态变量，并有助于轻松构建智能反馈循环。
- Tavily AI 是一款出色的人工智能搜索引擎，非常适合进行网络研究以及从网站获取数据以支持我们的深度研究系统。

本项目专注于构建一个用于深度研究和结构化报告生成的规划代理，作为 OpenAI 深度研究的替代方案。该代理遵循流行的规划代理设计模式，自动执行分析用户定义主题、进行深度网络研究以及生成结构良好的报告的过程。该工作流程实际上受到了 LangChain 自己的 Report mAIstro 的启发，所以要充分肯定他们想出了这个工作流程，我以此为基础灵感，然后构建了这个系统，它包括以下组件：

#### 1\. 报告规划：

- 代理分析用户提供的主题和默认报告模板，以创建报告的自定义计划。
- 诸如引言、关键部分和结论等部分是根据主题定义的。
- 在确定主要部分之前，使用网络搜索工具收集所需信息。

#### 2\. 研究与写作的并行执行：

- 该代理使用并行执行来高效地执行：
	- 网络研究：为每个部分生成查询，并通过网络搜索工具执行以检索最新信息。
	- 章节写作：检索到的数据用于为每个章节撰写内容，过程如下：
		- 研究人员从网络收集相关数据。
		- 章节编写人员使用这些数据为指定章节生成结构化内容。

#### 3\. 格式化已完成部分：

- 一旦所有部分都撰写完成，就会对其进行格式化，以确保一致性并符合报告结构。

#### 4\. 引言和结论撰写：

- 在主要部分完成并格式化之后：
	- 引言和结论是根据其余部分的内容（并行）编写的
	- 此过程可确保这些部分与报告的整体流程和见解保持一致。

#### 5\. 最终编译：

- 所有已完成的部分汇总在一起以生成最终报告。
- 最终输出是一份采用维基文档风格的全面且结构化的报告。

现在让我们开始使用 LangGraph 和 Tavily 逐步构建这些组件。

## 我们深度研究与结构化报告生成规划智能体人工智能系统的实践实施

我们现在将基于上一节详细讨论的架构，逐步为我们的深度研究报告生成代理人工智能系统实现端到端工作流程，并提供详细解释、代码和输出。

### 安装依赖项

我们首先安装必要的依赖项，这些依赖项将是我们用于构建系统的库。这包括 langchain、LangGraph，还有用于生成漂亮的 markdown 报告的 rich。

```diff
!pip install langchain==0.3.14
!pip install langchain-openai==0.3.0
!pip install langchain-community==0.3.14
!pip install langgraph==0.2.64
!pip install rich
```

### 输入 OpenAI API 密钥

我们使用 getpass()函数输入我们的 OpenAI 密钥，这样我们就不会在代码中意外暴露我们的密钥。

```java
from getpass import getpass
OPENAI_KEY = getpass('Enter Open AI API Key: ')
```

### 输入塔维利搜索 API 密钥

我们使用 getpass()函数输入我们的 Tavily 搜索密钥，这样我们就不会在代码中意外暴露我们的密钥。你可以从这里获取密钥，而且他们有慷慨的免费套餐。

```ini
TAVILY_API_KEY = getpass('Enter Tavily Search API Key: ')
```

### 设置环境变量

接下来，我们设置一些系统环境变量，这些变量将在稍后验证我们的LLM和 Tavily Search 时使用。

```lua
import os
os.environ['OPENAI_API_KEY'] = OPENAI_KEY
os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY
```

### 定义代理状态架构

我们使用 LangGraph 将我们的智能系统构建为一个带有节点的图，其中每个节点由整个工作流程中的一个特定执行步骤组成。每组特定的操作（节点）将具有如下定义的自己的模式。你可以根据自己的报告生成风格进一步自定义此内容。

```python
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
import operator
from typing import  Annotated, List, Optional, Literal

# defines structure for each section in the report
class Section(BaseModel):
    name: str = Field(
        description="Name for a particular section of the report.",
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section.",
    )
    research: bool = Field(
        description="Whether to perform web search for this section of the report."
    )
    content: str = Field(
        description="The content for this section."
    )

class Sections(BaseModel):
    sections: List[Section] = Field(
        description="All the Sections of the overall report.",
    )

# defines structure for queries generated for deep research
class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Query for web search.")

class Queries(BaseModel):
    queries: List[SearchQuery] = Field(
        description="List of web search queries.",
    )

# consists of input topic and output report generated
class ReportStateInput(TypedDict):
    topic: str # Report topic

class ReportStateOutput(TypedDict):
    final_report: str # Final report

# overall agent state which will be passed and updated in nodes in the graph
class ReportState(TypedDict):
    topic: str # Report topic
    sections: list[Section] # List of report sections
    completed_sections: Annotated[list, operator.add] # Send() API
    report_sections_from_research: str # completed sections to write final sections
    final_report: str # Final report

# defines the key structure for sections written using the agent 
class SectionState(TypedDict):
    section: Section # Report section
    search_queries: list[SearchQuery] # List of search queries
    source_str: str # String of formatted source content from web search
    report_sections_from_research: str # completed sections to write final sections
    completed_sections: list[Section] # Final key in outer state for Send() API

class SectionOutputState(TypedDict):
    completed_sections: list[Section] # Final key in outer state for Send() API
```

### 实用函数

我们定义了一些实用函数，这些函数将帮助我们运行并行网络搜索查询并格式化从网络获得的结果。

#### 1\. 运行搜索查询(…)

这将异步运行针对特定查询列表的 Tavily 搜索查询，并返回搜索结果。这是异步的，因此它是非阻塞的，可以并行执行。

```python
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
import asyncio
from dataclasses import asdict, dataclass

# just to handle objects created from LLM reponses
@dataclass
class SearchQuery:
    search_query: str
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

tavily_search = TavilySearchAPIWrapper()

async def run_search_queries(
    search_queries: List[Union[str, SearchQuery]],
    num_results: int = 5,
    include_raw_content: bool = False
) -> List[Dict]:
    search_tasks = []
    for query in search_queries:
        # Handle both string and SearchQuery objects
        # Just in case LLM fails to generate queries as:
        # class SearchQuery(BaseModel):
        #     search_query: str
        query_str = query.search_query if isinstance(query, SearchQuery) 
                        else str(query) # text query
        try:
            # get results from tavily async (in parallel) for each search query
            search_tasks.append(
                tavily_search.raw_results_async(
                    query=query_str,
                    max_results=num_results,
                    search_depth='advanced',
                    include_answer=False,
                    include_raw_content=include_raw_content
                )
            )
        except Exception as e:
            print(f"Error creating search task for query '{query_str}': {e}")
            continue
    # Execute all searches concurrently and await results
    try:
        if not search_tasks:
            return []
        search_docs = await asyncio.gather(*search_tasks, return_exceptions=True)
        # Filter out any exceptions from the results
        valid_results = [
            doc for doc in search_docs
            if not isinstance(doc, Exception)
        ]
        return valid_results
    except Exception as e:
        print(f"Error during search queries: {e}")
        return []
```

#### 2\. 格式化搜索查询结果(…)

这将从 Tavily 搜索结果中提取上下文，确保内容不会从相同的 URL 重复，并将其格式化以显示来源、URL 和相关内容（以及可选的原始内容，可根据令牌数量进行截断）

```python
import tiktoken
from typing import List, Dict, Union, Any

def format_search_query_results(
    search_response: Union[Dict[str, Any], List[Any]],
    max_tokens: int = 2000,
    include_raw_content: bool = False
) -> str:
    encoding = tiktoken.encoding_for_model("gpt-4")
    sources_list = []

    # Handle different response formats if search results is a dict
    if isinstance(search_response, dict):
        if 'results' in search_response:
            sources_list.extend(search_response['results'])
        else:
            sources_list.append(search_response)
    # if search results is a list
    elif isinstance(search_response, list):
        for response in search_response:
            if isinstance(response, dict):
                if 'results' in response:
                    sources_list.extend(response['results'])
                else:
                    sources_list.append(response)
            elif isinstance(response, list):
                sources_list.extend(response)

    if not sources_list:
        return "No search results found."

    # Deduplicate by URL and keep unique sources (website urls)
    unique_sources = {}
    for source in sources_list:
        if isinstance(source, dict) and 'url' in source:
            if source['url'] not in unique_sources:
                unique_sources[source['url']] = source

    # Format output
    formatted_text = "Content from web search:\n\n"
    for i, source in enumerate(unique_sources.values(), 1):
        formatted_text += f"Source {source.get('title', 'Untitled')}:\n===\n"
        formatted_text += f"URL: {source['url']}\n===\n"
        formatted_text += f"Most relevant content from source: {source.get('content', 'No content available')}\n===\n"

        if include_raw_content:
            # truncate raw webpage content to a certain number of tokens to prevent exceeding LLM max token window
            raw_content = source.get("raw_content", "")
            if raw_content:
                tokens = encoding.encode(raw_content)
                truncated_tokens = tokens[:max_tokens]
                truncated_content = encoding.decode(truncated_tokens)
                formatted_text += f"Raw Content: {truncated_content}\n\n"

    return formatted_text.strip()
```

我们可以按如下方式测试这些函数，看看它们是否有效：

```python
docs = await run_search_queries(['langgraph'], include_raw_content=True)
output = format_search_query_results(docs, max_tokens=500, 
   include_raw_content=True)
print(output)
```

#### Output

```diff
Content from web search:

Source Introduction - GitHub Pages:
===
URL: https://langchain-ai.github.io/langgraphjs/
===
Most relevant content from source: Overview¶. LangGraph is a library for
 building stateful, multi-actor applications with LLMs, used to create agent
 and multi-agent workflows......
===
Raw Content: 🦜🕸️LangGraph.js¶
⚡ Building language agents as graphs ⚡
Looking for the Python version? Click
here ( docs).
Overview......

Source ️LangGraph - GitHub Pages:
===
URL: https://langchain-ai.github.io/langgraph/
===
Most relevant content from source: Overview¶. LangGraph is a library for
 building stateful, multi-actor applications with LLMs, ......
===
Raw Content: 🦜🕸️LangGraph¶
⚡ Building language agents as graphs ⚡
Note
Looking for the JS version? See the JS repo and the JS docs.
Overview¶
LangGraph is a library for building
stateful, multi-actor applications with LLMs, ......
```

### 创建默认报告模板

这是LLM了解如何构建通用报告的起点，它将以此为指导方针，根据主题构建自定义报告结构。请记住，这不是最终的报告结构，而更像是引导代理的提示。

```ini
# Structure Guideline
DEFAULT_REPORT_STRUCTURE = """The report structure should focus on breaking-down the user-provided topic
                              and building a comprehensive report in markdown using the following format:

                              1. Introduction (no web search needed)
                                    - Brief overview of the topic area

                              2. Main Body Sections:
                                    - Each section should focus on a sub-topic of the user-provided topic
                                    - Include any key concepts and definitions
                                    - Provide real-world examples or case studies where applicable

                              3. Conclusion (no web search needed)
                                    - Aim for 1 structural element (either a list of table) that distills the main body sections
                                    - Provide a concise summary of the report

                              When generating the final response in markdown, if there are special characters in the text,
                              such as the dollar symbol, ensure they are escaped properly for correct rendering e.g $25.5 should become \$25.5
                          """
```

### 报告规划器的指令提示

有两个主要的指令提示符：

#### 1\. 报告计划查询生成器提示

帮助LLM根据主题生成初始问题列表，以便从网络获取更多关于该主题的信息，从而规划报告的整体章节和结构

```ini
REPORT_PLAN_QUERY_GENERATOR_PROMPT = """You are an expert technical report writer, helping to plan a report.

The report will be focused on the following topic:
{topic}

The report structure will follow these guidelines:
{report_organization}

Your goal is to generate {number_of_queries} search queries that will help gather comprehensive information for planning the report sections.

The query should:
1. Be related to the topic
2. Help satisfy the requirements specified in the report organization

Make the query specific enough to find high-quality, relevant sources while covering the depth and breadth needed for the report structure.
"""
```

#### 2\. 报告计划部分生成器提示

在这里，我们使用默认报告模板、主题名称以及初始查询生成的搜索结果来输入LLM，以创建报告的详细结构。LLM将为报告中的每个主要部分生成包含以下字段的结构化响应（这只是报告结构——此步骤不创建内容）：

- 名称 – 报告此部分的名称。
- 描述 – 本节将涵盖的主要主题和概念的简要概述。
- 研究 – 是否要对报告的这一部分进行网络搜索。
- 内容 – 该部分的内容，你现在可以留空。
```ini
REPORT_PLAN_SECTION_GENERATOR_PROMPT = """You are an expert technical report writer, helping to plan a report.

Your goal is to generate the outline of the sections of the report.

The overall topic of the report is:
{topic}

The report should follow this organizational structure:
{report_organization}

You should reflect on this additional context information from web searches to plan the main sections of the report:
{search_context}

Now, generate the sections of the report. Each section should have the following fields:
- Name - Name for this section of the report.
- Description - Brief overview of the main topics and concepts to be covered in this section.
- Research - Whether to perform web search for this section of the report or not.
- Content - The content of the section, which you will leave blank for now.

Consider which sections require web search.
For example, introduction and conclusion will not require research because they will distill information from other parts of the report.
"""
```

### 报表规划器的节点函数

我们将构建报告规划器节点的逻辑，其目标是根据输入的用户主题和默认报告模板指南，创建一个带有主要章节名称和描述的结构化自定义报告模板。

![Node Function for Report Planner](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161136.455.webp)

报告规划器节点功能 – 来源：作者

此函数使用先前创建的两个提示来：

- 首先，根据用户主题生成一些查询
- 在网络上搜索并获取有关这些查询的一些信息
- 使用此信息生成报告的整体结构，包括需要创建的关键部分
```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

async def generate_report_plan(state: ReportState):
    """Generate the overall plan for building the report"""
    topic = state["topic"]
    print('--- Generating Report Plan ---')

    report_structure = DEFAULT_REPORT_STRUCTURE
    number_of_queries = 8

    structured_llm = llm.with_structured_output(Queries)

    system_instructions_query = REPORT_PLAN_QUERY_GENERATOR_PROMPT.format(
        topic=topic,
        report_organization=report_structure,
        number_of_queries=number_of_queries
    )

    try:
        # Generate queries
        results = structured_llm.invoke([
            SystemMessage(content=system_instructions_query),
            HumanMessage(content='Generate search queries that will help with planning the sections of the report.')
        ])
        # Convert SearchQuery objects to strings
        query_list = [
            query.search_query if isinstance(query, SearchQuery) else str(query)
            for query in results.queries
        ]
        # Search web and ensure we wait for results
        search_docs = await run_search_queries(
            query_list,
            num_results=5,
            include_raw_content=False
        )
        if not search_docs:
            print("Warning: No search results returned")
            search_context = "No search results available."
        else:
            search_context = format_search_query_results(
                search_docs,
                include_raw_content=False
            )
        # Generate sections
        system_instructions_sections = REPORT_PLAN_SECTION_GENERATOR_PROMPT.format(
            topic=topic,
            report_organization=report_structure,
            search_context=search_context
        )
        structured_llm = llm.with_structured_output(Sections)
        report_sections = structured_llm.invoke([
            SystemMessage(content=system_instructions_sections),
            HumanMessage(content="Generate the sections of the report. Your response must include a 'sections' field containing a list of sections. Each section must have: name, description, plan, research, and content fields.")
        ])

        print('--- Generating Report Plan Completed ---')
        return {"sections": report_sections.sections}

    except Exception as e:
        print(f"Error in generate_report_plan: {e}")
        return {"sections": []}
```

### 章节构建器的指令提示 - 查询生成器

有一个主要的指令提示符：

#### 1\. 报告部分查询生成器提示

帮助LLM为需要构建的特定部分主题生成全面的问题列表

```ini
REPORT_SECTION_QUERY_GENERATOR_PROMPT = """Your goal is to generate targeted web search queries that will gather comprehensive information for writing a technical report section.

Topic for this section:
{section_topic}

When generating {number_of_queries} search queries, ensure that they:
1. Cover different aspects of the topic (e.g., core features, real-world applications, technical architecture)
2. Include specific technical terms related to the topic
3. Target recent information by including year markers where relevant (e.g., "2024")
4. Look for comparisons or differentiators from similar technologies/approaches
5. Search for both official documentation and practical implementation examples

Your queries should be:
- Specific enough to avoid generic results
- Technical enough to capture detailed implementation information
- Diverse enough to cover all aspects of the section plan
- Focused on authoritative sources (documentation, technical blogs, academic papers)"""
```

### 节点功能用于章节构建器 - 生成查询（查询生成器）

这使用上面的部分主题和指令提示来生成一些问题，以便在网络上进行搜索，从而获取有关该部分主题的有用信息。

![Node Function for Section Builder - Generate Queries (Query Generator)](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161210.363.webp)

查询生成器节点功能 – 来源：作者

```python
def generate_queries(state: SectionState):
    """ Generate search queries for a specific report section """

    # Get state
    section = state["section"]
    print('--- Generating Search Queries for Section: '+ section.name +' ---')
    # Get configuration
    number_of_queries = 5
    # Generate queries
    structured_llm = llm.with_structured_output(Queries)
    # Format system instructions
    system_instructions = REPORT_SECTION_QUERY_GENERATOR_PROMPT.format(section_topic=section.description,                                                                       number_of_queries=number_of_queries)
    # Generate queries
    user_instruction = "Generate search queries on the provided topic."
    search_queries = structured_llm.invoke([SystemMessage(content=system_instructions),
                                     HumanMessage(content=user_instruction)])

    print('--- Generating Search Queries for Section: '+ section.name +' Completed ---')
    return {"search_queries": search_queries.queries}
```

### 章节生成器的节点功能 – 搜索网络

获取由 generate\_queries(…)针对特定部分生成的查询，在网络上进行搜索，并使用我们之前定义的实用函数对搜索结果进行格式化。

![Node Function for Section Builder - Search Web](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161255.752.webp)

网络研究员节点功能 – 来源：作者

```python
async def search_web(state: SectionState):
    """ Search the web for each query, then return a list of raw sources and a formatted string of sources."""

    # Get state
    search_queries = state["search_queries"]
    print('--- Searching Web for Queries ---')
    # Web search
    query_list = [query.search_query for query in search_queries]
    search_docs = await run_search_queries(search_queries, num_results=6, include_raw_content=True)
    # Deduplicate and format sources
    search_context = format_search_query_results(search_docs, max_tokens=4000, include_raw_content=True)

    print('--- Searching Web for Queries Completed ---')
    return {"source_str": search_context}
```

### 章节构建器 - 章节编写器的指令提示

有一个主要的指令提示符：

#### 1\. 章节编写提示

约束LLM使用特定的风格、结构、长度、方法指南生成并写入特定部分的内容，并且还会发送之前使用 search\_web(…)函数从网络获取的文档。

```markdown
SECTION_WRITER_PROMPT = """You are an expert technical writer crafting one specific section of a technical report.

Title for the section:
{section_title}

Topic for this section:
{section_topic}

Guidelines for writing:

1. Technical Accuracy:
- Include specific version numbers
- Reference concrete metrics/benchmarks
- Cite official documentation
- Use technical terminology precisely

2. Length and Style:
- Strict 150-200 word limit
- No marketing language
- Technical focus
- Write in simple, clear language do not use complex words unnecessarily
- Start with your most important insight in **bold**
- Use short paragraphs (2-3 sentences max)

3. Structure:
- Use ## for section title (Markdown format)
- Only use ONE structural element IF it helps clarify your point:
  * Either a focused table comparing 2-3 key items (using Markdown table syntax)
  * Or a short list (3-5 items) using proper Markdown list syntax:
    - Use \`*\` or \`-\` for unordered lists
    - Use \`1.\` for ordered lists
    - Ensure proper indentation and spacing
- End with ### Sources that references the below source material formatted as:
  * List each source with title, date, and URL
  * Format: \`- Title : URL\`

3. Writing Approach:
- Include at least one specific example or case study if available
- Use concrete details over general statements
- Make every word count
- No preamble prior to creating the section content
- Focus on your single most important point

4. Use this source material obtained from web searches to help write the section:
{context}

5. Quality Checks:
- Format should be Markdown
- Exactly 150-200 words (excluding title and sources)
- Careful use of only ONE structural element (table or bullet list) and only if it helps clarify your point
- One specific example / case study if available
- Starts with bold insight
- No preamble prior to creating the section content
- Sources cited at end
- If there are special characters in the text, such as the dollar symbol,
  ensure they are escaped properly for correct rendering e.g $25.5 should become \$25.5
"""
```

### 章节生成器的节点函数 - 编写章节（章节编写器）

使用上述的 SECTION\_WRITER\_PROMPT，并将章节名称、描述和网络搜索文档提供给它，然后将其传递给LLM以编写该章节的内容

![Node Function for Section Builder - Write Section (Section Writer)](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161330.195.webp)

章节编写者节点功能 – 来源：作者

```python
def write_section(state: SectionState):
    """ Write a section of the report """

    # Get state
    section = state["section"]
    source_str = state["source_str"]
    print('--- Writing Section : '+ section.name +' ---')
    # Format system instructions
    system_instructions = SECTION_WRITER_PROMPT.format(section_title=section.name,                                                     section_topic=section.description,                                                       context=source_str)
    # Generate section
    user_instruction = "Generate a report section based on the provided sources."
    section_content = llm.invoke([SystemMessage(content=system_instructions),
                                  HumanMessage(content=user_instruction)])
    # Write content to the section object
    section.content = section_content.content

    print('--- Writing Section : '+ section.name +' Completed ---')
    # Write the updated section to completed sections
    return {"completed_sections": [section]}
```

### 创建章节构建器子代理

此代理（或者更具体地说，子代理）将被并行调用多次，针对每个部分调用一次，以搜索网络、获取内容，然后撰写该特定部分。我们利用 LangGraph 的 Send 结构来实现这一点。

![Create the Section Builder Sub-Agent](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161407.452.webp)

章节构建器子代理 - 来源：作者

```python
from langgraph.graph import StateGraph, START, END

# Add nodes and edges
section_builder = StateGraph(SectionState, output=SectionOutputState)
section_builder.add_node("generate_queries", generate_queries)
section_builder.add_node("search_web", search_web)
section_builder.add_node("write_section", write_section)
section_builder.add_edge(START, "generate_queries")
section_builder.add_edge("generate_queries", "search_web")
section_builder.add_edge("search_web", "write_section")
section_builder.add_edge("write_section", END)
section_builder_subagent = section_builder.compile()

# Display the graph
from IPython.display import display, Image
Image(section_builder_subagent.get_graph().draw_mermaid_png())
```

#### Output

![langgraph.graph](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161442.204.webp)

### 创建动态并行化节点函数 – 并行化节写入

Send(…) 用于并行化，并针对每个部分调用一次 section\_builder\_subagent 以（并行地）写入内容

```python
from langgraph.constants import Send

def parallelize_section_writing(state: ReportState):
    """ This is the "map" step when we kick off web research for some sections of the report in parallel and then write the section"""

    # Kick off section writing in parallel via Send() API for any sections that require research
    return [
        Send("section_builder_with_web_search", # name of the subagent node
             {"section": s})
            for s in state["sections"]
              if s.research
    ]
```

### 创建格式节节点函数

这基本上是所有章节进行格式化并组合成一个大文档的部分。

![Create Format Sections Node Function](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161531.617.webp)

格式化章节节点功能 – 来源：作者

```python
def format_sections(sections: list[Section]) -> str:
    """ Format a list of report sections into a single text string """
    formatted_str = ""
    for idx, section in enumerate(sections, 1):
        formatted_str += f"""
{'='*60}
Section {idx}: {section.name}
{'='*60}
Description:
{section.description}
Requires Research:
{section.research}

Content:
{section.content if section.content else '[Not yet written]'}

"""
    return formatted_str

def format_completed_sections(state: ReportState):
    """ Gather completed sections from research and format them as context for writing the final sections """

    print('--- Formatting Completed Sections ---')
    # List of completed sections
    completed_sections = state["completed_sections"]
    # Format completed section to str to use as context for final sections
    completed_report_sections = format_sections(completed_sections)

    print('--- Formatting Completed Sections is Done ---')
    return {"report_sections_from_research": completed_report_sections}
```

### 最后一部分的指令提示

有一个主要的指令提示符：

#### 1\. 最终部分编写器提示

约束LLM根据某些关于风格、结构、长度、方法的指导方针生成并撰写引言或结论的内容，并且已经撰写部分的内容也会被发送。

```diff
FINAL_SECTION_WRITER_PROMPT = """You are an expert technical writer crafting a section that synthesizes information from the rest of the report.

Title for the section:
{section_title}

Topic for this section:
{section_topic}

Available report content of already completed sections:
{context}

1. Section-Specific Approach:

For Introduction:
- Use # for report title (Markdown format)
- 50-100 word limit
- Write in simple and clear language
- Focus on the core motivation for the report in 1-2 paragraphs
- Use a clear narrative arc to introduce the report
- Include NO structural elements (no lists or tables)
- No sources section needed

For Conclusion/Summary:
- Use ## for section title (Markdown format)
- 100-150 word limit
- For comparative reports:
    * Must include a focused comparison table using Markdown table syntax
    * Table should distill insights from the report
    * Keep table entries clear and concise
- For non-comparative reports:
    * Only use ONE structural element IF it helps distill the points made in the report:
    * Either a focused table comparing items present in the report (using Markdown table syntax)
    * Or a short list using proper Markdown list syntax:
      - Use \`*\` or \`-\` for unordered lists
      - Use \`1.\` for ordered lists
      - Ensure proper indentation and spacing
- End with specific next steps or implications
- No sources section needed

3. Writing Approach:
- Use concrete details over general statements
- Make every word count
- Focus on your single most important point

4. Quality Checks:
- For introduction: 50-100 word limit, # for report title, no structural elements, no sources section
- For conclusion: 100-150 word limit, ## for section title, only ONE structural element at most, no sources section
- Markdown format
- Do not include word count or any preamble in your response
- If there are special characters in the text, such as the dollar symbol,
  ensure they are escaped properly for correct rendering e.g $25.5 should become \$25.5"""
```

### 创建写入最终部分节点函数

此函数使用上述指令提示 FINAL\_SECTION\_WRITER\_PROMPT 来撰写引言和结论。此函数将使用下面的 Send(…)并行执行

![Create Write Final Sections Node Function](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161609.063.webp)

最后部分编写器节点功能 – 来源：作者

```python
def write_final_sections(state: SectionState):
    """ Write the final sections of the report, which do not require web search and use the completed sections as context"""

    # Get state
    section = state["section"]
    completed_report_sections = state["report_sections_from_research"]

    print('--- Writing Final Section: '+ section.name + ' ---')
    # Format system instructions
    system_instructions = FINAL_SECTION_WRITER_PROMPT.format(section_title=section.name,
                                                             section_topic=section.description,
                                                             context=completed_report_sections)

    # Generate section
    user_instruction = "Craft a report section based on the provided sources."
    section_content = llm.invoke([SystemMessage(content=system_instructions),
                                  HumanMessage(content=user_instruction)])

    # Write content to section
    section.content = section_content.content

    print('--- Writing Final Section: '+ section.name + ' Completed ---')
    # Write the updated section to completed sections
    return {"completed_sections": [section]}
```

### 创建动态并行化节点函数 – 并行化最终部分写入

Send(…) 用于并行化，并针对引言和结论中的每一个调用一次 write\_final\_sections 来（并行地）写入内容

```python
from langgraph.constants import Send

def parallelize_final_section_writing(state: ReportState):
    """ Write any final sections using the Send API to parallelize the process """

    # Kick off section writing in parallel via Send() API for any sections that do not require research
    return [
        Send("write_final_sections",
             {"section": s, "report_sections_from_research": state["report_sections_from_research"]})
                 for s in state["sections"]
                    if not s.research
    ]
```

### 编译最终报告节点功能

此函数将报告的所有部分合并在一起，并将其汇编成最终报告文档

![Compile Final Report Node Function](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161646.327.webp)

编译最终报告节点功能 – 来源：作者

```python
def compile_final_report(state: ReportState):
    """ Compile the final report """

    # Get sections
    sections = state["sections"]
    completed_sections = {s.name: s.content for s in state["completed_sections"]}

    print('--- Compiling Final Report ---')
    # Update sections with completed content while maintaining original order
    for section in sections:
        section.content = completed_sections[section.name]

    # Compile final report
    all_sections = "\n\n".join([s.content for s in sections])
    # Escape unescaped $ symbols to display properly in Markdown
    formatted_sections = all_sections.replace("\\$", "TEMP_PLACEHOLDER")  # Temporarily mark already escaped $
    formatted_sections = formatted_sections.replace("$", "\\$")  # Escape all $
    formatted_sections = formatted_sections.replace("TEMP_PLACEHOLDER", "\\$")  # Restore originally escaped $

    # Now escaped_sections contains the properly escaped Markdown text
    print('--- Compiling Final Report Done ---')
    return {"final_report": formatted_sections}
```

### 构建我们的深度研究与报告撰写代理

我们现在将所有已定义的组件和子代理组合在一起，并构建我们的主要规划代理。

![Deep Research & Structured Report Generation Planning Agentic AI System Architecture](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T160939.851.webp)

深度研究与报告撰写者智能工作流程 – 来源：作者

```python
builder = StateGraph(ReportState, input=ReportStateInput, output=ReportStateOutput)

builder.add_node("generate_report_plan", generate_report_plan)
builder.add_node("section_builder_with_web_search", section_builder_subagent)
builder.add_node("format_completed_sections", format_completed_sections)
builder.add_node("write_final_sections", write_final_sections)
builder.add_node("compile_final_report", compile_final_report)

builder.add_edge(START, "generate_report_plan")
builder.add_conditional_edges("generate_report_plan",
                              parallelize_section_writing,
                              ["section_builder_with_web_search"])
builder.add_edge("section_builder_with_web_search", "format_completed_sections")
builder.add_conditional_edges("format_completed_sections",
                              parallelize_final_section_writing,
                              ["write_final_sections"])
builder.add_edge("write_final_sections", "compile_final_report")
builder.add_edge("compile_final_report", END)

reporter_agent = builder.compile()
# view agent structure
display(Image(reporter_agent.get_graph(xray=True).draw_mermaid_png()))
```

#### Output

![Mermaid graph ](https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/unnamed-2025-02-05T161806.861.webp)

我们现在准备好运行并测试我们的智能体系统了！

### 运行并测试我们的深度研究与报告撰写代理

让我们最终对我们的深度研究报告撰写代理进行测试！我们将创建一个简单的函数来实时流式传输进度，然后展示最终报告。一旦你有了一个能正常运行的代理，我建议关闭所有中间打印消息！

```python
from IPython.display import display
from rich.console import Console
from rich.markdown import Markdown as RichMarkdown

async def call_planner_agent(agent, prompt, config={"recursion_limit": 50}, verbose=False):
    events = agent.astream(
        {'topic' : prompt},
        config,
        stream_mode="values",
    )

    async for event in events:
        for k, v in event.items():
            if verbose:
                if k != "__end__":
                    display(RichMarkdown(repr(k) + ' -> ' + repr(v)))
            if k == 'final_report':
                print('='*50)
                print('Final Report:')
                md = RichMarkdown(v)
                display(md)
```

#### 测试运行

```csharp
topic = "Detailed report on how is NVIDIA winning the game against its competitors"
await call_planner_agent(agent=reporter_agent,
                         prompt=topic)
```

#### Output

```diff
--- Generating Report Plan ---
--- Generating Report Plan Completed ---
--- Generating Search Queries for Section: NVIDIA's Market Dominance in GPUs
 ------ Generating Search Queries for Section: Strategic Acquisitions and
 Partnerships ---
--- Generating Search Queries for Section: Technological Innovations and AI
 Leadership ---

--- Generating Search Queries for Section: Financial Performance and Growth
 Strategy ---
--- Generating Search Queries for Section: NVIDIA's Market Dominance in GPUs
 Completed ---
--- Searching Web for Queries ---
--- Generating Search Queries for Section: Financial Performance and Growth
 Strategy Completed ---
--- Searching Web for Queries ---
--- Generating Search Queries for Section: Technological Innovations and AI
 Leadership Completed ---
--- Searching Web for Queries ---
--- Generating Search Queries for Section: Strategic Acquisitions and
 Partnerships Completed ---
--- Searching Web for Queries ---
--- Searching Web for Queries Completed ---
--- Writing Section : Strategic Acquisitions and Partnerships ---
--- Searching Web for Queries Completed ---
--- Writing Section : Financial Performance and Growth Strategy ---
--- Searching Web for Queries Completed ---
--- Writing Section : NVIDIA's Market Dominance in GPUs ---
--- Searching Web for Queries Completed ---
--- Writing Section : Technological Innovations and AI Leadership ---
--- Writing Section : Strategic Acquisitions and Partnerships Completed ---
--- Writing Section : Financial Performance and Growth Strategy Completed ---
--- Writing Section : NVIDIA's Market Dominance in GPUs Completed ---
--- Writing Section : Technological Innovations and AI Leadership Completed ---
--- Formatting Completed Sections ---
--- Formatting Completed Sections is Done ---
--- Writing Final Section: Introduction ------ Writing Final Section:
 Conclusion ---

--- Writing Final Section: Introduction Completed ---
--- Writing Final Section: Conclusion Completed ---
--- Compiling Final Report ---
--- Compiling Final Report Done ---
==================================================
Final Report:
```
[查看全屏](https://www.analyticsvidhya.com/wp-content/plugins/pdfjs-viewer-shortcode/pdfjs/web/viewer.php?file=https://cdn.analyticsvidhya.com/wp-content/uploads/2025/02/nvidia_report.pdf&attachment_id=219818&dButton=true&pButton=true&oButton=false&sButton=true&pagemode=none&_wpnonce=43c3249032)

如上所示，它为我们给定的主题提供了一份相当全面、研究充分且结构良好的报告！

## 结论

如果你正在阅读这篇文章，我赞赏你在这本篇幅巨大的指南中坚持读到最后的努力！在这里我们看到，构建一个类似于 OpenAI 推出的成熟商业产品（而且价格不菲！）并不太难，OpenAI 这家公司绝对知道如何在生成式人工智能以及现在的智能体人工智能领域推出高质量的产品。

我们看到了一个关于如何构建我们自己的深度研究和报告生成智能 AI 系统的详细架构和工作流程，而且总体来说，运行这个系统，正如承诺的那样，花费不到一美元！如果你在所有事情上都使用开源组件，那它完全免费！此外，它完全可定制，你可以控制搜索的方式、报告的结构、长度和风格。请注意，如果你使用 Tavily，在运行这个深度研究智能体时很容易进行大量搜索，所以要注意并跟踪你的使用情况。这只是为你提供了一个构建基础，你可以自由使用这段代码和系统，对其进行定制并使其变得更好！