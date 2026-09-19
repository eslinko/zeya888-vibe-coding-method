# Lightweight follow-up — author dual plans + LAUNCH (after triage PASS)

**Категория:** operator (VAL / docs author)  
**Guide SSOT:** [`../../guides/lightweight-followup.md`](../../guides/lightweight-followup.md)  
**Prerequisite:** [`lightweight-followup-triage.md`](./lightweight-followup-triage.md) verdict **PASS**  
**Sample shape:** observe note + landing `*-LAUNCH.md` (process only)  
**Claims:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | Triage PASS — нужны implement + validate + launch | Этот prompt → 3 artifacts |
| 2 | Handoff в Builder / обратно в Validator | LAUNCH copy-paste (+ optional thin Task) |

**Запрет:** запускать authoring после ESCALATE или без triage (unless operator explicitly waives triage **and** restates hard-fail checklist as clear — still fail closed on Unknown).

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/lightweight-followup.md
@docs/methodology/Zeya888-builder-queue/prompts/operator/lightweight-followup-triage.md
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml

builder_project: <key>
workspace_root: /Users/eslinko/Development/DOGEstonia
focus_role: validator

$slug=                 # e.g. landing-emergency-contacts-nav-links
$gap=
$triageVerdict=PASS    # must be PASS; paste triage HIT table if available
$touchList=            # operator-locked surfaces

Lightweight follow-up AUTHOR (dual plans + LAUNCH).
Prerequisite: triage PASS for this $gap. If not PASS → STOP.

MODE: write plans + launch only. No product code until BLD packet. No commit/push.
No new STORY / pkg / materialize.
Claims: verified as-is with paths before listing edits.

## Artifacts to create
1) .cursor/plans/$slug.plan.md
   - locks table; verified as-is; exact file touch list; OOS; prove todos
   - implement-only scope
2) .cursor/plans/$slug-validate.plan.md
   - validate-only; checks table must-PASS; optional smoke = N/A ok if server down
   - no product edits by default
3) {$focus_folder}/docs/tasks/prompts/$slug-LAUNCH.md
   - link both plans + analysis.mdc
   - §Copy-paste BLD implement (stop before validate)
   - §After implement → VAL validate packet
   - §Optional thin Task (below)

## Authoring rules
- Cite existing map/helpers (Grep/Read); do not invent components.
- Locales: list each file; labels/hrefs rules; no invent policy if operator locked strings.
- Separate implement vs validate plans (anti mega-plan).
- LAUNCH tells BLD: when implement PASS, stop.

## Optional thin Task / subagent (2B)
If operator wants Task instead of paste, put these two blocks in LAUNCH (one Task each):

### Task — BLD implement
description: Lightweight follow-up implement for $slug (builder_project=$builder_project). Attach analysis.mdc + implement plan only. Execute plan todos; ask-scoped; no STORY/pkg; no validate; no commit unless asked. Stop on implement PASS.
prompt: |
  @.cursor/rules/analysis.mdc
  @.cursor/plans/$slug.plan.md
  builder_project: $builder_project
  Implement the plan only. Mark todos. Stop before validate.

### Task — VAL validate
description: Lightweight follow-up validate for $slug. Attach analysis.mdc + validate plan only. PASS/FAIL with paths; no edits unless FAIL and operator says fix.
prompt: |
  @.cursor/rules/analysis.mdc
  @.cursor/plans/$slug-validate.plan.md
  builder_project: $builder_project
  Validate only per plan. Report PASS/FAIL with file evidence.

## End
Reply with paths created + short BLD packet preview. Do not start implement in this turn unless operator says «запиши в код» / implement now.
```

---

## Примечания

- Commit: separate wave via [`git-commit-prompt.md`](../../../git-commit-prompt.md); exclude `docs/analysis/**` unless asked.  
- Fixed `*_builder.plan.md`: not used for this track — ephemeral `$slug` plans only.
