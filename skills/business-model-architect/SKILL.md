---
name: business-model-architect
description: >
  Designs, analyzes, and documents complete business model plans from scratch OR for any existing digital platform.
  Outputs a professional, investor-ready business model plan covering: canvas selection, value proposition, revenue architecture,
  unit economics, customer segments, acquisition strategy, competitive moat, MVP validation roadmap, pivot triggers, SWOT,
  risk analysis, and financial projections. Use when user says "create a business model", "build a business plan", "analyze this
  business", "how should I monetize X", "what business model fits Y", "plan for my startup", or provides a URL and asks for
  strategy, revenue model, or business breakdown.
version: 2.0.0
tags: [business-model, strategy, bmc, lean-canvas, startup, saas, marketplace, platform, d2c, revenue, unit-economics, mvp, planning]
---

# Business Model Architect

> **Upgraded from:** `business-model-analyst` v1.0.0
> **Key improvements:** Full canvas lifecycle (BMC + Lean Canvas), first-principles model selection, MVP validation framework,
> pivot detection logic, unit economics formulas, model archetype routing, financial scenario modeling, and NotebookLM research integration.

Produces expert-level business model plans — either from a URL (reverse-engineering the model) or from a business idea (first-principles design).
Modeled after Strategyzer, LEANSTACK, and SBA standards. Research-grounded via 66+ source NotebookLM deep report.

---

## Step 0 — Trigger Detection & Mode Selection

Determine which mode applies before any research:

| Trigger | Mode |
|---------|------|
| URL provided | **`REVERSE` mode** — analyze existing model |
| Business idea / concept described | **`DESIGN` mode** — build model from scratch |
| Both URL + concept | **`HYBRID` mode** — clone + differentiate |

---

## Step 1 — Intelligence Gathering

### REVERSE Mode (existing platform/site)

Run ALL in parallel:

1. **`read_url_content`** — scrape: `/`, `/pricing`, `/features`, `/about`, `/blog`, `/api`, `/affiliate`, `/partners`
   - Capture: OG metadata, navigation, pricing tiers, CTAs, testimonials
2. **`search_web`** (3 parallel searches):
   - `"[site name]" pricing features review`
   - `"[site name]" business model revenue how it works`
   - `"[site name]" site:reddit.com OR site:blackhatworld.com` (community intel)
3. **`browser_subagent`**:
   - Public site: hero, pricing page, feature grid, social proof
   - Logged in (if credentials given): full dashboard, checkout flow, account tiers, referral/affiliate program
4. **Data quality hierarchy:**
   ```
   P1: Live authenticated dashboard data
   P2: Public pricing/feature pages
   P3: Forum/community verification (BHW, Reddit)
   P4: Web research / press
   P5: Industry estimates — label [ESTIMATED]
   ```

### DESIGN Mode (new business idea)

Run ALL in parallel:

1. **`search_web`** (3 parallel):
   - `"[industry] business model examples 2025"`
   - `"[problem space] market size TAM"`
   - `"[closest competitor] revenue model how they make money"`
2. **Clarify with user** (if not already known):
   - What problem does it solve? Who has this problem?
   - What's the closest existing alternative customers use today?
   - Does the user pay or does someone else subsidize? (multi-sided vs direct)

---

## Step 2 — Model Archetype Selection

Apply this decision tree BEFORE building any document:

```
Q1: Is the user also the customer?
  YES → Direct Model (Coffee shop, SaaS solo tool, B2C)
  NO  → Multi-sided Model

Q2 (if multi-sided): Are buyers and sellers transacting?
  YES → Marketplace Model (Airbnb, Etsy, Upwork)
  NO  → Platform Model (Facebook, Google Search)

Q3: Is recurring revenue central?
  YES → Subscription/SaaS layer on top of chosen archetype
  NO  → Transactional

Q4: Is primary value in access or ownership?
  ACCESS → Subscription / rental / licensing
  OWNERSHIP → One-time sale / perpetual license
```

**Document the chosen archetype.** One canvas = one business model. Never mix archetypes in a single canvas.

---

## Step 3 — Framework Selection

| Scenario | Use |
|----------|-----|
| Established business / investor deck | **Business Model Canvas (BMC)** — 9 blocks |
| Early-stage startup / high uncertainty | **Lean Canvas** — problem/solution focused |
| New product within existing company | **Value Proposition Canvas** — VPC only |
| All three | Lean Canvas to validate → BMC to scale |

### BMC — 9 Block Analysis Template

