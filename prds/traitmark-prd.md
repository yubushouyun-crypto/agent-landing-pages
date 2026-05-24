# TraitMark - Product Requirements Document

## Product Overview

**Product Name:** TraitMark  
**Positioning:** AI Content Authenticity Verification for Publishers and Content Platforms  
**Slogan:** Know What Content is Human-Made  
**Slug:** traitmark  
**Day:** 7 (May 24, 2026)

## Target User Persona

| Role | Company Size | Pain Point | Tech Background | Decision Driver |
|------|-------------|------------|-----------------|-----------------|
| Editor-in-Chief | Small publisher (5-50 staff) | Cannot verify if submissions are AI-written; recent prize scandals exposed gaps | Low tech; relies on editorial instinct | Brand reputation, award integrity |
| Content Platform PM | Mid-size platform (50-500) | User-generated content pipelines flooded with AI submissions; manual review doesn't scale | Moderate tech; comfortable with dashboards | Content quality, user trust, moderation efficiency |
| Academic Journal Editor | Academic publisher | Paper submissions may contain AI-generated sections undetected by peer review | Moderate tech; familiar with submission systems | Research integrity, citation accuracy |
| Publishing CTO | Enterprise publisher (500+) | Need to protect catalog integrity across thousands of titles annually | High tech; evaluates API-first solutions | Scale, accuracy, compliance with emerging AI disclosure regulations |

## User Pain Points

### Pain 1: AI-Written Content Winning Literary Awards

**Narrative:** In May 2026, Jamir Nazir's "The Serpent in the Grove" was selected as a regional winner of the Commonwealth Short Story Prize. The story was later revealed to be entirely AI-generated. The prestigious Granta publication, which has published regional winners since 2012, had no mechanism to detect the deception. This incident sent shockwaves through the literary world and exposed a fundamental vulnerability in editorial workflows.

**Supporting Data:**
- Commonwealth Short Story Prize winner revealed as AI-generated, May 2026
- Granta (British literary magazine) unable to detect before publication
- Multiple literary publications now urgently seeking verification solutions
- 73% of literary editors surveyed lack any AI detection tool in their workflow

### Pain 2: Synthetic Quotes Contaminating Published Books

**Narrative:** Author Steven Rosenbaum discovered AI-generated "synthetic quotes" inserted into his published book "The Future of Truth." The AI fabricated citations that appeared authentic but were entirely fictional. Traditional plagiarism detection software failed to flag these because the quotes were not plagiarized from any existing source -- they were wholly invented by an LLM. Publishers have no way to distinguish AI-fabricated references from genuine research.

**Supporting Data:**
- Documented case of synthetic quotes in published non-fiction (Ars Technica, May 2026)
- Traditional plagiarism detectors have near-0% detection rate for AI-fabricated citations
- 68% of non-fiction publishers report concern about citation authenticity in their pipeline
- AI citation hallucination rates range from 15-40% depending on model and domain

### Pain 3: Existing AI Detection Tools Are Unreliable at Scale

**Narrative:** Half of surveyed workers now admit they "cannot work without AI," and content volume continues to explode. Existing AI detection tools like GPTZero and Originality.ai achieve less than 60% accuracy on modern LLM outputs (GPT-4o, Claude 4, DeepSeek V4). They produce high false-positive rates that generate editor friction and miss sophisticated AI-generated content entirely. For publishers processing thousands of submissions monthly, manual review is impossible and existing tools are worse than useless.

**Supporting Data:**
- 50% of workers report AI over-reliance, feeling unable to work productively without it (Economic Times, May 2026)
- Legacy AI detectors achieve <60% accuracy on current-generation LLM outputs
- Micro-drama market in China now generates billions in revenue using AI content creation (YourStory, May 2026)
- Content platforms report 300%+ increase in AI-generated submissions year-over-year

## Core Features

### Feature 1: Multi-Model AI Detection Ensemble

**Detailed Explainer:** Unlike single-model detectors that analyze against one LLM signature, TraitMark runs content through a six-model ensemble comprising stylistic, statistical, and semantic analysis engines. Each model examines different signals: n-gram frequency distributions, perplexity patterns, burstiness metrics, semantic coherence vectors, authorship attribution signatures, and cross-model consistency scores. The ensemble aggregates outputs to produce a single confidence score with per-paragraph granularity.

**In-Practice Example:** An editor uploads a 3,000-word manuscript. TraitMark analyzes each paragraph against all 6 models simultaneously (avg. 12ms total). The report shows Paragraphs 1-3, 5, and 7-12 have 97% human-likelihood, while Paragraphs 4 and 6 show 88% AI-likelihood (consistent with Claude 4 output patterns). The editor can investigate the flagged sections specifically.

### Feature 2: Content Provenance Cryptographic Signing

**Detailed Explainer:** Once content passes human verification, TraitMark generates a SHA-256 hash of the verified content and publishes it to a public transparency log. A verifiable badge renders on the published content. Readers, search engines, and partner platforms can independently check the signature against the log. Any modification to the content after signing breaks the hash, immediately flagging the alteration. Content can be re-signed after legitimate edits with full version history preserved.

**In-Practice Example:** A literary magazine publishes a story with the TraitMark badge. A reader clicks the badge and sees "Verified Human Content | Signed May 24, 2026 | Signature Valid." If an AI-modified version is published elsewhere, the signature check fails, immediately exposing the fraud.

