---
title: "Building a Knowledge Graph with LlamaCloud & Neo4J - LlamaIndex"
source: "https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?utm_source=socials&utm_medium=li_social"
author:
published: 2025-08-18
created: 2025-08-18
description:
tags:
---
[Skip to content](https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?utm_source=socials&utm_medium=li_social#building-a-knowledge-graph-with-llamacloud-neo4j)

## 使用 LlamaCloud 和 Neo4J 构建知识图谱

检索增强生成（RAG）是一种用于利用外部知识增强语言模型（LLMs）的强大技术，但传统的语义相似性搜索往往无法捕捉实体之间的细微关系，并且可能会遗漏跨多个文档的关键上下文。通过将非结构化文档转换为结构化知识表示，我们可以执行复杂的图遍历、关系查询和上下文推理，这远远超出了简单的相似性匹配。

像 LlamaParse 和 LlamaExtract 这样的工具提供了强大的解析和提取功能，可将原始文档转换为结构化数据，而 Neo4j 则作为知识图谱表示的支柱，构成了 GraphRAG 架构的基础，该架构不仅能够理解存在哪些信息，还能理解所有信息是如何相互连接的。

在本端到端教程中，我们将详细讲解一个法律文档处理示例，该示例展示了如下完整流程。

该管道包含以下步骤：

- 使用 [LlamaParse](https://www.llamaindex.ai/llamaparse) 来解析 PDF 文档并提取可读文本
- 使用大语言模型对合同类型进行分类，实现上下文感知处理
- 利用 [LlamaExtract](https://www.llamaindex.ai/llamaextract) 根据分类为每个特定合同类别提取不同的相关属性集
- 将所有结构化信息存储到一个 Neo4j 知识图谱中，创建一个丰富的、可查询的表示形式，该表示形式能够捕捉法律文件中的内容和复杂关系

## 设置要求

In \[ \]:

```js
!pip install llama-index-workflows llama-cloud-services jsonschema openai neo4j llama-index-llms-openai
```

!pip install llama-index-workflows llama-cloud-services jsonschema openai neo4j llama-index-llms-openai

In \[ \]:

```js
import re
import uuid
from datetime import date
from typing import List, Optional

from getpass import getpass
from neo4j import AsyncGraphDatabase
from openai import AsyncOpenAI
from pydantic import BaseModel, Field

from llama_cloud_services.extract import (
    ExtractConfig,
    ExtractMode,
    LlamaExtract,
    SourceText,
)
from llama_cloud_services.parse import LlamaParse

from llama_index.llms.openai import OpenAI
```

import re import uuid from datetime import date from typing import List, Optional from getpass import getpass from neo4j import AsyncGraphDatabase from openai import AsyncOpenAI from pydantic import BaseModel, Field from llama\_cloud\_services.extract import ( ExtractConfig, ExtractMode, LlamaExtract, SourceText, ) from llama\_cloud\_services.parse import LlamaParse from llama\_index.llms.openai import OpenAI

## 下载示例合同

在这里，我们从 Cuad 数据集中下载一个示例 PDF

In \[ \]:

```js
!wget https://raw.githubusercontent.com/tomasonjo/blog-datasets/5e3939d10216b7663687217c1646c30eb921d92f/CybergyHoldingsInc_Affliate%20Agreement.pdf
```

!wget https://raw.githubusercontent.com/tomasonjo/blog-datasets/5e3939d10216b7663687217c1646c30eb921d92f/CybergyHoldingsInc\_Affliate%20Agreement.pdf

## Set Up Neo4J

对于 Neo4j，最简单的方法是创建一个免费的 [Aura 数据库实例](https://neo4j.com/product/auradb/) ，并在此处复制您的凭证。

In \[ \]:

```js
db_url = "your-db-url"
username = "neo4j"
password = "your-password"

neo4j_driver = AsyncGraphDatabase.driver(
    db_url,
    auth=(
        username,
        password,
    ),
)
```

db\_url = "your-db-url" username = "neo4j" password = "your-password" neo4j\_driver = AsyncGraphDatabase.driver( db\_url, auth=( username, password, ), )

## 使用 LlamaParse 解析合同

接下来，我们设置 LlamaParse 并解析 PDF。在这种情况下，我们使用 `parse_page_without_llm` 模式。

In \[ \]:

```js
import os

os.environ["LLAMA_CLOUD_API_KEY"] = getpass("Enter your Llama API key: ")
os.environ["OPENAI_API_KEY"] = getpass("Enter your OpenAI API key: ")
```

import os os.environ\["LLAMA\_CLOUD\_API\_KEY"\] = getpass("Enter your Llama API key: ") os.environ\["OPENAI\_API\_KEY"\] = getpass("Enter your OpenAI API key: ")

```js
Enter your Llama API key: ··········
Enter your OpenAI API key: ··········
```

In \[ \]:

```js
# Initialize parser with specified mode
parser = LlamaParse(parse_mode="parse_page_without_llm")

# Define the PDF file to parse
pdf_path = "CybergyHoldingsInc_Affliate Agreement.pdf"

# Parse the document asynchronously
results = await parser.aparse(pdf_path)
```

\# Initialize parser with specified mode parser = LlamaParse(parse\_mode="parse\_page\_without\_llm") # Define the PDF file to parse pdf\_path = "CybergyHoldingsInc\_Affliate Agreement.pdf" # Parse the document asynchronously results = await parser.aparse(pdf\_path)

```js
Started parsing the file under job_id 888cf1ec-eb95-40df-8508-bdcbd0d0b63f
```

In \[ \]:

```js
print(results.pages[0].text)
```

print(results.pages\[0\].text)

```js
Exhibit 10.27

    MARKETING AFFILIATE AGREEMENT

                 Between:

Birch First Global Investments Inc.

                And

    Mount Knowledge Holdings Inc.

    Dated: May 8, 2014

    1

    Source: CYBERGY HOLDINGS, INC., 10-Q, 5/20/2014
```

## 合同分类

在这个例子中，我们想要对传入的合同进行分类。它们可以是 `  联盟协议  ` 或 `  联合品牌  ` 。我们在下面定义一个分类提示，并要求大语言模型（LLM）也返回分类的原因。

In \[ \]:

```js
llm = OpenAI(model="gpt-4o-mini")

classification_prompt = """You are a legal document classification assistant.
Your task is to identify the most likely contract type based on the content of the first 10 pages of a contract.

Instructions:

Read the contract excerpt below (up to the first 10 pages).

Review the list of possible contract types.

Choose the single most appropriate contract type from the list.

Justify your classification briefly, based only on the information in the excerpt.

Contract Excerpt:
{contract_text}

Possible Contract Types:
{contract_type_list}

Output Format:
<Reason>brief_justification</Reason>
<ContractType>chosen_type_from_list</ContractType>
"""
```

llm = OpenAI(model="gpt-4o-mini") classification\_prompt = """You are a legal document classification assistant. Your task is to identify the most likely contract type based on the content of the first 10 pages of a contract. Instructions: Read the contract excerpt below (up to the first 10 pages). Review the list of possible contract types. Choose the single most appropriate contract type from the list. Justify your classification briefly, based only on the information in the excerpt. Contract Excerpt: {contract\_text} Possible Contract Types: {contract\_type\_list} Output Format:brief\_justification chosen\_type\_from\_list """

In \[ \]:

```js
from llama_index.core.llms import ChatMessage

def extract_reason_and_contract_type(text):
    reason_match = re.search(r"<Reason>(.*?)</Reason>", text, re.DOTALL)
    reason = reason_match.group(1).strip() if reason_match else None

    contract_type_match = re.search(
        r"<ContractType>(.*?)</ContractType>", text, re.DOTALL
    )
    contract_type = (
        contract_type_match.group(1).strip() if contract_type_match else None
    )

    return {"reason": reason, "contract_type": contract_type}

async def classify_contract(
    contract_text: str, contract_types: list[str]
) -> dict:
    prompt = classification_prompt.format(
        contract_text=file_content, contract_type_list=contract_types
    )
    history = [ChatMessage(role="user", content=prompt)]

    response = await llm.achat(history)
    return extract_reason_and_contract_type(response.message.content)
```

from llama\_index.core.llms import ChatMessage def extract\_reason\_and\_contract\_type(text): reason\_match = re.search(r" (.\*?) ", text, re.DOTALL) reason = reason\_match.group(1).strip() if reason\_match else None contract\_type\_match = re.search( r" (.\*?) ", text, re.DOTALL ) contract\_type = ( contract\_type\_match.group(1).strip() if contract\_type\_match else None ) return {"reason": reason, "contract\_type": contract\_type} async def classify\_contract( contract\_text: str, contract\_types: list\[str\] ) -> dict: prompt = classification\_prompt.format( contract\_text=file\_content, contract\_type\_list=contract\_types ) history = \[ChatMessage(role="user", content=prompt)\] response = await llm.achat(history) return extract\_reason\_and\_contract\_type(response.message.content)

In \[ \]:

```js
contract_types = ["Affiliate_Agreements", "Co_Branding"]

# Take only the first 10 pages for contract classification as input
file_content = " ".join([el.text for el in results.pages[:10]])

classification = await classify_contract(file_content, contract_types)
classification
```

contract\_types = \["Affiliate\_Agreements", "Co\_Branding"\] # Take only the first 10 pages for contract classification as input file\_content = " ".join(\[el.text for el in results.pages\[:10\]\]) classification = await classify\_contract(file\_content, contract\_types) classification

## 设置 LlamaExtract

接下来，我们定义一些模式，可用于从我们的合同中提取相关信息。我们定义的字段既有摘要信息，也有结构化数据提取。

在这里，我们定义了两个 Pydantic 模型： `Location` 捕获结构化地址信息，包含国家、州和地址等可选字段，而 `Party` 表示合同方，包含必填的名称和可选的位置详细信息。字段描述通过确切告知 LLM 在每个字段中查找哪些信息来指导提取过程。

In \[ \]:

```js
class Location(BaseModel):
    """Location information with structured address components."""

    country: Optional[str] = Field(None, description="Country")
    state: Optional[str] = Field(None, description="State or province")
    address: Optional[str] = Field(None, description="Street address or city")

class Party(BaseModel):
    """Party information with name and location."""

    name: str = Field(description="Party name")
    location: Optional[Location] = Field(
        None, description="Party location details"
    )
```


请记住，我们有多种合同类型，因此我们需要为每种类型定义特定的提取模式，并创建一个映射系统，以便根据我们的分类结果动态选择合适的模式。

In \[ \]:

```js
class BaseContract(BaseModel):
    """Base contract class with common fields."""

    parties: Optional[List[Party]] = Field(
        None, description="All contracting parties"
    )
    agreement_date: Optional[str] = Field(
        None, description="Contract signing date. Use YYYY-MM-DD"
    )
    effective_date: Optional[str] = Field(
        None, description="When contract becomes effective. Use YYYY-MM-DD"
    )
    expiration_date: Optional[str] = Field(
        None, description="Contract expiration date. Use YYYY-MM-DD"
    )
    governing_law: Optional[str] = Field(
        None, description="Governing jurisdiction"
    )
    termination_for_convenience: Optional[bool] = Field(
        None, description="Can terminate without cause"
    )
    anti_assignment: Optional[bool] = Field(
        None, description="Restricts assignment to third parties"
    )
    cap_on_liability: Optional[str] = Field(
        None, description="Liability limit amount"
    )

class AffiliateAgreement(BaseContract):
    """Affiliate Agreement extraction."""

    exclusivity: Optional[str] = Field(
        None, description="Exclusive territory or market rights"
    )
    non_compete: Optional[str] = Field(
        None, description="Non-compete restrictions"
    )
    revenue_profit_sharing: Optional[str] = Field(
        None, description="Commission or revenue split"
    )
    minimum_commitment: Optional[str] = Field(
        None, description="Minimum sales targets"
    )

class CoBrandingAgreement(BaseContract):
    """Co-Branding Agreement extraction."""

    exclusivity: Optional[str] = Field(
        None, description="Exclusive co-branding rights"
    )
    ip_ownership_assignment: Optional[str] = Field(
        None, description="IP ownership allocation"
    )
    license_grant: Optional[str] = Field(
        None, description="Brand/trademark licenses"
    )
    revenue_profit_sharing: Optional[str] = Field(
        None, description="Revenue sharing terms"
    )

mapping = {
    "Affiliate_Agreements": AffiliateAgreement,
    "Co_Branding": CoBrandingAgreement,
}
```


```js
extractor = LlamaExtract()

agent = extractor.create_agent(
    name=f"extraction_workflow_import_{uuid.uuid4()}",
    data_schema=mapping[classification["contract_type"]],
    config=ExtractConfig(
        extraction_mode=ExtractMode.BALANCED,
    ),
)

result = await agent.aextract(
    files=SourceText(
        text_content=" ".join([el.text for el in results.pages]),
        filename=pdf_path,
    ),
)

result.data
```


```js
Uploading files: 100%|██████████| 1/1 [00:00<00:00,  2.85it/s]
Creating extraction jobs: 100%|██████████| 1/1 [00:00<00:00,  1.25it/s]
Extracting files: 100%|██████████| 1/1 [00:10<00:00, 10.87s/it]
```

Out\[ \]:

```js
{'parties': [{'name': 'Birch First Global Investments Inc.',
   'location': {'country': 'U.S. Virgin Islands',
    'state': None,
    'address': '9100 Havensight, Port of Sale, Ste. 15/16, St. Thomas, VI 0080'}},
  {'name': 'Mount Knowledge Holdings Inc.',
   'location': {'country': 'United States',
    'state': 'Nevada',
    'address': '228 Park Avenue S. #56101 New York, NY 100031502'}}],
 'agreement_date': '2014-05-08',
 'effective_date': '2014-05-08',
 'expiration_date': None,
 'governing_law': 'State of Nevada',
 'termination_for_convenience': True,
 'anti_assignment': True,
 'cap_on_liability': "Company's liability shall not exceed the fees that MA has paid under this Agreement.",
 'exclusivity': None,
 'non_compete': None,
 'revenue_profit_sharing': 'MA PURCHASE DISCOUNT: Level I: 15%, Level II: 20%, Level III: 25% (based on annual purchase volume)',
 'minimum_commitment': 'MA commits to purchase a minimum of 100 Units in aggregate within the Territory within the first six months of term of this Agreement.'}
```

## Import into Neo4j

最后一步是获取我们提取的结构化信息，并构建一个表示合同实体之间关系的知识图谱。我们需要定义一个图模型，该模型指定我们的合同数据应如何在 Neo4j 中作为节点和关系进行组织。

我们的图模型由三种主要节点类型组成：

- **合同节点** 存储核心协议信息，包括日期、条款和法律条款
- **参与方节点** 代表具有其名称的签约实体
- **位置节点** 通过地址组件捕获地理信息。

现在我们将根据定义的图模型，将提取的合同数据导入到 Neo4j 中。

In \[ \]:

```js
import_query = """
WITH $contract AS contract
MERGE (c:Contract {path: $path})
SET c += apoc.map.clean(contract, ["parties", "agreement_date", "effective_date", "expiration_date"], [])
// Cast to date
SET c.agreement_date = date(contract.agreement_date),
    c.effective_date = date(contract.effective_date),
    c.expiration_date = date(contract.expiration_date)

// Create parties with their locations
WITH c, contract
UNWIND coalesce(contract.parties, []) AS party
MERGE (p:Party {name: party.name})
MERGE (c)-[:HAS_PARTY]->(p)

// Create location nodes and link to parties
WITH p, party
WHERE party.location IS NOT NULL
MERGE (p)-[:HAS_LOCATION]->(l:Location)
SET l += party.location
"""

response = await neo4j_driver.execute_query(
    import_query, contract=result.data, path=pdf_path
)
response.summary.counters
```


```js
{'_contains_updates': True, 'labels_added': 5, 'relationships_created': 4, 'nodes_created': 5, 'properties_set': 16}
```

## 在工作流程中将所有内容整合在一起

最后，我们可以将所有这些逻辑组合成一个单一的可执行的智能工作流程。我们来实现这样一个工作流程：它能够通过接受单个 PDF 文件来运行，并每次都向我们的 Neo4j 图中添加新条目。

In \[ \]:

```js
affiliage_extraction_agent = extractor.create_agent(
    name="Affiliate_Extraction",
    data_schema=AffiliateAgreement,
    config=ExtractConfig(
        extraction_mode=ExtractMode.BALANCED,
    ),
)
cobranding_extraction_agent = extractor.create_agent(
    name="CoBranding_Extraction",
    data_schema=CoBrandingAgreement,
    config=ExtractConfig(
        extraction_mode=ExtractMode.BALANCED,
    ),
)
```


```js
from llama_index.core.workflow import (
    Workflow,
    Event,
    Context,
    StartEvent,
    StopEvent,
    step,
)

class ClassifyDocEvent(Event):
    parsed_doc: str
    pdf_path: str

class ExtactAffiliate(Event):
    file_path: str

class ExtractCoBranding(Event):
    file_path: str

class BuildGraph(Event):
    file_path: str
    data: dict

class KnowledgeGraphBuilder(Workflow):
    def __init__(
        self,
        parser: LlamaParse,
        affiliate_extract_agent: LlamaExtract,
        branding_extract_agent: LlamaExtract,
        classification_prompt: str,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.parser = parser
        self.affiliate_extract_agent = affiliate_extract_agent
        self.branding_extract_agent = branding_extract_agent
        self.classification_prompt = classification_prompt
        self.llm = OpenAI(model="gpt-4o-mini")

    @step
    async def parse_file(
        self, ctx: Context, ev: StartEvent
    ) -> ClassifyDocEvent:
        results = await self.parser.aparse(ev.pdf_path)
        parsed_doc = " ".join([el.text for el in results.pages[:10]])
        return ClassifyDocEvent(parsed_doc=parsed_doc, pdf_path=ev.pdf_path)

    @step
    async def classify_contract(
        self, ctx: Context, ev: ClassifyDocEvent
    ) -> ExtactAffiliate | ExtractCoBranding | StopEvent:
        prompt = self.classification_prompt.format(
            contract_text=ev.parsed_doc,
            contract_type_list=["Affiliate_Agreements", "Co_Branding"],
        )
        history = [ChatMessage(role="user", content=prompt)]

        response = await llm.achat(history)
        reason_match = re.search(
            r"<Reason>(.*?)</Reason>", response.message.content, re.DOTALL
        )
        reason = reason_match.group(1).strip() if reason_match else None

        contract_type_match = re.search(
            r"<ContractType>(.*?)</ContractType>",
            response.message.content,
            re.DOTALL,
        )
        contract_type = (
            contract_type_match.group(1).strip()
            if contract_type_match
            else None
        )
        if contract_type == "Affiliate_Agreements":
            return ExtactAffiliate(file_path=ev.pdf_path)
        elif contract_type == "Co_Branding":
            return ExtractCoBranding(file_path=ev.pdf_path)
        else:
            return StopEvent()

    @step
    async def extract_affiliate(
        self, ctx: Context, ev: ExtactAffiliate
    ) -> BuildGraph:
        result = await self.affiliate_extract_agent.aextract(ev.file_path)
        return BuildGraph(data=result.data, file_path=ev.file_path)

    @step
    async def extract_co_branding(
        self, ctx: Context, ev: ExtractCoBranding
    ) -> BuildGraph:
        result = await self.branding_extract_agent.aextract(ev.file_path)
        return BuildGraph(data=result.data, file_path=ev.file_path)

    @step
    async def build_graph(self, ctx: Context, ev: BuildGraph) -> StopEvent:
        import_query = """
    WITH $contract AS contract
    MERGE (c:Contract {path: $path})
    SET c += apoc.map.clean(contract, ["parties", "agreement_date", "effective_date", "expiration_date"], [])
    // Cast to date
    SET c.agreement_date = date(contract.agreement_date),
      c.effective_date = date(contract.effective_date),
      c.expiration_date = date(contract.expiration_date)

    // Create parties with their locations
    WITH c, contract
    UNWIND coalesce(contract.parties, []) AS party
    MERGE (p:Party {name: party.name})
    MERGE (c)-[:HAS_PARTY]->(p)

    // Create location nodes and link to parties
    WITH p, party
    WHERE party.location IS NOT NULL
    MERGE (p)-[:HAS_LOCATION]->(l:Location)
    SET l += party.location
    """
        response = await neo4j_driver.execute_query(
            import_query, contract=ev.data, path=ev.file_path
        )
        return StopEvent(response.summary.counters)
```



```js
knowledge_graph_builder = KnowledgeGraphBuilder(
    parser=parser,
    affiliate_extract_agent=affiliage_extraction_agent,
    branding_extract_agent=cobranding_extraction_agent,
    classification_prompt=classification_prompt,
    timeout=None,
    verbose=True,
)
```


```js
response = await knowledge_graph_builder.run(
    pdf_path="CybergyHoldingsInc_Affliate Agreement.pdf"
)
```

response = await knowledge\_graph\_builder.run( pdf\_path="CybergyHoldingsInc\_Affliate Agreement.pdf" )

```js
Running step parse_file
Started parsing the file under job_id a0bac8af-c6a4-4bd4-85d8-a44e7e302eed
Step parse_file produced event ClassifyDocEvent
Running step classify_contract
Step classify_contract produced event ExtactAffiliate
Running step extract_affiliate
```

```js
Uploading files: 100%|██████████| 1/1 [00:00<00:00,  2.66it/s]
Creating extraction jobs: 100%|██████████| 1/1 [00:00<00:00,  4.20it/s]
Extracting files: 100%|██████████| 1/1 [00:08<00:00,  8.41s/it]
```

```js
Step extract_affiliate produced event BuildGraph
Running step build_graph
Step build_graph produced event StopEvent
```