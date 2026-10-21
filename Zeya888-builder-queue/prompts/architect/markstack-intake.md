# Markstack — residual → L1 / L1.5 / L2 story intake

**Категория:** architect (pre-Apply / docs-wave)  
**Guide SSOT:** [`../../guides/markstack.md`](../../guides/markstack.md)  
**Claims:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Не заменяет:** P1.3–P8 · overnight OP · [`../operator/lightweight-followup-triage.md`](../operator/lightweight-followup-triage.md) (post-Done, no new STORY)

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | После live UI / скринов+комментов нужны новые или уточнённые `STORY-*` до Apply | Этот prompt → Interview → L1→L1.5→L2 |
| 2 | Residual marks + locks (docs-only / phased wire) | Follow guide §3–§4; materialize only on verb |
| 3 | Post-Done мелкий gap без STORY | STOP → lightweight-followup |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/markstack.md
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml

builder_project: <key from profiles.yaml>
$residual=          # interview path, marks list, or screenshot notes
$locks=             # e.g. 1A docs-only · 2A wire phase · or Unknown
$packageDir=        # backlog-stories/<pkg>/ if known

Markstack intake (L1 → L1.5 → L2). Follow guides/markstack.md.
MODE: docs-only intake. No product code. No invent OP PASS. No empty pipeline trees (name ≠ create).
Claims: Read/Grep/Glob with paths; else Unknown.
Default: plan + drafts in chat; materialize L1/L1.5/L2 files only after operator «запиши» / «materialize».

## Step 0 — Route check
If parent story Done and ask is small hygiene without new STORY → STOP; point to lightweight-followup.
If pure REQ→package with no residual → prefer req-to-backlog-stories / ui-admin / mixed.

## Step 1 — Code probe
For each residual symptom: Present | Partial | Absent with path evidence.

## Step 2 — Interview SSOT
Locks + allocation table (mark → story) + explicit non-goals.
Write INTERVIEW-*.md only on materialize verb (or use existing $residual if already Interview).

## Step 3 — Sufficiency
Need UX prompts? Sibling REQ? Or CSS/code lock only.

## Step 4 — L1 (per story)
FR numbered + AC + OOS + DoD. Product language. Meta: structure | visual | gate.

## Step 5 — L1.5
ARCH § or ARCH-DELTA · ownership table · explicit supersede.

## Step 6 — L2
3–5 tasks · Order · FR links · skill · Status Await.

## Step 7 — Cross-links
INDEX · sibling packages · depends (HTTP before SPA wire when applicable).

## Step 8 — Stop
Docs wave complete when artifacts on disk (after materialize). Apply / P1.3 separately.
Do not invent Present=PASS; step 9 Present table is a later wave.

Return: paths created or planned; blockers; what was skipped (name≠create).
```

---

## Notes

- Layers stay tagged **L1 / L1.5 / L2**; brand name is **Markstack**.  
- Связанные: [`req-to-backlog-stories.md`](./req-to-backlog-stories.md), [`req-to-ui-admin-layers.md`](./req-to-ui-admin-layers.md), [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md), [`../operator/lightweight-followup-triage.md`](../operator/lightweight-followup-triage.md).
