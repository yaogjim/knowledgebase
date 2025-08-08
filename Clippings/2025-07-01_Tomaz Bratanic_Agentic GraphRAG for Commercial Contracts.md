---
title: "Agentic GraphRAG for Commercial Contracts"
source: "https://towardsdatascience.com/agentic-graphrag-for-commercial-contracts/"
author:
  - "[[Tomaz Bratanic]]"
published: 2025-04-03
created: 2025-07-01
description: "Structuring legal information as a knowledge graph to increase the answer accuracy using a LangGraph agent"
tags:
  - "clippings"
---
在每一项业务中，法律合同都是基础性文件，它定义了各方之间的关系、义务和责任。无论是合伙协议、保密协议还是供应商合同，这些文件通常都包含推动决策、风险管理和合规所需的关键信息。然而，解读并从这些合同中提取见解可能是一个复杂且耗时的过程。

在这篇文章中，我们将探讨如何通过使用 Agentic GraphRAG 实现一个端到端的解决方案，来简化理解和处理法律合同的流程。我将 GraphRAG 视为一个统称，用于指代任何从知识图谱中存储的信息进行检索或推理的方法，从而实现更结构化和上下文感知的响应。

通过将法律合同构建到 Neo4j 中的知识图谱中，我们可以创建一个强大的信息库，便于查询和分析。在此基础上，我们将构建一个 LangGraph 智能体，使用户能够就合同提出特定问题，从而能够快速发现新的见解。

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/image-18.png)

代码可在这个 [GitHub 仓库](https://github.com/tomasonjo-labs/legal-tech-chat) 中获取。

### 为什么数据结构化很重要

某些领域使用简单的检索增强生成（RAG）效果良好，但法律合同却带来了独特的挑战。

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/0XIRjUsP_VAqjwDlR.png)

使用朴素向量检索增强生成（RAG）从无关合同中提取信息

如图所示，仅依靠向量索引来检索相关文本块可能会带来风险，比如从无关合同中提取信息。这是因为法律语言具有高度的结构性，不同协议中相似的措辞可能导致不正确或误导性的检索结果。这些局限性凸显了需要一种更具结构性的方法，比如 GraphRAG，以确保精确且上下文感知的检索。

要实现 GraphRAG，我们首先需要构建一个知识图谱。

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/1jmw9OfKkRD6SOI7uEusWGQ.png)

包含结构化和非结构化信息的法律知识图谱。

为了构建法律合同的知识图谱，我们需要一种方法来从文档中提取结构化信息，并将其与原始文本一起存储。LLM 可以通过通读合同并识别关键细节（如各方、日期、合同类型和重要条款）来提供帮助。我们不再将合同仅仅视为一大段文本，而是将其分解为反映其潜在法律含义的结构化组件。例如，LLM 可以识别出“ACME 公司同意从 2024 年 1 月 1 日起每月支付 10,000 美元”这句话既包含付款义务又包含起始日期，然后我们可以将这些信息以结构化格式存储。

一旦我们拥有了这种结构化数据，就将其存储在知识图谱中，其中公司、协议和条款等实体及其关系都会被表示出来。非结构化文本仍然可用，但现在我们可以利用结构化层来优化搜索并使检索更加精确。我们不再只是获取最相关的文本块，而是可以根据合同的属性对其进行筛选。这意味着我们能够回答简单的基于检索增强生成（RAG）难以处理的问题，比如上个月签署了多少份合同，或者我们与某家特定公司是否有任何有效的协议。这些问题需要进行聚合和筛选，仅靠标准的基于向量的检索是无法做到的。

通过结合结构化和非结构化数据，我们还使检索更具上下文感知能力。如果用户询问合同的付款条款，我们确保搜索局限于正确的协议，而不是依赖文本相似度，因为文本相似度可能会引入来自不相关合同的条款。这种混合方法克服了简单的检索增强生成（RAG）的局限性，并允许对法律文件进行更深入、更可靠的分析。

### 图构建

我们将利用一个大语言模型（LLM）从法律文件中提取结构化信息，使用 [**CUAD（合同理解阿提克斯数据集）**](https://www.atticusprojectai.org/cuad) **，这是一个广泛用于合同分析的基准数据集，遵循 CC BY 4.0 许可协议。CUAD 数据集包含 500 多份合同，使其成为评估我们结构化提取流程的理想数据集。**

合同的词元计数分布如下所示。

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/image-19-1024x792.png)

