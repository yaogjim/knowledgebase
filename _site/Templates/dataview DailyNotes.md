

## 今日更新
```dataview
TABLE split(file.folder, "/")[0] AS "文件夹"
FROM "Readwise"
WHERE date(today) - file.mtime <= dur(1 day)
SORT file.mtime DESC,file.folder DESC
```

```dataview
TABLE split(file.folder, "/")[0] AS "文件夹"
FROM "Omnivore"
WHERE date(today) - file.mtime <= dur(1 day)
SORT file.mtime DESC,file.folder DESC
```


```dataview
TABLE split(file.folder, "/")[0] AS "文件夹"
FROM "Zotero"
WHERE date(today) - file.mtime <= dur(1 day)
SORT file.mtime DESC,file.folder DESC
```