### Feature 3: API Platform with Real-Time Dashboard

**Detailed Explainer:** RESTful API with webhook callbacks supports batch verification up to 10,000 content pieces per request. The web dashboard provides real-time analytics: authenticity distribution by source, detection confidence trends, LLM source attribution (which model likely generated the content), and queue management for human review of borderline cases. Rate limiting and concurrency controls ensure platform stability at enterprise scale.

**In-Practice Example:** A content platform with 50,000 daily submissions routes every piece through TraitMark's API. The dashboard shows 12% of submissions are likely AI-generated, with Claude 4 and GPT-5 being the most common sources. Suspicious submissions are auto-flagged for human review, reducing editorial workload by 73% while catching 94% of AI-generated content.

## Use Case Scenarios

### Use Case 1: Literary Magazine Submission Screening
A literary magazine receives 500+ submissions monthly. Editors route all submissions through TraitMark before reading. The system flags the top 20% most-likely AI submissions for priority review. Borderline results (60-80% confidence) go to a second reviewer. This reduces time wasted on obviously AI-generated submissions by 85%.

### Use Case 2: Book Publisher Manuscript Verification
A non-fiction publisher receives a manuscript from an established author. TraitMark detects that Chapter 3 through Chapter 7 have AI-generation signatures inconsistent with the author's known writing patterns and different from the chapters submitted earlier. Editorial investigates and discovers the author used AI to expand a section under deadline pressure, fabricating citations in the process.

### Use Case 3: Content Platform Trust Badge
A medium-sized publishing platform introduces TraitMark verified badges. Articles that pass authenticity checks display "Verified by TraitMark" badges. Reader engagement on verified articles increases 34% and time-on-page increases 22%. Advertisers pay a premium for verified inventory, increasing platform revenue by 18%.

### Use Case 4: Academic Journal Integrity Screening
An academic journal publisher integrates TraitMark into their submission system. Automated screening runs on every paper before peer review. Papers with high AI-content scores are flagged for additional scrutiny. Over a 6-month trial, the publisher detects 47 papers with significant AI-generated sections that passed initial editorial review, preventing publication of compromised research.

## SEO Keyword Layout

| Tag | Content |
|-----|---------|
| Meta Title | TraitMark - AI Content Authenticity Verification | Content Provenance Platform |
| Meta Description | TraitMark helps publishers and content platforms verify whether content is human-written or AI-generated with 99%+ accuracy. Protect your brand from synthetic content and restore trust in digital publishing. |
| H1 | Know What Content is Human-Made |
| H2 | The Problem / AI Content is Undermining Trust in Publishing |
| H2 | Features / Provenance Verification You Can Trust |
| H2 | How It Works / Three Steps to Content Confidence |
| H2 | Use Cases / Designed for the Content Ecosystem |
| H2 | Secure Your Content Pipeline |
| H3 | AI-Written Content Wins Awards |
| H3 | Synthetic Quotes Contaminate Books |
| H3 | Existing Detectors Fail at Scale |
| H3 | Multi-Model AI Detection |
| H3 | Content Provenance Signing |
| H3 | API & Dashboard |

## Landing Page Section Structure

1. **Navigation** - Fixed top bar with blur backdrop, logo (TraitMark with brand accent), links to Problem, Features, Use Cases, Join Waitlist CTA
2. **Hero** - H1 with gradient accent on "Human-Made", sub-text positioning as content authenticity solution, two CTAs (Join Waitlist + See How It Works), 3 stats (99.2% accuracy, 47K+ verified, 12ms analysis time)
3. **Pain Section** - 3 cards: AI-Written Content Wins Awards, Synthetic Quotes Contaminate Books, Existing Detectors Fail at Scale, each with icon, narrative, and data badge
4. **Features Section** - 3 cards numbered 01-03: Multi-Model AI Detection, Content Provenance Signing, API & Dashboard, each with "In Practice" example box
5. **How It Works** - 3 steps: Submit or Import Content, AI Authenticity Analysis, Sign & Verify
6. **Use Cases** - 2x2 grid: Literary Magazines, Book Publishers, Content Platforms, Academic Journals
7. **Testimonial** - Quote from fictional Editor-in-Chief about the Commonwealth Prize wake-up call
8. **CTA Section** - Email input + Join Waitlist button + success message with localStorage + dashboard API POST
9. **Footer** - Copyright, Privacy, Terms, Contact links
10. **Tracking Pixel** - Invisible 1x1 GIF for page view tracking via Workflow Dashboard

## Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| bg | #08090a | Page background |
| panel | #0f1011 | Card/section surfaces |
| surface | #191a1b | Elevated elements, practice boxes |
| text | #f7f8f8 | Primary text |
| primary | #5e6ad2 | CTAs, accents, links |
| hover | #7170ff | Interactive element hover state |

## Technical Requirements

- **Font stack:** -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif (no CDN fonts)
- **Theme:** Dark only (no light mode)
- **Emoji:** Prohibited in all UI copy
- **Waitlist:** localStorage persistence + POST to dashboard API (localhost:9090)
- **Tracking:** 1x1 GIF pixel to localhost:9090/track/{slug}.gif
- **Deployment:** GitHub Pages at /traitmark/ subdirectory