此数据集中的大多数合同相对较短，词元计数低于10,000。然而，也有一些长得多的合同，少数合同的词元数高达80,000。这些长合同很罕见，而短合同占大多数。分布呈现出急剧下降的趋势，这意味着长合同是例外而非常态。

我们正在使用 Gemini-2.0-Flash 进行提取，它有 100 万个标记的输入限制，所以处理这些合同不是问题。即使我们数据集中最长的合同（约 80,000 个标记）也完全在模型的处理能力范围内。由于大多数合同要短得多，我们不必担心截断问题或将文档拆分成更小的块来进行处理。

#### 结构化数据提取

大多数商业语言模型（LLMs）都可以选择使用 Pydantic 对象来定义输出的模式。一个位置示例：

```python
class Location(BaseModel):
    """
    Represents a physical location including address, city, state, and country.
    """

    address: Optional[str] = Field(
        ..., description="The street address of the location.Use None if not provided"
    )
    city: Optional[str] = Field(
        ..., description="The city of the location.Use None if not provided"
    )
    state: Optional[str] = Field(
        ..., description="The state or region of the location.Use None if not provided"
    )
    country: str = Field(
        ...,
        description="The country of the location. Use the two-letter ISO standard.",
    )
```

在使用大语言模型（LLMs）进行结构化输出时，Pydantic 通过指定属性类型并提供指导模型响应的描述来帮助定义清晰的模式。每个字段都有一个类型，例如 `str` 或 `Optional[str]` ，以及一个描述，该描述会准确告诉大语言模型如何格式化输出。

例如，在一个 `位置` 模型中，我们定义了诸如 `地址 ` 、 `  城市  ` 、 ` 州/省` 和 `国家` 等关键属性，明确了期望的数据内容以及数据应如何结构化。例如， ` 国家` 字段遵循两个字母的国家代码标准，如 `"美国"` 、 `"法国"` 或 `"日本"` ，而不是像“美国”或“USA”这样不一致的变体。这一原则也适用于其他结构化数据，ISO 8601 将日期保持在标准格式（ `YYYY-MM-DD` ），等等。

通过使用 Pydantic 定义结构化输出，我们使 LLM 的响应更可靠、机器可读，并且更易于集成到数据库或 API 中。清晰的字段描述进一步帮助模型生成格式正确的数据，减少了后处理的需求。

Pydantic 模式模型可以更加复杂，如下方的 **合同** 模型所示，它捕捉了法律协议的关键细节，确保提取的数据遵循标准化结构。

```python
class Contract(BaseModel):
    """
    Represents the key details of the contract.
    """
  
    summary: str = Field(
        ...,
        description=("High level summary of the contract with relevant facts and details. Include all relevant information to provide full picture."
        "Do no use any pronouns"),
    )
    contract_type: str = Field(
        ...,
        description="The type of contract being entered into.",
        enum=CONTRACT_TYPES,
    )
    parties: List[Organization] = Field(
        ...,
        description="List of parties involved in the contract, with details of each party's role.",
    )
    effective_date: str = Field(
        ...,
        description=(
            "Enter the date when the contract becomes effective in yyyy-MM-dd format."
            "If only the year (e.g., 2015) is known, use 2015-01-01 as the default date."
            "Always fill in full date"
        ),
    )
    contract_scope: str = Field(
        ...,
        description="Description of the scope of the contract, including rights, duties, and any limitations.",
    )
    duration: Optional[str] = Field(
        None,
        description=(
            "The duration of the agreement, including provisions for renewal or termination."
            "Use ISO 8601 durations standard"
        ),
    )
  
    end_date: Optional[str] = Field(
        None,
        description=(
            "The date when the contract expires. Use yyyy-MM-dd format."
            "If only the year (e.g., 2015) is known, use 2015-01-01 as the default date."
            "Always fill in full date"
        ),
    )
    total_amount: Optional[float] = Field(
        None, description="Total value of the contract."
    )
    governing_law: Optional[Location] = Field(
        None, description="The jurisdiction's laws governing the contract."
    )
    clauses: Optional[List[Clause]] = Field(
        None, description=f"""Relevant summaries of clause types. Allowed clause types are {CLAUSE_TYPES}"""
    )
```

此合同模式以结构化方式组织法律协议的关键细节，便于使用大语言模型（LLMs）进行分析。它包括不同类型的条款，如保密或终止条款，每个条款都有简短摘要。涉及的各方列出了其名称、地点和角色，而合同细节涵盖了开始和结束日期、总价值和适用法律等内容。一些属性，如适用法律，可以使用嵌套模型进行定义，从而实现更详细和复杂的输出。

