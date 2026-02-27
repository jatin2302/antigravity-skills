---
name: fastestrank-intake
description: AI Intake & Sales Agent that filters money from noise. Reads BHW WTB posts and inbound leads, extracts budget/intent/urgency/red flags, classifies as Buy/Nurture/Reject, and drafts fixed-scope offers. Takes lead text, chat logs, or emails as input. Outputs 1-paragraph deal summary, Go/No-Go recommendation, and offer draft ready for human approval in ≤2 minutes. Use when processing SEO service leads, qualifying BHW opportunities, evaluating client fit, or generating service proposals.
---

# FastestRank Lead Intake Agent

Qualify inbound leads and BHW opportunities in under 2 minutes. Filter money from noise.

## When to Use This Skill
- Processing WTB (Want to Buy) posts from BlackHatWorld
- Qualifying inbound leads from your website
- Evaluating potential client fit
- Drafting fixed-scope offers

## Qualification Framework

### Signal Extraction
From any lead text, extract:
- **Budget**: Stated or implied spend capacity
- **Intent**: What do they actually want done?
- **Urgency**: Timeline and pain level (1-5)
- **Red Flags**: Unrealistic expectations, "cheap", multiple revisions, vague scope

### Classification
| Category | Criteria | Action |
|:---|:---|:---|
| 🟢 **Buy** | Clear budget, defined scope, realistic timeline | Draft offer immediately |
| 🟡 **Nurture** | Interest but unclear scope or budget | Send qualifying questions |
| 🔴 **Reject** | Red flags, no budget, unrealistic asks | Polite decline template |

### Output
1. **Deal Summary** (1 paragraph): Who, what, budget, timeline
2. **Go/No-Go Score** (0-100)
3. **Offer Draft**: Fixed-scope proposal with deliverables, timeline, price

## Usage
- "Qualify this BHW post: [paste post]"
- "Is this lead worth pursuing? [paste email]"
- "Draft a fixed-scope SEO offer for $500/mo targeting 10 keywords."
