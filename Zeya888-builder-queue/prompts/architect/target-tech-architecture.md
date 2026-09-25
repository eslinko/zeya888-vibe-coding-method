# Inputs → target technical architecture (+ CTO/CPO interview)

**Категория:** architect (REQ and/or existing stories → целевая tech-реализация фокуса)  
**Единственный промпт этого процесса.** Packaging / runtime image — пакет тем внутри этого прогона, не второй файл.  
**Было:** `req-to-target-tech-architecture.md` (переименован; вход больше не только REQ).  
**Не заменяет:** PA.2 REQ authoring · scatter · consistency-audit · story/ADMIN package prompts · P3  
**Не создаёт:** новые STORY, pkg, product code, stub schemas/files «чтобы path существовал», task README  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Даты отчёта:** [`../../guides/builder-artifact-dates.md`](../../guides/builder-artifact-dates.md) — live `--print-utc-now`

---

## Use cases (когда брать этот промпт)

Нужен отдельный SSOT **целевой технической архитектуры** фокуса. Вход — на равных: functional/product REQ, уже нарезанный пакет STORY, явный список STORY, или комбинация. Тот же промпт закрывает и **bootstrap infra / deployability** (runtime start, ownership, packaging Git FS → image) — classify `deployability-gap`.

| Use case | Да / нет |
|----------|----------|
| Functional / product REQ есть; нужно **как** это реализовать в стеке без смешения в сам REQ | **Да** |
| Mid-lifecycle: REQ + уже существующий story package / list — arch под нарезанный slice | **Да** |
| Stories-only: пакет или список STORY без отдельного REQ path — нужен arch SSOT под этот scope | **Да** |
| Parent product REQ разложен на child; у child нет path-level tech realization | **Да** |
| Пробел **bootstrap infra / packaging / deployability** | **Да** — packaging-темы обязательны |
| Оператор просит **новые** STORY / ADMIN / pkg | **Нет** → [`req-to-backlog-stories.md`](./req-to-backlog-stories.md) / mixed / ADMIN |
| Нужен только audit parent+children vs цель | **Нет** → [`cross-project-req-consistency-audit.md`](./cross-project-req-consistency-audit.md) |

**Advisory (не hard-STOP, до story prompts):** молчание REQ/stories о packaging при Git-owned non-JS и start ≠ src tree даёт false-green AC. Закрывать packaging-темы **здесь**, до [`req-to-backlog-stories.md`](./req-to-backlog-stories.md) / [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md), если stories ещё не нарезаны.

**Урок (чеклист, если фокус трогает Git FS + non-src start):** Git ownership ≠ image packaging.

**Что писать:** целевая tech-реализация **фокуса** (компоненты, потоки, ownership, контракты, runtime/packaging/verify где уместно). Можно **цитировать** переданные STORY keys как границы фокуса.  
**Чего не писать:** новые STORY keys, epic waves, task README, «сделать ticket X».

**Разделение уровней (Phase 0 шапка):**

| Уровень | Где живёт | Содержание |
|---------|-----------|------------|
| Functional / product | `$requirementDoc` (если задан) | Зачем, кому, поведение, scope/OOS, DoD |
| Story scope | `$storyPackageDir` / `$storyList` (если заданы) | Уже существующие STORY — границы фокуса, не новые work items |
| Target technical architecture | `{focus}/docs/architecture/…` | Как реализовать фокус в коде/инфре |
| Work items | backlog STORY / ADMIN (другие промпты) | Новые шаги работы |

---

## Когда / не использовать (кратко)

**Когда:** есть хотя бы один фокусный вход (REQ и/или stories); целевая tech-реализация не оформлена SSOT; нужен CTO/CPO диалог + architecture + interview report.

**Не использовать**, если нужны только новые story/ADMIN packages или consistency audit.

**Подстановка оператором:**