*嵌套对象方法在处理复杂数据关系的一些人工智能模型中运行良好，而其他模型可能会在深度嵌套的细节上遇到困难。*

我们可以使用以下示例来测试我们的方法。我们正在使用 LangChain 框架来编排 LLMs。

```python
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
llm.with_structured_output(Contract).invoke(
    "Tomaz works with Neo4j since 2017 and will make a billion dollar until 2030."
    "The contract was signed in Las Vegas"
)
```

其输出

```python
Contract(
    summary="Tomaz works with Neo4j since 2017 and will make a billion dollar until 2030.",
    contract_type="Service",
    parties=[
        Organization(
            name="Tomaz",
            location=Location(
                address=None,
                city="Las Vegas",
                state=None,
                country="US"
            ),
            role="employee"
        ),
        Organization(
            name="Neo4j",
            location=Location(
                address=None,
                city=None,
                state=None,
                country="US"
            ),
            role="employer"
        )
    ],
    effective_date="2017-01-01",
    contract_scope="Tomaz will work with Neo4j",
    duration=None,
    end_date="2030-01-01",
    total_amount=1_000_000_000.0,
    governing_law=None,
    clauses=None
)
```

既然我们的合同数据已呈结构化格式，那么我们就可以定义将其导入 Neo4j 所需的 Cypher 查询，将实体、关系和关键条款映射到一个图结构中。这一步将原始提取的数据转换为一个可查询的知识图谱，从而能够高效地遍历和检索合同洞察。

```sql
UNWIND $data AS row
MERGE (c:Contract {file_id: row.file_id})
SET c.summary = row.summary,
    c.contract_type = row.contract_type,
    c.effective_date = date(row.effective_date),
    c.contract_scope = row.contract_scope,
    c.duration = row.duration,
    c.end_date = CASE WHEN row.end_date IS NOT NULL THEN date(row.end_date) ELSE NULL END,
    c.total_amount = row.total_amount
WITH c, row
CALL (c, row) {
    WITH c, row
    WHERE row.governing_law IS NOT NULL
    MERGE (c)-[:HAS_GOVERNING_LAW]->(l:Location)
    SET l += row.governing_law
}
FOREACH (party IN row.parties |
    MERGE (p:Party {name: party.name})
    MERGE (p)-[:HAS_LOCATION]->(pl:Location)
    SET pl += party.location
    MERGE (p)-[pr:PARTY_TO]->(c)
    SET pr.role = party.role
)
FOREACH (clause IN row.clauses |
    MERGE (c)-[:HAS_CLAUSE]->(cl:Clause {type: clause.clause_type})
    SET cl.summary = clause.summary
)
```

此 Cypher 查询通过创建具有诸如 `摘要 ` 、 `  合同类型  ` 、 `  生效日期  ` 、 ` 期限` 和 `总金额` 等属性的 `合同` 节点，将结构化合同数据导入到 Neo4j 中。如果指定了适用法律，则将合同链接到一个 `地点` 节点。合同涉及的各方存储为 `当事人` 节点，每个当事人连接到一个 `地点` 并被赋予与合同相关的角色。该查询还处理条款，创建 `条款` 节点并将它们链接到合同，同时存储它们的类型和摘要。

在处理和导入合同后，生成的图遵循以下图模式。

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/11KHDth5g7nGRES_LSpqCyw.png)

导入的法律图模式

让我们也来看一份合同。  

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/image-20.png)

此图表代表一种合同结构，其中一份合同（橙色节点）连接到各种条款（红色节点）、各方（蓝色节点）和地点（紫色节点）。该合同有三个条款： *续约与终止* 、 *责任与赔偿* 以及 *保密与不披露* 。涉及两方，即 *Modus Media International* 和 *Dragon Systems, Inc.*，各方分别与各自的地点相连，即荷兰（NL）和美国（US）。该合同受美国法律管辖。合同节点还包含其他元数据，包括日期和其他相关细节。

一个包含 CUAD 法律合同的公共只读实例可通过以下凭证获取。

```markup
URI: neo4j+s://demo.neo4jlabs.com
username: legalcontracts
password: legalcontracts
database: legalcontracts
```

#### 实体解析

