# AI对冲基金技术文档

## 1. 技术概述

### a. 系统架构图

```
+-----------------------+
|      AI对冲基金系统    |
+-----------------------+
           |
           v
+-----------------------+
|      市场数据代理      |
+-----------------------+
           |
           v
+-----------------------+        +-----------------------+
|   定量分析代理        | ------>|  风险管理代理         |
+-----------------------+        +-----------------------+
                                      |
                                      v
                             +-----------------------+
                             |  组合管理代理         |
                             +-----------------------+
                                      |
                                      v
                             +-----------------------+
                             |      订单执行         |
                             +-----------------------+
```

### b. 组件功能概述及相互关系图

```
+-------------------+    收集和预处理市场数据    +-------------------------+
|   市场数据代理    | ------------------------> |     定量分析代理         |
+-------------------+                             +-------------------------+
                                                         |
                                                         |  生成交易信号
                                                         v
                                                +-------------------------+
                                                |    基础分析代理          |
                                                +-------------------------+
                                                         |
                                                         |  风险评估
                                                         v
                                                +-------------------------+
                                                |   风险管理代理           |
                                                +-------------------------+
                                                         |
                                                         |  生成交易决策
                                                         v
                                                +-------------------------+
                                                |  组合管理代理           |
                                                +-------------------------+
```

### c. 主要组件功能和职责详解

#### 市场数据代理（Market Data Agent）

**概要**：负责收集和预处理指定股票的历史市场数据和财务指标。

**输入**：
- 股票代码（ticker）
- 起始日期（start_date）
- 结束日期（end_date）

**输出**：
- 价格数据（prices）
- 财务指标（financial_metrics）

**依赖关系**：
- `src/tools.py` 中的 `get_prices` 和 `get_financial_metrics` 函数

**关键接口**：
- `market_data_agent(state: AgentState)`

**数据流**：
输入的股票代码和日期范围，通过API获取价格和财务数据，并将其存储在状态中供后续代理使用。

#### 定量分析代理（Quantitative Agent）

**概要**：分析技术指标并生成交易信号。

**输入**：
- 价格数据（prices）

**输出**：
- 综合交易信号（信号类型和置信度）
- 各技术指标的具体分析和理由

**依赖关系**：
- `src/tools.py` 中的各类计算函数（如 `calculate_macd`，`calculate_rsi` 等）

**关键接口**：
- `quant_agent(state: AgentState)`

**数据流**：
使用价格数据计算技术指标，生成对应的交易信号，并将分析结果存储在状态中。

#### 基础分析代理（Fundamentals Agent）

**概要**：分析财务指标并生成交易信号。

**输入**：
- 财务指标数据（financial_metrics）

**输出**：
- 综合交易信号（信号类型和置信度）
- 各财务指标的具体分析和理由

**依赖关系**：
- `src/tools.py` 中的 `calculate_*` 函数

**关键接口**：
- `fundamentals_agent(state: AgentState)`

**数据流**：
使用财务数据评估企业的盈利能力、增长性、财务健康状况及估值水平，生成交易信号并存储在状态中。

#### 风险管理代理（Risk Management Agent）

**概要**：评估组合风险并设置仓位限制。

**输入**：
- 定量分析代理和基础分析代理的交易信号
- 当前投资组合状态

**输出**：
- 最大仓位大小
- 风险评分
- 交易行动建议（买入、卖出或持有）
- 交易决策的理由

**依赖关系**：
- 使用 `langchain` 和 `langchain-openai` 库与LLM交互生成风险评估

**关键接口**：
- `risk_management_agent(state: AgentState)`

**数据流**：
综合前置分析代理的交易信号及当前组合状态，通过语言模型生成风险评估和交易建议，并将结果存储在状态中。

#### 组合管理代理（Portfolio Management Agent）

**概要**：基于团队分析和风险评估做出最终的交易决策并生成订单。

**输入**：
- 定量分析代理、基础分析代理及风险管理代理的交易信号
- 当前投资组合状态

**输出**：
- 最终交易行动（买入、卖出或持有）
- 交易数量
- 交易决策的理由

**依赖关系**：
- 使用 `langchain` 和 `langchain-openai` 库与LLM交互生成组合决策

