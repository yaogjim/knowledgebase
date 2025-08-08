# Readwise 今日内容
```dataviewjs
const yesterday = new Date(Date.now() - 7*24*60*60*1000);

const pages = dv.pages()
  .where(page => page.file.path.startsWith("Readwise") && page.file.mtime > yesterday)
  .sort(page => page.file.mtime, "desc");

for (const page of pages) {
    dv.paragraph("## "+page.file.link);
    let content = await dv.io.load(page.file.path);
    // 处理图片链接，设置图片大小 
    content = content.replace(/\!\[.*?\]\((.*?)\)/g, (match, imageUrl) => { 
    return `![|30x30](${imageUrl})`; 
    // 这里设置图片的大小为500x300 
    });
    dv.paragraph(content);
}

```

# Readlater 今日内容
```dataviewjs
const yesterday = new Date(Date.now() - 7*24*60*60*1000);

const pages = dv.pages()
  .where(page => page.file.path.startsWith("zDaily") && page.file.mtime > yesterday)
  .sort(page => page.file.mtime, "desc");

for (const page of pages) {
    dv.paragraph("## "+page.file.link);
    let content = await dv.io.load(page.file.path);
    // 处理图片链接，设置图片大小 
    content = content.replace(/\!\[.*?\]\((.*?)\)/g, (match, imageUrl) => { 
    return `![|30x30](${imageUrl})`; 
    // 这里设置图片的大小为500x300 
    });
    dv.paragraph(content);
}

```

---
---

# ![[Omnivore 今日内容]]

---

# ![[Zotero 今日内容]]