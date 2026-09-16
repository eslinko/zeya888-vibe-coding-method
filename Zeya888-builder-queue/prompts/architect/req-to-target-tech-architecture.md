# Requirement → target technical architecture (+ CTO/CPO interview)

**Категория:** architect (functional REQ → целевая tech-реализация фокуса)  
**Sibling (узкий bootstrap / pre-story infra):** [`req-to-tech-architecture.md`](./req-to-tech-architecture.md) — deployability / packaging / runtime image до story package  
**Не заменяет:** PA.2 REQ authoring · scatter · consistency-audit · story/ADMIN package prompts · P3  
**Не создаёт:** STORY, pkg, product code, stub schemas/files «чтобы path существовал», task README  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Даты отчёта:** [`../../guides/builder-artifact-dates.md`](../../guides/builder-artifact-dates.md) — live `--print-utc-now`

---

## Use cases (когда брать этот промпт)

REQ **часто (но не всегда)** пишется на уровне **функциональных / продуктовых** требований: что система должна делать для пользователя/оператора, границы scope, DoD в терминах поведения. Техническая реализация фокуса при этом может быть намеренно не зафиксирована (или зафиксирована фрагментарно). Этот промпт как раз для таких случаев: **отдельный документ (или система) целевой технической архитектуры фокуса REQ** — не backlog задач.

| Use case | Да / нет |
|----------|----------|
| Functional / product REQ есть; нужно **как** это реализовать в стеке проекта (модули, данные, границы, runtime) без смешения в сам REQ | **Да** |
| Child / mid-lifecycle REQ на фичу в уже живущем проекте (не только bootstrap greenfield) | **Да** |
| Parent product REQ уже разложен на per-project child; у child нет path-level tech realization | **Да** |
| Нужен SSOT «target tech arch» для согласования CTO/CPO **до** или **вместо** немедленного story slice | **Да** |
| REQ уже целиком technical (path-level contracts, runtime, packaging) и оператор просит только stories | **Нет** → [`req-to-backlog-stories.md`](./req-to-backlog-stories.md) / mixed / ADMIN |
| Нужен только audit согласованности parent+children vs цель | **Нет** → [`cross-project-req-consistency-audit.md`](./cross-project-req-consistency-audit.md) |
| Фокус именно **bootstrap infra / deployability packaging seam** перед первыми stories | Предпочтительнее узкий sibling [`req-to-tech-architecture.md`](./req-to-tech-architecture.md) (можно оба: сначала этот на focus, sibling на image/packaging) |
| Оператор просит задачи / STORY / pkg | **Нет** — этот промпт пишет **архитектуру**, не decomposition в work items |

**Что писать в выходном документе:** целевая техническая реализация **фокуса** REQ (компоненты, потоки данных, ownership артефактов, контракты, runtime/verify где уместно).  
**Чего не писать:** списки STORY keys, epic waves, task README, «сделать ticket X» — если нужна декомпозиция в работу, это следующий шаг отдельным промптом.

**Разделение уровней (держи в шапке ответа Phase 0):**

| Уровень | Где живёт | Содержание |
|---------|-----------|------------|
| Functional / product | `$requirementDoc` | Зачем, кому, поведение, scope/OOS, DoD в product terms |
| Target technical architecture | `{focus}/docs/architecture/…` (этот промпт) | Как в коде/инфре реализовать фокус REQ |
| Work items | backlog STORY / ADMIN (другие промпты) | Что делать по шагам |

---

## Когда / не использовать (кратко)

**Когда:** документ типа requirement (per-project или иной REQ-like), фокус понятен, но **целевая tech-реализация** не оформлена отдельным SSOT; нужен интерактивный CTO/CPO диалог + запись architecture + interview report с линками на REQ.

**Не использовать**, если нужен только story package / UI ADMIN / consistency audit / чистый packaging-bootstrap sibling без обсуждения реализации фокуса фичи.

**Урок (включать в чеклист, если фокус трогает Git FS + non-src start):** Git ownership ≠ image packaging.

**Подстановка оператором:**

| Поле | Значение |
|------|----------|
| `$requirementDoc=` | path REQ / requirement-like doc |
| `$builderProject=` | ключ профиля (`landing` \| `spa` \| `gateway` \| `aibridge` \| …) |
| `$slice=` | опц. сужение §§ / blocks (фокус интервью) |
| `$archPackageSlug=` | опц. kebab для подпапки / stem файла; пусто → из REQ id/title |
| `$archDocMode=` | опц. `single` \| `system` \| `auto` (дефолт `auto`) |

**Дефолт:** интервью + drafts **в чате**; диск — только после «запиши» / «materialize».

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/builder-artifact-dates.md
$requirementDoc=
$builderProject=
$slice=
$archPackageSlug=
$archDocMode=auto

