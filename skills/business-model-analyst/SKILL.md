---
name: business-model-analyst
description: Conducts deep business model analysis for any website or digital platform. Produces a professional, structured business plan MD file covering services, pricing, workflow, revenue model, customer segments, acquisition strategy, competitive moat, SWOT, risk analysis, and financial projections. Use when user says "analyze this website", "business plan for X", "how does this site make money", "market research on X", or provides a URL and asks for a business breakdown.
version: 1.0.0
tags: [market-research, business-model, competitive-analysis, strategy, saas, platforms]
---

# Business Model Analyst

Produces a complete, expert-level business analysis document for any digital platform or website. Modeled after professional marketing analyst outputs. Source data comes from live browser sessions, public web research, and platform metadata.

---

## Workflow

### Phase 1 — Intelligence Gathering (Multi-Source)

Run ALL of the following in parallel:

1. **Read public pages** via `read_url_content`:
   - Homepage, /pricing, /features, /about, /blog, /api, /affiliate, /partners
   - Capture: OG description, title, navigation items, any visible pricing

2. **Web research** via `search_web` (run 3 searches in parallel):
   - `"[site name]" pricing features review`
   - `"[site name]" site:blackhatworld.com` (if grey-hat/marketing tool)
   - `"[site name]" business model how it works`

3. **Browser session** via `browser_subagent`:
   - If user is logged in: extract full dashboard — every page, every price
   - If public site: extract all navigation, pricing tiers, feature lists, CTAs, testimonials
   - Capture screenshots of: homepage hero, pricing page, dashboard (if accessible)

4. **If login credentials provided** — log in via browser and extract:
   - Full service/product list with exact prices
   - Order/checkout flow
   - Account features (tiers, API, team features)
   - Any referral/affiliate program
   - Deposit/credit/subscription system

---

### Phase 2 — Analysis Framework

Apply this framework to all gathered data:

```
BUSINESS MODEL TYPE → Identify:
  - Transactional / SaaS / Marketplace / Platform / Agency / Hybrid

REVENUE ARCHITECTURE → Map all streams:
  - Primary (core product sales)
  - Secondary (marketplace, commissions, add-ons)
  - Retention mechanics (bonuses, credits, subscriptions)
  - Growth mechanics (referral, affiliate, API resellers)

OPERATIONS STACK → Identify:
  - Core production asset (what enables delivery)
  - Delivery mechanism (how orders are fulfilled)
  - Automation layer (what runs without manual touch)
  - Tech stack (frontend, backend, integrations)

CUSTOMER SEGMENTS → Define 3–5 with:
  - Who they are
  - What they want
  - How they buy
  - Average order value + LTV estimate

COMPETITIVE MOAT → Identify defensible advantages:
  - Asset moat (hard-to-copy infrastructure)
  - Network moat (community, trust, distribution)
  - Switching cost moat (integrations, data, workflows)
  - Price moat (cost floor defense)
```

---

### Phase 3 — Document Output

Save to: `[project_root]/AaaS_Research/[SiteName]_Business_Plan.md`

Follow the **exact 16-section structure** from `examples/output_template.md`.

**Non-negotiable sections:**
1. Executive Summary (one-paragraph + key data table)
2. Problem Being Solved (user pain → platform solution)
3. Product & Service Catalog (exact prices in tables — never approximate if live data available)
4. End-to-End Workflow (customer journey as code block flow)
5. Business Model (type + logic + why it works)
6. Revenue Streams & Unit Economics (per-service margin math)
7. Platform Architecture & Technology
8. Customer Segments (structured profiles per segment)
9. Customer Acquisition Strategy (per channel)
10. Pricing Strategy (why this model, mechanics explained)
11. Competitive Landscape (comparison table + positioning map)
12. Competitive Moat (layered, not generic)
13. Growth Roadmap (phased, 4 phases minimum)
14. SWOT (tables, not bullets)
15. Risk Analysis (severity + mitigation per risk)
16. Financial Model (scenarios with tables, cost structure)

---

## Instructions

### Writing Style Rules
- Write as an **expert marketing analyst** — authoritative, direct, data-driven
- No hedging language ("probably", "might", "could be") unless genuinely uncertain
- Use tables for all comparative data, pricing, and segment profiles
- Use code blocks (```text```) for all workflows and stack diagrams
- Every price must be exact — never say "variable" if live data was accessible
- Flag incomplete data explicitly: mark as `[UNVERIFIED]` or `[ESTIMATED]`

### Data Quality Hierarchy
```
Priority 1: Live authenticated dashboard data (log in if credentials given)
Priority 2: Public page content (pricing pages, feature pages)
Priority 3: BHW/forum research (community-verified pricing)
Priority 4: Web research (general market intel)
Priority 5: Industry estimates (clearly labeled as such)
```

### Unit Economics Formula
Always calculate for each service:
```
Revenue per unit:         [price × quantity]
Estimated delivery cost:  [proxy + infrastructure + account cost]
Gross margin:             [(revenue - cost) / revenue × 100]%
```

### Competitive Moat Analysis
Go beyond generic. For each moat layer, ask:
- How long would it take a well-funded competitor to replicate this?
- What is the switching cost imposed on customers?
- What network effects compound this advantage over time?

### Financial Model Rules
- Always show 2 scenarios: Conservative + Growth
- Conservative = current trajectory, no new channels
- Growth = referral program kicks in + new segment adoption
- Always include a cost structure table separately from revenue

---

## Pre-Execution Checklist

Before starting analysis:
- [ ] Do I have the URL? → Required
- [ ] Are credentials provided? → Log in if yes
- [ ] Is this a public site with visible pricing? → Scrape directly
- [ ] Is this a locked/grey-hat platform? → Use BHW + forum research
- [ ] Output file path confirmed?

---

## Error Handling

| Situation | Action |
|-----------|--------|
| Browser subagent fails (503/timeout) | Retry once; fall back to `read_url_content` + web research |
| Login fails | Flag to user, proceed with public data only |
| Pricing not visible publicly | Mark as `[LOGIN REQUIRED]`, use BHW/forum intel |
| No competitor data found | Build comparison from feature set inference |
| Site is non-English | Translate key sections, note language in header |

---

## Resources
- [Example output](examples/output_template.md) — Reference the full 16-section structure
- [UpvoteGG reference](examples/upvotegg_reference.md) — Real completed analysis for calibration
