# Dialog restore extract — Cross-project system analysis

**UTC:** 2026-11-18T17:17:06Z · link validate-96 analysis  
**Prompt:** [`../../prompts/migration/migration-dialog-restore-extract-root-cross.md`](../../prompts/migration/migration-dialog-restore-extract-root-cross.md) · fixup [`../../prompts/migration/migration-dialog-restore-extract-fixup.md`](../../prompts/migration/migration-dialog-restore-extract-fixup.md)  
**Method:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

## Identity

| Field | Value |
|-------|-------|
| dialogTitle | `Cross-project system analysis` |
| rootKind | `doge_platform` |
| clientId | _(empty — not client_tenancy)_ |
| workspace_root | `/Users/eslinko/Development/DOGEstonia` |
| transcript / agent-store id | `4bd38bd5-f2e2-48be-a302-46f02097f165` |
| slug | `cross-project-system-analysis` |
| extract path | `docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/cross-project-system-analysis-extract.md` |
| Suggested HTML card | `id="cross-project-system-analysis"` · `data-title="Cross-project system analysis"` · `data-role="Cross"` |

Restore-console card **Present** in [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html) (lines ~188–261).  
Peer bridge under `analysis/dialog-bridges/`: **Absent** (`cross-project-system-analysis-bridge.md` not on disk).

## Bootstrap SSOT (orientation init)

| Item | Path |
|------|------|
| Orientation prompt (read from disk) | `docs/methodology/Zeya888-builder-queue/prompts/architect/cross-project-system-orientation.md` |
| Primer SoT | `docs/modules/dashboard/search-matching-interviews/00-architecture-primer.md` |
| Supporting `@` | `docs/analysis/` · `docs/modules/` · `.cursor/rules/analysis.mdc` |
| `$topic` / `$focusModule` in default fence | empty (match restore HTML Cross card; historical values → Overlay) |

### Filled default paste block

```text
@.cursor/rules/analysis.mdc
@docs/modules/dashboard/search-matching-interviews/00-architecture-primer.md
@docs/analysis/
@docs/modules/
$topic=
$focusModule=

Cross-project system orientation (Architect Studio pre-PA).
Projects in scope: doge-complaints-gateway, doge-identity-service, spa-app, GPT UI (+ root docs).

MODE: read-only orientation + code verify only.
STOP after Phase A–C tables in chat.
Do NOT: materialize EPIC/STORY/REQ/pkg; do NOT copy PA/P1; do NOT edit files;
      do NOT propose next actions beyond clarifying questions.
Code claims: only after Read/Grep with path:line; else Unknown.
Wait for my explicit go-ahead before any Studio/Builder step.

Жёстко (analysis.mdc + MODE):
- Только факты из прочитанных файлов / кода. Нет assumptions, нет silent invent.
- Code claim — только после Read/Grep с path:line; иначе Unknown. Doc claim — с path.
- Не edit файлов; не materialize EPIC/STORY/REQ/pkg; не копировать PA/P1 в ответ.
- Product Story Done ≠ «нашли gaps» / ≠ таблица candidates.

Reading order (не «весь монорепо»):
1) @docs/modules/dashboard/search-matching-interviews/00-architecture-primer.md — SoT system map для текущего stack.
2) @docs/modules/ (+ $focusModule если задан) — product/concept modules.
3) @docs/analysis/ — сквозная integration analytics.
4) Опц. concept: docs/network-architecture/; docs/DOGEstonia.md — помечай legacy/возможно устаревшее.
5) Per-project one-pagers только после primer, по необходимости:
   - doge-complaints-gateway/docs/high-level-description.md
   - GPT UI/docs/concept-and-goals.md
   - identity / spa: architecture или runtime-docs (пути — только после verify exists)
6) Descent-канон (для сверки, не как единственный SSOT):
   {gateway|identity|spa|GPT UI}/docs/requirements/ и соответствующий docs/tasks/

Единого docs/requirements/ в корне НЕТ — слой фрагментирован; опиши карту «где искать FR» как есть.

## Phase A — System orientation (карта, не stories)
Выход:
1) Один абзац product concept (DOGEstonia / civic signals).
2) Таблица 4 компонентов: роль | стек | trust boundary | ключевые inbound/outbound.
3) Сквозной data flow: GPT UI → gateway → Issues → spa-app; identity поперёк.
4) Privacy invariant (gateway без PII vs identity) — из primer, со ссылкой на path.
5) Раздел Verified vs Unknown (Unknown → вопросы, не выдумки).

## Phase B — Cross-project requirements analytics
1) Карта слоёв: docs/modules (product FR) | docs/analysis (integration) | per-project docs/requirements (исполнение Builder).
2) Для $topic или выбранного модуля / $focusModule:
   - кандидаты в modules + analysis (read/grep);
   - сверка с per-project REQ / backlog stories (exists? overlap?).
3) Gap table:
| Claim | Source path | Status (in-docs / in-code-unverified / missing) | Owning project(s) |

Code status = in-code-unverified, пока нет path:line verify. Не утверждай «есть в коде» без Read/Grep.

## Phase C — Descending story candidates (in chat only)
Таблица (только в чате; не materialize; не запускай Studio/Builder):
| Candidate | Why | Primary project | Deps | Suggested intake label (PA.2 / PA.3 / P1.1) |

Suggested intake = метка типа intake, НЕ инструкция «скопируй PA.x» / «открой Builder».
Не предлагай copy PA/P1 и не предлагай следующие шаги Studio/Builder, пока оператор не дал explicit go-ahead.

## End of reply
Handoff: none.
Reply ends with: (1) Verified code facts (path:line only) (2) clarifying questions only.
Do not suggest next Studio/Builder steps.
```

