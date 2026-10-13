# Requirement → UI ADMIN layer package

**Категория:** architect (post-PA.2 / pre-story)  
**Не заменяет:** выполнение ADMIN «Выполни…» / P1.3  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Эталон пакета:** `spa-app/docs/tasks/backlog-stories/public-home/ADMIN-PH-01…06` (+ `PRODUCT-BRIEF.md`, `INDEX.md`)

**Когда:** spa / landing (или visual/mixed) requirement → нужна **система файлов-планов по слоям**, а **не** сразу финальные `STORY-*`.

**Не использовать** для чистого backend / non-UI — [`req-to-backlog-stories.md`](./req-to-backlog-stories.md). Если в одном FE REQ есть и UI-срезы, и tech-стори без мокапов, и нужны **ADMIN + STORY сразу** — [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md).

Пакет backlog **не** подаётся. **Всегда NEW** `…/backlog-stories/<slug>/` (slug из `$featureSlug` или REQ). Не reuse `public-home` / чужие пакеты.

**Дефолт записи:** plan + полные drafts в чате; диск — только «запиши».

---

## Два промпта в этом файле

| Промпт | Когда копировать | Коротко, чем отличается |
|--------|------------------|-------------------------|
| **A — UX ещё нет** | Нужно спланировать полный канон, включая генерацию UX-промптов / state matrix | Пакет = BRIEF + INDEX + **ADMIN-01…06**. Первый executable = **ADMIN-01**. |
| **B — UX уже на входе** | Артборды (со стейтами) + **своя спека на каждый артборд** уже переданы в промпт (`@` файлы) | **Нет ADMIN-01 и ADMIN-02**. Первый executable = **ADMIN-03 (icons)**. Все UX-файлы из входа промпта → **явная таблица во Входе** ADMIN-03 (полная детализация по путям); дальше 04→05→06 как в A. |

Канон слоёв (общая таблица; в B слои 01–02 **omit** с why):

| # | Файл | Роль |
|---|------|------|
| 0 | `PRODUCT-BRIEF.md` | locked brief из REQ |
| — | `INDEX.md` | статусы слоёв + порядок |
| 01 | `ADMIN-{PREFIX}-01-product-ux-prompts.md` | UX prompts / state matrix → later `UX-PROMPTS.md` (**только A**) |
| 02 | `ADMIN-…-02-ux-mockup-intake.md` | mockup specs intake (**только A**) |
| 03 | `ADMIN-…-03-icon-assets-catalog.md` | icon catalog plan (**первый слой в B**) |
| 04 | `ADMIN-…-04-api-requirements.md` | API needs vs verified code/docs |
| 05 | `ADMIN-…-05-backlog-stories-l10n.md` | **deliverable later:** STORY-* + l10n (не создавать STORY в этом промпте) |
| 06 | `ADMIN-…-06-tech-decomposition.md` | epic/tasks/pkg plan (scaffold later; no execute) |

Структура каждого ADMIN: Meta (Key/Status/Depends/Blocks/Skill) · Цель · Вход · Deliverable · Acceptance · Как выполнять — **как** ADMIN-PH-*.

---

## Copy-paste A — Requirement → UI ADMIN (UX prompts ещё нужны)

**Подстановка (только это):**

| Поле | Значение |
|------|----------|
| `$requirementDoc=` | path REQ (напр. `spa-app/docs/requirements/15-early-signal-….md`) |
| `$builderProject=` | `spa` \| `landing` |
| `$featureSlug=` | опц. короткий префикс (напр. `ES` → `ADMIN-ES-01-…`); пусто → вывести из REQ title в plan |

