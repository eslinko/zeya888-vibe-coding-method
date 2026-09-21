# Requirement → FE mixed package (ADMIN + STORY)

**Категория:** architect (post-PA.2 / pre-P1.3)  
**Не заменяет:** выполнение ADMIN «Выполни…» / PA.3 / P1.3  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

**Когда:** `spa` / `landing` / `capybara` — **одно** per-project requirement, в котором могут быть и visual surfaces (артборды / мокапы), и технические срезы без мокапов. Нужны **ADMIN-01…06 и продуктовые STORY-*** в одном пакете.

**Не использовать:**
- все срезы `tech_first` (нет UI) → STOP, [`req-to-backlog-stories.md`](./req-to-backlog-stories.md);
- чистый UI и стори сознательно откладываются до мокапов → [`req-to-ui-admin-layers.md`](./req-to-ui-admin-layers.md) (ADMIN only; STORY через ADMIN-05).

**Advisory (не hard-STOP):** если REQ prefer SSR / `dist` start и Git-owned non-JS (schemas/assets via FS), а linked tech-architecture ещё нет — сначала [`req-to-target-tech-architecture.md`](./req-to-target-tech-architecture.md) (packaging seam — пакет тем того же промпта), затем этот промпт.

**Эталон структуры пакета:** `spa-app/docs/tasks/backlog-stories/early-signal-dashboard/INDEX.md` (Admin queue + Product stories).  
**Эталон структуры ADMIN-файла:** `public-home/ADMIN-PH-01…06` (Meta / Цель / Вход / Deliverable / Acceptance / Как выполнять).  
**Не эталон контента ADMIN:** заполненные `ADMIN-ESD-02/03/04` после мокапов M136–M140 — выход этого промпта = **до** intake (Expected projected + TODO).

**Подстановка (только это):**

| Поле | Значение |
|------|----------|
| `$requirementDoc=` | path REQ (напр. `spa-app/docs/requirements/15-early-signal-….md`) |
| `$builderProject=` | `spa` \| `landing` \| `capybara` |
| `$featureSlug=` | опц. короткий префикс (напр. `ES` → `ADMIN-ES-01-…`); пусто → вывести из REQ title в plan |

Пакет backlog **не** подаётся. **Всегда NEW** `…/backlog-stories/<slug>/`. Не reuse `public-home` / `early-signal-dashboard` / чужие пакеты.

**Канон слоёв (omit только с why в plan table):**

| # | Файл | Роль в этом промпте |
|---|------|---------------------|
| 0 | `PRODUCT-BRIEF.md` | locked brief из REQ |
| — | `INDEX.md` | Admin queue + Product stories (колонка orientation) |
| 01 | `ADMIN-{PREFIX}-01-product-ux-prompts.md` | UX prompts plan → later `UX-PROMPTS.md` |
| 02 | `ADMIN-…-02-ux-mockup-intake.md` | mockup intake plan (Spec/PNG TBD) |
| 03 | `ADMIN-…-03-icon-assets-catalog.md` | icon catalog plan (без выдуманных `ic-*`) |
| 04 | `ADMIN-…-04-api-requirements.md` | API needs vs verify (Unknown / sibling REQ) |
| 05 | `ADMIN-…-05-backlog-stories-l10n.md` | L10N + **refine** ui_first стори после мокапов (стори уже пишет Phase 3) |
| 06 | `ADMIN-…-06-tech-decomposition.md` | projected epic/wave/task sketch; no execute |

**Дефолт записи:** plan + полные drafts в чате; диск — только «запиши».

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
$requirementDoc=
$builderProject=
$featureSlug=

Requirement → FE mixed package (ADMIN + STORY). Plan mode.
@$requirementDoc
builder_project: $builderProject
feature_prefix: ADMIN-$featureSlug- (if $featureSlug empty — derive PREFIX from REQ title; show in plan)