由于公司、个人和地点的引用方式存在差异，法律合同中的实体解析具有挑战性。一家公司在一份合同中可能显示为“Acme Inc.”，而在另一份合同中可能显示为“Acme Corporation”，这就需要一个流程来确定它们是否指的是同一个实体。

一种方法是使用文本嵌入或诸如莱文斯坦距离之类的字符串距离度量来生成候选匹配项。嵌入捕获语义相似性，而字符串距离度量字符级别的差异。一旦确定了候选项，就需要进行额外的评估，比较诸如地址或税务 ID 之类的元数据，分析图中的共享关系，或者对关键情况进行人工审核。

对于大规模解析实体，像 [重复数据删除工具（Dedupe）](https://github.com/dedupeio/dedupe) 这样的开源解决方案和像 [森辛（Senzing）](https://senzing.com/) 这样的商业工具都提供了自动化方法。选择正确的方法取决于数据质量、准确性要求以及人工监督是否可行。

在构建好法律图谱后，我们可以着手进行智能体 GraphRAG 的实现。

### 智能代理图结构检索增强生成模型

智能体架构在复杂性、模块化和推理能力方面差异很大。其核心是，这些架构涉及一个作为中央推理引擎的大语言模型（LLM），通常还辅以工具、内存和编排机制。关键区别在于大语言模型在决策时有多大的自主性，以及与外部系统的交互是如何构建的。

对于类似聊天机器人的实现而言，最简单且最有效的设计之一，尤其是直接采用“带工具的大语言模型（LLM）”方法。在这种设置中，大语言模型充当决策者，动态选择调用哪些工具（如果有的话），在必要时重试操作，并按顺序执行多个工具以满足复杂请求。

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/image-21.png)

该图表展示了一个简单的 LangGraph 智能体工作流程。它从 `__start__` 开始，移动到 `assistant` 节点，在该节点 LLM 处理用户输入。从那里开始，助手可以调用 `tools` 来获取相关信息，或者直接过渡到 `__end__` 以完成交互。如果使用了工具，助手会在决定是否调用另一个工具或结束会话之前处理响应。这种结构允许智能体在响应之前自主确定何时需要外部信息。

这种方法特别适用于像 Gemini 或 GPT-4o 这样更强的商业模型，它们在推理和自我纠正方面表现出色。

#### Tools

大语言模型（LLMs）是强大的推理引擎，但其有效性往往取决于它们配备外部工具的程度。这些工具，无论是数据库查询、应用程序编程接口（APIs）还是搜索功能，都能扩展大语言模型（LLM）检索事实、进行计算或与结构化数据交互的能力。

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/image-22.png)

设计出既通用到足以处理各种查询，又精确到足以返回有意义结果的工具，这更像是一门艺术而非科学。我们真正构建的是一个位于大语言模型（LLM）和底层数据之间的语义层。我们不是要求大语言模型理解 Neo4j 知识图谱或数据库模式的精确结构，而是定义一些工具来抽象掉这些复杂性。

通过这种方法，LLM 无需知道合同信息是存储为图节点和关系，还是存储为文档存储中的原始文本。它只需要调用正确的工具，根据用户的问题获取相关数据。

在我们的案例中，合同检索工具充当了这个语义接口。当用户询问合同条款、义务或相关方时，大语言模型（LLM）会调用一个结构化查询工具，该工具将请求转换为数据库查询，检索相关信息，并以大语言模型能够解释和总结的格式呈现出来。这使得系统具有灵活性且与模型无关，不同的大语言模型（LLMs）可以与合同数据进行交互，而无需直接了解其存储方式或结构。

设计最优工具集没有一刀切的标准。对一个模型有效的方法对另一个模型可能会失败。一些模型能很好地处理模糊的工具指令，而另一些模型则在复杂参数方面存在困难，或者需要明确的提示。通用性和特定任务效率之间的权衡意味着工具设计需要针对所使用的大语言模型（LLM）进行迭代、测试和微调。  
对于合同分析而言，一个有效的工具应该能够检索合同并总结关键条款，而无需用户严格措辞查询。实现这种灵活性取决于精心的提示工程、稳健的模式设计以及对不同 LLM 能力的适配。随着模型的发展，使工具更直观、有效的策略也在不断演变。

在本节中，我们将探索工具实现的不同方法，比较它们的灵活性、有效性以及与各种大语言模型（LLMs）的兼容性。

我更喜欢的方法是动态且确定性地构建一个 Cypher 查询，并针对数据库执行该查询。这种方法在保持实现灵活性的同时，确保了一致且可预测的查询生成。通过以这种方式构建查询，我们强化了语义层，允许用户输入无缝转换为数据库检索操作。这使得 LLM 专注于检索相关信息，而不是理解底层数据模型。