**关键接口**：
- `portfolio_management_agent(state: AgentState)`

**数据流**：
综合所有前置代理的分析和风险评估，通过语言模型生成最终的交易决策，并将结果存储在状态中。

### d. 组件交互过程详细说明

1. **市场数据代理**：系统的入口点，接收股票代码和日期范围，调用API获取历史价格数据和财务指标，将数据存储在状态中。

2. **定量分析代理**：使用市场数据代理提供的价格数据，计算技术指标（如MACD、RSI、布林带和OBV），生成相应的交易信号及理由，并将结果存储在状态中。

3. **基础分析代理**：利用市场数据代理提供的财务指标，评估公司的盈利能力、成长性、财务健康状况及估值水平，生成交易信号及理由，并将结果存储在状态中。

4. **风险管理代理**：综合定量分析代理和基础分析代理生成的交易信号，以及当前的投资组合状态，评估组合风险，设置最大仓位大小，生成交易行动建议，并将结果存储在状态中。

5. **组合管理代理**：在风险管理代理的基础上，结合所有交易信号和当前组合状态，做出最终的交易决策（买入、卖出或持有），并生成具体的交易订单。

6. **最终结果**：组合管理代理的决策被输出，可以用于实际交易或后续分析。

### e. 开发环境和设置要求

**开发环境**：
- **操作系统**：跨平台（Windows, macOS, Linux）
- **编程语言**：Python 3.9+
- **包管理工具**：Poetry

**设置要求**：

1. **克隆仓库**：
    ```bash
    git clone https://github.com/your-repo/ai-hedge-fund.git
    cd ai-hedge-fund
    ```

2. **安装Poetry**（如果未安装）：
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **安装依赖**：
    ```bash
    poetry install
    ```

4. **配置环境变量**：
    - 复制示例环境变量文件：
        ```bash
        cp .env.example .env
        ```
    - 编辑 `.env` 文件，填入实际的 `OPENAI_API_KEY` 和 `FINANCIAL_DATASETS_API_KEY`。

5. **依赖的关键库**：
    - `langchain` 和 `langchain-openai` 用于与语言模型交互
    - `pandas`, `numpy` 进行数据处理
    - `matplotlib` 用于可视化
    - `python-dotenv` 管理环境变量

## 2. 关键实现细节

### a. 重要代码特性

- **多代理架构**：系统采用多个专门的代理（Market Data、Quantitative、Fundamentals、Risk Management、Portfolio Management）协同工作，实现复杂的交易决策。
- **技术与基础分析结合**：结合技术指标（MACD、RSI、布林带、OBV）和财务指标进行全面分析。
- **使用语言模型**：通过 `langchain` 与 OpenAI 的语言模型交互，生成风险评估和交易决策。
- **回测功能**：提供强大的回测能力，能够模拟历史交易并分析绩效。
- **模块化设计**：代码结构清晰，各组件职责分明，便于维护和扩展。

### b. 核心特性代码片段及解释

#### 1. 市场数据代理

**代码片段**：
```python
def market_data_agent(state: AgentState):
    """负责收集和预处理市场数据"""
    messages = state["messages"]
    data = state["data"]

    # 设置默认日期
    end_date = data["end_date"] or datetime.now().strftime('%Y-%m-%d')
    if not data["start_date"]:
        # 计算结束日期前三个月的起始日期
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        start_date = end_date_obj.replace(month=end_date_obj.month - 3) if end_date_obj.month > 3 else \
            end_date_obj.replace(year=end_date_obj.year - 1, month=end_date_obj.month + 9)
        start_date = start_date.strftime('%Y-%m-%d')
    else:
        start_date = data["start_date"]

    # 获取历史价格数据
    prices = get_prices(
        ticker=data["ticker"], 
        start_date=start_date, 
        end_date=end_date,
    )

    # 获取财务指标
    financial_metrics = get_financial_metrics(
        ticker=data["ticker"], 
        report_period=end_date, 
        period='ttm', 
        limit=1,
    )

    return {
        "messages": messages,
        "data": {
            **data, 
            "prices": prices, 
            "start_date": start_date, 
            "end_date": end_date,
            "financial_metrics": financial_metrics,
        }
    }
```

**实现解释**：

