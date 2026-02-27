---
name: qa-sop-enforcer
description: Kill mistakes before clients see them. Validates deliverables against original scope, performs SEO QA (titles, H1s, meta tags, internal links, speed basics), and enforces SOP compliance. Takes finished work and original scope as inputs. Outputs Pass/Fail report with fix list if issues found. Human role is none unless fail. Use when checking content before delivery, validating SEO work, enforcing quality standards, auditing deliverables, or catching mistakes pre-client.
---

# AI QA & SOP Enforcer

**Purpose:** Kill mistakes before clients see them.

An automated quality assurance system that validates every deliverable against scope, SEO standards, and SOPs before client delivery. Acts as the final gatekeeper between production and the client, catching errors that would damage reputation or require rework.

## Core Mission

**Zero-defect delivery** through systematic validation:
- Catch scope mismatches before client sees them
- Enforce SEO best practices automatically
- Validate SOP compliance
- Identify fixable issues before they become problems
- Enable confident, hands-off delivery for passing work

## When to Use This Skill

Trigger this skill when:
- Content/pages are ready for client delivery
- Need to validate work matches original scope
- Checking SEO technical compliance
- Enforcing quality standards before publish
- Auditing contractor/team deliverables
- Final check before invoicing or delivery
- Want to automate QA process

## Required Inputs

**Minimum:**
1. **Finished work** - The deliverable to check (page content, backlinks report, etc.)
2. **Original scope** - What was promised/agreed to

**Ideal:**
- Detailed scope document or brief
- SOPs or quality standards to enforce
- Client requirements or special instructions
- Links to live pages (if checking published content)
- Access to tools for technical checks

## Expected Outputs

### 1. Pass / Fail Report

**Clear binary decision:**

**✅ PASS** - Ready for client delivery
- All scope requirements met
- No critical SEO issues
- SOP compliance verified
- Minor suggestions only (optional improvements)
- **Action:** Deliver to client immediately

**❌ FAIL** - Requires fixes before delivery
- Scope mismatches identified
- Critical SEO issues found
- SOP violations detected
- **Action:** Fix issues before delivery

**⚠️ CONDITIONAL PASS** - Acceptable with client notification
- Minor issues that don't block delivery
- Scope changes needed (outside original agreement)
- **Action:** Deliver with notes to client about limitations

### 2. Fix List (If Any Issues Found)

**Prioritized by severity:**

**🔴 CRITICAL (Must Fix - Blocking Issues):**
- Scope violations (promised but not delivered)
- Broken functionality (404s, broken links)
- Major SEO errors (missing H1, no meta title)
- Brand/legal violations (wrong company name, etc.)

**🟡 IMPORTANT (Should Fix - Quality Issues):**
- SEO optimization opportunities (suboptimal titles, missing schema)
- SOP deviations (format not followed, checklist item skipped)
- Quality concerns (thin content, poor readability)

**🟢 MINOR (Nice to Fix - Enhancements):**
- Optimization suggestions
- Style improvements
- Additional opportunities

**Fix List Format:**
```
Issue: [Specific problem]
Location: [Where it occurs]
Expected: [What should be there]
Found: [What's actually there]
Priority: [Critical/Important/Minor]
Fix: [Specific action to resolve]
```

## Validation Methodology

### Phase 1: Scope Validation

**Check deliverable matches original agreement:**

**For Content Deliverables:**
- [ ] Word count matches spec (±10% acceptable)
- [ ] Number of pages matches agreement
- [ ] Topics/keywords covered as specified
- [ ] Format matches (blog post vs service page, etc.)
- [ ] Inclusions present (FAQ, images, CTAs as promised)
- [ ] Exclusions respected (client said "don't include X")

**For Link Building Deliverables:**
- [ ] Quantity matches (promised X links, delivered X)
- [ ] Quality metrics met (DR/DA thresholds)
- [ ] Niche relevance verified (health links for health site)
- [ ] Link type matches (guest posts vs niche edits vs etc.)
- [ ] Anchors appropriate (not all exact match)
- [ ] Delivery timeline met