MODE: plan-only. STOP after classification + layer plan + full drafts in chat.
Do NOT: edit files until «запиши»; create pkg / epic / task README / UX-PROMPTS.md;
      write STORY-*-icon-assets.md or STORY-*-api-requirements.md now;
      generate PNG mockups; invent mockup-NN / ic-* / gateway HTTP paths/fields
      (cite sibling REQ or Unknown + question);
      run P1.3/P3; propose «Выполни ADMIN-01» until operator go-ahead;
      ask operator for backlog package path; reuse existing packages
      (public-home, early-signal-dashboard, etc.).
Code claims: only after Read/Grep with path:line; else Unknown.

Etalon INDEX structure: spa-app/docs/tasks/backlog-stories/early-signal-dashboard/INDEX.md
  (Admin queue + Product stories). Content of ADMIN-ESD-02/03/04 after M136–M140
  is ANTI-etalon — do not copy filled mockup/icon/API tables.
Etalon ADMIN file shape: public-home/ADMIN-PH-* Meta/Goal/Input/Deliverable/Acceptance/Как выполнять.
Etalon ui_first story shape: STORY-SPA-ES-01 sections (Артборд/Иконки = projected TBD).
Etalon tech_first story shape: STORY-SPA-HL-02 (no Артборд; ui_scope: none).
Write into a NEW package only.

## Phase 0 — Package path (NEW, mandatory)
Proposed path: `{spa-app|landing|capybara}/docs/tasks/backlog-stories/<kebab-slug>/`
Slug from $featureSlug (expanded) or REQ title/id.
Why: ADMIN set + stories; always NEW; never reuse.
Table: | Decision | Path | Why |
Decision must be `new`. Override to existing path ONLY if operator explicitly orders in chat.

## Phase 1 — Classify slices (mandatory)
Из @$requirementDoc нарезать срезы. Таблица:
| Slice | REQ § | Has UI? (yes/no + REQ quote) | orientation (ui_first \| tech_first) | Why | STORY key | ADMIN layers that feed this slice |

Rules (no guessing; unclear → Unknown + question):
- ui_first / Has UI = yes: REQ names screen/route/composition/states/artboard/DOM;
  P3 will need Path A @mockup or UX brief. New visual surface stays ui_first even if API is involved.
- tech_first / Has UI = no: FE without new composition — consume API, env/bake, tests,
  l10n plumbing without a new screen, repository/service, regression of existing chrome.
  Text AC is enough. ui_scope: none.
- Package orientation: mixed (both kinds) or ui_only (all ui_first).
- If ALL slices tech_first → STOP. Tell operator to use req-to-backlog-stories.md. No drafts.

## Phase 2 — Layer plan
| Layer | Include? (yes / omit+why) | Skill | Depends | Blocks | Proposed filename |
01…06 + BRIEF + INDEX. Default = all six ADMIN; omit only with explicit why (e.g. no new icons).
If package is ui_only, still include 01–03 (visual pipeline). Do not omit 01–03 when any ui_first slice exists.

ADMIN-05 does NOT create STORY files (Phase 3 already does). Layer 05 = L10N conventions
+ later fill of ui_first projected sections after mockups.
ADMIN-06 = projected epic/wave/task sketch only; no folders, no execute.

Proposed $dashboardFile delta:
  spa → spa-mvp-dashboard.md; landing → landing-mvp-dashboard.md; capybara → capybara-mvp-dashboard.md.
By package = NEW path.
Remaining = ADMIN keys Todo + ui_first Draft (blocked on ADMIN-02) + tech_first Todo.
Do not count ui_first as P1.3-ready.
§Now = package path + next ADMIN-01 (and note tech_first may P1.3 separately).
Canon: docs/methodology/Zeya888-builder-queue/workflow/backlog-dashboard-maintenance.md
Dashboard edit only on «запиши».

## Phase 3 — Drafts in chat
Full markdown for:
1) PRODUCT-BRIEF.md (from REQ; locked intent; out of scope; parent/sibling REQ links;
   list planned STORY keys with orientation)
