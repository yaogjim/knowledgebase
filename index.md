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

<!-- 1. 准备数据 -->
{% assign sorted_notes = site.clippings | sort: 'created' | reverse %}

<!-- 2. 全新逻辑：一次性处理所有内容，并在此过程中“捕获”导航和内容 -->
{% assign captured_nav_links = "" %}
{% assign current_month = "" %}
{% assign current_day = "" %}

{% capture captured_content %}
  {% for note in sorted_notes %}
    {% if note.created %}
      {% assign note_month = note.created | date: '%Y-%m' %}
      {% assign note_day = note.created | date: '%d' %}

      <!-- A. 月份变更检测 -->
      {% if note_month != current_month %}
        <!-- A1. 如果不是第一个月，则结束上一个月的 div -->
        {% if current_month != "" %}
            </div> <!-- close .post-list -->
          </div> <!-- close .month-content-panel -->
        {% endif %}

        <!-- A2. 捕获新的导航链接，并追加到变量中 -->
        {% capture nav_link %}
          <a class="month-nav-item" data-target="#content-{{ note_month }}">{{ note_month | date: "%Y 年 %B" }}</a>
        {% endcapture %}
        {% assign captured_nav_links = captured_nav_links | append: nav_link %}

        <!-- A3. 开始新的月份面板 -->
        <div id="content-{{ note_month }}" class="month-content-panel">
          <div class="post-list">
        {% assign current_month = note_month %}
        {% assign current_day = "" %} <!-- 每个新月份都重置日期 -->
      {% endif %}

      <!-- B. 日期变更检测 -->
      {% if note_day != current_day %}
        <h3 class="day-group">{{ note.created | date: "%-d 日" }}</h3>
        {% assign current_day = note_day %}
      {% endif %}

      <!-- C. 渲染笔记条目 -->
      <li class="note-item">
        <div class="note-title"><a href="{{ note.url | relative_url }}">{{ note.title | default: "无标题笔记" }}</a></div>
        <div class="note-details">
          {% if note.author %}<span>✍️ {{ note.author | join: ', ' | remove: '[[' | remove: ']]' }}</span>{% endif %}
          {% if note.source %}<span>🔗 <a href="{{ note.source }}" target="_blank" rel="noopener noreferrer">来源链接</a></span>{% endif %}
        </div>
        {% if note.tags %}
        <div class="note-tags">
          {% assign flat_tags_string = note.tags | join: ' ' %}
          {% assign tag_list = flat_tags_string | split: ' ' %}
          {% for tag in tag_list %}
            {% if tag != "" and tag != "#" %}
              <span class="tag">{{ tag }}</span>
            {% endif %}
          {% endfor %}
        </div>
        {% endif %}
      </li>
    {% endif %}
  {% endfor %}

  <!-- D. 循环结束后，关闭最后一个月份的 div -->
  {% if sorted_notes.size > 0 %}
      </div> <!-- close .post-list -->
    </div> <!-- close .month-content-panel -->
  {% endif %}
{% endcapture %}

<!-- 3. 渲染最终页面 -->
<h1>我的知识库</h1>
<nav class="month-nav" id="month-navigator">
  {{ captured_nav_links }}
</nav>

<div class="content-container">
  {{ captured_content }}
</div>


<!-- 4. JavaScript 逻辑 (保持不变) -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const navContainer = document.getElementById('month-navigator');
    if (!navContainer) return;

    const navLinks = navContainer.querySelectorAll('.month-nav-item');
    const contentPanels = document.querySelectorAll('.month-content-panel');

    if (navLinks.length === 0) return;

    navLinks[0].classList.add('is-active');
    const firstPanelId = navLinks[0].getAttribute('data-target');
    const firstPanel = document.querySelector(firstPanelId);
    if (firstPanel) {
      firstPanel.classList.add('is-visible');
    }

    navLinks.forEach(link => {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        navLinks.forEach(nav => nav.classList.remove('is-active'));
        contentPanels.forEach(panel => panel.classList.remove('is-visible'));
        this.classList.add('is-active');
        const targetId = this.getAttribute('data-target');
        const targetPanel = document.querySelector(targetId);
        if (targetPanel) {
          targetPanel.classList.add('is-visible');
        }
      });
    });
  });
</script>