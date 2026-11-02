#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MxsDoc-Site 站内链接门禁检查器（相对链接策略）
====================================================
站点同时部署在两处：
  - GitHub Pages 子路径: https://ptreezh.github.io/mxsdoc-site/
  - 独立域名（自动抓取镜像）: https://agent.gofreeteam.com/
两处路径前缀不同，因此站内链接必须使用**相对链接**，
才能在两处同时正确解析。

规则（匹配即违规，提交被拦截）：
  1. 根绝对路径:  href="/x.html"、src="/x.js"、url(/x)
                  -> 裸 "/" 开头在两处都解析错（GitHub Pages 顶层 404 / 域名根目录错位）
  2. 同站绝对 URL: href="https://ptreezh.github.io/mxsdoc-site/x.html"
                  -> 镜像站会跳回 GitHub，破坏"站内相对"要求

合法（放行）：
  - 相对路径: index.html、../index.html、customers/index.html、#anchor
  - 协议相对: "//cdn.xxx/..."
  - 外部完整 URL: "https://..."（非本站）、"mailto:"、"tel:"、"javascript:"、"data:"
  - <link rel="canonical">：SEO 要求绝对 URL，逐行豁免

用法:
  python check-root-paths.py            # 扫描整个仓库
  python check-root-paths.py --staged   # 只查暂存区（pre-commit 用）
退出码: 0=通过  1=发现违规
"""
import os
import re
import subprocess
import sys

# 违规模式
PATTERN_ROOT_ABS = re.compile(r"""(?i)\b(?:href|src)\s*=\s*["']/(?!/)""")
PATTERN_URL_FUNC = re.compile(r"""(?i)url\(\s*["']?/(?!/)""")
PATTERN_ABS_SITE = re.compile(
    r"""(?i)\b(?:href|src)\s*=\s*["']https?://"""
    r"""(?:ptreezh\.github\.io/mxsdoc-site|agent\.gofreeteam\.com)"""
)
PATTERN_CANONICAL = re.compile(r"""(?i)<link[^>]*rel=["']canonical["']""")

# 需要检查的文件扩展名
TARGET_EXTS = {".html", ".htm", ".shtml", ".xhtml"}
# 只扫 HTML：canonical / og / JSON-LD 里的绝对 URL 是 SEO 规范，不在此拦截


def walk_html_files(root: str, staged_files: list[str] | None = None) -> list[str]:
    """返回待检查的 html 文件绝对路径列表。"""
    if staged_files is not None:
        # staged 模式: 来自 git diff --cached
        r = []
        for f in staged_files:
            if os.path.splitext(f)[1].lower() in TARGET_EXTS:
                p = os.path.join(root, f)
                if os.path.isfile(p):
                    r.append(p)
        return r
    # 全量模式: 遍历仓库
    r = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "node_modules", "dist", "build", "vendor")]
        for fn in filenames:
            if os.path.splitext(fn)[1].lower() in TARGET_EXTS:
                r.append(os.path.join(dirpath, fn))
    return r


def check_file(path: str) -> list[tuple[int, str, str]]:
    """返回违规行列表 [(line_no, matched_part, line_text), ...] 或 []。"""
    violations = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.rstrip("\r\n")
                is_canonical = bool(PATTERN_CANONICAL.search(line))
                pats = [PATTERN_ROOT_ABS, PATTERN_URL_FUNC]
                if not is_canonical:
                    pats.append(PATTERN_ABS_SITE)
                for pat in pats:
                    m = pat.search(line)
                    if m:
                        # 只截取违规片段用于展示
                        s = max(0, m.start() - 25)
                        e = min(len(line), m.end() + 45)
                        snippet = line[s:e]
                        violations.append((lineno, m.group(0), snippet))
                        break  # 一行只报一次
    except OSError as exc:
        violations.append((0, "", f"<read error: {exc}>"))
    return violations


def main() -> int:
    root = os.path.dirname(os.path.abspath(__file__))
    # 仓库根 = .githooks 的上一级
    repo_root = os.path.dirname(root)

    staged = "--staged" in sys.argv[1:]
    if staged:
        try:
            out = subprocess.run(
                ["git", "-C", repo_root, "diff", "--cached", "--name-only",
                 "--diff-filter=ACMR"],
                capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError:
            print("!! 无法读取暂存区，跳过门禁", file=sys.stderr)
            return 0
        files = walk_html_files(repo_root, out.stdout.splitlines())
    else:
        files = walk_html_files(repo_root)

    total_bad = 0
    for f in sorted(files):
        v = check_file(f)
        if v:
            rel = os.path.relpath(f, repo_root)
            total_bad += len(v)
            print(f"[FAIL] {rel}")
            for lineno, matched, snippet in v:
                print(f"   :{lineno}  {snippet}")
    if total_bad:
        print("")
        print(f"❌ 发现 {total_bad} 处非相对站内链接。")
        print("   站点同时部署在 GitHub Pages 子路径 /mxsdoc-site/ 与 agent.gofreeteam.com，")
        print("   站内链接必须是相对链接，否则其中一处必然 404 或跳回 GitHub。")
        print("   修复示例:")
        print('     href="/scenario.html"                          ->  href="scenario.html"')
        print('     href="/mxsdoc-site/scenario.html"               ->  href="scenario.html"')
        print('     href="https://ptreezh.github.io/mxsdoc-site/x.html" ->  href="x.html"')
        print('     (一级子目录页面用 ../ 前缀，例如 ../index.html)')
        return 1
    # 非 staged 模式打印汇总
    if not staged:
        print(f"✅ 扫描 {len(files)} 个 HTML 文件，0 处非相对站内链接。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