我们的工具旨在识别相关合同，因此我们需要为 LLM 提供根据各种属性搜索合同的选项。输入描述同样作为一个 Pydantic 对象提供。

```python
class ContractInput(BaseModel):
    min_effective_date: Optional[str] = Field(
        None, description="Earliest contract effective date (YYYY-MM-DD)"
    )
    max_effective_date: Optional[str] = Field(
        None, description="Latest contract effective date (YYYY-MM-DD)"
    )
    min_end_date: Optional[str] = Field(
        None, description="Earliest contract end date (YYYY-MM-DD)"
    )
    max_end_date: Optional[str] = Field(
        None, description="Latest contract end date (YYYY-MM-DD)"
    )
    contract_type: Optional[str] = Field(
        None, description=f"Contract type; valid types: {CONTRACT_TYPES}"
    )
    parties: Optional[List[str]] = Field(
        None, description="List of parties involved in the contract"
    )
    summary_search: Optional[str] = Field(
        None, description="Inspect summary of the contract"
    )
    country: Optional[str] = Field(
        None, description="Country where the contract applies. Use the two-letter ISO standard."
    )
    active: Optional[bool] = Field(None, description="Whether the contract is active")
    monetary_value: Optional[MonetaryValue] = Field(
        None, description="The total amount or value of a contract"
    )
```

使用大语言模型（LLM）工具时，属性会根据其用途采用各种形式。有些字段是简单的字符串，例如 `contract_type` （合同类型）和 `country` （国家），它们存储单个值。其他字段，如 `parties` （参与方），是字符串列表，允许多个条目（例如，合同中涉及的多个实体）。

除了基本数据类型外，属性还可以表示复杂对象。例如， `monetary_value` 使用 `MonetaryValue` 对象，该对象包含诸如货币类型和运算符等结构化数据。虽然带有嵌套对象的属性提供了清晰且结构化的数据表示，但模型往往难以有效地处理它们，因此我们应该保持它们简单。

作为该项目的一部分，我们正在试验一个额外的 `cypher_aggregation` 属性，为需要特定过滤或聚合的场景为 LLM 提供更大的灵活性。

```python
cypher_aggregation: Optional[str] = Field(
    None,
    description="""Custom Cypher statement for advanced aggregations and analytics.

    This will be appended to the base query:
    \`\`\`
    MATCH (c:Contract)
    <filtering based on other parameters>
    WITH c, summary, contract_type, contract_scope, effective_date, end_date, parties, active, monetary_value, contract_id, countries
    <your cypher goes here>
    \`\`\`
    
    Examples:
    
    1. Count contracts by type:
    \`\`\`
    RETURN contract_type, count(*) AS count ORDER BY count DESC
    \`\`\`
    
    2. Calculate average contract duration by type:
    \`\`\`
    WITH contract_type, effective_date, end_date
    WHERE effective_date IS NOT NULL AND end_date IS NOT NULL
    WITH contract_type, duration.between(effective_date, end_date).days AS duration
    RETURN contract_type, avg(duration) AS avg_duration ORDER BY avg_duration DESC
    \`\`\`
    
    3. Calculate contracts per effective date year:
    \`\`\`
    RETURN effective_date.year AS year, count(*) AS count ORDER BY year
    \`\`\`
    
    4. Counts the party with the highest number of active contracts:
    \`\`\`
    UNWIND parties AS party
    WITH party.name AS party_name, active, count(*) AS contract_count
    WHERE active = true
    RETURN party_name, contract_count
    ORDER BY contract_count DESC
    LIMIT 1
    \`\`\`
    """
```

\`cypher\_aggregation\` 属性允许大语言模型（LLMs）定义用于高级聚合和分析的自定义 Cypher 语句。它通过追加问题指定的聚合逻辑来扩展基本查询，从而实现灵活的筛选和计算。

此功能支持多种用例，如按合同类型统计合同数量、计算平均合同期限、分析合同随时间的分布情况以及根据合同活动识别关键方。通过利用此属性，大语言模型（LLM）可以动态生成针对特定分析需求的见解，而无需预定义的查询结构。

虽然这种灵活性很有价值，但应该仔细评估，因为由于操作的复杂性增加，适应性的提高是以降低一致性和稳健性为代价的。

当我们向语言模型（LLM）展示一个函数时，必须明确定义其名称和描述。结构良好的描述有助于引导模型正确使用该函数，确保它理解函数的目的、预期输入和输出。这减少了歧义，并提高了语言模型生成有意义且可靠查询的能力。

```python
class ContractSearchTool(BaseTool):
    name: str = "ContractSearch"
    description: str = (
        "useful for when you need to answer questions related to any contracts"
    )
    args_schema: Type[BaseModel] = ContractInput
