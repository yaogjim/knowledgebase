

## 今日更新
```dataview
TABLE split(file.folder, "/")[0] AS "文件夹"
FROM ""
WHERE date(today) - file.mtime <= dur(1 day)
SORT file.mtime DESC,file.folder DESC
```

## 本周更新

```dataview
TABLE split(file.folder, "/")[0] AS "文件夹",dateformat(file.mtime, "yyyy-MM-dd") AS "修改时间"
FROM ""
WHERE date(today) - file.mtime <= dur(7 day)
SORT file.folder DESC,file.mtime DESC
```

---