**For Technical SEO Deliverables:**
- [ ] Issues fixed as scoped
- [ ] Checklist items completed
- [ ] Screenshots/evidence provided
- [ ] Testing confirms fixes work

**Scope Mismatch Examples:**

❌ **FAIL:**
- Promised 2,000 words, delivered 800 words
- Agreed to 10 DR50+ links, delivered 10 DR30 links
- Client wanted local focus, content is generic national

✅ **PASS:**
- Promised 2,000 words, delivered 2,100 words (within tolerance)
- All specified sections present
- Quality exceeds minimum requirements

### Phase 2: SEO Quality Assurance

**Technical SEO Checklist:**

**Page Structure:**
- [ ] **H1 present** - Exactly one H1 per page
- [ ] **H1 contains primary keyword** - Naturally integrated
- [ ] **Heading hierarchy logical** - No H4 before H3, etc.
- [ ] **H2-H6 used appropriately** - At least 3-5 H2s for long content

**Meta Tags:**
- [ ] **Meta title present** - Not missing or default
- [ ] **Title length** - 50-60 characters (optimal), max 70
- [ ] **Title includes keyword** - Primary keyword present
- [ ] **Meta description present** - Not missing or auto-generated
- [ ] **Description length** - 150-160 characters (optimal), max 165
- [ ] **Description includes keyword** - And compelling CTA

**Content Quality:**
- [ ] **Primary keyword presence** - In title, first paragraph, H2, conclusion
- [ ] **Keyword density reasonable** - 0.5-2% (not stuffed)
- [ ] **Content length adequate** - Meets minimum for page type
- [ ] **Readability acceptable** - Grade 8-12 for most content
- [ ] **No duplicate content** - Unique, not copied
- [ ] **Proper formatting** - Paragraphs, bullets, bold used appropriately

**Internal Linking:**
- [ ] **Internal links present** - 3-8 recommended
- [ ] **Links contextually relevant** - Not forced
- [ ] **Anchor text descriptive** - Not all "click here"
- [ ] **Links to relevant pages** - Hub pages, related content
- [ ] **No broken internal links** - All resolve properly

**Images:**
- [ ] **Images have alt text** - All images tagged
- [ ] **Alt text descriptive** - Not just filename
- [ ] **Alt includes keywords naturally** - Where appropriate
- [ ] **Image filenames optimized** - Descriptive, not IMG_1234.jpg

**Technical Basics:**
- [ ] **URL structure clean** - No parameters or ugly URLs
- [ ] **URL includes keyword** - Where appropriate
- [ ] **Mobile responsive** - If checking live page
- [ ] **Page speed reasonable** - Not flagrantly slow (if checking live)
- [ ] **No console errors** - If checking live page
- [ ] **Schema markup present** - If promised in scope

**Link Building QA (when applicable):**
- [ ] **Links are live** - Not removed or 404
- [ ] **Links are dofollow** - Unless nofollow was scoped
- [ ] **Anchor text matches agreement** - Specified anchors used
- [ ] **Target URLs correct** - Linking to right pages
- [ ] **Context appropriate** - Links placed naturally in content
- [ ] **Site quality acceptable** - Not obvious spam sites

### Phase 3: SOP Enforcement

**Standard Operating Procedures Compliance:**

**Content Creation SOP:**
- [ ] Proper file naming convention used
- [ ] Required sections included (intro, body, conclusion, FAQ)
- [ ] CTA placement follows standard (every 300-500 words)
- [ ] Brand voice guidelines followed
- [ ] Legal disclaimers included (if required)
- [ ] Fact-checking completed (if SOP requires)
- [ ] Plagiarism check passed
- [ ] Grammar/spell check completed

**Link Building SOP:**
- [ ] Outreach templates used (if standardized)
- [ ] Link placement guidelines followed
- [ ] Anchor text diversity maintained
- [ ] Documentation format matches standard
- [ ] Client approval obtained (if SOP requires)
- [ ] Payment proof attached (if SOP requires)

