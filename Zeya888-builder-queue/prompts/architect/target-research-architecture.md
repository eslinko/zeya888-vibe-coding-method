# Inputs → target research architecture (+ research lead interview)

**Категория:** architect (research REQ + prior research-pipe → целевая **research-архитектура** процесса сбора сложных данных)  
**Единственный промпт этого процесса.** Роли диалогов / schema / phases / evidence — пакет тем внутри этого прогона, не второй файл.  
**Адаптация от:** [`target-tech-architecture.md`](./target-tech-architecture.md) (код/инфра). Этот файл — **не** tech-arch и **не** Builder Queue STORY/P3.  
**Не заменяет:** PA.2 REQ authoring · tech-arch · scatter · story/ADMIN · P3 code  
**Не создаёт:** product code, STORY/pkg, stub prompts/schemas «чтобы path существовал», массовый сбор данных  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Даты отчёта:** [`../../guides/builder-artifact-dates.md`](../../guides/builder-artifact-dates.md) — live `--print-utc-now`  
**Эталон research-pipe (read-only образец):** FLOOU-EU-REGMAP — charter + ARCHITECTURE + 12 prompts + `pipe-docs/` under `Floou/docs/analysis/eu-agencies-collector/`

---

## Use cases (когда брать этот промпт)

Нужен отдельный SSOT **целевой research-архитектуры** (как исполнять исследование: роли, фазы, schema, handoff, verification, human deliverable) — **без** смешения в сам product REQ и **без** нарезки code STORY.

| Use case | Да / нет |
|----------|----------|
| Research / product REQ есть; нужно **как** устроить research-pipe (диалоги, контракты, gates) | **Да** |
| Есть RETRO / prior pipe (например REGMAP) — нужно экстраполировать паттерны на новый project_id | **Да** |
| Process kit отсутствует (`process-kit-missing`) или разрознен (`research-pipe-gap`) | **Да** — theme pack ролей/схемы обязателен |
| Нужна tech-архитектура кода/деплоя | **Нет** → [`target-tech-architecture.md`](./target-tech-architecture.md) |
| Оператор просит **новые** STORY / ADMIN / pkg / P3 | **Нет** → story/ADMIN prompts |
| Нужен только audit REQ vs цель без arch | **Нет** → consistency-audit / обычный analysis |
| Сразу массовый сбор фактов (посредники, органы) без process kit | **Нет** — сначала этот промпт (или уже готовый kit), потом orchestrator run |

**Advisory:** молчание REQ о ролях/schema/evidence при «сложном сборе» даёт false-green: call-sheet без проверяемой цепочки. Закрывать research-pipe темы **здесь**, до запуска сбора.

**Урок (чеклист):** product REQ ≠ research architecture ≠ execution packages на диске.  
**Урок (REGMAP):** competent authorities ≠ commercial intermediaries — разные project_id / entity_type / call-sheet.

**Что писать:** целевая research-реализация **фокуса** (роли диалогов, фазы P*, schema/CSV, evidence rules, pipe-docs layout, verification, human deliverable). Можно **цитировать** prior pipe paths и RETRO как границы/эталон.  
**Чего не писать:** новые STORY keys, epic waves, task README, «сделать ticket X», выдуманные фирмы/контакты, stub prompt bodies «на будущее».

**Разделение уровней (Phase 0 шапка):**

| Уровень | Где живёт | Содержание |
|---------|-----------|------------|
| Functional / product research | `$requirementDoc` | Зачем, кому, scope/OOS, DoD каталога / call-sheet |
| Prior pipe / RETRO | `$retroDoc` / `$priorPipeRoot` | Образец процесса и что reuse |
| Target research architecture | `$researchRoot` (charter, ARCHITECTURE, prompts kit, schema rules) | Как устроить исследование |
| Execution packages | `pipe-docs*` (другие волны) | Фактический сбор после kit + «запусти» |
| Work items code | backlog STORY (другие промпты) | Не этот промпт |

---

## Когда / не использовать (кратко)

**Когда:** есть research REQ (и желательно RETRO/prior pipe); целевой research-kit не оформлен SSOT; нужен интерактивный диалог research-lead + architecture docs + interview report.

**Не использовать**, если нужны tech-arch кода, новые story packages, или уже пора только исполнять готовый orchestrator.

**Подстановка оператором:**

| Поле | Значение |
|------|----------|
| `$requirementDoc=` | **обязателен** path research REQ |
| `$retroDoc=` | опц. RETRO / process-extract (паттерны prior pipe) |
| `$priorPipeRoot=` | опц. корень эталонного research-pipe (charter, ARCHITECTURE, prompts, pipe-docs) |
| `$researchRoot=` | корень зоны исследования (обязателен); куда ляжет новый kit |
| `$slice=` | опц. сужение §§ REQ / тем RETRO |
| `$archPackageSlug=` | опц. kebab; пусто → из REQ id (напр. `floou-eu-int`) |
| `$archDocMode=` | опц. `single` \| `system` \| `auto` (для research-pipe дефолт рекомендации: `system`) |
| `$projectId=` | опц. новый research project_id (напр. `FLOOU-EU-INT`) |

