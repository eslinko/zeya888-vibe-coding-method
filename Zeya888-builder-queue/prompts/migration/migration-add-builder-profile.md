# Migration — add Builder Queue profile from intake

**Категория:** migration (bootstrap new `builder_project`)  
**Guide SSOT:** [`../../guides/add-builder-profile.md`](../../guides/add-builder-profile.md)  
**Intake SSOT:** [`../../specs/profile-intakes/`](../../specs/profile-intakes/)  
**Claims:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Не заменяет:** Phase 0 / P1–P8 product work; не пишет product code под `focus_folder/src`

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | Новый проект в monorepo — нужен профиль Builder Queue с нуля | Intake YAML → этот prompt → materialize |
| 2 | Alias ≠ имя папки (`spa` / `spa-app`) | `profile_key` + явный `focus_folder` в intake |
| 3 | Split от существующего профиля | intake `source_profile` / `source_split` + guide §5 |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/add-builder-profile.md
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
@docs/methodology/Zeya888-builder-queue/specs/profiles-fields.md
@docs/methodology/Zeya888-builder-queue/specs/input-package-spec.md
@docs/methodology/Zeya888-builder-queue/tools/workflow-console.html
@.cursor/plans/Gateway_builder.plan.md
@docs/methodology/Zeya888-builder-queue/specs/profile-intakes/<profile_key>.yaml

$profile_key=
$focus_folder=

Migration: add Builder Queue profile from intake (plan → materialize).
workspace_root: /Users/eslinko/Development/DOGEstonia

MODE: plan-only until explicit «запиши» / «materialize».
Do NOT: edit files until materialize; Build / Execute plan on *_builder.plan.md;
      invent HTTP/AC/product stories; commit docs/tasks/** or push;
      invent dates (use --print-utc-now for pkg created_at);
      leave intake in pending after successful verify.
Claims: Read/Grep with path; else Unknown.
Checklist SSOT: guides/add-builder-profile.md §1 (all 13 steps). Gateway clone: guide §2.

## Step 0 — Load intake
Read @specs/profile-intakes/<profile_key>.yaml.
Required: profile_key, focus_folder. Missing either → STOP + ask.
If file is under profile-intakes/done/ → STOP (already materialized) unless operator orders redo.
If profile_key already exists in profiles.yaml enabled → STOP + ask (reuse vs overwrite).
Verify focus_folder exists on disk (or ask operator to create empty project root first).

## Step 1 — Derive (chat table)
From intake + guide §0 Derived defaults:
| Field | Value | Source (intake \| derived) |
Include: tasks_dir, plan_file, pipeline_doc, active_packages_dir, current_pointer,
build_windows_subdir, build_window_prefix, next_readme_dotfile, pkg_path_prefix,
input_package_yaml_key, artifact_kind, build_window_title, operator_contract path,
TitleCase plan filename (respect plan_title_case override), has_ux_pipeline for console.
Apply optional overrides from intake (stack_label, skills, test_command, default_input_kind,
source_profile, source_split).

## Step 2 — Plan file list (chat only)
Enumerate every path that materialize will create or edit (profiles.yaml, console,
tasks SSOT files, contract, *_builder.plan.md, propagation touchpoints, VERSION/CHANGELOG).
If source_profile set — list split steps from guide §5.

## End of plan reply
Handoff: none until materialize.
Reply: derived table + file list + clarifying questions only.
Do not start writing until «запиши».

## Materialize (только по «запиши»)
Execute guide §1 Checklist in order:

1) Intake already on disk (this file).
2) profiles.yaml — projects.{profile_key} enabled: true; derived + overrides.
3) input-package-spec.md §2 — add row for profile_key (tasks_dir, pointer, active-packages).
4) workflow-console.html — BUILDER_PROJECTS + PROJECT_PROFILES.{profile_key} (fields 1:1 YAML);
   hasUxPipeline from intake has_ux_pipeline (default false); bump console version pill.
5) Tasks SSOT under {focus_folder}/docs/tasks/:
   - {key}-active-packages/pkg-bootstrap-pending.yaml
     (schema like scripts pkg-bootstrap-pending; activation: none;
      created_at from --print-utc-now; tasks_root = pkg_path_prefix; linear_paths: [])
   - {key}-active-package.current.yaml → that package_file
   - bullrun-launch-index.md (bootstrap §Актуальная точка → pending pkg)
   - backlog-stories/INDEX.md
   - {key}-story-execution-pipeline.md (minimal stub pointing to workflow P1–P8)
   - run-reports/{key}-build-windows/README.md
6) Split if source_profile — guide §5.
7) contracts/{key}-operator-contract.md — thin clone scripts/landing/zeya888 contract shape;
   resolve-start-from-index + sync-index + fixed plan @attach rule; no invent AC.
8) .cursor/plans/{TitleCase}_builder.plan.md — FULL Gateway structural clone (guide §2);
   substitute paths; §Шаг 0 must match live --verify after step 10.
9) Thin propagation only where profile keys are already listed:
   workflow.md §profiles / session-starter.md / queue-manual.md / MANIFEST.md /
   builder-session SKILL.md / builder-operator-habits.mdc.
10) From workspace root:
    python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project {profile_key} --verify
    FAIL → stop and fix; do not move intake.
11) Bump docs/methodology/Zeya888-builder-queue/VERSION + CHANGELOG entry for this profile.
12) Never Build on *_builder.plan.md.
13) Do not commit unless operator asked.

14) Move intake:
    specs/profile-intakes/{profile_key}.yaml → specs/profile-intakes/done/{profile_key}.yaml

Handoff after ok verify:
«Profile {profile_key} ready. Next: new chat builder_project: {profile_key} + Phase 0
(@session-starter.md). Verify: ok N paths. Intake archived under profile-intakes/done/.»
```

---

## Примечания (не в copy-paste)

- Folder already present, **no intake yet** → [`migration-profile-from-checked-out-dir.md`](./migration-profile-from-checked-out-dir.md) (inspect → write intake → then this prompt / guide §1).
- Template: [`../../specs/profile-intakes/_TEMPLATE.yaml`](../../specs/profile-intakes/_TEMPLATE.yaml).
- Sample teaching profile (not intake): [`../../examples/sample-profiles/minimal.yaml`](../../examples/sample-profiles/minimal.yaml).
- Bootstrap pkg образец: `scripts/docs/tasks/scripts-active-packages/pkg-bootstrap-pending.yaml`.
- CLI scaffold (`--scaffold-profile`) — **не** этот prompt; отдельный этап.