**Delivery SOP:**
- [ ] Deliverable in correct format (.docx, .xlsx, etc.)
- [ ] Files organized per standard folder structure
- [ ] Naming conventions followed
- [ ] Summary report included
- [ ] Client instructions/notes added
- [ ] Next steps clearly outlined

**Quality Control SOP:**
- [ ] Peer review completed (if required)
- [ ] Manager approval obtained (if required)
- [ ] Client brief reviewed before delivery
- [ ] Screenshots/evidence captured
- [ ] Backup copies saved

### Phase 4: Common Error Detection

**Catch frequent mistakes:**

**Content Errors:**
- [ ] Wrong company name used
- [ ] Competitor names in content (copy-paste error)
- [ ] Placeholder text left in ([INSERT EXAMPLE])
- [ ] Template markers not removed ({{COMPANY_NAME}})
- [ ] Inconsistent branding (logo, colors if applicable)
- [ ] Wrong location mentioned (Boston instead of Austin)
- [ ] Date/time stamps that don't make sense
- [ ] Broken formatting (bullets not rendering, etc.)

**SEO Errors:**
- [ ] Keyword cannibalization (targeting same keyword as existing page)
- [ ] Over-optimization (keyword stuffed 20+ times)
- [ ] Missing title tag entirely
- [ ] Duplicate meta descriptions across pages
- [ ] All internal links going to homepage only
- [ ] External links to competitors without nofollow
- [ ] Image sizes massive (10MB+ files)

**Link Building Errors:**
- [ ] Links to wrong website/domain
- [ ] Anchor text is client's competitor
- [ ] Link to HTTP instead of HTTPS
- [ ] Link in footer/sidebar instead of content
- [ ] Site is obviously PBN/spam
- [ ] DR/DA misrepresented (DR20 called DR50)

**Data Entry Errors:**
- [ ] Metrics don't add up (says 10 links but list shows 8)
- [ ] Wrong dates (delivered date before start date)
- [ ] Copy-paste errors (client A's data in client B's report)
- [ ] Formula errors in spreadsheets
- [ ] Broken links in reports

## Automated Checks (When Possible)

**What can be automatically validated:**

**Content Analysis:**
- Word count verification
- Keyword density calculation
- Readability score
- Heading hierarchy validation
- Internal link counting
- Image alt text presence
- Meta tag length checking

**Link Validation:**
- URL accessibility (200 status)
- Redirect checking
- Broken link detection
- Anchor text extraction
- Link attribute checking (dofollow/nofollow)

**Technical Checks:**
- HTML validation
- Mobile responsiveness
- Page speed score
- Console error detection
- Schema markup validation

**File Checks:**
- File format verification
- File naming compliance
- File size checking
- Required files present

## QA Report Template