**Hard gate:** `$requirementDoc` и `$researchRoot` обязательны. Пусто → STOP, спросить оператора.

**Дефолт:** интервью + drafts **в чате**; диск — только после «запиши» / «materialize».

**Пример подстановки (FLOOU intermediaries):**

```text
$requirementDoc=Floou/docs/analysis/eu-agencies-collector/requirements/REQ-FLOOU-INT-01-commercial-intermediaries-catalog.md
$retroDoc=Floou/docs/analysis/eu-agencies-collector/requirements/RETRO-FLOOU-EU-REGMAP-process-extract.md
$priorPipeRoot=Floou/docs/analysis/eu-agencies-collector
$researchRoot=Floou/docs/analysis/eu-agencies-collector
$archPackageSlug=floou-eu-int
$archDocMode=system
$projectId=FLOOU-EU-INT
```

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/builder-artifact-dates.md
@docs/methodology/Zeya888-builder-queue/prompts/architect/target-research-architecture.md
$requirementDoc=
$retroDoc=
$priorPipeRoot=
$researchRoot=
$slice=
$archPackageSlug=
$archDocMode=system
$projectId=

workspace_root: /Users/eslinko/Development/DOGEstonia

Architect Studio — INPUTS → TARGET RESEARCH ARCHITECTURE
(research REQ + optional RETRO/prior pipe → research-process kit architecture;
 + interactive research-lead interview).
@$requirementDoc
@$retroDoc (если задан)
@$priorPipeRoot (если задан — charter/ARCHITECTURE/prompts/pipe-docs как эталон)
research_root: $researchRoot
@$slice (если задан — только эти §§/темы)
$archPackageSlug= (опц.)
$archDocMode=auto|single|system
$projectId= (опц.)

MODE: analysis.mdc. Human language. Explain terms. Interactive interview.
This prompt produces TARGET RESEARCH ARCHITECTURE for the focus —
NOT tech/code architecture, NOT new backlog stories, NOT tasks, NOT data collection runs,
NOT inventing intermediary/agency facts.
Inputs on equal footing: REQ + optional RETRO + optional prior pipe (read-only etalon).
Dialog roles / schema / phases / evidence / human deliverable = theme pack INSIDE this prompt — not a second prompt.
No product code. No NEW STORY/pkg/P3. No stub prompt/schema files “so paths exist”.
Do NOT invent dialog counts, CSV columns, package paths, or evidence rules beyond
@$requirementDoc + @$retroDoc + @$priorPipeRoot (Opened files) + operator answers in this chat.
Gap → Unknown + question (do not silently omit).
Doc claim = path after Read. Prior-pipe claim = path under $priorPipeRoot. Code claim N/A unless operator asks coexistence with tooling scripts (then path:line).
Plan-first: STOP after Phase 2 synthesis in chat. Disk write ONLY after explicit «запиши».
Other-протокол: if operator asks a counter-question, answer it first, then re-ask your pending question.

HARD GATE: $requirementDoc and $researchRoot must be set.
If either empty → STOP and ask the operator. Do not invent a focus.

Research architecture zone (propose under $researchRoot; exact tree decided in interview):
  - Charter (new project_id)
  - ARCHITECTURE.md (execution model: roles, phases, Task spawn, handoff)
  - Prompts kit / README (ролевые промпты — bodies only on materialize if operator asked full kit)
  - Schema / contract rules (CSV headers, enums, ID rules)
  - pipe-docs* layout rules (где пишут пакеты; пустые CSV не scaffold заранее)
Interview / analysis reports zone:
  {$researchRoot}/requirements/ OR {$researchRoot}/docs/analysis/ —
  prefer {$researchRoot}/requirements/ for INT-family; else {$researchRoot}/ with clear prefix.
If folder missing → create only on materialize, not earlier.

Resolve prior pipe (read-only):
- If $priorPipeRoot set → Read charter, ARCHITECTURE.md, prompts README (and sample 01/03/12 if needed), pipe-docs/README — cite paths.
- If $retroDoc set → Read fully; use as “what to extrapolate / what not to copy blindly”.
- Do NOT modify prior pipe packages during this prompt unless operator explicitly orders a thin Related link.

