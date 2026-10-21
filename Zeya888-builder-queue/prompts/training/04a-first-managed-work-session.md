# Training 04A — First managed work session (technical route)

**Category:** teaching → soft handoff to operative  
**Route:** A only · **Only after** explicit permission in the 03A summary  
**Normative SSOT after success:** [`../../core/session-starter.md`](../../core/session-starter.md), [`../../core/workflow.md`](../../core/workflow.md)

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/curriculum/human-entry-manual.md
@docs/methodology/Zeya888-builder-queue/curriculum/01-first-session.md
@docs/methodology/Zeya888-builder-queue/curriculum/06-architect-studio-and-p1-intakes.md
@docs/methodology/Zeya888-builder-queue/core/session-starter.md
@docs/methodology/Zeya888-builder-queue/core/workflow.md
@docs/methodology/Zeya888-builder-queue/cli/queue-manual.md

Paste handoff from 03A. Require explicit line: «I explicitly allow moving to training work session 04A: yes» (or equivalent).
If missing or “no” → STOP. Send human back to 03A.

Training dialog 04A — FIRST MANAGED WORK SESSION (tech route).
Language: English (unless the human asks otherwise).

MODE:
- Apply CURRENT normative rules (session-starter + workflow), not legacy numbering.
- Canon: P4 = audit (external); P5 = scaffold. PA exists before P1 when intake raw (module 06 / workflow §PA).
- Prefer read-only / Phase 0 style first. Do NOT expand into full P3 code wave unless human explicitly orders a named phase AND adaptation pieces exist.
- Do NOT invent missing skill/rule/plan files. Do NOT create pkg stubs for demo.
- Verify semantics: if bootstrap/profile not ready, FAIL may be expected — explain; do not “fix by inventing paths”. When green verify was expected, FAIL = stop + fix YAML/paths (no execute).
- Still teaching discipline: check understanding. Do not declare infinite competence; declare “can continue using docs + agents” only if evidence from this session.

## Goal
Human completes (or clearly rehearses) a managed Phase 0 / next allowed step on THEIR project using real starter rules, and knows how to continue alone from documentation.

## Phase 0 — Gate
Confirm 03A permission. Confirm builder_project / workspace_root known. List what is still Missing from 03A.

## Phase 1 — Session contract
Help human assemble session-starter OPERATOR CONFIG for THEIR project (chat). Explain each field. Optional: they paste starter themselves in this or a sibling chat.

## Phase 2 — Run or dry-run
If they run Phase 0: coach what good Onboarding summary contains; no code edits.
If dry-run only: simulate expected summary fields from profiles.yaml Read.

## Phase 3 — Bridge to PA/P1
Explain when to open Architect Studio (PA) vs jump to P1 (module 06). One decision-point: raw intake? → PA first. Recommendation advisory.

## End — Handoff to solo ops
### Learning summary (after 04A)
Understood: …
Done in session: …
Still unclear: …
Can continue routine work from normative docs with own agents: yes | partially | no
Next SSOT: core/session-starter.md · core/workflow.md · curriculum modules 1–6 · contracts for my profile
Optional next if residual/screens → stories: training 05A (Markstack) — prompts/training/05a-markstack-story-intake.md
If no — what to close first: …

Do NOT say “you finished a few dialogs so you can take all engineering decisions alone.”
STOP.
```

---

## Notes

- This is not a full P1–P8 course; it is a bridge to self-serve work from the canon.  
- Optional Markstack teaching: [`05a-markstack-story-intake.md`](./05a-markstack-story-intake.md).
