# Feishu Aily Skills Collection

This folder contains skills migrated from **Feishu Aily (飞书 Aily 智能体)**. The purpose of sharing these on GitHub is to help developers learn how to write SKILL.md files for OpenClaw.

## About

These skills were originally built for the Feishu Aily platform and have been migrated to work with OpenClaw. Each skill is self-contained in its own directory with a `SKILL.md` file that defines the skill's behavior, triggers, and instructions.

## What is a SKILL.md?

A `SKILL.md` file is a markdown document that teaches an AI agent how to perform specific tasks. It typically includes:

- **Frontmatter metadata** (lines 1-5): Contains `name`, `label`, and `description` fields
- **Instructions**: Detailed guidance on when and how to execute the skill
- **References**: Optional supporting documentation
- **Scripts**: Optional executable scripts for the skill

## Skills List

### 📄 Document Generation (aily-doc-*)

| Name | Label | Description |
|------|-------|-------------|
| `aily-doc-annual-report` | 文档创作年度报告 | 文档创作年度报告：主要借助 `aily-doc` 获取用户年度文档信息（数量、点赞、评论、PV、UV 等），并基于这些指标与代表性文档产出年度总结型飞书云文档。 |
| `aily-doc-business-plan` | 商业计划书 | 商业计划书：强调市场机会、产品与商业模式、竞争、团队、财务与风险，形成可评审BP。 |
| `aily-doc-business-review-report` | 季度/年度业务汇报 | 季度/年度业务汇报：围绕指标达成、业务进展、问题与对策输出结构化业务汇报。 |
| `aily-doc-company-research` | 公司调研 | 公司调研：基于官方与公开信息输出公司概况、业务结构、竞争位置、经营与风险的结构化研究。 |
| `aily-doc-competitive-analysis` | 竞品分析 | 竞品分析：通过统一维度对比产品与市场信息，形成结构化对比结论与机会点。 |
| `aily-doc-concept-explainer` | 概念解释 | 概念解释：由浅入深讲清概念的定义、原理与本质，面向不同知识背景的读者。 |
| `aily-doc-group-chat-summary` | 群聊内容摘要 | 基于飞书群聊的**智能摘要与洞察**生成能力。从指定群聊/时间范围的消息中提取关键信息，识别决策、行动项、风险，生成**飞书云文档结构化摘要**。 |
| `aily-doc-industry-research` | 行业研究报告 | 面向特定行业/赛道的**系统性深度研究**能力。从行业定义、市场规模、竞争格局、技术趋势、政策环境、投融资动态等多维度进行**广覆盖、深挖掘**的全面调研，输出结构化的行业研究报告。 |
| `aily-doc-marketing-campaign-plan` | 活动营销方案 | 活动营销方案：明确目标人群、核心卖点、传播节奏、渠道矩阵、预算与风险，形成可执行方案。 |
| `aily-doc-paper-deepresearch` | 前沿论文解读 | 面向学术论文的**原文级调研（Deep Research）**能力模块。适用于：用户指定某篇论文要求"读透 + 追踪背景 + 扩展最新相关工作"，或用户给出某个学术 topic 要求系统性深度调研与写作综述。 |
| `aily-doc-pre-meeting-brief` | 会前材料准备 | 会前材料准备：围绕会议议题、决策点与材料清单，结合历史会议纪要与当前任务进展，生成可讨论、可决策的会前材料。 |
| `aily-doc-product-launch-materials` | 产品发布会材料 | 产品发布会材料：聚焦卖点、发布流程、演示与FAQ，适用于对外宣讲与发布会材料。 |
| `aily-doc-project-kickoff-report` | 项目启动报告 | 项目启动报告：统一目标、范围、里程碑、分工与风险，形成可落地的启动材料。 |
| `aily-doc-technical-solution` | 技术方案 | 技术方案：围绕业务目标与约束，输出架构设计、关键模块、技术选型、风险与实施计划的完整技术方案。 |
| `aily-doc-topic-trend-report` | 新闻总结 | 根据用户指定的**主题**和**时间范围**，自动检索权威动态，生成一份**飞书云文档动态报告**，按类别聚类，每条新闻含 intro / description / 索引链接。强调**时间筛选 + 权威优先 + 去重**。 |
| `aily-doc-weekly-work-report` | 工作周报 | 基于飞书生态的**每周周报**自动生成 Skill：从当周**日程、任务、妙记、云文档**中提取工作内容，使用 `knowledge_answer` 兜底补全遗漏信息，最终调用 `doc_agent (writer)` 生成结构化的飞书云文档周报。 |

### 🔧 System & Utilities