- **函数用途**：`market_data_agent` 负责从API获取指定股票的历史价格数据和财务指标，并将其存储在状态中供后续代理使用。
- **主要变量**：
  - `state`: 包含当前消息和数据的状态字典。
  - `end_date` 和 `start_date`: 确定数据获取的时间范围。
  - `prices`: 从金融数据API获取的历史价格数据。
  - `financial_metrics`: 从金融数据API获取的最新财务指标。
- **控制流程**：
  1. 确定数据获取的起始日期和结束日期。
  2. 调用 `get_prices` 获取历史价格数据。
  3. 调用 `get_financial_metrics` 获取财务指标。
  4. 将获取的数据更新到状态中并返回。

#### 2. 定量分析代理

**代码片段**：
```python
def quant_agent(state: AgentState):
    """分析技术指标并生成交易信号。"""
    show_reasoning = state["metadata"]["show_reasoning"]

    data = state["data"]
    prices = data["prices"]
    prices_df = prices_to_df(prices)
    
    # 计算技术指标
    macd_line, signal_line = calculate_macd(prices_df)
    rsi = calculate_rsi(prices_df)
    upper_band, lower_band = calculate_bollinger_bands(prices_df)
    obv = calculate_obv(prices_df)
    
    # 生成单独的信号
    signals = []
    
    # MACD 信号
    if macd_line.iloc[-2] < signal_line.iloc[-2] and macd_line.iloc[-1] > signal_line.iloc[-1]:
        signals.append('bullish')
    elif macd_line.iloc[-2] > signal_line.iloc[-2] and macd_line.iloc[-1] < signal_line.iloc[-1]:
        signals.append('bearish')
    else:
        signals.append('neutral')
    
    # RSI 信号
    if rsi.iloc[-1] < 30:
        signals.append('bullish')
    elif rsi.iloc[-1] > 70:
        signals.append('bearish')
    else:
        signals.append('neutral')
    
    # 布林带信号
    current_price = prices_df['close'].iloc[-1]
    if current_price < lower_band.iloc[-1]:
        signals.append('bullish')
    elif current_price > upper_band.iloc[-1]:
        signals.append('bearish')
    else:
        signals.append('neutral')
    
    # OBV 信号
    obv_slope = obv.diff().iloc[-5:].mean()
    if obv_slope > 0:
        signals.append('bullish')
    elif obv_slope < 0:
        signals.append('bearish')
    else:
        signals.append('neutral')
    
    # 收集理由
    reasoning = {
        "MACD": {
            "signal": signals[0],
            "details": f"MACD线{'上穿' if signals[0] == 'bullish' else '下穿' if signals[0] == 'bearish' else '未穿越'}信号线"
        },
        "RSI": {
            "signal": signals[1],
            "details": f"RSI值为{rsi.iloc[-1]:.2f}，（{'超卖' if signals[1] == 'bullish' else '超买' if signals[1] == 'bearish' else '中性'})"
        },
        "Bollinger": {
            "signal": signals[2],
            "details": f"价格{'低于下轨' if signals[2] == 'bullish' else '高于上轨' if signals[2] == 'bearish' else '在轨道内'}"
        },
        "OBV": {
            "signal": signals[3],
            "details": f"OBV斜率为{obv_slope:.2f}（{'看涨' if signals[3] == 'bullish' else '看跌' if signals[3] == 'bearish' else '中性'})"
        }
    }
    
    # 确定整体信号
    bullish_signals = signals.count('bullish')
    bearish_signals = signals.count('bearish')
    
    if bullish_signals > bearish_signals:
        overall_signal = 'bullish'
    elif bearish_signals > bullish_signals:
        overall_signal = 'bearish'
    else:
        overall_signal = 'neutral'
    
    # 计算置信度
    total_signals = len(signals)
    confidence = max(bullish_signals, bearish_signals) / total_signals
    
    # 生成消息内容
    message_content = {
        "signal": overall_signal,
        "confidence": round(confidence, 2),
        "reasoning": reasoning
    }

    # 创建定量分析消息
    message = HumanMessage(
        content=str(message_content),  # 将字典转换为字符串
        name="quant_agent",
    )

    # 如果设置了显示理由，打印理由
    if show_reasoning:
        show_agent_reasoning(message_content, "Quant Agent")
    
    return {
        "messages": [message],
        "data": data,
    }
```