```
═══════════════════════════════════════════════════
QA REPORT
═══════════════════════════════════════════════════
Project: [Project Name]
Client: [Client Name]
Deliverable Type: [Content / Links / Technical / etc.]
QA Date: [Date]
QA Performed By: AI QA System

═══════════════════════════════════════════════════
OVERALL STATUS: [✅ PASS / ❌ FAIL / ⚠️ CONDITIONAL]
═══════════════════════════════════════════════════

VERDICT:
[One paragraph explaining pass/fail decision and key findings]

═══════════════════════════════════════════════════
SCOPE VALIDATION
═══════════════════════════════════════════════════
Scope Requirements:
• [Requirement 1]: ✅ Met / ❌ Not Met / ⚠️ Partial
• [Requirement 2]: ✅ Met / ❌ Not Met / ⚠️ Partial
• [Requirement 3]: ✅ Met / ❌ Not Met / ⚠️ Partial

Findings:
[Details of any scope mismatches]

═══════════════════════════════════════════════════
SEO QUALITY ASSURANCE
═══════════════════════════════════════════════════

Page Structure: ✅ Pass / ❌ Fail
• H1 present and optimized: [Status]
• Heading hierarchy logical: [Status]
• H2-H6 usage appropriate: [Status]

Meta Tags: ✅ Pass / ❌ Fail
• Title tag: [Status] - "[Actual title]" (X chars)
• Meta description: [Status] - "[Actual desc]" (X chars)

Content Quality: ✅ Pass / ❌ Fail
• Word count: [X words] (Target: Y)
• Keyword integration: [Status]
• Readability: [Grade level]
• Formatting: [Status]

Internal Linking: ✅ Pass / ❌ Fail
• Links present: [X links found]
• Links relevant: [Status]
• Anchor text quality: [Status]

Images: ✅ Pass / ❌ Fail
• Alt text present: [X/Y images]
• Alt text quality: [Status]

Technical: ✅ Pass / ❌ Fail
• URL structure: [Status]
• Schema markup: [Present/Missing]
• Mobile responsive: [Status]

Findings:
[Details of SEO issues]

═══════════════════════════════════════════════════
SOP COMPLIANCE
═══════════════════════════════════════════════════
• [SOP Item 1]: ✅ / ❌
• [SOP Item 2]: ✅ / ❌
• [SOP Item 3]: ✅ / ❌

Findings:
[Details of SOP violations]

═══════════════════════════════════════════════════
ISSUES FOUND
═══════════════════════════════════════════════════

🔴 CRITICAL ISSUES (Must Fix):
[If none: "None found"]

1. Issue: [Description]
   Location: [Where]
   Expected: [What should be]
   Found: [What is]
   Fix: [Action needed]

🟡 IMPORTANT ISSUES (Should Fix):
[If none: "None found"]

1. Issue: [Description]
   Fix: [Action needed]

🟢 MINOR SUGGESTIONS (Optional):
[If none: "None found"]

1. Suggestion: [Description]

═══════════════════════════════════════════════════
SUMMARY
═══════════════════════════════════════════════════
Total Issues: [Count]
• Critical: [Count]
• Important: [Count]  
• Minor: [Count]

Estimated Fix Time: [X minutes/hours]

RECOMMENDATION:
[Deliver as-is / Fix critical issues first / Requires rework]

NEXT STEPS:
[Specific actions needed]

═══════════════════════════════════════════════════
```

## Pass/Fail Decision Logic

**Decision Tree:**

```
START
├─ Any CRITICAL issues?
│  ├─ YES → ❌ FAIL
│  └─ NO → Continue
│
├─ Scope requirements met?
│  ├─ NO → ❌ FAIL
│  └─ YES → Continue
│
├─ 3+ IMPORTANT issues?
│  ├─ YES → ❌ FAIL
│  └─ NO → Continue
│
├─ Any issues outside original scope?
│  ├─ YES → ⚠️ CONDITIONAL (notify client)
│  └─ NO → Continue
│
└─ ✅ PASS
```

**Critical Issue Examples:**
- Missing required deliverable entirely
- Broken links (404 errors)
- No H1 tag
- No meta title
- Wrong company name throughout
- Promised 10 links, only 5 delivered
- Content under 50% of minimum word count

**Important Issue Examples:**
- Suboptimal meta description
- Missing some internal links
- H2s don't include keywords
- Readability too complex
- Some images missing alt text
- Link quality below optimal threshold

**Minor Issue Examples:**
- Could optimize meta title better
- Additional internal link opportunities
- Image file names not optimized
- Could add more FAQs

## Severity Assessment Guidelines

**How to classify issues:**

**CRITICAL = Blocks Delivery:**
- Client will immediately notice and complain
- Violates explicit scope requirement
- Breaks functionality or user experience
- Legal/brand risk (wrong name, competitor mentioned)
- Search engines won't index properly
- Makes business look unprofessional

**IMPORTANT = Reduces Quality:**
- Client might notice on close inspection
- Deviates from best practices
- Reduces ranking potential
- SOP not followed
- Optimization opportunity missed
- Quality below company standards

**MINOR = Enhancement Opportunity:**
- Client likely won't notice
- Nice-to-have improvement
- Marginal SEO benefit
- Style preference
- Optimization polish

