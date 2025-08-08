---
layout: default
title: "我的笔记列表"
---

<style>
  /* 
    使用唯一的 ID 来包裹整个布局，确保我们的样式优先级更高，
    从而覆盖主题的默认布局样式。
  */
  #custom-knowledge-base {
    display: flex;
    flex-wrap: wrap; /* 在窄屏幕上允许换行 */
    gap: 30px;
  }

  #custom-knowledge-base .sidebar {
    width: 100%; /* 在移动端占满整行 */
    flex-shrink: 0;
    font-size: 0.9em;
  }

  #custom-knowledge-base .main-content {
    width: 100%; /* 在移动端占满整行 */
    flex-grow: 1;
  }

  /* 当屏幕宽度大于 768px (平板和桌面) 时，应用双列布局 */
  @media (min-width: 768px) {
    #custom-knowledge-base .sidebar {
      width: 220px; /* 在宽屏上固定宽度 */
    }
    #custom-knowledge-base .main-content {
      width: calc(100% - 250px); /* 自动计算剩余宽度 */
    }
  }

  /* --- 侧边栏内部样式 --- */
  .sidebar h3 {
    font-size: 1.2em;
    border-bottom: 1px solid #ddd;
    padding-bottom: 5px;
    margin-top: 0;
    margin-bottom: 15px;
  }
  .sidebar ul {
    list-style: none;
    padding: 0;
    margin: 0 0: 25px 0;
  }
  .sidebar ul li a {
    text-decoration: none;
    color: #007bff;
    display: block;
    padding: 4px 0;
  }
  .sidebar .tag-cloud a {
    display: inline-block;
    background-color: #f0f0f0;
    color: #555;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.95em;
    margin-right: 6px;
    margin-bottom: 8px;
    text-decoration: none;
    border: 1px solid #e0e0e0;
  }

  /* --- 右侧主内容区样式 --- */
  .main-content h1 {
    margin-top: 0;
  }
  .post-list { list-style: none; padding-left: 0; }
  .month-group { margin-top: 0; padding-top: 10px; font-size: 1.5em; }
  .day-group { margin-top: 30px; border-bottom: 1px solid #eee; padding-bottom: 10px; font-size: 1.2em; color: #444; }
  .note-item { list-style-type: '▸'; margin-left: 20px; padding-left: 10px; margin-bottom: 20px; }
  .note-title a { text-decoration: none; font-weight: bold; color: #333; font-size: 1.1em; }
  .note-details { font-size: 0.9em; color: #777; padding-left: 20px; margin-top: 5px; }
  .note-details span { margin-right: 15px; }
  .note-tags { margin-top: 8px; padding-left: 20px; }
</style>

{% assign sorted_notes = site.clippings | reverse %}

<!-- 这是关键：用一个唯一的 ID 包裹所有内容 -->
<div id="custom-knowledge-base">
  
  <!-- 侧边栏 -->
  <aside class="sidebar">
    <h3>归档</h3>
    <ul>
      {% assign months = sorted_notes | map: 'created' | map: '%Y-%m' | uniq %}
      {% for month_code in months %}
        <li><a href="#month-{{ month_code }}">{{ month_code | date: "%Y 年 %B" }}</a></li>
      {% endfor %}
    </ul>

    <h3>标签</h3>
    <div class="tag-cloud">
      {% assign all_tags = "" %}
      {% for note in sorted_notes %}
        {% if note.tags %}
          {% assign tag_string = note.tags | first | append: " " %}
          {% assign all_tags = all_tags | append: tag_string %}
        {% endif %}
      {% endfor %}
      {% assign unique_tags = all_tags | split: " " | uniq | sort %}
      {% for tag in unique_tags %}
        {% if tag != "" and tag != "#" %}
          <a>{{ tag }}</a>
        {% endif %}
      {% endfor %}
    </div>
  </aside>

  <!-- 主内容区 -->
  <main class="main-content">
    <h1>笔记列表</h1>
    {% assign current_month = "" %}
    {% assign current_day = "" %}
    <div class="post-list">
      {% for note in sorted_notes %}
        {% assign note_month_code = note.created | date: "%Y-%m" %}
        {% if note_month_code != current_month %}
          <h2 class="month-group" id="month-{{ note_month_code }}">{{ note.created | date: "%Y 年 %B" }}</h2>
          {% assign current_month = note_month_code %}
          {% assign current_day = "" %}
        {% endif %}
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
          {% if note.tags %}<div class="note-tags">{% assign tag_list = note.tags | first | split: ' ' %}{% for tag in tag_list %}{% if tag != "" and tag != "#" %}<a class="tag">{{ tag }}</a>{% endif %}{% endfor %}</div>{% endif %}
        </li>
      {% endfor %}
    </div>
  </main>
</div>