**实现解释**：

- **函数用途**：`quant_agent` 负责计算技术指标（MACD、RSI、布林带、OBV），生成相应的交易信号，并将结果存储在状态中。
- **主要变量**：
  - `show_reasoning`: 是否显示代理的推理过程。
  - `prices_df`: 通过 `prices_to_df` 函数将价格数据转换为DataFrame格式。
  - `macd_line`, `signal_line`, `rsi`, `upper_band`, `lower_band`, `obv`: 计算得到的各技术指标。
  - `signals`: 各技术指标生成的信号列表。
  - `reasoning`: 各技术指标生成信号的具体理由。
  - `message_content`: 综合交易信号及其置信度和理由。
- **控制流程**：
  1. 计算各技术指标。
  2. 根据指标的变化生成单独的交易信号（看涨、看跌、中性）。
  3. 收集每个指标的具体理由。
  4. 综合所有信号，确定整体交易信号和置信度。
  5. 创建并返回交易信号消息。

#### 3. 风险管理代理

**代码片段**：
```python
def risk_management_agent(state: AgentState):
    """评估组合风险并设置仓位限制"""
    show_reasoning = state["metadata"]["show_reasoning"]
    portfolio = state["data"]["portfolio"]
    
    # 获取定量分析和基础分析的消息
    quant_message = next(msg for msg in state["messages"] if msg.name == "quant_agent")
    fundamentals_message = next(msg for msg in state["messages"] if msg.name == "fundamentals_agent")

    # 创建提示模板
    template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a risk management specialist.
                Your job is to take a look at the trading analysis and
                evaluate portfolio exposure and recommend position sizing.
                Provide the following in your output (as a JSON):
                "max_position_size": <float greater than 0>,
                "risk_score": <integer between 1 and 10>,
                "trading_action": <buy | sell | hold>,
                "reasoning": <concise explanation of the decision>
                """
            ),
            (
                "human",
                f"""Based on the trading analysis below, provide your risk assessment.

                Quant Analysis Trading Signal: {quant_message.content}
                Fundamental Analysis Trading Signal: {fundamentals_message.content}

                Here is the current portfolio:
                Portfolio:
                Cash: {portfolio['cash']:.2f}
                Current Position: {portfolio['stock']} shares
                
                Only include the max position size, risk score, trading action, and reasoning in your JSON output.  Do not include any JSON markdown.
                """
            ),
        ]
    )

    # 生成提示
    prompt = template.invoke(
        {
            "quant_message": quant_message.content,
            "fundamentals_message": fundamentals_message.content,
            "portfolio_cash": f"{portfolio['cash']:.2f}",
            "portfolio_stock": portfolio["stock"]
        }
    )

    # 调用LLM生成结果
    result = llm.invoke(prompt)
    message = HumanMessage(
        content=result.content,
        name="risk_management_agent",
    )

    # 如果设置了显示理由，打印理由
    if show_reasoning:
        show_agent_reasoning(message.content, "Risk Management Agent")
    
    return {"messages": state["messages"] + [message]}
```

**实现解释**：

- **函数用途**：`risk_management_agent` 负责综合定量和基础分析的交易信号，评估当前投资组合的风险，推荐仓位大小，并给出交易行动建议。
- **主要变量**：
  - `show_reasoning`: 是否显示代理的推理过程。
  - `portfolio`: 当前投资组合，包括现金和股票持仓。
  - `quant_message`, `fundamentals_message`: 前置代理生成的交易信号消息。
  - `template`: 用于与语言模型交互的提示模板。
  - `prompt`: 生成的完整提示。
  - `result`: 语言模型生成的风险评估结果。
- **控制流程**：
  1. 获取定量分析和基础分析的交易信号。
  2. 创建与语言模型交互的提示模板，包含交易信号和当前组合状态。
  3. 调用语言模型生成风险评估结果。
  4. 创建并返回风险管理代理的消息。

#### 4. 回测功能

