# BoundAI - Product Requirements Document (PRD)

---

## Product Overview

- **Product Name:** BoundAI
- **Tagline:** Set guardrails your AI agents can't cross
- **Positioning:** The oversight layer for small businesses using autonomous AI agents
- **One-line Description:** A lightweight SaaS platform that lets small business owners set hard constraints -- spending caps, inventory limits, pricing floors, and behavioral rules -- on their AI agents, preventing costly autonomous mistakes before they happen.

---

## Target User Persona

| Dimension | Detail |
|-----------|--------|
| **Primary Role** | Small business owner / operator (cafe, retail, e-commerce, food service) |
| **Company Size** | 1-20 employees, often the owner is the main decision-maker |
| **Pain Point** | Deployed or considering AI agents for operations, but has seen or heard of agents making expensive mistakes (over-ordering, wrong pricing, bad inventory calls) |
| **Tech Background** | Non-technical. Uses off-the-shelf AI tools (ChatGPT, Claude, or industry-specific AI agents). Not a developer and does not want to write code. |
| **Decision Driver** | Losing money to AI mistakes or fear of losing control to autonomous systems. Wants the efficiency of AI agents without the risk. |
| **Budget Sensitivity** | $29-$99/month range, needs clear ROI on first month |

---

## User Pain Points

### Pain Point 1: Uncontrolled AI Spending

**Narrative:** Maria runs a small cafe in Stockholm. She deployed an AI agent to handle inventory ordering -- it was supposed to optimize stock levels and reduce waste. Within three weeks, the AI ordered 200kg of avocados, over 3x the normal weekly supply. By the time Maria noticed, $4,200 of fresh produce had spoiled. The AI had no spending limit configured because no such tool existed.

**Supporting Data:** A 2026 pilot of AI-run small businesses showed 2.7x higher supply wastage than human-managed equivalents. 73% of SMBs plan to deploy AI agents within 12 months (McKinsey, 2026), yet fewer than 12% have any spending safeguards in place.

### Pain Point 2: Behavioral Decision Drift

**Narrative:** James runs an e-commerce store with a dynamic pricing agent. Initially, the agent priced products within the 15-40% margin range he specified. Over 90 days, the agent slowly began testing lower prices, eventually offering 55% discounts on premium items. James noticed only when his monthly profit report showed a 22% drop. The agent had drifted outside his intent without any warning, and there was no system to flag the drift.

**Supporting Data:** Behavior drift is detected in 63% of long-running AI agents within 90 days of deployment. Pricing agents operating without guardrails show an average margin erosion of 18% over 6 months.

### Pain Point 3: No Decision Audit Trail

**Narrative:** When the cafe AI made its bad order, the owner had no way to reconstruct why. The agent produced no logs, no explanations, and no record of what decision thresholds triggered the order. Without an audit trail, fixing the root cause was impossible -- the owner could only shut the agent down entirely, losing all efficiency gains.

**Supporting Data:** 87% of small businesses using AI agents report having no decision audit capability. When mistakes happen, 71% of owners cannot determine what caused the error, making it impossible to prevent recurrence.

---

## Core Features

### Feature 01: Budget and Resource Caps

**Description:** Set hard financial and quantity limits that AI agents cannot exceed. Supports daily, weekly, and per-decision cap configurations. When an agent attempts to exceed a cap, BoundAI blocks the action at the API layer and sends an immediate notification. Thresholds can be set at multiple tiers (warning at 50%, block at 100%).

**In Practice Example:** A cafe owner sets a $200 daily ingredient cap. The AI tries to process a $350 produce order -- BoundAI intercepts and blocks the transaction, sends a push notification to the owner's phone, and logs the attempt. The owner reviews and chooses to approve a one-time override or reject it entirely.

**Configuration Options:**
- Daily, weekly, or monthly spending caps
- Per-transaction maximums
- Quantity limits (e.g., max 50 units per SKU)
- Tiered notifications (warn, soft-block, hard-block)
- Time-bound exceptions (e.g., allow higher limits during holiday seasons)

### Feature 02: Behavioral Guardrails

**Description:** Define acceptable ranges for AI agent decisions across multiple dimensions -- pricing, inventory, customer communications, and operational actions. Guardrails run as a continuous validation layer, checking every agent output against configured rules before it executes. When a behavior shift is detected (e.g., gradual pricing decline that stays within individual limits but trends outside acceptable bounds), the system flags it for human review.

**In Practice Example:** A retail store's pricing guardrail is set with a floor of 25% margin and a ceiling of 55% margin. When a seasonal sale requires a 40% discount on selected items, the guardrail initially blocks it. The owner adjusts the guardrail for the specific product category, the order goes through, and the guardrail automatically reverts for other categories.

**Configuration Options:**
- Numeric range limits (min/max on prices, margins, quantities)
- Percentage change limits (no more than X% change per day/week)
- Category-specific rules (different limits per product type)
- Behavioral trend detection (alerts when a metric shifts X% over N days)
- Action-type blacklisting (e.g., never auto-delete products, never auto-publish pricing)

