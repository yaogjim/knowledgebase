---
title: "Build a powerful RAG workflow using LangGraph and Elasticsearch"
source: "https://www.elastic.co/search-labs/blog/build-rag-workflow-langgraph-elasticsearch"
author:
  - "[[Elasticsearch Labs]]"
published: 2025-04-23
created: 2025-06-26
description: "In this blog, we will show you how to configure and customize the LangGraph Retrieval Agent Template with Elasticsearch to build a powerful RAG workflow for efficient data retrieval and AI-driven responses."
tags:
  - "clippings"
---
Elasticsearch 与行业领先的生成式人工智能工具和供应商有原生集成。查看我们关于超越 RAG 基础，或构建可用于生产的应用程序——弹性向量数据库的网络研讨会。

要为您的用例构建最佳搜索解决方案，立即开始免费云试用或在本地机器上试用 Elastic。

LangGraph 检索代理模板是 LangChain 开发的一个入门项目，用于在 LangGraph Studio 中使用 LangGraph 创建基于检索的问答系统。此模板已预先配置，可与 Elasticsearch 无缝集成，使开发人员能够快速构建可高效索引和检索文档的代理。

本博客重点介绍如何使用 LangGraph Studio 和 LangGraph CLI 运行和定制 LangChain 检索代理模板。该模板提供了一个构建检索增强生成（RAG）应用程序的框架，利用了诸如 Elasticsearch 等各种检索后端。

我们将引导您完成设置、配置环境，并在自定义代理流程时与 Elastic 一起高效地执行模板。

## 前提条件

在继续之前，请确保你已安装以下内容：

- Elasticsearch 云部署或本地 Elasticsearch 部署（或在 Elastic Cloud 上创建 14 天免费试用版） - 版本 8.0.0 或更高
- Python 3.9 及以上版本
- 访问诸如 Cohere（本指南中使用）、OpenAI 或 Anthropic/Claude 等 LLM 提供商

## 创建 LangGraph 应用程序

### 1\. 安装 LangGraph 命令行界面

```sh
pip install --upgrade "langgraph-cli[inmem]"
```

### 2\. 从检索代理模板创建 LangGraph 应用程序

```sh
mkdir lg-agent-demo
cd lg-agent-demo
langgraph new lg-agent-demo
```

您将看到一个交互式菜单，可让您从可用模板列表中进行选择。选择 4 代表检索代理，选择 1 代表 Python，如下所示：

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2F6a41a41f95c2477c67810adc7be46d91faf06878-1600x407.png&w=3840&q=75)

- 故障排除：如果你遇到错误“urllib.error.URLError: <urlopen error \[SSL: CERTIFICATE\_VERIFY\_FAILED\] certificate verify failed: unable to get local issuer certificate (\_ssl.c:1000)> ”

请运行 Python 的安装证书命令来解决该问题，如下所示。

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2F83ec238136c41738457299fd42c83aff32eb5b97-1407x75.png&w=3840&q=75)

### 3\. 安装依赖项

在新的 LangGraph 应用程序的根目录中，创建一个虚拟环境，并以 `edit` 模式安装依赖项，以便服务器使用你的本地更改：

```sh
#For Mac
python3 -m venv lg-demo
source lg-demo/bin/activate 
pip install -e .

#For Windows
python3 -m venv lg-demo
lg-demo\Scripts\activate 
pip install -e .
```

## 设置环境

### 1\. 创建一个.env 文件

`.env` 文件保存 API 密钥和配置，以便应用程序可以连接到你选择的 LLM 和检索提供程序。通过复制示例配置生成一个新的 `.env` 文件：

```sh
cp .env.example .env
```

### 2\. 配置. env 文件

`.env` 文件附带一组默认配置。你可以根据自己的设置添加必要的 API 密钥和值来更新它。任何与你的用例无关的密钥可以保持不变或删除。