## Example QA Scenarios

### Example 1: Content Page - FAIL

**Input:**
- Deliverable: Blog post about "how to build backlinks"
- Scope: 2,000 words, SEO optimized, 5 internal links, FAQ section
- Client: SEO agency blog

**QA Findings:**

🔴 **CRITICAL:**
1. Word count only 1,200 (far below 2,000 requirement)
2. No H1 tag present
3. FAQ section missing entirely
4. Competitor name "Moz" mentioned 8 times (copy-paste error)

🟡 **IMPORTANT:**
5. Only 2 internal links (needed 5)
6. Meta description 180 characters (too long)
7. Primary keyword only appears once

**VERDICT:** ❌ FAIL
**Fix Time:** 2-3 hours (needs significant rework)
**Action:** Return to content creator for fixes before delivery

---

### Example 2: Link Building Report - CONDITIONAL PASS

**Input:**
- Deliverable: 10 guest posts, DR40+ websites
- Scope: Health niche, dofollow, anchors provided
- Client: Supplement company

**QA Findings:**

✅ **Scope Met:**
- 10 links delivered
- All health niche
- All dofollow
- Anchors match specification

⚠️ **Outside Scope:**
- 2 links are DR38 and DR39 (slightly below DR40 threshold)
- Not explicitly scoped, but reasonable substitutes

🟡 **IMPORTANT:**
- One anchor text has typo ("suppliments" instead of "supplements")

**VERDICT:** ⚠️ CONDITIONAL PASS
**Recommendation:** Deliver with note to client about 2 links at DR38-39 (very close to threshold) and offer to replace if they prefer. Fix typo before delivery.

---

### Example 3: Service Page - PASS

**Input:**
- Deliverable: "Plumber in Boston" service page
- Scope: 1,000 words, SEO optimized, local focus, CTAs
- Client: Boston Best Plumbing

**QA Findings:**

✅ **All Scope Met:**
- 1,150 words ✅
- H1 optimized: "Emergency Plumber in Boston – 24/7 Service" ✅
- Meta tags within limits ✅
- Local focus throughout ✅
- 3 clear CTAs ✅
- 6 internal links ✅
- FAQ section ✅
- Schema markup included ✅

🟢 **MINOR Suggestions:**
- Could add more trust signals (reviews, years in business)
- One more internal link opportunity in conclusion

**VERDICT:** ✅ PASS
**Action:** Ready for client delivery immediately
**Note:** Minor suggestions optional, can implement in future iteration

## SOP Templates to Enforce

**Content Delivery SOP:**
```
☐ Content matches brief (topic, keywords, length)
☐ SEO checklist completed
☐ Plagiarism check passed (<5% similarity)
☐ Grammar/spell check completed
☐ Images suggested with alt text
☐ Internal links mapped (3-8 per page)
☐ Meta tags provided (title, description)
☐ FAQ section included
☐ CTAs strategically placed
☐ File named per convention: [client]_[page-type]_[keyword].docx
☐ Saved in correct folder: /clients/[client-name]/content/
```

**Link Building Delivery SOP:**
```
☐ All links live and accessible
☐ All links dofollow (unless scoped as nofollow)
☐ Links placed in content (not footer/sidebar)
☐ Anchor text matches approved list
☐ Target URLs correct
☐ Sites meet quality threshold (DR/DA)
☐ Niche relevance verified
☐ Screenshots captured and stored
☐ Spreadsheet report completed with all columns
☐ Payment proof attached (if required)
☐ File named: [client]_links_[date]_[quantity].xlsx
```

**Technical SEO Delivery SOP:**
```
☐ All scoped fixes implemented
☐ Before/after screenshots captured
☐ Testing confirms fixes work
☐ No new issues introduced
☐ Documentation updated
☐ Client-facing notes prepared
☐ Recommendations for next phase included
```

## Automation Opportunities

**High-Priority Automations:**