```text
@.cursor/rules/analysis.mdc
$requirementDoc=
$builderProject=
$featureSlug=

Requirement → UI ADMIN layer package — VARIANT A (UX prompts ещё нужны) (plan mode).
@$requirementDoc
builder_project: $builderProject
feature_prefix: ADMIN-$featureSlug- (if $featureSlug empty — derive PREFIX from REQ title; show in plan)

MODE: plan-only. STOP after layer plan + full drafts in chat.
Do NOT: edit files until «запиши»; create STORY-*.md / pkg / epic / task README now;
      run P1.3/P3; invent gateway HTTP paths/fields (cite sibling REQ or TBD Open question);
      generate PNG mockups; propose «Выполни ADMIN-01» / Builder until operator go-ahead;
      ask operator for backlog package path; reuse existing packages (public-home, etc.).
Code claims: only after Read/Grep with path:line; else Unknown.

Etalon structure: spa-app/docs/tasks/backlog-stories/public-home/ADMIN-PH-01…06
(+ PRODUCT-BRIEF.md, INDEX.md). Match Meta/Depends/Blocks/Skill/Deliverable/Acceptance/Как выполнять.
Etalon = structure only — write into a NEW package, never into public-home.

## Phase 0 — Package path (NEW, mandatory)
Proposed path: `{spa-app|landing}/docs/tasks/backlog-stories/<kebab-slug>/`
Slug from $featureSlug (expanded) or REQ title/id.
Why: UI ADMIN set is large; always NEW; never reuse.
Table: | Decision | Path | Why |
Decision must be `new`. Override to existing path ONLY if operator explicitly orders in chat (not an input field).

## Phase 1 — Own surfaces
Из @$requirementDoc:
- surfaces / artboards / states (A–E etc.)
- API seams (consume existing vs Unknown / sibling REQ)
- l10n needs; out of scope
Таблица: | Surface / claim | REQ § | Notes |

## Phase 2 — Layer plan
| Layer | Include? (yes / omit+why) | Skill | Depends | Blocks | Proposed filename |
01…06 + BRIEF + INDEX. Default = all six ADMIN; omit only with explicit why (e.g. no new icons).
Include Phase 0 package path in the plan summary.
Proposed $dashboardFile delta (spa → spa-mvp-dashboard.md; landing → landing-mvp-dashboard.md):
By package = NEW path; Remaining = ADMIN keys Todo / «ADMIN package Todo»; §Now = package path + ADMIN-01 next.
Do not count STORY as Done (stories do not exist yet).
Canon: docs/methodology/Zeya888-builder-queue/workflow/backlog-dashboard-maintenance.md
Dashboard edit only on «запиши».

Planned STORY keys (names only) go **inside** ADMIN-05 draft as target table — do NOT write STORY files in this prompt.

## Phase 3 — Drafts in chat
Full markdown for:
1) PRODUCT-BRIEF.md (from REQ; locked intent; out of scope; links to parent/sibling REQ)
2) INDEX.md (Todo statuses; order 01→06)
3) Each included ADMIN-0N (complete executable plan file text)

ADMIN-05 lists future STORY-* keys + l10n plan; files appear only when operator later runs ADMIN-05.
ADMIN-06 describes future epic/task/pkg scaffold; does not create them now.

## End of plan reply
Handoff: none until materialize.
Reply ends with: Phase 0 path + layer plan + drafts + proposed INDEX/dashboard delta + clarifying questions only.
Do not suggest executing ADMIN layers or P1 until operator go-ahead.

## Materialize (только по «запиши»)
1) Create the NEW package directory from Phase 0 (do not write into an unrelated existing package).
2) Write PRODUCT-BRIEF.md, INDEX.md (ADMIN statuses Todo), included ADMIN-*.md only.
3) If root backlog-stories/INDEX.md exists — add package pointer row.
4) Sync $dashboardFile: By package, Remaining (ADMIN Todo), §Now (path + next ADMIN-01), Updated/Last change — recount from disk ([backlog-dashboard-maintenance.md](../../workflow/backlog-dashboard-maintenance.md)).
5) Do NOT write STORY-*.md, pkg, epic, UX-PROMPTS.md, icon PNGs.
6) Optional note: `npm run dashboard:aggregate`.
7) Handoff: «ADMIN package + dashboard ready at <path> → operator runs layers (“Выполни ADMIN-…”);
   after ADMIN-05/06 done → P1.3 on stories. This prompt stops.»
```