```python
# To separate your traces from other applications
LANGSMITH_PROJECT=retrieval-agent

# LLM choice (set the API key for your selected provider):
ANTHROPIC_API_KEY=your_anthropic_api_key
FIREWORKS_API_KEY=your_fireworks_api_key
OPENAI_API_KEY=your_openai_api_key

# Retrieval provider (configure based on your chosen service):

## Elastic Cloud:
ELASTICSEARCH_URL=https://your_elastic_cloud_url
ELASTICSEARCH_API_KEY=your_elastic_api_key

## Elastic Local:
ELASTICSEARCH_URL=http://host.docker.internal:9200
ELASTICSEARCH_USER=elastic
ELASTICSEARCH_PASSWORD=changeme

## Pinecone:
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name

## MongoDB Atlas:
MONGODB_URI=your_mongodb_connection_string

# Cohere API key:
COHERE_API_KEY=your_cohere_api_key
```

- 示例 `.env` 文件（使用 Elastic Cloud 和 Cohere）

以下是一个示例 `.env` 配置，用于将 Elastic Cloud 用作检索提供程序，并将 Cohere 用作 LLM，如本博客中所示：

```python
# To separate your traces from other applications
LANGSMITH_PROJECT=retrieval-agent
#Retrieval Provider
# Elasticsearch configuration
ELASTICSEARCH_URL=elastic-url:443
ELASTICSEARCH_API_KEY=elastic_api_key
# Cohere API key
COHERE_API_KEY=cohere_api_key
```

*注意：虽然本指南在响应生成和嵌入方面都使用了 Cohere，但你可以根据自己的用例自由使用其他 LLM 提供商，如 OpenAI、Claude，甚至是本地 LLM 模型。确保你打算使用的每个密钥都在 `.env` 文件中存在且设置正确。*

### 3\. 更新配置文件 - configuration.py

在用适当的 API 密钥设置好你的 `.env` 文件后，下一步是更新应用程序的默认模型配置。更新配置可确保系统使用你在 `.env` 文件中指定的服务和模型。

导航到配置文件：

```sh
cd src/retrieval_graph
```

`configuration.py` 文件包含检索代理用于三个主要任务的默认模型设置：

- 嵌入模型 - 将文档转换为向量表示形式
- 查询模型 - 将用户的查询处理为向量
- 响应模型 – 生成最终响应

默认情况下，代码使用来自 OpenAI（例如， `openai/text-embedding-3-small` ）和 Anthropic（例如， `anthropic/claude-3-5-sonnet-20240620 and anthropic/claude-3-haiku-20240307` ）的模型。  
  
在本博客中，我们将改用 Cohere 模型。如果您已经在使用 OpenAI 或 Anthropic，则无需进行更改。

#### 示例更改（使用 Cohere）：

打开 `configuration.py` 并按如下所示修改模型默认设置：

```python
…
 embedding_model: Annotated[
       str,
       {"__template_metadata__": {"kind": "embeddings"}},
   ] = field(
       default="cohere/embed-english-v3.0",
…
response_model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
       default="cohere/command-r-08-2024",
…
query_model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
       default="cohere/command-r-08-2024",
       metadata={
```

## 使用 LangGraph CLI 运行检索代理

### 1\. 启动 LangGraph 服务器

```sh
cd lg-agent-demo
langgraph dev
```

这将在本地启动 LangGraph API 服务器。如果运行成功，你应该会看到类似这样的内容：

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2Fe3c3344b24651067e2d0892d870feca505b3be35-1494x542.png&w=3840&q=75)

打开 Studio 用户界面网址。

有两种可用的图：

- 检索图：从 Elasticsearch 检索数据，并使用 LLM 响应查询。
- 索引器图：将文档索引到 Elasticsearch 中，并使用 LLM 生成嵌入向量。

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2F99b579ca44b2d13f61da7e1de5886ea5b9a5e16f-1600x1009.png&w=3840&q=75)

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2Ff54d182d2789b6a4d113b0c88063531ea0b6de5d-1600x1009.png&w=3840&q=75)