```

最后，我们需要实现一个函数，该函数处理给定的输入，构造相应的 Cypher 语句，并高效地执行它。

该函数的核心逻辑围绕构建 Cypher 语句展开。我们首先将合同作为查询的基础进行匹配。

```python
cypher_statement = "MATCH (c:Contract) "
```

接下来，我们需要实现处理输入参数的函数。在这个示例中，我们主要使用属性根据给定的标准来筛选合同。

  
**简单属性过滤**  
例如， `contract_type` 属性用于执行简单的节点属性过滤。

```python
if contract_type:
    filters.append("c.contract_type = $contract_type")
    params["contract_type"] = contract_type
```

这段代码在使用查询参数作为值时，为 `contract_type` 添加了一个 Cypher 过滤器，以防止查询注入安全问题。

由于可能的合同类型值在属性描述中给出

```python
contract_type: Optional[str] = Field(
    None, description=f"Contract type; valid types: {CONTRACT_TYPES}"
)
```

我们不必担心将输入值映射到有效的合同类型，因为大语言模型（LLM）会处理这一点。

**推断属性过滤**

我们正在构建工具，以便让大型语言模型（LLM）与知识图谱进行交互，其中这些工具充当结构化查询的抽象层。一个关键特性是能够在运行时使用推断属性，这类似于本体，但却是动态计算的。

```python
if active is not None:
    operator = ">=" if active else "<"
    filters.append(f"c.end_date {operator} date()")
```

在此， `active` 用作运行时分类，确定合同是正在进行中（ `>= date()` ）还是已过期（ `< date()` ）。此逻辑通过仅在需要时计算属性来扩展结构化知识图谱查询，从而实现更灵活的大语言模型（LLM）推理。通过在工具中处理此类逻辑，我们确保大语言模型与简化、直观的操作进行交互，使其专注于推理而非查询制定。

**邻居过滤**

有时，过滤取决于相邻节点，例如将结果限制为涉及特定方的合同。 `parties` 属性是一个可选列表，当提供该列表时，它确保只考虑与这些实体相关联的合同：

```python
if parties:
    parties_filter = []
    for i, party in enumerate(parties):
        party_param_name = f"party_{i}"
        parties_filter.append(
            f"""EXISTS {{
            MATCH (c)<-[:PARTY_TO]-(party)
            WHERE toLower(party.name) CONTAINS ${party_param_name}
        }}"""
        )
        params[party_param_name] = party.lower()
```

这段代码根据合同关联的各方对合同进行筛选，将逻辑视为 **与** ，这意味着合同要被纳入，必须满足所有指定条件。它会遍历提供的 `parties` 列表，并构建一个查询，其中每个方的条件都必须成立。

为每一方生成一个唯一的参数名称以避免冲突。 `EXISTS` 子句确保合同与名称包含指定值的一方具有 `PARTY_TO` 关系。名称会转换为小写以实现不区分大小写的匹配。每个方条件分别添加，在它们之间强制使用隐式的 **AND** 。

如果需要更复杂的逻辑，例如支持 **或** 条件或允许不同的匹配标准，那么输入就需要改变。不再是简单的参与方名称列表，而是需要一种指定运算符的结构化输入格式。

*此外，我们可以实现一种能够容忍轻微拼写错误的当事人匹配方法，通过处理拼写和格式上的变化来提升用户体验。*

**自定义运算符过滤**

为了增加更多灵活性，我们可以引入一个运算符对象作为嵌套属性，从而对过滤逻辑有更多的控制权。我们不再硬编码比较操作，而是定义一个运算符枚举并动态使用它。

例如，对于货币值，合同可能需要根据其总额大于、小于或恰好等于指定值来进行筛选。我们没有采用固定的比较逻辑，而是定义了一个枚举来表示可能的运算符：

```python
class NumberOperator(str, Enum):
    EQUALS = "="
    GREATER_THAN = ">"
    LESS_THAN = "<"

class MonetaryValue(BaseModel):
    """The total amount or value of a contract"""
    value: float
    operator: NumberOperator

