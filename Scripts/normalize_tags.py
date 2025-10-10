
#!/usr/bin/env python3

"""
normalize_tags.py  （默认 dry-run）
将 frontmatter 中的 `tags` 由“含 # 的字符串”规范为 YAML 数组（去掉 # 与多余空格）。
- 仅处理已有 frontmatter 的文件；不触碰正文。
- 默认只打印拟做的变更；加 `--apply` 才会写入。

用法：
  python3 normalize_tags.py --vault-root /path/to/vault --target-folder _clippings [--apply]
"""
import argparse, pathlib, re, json

def find_bounds(text):
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        for i in range(1, min(400,len(lines))):
            if lines[i].strip() == "---":
                return 0, i
    return None, None

def extract_tags_line(fm_lines):
    # return index and raw value (after ':')
    for idx, ln in enumerate(fm_lines):
        m = re.match(r'^\s*tags\s*:\s*(.*)$', ln, flags=re.IGNORECASE)
        if m:
            return idx, m.group(1).strip()
    return None, None

def to_array(raw):
    # raw might be "", "[]", or a quoted string possibly containing #tags
    # Extract words starting with # or @word or plain words separated by space/#/comma
    s = raw.strip().strip('"').strip("'")
    if s.startswith('[') and s.endswith(']'):
        return None  # already array-ish; skip
    # split by '#' and separators
    parts = re.split(r'[#,]', s)
    tags = []
    for part in parts:
        t = part.strip()
        if not t:
            continue
        # remove leading @ or extra spaces
        t = t.lstrip('#').strip()
        if not t:
            continue
        tags.append(t)
    # deduplicate preserve order
    seen = set()
    out = []
    for t in tags:
        if t not in seen:
            out.append(t)
            seen.add(t)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault-root", required=True)
    ap.add_argument("--target-folder", default="_clippings")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    root = pathlib.Path(args.vault_root).resolve()
    tgt = (root / args.target-folder).resolve()

    changes = []
    for p in tgt.rglob("*.md"):
        text = p.read_text(encoding="utf-8", errors="ignore")
        s, e = find_bounds(text)
        if s is None:
            continue
        lines = text.splitlines()
        fm_lines = lines[s:e+1]
        idx, raw = extract_tags_line(fm_lines)
        if idx is None or raw is None:
            continue
        arr = to_array(raw)
        if arr is None or not arr:
            continue
        # build new block
        repl = ["tags:"]
        for t in arr:
            repl.append(f'  - "{t}"')
        new_fm_lines = fm_lines[:idx] + repl + fm_lines[idx+1:]
        new_text = "\n".join(new_fm_lines + lines[e+1:])
        changes.append({"file": p.as_posix(), "new_tags": arr})
        if args.apply:
            p.write_text(new_text, encoding="utf-8")

    print(json.dumps({"changed": len(changes), "details": changes[:10]}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