## Context transfer

### Mission

Долгоживущий **Cross / doge_platform** диалог: карта classic-four + фрагментированный FR-слой (`docs/modules` · `docs/analysis` · per-project REQ) → Architect Studio pre-PA волны (parent→child, gap process). Поздние волны этого store = **aibridge child REQ-14** (seamless TG orchestration) → Option-1/2 closeout → **STORY-96**. **Не** single `builder_project` O/V role-lock. Init после wipe = orientation fence выше, не OP/VAL bootstrap.

### Active goal — aibridge REQ-14 (restore SSOT)

**Product (one paragraph):** гражданин в Telegram рассказывает историю → aibridge сам ведёт prepare (extractor→checker→normalizer, уточнения без новой «дальше») → обзор того же кандидата → **Отправить**; Looks right **не** обязателен в новом маршруте; free-text «отправляй» **не** шлёт в gateway.

| Item | Path / fact |
|------|-------------|
| Parent product | [`docs/requirements backlog/REQ15-DOGEstonia-Interview-DeepSeek-And-Telegram-Channel.md`](../../../../../docs/requirements%20backlog/REQ15-DOGEstonia-Interview-DeepSeek-And-Telegram-Channel.md) |
| Child REQ (aibridge) | [`doge-ai-bridge/docs/requirements/REQ-14-REQ15-SEAMLESS-ROLE-ORCHESTRATION-TELEGRAM.md`](../../../../../doge-ai-bridge/docs/requirements/REQ-14-REQ15-SEAMLESS-ROLE-ORCHESTRATION-TELEGRAM.md) |
| Status now | **Draft — awaiting PA.2** · **≠ Accepted** (Meta re-read 2026-11-18T14:50:18Z) |
| Package INDEX | [`…/req-14-req15-seamless-role-orchestration/INDEX.md`](../../../../../doge-ai-bridge/docs/tasks/backlog-stories/req-14-req15-seamless-role-orchestration/INDEX.md) |
| Arch | [`doge-ai-bridge/docs/architecture/req15-seamless-role-orchestration/`](../../../../../doge-ai-bridge/docs/architecture/req15-seamless-role-orchestration/) |
| **Org goal after wipe** | Reach **REQ-14 Accepted** only via Option-2 **A→E** + explicit operator «да» — [`req14-option2-accepted-next-steps-2026-11-18.md`](../../../../../doge-ai-bridge/docs/analysis/req14-option2-accepted-next-steps-2026-11-18.md) |

```text
A honesty+smoke → B CODE 96/AC-21 → C live EP → D org P7/P8 → E Accepted (explicit only)
```

**Current proximity (disk):** B **Met** on tip **96** · C Keep (EP) · D org open (96 next P7; 87/90 Product/P8 PENDING) · E **not** stamped.

### Dialog arc (ordered; confirmed from agent-store + disk)

