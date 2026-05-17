# AgentLens — PRD: 产品落地页

---

## 一、产品概述

### 产品名
**AgentLens**

### 定位
AI Agent 可观测性与治理平台 — 让每一支 AI Agent 都在你的掌控之中。

> 当所有人都在造 Agent，AgentLens 负责管好它们。

### Slogan
**See every agent. Control every outcome.**

（中文备选：看得见的 Agent，管得住的风险。）

---

## 二、目标用户

根据数据分析结论（77% 的 IT 经理表示 AI Agent 已失控），核心用户画像：

| 维度 | 描述 |
|------|------|
| 角色 | IT 经理、工程负责人、DevOps 团队 lead |
| 公司规模 | 50-500 人的中型企业，已部署 3+ 个 AI Agent |
| 痛点 | 不知道 Agent 在做什么、成本失控、安全风险不可见、没有统一的治理面板 |
| 技术背景 | 熟悉 API、Kubernetes、监控工具（Datadog、Grafana） |
| 决策驱动力 | 合规需求、成本控制、安全审计 |

---

## 三、用户痛点描述

### 痛点 1：Agent 失控

> "我们用了 5 个不同的 AI Agent——客服、代码审查、内容生成、数据分析、销售辅助。每个都有独立的管理后台，没有统一的视图。上周客服 Agent 突然产生了 $3,000 的 API 费用，我们 3 天后才发现。"

AI Agent 的采用正在爆炸式增长，但企业缺乏一个统一的仪表盘来回答最基本的问题：**有哪些 Agent 在运行？它们在调用什么模型？花了多少钱？**

### 痛点 2：成本黑洞

> "一个月前我批准了 $500 的 API 预算。月底账单来了——$4,700。没人能说清楚钱花在了哪里。"

LLM API 调用成本是变量费用，没有监控意味着没有上限。当 5 个 Agent × 每天数千次调用 × 不同模型定价时，账单失控只是时间问题。

### 痛点 3：安全盲区

> "第三方 Agent 读了我们内部的客户数据，发送给了 GPT-4。没人知道这件事，直到客户投诉。"

Agent 有权访问敏感数据，但没有审计日志追踪它们做了什么、访问了什么、数据去了哪里。合规团队无法回答审计问题。

---

## 四、核心功能

### 功能一：统一 Agent 目录

**自动发现并注册组织中所有 AI Agent，构建完整的 Agent 清单。**

不再需要问"我们到底有多少个 Agent？"。AgentLens 自动识别正在运行的 Agent，展示其模型、调用频率、权限范围和使用者。五分钟内，你就能获得整个组织 Agent 生态的全景图。

> 例如：统一目录会显示"客服 Agent 使用 GPT-4o，日均调用 2,300 次，归属市场部"，一目了然。

### 功能二：实时成本监控 + 预算控制

**监控每一笔 API 调用的成本，设置预算警报和自动熔断机制。**

按 Agent、团队、模型维度实时追踪花费。设置月度预算上限，当 Agent 调用接近阈值时自动通知；超额时自动降级到备用模型或暂停非关键 Agent。

> 例如：你可以设置"客服 Agent 月预算 $500，达到 80% 时发通知，超出时降级到 GPT-4o-mini"——不再有意外账单。

### 功能三：安全审计与策略引擎

**全链路记录 Agent 行为，自动检测异常访问和敏感数据泄露。**

每次 Agent 调用、每个数据访问、每次外部请求都被记录到不可篡改的审计日志中。策略引擎支持自定义规则：检测异常高频调用、阻止模型发布行为、标记包含敏感信息的输出。

> 例如：当客服 Agent 突然在凌晨 3 点调用数据库读取了 10,000 条客户记录，AgentLens 立即发出告警并自动阻断。

---

## 五、适用场景

| 场景 | 说明 |
|------|------|
| 多 Agent 部署管理 | 组织用了多个 Agent 但缺乏统一管理面板时，AgentLens 提供唯一入口 |
| API 成本治理 | CFO 追问 AI 支出时，给出按 Agent、团队、项目的精细化成本报告 |
| 合规审计准备 | SOC2/ISO 审计需要 Agent 行为记录时，一键导出审计日志 |
| Agent 上线审核 | 新 Agent 上线前，用策略引擎预审其权限和访问范围 |
| 异常行为告警 | Agent 行为偏离正常模式时（高频调用、异常数据访问），实时告警 |

---

## 六、SEO 关键词布局

### Meta Title
`AgentLens - AI Agent Observability & Governance Platform | Monitor, Control & Audit Your AI Agents`

### Meta Description
`AgentLens provides unified observability, cost monitoring, and security auditing for all your AI agents. Discover rogue agents, control API spend, and ensure compliance across your entire AI agent ecosystem. Start free.`

### H1
`See Every AI Agent. Control Every Outcome.`

### H2 标签
- `Your AI Agents Are Running Wild. Here's the Dashboard.`
- `Know What Every Agent Is Doing, Right Now`
- `Stop API Cost Surprises Before They Happen`
- `Audit Every Agent Action, Automatically`
- `Built for Teams That Can't Afford Agent Chaos`
- `Join the Waitlist`

### H3 标签
- `Unified Agent Directory — No More Blind Spots`
- `Real-Time Cost Monitoring & Budget Controls`
- `Security Audit Trail & Policy Engine`

---

## 七、落地页结构

```
Navigation: [Logo] AgentLens  |  Product  |  Docs  |  Pricing  |  [Join Waitlist]

Hero Section:
  - H1: See Every AI Agent. Control Every Outcome.
  - Sub: The first observability platform built for the age of autonomous AI agents.
  - CTA: Join the Waitlist
  - Social proof teaser: "Join 200+ engineering teams"

Problem Section:
  - Headline: Your AI Agents Are Running Wild
  - 3 pain points with icon + short copy

Solution Section:
  - Headline: Meet AgentLens
  - 3 feature cards (icon + title + description)

How It Works:
  - 3-step visual flow

Use Cases:
  4 scenario cards

Stats/Trust Bar:
  - Key metric: "77% of IT managers say AI agents are out of control"
  - Source: industry survey

Final CTA:
  - Headline: Don't Let Your AI Agents Run Your Budget
  - Sub: Join the waitlist. Be the first to know when AgentLens launches.
  - Email input + button

Footer: Product / Company / Legal
```
