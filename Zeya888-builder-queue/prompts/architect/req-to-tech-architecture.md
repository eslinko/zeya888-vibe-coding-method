# Requirement → tech architecture (+ CTO/CPO interview) — bootstrap / pre-story infra

**Категория:** architect (post-REQ / pre-story-package · **узкий** infra/deployability)  
**Общий sibling (functional REQ → целевая tech-реализация фокуса):** [`req-to-target-tech-architecture.md`](./req-to-target-tech-architecture.md)  
**Не заменяет:** PA.2 REQ authoring · scatter · consistency-audit · [`req-to-backlog-stories.md`](./req-to-backlog-stories.md) / [`req-to-ui-admin-layers.md`](./req-to-ui-admin-layers.md) / [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md)  
**Не создаёт:** STORY, pkg, product code, stub schemas/files «чтобы path существовал»  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Даты отчёта:** [`../../guides/builder-artifact-dates.md`](../../guides/builder-artifact-dates.md) — live `--print-utc-now`

**Когда (узкий scope):** per-project product REQ есть (или почти canonical), но **техническая инфраструктура / deployability** не проработаны до path-level (runtime start, ownership классов артефактов, packaging Git FS assets, verify surfaces). Нужен **отдельный** tech-architecture SSOT + отчёт интервью **до** slice в STORY/ADMIN — особенно bootstrap / first cut.

**Не использовать**, если нужен общий документ **целевой технической реализации фокуса** functional REQ (не только packaging/bootstrap) — [`req-to-target-tech-architecture.md`](./req-to-target-tech-architecture.md). Если оператор просит только story package / UI ADMIN / consistency audit — соответствующие sibling prompts. Узкий этот промпт — **после** REQ и **перед** story prompts, когда пробел именно infra/deployability.

**Урок (обязателен в чеклисте):** Git ownership ≠ image packaging. «Schemas MUST remain in Git» ≠ «readable after `astro build` when start = `dist/server/entry.mjs`».

**Подстановка оператором:**

| Поле | Значение |
|------|----------|
| `$requirementDoc=` | path per-project REQ (напр. `landing/docs/requirements/REQ1-Node customization.md`) |
| `$builderProject=` | ключ профиля (`landing` \| `spa` \| `gateway` \| …) |
| `$slice=` | опц. сужение §§ / blocks REQ |
| `$archPackageSlug=` | опц. kebab для подпапки architecture; пусто → resolve из REQ id/title |

**Дефолт:** интервью + drafts **в чате**; запись на диск — только после «запиши» / «materialize».

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/builder-artifact-dates.md
$requirementDoc=
$builderProject=
$slice=
$archPackageSlug=

workspace_root: /Users/eslinko/Development/DOGEstonia

Architect Studio — REQ → TECH ARCHITECTURE (+ interactive CTO/CPO interview).
@$requirementDoc
builder_project: $builderProject
@$slice (если задан — только эти §§/blocks)
$archPackageSlug= (опц.)

MODE: analysis.mdc. Human language. Explain terms. Interactive interview.
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

## Phase 0 — Inventory (before first interview question)
1) Read @$requirementDoc fully (or $slice).
2) List {$focusFolder}/docs/architecture/ (etalon). Decide layout for THIS run:
   - Numbered series exists (e.g. 00…N.md) → propose next numbers for new docs; root overview may be a new numbered file that links siblings.
   - Empty / missing → single or system under architecture/ starting with 00-overview.md.
   - Many distinct concerns → subfolder architecture/<kebab>/ + 00-overview.md as root (+ siblings). Use $archPackageSlug if set; else kebab from REQ id/title.
3) Table in chat:
| Concern | REQ says (cite §) | Silent | Conflicts with code (path:line or Unknown) | Interview needed? |
Include at least: runtime/start; ownership (Git/Volume/CDN/external) per artifact class; packaging seam for Git FS assets; verify surface (src vs production entry); env/fail-closed; deploy/residual; phase seams.
4) Do NOT dump the full questionnaire. Start Phase 1 with ONE topic.

## Phase 1 — Interactive interview (one topic per turn; max 2 related)

### Decision-point protocol (HARD — every question that offers a choice)
Whenever you ask the operator a decision question (2–3 options + Other), the **same turn** MUST include, in order, before waiting for the answer:

1) **Question** — plain-language term explain + the ask (one topic).
2) **Options analytics** — for EACH option: meaning; pros; cons/risks; impact on REQ goals/AC/DoD (cite §§). No invent beyond REQ + as-is (path:line) + stated options.
3) **Architecture & project fit** — how each option aligns or conflicts with existing `{focus}/docs/architecture/`, the role of this `$builderProject` microservice/focus (boundaries, ownership), and as-is seams (path:line) or Unknown. Mark: fits | tension | conflicts | Unknown.
4) **Recommendation** — mandatory: one preferred option + why. State explicitly: **решение остаётся за оператором** — advisory only; do not treat as chosen until the operator answers.
5) STOP that turn; wait for the operator’s choice.

Do NOT ask a multi-option decision without blocks 2–4. Do NOT hide the recommendation. Do NOT decide unilaterally.