1. **Closed — Orientation Phase A–C (2026-09-30):** paste Cross orientation · `$topic` = симуляционные данные в систему · `$focusModule` = gateway, identity, threads · Phase A–C tables in chat · no materialize that turn.  
2. **Closed — Life-sim node load interview (2026-10-03):** `life-sim-node-load-run.md` + gateway life-sim manual · interview before wipe/load · orientation already Present.  
3. **Closed — Parent REQ13 → child REQs (2026-10-13):** `parent-requirement-to-project-reqs` · targets gateway / aibridge / spa · children materialized after go-ahead (e.g. aibridge REQ-09 Present on disk).  
4. **Closed — Parent REQ15 → children + instruction locks (2026-10-31+):** targets aibridge / telegram / spa / gateway · GPT UI REQ-48 + aibridge REQ-12/13 family · Lock C hybrid instructions SSOT cited in arc.  
5. **Closed — REQ15 gap-process docs wave:** `docs/analysis/req15-gap-*` / triage / process Present under `docs/analysis/`.  
6. **Historical — STORY-96 Layer-1 authoring:** REQ-14 Option-2 B vehicle authored as Todo `CODE_REQUIRED` · 86 docs parent ≠ reopen (extract first wave).  
7. **Current tip (now):** **[STORY-AIBRIDGE-96](../../../../../doge-ai-bridge/docs/tasks/backlog-stories/req-14-req15-seamless-role-orchestration/STORY-AIBRIDGE-96-prepare-interrupt-same-run-resume-runtime.md)** · **P5 Done** · Finish Line **Met** · tip pkg-000099 · next **P7** · ≠ reopen as CODE Todo · REQ-14 Status Draft ≠ Accepted · 86 docs parent Keep.  
8. **Closed — restore extract Written** · tip-honesty fixup · **this deepen:** REQ-14 + STORY-96 restore depth · no HTML · no product code · no dialog-bridges/.

### Verified state

| Check | Result |
|-------|--------|
| Primer on disk | Present · `docs/modules/dashboard/search-matching-interviews/00-architecture-primer.md` (dated 2026-06-30) |
| `docs/modules/` · `docs/analysis/` | Present (dirs) |
| Classic-four dirs | Present: `doge-complaints-gateway` · `doge-identity-service` · `spa-app` · `GPT UI` |
| Restore card Cross | Present · `id=cross-project-system-analysis` · `data-role=Cross` |
| Orientation SSOT | Present · `prompts/architect/cross-project-system-orientation.md` |
| Parent REQ13 / REQ15 backlog | Present under `docs/requirements backlog/` |
| STORY-AIBRIDGE-96 | **P5 Done** · Finish Line **Met** · next **P7** · UTC `2026-11-18T14:26:59Z` (Meta re-read) |
| Peer `*-bridge.md` for this title | **Absent** |
| Exact completeness of every interim Studio wave in JSONL | **Unknown** (not fully re-read; arc bullets = confirmed milestones only) |

### Tip honesty (current)

| Tip path | Meta Status | Finish Line / Delivery | Next | UTC of Meta / re-read |
|----------|-------------|------------------------|------|------------------------|
| STORY-AIBRIDGE-96 | 🟢 **Product Done** · tip pkg-000099 · P8 | `CODE_REQUIRED` **Met** · AC-96-01…08 `[x]` | **DONE** | 2026-11-18T15:11:25Z · validate [`req14-story-96-…`](../../../../../doge-ai-bridge/docs/analysis/req14-story-96-validate-vs-req14-2026-11-18.md) |
| STORY-AIBRIDGE-86 | 🟡 P5 Done · docs parent | tip ≠ product Met alone · residual owned by **96 Met** · ≠ reopen | P7 | 2026-11-18 |
| REQ-14 | Draft — awaiting PA.2 | ≠ Accepted | Option-2 **C** live EP / **D** org / **E** explicit only | 2026-11-18T14:50:18Z |

> **Stale-doc trap:** [`req14-option1-91-92-validate-vs-req14-2026-11-18.md`](../../../../../doge-ai-bridge/docs/analysis/req14-option1-91-92-validate-vs-req14-2026-11-18.md) and gap rows may still say «96 Open / CODE_REQUIRED Todo». Prefer **this Tip honesty table + story Meta/INDEX** + code/goal validate [`req14-story-96-validate-vs-req14-2026-11-18.md`](../../../../../doge-ai-bridge/docs/analysis/req14-story-96-validate-vs-req14-2026-11-18.md) (B Met · Accepted No · 50 passed) over those prose rows.

### Multi-iteration map (REQ-14 closeout waves)

