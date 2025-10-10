---
title: "Building Location-Aware AI Agents with DeepAgents and Camino AI"
source: "https://blog.getcamino.ai/deepagents-location-intelligence"
author:
published: 2025-09-12
created: 2025-09-12
description: "Learn how to create sophisticated AI research agents that combine location intelligence with web search capabilities using DeepAgents framework and Camino AI."
tags:
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
人工智能代理正变得越来越复杂，但大多数都缺乏现实世界的空间感知能力。今天，我们将向您展示如何使用 [深度代理](https://blog.langchain.com/deep-agents/) 和 **卡米诺人工智能** 构建智能的位置感知代理，这些代理能够理解、研究和推理地点与位置。

## What We're Building

我们将创建一个结合了以下内容的人工智能研究代理：

- 通过 Camino AI 实现的 **位置智能**
- 通过 Tavily 实现的 **网络搜索功能**
- 通过 DeepAgents 实现的复杂推理

此智能体可以回答如下复杂查询：

- 巴黎最好的咖啡店有哪些？
- 在金门大桥附近找到适合家庭就餐的餐厅
- 研究麻省理工学院周边的创业生态系统

## Prerequisites

```
pip install deepagents camino-ai-sdk tavily-python python-dotenv
```

你将需要以下的 API 密钥：

- [卡米诺人工智能](https://app.getcamino.ai/) \- 用于位置智能
- [塔维利（Tavily）](https://tavily.com/) - 用于网络搜索
- [Anthropic](https://anthropic.com/) - 用于（DeepAgents 所使用的）语言模型

## 完整实现

```
import os
from typing import Literal
from tavily import TavilyClient
from camino_ai import CaminoAI, APIError
from deepagents import create_deep_agent
from dotenv import load_dotenv

load_dotenv()

# Initialize clients
tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
camino_client = CaminoAI(api_key=os.environ.get("CAMINO_API_KEY"))

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """
    Run a web search to find current information and context.
    
    Use this for general research, news, reviews, and background information
    that complements location data.
    """
    try:
        return tavily_client.search(
            query,
            max_results=max_results,
            include_raw_content=include_raw_content,
            topic=topic,
        )
    except Exception as e:
        return f"Web search error: {str(e)}"

# Define the agent's research methodology
research_instructions = """You are an expert location researcher and travel advisor. 

Your mission is to provide comprehensive, actionable insights about places, businesses, and locations.

## Your Tools

You have access to multiple Camino AI location intelligence tools:

**\`query\`**: General location search for finding places, businesses, restaurants, hotels, attractions, etc. This tool understands natural language queries like "coffee shops in downtown Seattle" or "family restaurants near Central Park."

**\`search\`**: Alternative search method with different ranking algorithms.

**\`context\`**: Get contextual information about a specific location or area.

**\`journey\`**: Plan routes and journeys between multiple locations.

**\`relationship\`**: Understand spatial relationships between locations.

**\`internet_search\`**: Use this for gathering additional context, reviews, recent news, opening hours, pricing, or any supplementary information about locations you've found.

## Research Methodology

1. **Location Discovery**: Start with Camino AI tools to find relevant places
2. **Context Gathering**: Use internet_search to get reviews, recent information, and context
3. **Synthesis**: Combine location data with web research for comprehensive insights
4. **Recommendations**: Provide specific, actionable recommendations with reasoning

## Output Format

Structure your responses as:
- **Summary**: Brief overview of findings
- **Top Recommendations**: 3-5 specific places with details
- **Insights**: Key patterns, trends, or notable findings
- **Practical Tips**: Hours, pricing, reservation info, etc.

Always cite your sources and be specific about locations, addresses, and practical details.
"""

# Create the location-aware research agent with all Camino AI tools
agent = create_deep_agent(
    tools=[
        camino_client.search, 
        camino_client.query, 
        camino_client.context, 
        camino_client.journey, 
        camino_client.relationship, 
        internet_search
    ],
    instructions=research_instructions,
)

# Example usage
if __name__ == "__main__":
    queries = [
        "What are the best coffee shops in Paris?"
    ]
    
    for query in queries:
        print(f"\n🔍 Query: {query}")
        print("=" * 50)
        
        result = agent.invoke({
            "messages": [{"role": "user", "content": query}]
        })
        
        print(result['messages'][-1])
```

## 为什么这种组合有效

### 🎯 卡米诺人工智能的优势

- **自然语言理解** ：处理诸如“适合工作的安静咖啡店”之类的查询
- **人工智能驱动的排名** ：结果按相关性和质量排序
- **空间推理** ：理解接近度、方向和关系
- **结构化数据** ：干净、一致的位置信息

### 🌐 塔维利集成

- **当前信息** ：评论、营业时间、近期变动
- **背景与上下文** ：社区洞察、趋势
- **验证** ：将位置数据与网络来源进行交叉引用

### 🤖深度智能体框架

- **多步推理** ：规划研究方法
- **工具协调** ：智能整合位置数据和网络数据
- **自适应响应** ：根据查询类型调整方法

## Advanced Use Cases

### 旅行规划代理

```
travel_query = """
Plan a perfect day in San Francisco for a tech entrepreneur visiting for the first time. 
Include must-see tech landmarks, great coffee shops for meetings, and dinner recommendations.
"""

result = agent.invoke({
    "messages": [{"role": "user", "content": travel_query}]
})
```

### 市场调研代理

```
market_query = """
Analyze the restaurant scene in Brooklyn's DUMBO neighborhood. 
What types of cuisines are popular? Any gaps in the market?
"""

result = agent.invoke({
    "messages": [{"role": "user", "content": market_query}]
})
```

### 房地产分析

```
real_estate_query = """
Evaluate the amenities and walkability around 123 Main St, Boston. 
What restaurants, shops, and services are within walking distance?
"""

result = agent.invoke({
    "messages": [{"role": "user", "content": real_estate_query}]
})
```

## Real-World Results

以下是我们的智能体针对“巴黎最佳咖啡店”生成的内容（ [在 LangSmith 上查看完整记录](https://smith.langchain.com/public/7fec9cc2-b70a-4b63-a4f1-1ec678a13632/r) ）：

#### Summary

巴黎已从传统的咖啡馆文化发展而来，开始接纳世界级的特色咖啡，市内遍布着众多出色的第三波咖啡店。这一场景将传统巴黎咖啡馆的氛围与现代咖啡技艺相结合，既有本地烘焙商，也有来自世界各地的咖啡豆。

#### Top Recommendations

**望远镜咖啡馆 ⭐⭐⭐⭐⭐**

- **地址** ：巴黎维勒多街 5 号，75001 巴黎（第一区）
- **营业时间** ：周一至周五上午 8:30 至下午 4:00（周末休息）
- **特色** ：巴黎特色咖啡界先驱，出色的馥芮白咖啡
- **其特别之处** ：这是一个小巧温馨的空间，以使用来自比利时烘焙商 Caffènation 的咖啡豆精心制作咖啡而闻名

**2\. 十美女 ⭐⭐⭐⭐⭐**

- **Multiple locations**:
	- 巴黎市10区格兰奇奥贝尔街10号，邮编75010（圣马丁运河）
	- 巴士底狱：巴黎布雷盖街17 - 19号，75011巴黎
	- 圣日耳曼：位于第六区
- **工作时间** ：通常为上午 8:00 至下午 5:00（因地点而异）
- **特色** ：自有咖啡烘焙工坊，提供优质的酸面团面包和糕点
- **其特别之处** ：受澳大利亚影响的咖啡馆，提供一流的咖啡和美食

**3\. 乐骑咖啡馆 ⭐⭐⭐⭐**

- **地址** ：路易 - 菲利普桥街，玛莱区（第四区）
- **特色** ：咖啡与自行车租赁 - 独特概念
- **它的特别之处** ：位于玛莱区中心地带，将优质咖啡与自行车租赁服务相结合

**4\. 花神咖啡馆⭐⭐⭐⭐（历史悠久）**

- **地址** ：圣日耳曼大道 172 号，75006 巴黎（第 6 区）
- **营业时间** ：每日上午 7:30 至凌晨 1:30
- **其特别之处** ：曾有萨特和波伏娃等知识分子常去光顾的传奇咖啡馆

**5\. 双叟咖啡馆 ⭐⭐⭐⭐（历史悠久）**

- **地址** ：巴黎圣日耳曼德佩广场，75006 巴黎（第 6 区）
- **营业时间** ：每日上午 7:30 至凌晨 1:00
- **其特别之处** ：标志性的文学咖啡馆，设有户外露台，是观察巴黎生活的绝佳场所

#### Insights

- **第三波咖啡运动** ：巴黎已经通过像贝维尔烘焙坊（Belleville Brûlerie）、游击咖啡（Partisan）和 KB 咖啡烘焙（KB Coffee Roasters）这样的当地烘焙商，全面接受了精品咖啡文化
- **地理分布** ：玛莱区（第 3 - 4 区）和圣马丁运河（第 10 区）有大量时尚的咖啡店
- **咖啡文化的演变** ：传统咖啡馆文化与现代精品咖啡完美共存

#### Practical Tips

- **营业时间** ：大多数特色咖啡店比传统咖啡馆关门更早（通常下午 4 点至 5 点）
- **价格** ：特色咖啡店的浓缩咖啡饮品售价为 3 至 5 欧元，传统咖啡馆则为 1.50 至 3 欧元。
- **语言** ：特色咖啡店的咖啡师通常会说英语；友好地说一声“bonjour”（法语：你好）会很有帮助
- \*\*最佳时间\*\*：上午去特色商店逛逛，品尝最新鲜的咖啡，感受最佳氛围

## Best Practices

### 查询优化

- 明确位置和偏好
- 包括“适合家庭”或“经济实惠”等背景信息
- 在相关时提及接近度要求

### 2\. 工具选择策略

- 首先使用 `location_query` 进行发现
- 使用 `internet_search` 进行验证和获取上下文信息
- 结合见解以提供全面的推荐

### 3\. Error Handling

```
def robust_location_query(query: str, max_results: int = 5):
    try:
        response = camino_client.query(query, limit=max_results)
        if not response.get('results'):
            return f"No locations found for: {query}"
        return response
    except APIError as e:
        return f"Location service temporarily unavailable: {str(e)}"
```

## Cost Optimization

- **Camino AI** ：每次查询 0.001 美元（比谷歌地图便宜 1000 倍）
- **塔维利** ：按搜索付费模式
- **Anthropic** ：基于使用量的定价

组合成本通常低于每复杂研究查询0.01美元。

## Deployment Options

### Local Development

```
export CAMINO_API_KEY="your_camino_key"
export TAVILY_API_KEY="your_tavily_key"
export ANTHROPIC_API_KEY="your_anthropic_key"
python location_agent.py
```

### 生产部署

- 部署在 AWS Lambda、谷歌云函数或类似服务上
- 使用环境变量进行 API 密钥管理
- 为频繁请求的位置实现缓存
- 添加速率限制和使用情况监控

## Get Started Today

准备好构建位置智能代理了吗？

1. **获取您的 Camino AI API 密钥** ： [app.getcamino.ai](https://app.getcamino.ai/)
2. **安装包** ： `pip install deepagents camino-ai-sdk tavily-python python-dotenv`
3. **复制上面的代码** 并开始实验
4. **加入我们的社区** ：分享你的构建并获得帮助

***关于 Camino AI** ：我们为人工智能代理提供价格亲民的位置智能应用程序编程接口，提供自然语言处理、路径规划和空间推理功能，成本比传统替代品低 17 倍。*