### 2\. 配置索引器图

- 打开索引器图。
- 点击管理助手。
	- 点击“添加新助手”，按指定输入用户详细信息，然后关闭窗口。

```json
{"user_id": "101"}
```

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2F6f87958e40760ac9671639f4995962bcea090991-1600x1139.png&w=3840&q=75)

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2F8f802f6b65b3f06d7d1a521c3f40385c6006413b-1422x1212.png&w=3840&q=75)

### 3\. 索引示例文档

- 为以下示例文档建立索引，这些文档代表了 NoveTech 组织的一份假设性季度报告：

```json
[
  {    "page_content": "NoveTech Solutions Q1 2025 Report - Revenue: $120.5M, Net Profit: $18.2M, EPS: $2.15. Strong AI software launch and $50M government contract secured."
  },
  {
  },
  {
    "page_content": "NoveTech Solutions Financial Overview - Operating expenses at $85.3M, Gross Margin 29.3%. Stock price rose from $72.5 to $78.3. Market Cap reached $5.2B."
  },
  {
    "page_content": "NoveTech Solutions Challenges - Rising supply chain costs impacting hardware production. Regulatory delays slowing European expansion. Competitive pressure in cybersecurity sector."
  },
  {
    "page_content": "NoveTech Solutions Future Outlook - Expected revenue for Q2 2025: $135M. New AI chatbot and blockchain security platform launch planned. Expansion into Latin America."
  },
  {
    "page_content": "NoveTech Solutions Market Performance - Year-over-Year growth at 12.7%. Stock price increase reflects investor confidence. Cybersecurity and AI sectors remain competitive."
  },
  {
  },
  {
    "page_content": "NoveTech Solutions CEO Statement - 'NoveTech Solutions continues to innovate in AI and cybersecurity. Our growth strategy remains strong, and we foresee steady expansion in the coming quarters.'"
  }
]
```

文档索引完成后，你将在线程中看到一条删除消息，如下所示。

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2Ffd3a1efd64cb54d54ea56ef5055249dd066d5708-1600x854.png&w=3840&q=75)

### 4\. 运行检索图

- 切换到检索图。
- 输入以下搜索查询：

```sh
What was NovaTech Solutions total revenue in Q1 2025?
```

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2Feb4d8ddfe0effd7e1868fba921b8ef13f7baf27a-1600x755.png&w=3840&q=75)

系统将根据索引数据返回相关文档并提供准确答案。

## 自定义检索代理

为了提升用户体验，我们在检索图中引入了一个定制步骤，以预测用户接下来可能会问的三个问题。此预测基于：

- 从检索到的文档中提取的上下文
- 先前的用户交互
- 上次用户查询

要实现查询预测功能，需要进行以下代码更改：

### 1\. 更新 graph.py

- 添加 `predict_query` 函数：

```python
async def predict_query(
   state: State, *, config: RunnableConfig
) -> dict[str, list[BaseMessage]]:
   logger.info(f"predict_query predict_querypredict_query predict_query predict_query predict_query")  # Log the query

   configuration = Configuration.from_runnable_config(config)
   prompt = ChatPromptTemplate.from_messages(
       [
           ("system", configuration.predict_next_question_prompt),
           ("placeholder", "{messages}"),
       ]
   )
   model = load_chat_model(configuration.response_model)
   user_query = state.queries[-1] if state.queries else "No prior query available"
   logger.info(f"user_query: {user_query}")
   logger.info(f"statemessage: {state.messages}")
   #human_messages = [msg for msg in state.message if isinstance(msg, HumanMessage)]

   message_value = await prompt.ainvoke(
       {
           "messages": state.messages,
           "user_query": user_query,  # Use the most recent query as primary input
           "system_time": datetime.now(tz=timezone.utc).isoformat(),
       },
       config,
   )

   next_question = await model.ainvoke(message_value, config)
   return {"next_question": [next_question]}
```