| Поле | Значение |
|------|----------|
| `$requirementDoc=` | опц. path REQ / requirement-like doc |
| `$storyPackageDir=` | опц. папка пакета (`…/backlog-stories/<pkg>/` с INDEX + `STORY-*.md`) |
| `$storyList=` | опц. CSV путей или STORY keys |
| `$builderProject=` | ключ профиля (обязателен) |
| `$slice=` | опц. сужение §§ / blocks / story keys |
| `$archPackageSlug=` | опц. kebab; пусто → из REQ id / package folder / first story key |
| `$archDocMode=` | опц. `single` \| `system` \| `auto` (дефолт `auto`) |

**Hard gate:** хотя бы один из `$requirementDoc` \| `$storyPackageDir` \| `$storyList`. Пустой набор → STOP, спросить оператора.

**Resolve stories:** `$storyPackageDir` → INDEX + все `STORY-*.md` в пакете; если оба `$storyPackageDir` и `$storyList` — пересечение (keys/paths из list внутри пакета). Только `$storyList` → resolve путей относительно focus `$tasksRoot`; missing file → Unknown + вопрос. Не invent story content.

**Дефолт:** интервью + drafts **в чате**; диск — только после «запиши» / «materialize».

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/builder-artifact-dates.md
$requirementDoc=
$storyPackageDir=
$storyList=
$builderProject=
$slice=
$archPackageSlug=
$archDocMode=auto

workspace_root: /Users/eslinko/Development/DOGEstonia

Architect Studio — INPUTS → TARGET TECHNICAL ARCHITECTURE (REQ and/or existing stories → tech realization of focus; + interactive CTO/CPO interview).
@$requirementDoc (если задан)
@$storyPackageDir (если задан — package folder)
$storyList= (опц. CSV paths or STORY keys)
builder_project: $builderProject
@$slice (если задан — только эти §§/blocks/story keys)
$archPackageSlug= (опц.)
$archDocMode=auto|single|system

MODE: analysis.mdc. Human language. Explain terms. Interactive interview.
This prompt produces TARGET TECH ARCHITECTURE for the focus — NOT new backlog stories, NOT tasks, NOT code.
Inputs on equal footing: REQ and/or existing story package / story list.
Packaging / runtime image is a theme pack INSIDE this prompt when applicable — not a second prompt.
No product code. No NEW STORY/pkg/P3. No stub files “so paths exist”.
Do NOT invent APIs, fields, paths, or deploy contracts beyond @$requirementDoc + resolved stories + operator answers in this chat.
Gap → Unknown + question (do not silently omit).
Code claim = path:line after Read/Grep; else Unknown. Doc claim = path (REQ or STORY).
Plan-first: STOP after Phase 2 synthesis in chat. Disk write ONLY after explicit «запиши».
Other-протокол: if operator asks a counter-question, answer it first, then re-ask your pending question.

HARD GATE: at least one of $requirementDoc | $storyPackageDir | $storyList must be set.
If all empty → STOP and ask the operator. Do not invent a focus.

Resolve $focusFolder / $tasksRoot from docs/methodology/Zeya888-builder-queue/specs/profiles.yaml for $builderProject.
Architecture zone: {$focusFolder}/docs/architecture/
Analysis zone: {$focusFolder}/docs/analysis/
If docs/analysis/ missing → create only on materialize (with interview report), not earlier.

Resolve story set:
- $storyPackageDir set → Read INDEX.md + STORY-*.md under that folder.
- Both $storyPackageDir and $storyList → intersection only (keys/paths from list that exist in package).
- Only $storyList → resolve each key/path under $tasksRoot / focus; missing → Unknown + question.
- Cite existing STORY keys as focus bounds; do NOT create new STORY files or keys.

## Phase 0 — Classify + inventory (before first interview question)
1) Read @$requirementDoc fully (or $slice) if set. Read resolved stories if set.
2) State Story scope in one line: package | list | none (+ count of STORY files read).
3) Classify focus level in chat (one table row) — use REQ and/or story AC as evidence:
   | Level | Evidence (§ / STORY) | Implication |
   Functional-heavy | … | this prompt is primary |
   Mixed functional+tech | … | extract tech into arch doc; keep REQ product-facing unless operator asks rewrite |
   Already path-level technical | … | ask: still want target-arch doc, or switch to implement / P1.3 |
   Deployability-gap | … | SAME prompt; packaging theme pack mandatory |
