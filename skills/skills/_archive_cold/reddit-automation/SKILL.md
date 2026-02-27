---
name: reddit-automation
description: Automate Reddit services using Airtable and Make.com. Orchestrates the flow from order reception to worker assignment, AI verification, and client reporting. Use when setting up or managing the automated Reddit service fulfillment system.
---

# Reddit Service Automation Orchestration

**Objective:** Transition from a manual, high-touch "middleman" workflow to an automated "orchestrator" system. The goal is to "touch data once" and utilize AI and automation for the remainder of the process.

## 1. System Architecture (The Tech Stack)
To execute this plan, the following core components are required:

*   **Central Brain:** **Airtable** (Stores Clients, Active Orders, Workers, and Deliveries).
*   **Input Mechanism:** **Tally Forms** or **Typeform** (For client orders and worker proof-of-work submissions).
*   **The Engine:** **Make.com** (Connects tools; e.g., "If Order Created -> Notify Worker").
*   **Workforce Huddle:** **Discord** or **Slack** (For job posting and claiming).
*   **Quality Control:** **OpenAI (GPT-4o)** via Make.com (Verifies links, sentiment, and context).

## 2. Implementation Phase 1: Database Construction
Replace manual tracking with a relational database in Airtable containing three specific linked tables.

**Table A: Clients**
*   `Client ID` (Auto-number)
*   `Name`
*   `Email`
*   `Status` (Active/Churned — utilize "Green Tick" logic)
*   `Total Spend` (Rollup)
*   `Linked Orders` (Link to Orders table)

**Table B: Orders**
*   `Order ID`
*   `Client` (Link to Clients)
*   `Service Type` (e.g., "Review", "Comment", "Thread")
*   `Status` (Pending, In Progress, Reviewing, Completed)
*   `Input Data` (Promotional URLs, keywords)
*   `Quantity Ordered` (Number)
*   `Assigned Worker` (Link to Workers)
*   `Proof Links` (Long Text or Link to Deliveries)

**Table C: Workers**
*   `Worker Name` (e.g., Tank, Nivea)
*   `Platform` (Telegram/Skype)
*   `Payment Details`
*   `Performance Score` (Rollup of valid tasks)

## 3. Implementation Phase 2: Workflow Automation
Configure **Make.com** to handle the following three scenarios.

**Scenario A: New Order Processing**
*   **Trigger:** A "New Order" form is submitted in Airtable/Tally.
*   **Action:**
    1.  Create a record in the `Orders` table.
    2.  Send a message to the Discord channel `#new-jobs`: *"New Order: 5 Reddit Comments. Payout: $X. Reply to claim."* (Or auto-assign to primary workers).

**Scenario B: Work Submission & Verification (The "Magic" Step)**
*   **Trigger:** A worker fills out a "Work Submission Form" containing a list of Reddit links.
*   **Action:**
    1.  **Split Data:** Iterate through the submitted links.
    2.  **AI Audit:** Send data to OpenAI with the system prompt: *"You are a Reddit QA Auditor. Check this link: {{Link}}. Does it exist? Is the sentiment positive? Does it mention the client's brand {{Brand}} naturally? Rate 1-10"*.
    3.  **Decision Logic:**
        *   **If Score > 8:** Mark as "Verified".
        *   **If Score < 8:** Send a Discord DM to the worker: *"Link {{Link}} failed audit. Reason: {{AI_Reason}}. Please fix"*.
    4.  **Aggregation:** When all links in an order are "Verified," update the Order Status to "Completed".

**Scenario C: Reporting**
*   **Trigger:** Order Status changes to "Completed".
*   **Action:**
    1.  Generate a report (Google Doc or PDF).
    2.  Email the client: *"Your order for {{Service_Type}} is complete. Here is your report"*.

## 4. Implementation Phase 3: Immediate Deployment
To activate this system immediately:
1.  **Migration:** Export "Green Tick" clients from OneNote to CSV and import them into the Airtable "Clients" table.
2.  **Platform Setup:** Create the Airtable Base, a free Make.com account, and a dedicated Discord server for workers.
3.  **Bot Setup:** Connect Make.com to both Discord and the OpenAI API.

## 5. Future Scalability: "The Hunter"
*Note: This phase is to be activated only after fulfillment is stable.*

*   **Lead Gen:** Use **Apify** to scrape `r/marketing` for keywords like "SEO help".
*   **Enrichment:** Use **Clay** to find the emails of those posters.
*   **Outreach:** Use **Instantly.ai** to send cold emails.
