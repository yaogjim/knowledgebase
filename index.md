---
layout: default
title: "我的笔记列表"
---

<style>
  /* --- 基础和布局 (样式部分保持不变) --- */
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    background-color: #f8f9fa; /* 为页面添加一个浅灰色背景 */
  }
  .wrapper {
    max-width: 960px;
    margin: 0 auto;
    padding: 20px;
  }
  h1 {
    text-align: center;
    margin-bottom: 25px;
    color: #343a40;
  }
  .month-nav {
    display: flex;
    flex-wrap: wrap;
    justify-content: center; /* 居中对齐 */
    gap: 10px;
    padding-bottom: 15px;
    border-bottom: 1px solid #dee2e6;
    margin-bottom: 30px;
  }
  .month-nav-item {
    padding: 8px 15px;
    border: 1px solid #ced4da;
    border-radius: 20px;
    text-decoration: none;
    color: #495057;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .month-nav-item:hover {
    background-color: #e9ecef;
    border-color: #adb5bd;
  }
  .month-nav-item.is-active {
    background-color: #007bff;
    color: white;
    border-color: #007bff;
    font-weight: bold;
  }
  .month-content-panel {
    display: none; /* 默认隐藏 */
  }
  .month-content-panel.is-visible {
    display: block; /* 显示激活的面板 */
  }
  .post-list {
    list-style: none;
    padding-left: 0;
  }
  .day-group {
    margin-top: 40px;
    padding-bottom: 10px;
    border-bottom: 2px solid #e9ecef;
    font-size: 1.4em;
    color: #495057;
  }
  .note-item {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px; /* 圆角 */
    padding: 20px 25px; /* 内部边距 */
    margin-bottom: 20px; /* 卡片间距 */
    box-shadow: 0 2px 4px rgba(0,0,0,0.05); /* 轻微阴影 */
    transition: all 0.2s ease-in-out; /* 平滑过渡效果 */
    list-style-type: none; /* 移除默认的列表点 */
    margin-left: 0; /* 覆盖旧的缩进 */
  }
  .note-item:hover {
    transform: translateY(-4px); /* 向上移动 */
    box-shadow: 0 5px 15px rgba(0,0,0,0.08); /* 阴影加深 */
  }
  .note-title a {
    text-decoration: none;
    font-weight: bold;
    color: #0056b3; /* 标题链接颜色 */
    font-size: 1.2em;
    transition: color 0.2s ease;
  }
  .note-title a:hover {
    color: #003d82;
    text-decoration: underline;
  }
  .note-details {
    font-size: 0.9em;
    color: #6c757d; /* 细节文字颜色变浅 */
    padding-left: 0; /* 移除旧的缩进 */
    margin-top: 8px;
  }
  .note-details span {
    margin-right: 15px;
  }
  .note-details a {
    color: #007bff;
    text-decoration: none;
  }
  .note-details a:hover {
    text-decoration: underline;
  }
  .note-tags {
    margin-top: 15px; /* 增加与上方内容的间距 */
    padding-left: 0; /* 移除旧的缩进 */
  }
  .tag {
    display: inline-block;
    background-color: #e9ecef;
    color: #495057;
    padding: 5px 12px;
    border-radius: 15px;
    font-size: 0.85em;
    margin-right: 8px;
    margin-bottom: 8px;
    text-decoration: none;
    border: 1px solid #dee2e6;
    transition: all 0.2s ease;
  }
  .tag:hover {
    background-color: #ced4da;
    border-color: #adb5bd;
    color: #212529;
  }
</style>

<!-- ===================================================================== -->
<!-- =================== 核心修正：基于您的建议的全新排序逻辑 =================== -->
<!-- ===================================================================== -->

{%- comment -%}
步骤 1: 【分组】我们不再直接排序，而是先按一个标准化的日期字符串进行分组。
`date: '%Y-%m-%d %H:%M:%S'` 会将所有日期格式（无论带不带时间）都统一转换成一个
可以按字典序正确排序的字符串。无效的日期会返回空字符串，自动被忽略。
{%- endcomment -%}
{%- assign notes_grouped_by_time = site.clippings | group_by_exp: "item", "item.created | date: '%Y-%m-%d %H:%M:%S'" -%}

{%- comment -%}
步骤 2: 【排序】我们对这些“组”进行排序。因为组的 `name` 属性现在是标准化的日期字符串，
所以 `sort: 'name'` 是绝对安全的，并且能得到正确的时序。
{%- endcomment -%}
{%- assign sorted_groups = notes_grouped_by_time | sort: 'name' | reverse -%}

{%- comment -%}
步骤 3: 【重组】我们将排好序的组重新展开，得到一个最终的、正确排序的笔记列表。
{%- endcomment -%}
{%- assign sorted_notes = "" | split: "" -%}
{%- for group in sorted_groups -%}
  {%- for note in group.items -%}
    {%- assign sorted_notes = sorted_notes | push: note -%}
  {%- endfor -%}
{%- endfor -%}

<!-- 步骤 4: 【安全分组】现在，对这个绝对干净且排好序的列表进行按月份分组 -->
{%- assign notes_by_month = sorted_notes | group_by_exp: "note", "note.created | date: '%Y-%m'" -%}

<!-- ===================================================================== -->
<!-- =================== 数据处理结束，开始渲染页面 ===================== -->
<!-- ===================================================================== -->

<!-- 3. 顶部导航栏 -->
<h1>我的随手Obsidian 记录</h1>
<nav class="month-nav" id="month-navigator">
  {% for month in notes_by_month %}
    <a class="month-nav-item" data-target="#content-{{ month.name }}">{{ month.name | date: "%Y 年 %B" }}</a>
  {% endfor %}
</nav>

<!-- 4. 内容容器 (这部分使用之前的健壮显示逻辑，无需改动) -->
<div class="content-container">
  {% for month in notes_by_month %}
    <div id="content-{{ month.name }}" class="month-content-panel">
      <ul class="post-list">
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
              {% if note.author and note.author != "" %}
                <span>✍️ 
                {%- if note.author contains '[' -%}
                  {{ note.author | join: ', ' | remove: '[[' | remove: ']]' }}
                {%- else -%}
                  {{ note.author }}
                {%- endif -%}
                </span>
              {% endif %}
              {% if note.source %}<span>🔗 <a href="{{ note.source }}" target="_blank" rel="noopener noreferrer">来源链接</a></span>{% endif %}
            </div>
            {% if note.tags and note.tags != "" %}
              <div class="note-tags">
                {%- assign tag_string = note.tags | join: ' ' -%}
                {%- assign tag_list = tag_string | split: ' ' -%}
                {%- for tag in tag_list -%}
                  {%- if tag != "" and tag != "#" -%}
                    <a href="#" class="tag">{{ tag }}</a>
                  {%- endif -%}
                {%- endfor -%}
              </div>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endfor %}
</div>

<!-- 5. JavaScript 逻辑 (保持不变) -->
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