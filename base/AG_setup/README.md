# AG Setup — Antigravity Agent Operating System

> A modular, file-based OS for AI coding agents. Handles session lifecycle, TDD execution, multi-agent wave coordination, and continuous learning — all through persistent markdown files.

**Version:** 3.1 | **Owner:** Jatin Bhutani

---

## Architecture

```
~/.gemini/
├── GEMINI.md                              ← Global Rules (V7) — always active
│
├── antigravity/
│   ├── README.md                          ← This file
│   │
│   ├── skills/                            ← Meta-skills (loaded per session as needed)
│   │   ├── ag-operating-protocols/        ← Boot sequence, pre-flight gates, handoffs
│   │   ├── agentic-planning-execution/    ← TDD specs, batch execution, 3-Strike
│   │   ├── continuous-improvement-protocol/ ← Retro → KI extraction → rule modification
│   │   ├── multi-agent-coordination/      ← Lead agent, waves, contracts, bug triage
│   │   ├── token-hygiene-and-skills/      ← ROI evaluation, pruning, surgical edits
│   │   ├── api-orchestrator/              ← Multi-tool orchestration, Composio, SDKs
│   │   ├── dev-browser/                   ← Browser automation with persistent state
│   │   ├── integrating-notebooklm/        ← NotebookLM research & content creation
│   │   ├── learning-from-tutorials/       ← YouTube tutorial curation via NotebookLM
│   │   └── prompt-refinement/             ← Prompt critique and expansion
│   │
│   ├── global_workflows/                  ← Slash commands (18 workflows)
│   │   ├── ag-build.md                    ← /ag-build — execute task plans
│   │   ├── ag-validate.md                 ← /ag-validate — close out tasks
│   │   ├── ag-status.md                   ← /ag-status — session snapshot
│   │   ├── TEMPLATE.md                    ← Dual-mode task plan template
│   │   ├── new-project-setup.md           ← /new-project-setup — PIP v2
│   │   ├── session-handoff.md             ← /session-handoff — context management
│   │   ├── clone-landing.md               ← /clone-landing — single-page clone
│   │   ├── clone-site.md                  ← /clone-site — multi-page clone
│   │   ├── clone-app.md                   ← /clone-app — full app clone
│   │   ├── clone-wordpress.md             ← /clone-wordpress — WP theme clone
│   │   ├── deploy-cpanel.md               ← /deploy-cpanel — cPanel deployment
│   │   ├── seo-audit.md                   ← /seo-audit — full SEO audit
│   │   ├── client-onboarding.md           ← /client-onboarding — intake flow
│   │   ├── prompt-writer.md               ← /prompt-writer — prompt generation
│   │   ├── skill-manager.md               ← /skill-manager — skill evaluation
│   │   ├── sync-ag-skills.md              ← /sync-ag-skills — repo sync
│   │   └── antigravity-skill-creator.md   ← skill creation workflow
│   │
│   ├── knowledge/                         ← Extracted KIs from continuous improvement
│   └── brain/                             ← NotebookLM AG Brain artifacts
│
your-project/
└── _agent/                                ← Per-project memory (created by /new-project-setup)
    ├── gemini.md                           ← Project identity + invariants (read at boot)
    ├── progress.md                         ← Session handoffs (read at boot)
    ├── findings.md                         ← Knowledge items + retros (read at boot)
    ├── bugs.md                             ← Cross-agent bug log
    ├── tasks/
    │   ├── task_plan.md                    ← Active plan (from TEMPLATE.md)
    │   └── archive/                        ← Completed plans (moved by /ag-validate)
    └── workflows/                          ← Project-specific workflow overrides
```

---

## The 3 Layers

### Layer 1 — Always-On (`GEMINI.md` → Global Rules V7)
Runs on every session. Defines operator mindset, 6 meta-skill references, and always-on rules for file locations, skill storage, edit discipline, AG Brain queries, and session handoffs.

### Layer 2 — Workflows (18 slash commands)

| Command | Purpose |
|---------|---------|
| `/ag-build` | Execute plan — forks to Single-Agent TDD or Multi-Agent waves |
| `/ag-validate` | Test every criterion → fix failures → write changelog → archive |
| `/ag-status` | Snapshot of active task, bugs, KI count, build health |
| `/new-project-setup` | Full PIP discovery interview → 4 memory files → NotebookLM notebook |
| `/session-handoff` | Manage context handoffs between sessions |
| `/clone-landing` | Clone a landing page |
| `/clone-site` | Clone a multi-page website |
| `/clone-app` | Clone a full interactive web app |
| `/clone-wordpress` | Clone into a WordPress theme |
| `/deploy-cpanel` | Deploy to cPanel hosting |
| `/seo-audit` | Full SEO audit on a website |
| `/client-onboarding` | Client intake through project kickoff |
| `/prompt-writer` | Generate high-fidelity prompts |
| `/skill-manager` | Evaluate, install, or skip discovered skills |
| `/sync-ag-skills` | Sync skills to the antigravity-skills repo |

### Layer 3 — Execution Modes

**SINGLE-AGENT** (≤2 files, one domain)
- TDD: write test → RED → implement → GREEN → refactor
- 3-Strike: 3 failures on same test → stop → escalate

**MULTI-AGENT** (3+ files, multiple domains)
- Lead Agent spawns, coordinates, never implements
- Domain skills auto-load per file scope (core/api/ui/qa)
- Wave 1 → gate on contracts → Wave 2 → gate → Wave 3 (QA)
- File ownership strictly enforced; cross-scope bugs logged to `_agent/bugs.md`

---

## Meta-Skills Reference

| Skill | When AG Loads It |
|-------|-----------------|
| `ag-operating-protocols` | Every session start |
| `agentic-planning-execution` | Every planning and build phase |
| `continuous-improvement-protocol` | After major epics, when `findings.md` > 150 lines |
| `multi-agent-coordination` | When `task_plan.md` declares `Mode: MULTI-AGENT` |
| `token-hygiene-and-skills` | When evaluating new skills or context is bloating |
| `api-orchestrator` | When task involves multi-tool orchestration or external SDKs |
| `dev-browser` | When task requires browser automation or web testing |
| `integrating-notebooklm` | When task involves NotebookLM research or content creation |
| `learning-from-tutorials` | When curating and learning from YouTube tutorials |
| `prompt-refinement` | When critiquing and expanding prompts |

---

## Typical Session

```bash
/ag-status                        # What's the current state?
# Plan your task (edit _agent/tasks/task_plan.md using TEMPLATE)
/ag-build                         # Execute
/ag-validate                      # Close out
```

---

## Changelog

### v3.1 (2026-03-07)
- **Added** README.md — full architecture documentation
- **Added** Domain Skill Loading section in ag-build workflow
- **Improved** TEMPLATE.md — Domain Skill column in Agent Assignments
- **Improved** gemini.md project template — directory map, code standards, invariants

### v3.0 (2026-03-07)
- Dual-mode TEMPLATE.md, Path A/B execution fork, 6-step ag-validate, project template

### v2.0
- 18 workflows, 10 skills, NotebookLM integration, project registry

### v1.0
- Initial: GLOBAL_RULES, 5 meta-skills, multi-agent workflows
