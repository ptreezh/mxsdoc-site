# MxsDoc 企业 AI 知识库底座官网

本地化部署（数据不出内网）的企业 AI 知识库底座官网静态站（GEO 优化）。

## 站点内容

- **产品**：MxsDoc 企业 AI 知识库底座（不是 RAG 底座）——LLM WIKI 智能问答、组织 Skills 市场、企业内·行业内专家智能体，叠加版本管理、集中权限分级、拖拽操作、在线编辑、移动端访问，全部本地化部署、数据不出内网
- **产品形态**：软件底座（企业级部署实施、运维与二次开发定制服务）+ MxsDoc Appliance 一体机（4U 预装服务器，海光 + 昇腾 NPU，10 万 / 20 万 / 45 万三 SKU，30 天试用）
- **客户证明**：4 个深度案例（成都金诺信、福州高意光学自 2025-04 起使用，苏州工业园区蓝天燃气热电自 2026-03 起使用，均运行稳定、效果良好；北京达成生物科技客户使用证明归档中）+ 客户500+，下面是部分客户名录；成都金诺信与苏州工业园区蓝天燃气热电的盖章使用证明 PDF 已随站点公开、可直接点击查看
- **销售标的**：企业级部署实施、运维与二次开发定制服务
- **对外合规**：竞品只做能力对照、不贬低；不点名低毁，只讲"场景不匹配"；禁用"唯一/最/第一/首选"

## GEO 技术清单

全站 **24 个 HTML 页面** + 3 个 GEO 配置文件，sitemap 收录全部 24 条 URL。