```
CUSTOMER SEGMENTS
  - Who are the users? Who are the payers? (may differ)
  - Demographics + psychographics (3–5 personas min)
  - Segment priority: primary / secondary / tertiary

VALUE PROPOSITION
  - Core job-to-be-done
  - Pain relievers (explicit list)
  - Gain creators (explicit list)
  - Differentiators vs existing alternatives

CHANNELS
  - Awareness: [SEO / paid / word-of-mouth / PR]
  - Evaluation: [trial / demo / reviews]
  - Purchase: [web / sales-assisted / partner]
  - Post-sale: [onboarding / support / community]
  - CAC estimate per channel

CUSTOMER RELATIONSHIPS
  - Self-serve / dedicated / automated / community
  - Retention mechanics (bonuses, credits, subscriptions, gamification)
  - NPS / churn targets

REVENUE STREAMS
  - Primary stream type: [asset sale / subscription / usage / licensing / commission]
  - Pricing mechanism: [fixed / dynamic / freemium / tiered]
  - Per-stream unit economics (see Step 4)

KEY ACTIVITIES
  - Core production activity (what must never stop)
  - Delivery mechanism
  - Growth activity (acquisition engine)
  - Automation layer (zero-touch processes)

KEY RESOURCES
  - Intellectual property / data / brand
  - Technology platform / infrastructure
  - Human: key roles that cannot be outsourced
  - Financial: runway / credit lines

KEY PARTNERSHIPS
  - Supply-side (production partners, APIs, data providers)
  - Distribution-side (affiliates, resellers, integrations)
  - Strategic (co-marketing, licensing)

COST STRUCTURE
  - Fixed vs variable breakdown
  - Biggest cost drivers (top 3)
  - Cost-value alignment (is cost structure serving value prop?)
```

### Lean Canvas — Startup Adaptation

Replace these BMC blocks for early-stage ventures:

| BMC Block | Lean Canvas Replacement | Why |
|-----------|------------------------|-----|
| Key Partnerships | **Problem** (top 3 + existing alternatives) | Partners are premature; problem is riskiest unknown |
| Key Activities | **Solution** (simplest possible MVP) | Activities are derivative of solution |
| Key Resources | **Key Metrics** (1–2 macro metrics right now) | Resources can be acquired; metrics guide what to build |
| Customer Relationships | **Unfair Advantage** (what can't be copied or bought) | "Be nice" isn't defensible; moat is the risk |

---

## Step 4 — Unit Economics Module

Calculate for EVERY revenue stream:

```
REVENUE UNIT
  Revenue per unit:          [unit price × expected quantity]
  CAC (Customer Acq. Cost):  [total acquisition spend ÷ new customers]
  CLV (Customer Lifetime):   [avg monthly revenue × avg months retained]
  CLV:CAC Ratio:             [CLV ÷ CAC] → target ≥ 3:1
  Payback period:            [CAC ÷ monthly gross margin per customer]

MARGIN
  Gross margin per unit:     [(revenue - COGS) ÷ revenue × 100]%
  Contribution margin:       [revenue - variable costs]
  Break-even units:          [fixed costs ÷ contribution margin per unit]

SaaS-SPECIFIC
  MRR:                       [monthly recurring revenue]
  ARR:                       [MRR × 12]
  Churn rate:                [lost customers ÷ total customers]
  Net Revenue Retention:     [(MRR end - churn + expansion) ÷ MRR start]
  Cohort retention at 3mo:   [% of month-1 cohort still active at month 3]
```

Flag any CLV:CAC < 3:1 as a RED FLAG — model is not viable at scale without intervention.

---

## Step 5 — MVP Validation Roadmap

For DESIGN mode or any unvalidated assumption, prescribe the right MVP type:

| MVP Method | Validates | Example |
|-----------|-----------|---------|
| Landing Page / Smoke Test | Market demand | Buffer pre-launch signup |
| Concierge MVP | Willingness to pay | Zappos — manual order fulfillment |
| Wizard of Oz | Technical feasibility | Human-powered backend |
| Demo Video | User pain resonance | Dropbox explainer video |
| A/B Test | Competitive advantage | Price/feature variant tests |

**Riskiest Assumption First:** Always identify the single biggest "leap of faith" and design the cheapest test to kill or confirm it before building.

For platform/marketplace models, address the chicken-and-egg problem:
- Seed supply first (anchor suppliers before demand)
- Single-player utility (tool provides value even with 1 user)
- Concierge matching (manual before algorithmic)
- Subsidize the scarce side (Uber paid drivers first)

---

## Step 6 — Competitive Moat Analysis

Go beyond generic. For each moat layer, answer all 3 questions:

```
ASSET MOAT
  - What hard-to-copy infrastructure exists?
  - How long would a well-funded clone take to replicate it?
  - What IP / data / brand is exclusive?

NETWORK MOAT
  - Does value increase as more users join? (Metcalfe's Law)
  - What community, trust, or distribution is locked in?
  - Is retention driven by relationship or by lock-in?

SWITCHING COST MOAT
  - What integrations, data exports, or workflows tie customers in?
  - What is the true cost (time + money) to switch?
  - Is there a learning curve the customer has already paid?

PRICE MOAT
  - What is the cost floor? Can you sustain lower prices than competitors?
  - Is there a scale advantage that compounds?
  - What subsidization or cross-subsidy can you deploy?
```

---

## Step 7 — Pivot Trigger Detection

Embed pivot monitoring in the plan. Flag these 6 signals as active monitoring criteria:

1. **No Traction** — target audience doesn't care about the problem
2. **Low Value Resonance** — value prop doesn't solve the problem clearly enough
3. **Acquisition/Retention Failure** — growth targets missed despite solid product
4. **Pricing Resistance** — customers won't pay at proposed price point
5. **Cost/Technical Ceiling** — product can't be built or costs are unsustainable
6. **External Threat** — regulation, platform risk, or competitor disrupts the model

For each pivot scenario, document: trigger metric + threshold + recommended response.

---

## Step 8 — Document Output Structure

Save to: `[project_root]/_agent/research/[BusinessName]_Business_Model_Plan.md`

Use this **18-section structure** (expanded from v1.0.0's 16 sections):

```
1.  Executive Summary              — elevator pitch + key data table
2.  Problem & Market Gap           — user pain → current alternatives → your solution
3.  Model Archetype & Canvas       — chosen framework with justification
4.  Business Model Canvas / Lean Canvas  — all 9 blocks filled in detail
5.  Product & Service Catalog      — exact prices in tables; [UNVERIFIED] if not confirmed
6.  End-to-End Customer Journey    — as a code-block flow (Discover → Buy → Use → Refer)
7.  Revenue Streams & Unit Economics — per-stream margin math + CLV:CAC table
8.  MVP Validation Roadmap         — riskiest assumption + cheapest test
9.  Platform / Tech Architecture   — stack, delivery, automation layer
10. Customer Segments              — 3–5 structured personas
11. Customer Acquisition Strategy  — per-channel breakdown with CAC estimates
12. Pricing Strategy               — mechanism, rationale, and competitive context
13. Competitive Landscape          — comparison table + positioning map
14. Competitive Moat               — layered (asset / network / switching / price)
15. Pivot Triggers & Early Warning System — 6-signal monitoring table
16. Growth Roadmap                 — 4 phases minimum (Validate → Launch → Scale → Expand)
17. SWOT Analysis                  — tables, not bullets
18. Financial Model                — Conservative + Growth scenarios with cost structure table
```

---

## Writing Standards

- **Tone:** Expert analyst — authoritative, direct, data-driven. No hedging.
- **Prices:** Always exact. Never say "variable" if live data was accessible. Mark gaps as `[UNVERIFIED]` or `[LOGIN REQUIRED]`.
- **Tables:** All comparative data, pricing, segment profiles, SWOT.
- **Code blocks:** All workflows, stack diagrams, customer journeys.
- **Red Flags:** Surface explicitly with emoji 🔴 — never bury.
- **Estimates:** Always label `[ESTIMATED]` with the basis for estimation.

---

## Pre-Execution Checklist

- [ ] Mode selected: REVERSE / DESIGN / HYBRID?
- [ ] URL provided? → Scrape it
- [ ] Business idea described? → Run market research
- [ ] Credentials provided? → Log in, extract full dashboard
- [ ] Model archetype identified? (Direct / Multi-sided / Marketplace / Platform)
- [ ] Canvas type selected? (BMC vs Lean Canvas)
- [ ] Output file path confirmed?

---

## Error Handling

| Situation | Action |
|-----------|--------|
| Browser 503 / timeout | Retry once → fall back to `read_url_content` + web research |
| Login fails | Flag to user, proceed with public data + `[LOGIN REQUIRED]` markers |
| Pricing not publicly visible | Mark `[LOGIN REQUIRED]`, use forum/community intel |
| No competitor data | Infer from feature set + pricing tier positioning |
| Non-English site | Translate key sections; note language in document header |
| User idea is too vague | Ask 3 clarifying questions: problem, customer, and existing alternative |
| CLV:CAC < 3:1 | Surface as 🔴 RED FLAG with recommended intervention |

---

## Resources

- [Original skill](../business-model-analyst/SKILL.md) — v1.0.0 reference
- [Strategyzer BMC template](https://www.strategyzer.com/library/the-business-model-canvas)
- [Lean Canvas via LEANSTACK](https://leanstack.com/articles/the-lean-canvas-diagnostic-part-1-of-7---backstory)
- [SBA Business Plan Guide](https://www.sba.gov/business-guide/plan-your-business/write-your-business-plan)
- [MVP Validation Methods](https://gloriumtech.com/mvp-testing-how-to-avoid-mistakes-build-what-users-want/)
- NotebookLM Notebook: [Business Model Plan — Research & Framework](https://notebooklm.google.com/notebook/8d0ca479-72b0-487f-838c-9727c7aca573)
