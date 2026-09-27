#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MxsDoc-Site 根路径门禁检查器 (GitHub Pages 子路径部署)
========================================================
站点部署在 https://ptreezh.github.io/mxsdoc-site/ 子路径下。
任何裸 "/x.html" 根路径会解析到 https://ptreezh.github.io/x.html（顶层 → 404）。

规则（匹配即违规，提交被拦截）：
  - 双引号根路径:   "/(?!mxsdoc-site|//)
    e.g. href="/"、href="/#features"、href="/scenario.html"、src="/x.js"
  - style url():    url(/x)、url("/x")、url('/x')

合法（放行）：
  - "/mxsdoc-site/..."   已带前缀
  - "//cdn.xxx/..."      协议相对 URL
  - "https://..."/"mailto:"/"tel:"/"javascript:"/"data:"  完整/特殊协议
  - 相对路径 ../x.html、x.html、#anchor、/mxsdoc-site/#anchor

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
PATTERN_QUOTED = re.compile(r'"(/(?!mxsdoc-site|//))')          # "/(...) 双引号根路径
PATTERN_URL = re.compile(r'url\(\s*[\'"]?(/(?!mxsdoc-site|//))')  # url(/...) 样式内根路径

# 需要补前缀的文件扩展名
TARGET_EXTS = {".html", ".htm", ".shtml", ".xhtml", ".xml", ".json", ".js", ".css", ".txt"}
# xml/json/js/css/txt 也纳入？js/css 内的根路径同样 404。但 canonical/og 多为完整URL。
# 这里保持专注 HTML（含内联样式）。js 中的路径由 sitemap/API 层处理，另行维护。


def walk_html_files(root, staged_files=None):
    """返回待检查的 html 文件绝对路径列表。"""
    if staged_files is not None:
        # staged 模式: 来自 git diff --cached
        r = []
        for f in staged_files:
            if os.path.splitext(f)[1].lower() in {".html", ".htm", ".shtml", ".xhtml"}:
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
            if os.path.splitext(fn)[1].lower() in {".html", ".htm", ".shtml", ".xhtml"}:
                r.append(os.path.join(dirpath, fn))
    return r


def check_file(path):
    """返回违规行列表 [(line_no, matched_part, line_text), ...] 或 []。"""
    violations = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.rstrip("\r\n")
                for pat in (PATTERN_QUOTED, PATTERN_URL):
                    m = pat.search(line)
                    if m:
                        # 只截取违规片段用于展示
                        s = max(0, m.start() - 25)
                        e = min(len(line), m.end() + 45)
                        snippet = line[s:e]
                        violations.append((lineno, m.group(1), snippet))
                        break  # 一行只报一次
    except OSError as exc:
        violations.append((0, "", f"<read error: {exc}>"))
    return violations


def main():
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
        print(f"❌ 发现 {total_bad} 处缺少 /mxsdoc-site/ 前缀的根路径。")
        print("   本仓库部署在 GitHub Pages 子路径 /mxsdoc-site/ 下，裸 /x 会 404。")
        print("   修复示例:")
        print('     href="/"           ->  href="/mxsdoc-site/"')
        print('     href="/#features"  ->  href="/mxsdoc-site/#features"')
        print('     href="/x.html"     ->  href="/mxsdoc-site/x.html"')
        print('   (子目录页面也可用相对路径 ../x.html)')
        return 1
    # 非 staged 模式打印汇总
    if not staged:
        print(f"✅ 扫描 {len(files)} 个 HTML 文件，0 处裸根路径。")
    return 0


if __name__ == "__main__":
    sys.exit(main())