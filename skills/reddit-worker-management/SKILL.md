---
name: reddit-worker-management
description: Manage Reddit service workers including recruitment from Discord, onboarding with SLA, assigning tasks in CRM, and performing Quality Assurance (QA) on submitted work.
---

# Reddit Worker Management

## 1. Recruitment (Discord)

Use this template to recruit new workers from your Discord groups.

**Recruitment Message:**
> **Hiring: Reddit Comment Posters ($2.50 - $4.00 per comment)**
>
> We are looking for 2-3 reliable people with aged Reddit accounts.
>
> **The Job:**
> - We provide the content.
> - You provide the account and post it.
> - You check if it "sticks" (remains visible).
>
> **Requirements:**
> - Aged Reddit account (must have karma).
> - Ability to follow instructions exactly.
>
> **The Test:**
> I will send you 1 content piece. You post it on a thread. If it stays live, you're hired.
>
> **DM me "REDDIT POSTER" to apply.**

---

## 2. Onboarding Workflow

When a worker replies:
1.  **Send SLA**: Share the `docs/worker-sla.md` file content.
2.  **Assign Test Task**:
    - Provide: Thread URL + Comment Text.
    - Ask them to post within 12h.
3.  **Evaluate**: Did it stick? Is it visible?

---

## 3. QA Checklist (Pass/Fail)

For every submitted link, check:

- [ ] **Visible?** Open link in Incognito mode. Is it there?
- [ ] **Correct Content?** Did they post what you sent? (Small edits for grammar are OK, changing meaning is NOT).
- [ ] **Account Health?** Does the account look real?

**If Pass:**
- Add to `Worker Board` tab in `CRM Leads Manager .xlsx`.
- Mark as "Verified".

**If Fail:**
- DM worker: "Link failed QA (Removed/Shadowbanned). Can you edit/repost? (If allowed by client)".

---

## 4. Assignment Management

When assigning a new order:
1.  Open `CRM Leads Manager .xlsx`.
2.  Go to **Worker Assignments** tab.
3.  Fill in:
    - Worker Name
    - Order ID
    - **Content Link** (Google Doc or Cell ref with the text to post)
    - Deadline
4.  Ping worker: "New batch assigned. Content provided. Go!"