## Phase 0 — Classify + inventory (before first interview question)
1) Read @$requirementDoc fully (or $slice). Read @$retroDoc if set. Skim @$priorPipeRoot etalon files if set.
2) State Prior-pipe scope in one line: path | none (+ key artifacts opened).
3) Classify focus level in chat (one table row) — use REQ (± RETRO) as evidence:
   | Level | Evidence (§ / path) | Implication |
   Functional-heavy research REQ | … | this prompt is primary |
   Mixed REQ + partial kit on disk | … | extract missing process into arch; keep REQ product-facing |
   Already path-level process kit | … | ask: still want target-research-arch doc, or switch to orchestrator run |
   process-kit-missing / research-pipe-gap | … | SAME prompt; roles+schema+phases theme pack mandatory |
4) State use case aloud in one sentence (why this run exists).
5) List existing research-arch artifacts under $researchRoot (etalon). Decide layout:
   - $archDocMode=single → one RESEARCH-ARCH-<slug>.md
   - $archDocMode=system → set: Charter + ARCHITECTURE.md + prompts/README (+ schema contract doc) — default for new pipe
   - $archDocMode=auto → system if ≥3 concerns (roles, schema, phases) OR operator asks system; else single
   - Do not renumber/destroy prior REGMAP files; new project_id = parallel kit (names decided in interview)
   Slug: $archPackageSlug or REQ id/stem.
6) Inventory table:
| Concern | Source says (cite REQ § / RETRO § / prior path) | Silent | As-is on disk (path or Unknown) | Interview needed? |
Typical concerns when relevant:
  goal/OOS; entity types (gov vs commercial); dialog roles & owners;
  phases (Prep/P0–P6 or adapted); schema/CSV/enums/ID rules;
  evidence standard for non-gov sources; geography reuse (country_manifest);
  link to prior pipe (read-only inputs); specialists vs regional;
  independent verification (analog of dialog 12); human call-sheet deliverable;
  acceptance gates; coexistence with gov call-sheet; explicit non-goals (no Kanna verdict without dossier).
7) Do NOT dump the full questionnaire. Start Phase 1 with ONE topic tied to the largest silent gap.

## Phase 1 — Interactive interview (one topic per turn; max 2 related)

### Decision-point protocol (HARD — every question that offers a choice)
Whenever you ask the operator a decision question (2–3 options + Other), the **same turn** MUST include, in order, before waiting for the answer:

1) **Question** — plain-language term explain + the ask (one topic).
2) **Options analytics** — for EACH option: meaning; pros; cons/risks; impact on REQ goals/DoD (cite). No invent beyond inputs + as-is paths + stated options.
3) **Architecture & project fit** — align/conflict with prior pipe ($priorPipeRoot), RETRO lessons, existing $researchRoot artifacts.
   Mark: fits | tension | conflicts | Unknown.
4) **Recommendation** — mandatory: one preferred option + why. State: **решение остаётся за оператором** — advisory only.
5) STOP that turn; wait for the operator’s choice.

Do NOT ask a multi-option decision without blocks 2–4. Do NOT hide the recommendation. Do NOT decide unilaterally.

### After EACH operator answer
Reply with exactly:
1) **Confirm** — chosen option; recommendation **accepted** | **overridden** (+ one-line if overridden).
2) **Follow-through analytics** — what this locks for REQ / research-arch / next themes.
3) **Next question** (full Decision-point protocol) OR “checklist closed → Phase 2”.

Rules:
- Explain every research-process term before asking (charter, owner_id, discovery vs depth-pass, claim/evidence, READY_FOR_REVIEW vs ACCEPTED, call-sheet).
- Offer 2–3 concrete options + Other.
- Skip a theme ONLY if inputs already close it with path-level wording (cite REQ § / RETRO § / prior path).
- Themes (order by focus). Roles+schema+phases pack NOT optional when classify = process-kit-missing | research-pipe-gap:
  R1 CPO/research lead: success cases / conscious OOS for the catalog & call-sheet
  R2 Entity model: intermediary types enum; gov vs commercial fence; pan-EU rows
  R3 Dialog/role map: how many roles; which reuse REGMAP 01–12 pattern; which rename
  R4 Phases & gates: Prep → framework → schema → discovery → depth → specialists → verify → accept
  R5 Schema & handoff: CSV entities, ID pattern, package folder contract, versioning
  R6 Evidence standard: what counts as OPENED for company sites; UNKNOWN rules; no invent contacts
  R7 Geography & ownership: reuse country_manifest G1–G5 vs new grouping
  R8 Prior-pipe inputs: which REGMAP/final/call-sheet/FLOOU-10 paths are frozen inputs
  R9 Specialists: Novel Food desk / labs / multi-country (if in REQ)
  R10 Independent verification: analog of dialog 12; author cannot ACCEPTED self
  R11 Human deliverable: call-sheet columns; separation from gov call-sheet
  R12 Execution in Cursor: root orchestrator + Task spawn + workspace-relative paths (if yes)
  R13 Acceptance / PARTIAL rules; blockers & external briefs pattern (if reuse)
  R14 Privacy / outreach ethics (contacting firms; no spam invent)
