---
title: "2025-11-20_https_www_linkedin_com_in_victorialslocum_https_ww_返回博客列表_blog"
source: "https://weaviate.io/blog/elysia-agentic-rag"
author:
  - "[[@https://www.linkedin.com/in/victorialslocum/,https://www.linkedin.com/in/dannyjameswilliams/,https://www.linkedin.com/in/edwardschmuhl/]]"
published: 2025-11-20
created: 2025-11-20
description:
tags:
  - "#getting"
  - "#define"
  - "weaviate"
  - "elysia"
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

# [返回博客列表](blog)

[返回博客列表](/blog)

![Elysia: Building an end-to-end agentic RAG app](/assets/images/hero-8ea5c4230dc233c3105f8dccf5387ad5.png)

## 引言：什么是 Elysia？

在人工智能聊天机器人日益普及的今天，大多数仍受限于相同的桎梏：输入输出皆为文本。但若你的 AI 不仅能动态决定说什么，还能自主选择如何呈现呢？如果它能学习你的偏好，智能分类、标记并检索数据，同时将决策过程完全透明化呢？

欢迎了解 [Elysia](https://github.com/weaviate/elysia) ——我们开源的智能 RAG 框架，它从根本上重新思考了如何通过人工智能与数据互动。

Elysia 是一款基于决策树的智能代理系统，它能智能判断该使用哪些工具、已获得哪些结果、是否应继续执行流程或是否已完成目标。该系统不仅提供 **完整的前端界面** ，还支持通过 **pip 轻松安装** 的 **Python 软件包** 。

开箱即用，Elysia 应用可连接您的 [Weaviate 集群](https://console.weaviate.cloud/) 并执行智能搜索——仅根据用户的自然语言自动生成独特筛选条件和搜索参数——同时在前端动态展示结果。

整个项目完全开源，且以可定制化为设计核心。您可以直接使用它来高效搜索数据，也可以安装 Python 包，轻松创建工具，将 Elysia 应用于任何需要智能 AI 代理的场景。

 您的浏览器不支持视频标签。

## How Does It Work?

Elysia 采用现代化 Web 应用架构，配备功能完整的前端以实现响应式实时界面，后端基于 FastAPI 同时服务于 Web 界面和 API。核心逻辑采用纯 Python 编写——即我们称之为"血汗与泪水"的自定义逻辑——由 [DSPy](https://docs.weaviate.io/integrations/llm-agent-frameworks/dspy) 处理 LLM 交互，从而实现灵活且面向未来的实施方案。

我们致力于让 [入门体验](#getting-started) 尽可能简单——所有功能都集成在单个可通过 pip 安装的包中。若要将 Elysia 作为应用程序使用，您需要一个包含数据的 [Weaviate Cloud](https://console.weaviate.cloud/) 实例。通过 `pip install elysia-ai` 安装后，您既可以使用 `elysia start` 启动完整网页界面，也可以通过导入 Python 库并初始化树对象来进行程序化查询。

```bash
pip install elysia-ai
elysia start
```

要开始使用此 Web 应用程序，只需前往“设置”选项卡创建您的第一个配置，添加您的 Weaviate 集群详细信息以及您选择的模型提供商和密钥，为其命名并点击保存。然后，您可以转到“数据”选项卡分析您的集合，瞧！智能 RAG 功能即可使用。用户还可以创建多个配置，以便轻松在不同数据集群或模型提供商之间切换。

在这款精美的网络应用和易用的 Python 库背后，其实蕴含着相当复杂的技术架构。Elysia 设计的三大核心要素——可定制决策树架构、动态数据显示类型、以及 AI 数据分析与感知能力——它们的组合在 **任何其他** 开源智能体框架中都未曾出现过。

![Elysia architecture](/assets/images/architecture-diagram-58c560f782cadc2f190ca955dc06cffb.png)

## Elysia 的三大支柱

### 1\. 决策树与决策代理

Elysia 的核心在于其决策树架构。与那些在运行时可以调用所有可用工具的简单智能体平台不同，Elysia 预定义了一个由可能节点组成的网络，每个节点都对应一个特定操作。决策树中的每个节点都由一个具备全局环境感知能力的决策智能体进行协调，该智能体能够评估当前环境、可用操作、过往行动及未来可能采取的动作，从而制定出最优工具使用策略。

决策代理还会输出推理过程，这些信息将传递给后续代理，以便它们继续朝着同一目标努力。每个代理都能知晓先前代理的意图。

![Elysia decision tree simplified](/assets/images/decision-tree-d4e2dca43763dd0093c62994c7ab9e1c.png)

树状结构还支持高级错误处理机制和完成条件设定。例如，当智能体判定某项任务无法通过现有数据完成时，可在树状步骤中设置"不可能标志"。假设您询问电商数据集中裤装价格，但当前仅有珠宝数据集可用，智能体将识别这种数据不匹配的情况，并向决策树反馈任务无法执行。同样地，若 Elysia 进行查询后获得无关的搜索结果，这并不构成失败。返回决策树时，智能体可识别出应当采用不同搜索词或放宽筛选条件重新查询。

此外，当工具遇到错误时——可能是由于连接问题或生成查询中的拼写错误——这些错误会被捕获并沿决策树回传。决策代理随后可以智能选择是否通过修正重试，或完全尝试另一种方法。为防止无限循环，决策树的遍历次数设有硬性上限。

整个架构为开发者提供了极大的灵活性。用户可 [添加自定义工具](https://weaviate.github.io/elysia/creating_tools/) 与分支，使决策树能按需简繁伸缩。工具可配置为基于特定条件自动触发——例如当聊天上下文超过 5 万个标记时，摘要工具便会自动激活。其他工具可保持隐藏状态直至满足触发条件，仅在当前状态相关时才会作为选项显现。

实时可观测性是 Elysia 区别于其他黑盒 AI 系统的核心优势之一。前端界面会动态展示完整的决策树遍历过程，让您能实时观察 LLM 在处理查询时每个节点的推理逻辑。这种透明度帮助用户准确理解系统做出特定决策的原因，并在问题出现时及时修正。

![Elysia tree](/assets/images/elysiatree-ee194040ecca780f0268b56322afa3d2.png)

### 2\. 以动态格式展示数据源

当其他 AI 助手仅限于文本回复（或偶尔支持图文）时，Elysia 能够 **根据内容和语境智能选择数据呈现方式** 。该系统目前支持七种不同的展示格式：通用数据展示、表格、电商产品卡片、（GitHub）任务单、对话与消息、文档以及图表。

 您的浏览器不支持视频标签。

但 Elysia 如何知道该为你的特定数据使用哪种显示类型呢？

在使用任何 Weaviate 工具之前，Elysia 会先分析您的数据集。LLM 将通过抽样检查数据结构、验证字段、创建摘要并生成元数据。基于此分析，系统会从可用选项中推荐最合适的显示格式。用户也可手动调整这些显示映射，以更好地满足自身需求。

未来，我们还希望借助这一架构开发新功能，让不同显示界面支持不同的后续操作。酒店信息屏可能集成预订功能，Slack 对话显示界面可直接回复消息，商品卡片则能提供加入购物车功能。这将推动 Elysia 从被动信息检索工具向主动助手转型，帮助用户基于数据直接采取行动。

我们将持续增加更多显示类型，以提升可定制化程度，使 Elysia 能够适应几乎任何使用场景或行业特定需求。

### 3\. Elysia 是您数据的自动专家

像我们自家的 [Verba](https://github.com/weaviate/Verba) 这样的朴素 RAG 系统，在处理复杂数据、多种数据类型或位置、以及重复或相似数据时可能会举步维艰，因为 **它们无法全面把握所处环境的全貌** 。在目睹社区（包括我们自己😅）为此困扰后，我们认定这正是 Elysia 需要着力解决的核心问题之一。

如上所述，将 Weaviate 云实例连接至 Elysia 后，LLM 会分析您的数据集以检查数据结构、创建摘要、生成元数据并选择显示类型。这不仅是用户可见的有用信息，更显著提升了 Elysia 处理复杂查询和提供专业回答的能力。此能力正是先前如 Verba 等系统的短板——由于其盲目搜索方式，这类系统常因数据模糊性而失效。

生成元数据在处理树状结构中的复杂查询和任务时确实至关重要。我们见过的其他传统 RAG 和查询系统往往进行盲目的向量搜索，不了解所搜索数据的整体结构和含义，只能寄希望于获得相关结果。但借助 Elysia，我们构建的系统能够在执行查询等操作之前 **理解并考虑特定数据的结构和内容** 。

该网络平台还配备了一个功能全面的数据浏览器，支持 BM25 搜索、排序和筛选功能。它能自动对字段中的唯一值进行分组，并为数值数据提供最小/最大范围，让 Elysia 和用户都能清晰掌握可用数据情况。

数据总览面板提供了所有可用集合的高层概览，而集合探索器则支持对单个数据集进行详细检查。在查看表格数据时，我们为选定条目提供完整的对象视图，使庞大且嵌套的数据对象能以结构化、可读的格式呈现。此外，在元数据标签页内，用户可编辑 LLM 生成的元数据、显示类型和摘要——众所周知，LLM 的生成效果 *远非* 完美。

 您的浏览器不支持视频标签。

## 我们构建的其他炫酷功能

我们实施的反馈系统远不止简单的评分。每位用户都在自己的 Weaviate 实例中维护着一套专属的反馈案例库。当您发起查询时，Elysia 会首先通过向量相似度匹配，搜索您曾给予积极评价的类似历史查询记录。

![Feedback system in Elysia](/assets/images/feedback-system-fe57cc82d7fb26bc048c9a8e4019d63c.gif)

系统随后可以将这些正面示例作为 **少量样本示范** ，使较小模型也能产生更佳响应。如果您一直使用更庞大、更昂贵的模型处理复杂任务，并对输出结果给予正面评价，Elysia 就能将这些高质量响应作为范例，供更小更快的模型在处理类似查询时参考。长此以往，这既能降低成本、提升响应速度，又能持续保持输出质量。

将交互限制在单一用户内，可确保个人偏好不会干扰他人体验，同时保障数据安全。该功能通过简单的配置复选框即可启用，并在后台透明运行，仅根据您的交互持续优化整个系统。

### 按需分块：更智能的文档处理

传统的 RAG 系统会预先对所有文档进行分块处理，这可能会 *大幅* 增加存储需求。这也是我们观察到社区面临的另一个难题，因此我们提出的解决方案是 **在查询时进行分块** ，而非依赖预先分块策略。初始搜索使用文档级向量，能有效概括文档要点，但无法定位内部相关段落。当文档超过令牌阈值且与查询相关时，Elysia 会介入并动态进行分块处理。

系统将这些文本块存储在一个并行、量化的集合中，并交叉引用原始文档。这意味着后续对相似信息的查询可以利用先前已分块的内容，使系统随着时间的推移变得更加高效。这种方法在保持甚至提高检索质量的同时，降低了存储成本。

展望未来版本，这种架构还能支持灵活的文本分块策略。不同文档类型可采用不同分块方式——代码或许会按函数或类边界分块，而散文体内容则可能采用语义分块或简单的固定尺寸分块。

### 通过静态 HTML 提供前端服务

我们想要解决的另一个问题是如何在不启动后端 *和* 前端服务器的情况下提供 NextJS 前端服务。我们发现可以通过 FastAPI 将 Elysia 的前端作为静态 HTML 提供，从而无需单独的 Node.js 服务器。这一架构调整意味着所有功能都可以通过单个 Python 包运行，有助于简化部署流程并降低运维复杂度。只需简单的 pip 安装，就能获得一个完整的、生产就绪的应用程序，可在任何支持 Python 的环境中进行部署。是不是很酷？

### 多模型策略

除了反馈系统允许在小模型和大模型之间无损切换外，Elysia 还能智能地 **根据任务复杂度将不同任务路由至合适规模的模型** 。轻量化的小模型处理决策代理和简单任务，而更强大的大模型则留给需要深度推理的复杂工具操作。我们默认选用 Gemini 进行构建，因为它不仅性能卓越，还拥有超大上下文窗口、极快响应速度以及cost-effectiveness.功能。

然而，我们钟爱 Weaviate 生态系统和开发的主要原因之一，是始终能灵活选择各类服务商、工具和集成方案。因此，所有模型选择当然都支持通过配置文件完全自定义，兼容包括本地模型在内的几乎所有服务商。更进一步，用户还能为系统不同模块配置不同模型，根据具体的性能、安全、成本和延迟需求进行精准优化。

### Customize your blob

整个应用界面的个性化定制是我们未来版本将持续开发的功能之一，但目前您可以通过自定义专属的 Elysia 数据块来提前体验——这些个性化设置将持久保存在您的应用中！未来，这些定制功能将支持用户重新塑造 Elysia 的品牌形象，使其更贴合企业自身特色。

 您的浏览器不支持视频标签。

## The Technical Stack

Elysia 的技术栈相对简洁。其检索功能完全由 Weaviate 驱动——通过智能体构建定制化查询与聚合方案，同时利用 Weaviate 的高速向量搜索快速检索相似历史对话并存储会话记录。此外，我们采用 DSPy、NextJS、FastAPI 框架，并以 Gemini 作为核心测试模型。

Weaviate 提供了构建稳健应用所需的全部功能，例如 [命名向量](https://docs.weaviate.io/weaviate/manage-collections/vector-config#define-named-vectors) 、多种 [搜索类型](https://docs.weaviate.io/weaviate/search) （向量搜索、关键词搜索、混合搜索、聚合搜索）以及 [过滤器](https://docs.weaviate.io/weaviate/search/filters) 。其对 [交叉引用](https://docs.weaviate.io/weaviate/manage-collections/cross-references) 的原生支持是按需分块功能的基础，使得 Elysia 能够维护原始文档与其动态生成片段之间的关联关系。Weaviate 的 [量化选项](https://docs.weaviate.io/weaviate/configuration/compression) 在 Alpha 测试阶段发布时有效帮助我们管理数据存储成本，而云集合设置让我们能够轻松存储生成的元数据和用户信息。

DSPy 充当 LLM 交互层。团队（准确说是我们的后端魔法师 Danny）选择 DSPy 是因为它提供了一个灵活且面向未来的语言模型操作框架。除了基础的提示管理功能，DSPy 还能轻松实现小样本学习——这正是 Elysia 反馈系统的核心驱动力。该框架还支持提示优化功能，未来版本可能会集成这项能力。

但是，Elysia 的核心逻辑是用纯 Python（以及血汗与泪水）编写的。这样做让我们对实现拥有完全控制权，并将所需工具保持在最低限度。虽然 pip 安装确实会引入 DSPy 和其他库的（大量）依赖，但 Elysia 的核心逻辑（在我们看来）是精简且易于理解的。

## 现实案例：为 Glowe 聊天功能提供动力

为了验证 Elysia 是否能如我们所愿成为灵活的智能体框架，我们决定将其应用于 AI 美妆电商应用 [Glowe](/blog/glowe-app) 的聊天界面中。

![Glowe built with Elysia](/assets/images/glowe-elysia-752f28b4348ea99f20a0a62c5abc2699.png)

针对 Glowe-Elysia 项目，我们专门定制了三款工具以满足应用需求：

1.  一款用于通过复杂筛选条件查找合适产品的查询代理工具（由 [Weaviate 查询代理](https://docs.weaviate.io/agents/query) 提供支持）
2.  一款通过自然语言为用户生成专属产品组合的堆栈生成工具
3.  一款基于当前情境与用户个性化需求提供推荐的相关产品工具

Elysia 内置了所有复杂功能——文本响应、递归、自愈、错误处理和流式传输。我们可以完全专注于实现应用特有的逻辑，而无需构建枯燥的 AI 基础设施。

## Getting Started

上手 Elysia 只需极简配置。以下是分步指南：

### Web app

**第一步：安装依赖并启动应用**

运行以下命令启动网页界面

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install elysia-ai
elysia start
```

**第二步：获取数据**

如果您还没有一个包含数据的 Weaviate Cloud 集群，请前往 [Weaviate Cloud 控制台](https://console.weaviate.cloud/) 并 [创建一个免费的沙盒集群](https://docs.weaviate.io/cloud/quickstart#11-create-a-cluster) 。

随后，您可以通过 [快速入门教程](https://docs.weaviate.io/weaviate/quickstart) 向集群添加数据，或者将这段提示词复制到您常用的氛围编程 LLM 聊天工具中。

````markdown
You are helping a user create a custom Python script to import their data into Weaviate. Follow these steps exactly and **DO NOT modify any code except where explicitly marked with `# LLM TODO:`**.

## Step 1: Gather Requirements and Setup Environment

Ask the user to provide the following information AND complete the environment setup:

### Part A: Requirements

1. **Embedding Model Provider**: What embedding model provider would you like to use?
 - Available options: [https://docs.weaviate.io/weaviate/model-providers](https://docs.weaviate.io/weaviate/model-providers)
 - If unsure, recommend `text2vec-weaviate` (built-in, no API key required)
2. **Data Location**: Where is your data located?
 - Local file path (e.g., `/path/to/data.json`)
 - URL endpoint
 - Other source
3. **Data Schema**: Please provide an example object from your data. This will be used to define the property schema.
 - Example: `{"title": "Sample Title", "content": "Sample content text", "category": "example"}`

### Part B: Environment Setup

Please also complete this setup:

**Create Environment File**
Create a `.env` file in your project directory with these variables:

```
WEAVIATE_URL=
WEAVIATE_API_KEY=
EMBEDDINGS_PROVIDER_API_KEY=

```

**Setup Instructions:**

- Sign up for a free Weaviate Cloud account: [https://console.weaviate.cloud/](https://console.weaviate.cloud/)
- Create a free Sandbox cluster
- Copy your cluster URL and API key to the `.env` file
- If using `text2vec-weaviate`, leave `EMBEDDINGS_PROVIDER_API_KEY` empty
- If using another provider, add your API key for that provider

**WAIT for the user's response to Part A and confirmation that they have completed Part B before proceeding to Step 2.**

## Step 2: Virtual Environment Setup

Check if the user has a virtual environment. If not, instruct them to create one:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate

```

## Step 3: Install Dependencies

Install required packages:

```bash
pip install -U weaviate-client python-dotenv

```

## Step 4: Generate Custom Import Script

Create a file called `import_data.py` with the following code. **CRITICAL: Only modify sections marked with `# LLM TODO:`**

```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType, Tokenization
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_API_KEY"]
embeddings_provider_api_key = os.environ.get("EMBEDDINGS_PROVIDER_API_KEY", "")

# Connect to Weaviate Cloud
if embeddings_provider_api_key:
 client = weaviate.connect_to_weaviate_cloud(
 cluster_url=weaviate_url,
 auth_credentials=Auth.api_key(weaviate_api_key),
 headers={"X-xx-Api-Key": embeddings_provider_api_key}  # LLM TODO: Replace 'xx' with correct provider header name (e.g., "X-OpenAI-Api-Key", "X-Cohere-Api-Key")
 )
else:
 client = weaviate.connect_to_weaviate_cloud(
 cluster_url=weaviate_url,
 auth_credentials=Auth.api_key(weaviate_api_key)
 )

print(f"Weaviate client ready: {client.is_ready()}")  # Should print: True

# Create collection
collection = client.collections.create(
 name="YourCollectionName",  # LLM TODO: Replace with appropriate collection name based on user's data
 vector_config=[
 Configure.Vectors.text2vec_weaviate(  # LLM TODO: Replace with user's chosen provider (e.g., text2vec_openai, text2vec_cohere)
 name="default",
 source_properties=["property1", "property2"],  # LLM TODO: Set source properties for vectorization based on user's data schema
 ),
 ],
 properties=[
 # LLM TODO: Define properties based on user's example data
 # Example:
 # Property(name="title", data_type=DataType.TEXT),
 # Property(name="content", data_type=DataType.TEXT),
 # Property(name="category", data_type=DataType.TEXT, skip_vectorization=True),
 ]
)

# LLM TODO: Load data based on user's specified location
# For local JSON file:
# with open("FILE_PATH", "r") as f:
# data = json.load(f)

# For URL endpoint (note make sure to pip install and import requests library:
# response = requests.get("YOUR_URL")
# data = response.json()

# For other formats, adjust accordingly

# Import data in batches
with collection.batch.fixed_size(batch_size=200) as batch:
 for i, item in enumerate(data):
 batch.add_object({
 # LLM TODO: Map user's data properties to collection schema
 # Example:
 # "title": item["title"],
 # "content": item["content"],
 # "category": item["category"],
 })

 if batch.number_errors > 10:
 print("Batch import stopped due to excessive errors.")
 break

 # Progress indicator
 if i % 100 == 0:
 print(f"Imported {i} objects...")

# Check for import errors
failed_objects = collection.batch.failed_objects
if failed_objects:
 print(f"Number of failed imports: {len(failed_objects)}")
 print(f"First failed object: {failed_objects[0]}")
else:
 print("All objects imported successfully!")

print(f"Total objects in collection: {collection.aggregate.over_all(total_count=True).total_count}")

client.close()

### LLM TODO Instructions Summary:

1. **Line with headers**: Replace 'xx' in header name with correct provider (only if not using text2vec-weaviate)
2. **Collection name**: Choose appropriate name based on user's data type
3. **Vector config**: Replace with user's chosen embedding provider
4. **Source properties**: Set which properties should be vectorized
5. **Properties schema**: Define all properties from user's example data
6. **Data loading**: Implement correct data loading method based on user's data location
7. **Object mapping**: Map user's data fields to the defined schema

## Step 5: Error Handling

If there are any errors during execution:

1. First consult the Weaviate documentation: [https://docs.weaviate.io/weaviate/quickstart](https://docs.weaviate.io/weaviate/quickstart)
2. Check the specific error message and troubleshoot accordingly
3. Verify the `.env` file is properly configured
4. Ensure the data schema matches the actual data structure

## Step 6: Execute the Script

Run the import script:

```bash
python import_data.py

```

Upon successful completion, inform the user that their data has been imported to Weaviate and provide next steps for querying their data.

---

## Important Reminders:

- **Only modify code sections marked with `# LLM TODO:`**
- **Wait for user responses at Steps 1 and 2**
- **If using `text2vec-weaviate`, no external API key is needed**
- **Preserve all existing code structure and imports**
````

**第三步：添加配置设置**

在配置编辑器中，您可以添加 Weaviate 集群 URL 和 API 密钥，并设置模型及模型提供商的 API 密钥。您还可以创建多个配置，以便轻松切换数据集群或模型提供商。

![Elysia app config](/assets/images/config-7c9fcdd9bdcfde92c4235ad4f5cd169b.png)

在左侧菜单栏中，你还可以 [定制专属的 blob 形象](#customize-your-blob) ！

**第四步：分析数据**

在左侧菜单栏的 `数据` 选项卡下，您可以分析数据集，系统将提示 LLM 生成属性描述、数据集摘要、示例查询，并为每个数据集选择显示类型。

点击数据源时，您可以查看集合中的所有项目并编辑任意元数据，包括选择其他显示类型或配置属性映射。

**第五步：开始对话**

是时候开始提问了！前往 `聊天` 标签页创建新对话，与您的数据互动。若想查看决策树，请点击聊天视图左上角的绿色按钮切换至树状视图，将鼠标悬停在任意节点上即可查看节点描述、LLM 指令及其推理过程。每个新用户查询都会在此视图中生成新的决策树。

![Elysia app chat](/assets/images/chat-0d78666bb863b8ae6afe1c2ab21ef06e.png)

设置也可在每次对话级别进行配置。您可以添加更详细的智能体指令，或调整模型设置。

### As a Python Library

只需安装：

```bash
pip install elysia-ai
```

然后在 Python 中，使用 Elysia 就像这样简单：

```python
from elysia import tree, preprocess
preprocess("<your_collection_name>")

tree = Tree()
tree("What is Elysia?")
```

使用 Elysia 需要访问 LLMs 和您的 Weaviate 云详细信息，这些信息可在本地环境文件中设置或直接在 Python 中配置。 [完整文档](https://weaviate.github.io/elysia/) 提供了详细的配置选项和示例。

## What's Next?

我们还在酝酿中 🧑🍳

我们已规划并正在开发多项功能，包括类似 Verba 的自定义主题系统，让用户能将 Elysia 的界面风格与自身品牌调性相匹配。至于更多惊喜，还请拭目以待👀

## 结论：智能 RAG 的未来图景

Elysia 不仅仅是一个 RAG 实现方案——我们构建它是为了展示 AI 应用的创新可能。通过融合透明的智能体决策机制、动态可视化界面，以及持续进化的个性化优化系统，我们正在打造一款能真正理解用户意图的 AI 助手。它不仅能听懂你的问题，更懂得如何以最有效的方式呈现答案。

Elysia 将逐步取代我们最初的 RAG 应用 Verba，成为我们以向量数据库为核心开发尖端应用的下一阶段。我们已突破简单的问答-检索-生成流程，构建起一套能开发复杂智能体化 AI 应用的基础架构，同时确保开发者与用户体验始终简洁直观。

无论您是在构建电商聊天机器人、企业内部知识专家，还是开发全新应用，Elysia 都能为超越文本生成的 AI 体验奠定基础。我们迫不及待想见证您的创造！

那么，准备好开始了吗？访问 [演示](https://elysia.weaviate.io/) ，查看 [GitHub 代码仓库](https://github.com/weaviate/elysia) ，或深入 [文档](https://weaviate.github.io/elysia/) 开始构建。

![Team picture](/assets/images/team-0b5603b7887d27a520cf7f88a3b8ae35.png)

* * *

## 准备好开始构建了吗？

查看 [快速入门教程](https://docs.weaviate.io/weaviate/quickstart) ，或通过 [Weaviate Cloud (WCD)](https://console.weaviate.cloud/) 免费试用构建惊艳应用。