# Migration — Builder Queue profile from checked-out directory

**Категория:** migration (bootstrap new `builder_project`)  
**Guide SSOT:** [`../../guides/add-builder-profile.md`](../../guides/add-builder-profile.md)  
**Materialize (half B):** [`migration-add-builder-profile.md`](./migration-add-builder-profile.md)  
**Intake template:** [`../../specs/profile-intakes/_TEMPLATE.yaml`](../../specs/profile-intakes/_TEMPLATE.yaml)  
**Claims:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Instance shape (reference only):** [`.cursor/plans/zeya888-brand_profile_bootstrap.plan.md`](../../../../../.cursor/plans/zeya888-brand_profile_bootstrap.plan.md)

**Когда:** папка уже в workspace **или** задан `$git_repo` для clone в `$focus_folder`.  
**Не заменяет:** Phase 0 / P1–P8 product work; не пишет product code под `focus_folder/src`. Clone только если `$git_repo` непустой и **только по verb** («запиши» / «только intake»).

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | Код уже зачекаучен / склонирован в workspace; intake ещё нет | Этот prompt: inspect → intake → materialize |
| 2 | Alias ≠ имя папки (`spa` / `spa-app`, `zeya888-brand` / `zeya888`) | Явный `$profile_key` + `$focus_folder` |
| 3 | Пустой/почти пустой remote vs зелёный стек | Inspect → `stack_label` / skills; Unknown → minimal `test_command`, не invent skills |
| 4 | Intake YAML уже лежит в `profile-intakes/` (pending) | **Не этот prompt** → [`migration-add-builder-profile.md`](./migration-add-builder-profile.md) |
| 5 | Нужен checkout из git | `$git_repo` (+ опц. `$git_branch`) → clone в `$focus_folder` по verb → inspect → intake → materialize |

**`$focus_folder`:** если `$git_repo` пуст — имя уже существующей директории под `workspace_root`; если `$git_repo` задан — путь, **куда** чекаутить.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/add-builder-profile.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-add-builder-profile.md
@docs/methodology/Zeya888-builder-queue/specs/profile-intakes/_TEMPLATE.yaml
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
@docs/methodology/Zeya888-builder-queue/specs/profiles-fields.md
@docs/methodology/Zeya888-builder-queue/specs/input-package-spec.md
@docs/methodology/Zeya888-builder-queue/tools/workflow-console.html
@.cursor/plans/Gateway_builder.plan.md

$profile_key=
$focus_folder=
$git_repo=
$git_branch=
$plan_title_case=
$display_name=
$default_input_kind=
$has_ux_pipeline=false

Migration: profile from checked-out dir or $git_repo clone (inspect → intake → materialize).
workspace_root: /Users/eslinko/Development/DOGEstonia

MODE: plan-only until explicit operator verb.
Verbs:
  «запиши» / «materialize» → optional clone (if $git_repo) + write pending intake
                                 (+ optional thin instance plan) AND full materialize (guide §1).
  «только intake» / «prep only» → optional clone (if $git_repo) + stop after intake
                                 + optional instance plan (no profiles.yaml / console / Gateway clone yet).
