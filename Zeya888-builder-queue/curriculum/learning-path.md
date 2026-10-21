# Learning path — Zeya888 Builder Queue

**Human first entry:** [`human-entry-manual.md`](./human-entry-manual.md)  
**Method meaning:** [`00-guide-for-humans.md`](./00-guide-for-humans.md)  
**Training dialogues (AI):** [`../prompts/training/INDEX.md`](../prompts/training/INDEX.md)  
**Consultation / guided adoption:** [`../guides/consultation-positioning.md`](../guides/consultation-positioning.md)

## Document roles (on conflict)

| Role | Where | Rule |
|------|-------|------|
| **Normative** | `core/workflow.md`, `core/session-starter.md`, `contracts/`, `specs/` | Canon for agent and operator |
| **Teaching** | `curriculum/`, `prompts/training/` | Learning; does not override canon |
| **Legacy** | `core/workflow-legacy.md` | Historical full prompts; phase numbering may differ |

---

## Two learning routes

Both start with the entry manual and dialogues **1 → 2**. Then they branch.

### Shared intro (everyone)

1. [`human-entry-manual.md`](./human-entry-manual.md) — choose route, open chat, paste prompt  
2. Training **01** — how the system works  
3. Training **02** — how the operator steers work  

### Route A — technical operator (+ own agents)

**Expected outcome:** understand the system, connect the project, run the cycle from documentation yourself.

4. Training **03A** — connect your project (adaptation plan; no demo code/pkg)  
5. Training **04A** — first managed work session (only after explicit human go-ahead)  
6. Then — curriculum modules 1–6 below and [`../core/session-starter.md`](../core/session-starter.md)  
7. Optional training **05A** — Markstack (L1→L1.5→L2) when residual / screens → stories before Apply ([`../prompts/training/05a-markstack-story-intake.md`](../prompts/training/05a-markstack-story-intake.md))

### Route B — fintech vibe-coder

**Expected outcome:** understand value and shape, your role, prepare a brief for guided adoption. **Do not** claim readiness for solo operation of every engineering decision.

4. Training **03B** — project brief  
5. [`../guides/consultation-positioning.md`](../guides/consultation-positioning.md) — self-serve vs guided adoption  
6. Stop at contacting the author (contact in the memo)

---

## Curriculum modules (reference / after learning dialogs)

These files are **explanations + pointers to operative**. They **do not replace** training 01–02.  
[`01-first-session.md`](./01-first-session.md) = **operative** Phase 0 onboarding, not the “how the system works” training dialog.

| # | Topic | Human (explanations) | Operative (prompts / spec) | Outcome |
|---|-------|----------------------|----------------------------|---------|
| 0 | Method overview | [00-guide-for-humans.md](./00-guide-for-humans.md) | [MANIFEST.md](../MANIFEST.md) | Why the method, architect role, three SSOT layers |
| 1 | First work session | [01-first-session.md](./01-first-session.md) | [session-starter.md](../core/session-starter.md) | Phase 0 onboarding |
| 2 | Package + window | [02-first-package-and-window.md](./02-first-package-and-window.md) | [input-package-spec.md](../specs/input-package-spec.md) | verify + build window |
| 3 | Workflow PA + P0–P8 | [03-workflow-phases-explained.md](./03-workflow-phases-explained.md) | [workflow.md](../core/workflow.md) | PA → P1 → full cycle |
| 4 | CLI and contracts | [04-cli-and-contracts-explained.md](./04-cli-and-contracts-explained.md) | [queue-manual.md](../cli/queue-manual.md) | Commands and operator rules |
| 5 | Your project | [05-connect-your-project.md](./05-connect-your-project.md) | [cursor-setup.md](../integration/cursor-setup.md) | profiles + plan |
| 6 | Architect Studio + P1 intakes | [06-architect-studio-and-p1-intakes.md](./06-architect-studio-and-p1-intakes.md) | [workflow.md](../core/workflow.md) §PA + §P1 · [markstack.md](../guides/markstack.md) | Studio = PA; three intakes; Markstack for residual; handoff |

**For route A after 04A:** module 5 ↔ training 03A; module 6 ↔ PA → P1 bridge; optional training **05A** ↔ Markstack when residual UI → stories.

## For instructors

- Demo profile: [`../examples/sample-profiles/minimal.yaml`](../examples/sample-profiles/minimal.yaml)
- Reference plans — structure review only: [`../examples/reference-plans/`](../examples/reference-plans/)
- Full self-contained prompts (legacy): [`../core/workflow-legacy.md`](../core/workflow-legacy.md)

## Prerequisites

- Cursor IDE (or equivalent with `@` files)
- Route A: Python 3.11+, basic git and YAML
- Route B: enough to describe the project goal in plain language

## Order (short)

1. Entry manual → training 01 → 02.  
2. Branch A: 03A → 04A → modules 1–6 / starter → optional **05A** (Markstack) if residual intake.  
3. Branch B: 03B → consultation memo → contact the author.  
4. Module 6 + workflow §PA — **before** first P1 if intake is raw.  
5. Residual / screens → stories: training 05A then operative [`markstack-intake.md`](../prompts/architect/markstack-intake.md) (not lightweight-followup).