**代码片段**：
```python
class Backtester:
    def __init__(self, agent, ticker, start_date, end_date, initial_capital):
        self.agent = agent
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.portfolio = {"cash": initial_capital, "stock": 0}
        self.portfolio_values = []

    def parse_action(self, agent_output):
        try:
            # 期望代理输出JSON格式
            import json
            decision = json.loads(agent_output)
            return decision["action"], decision["quantity"]
        except:
            print(f"解析交易动作时出错: {agent_output}")
            return "hold", 0

    def execute_trade(self, action, quantity, current_price):
        """根据组合约束验证并执行交易"""
        if action == "buy" and quantity > 0:
            cost = quantity * current_price
            if cost <= self.portfolio["cash"]:
                self.portfolio["stock"] += quantity
                self.portfolio["cash"] -= cost
                return quantity
            else:
                # 计算最大可买数量
                max_quantity = self.portfolio["cash"] // current_price
                if max_quantity > 0:
                    self.portfolio["stock"] += max_quantity
                    self.portfolio["cash"] -= max_quantity * current_price
                    return max_quantity
                return 0
        elif action == "sell" and quantity > 0:
            quantity = min(quantity, self.portfolio["stock"])
            if quantity > 0:
                self.portfolio["cash"] += quantity * current_price
                self.portfolio["stock"] -= quantity
                return quantity
            return 0
        return 0

    def run_backtest(self):
        dates = pd.date_range(self.start_date, self.end_date, freq="B")

        print("\n开始回测...")
        print(f"{'日期':<12} {'股票':<6} {'操作':<6} {'数量':>8} {'价格':>8} {'现金':>12} {'持仓':>8} {'总价值':>12}")
        print("-" * 70)

        for current_date in dates:
            lookback_start = (current_date - timedelta(days=30)).strftime("%Y-%m-%d")
            current_date_str = current_date.strftime("%Y-%m-%d")

            agent_output = self.agent(
                ticker=self.ticker,
                start_date=lookback_start,
                end_date=current_date_str,
                portfolio=self.portfolio
            )

            action, quantity = self.parse_action(agent_output)
            df = get_price_data(self.ticker, lookback_start, current_date_str)
            current_price = df.iloc[-1]['close']

            # 执行交易
            executed_quantity = self.execute_trade(action, quantity, current_price)

            # 更新总组合价值
            total_value = self.portfolio["cash"] + self.portfolio["stock"] * current_price
            self.portfolio["portfolio_value"] = total_value

            # 记录当前状态
            print(
                f"{current_date.strftime('%Y-%m-%d'):<12} {self.ticker:<6} {action:<6} {executed_quantity:>8} {current_price:>8.2f} "
                f"{self.portfolio['cash']:>12.2f} {self.portfolio['stock']:>8} {total_value:>12.2f}"
            )

            # 记录组合价值
            self.portfolio_values.append(
                {"Date": current_date, "Portfolio Value": total_value}
            )

    def analyze_performance(self):
        # 将组合价值转换为DataFrame
        performance_df = pd.DataFrame(self.portfolio_values).set_index("Date")

        # 计算总回报
        total_return = (
                           self.portfolio["portfolio_value"] - self.initial_capital
                       ) / self.initial_capital
        print(f"总回报: {total_return * 100:.2f}%")

        # 绘制组合价值随时间变化
        performance_df["Portfolio Value"].plot(
            title="组合价值随时间变化", figsize=(12, 6)
        )
        plt.ylabel("组合价值 ($)")
        plt.xlabel("日期")
        plt.show()

        # 计算每日回报
        performance_df["Daily Return"] = performance_df["Portfolio Value"].pct_change()

        # 计算夏普比率（假设一年252个交易日）
        mean_daily_return = performance_df["Daily Return"].mean()
        std_daily_return = performance_df["Daily Return"].std()
        sharpe_ratio = (mean_daily_return / std_daily_return) * (252 ** 0.5)
        print(f"夏普比率: {sharpe_ratio:.2f}")

        # 计算最大回撤
        rolling_max = performance_df["Portfolio Value"].cummax()
        drawdown = performance_df["Portfolio Value"] / rolling_max - 1
        max_drawdown = drawdown.min()
        print(f"最大回撤: {max_drawdown * 100:.2f}%")

        return performance_df
```

**实现解释**：