| Name | Label | Description |
|------|-------|-------------|
| `aily-self-improvement` | - | Captures learnings, errors, and corrections to enable continuous improvement. Use when: (1) An operation or tool fails unexpectedly, (2) User corrects the agent, (3) User requests a capability that doesn't exist, (4) A better approach or knowledge gap is discovered. Also review learnings before major tasks. |
| `aily-skill-creator` | AI生成技能 | 帮助用户创建和更新技能，扩展 aily 工作助手的功能。 |
| `memory-management` | 记忆管理 | 两级记忆系统，让 aily 成为真正的工作协作者。解码速记、缩写、昵称和内部用语，让 aily 像同事一样理解请求。aily.md 用于工作记忆，memory/ 目录用于完整知识库。 |
| `openclaw` | 上下文工作区 | 借鉴 OpenClaw 的工作区理念，通过 soul.md、user.md、tools.md 等结构化文件管理 aily 的身份、用户画像和环境上下文。支持工作区初始化、会话上下文注入、每日记忆日志和上下文生命周期管理。与 memory-management 技能互补使用。 |
| `task-management` | 任务管理 | 基于共享 TASKS.md 文件的简易任务管理。适用于用户查询任务状态、添加/完成任务或需要跟踪待办事项时使用。 |
| `skill-checker` | - | Use this skill when the user wants to check, test, or optimize a skill. Covers: testing whether a skill's description triggers correctly, optimizing description wording, scanning whether a skill works in a target environment, and adapting a skill to use environment-specific capabilities. |
| `feishu-context` | - | 飞书上下文缓存与构建。将群消息、联系人缓存到本地，按话题整合为结构化上下文。触发场景: "之前聊的那个事帮我看看"、"XX最近什么进展"、"帮我捋一下XX相关的信息"。 |

### 📊 Data & Analytics

| Name | Label | Description |
|------|-------|-------------|
| `analytics-tracking` | - | Use this skill for analytics tracking implementation and measurement setup: GA4, Google Tag Manager, Mixpanel, Segment, event tracking, conversion tracking, UTM parameters, data layer configuration, and debugging analytics that aren't firing. Use when users want to measure marketing results, track user behavior, create tracking plans, or implement attribution. |
| `data-context-extractor` | 数据上下文提取 | 通过提取分析师的领域知识，生成或改进公司级数据分析技能。 |
| `data-exploration` | 数据探索 | 数据集画像和探索，理解数据的结构、质量和分布模式。适用于接触新数据集、评估数据质量、发现列分布、识别空值和异常值，或决定分析维度。 |
| `data-validation` | 数据验证 | 在分享给干系人前对分析进行 QA 检查——方法论验证、准确性核实和偏差检测。适用于审查分析错误、检查幸存者偏差、验证聚合逻辑或准备可复现性文档。 |
| `data-visualization` | 数据可视化 | 使用 Python（matplotlib、seaborn、plotly）创建数据可视化。适用于构建图表、选择图表类型、创建出版级图形或应用无障碍和色彩理论等设计原则。 |
| `interactive-dashboard-builder` | 交互式仪表盘构建 | 使用 Chart.js 构建自包含的交互式 HTML 仪表盘，支持下拉筛选和专业样式。适用于创建仪表盘、交互式报告或生成无需服务器即可运行的可分享 HTML 文件。 |
| `sql-queries` | SQL查询 | 跨主流数仓方言（Snowflake、BigQuery、Databricks、PostgreSQL 等）编写正确且高性能的 SQL。适用于编写查询、优化慢 SQL、跨方言转换，或构建包含 CTE、窗口函数和聚合的复杂分析查询。 |
| `statistical-analysis` | 统计分析 | 应用描述性统计、趋势分析、异常值检测和假设检验等统计方法。适用于分析分布、显著性检验、异常检测、相关性计算或统计结果解读。 |
| `metrics-tracking` | - | Define, track, and analyze product metrics with frameworks for goal setting and dashboard design. Use when setting up OKRs, building metrics dashboards, running weekly metrics reviews, identifying trends, or choosing the right metrics for a product area. |
| `performance-analytics` | 营销绩效分析 | 分析营销绩效，包含关键指标、趋势分析和优化建议。适用于构建绩效报告、回顾活动效果、分析渠道指标（邮件、社媒、付费、SEO）或识别有效策略和改进方向。 |
| `variance-analysis` | - | 财务差异分析专家。将预算与实际（Budget vs Actual）的差异分解为驱动因素，提供叙述性解释和瀑布图分析。适用于分析预算执行偏差、同比环比变化、收入或费用差异，或为管理层准备差异分析报告。 |
| `single-cell-rna-qc` | 单细胞RNA质控 | 对单细胞 RNA-seq 数据（.h5ad 或 .h5 文件）执行质控，使用 scverse 最佳实践的 MAD 过滤和综合可视化。适用于 QC 分析、低质量细胞过滤、数据质量评估或遵循 scverse/scanpy 单细胞分析最佳实践。 |

