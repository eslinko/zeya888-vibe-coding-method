# Process observe: lightweight follow-up after Done stories (no new STORY)

> **Kind:** process capture for methodology extrapolation (not a worklog of product content).  
> **Date:** 2026-09-19  
> **Context sample:** landing · after Builder Queue stories already Done · small discovery gap.  
> **Rules in force:** [analysis.mdc](../../../.cursor/rules/analysis.mdc) · [git-commit.md](../../git-commit.md) / [git-commit-prompt.md](../../git-commit-prompt.md)

## What this is / is not

| Is | Is not |
|----|--------|
| Sequence of **roles, gates, artifact classes** | Description of the feature / REQ / AC |
| Pattern for “Done story, small miss, no new STORY” | Replacement for P1.3–P8 Builder Queue |
| Input for a methodology dialog to **extrapolate** | Instruction to re-run the same product change |

Product names, routes, and copy from the sample wave are **placeholders for the process**, not the deliverable of this note.

---

## Trigger

1. Product stories already **Done** in pipeline / pkg / gate (runtime exists).
2. Operator (or validate) finds a **small discovery/hygiene gap** that was never in story AC (e.g. chrome link, stale Meta status).
3. Operator judges: **too small for a new STORY** · ask-scoped · analysis.mdc (name ≠ create).

---

## Roles (same chat or split)

| Role | Job |
|------|-----|
| **Docs / plan author** | Sync stale status if needed; write implement `.plan` + launch prompt + **separate** validate `.plan` |
| **Implementer** | Execute implement plan only; mark plan todos; stop when implement PASS |
| **Validator** | Execute validate plan only (Read/Grep/Shell); PASS/FAIL with paths; no edits unless FAIL + operator says fix |
| **Commit agent** | `git-commit` methodology: filter · group · plan · commit · push **only** if operator ordered push |

Do not merge implement + validate into one “do everything” plan when the operator asked for two plans.

---

## Artifact sequence (class → class)

```text
[optional] backlog Meta/INDEX hygiene (Done sync)
        ↓
implement .plan.md   (touch list, locale rules, OOS, prove)
        ↓
LAUNCH prompt.md     (copy-paste: @analysis + @implement-plan)
        ↓
implement wave       (product/docs edits per plan)
        ↓
validate .plan.md    (checks table; smoke optional/N/A)
        ↓
validate wave        (verdict PASS|FAIL)
        ↓
git-commit (+ push if explicit)
```

### Plan author constraints (verified pattern)

- **No new STORY / pkg / materialize** unless operator expands scope.
- Plans cite **verified** as-is (where UI already maps arrays / helpers) — no invent components.
- Implement plan lists **exact surfaces** (e.g. locale arrays vs action rows) and **l10n** expectations per locale file.
- Validate plan is **validate-only**; optional smoke must not FAIL the whole gate if server down (N/A).
- Launch prompt points to both plans; tells implementer to **stop** before validate.

---

## Gates

| Gate | Pass condition |
|------|----------------|
| Scope | Deliverable class matches operator ask (plans only → plans only; implement → code/locales; validate → report) |
| analysis.mdc | Claims from disk; no stub trees because a path was named |
| Validate | All must-PASS checks evidenced; smoke N/A allowed |
| Commit | No `docs/analysis/**`; no secrets/session agent ids; push only on explicit ask |

---

## Anti-patterns observed (avoid when extrapolating)

1. **Story inflation** — opening a full STORY/pkg for a one-surface locale append.
2. **Plan-checklist obedience** — implementing extras “while here” outside the implement plan.
3. **Validate edits by default** — validate plan says report; fix only on FAIL + order.
4. **Stale Meta** — pipeline Done while backlog card still `Todo` (hygiene before or with docs commit).
5. **Single mega-plan** — mixing “write plans”, “implement”, “validate”, “commit” when operator split them.

---

## Extrapolation hooks (for methodology dialog)

**Extrapolated (2026-09-19):** guide + prompts — [`../guides/lightweight-followup.md`](../guides/lightweight-followup.md) · [`../prompts/operator/lightweight-followup-triage.md`](../prompts/operator/lightweight-followup-triage.md) · [`../prompts/operator/lightweight-followup-author.md`](../prompts/operator/lightweight-followup-author.md).

When generalizing further, ask:

1. What is the **smallest artifact class** that closes the gap (locale key vs component vs story)?
2. Should **implement** and **validate** stay as separate plans/chats?
3. Where do launch prompts live (project `docs/tasks/prompts/` vs methodology prompts)?
4. How does this sit next to Builder Queue overnight (orthogonal follow-up vs in-queue story)?
5. Commit grouping: product locale commit vs docs/process commit vs exclude analysis?

---

## Sample paths (this observation only — not template SSOT)

| Artifact | Example path class |
|----------|-------------------|
| Implement plan | `.cursor/plans/<slug>.plan.md` |
| Validate plan | `.cursor/plans/<slug>-validate.plan.md` |
| Launch | `<project>/docs/tasks/prompts/<slug>-LAUNCH.md` |
| This note | `docs/methodology/Zeya888-builder-queue/analysis/` |

Do not treat sample product files as required outputs of the process pattern.
