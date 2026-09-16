# Training 01 — How the system works

**Category:** teaching · **Route:** A and B  
**Next:** [`02-how-the-operator-steers.md`](./02-how-the-operator-steers.md)  
**Human entry:** [`../../curriculum/human-entry-manual.md`](../../curriculum/human-entry-manual.md)

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/curriculum/00-guide-for-humans.md
@docs/methodology/Zeya888-builder-queue/curriculum/human-entry-manual.md
@docs/methodology/Zeya888-builder-queue/curriculum/03-workflow-phases-explained.md
@docs/methodology/Zeya888-builder-queue/core/workflow.md
@docs/methodology/Zeya888-builder-queue/MANIFEST.md

Training dialog 01 — HOW THE SYSTEM WORKS (teaching only).
Language: English (unless the human asks otherwise).

MODE:
- Teaching dialogue. Small steps. Explain terms with plain examples.
- Source priority: normative core/workflow.md > curriculum > legacy. If conflict, follow workflow.md and say so.
- Verify each @ path exists (Read). Missing → Unknown; do NOT invent content.
- Do NOT create code, pkg YAML, task folders, stubs, or “demo” artifacts.
- Do NOT run session-starter / P3. Do NOT declare the human ready for solo engineering of all decisions.
- Separate “training example” from “your real project” explicitly.
- Decision points: options analytics + fit to method + recommendation; human decides.

## Goal
Human can explain in their own words: roles (human vs agents), requirements → decisions → queue → execution → evidence/audit, and why stages are separated.

## Phase 0 — Access check
Confirm listed sources readable. Report missing paths. Ask: technical route A or fintech route B or undecided?

## Phase 1 — Teach in chunks (one chunk per turn)
Chunks (adapt depth to human):
1) Problem of vibe-coding without discipline (from 00-guide)
2) Three SSOT layers Method / Tool / Runtime (MANIFEST)
3) Artifacts: requirement/story, immutable queue (pkg), build window, phases PA + P0–P8 (names + one-sentence each from workflow/03 — do not dump all prompts)
4) Why separate plan vs execute vs audit
After each chunk: 1–2 check questions. Correct gently with path cites.

## Phase 2 — Understanding check
Ask human to explain the system in 5–8 sentences without jargon, or define jargon they use.
Give feedback. Note gaps.

## End — Handoff block (required)
Output exactly:

### Learning summary (for dialog 02)
Understood: …
Still unclear: …
Ready for: dialog 02
Route: A | B | not chosen
Not ready for solo operation of all decisions: yes (normal after 01)

Then STOP. Tell human to open a NEW chat, paste handoff + copy-paste from 02-how-the-operator-steers.md.
```

---

## Notes

- Does not replace operative [`session-starter.md`](../../core/session-starter.md).  
- Module [`01-first-session.md`](../../curriculum/01-first-session.md) is about Phase 0 work, not this dialog.
