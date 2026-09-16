# Migration bootstrap — SPA images generation (universal)

**Категория:** migration (session restore + execution bootstrap for image wave)  
**Profiles SSOT:** [`../../specs/profiles.yaml`](../../specs/profiles.yaml)  
**Method SSOT:** [`../../core/workflow.md`](../../core/workflow.md)  
**Claims rule:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | Новый/сброшенный чат, нужно быстро запустить image wave только для SPA | Вставить Copy-paste блок и задать `$imagesInput=` |
| 2 | Нужны functional `ic-*` и mascot в одной волне | Использовать обязательный split: Contour A (Lucide) + Contour B (GenerateImage) |
| 3 | Нужно исключить смешение с landing-стилем | Следовать hard bans и style fence из SPA-доков |

**Scope lock:** только `builder_project: spa` и только `spa-app` paths.  
**Out of scope:** `landing` runtime outputs, cross-project image drop-ins, commits/push.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
@spa-app/docs/UX/SPA-CATALOG-IMAGE-WAVE.md
@spa-app/docs/UX/SPA-ICON-STYLE-PROMPTS.md
@spa-app/docs/UX/references/DogeEstonia Character.png
@spa-app/docs/UX/references/floral-band-reference.png
@spa-app/scripts/generate-icons-from-lucide.py
@spa-app/scripts/icons/icon-manifest.yaml
@spa-app/docs/tasks/backlog-stories/icons/ICON-GENERATION-INDEX.md
$imagesInput=

builder_project: spa
workspace_root: /Users/eslinko/Development/DOGEstonia

Migration bootstrap. Start Images generation dialog for spa-app only.

MODE: execution allowed, SPA-only. No product code outside spa-app.
Claims: path-based only (Read/Glob/rg/Shell command outputs); else Unknown.
No assumptions, no invented AC, no invented filenames/paths.
No commits/push. No landing output paths for spa functional icons.

## Step 0 — Resolve profile and prechecks
1) Resolve `spa` from profiles.yaml:
   - focus_folder, tasks_dir, plan_file, pipeline_doc, test_command, execution skill.
2) Confirm required refs exist:
   - spa-app/docs/UX/references/DogeEstonia Character.png
   - spa-app/docs/UX/references/floral-band-reference.png
3) Read `$imagesInput` fully. If missing/unreadable -> STOP and ask.
4) Optional gate before execution:
   - python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project spa --verify

## Step 1 — Classify work from `$imagesInput`
Build factual lists:
- NEW functional `ic-*`
- NEW mascot/illustration assets
- Reuse (must verify on disk)
- Skip / Viz / docs-only (must not generate PNG)

Anti-dup: prefer catalog Reuse + ICON-GENERATION-INDEX over regeneration.

## Step 2 — Contour A (functional `ic-*`, default path)
For each NEW functional icon:
1) Pick `lucide_id` from catalog hints/peers; verify icon exists in lucide-static.
2) Update `spa-app/scripts/icons/icon-manifest.yaml` row (`catalog`, `file`, `out_dir`, `lucide_id`, `color`).
3) If needed, align catalog alias in `generate-icons-from-lucide.py` (e.g. `es`).
4) Run from `spa-app`:
   - npm run icons:generate
   - npm run icons:validate
   - or targeted generate by catalog/file when wave requires narrow scope
5) QA facts:
   - PNG RGBA 256x256
   - transparent background/corners
   - optical consistency with SPA peers from SPA-ICON-STYLE-PROMPTS

Hard bans for Contour A:
- Do not use landing SHARED LOCK style.
- Do not generate Viz/device chrome/folk ETM as `ic-*`.
- Do not invent extra files beyond catalog NEW rows.

## Step 3 — Contour B (mascot/illustration only)
Apply only to NEW mascot/illustration rows from `$imagesInput`:
1) Use GenerateImage with `reference_image_paths` including:
   - spa-app/docs/UX/references/DogeEstonia Character.png
2) Keep character continuity (same face/cap/palette/proportions).
3) Save exactly to pinned catalog path under `spa-app`.
4) Verify real alpha (no opaque plate), existence and readability on dark SPA UI context.

Hard bans for Contour B:
- Do not redraw a second doge identity.
- Do not reuse this contour for functional `ic-*`.

## Step 4 — Same-wave sync and report
1) If wave scope includes docs/index sync: update only factual ON DISK statuses.
2) Return only:
   - `$imagesInput` used
   - table: `file | method (Lucide|GenerateImage|reuse|skip) | path | exists yes/no`
   - manifest catalog keys touched
   - mascot continuity refs used + alpha check result
   - commands run (`icons:generate`, `icons:validate`, targeted commands)
   - blockers (if any), without invented substitutes

STOP conditions:
- Missing required refs
- Invalid/unreadable `$imagesInput`
- Missing lucide id for a functional NEW row (unless operator explicitly allows GenerateImage exception)
```

---

## Примечания

- Execution split and style fences: [`../../../../spa-app/docs/UX/SPA-CATALOG-IMAGE-WAVE.md`](../../../../spa-app/docs/UX/SPA-CATALOG-IMAGE-WAVE.md), [`../../../../spa-app/docs/UX/SPA-ICON-STYLE-PROMPTS.md`](../../../../spa-app/docs/UX/SPA-ICON-STYLE-PROMPTS.md)
- As-is method context: [`../../analysis/retrospective-catalog-driven-image-generation-as-is-2026-08.md`](../../analysis/retrospective-catalog-driven-image-generation-as-is-2026-08.md)
- This prompt is SPA migration bootstrap; not a landing generation prompt.
