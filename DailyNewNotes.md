# Readwise 今日内容
```dataviewjs
const yesterday = new Date(Date.now() - 86400000);

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
# 阅读回顾

```dataviewjs
const yesterday = new Date(Date.now() - 86400000);

const pages = dv.pages()
  .where(page => page.file.path.startsWith("zDaily/thoughts") && page.file.mtime > yesterday)
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