4) State use case aloud in one sentence (why this run exists).
5) List {$focusFolder}/docs/architecture/ (etalon). Decide layout:
   - $archDocMode=single → one file TECH-ARCH-<slug>.md or next numbered self-contained file
   - $archDocMode=system → subfolder architecture/<kebab>/ + 00-overview.md root + siblings
   - $archDocMode=auto → single if one concern; system if ≥3 concerns OR operator asks system
   - Numbered series: propose next numbers; do not renumber old docs
   - Empty / missing → start with 00-overview.md
   Slug: $archPackageSlug or REQ id/stem or package folder name or first story key.
6) Inventory table:
| Concern | Source says (cite REQ § and/or STORY path) | Silent | As-is code (path:line or Unknown) | Interview needed? |
Typical concerns when relevant:
  goal/OOS; components & boundaries; data model & contracts; runtime/start; ownership (Git/Volume/CDN/external);
  packaging seam (MANDATORY if Git FS + non-src start OR classify = deployability-gap); env/fail-closed; verify surfaces;
  deploy/residual; integration seams; privacy/security; migration / coexistence with current code.
7) Do NOT dump the full questionnaire. Start Phase 1 with ONE topic tied to the largest silent gap.

## Phase 1 — Interactive interview (one topic per turn; max 2 related)

### Decision-point protocol (HARD — every question that offers a choice)
Whenever you ask the operator a decision question (2–3 options + Other), the **same turn** MUST include, in order, before waiting for the answer:

1) **Question** — plain-language term explain + the ask (one topic).
2) **Options analytics** — for EACH option: meaning; pros; cons/risks; impact on REQ goals/DoD and/or STORY AC (cite). No invent beyond inputs + as-is (path:line) + stated options.
3) **Architecture & project fit** — align/conflict with existing `{focus}/docs/architecture/`, `$builderProject` role (boundaries, ownership), as-is seams (path:line) or Unknown.
   Mark: fits | tension | conflicts | Unknown.
4) **Recommendation** — mandatory: one preferred option + why. State: **решение остаётся за оператором** — advisory only.
5) STOP that turn; wait for the operator’s choice.

Do NOT ask a multi-option decision without blocks 2–4. Do NOT hide the recommendation. Do NOT decide unilaterally.

### After EACH operator answer
Reply with exactly:
1) **Confirm** — chosen option; recommendation **accepted** | **overridden** (+ one-line if overridden).
2) **Follow-through analytics** — what this locks for REQ / stories / architecture / next themes.
3) **Next question** (full Decision-point protocol) OR “checklist closed → Phase 2”.

Rules:
- Explain every technical term before asking.
- Offer 2–3 concrete options + Other.
- Skip a theme ONLY if inputs already close it with path-level wording (cite REQ § or STORY path).
- Themes (order by focus). Packaging pack NOT optional when Git FS + non-src start OR classify = deployability-gap:
  F1 CPO: success cases / conscious OOS for the focus
  F2 Target components & trust boundaries
  F3 Data / schemas / contracts (logical; no invent fields beyond inputs+answers)
  F4 Runtime topology & start: static | SSR | hybrid | worker — production start command
  F5 Ownership matrix by artifact class (Git/Volume/CDN/external)
  F6 Packaging seam (REQUIRED when applicable — Git ownership ≠ image packaging):
     Git-owned non-JS via fs / import.meta.url in runtime image when start ≠ src tree;
     verify names production entry, not only src unit tests
  F7 Env / bind / fail-closed / health
  F8 Verify surfaces (src unit vs production entry — name which)
  F9 Deploy & residual: live proof vs local substitute gate
  F10 Integration with existing modules; migration seams (asset × runtime) when phases apply
  F11 Observability / runbook hooks (only if in input scope)
  F12 Privacy / security if PII or trust
- Do NOT invent new STORY keys or task lists. Citing input STORY keys as focus bounds is OK.
- Record for interview report: question → options summary → agent recommendation → operator decision (accepted|overridden) → verbatim answer.

