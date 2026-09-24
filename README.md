# MxsDoc 文件管理系统官网

本地化部署的企业文件/图纸文档管理系统官网静态站（GEO 优化）。

## 站点内容

- **产品**：MxsDoc 文件管理系统（版本管理、集中权限分级、拖拽操作、在线编辑、移动端访问、本地化部署）
- **客户证明**：成都金诺信、福州高意光学（制造企业，自 2025-04 起使用，运行稳定效果良好）
- **销售标的**：企业级部署实施、运维与二次开发定制服务

## GEO 技术清单

| 文件 | 说明 |
|------|------|
| `index.html` | 首页：价值主张 + 客户证明 + 可引用 CLAIMS 句 + SoftwareApplication/FAQPage schema |
| `features.html` | 产品功能页：六大核心功能详情 + FAQ + SoftwareApplication/FAQPage schema |
| `scenario.html` | 应用场景页：三场景故事（制造图纸/知识库AI问答/涉密合规）+ 11 方案对比矩阵 + IMA/Obsidian/飞书深度对比 + FAQ schema |
| `customers/chengdu-jinnuoxin.html` | 客户案例页：成都金诺信（可见证据 + Review schema + BreadcrumbList） |
| `customers/fuzhou-gaoyi-guangxue.html` | 客户案例页：福州高意光学（可见证据 + Review schema + BreadcrumbList） |
| `contact.html` | 留资表单页：免费试用/企业部署咨询（ContactPage schema） |
| `llms.txt` | AI 可读站点摘要（Claude/GPT 等读取，含全站页面索引） |
| `robots.txt` | 放行 GPTBot/ClaudeBot/Google-Extended/PerplexityBot/CCBot 等 AI 爬虫 |
| `sitemap.xml` | 站点地图（6 URL） |

## 路线图

- [x] Phase 1 MVP：单页首页 + GEO 层（2026-09-24）
- [x] Phase 2：功能页/案例独立页/联系表单（5 页闭环）
- [ ] Phase 3：博客/解决方案/对比页（AI 高引内容）
  - [x] 应用场景 + 竞品对比页（scenario.html，2026-09-25）
  - [ ] 博客/深度文章

## 本地预览

```bash
# 任选：直接打开 index.html，或用 Python 起本地服务
python -m http.server 8000
```