
#!/usr/bin/env python3

"""
bulk_frontmatter_init.py  (v1.1 safe-merge)
为 Vault 中的 `_clippings` 目录批量添加/补齐默认 Frontmatter（“未读/初始状态”）。
- 对于**没有 frontmatter**的 .md：插入一段默认 frontmatter（不会覆盖正文）。
- 对于**已有 frontmatter**的 .md：只在结束 `---` 之前**追加缺失键**（不重写、不删除、不覆盖）。

用法：
  python3 bulk_frontmatter_init.py --vault-root /path/to/your/vault --target-folder _clippings [--merge-missing] [--set-review-next 7] [--dry-run]

参数：
  --vault-root       Vault 根目录（必须）
  --target-folder    目标相对目录（默认 _clippings）
  --merge-missing    为已有 frontmatter 的文件，追加缺失键（安全）
  --set-review-next  为新添加/补齐的 review_next 设为 N 天后（整数）
  --dry-run          只输出将要进行的变更统计与示例，不写文件

默认键（不会覆盖既有值）：
  status: inbox, review_level: 0, importance: 2, effort: 2, review_count: 0, decision: null,
  review_next: null, review_interval: null, topics: [], links_out: [], summary: "", pov: "", actions: []
  （保留你原有的 title/source/author/tags/published/created 等字段）
"""
import argparse, os, sys, re, json, datetime, pathlib
from typing import List

DEFAULTS = {
    "status": "inbox",
    "importance": 2,
    "effort": 2,
    "review_level": 0,
    "review_next": None,
    "review_interval": None,
    "review_count": 0,
    "decision": None,
    "topics": [],
    "links_out": [],
    "summary": "",
    "pov": "",
    "actions": []
}

def fmt_yaml_line(k, v):
    if v is None:
        return f"{k}: null"
    if isinstance(v, bool):
        return f"{k}: {'true' if v else 'false'}"
    if isinstance(v, (int, float)):
        return f"{k}: {v}"
    if isinstance(v, list):
        if not v: return f"{k}: []"
        # simple one-per-line block
        lines = [f"{k}:"]
        for item in v:
            if isinstance(item, (int,float)):
                lines.append(f"  - {item}")
            else:
                s = str(item).replace('"','\\"')
                lines.append(f'  - "{s}"')
        return "\n".join(lines)
    s = str(v).replace('"','\\"')
    return f'{k}: "{s}"'

def find_frontmatter_bounds(text: str):
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        for i in range(1, min(len(lines), 400)):
            if lines[i].strip() == "---":
                return 0, i
    return None, None

def key_present(fm_lines: List[str], key: str):
    pat = re.compile(rf'^\s*{re.escape(key)}\s*:', re.IGNORECASE)
    return any(bool(pat.match(ln)) for ln in fm_lines)

def insert_missing_keys(fm_lines: List[str], defaults: dict, set_review_next_days: int|None):
    # Append missing keys before the closing '---'
    out = fm_lines[:-1]  # all but last '---'
    added = []
    for k, v in defaults.items():
        if not key_present(fm_lines, k):
            if k == "review_next" and set_review_next_days is not None:
                d = (datetime.date.today() + datetime.timedelta(days=set_review_next_days)).isoformat()
                out.append(fmt_yaml_line(k, d))
            else:
                out.append(fmt_yaml_line(k, v))
            added.append(k)
    out.append(fm_lines[-1])
    return out, added

def build_new_frontmatter(set_review_next_days: int|None):
    lines = ["---"]
    # keep a 'date' by default to help dashboard sorting
    lines.append(fmt_yaml_line("date", datetime.date.today().isoformat()))
    for k, v in DEFAULTS.items():
        if k == "review_next" and set_review_next_days is not None:
            d = (datetime.date.today() + datetime.timedelta(days=set_review_next_days)).isoformat()
            lines.append(fmt_yaml_line(k, d))
        else:
            lines.append(fmt_yaml_line(k, v))
    lines.append("---")
    return "\n".join(lines) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault-root", required=True)
    ap.add_argument("--target-folder", default="_clippings")
    ap.add_argument("--merge-missing", action="store_true")
    ap.add_argument("--set-review-next", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = pathlib.Path(args.vault_root).resolve()
    target = (root / args.target_folder).resolve()
    if not target.exists():
        print(json.dumps({"error": f"目标目录不存在: {target.as_posix()}"}))
        sys.exit(2)

    stats = {"added_frontmatter":0, "merged_missing":0, "untouched":0, "files":0}
    examples = []

    for p in target.rglob("*.md"):
        text = p.read_text(encoding="utf-8", errors="ignore")
        start, end = find_frontmatter_bounds(text)
        if start is None:
            # add a brand-new frontmatter
            new_fm = build_new_frontmatter(args.set_review_next)
            new_text = new_fm + text
            stats["added_frontmatter"] += 1
            if args.dry_run:
                examples.append({"file": p.as_posix(), "action": "add-fm"})
            else:
                p.write_text(new_text, encoding="utf-8")
        else:
            if not args.merge_missing:
                stats["untouched"] += 1
            else:
                lines = text.splitlines()
                fm_lines = lines[start:end+1]
                new_fm_lines, added_keys = insert_missing_keys(fm_lines, DEFAULTS, args.set_review_next)
                if added_keys:
                    new_text = "\n".join(new_fm_lines + lines[end+1:])
                    stats["merged_missing"] += 1
                    if args.dry_run:
                        examples.append({"file": p.as_posix(), "action": "merge-missing", "added": added_keys})
                    else:
                        p.write_text(new_text, encoding="utf-8")
                else:
                    stats["untouched"] += 1
        stats["files"] += 1

    print(json.dumps({"stats": stats, "examples": examples}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
