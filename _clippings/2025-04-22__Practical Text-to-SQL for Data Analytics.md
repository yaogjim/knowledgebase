---
title: "Practical Text-to-SQL for Data Analytics"
source: "https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics"
author:
published: 2025-07-11
created: 2025-04-22
description:
tags:
  - "clippings"
---
[Skip to main content](https://www.linkedin.com/blog/engineering/ai/#lithograph-app)

[人工智能](https://www.linkedin.com/blog/engineering/artificial-intelligence)

## 用于数据分析的实用文本到 SQL 转换

[Authored by 陈艾伯特](https://www.linkedin.com/in/albertcc)

2024 年 12 月 9 日

共同作者：Albert Chen、Manas Bundele、Gaurav Ahlawat、Patrick Stetz、Zhitao (James) W.、Qiang Fei、Don Jung、Audrey Chu、Bharadwaj Jayaraman、Ayushi Panth、Yatin Arora、Sourav Jain、Renjith Varma、Alex Ilin、Iuliia Melnychuk 🇺🇦、Chelsea C.、Joyan Sil 和 Xiaofeng Wang

![Typical user interaction with SQL Bot](https://media.licdn.com/dms/image/v2/D4D08AQHqXsGS6_tDzw/croft-frontend-shrinkToFit1024/croft-frontend-shrinkToFit1024/0/1733409700827?e=2147483647&v=beta&t=tcREkjBt6w8H4NKujpmpmwQHUz0IRE2reZVqTG3exVw)

图 1：与 SQL Bot 的典型用户交互

![Knowledge graph. Users, table clusters, tables, and fields are nodes. The nodes have attributes derived from DataHub, query logs, crowdsourced domain knowledge, etc.](https://media.licdn.com/dms/image/v2/D4D08AQGpwSLogeNOxQ/croft-frontend-shrinkToFit1024/croft-frontend-shrinkToFit1024/0/1733409778600?e=2147483647&v=beta&t=HVJZuhhXaW9ZrpWjjT4TliZDrIKqCnCxOZnEiUc4Vr8)

图 2：知识图谱。用户、表集群、表和字段是节点。这些节点具有从数据中心、查询日志、众包领域知识等派生的属性。

![Modeling architecture. The user’s question is classified and delegated to the appropriate flow. Open-ended follow-up chats are handled by an agent.](https://media.licdn.com/dms/image/v2/D4D08AQFs4aVHGWNHnQ/croft-frontend-shrinkToFit1024/croft-frontend-shrinkToFit1024/0/1733776847861?e=2147483647&v=beta&t=K-CEVLdprBTUMf3PUzVdr4Xs_D_t6C_eJijrhi1dtMM)

图 3：建模架构。用户的问题被分类并分配到适当的流程。开放式后续聊天由代理处理。

图 4：用户界面中的丰富显示元素有助于用户理解推荐表。

图 5：查询输出包括验证检查、解释和表格。

领英的每个数据集都有自己的访问控制列表，该列表仅允许特定用户或组对数据集进行读取访问。为防止用户运行查询时被拒绝访问的情况，我们会检查用户是否是具有适当访问权限的组的成员，如果是，我们会自动提供利用该组凭证所需的代码。这减少了用户的挫败感，尤其是对于领英新接触 SQL 的用户。

## 策略#4：用户定制选项

我们希望用户能够在不向平台团队提出请求的情况下提高 SQL Bot 的性能。为此，我们提供了三个控制手段，使用户能够针对其产品领域定制体验：  

1. 数据集定制：用户可以通过提供电子邮件组或明确指定要使用的用户和数据集，为某个产品领域定义数据集。该产品领域的数据集是该领域用户组通常使用的数据集，并可选择按指定包含或排除其他数据集。用户可以通过用户界面选择要使用的产品领域。
2. 自定义说明：用户可以直接在 DARWIN 中向 SQL Bot 提供自定义文本说明。这些说明既可以丰富 SQL Bot 的整体领域知识，也可以为 SQL Bot 提供特定行为的指导方针，以匹配用户偏好。在选择表和字段以及编写和修复查询时，会使用用户提供的说明。
3. 示例查询：用户可以创建示例查询，以便编入我们的向量存储中。可以通过创建一个笔记本并将其标记为“已认证”，直接在达尔文系统中添加这些查询。

## 策略#5：持续对标

该机器人有许多超参数，例如要嵌入什么文本、要传递给每个LLM的上下文是什么、如何表示上下文和元提示、如何管理智能体内存、要检索多少项、要运行多少次自我校正以及模型架构中要包含哪些步骤。因此，开发一个基准集来评估质量和性能至关重要。  

基准测试最好针对特定应用进行定制，因为文本到 SQL 的要求可能因目标用户、数据集数量、表名和列名的清晰度、所需查询的复杂性、SQL 方言、目标响应时间以及所需的专业领域知识程度等因素而有很大差异。我们与 10 个产品领域的领域专家合作，定义了一组超过 130 个基准问题。每个问题都包括一个表述清晰的问题和正确答案。  

我们的评估指标包括与真实情况相比的表和字段召回率、表/字段幻觉率、语法正确性和响应延迟。这些指标易于计算，在开发的第一阶段，当我们致力于找到正确的表/字段并避免明显的查询问题时，我们重点关注了这些指标。  

例如，此图表显示了通过添加重排器、描述和示例查询，表格召回率的提升情况：

图 6：重新排序器、描述和示例查询有助于 SQL Bot 识别正确的表。

但是，这些指标不足以评估查询准确性。为此，我们结合人工评估和以LLM作为评判标准，根据问题、表模式和基本事实来评估回答。评分标准包括整体分数以及在表、列、连接、过滤器、聚合等方面的正确性维度，以及回答在效率和复杂性方面的质量。这种方法对我们来说比运行 SQL 查询并比较输出更实用，因为它不需要数据访问，使我们能够评估查询与正确答案的接近程度，并深入了解如何改进模型。  

我们很早就发现，回答一个问题可能有多种方式。现在，我们约 60%的基准问题都有多个答案。如果没有这些额外的答案，我们召回率的报告就会少报 10%-15%。我们每三个月进行一次专家人工审核，将被接受的答案添加到我们的基准中。LLM-as-a-judge 有助于这个过程：我们发现，它在 75%的情况下返回的分数与人工评分相差在 1 分以内，较大的分歧往往表明我们的状态跟踪（SOT）中没有正确答案。我们要求专家审查这些情况，并在需要时更新我们的基准。

## 结论

在过去一年多的时间里，我们通过一个在我们的优先产品领域拥有专业知识的虚拟团队构建了 SQL Bot。我们早期的试点项目引起了用户的极大兴趣，并且在集成到 DARWIN 后的几个月里，我们看到了持续的应用。在最近的一项调查中，约 95%的人将 SQL Bot 的查询准确性评为“及格”或更高，约 40%的人将查询准确性评为“非常好”或“优秀”。  

展望未来，存在改善用户体验的机会，例如通过更快的响应时间、在线查询修订、展示 SQL Bot 用于回答问题的上下文以及随着时间的推移从用户交互中学习。此外，通过确定倡导者来领导各自领域内的自助式上下文管理工作，有助于提高语义准确性。  

一个收获是，“使用人工智能修复”功能易于开发，但使用率非常高——占我们会话的 80%——经常为用户节省调试查询的时间。识别这样的高投资回报率痛点是开始文本到 SQL 之旅的一个好起点。

## 致谢

感谢工程/产品部门参与该项目的所有贡献者，包括 Michael Cheng、Clarisse Rahbar、Sparsh Agarwal、Manohar Mohan Rao、Paul Lee、Vishal Chandawarkar。  

感谢 Trino 专家们集思广益、编写查询计划解析器并审阅这篇博客文章：Erik Krogen、Slim Bouguerra。  

感谢数据科学专家精心整理基准数据集并评估查询准确性：卡维·谭、安德鲁·贾巴拉、诺拉·吴、郭若云、史蒂夫·纳、阿希什·特里帕蒂、迈克尔·科斯克、陈凌军、科尔·席尔瓦、纪斐然、罗珍妮特、富兰克林·马什、杨梦瑶、林涛、朱焕奇、保罗·马齐拉斯、安德鲁·柯克。  

感谢工程合作伙伴提供用于知识图谱构建的 API：Shailesh Jannu、Na Zhang、Leo Sun、Alex Bachuk、Steve Calvert。  

感谢领导对本项目的支持：徐亚、李政、丁佳、黄国宁、Harikumar Velayutham、Shishir Sathe、Justin Dyer。  

主题：生成式人工智能 人工智能 数据管理 数据科学

- [产品设计](https://www.linkedin.com/blog/engineering/product-design)
	[使用 Ju...构建协作式提示工程游乐场](https://www.linkedin.com/blog/engineering/product-design/building-collaborative-prompt-engineering-playgrounds-using-jupyter-notebook)
	阿贾伊·普拉卡什 2025 年 2 月 13 日
	![](https://media.licdn.com/dms/image/v2/D4D08AQGjTYbN5UtiOg/croft-frontend-shrinkToFit767/B4DZT8ALjpGkAQ-/0/1739394694227?e=2147483647&v=beta&t=LJd4SIgJx9IY4Rdw7d2Rk7ZiiCRkZDBBMsbWQ8KF_5w)
- [营销](https://www.linkedin.com/blog/engineering/marketing)
	[通过数据驱动的归因分析获得的买家旅程洞察](https://www.linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution)
	约翰·本奇纳 2025 年 1 月 22 日
	![](https://media.licdn.com/dms/image/v2/D4D08AQGkfqQ8hTSyDQ/croft-frontend-shrinkToFit1024/croft-frontend-shrinkToFit1024/0/1727903865702?e=2147483647&v=beta&t=G6jwkQKs9ofiIlXDmks9sa7HK-CWm_OMYJ7D0cLAJ-I)
- [生成式人工智能](https://www.linkedin.com/blog/engineering/generative-ai)
	[我们如何构建适应领域的基础生成式人工智能模型来推动……](https://www.linkedin.com/blog/engineering/generative-ai/how-we-built-domain-adapted-foundation-genai-models-to-power-our-platform)
	普拉文·库马尔·博迪古特拉 2024 年 12 月 18 日
	![](https://media.licdn.com/dms/image/v2/D4D08AQFyupxn30RDCw/croft-frontend-shrinkToFit1024/croft-frontend-shrinkToFit1024/0/1734471896974?e=2147483647&v=beta&t=dJ31oHKPaFH1BtaVGQc4IuOzz-0lbRsc362ZwEHco80)