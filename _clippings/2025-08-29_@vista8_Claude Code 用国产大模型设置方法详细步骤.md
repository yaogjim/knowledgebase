---
title: "Claude Code 用国产大模型设置方法详细步骤"
source: "https://x.com/vista8/status/1960616499519086817"
author:
  - "[[@vista8]]"
published: 2025-08-29
created: 2025-08-29
description:
tags:
  - "@vista8 #Claude #国产大模型 #AI #API"
---
**向阳乔木** @vista8 [2025-08-27](https://x.com/vista8/status/1960616499519086817)

Claude Code 用国产大模型设置方法详细步骤  
  
一、 电脑安装Nodejs 18+  
  
没有的这里下载安装  
  
https://nodejs.org  
  
安装后，终端中输入下面指令回车：  
  
npm install -g @anthropic-ai/claude-code  
  
备注：-g 参数代表全局安装，未来在任何终端 Tab 都能用。  
  
二. 设置国产模型 API  
  
核心逻辑： 获取API，设置环境变量  
  
API：全称 Application Programming Interface，应用程序接口，用于软件间的“交流”和“数据交换”的“桥梁”。  
  
环境变量： 用于存储配置信息的“变量”，比如存 API 密钥，让程序知道用哪个国产模型的 API。  
  
1\. Deepseek 配置  
  
获取 API 地址：

https://platform.deepseek.com/api\_keys  
  
终端输入以下环境变量并回车  
  
export ANTHROPIC\_BASE\_URL=https://api.deepseek.com/anthropic

export ANTHROPIC\_AUTH\_TOKEN="换成你的API"

export ANTHROPIC\_MODEL=deepseek-chat

export ANTHROPIC\_SMALL\_FAST\_MODEL=deepseek-chat  
  
备注： export 的核心作用，让环境变量从"私人信息"变成"公共信息"，确保启动的程序都能读取到配置。  
  
注意，这也只是临时设置，关闭终端就没了。  
  
要永久保留，需写入终端配置文件，以MacOS 的 zsh Shell为例，输入下面指令回车：  
  
echo '

export ANTHROPIC\_BASE\_URL=https://api.deepseek.com/anthropic

export ANTHROPIC\_AUTH\_TOKEN="换成你的API"

export ANTHROPIC\_MODEL=deepseek-chat

export ANTHROPIC\_SMALL\_FAST\_MODEL=deepseek-chat' >> ~/.zshrc && source ~/.zshrc  
  
2\. 智谱GLM 4.5  
  
获取 API 地址：  
  
https://bigmodel.cn/usercenter/proj-mgmt/apikeys…  
  
终端输入以下环境变量并回车  
  
export ANTHROPIC\_BASE\_URL=https://open.bigmodel.cn/api/anthropic

export ANTHROPIC\_AUTH\_TOKEN=你的API  
  
3\. Kimi K2  
  
获取 API 地址：  
  
https://platform.moonshot.cn/console/api-keys…  
  
终端输入以下环境变量并回车  
  
export ANTHROPIC\_BASE\_URL="https://api.moonshot.cn/anthropic/"

export ANTHROPIC\_API\_KEY="你的API"  
  
三、启动国产模型 API 的 Claude  
  
终端输入 claude 启动。  
  
如果想让 AI 自动执行，不需要你的确认，则输入：  
  
claude --dangerously-skip-permissions  
  
四、Claude Code 教程  
  
强烈推荐吴恩达和Anthropic公司推出的CC教程。  
  
https://bilibili.com/video/BV1k1bBzTEF5/…  
  
五、小技巧  
  
技巧1：  
  
输入 /init ，可以创建一个名字叫http://CLAUDE.md的文件。  
  
能写入编程规范和重要记忆，类似Cursor的Rules功能。  
  
甚至每个文件夹都可创建一个。  
  
让AI写代码更聪明些。  
  
例如，X上著名产品经理 Datou的推荐的这段提示词，亲测好用。  
  
提示词地址： https://xiangyangqiaomu.feishu.cn/wiki/HfOqw18eUi0nLtkrsxScPEbynmc…  
  
技巧2：  
  
输入下面指令，每当任务或子任务完成，都有塞尔达音效提示，非常带感。  
  
\> npm install -g zelda-claude-code@latest

![Image](https://pbs.twimg.com/media/GzWCTkIa4AEbHh0?format=jpg&name=large)