| Wave | What (disk) | Outcome vs Accepted |
|------|-------------|---------------------|
| REQ15 parent→children | aibridge / telegram / spa / gateway + GPT UI REQ-48 | children Draft · ≠ Accepted |
| Looks-right residual | **87** Closed harness · **88** docs → **90** Met harness | ≠ Accepted · Product/P8 org PENDING |
| Soft reply quality | **91** (REQ-12) `CODE_REQUIRED` Met | ≠ invent REQ-12/14 Accepted |
| Journey Package Gate | **92** PACKAGE_GATE Met · Product Done | necessary · **not** sufficient for Accepted |
| Option-1 docs honesty | **93** Finish Line · **94** REQ↔INDEX · **95** Accepted blockers fence | Done · fence names C/D/E |
| Validate 91/92 vs REQ-14 | [`req14-option1-91-92-validate…`](../../../../../doge-ai-bridge/docs/analysis/req14-option1-91-92-validate-vs-req14-2026-11-18.md) | Accepted **No** |
| Validate **96** vs REQ-14 (code+goal) | [`req14-story-96-validate-vs-req14-2026-11-18.md`](../../../../../doge-ai-bridge/docs/analysis/req14-story-96-validate-vs-req14-2026-11-18.md) | **B Met** · Accepted **No** · pytest 50 |
| Interrupt chain | **83** surface+library → **86** docs parent → **96** runtime AC-21 | Option-2 **B Met** on tip 96 |
| Option-2 remaining | **C** live EP · **D** org P7/P8 · **E** Accepted explicit | **Open** |

**Process / analysis pointers (do not invent; re-read on restore):**

- Option-1 process: [`req14-option1-anti-circle-closeout-process-2026-11-17.md`](../../../../../doge-ai-bridge/docs/analysis/req14-option1-anti-circle-closeout-process-2026-11-17.md)
- Residual gap: [`req15-looks-right-residual-target-gap-2026-11-17.md`](../../../../../doge-ai-bridge/docs/analysis/req15-looks-right-residual-target-gap-2026-11-17.md)
- Inventory / AC vulns: [`req14-child-req-story-inventory-2026-11-17.md`](../../../../../doge-ai-bridge/docs/analysis/req14-child-req-story-inventory-2026-11-17.md) · [`req14-ac-tech-solution-vulnerabilities-by-layer-2026-11-17.md`](../../../../../doge-ai-bridge/docs/analysis/req14-ac-tech-solution-vulnerabilities-by-layer-2026-11-17.md)
- AC gap reaudit: [`req15-req14-target-ac-gap-reaudit-2026-11-13.md`](../../../../../doge-ai-bridge/docs/analysis/req15-req14-target-ac-gap-reaudit-2026-11-13.md)
- Live EP: [`story-85-req14-live-evidence-explicit-partial-20261113.md`](../../../../../doge-ai-bridge/docs/analysis/story-85-req14-live-evidence-explicit-partial-20261113.md)

### STORY-96 deep packet (last story sent to work)

**Why it exists:** tip **86** is P5 Done / docs parent — **cannot** hand as Todo to CODE. **96** is the clean `CODE_REQUIRED` vehicle for product-path **AC-AIB-14-21** (Option-2 §B). Soft Keep: **83** interrupt surface · **79** product façade · **76** budgets · fence **95**.

**Solves (observable):** after mid-prepare interrupt (`interrupted_retryable`), product prepare entry (Prepare CTA **and/or** structured/channel prepare entry sharing the unified gate) must:

1. Resume the **same** `active_run_id` via CAS, **or**
2. Expose **explicit** citizen-visible retryable interrupted —

and must **not**: eternal processing · silent new `run_id` as «resume» · Pass from library-only `resume_prepare_after_interrupt`.

**Meta now (disk):** re-Read story Meta (Product Done / P8 may supersede older P5 tip prose) · Finish Line **Met** · tip pkg-000099 · Done ≠ REQ-14 Accepted.  
**Code+goal validate SSOT:** [`req14-story-96-validate-vs-req14-2026-11-18.md`](../../../../../doge-ai-bridge/docs/analysis/req14-story-96-validate-vs-req14-2026-11-18.md) — AC table path:line · Option-2 scorecard · **50 passed** · **B Met** · Accepted **No**.

**Evidence on disk:**