### 💼 Sales & Marketing

| Name | Label | Description |
|------|-------|-------------|
| `brainstorming` | - | Use this skill when the user wants to discuss, plan, or design something BEFORE implementation. Triggers for: exploring ideas, gathering requirements, creating design specs, comparing architectural approaches, or reviewing design decisions. |
| `brand-voice` | 品牌语调 | 在内容中应用和维护品牌语调、风格指南和核心信息。适用于审查内容一致性、记录品牌调性、适配不同受众语气或检查术语和风格合规。 |
| `call-prep` | 电话准备 | 为销售电话准备客户背景、与会者调研和议程建议。独立使用 Web 搜索即可工作，接入 CRM、邮件、聊天或会议记录后效果更佳。触发词：「帮我准备和 [公司] 的电话」「电话准备 [公司]」。 |
| `campaign-planning` | 营销活动策划 | 使用 OAMC 框架（目标、受众、信息、渠道、衡量）规划营销活动，涵盖受众分群、渠道策略、内容日历和 KPI 设定。适用于活动上线、产品发布、内容排期或预算分配。 |
| `competitive-analysis` | - | Analyze competitors with feature comparison matrices, positioning analysis, and strategic implications. Use when researching a competitor, comparing product capabilities, assessing competitive positioning, or preparing a competitive brief for product strategy. |
| `competitive-intelligence` | 竞争情报 | 深度调研竞品并生成交互式 HTML 竞争卡片，包含产品对比矩阵和销售话术。触发词：「竞争情报」「调研竞品」「我们和 [竞品] 怎么比」「[竞品] 的战卡」。 |
| `competitor-alternatives` | - | Use this skill when the user wants to create competitor comparison or alternative pages for websites, landing pages, or SEO content. Trigger on requests mentioning 'alternative page,' 'vs page,' 'competitor comparison page,' '[Product] vs [Product],' '[Product] alternative,' etc. |
| `content-creation` | 内容创作 | 撰写多渠道营销内容——博客、社交媒体、邮件、落地页、新闻稿和案例研究。适用于任何营销内容写作，支持渠道专属格式、SEO 优化、标题选项和行动号召。 |
| `content-strategy` | - | When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. Also use when the user mentions "content strategy," "what should I write about," "content ideas," "blog strategy," "topic clusters," etc. |
| `copy-editing` | - | When the user wants to edit, review, or improve existing marketing copy. Also use when the user mentions 'edit this copy,' 'review my copy,' 'copy feedback,' 'proofread,' 'polish this,' 'make this better,' etc. |
| `copywriting` | - | When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages. |
| `daily-briefing` | 每日销售简报 | 提供每日优先级排序的销售简报。独立使用时需手动输入会议和优先事项，接入日历、CRM 和邮件后效果更佳。触发词：「晨间简报」「今日安排」「帮我准备今天的工作」。 |
| `draft-outreach` | 外联邮件撰写 | 先调研潜客再撰写个性化外联邮件，默认使用 Web 搜索，接入数据增强和 CRM 后效果更佳。触发词：「给 [人/公司] 写外联邮件」「写冷启动邮件给 [潜客]」。 |
| `launch-strategy` | - | When the user wants to plan or create a launch strategy, release plan, or go-to-market strategy for their OWN product, feature, or announcement—including minor updates and bug fixes. |
| `marketing-competitive-analysis` | 营销竞品分析 | 调研竞品并对比定位、信息传递、内容策略和市场表现。适用于竞品分析、构建竞争卡片、识别内容缺口、对比功能宣传或准备竞争定位建议。 |
| `marketing-ideas` | - | When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. Also use when the user asks for 'marketing ideas,' 'growth ideas,' 'how to market,' 'marketing strategies,' etc. |
| `marketing-psychology` | - | Use when the user wants to apply psychological principles, mental models, or behavioral science to marketing. Trigger on mentions of 'psychology,' 'mental models,' 'cognitive bias,' 'persuasion,' etc. |
| `pricing-strategy` | - | Use this skill when the user wants help with pricing decisions, packaging, or monetization strategy. Trigger on: figuring out what to charge, how to structure pricing tiers, choosing value metrics, freemium vs free trial decisions, etc. |
| `product-competitive-analysis` | 产品竞品分析 | 通过功能对比矩阵、定位分析和战略影响评估来分析竞品。适用于竞品调研、产品能力对比、竞争定位评估或为产品战略准备竞品简报。 |
| `product-marketing-context` | - | When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'positioning,' etc. |
| `programmatic-seo` | - | When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "directory pages," etc. |
| `social-content` | - | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or other platforms. |

