---
title: "2026-03-03_gemchanger_gemchanger_如何像量化交易员一样进行模拟_每个模型_每个公式_可运行代码_这"
source: "https://x.com/gemchange_ltd/status/2027744530124951831"
author:
  - "[[@gemchanger]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@gemchanger"
  - "self"
  - "np"
---

# gemchanger # 如何像量化交易员一样进行模拟。每个模型、每个公式、可运行代码。 这

**gemchanger**

# 如何像量化交易员一样进行模拟。每个模型、每个公式、可运行代码。

这不是一份技术清单。

这是一个故事——从抛硬币开始，到机构级模拟引擎结束。

每个章节都以前一章节为基础。跳过前面的章节，后面的数学计算就难以理解。请按顺序阅读，读到最后，你将得到堆栈每一层的可运行代码。

免责声明： 非财务建议，请自行研究

## 第一部分：决定一切的抛硬币

你现在看到的是一份 Polymarket 合约。“美联储会在 3 月份降息吗？”答案是“会”，交易价格为 0.62 美元。

你的直觉告诉你：概率是62%。也许你觉得应该是70%。于是你买了。

恭喜。你刚才做了每个散户交易者都会做的事：你把预测市场合约当作一枚已知存在偏差的抛硬币游戏，估计了自己的偏差，然后押注两者之间的差值。

- 你根本不知道自己对70%的估计有多大把握。
- 你不知道明天的就业报告出来后情况会发生怎样的变化。
- 你不知道它与 Polymarket 上其他六个与美联储相关的合约有何关联。
- 即使你最终判断正确，你也无法确定从现在到最终结果出来之前的价格走势是否能让你获利退出。

抛硬币有一个参数：p。

预测市场合约嵌入到一系列相关事件的组合中，具有随时间变化的信息流、订单簿动态和执行风险，有几十种。

## 第二部分 ：蒙特卡洛。无人足够尊重的基金会

本文中的所有模拟最终都可简化为蒙特卡罗方法：从分布中抽取样本，计算统计量，重复。

事件概率 p=P(A) 的估计量就是样本均值：

