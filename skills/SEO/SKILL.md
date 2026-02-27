---
name: seo-strategist
description: Turn SEO chaos into executable ranked plans. Performs intent-first keyword clustering, service + location page mapping, competitor gap analysis, and internal linking strategy. Takes client URL, niche, and locations as input and outputs structured page lists, keyword mappings, and execution checklists. Use when someone needs an SEO content strategy, site structure planning, keyword research organization, competitor content gap analysis, or local SEO page architecture.
---

# AI SEO Strategist

**Purpose:** Turn chaos into ranked plans.

An intent-driven SEO planning skill that transforms messy keyword data and competitive landscapes into clear, executable content strategies with proper site architecture and internal linking logic.

## Core Capabilities

1. **Intent-First Keyword Clustering** - Group keywords by user intent, not just similarity
2. **Service + Location Page Mapping** - Architect scalable local SEO page structures  
3. **Competitor Gap Extraction** - Identify rankable opportunities competitors are missing
4. **Internal Linking Logic** - Build topical authority through strategic link architecture

## When to Use This Skill

Trigger this skill when the user:
- Needs an SEO content strategy for a website
- Wants to organize keyword research into an actionable plan
- Asks for site structure or page architecture planning
- Needs competitor content gap analysis
- Wants local SEO page mapping (service + location combinations)
- Asks how to structure internal linking
- Needs a content execution roadmap with prioritization

## Required Inputs

1. **Client URL** - The website being optimized (or competitor if benchmarking)
2. **Niche/Industry** - Business type and target market
3. **Location(s)** - Geographic areas to target (single city, multiple cities, or national)

## Optional Inputs (will gather if needed)

- Primary services offered
- Current ranking positions (if available)
- Known competitors
- Existing page structure
- Business goals and constraints

## Expected Outputs

The skill produces three core deliverables:

### 1. Page List (Structured Site Architecture)
A complete list of recommended pages organized by:
- **Core pages** (homepage, about, services overview)
- **Service pages** (main service offerings)
- **Location pages** (if local SEO)
- **Service + Location combinations** (for multi-location businesses)
- **Supporting content** (blog posts, guides, comparison pages)
- **Priority level** (P0 = critical, P1 = high value, P2 = nice to have)

### 2. Keyword → Page Map
For each page, a mapped list of:
- **Primary keyword** (main target, search volume, difficulty)
- **Secondary keywords** (2-5 supporting terms)
- **Search intent** (informational, commercial, transactional, navigational)
- **Funnel stage** (awareness, consideration, decision)
- **Content angle** (how to position the page)