Do NOT: edit files / clone before verb; Build / Execute plan on *_builder.plan.md;
      invent HTTP/AC/product stories; commit docs/tasks/** or push;
      invent dates (use --print-utc-now for pkg created_at);
      leave intake pending after ok verify.
$git_repo empty → $focus_folder must already exist under workspace_root.
$git_repo non-empty → clone into $focus_folder on verb (not in plan-only).
Claims: Read/Grep with path under $focus_folder (after path exists); else Unknown.
Checklist SSOT: guides/add-builder-profile.md §1. Do not fork the 13 steps —
delegate materialize to migration-add-builder-profile / guide §1.

## Step 0 — Preconditions
Required: $profile_key, $focus_folder. Missing either → STOP + ask.
$path = {workspace_root}/{$focus_folder}

If $git_repo is empty:
  Verify $path exists. Missing → STOP + ask (clone first or set $git_repo).
If $git_repo is non-empty:
  $focus_folder = checkout target (may be missing now).
  Plan will clone $git_repo → $path on verb.
  If $path already exists with .git → report remote/branch (Read); do NOT re-clone
    unless operator orders wipe/redo; conflicting non-git content → STOP + ask.
  If $git_branch set → after clone: checkout that branch (create local tracking if needed).
  If $git_branch empty → leave clone on remote default branch.

If specs/profile-intakes/done/$profile_key.yaml exists → STOP (already materialized)
  unless operator orders redo.
If specs/profile-intakes/$profile_key.yaml (pending) already exists →
  STOP and hand off to migration-add-builder-profile (intake already written).
If profile_key already in profiles.yaml enabled → STOP + ask (reuse vs overwrite).

## Step 1 — Inspect (chat evidence)
Only after $path exists. If plan-only and $git_repo set and $path missing:
  table «pending clone» ($git_repo → $focus_folder [@$git_branch|default]);
  stack_label Unknown until verb; do not invent stack from URL alone.
When $path exists — Read real files under $focus_folder (cite paths):
  README*, package.json, composer.json, pyproject.toml, go.mod, Cargo.toml,
  Dockerfile, .nvmrc, lockfiles, existing docs/tasks/ if any.
Derive candidates:
  | Field | Value | Evidence path |
  stack_label, test_command, execution_skill_* (omit if Unknown),
  default_input_kind hint (empty/docs-heavy → backlog_story; ask if unclear),
  plan_title_case (use $plan_title_case if set; else TitleCase($profile_key)).
Empty repo / no stack markers → stack_label: Unknown;
  test_command: "cd {$focus_folder} && ls"; do NOT invent skills.
Optional: note pattern docs/analysis/{key}-profile-prep-YYYY-MM-DD.md (plan-only until verb).

## Step 2 — Derived table (chat)
Same columns as migration-add-builder-profile Step 1 / guide §0 Derived defaults:
tasks_dir, plan_file, pipeline_doc, active_packages_dir, current_pointer,
build_windows_subdir, build_window_prefix, next_readme_dotfile, pkg_path_prefix,
input_package_yaml_key, artifact_kind, build_window_title, operator_contract,
TitleCase plan filename, has_ux_pipeline, stack/test/skills from Step 1.
Apply optional overrides from operator vars ($display_name note-only;
$default_input_kind; $has_ux_pipeline).
Note $git_repo / $git_branch in plan summary when set (not intake YAML fields).

## Step 3 — Plan file list (chat only)
List every path for:
  A) Prep: specs/profile-intakes/{profile_key}.yaml;
     optional .cursor/plans/{profile_key}_profile_bootstrap.plan.md (instance);
     optional docs/analysis/{key}-profile-prep-*.md
     + clone target $path when $git_repo set
  B) Materialize: same list as migration-add-builder-profile Step 2
     (profiles.yaml, console, tasks SSOT, contract, *_builder.plan.md,
      propagation, VERSION/CHANGELOG).

## End of plan reply
Handoff: none until verb.
Reply: preconditions + (inspect evidence or pending-clone note) + derived table
+ file list (A+B) + clarifying questions.
Do not write / clone until «запиши» / «только intake».

## On «только intake» / «prep only»
0) If $git_repo non-empty and clone needed (path missing or operator-ordered redo):
   git clone $git_repo $path
   if $git_branch non-empty → checkout $git_branch
   Do not invent product commits; empty remote OK (stack Unknown).
1) Inspect $path (Step 1).
2) Write pending intake from _TEMPLATE + derived overrides
   → specs/profile-intakes/{profile_key}.yaml (NOT done/).
3) Optional thin instance plan:
   .cursor/plans/{profile_key}_profile_bootstrap.plan.md
   (shape like zeya888-brand_profile_bootstrap: derived table, STOP, copy-paste
    pointing at migration-add-builder-profile).
4) Optional analysis note under docs/analysis/.
5) STOP. Tell operator: next paste migration-add-builder-profile with this intake,
   or say «запиши» / «materialize» in this chat to continue.
   If cloned: one line «Cloned $git_repo → $focus_folder [@$git_branch|default]».

## On «запиши» / «materialize»
0) If $git_repo non-empty and clone needed (path missing or operator-ordered redo):
   git clone $git_repo $path
   if $git_branch non-empty → checkout $git_branch
   Do not invent product commits; empty remote OK (stack Unknown).
1) Inspect $path (Step 1) if not already done after clone.
2) Write pending intake (and optional instance plan / analysis note) if not yet written.
3) Execute materialize checklist from @migration-add-builder-profile.md /
   guides/add-builder-profile.md §1 (all steps including Gateway clone §2,
   --project {profile_key} --verify, VERSION/CHANGELOG, intake → done/).
4) Never Build on *_builder.plan.md.
5) Do not commit unless operator asked.

Handoff after ok verify:
«Profile {profile_key} ready from checked-out {focus_folder}.
 Next: new chat builder_project: {profile_key} + Phase 0 (@session-starter.md).
 Verify: ok N paths. Intake archived under profile-intakes/done/.»
If cloned this wave: «Cloned $git_repo → $focus_folder [@$git_branch|default].»
```

---

## Примечания (не в copy-paste)

- **Gap this fills:** `migration-add-builder-profile` assumes intake already on disk; this wrapper adds optional `$git_repo` clone + inspect + intake authoring.
- **Prep reference:** [`docs/analysis/zeya888-brand-profile-prep-2026-09-18.md`](../../../../../docs/analysis/zeya888-brand-profile-prep-2026-09-18.md) (optional analysis note pattern).
- **Reusable methodology plan (system, not instance):** [`.cursor/plans/Zeya888_profile_bootstrap.plan.md`](../../../../../.cursor/plans/Zeya888_profile_bootstrap.plan.md) / [`.cursor/plans/add_builder_profile.plan.md`](../../../../../.cursor/plans/add_builder_profile.plan.md).
- **Out of scope:** `CLI --scaffold-profile`; inventing STORY/AC; writing `$git_repo` into intake YAML (prompt var only).
- Bootstrap pkg образец: `scripts/docs/tasks/scripts-active-packages/pkg-bootstrap-pending.yaml`.
