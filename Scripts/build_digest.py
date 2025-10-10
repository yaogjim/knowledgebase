
#!/usr/bin/env python3

import argparse, os, pathlib, datetime, re

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault-root", default=".")
    ap.add_argument("--clippings", default="_clippings")
    ap.add_argument("--out", default="weekly")
    return ap.parse_args()

def read_frontmatter(p):
    text = p.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        for i in range(1, min(200, len(lines))):
            if lines[i].strip() == "---":
                fm = "\n".join(lines[1:i])
                return fm, text[i+1:]
    return None, text

def kv(fm_text):
    d = {}
    for line in fm_text.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip()
    return d

def iso_date(s):
    if not s: return None
    s = s.strip('"').strip("'")
    try:
        return datetime.date.fromisoformat(s)
    except:
        return None

def main():
    args = parse_args()
    root = pathlib.Path(args.vault_root).resolve()
    clip = root / args.clippings
    out_dir = root / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    start = datetime.date.today() - datetime.timedelta(days=7)
    items = []
    for p in clip.rglob("*.md"):
        fm_text, _ = read_frontmatter(p)
        if not fm_text:
            continue
        d = kv(fm_text)
        status = (d.get("status") or "").strip('"').strip("'")
        if status not in ("evergreen","draft","published"):
            continue
        d_date = iso_date(d.get("date")) or iso_date(d.get("created"))
        if not d_date:
            d_date = datetime.date.fromtimestamp(p.stat().st_mtime)
        if d_date >= start:
            title = (d.get("title") or p.stem).strip('"').strip("'")
            rel = p.relative_to(root).as_posix()
            items.append((d_date, title, rel))

    items.sort(key=lambda x: (x[0], x[1]), reverse=True)
    year, week, _ = datetime.date.today().isocalendar()
    outp = out_dir / f"weekly-digest-{year}-{week:02d}.md"
    with open(outp, "w", encoding="utf-8") as f:
        f.write(f"# Weekly Digest (Week {week})\n\n")
        for d, t, rel in items:
            f.write(f"- {d.isoformat()} — [{t}]({rel})\n")
    print(f"[digest] wrote: {outp} | {len(items)} items")

if __name__ == "__main__":
    main()
