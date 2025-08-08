
```dataviewjs
const yesterday = new Date(Date.now() - 86400000);

const pages = dv.pages()
  .where(page => page.file.path.startsWith("Zotero/") && page.file.mtime > yesterday)
  .sort(page => page.file.mtime, "desc");

for (const page of pages) {
    dv.paragraph("## "+page.file.link);
    const content = await dv.io.load(page.file.path);
    const limitedContent = content.split("\n").slice(0, 20).join("\n"); 
    dv.paragraph(limitedContent);
}

```