2) INDEX.md — two queues:
   Admin queue (01…06 Status Todo);
   Product stories (key | file | orientation | status Draft/Todo | Blocked-on)
3) Each included ADMIN-0N (complete plan file). Status Todo.
   Every layer that later fills from mockups/code MUST contain:
   - ## Expected projected content
     (what the future deliverable will look like; not claims of files that do not exist.
      ADMIN-02: target dir `{focus}/docs/UX/mockups/<kebab-slug>/`;
      table Artboard | Future story | Spec TBD | PNG TBD — no mockup-NN unless file exists on disk.
      ADMIN-03: catalog filename + public/icons/<slug>/ convention; no invented ic-* from missing artboards.
      ADMIN-04: needs table from REQ; verify Read/Grep or Unknown; no invented HTTP.)
   - ## TODO (layer execution)
     checklist for later «Выполни ADMIN-0N» — do not claim deliverables exist.
4) Each product STORY-*.md:
   - ui_first: Meta (orientation: ui_first; ui_scope: visual|mixed; Status Draft;
     Blocked-on: ADMIN-02 mockups; parent REQ); Зачем; FR/AC from REQ; Вне scope;
     §Артборд / §Иконки / §L10N = Expected projected + TODO; no invented mockup paths.
   - tech_first: full draft like non-UI backlog story (Meta, Scope, verified state or Unknown,
     AC from REQ, точки в коде if known, deps); ui_scope: none; no Артборд.

Do NOT draft UX-PROMPTS.md, mockup specs, icon-catalog STORY, api-requirements STORY.

## End of plan reply
Handoff: none until materialize.
Reply ends with: Phase 0 path + classification table + package orientation + layer plan
+ drafts + proposed INDEX/dashboard delta + clarifying questions only.
Do not suggest executing ADMIN layers until operator go-ahead.
Do not suggest P1.3 for ui_first until ADMIN-02 closed.
tech_first P1.3: mention as allowed after materialize, separate wave, only if operator go-ahead.

## Materialize (только по «запиши»)
1) Create the NEW package directory from Phase 0.
2) Write PRODUCT-BRIEF.md, INDEX.md, included ADMIN-*.md, and each product STORY-*.md.
3) If root backlog-stories/INDEX.md exists — add package pointer row.
4) Sync $dashboardFile: By package, Remaining (ADMIN Todo + ui_first Draft blocked + tech_first Todo),
   §Now, Updated/Last change — recount from disk
   ([backlog-dashboard-maintenance.md](../../workflow/backlog-dashboard-maintenance.md)).
5) Do NOT write UX-PROMPTS.md, mockup spec/PNG, STORY-*-icon-assets.md,
   STORY-*-api-requirements.md, pkg, epic, task README.
6) Optional note: `npm run dashboard:aggregate`.
7) Handoff: «ADMIN + STORY package ready at <path>.
   ui_first: operator runs ADMIN-01…04 → refine stories (ADMIN-05) → P1.3.
   tech_first: optional PA.3 → P1.3 now, separate wave, not mixed with ui_first in one pkg
   unless operator explicitly orders. This prompt stops.»
```

---

## Примечания (не в copy-paste)

- Связанные: [`req-to-backlog-stories.md`](./req-to-backlog-stories.md) (non-UI), [`req-to-ui-admin-layers.md`](./req-to-ui-admin-layers.md) (UI ADMIN only, STORY later), [`req-to-target-tech-architecture.md`](./req-to-target-tech-architecture.md) (target tech of focus; packaging — пакет тем), [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md).
- Dashboard: [`../../workflow/backlog-dashboard-maintenance.md`](../../workflow/backlog-dashboard-maintenance.md).
- Support docs (`UX-PROMPTS.md`, icon catalog STORY, api-req STORY) — deliverable слоёв 01/03/04, не этого промпта.
- Human: [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md).