## Phase 2 — Synthesis (chat only; STOP)
Produce in chat:
- Proposed doc tree under architecture/
- Draft outline of root (and siblings). Required root sections:
  Context & inputs (REQ and/or story scope — functional vs tech split);
  Target technical architecture of the focus (components, flows);
  Ownership / contracts as decided;
  Runtime / packaging / verify / env / deploy-residual — when in scope (mandatory if packaging pack applied);
  Coexistence with as-is (paths or Unknown); seams (cite input STORY keys only — do NOT invent new ones);
  Open questions;
  Explicit “Not in this doc”: NEW work items / NEW STORY / pkg
- Open Unknowns list
- Proposed interview report path + Related link rows for each input that exists
STOP. Wait for «запиши».

## Phase 3 — Materialize (только по «запиши»)
1) python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
   Use utc_date / utc_now from stdout only.
2) Write architecture doc(s) as agreed. Root must link every provided input (REQ and/or story package INDEX and/or listed STORY paths). Title: target technical architecture of the focus — not “implementation tasks”.
3) Write interview report (NEW reports use this prefix only; do not rename historical zeya888.req-*-tech-arch-interview-* files):
   {$focusFolder}/docs/analysis/zeya888.target-tech-arch-interview-<slug>-<utc_date>.md
   slug = $archPackageSlug or REQ id/stem or package folder or first story key; do not invent a new REQ number.
   Required sections: inputs + use-case; Story scope line; level classify; verbatim decision log
   (question → options analytics summary → agent recommendation → operator decision accepted|overridden → answer);
   open Unknowns; link matrix inputs ↔ arch root ↔ report; packaging N/A vs decided;
   method note «inputs (REQ and/or stories) ≠ target tech arch ≠ new work items»;
   method note «Git ownership ≠ image packaging» when packaging pack applied (else «packaging N/A»);
   method note «recommendation advisory; operator decides».
4) Patch links only (do NOT rewrite DoD/AC unless operator explicitly asked):
   - If $requirementDoc set → Related / Architecture: arch root + interview report.
   - If stories set → Related / Architecture on package INDEX and/or each listed STORY (thin links).
5) Reply: arch root | siblings | report | link patch summary | handoff:
   - optional PA.2 refine REQ (still functional) with pointers to tech-arch
   - optional req-to-backlog-stories / ui-admin / mixed when operator wants NEW work items
   - No second architecture prompt. No P3.

## analysis.mdc gates (hard)
- Name ≠ create: do not scaffold empty schemas, sample packs, or code because a future AC named a path.
- Ask-scoped delivery: materialize only on «запиши».
- No plan-over-ask.
- Claims only from: REQ path, STORY path, code path:line, operator answers in this chat.
- Do not smuggle NEW STORY/pkg/task scaffolding into architecture docs.
```

---

## Примечания (не в copy-paste)

- **Decision points:** analytics по опциям + fit к architecture/роли + обязательная рекомендация; **решение за оператором**. При запросе ОЯЗ-расшифровки вариантов — attach [`decision-point-human-language.md`](./decision-point-human-language.md) (companion; не заменяет HARD Decision-point protocol).
- **Зоны:** tech SSOT = `{focus}/docs/architecture/`; новые interview = `{focus}/docs/analysis/zeya888.target-tech-arch-interview-…`. Исторические `zeya888.req-target-tech-arch-interview-…` / `zeya888.req-tech-arch-interview-…` не переименовывать.
- **Packaging:** не отдельный промпт; при Git FS + non-src start или `deployability-gap` — F4–F9 обязательны. Узкий `$slice` допустим.
- **Stories:** вход на равных с REQ; цитировать можно, создавать новые — нельзя.
- **Incident (method):** NC SSR schema packaging — ownership OK, deployability miss; see `docs/analysis/zeya888.*-nc-ssr-schema-packaging-*` when present.
- Human layer: [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md).
- Связанные: [`decision-point-human-language.md`](./decision-point-human-language.md), [`cross-project-req-consistency-audit.md`](./cross-project-req-consistency-audit.md), [`req-to-backlog-stories.md`](./req-to-backlog-stories.md), [`req-to-ui-admin-layers.md`](./req-to-ui-admin-layers.md), [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md), [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md).