| 文件 | 说明 |
|------|------|
| `index.html` | 首页：价值主张（企业 AI 知识库底座）+ 客户证明 + 可引用 CLAIMS 句 + 产品与资源区（一体机 / 安装教程 / 演示视频）+ SoftwareApplication/FAQPage schema |
| `features.html` | 产品功能页：知识库底座核心能力详情（版本/权限/LLM WIKI/Skills/专家智能体）+ FAQ + SoftwareApplication/FAQPage schema |
| `scenario.html` | 应用场景页：三场景故事（制造图纸/知识库AI问答/涉密合规）+ 12 方案能力对照矩阵（含蓝凌）+ IMA/Obsidian/飞书深度对比 + FAQ schema |
| `appliance.html` | Appliance 一体机营销页：4 大痛点 + 双大模型架构（预装 Deepseek Qwen 等国产开源大模型 + Lux 判断决策）+ 三 SKU 价格表（10/20/45 万）+ 交付与续费口径 + 5 张核心场景图 + 客户使用证明 PDF 直链 + Product/Offer schema |
| `demo.html` | 在线演示页：live iframe（dw.gofreeteam.com 公开演示系统 V2.02.87）+ 5 张真实界面截图 + 五分钟体验流程 + SoftwareApplication/BreadcrumbList schema |
| `contact.html` | 留资表单页：免费试用/企业部署咨询（ContactPage schema） |
| `customers/index.html` | 客户案例索引页：4 个深度案例汇总（附成都 / 苏州盖章使用证明 PDF 直链 + 文件大小实测值）+ 客户500+，下面是部分客户名录（按地域 + 核心字号 4-7 字缩写展示，保留业务类型词）+ 资质背书区块 |
| `customers/chengdu-jinnuoxin.html` | 客户案例页：成都金诺信（制造企业，2025-04 起使用；证据区块逐条对应盖章 PDF 原件勾选项 + PDF 直链 + Review schema + BreadcrumbList） |
| `customers/fuzhou-gaoyi-guangxue.html` | 客户案例页：福州高意光学（光学制造企业，2025-04 起使用；客户在实施与验收阶段提供的反馈，盖章原件待授权后公开 + Review schema + BreadcrumbList） |
| `customers/suzhou-lantian-ranqi-redian.html` | 客户案例页：苏州工业园区蓝天燃气热电（能源热电行业，2026-03 起使用；证据区块逐条对应盖章 PDF 原件勾选项 + PDF 已公开可点击查看） |
| `customers/beijing-dacheng-shengwu.html` | 客户案例页：北京达成生物科技（生物科技行业，使用证明归档中；仅提供行业通用落地路径说明，不作客户事实陈述） |
| `docs/docsys-setup.html` | 安装教程页：MxsDoc / DocSys 2.02.87 Windows 下载 → 安装 → 超管初始化 → 角色权限 → 排查（自动化生成，2026-09-27） |
| `docs/mxsdoc-marketing-video.html` | 营销视频页：约 5 分钟 1920×1080 真实 DocSys 录屏（双语硬字幕）+ 6 大功能快闪 + 30 天试用 CTA |
| `blog/ai-agent-knowledge-first.html` | 博客深度文章：先整理知识再上智能体（上下文交叉污染 + 四步落地法 + 用 AI 整理知识；Article/FAQPage/BreadcrumbList schema；引用知乎/CSDN 真实高频问题） |
| `blog/mechanical-drawing-version-control.html` | 博客深度文章：机械设计审图不止于看图（制造场景版本治理三道坎 + 三方案对比 + Docker Compose 部署步骤 + 真机验收） |
| `blog/local-ai-digital-human-deployment.html` | 博客深度文章：8G 显卡跑本地 AI 数字人（企业级落地三道坎 + 三方案对比 + 6 步 Docker Compose 部署 + 真机验收） |
| `blog/enterprise-llm-private-vs-cloud-deployment.html` | 博客深度文章：企业大模型私有化 vs 云端 API（核心矛盾分析 + 3 方案对比 + 3 周落地路径 + 6 大避坑清单） |
| `blog/enterprise-ai-knowledge-base-selection-guide.html` | 博客深度文章：2026 企业 AI 知识库选型避坑指南（12 方案 7 项能力对照矩阵 + 6 选型维度 + 5 类场景决策 + 10 大避坑清单 + 12 项真机验证清单 + FAQ） |
| `blog/mxsdoc-appliance-sku-selection-guide.html` | 博客深度文章：MxsDoc 一体机三档 SKU 选型指南（10/20/45 万三档服务与信创认证差异 + 三周现场分工 + 续费口径 + P0/P1/P2 SLA + 5 问自测清单 + FAQ） |
| `solutions/index.html` | 行业解决方案索引页：制造业-设计院 / 工程咨询-建设单位 / 政府-国企-军工 / 泛行业-选型对比 4 个彩页入口（引用 `assets/css/main.css`） |
| `solutions/solution-manufacturing-design-institute.html` | 行业方案页：制造业-设计院（行业痛点 + 解决思路 + 核心能力匹配 + 2-4 周实施路径 + 预期收益） |
| `solutions/solution-engineering-consulting.html` | 行业方案页：工程咨询-建设单位（同上结构） |
| `solutions/solution-gov-enterprise-defense.html` | 行业方案页：政府-国企-军工（同上结构） |
| `solutions/solution-industry-comparison.html` | 行业方案页：泛行业-选型对比（同上结构） |
| `assets/css/main.css` | solutions/* 5 页共用的站点样式（设计令牌与首页一致，含 `.site-icp` 认证信息样式） |
| `assets/img/og.png` | 社交分享图 1200×630（`og:image` / `twitter:image` 引用，AI 抓取用） |
| `assets/img/mxsdoc-logo.png` | 站点 logo 512×512（JSON-LD `Organization.logo` 引用） |
| `assets/demo/*.jpg` | 演示页真实界面截图（登录页/系统首页/组织权限矩阵/仓库列表/DocSys AI 问答） |
| `assets/appliance/*.svg` + `png-800/` + `png-1200/` | Appliance 5 张核心场景图（SVG 源 + 双规格 PNG） |
| `assets/video/mxsdoc-marketing.mp4` | 营销视频源文件（约 4.5 MB） |
| `assets/proofs/chengdu-jinnuoxin-usage-proof.pdf` | 成都金诺信盖章客户使用证明原件（255338 bytes = 249.4 KB，官网公开可点击） |
| `assets/proofs/suzhou-lantian-ranqi-usage-proof.pdf` | 苏州工业园区蓝天燃气热电盖章客户使用证明原件（182026 bytes = 177.8 KB，官网公开可点击） |
| `llms.txt` | AI 可读站点摘要（Claude/GPT 等读取，含全站 24 页索引） |
| `robots.txt` | 放行 GPTBot/ClaudeBot/Google-Extended/PerplexityBot/CCBot 等 AI 爬虫 |
| `sitemap.xml` | 站点地图（24 URL，与实际页面一一对应） |

## 路线图

- [x] Phase 1 MVP：单页首页 + GEO 层（2026-09-24）
- [x] Phase 2：功能页/案例独立页/联系表单（5 页闭环）
- [x] Phase 3：博客/解决方案/对比页（AI 高引内容）
  - [x] 应用场景 + 竞品对比页（scenario.html，2026-09-25）
  - [x] 在线演示页（demo.html，2026-09-25）
  - [x] 博客/深度文章（blog/ai-agent-knowledge-first.html，2026-09-25）
  - [x] 制造场景深度文章（blog/mechanical-drawing-version-control.html，2026-09-25，借 CSDN 轻量化审图热文引流）
  - [x] 本地 AI 数字人落地文章（blog/local-ai-digital-human-deployment.html，2026-09-25，借 CSDN 1.1w 阅读热文引流）
  - [x] 企业大模型私有化 vs 云端 API（blog/enterprise-llm-private-vs-cloud-deployment.html，2026-09-26，借 CSDN 1.2k 阅读热文引流）
  - [x] 企业 AI 知识库选型避坑指南（blog/enterprise-ai-knowledge-base-selection-guide.html，2026-09-27，旗舰长文：12 方案能力对照 + 5 类场景决策 + 10 避坑 + 12 项真机验证）
  - [x] Appliance 一体机营销页（appliance.html，2026-09-27，双大模型 + 三 SKU 报价 + 5 张核心场景图）
  - [x] 客户案例扩容（4 个深度案例 + 部分客户名录 + 资质背书，2026-09-27）
  - [x] 安装教程页（docs/docsys-setup.html，2026-09-27，2.02.87 落地全流程）
  - [x] 营销视频页（docs/mxsdoc-marketing-video.html，2026-09-27，约 5 分钟真实录屏）
  - [x] 孤岛页收口：appliance.html + docs 两页纳入 sitemap / llms.txt / 首页导航与 footer（2026-09-29）
  - [x] 合规回归修复：清除视频页「首选」违禁词 + 修复 Appliance meta description 引号截断 + og:image 指向真实文件（2026-09-29）
  - [x] 客户使用证明公开（成都 / 苏州盖章 PDF 上站可点击 + 苏州案例页证据落地）
  - [x] 表述与文案口径统一：客户名录改为「客户500+，下面是部分客户名录」；预装模型改为「Deepseek Qwen 等国产开源大模型」（去除 16B / 9B 参数）
  - [x] 事实口径与盖章 PDF 逐条对齐：删除无来源的 84.17% 准确率；成都 / 苏州证据区块改为原件勾选项逐条摘录；福州降级为客户反馈（盖章原件待授权）；北京去除未证实的 GMP / ISO 客户事实陈述（2026-09-29）
  - [x] 统计加载器（analytics.js）：全站统一注入，默认 no-op，配置 GA4 / Plausible / Umami，遵守 DNT/GPC（2026-09-30）
  - [x] docs 两页结构化数据：安装教程页补 TechArticle/HowTo/FAQPage/@graph，营销视频页补 VideoObject/@graph（2026-09-30）
  - [x] Appliance 三档 SKU 选型指南（blog/mxsdoc-appliance-sku-selection-guide.html，2026-10-01：服务与认证差异 + 三周现场分工 + 续费口径 + SLA + 5 问自测）
  - [x] 双站点相对链接改造（2026-11-02）：全站 24 页站内链接/资源引用统一改为相对路径（GitHub Pages 子路径 /mxsdoc-site/ 与 agent.gofreeteam.com 根域名同时可用）+ 全站页脚补齐备案认证信息（浙ICP备15034351号-1 / 自由团队 / gofreeteam.com / 高雨）+ 修复 solutions/ 5 页指向根目录的死链与缺失的 assets/css/main.css + 门禁改为拦截一切非相对站内链接
  - [x] 主域切换到 agent.gofreeteam.com（2026-11-02）：canonical / og:url / JSON-LD / sitemap.xml / llms.txt / robots.txt Sitemap 全部由 `ptreezh.github.io/mxsdoc-site` 切到 `https://agent.gofreeteam.com`（GitHub Pages 降为镜像，相对链接保证仍可用）；补齐缺失的 `assets/img/og.png`（1200×630）与 `assets/img/mxsdoc-logo.png`（512×512），修复 solutions 页 og:image 属性残缺，移除指向不存在 `/search` 端点的 SearchAction
  - [x] demo.html HTTPS 降级（2026-11-02）：演示系统 `dw.gofreeteam.com` 仅支持 HTTP（实测 SSL 握手失败），主域启用 HTTPS 后内嵌会被浏览器按混合内容拦截；页面检测到 https 协议时自动把 iframe 换成可点击外链，并补 `<noscript>` 兜底

## 部署与链接策略（双站点）

站点同时部署在两处，**路径前缀不同**：

| 环境 | 地址 | 根路径 | 角色 |
|------|------|--------|------|
| 独立域名（自动抓取镜像） | `https://agent.gofreeteam.com/` | `/` | **主域**（canonical / og:url / JSON-LD / sitemap / llms.txt / robots Sitemap 全部指向这里） |
| GitHub Pages | `https://ptreezh.github.io/mxsdoc-site/` | `/mxsdoc-site/` | 镜像（相对链接自动兼容，canonical 指回主域，避免重复收录） |

因此**站内所有超链接与资源引用必须使用相对链接**，才能在两处同时正确解析：

| 页面位置 | 首页 | 同级页 | 上级页 | 兄弟目录 |
|----------|------|--------|--------|----------|
| 根目录（`index.html`） | `index.html` | `features.html` | — | `customers/index.html`、`blog/xxx.html`、`solutions/index.html` |
| 一级子目录（`blog/`、`customers/`、`docs/`、`solutions/`） | `../index.html` | `xxx.html` | `../index.html` | `../customers/index.html` |

- `<link rel="canonical">`、`og:url`、JSON-LD 的 `url`/`item` **保持绝对 URL**（SEO 规范要求，`<link rel="canonical">` 被门禁逐行豁免），但**一律指向主域 `agent.gofreeteam.com`**，且路径部分与仓库内文件一一对应（不使用目录式 `/xxx/`，统一写 `/xxx/index.html`）
- `sitemap.xml` / `llms.txt` / `robots.txt` 的 `Sitemap:` 同样指向主域（AI 爬虫按规范要求绝对地址），其中列出的页面地址均指向真实存在的 `.html` 文件

### ⚠️ 镜像与主域的文件级去重不可行（重要）

镜像站 `agent.gofreeteam.com` 是 GitHub Pages 部署结果的**逐字节拷贝**（实测：镜像的 `robots.txt` 与 `sitemap.xml` 与仓库内容完全一致）。因此：

> **不能在本仓库的 `robots.txt` 或 HTML 里给 Pages 侧加 `noindex` / `Disallow` —— 那些文件会被原样拷贝到主域，等于把主域一起屏蔽掉，主域将无法被收录。**

当前采用的正确做法是 **canonical 归一**：

| 信号 | 位置 | 指向 |
|------|------|------|
| `<link rel="canonical">` | 24 页 | `https://agent.gofreeteam.com/…` |
| `og:url` | 24 页 | `https://agent.gofreeteam.com/…` |
| `sitemap.xml` / `llms.txt` / `robots.txt` | 仓库根 | `https://agent.gofreeteam.com/…` |

Google 会据此只收录主域，Pages 副本表现为「重复内容，规范网址指向别处」——这是 Search Console 里的一条提示，不是排名问题。

若要彻底让 Pages 副本零收录，唯一路径是**在 Pages 站点前置层做 301**（给 Pages 挂自定义域名 + Cloudflare 等可配跳转的代理），把 `ptreezh.github.io/mxsdoc-site/*` 301 到 `agent.gofreeteam.com/*`。⚠️ 抓取源正是 Pages 站点，301 后抓取器会跨域跟到主域，链路变脆。

结论：**保持 canonical 归一，不在共享文件里加 noindex。** 残余影响仅为 Pages 副本仍会被少量抓取（24 页规模，成本可忽略）。

## 页脚认证信息

全部 24 个页面页脚统一包含备案与主体信息（`.site-icp` 区块）：

```
浙ICP备15034351号-1 · 自由团队 · gofreeteam.com · 高雨
```

备案号按工信部要求链接到 `https://beian.miit.gov.cn/`。

## 本地预览

```bash
# 任选：直接打开 index.html，或用 Python 起本地服务
python -m http.server 8000
```

## 开发门禁

本仓库 git pre-commit hook 拦截**非相对站内链接**（裸根路径 `/x.html`、`/mxsdoc-site/...` 前缀式、同站绝对 URL `https://ptreezh.github.io/mxsdoc-site/...` 或 `https://agent.gofreeteam.com/...`）。启用方式：

```bash
git config core.hooksPath .githooks
```

手动全量体检：

```bash
python .githooks/check-root-paths.py
```