### 3. Execution Checklist
A prioritized action plan with:
- **Quick wins** (low-hanging fruit to implement first)
- **Content creation sequence** (order to build pages)
- **Internal linking strategy** (hub pages, supporting content, link flow)
- **Competitor gaps to exploit** (opportunities they're missing)
- **Timeline estimates** (realistic production schedule)
- **Success metrics** (what to measure)

## Methodology

### Step 1: Discovery & Research

**Gather Core Information:**
- Confirm client URL, niche, and target locations
- Understand business model and service offerings
- Identify 3-5 main competitors
- Determine content creation capacity (how fast can they produce?)

**Conduct Initial Analysis:**
- Crawl competitor sites to understand their structure
- Use web search to identify ranking patterns in the niche
- Assess current site (if it exists) for gaps and opportunities
- Note any unique angles or underserved sub-niches

### Step 2: Keyword Research & Clustering

**Research Strategy:**
- Start with seed keywords based on services and locations
- Expand using related searches, "people also ask", and competitor keywords
- Search for "[service] + [location]", "[niche] + [need]", "[problem] + solution"
- Capture long-tail variations and question-based queries

**Intent-First Clustering:**
Unlike traditional keyword grouping (which clusters by word similarity), this skill organizes by **user intent**:

- **Informational Intent** → Blog posts, guides, "what is", "how to"
  - Example: "what is SEO audit", "how does local SEO work"
  
- **Commercial Investigation** → Comparison pages, "best" lists, reviews
  - Example: "best SEO agency in Boston", "SEO services comparison"
  
- **Transactional Intent** → Service pages, pricing, "near me"
  - Example: "hire SEO consultant", "SEO services Boston", "SEO agency near me"
  
- **Navigational Intent** → Brand pages, location pages
  - Example: "[brand name] reviews", "contact [business]"

**Clustering Rules:**
1. Group by intent first, then by topic
2. Each cluster becomes a potential page (or group of related pages)
3. High commercial intent = priority pages
4. Informational clusters support the money pages
5. Question clusters often become FAQ sections or blog posts

### Step 3: Service + Location Page Mapping

**For Local/Multi-Location Businesses:**

Create a matrix-based architecture:

**Services:**
- Primary Service 1
- Primary Service 2  
- Primary Service 3

**Locations:**
- Location 1
- Location 2
- Location 3

**Page Structure:**
```
Homepage
├── Services Hub Page
│   ├── Service 1 Page (target: "service 1 [state/region]")
│   │   ├── Service 1 + Location 1 (target: "service 1 location 1")
│   │   ├── Service 1 + Location 2
│   │   └── Service 1 + Location 3
│   ├── Service 2 Page
│   │   └── [Same pattern]
│   └── Service 3 Page
│       └── [Same pattern]
├── Locations Hub Page
│   ├── Location 1 Overview (target: "services in location 1")
│   ├── Location 2 Overview
│   └── Location 3 Overview
└── Supporting Content
    ├── Blog/Resources
    └── FAQs
```

**Scaling Logic:**
- 1-3 services × 1-5 locations = individual service+location pages
- 3+ services × 5+ locations = use hub pages + selective combinations
- Only create combinations where there's actual search demand
- Avoid thin content - each page needs unique value

**For National/E-commerce:**

Organize by product/service categories and intent:
```
Homepage
├── Category Hub Pages
│   ├── Category 1 Overview
│   │   ├── Comparison Pages (commercial intent)
│   │   ├── Product/Service Pages (transactional)
│   │   └── Supporting Content (informational)
│   └── Category 2 Overview
│       └── [Same pattern]
└── Content Hub
    ├── Guides
    ├── How-To Content
    └── Industry Resources
```

### Step 4: Competitor Gap Extraction

**Analysis Process:**

1. **Map Competitor Rankings:**
   - What pages do top competitors have?
   - What keywords are they ranking for?
   - What's their content structure?

2. **Identify Gaps:**
   - Keywords they rank for but content is weak
   - Questions they don't answer
   - Services/locations they don't cover
   - Content formats they're missing (videos, tools, calculators)

3. **Find Opportunities:**
   - Lower competition terms with decent volume
   - Questions with featured snippet potential
   - Local areas with weak competition
   - Topics where you can provide unique insight

4. **Prioritize Gaps:**
   - Highest potential ROI (good volume, weak competition)
   - Quick wins (can rank within 3-6 months)
   - Strategic gaps (aligned with business goals)

**Output Format:**
- Competitor name
- Gap identified (keyword/topic)
- Search volume
- Current top rankers
- Why it's winnable
- Recommended action

### Step 5: Internal Linking Logic

**Hub-and-Spoke Architecture:**

**Hub Pages** (pillars) = Comprehensive guides on core topics
- Link to all related supporting content
- Get links from supporting content back
- Serve as topical authority centers

**Spoke Pages** (supporting) = Specific subtopics, how-tos, examples
- Link up to relevant hub page
- Link laterally to related spoke pages
- Build depth around hub topics

**Linking Rules:**

1. **Topical Relevance First**
   - Only link when contextually relevant
   - Use descriptive anchor text
   - Link from less important to more important pages

2. **Follow User Journey**
   - Awareness content → Consideration content → Decision pages
   - Educational posts → Comparison pages → Service pages
   - Answer questions → Demonstrate value → Drive conversion

3. **Distribution Strategy**
   - Homepage links to main service/category hubs
   - Hub pages link to 5-10 related spoke pages
   - Spoke pages link to 2-3 related spokes + parent hub
   - Every page should be ≤3 clicks from homepage

4. **Priority Flow**
   - Send most link equity to money pages (services, products)
   - Use blog content to support commercial pages
   - Avoid orphan pages (pages with no internal links)

**Example Structure:**
```
Homepage (Authority: 100)
↓
Service Hub: "SEO Services" (Authority: 50)
├→ Local SEO Services (Authority: 30)
│  ├→ "Local SEO for Restaurants" (blog post)
│  ├→ "Google Business Profile Guide" (blog post)
│  └→ Links back to Service Hub
├→ Technical SEO Services (Authority: 30)
│  └→ Supporting blog content
└→ Content Marketing Services (Authority: 30)
   └→ Supporting blog content
```

### Step 6: Create Execution Plan

**Prioritization Framework:**

**P0 - Critical (Do First):**
- Core service pages with high commercial intent
- Homepage optimization
- Main location pages (if local)
- Quick wins (low competition, decent volume)

**P1 - High Value (Do Next):**
- Service + location combinations (top combinations only)
- Key comparison/commercial investigation pages
- Competitor gap opportunities with high ROI
- Essential supporting content for link flow

**P2 - Nice to Have (Do Later):**
- Long-tail variations
- Lower volume location combinations
- Deep-dive informational content
- Tertiary topics

**Realistic Timeline:**
- P0 pages: Month 1-2
- P1 pages: Month 2-4
- P2 pages: Month 4-6+
- Account for content creation speed (1-2 pages per week for most teams)

## Output Format Preferences

Create outputs in appropriate formats:

**Page List & Keyword Map** → `.xlsx` spreadsheet
- Tab 1: Complete page list with priority, URLs, status
- Tab 2: Keyword research data with clustering
- Tab 3: Keyword → Page mapping
- Tab 4: Competitor gap analysis

**Execution Checklist** → `.docx` document or `.md` file
- Prioritized task list
- Timeline and dependencies
- Internal linking map
- Success metrics to track

**Visual Architecture** → `.pptx` presentation (if complex)
- Site structure diagram
- Hub-and-spoke visualization
- Internal linking flow

## Best Practices

**Think Like a User:**
- Search intent > keyword similarity
- Answer the question, don't just rank
- One clear primary intent per page

**Be Strategic:**
- Don't create pages just because keywords exist
- Every page needs a purpose in the funnel
- Quality > quantity for local combinations

**Stay Practical:**
- Match content volume to team capacity
- Focus on achievable wins, not fantasy rankings
- Build foundation before scale

**Internal Links Matter:**
- Structure shows Google what's important
- Helps users navigate logically
- Passes authority to money pages

## Common Patterns by Business Type

**Local Service Business (plumber, lawyer, dentist):**
- Strong service pages + location variations
- FAQ-heavy for informational intent
- Heavy emphasis on "near me" and local modifiers
- Google Business Profile optimization critical

**SaaS/Software:**
- Feature pages + use case pages
- Comparison pages (vs competitors)
- Integration and tool pages
- Educational content for awareness stage

**E-commerce:**
- Category pages + product pages
- Buying guides and comparisons
- "Best [product] for [use case]" pages
- Size guides, FAQs, tutorials

**B2B Services (agency, consulting):**
- Service pages + industry pages
- Case studies and results
- Thought leadership content
- "How we do [service]" pages

## Quality Checks

Before finalizing the plan:

✅ **Every page has a clear search intent**
✅ **Primary keywords have realistic search volume**
✅ **Page hierarchy makes logical sense**
✅ **No thin content (service+location pages have unique angles)**
✅ **Internal linking supports user journey**
✅ **Quick wins are identified and prioritized**
✅ **Timeline is realistic given resources**
✅ **Metrics for success are defined**

## Success Metrics to Track

Recommend tracking:
- Keyword rankings for primary targets
- Organic traffic by page
- Click-through rate from search
- Pages indexed by Google
- Internal linking depth (avg clicks from homepage)
- Page authority/PageRank flow
- Conversion rate by page type

## Integration with Other Skills

This skill works well with:
- **xlsx skill** - For creating structured keyword maps and page lists
- **docx skill** - For execution checklists and content briefs
- **web_search** - For competitive research and keyword validation
- **pptx skill** - For visual site architecture diagrams

## Example Interaction Flow

**User:** "Help me create an SEO strategy for my plumbing company in Boston. We serve Boston, Cambridge, and Somerville."

**AI with Skill:**
1. Asks: What services do you offer? (drain cleaning, water heater, emergency plumbing, etc.)
2. Researches: Top plumbing sites in Boston area, keyword volumes, competitor structure
3. Creates keyword clusters by intent (emergency vs. planned service)
4. Maps service + location architecture (3 services × 3 locations = 9 pages + hubs)
5. Identifies gaps (competitors weak on "same-day water heater installation")
6. Builds internal linking strategy (service hubs → location pages → supporting blog)
7. Outputs:
   - Excel file with 25 recommended pages, keyword map, priorities
   - Word doc with 90-day execution checklist
   - PowerPoint with site architecture visualization

**User role:** Review the plan, confirm it makes sense for their business, greenlight execution.

## Notes

- Search volume data is directional, not absolute (use for prioritization)
- Local search often shows lower volumes but converts better
- Competitor gaps are opportunities, not guarantees
- This creates the strategy; content creation is separate
- SEO is long-term; set expectations for 3-6 month results
- Keep updating based on what actually ranks

## Anti-Patterns to Avoid

❌ Creating pages for every possible keyword variation
❌ Exact match anchor text over-optimization  
❌ Ignoring search intent in favor of volume
❌ Building too much before validating what ranks
❌ Service+location pages with identical content
❌ Internal linking without topical relevance
❌ Prioritizing vanity metrics over business impact
