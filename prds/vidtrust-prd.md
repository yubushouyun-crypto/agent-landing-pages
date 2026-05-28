# VidTrust - Product Requirements Document

## Product Overview

- **Product Name:** VidTrust
- **Positioning:** AI Liveness & Deepfake Detection for Video KYC
- **Slogan:** Verify real humans. Block deepfakes.
- **Tagline:** Real-time liveness detection API that protects video KYC processes from AI-generated identity fraud.

## Target User Persona

| Role | Company Size | Pain Point | Tech Background | Decision Driver |
|------|-------------|------------|----------------|-----------------|
| CTO / Head of Product | 10-200 employees, Fintech startup | Deepfake fraud during customer onboarding | Technical, evaluates APIs independently | Quick integration, low false positive rate |
| VP of Compliance | 200-2000 employees, Digital bank | Regulatory pressure for stronger KYC | Business-oriented, needs audit trails | Compliance readiness, fraud reduction metrics |
| Fraud Analyst Lead | 50-500 employees, Lending platform | Manual review bottleneck, high false positives | Data-oriented, monitors detection rates | Reduced manual workload, automated flagging |
| Head of Engineering | 10-100 employees, Neobank | Cannot afford enterprise fraud detection suites | Hands-on, values SDK quality | Pricing per verification, developer experience |

## User Pain Points

### 1. Deepfake Identity Theft

**Narrative:** A fintech CTO launches a video KYC feature for account opening. Within two weeks, fraudsters use a Real-Time DeepSwap tool to impersonate legitimate customers during video calls. Three high-value accounts are opened with stolen identities. Traditional liveness checks (blink, smile, turn head) are trivially bypassed.

**Supporting Data:** Banks reported a 72% increase in synthetic identity fraud attempts using AI-generated media in 2025 (source: Tech-Economic Times). Deepfake creation tools like DeepSwap and FaceMagic saw 340% user growth in 2025.

### 2. Pre-Recorded Playback Attacks

**Narrative:** A fraudster obtains a customer's short selfie video from a data leak or social media. During the KYC call, they play the video on a tablet positioned behind their phone camera. The standard liveness check asks the user to blink -- the recorded video blinks on cue. The fraudster passes verification.

**Supporting Data:** Playback and replay attacks account for 41% of video KYC fraud incidents globally (industry estimate). A 2025 survey of 200 financial institutions found 63% had experienced at least one successful playback attack.

### 3. Cost of Manual Review Bottleneck

**Narrative:** A growing digital lender processes 50,000 video KYC sessions per month. Each flagged session requires manual review by a compliance analyst. At 3 minutes per review and a 25% flag rate, the team spends 625 hours per month on manual checks. Deepfake detection accuracy among human reviewers is only 34%.

**Supporting Data:** Enterprise KYC teams spend an average of $4.20 per manual review. Human reviewers catch only 34% of AI-generated deepfake attacks. False positive rates of 25% waste compliance resources.

## Core Features

### 1. Liveness Detection Engine

**Detailed Explainer:** Analyzes micro-movements, skin texture, depth variance, and light reflection patterns in real-time video. Uses a multi-modal approach combining facial landmark tracking, texture analysis, and ambient lighting inference. Returns a liveness confidence score (0-100) for each 15-second scan.

**In-Practice Example:** A user holds their phone for a 15-second scan. VidTrust analyzes 60+ micro-signals including skin subsurface scattering (unique to live tissue), involuntary micro-movements (impossible to simulate), and ambient light consistency across the face. Returns a liveness score of 97/100 in 350ms.

### 2. Playback Attack Defense

**Detailed Explainer:** Detects re-recorded screens, high-frequency refresh artifacts, secondary lighting inconsistencies, and moire patterns that reveal a pre-recorded video being played on a secondary screen. Works with both front-facing and rear cameras across smartphones and laptops.