| Piece | Fact |
|-------|------|
| Entry gate | `prepare.py` ~L85–125 (interrupted → resume, no uuid4 as resume) · arch `06` §86 As-built |
| Fresh prepare | uuid4 after gate Keep (`prepare.py` ~L127) |
| Harness owned by 96 | [`tests/test_story_96_prepare_interrupt_same_run_resume_runtime.py`](../../../../../doge-ai-bridge/tests/test_story_96_prepare_interrupt_same_run_resume_runtime.py) · story claims **9 passed** |
| Tip-86 suite | `tests/test_story_86_*` may exist · **≠** alone Met under 96 Finish Line |
| Older Option-2 «uuid4 Absent» | **Stale** vs as-built gate |

**AC spine (01…08) — restore must re-check checkboxes on story:**

| AC | Pass means | Key FAIL |
|----|------------|----------|
| 01 | same `run_id` on product prepare entry after interrupt · CTA+structured same gate | new `run_id` as resume · library-only proof · split gate |
| 02 | continue product path same `run_id` · no hung processing | silent `run_id` switch · entered with no hop evidence |
| 03 | cas_mismatch → explicit interrupted | silent fresh prepare as resume |
| 04 | non-interrupted → fresh `run_id` Keep | interrupt-gate blocks ordinary prepare |
| 05 | free-text while interrupted ≠ alone resume (83 Keep) | free-text resumes/starts prepare as CTA |
| 06 | product-path harness covers 01…05 under **96** | only library CAS green · tip-86-alone Pass · Code WAIVE |
| 07 | 83 regression Keep | break interrupt surface / library CAS · reopen 83 Todo |
| 08 | Done ≠ Accepted · live not required · 86 ≠ Todo | invent Accepted from 96 alone |

**How to re-validate STORY-96 after wipe**

1. Read Meta: Status · Finish Line · AC-96-01…08 `[x]` · next.  
2. Harness:

```bash
cd doge-ai-bridge
.venv/bin/python -m pytest tests/test_story_96_prepare_interrupt_same_run_resume_runtime.py -q
```

3. Optional Option-2 A1 peer smoke (87+90+91+92) from Option-2 doc.  
4. Optional manual A2 step 4: mid-prepare interrupt → Prepare again → same `run_id` **or** explicit retryable interrupted.  
5. **FAIL** if Met claimed only from `test_story_86_*` or library resume outside product prepare entry.  
6. Story Done still **≠** invent REQ-14 Accepted / live SUCCESS.

### Proximity validator — distance to REQ-14 Accepted

Restore agent runs this **after** orientation Phase A–C (or immediately if reclaiming REQ-14 tip). **Disk Meta first.**

```text
Goal = REQ-14 Status Accepted (explicit operator «да» only).
Distance = remaining Option-2 gates (A…E).

1) Read REQ-14 Status.
   - If Accepted without recorded explicit order → honesty FAIL (do not invent).
   - Expected now: Draft ≠ Accepted.

2) Re-Read Tip honesty / story Meta:
   - 96 Finish Line Met? next P7?
   - 86 docs parent ≠ Todo?
   - 92 Package Gate Met? 91 Met? 95 fence Done?

3) Option-2 scorecard (fill Met / Open / Keep):
   A smoke — pytest 87/90/91/92 (+96)
   B CODE AC-21 — 96 Finish Line Met (current) · ≠ reopen 86
   C live EP — Keep unless recorded live SUCCESS (story-85); mocks ≠ Pass
   D org P7/P8 — INDEX: 87/90 Product Done PENDING · 92 Product Done · 96 next P7 · tip 91 org
   E Accepted — only after B+C+D + explicit «да» + reaudit AC-AIB-14-01…24 vs evidence

4) Stale-doc trap: gap/option1-validate may say «96 Open» → prefer Meta/INDEX/Tip honesty + [`req14-story-96-validate-vs-req14-2026-11-18.md`](../../../../../doge-ai-bridge/docs/analysis/req14-story-96-validate-vs-req14-2026-11-18.md).

5) Report one block:
   Met gates | Open gates | next safe ask | never invent Accepted/live SUCCESS
```

**Distortion fence (must keep):**

- Story / Finish Line Done ≠ REQ-14 Accepted.  
- Harness Pass ≠ live Railway/TG SUCCESS.  
- Option-1 complete (91/92/93–95) ≠ Option-2 Accepted.  
- tip-86 P5 Done ≠ AC-21 product Met (owned by **96**, now Met).  
- Package Gate **92** Met ≠ full AC-05…24 Pass / Accepted.

