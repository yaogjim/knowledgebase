---
title: "**Claude AI 编程模型实时安全性监控**"
source: "https://x.com/9hills/status/1988518261278052753"
author:
  - "[[@9hills]]"
published: 2025-11-13
created: 2025-11-13
description:
tags:
  - "@9hills # AIcoding #Claude #安全性监控 #GLM #模型监控 #编程安全 #机器学习"
---
**九原客** @9hills [2025-11-12](https://x.com/9hills/status/1988518261278052753)

客户说应用首页登录有概率出现问题，直接用 claude 监控，除了费点token（用的GLM-4.6包月），没啥缺点。

主要是不用处理各种边缘case，碰到任何问题模型可以自由应对。

claude --output-format stream-json --dangerously-skip-permissions -p '首先用shell生成<timestamp>。然后在playwright-mcp里登录 https://xxxxx/ 然后使用 admin / xxxxxx 登录到主页，保存主页截图（capture.png）和过程中的详细信息尤其是错误信息（比如登录失败，500错误等，文件名error.log）到result/<timestamp> 目录中' --verbose

---

**九原客** @9hills [2025-11-12](https://x.com/9hills/status/1988518554069811369)

playwright 配置 isolated 避免cookie 持久化。

{

"mcpServers": {

"playwright": {

"command": "npx",

"args": \[

"@playwright/mcp@latest",

"--isolated",

"--ignore-https-errors"

\]

}

}

}  
配置 playwright 为独立模式以避免 cookie 持久化。

{

"mcpServers": {

"playwright": {

"command": "npx",

"参数": \[

"@playwright/mcp@latest",

"--isolated",

"--ignore-https-errors"

\]

}

}

}

---

**X.Y Lu** @zola\_xynb [2025-11-12](https://x.com/zola_xynb/status/1988576224692805963)

这种方式admin账号不都泄露给模型厂商了？

---

**九原客** @9hills [2025-11-12](https://x.com/9hills/status/1988576495338688714)

😆其实也不是很在意。可以用.env 来弄。

---

**CES** @CES

Innovation starts here. CES 2026 brings the global tech community together. Save $200 when you register before December 2.  
创新由此启航。2026年国际消费电子展汇聚全球科技精英，12月2日前注册可享200美元优惠。

---

**SWH | (168, 168)** @swh16888 [2025-11-12](https://x.com/swh16888/status/1988519204656447778)

意思是讓Claude code 用playwright 抓異常？ 跑在自己電腦上還是客戶那邊？

---

**九原客** @9hills [2025-11-12](https://x.com/9hills/status/1988519788663193893)

放到server上了。

和前几天看到的木马实时用模型生成加壳代码异曲同工，从AI Coding到 只写 Prompt。

---

**寿司云VPN 私信领5折券** @ssyunorg [2025-11-12](https://x.com/ssyunorg/status/1988522702689521922)

“套餐仅可在特定编程工具中使用” glm 他们能检测到我在哪用吗，比如自己用Claude agent sdk调用

---

**九原客** @9hills [2025-11-12](https://x.com/9hills/status/1988523836426408186)

他们肯定是鼓励的

---

**hristo** @hristoHeli [2025-11-12](https://x.com/hristoHeli/status/1988542194957832585)

qwen-coder 使用 chrome-devtools-mcp，搭配 openrouter 的 free model，可用的有 glm polaris kat-coder deepseek ，也是可以的  
qwen-coder 使用 chrome-devtools-mcp，搭配 openrouter 的免费模型，可用的有 glm polaris kat-coder deepseek ，也是可以的