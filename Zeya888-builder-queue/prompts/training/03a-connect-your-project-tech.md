# Training 03A — Connect your project (technical route)

**Category:** teaching · **Route:** A only  
**Input:** summary from dialog 02 with route A  
**Next:** [`04a-first-managed-work-session.md`](./04a-first-managed-work-session.md) after explicit go-ahead

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/curriculum/human-entry-manual.md
@docs/methodology/Zeya888-builder-queue/curriculum/05-connect-your-project.md
@docs/methodology/Zeya888-builder-queue/curriculum/04-cli-and-contracts-explained.md
@docs/methodology/Zeya888-builder-queue/integration/cursor-setup.md
@docs/methodology/Zeya888-builder-queue/guides/add-builder-profile.md
@docs/methodology/Zeya888-builder-queue/guides/client-tenancy.md
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
@docs/methodology/Zeya888-builder-queue/specs/profiles-fields.md
@docs/methodology/Zeya888-builder-queue/specs/clients.yaml
@docs/methodology/Zeya888-builder-queue/examples/sample-profiles/minimal.yaml

Paste handoff from dialog 02 (route A) above.

Training dialog 03A — CONNECT YOUR PROJECT (tech route, teaching + adaptation PLAN only).
Language: English (unless the human asks otherwise).

MODE:
- Teach delivery composition + adaptation plan for THEIR repo.
- Read their repo only if they give path / @ project roots. Missing → ask; do not invent stack.
- Do NOT create profile YAML, builder plan, pkg, code, or stubs “so paths exist” unless human explicitly says «запиши» / “write it” AND this is still teaching-plan only — default = chat plan only, no disk writes.
- Default this dialog: **plan in chat only**. No materialize.
- Explain verify: bootstrap FAIL can be normal before first real pkg; FAIL=stop applies in execution sessions when green verify was expected (cite curriculum/04 + session-starter). See cursor-setup “Delivery composition”.
- Normative > teaching. Unknown if deps missing from disk — point to add-builder-profile, do not fabricate skill/rule bodies.

## Goal
Verified adaptation plan: what to place where; profile fields; readiness criteria; how they will run the cycle alone later. Not “fully configured production” unless already true on disk.

## Phase 0
Confirm sources + handoff. Ask workspace path and project name.

## Phase 1 — Delivery map
Explain what lives in methodology package vs workspace (.cursor/skills, .cursor/rules, *_builder.plan.md) per cursor-setup. Check which pieces exist (Read/Glob). Table: present | missing | how to obtain (guide path).

## Phase 2 — Profile & readiness
Walk add-builder-profile / profiles-fields at human pace. Ask: flat peer at workspace root vs nested client under `clients/<Client>/`? If nested → also walk client-tenancy + clients.yaml (portable plans, `$clientId` ≠ `builder_project`). Draft checklist of readiness criteria (verify path, contract, plan file naming). Still chat-only.

## Phase 3 — Understanding check
Human restates the adaptation plan in their words. Correct with paths.

## End — Handoff
### Learning summary (for 04A)
Understood: …
Still unclear: …
Adaptation plan (short): …
Already on disk: … | Missing: …
I explicitly allow moving to training work session 04A: yes | no | later
Ready for routine solo ops after 04A: not yet / partially / yes (only with evidence)

If “yes” on 04A permission → tell them next file 04a. Else STOP and wait.
```

---

## Notes

- Related module: [`05-connect-your-project.md`](../../curriculum/05-connect-your-project.md).
