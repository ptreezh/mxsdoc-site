# MxsDoc 企业 AI 知识库底座官网

本地化部署（数据不出内网）的企业 AI 知识库底座官网静态站（GEO 优化）。

## 站点内容

- **产品**：MxsDoc 企业 AI 知识库底座（不是 RAG 底座）——LLM WIKI 智能问答、组织 Skills 市场、企业内·行业内专家智能体，叠加版本管理、集中权限分级、拖拽操作、在线编辑、移动端访问，全部本地化部署、数据不出内网
- **客户证明**：成都金诺信、福州高意光学（制造企业，自 2025-04 起使用，运行稳定效果良好）
- **销售标的**：企业级部署实施、运维与二次开发定制服务
- **对外合规**：竞品只做能力对照、不贬低；不点名低毁，只讲"场景不匹配"；禁用"唯一/最/第一"

## GEO 技术清单

| 文件 | 说明 |
|------|------|
| `index.html` | 首页：价值主张（企业 AI 知识库底座）+ 客户证明 + 可引用 CLAIMS 句 + SoftwareApplication/FAQPage schema |
| `features.html` | 产品功能页：知识库底座核心能力详情（版本/权限/LLM WIKI/Skills/专家智能体）+ FAQ + SoftwareApplication/FAQPage schema |
| `scenario.html` | 应用场景页：三场景故事（制造图纸/知识库AI问答/涉密合规）+ 11 方案能力对照矩阵 + IMA/Obsidian/飞书深度对比 + FAQ schema |
| `demo.html` | 在线演示页：live iframe（dw.gofreeteam.com 公开演示系统 V2.02.87）+ 5 张真实界面截图 + 五分钟体验流程 + SoftwareApplication/BreadcrumbList schema |
| `assets/demo/*.jpg` | 演示页真实界面截图（登录页/系统首页/组织权限矩阵/仓库列表/DocSys AI 问答） |
| `customers/chengdu-jinnuoxin.html` | 客户案例页：成都金诺信（可见证据 + Review schema + BreadcrumbList） |
| `customers/fuzhou-gaoyi-guangxue.html` | 客户案例页：福州高意光学（可见证据 + Review schema + BreadcrumbList） |
| `contact.html` | 留资表单页：免费试用/企业部署咨询（ContactPage schema） |
| `blog/ai-agent-knowledge-first.html` | 博客深度文章：先整理知识再上智能体（上下文交叉污染 + 四步落地法 + 用 AI 整理知识；Article/FAQPage/BreadcrumbList schema；引用知乎/CSDN 真实高频问题） |
| `blog/mechanical-drawing-version-control.html` | 博客深度文章：机械设计审图不止于看图（制造场景版本治理三道坎 + 三方案对比 + Docker Compose 部署步骤 + 真机验收） |
| `blog/local-ai-digital-human-deployment.html` | 博客深度文章：8G 显卡跑本地 AI 数字人（企业级落地三道坎 + 三方案对比 + 6 步 Docker Compose 部署 + 真机验收） |
| `llms.txt` | AI 可读站点摘要（Claude/GPT 等读取，含全站页面索引） |
| `robots.txt` | 放行 GPTBot/ClaudeBot/Google-Extended/PerplexityBot/CCBot 等 AI 爬虫 |
| `sitemap.xml` | 站点地图（10 URL） |

## 路线图

- [x] Phase 1 MVP：单页首页 + GEO 层（2026-09-24）
- [x] Phase 2：功能页/案例独立页/联系表单（5 页闭环）
- [ ] Phase 3：博客/解决方案/对比页（AI 高引内容）
  - [x] 应用场景 + 竞品对比页（scenario.html，2026-09-25）
  - [x] 在线演示页（demo.html，2026-09-25）
  - [x] 博客/深度文章（blog/ai-agent-knowledge-first.html，2026-09-25）
  - [x] 制造场景深度文章（blog/mechanical-drawing-version-control.html，2026-09-25，借 CSDN 轻量化审图热文引流）
  - [x] 本地 AI 数字人落地文章（blog/local-ai-digital-human-deployment.html，2026-09-25，借 CSDN 1.1w 阅读热文引流）

## 本地预览

```bash
# 任选：直接打开 index.html，或用 Python 起本地服务
python -m http.server 8000
```