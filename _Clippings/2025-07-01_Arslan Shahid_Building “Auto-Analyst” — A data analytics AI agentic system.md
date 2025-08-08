---
title: "Building “Auto-Analyst” — A data analytics AI agentic system"
source: "https://www.firebird-technologies.com/p/building-auto-analyst-a-data-analytics"
author:
  - "[[Arslan Shahid]]"
published: 2024-09-01
created: 2025-07-01
description: "A technical guide on making a AI ‘Auto-Analyst’"
tags:
  - "clippings"
---
### 打造人工智能“自动分析师”的技术指南

![](https://substackcdn.com/image/fetch/$s_!v-CY!)

我一直在开发由人工智能驱动的智能体，以减轻我作为数据科学家/分析师的工作量。虽然流行文化经常展示人工智能取代人类工作，但在现实中，大多数人工智能智能体并不是人类的替代品。相反，它们帮助我们更高效地工作。这个智能体就是为此而设计的。此前，我设计了一个数据可视化智能体，它仅使用自然语言输入就能帮助我更快地制作可视化图表。

## Design

![](https://substackcdn.com/image/fetch/$s_!MrCz!)

作者提供的图片

流程图展示了一个从用户定义目标开始的系统。然后，规划器代理将任务委托给一组工作器代理，每个工作器代理负责生成代码以解决问题的特定部分。最后，所有单独的代码片段由代码组合器代理收集并整合，从而产生一个完成整个目标的单一、连贯的脚本。

***注意：规划器智能体可以将任务委托给部分智能体，不一定是全部。此外，每个智能体都有自己的一组输入，图中未显示。***

> 想找人帮你设计和构建人工智能代理吗？或者你正在构建的代理/RAG 应用程序遇到了问题。  
> [随时联系：](https://tally.so/r/3x9bgo)

## 单个组件

这篇博客文章将逐步指导你构建该智能体，为每个单独的组件展示代码块。在接下来的部分，我们将演示这些部分是如何无缝集成的。

## 规划器智能体

规划器智能体接收三个输入，即用户定义的目标、可用数据集和智能体描述。它以如下格式输出一个计划：

智能体1 -> 智能体2 -> 智能体3…

```markup
# You can use other orchestration libraries but I found DSPy
# good for building fast, simpler and evaluation (making the application more relibale)
import dspy

# This object inherits from the dspy.Signature class
# The text inside """ is the prompt
class analytical_planner(dspy.Signature):
    """ You are data analytics planner agent. You have access to three inputs
    1. Datasets
    2. Data Agent descriptions
    3. User-defined Goal
    You take these three inputs to develop a comprehensive plan to achieve the user-defined goal from the data & Agents available.
    In case you think the user-defined goal is infeasible you can ask the user to redefine or add more description to the goal.

    Give your output in this format:
    plan: Agent1->Agent2->Agent3
    plan_desc = Use Agent 1 for this reason, then agent2 for this reason and lastly agent3 for this reason.

    You don't have to use all the agents in response of the query
    
    """
# Input fields and their descriptions
    dataset = dspy.InputField(desc="Available datasets loaded in the system, use this df_name,columns  set df as copy of df_name")
    Agent_desc = dspy.InputField(desc= "The agents available in the system")
    goal = dspy.InputField(desc="The user defined goal ")
# Output fields and their description
    plan = dspy.OutputField(desc="The plan that would achieve the user defined goal")
    plan_desc= dspy.OutputField(desc="The reasoning behind the chosen plan")
```

![](https://www.firebird-technologies.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/fba2145c-efd5-4597-a817-912b125a1395_788x153.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:153,%22width%22:788,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:%22%22,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

规划器智能体的示例输出

## 分析代理

大多数分析代理都有一个共同的结构，只是在提示方面略有不同。它们接受两个输入：用户定义的目标和数据集索引。它们产生两个输出：分析代码和注释，这对于调试或重新引导代理可能很有用。

```markup
# I define analysis agents as those agents that are in the middle-layer
# they produce code for a specialised data analysis task
class preprocessing_agent(dspy.Signature):
    """ You are a data pre-processing agent, your job is to take a user-defined goal and available dataset,
    to build an exploratory analytics pipeline. You do this by outputing the required Python code. 
    You will only use numpy and pandas, to perform pre-processing and introductory analysis

    """
    dataset = dspy.InputField(desc="Available datasets loaded in the system, use this df_name,columns  set df as copy of df_name")
    goal = dspy.InputField(desc="The user defined goal ")
    commentary = dspy.OutputField(desc="The comments about what analysis is being performed")
    code = dspy.OutputField(desc ="The code that does the data preprocessing and introductory analysis")

class statistical_analytics_agent(dspy.Signature):
    """ You are a statistical analytics agent. 
    Your task is to take a dataset and a user-defined goal, and output 
    Python code that performs the appropriate statistical analysis to achieve that goal.
    You should use the Python statsmodel library"""
    dataset = dspy.InputField(desc="Available datasets loaded in the system, use this df_name,columns  set df as copy of df_name")
    goal = dspy.InputField(desc="The user defined goal for the analysis to be performed")
    commentary = dspy.OutputField(desc="The comments about what analysis is being performed")
    code = dspy.OutputField(desc ="The code that does the statistical analysis using statsmodel")

class sk_learn_agent(dspy.Signature):
# Prompt
    """You are a machine learning agent. 
    Your task is to take a dataset and a user-defined goal, and output Python code that performs the appropriate machine learning analysis to achieve that goal. 
    You should use the scikit-learn library."""
# Input Fields
    dataset = dspy.InputField(desc="Available datasets loaded in the system, use this df_name,columns. set df as copy of df_name")
    goal = dspy.InputField(desc="The user defined goal ")
# Output Fields
    commentary = dspy.OutputField(desc="The comments about what analysis is being performed")
    code = dspy.OutputField(desc ="The code that does the Exploratory data analysis")

## I worked on the data-viz agent and already optimized using DSPy.
## The only big difference is that this agents takes another input of styling index
```

![](https://www.firebird-technologies.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/39ba51c2-1a5c-49b3-8d0d-5e6f04f2a640_788x620.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:620,%22width%22:788,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:%22%22,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

其中一个智能体的示例输出

## 代码组合代理

此代理的目的是将所有代理的输出清理成一个连贯的脚本。它接收一长串代码列表，并输出代码。

```markup
class code_combiner_agent(dspy.Signature):
    """ You are a code combine agent, taking Python code output from many agents and combining the operations into 1 output
    You also fix any errors in the code"""
    agent_code_list =dspy.InputField(desc="A list of code given by each agent")
    refined_complete_code = dspy.OutputField(desc="Refined complete code base")
```

## 可选代理/索引

为了让智能体工作得更顺畅并捕捉一些错误，我还构建了这些额外的智能体或索引。

```markup
# The same signature used in Data Viz agent post
class Data_Viz(dspy.Signature):
    """
    You are AI agent who uses the goal to generate data visualizations in Plotly.
    You have to use the tools available to your disposal
    {dataframe_index}
    {styling_index}

    You must give an output as code, in case there is no relevant columns, just state that you don't have the relevant information
    """
    goal = dspy.InputField(desc="user defined goal which includes information about data and chart they want to plot")
    dataframe_context = dspy.InputField(desc=" Provides information about the data in the data frame. Only use column names and dataframe_name as in this context")
    styling_context = dspy.InputField(desc='Provides instructions on how to style your Plotly plots')
    code= dspy.OutputField(desc="Plotly code that visualizes what the user needs according to the query & dataframe_index & styling_context")

# An optional agent that checks if the user-defined goal works well
class goal_refiner_agent(dspy.Signature):
    """You take a user-defined goal given to a AI data analyst planner agent, 
    you make the goal more elaborate using the datasets available and agent_desc"""
    dataset = dspy.InputField(desc="Available datasets loaded in the system, use this df_name,columns  set df as copy of df_name")
    Agent_desc = dspy.InputField(desc= "The agents available in the system")
    goal = dspy.InputField(desc="The user defined goal ")
    refined_goal = dspy.OutputField(desc='Refined goal that helps the planner agent plan better')
```

我没有输入关于整个数据集的信息，而是构建了一个检索器，它接收有关可用数据的信息。

```markup
# I choose a LLama-Index based retriever as it was more convenient.
# Basically you can feed your data in a multiple ways.
# Providing description about column names, dataframe reference
# And also what purpose the data was collected etc.
dataframe_index =  VectorStoreIndex.from_documents(docs)

# I also defined a styling index for the data visualization agent.
# Which has natural language instructions on how to style different visualizations
style_index =  VectorStoreIndex.from_documents(styling_instructions)
```

## 将所有内容整合为一个系统

在 DSPy 中，要编译一个复杂的 LLM 应用程序，你需要定义一个包含两个基本方法的模块：\`\_\_init\_\_\` 和 \`forward\`。

\_\_init\_\_ ` 方法通过定义整个过程中将会使用的所有变量来初始化模块。然而，` `forward 方法才是实现核心功能的地方。此方法概述了一个组件的输出如何与其他组件交互，从而有效地驱动应用程序的逻辑。`

```markup
# This module takes only one input on initiation
class auto_analyst(dspy.Module):
    def __init__(self,agents):
# Defines the available agents, their inputs, and description
        self.agents = {}
        self.agent_inputs ={}
        self.agent_desc =[]
        i =0
        for a in agents:
            name = a.__pydantic_core_schema__['schema']['model_name']
# Using CoT prompting as from experience it helps generate better responses
            self.agents[name] = dspy.ChainOfThought(a)
            agent_inputs[name] ={x.strip() for x in str(agents[i].__pydantic_core_schema__['cls']).split('->')[0].split('(')[1].split(',')}
            self.agent_desc.append(str(a.__pydantic_core_schema__['cls']))
            i+=1
# Defining the planner, refine_goal & code combiner agents seperately
# as they don't generate the code & analysis they help in planning, 
# getting better goals & combine the code
        self.planner = dspy.ChainOfThought(analytical_planner)
        self.refine_goal = dspy.ChainOfThought(goal_refiner_agent)
        self.code_combiner_agent = dspy.ChainOfThought(code_combiner_agent)
# these two retrievers are defined using llama-index retrievers
# you can customize this depending on how you want your agents
        self.dataset =dataframe_index.as_retriever(k=1)
        self.styling_index = style_index.as_retriever(similarity_top_k=1)
        
    def forward(self, query):
# This dict is used to quickly pass arguments for agent inputs
        dict_ ={}
# retrieves the relevant context to the query
        dict_['dataset'] = self.dataset.retrieve(query)[0].text
        dict_['styling_index'] = self.styling_index.retrieve(query)[0].text
        dict_['goal']=query
        dict_['Agent_desc'] = str(self.agent_desc)
# output_dictionary that stores all agent outputs
        output_dict ={}
# this comes up with the plan
        plan = self.planner(goal =dict_['goal'], dataset=dict_['dataset'], Agent_desc=dict_['Agent_desc'] )
        output_dict['analytical_planner'] = plan
        plan_list =[]
        code_list =[]
# if the planner worked as intended it should give agents seperated by ->
        if plan.plan.split('->'):
            plan_list = plan.plan.split('->')
# in case the goal is unclear, it sends it to refined goal agent
        else:
            refined_goal = self.refine_goal(dataset=data, goal=goal, Agent_desc= self.agent_desc)
            forward(query=refined_goal)
# passes the goal and other inputs to all respective agents in the plan
        for p in plan_list:
            inputs = {x:dict_[x] for x in agent_inputs[p.strip()]}
            output_dict[p.strip()]=self.agents[p.strip()](**inputs)
# creates a list of all the generated code, to be combined as 1 script
            code_list.append(output_dict[p.strip()].code)
# Stores the last output
        output_dict['code_combiner_agent'] = self.code_combiner_agent(agent_code_list = str(code_list))
        
        return output_dict
# you can store all available agent signatures as a list
agents =[preprocessing_agent, statistical_analytics_agent, sk_learn_agent,data_viz_agent]

# Define the agentic system
auto_analyst_system = auto_analyst(agents)

# the system is preloaded with Chicago crime data
goal = "What is the cause of crime in Chicago?"

# Asking the agentic system to perform analysis for this query
output = auto_analyst_system(query = goal)
```

现在逐步查看查询结果。

*对于这个查询 = “芝加哥犯罪的原因是什么？”*

![](https://www.firebird-technologies.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/a4c23219-188a-435c-bbdf-77173f286a24_788x127.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:127,%22width%22:788,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:%22%22,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

规划器智能体输出，推荐预处理智能体->统计智能体->数据可视化智能体

执行计划，首先是预处理代理

![](https://www.firebird-technologies.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/9f337673-cee9-46f9-a020-ea264618e54f_788x527.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:527,%22width%22:788,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:%22%22,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

从评论和推理中可以看出，它会清理数据并进行一些基于计数的基本分析。

下一个统计分析代理

![](https://www.firebird-technologies.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/84ecdd49-8d48-4785-9b9d-a8e3954e390c_788x486.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:486,%22width%22:788,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:%22%22,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

智能体构建了一个 ARIMA 模型来分析犯罪数量随时间的变化。

接下来是 Plotly 数据可视化代理

![](https://www.firebird-technologies.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/b82bd74c-dcd2-432e-a842-89b86f93cbd7_788x380.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:380,%22width%22:788,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:%22%22,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

构建一个类似热力图的可视化效果。

最后，代码组合代理，将所有内容整合在一起

![](https://www.firebird-technologies.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/679797e2-f40e-4373-9891-ed30e4e286a2_788x707.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:707,%22width%22:788,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:%22%22,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

结合了预处理、ARIMA 模型和 Plotly 可视化

这是执行上一个智能体的代码后得到的输出。

![](https://www.firebird-technologies.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/2f2912d4-5c67-4c34-acc3-93033dd68d0b_788x901.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:901,%22width%22:788,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:%22%22,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

输出的前半部分

![](https://www.firebird-technologies.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/7157640f-1ab7-401a-9bdb-005876cbf881_788x1115.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:1115,%22width%22:788,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:%22%22,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

所有由智能体生成的输出

> 看起来很酷，对吧？想让我帮你设计、实现和评估人工智能智能体吗？点击这里：

## 局限性

和许多智能体一样，当它按预期运行时，表现出色。这只是我计划随着时间不断改进的一个项目的首次迭代。请关注我和火鸟科技以获取最新消息。以下是目前的局限性：

1. **幻觉** ：由于幻觉，该智能体有时会生成无法执行的代码。
2. **不可靠/不一致** ：智能体的输出不一致，相同查询的不同变体产生的代码差异显著。
3. **混合输出** ：许多智能体并非专门处理问题的不同方面。例如，数据预处理智能体生成它自己的可视化结果，而数据可视化智能体也会创建它自己的可视化结果。

## 后续步骤

这是一个正在进行的项目；这些是我接下来可能会采取的改进智能体的步骤

1. **优化签名/提示** ：DSPy 旨在评估 LLM 应用程序，这只是实现过程，接下来我得找出最佳前缀、签名和提示。
2. **添加护栏：** 自动修复智能体生成的代码是许多其他智能体系统中使用的一种解决方案。尝试限制提示注入攻击也在规划之中
3. **添加记忆/交互：** 此智能体一步完成所有操作，而且各个组件之间不存在交互，它们无法看到彼此的输出。
4. **构建用户界面：** 目前我只构建了代理后端用于进一步测试并收集用户反馈，之后我会构建一个用户界面。
