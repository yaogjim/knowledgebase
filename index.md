---
layout: default
title: "我的笔记列表"
---

<style>
  /* --- 基础和布局 --- */
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"; }
  .wrapper { max-width: 960px; margin: 0 auto; padding: 20px; }
  
  /* --- 顶部月份导航 --- */
  .month-nav {
    display: flex;
    flex-wrap: wrap; /* 在窄屏幕上换行 */
    gap: 10px;
    padding-bottom: 15px;
    border-bottom: 1px solid #ddd;
    margin-bottom: 30px;
  }
  .month-nav-item {
    padding: 8px 15px;
    border: 1px solid #ddd;
    border-radius: 20px;
    text-decoration: none;
    color: #333;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .month-nav-item:hover {
    background-color: #f0f0f0;
    border-color: #ccc;
  }
  .month-nav-item.is-active {
    background-color: #007bff;
    color: white;
    border-color: #007bff;
    font-weight: bold;
  }

  /* --- 月份内容面板 --- */
  .month-content-panel {
    display: none; /* 默认隐藏所有月份的内容 */
  }
  .month-content-panel.is-visible {
    display: block; /* 只显示被激活的那个 */
  }
  
  /* --- 笔记列表样式 --- */
  .post-list { list-style: none; padding-left: 0; }
  .day-group { margin-top: 30px; border-bottom: 1px solid #eee; padding-bottom: 10px; font-size: 1.2em; color: #444; }
  .note-item { list-style-type: '▸'; margin-left: 20px; padding-left: 10px; margin-bottom: 20px; }
  .note-title a { text-decoration: none; font-weight: bold; color: #333; font-size: 1.1em; }
  .note-details { font-size: 0.9em; color: #777; padding-left: 20px; margin-top: 5px; }
  .note-details span { margin-right: 15px; }
  .note-tags { margin-top: 8px; padding-left: 20px; }
  .tag {
    display: inline-block; background-color: #f0f0f0; color: #555;
    padding: 4px 10px; border-radius: 15px; font-size: 0.9em;
    margin-right: 6px; margin-bottom: 8px; text-decoration: none;
    border: 1px solid #e0e0e0;
  }
</style>

<!-- 1. 强制排序：在这里直接对 `site.clippings` 进行排序和反转，确保顺序正确 -->
{% assign sorted_notes = site.clippings | sort: 'created' | reverse %}

<!-- 2. 按月份分组：使用 `group_by_exp` 过滤器将所有笔记按月份分组 -->
{% assign notes_by_month = sorted_notes | group_by_exp: "note", "note.created | date: '%Y-%m'" %}

<!-- 3. 顶部导航栏 -->
<h1>我的知识库</h1>
<nav class="month-nav" id="month-navigator">
  {% for month in notes_by_month %}
    <!-- `data-target` 属性是关键，它链接到下面对应的内容面板 -->
    <a class="month-nav-item" data-target="#content-{{ month.name }}">{{ month.name | date: "%Y 年 %B" }}</a>
  {% endfor %}
</nav>

<!-- 4. 内容容器 -->
<div class="content-container">
  {% for month in notes_by_month %}
    <!-- 每个月份的内容都包裹在一个带唯一 ID 的 div 中 -->
    <div id="content-{{ month.name }}" class="month-content-panel">
      <div class="post-list">
        {% assign current_day = "" %}
        {% for note in month.items %}
          {% assign note_day = note.created | date: "%d" %}
          {% if note_day != current_day %}
            <h3 class="day-group">{{ note.created | date: "%-d 日" }}</h3>
            {% assign current_day = note_day %}
          {% endif %}
          <li class="note-item">
            <div class="note-title"><a href="{{ note.url | relative_url }}">{{ note.title | default: "无标题笔记" }}</a></div>
            <div class="note-details">
              {% if note.author %}<span>✍️ {{ note.author | join: ', ' | remove: '[[' | remove: ']]' }}</span>{% endif %}
              {% if note.source %}<span>🔗 <a href="{{ note.source }}" target="_blank" rel="noopener noreferrer">来源链接</a></span>{% endif %}
            </div>
            {% if note.tags %}<div class="note-tags">{% assign tag_list = note.tags | first | split: ' ' %}{% for tag in tag_list %}{% if tag != "" and tag != "#" %}<span class="tag">{{ tag }}</span>{% endif %}{% endfor %}</div>{% endif %}
          </li>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>

<!-- 5. JavaScript 逻辑 -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const navContainer = document.getElementById('month-navigator');
    if (!navContainer) return;

    const navLinks = navContainer.querySelectorAll('.month-nav-item');
    const contentPanels = document.querySelectorAll('.month-content-panel');

    // 如果没有导航链接，就什么都不做
    if (navLinks.length === 0) return;

    // 默认激活第一个导航链接并显示对应内容
    navLinks[0].classList.add('is-active');
    const firstPanelId = navLinks[0].getAttribute('data-target');
    const firstPanel = document.querySelector(firstPanelId);
    if (firstPanel) {
      firstPanel.classList.add('is-visible');
    }

    //为每个导航链接添加点击事件
    navLinks.forEach(link => {
      link.addEventListener('click', function(event) {
        event.preventDefault(); // 阻止链接的默认跳转行为

        // 移除所有链接的激活状态
        navLinks.forEach(nav => nav.classList.remove('is-active'));
        // 隐藏所有内容面板
        contentPanels.forEach(panel => panel.classList.remove('is-visible'));

        // 激活当前点击的链接
        this.classList.add('is-active');
        
        // 显示目标内容面板
        const targetId = this.getAttribute('data-target');
        const targetPanel = document.querySelector(targetId);
        if (targetPanel) {
          targetPanel.classList.add('is-visible');
        }
      });
    });
  });
</script>