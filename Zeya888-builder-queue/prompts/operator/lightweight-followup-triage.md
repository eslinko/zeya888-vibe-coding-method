# Lightweight follow-up — complexity triage (VAL)

**Категория:** operator (VAL gate)  
**Guide SSOT:** [`../../guides/lightweight-followup.md`](../../guides/lightweight-followup.md) §3  
**Next if PASS:** [`lightweight-followup-author.md`](./lightweight-followup-author.md)  
**Claims:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Не заменяет:** P4/P7 story audit · full Builder Queue

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | После Done-стори нашли мелкий gap; неясно, нужен ли STORY | Этот prompt → PASS \| ESCALATE |
| 2 | Оператор хочет low-complexity track | Сначала triage; **запрещено** писать implement plan до PASS |
| 3 | Подозрение, что задача сложная | Fail closed → ESCALATE |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/lightweight-followup.md
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml

builder_project: <key from profiles.yaml>
workspace_root: /Users/eslinko/Development/DOGEstonia
focus_role: validator

$gap=
$parentStoryOrPkg=   # Done story / pkg path or Unknown
$ask=

Lightweight follow-up TRIAGE only (complexity gate).
MODE: read-only. No plans, no product edits, no commits.
Claims: Read/Grep with paths; else Unknown → treat as risk (fail closed).

## Step 0 — Restate ask
One sentence: deliverable class (locale/config/docs/other) + surfaces named by operator.

## Step 1 — Verify parent Done
Find evidence that parent work is Done (bullrun / backlog Meta / pkg gate). Missing → HIT #6.

## Step 2 — Hard-fail rubric
Apply guides/lightweight-followup.md §3 Hard HIT 1–10.
For each HIT: HIT|clear with path evidence or N/A with why.
Grep as-is for “existing map/helper” before clearing HIT #2/#3.

## Step 3 — Soft signals
List soft signals if any; they cannot clear a hard HIT.

## Step 4 — Verdict (exactly one)
- PASS — lightweight allowed. List allowed touch classes. Next: run lightweight-followup-author.md (do not author in this turn unless operator pastes author prompt now).
- ESCALATE — name blocking HIT ids + recommended route (PA | P1.3 STORY | full BQ | ask operator). Stop.

Do NOT write .cursor/plans/* or LAUNCH in triage.
```

---

## Примечания

- Evolving rubric: edit **guide §3** only; this file stays a thin fence.  
- If operator pastes triage+author in one message: still emit triage verdict **first**; author only if PASS.