if monetary_value:
    filters.append(f"c.total_amount {monetary_value.operator.value} $total_value")
    params["total_value"] = monetary_value.value
```

这种方法使系统更具表现力。工具界面并非采用严格的过滤规则，而是允许大语言模型（LLM）不仅指定一个值，还能指定该值应如何进行比较，从而在保持大语言模型交互简单且声明式的同时，更易于处理更广泛的查询。

一些大语言模型（LLMs）在处理嵌套对象作为输入时存在困难，这使得处理基于运算符的结构化过滤变得更加困难。添加一个 *between* 运算符会引入额外的复杂性，因为它需要两个单独的值，这可能会导致解析和输入验证中的歧义。

**最小值和最大值属性**

为了让事情更简单，我倾向于使用日期的 `min` 和 `max` 属性，因为这自然支持范围过滤，并且使 *between* 逻辑变得直接明了。

```python
if min_effective_date:
    filters.append("c.effective_date >= date($min_effective_date)")
    params["min_effective_date"] = min_effective_date
if max_effective_date:
    filters.append("c.effective_date <= date($max_effective_date)")
    params["max_effective_date"] = max_effective_date
```

此函数通过在提供 `min_effective_date` 和 `max_effective_date` 时添加可选的下限和上限条件，根据生效日期范围过滤合同，确保只包含指定日期范围内的合同。

**语义搜索**

一个属性也可用于语义搜索，在这里我们不是预先依赖向量索引，而是使用一种后过滤方法来进行元数据过滤。首先，应用结构化过滤器，如日期范围、货币值或参与方，来缩小候选集。然后，对这个经过过滤的子集进行向量搜索，以根据语义相似性对结果进行排序。

```python
if summary_search:
    cypher_statement += (
        "WITH c, vector.similarity.cosine(c.embedding, $embedding) "
        "AS score ORDER BY score DESC WITH c, score WHERE score > 0.9 "
    )  # Define a threshold limit
    params["embedding"] = embeddings.embed_query(summary_search)
else:  # Else we sort by latest
    cypher_statement += "WITH c ORDER BY c.effective_date DESC "
```

当提供 `summary_search` 时，此代码通过计算合同嵌入与查询嵌入之间的余弦相似度来应用语义搜索，按相关性对结果进行排序，并使用 0.9 的阈值过滤掉低得分匹配项。否则，它默认按最近的 `effective_date` 对合同进行排序。

**动态查询**

密码聚合属性是我想要测试的一个实验，它赋予大语言模型（LLM）一定程度的部分文本到密码的能力，使其能够在初始结构化过滤之后动态生成聚合。这种方法不是预先定义每一种可能的聚合，而是让大语言模型根据需要指定诸如计数、平均值或分组汇总等计算，从而使查询更加灵活且富有表现力。然而，由于这将更多的查询逻辑转移到了大语言模型上，要确保所有生成的查询都能正确运行就变得很有挑战性，因为格式错误或不兼容的 Cypher 语句可能会导致执行中断。在灵活性和可靠性之间的这种权衡是系统设计中的一个关键考虑因素。

```python
if cypher_aggregation:
    cypher_statement += """WITH c, c.summary AS summary, c.contract_type AS contract_type, 
      c.contract_scope AS contract_scope, c.effective_date AS effective_date, c.end_date AS end_date,
      [(c)<-[r:PARTY_TO]-(party) | {party: party.name, role: r.role}] AS parties, c.end_date >= date() AS active, c.total_amount as monetary_value, c.file_id AS contract_id,
      apoc.coll.toSet([(c)<-[:PARTY_TO]-(party)-[:LOCATED_IN]->(country) | country.name]) AS countries """
    cypher_statement += cypher_aggregation
