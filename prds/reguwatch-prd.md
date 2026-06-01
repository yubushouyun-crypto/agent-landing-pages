# ReguWatch - Product Requirements Document

## Product Overview

**Product Name:** ReguWatch
**Positioning:** Automated social media regulatory compliance monitoring for platforms
**Slogan:** Stay ahead of social media regulatory compliance
**Tagline:** Automatically detect age-restricted content, scam patterns, and child safety violations before regulators come knocking.

## Target Persona

| Role | Company Size | Pain Point | Tech Background | Decision Driver |
|------|-------------|-------------|-----------------|-----------------|
| Head of Trust & Safety | 50-500 employees | Manual content review can't keep pace with new regulations | Moderate -- understands moderation pipelines but not legal details | Regulatory deadlines and lawsuit exposure |
| Compliance Officer | 100-1000 employees | Multiple jurisdictions with conflicting regulations | Low -- legal background, needs automated reporting | Audit readiness and regulator demands |
| CTO / VP Engineering | 50-500 employees | Building in-house compliance tooling is expensive and slow | High -- runs the engineering team | Cost of building vs buying compliance tech |
| Chief Legal Officer | 200-2000 employees | Increasing regulatory enforcement actions | Low -- needs clear compliance evidence | Board-level liability concerns |

## User Pain Points

### Pain 1: Regulatory deadlines are approaching fast with no automated solution

France will ban under-15s from social media starting September 2026, following Australia's world-first ban. Similar legislation is under consideration across the EU, UK, and US states. Mid-size platforms lack the engineering resources to build compliance tooling for each new regulation as it passes.

**Supporting data:** France announced the ban via Tech-Economic Times (Dec 31, 2025), setting a September 2026 deadline. Australia's ban for under-16s came into force in December 2025. The regulatory trend is accelerating -- platforms operating in multiple regions face a compliance patchwork that changes quarterly.

### Pain 2: Legal liability is becoming existential for non-compliant platforms

Meta was sued by the US Virgin Islands for failing to protect users from scam ads and dangers to children. Reuters investigations (Dec 31, 2025) revealed Meta created an internal "playbook" to fend off pressure to crack down on scammers. This demonstrates that even large platforms face escalating legal risk, and that platforms actively resist compliance -- making them targets for enforcement.

**Supporting data:** US Virgin Islands lawsuit targets Meta specifically for scam ads and child safety failures. The Reuters investigation shows the gap between what platforms should do and what they actually do, creating a liability window that regulators are now exploiting.

### Pain 3: AI-generated content has made manual moderation impossible at scale

Instagram's head product exec Adam Mosseri stated that AI-generated content is so ubiquitous that "it will be more practical to fingerprint real media than fake media" (Engadget, Dec 31, 2025). With AI content flooding feeds, traditional moderation approaches that try to detect fake content are no longer viable. Platforms need a fundamentally different approach focused on regulatory compliance signals.

**Supporting data:** Instagram's Adam Mosseri acknowledged the shift in approach -- from detecting AI content to fingerprinting authentic content. This signals a scale problem that affects every social platform globally.

## Core Features

### Feature 1: Regulation-Aware Content Scanning

**Description:** An engine that scans every post, comment, and DM against the latest regional regulatory frameworks. Covers three primary domains: age restriction rules (France under-15 ban, Australia under-16 ban), scam detection patterns (fraudulent ads, phishing, impersonation), and child safety indicators (content and interaction patterns). The regulatory rule set updates automatically as new regulations pass.

**In-practice example:** A French teenager posts content referencing alcohol. ReguWatch flags it for age-compliance review under France's new social media restrictions, along with the specific regulation cited and recommended action.

### Feature 2: Automated Regulatory Reporting

**Description:** Generate compliance reports mapped to specific regulations in each jurisdiction. Reports are ready for audit or regulator submission with one click. Includes trend analysis showing how compliance posture changes over time, with drill-down into specific flagged content and enforcement actions taken.