- Do NOT invent new STORY keys or start data collection. Citing prior package_ids as etalon is OK.
- Record for interview report: question → options summary → agent recommendation → operator decision (accepted|overridden) → verbatim answer.

## Phase 2 — Synthesis (chat only; STOP)
Produce in chat:
- Proposed doc tree under $researchRoot (charter / ARCHITECTURE / prompts / schema — as decided)
- Draft outline of root ARCHITECTURE (and siblings). Required root sections:
  Context & inputs (REQ / RETRO / prior pipe — product vs process split);
  Target research architecture (roles, phases, flows);
  Schema & evidence contracts as decided;
  Pipe-docs layout & package lifecycle;
  Human deliverable (call-sheet) vs research packages;
  Coexistence with prior pipe (paths); explicit reuse vs do-not-copy;
  Open questions;
  Explicit “Not in this doc”: NEW STORY/pkg; mass collection run; invent facts
- Open Unknowns list
- Proposed interview report path + Related link rows for each input that exists
STOP. Wait for «запиши».

## Phase 3 — Materialize (только по «запиши»)
1) python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
   Use utc_date / utc_now from stdout only.
2) Write research architecture doc(s) as agreed. Root must link every provided input
   (REQ, RETRO, prior charter/ARCHITECTURE as etalon). Title: target research architecture — not “implementation tasks”, not “collected firms”.
3) Write interview report (NEW reports use this prefix only):
   {$researchRoot}/requirements/zeya888.target-research-arch-interview-<slug>-<utc_date>.md
   (if requirements/ missing and operator chose another analysis zone — use that zone; do not scatter silently)
   slug = $archPackageSlug or REQ id/stem; do not invent a new REQ number.
   Required sections: inputs + use-case; Prior-pipe scope line; level classify; verbatim decision log
   (question → options analytics summary → agent recommendation → operator decision accepted|overridden → answer);
   open Unknowns; link matrix inputs ↔ arch root ↔ report;
   method note «REQ ≠ target research arch ≠ execution packages ≠ new STORY»;
   method note «gov competent authority ≠ commercial intermediary» when INT-family;
   method note «recommendation advisory; operator decides»;
   method note «name ≠ create: prompt/schema bodies only if this materialize wave explicitly included them».
4) Patch links only (do NOT rewrite REQ DoD/AC unless operator explicitly asked):
   - $requirementDoc → Related / Architecture: arch root + interview report.
   - $retroDoc → thin Related link if present.
5) Reply: arch root | siblings | report | link patch summary | handoff:
   - optional: operator orders full prompt-kit authoring wave (separate explicit ask)
   - optional: orchestrator run for data collection (separate explicit ask)
   - No second architecture prompt. No P3 code. No silent web scrape of intermediaries.

## analysis.mdc gates (hard)
- Name ≠ create: do not scaffold empty schemas, empty prompt bodies, or pipe-docs CSV because a future AC named a path — unless this materialize wave explicitly ordered those bodies.
- Ask-scoped delivery: materialize only on «запиши».
- No plan-over-ask.
- Claims only from: REQ path, RETRO path, prior-pipe path, operator answers in this chat.
- Do not smuggle NEW STORY/pkg/task scaffolding or invented intermediary rows into architecture docs.
```

---

## Примечания (не в copy-paste)

- **Decision points:** analytics по опциям + fit к prior pipe/RETRO + обязательная рекомендация; **решение за оператором**. ОЯЗ-расшифровка вариантов — [`decision-point-human-language.md`](./decision-point-human-language.md) (companion; не заменяет HARD protocol).
- **Зоны:** research SSOT под `$researchRoot` (charter / ARCHITECTURE / prompts / schema rules); interview = `…/requirements/zeya888.target-research-arch-interview-…` (или зона, выбранная в интервью).
- **Не путать** с [`target-tech-architecture.md`](./target-tech-architecture.md): там код/runtime/packaging; здесь research-pipe.
- **Prior pipe:** эталон REGMAP читать, не переписывать; новый `project_id` параллелен.
- **Materialize scope:** по умолчанию architecture docs + interview report + thin REQ links. Полные тела N промптов / CSV schema files — только если оператор в Phase 1–2 явно включил их в эту волну «запиши».
- Human layer (Architect Studio): [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md) — контекст студии; research-pipe не обязан идти в P1.3 stories.
- Связанные: [`target-tech-architecture.md`](./target-tech-architecture.md), [`decision-point-human-language.md`](./decision-point-human-language.md).  
  Floou INT REQ/RETRO (пример входа): `Floou/docs/analysis/eu-agencies-collector/requirements/`.