### After EACH operator answer
Reply with exactly:
1) **Confirm** — chosen option; recommendation **accepted** | **overridden** (+ one-line implication if overridden).
2) **Follow-through analytics** — what this locks for REQ / packaging / next themes.
3) **Next question** (full Decision-point protocol again) OR “checklist closed → Phase 2”.

Rules:
- Explain every technical term in plain language before asking.
- Offer 2–3 concrete options + Other.
- Skip a checklist item ONLY if REQ already closes it with path-level wording (cite §). Otherwise ask.
- Mandatory themes (order flexible; packaging is NOT optional when Git FS + non-src start):
  T1 CPO goal / success cases / conscious out-of-scope
  T2 Runtime topology: static | SSR | hybrid | worker — and real production start command
  T3 Ownership matrix by artifact class (content, schemas, static assets, secrets, config)
  T4 Packaging seam (REQUIRED if Git-owned non-JS loaded via fs / import.meta.url AND start ≠ src tree):
     how files appear in the runtime image after build; verify must name production entry, not only src unit tests
  T5 Env / bind / fail-closed / health
  T6 Deploy & residual: live proof vs mandatory local substitute gate when live is deferred
  T7 Observability / operator runbook hooks (only if in REQ scope)
  T8 Migration seams between REQ phases — who owns intersection A×B (asset story × runtime story)
  T9 Privacy / security boundaries if profile/REQ touch PII or trust boundaries
- Record for interview report: question → options summary → agent recommendation → operator decision (accepted|overridden) → verbatim answer.

## Phase 2 — Synthesis (chat only; STOP)
Produce in chat:
- Proposed doc tree (paths under architecture/)
- Draft outline of root (and each sibling): Context & parent REQ; runtime topology; ownership matrix; packaging & verify surfaces; env/fail-closed; deploy/residual; seams & story-slice hints (do NOT invent STORY keys unless operator named them); open questions
- Open Unknowns list
- Proposed interview report path + REQ Related link rows
STOP. Wait for «запиши». Do not suggest running story-package prompts until materialize completes (or operator overrides).

## Phase 3 — Materialize (только по «запиши»)
1) python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
   Use utc_date / utc_now from stdout only.
2) Write architecture docs as agreed in Phase 2 (root must link to @$requirementDoc).
3) Write interview report:
   {$focusFolder}/docs/analysis/zeya888.req-tech-arch-interview-<slug>-<utc_date>.md
   slug = REQ id or filename stem; do not invent a new REQ number.
   Required sections: inputs; verbatim decision log (question → options analytics summary → agent recommendation → operator decision accepted|overridden → answer); open Unknowns; link matrix REQ ↔ arch root ↔ report; method note «Git ownership ≠ image packaging»; method note «recommendation advisory; operator decides».
4) Patch @$requirementDoc Related / Architecture (links only): arch root + interview report. Do NOT rewrite DoD/AC unless operator explicitly asked in this chat.
5) Reply: arch root path | sibling paths | report path | REQ link patch summary | handoff:
   «tech-arch linked → optional PA.2 refine REQ wording → then req-to-backlog-stories / req-to-ui-admin-layers / req-to-frontend-mixed-package. No P3.»

## analysis.mdc gates (hard)
- Name ≠ create: do not scaffold empty schemas, sample packs, or code because a future AC named a path.
- Ask-scoped delivery: materialize only on «запиши».
- No plan-over-ask.
- Claims only from: REQ path, code path:line, operator answers in this chat.
```

---

## Примечания (не в copy-paste)

- **Decision points:** на каждом вопросе с опциями — analytics по опциям + fit к architecture/роли микросервиса + обязательная рекомендация; **решение за оператором**.
- **Зоны:** tech SSOT = `{focus}/docs/architecture/`; interview = `{focus}/docs/analysis/zeya888.req-tech-arch-interview-…`. Root (или single) tech doc **и** interview report линкуются с REQ.
- **Vs общий sibling:** [`req-to-target-tech-architecture.md`](./req-to-target-tech-architecture.md) — functional REQ → целевая tech-реализация **фокуса** (не только bootstrap packaging).
- **Почему до stories:** `req-to-backlog-stories` / mixed **не invent** сверх REQ → молчание REQ о packaging даёт false-green AC («committed in src» без production entry). Этот промпт закрывает пробел интервью + tech-arch SSOT.
- **Advisory (не hard-STOP):** если REQ prefer SSR/`dist` start и Git FS assets, а linked tech-arch ещё нет — оператору лучше прогнать этот промпт **до** story slice ([`req-to-backlog-stories.md`](./req-to-backlog-stories.md), [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md)).
- Human layer: [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md).
- Связанные: [`req-to-target-tech-architecture.md`](./req-to-target-tech-architecture.md), [`cross-project-req-consistency-audit.md`](./cross-project-req-consistency-audit.md) (пакет REQ vs цель), [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md) / [`cross-project-req-scatter.md`](./cross-project-req-scatter.md) (раньше), story prompts — после materialize.
- Incident ref (method): NC SSR schema packaging — ownership OK, deployability miss; see project `docs/analysis/zeya888.*-nc-ssr-schema-packaging-*` when present.