### ⚖️ Legal & Compliance

| Name | Label | Description |
|------|-------|-------------|
| `canned-responses` | 法务模板回复 | 为常见法律咨询生成模板化回复，同时识别需要个案处理的情形。适用于数据主体请求、供应商咨询、NDA 请求、诉讼保全通知等日常法律问题的回复管理。 |
| `compliance` | 合规管理 | 导航隐私法规（GDPR、CCPA），审查数据保护协议，处理数据主体请求。适用于审查数据处理协议、响应数据主体访问/删除请求、评估跨境数据传输要求或隐私合规评估。 |
| `contract-review` | 合同审查 | 依据组织谈判手册审查合同，标记偏差并生成修改建议。适用于审查供应商合同、客户协议或任何需要逐条对比标准条款的商业协议。 |
| `legal-risk-assessment` | 法律风险评估 | 使用严重性×可能性框架评估和分类法律风险，包含升级标准。适用于评估合同风险、交易敞口、问题分级，或判断是否需要高级法律顾问介入。 |
| `nda-triage` | 保密协议分拣 | 筛选收到的 NDA，按绿灯（标准）、黄灯（需审查）、红灯（重大问题）分类。适用于销售或商务拓展提交新 NDA 时的风险评估和路由决策。 |

### 💰 Finance & Accounting

| Name | Label | Description |
|------|-------|-------------|
| `audit-support` | - | Support SOX 404 compliance with control testing methodology, sample selection, sample size determination, and documentation standards. Use when generating testing workpapers, selecting audit samples, determining sample sizes, etc. |
| `close-management` | - | Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close progress, identifying blockers, or sequencing close activities by day. |
| `compensation-benchmarking` | - | Benchmark compensation against market data. Trigger with "what should we pay", "comp benchmark", "market rate for", "salary range for", "is this offer competitive", etc. |
| `financial-statements` | - | Generate income statements, balance sheets, and cash flow statements with GAAP presentation and period-over-period comparison. Use when preparing financial statements for reporting or filing. |
| `journal-entry-prep` | - | Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization, fixed asset depreciation, payroll entries, etc. |
| `reconciliation` | - | Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data. Use when performing bank reconciliations, GL-to-subledger recs, intercompany reconciliations, etc. |

### 🧪 Science & Research

| Name | Label | Description |
|------|-------|-------------|
| `scientific-problem-selection` | 科研选题 | 辅助科研人员进行选题、项目构思、困境突破和战略决策。适用于用户想要推介新研究想法、解决项目难题、评估项目风险、规划研究策略或需要科研方向建议时使用。 |
| `instrument-data-to-allotrope` | 仪器数据转换 | 将实验室仪器输出文件（PDF、CSV、Excel、TXT）转换为 Allotrope Simple Model (ASM) JSON 格式或扁平化 2D CSV。适用于科学家将仪器数据标准化以导入 LIMS 系统、数据湖或下游分析。 |

### 👥 HR & People

| Name | Label | Description |
|------|-------|-------------|
| `employee-handbook` | - | Answer employee questions about company policies, benefits, and procedures. Use when users ask about PTO, vacation, sick leave, parental leave, health insurance, 401k, remote work policy, etc. |
| `interview-prep` | - | Help hiring managers and interviewers create structured interview plans with competency-based questions and scorecards for evaluating candidates. |
| `org-planning` | - | Headcount planning, org design, and team structure optimization. Trigger with "org planning", "headcount plan", "team structure", "reorg", etc. |
| `people-analytics` | - | Analyze workforce data — attrition, engagement, diversity, and productivity. Trigger with "attrition rate", "turnover analysis", "diversity metrics", etc. |
| `recruiting-pipeline` | - | Track and manage recruiting pipeline stages. Trigger with "recruiting update", "candidate pipeline", "how many candidates", "hiring status", etc. |

### 🛠️ Engineering & Development

