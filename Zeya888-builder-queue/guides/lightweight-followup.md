# Lightweight follow-up — process SSOT

> **Provenance:** [`../analysis/process-observe-lightweight-followup-after-done-stories-2026-09-19.md`](../analysis/process-observe-lightweight-followup-after-done-stories-2026-09-19.md)  
> **Prompts:** [`../prompts/operator/lightweight-followup-triage.md`](../prompts/operator/lightweight-followup-triage.md) → [`../prompts/operator/lightweight-followup-author.md`](../prompts/operator/lightweight-followup-author.md)  
> **Claims:** [`.cursor/rules/analysis.mdc`](../../../.cursor/rules/analysis.mdc)  
> **Не заменяет:** Builder Queue P1.3–P8 · overnight OP · P4/P7 story audit

## 1. Когда это

| Trigger | Not this |
|---------|----------|
| Product story already **Done**; small discovery/hygiene gap **outside** story AC | New feature / REQ → STORY |
| Operator judges: too small for new STORY; ask-scoped | Full pkg / materialize / epic decompose |
| Verified as-is: existing UI already maps the data surface | New component / route / schema / NC |

Orthogonal to the active Builder Queue package: **do not** invent `STORY-*` / rewrite immutable `pkg-*` unless triage **ESCALATE**.

## 2. Role flow

```text
VAL chat: triage (complexity gate)
    │
    ├─ ESCALATE → stop; route to PA / P1.3 / full BQ (operator chooses)
    └─ PASS → VAL (or docs author): dual plans + LAUNCH
              │
              ├─ BLD: implement plan only → stop
              └─ VAL: validate plan only → PASS|FAIL
                    └─ commit agent (optional, explicit)
```

| Role | Job |
|------|-----|
| **Triage (VAL)** | Hard-fail complexity rubric; verdict PASS \| ESCALATE only |
| **Author (usually VAL)** | After PASS: implement `.plan` + validate `.plan` + project `*-LAUNCH.md` |
| **Builder** | Execute implement plan; mark todos; **stop** before validate |
| **Validator** | Execute validate plan; report; edit only if FAIL + operator says fix |
| **Commit** | [`git-commit.md`](../../git-commit.md) — plan first; push only if asked |

Do **not** merge implement + validate into one mega-plan when using this method.

## 3. Complexity gate (hard-fail)

**Any single HIT → ESCALATE.** Soft signals never override a hard HIT. If uncertain → **ESCALATE** (fail closed).

### Hard HIT (must ESCALATE)

1. Needs **new** `STORY-*` / epic / immutable `pkg-*` / P1 materialize / bullrun queue change.
2. New **runtime surface**: page/route, component, schema, API, middleware, adapter, NC Volume path, new npm dependency for the fix.
3. Changes **control flow** of existing components (not “append to already-mapped array/config”).
4. Touches **> 1 concern class** in one ask (e.g. locale + schema + UI layout) without operator narrowing.
5. **Security / auth / secrets / exploit-adjacent** or production infra deploy.
6. Parent story **not Done** (or unknown) — gap is unfinished AC, not follow-up.
7. Requires **P2 build window / P3 TASK_BATCH / P4–P7 story audit** to be correct.
8. Cross-**builder_project** or rename of profile SSOT.
9. Agent would need to **invent** AC, product copy policy, or architecture options (analysis.mdc: ask, don’t invent) — and operator did not lock them.
10. Estimated touch set **> 8 paths** or **> 3 locales** *and* no verified “same pattern already exists for each locale file”.

### Soft signals (strengthen ESCALATE; alone may PASS only if operator explicitly overrides in chat)

- Unverified whether UI maps the data (must Grep first; if still Unknown → hard HIT #9/#3).
- Meta/INDEX hygiene entangled with product edit and commit split unclear.
- Operator says “while here also…” scope creep.

### PASS (lightweight allowed) — all must hold

- Hard HIT count = 0.
- Deliverable class is small (typical: locale/config append, Meta status sync, one-line link, docs hygiene).
- Verified as-is cites **paths** proving existing map/helper.
- Operator ask matches that class (analysis.mdc Core 11–12).

## 4. Artifact classes

| Artifact | Path class | Notes |
|----------|------------|-------|
| Implement plan | `.cursor/plans/<slug>.plan.md` | Exact surfaces, OOS, prove todos |
| Validate plan | `.cursor/plans/<slug>-validate.plan.md` | Checks table; validate-only |
| Launch | `{focus}/docs/tasks/prompts/<slug>-LAUNCH.md` | Copy-paste BLD + VAL packets; thin Task optional |
| Triage note (optional) | chat only or `docs/analysis/` if operator asks | Do not invent analysis file |

## 5. Handoff

**Primary:** copy-paste packets in LAUNCH (BLD then VAL).  
**Thin Task/subagent (optional):** same fences as packets; one Task = implement-only OR validate-only — never both. See author prompt §Task.

## 6. Anti-patterns

1. Story inflation for one-surface append.  
2. Plan-checklist obedience / drive-by extras.  
3. Validate edits by default.  
4. Single mega-plan (author+implement+validate+commit).  
5. Skipping triage “because it looks small”.  
6. Soft-signal PASS when any hard HIT fired.

## 7. Relation to migration-validator

[`migration-validator.md`](../prompts/migration/migration-validator.md) restores VAL role for P4/P7 **story** audit.  
Lightweight follow-up is a **separate** VAL branch: triage → author → BLD → VAL validate. Link from validator bootstrap; do not fold into P4.
