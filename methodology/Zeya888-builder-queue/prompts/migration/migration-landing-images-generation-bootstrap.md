# Migration bootstrap — Landing images generation (universal)

**Категория:** migration (session restore + execution bootstrap for image wave)  
**Profiles SSOT:** [`../../specs/profiles.yaml`](../../specs/profiles.yaml)  
**Method SSOT:** [`../../core/workflow.md`](../../core/workflow.md)  
**Claims rule:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | Новый/сброшенный чат, нужно быстро запустить image wave только для landing | Вставить Copy-paste блок и задать `$imagesInput=` |
| 2 | Нужны trust/social glyphs и AI-ассеты в одной волне | Использовать обязательный split: Contour A (`icons:land-ui`) + Contour B (`GenerateImage`) |
| 3 | Нужно исключить смешение со SPA-стилем | Следовать hard bans и style fence из landing-доков |

**Scope lock:** только `builder_project: landing` и только `landing` paths.  
**Out of scope:** `spa-app` runtime outputs, cross-project image drop-ins, commits/push.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
@landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-style-prompts.md
@landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-assets.md
@landing/scripts/generate-land-lucide-icons.py
@landing/scripts/icons/land-image-manifest.yaml
@landing/package.json
@landing/docs/UX/references/DogeEstonia Character.png
@landing/docs/UX/references/floral-band-reference.png
@landing/docs/UX/references/skirt_ornament_reference.png
$imagesInput=

builder_project: landing
workspace_root: /Users/eslinko/Development/DOGEstonia

Migration bootstrap. Start Images generation dialog for landing only.

MODE: execution allowed, landing-only. No product code outside landing.
Claims: path-based only (Read/Glob/rg/Shell command outputs); else Unknown.
No assumptions, no invented AC, no invented filenames/paths.
No commits/push. No spa output paths for landing assets.

## Step 0 — Resolve profile and prechecks
1) Resolve `landing` from profiles.yaml:
   - focus_folder, tasks_dir, plan_file, pipeline_doc, test_command, execution skill.
2) Read `$imagesInput` fully. If missing/unreadable -> STOP and ask.
3) For rows requiring refs, confirm required files exist on disk:
   - landing/docs/UX/references/DogeEstonia Character.png
   - landing/docs/UX/references/floral-band-reference.png
   - landing/docs/UX/references/skirt_ornament_reference.png
4) Optional gate before execution:
   - python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project landing --verify

## Step 1 — Classify work from `$imagesInput`
Build factual lists by `method`/row intent:
- NEW or regen trust/social glyphs (manifest-driven)
- NEW or regen AI/crop_or_ai assets (brand/mascot/scene/process/value)
- Reuse (must verify on disk)
- Skip/docs-only rows (must not generate binary)

Anti-dup: prefer existing delivered assets and catalog statuses over blind regeneration.

## Step 2 — Contour A (trust/social glyphs, default script path)
For entries meant for script pipeline (`lucide` / `social_svg`):
1) Verify/adjust row in `landing/scripts/icons/land-image-manifest.yaml` (`id`, `method`, `save_to`, source id).
2) Run from `landing`:
   - npm run icons:land-ui
3) QA facts:
   - PNG RGBA and expected size/padding from manifest defaults
   - output path matches `save_to`
   - visual consistency for trust/social set

Hard bans for Contour A:
- Do not use SPA `ic-*` pipeline for landing trust/social.
- Do not invent ids/files outside `$imagesInput` scope.

## Step 3 — Contour B (AI/crop_or_ai assets only)
Apply only to rows marked AI/crop_or_ai in `$imagesInput`:
1) Use `STORY-LAND-image-style-prompts.md`:
   - Global style + `style_type` lock + row-specific depict intent.
2) Attach refs when required by row/style:
   - character/logo continuity for mascot/brand
   - floral/skirt refs only where row intent requires them
3) Use `GenerateImage` for AI rows; for crop/logo adaptation follow row method and save target.
4) Save exactly to pinned `save_to` path under `landing`.
5) Verify alpha/existence/readability and style compliance against landing style fence.

Hard bans for Contour B:
- Do not use SPA icon SHARED LOCK for landing marketing art.
- Do not invent new brand variants, text, URLs, or CTA copy inside assets.

## Step 4 — Same-wave sync and report
1) If wave scope includes docs/index sync: update only factual ON DISK statuses.
2) Return only:
   - `$imagesInput` used
   - table: `id | method (land-ui|GenerateImage|crop_or_ai|reuse|skip) | path | exists yes/no`
   - manifest ids touched
   - refs used (character/floral/skirt/logo) + alpha check result
   - commands run (`icons:land-ui`, verification/QA commands)
   - blockers (if any), without invented substitutes

STOP conditions:
- Invalid/unreadable `$imagesInput`
- Missing required refs for a row that requires them
- Missing manifest/source id for Contour A row
```

---

## Примечания

- Landing style/runtime SSOT: [`../../../../landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-style-prompts.md`](../../../../landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-style-prompts.md), [`../../../../landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-assets.md`](../../../../landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-assets.md)
- As-is method context: [`../../analysis/retrospective-catalog-driven-image-generation-as-is-2026-08.md`](../../analysis/retrospective-catalog-driven-image-generation-as-is-2026-08.md)
- This prompt is landing migration bootstrap; not a SPA generation prompt.