---

## Copy-paste B — Requirement → UI ADMIN (UX assets уже даны)

**Когда:** артборды со стейтами и **отдельная спека на каждый артборд** уже есть в контексте промпта. Не генерировать UX-промпты; не создавать ADMIN-01/02.

**Подстановка:**

| Поле | Значение |
|------|----------|
| `$requirementDoc=` | path REQ |
| `$builderProject=` | `spa` \| `landing` |
| `$featureSlug=` | опц. префикс; пусто → из REQ title |
| UX files | обязательный вход: оператор `@`-ит **все** артборды и **все** спеки; промпт обязан обработать каждый переданный файл |

```text
@.cursor/rules/analysis.mdc
$requirementDoc=
$builderProject=
$featureSlug=

Requirement → UI ADMIN layer package — VARIANT B (UX assets уже даны) (plan mode).
@$requirementDoc
builder_project: $builderProject
feature_prefix: ADMIN-$featureSlug- (if $featureSlug empty — derive PREFIX from REQ title; show in plan)

UX INPUT (mandatory): operator attached / @-mentioned artboard files (with states)
and per-artboard spec files. Process EVERY such file from this prompt turn — do not drop,
summarize away, or invent missing pairs.

MODE: plan-only. STOP after layer plan + full drafts in chat.
Do NOT: edit files until «запиши»; create STORY-*.md / pkg / epic / task README now;
      run P1.3/P3; invent gateway HTTP paths/fields (cite sibling REQ or TBD Open question);
      generate PNG mockups or UX-PROMPTS.md; invent artboards/specs not in the prompt input;
      create ADMIN-01 or ADMIN-02 files; propose «Выполни ADMIN-01/02» / Builder until operator go-ahead;
      ask operator for backlog package path; reuse existing packages (public-home, etc.).
Code claims: only after Read/Grep with path:line; else Unknown.

Etalon structure: spa-app/docs/tasks/backlog-stories/public-home/ADMIN-PH-03…06
(+ PRODUCT-BRIEF.md, INDEX.md). Match Meta/Depends/Blocks/Skill/Deliverable/Acceptance/Как выполнять
for included layers. Etalon = structure only — write into a NEW package, never into public-home.
Layers 01–02 are OMITTED (why: UX artboards+specs already provided as prompt inputs).

## Phase 0 — Package path (NEW, mandatory)
Proposed path: `{spa-app|landing}/docs/tasks/backlog-stories/<kebab-slug>/`
Slug from $featureSlug (expanded) or REQ title/id.
Why: UI ADMIN set is large; always NEW; never reuse.
Table: | Decision | Path | Why |
Decision must be `new`. Override to existing path ONLY if operator explicitly orders in chat (not an input field).

## Phase 1 — UX inventory (mandatory, full file detail)
From every artboard and every spec file attached / @-mentioned in this prompt
(and surfaces claimed in @$requirementDoc):
Build table covering ALL input UX files:
| Artboard file (path) | States | Spec file (path) | REQ § / surface | Notes |
Rules:
- Each artboard MUST map to its own spec file. Missing pair → Unknown / Open question (do not invent).
- Paths must be concrete workspace-relative paths from the prompt input — not «see UX folder».
- If operator attached N artboards and M specs, account for all N+M files in the table or Notes.
Also list: API seams (consume existing vs Unknown / sibling REQ); l10n needs; out of scope.
Surfaces table (from REQ): | Surface / claim | REQ § | Notes |

## Phase 2 — Layer plan
| Layer | Include? (yes / omit+why) | Skill | Depends | Blocks | Proposed filename |
Default include: BRIEF + INDEX + ADMIN-03 + ADMIN-04 + ADMIN-05 + ADMIN-06.
Default omit: ADMIN-01 (why: UX prompts not needed — artboards+specs already input);
              ADMIN-02 (why: mockup intake not a separate layer — assets already input).
Further omit (e.g. no new icons) only with explicit why.
First executable layer = ADMIN-03. Depends for 03: PRODUCT-BRIEF + UX inventory (no Depends on 01/02).
Include Phase 0 package path in the plan summary.
Proposed $dashboardFile delta (spa → spa-mvp-dashboard.md; landing → landing-mvp-dashboard.md):
By package = NEW path; Remaining = ADMIN-03…06 Todo / «ADMIN package Todo»;
§Now = package path + ADMIN-03 next.
Do not count STORY as Done (stories do not exist yet).
Canon: docs/methodology/Zeya888-builder-queue/workflow/backlog-dashboard-maintenance.md
Dashboard edit only on «запиши».

Planned STORY keys (names only) go **inside** ADMIN-05 draft as target table — do NOT write STORY files in this prompt.

## Phase 3 — Drafts in chat
Full markdown for:
1) PRODUCT-BRIEF.md (from REQ; locked intent; out of scope; links to parent/sibling REQ;
   note: UX assets provided at package start — list inventory summary)
2) INDEX.md (Todo for 03→06; document omit 01/02 + why; order starts at 03)
3) ADMIN-03 (icons) — complete executable plan:
   - Вход MUST embed the full Phase 1 UX inventory table (every artboard path + every spec path + states).
     This table is the authoritative input parameter list for the first ADMIN — not a prose summary.
   - Goal/Deliverable/Acceptance/Как выполнять as etalon ADMIN-*-03; use those files as sources.
4) ADMIN-04, ADMIN-05, ADMIN-06 — complete drafts as in variant A for those layers;
   each Вход MUST include the same UX file table (full copy or explicit «same as ADMIN-03 Вход»
   plus repeated concrete paths for files that layer needs). Do not reduce to «UX ready».

ADMIN-05 lists future STORY-* keys + l10n plan; files appear only when operator later runs ADMIN-05.
ADMIN-06 describes future epic/task/pkg scaffold; does not create them now.
Do NOT draft ADMIN-01 or ADMIN-02.

## End of plan reply
Handoff: none until materialize.
Reply ends with: Phase 0 path + UX inventory + layer plan + drafts + proposed INDEX/dashboard delta
+ clarifying questions only (e.g. unpaired artboard/spec).
Do not suggest executing ADMIN layers or P1 until operator go-ahead.
Do not suggest ADMIN-01/02.

## Materialize (только по «запиши»)
1) Create the NEW package directory from Phase 0 (do not write into an unrelated existing package).
2) Write PRODUCT-BRIEF.md, INDEX.md (03…06 Todo; omit 01/02 noted), ADMIN-03…06 only
   (ADMIN-03 Вход retains full UX file table).
3) If root backlog-stories/INDEX.md exists — add package pointer row.
4) Sync $dashboardFile: By package, Remaining (ADMIN-03…06 Todo), §Now (path + next ADMIN-03),
   Updated/Last change — recount from disk
   ([backlog-dashboard-maintenance.md](../../workflow/backlog-dashboard-maintenance.md)).
5) Do NOT write STORY-*.md, pkg, epic, UX-PROMPTS.md, ADMIN-01/02, icon PNGs.
6) Optional note: `npm run dashboard:aggregate`.
7) Handoff: «ADMIN package (UX-ready, start ADMIN-03) + dashboard ready at <path> →
   operator runs layers (“Выполни ADMIN-03” …);
   after ADMIN-05/06 done → P1.3 on stories. This prompt stops.»
```

---

## Примечания (не в copy-paste)

- Связанные: [`req-to-backlog-stories.md`](./req-to-backlog-stories.md) (non-UI, reuse|new), [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md) (FE mixed: ADMIN + STORY), [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md).
- Dashboard: [`../../workflow/backlog-dashboard-maintenance.md`](../../workflow/backlog-dashboard-maintenance.md).
- Landing: те же слои (A: 01–06; B: 03–06); пути mockups/icons — по `landing/docs/…` после verify exists.
- Human: [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md).
