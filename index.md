---
layout: default
title: "我的笔记列表"
render_with_liquid: true
---

<style>
  /* --- 基础布局 --- */
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    background-color: #f8f9fa;
  }
  .wrapper {
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
  }
  h1 {
    text-align: center;
    margin-bottom: 25px;
    color: #343a40;
  }

  /* --- 顶部月份筛选 --- */
  .month-nav {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    padding-bottom: 15px;
    border-bottom: 1px solid #dee2e6;
    margin-bottom: 20px;
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

  /* --- 月份面板 --- */
  .month-content-panel {
    display: none;
  }
  .month-content-panel.is-visible {
    display: block;
  }

  /* --- 两栏布局：左日期，右全文 --- */
  .month-layout {
    display: grid;
    grid-template-columns: 260px minmax(0, 1fr);
    gap: 20px;
    align-items: start;
  }

  .date-sidebar {
    position: sticky;
    top: 20px;
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    max-height: calc(100vh - 40px);
    overflow: auto;
    padding: 12px;
  }

  .date-list {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .date-item {
    margin-bottom: 8px;
  }

  .date-group {
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    background: #fff;
    overflow: hidden;
  }

  .date-group[open] {
    border-color: #d1d5db;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }

  .date-nav-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 10px;
    cursor: pointer;
    color: #495057;
    transition: all 0.2s ease;
    user-select: none;
    list-style: none;
  }

  .date-nav-item::-webkit-details-marker {
    display: none;
  }

  .date-nav-item:hover {
    background: #f3f4f6;
  }

  .date-nav-item.is-active {
    background-color: #007bff;
    color: #fff;
    font-weight: 600;
  }

  .date-label {
    display: flex;
    align-items: center;
    gap: 8px;
    min-width: 0;
  }

  .date-arrow {
    width: 14px;
    font-size: 11px;
    transform: rotate(0deg);
    transition: transform 0.2s ease;
  }

  .date-group[open] .date-arrow {
    transform: rotate(90deg);
  }

  .date-count {
    font-size: 0.85em;
    opacity: 0.9;
  }

  .date-doc-list {
    list-style: none;
    margin: 0;
    padding: 0 8px 8px 8px;
    border-top: 1px solid #eef2f7;
    background: #fcfcfd;
  }

  .date-doc-item {
    margin-top: 6px;
  }

  .date-doc-item.is-overflow {
    display: none;
  }

  .date-group.is-expanded .date-doc-item.is-overflow {
    display: block;
  }

  .date-doc-link {
    display: block;
    font-size: 0.88em;
    color: #495057;
    text-decoration: none;
    padding: 5px 6px;
    border-radius: 6px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .date-doc-link:hover {
    color: #0056b3;
    background: #edf2ff;
  }

  .date-toggle-wrap {
    padding: 8px 8px 10px 8px;
    border-top: 1px dashed #e5e7eb;
    background: #fcfcfd;
  }

  .date-toggle-btn {
    width: 100%;
    border: 1px solid #d1d5db;
    background: #fff;
    color: #374151;
    border-radius: 6px;
    font-size: 0.86em;
    padding: 6px 8px;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .date-toggle-btn:hover {
    background: #eef2ff;
    border-color: #c7d2fe;
    color: #1d4ed8;
  }

  .docs-pane {
    min-height: 300px;
  }

  .day-docs-panel {
    display: none;
  }

  .day-docs-panel.is-visible {
    display: block;
  }

  .day-title {
    margin: 0 0 16px 0;
    padding-bottom: 10px;
    border-bottom: 2px solid #e9ecef;
    font-size: 1.3em;
    color: #343a40;
  }

  .doc-item {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 32px 36px; /* 增加内边距，呼吸感更强 */
    margin-bottom: 24px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.06); /* 稍微加深阴影 */
    transition: all 0.2s ease-in-out;
  }

  .doc-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.08); /* 悬浮时阴影更柔和 */
  }

  .doc-title {
    margin: 0;
    line-height: 1.3;
  }

  .doc-title a {
    text-decoration: none;
    font-weight: 700;
    color: #0056b3;
    font-size: 1.4em; /* 标题字号调大 */
  }

  .doc-title a:hover {
    color: #003d82;
    text-decoration: underline;
  }

  .doc-meta {
    font-size: 0.9em;
    color: #6c757d;
    margin-top: 8px;
    margin-bottom: 14px;
  }

  .doc-meta span {
    margin-right: 15px;
  }

  .doc-meta a {
    color: #007bff;
    text-decoration: none;
  }

  .doc-meta a:hover {
    text-decoration: underline;
  }

  .doc-tags {
    margin-bottom: 14px;
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

  .doc-content {
    border-top: 1px solid #f1f3f5;
    margin-top: 12px;
    padding-top: 24px;
    line-height: 1.85; /* 行高增加至 1.85 */
    color: #212529;
    overflow-wrap: anywhere;
    font-size: 18px; /* 字号增加至 18px */
    letter-spacing: 0.01em; /* 增加一点点字间距 */
  }

  .doc-content,
  .doc-content p,
  .doc-content li,
  .doc-content blockquote {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  }

  .doc-content p {
    margin: 0 0 1.25em 0; /* 段落间距增加 */
  }

  .doc-content h1,
  .doc-content h2,
  .doc-content h3,
  .doc-content h4 {
    margin-top: 1.8em;
    margin-bottom: 0.8em;
    line-height: 1.4;
    color: #111827; /* 标题颜色加深 */
    font-weight: 700;
  }

  .doc-content blockquote {
    margin: 1em 0;
    padding: 0.6em 1em;
    border-left: 4px solid #cbd5e1;
    background: #f8fafc;
    color: #334155;
  }

  .doc-content code {
    background: #f1f5f9;
    border-radius: 4px;
    padding: 0.12em 0.35em;
    font-size: 0.92em;
  }

  .doc-content pre {
    overflow: auto;
    background: #0f172a;
    color: #e2e8f0;
    border-radius: 8px;
    padding: 12px;
  }

  .doc-content pre code {
    background: transparent;
    padding: 0;
    color: inherit;
  }

  .doc-content img,
  .doc-content video,
  .doc-content iframe {
    max-width: 100%;
    height: auto;
  }

  @media (max-width: 992px) {
    .month-layout {
      grid-template-columns: 1fr;
    }

    .date-sidebar {
      position: static;
      max-height: none;
    }
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

{%- assign sidebar_preview_limit = 10 -%}
{%- comment -%} 左侧日期下默认预览文档条数：可改为 5/8 等 {%- endcomment -%}

<!-- 步骤 4: 【安全分组】现在，对这个绝对干净且排好序的列表进行按月份分组 -->
{%- assign notes_by_month = sorted_notes | group_by_exp: "note", "note.created | date: '%Y-%m'" -%}

<!-- ===================================================================== -->
<!-- =================== 数据处理结束，开始渲染页面 ===================== -->
<!-- ===================================================================== -->

<!-- 3. 顶部月份导航 -->
<h1>我的随手Obsidian 记录</h1>
<nav class="month-nav" id="month-navigator">
  {% for month in notes_by_month %}
    {% if month.name and month.name != "" and month.name contains "-" %}
      <a class="month-nav-item" data-target="#content-{{ month.name }}">{{ month.name | date: "%Y-%m" }}</a>
    {% endif %}
  {% endfor %}
</nav>

<!-- 4. 内容容器：左侧日期列表，右侧日期下所有文章全文 -->
<div class="content-container">
  {% for month in notes_by_month %}
    {% if month.name and month.name != "" and month.name contains "-" %}
    {% assign notes_by_day = month.items | group_by_exp: "note", "note.created | date: '%Y-%m-%d'" %}
    <div id="content-{{ month.name }}" class="month-content-panel" data-month="{{ month.name }}">
      <div class="month-layout">
        <aside class="date-sidebar">
          <ul class="date-list">
            {% for day in notes_by_day %}
              {% if day.name and day.name != "" and day.name contains "-" %}
              {% assign day_panel_id = "day-" | append: month.name | append: "-" | append: day.name | replace: "-", "" %}
              <li class="date-item">
                <details class="date-group" data-month="{{ month.name }}" data-target="#{{ day_panel_id }}">
                  <summary class="date-nav-item" data-month="{{ month.name }}" data-target="#{{ day_panel_id }}">
                    <span class="date-label">
                      <span class="date-arrow">▶</span>
                      <span>{{ day.name | date: "%m-%d" }}</span>
                    </span>
                    <span class="date-count">{{ day.items | size }}</span>
                  </summary>

                  <ul class="date-doc-list">
                    {% for note in day.items %}
                      {% assign note_id = note.url | slugify %}
                      <li class="date-doc-item{% if forloop.index > sidebar_preview_limit %} is-overflow{% endif %}">
                        <a class="date-doc-link sidebar-doc-trigger" href="#doc-{{ note_id }}" data-day-target="#{{ day_panel_id }}" title="{{ note.title | default: '无标题笔记' }}">{{ note.title | default: "无标题笔记" }}</a>
                      </li>
                    {% endfor %}
                  </ul>

                  {% if day.items.size > sidebar_preview_limit %}
                    <div class="date-toggle-wrap">
                      <button
                        type="button"
                        class="date-toggle-btn"
                        data-expand-text="展开全部（{{ day.items.size }}）"
                        data-collapse-text="收起"
                      >展开全部（{{ day.items.size }}）</button>
                    </div>
                  {% endif %}
                </details>
              </li>
              {% endif %}
            {% endfor %}
          </ul>
        </aside>

        <section class="docs-pane">
          {% for day in notes_by_day %}
            {% if day.name and day.name != "" and day.name contains "-" %}
            {% assign day_panel_id = "day-" | append: month.name | append: "-" | append: day.name | replace: "-", "" %}
            <div id="{{ day_panel_id }}" class="day-docs-panel" data-month="{{ month.name }}">
              <h3 class="day-title">{{ day.name | date: "%Y-%m-%d" }}（{{ day.items | size }} 篇）</h3>

              {% for note in day.items %}
                {% assign note_id = note.url | slugify %}
                <article class="doc-item" id="doc-{{ note_id }}">
                  <h4 class="doc-title"><a href="{{ note.url | relative_url }}">{{ note.title | default: "无标题笔记" }}</a></h4>
                  <div class="doc-meta">
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
                    <div class="doc-tags">
                      {%- assign tag_string = note.tags | join: ' ' -%}
                      {%- assign tag_list = tag_string | split: ' ' -%}
                      {%- for tag in tag_list -%}
                        {%- if tag != "" and tag != "#" -%}
                          <span class="tag">{{ tag }}</span>
                        {%- endif -%}
                      {%- endfor -%}
                    </div>
                  {% endif %}

                  <div class="doc-content">
                    {{ note.content | markdownify | replace: 'src="', 'data-src="' | replace: "src='", "data-src='" }}
                  </div>
                </article>
              {% endfor %}
            </div>
            {% endif %}
          {% endfor %}
        </section>
      </div>
    </div>
    {% endif %}
  {% endfor %}
</div>

<!-- 5. JavaScript 逻辑：月份切换 + 日期切换 -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const monthNavigator = document.getElementById('month-navigator');
    if (!monthNavigator) return;

    const monthLinks = monthNavigator.querySelectorAll('.month-nav-item');
    const monthPanels = document.querySelectorAll('.month-content-panel');
    const dayGroups = document.querySelectorAll('.date-group');

    function activateDayInPanel(panel, dayTargetId, keepCollapsed, skipScroll) {
      if (!panel) return;

      const dayLinks = panel.querySelectorAll('.date-nav-item');
      const dayPanels = panel.querySelectorAll('.day-docs-panel');
      const groups = panel.querySelectorAll('.date-group');

      // 1. Remove active state from all headers
      dayLinks.forEach(function(link) {
        link.classList.remove('is-active');
      });

      // 2. Hide all day panels
      dayPanels.forEach(function(dayPanel) {
        dayPanel.classList.remove('is-visible');
      });

      // 3. Close other details only if we are not "keeping collapsed" (which actually means "don't force open everything" but we usually want singleton open)
      // Actually, if we click a doc, we want its parent group to stay OPEN.
      // The current logic: groups.forEach... removeAttribute('open') closes EVERYTHING.
      // If we are navigating to a doc, we likely want to keep the current group open if it is the target group.
      
      const targetGroup = panel.querySelector('.date-group[data-target="' + dayTargetId + '"]');

      // Only close others if we are switching groups logic. 
      // Simplified: Close all, then open target.
      groups.forEach(function(group) {
        if (group !== targetGroup) {
           group.removeAttribute('open');
        }
      });

      const targetDayLink = panel.querySelector('.date-nav-item[data-target="' + dayTargetId + '"]');
      const targetDayPanel = panel.querySelector(dayTargetId);

      if (targetDayLink) {
        targetDayLink.classList.add('is-active');
      }

      if (targetGroup) {
        // Always ensure target group is open when activating
        targetGroup.setAttribute('open', 'open');
      }

      if (targetDayPanel) {
        targetDayPanel.classList.add('is-visible');
        if (!skipScroll) {
           targetDayPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    }

    function activateMonth(monthLink) {
      if (!monthLink) return;

      monthLinks.forEach(function(link) {
        link.classList.remove('is-active');
      });

      monthPanels.forEach(function(panel) {
        panel.classList.remove('is-visible');
      });

      monthLink.classList.add('is-active');

      const monthTargetId = monthLink.getAttribute('data-target');
      const targetMonthPanel = document.querySelector(monthTargetId);
      if (!targetMonthPanel) return;

      targetMonthPanel.classList.add('is-visible');

      // Auto-select first day but DO NOT SCROLL (skipScroll=true)
      const firstDayLink = targetMonthPanel.querySelector('.date-nav-item');
      if (firstDayLink) {
        // On month load, keepCollapsed=true (maybe?), skipScroll=true
        activateDayInPanel(targetMonthPanel, firstDayLink.getAttribute('data-target'), true, true);
      }
    }

    // ... Event Listeners ...

    monthLinks.forEach(function(link) {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        activateMonth(link);
      });
    });

    document.querySelectorAll('.date-nav-item').forEach(function(link) {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        
        const monthName = link.getAttribute('data-month');
        const monthPanel = document.querySelector('#content-' + monthName);
        const dayTargetId = link.getAttribute('data-target');
        
        // 检查当前点击的日期是否已经是激活状态
        const isActive = link.classList.contains('is-active');
        
        if (isActive) {
           // 如果已激活，则仅做“展开/收起”的切换，不触发页面滚动或重置
           const targetGroup = monthPanel.querySelector('.date-group[data-target="' + dayTargetId + '"]');
           if (targetGroup) {
             if (targetGroup.hasAttribute('open')) {
               targetGroup.removeAttribute('open');
             } else {
               targetGroup.setAttribute('open', 'open');
             }
           }
        } else {
           // 如果未激活，执行标准的激活流程（展开列表 + 滚动右侧 + 关闭其他）
           activateDayInPanel(monthPanel, dayTargetId, false, false);
        }
      });
    });

    // NEW: Handle sidebar doc links
    document.querySelectorAll('.sidebar-doc-trigger').forEach(function(link) {
      link.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent jump to new page
        event.stopPropagation();

        const monthPanel = link.closest('.month-content-panel');
        const dayTargetId = link.getAttribute('data-day-target');
        const noteId = link.getAttribute('href'); // #doc-slug

        // Activate day but SKIP scrolling to day top
        activateDayInPanel(monthPanel, dayTargetId, true, true);

        // Scroll to specific note
        const noteEl = document.querySelector(noteId);
        if (noteEl) {
           // Small timeout to allow layout to stabilize after display:block
           setTimeout(() => {
             noteEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
             // Temporary highlight
             noteEl.style.transition = 'background-color 0.5s';
             const originalBg = noteEl.style.backgroundColor;
             noteEl.style.backgroundColor = '#fff3cd'; 
             setTimeout(() => { noteEl.style.backgroundColor = originalBg; }, 1500);
           }, 50);
        }
      });
    });


    dayGroups.forEach(function(group) {
      group.removeAttribute('open');
    });

    document.querySelectorAll('.date-toggle-btn').forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.preventDefault();
        event.stopPropagation();

        const group = button.closest('.date-group');
        if (!group) return;

        const isExpanded = group.classList.toggle('is-expanded');
        button.textContent = isExpanded
          ? (button.getAttribute('data-collapse-text') || '收起')
          : (button.getAttribute('data-expand-text') || '展开全部');
      });
    });

    if (monthLinks.length > 0) {
      activateMonth(monthLinks[0]);
    }
  });
</script>