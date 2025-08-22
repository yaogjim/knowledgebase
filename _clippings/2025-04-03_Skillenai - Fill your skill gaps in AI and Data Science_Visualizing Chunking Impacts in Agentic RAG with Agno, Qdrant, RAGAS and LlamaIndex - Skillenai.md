---
title: "Visualizing Chunking Impacts in Agentic RAG with Agno, Qdrant, RAGAS and LlamaIndex - Skillenai"
source: "https://skillenai.com/competition-post/visualizing-chunking-impacts-in-agentic-rag-with-agno-qdrant-ragas-and-llamaindex/"
author:
  - "[[Skillenai - Fill your skill gaps in AI and Data Science]]"
published: 2025-03-28
created: 2025-04-03
description: "In the AI Agents world of Retrieval-Augmented Generation (Agentic-RAG), one challenge that persists is how Agents chunk our source documents to optimize response accuracy and relevance. This blog series dives into how different chunking strategies — Fixed, Semantic, Agentic, and Recursive Chunking— impact the performance of Agentic RAG systems. Using Agno for creating agent and orchestration and"
tags:
  - "clippings"
---
在检索增强生成（Agentic-RAG）的人工智能智能体领域，一个持续存在的挑战是智能体如何对我们的源文档进行分块，以优化响应的准确性和相关性。本博客系列深入探讨不同的分块策略——固定分块、语义分块、智能体分块和递归分块——如何影响 Agentic RAG 系统的性能。使用 `Agno` 进行智能体创建和编排，并将 `Qdrant` 用作向量存储，我们通过 `RAGAS` 和 `LlamaIndex` 评估分块效果，并通过基于指标的深入分析将结果可视化。这一探索不仅揭示了分块方法中的细微差别，还为在实际应用中优化检索管道奠定了基础。