```

如果未提供密码聚合，我们将返回已识别合同的总数以及仅五个示例合同，以避免提示信息过多。处理过多的行至关重要，因为在处理大量结果集时陷入困境的 LLM 并无用处。此外，让 LLM 生成包含 100 个合同标题的答案也不是良好的用户体验。

```python
cypher_statement += """WITH collect(c) AS nodes
RETURN {
    total_count_of_contracts: size(nodes),
    example_values: [
      el in nodes[..5] |
      {summary:el.summary, contract_type:el.contract_type, 
       contract_scope: el.contract_scope, file_id: el.file_id, 
        effective_date: el.effective_date, end_date: el.end_date,
        monetary_value: el.total_amount, contract_id: el.file_id, 
        parties: [(el)<-[r:PARTY_TO]-(party) | {name: party.name, role: r.role}], 
        countries: apoc.coll.toSet([(el)<-[:PARTY_TO]-()-[:LOCATED_IN]->(country) | country.name])}
    ]
} AS output"""
```

这条 Cypher 语句将所有匹配的合同收集到一个列表中，返回总数以及最多五个带有关键属性的示例合同，这些属性包括摘要、类型、范围、日期、货币价值、具有角色的关联方以及唯一的国家/地区位置。  
既然我们的合同搜索工具已经构建完成，我们将其交给大语言模型（LLM），就这样，我们实现了智能代理式的 GraphRAG。

### 智能体基准测试

如果你认真考虑实施智能代理式 GraphRAG，你需要一个评估数据集，它不仅是一个基准，更是整个项目的基础。一个构建良好的数据集有助于定义系统应处理的范围，确保初始开发与实际用例保持一致。除此之外，它还是评估性能的宝贵工具，能让你衡量大语言模型（LLM）与图的交互效果、信息检索能力以及推理应用能力。对于提示工程优化也至关重要，能让你根据明确的反馈而非猜测，反复优化查询、工具使用和响应格式。没有结构化的数据集，你就像在盲目飞行，改进难以量化，不一致性也更难发现。

The code for the benchmark is [available on GitHub](https://github.com/tomasonjo-labs/legal-tech-chat/blob/main/research/benchmark/benchmark_evaluate.ipynb).

我已经编制了一份包含 22 个问题的列表，我们将用它来评估该系统。此外，我们将引入一个名为 `answer_satisfaction` 的新指标，在这个指标中我们将提供一个自定义提示。

```python
answer_satisfaction = AspectCritic(
    name="answer_satisfaction",
    definition="""You will evaluate an ANSWER to a legal QUESTION based on a provided SOLUTION.

Rate the answer on a scale from 0 to 1, where:
- 0 = incorrect, substantially incomplete, or misleading
- 1 = correct and sufficiently complete

Consider these evaluation criteria:
1. Factual correctness is paramount - the answer must not contradict the solution
2. The answer must address the core elements of the solution
3. Additional relevant information beyond the solution is acceptable and may enhance the answer
4. Technical legal terminology should be used appropriately if present in the solution
5. For quantitative legal analyses, accurate figures must be provided

+ fewshots
"""
```

许多问题可能会返回大量信息。例如，询问 2020 年之前签署的合同可能会产生数百个结果。由于大语言模型（LLM）会收到总数和一些示例条目，我们的评估应关注总数，而不是大语言模型选择展示哪些具体示例。

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/1CrZ1PejU0Qbm5yopJeo4MA.png)

基准测试结果。

所提供的结果表明，对于大多数工具调用，所有评估模型（Gemini 1.5 Pro、Gemini 2.0 Flash 和 GPT-4o）的表现都同样出色，GPT-4o 略优于 Gemini 模型（0.82 对 0.77）。主要在使用部分 `text2cypher` 时，尤其是在各种聚合操作中，会出现明显差异。

*请注意，这只是 22 个相当简单的问题，所以我们并没有真正探究大语言模型（LLMs）的推理能力。*

此外，我还见过一些项目，在这些项目中，通过利用 Python 进行聚合可以显著提高准确性，因为大语言模型（LLMs）通常在处理 Python 代码生成和执行方面比直接生成复杂的 Cypher 查询表现更好。

### Web 应用程序

我们还构建了一个简单的 React Web 应用程序，由托管在 FastAPI 上的 LangGraph 提供支持，它将响应直接流式传输到前端。特别感谢 [阿内伊·戈尔基奇](https://github.com/easwee) 创建这个 Web 应用程序。

你可以使用以下命令启动整个堆栈：

```bash
docker compose up
```

然后导航到 `localhost:5173`  

![](https://contributor.insightmediagroup.io/wp-content/uploads/2025/04/image-23.png)

### Summary

随着大语言模型（LLMs）的推理能力不断增强，当与合适的工具相结合时，它们可以成为处理法律合同等复杂领域的强大智能体。在这篇文章中，我们只是触及了表面，重点关注了合同的核心属性，而几乎没有涉及实际协议中丰富多样的条款。从扩大条款覆盖范围到优化工具设计和交互策略，都有很大的发展空间。

代码可在 [GitHub](https://github.com/tomasonjo-labs/legal-tech-chat) 上获取。