| Name | Label | Description |
|------|-------|-------------|
| `backend-testing` | - | Write comprehensive backend tests including unit tests, integration tests, and API tests. Use when testing REST APIs, database operations, authentication flows, business logic, etc. |
| `feature-spec` | - | Write structured product requirements documents (PRDs) with problem statements, user stories, requirements, and success metrics. |
| `receiving-code-review` | - | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable. |
| `systematic-debugging` | - | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. |
| `tailwind-design-system` | - | Tailwind CSS v4 design system toolkit. Use for creating React components with Tailwind v4, configuring @theme and design tokens, implementing dark mode, etc. |
| `test-driven-development` | - | Use when implementing any feature or bugfix, before writing implementation code. |
| `verification-before-completion` | - | Use when about to claim work is complete, fixed, verified, or passing, before committing or creating PRs. |
| `writing-plans` | - | Use when you have a spec or requirements document for implementing a feature, and need to create a detailed development plan with exact file paths, test strategies, and step-by-step coding tasks. |
| `writing-skills` | - | Use when checking, testing, or reviewing existing skills for trigger accuracy, environment compatibility, or deployment readiness. |

### 🔗 Integrations & Platforms

| Name | Label | Description |
|------|-------|-------------|
| `bilibili-cli` | - | Interact with Bilibili (B站/哔哩哔哩) via CLI — fetch video info, subtitles, comments, download audio, search users/videos, browse trending rankings, manage favorites, and perform interactions. |
| `feishu-project-official` | 飞书项目-官方 | 飞书项目（Meego/Meegle）操作工具。支持查询和管理工作项、节点流转、视图查询、个人待办、排期统计等功能。 |
| `humanizer-zh` | - | 检测并去除文本中特定的 AI 生成痕迹，使其更像人类自然书写。当用户明确提及 AI 写作特征、机器生成感、ChatGPT 风格或需要去除 AI 痕迹时使用。 |
| `xiaohongshu-cn` | - | 小红书分析 - 热门笔记发现、关键词监控、趋势分析（Instagram 中国版）。 |

### 🎯 Support & Operations

| Name | Label | Description |
|------|-------|-------------|
| `customer-research` | - | Use this skill to research customer-specific questions and investigate account contexts. Search across internal documentation, knowledge bases, CRM records, and connected sources. |
| `escalation` | - | Structure and package support escalations for engineering, product, or leadership with full context, reproduction steps, and business impact. |
| `knowledge-management` | - | Write and maintain knowledge base articles from resolved support issues. Use when a ticket has been resolved and the solution should be documented. |
| `response-drafting` | - | Draft professional, empathetic customer-facing responses adapted to the situation, urgency, and channel. Use when responding to customer tickets, escalations, outage notifications, etc. |
| `ticket-triage` | - | Triage incoming support tickets by categorizing issues, assigning priority P1-P4, and recommending routing. Use when a new ticket or customer issue comes in. |

### 📋 Other

| Name | Label | Description |
|------|-------|-------------|
| `meeting-briefing` | 会议简报 | 为具有法律相关性的会议准备结构化简报并跟踪行动项。适用于合同谈判、董事会会议、合规审查或任何需要法律背景、调研资料或行动跟踪的会议。 |
| `roadmap-management` | - | Plan and prioritize product roadmaps using frameworks like RICE, MoSCoW, and ICE. Use when creating a roadmap, reprioritizing features, mapping dependencies, etc. |
| `stakeholder-comms` | - | Draft stakeholder updates tailored to audience — executives, engineering, customers, or cross-functional partners. |
| `user-research-synthesis` | - | Synthesize qualitative and quantitative user research into structured insights and opportunity areas. |
| `using-superpowers` | - | Use this skill at the beginning of EVERY user request to check for specialized skills before acting. |
| `ux-writer` | - | Use this skill when the user needs to write, refine, or translate UI copy for product interfaces — including button labels, tooltips, error messages, etc. |

## Directory Structure

```
skills/
├── skill-name/
│   ├── SKILL.md          # Main skill definition (required)
│   ├── references/       # Supporting documentation (optional)
│   │   └── *.md
│   ├── scripts/          # Executable scripts (optional)
│   │   └── *.py
│   └── templates/        # Template files (optional)
│       └── *.md
```

## How to Use

1. Browse the skills list above to find one that matches your needs
2. Navigate to the skill's directory
3. Read the `SKILL.md` file to understand the skill's purpose and triggers
4. If the skill has `references/` or `scripts/`, explore those for additional context

## Contributing

Feel free to use these skills as templates for creating your own OpenClaw skills. The key to a good skill is:

- **Clear triggers**: Make it obvious when the skill should be activated
- **Focused scope**: Each skill should do one thing well
- **Good documentation**: Include examples and edge cases
- **Optional references**: Provide additional context when needed

## License

Each skill may have its own license. Please check individual directories for license information.