- **类用途**：`Backtester` 类用于模拟历史交易，评估交易策略的绩效。
- **主要方法**：
  - `__init__`: 初始化回测所需的参数，包括代理函数、股票代码、日期范围和初始资本。
  - `parse_action`: 解析代理输出的交易动作和数量。
  - `execute_trade`: 根据当前组合状态和交易动作执行买卖操作，确保交易合法。
  - `run_backtest`: 按照指定日期范围逐日模拟交易过程，记录组合状态。
  - `analyze_performance`: 分析回测结果，计算总回报、夏普比率、最大回撤，并绘制组合价值曲线。

- **关键变量**：
  - `self.agent`: 用于生成交易决策的代理函数。
  - `self.portfolio`: 当前投资组合状态，包括现金和股票持仓。
  - `self.portfolio_values`: 记录每个交易日的组合价值。

- **控制流程**：
  1. 遍历回测期间的每个交易日。
  2. 对于每个日期，调用代理生成交易决策。
  3. 解析并执行交易，更新组合状态。
  4. 记录每日组合价值。
  5. 回测结束后，分析和展示绩效指标。

#### 5. 运行对冲基金

**代码片段**：
```python
def run_hedge_fund(ticker: str, start_date: str, end_date: str, portfolio: dict, show_reasoning: bool = False):
    final_state = app.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Make a trading decision based on the provided data.",
                )
            ],
            "data": {
                "ticker": ticker,
                "portfolio": portfolio,
                "start_date": start_date,
                "end_date": end_date,
            },
            "metadata": {
                "show_reasoning": show_reasoning,
            }
        },
    )
    return final_state["messages"][-1].content
```

**实现解释**：

- **函数用途**：`run_hedge_fund` 函数作为系统的入口，启动整个代理工作流，根据提供的参数生成最终的交易决策。
- **主要变量**：
  - `ticker`: 股票代码。
  - `start_date`, `end_date`: 回测或交易决策的日期范围。
  - `portfolio`: 当前投资组合状态。
  - `show_reasoning`: 是否显示各代理的推理过程。
- **控制流程**：
  1. 构建初始状态，包括消息、数据和元数据。
  2. 调用工作流 `app` 执行代理链。
  3. 返回最终代理（组合管理代理）的交易决策内容。

### c. 开发环境和设置要求

（见技术概述中的部分e）

---

# 结束语

本文档详细分析了AI对冲基金项目的系统架构、各组件的功能与职责以及关键实现细节。通过多代理协同工作，结合技术与基础分析，并利用先进的语言模型进行风险评估和决策生成，系统实现了自动化的交易决策和回测功能。模块化和清晰的代码结构为系统的维护和扩展提供了坚实的基础。

如需进一步了解或参与项目开发，请参考 [README.md](./README.md) 文档，或直接访问项目的 [GitHub 仓库](https://github.com/your-repo/ai-hedge-fund.git)。

# 许可证

本文档及相关项目文件遵循 MIT 许可证。详情请参阅 [LICENSE](./LICENSE) 文件。

# 贡献指南

欢迎贡献！请按照以下步骤进行：

1. Fork 本仓库
2. 创建一个功能分支
3. 提交您的更改
4. 推送到分支
5. 创建一个 Pull Request

详细信息请参阅 [Contributing](./README.md#contributing)。

# 常见问题

**Q1: 如何运行对冲基金交易系统？**

A1: 请参考 [README.md](./README.md#running-the-hedge-fund) 中的 “运行对冲基金” 部分，使用以下命令启动系统：

```bash
poetry run python src/agents.py --ticker AAPL
```

**Q2: 如何进行回测？**

A2: 请参考 [README.md](./README.md#running-the-backtester) 中的 “运行回测” 部分，使用以下命令运行回测：

```bash
poetry run python src/backtester.py --ticker AAPL
```

# 联系方式

如有任何问题或建议，请联系 [Your Name](mailto:your.email@example.com)。

# 参考文献

- [LangChain 文档](https://langchain.com/docs/)
- [Pandas 文档](https://pandas.pydata.org/docs/)
- [Matplotlib 文档](https://matplotlib.org/stable/contents.html)

# 结束

感谢您阅读本技术文档。希望能够帮助您更好地理解和使用AI对冲基金系统！
