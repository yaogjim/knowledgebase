# 我的知识库

基于Jekyll构建的yaogjim 个人Obsidian笔记整理与分享平台。

## 特性

✅ **现代化设计**: 响应式布局，支持移动端浏览  
✅ **导航优化**: 顶部导航栏 + 面包屑导航  
✅ **智能分组**: 按月份和日期自动整理笔记  
✅ **相关推荐**: 每篇文章显示相关文章推荐  
✅ **图片灯箱**: 支持图片点击放大查看  
✅ **Mermaid图表**: 支持流程图、思维导图等  
✅ **标签系统**: 文章标签展示和筛选  

## 本地开发

### 方法一：使用当前自定义主题（推荐）

```bash
# 1. 克隆仓库
git clone [你的仓库地址]
cd knowledgebase

# 2. 安装依赖
bundle install

# 3. 启动开发服务器
bundle exec jekyll serve

# 4. 在浏览器访问
open http://localhost:4000
```

### 方法二：切换到Just the Docs主题

如果你想使用专业的Just the Docs主题：

1. **修改Gemfile**:
   ```ruby
   # 取消下面这行的注释
   gem "just-the-docs", "~> 0.8.0"
   ```

2. **修改_config.yml**:
   ```yaml
   # 取消下面这行的注释
   theme: just-the-docs
   ```

3. **安装主题**:
   ```bash
   bundle install
   bundle exec jekyll serve
   ```

## 文件结构

```
├── _clippings/           # Obsidian导出的笔记文件
├── _layouts/            
│   ├── default.html     # 默认页面布局
│   └── post.html        # 文章页面布局
├── assets/css/          
│   └── post.css         # 文章页面样式
├── index.md             # 首页
├── _config.yml          # Jekyll配置
└── Gemfile             # Ruby依赖管理
```

## 添加新笔记

1. 将Obsidian笔记导出为Markdown文件
2. 放置在`_clippings/`目录下
3. 确保文件包含以下front matter:

```yaml
---
title: "笔记标题"
created: 2024-01-15 10:30:00
author: ["作者名"]
source: "https://来源链接"
tags: ["标签1", "标签2"]
---
```

## 自定义配置

### 修改站点信息
编辑`_config.yml`文件：

```yaml
title: "你的知识库名称"
description: "你的知识库描述"
baseurl: "/your-repo-name"
url: "https://username.github.io"
author: "你的名字"
```

### 自定义样式
- 首页样式：修改`index.md`中的`<style>`部分
- 文章页样式：修改`assets/css/post.css`

### 添加导航链接
编辑`_layouts/post.html`中的导航部分：

```html
<div class="nav-right">
  <a href="{{ '/' | relative_url }}" class="nav-link">🏠 首页</a>
  <a href="/about" class="nav-link">📖 关于</a>
  <a href="#" class="nav-link" onclick="history.back();">⬅️ 返回</a>
</div>
```