**In-practice example:** A European content platform receives a data request from French regulators. The compliance team generates a complete report showing all under-15 flagged content in the past 30 days, with action taken, timestamp, and regulation reference.

### Feature 3: Scam Pattern Intelligence Engine

**Description:** ML models trained on the latest scam campaign patterns detect fraudulent ads, phishing links, and impersonation attempts before they reach users. The model updates in near real-time as new scam vectors emerge, learning from cross-platform pattern data.

**In-practice example:** A new wave of AI-generated celebrity endorsement scams hits multiple platforms overnight. ReguWatch identifies the pattern within hours and begins flagging similar content across the entire content catalog.

## Use Case Scenarios

### Use Case 1: Age-Gating Compliance
A social platform operating in France and Australia needs to comply with both countries' age restriction laws. ReguWatch scans all new user registrations and content for age-related compliance issues, flagging content that should be restricted from minors. The platform's trust team receives daily compliance summaries and can generate on-demand reports for each regulator.

### Use Case 2: Scam Ad Detection at Scale
A mid-size content platform runs a programmatic ad marketplace. Fraudulent ads slip through existing filters. ReguWatch's Scam Pattern Intelligence Engine catches a coordinated scam campaign within hours of the first fake ad being submitted, blocking 95% of scam attempts before they reach users.

### Use Case 3: Child Safety Regulatory Compliance
A messaging platform with 2 million users must comply with evolving child safety regulations across the EU and US. ReguWatch flags potentially unsafe interaction patterns and escalates them to human reviewers with full context, reducing manual review workload by 70% while improving detection rates.

### Use Case 4: Cross-Jurisdiction Reporting for IPO Preparation
A social platform preparing for an IPO needs to demonstrate regulatory compliance readiness to auditors and potential investors. ReguWatch generates comprehensive compliance reports covering all jurisdictions the platform operates in, with trend data showing continuous improvement over time.

## SEO Keyword Layout

- **Meta title:** ReguWatch - Automated Social Media Compliance Monitoring | Regulatory Tech
- **Meta description:** Automate compliance with global social media regulations including age restrictions, scam detection, and child safety. ReguWatch helps platforms stay ahead of regulators with real-time content monitoring.
- **H1:** Stay Ahead of Social Media Regulatory Compliance
- **H2 (Pain):** The compliance gap is widening
- **H2 (Features):** Compliance that works while you sleep
- **H3 (Pain cards):** Regulatory deadlines are accelerating / Legal liability is becoming existential / AI-generated content overwhelms moderation
- **H3 (Feature cards):** Regulation-Aware Content Scanning / Automated Regulatory Reporting / Scam Pattern Intelligence Engine

## Landing Page Section Structure

1. **Navigation** -- fixed top bar with logo (ReguWatch), links to Pain/Features/How It Works/Use Cases, Join Waitlist CTA button
2. **Hero** -- H1 with gradient accent on "Regulatory Compliance", sub-text, 2 CTAs (Join Waitlist + See How It Works), 3 stats with badge labels (90d until France ban, 72% lack compliance, 3x lawsuits YoY)
3. **Pain Section** -- 3 cards: regulatory deadlines accelerating (France ban Sept 2026), legal liability (Meta US Virgin Islands lawsuit), AI content overwhelming moderation (Instagram chief statement)
4. **Features Section** -- 3 cards numbered 01-03: Regulation-Aware Content Scanning, Automated Regulatory Reporting, Scam Pattern Intelligence Engine, each with "In practice" box
5. **How It Works** -- 3 steps: Connect Platform, Select Jurisdictions, Monitor and Report
6. **Use Cases** -- 2x2 grid: Age-Gating Compliance, Scam Ad Detection, Child Safety Flagging, Cross-Jurisdiction Reporting
7. **Testimonial** -- Quote block from fictional "Sarah Chen, Head of Trust & Safety" citing 80% reduction in compliance review time
8. **CTA Section** -- Email input + Join Waitlist button + localStorage-backed success message + optional dashboard API POST
9. **Footer** -- Copyright 2026 + Privacy / Terms / Contact links
