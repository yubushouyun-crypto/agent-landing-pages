# BrandArmor - Product Requirements Document

## Product Overview

**Product Name:** BrandArmor

**Positioning:** Social Media Brand Impersonation & Scam Detection for Brand Safety Teams

**Slogan:** Stop scammers from impersonating your brand on social media

**One-line Description:** BrandArmor monitors Facebook, Instagram, LinkedIn, and Twitter for scam ads and impersonation accounts targeting your brand, providing AI-powered detection, real-time alerts, and automated takedown workflows.

## Target User Persona

| Attribute | Primary Persona | Secondary Persona |
|-----------|----------------|-------------------|
| **Role** | Brand Safety Manager | Head of Marketing / CMO |
| **Company Size** | 50-500 employees | 200-2000 employees |
| **Pain Point** | Manual scam monitoring consumes 2+ hours daily; learns about impersonation from customer complaints | Reputation damage from scam ads erodes customer trust and increases support costs |
| **Tech Background** | Comfortable with dashboards and automated workflows | Strategic decision-maker focused on ROI and risk reduction |
| **Decision Driver** | Reduce manual workload, protect customers, maintain brand trust | Reduce legal liability, protect share price, demonstrate regulatory compliance |

## User Pain Points

### Pain Point 1: Brands discover impersonation scams through angry customer calls

**Narrative:** Sarah, Brand Safety Lead at a fintech company with 120 employees, starts every morning checking customer support tickets for mentions of "scam" and "fake ad." Yesterday, 14 customers called in about a fraudulent loan-offer ad on Instagram that looked identical to her company's branding. Each call costs 8 minutes of support time. Each victim who clicked the phishing link may have exposed their financial data. Sarah had no idea the ad existed until customers told her.

**Supporting Data:** Meta sued by US Virgin Islands over ads for scams, dangers to children — "the case cites reports that a large share of Meta's revenue comes from harmful ads" (Tech-Economic Times, Dec 2025)

### Pain Point 2: Social media platforms actively resist scam detection

**Narrative:** When Sarah reports scam ads to Meta, she gets automated responses saying the content "does not violate community standards." Reuters investigation revealed Meta created an internal "playbook" to fend off pressure to crack down on scammers. The platform's ad review systems are designed for volume, not verification. Individual brands have no leverage to force takedowns.

**Supporting Data:** Reuters investigation (Dec 31, 2025): "Meta created 'playbook' to fend off pressure to crack down on scammers, documents show"

### Pain Point 3: Manual monitoring is fundamentally unscalable

**Narrative:** With 3.2 billion fake ads removed by Meta in 2025 alone, and new ones appearing faster than they can be removed, Sarah's two-person team cannot audit even 0.01% of relevant content manually. Instagram chief Adam Mosseri acknowledged that AI-generated content is so ubiquitous that it is "more practical to fingerprint real media than fake media." The scale problem is only getting worse as generative AI makes scam content creation effortless.

**Supporting Data:** Instagram chief Adam Mosseri (Engadget, Dec 2025): "AI is so ubiquitous it will be more practical to fingerprint real media than fake media"

## Core Features

### Feature 1: Cross-Platform Scam Monitoring

**Description:** Continuously scans Facebook, Instagram, LinkedIn, Twitter, and TikTok for ads, posts, and accounts impersonating the brand. Uses computer vision to detect cloned logos and visual brand assets, NLP to analyze ad copy for scam patterns, and domain matching to flag suspicious URLs.

**In-practice example:** A fintech brand discovered 34 fake loan-offer ads on Instagram within the first hour of monitoring. BrandArmor flagged all of them with screenshots, ad IDs, and direct platform URLs for immediate reporting.

### Feature 2: AI-Powered Similarity Detection

**Description:** Vision AI compares brand assets (logos, color palettes, product imagery, typography) against active social ads across all platforms. NLP models trained on known scam patterns detect urgency language, unrealistic promises, mismatched domain names, and common phishing templates.

**In-practice example:** An e-commerce brand detected a deepfake video ad featuring their CEO offering 90% off sitewide. BrandArmor identified the ad within 12 minutes of publication and generated a complete evidence package.

### Feature 3: Automated Takedown Workflow

