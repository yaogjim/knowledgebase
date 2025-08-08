编码实现一个mcp-server-flomo，连接 flomo笔记库，实现几个常用操作： 在 MCP Client 对话示例： 
1. 记想法：帮我记录今天的 idea：xxx 
2. 记笔记：读一下这个 URL：xxx，摘要完记录到 flomo 
3. 总结笔记：总结一下我的 flomo 笔记，过去一个月我经常在想什么 
4. 相关笔记：帮我找一下我的 flomo，写了哪些跟 mcp 相关的内容 
5. 
6. 

主要演示开发一个 mcp server，操作私有数据的完整流程。  
用到 flomo API，应该只能做写入操作，
读取 flomo 数据，需要用无头浏览器在本地模拟抓取。