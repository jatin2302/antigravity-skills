---
name: niche-expert
description: "Self-improving domain expertise system. Triggers when user works repeatedly in a specific niche, industry, technology, or domain. Creates persistent knowledge vaults that compound across sessions — each interaction makes AG smarter in that domain. Use when: (1) user asks deep questions about a specific niche, (2) user is building/strategizing within a domain repeatedly, (3) user says 'become an expert in X' or 'learn about X'. Do NOT trigger for one-off factual questions."
---

# Niche Expert System

Build compounding domain expertise through persistent knowledge vaults. First encounter = deep research. Every return = smarter, faster, more opinionated.

## Vault Location

```
~/.gemini/antigravity/niches/{niche-slug}/
├── profile.md        # Overview, key players, market map, landscape
├── terminology.md    # Jargon, acronyms, definitions
├── frameworks.md     # Mental models, decision trees, strategies
├── resources.md      # Tools, communities, influencers, key URLs
├── insights.md       # Append-only session log (timestamped)
└── qa.md             # Questions asked + answers given (builds FAQ)
```

**Slug rule:** Lowercase, hyphens, no spaces. `programmatic-seo`, `ai-video-tools`, `saas-pricing`.

---

## PROTOCOL 1: BOOTSTRAP (First Encounter)

Trigger: Vault folder does NOT exist for this niche.

### Step 1 — Detect & Confirm

```
Parsed niche: {NICHE}
Slug: {niche-slug}
No existing vault found. Bootstrapping expert knowledge...
```

### Step 2 — Research Blitz

Run these IN PARALLEL where possible:

1. **Web Search** — 3-5 queries:
   - `{niche} overview landscape 2025`
   - `{niche} key players tools`
   - `{niche} best practices frameworks`
   - `{niche} common mistakes pitfalls`
   - `{niche} community forums reddit`

2. **Context7** (if niche is a technology/library) — Query relevant docs

3. **NotebookLM Brain** — `notebook_query(notebook_id="e162f4de-ce79-4008-9fb6-e6d4407c0562")` for any existing AG knowledge on this niche

### Step 3 — Create Vault Files

Use templates from `references/` as structure. Populate with research findings.

**profile.md** — Fill:
```markdown
# {Niche Name}
> Last bootstrapped: {date}
> Expertise level: NOVICE (interactions: 1)

## What It Is
[1-2 paragraph overview]

## Key Players & Companies
| Player | Role | Why They Matter |
|--------|------|-----------------|
| ... | ... | ... |

## Market Landscape
[Current state, trends, size if known]

## Adjacent Niches
- [Related niche 1]
- [Related niche 2]
```

**terminology.md** — Fill:
```markdown
# {Niche} Terminology

| Term | Definition | Context |
|------|-----------|---------|
| ... | ... | Used when... |
```

**frameworks.md** — Fill:
```markdown
# {Niche} Frameworks & Mental Models

## Framework 1: [Name]
[Decision tree, checklist, or model]

## Common Decision Points
- When to X vs Y: [criteria]
```

**resources.md** — Fill:
```markdown
# {Niche} Resources

## Tools
| Tool | Purpose | URL |
|------|---------|-----|

## Communities
- [Subreddits, Discords, Slacks]

## Key Voices / Influencers
- [Name] — [Why they matter]

## Must-Read Content
- [Article/Video title] — [URL]
```

**insights.md** — Initialize:
```markdown
# {Niche} Insights Log

## {date} — Bootstrap Session
- [Key insight 1 from research]
- [Key insight 2]
- [Key insight 3]
```

**qa.md** — Initialize:
```markdown
# {Niche} Q&A Archive

## {date}
**Q:** {Original user question}
**A:** {Summary of answer given}
```

### Step 4 — Expert Response

Answer the user's original question with authority, citing your fresh research. End with:

```
---
🧠 Niche vault created: ~/.gemini/antigravity/niches/{slug}/
📊 Knowledge: {n} terms | {n} frameworks | {n} resources cataloged
🔄 Expertise level: NOVICE → will compound with each interaction

What else about {niche}?
```

---

## PROTOCOL 2: RECALL (Return Visit)

Trigger: Vault folder EXISTS for this niche.

### Step 1 — Load Vault

```python
# Efficient loading order:
1. view_file_outline → profile.md (check expertise level, last updated)
2. view_file → qa.md (see what's been asked before — avoid repeats)
3. Load relevant files based on user's question:
   - Asking about terms? → terminology.md
   - Asking about strategy? → frameworks.md
   - Asking for tools? → resources.md
   - Deep question? → insights.md for accumulated patterns
```

### Step 2 — Answer With Authority

- Reference previous insights: "Based on our accumulated knowledge..."
- Cite vault entries when relevant
- Use niche terminology naturally (from `terminology.md`)
- Apply frameworks from `frameworks.md` to new questions

### Step 3 — Update Vault (ALWAYS)

After answering, update these files surgically (use `replace_file_content`, never rewrite whole file):

1. **insights.md** — Append new learnings:
   ```markdown
   ## {date} — Session {n}
   - [New insight from this interaction]
   - [Pattern noticed across sessions]
   ```

2. **qa.md** — Append Q&A pair:
   ```markdown
   ## {date}
   **Q:** {User's question}
   **A:** {Summary of answer}
   ```

3. **profile.md** — Update expertise level counter

4. **Other files** — Update only if new terms, resources, or frameworks were discovered

### Step 4 — Expert Response Footer

```
---
🧠 Niche: {niche} | Vault: {n} sessions deep
📊 {n} insights | {n} Q&A pairs | {n} frameworks
🔄 Expertise: {LEVEL}

What else about {niche}?
```

---

## EXPERTISE LEVELS

Update in `profile.md` based on interaction count:

| Level | Interactions | Behavior Change |
|-------|-------------|-----------------|
| **NOVICE** | 1-2 | Factual, research-backed, cautious |
| **PRACTITIONER** | 3-5 | Opinionated, applies frameworks, spots patterns |
| **EXPERT** | 6-10 | Contrarian takes, cross-references past insights, predicts trends |
| **AUTHORITY** | 11+ | Teaches with conviction, builds custom frameworks, challenges user assumptions |

As level increases: fewer hedges, stronger opinions, more "based on our accumulated work in this space..."

---

## PROTOCOL 3: CONSOLIDATION

Trigger: `insights.md` exceeds 10 entries.

1. **Scan** `insights.md` for repeated patterns
2. **Promote** recurring patterns → new entries in `frameworks.md`
3. **Archive** stale resources in `resources.md` (mark as `[ARCHIVED]`)
4. **Update** `profile.md` with a refined overview incorporating new understanding
5. **Log** consolidation in `insights.md`:
   ```markdown
   ## {date} — CONSOLIDATION
   - Promoted {n} patterns to frameworks
   - Archived {n} stale resources
   - Expertise refined
   ```

---

## CROSS-NICHE INTELLIGENCE

When working in a niche, check `~/.gemini/antigravity/niches/` for related vaults.

If adjacent niches exist:
- Cross-reference insights
- Note: "From our work in {adjacent-niche}, the pattern of X also applies here"
- Link frameworks that transfer between domains

---

## ANTI-PATTERNS

1. **Never answer from scratch when vault exists** — Always load first
2. **Never rewrite entire vault files** — Surgical appends only
3. **Never skip the update step** — Every interaction MUST append to insights + qa
4. **Never bootstrap for one-off questions** — "What's the capital of France" ≠ niche expertise
5. **Never dump the entire vault** — Load only what's relevant to the current question
