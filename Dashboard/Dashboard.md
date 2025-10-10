# Review Dashboard（仅扫描 `_clippings/`，容错缺失字段）

> 建议把本页设为 Obsidian 的首页或固定 Pin 页。查询限定在 `_clippings/`（含子目录）。

## 今日到期复盘
```dataview
TABLE file.link, status, review_level, review_next
FROM "_clippings"
WHERE (status = "r1" OR status = "r2" OR status = "r3") AND review_next AND review_next <= date(today)
SORT review_next ASC, importance DESC
LIMIT 30
```

## 阅读队列（按优先级；对缺失 status 视为 inbox）
```dataview
TABLE file.link, medium, importance, effort, default(date, default(created, file.ctime)) as when
FROM "_clippings"
WHERE (!status) OR status = "inbox" OR status = "queue"
SORT (importance - 0.5*effort) DESC, when DESC
LIMIT 50
```

## 进行中（WIP 预警）
```dataview
TABLE file.link, status, review_level, review_count, default(date, default(created, file.ctime)) as when
FROM "_clippings"
WHERE status = "r1" OR status = "r2" OR status = "r3"
SORT file.mtime DESC
```

## 合成候选（R3 与 Evergreen）
```dataview
TABLE file.link, topics, summary
FROM "_clippings"
WHERE status="r3" OR status="evergreen"
SORT file.mtime DESC
LIMIT 30
```

## 行动清单（可选：Tasks 插件）
```tasks
not done
path includes _clippings
sort by due
group by path
```