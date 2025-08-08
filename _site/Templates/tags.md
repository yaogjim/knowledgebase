

```dataview
TABLE length(rows.file.link) AS "笔记数量", tag FLATTEN file.tags AS tag 
GROUP BY tag 
SORT "笔记数量" DESC

```

```dataview

TABLE folder AS "文件夹", length(rows.file.link) AS "笔记数量"
FROM ""
FLATTEN file.folder AS folder
GROUP BY folder
SORT "笔记数量" DESC


```