# RecallFlow - Product Requirements Document

## Product Overview

- **Product Name:** RecallFlow
- **Positioning:** AI meeting intelligence that ships work, not just notes
- **Slogan:** Your meetings finally ship work
- **Category:** AI Productivity / Meeting Intelligence
- **Target Release:** Private beta June 2026

## Target User Persona

| Role | Company Size | Pain Point | Tech Background | Decision Driver |
|------|-------------|------------|-----------------|-----------------|
| VP of Engineering | 50-500 | Sprint planning generates 15+ action items - takes 3h to enter them | High - manages Linear/Jira/Notion stack | Team velocity, reducing overhead |
| Engineering Manager | 20-200 | Loses track of decisions made in 6+ meetings/week | Medium - uses project tools daily | Reducing manual admin work |
| Product Manager | 30-300 | Client call feedback never makes it to backlog | Medium - uses roadmap tools | Closing the feedback loop |
| CTO / Tech Lead | 5-50 | Documentation debt after every meeting | High - values system integration | Knowledge preservation |
| Operations Lead | 10-100 | Cross-team decisions get lost in email threads | Low - relies on notes + memory | Accountability and tracking |

## User Pain Points

### Pain Point 1: Decisions Made in Meetings Are Lost Within 48 Hours

**Narrative:** A 60-minute sprint planning call produces 8 critical decisions about architecture, feature prioritization, and resource allocation. Two days later, team members disagree on what was decided. The engineering manager remembers one version, the product manager remembers another. Time is wasted re-litigating settled questions.

**Supporting Data:**
- 68% of meeting decisions are never documented or tracked
- Teams spend 31 hours/month in meetings
- Average team member attends 7.6 meetings/week
- 47% of time in meetings is perceived as wasted

### Pain Point 2: Manual Action Extraction Creates Administrative Overhead

**Narrative:** After every meeting, someone must review notes, identify action items, assign owners, set due dates, and enter everything into the project management system. This manual handoff creates a bottleneck -- items are forgotten, deadlines are missed, and accountability suffers.

**Supporting Data:**
- 2-3 hours per week per team member spent on meeting follow-up
- $1.2 billion estimated annual loss to unactioned meeting outcomes in the US
- 54% of action items from meetings are never completed

### Pain Point 3: Meeting Information Lives in Tool Silos

**Narrative:** Meeting notes go in Notion. Tasks go in Linear. Decisions go in Slack threads. Documentation goes in Confluence. There is no bridge connecting a conversation to its output across the tool stack. Teams lose context switching between tools, and institutional knowledge fragments.

**Supporting Data:**
- Teams use an average of 5+ tools per meeting workflow
- 71% of knowledge workers say context switching hurts productivity
- Average cost of context switching: 23 minutes to refocus

## Core Features

### Feature 1: Smart Action Extraction

**Description:** During any meeting, RecallFlow continuously processes speech to identify natural language patterns that indicate action items, ownership assignments, and deadlines. It extracts structured data -- task description, assignee, due date, priority indicators -- and creates trackable items in connected project management tools (Linear, Jira, Asana, Monday.com).

**Technical Approach:** NLP-based pattern matching on real-time transcription, entity recognition for names and dates, sentiment analysis for priority detection, bi-directional sync with PM tools via REST APIs.

**In Practice:** During sprint retro, the PM says "Sarah, can you investigate the DB migration issue by Friday?" RecallFlow captures the task, assigns it to Sarah, sets a Friday due date, adds the context link, and creates a Linear issue -- before anyone leaves the call.

### Feature 2: Auto-Documentation

**Description:** Every meeting produces structured documentation automatically. Decisions are logged with their rationale. Blockers are captured with context. Technical proposals are saved as draft documents. All content is pushed to the team's knowledge base (Notion, Confluence, GitBook) with proper formatting, tags, and cross-references.

**Technical Approach:** Summarization via LLM, structured output parsing, template-based formatting, webhook integration for docs platforms, version-controlled meeting history.