![](https://i0.wp.com/skillenai.com/wp-content/uploads/2025/03/arch.png?resize=580%2C210&ssl=1)

#### 架构：

该架构始于 Agno 和 Qdrant 的集成，其中 `Agno` 促进代理式 RAG 工作流程， `Qdrant` 用作存储分块文档嵌入的向量数据库，在代理术语中也称为知识库。应用了多种分块策略——即固定、语义、代理和递归——每种策略都为输入文档提供不同的粒度和上下文重叠。然后，这些分块输入通过 Agno 的代理管道，以模拟真实世界的检索和推理设置。

下一阶段涉及 RAGAS 和 LlamaIndex，它们在评估中起着关键作用。 `RAGAS` 有助于创建一个黄金标准评估数据集，而 LlamaIndex 处理用于 RAGA 评估函数的LLM包装器。它们共同为每个分块策略生成诸如上下文召回率、忠实度和答案正确性等性能指标。最后，使用在 ReactJS 中创建的自定义仪表板将这些见解可视化，以比较不同策略如何影响智能体 RAG 系统的结果。此管道提供了一个全面的视角，以了解各种分块技术的权衡和效率。

#### 实施

智能检索增强生成（Agentic RAG）设置的项目结构如下所示。

```
.

├── agentic_chunk_benchmarking.py

├── create_eval_dataset.py

├── data

│   ├── ground_truth.json

│   └── test_data.pdf

├── fixed_chunk_benchmarking.py

├── recursive_chunk_benchmarking.py

├── requirements.txt

└── semantic_chunk_benchmarking.py
```

项目要求如下。

```
agno

python-dotenv

qdrant-client

anthropic

ollama

# pdf parser

pypdf

# chunking library

chonkie

# configuration

packaging

importlib-metadata

# evals

ragas

deepeval

# llama-index

llama-index

llama-index-llms-openai
```

包含安全凭证的环境文件如下。

```
collection_name=chunk_test

qdrant_url=http://localhost:6333

api_key=your key

ANTHROPIC_API_KEY=sk-ant-

OPENAI_API_KEY=sk-proj-
```

#### 固定分块策略

以下代码使用 RAGAS 评估框架评估一个检索增强生成（RAG）系统。它首先通过加载一个 PDF 文档来建立一个知识库，将其分块成片段，并将这些块存储在一个带有来自 Ollama 模型嵌入的 Qdrant 向量数据库中。该系统使用 Claude 3.7 Sonnet 作为语言模型，根据知识库回答查询。

```
import os

from create_eval_dataset import create_eval_ds

from agno.agent import Agent

from agno.document.chunking.fixed import FixedSizeChunking

from agno.embedder.ollama import OllamaEmbedder

from agno.models.anthropic import Claude

from qdrant_client import qdrant_client

from agno.knowledge.pdf import PDFKnowledgeBase

from agno.vectordb.qdrant import Qdrant

from dotenv import load_dotenv, find_dotenv

from ragas.llms import LlamaIndexLLMWrapper

from ragas import EvaluationDataset, evaluate

from ragas.metrics import Faithfulness, FactualCorrectness, ContextRelevance, ContextUtilization, ContextRecall

from llama_index.llms.openai import OpenAI

eval_llm = OpenAI(model='gpt-4o')

load_dotenv(find_dotenv())

doc_path = "data/test_data.pdf"

ground_truth_path = "data/ground_truth.json"

chunk_size = 1000

chunk_overlap = 200

# initialize the LLM (default to openai)

claude = Claude(id="claude-3-7-sonnet-20250219")

# initialize the qdrant client.

q_client = qdrant_client.QdrantClient(url=os.environ.get('qdrant_url'), api_key=os.environ.get('api_key'))

# create the qdrant vector store instance

vector_db = Qdrant(

    collection=os.environ.get('collection_name'),

    url=os.environ.get('qdrant_url'),

    api_key=os.environ.get('api_key'),

    embedder=OllamaEmbedder(id="nomic-embed-text:latest", dimensions=768)

)

# configure the knowledge base

knowledge_base = PDFKnowledgeBase(vector_db=vector_db,

                                  path=doc_path,

                                  chunking_strategy=FixedSizeChunking(

                                      chunk_size=chunk_size,

                                      overlap=chunk_overlap)

                                  )

if not q_client.collection_exists(collection_name=os.environ.get('collection_name')):

    knowledge_base.load(recreate=False)

# initialize agent

agent = Agent(knowledge=knowledge_base, search_knowledge=True, model=claude)

# create the dataset for evaluation

eval_dataset = create_eval_ds(agent=agent, ground_truth_path=ground_truth_path)

# trigger evals

evaluation_dataset = EvaluationDataset.from_list(eval_dataset)

evaluator_llm = LlamaIndexLLMWrapper(llm=eval_llm)

result = evaluate(dataset=evaluation_dataset, metrics=[Faithfulness(), ContextRelevance(),

                                                       ContextUtilization(), ContextRecall(),

                                                       FactualCorrectness()])

for score in result.scores:

    print(score)

# destroy the collection

if q_client.collection_exists(collection_name=os.environ.get('collection_name')):

    q_client.delete_collection(collection_name=os.environ.get('collection_name'))
```

评估过程首先从真实数据创建一个数据集，然后使用 GPT-4o 作为评估模型，以跨多个指标评估 RAG 系统的性能，这些指标包括忠实度、上下文相关性、上下文利用率、上下文召回率和事实正确性。这些指标衡量系统的回答与提供的上下文和事实准确性的匹配程度。

运行评估并打印每个指标的分数后，代码通过删除 Qdrant 集合进行清理。这个完整的流程展示了一个典型的 RAG 系统评估工作流程，其中文档知识被转换为向量嵌入，针对这些知识处理查询，并系统地衡量响应的质量。

#### 语义分块策略：

以下代码使用语义分块而非固定大小分块来评估一个 RAG 系统。它通过加载 PDF 文档 `splitting it into chunks based on semantic similarity with a threshold of 0.6` 来设置知识库，并使用 Ollama 嵌入将它们存储在 Qdrant 向量数据库中。该系统利用 Claude 3.5 Sonnet 作为其语言模型来处理针对知识库的查询。

```
import os

from agno.agent import Agent

from agno.document.chunking.semantic import SemanticChunking

from agno.embedder.ollama import OllamaEmbedder

from agno.models.anthropic import Claude

from qdrant_client import qdrant_client

from agno.knowledge.pdf import PDFKnowledgeBase

from agno.vectordb.qdrant import Qdrant

from dotenv import load_dotenv, find_dotenv

from ragas.llms import LlamaIndexLLMWrapper

from ragas import EvaluationDataset, evaluate

from ragas.metrics import Faithfulness, FactualCorrectness, ContextRelevance, ContextUtilization, ContextRecall

from llama_index.llms.openai import OpenAI

from create_eval_dataset import create_eval_ds

eval_llm = OpenAI(model='gpt-4o')

load_dotenv(find_dotenv())

doc_path = "data/test_data.pdf"

ground_truth_path = "data/ground_truth.json"

# initialize the LLM (default to openai)

claude = Claude(id="claude-3-5-sonnet-20241022")

# initialize the qdrant client.

q_client = qdrant_client.QdrantClient(url=os.environ.get('qdrant_url'), api_key=os.environ.get('api_key'))

# create the qdrant vector store instance

vector_db = Qdrant(

    collection=os.environ.get('collection_name'),

    url=os.environ.get('qdrant_url'),

    api_key=os.environ.get('api_key'),

    embedder=OllamaEmbedder(id="nomic-embed-text:latest", dimensions=768)

)

# configure the knowledge base

knowledge_base = PDFKnowledgeBase(vector_db=vector_db,

                                  path=doc_path,

                                  chunking_strategy=SemanticChunking(

                                      chunk_size=chunk_size,

                                      similarity_threshold=0.6)

                                  )

if not q_client.collection_exists(collection_name=os.environ.get('collection_name')):

    knowledge_base.load(recreate=False)

# initialize agent

agent = Agent(knowledge=knowledge_base,search_knowledge=True, model=claude)

# create the dataset for evaluation

eval_dataset = create_eval_ds(agent=agent, ground_truth_path=ground_truth_path)

evaluation_dataset = EvaluationDataset.from_list(eval_dataset)

evaluator_llm = LlamaIndexLLMWrapper(llm=eval_llm)

result = evaluate(dataset=evaluation_dataset, metrics=[Faithfulness(), ContextRelevance(),

                                                       ContextUtilization(), ContextRecall(),

                                                       FactualCorrectness()])

for score in result.scores:

    print(score)

# destroy the collection

if q_client.collection_exists(collection_name=os.environ.get('collection_name')):

    q_client.delete_collection(collection_name=os.environ.get('collection_name'))
```

评估工作流程从真实数据创建一个测试数据集，然后使用 GPT-4o 作为评估器，从忠实性、上下文相关性、上下文利用率、上下文召回率和事实正确性这五个指标对系统进行评估。这些指标全面衡量了系统的回答与所提供上下文的匹配程度以及保持事实准确性的情况。

在运行评估并打印每个指标的结果后，代码通过删除 Qdrant 集合进行清理。这展示了一个先进的 RAG 管道，该管道使用语义理解而非任意字符计数来确定文档块，有可能在保持相同严格评估方法的同时提高检索过程中的上下文相关性。

#### 代理分块策略：

以下代码评估一个 RAG 系统 `using agentic chunking, an advanced method that employs Claude 3.7 Sonnet to intelligently segment documents based on content understanding rather than arbitrary divisions` 。它处理一个 PDF 文档，并将分块存储在一个 Qdrant 向量数据库中，这些分块带有来自 Ollama 的 nomic-embed-text 模型的嵌入。该系统在分块过程和基于知识库回答查询时都使用相同的 Claude 模型。

```
import os

from agno.agent import Agent

from agno.document.chunking.agentic import AgenticChunking

from agno.embedder.ollama import OllamaEmbedder

from agno.models.anthropic import Claude

from qdrant_client import qdrant_client

from agno.knowledge.pdf import PDFKnowledgeBase

from agno.vectordb.qdrant import Qdrant

from dotenv import load_dotenv, find_dotenv

from ragas.llms import LlamaIndexLLMWrapper

from ragas import EvaluationDataset, evaluate

from ragas.metrics import Faithfulness, FactualCorrectness, ContextRelevance, ContextUtilization, ContextRecall

from llama_index.llms.openai import OpenAI

from create_eval_dataset import create_eval_ds

eval_llm = OpenAI(model='gpt-4o')

load_dotenv(find_dotenv())

doc_path = "data/test_data.pdf"

ground_truth_path = "data/ground_truth.json"

chunk_size = 1000

# initialize the LLM (default to openai)

claude = Claude(id="claude-3-7-sonnet-20250219")

# initialize the qdrant client.

q_client = qdrant_client.QdrantClient(url=os.environ.get('qdrant_url'), api_key=os.environ.get('api_key'))

# create the qdrant vector store instance

vector_db = Qdrant(

    collection=os.environ.get('collection_name'),

    url=os.environ.get('qdrant_url'),

    api_key=os.environ.get('api_key'),

    embedder=OllamaEmbedder(id="nomic-embed-text:latest", dimensions=768)

)

# configure the knowledge base

knowledge_base = PDFKnowledgeBase(vector_db=vector_db,

                                  path=doc_path,

                                  chunking_strategy=AgenticChunking(

                                      model=claude,

                                      max_chunk_size=chunk_size)

                                  )

if not q_client.collection_exists(collection_name=os.environ.get('collection_name')):

    knowledge_base.load(recreate=False)

# initialize agent

agent = Agent(knowledge=knowledge_base, search_knowledge=True, model=claude)

# create the dataset for evaluation

eval_dataset = create_eval_ds(agent=agent, ground_truth_path=ground_truth_path)

evaluation_dataset = EvaluationDataset.from_list(eval_dataset)

evaluator_llm = LlamaIndexLLMWrapper(llm=eval_llm)

result = evaluate(dataset=evaluation_dataset, metrics=[Faithfulness(), ContextRelevance(),

                                                       ContextUtilization(), ContextRecall(),

                                                       FactualCorrectness()])

for score in result.scores:

    print(score)

# destroy the collection

if q_client.collection_exists(collection_name=os.environ.get('collection_name')):

    q_client.delete_collection(collection_name=os.environ.get('collection_name'))
```

评估框架使用 RAGAS，并以 GPT-4o 作为评估模型，以五个关键指标评估系统的性能：忠实性、上下文相关性、上下文利用率、上下文召回率和事实正确性。这项全面评估考察了系统的回答与检索到的上下文的匹配程度以及保持事实准确性的情况。

在完成评估并输出分数后，代码通过删除 Qdrant 集合进行清理。此管道代表了一种复杂的 RAG 系统方法，该方法利用人工智能对文档分割做出明智决策，可能在确保块保持在最大 1000 个标记大小以下的同时，保持块中的语义连贯。

#### 递归分块策略：

以下代码评估一个 RAG 系统 `using recursive chunking, which hierarchically splits documents into progressively smaller segments based on document structure` 。它处理一个 PDF 文档，并将其分割成 1000 个标记的块，重叠 200 个标记，然后将这些块存储在一个 Qdrant 向量数据库中，并使用 Ollama 的 nomic-embed-text 模型生成嵌入。该系统使用 Claude 3.7 Sonnet 作为语言模型，利用这个知识库来回答查询。

```
import os

from agno.agent import Agent

from agno.document.chunking.recursive import RecursiveChunking

from agno.embedder.ollama import OllamaEmbedder

from agno.models.anthropic import Claude

from qdrant_client import qdrant_client

from agno.knowledge.pdf import PDFKnowledgeBase

from agno.vectordb.qdrant import Qdrant

from dotenv import load_dotenv, find_dotenv

from ragas.llms import LlamaIndexLLMWrapper

from ragas import EvaluationDataset, evaluate

from ragas.metrics import Faithfulness, FactualCorrectness, ContextRelevance, ContextUtilization, ContextRecall

from llama_index.llms.openai import OpenAI

from create_eval_dataset import create_eval_ds

eval_llm = OpenAI(model='gpt-4o')

load_dotenv(find_dotenv())

doc_path = "data/test_data.pdf"

ground_truth_path = "data/ground_truth.json"

chunk_size = 1000

chunk_overlap = 200

# initialize the LLM (default to openai)

claude = Claude(id="claude-3-7-sonnet-20250219")

# initialize the qdrant client.

q_client = qdrant_client.QdrantClient(url=os.environ.get('qdrant_url'), api_key=os.environ.get('api_key'))

# create the qdrant vector store instance

vector_db = Qdrant(

    collection=os.environ.get('collection_name'),

    url=os.environ.get('qdrant_url'),

    api_key=os.environ.get('api_key'),

    embedder=OllamaEmbedder(id="nomic-embed-text:latest", dimensions=768)

)

# configure the knowledge base

knowledge_base = PDFKnowledgeBase(vector_db=vector_db,

                                  path=doc_path,

                                  chunking_strategy=RecursiveChunking(

                                      chunk_size=chunk_size,

                                      overlap=chunk_overlap)

                                  )

if not q_client.collection_exists(collection_name=os.environ.get('collection_name')):

    knowledge_base.load(recreate=False)

# initialize agent

agent = Agent(knowledge=knowledge_base, search_knowledge=True, model=claude)

# create the dataset for evaluation

eval_dataset = create_eval_ds(agent=agent, ground_truth_path=ground_truth_path)

evaluation_dataset = EvaluationDataset.from_list(eval_dataset)

evaluator_llm = LlamaIndexLLMWrapper(llm=eval_llm)

result = evaluate(dataset=evaluation_dataset, metrics=[Faithfulness(), ContextRelevance(),

                                                       ContextUtilization(), ContextRecall(),

                                                       FactualCorrectness()])

for score in result.scores:

    print(score)

# destroy the collection

if q_client.collection_exists(collection_name=os.environ.get('collection_name')):

    q_client.delete_collection(collection_name=os.environ.get('collection_name'))
```

评估过程从真实数据创建一个测试数据集，然后使用 GPT-4o 作为评估器来评估五个关键指标：忠实度、上下文相关性、上下文利用率、上下文召回率和事实正确性。这些指标全面衡量系统的回答与所提供的上下文和事实准确性的匹配程度。

在评估并打印分数之后，代码通过删除 Qdrant 集合进行清理。这种方法利用递归分块保留分层文档结构的能力，在使用与先前实现中相同严格的方法评估系统时，通过保持章节、小节和段落之间的关系，有可能改进信息检索。

#### 创建评估数据集：

以下代码通过处理真实数据并将其与智能体生成的响应进行比较，创建了一个用于测试 RAG 系统的评估数据集。它读取一个包含问题和预期答案的 JSON 文件，然后遍历每个项目，将问题提交给智能体，并捕获其响应以及检索到的上下文文档。

对于每一对问答，该函数会构建一个响应对象，其中包含原始问题、真实参考答案、智能体的实际响应，以及智能体为生成答案而检索到的上下文集。这些上下文是从智能体响应中的参考元数据中提取的，有助于深入了解系统用于制定答案的文档。

```
import json

from time import sleep

test_data = []

def create_eval_ds(agent, ground_truth_path):

    with open(ground_truth_path, 'r') as f:

        data = json.load(f)

        for obj in data:

            print(f'question:{obj["question"]}')

            resp = {'user_input': obj["question"], 'reference': obj["answer"]}

            # trigger the agent

            response = agent.run(obj["question"], markdown=True)

            relevant_docs = []

            for reference in response.extra_data.references:

                relevant_docs.extend([item['content'] for item in reference.references])

            resp['retrieved_contexts'] = relevant_docs

            resp['response'] = response.content

            test_data.append(resp)

            sleep(60)

    return test_data
```

该函数在问题之间包含 60 秒的延迟，以防止速率限制或留出处理时间。生成的数据集被构建为一个字典列表，每个字典包含问题、参考答案、智能体响应和检索到的上下文，然后像 RAGAS 这样的评估框架可以使用这些数据来衡量 RAG 系统在各种指标上的性能。

#### 执行情况与结果：

一旦你运行，我们就会有由 ragas 和 LlamaIndex wrappen 为LLM提供支持的不同评估，以评估我们的评估数据集。下面显示了其中一个输出运行结果。

```
{'faithfulness': 1.0, 'nv_context_relevance': 1.0, 'context_utilization': 0.7408430916026282, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.46)}

{'faithfulness': 1.0, 'nv_context_relevance': 1.0, 'context_utilization': 0.46957671956889324, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.59)}

{'faithfulness': 1.0, 'nv_context_relevance': 1.0, 'context_utilization': 0.8333333332916666, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.25)}

{'faithfulness': 0.9411764705882353, 'nv_context_relevance': 1.0, 'context_utilization': 0.3652996309200647, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.0)}

{'faithfulness': 0.9047619047619048, 'nv_context_relevance': 1.0, 'context_utilization': 0.5833333333041666, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.9)}

{'faithfulness': 0.8, 'nv_context_relevance': 1.0, 'context_utilization': 0.249999999975, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.15)}

{'faithfulness': 1.0, 'nv_context_relevance': 1.0, 'context_utilization': 0.99999999998, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.7)}

{'faithfulness': 1.0, 'nv_context_relevance': 1.0, 'context_utilization': 0.5833333333041666, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.25)}

{'faithfulness': 0.9166666666666666, 'nv_context_relevance': 1.0, 'context_utilization': 0.9999999999, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.17)}

{'faithfulness': 0.9090909090909091, 'nv_context_relevance': 1.0, 'context_utilization': 0.8666666666377778, 'context_recall': 1.0, 'factual_correctness(mode=f1)': np.float64(0.31)}
```

![](https://i0.wp.com/skillenai.com/wp-content/uploads/2025/03/fig1.png?resize=580%2C638&ssl=1)

![](https://i0.wp.com/skillenai.com/wp-content/uploads/2025/03/fig2.png?resize=580%2C653&ssl=1)

![](https://i0.wp.com/skillenai.com/wp-content/uploads/2025/03/fig3.png?resize=580%2C651&ssl=1)

![](https://i0.wp.com/skillenai.com/wp-content/uploads/2025/03/fig4.png?resize=580%2C649&ssl=1)

![](https://i0.wp.com/skillenai.com/wp-content/uploads/2025/03/fig5.png?resize=580%2C429&ssl=1)

#### 接下来是什么？

我们将了解如何构建这些仪表板并将数据导入其中，以便我们能够看到不同实验的对比分析。

#### 为什么我们不使用 MlOps 平台？

我们当然可以使用 MlOps 平台，但它们本质上要先进得多，仅仅为了可视化性能数据，我们并不需要整个平台。但是，我们将在后续博客中专门介绍 MLOps 平台，特别是 Mlflow，看看我们如何在生成式人工智能项目中利用 Mlflow。

#### 结论：

我们对分块策略的评估表明，文档分割在所有 RAGAS 指标上都会对 RAG 系统性能产生重大影响。虽然固定大小分块提供了一个基线，但语义和智能方法通过尊重自然信息边界，能更好地保持上下文完整性。值得注意的是，使用 Claude 3.7 十四行诗的智能分块通过利用LLM对文档结构的理解，展现出卓越的上下文相关性和事实正确性，而递归分块在分层文档方面表现出色。这些发现强调，分块不仅仅是一个技术细节，而是一项基本的架构决策，应根据特定的文档类型和用例进行定制，以构建更准确、更可靠的 RAG 系统。