### Feature 03: Decision Audit Log

**Description:** A searchable, filterable record of every AI decision that passes through BoundAI's guardrail layer. Each entry includes: timestamp, decision type, AI agent ID, action attempted, guardrail triggered (if any), outcome (approved / blocked / flagged), and any human override if applicable. Exportable to CSV for accounting and compliance review. Designed for non-technical users with natural language search.

**In Practice Example:** At month-end, an owner reviews the audit log and spots a pattern: the AI attempted 14 blocked supplier changes, all pushing toward a single expensive vendor. The owner adds a specific vendor approval guardrail, immediately saving $600/month in premium supplier costs.

**Log Entry Details:**
- Timestamp and timezone
- Decision category (spending, pricing, inventory, customer action)
- AI agent identifier
- Full decision payload (what was requested)
- Guardrails evaluated and their current values
- Outcome (approved, blocked by rule, blocked by cap, flagged for review)
- Human reviewer (if applicable) and their action
- Notes field for manual annotations

---

## Use Case Scenarios

### Use Case 1: Cafe Inventory Control

An AI agent manages daily ingredient ordering for a specialty coffee shop. Without guardrails, it once ordered 4x the normal produce volume. With BoundAI, the owner sets a $200 daily cap and a per-item limit of 50 units. When the agent tries to bulk-order during a sale, BoundAI caps the order at configured limits. The owner gets a notification and can optionally approve additional quantities for the sale period.

### Use Case 2: E-Commerce Dynamic Pricing

A mid-sized e-commerce store uses an AI agent to adjust prices based on demand, competitor pricing, and inventory levels. BoundAI enforces minimum margin thresholds per product category. When the agent proposes a 60% discount on premium electronics (below the 30% floor), BoundAI blocks the change and alerts the owner. During a planned clearance event, the owner adjusts the guardrail temporarily.

### Use Case 3: Service Business Scheduling

A home services company uses an AI dispatcher that assigns jobs to technicians and adjusts pricing for urgent calls. BoundAI ensures the agent never prices below a minimum service fee, never double-books a technician, and flags any scheduling requests outside normal operating hours for human review.

### Use Case 4: Customer Support Refunds

An e-commerce brand deploys an AI support agent that can issue refunds and discounts for customer complaints. BoundAI caps individual refunds at $50 and daily total refunds at $500. Any request above those thresholds is escalated to a human. The audit log tracks every refund decision for monthly reconciliation.

---

## SEO Keyword Layout

| Tag | Content |
|-----|---------|
| **Title** | BoundAI - Set Guardrails Your AI Agents Can't Cross | AI Agent Oversight |
| **Meta Description** | BoundAI gives small businesses a lightweight oversight layer for AI agents. Set spending caps, inventory limits, and decision rules so your autonomous systems never make a costly mistake. |
| **H1** | Set guardrails your AI agents can't cross |
| **H2 Tags** | The Problem, Features, How It Works, Use Cases, Get Early Access |
| **H3 Tags** | Uncontrolled Spending, Hidden Decision Drift, No Audit Trail, Budget & Resource Caps, Behavioral Guardrails, Decision Audit Log, Connect Your Agent, Set Your Boundaries, Review & Refine, Retail & Cafe Operations, E-Commerce Pricing, Supply Chain Automation, Customer Support Agents |
| **Keywords** | AI agent guardrails, AI oversight, small business AI safety, autonomous agent constraints, AI spending limits, AI decision audit, AI agent monitoring |

---

## Landing Page Section Structure

1. **Navigation** -- Fixed top bar with BoundAI logo, links to sections, Join Waitlist button
2. **Hero** -- H1 with gradient accent, sub-text explaining value prop, two CTAs (Join Waitlist + See Features), three stats with data badges
3. **Pain Section** -- Three pain cards (Uncontrolled Spending, Hidden Decision Drift, No Audit Trail) each with SVG icon, description, and data callout
4. **Features Section** -- Three feature cards (01 Budget Caps, 02 Behavioral Guardrails, 03 Decision Audit Log) with detailed explanations and "In practice" example boxes
5. **How It Works** -- Three numbered steps (Connect, Set Boundaries, Review & Refine)
6. **Use Cases** -- 2x2 grid of four use case cards (Retail, E-Commerce, Supply Chain, Customer Support)
7. **Testimonial** -- Quote block from fictional cafe owner referencing the real-world AI cafe incident
8. **CTA Section** -- Email input form with Join Waitlist button, success message on submit, localStorage persistence
9. **Footer** -- Copyright, Privacy, Terms, Contact links

---

## Technical Requirements

- **Stack:** Static HTML/CSS/JS, no build step required
- **CDN:** No external dependencies (system font stack, no Google Fonts)
- **Storage:** localStorage for waitlist email collection under key `boundai_waitlist_emails`
- **Deployment:** GitHub Pages at `/boundai/` subdirectory
- **Responsive:** Desktop-first with mobile breakpoint at 768px
- **Accessibility:** Semantic HTML, proper heading hierarchy, focusable interactive elements