- 修改 `respond` 函数以返回 `response` 对象，而不是消息：

```python
async def respond(
   state: State, *, config: RunnableConfig
) -> dict[str, list[BaseMessage]]:
   """Call the LLM powering our "agent"."""
   configuration = Configuration.from_runnable_config(config)
   # Feel free to customize the prompt, model, and other logic!
   prompt = ChatPromptTemplate.from_messages(
       [
           ("system", configuration.response_system_prompt),
           ("placeholder", "{messages}"),
       ]
   )
   model = load_chat_model(configuration.response_model)

   retrieved_docs = format_docs(state.retrieved_docs)
   message_value = await prompt.ainvoke(
       {
           "messages": state.messages,
           "retrieved_docs": retrieved_docs,
           "system_time": datetime.now(tz=timezone.utc).isoformat(),
       },
       config,
   )
   response = await model.ainvoke(message_value, config)
   # We return a list, because this will get added to the existing list
   return {"response": [response]}
```

- 更新图结构以添加用于 predict\_query 的新节点和边：

```python
builder.add_node(generate_query)
builder.add_node(retrieve)
builder.add_node(respond)
builder.add_node(predict_query)
builder.add_edge("__start__", "generate_query")
builder.add_edge("generate_query", "retrieve")
builder.add_edge("retrieve", "respond")
builder.add_edge("respond", "predict_query")
```

### 2\. 更新 prompts.py

- 在 `prompts.py` 中为查询预测精心设计提示：

```python
PREDICT_NEXT_QUESTION_PROMPT = """Given the user query and the retrieved documents, suggest the most likely next question the user might ask.

**Context:**
- Previous Queries:
{previous_queries}

- Latest User Query: {user_query}

- Retrieved Documents:
{retrieved_docs}

**Guidelines:**
1. Do not suggest a question that has already been asked in previous queries.
2. Consider the retrieved documents when predicting the next logical question.
3. If the user's query is already fully answered, suggest a relevant follow-up question.
4. Keep the suggested question natural and conversational.
5. Suggest at least 3 question

System time: {system_time}"""
```

### 3\. 更新 configuration.py

- 添加 `predict_next_question_prompt` ：

### 4\. 更新 state.py

- 添加以下属性：

```python
response: Annotated[Sequence[AnyMessage], add_messages]
next_question : Annotated[Sequence[AnyMessage], add_messages]
```

### 5\. 重新运行检索图

- 再次输入以下搜索查询：

```sh
What was NovaTech Solutions total revenue in Q1 2025?
```

系统将处理输入并预测用户可能会问的三个相关问题，如下所示。

![](https://www.elastic.co/search-labs/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fme0ej585%2Fsearch-labs-import-testing%2F70e855a2e4edc0ba5a147588df0de30eb081d053-1600x777.png&w=3840&q=75)

## 结论

在 LangGraph Studio 和 CLI 中集成检索代理模板有几个关键好处：

- 加速开发：模板和可视化工具简化了检索工作流程的创建和调试，减少了开发时间。
- 无缝部署：对 API 的内置支持和自动缩放功能可确保在各个环境中顺利部署。
- 轻松更新：修改工作流程、添加新功能以及集成其他节点都很简单，这使得扩展和增强检索过程变得更加容易。
- 持久内存：系统保留代理状态和知识，提高一致性和可靠性。
- 灵活的工作流建模：开发人员可以针对特定用例自定义检索逻辑和通信规则。
- 实时交互与调试：与正在运行的智能体进行交互的能力有助于高效测试和解决问题。

通过利用这些功能，组织可以构建强大、高效且可扩展的检索系统，从而提高数据可访问性和用户体验。

该项目的完整源代码可在 GitHub 上获取。
