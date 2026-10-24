# Markstack — process SSOT (L1 → L1.5 → L2 story intake)

> **Provenance:** [`../../../../spa-app/docs/analysis/method-l1-l15-l2-story-intake-and-retrospective-2026-10-21.md`](../../../../spa-app/docs/analysis/method-l1-l15-l2-story-intake-and-retrospective-2026-10-21.md)  
> **Prompt (operative):** [`../prompts/architect/markstack-intake.md`](../prompts/architect/markstack-intake.md)  
> **Training:** [`../prompts/training/05a-markstack-story-intake.md`](../prompts/training/05a-markstack-story-intake.md)  
> **Claims:** [`.cursor/rules/analysis.mdc`](../../../../.cursor/rules/analysis.mdc)  
> **Не заменяет:** Builder Queue P1.3–P8 · overnight OP · lightweight-followup (post-Done, no new STORY) · P4/P7 story audit

**Brand:** Markstack · **Layers (keep tags):** L1 / L1.5 / L2  
Трёхслойная постановка product story **до** runtime Apply — из сырого OP residual (live UI marks, скрины+комменты, locks).

## 1. Когда это

| Trigger | Not this |
|---------|----------|
| Live UI residual / rough screenshots + comments after testing | Post-Done hygiene **without** new STORY → [`lightweight-followup.md`](./lightweight-followup.md) |
| Need new or tightened `STORY-*` (FR/AC/OOS) **before** Apply | Pure REQ→package materialize with no residual → [`req-to-backlog-stories.md`](../prompts/architect/req-to-backlog-stories.md) / ui-admin / mixed |
| Operator locked docs-only (1A) or phased wire (2A) | Invent OP PASS / declare citizen-ready without Present table + OP eye |

**L1/L1.5/L2 ≠ P0–P8.** Markstack = intake quality. P3/P5 = execution and evidence. Gate BLOCK / OP eye = separate.

## 2. Layers

| Layer | Name | Artifact | Question |
|-------|------|----------|----------|
| **L1** | Product FR / AC | `STORY-*.md` · numbered FR · Out of scope · AC checkboxes · DoD | *What* must be true for citizen/operator — no JSX recipe |
| **L1.5** | Architecture locks | `ARCHITECTURE.md` §N · or `ARCH-DELTA-*.md` · ownership table | *Where* the rule lives · what supersedes · package boundaries |
| **L2** | Tech subtasks | `task-…-t0N` table in the same story · Order · skill | *How* to slice Apply into atoms with file targets |

## 3. Preconditions

1. **Interview SSOT** — operator decisions + code facts (not negotiable in Apply).  
2. **Sufficiency gate** — per mark: **UX** | **REQ** | **CSS/code**.  
3. **UX prompts** — when visual is Absent / wrong asset / layout Apply would invent (logo plate, new page composition, strip residual not covered by existing artboard). Draft `UX-PROMPTS-*.md` **before** L1 for those marks. Gen/intake PASS may be a later wave; stories cite the prompt and stay `visual BLOCK` until intake.  
4. **REQ** — only if a new service contract is required (sibling project).  
5. Then **L1 → L1.5 → L2** per story.  
6. INDEX / tip / depends updated. Pipeline epic folders — on Apply / P1.3, not required in docs-wave (**name ≠ create**).

## 4. Algorithm

```text
1. Code probe (grep/read) → Present / Partial / Absent vs OP symptoms
2. Interview: locks + allocation table + explicit non-goals
3. Sufficiency: per mark UX | REQ | CSS/code — if UX → draft UX-PROMPTS (gate; do not jump to L1)
4. L1: FR + AC + OOS + DoD (product language) · cite Interview + UX tip when visual
5. L1.5: arch § / delta · map Story→§ · supersede notes
6. L2: 3–5 tasks · Order · FR links · Await Apply
7. Cross-links INDEX · sibling packages · depends (HTTP before SPA wire)
8. Stop (docs wave) OR Apply separately
9. Later: code validation vs L1 (Present/Partial/Absent table) — do not invent PASS
```

In every story **Meta:** three fields — `structure | visual | gate` (avoid “structure Done” read as visual Done).

### 4.1 L1 quality

- FR numbered and **checkable** on live UI or test.  
- OOS explicit (else Apply inflates scope).  
- No “make it pretty” without measurable chrome.  
- Do not duplicate HTTP contract in SPA story — **link** sibling REQ/story.

### 4.2 L1.5 quality

- One ownership table: Rule → Owner file/package.  
- Supersede old locks **explicitly**.  
- No JSX snippets as “architecture” — seams only.

### 4.3 L2 quality

- Tasks ≤ what one Apply package can close.  
- Order with hard depends.  
- Skill declared.  
- Status Await until Apply — do not mark Done in docs-wave.

## 5. Done (intake wave)

| Complete when |
|---------------|
| Interview (if needed) + **UX-PROMPTS for every UX-class mark** + L1 stories + L1.5 locks + L2 tasks + INDEX/depends on disk |
| No empty epic pipeline trees created “so paths exist” |
| Operator can hand off to Apply / P1.3 without oral legend (visual may still BLOCK pending artboard intake) |

**Not Done for citizen:** until (a) code Present table vs L1 and (b) OP eye / Path A on target URL.

## 6. Anti-patterns

1. Skipping Interview and inventing FR from memory.  
2. **Interview → L1 without Sufficiency UX table** when visual would be invented.  
3. Confusing L\* intake with P\* Builder Queue phases.  
4. Self-ACCEPTED / invent PASS after docs-wave.  
5. L2 Done while Apply not run.  
6. Pipeline scaffold under name≠create docs-wave.  
7. Using Markstack for post-Done one-surface hygiene (use lightweight-followup).

## 7. Relation to other methods

| Method | Use when |
|--------|----------|
| [`req-to-backlog-stories.md`](../prompts/architect/req-to-backlog-stories.md) / ui-admin / mixed | REQ → STORY/ADMIN package materialize |
| **Markstack** | Residual / screens → layered L1–L2 quality on stories **before** Apply |
| [`lightweight-followup.md`](./lightweight-followup.md) | Parent story **Done**; small gap; **no** new STORY |
| Builder Queue P1.3–P8 | Execute / evidence after intake is on disk |
