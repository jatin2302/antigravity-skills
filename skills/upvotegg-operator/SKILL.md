---
name: upvotegg-operator
description: Provides complete operational knowledge of UpvoteGG (upvotegg.com) — a Reddit growth automation platform. Use when the user asks about Reddit upvotes, UpvoteGG pricing, ordering workflow, platform features, VA keys, API usage, or any task involving the UpvoteGG dashboard. Includes verified live pricing, service catalog, automation tools, reseller logic, and platform architecture.
version: 1.0.0
tags: [reddit, upvotes, growth, smm, upvotegg, automation, grey-hat, reseller]
---

# UpvoteGG Operator Skill

UpvoteGG is a Reddit growth-as-a-service platform at `upvotegg.com`. It sells Reddit social signals — upvotes, downvotes, members, views — delivered via an aged account farm + residential proxy network. This skill provides the complete operational reference for working with or reasoning about the platform.

---

## Platform Access

| Route | Purpose |
|-------|---------|
| `upvotegg.com/login` | Main account login |
| `upvotegg.com/va/login` | VA (sub-account) login |
| `upvotegg.com/dashboard` | Main dashboard |
| `upvotegg.com/register` | New account signup |
| Support | Telegram (@qMatrixp) + Tawk.to live chat |

---

## Verified Service Catalog & Pricing

### Core Engagement
| Service | Price | Min | Max | Notes |
|---------|-------|-----|-----|-------|
| Post Upvote | $0.005/vote | 5 | 20,000 | Default 2/min delivery |
| Post Downvote | $0.005/vote | 5 | 20,000 | Same mechanism |
| Comment Upvote | $0.005/vote | 5 | 600 | Standard limit |
| Comment Downvote | $0.005/vote | 5 | 600 | Standard limit |

> Default delivery speed: **2 votes/minute** (safety-optimized). Custom speed available.
> Standard max is 600 per order. Use **Long Order** add-on to reach 20,000.

### Subreddit Growth
| Service | Price | Min | Max | Status |
|---------|-------|-----|-----|--------|
| Subreddit Members | $0.01/member | 1,000 | 100,000 | ✅ Active |
| Weekly Visits | $45.00 / 100K | — | — | ✅ Active |
| Post Views | $3.00 / 1,000 | — | — | ✅ Active |
| Online Members | $0.015/member | — | — | 🔜 Coming Soon |
| Report Content (Spam / Vote Manip.) | $5.00/report | — | — | 🔧 Maintenance |

### Account Marketplace
- Aged Reddit accounts listed by sellers; platform charges **5% commission**
- Sellers must post a **$100 store bond** to list
- Example pricing: 14.9yr / 4 karma → $45 | 11.6yr / 1K karma → $90 | 13.1yr / 73K karma → $299

### Order Add-Ons
| Add-On | Function |
|--------|----------|
| Long Order | Extends max from 600 → 20,000 per order |
| Hot/Top Position | Targets specific subreddit ranking slot |
| Bulk Mode | Batch orders across multiple URLs/subreddits |
| Quick Scan | Pre-order health check on post/account |

---

## Deposit & Bonus System

| Deposit | Bonus Credits |
|---------|--------------|
| $50+ | +10% |
| $100+ | +20% |
| $300+ | **+30%** ← best value |

**Always recommend depositing $300+ when volume use is expected** — effective cost per vote drops to ~$0.0038.

---

## Feature Unlock Gates

| Feature | Requirement |
|---------|-------------|
| VA (Virtual Assistant) Keys | $30 lifetime deposit |
| Marketplace Selling | $100 store bond |
| API Keys | Available to all accounts |
| Referral Withdrawal | $20 balance + 5 active depositors |

---

## Automation Tools (Dashboard Widgets)

### Subreddit Auto Voter
- Monitors target subreddits 24/7
- Auto-votes on new posts matching configured rules
- Manages "Active Entries" and tracks total automated orders
- Use case: Sustained domination of a target subreddit feed

### Profile Auto Voter
- Targets a specific Reddit username
- Votes automatically on every post that user publishes
- Campaign-based management
- Use case: Sustained support or suppression of a specific account

