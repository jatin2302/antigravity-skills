---
name: finding-reddit-threads
description: Discovers relevant Reddit threads for brand promotion and generates tailored engagement suggestions. Use when the user wants to identify marketing opportunities on Reddit.
---

# Finding Reddit Threads

## When to use this skill
- When searching for niche subreddits and active discussions related to a brand or product.
- When identifying organic promotion opportunities on Reddit.
- When generating authentic-sounding comments for Reddit engagement.

## Workflow
1. [ ] **Define Brand Profile**: Create a JSON profile with brand name, products, and initial keywords.
2. [ ] **Expand Search Terms**: Use the `discover_context.py` script to get AI-suggested subreddits and keywords.
3. [ ] **Search and Scrape**: Execute `search_threads.py` to find active Reddit threads.
4. [ ] **Quality Filter**: Review the threads for activity, non-archived status, and sentiment.
5. [ ] **Generate Engagement**: Use `generate_comment.py` to draft responses that align with the subreddit's tone.

## Instructions

### 1. Brand Profile Structure
Create a `brand_profile.json` in the root of your project:
```json
{
  "brand_name": "ExampleBrand",
  "products": ["Product A", "Product B"],
  "keywords": ["problem solved by product", "best tool for X"],
  "target_subreddits": ["niche_sub"],
  "persona": "A helpful expert in X"
}
```

### 2. Discovering Context
If keywords are limited, run the discovery script to expand the search space:
```bash
python .agent/skills/finding-reddit-threads/scripts/discover_context.py
```

### 3. Finding Threads
Search for threads using the expanded keywords:
```bash
python .agent/skills/finding-reddit-threads/scripts/search_threads.py
```
*Note: This script uses `old.reddit.com` for efficient scraping without API limits.*

### 4. Tailoring Comments
Generate responses for discovered threads:
```bash
python .agent/skills/finding-reddit-threads/scripts/generate_comment.py --thread_id [ID]
```

## Best Practices
- **Authenticity First**: Avoid corporate speak. Use the generated persona to keep comments human.
- **Subreddit Etiquette**: Different subreddits have different "vibes" (e.g., r/tech is blunt, r/support is empathetic). Always adapt the tone.
- **Check Expiry**: Ensure threads are not archived before suggesting comments.

## Resources
- [Brand Profile Template](resources/brand_profile_template.json)
- [Example Discovery Output](examples/discovery_output.json)