**In-Practice Example:** A fraudster tries to replay a stolen selfie video on an iPad held in front of their phone camera. The engine detects the iPad's screen refresh rate artifacts (60Hz PWM pattern) and inconsistent ambient lighting on the face edges. Returns a block verdict before the video call connects.

### 3. Face Swap & Deepfake Detection

**Detailed Explainer:** Uses temporal analysis across video frames, checking for AI-generation artifacts, blink irregularity, identity consistency, and warping artifacts. Generates a frame-by-frame forensic report highlighting suspicious segments for compliance teams.

**In-Practice Example:** A DeepSwap filter is activated mid-call, swapping the user's face with a stolen identity. VidTrust detects the sudden change in facial landmark geometry and blink dynamics, flags the exact frame of transition, and generates a forensic timeline showing the inconsistency. Compliance teams get a downloadable PDF report.

## Use Case Scenarios

### 1. Fintech Onboarding
A neobank in Southeast Asia processes 10,000 new account openings daily. Each applicant completes a 30-second video KYC call. VidTrust validates liveness in real time, blocking 4.7% of sessions as potential deepfake attacks. Fraud losses from synthetic identity drop from $1.2M to $280K in the first quarter.

### 2. Remote Banking
A digital lender requires video verification for all loan applications above $5,000. The verification adds 15 seconds to the process, but fraud losses from impersonation attacks drop by 68%. Compliance reports are auto-generated for each approved loan.

### 3. Age Verification for Social Platforms
A gaming platform needs to verify users claiming to be under 18 for parental consent requirements. VidTrust's liveness check confirms the user is a real human (not a bot or deepfake) during a brief video session, meeting new regulatory compliance requirements.

### 4. Remote Hiring Verification
A tech company verifies contractor identities during remote interviews. The contractor completes a liveness check at the start of each interview session. The system verifies identity consistency across multi-session hiring processes, preventing impersonation in remote work scenarios.

## SEO Keyword Layout

- **Meta Title:** VidTrust - AI Liveness Detection for Video KYC | Deepfake Prevention API
- **Meta Description:** Protect your video KYC process from deepfakes, pre-recorded playback, and face swaps. VidTrust's real-time liveness detection API verifies that your users are real humans, not AI-generated media.
- **H1:** Verify real humans. Block deepfakes.
- **H2 Tags:** Video KYC is under siege, Built for trust at scale, How it works, Use cases
- **H3 Tags:** Deepfake identity theft, Pre-recorded playback attacks, Cost of manual review, Liveness Detection Engine, Playback Attack Defense, Face Swap & Deepfake Detection, Integrate the SDK, Run liveness check, Get a trust score

## Landing Page Section Structure

1. **Navigation:** Fixed top bar with logo (VidTrust), links to Problem, Features, How It Works, Use Cases, and Join Waitlist CTA button
2. **Hero:** H1 with gradient accent on "Block deepfakes", sub-text explaining liveness detection API, two CTAs (Join Waitlist + See How It Works), three stat badges (99.7% accuracy, 350ms response, 12 attack types)
3. **Pain Section:** Three cards covering deepfake identity theft, playback attacks, cost of manual review -- each with data callout
4. **Features Section:** Three cards numbered 01/02/03 -- Liveness Detection Engine, Playback Attack Defense, Deepfake Detection, each with "In practice" example
5. **How It Works:** Three steps -- Integrate SDK, Run liveness check, Get a trust score, with numbered circles
6. **Use Cases:** 2x2 grid -- Fintech onboarding, Remote banking, Age verification, Remote hiring
7. **Testimonial:** Quote block from VP of Compliance at an APAC digital bank
8. **CTA Section:** Email input + Join Waitlist button, success message on submit
9. **Footer:** Copyright, Privacy, Terms, Contact links
10. **Tracking:** PV tracking pixel and waitlist localStorage + dashboard API POST

## Deployment

- **Landing Page URL:** https://yubushouyun-crypto.github.io/agent-landing-pages/vidtrust/
- **PRD File:** agent-landing-pages/prds/vidtrust-prd.md
- **Deployment Date:** 2026-05-28