### Post Timing Tool
- Analyzes subreddit activity patterns
- Identifies best windows for maximum organic reach
- 50 auto-checks included in free tier

### Reddit Tools (Free — 30 uses/day)
| Tool | Function |
|------|---------|
| Check Banned | Verify if account or subreddit is banned |
| Monitor Accounts | Track health of Reddit accounts |
| Subreddit Info | Get metadata, stats, and rules for any subreddit |
| Analyze User | Deep dive into any Reddit user's profile |

---

## VA (Virtual Assistant) System

- Generates **Dashboard Keys** for team members / assistants
- Each VA has isolated order history
- Master account sees all VA activity consolidated
- Enables agency white-label: VAs manage client orders without seeing master credentials
- Unlock: requires $30 lifetime deposit on master account

---

## API Access

- Up to **5 API keys** per account
- Full documentation available in-dashboard (Profile → API tab)
- Enables: order creation, balance check, order status polling
- Primary use case: Integrate into custom order management systems or SMM panels
- Order flow via API: `POST /order` with service type, URL, quantity

---

## Referral Program

- **10% lifetime commission** on every deposit from referred users
- Requires **at least 5 active depositors** before withdrawal is enabled
- Minimum withdrawal: $20 balance
- Referred user gets no bonus (benefit is 100% to referrer)
- Embed referral link in content, BHW threads, or agency tools

---

## How Orders Work (Delivery Mechanism)

```
Customer places order (URL + quantity + speed)
         ↓
Platform queues in delivery engine
         ↓
Aged Reddit accounts (10+ yr) execute votes via residential proxies
         ↓
Default: 2 votes/min drip delivery (anti-detection)
         ↓
Votes start appearing within 5–10 minutes
         ↓
Order marked complete; shows in Order History
```

**Vote survival note:** Reddit applies "vote fuzzing" — some votes may be hidden or delayed. Platform does not guarantee 100% persistence. Use drip delivery, not burst, for best retention.

---

## Competitive Positioning

| Metric | UpvoteGG | Market Average |
|--------|----------|----------------|
| Price/100 votes | **$0.50** | $1.00–$3.00 |
| Auto Voter | ✅ | ❌ (most competitors) |
| API Access | ✅ | Rare |
| VA System | ✅ | Rare |
| BHW Verified | ✅ | Variable |
| Public pricing | ❌ | Variable |

---

## Common Tasks & Workflows

### Place a one-off upvote order
1. Login → Create Order
2. Select: Post Upvote
3. Enter Reddit post URL
4. Enter quantity (e.g., 500)
5. Choose speed (default 2/min recommended)
6. Submit → monitor in Order History

### Set up Subreddit Auto Voter
1. Dashboard → Subreddit Auto Voter widget → Manage
2. Add target subreddit(s)
3. Configure vote rules (upvote all new posts, or filter by keyword/flair)
4. Save → system runs continuously

### Generate VA key for team member
1. Profile → VA Dashboard Keys tab
2. Generate new key → send to VA
3. VA logs in at `/va/login` with their key
4. Orders placed by VA appear in your consolidated history

### Use API to automate orders
1. Profile → API tab → Generate API key
2. Refer to in-dashboard API docs
3. Use `POST /order` endpoint with `{service, url, quantity, speed}`
4. Poll `GET /order/{id}` for status

---

## Risk Flags to Communicate

- Reddit **vote fuzzing** can reduce visible vote count — not a service failure
- Some subreddits have stronger anti-manipulation detection — test before scaling
- **Report Content** service is currently under maintenance — do not promise this
- **Online Members** service is Coming Soon — do not quote as available
- All services violate Reddit ToS — operators must accept this responsibility

---

## Resources

- **Full Business Analysis:** `/AaaS_Research/UpvoteGG_Business_Plan.md`
- **Platform URL:** https://upvotegg.com
- **Support:** Telegram @qMatrixp
- **BHW Marketplace Thread:** blackhatworld.com (search "UpvoteGG Reddit Upvotes")