**In Practice:** After a 45-minute architecture review, RecallFlow produces a decision log with 7 entries, updates the ADR (Architecture Decision Record) in the team wiki, and appends an entry to the shared changelog documenting the rationale.

### Feature 3: Decision Intelligence

**Description:** RecallFlow cross-references meeting decisions against active project timelines, past commitments, and dependency graphs. When a decision conflicts with existing plans, it surfaces the conflict proactively with suggested alternatives. This prevents teams from making promises they cannot keep.

**Technical Approach:** Graph-based dependency mapping, timeline comparison engine, conflict detection algorithms, natural language suggestion generation.

**In Practice:** The product team agrees to move the launch date forward by two weeks. RecallFlow cross-references the decision against the engineering project plan, identifies 3 conflicting dependencies that were committed to other teams, and suggests a revised timeline that accounts for the ripple effects.

## Use Case Scenarios

### Scenario 1: Sprint Planning
A 12-person engineering team runs weekly sprint planning in Google Meet. RecallFlow extracts each user story mentioned, assigns story points based on discussion complexity, creates Jira tickets with acceptance criteria parsed from conversation, and updates the sprint board -- all within 5 minutes of the meeting ending.

### Scenario 2: Client Discovery Call
A 30-minute call with a potential client covers 12 feature requests and 3 deal-breaker requirements. RecallFlow captures every request as a structured feature record, flags the deal-breakers with priority markers, generates a meeting summary for the client, and creates a CRM update with next steps.

### Scenario 3: Design Review
A designer presents a new onboarding flow. The team provides 8 pieces of feedback. RecallFlow maps each feedback item to the relevant screen or interaction, categorizes by severity (blocker/nice-to-have/visual polish), and creates Figma-linked revision tickets.

### Scenario 4: Engineering One-on-One
A manager and direct report discuss career growth, project blockers, and personal OKRs. RecallFlow captures confidential notes accessible only to the participants, tracks progress on previously discussed goals, and generates a growth history over time.

## SEO Keyword Layout

- **Meta Title:** RecallFlow - AI Meeting Intelligence That Ships Work | Meeting AI, Action Tracking, Documentation
- **Meta Description:** RecallFlow transforms meeting conversations into project tasks, documentation updates, and decision logs. Stop manually transcribing and start shipping.
- **H1:** Your meetings finally ship work
- **H2 Tags:** The meeting productivity crisis, Your meeting intelligence engine, How it works, Built for every meeting type, Stop transcribing. Start shipping.
- **H3 Tags:** Lost decisions, Manual action tracking, Disconnected tools, Smart Action Extraction, Auto-Documentation, Decision Intelligence, Connect Your Calendar, Talk Naturally, Work Gets Done, Sprint Planning, Client Calls, Design Reviews, One-on-Ones

## Landing Page Section Structure

1. **Navigation** -- Fixed top bar with logo (RecallFlow), anchor links to Problem, Features, How It Works, Use Cases sections, and prominent Join Waitlist CTA button with brand accent.
2. **Hero** -- H1 with gradient accent text ("ship work"), subtitle paragraph, two CTAs (Join Waitlist primary, See How It Works ghost), and 3 stat cards (73%, 2.4x, 94%) with data badges.
3. **Pain Section** -- 3 pain cards (Lost decisions, Manual action tracking, Disconnected tools) each with SVG icon, descriptive paragraph, and data callout with supporting stat.
4. **Features Section** -- 3 feature cards numbered 01-03 (Smart Action Extraction, Auto-Documentation, Decision Intelligence) each with icon, description, and "In practice" example box.
5. **How It Works** -- 3 numbered steps in circles (Connect Calendar, Talk Naturally, Work Gets Done) with descriptions.
6. **Use Cases** -- 4 cards in 2x2 grid (Sprint Planning, Client Calls, Design Reviews, One-on-Ones).
7. **Testimonial** -- Single quote block from fictional VP of Engineering with attribution.
8. **CTA Section** -- Email input form + Join Waitlist button + hidden success message. localStorage-based email collection under key `recallflow_waitlist_emails`.
9. **Footer** -- Copyright line, Privacy / Terms / Contact links.
