---
layout: default
title: "我的笔记列表"
---

<style>
  /* CSS 样式与之前相同，无需修改 */
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"; }
  .wrapper { max-width: 960px; margin: 0 auto; padding: 20px; }
  .month-nav {
    display: flex; flex-wrap: wrap; gap: 10px;
    padding-bottom: 15px; border-bottom: 1px solid #ddd; margin-bottom: 30px;
  }
  .month-nav-item {
    padding: 8px 15px; border: 1px solid #ddd; border-radius: 20px;
    text-decoration: none; color: #333; cursor: pointer; transition: all 0.2s ease;
  }
  .month-nav-item:hover { background-color: #f0f0f0; border-color: #ccc; }
  .month-nav-item.is-active {
    background-color: #007bff; color: white; border-color: #007bff; font-weight: bold;
  }
  .month-content-panel { display: none; }
  .month-content-panel.is-visible { display: block; }
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

<!-- ===================================================================== -->
<!--                        终极防御性 Liquid 逻辑                       -->
<!-- ===================================================================== -->

{% comment %}
  步骤 1: 使用 'where_exp' 过滤器创建一个“干净”的笔记列表。
  这个表达式 "item", "item.created" 会筛选出所有 'created' 字段存在且不为 nil 或 false 的笔记。
  这是比手动 for 循环更稳健的方式。
{% endcomment %}
{% assign notes_with_date = site.clippings | where_exp: "item", "item.created" %}

{% comment %} 
  步骤 2: 对这个 100% 干净的列表进行后续操作。
{% endcomment %}
{% assign sorted_notes = notes_with_date | sort: 'created' %}
{% assign notes_by_month = sorted_notes | group_by_exp: "note", "note.created | date: '%Y-%m'" %}
{% assign reversed_months = notes_by_month | reverse %}


<!-- ===================================================================== -->
<!--                        页面 HTML 结构部分 (无需修改)                  -->
<!-- ===================================================================== -->

<h1>我的知识库</h1>
<nav class="month-nav" id="month-navigator">
  {% for month in reversed_months %}
    <a class="month-nav-item" data-target="#content-{{ month.name }}">{{ month.name | date: "%Y 年 %B" }}</a>
  {% endfor %}
</nav>

<div class="content-container">
  {% for month in reversed_months %}
    <div id="content-{{ month.name }}" class="month-content-panel">
      <div class="post-list">
        {% assign current_day = "" %}
        {% assign notes_in_month = month.items | reverse %}
        {% for note in notes_in_month %}
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

<!-- JavaScript 逻辑与之前相同，无需修改 -->
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