**Description:** Generates prefilled legal takedown requests formatted for each platform's specific reporting system. Tracks report status across platforms, sends reminders for unresolved cases, and maintains a complete audit trail of every action taken for compliance and reporting.

**In-practice example:** A SaaS company reduced scam ad takedown time from 3 days (manual) to under 4 hours using BrandArmor's automated reporting pipeline across 4 social platforms.

## Use Cases

### Use Case 1: Fintech and Banking

Scammers run fake loan ads and phishing campaigns impersonating financial brands. Regulators including the FTC hold brands accountable for impersonation fraud even when they are the victim. BrandArmor provides continuous monitoring and rapid takedown to protect both customers and regulatory standing.

### Use Case 2: E-commerce and Retail

Fake giveaway ads offering unrealistic discounts on popular products drive traffic to credential harvesting pages. Each incident erodes hard-won customer trust. BrandArmor detects these ads hours after publication and automates takedown reporting.

### Use Case 3: SaaS and Technology

Scammers clone landing pages of popular SaaS tools and run ads offering fake enterprise trials. Unsuspecting IT buyers expose their organizations to supply chain attacks. BrandArmor monitors for domain clones and brand-mimicking ads.

### Use Case 4: Digital Agencies

Agencies managing multiple brand accounts need centralized monitoring across client portfolios. BrandArmor provides multi-brand dashboards, per-client reporting, and configurable alert routing to the appropriate account team.

## SEO Keyword Layout

| Tag | Content |
|-----|---------|
| **Title** | BrandArmor - Stop Social Media Brand Impersonation \| Scam Ad Detection |
| **Meta Description** | BrandArmor detects and removes scam ads and impersonation accounts targeting your brand on social media. AI-powered monitoring across Facebook, Instagram, LinkedIn, and Twitter. |
| **H1** | Stop scammers from impersonating your brand on social media |
| **H2** | The Problem / Features / How It Works / Who needs BrandArmor |
| **H3** | Cross-Platform Scam Monitoring / AI-Powered Similarity Detection / Automated Takedown Workflow / Connect your brand / AI scans the surface / Alert and act / Fintech and Banking / E-commerce and Retail / SaaS and Technology / Digital Agencies |

## Landing Page Section Structure

1. **Navigation** — Fixed top bar with blur backdrop, logo, links to sections, Join Waitlist CTA button
2. **Hero** — H1 with gradient accent on "impersonating," sub-text explaining value proposition, two CTAs (primary + ghost), 3 stats with data badges (87% learn from complaints, 3.2B fake ads removed, 64% of victims trusted the brand lookalike)
3. **Pain section** — 3 cards: (a) discover scams through support tickets, (b) platforms resist policing, (c) manual monitoring cannot keep up. Each with icon, title, body paragraph, data callout
4. **Features section** — 3 cards numbered 01-03: Cross-Platform Scam Monitoring, AI-Powered Similarity Detection, Automated Takedown Workflow. Each with inline "In practice" example box
5. **How It Works** — 3 steps with numbered circles: Connect brand, AI scans surface, Alert and act
6. **Use Cases** — 4 cards in 2x2 grid: Fintech/Banking, E-commerce/Retail, SaaS/Technology, Digital Agencies
7. **Testimonial** — Quote block with author name and role
8. **CTA section** — Email input + Join Waitlist button + success message; local storage tracking
9. **Footer** — Copyright, Privacy, Terms, Contact links

## Signal Triangulation

Three independent signal types converging on social media brand impersonation as a product opportunity:

1. **Legal/Regulatory Signal:** Meta sued by US Virgin Islands over scam ads — "a large share of Meta's revenue comes from harmful ads." Multiple jurisdictions taking legal action. (Tech-Economic Times, Dec 31 2025)

2. **Investigative Signal:** Reuters investigation reveals Meta created internal "playbook" to resist pressure to crack down on scammers. Platform incentives are misaligned with brand protection. (Reuters, Dec 31 2025)

3. **Industry Signal:** Instagram chief Adam Mosseri acknowledges AI content is outpacing detection capabilities. Official admission that platforms cannot solve this problem alone. (Engadget, Dec 31 2025)
