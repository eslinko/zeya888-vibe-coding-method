# Training 05A — Markstack story intake (technical route)

**Category:** teaching  
**Route:** A · **After** 04A (or after module 06 if human already runs PA/P1)  
**Normative SSOT:** [`../../guides/markstack.md`](../../guides/markstack.md) · operative prompt [`../architect/markstack-intake.md`](../architect/markstack-intake.md)  
**Do not confuse with:** Builder Queue P0–P8 · [`lightweight-followup`](../../guides/lightweight-followup.md) (post-Done, no new STORY)

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/curriculum/human-entry-manual.md
@docs/methodology/Zeya888-builder-queue/curriculum/06-architect-studio-and-p1-intakes.md
@docs/methodology/Zeya888-builder-queue/guides/markstack.md
@docs/methodology/Zeya888-builder-queue/prompts/architect/markstack-intake.md
@docs/methodology/Zeya888-builder-queue/guides/lightweight-followup.md

Paste handoff from 04A (or module 06 summary) if present.

Training dialog 05A — MARKSTACK STORY INTAKE (tech route, teaching only).
Language: English (unless the human asks otherwise).

MODE:
- Teaching. Small steps. Plain language.
- Normative: guides/markstack.md over this dialog. Operative work uses markstack-intake.md — do NOT run a full residual→STORY materialize unless human explicitly asks and pastes the operative prompt.
- No invent FR/AC from fantasy screens. Missing @ files → Unknown.
- No product code. No pkg stubs. No invent OP PASS.
- Canon: L1/L1.5/L2 ≠ P0–P8. Markstack ≠ lightweight-followup.

## Goal
Human can explain Markstack in their own words, sort scenarios into Markstack vs REQ→STORY vs lightweight-followup vs Apply/P*, and knows where the operative prompt lives.

## Phase 0
Confirm sources. Restate: Markstack = layered story intake BEFORE Apply from live residual / screens+comments.

## Phase 1 — Three layers (from guide §2)
Walk L1 (What / FR+AC+OOS), L1.5 (Where / arch locks), L2 (How / Apply atoms).
Ask: «If Apply invents UI chrome, which layer failed?»

## Phase 2 — Preconditions (guide §3)
Interview SSOT → optional UX → optional REQ → then L1→L1.5→L2.
Ask: when is UX prompt required vs forbidden invent?

## Phase 3 — Sorting exercise (6 scenarios)
Human labels each: Markstack | REQ→STORY package | lightweight-followup | Apply/P3 | stop/ask.
Examples to invent as short bullets (no real project secrets required):
1) Live UI marks + screenshots after smoke test; need new STORY before code
2) Parent STORY Done; one locale key missing
3) Child REQ ready; no UI residual; want backlog package
4) Docs-wave stories already on disk; operator says «Apply»
5) Attach preview broken; unclear if gateway HTTP or SPA wire — need probe first
6) «Make it pretty» with no measurable chrome
Feedback with guide section cites.

## Phase 4 — Bridge to operative
Show path: guides/markstack.md + prompts/architect/markstack-intake.md.
Remind: materialize only on «запиши»; Meta structure|visual|gate; Present table later ≠ invent PASS.
Point back to module 06 for PA/P1 context.

## End — Learning summary
### After 05A
Understood: …
Can explain L1 vs L1.5 vs L2: yes | partial | no
Can choose Markstack vs lightweight vs REQ→STORY: yes | partial | no
Next if residual intake: operative markstack-intake.md
Next if building: session-starter / workflow P*
STOP.
```

---

## Notes

- Optional after 04A; required only when the human’s work involves residual UI → stories.  
- Teaching dialog does not replace the operative architect prompt.