### Map Present/Absent (doge_platform)

| Layer | Status |
|-------|--------|
| Classic-four components (primer §3) | **Present** in primer: gateway · identity · spa · GPT UI (+ agreements/web3 marked future/out) |
| Data-flow GPT UI → gateway → Issues → spa; identity cross-cut | **Present** primer §4 |
| Privacy invariant (gateway no PII vs identity) | **Present** primer §5 |
| FR map: `docs/modules` (product) \| `docs/analysis` (integration) \| `{project}/docs/requirements` (Builder) | **Present** as fragmented layout · **no** single root `docs/requirements/` |
| Client tenancy MS table | **N/A** this rootKind (use Alvasar Root extract if needed) |

### Decisions locked

- Init after wipe = **full Cross orientation fence** (not OP/VAL migration-role-bootstrap).  
- analysis.mdc: path:line or Unknown · name ≠ create · no invent Accepted/live SUCCESS.  
- Studio/Builder/scatter materialize only after explicit operator go-ahead.  
- STORY-96 Finish Line **Met** · tip-86 ≠ Todo handoff · **REQ-14 Accepted still Open** (Draft).  
- Option-2 path A→E is the Accepted route; B closed on tip 96; C/D/E remain.  
- Historical first-wave topic (life-sim / simulation data) ≠ default empty `$topic` in HTML card — restore via Overlay if reclaiming that thread.

### Forbidden

- Scatter / Studio / Builder / child REQ write without go-ahead.  
- Product code / commit / push unless explicitly ordered.  
- Edit `dialog-restore-console.html` in extract-only runs.  
- Write under `analysis/dialog-bridges/`.  
- Encyclopedia dump — pointers + full orientation + overlay only.  
- Claim REQ-14 Accepted from Option-1 / 92 / 96 alone.

### Focus paths (relevant to recent tip + orientation)

- `docs/modules/dashboard/search-matching-interviews/00-architecture-primer.md`  
- `docs/analysis/` (REQ15 gap / stitch / readiness notes)  
- `docs/requirements backlog/REQ15-DOGEstonia-Interview-DeepSeek-And-Telegram-Channel.md`  
- `docs/requirements backlog/REQ13-DOGEstonia-Issue-Sense-Brief-And-Civic-Poster.md`  
- `doge-ai-bridge/docs/requirements/REQ-14-REQ15-SEAMLESS-ROLE-ORCHESTRATION-TELEGRAM.md`  
- `doge-ai-bridge/docs/tasks/backlog-stories/req-14-req15-seamless-role-orchestration/INDEX.md`  
- `doge-ai-bridge/docs/tasks/backlog-stories/req-14-req15-seamless-role-orchestration/STORY-AIBRIDGE-96-prepare-interrupt-same-run-resume-runtime.md`  
- `doge-ai-bridge/docs/tasks/backlog-stories/req-14-req15-seamless-role-orchestration/STORY-AIBRIDGE-86-prepare-interrupt-same-run-resume.md`  
- `doge-ai-bridge/tests/test_story_96_prepare_interrupt_same_run_resume_runtime.py`  
- `doge-ai-bridge/docs/architecture/req15-seamless-role-orchestration/06-residual-ac-closeouts.md`  
- `doge-ai-bridge/docs/analysis/req14-option2-accepted-next-steps-2026-11-18.md`  
- `doge-ai-bridge/docs/analysis/req14-option1-91-92-validate-vs-req14-2026-11-18.md`  
- `doge-ai-bridge/docs/analysis/req14-story-96-validate-vs-req14-2026-11-18.md`  
- `doge-ai-bridge/docs/analysis/req14-option1-anti-circle-closeout-process-2026-11-17.md`  
- `doge-ai-bridge/docs/analysis/req15-looks-right-residual-target-gap-2026-11-17.md`  
- `doge-ai-bridge/docs/analysis/p4-audit-STORY-AIBRIDGE-96-prepare-interrupt-same-run-resume-runtime-20261118.md`  
- `doge-ai-bridge/docs/analysis/p5-disposition-STORY-AIBRIDGE-96-prepare-interrupt-same-run-resume-runtime-20261118.md`  
- `docs/methodology/Zeya888-builder-queue/prompts/architect/cross-project-system-orientation.md`  
- `docs/methodology/Zeya888-builder-queue/guides/from-cross-project-req-to-story-packages.md`

## Starting focus packet

### 1) Default filled orientation