workspace_root: /Users/eslinko/Development/DOGEstonia

Architect Studio — REQ → TARGET TECHNICAL ARCHITECTURE (functional REQ → tech realization of focus; + interactive CTO/CPO interview).
@$requirementDoc
builder_project: $builderProject
@$slice (если задан — только эти §§/blocks)
$archPackageSlug= (опц.)
$archDocMode=auto|single|system

MODE: analysis.mdc. Human language. Explain terms. Interactive interview.
This prompt produces TARGET TECH ARCHITECTURE for the REQ focus — NOT backlog stories, NOT tasks, NOT code.
No product code. No STORY/pkg/P3. No stub files “so paths exist”.
Do NOT invent APIs, fields, paths, or deploy contracts beyond @$requirementDoc + operator answers in this chat.
Gap → Unknown + question (do not silently omit).
Code claim = path:line after Read/Grep; else Unknown. Doc claim = path.
Plan-first: STOP after Phase 2 synthesis in chat. Disk write ONLY after explicit «запиши».
Other-протокол: if operator asks a counter-question, answer it first, then re-ask your pending question.

Resolve $focusFolder from docs/methodology/Zeya888-builder-queue/specs/profiles.yaml for $builderProject (focus_folder).
Architecture zone: {$focusFolder}/docs/architecture/
Analysis zone: {$focusFolder}/docs/analysis/
If docs/analysis/ missing → create only on materialize (with interview report), not earlier.

## Phase 0 — Classify + inventory (before first interview question)
1) Read @$requirementDoc fully (or $slice).
2) Classify REQ level in chat (one table row):
   | Level | Evidence (§) | Implication |
   Functional-heavy | … | this prompt is primary |
   Mixed functional+tech | … | extract tech into arch doc; keep REQ product-facing unless operator asks to rewrite REQ |
   Already path-level technical | … | ask operator: still want target-arch doc, or switch to story prompts / bootstrap sibling |
3) State use case aloud in one sentence (why this run exists).
4) List {$focusFolder}/docs/architecture/ (etalon). Decide layout:
   - $archDocMode=single → one file TECH-ARCH-<slug>.md or next numbered file that is self-contained for this REQ focus
   - $archDocMode=system → subfolder architecture/<kebab>/ + 00-overview.md root + siblings by concern
   - $archDocMode=auto → single if focus is one concern; system if ≥3 distinct technical concerns OR operator asks for system
   - If numbered series exists and mode allows: propose next numbers; do not renumber old docs
5) Inventory table:
| Concern (focus of REQ) | REQ says (cite §) | Silent | As-is code (path:line or Unknown) | Interview needed? |
Concerns depend on THIS REQ focus (adapt; do not force unrelated infra). Typical set when relevant:
  goal/OOS; components & boundaries; data model & contracts; runtime/start; ownership (Git/Volume/CDN/external);
  packaging seam (if Git FS + non-src start); env/fail-closed; verify surfaces; integration seams; privacy/security;
  migration / coexistence with current code.
6) Do NOT dump the full questionnaire. Start Phase 1 with ONE topic tied to the largest silent gap for the REQ focus.

## Phase 1 — Interactive interview (one topic per turn; max 2 related)

### Decision-point protocol (HARD — every question that offers a choice)
Whenever you ask the operator a decision question (2–3 options + Other), the **same turn** MUST include, in order, before waiting for the answer:

1) **Question** — plain-language term explain + the ask (one topic).
2) **Options analytics** — for EACH option A/B/C/(Other framing): what it means; pros; cons/risks; impact on REQ goals/DoD (cite §§). No invent beyond REQ + known as-is (path:line) + stated options.
3) **Architecture & project fit** — how each option aligns or conflicts with:
   - existing `{focus}/docs/architecture/` (and primer/cross-project map if already in context);
   - role of this microservice / `$builderProject` focus (boundaries, ownership, what must NOT leak into another service);
   - as-is code seams (path:line) or Unknown.
   Mark fit: fits | tension | conflicts | Unknown (with what is missing).
4) **Recommendation** — mandatory: name one preferred option + why (REQ + architecture/project fit). State explicitly: **решение остаётся за оператором** — recommendation is advisory only; do not proceed as if chosen until the operator answers.
5) Then STOP that turn and wait for the operator’s choice (or Other).

Do NOT ask a multi-option decision without blocks 2–4. Do NOT hide the recommendation. Do NOT decide unilaterally or treat silence as acceptance.

### After EACH operator answer
Reply with exactly:
1) **Confirm** — which option was chosen (or Other paraphrase); note recommendation **accepted** | **overridden** (and one-line implication if overridden).
2) **Follow-through analytics** — brief: what this locks for REQ / architecture / next themes (cite §§; code path:line if relevant).
3) **Next question** (full Decision-point protocol again) OR “checklist closed for this focus → Phase 2”.

