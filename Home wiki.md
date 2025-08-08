## 我的任務
```dataview
TASK
WHERE !completed
SORT due DESC
```
## 我的想法
```dataview
LIST
from "奇思妙想"
sort file.mday desc
limit 10
```
---
![[DailyNewNotes|今日笔记摘录]]
---

---
## 今日更新
```dataview
TABLE split(file.folder, "/")[0] AS "文件夾"
FROM ""
WHERE date(today) - file.mtime <= dur(1 day)
AND !contains(file.path, "Templates") 
AND !contains(file.path, "ankicards") 
AND !contains(file.path, "images")
SORT file.mtime DESC,file.folder DESC
```

---

## 本週更新

```dataview
TABLE split(file.folder, "/")[0] AS "文件夾",dateformat(file.mtime, "yyyy-MM-dd") AS "修改時間"
FROM ""
WHERE date(today) - file.mtime <= dur(7 day)
AND !contains(file.path, "Templates") 
AND !contains(file.path, "images")
SORT file.folder DESC,file.mtime DESC
```

---