(Same FULL fence as Bootstrap SSOT above — Phase A–C intact.)

### 2) Overlay — must not lose after wipe

> **HTML merge:** append after init completes («AFTER orientation Phase A–C completes…»). **Never replace** orientation init.

```text
### OVERLAY — Cross-project system analysis (append after orientation Phase A–C)

rootKind: doge_platform · card: Cross · agent-store: 4bd38bd5-f2e2-48be-a302-46f02097f165
clientId: (empty)

ACTIVE GOAL (must not lose):
- aibridge child REQ-14 (parent REQ15): seamless TG prepare→draft→Send · Looks right not required · free-text «отправляй» does not send
- Status Draft ≠ Accepted · path to Accepted = Option-2 A→E + explicit «да» only
- Proximity now: B(AC-21/96) Met · C live EP Keep · D org P7/P8 open · E not stamped
- After restore: run «Proximity validator» section in this extract (disk Meta first)

DONE / KEEP:
- Orientation Phase A–C historically (2026-09-30) topic=simulation/life-sim · focusModule=gateway,identity,threads
- Life-sim node-load interview (prompt2 + gateway manual) — re-read manual if reclaiming load
- Parent→child REQ13 / REQ15 — children Present; Draft ≠ Accepted unless Status says so
- Looks-right residual: 87 Closed · 88→90 Met harness · Product/P8 org PENDING
- Option-1: 91 Met · 92 Package Gate Met · 93/94/95 docs Done · fence 95 names Accepted blockers
- Interrupt chain: 83 → 86 docs parent → 96 runtime · 86 ≠ reopen as Todo
- STORY-96 solves AC-21 product-path same-run resume (or explicit interrupted) · Finish Line Met · pkg-000099 · next P7 · UTC 2026-11-18T14:26:59Z
- Validate 96: Read Meta + pytest tests/test_story_96_prepare_interrupt_same_run_resume_runtime.py · FAIL if library-only / tip-86-alone
- Code+goal analysis Present: doge-ai-bridge/docs/analysis/req14-story-96-validate-vs-req14-2026-11-18.md (B Met · Accepted No · 50 passed)
- Restore extract deepen Present: REQ-14 packet · iteration map · 96 deep · proximity validator

OPEN / NEXT SAFE ASK — derive from Tip honesty + proximity scorecard only:
- (a) re-orient cold map only
- (b) STORY-96 next P7 / Product Done org (NOT «CODE Todo» — Finish Line already Met)
- (c) Option-2 C live EP Keep / honest live window (story-85)
- (d) Option-2 D org P7/P8 on 87/90/91 (+96)
- (e) Option-2 E Accepted talk — only after B+C+D + explicit operator «да» + AC-01…24 reaudit
- (f) other named parent/topic — do not invent
- ≠ invent live SUCCESS / REQ-14 Accepted
- Stale trap: gap/validate may say «96 Open» → prefer Meta/INDEX
- If reclaiming life-sim: life-sim-node-load-run + manual §4 before wipe/load

Hard bans: no HTML edit this extract wave; no dialog-bridges write; no OP/VAL role-bootstrap as Cross init; name ≠ create; analysis.mdc.
```

## Smoke checklist

- [x] Title matches sidebar / restore card `Cross-project system analysis`
- [x] rootKind `doge_platform` ↔ `cross-project-system-orientation.md`
- [x] clientId empty (not client_tenancy)
- [x] Orientation fence complete (Phase A–C present, not shortened)
- [x] Starting focus = orientation + overlay
- [x] Tip honesty table Present (96 / 86 / REQ-14)
- [x] Overlay OPEN consistent with Meta (no stale CODE Todo on 96)
- [x] Historical arc ≠ current tip conflated
- [x] REQ-14 Active goal + iteration map Present
- [x] STORY-96 deep packet + re-validate recipe Present
- [x] Proximity validator checklist Present
- [x] Orientation fence Phase A–C unchanged (not rewritten)
- [x] No invent beyond disk + confirmed arc (Unknowns named)

## Notes for later HTML merge

| Item | Suggestion |
|------|------------|
| Card id / data-role | Keep `cross-project-system-analysis` · **Cross** |
| Paste strategy | Keep full orientation init in `<pre>`; append `@` this extract / overlay after «AFTER orientation Phase A–C completes…» |
| Peer bridge | None Present — skip body copy |
| HTML edit | Separate operator ask after more Root/Cross extracts land |