中心极限定理给出了收敛速度：O(N^{-1/2}，方差为 Var(p^\_N)=p(1−p)/N。

当 p=0.5p 时 ，方差最大。 合约价格为 50 美分，是平台上最不确定、交易最活跃的合约，而此时蒙特卡罗估计的精确度也最低。

当 p=0.50 时，在 95% 置信度下达到 ±0.01 的精度：

这还能应付。但当你需要模拟路径而不仅仅是端点时，情况就会迅速恶化。

你的第一个可运行模拟

目标： 估计与资产挂钩的二元合约实现盈利的概率（例如，“苹果公司股价在 3 月 15 日之前能否收于 200 美元以上？”）

```python
import numpy as np

def simulate_binary_contract(S0, K, mu, sigma, T, N_paths=100_000):
 """
 Monte Carlo simulation for a binary contract.
 
 S0: Current asset price
 K: Strike / threshold
 mu: Annual drift
 sigma: Annual volatility
 T: Time to expiry in years
 N_paths: Number of simulated paths
 """
 # Simulate terminal prices via GBM
 Z = np.random.standard_normal(N_paths)
 S_T = S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
 
 # Binary payoff
 payoffs = (S_T > K).astype(float)
 
 # Estimate and confidence interval
 p_hat = payoffs.mean()
 se = np.sqrt(p_hat * (1 - p_hat) / N_paths)
 ci_lower = p_hat - 1.96 * se
 ci_upper = p_hat + 1.96 * se
 
 return {
 'probability': p_hat,
 'std_error': se,
 'ci_95': (ci_lower, ci_upper),
 'N_paths': N_paths
 }

# Example: AAPL at $195, strike $200, 20% vol, 30 days
result = simulate_binary_contract(S0=195, K=200, mu=0.08, sigma=0.20, T=30/365)
print(f"P(AAPL > $200) ≈ {result['probability']:.4f}")
print(f"95% CI: ({result['ci_95'][0]:.4f}, {result['ci_95'][1]:.4f})")
```

这套理论对单个合约、单个标的资产以及对数正态分布假设都适用。但真实的预测市场打破了所有这些假设。

评估您的模拟

在改进模拟之前，我们需要一种方法来衡量它的性能。 布里尔评分是标准的校准指标：

```python
def brier_score(predictions, outcomes):
 """Evaluate simulation calibration."""
 return np.mean((np.array(predictions) - np.array(outcomes))**2)

# Compare two models
model_A_preds = [0.7, 0.3, 0.9, 0.1]  # sharp, confident
model_B_preds = [0.5, 0.5, 0.5, 0.5]  # always uncertain
actual_outcomes = [1, 0, 1, 0]

print(f"Model A Brier: {brier_score(model_A_preds, actual_outcomes):.4f}")  # 0.05
print(f"Model B Brier: {brier_score(model_B_preds, actual_outcomes):.4f}")  # 0.25
```

布里尔评分低于 0.20 分就算不错了。

低于 0.10 为优秀。

历史上，最好的选举预测机构（538，经济学人）在总统选举中的准确率在 0.06-0.12 之间。

如果你的模拟结果能超越它，你就拥有优势。

## 第三部分 ：当 10 万个样本还不够时

现在，故事升级了。

Polymarket 提供极端事件合约。“标普 500 指数会在一周内下跌 20% 吗？”的交易价格为 0.003 美元。由于蒙特卡罗模拟的样本量仅为 10 万，因此可能只会命中一次或零次。

您的估算值要么是 0.00000，要么是 0.00001——两者​​都没有意义。

这并非理论上的问题，而是大多数散户交易者无法正确评估尾部风险合约的原因。

让罕见事件变得常见

重要性抽样用一个对稀有区域进行过采样的概率测度替换了原始概率测度，然后用似然函数校正偏差。

L 似然比或 Radon-Nikodym 导数

虽然没有直接用处，但它告诉你应该朝着哪个方向努力。

实际应用中最常用的方法是指数倾斜 。

如果你的基础分布服从增量为 Δ\_i 的随机游走，其矩生成函数为 M(γ)=E\[e^γΔ\]，那么你就倾斜了该分布：

选择 γ 值使罕见事件变得常见。对于当金额超过较大阈值时支付的合约，γ 满足伦德伯格方程 M(γ)=1。

尾部风险合约的重要性抽样

```python
def rare_event_IS(S0, K_crash, sigma, T, N_paths=100_000):
 """
 Importance sampling for extreme downside binary contracts.
 
 Example: P(S&P drops 20% in one week)
 """
 K = S0 * (1 - K_crash)  # e.g., 20% crash threshold
 
 # Original drift (risk-neutral)
 mu_original = -0.5 * sigma**2
 
 # Tilted drift: shift the mean toward the crash region
 # Choose mu_tilt so the crash threshold is ~1 std dev away instead of ~4
 log_threshold = np.log(K / S0)
 mu_tilt = log_threshold / T  # center the distribution on the crash
 
 Z = np.random.standard_normal(N_paths)
 
 # Simulate under TILTED measure
 log_returns_tilted = mu_tilt * T + sigma * np.sqrt(T) * Z
 S_T_tilted = S0 * np.exp(log_returns_tilted)
 
 # Likelihood ratio: original density / tilted density
 log_returns_original = mu_original * T + sigma * np.sqrt(T) * Z
 log_LR = (
 -0.5 * ((log_returns_tilted - mu_original * T) / (sigma * np.sqrt(T)))**2
 + 0.5 * ((log_returns_tilted - mu_tilt * T) / (sigma * np.sqrt(T)))**2
 )
 LR = np.exp(log_LR)
 
 # IS estimator
 payoffs = (S_T_tilted < K).astype(float)
 is_estimates = payoffs * LR
 
 p_IS = is_estimates.mean()
 se_IS = is_estimates.std() / np.sqrt(N_paths)
 
 # Compare with crude MC
 Z_crude = np.random.standard_normal(N_paths)
 S_T_crude = S0 * np.exp(mu_original * T + sigma * np.sqrt(T) * Z_crude)
 p_crude = (S_T_crude < K).mean()
 se_crude = np.sqrt(p_crude * (1 - p_crude) / N_paths) if p_crude > 0 else float('inf')
 
 return {
 'p_IS': p_IS, 'se_IS': se_IS,
 'p_crude': p_crude, 'se_crude': se_crude,
 'variance_reduction': (se_crude / se_IS)**2 if se_IS > 0 else float('inf')
 }

result = rare_event_IS(S0=5000, K_crash=0.20, sigma=0.15, T=5/252)
print(f"IS estimate: {result['p_IS']:.6f} ± {result['se_IS']:.6f}")
print(f"Crude estimate: {result['p_crude']:.6f} ± {result['se_crude']:.6f}")
print(f"Variance reduction factor: {result['variance_reduction']:.1f}x")
```

对于极端合约，IS 可以将方差降低 100 到 10,000 倍 。

这意味着 100 个 IS 样品比 1,000,000 个原始样品具有更高的精度。

这并非微小的改进，而是从“我们无法定价”到“我们可以交易”之间的区别。

## 第一部分第四节：用于实时更新的序列蒙特卡罗方法

但当故事从静态估算转向动态仿真时，我需要做什么？

想象： 今天是选举之夜，美国东部时间晚上8点01分。佛罗里达州的投票站刚刚关闭。初步计票结果显示，一位候选人的支持率上升了3个百分点。

您的模型需要立即更新 ，将这个新数据点纳入概率估计中，不仅要考虑佛罗里达州，还要考虑俄亥俄州、宾夕法尼亚州、密歇根州以及所有相关的州。

这是一个滤波问题 ，而工具是序列蒙特卡罗粒子滤波器。

状态空间模型

定义：

- 隐藏状态 x\_t：事件的“真实”概率（未观察到的概率）
- 观察值 y\_t：市场价格、民意调查结果、投票数、新闻​​信号

该状态通过逻辑随机游走演化 （保持概率有界）：

观测结果是对真实状态的带噪声的读数：

引导粒子滤波器

该算法维护 N 个“粒子”——每个粒子都是关于真实概率的一个假设，并随着数据的到达而重新加权：

```text
1. INITIALIZE: Draw x_0^{(i)} ~ Prior  for i = 1,...,N
 Set weights w_0^{(i)} = 1/N

2. FOR each new observation y_t:
 a. PROPAGATE:  x_t^{(i)} ~ f( · | x_{t-1}^{(i)} )
 b. REWEIGHT: w_t^{(i)} ∝ g( y_t | x_t^{(i)} )  
 c. NORMALIZE:  w̃_t^{(i)} = w_t^{(i)} / Σ_j w_t^{(j)}
 d. RESAMPLE if ESS = 1/Σ(w̃_t^{(i)})² < N/2
```

实时预测市场的粒子滤波器

```python
import numpy as np
from scipy.special import expit, logit  # sigmoid and logit

class PredictionMarketParticleFilter:
 """
 Sequential Monte Carlo filter for real-time event probability estimation.
 
 Usage during a live event (e.g., election night):
 pf = PredictionMarketParticleFilter(prior_prob=0.50)
 pf.update(observed_price=0.55) # market moves on early returns
 pf.update(observed_price=0.62) # more data
 pf.update(observed_price=0.58) # partial correction
 print(pf.estimate()) # filtered probability
 """
 def __init__(self, N_particles=5000, prior_prob=0.5,
 process_vol=0.05, obs_noise=0.03):
 self.N = N_particles
 self.process_vol = process_vol
 self.obs_noise = obs_noise
 
 # Initialize particles around prior
 logit_prior = logit(prior_prob)
 self.logit_particles = logit_prior + np.random.normal(0, 0.5, N_particles)
 self.weights = np.ones(N_particles) / N_particles
 self.history = []
 
 def update(self, observed_price):
 """Incorporate a new observation (market price, poll result, etc.)"""
 # 1. Propagate: random walk in logit space
 noise = np.random.normal(0, self.process_vol, self.N)
 self.logit_particles += noise
 
 # 2. Convert to probability space
 prob_particles = expit(self.logit_particles)
 
 # 3. Reweight: likelihood of observation given each particle
 log_likelihood = -0.5 * ((observed_price - prob_particles) / self.obs_noise)**2
 log_weights = np.log(self.weights + 1e-300) + log_likelihood
 
 # Normalize in log space for stability
 log_weights -= log_weights.max()
 self.weights = np.exp(log_weights)
 self.weights /= self.weights.sum()
 
 # 4. Check ESS and resample if needed
 ess = 1.0 / np.sum(self.weights**2)
 if ess < self.N / 2:
 self._systematic_resample()
 
 self.history.append(self.estimate())
 
 def _systematic_resample(self):
 """Systematic resampling - lower variance than multinomial."""
 cumsum = np.cumsum(self.weights)
 u = (np.arange(self.N) + np.random.uniform()) / self.N
 indices = np.searchsorted(cumsum, u)
 self.logit_particles = self.logit_particles[indices]
 self.weights = np.ones(self.N) / self.N
 
 def estimate(self):
 """Weighted mean probability estimate."""
 probs = expit(self.logit_particles)
 return np.average(probs, weights=self.weights)
 
 def credible_interval(self, alpha=0.05):
 """Weighted quantile-based credible interval."""
 probs = expit(self.logit_particles)
 sorted_idx = np.argsort(probs)
 sorted_probs = probs[sorted_idx]
 sorted_weights = self.weights[sorted_idx]
 cumw = np.cumsum(sorted_weights)
 lower = sorted_probs[np.searchsorted(cumw, alpha/2)]
 upper = sorted_probs[np.searchsorted(cumw, 1 - alpha/2)]
 return lower, upper

# --- Simulate election night ---
pf = PredictionMarketParticleFilter(prior_prob=0.50, process_vol=0.03)

# Incoming observations (market prices as new data arrives)
observations = [0.50, 0.52, 0.55, 0.58, 0.61, 0.63, 0.60, 
 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

print("Election Night Tracker:")
print(f"{'Time':>6}  {'Observed':>10}  {'Filtered':>10}  {'95% CI':>20}")
print("-" * 52)

for t, obs in enumerate(observations):
 pf.update(obs)
 ci = pf.credible_interval()
 print(f"{t:>5}h  {obs:>10.3f}  {pf.estimate():>10.3f}  ({ci[0]:.3f}, {ci[1]:.3f})")
```

为什么这种方法比直接使用市场价格更好？

因为粒子滤波器可以平滑噪声并传播不确定性 。

当市场价格在一次交易中从 0.58 美元飙升至 0.65 美元时，过滤器会意识到真实概率可能并没有发生太大变化，因此会根据观察过程的波动程度来调整更新。

## 第五部分 ：三种叠加式方差缩减技巧

在我们离开蒙特卡罗方法领域之前，这里有三种技术可以与上述所有内容相乘结合 。

自由对称

当收益函数是单调的（二元合约价格越高，超过执行价的概率就越高），方差减少就能得到保证：

典型的减少量约为 50-75%。除了将函数评估次数翻倍（无论如何你都要这样做）之外，无需任何额外的计算成本。

充分利用你已有的知识

如果您正在模拟随机波动率下的二元合约 {S\_T > K}（无封闭形式），请使用 Black-Scholes 数字价格 p\_{BS}​（有封闭形式）作为控制变量 ：

分而治之

将概率空间划分为 JJ J 个层，在每个层内进行抽样，然后合并。方差始终 ≤ 粗 MC（根据总方差定律），通过 Neyman 分配可获得最大收益 ：nj∝ωjσj​（对方差高的层进行过采样）。

```python
def stratified_binary_mc(S0, K, sigma, T, J=10, N_total=100_000):
 """
 Stratified MC for binary contract pricing.
 Strata defined by quantiles of the terminal price distribution.
 """
 n_per_stratum = N_total // J
 estimates = []
 
 for j in range(J):
 # Uniform draws within stratum [j/J, (j+1)/J]
 U = np.random.uniform(j/J, (j+1)/J, n_per_stratum)
 Z = norm.ppf(U)
 S_T = S0 * np.exp((-0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
 stratum_mean = (S_T > K).mean()
 estimates.append(stratum_mean)
 
 # Each stratum has weight 1/J
 p_stratified = np.mean(estimates)
 se_stratified = np.std(estimates) / np.sqrt(J)
 
 return p_stratified, se_stratified

p, se = stratified_binary_mc(S0=100, K=105, sigma=0.20, T=30/365)
print(f"Stratified estimate: {p:.6f} ± {se:.6f}")
```

将所有三个堆叠起来

在每个层内引入相反变量，并进行控制变量校正，通常可以实现比原始 MC 值降低 100-500 倍的方差。这在生产中并非可有可无，而是基本要求。

## 第五部分 I：建模相关矩阵无法做到的事情

分层贝叶斯模型通过共享的国家波动参数隐式地编码相关性。

但是尾部依赖性呢 ？尾部依赖性是指极端的共同波动，而这种波动在线性相关性中却无法体现出来。

2008 年，高斯 copula 函数无法有效模拟尾部相关性，这导致了全球金融危机。在预测市场中，也存在同样的问题：当某个摇摆状态出现意外结果时， 所有摇摆状态同时翻转的概率远高于高斯 copula 函数的预测值。

斯克拉定理

其中 C 是 copula 函数（纯依赖结构），F\_i 是边际累积分布函数。您可以分别对每个市场的边际行为进行建模，然后使用 copula 函数将它们连接起来，该 copula 函数能够捕捉包括尾部在内的依赖关系。

尾部依赖性问题

高斯 copula：尾部相关性 λU=λL=0。极端的协同运动被建模为具有零概率。

对于相关预测市场而言， 这是灾难性的错误 。

学生 t 系带

当 ν=4 且 ρ=0.6 时，尾部相关性约为 0.18 -z，这意味着当一个合约触及极端值时，发生极端联动的概率为 18%。高斯分布则认为该概率为 0%。

克莱顿 copula：仅下尾相关（λL=2^−1/θ）。当一个预测市场崩盘时，其他预测市场也会崩盘。无上尾相关性。

Gumbel copula：仅上尾相关（λU​=2−2^1/θ）。相关正分辨率。

模拟相关预测市场结果

```python
import numpy as np
from scipy.stats import norm, t as t_dist

def simulate_correlated_outcomes_gaussian(probs, corr_matrix, N=100_000):
 """Gaussian copula no tail dependence."""
 d = len(probs)
 L = np.linalg.cholesky(corr_matrix)
 Z = np.random.standard_normal((N, d))
 X = Z @ L.T
 U = norm.cdf(X)
 outcomes = (U < np.array(probs)).astype(int)
 return outcomes

def simulate_correlated_outcomes_t(probs, corr_matrix, nu=4, N=100_000):
 """Student-t copula symmetric tail dependence."""
 d = len(probs)
 L = np.linalg.cholesky(corr_matrix)
 Z = np.random.standard_normal((N, d))
 X = Z @ L.T
 
 # Divide by sqrt(chi-squared / nu) to get t-distributed
 S = np.random.chisquare(nu, N) / nu
 T = X / np.sqrt(S[:, None])
 U = t_dist.cdf(T, nu)
 outcomes = (U < np.array(probs)).astype(int)
 return outcomes

def simulate_correlated_outcomes_clayton(probs, theta=2.0, N=100_000):
 """Clayton copula (bivariate) lower tail dependence."""
 # Marshall-Olkin algorithm
 V = np.random.gamma(1/theta, 1, N)
 E = np.random.exponential(1, (N, len(probs)))
 U = (1 + E / V[:, None])**(-1/theta)
 outcomes = (U < np.array(probs)).astype(int)
 return outcomes


# --- Compare tail behavior ---
probs = [0.52, 0.53, 0.51, 0.48, 0.50]  # 5 swing state probabilities
state_names = ['PA', 'MI', 'WI', 'GA', 'AZ']

corr = np.array([
 [1.0, 0.7, 0.7, 0.4, 0.3],
 [0.7, 1.0, 0.8, 0.3, 0.3],
 [0.7, 0.8, 1.0, 0.3, 0.3],
 [0.4, 0.3, 0.3, 1.0, 0.5],
 [0.3, 0.3, 0.3, 0.5, 1.0],
])

N = 500_000

gauss_outcomes = simulate_correlated_outcomes_gaussian(probs, corr, N)
t_outcomes = simulate_correlated_outcomes_t(probs, corr, nu=4, N=N)

# P(sweep all 5 states)
p_sweep_gauss = gauss_outcomes.all(axis=1).mean()
p_sweep_t = t_outcomes.all(axis=1).mean()

# P(lose all 5 states)  
p_lose_gauss = (1 - gauss_outcomes).all(axis=1).mean()
p_lose_t = (1 - t_outcomes).all(axis=1).mean()

# If independent
p_sweep_indep = np.prod(probs)
p_lose_indep = np.prod([1-p for p in probs])

print("Joint Outcome Probabilities:")
print(f"{'':>25}  {'Independent':>12}  {'Gaussian':>12}  {'t-copula':>12}")
print(f"{'P(sweep all 5)':>25}  {p_sweep_indep:>12.4f}  {p_sweep_gauss:>12.4f}  {p_sweep_t:>12.4f}")
print(f"{'P(lose all 5)':>25}  {p_lose_indep:>12.4f}  {p_lose_gauss:>12.4f}  {p_lose_t:>12.4f}")
print(f"\nt-copula increases sweep probability by {p_sweep_t/p_sweep_gauss:.1f}x vs Gaussian")
```

这正是高斯 copula 在 2008 年失败的原因 ，也是它在预测市场组合方面会再次失败的原因。

v = 4 的 t-copula 通常显示极端联合结果的概率高出 2-5 倍。

如果你在交易相关预测市场合约时没有对尾部依赖性进行建模，那么你的投资组合就会在最重要的场景中彻底崩盘。

Copula 即将到来

对于 d>5 合约，二元 copula 函数不足以满足需求。Vinecopula 函数将 dd 个 d 维依赖关系分解为 d(d−1)/2 个二元条件 copula 函数，这些函数排列成树状结构：

- C-vine（星形）：一个中心事件驱动一切（例如，总统选举获胜 - 所有政策市场波动）
- D-vine（路径）：顺序依赖关系（例如，初选结果影响大选结果）
- R-vine（通用图）：最大灵活性

构建按 ∣τKendall∣ 排序的最大生成树，通过 AIC 选择配对 copula 族，并按顺序估计。实现：pyvinecopuli（Python），VineCopula（R）。

## 第五部分第二节：基于代理的仿真

到目前为止，所有步骤都假设您了解数据生成过程，只需要对其进行模拟即可。

但预测市场由各种各样的参与者组成 ——知情交易者、噪音交易者、做市商和机器人，他们的互动产生了涌现的动态，这是任何封闭形式的随机微分方程都无法捕捉的。

零智商启示录

即使每个交易者都完全非理性，市场仍然可以是有效的 。

Gode 和 Sunder (1993) 证明，零智能代理人（仅受预算约束而提交随机订单的交易员）在连续双向拍卖中实现了接近 100% 的配置效率。

Farmer、Patelli 和 Zovko (2005) 将此扩展到限制订单簿。

这解释了伦敦证券交易所96%的横截面价差变动。仅一个参数，就占了96%。

基于代理的预测市场模拟器

```python
import numpy as np
from collections import deque

class PredictionMarketABM:
 """
 Agent-based model of a prediction market order book.
 
 Agent types:
 - Informed: know the true probability, trade toward it
 - Noise: random trades
 - Market maker: provides liquidity around current price
 """
 def __init__(self, true_prob, n_informed=10, n_noise=50, n_mm=5):
 self.true_prob = true_prob
 self.price = 0.50  # initial price
 self.price_history = [self.price]
 
 # Order book (simplified as bid/ask queues)
 self.best_bid = 0.49
 self.best_ask = 0.51
 
 # Agent populations
 self.n_informed = n_informed
 self.n_noise = n_noise
 self.n_mm = n_mm
 
 # Track metrics
 self.volume = 0
 self.informed_pnl = 0
 self.noise_pnl = 0
 
 def step(self):
 """One time step: randomly select an agent to trade."""
 total = self.n_informed + self.n_noise + self.n_mm
 r = np.random.random()
 
 if r < self.n_informed / total:
 self._informed_trade()
 elif r < (self.n_informed + self.n_noise) / total:
 self._noise_trade()
 else:
 self._mm_update()
 
 self.price_history.append(self.price)
 
 def _informed_trade(self):
 """Informed trader: buy if price < true_prob, sell otherwise."""
 signal = self.true_prob + np.random.normal(0, 0.02)  # noisy signal
 
 if signal > self.best_ask + 0.01:  # buy
 size = min(0.1, abs(signal - self.price) * 2)
 self.price += size * self._kyle_lambda()
 self.volume += size
 self.informed_pnl += (self.true_prob - self.best_ask) * size
 elif signal < self.best_bid - 0.01:  # sell
 size = min(0.1, abs(self.price - signal) * 2)
 self.price -= size * self._kyle_lambda()
 self.volume += size
 self.informed_pnl += (self.best_bid - self.true_prob) * size
 
 self.price = np.clip(self.price, 0.01, 0.99)
 self._update_book()
 
 def _noise_trade(self):
 """Noise trader: random buy/sell."""
 direction = np.random.choice([-1, 1])
 size = np.random.exponential(0.02)
 self.price += direction * size * self._kyle_lambda()
 self.price = np.clip(self.price, 0.01, 0.99)
 self.volume += size
 self.noise_pnl -= abs(self.price - self.true_prob) * size * 0.5
 self._update_book()
 
 def _mm_update(self):
 """Market maker: tighten spread toward current price."""
 spread = max(0.02, 0.05 * (1 - self.volume / 100))
 self.best_bid = self.price - spread / 2
 self.best_ask = self.price + spread / 2
 
 def _kyle_lambda(self):
 """Price impact parameter."""
 sigma_v = abs(self.true_prob - self.price) + 0.05
 sigma_u = 0.1 * np.sqrt(self.n_noise)
 return sigma_v / (2 * sigma_u)
 
 def _update_book(self):
 spread = self.best_ask - self.best_bid
 self.best_bid = self.price - spread / 2
 self.best_ask = self.price + spread / 2
 
 def run(self, n_steps=1000):
 for _ in range(n_steps):
 self.step()
 return np.array(self.price_history)


# --- Simulation ---
np.random.seed(42)

# Scenario: true probability is 0.65, market starts at 0.50
sim = PredictionMarketABM(true_prob=0.65, n_informed=10, n_noise=50, n_mm=5)
prices = sim.run(n_steps=2000)

print("Agent-Based Prediction Market Simulation")
print(f"True probability: {sim.true_prob:.2f}")
print(f"Starting price: 0.50")
print(f"Final price: {prices[-1]:.4f}")
print(f"Price at t=500: {prices[500]:.4f}")
print(f"Price at t=1000: {prices[1000]:.4f}")
print(f"Total volume: {sim.volume:.1f}")
print(f"Informed P&L: ${sim.informed_pnl:.2f}")
print(f"Noise trader P&L: ${sim.noise_pnl:.2f}")
print(f"Convergence error:  {abs(prices[-1] - sim.true_prob):.4f}")
```

价格收敛的速度取决于知情交易者与噪音交易者的比例 、做市商价差对信息流的反应，以及知情交易者为何以噪音交易者的损失为代价来获取利润。

## 第五部分 III：生产堆栈

以下是完整的系统，从市场数据到交易执行：

- 第一层：数据摄取 - 来自 Polymarket CLOB API 的 WebSocket 数据源（实时价格、交易量） - 新闻/民意调查数据（经自然语言处理转化为概率信号） - 链上事件数据（Polygon）
- 第二层：概率引擎 - 分层贝叶斯模型（Stan/PyMC）状态级后验概率 - 粒子滤波器根据新的观测结果进行实时更新 - 用于风险管理的跳跃扩散随机微分方程路径模拟 - 集成：模型输出的加权平均值
- 第三层：依赖关系建模 - Vine copula 合约间的成对依赖关系 - 因子模型共享的国家/全球风险因素 - 通过 t-copula 进行尾部相关性估计
- 第四层：风险管理 - 基于期望值理论的风险价值和预期损失 反向压力测试可以识别最坏情况 - 相关性压力：如果各州之间的相关性激增会怎样？ - 流动性风险订单簿深度监控
- 第五层：监控 - 布里尔评分跟踪（我们是否已校准？） 损益归因（模型中哪个组成部分增加了价值？） - 回撤警报 模型漂移检测

## 参考

- Dalen (2025). “迈向预测市场的布莱克-斯科尔斯模型。” arXiv:2510.15205
- Saguillo 等人（2025）。“揭开概率森林的面纱：预测市场中的套利。” arXiv:2508.03474
- Madrigal-Cianci 等人 (2026)。“预测市场作为贝叶斯逆问题。” arXiv:2601.18815
- Farmer、Patelli 和 Zovko (2005)。“零智能的预测能力”。《美国国家科学院院刊》。
- Gode & Sunder (1993). “零智商交易者的市场配置效率。” JPE
- Kyle (1985). “连续拍卖与内幕交易。”《计量经济学》
- Glosten & Milgrom (1985). “买价、卖价和成交价。” JFE
- 霍夫曼和格尔曼（2014）。《禁止掉头示例》。JMLR
- Merton (1976). “标的股票收益不连续时的期权定价。” JFE
- Linzer (2013). “总统选举的动态贝叶斯预测”。JASA
- Gelman 等人（2020）。“更新的动态贝叶斯预测模型”。HDSR
- Aas、Czado、Frigessi 和 Bakken (2009)。“多重依赖的配对 Copula 构造”。《保险：数学与经济学》
- Wiese 等人（2020）。“量化生成对抗网络：金融时间序列的深度生成”。《量化金融》
- Kidger 等人（2021）。“神经随机微分方程作为无限维生成对抗网络”。ICML