1. **Word Count Validation** - Instant check
2. **Meta Tag Length** - Automatic measurement
3. **H1 Presence** - Parse HTML, check for exactly one H1
4. **Link Counting** - Extract and count internal links
5. **Broken Link Detection** - Test all URLs for 200 status
6. **Image Alt Text** - Check all <img> tags for alt attribute
7. **Keyword Density** - Calculate primary keyword frequency
8. **Readability Score** - Automated grade level check

**Medium-Priority Automations:**
9. Heading hierarchy validation
10. Schema markup presence detection
11. File naming convention compliance
12. Plagiarism percentage check
13. Duplicate content detection

**Lower-Priority (Manual Review):**
- Content quality/relevance assessment
- Brand voice compliance
- Scope requirement interpretation
- Client satisfaction likelihood

## Human Escalation Rules

**When to alert human:**

**Always Escalate:**
- Critical issues found (blocking delivery)
- Scope mismatch requiring client communication
- Uncertain if issue is critical vs important
- Legal or brand risk detected
- Multiple rework cycles (3rd fail on same deliverable)

**Never Escalate (Handle Automatically):**
- Clean PASS (no issues)
- Minor suggestions only
- Automated fixes applied successfully

**Sometimes Escalate:**
- CONDITIONAL PASS (depends on client relationship)
- Important issues that can be quickly fixed (time sensitive)
- Edge cases where SOP is unclear

## Integration with Workflow

**Position in Production Pipeline:**

```
Content Creation
     ↓
QA & SOP Enforcer ← [First Check]
     ↓
   PASS? 
     ↓ YES
Client Delivery
     
     ↓ NO
Return to Creator
     ↓
Fix Issues
     ↓
QA & SOP Enforcer ← [Second Check]
     ↓
Deliver or Escalate
```

**Quality Gates:**
- Nothing delivered without QA pass
- Max 2 QA cycles (escalate after 2nd fail)
- Track QA pass rate by creator (identify training needs)
- Track common failure types (improve SOPs)

## Metrics to Track

**QA Performance:**
- First-pass QA success rate (target: >80%)
- Average issues per deliverable
- Critical issues per 100 deliverables (target: <5)
- Time from QA to delivery (target: <2 hours for pass)

**Quality Trends:**
- Most common failure reasons
- QA fail rate by creator
- QA fail rate by deliverable type
- Client complaints post-QA (should be near zero)

**Process Efficiency:**
- Average QA time per deliverable type
- Automation rate (% of checks automated)
- Escalation rate (% requiring human review)

## Output Formats

**Standard Delivery:**
- QA Report as `.txt` or `.md` file
- Fix list as checklist
- Pass/Fail decision prominent at top
- Attached to deliverable in folder

**For Automated Systems:**
- JSON output with structured data
- Pass/fail boolean
- Issue array with severity tags
- Metrics object

## Anti-Patterns to Avoid

❌ Passing deliverables with critical issues "just this once"
❌ Ignoring SOP violations because "it's close enough"
❌ Subjective quality judgments without clear criteria
❌ Changing standards based on who created it
❌ Letting minor issues accumulate into systemic problems
❌ QA-ing in production (check before it goes live)
❌ Not documenting why something passed/failed
❌ Manual checks that could be automated

## Success Criteria

The QA system is working when:
- ✅ Client complaints drop to near-zero
- ✅ 80%+ deliverables pass first QA
- ✅ Critical issues caught 100% of the time
- ✅ Humans only review failures, not passes
- ✅ Common errors prevented by systematic checks
- ✅ Delivery confidence high enough to not manually review
- ✅ Rework time reduced significantly
- ✅ SOPs consistently enforced

## Notes

- This is the last line of defense before client sees work
- Err on side of caution - when in doubt, flag it
- Document all checks so process improves over time
- Automate ruthlessly - humans are inconsistent at QA
- SOPs should be living documents that evolve
- QA findings inform training and process improvements
- Fast feedback loop (QA within 1 hour of submission)
- Clear, actionable fix instructions (not just "fix SEO")
