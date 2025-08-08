```dataview
table file.name as name ,file.tags as tags
from "奇思妙想"
sort file.mday desc
limit 10
```

---
```dataview
list from "" where contains(file.name,"习惯")
```
---

```dataview
list from #阅读习惯
```

---

```dataview 
list from "" 
where contains(page-title ,"LLM") 
sort date desc
```

