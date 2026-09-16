# Connecting Zeya888 Builder Queue to Cursor

**Human entry (learning):** [`../curriculum/human-entry-manual.md`](../curriculum/human-entry-manual.md) · tech dialog: [`../prompts/training/03a-connect-your-project-tech.md`](../prompts/training/03a-connect-your-project-tech.md)

## 0. Delivery composition (what lives where)

| Component | Usual location | In methodology package? | If missing on disk |
|-----------|----------------|-------------------------|--------------------|
| Method docs + CLI + specs + curriculum + training prompts | `docs/methodology/Zeya888-builder-queue/` | **Yes** | Copy/symlink the folder |
| Operator contracts, templates | inside methodology | **Yes** | — |
| Cursor skill | `.cursor/skills/builder-session/SKILL.md` (workspace) | **No** (workspace) | Restore from your mirror / DOGEstonia-style layout; do not invent the skill body |
| Cursor rule | `.cursor/rules/builder-operator-habits.mdc` (+ `analysis.mdc`) | **No** (workspace) | Same |
| Runtime builder plan | `.cursor/plans/*_builder.plan.md` | **No** — you create from template | [`../templates/builder-plan-template.md`](../templates/builder-plan-template.md) + [`../guides/add-builder-profile.md`](../guides/add-builder-profile.md) |
| Profile row | `specs/profiles.yaml` (in methodology) or your own file | Partial | Intake → add-builder-profile |

Do not invent missing binaries or “hidden” dependencies: follow guides on disk; gap → Unknown.

## 1. Methodology in the workspace

Copy or symlink:

```
docs/methodology/Zeya888-builder-queue/
```

## 2. Skill (recommended)

File: [`.cursor/skills/builder-session/SKILL.md`](../../../.cursor/skills/builder-session/SKILL.md)

Triggers: `builder_project`, `pkg-`, build window, `Gateway_builder`, `GPT_builder`, `ID_builder`, `Capybara_builder`.

## 3. Rule

File: [`.cursor/rules/builder-operator-habits.mdc`](../../../.cursor/rules/builder-operator-habits.mdc)

## 4. Builder plan (runtime)

Create `.cursor/plans/YourProject_builder.plan.md` from [`../templates/builder-plan-template.md`](../templates/builder-plan-template.md).

## 5. profiles.yaml

**SSOT:** [`../guides/add-builder-profile.md`](../guides/add-builder-profile.md) — Intake Form, Checklist, Gateway clone for `*_builder.plan.md`, operative prompt.

Add a profile to [`../specs/profiles.yaml`](../specs/profiles.yaml) or create a separate file for your repo (copy [`../examples/sample-profiles/minimal.yaml`](../examples/sample-profiles/minimal.yaml)).

Fields — [`../specs/profiles-fields.md`](../specs/profiles-fields.md).

## 6. Session start

```
@docs/methodology/Zeya888-builder-queue/core/session-starter.md

builder_project: your_project
workspace_root: /path/to/repo
pipeline_profile: builder_full
```

**Fixed builder plans:** do not use the Build button on `*_builder.plan.md` — see [fixed-builder-plan-execution.md](../guides/fixed-builder-plan-execution.md).

## 7. Verify path

The CLI finds the workspace root by presence of:

`docs/methodology/Zeya888-builder-queue/specs/profiles.yaml`

If the methodology lives elsewhere — update `_repo_root()` in `builder_resolve_queue.py` or keep a compatible directory layout.

**FAIL during bootstrap:** may be normal before the first pkg — see [`../curriculum/04-cli-and-contracts-explained.md`](../curriculum/04-cli-and-contracts-explained.md) §Verify.