Rules:
- Explain every technical term in plain language before asking.
- Offer 2–3 concrete options + Other.
- Skip a theme ONLY if REQ already closes it with path-level wording for THIS focus (cite §).
- Themes (pick/order by focus; packaging mandatory when Git FS + non-src start applies):
  F1 CPO: success cases / conscious OOS for the focus
  F2 Target components & trust boundaries (what lives where)
  F3 Data / schemas / contracts (logical; no invent fields beyond REQ+answers)
  F4 Runtime topology & start command (if execution is in scope)
  F5 Ownership matrix by artifact class for this focus
  F6 Packaging seam (REQUIRED if applicable — Git ownership ≠ image packaging)
  F7 Env / bind / fail-closed / health (if applicable)
  F8 Verify surfaces: what proves the architecture (src unit vs production entry — name which)
  F9 Integration with existing modules (path:line as-is vs target)
  F10 Privacy / security if focus touches PII or trust
- Do NOT turn answers into STORY keys or task lists.
- Record for interview report: question → options summary → agent recommendation → operator decision (accepted|overridden) → verbatim answer.

## Phase 2 — Synthesis (chat only; STOP)
Produce in chat:
- Proposed doc tree under architecture/ (single path or system)
- Draft outline of root (and siblings if any). Required root sections:
  Context & parent REQ (functional vs tech split);
  Target technical architecture of the focus (components, flows);
  Ownership / contracts as decided;
  Runtime / packaging / verify only if in scope for this focus;
  Coexistence with as-is (paths or Unknown);
  Open questions;
  Explicit “Not in this doc”: work items / STORY / pkg
- Open Unknowns list
- Proposed interview report path + REQ Related link rows
STOP. Wait for «запиши». Optional handoff hints only after materialize (or operator override).

## Phase 3 — Materialize (только по «запиши»)
1) python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
   Use utc_date / utc_now from stdout only.
2) Write architecture doc(s) as agreed (root must link to @$requirementDoc). Title must say target technical architecture of the REQ focus — not “implementation tasks”.
3) Write interview report:
   {$focusFolder}/docs/analysis/zeya888.req-target-tech-arch-interview-<slug>-<utc_date>.md
   slug = REQ id or filename stem; do not invent a new REQ number.
   Required sections: inputs + use-case statement; REQ level classify; verbatim decision log
   (question → options analytics summary → agent recommendation → operator decision accepted|overridden → answer);
   open Unknowns; link matrix REQ ↔ arch root ↔ report; note if packaging seam was N/A vs decided;
   method note «functional REQ ≠ target tech arch ≠ work items»; method note «recommendation advisory; operator decides».
4) Patch @$requirementDoc Related / Architecture (links only): arch root + interview report.
   Do NOT rewrite functional DoD into tech AC unless operator explicitly asked in this chat.
5) Reply: arch root path | sibling paths | report path | REQ link patch summary | handoff options:
   - optional PA.2: refine REQ wording (still functional) with pointers to tech-arch
   - optional bootstrap sibling req-to-tech-architecture.md if packaging/deployability still open
   - optional req-to-backlog-stories / mixed / ADMIN when operator wants work items
   - No P3.

## analysis.mdc gates (hard)
- Name ≠ create: do not scaffold empty schemas, sample packs, or code because a future AC named a path.
- Ask-scoped delivery: materialize only on «запиши».
- No plan-over-ask.
- Claims only from: REQ path, code path:line, operator answers in this chat.
- Do not smuggle STORY/pkg/task scaffolding into architecture docs.
```

---

## Примечания (не в copy-paste)

- **Decision points:** на каждом вопросе с опциями — analytics по опциям + fit к architecture/роли микросервиса + обязательная рекомендация; **решение за оператором**.
- **Зоны:** target tech SSOT = `{focus}/docs/architecture/`; interview = `{focus}/docs/analysis/zeya888.req-target-tech-arch-interview-…`. Root (или single) **и** report линкуются с REQ.
- **Vs bootstrap sibling:** [`req-to-tech-architecture.md`](./req-to-tech-architecture.md) заточен под pre-story **infra/deployability** (packaging checklist как центр). Этот файл — **общий** процесс: любой REQ-like, часто functional → отдельный документ **целевой tech-реализации фокуса**.
- **Vs stories:** architecture отвечает «как устроено целевое»; stories — «какие работы». Не смешивать в одном materialize.
- Human layer: [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md).
- Связанные: [`req-to-tech-architecture.md`](./req-to-tech-architecture.md), [`cross-project-req-consistency-audit.md`](./cross-project-req-consistency-audit.md), [`req-to-backlog-stories.md`](./req-to-backlog-stories.md), [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md), [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md).
