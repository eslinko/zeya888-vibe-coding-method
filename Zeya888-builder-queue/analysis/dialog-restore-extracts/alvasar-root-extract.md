# Dialog restore extract — Alvasar Root

**UTC:** 2026-11-18T14:40:25Z · tip-honesty re-read this turn  
**Prompt:** [`../../prompts/migration/migration-dialog-restore-extract-root-cross.md`](../../prompts/migration/migration-dialog-restore-extract-root-cross.md)  
**Method:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

## Identity

| Field | Value |
|-------|-------|
| dialogTitle | `Alvasar Root` |
| rootKind | `client_tenancy` (operator wrote `client/Alvasar` → mapped to taxonomy) |
| clientId | `alvasar` (`clients.yaml` key; display Alvasar) |
| workspace_root | `/Users/eslinko/Development/DOGEstonia` |
| transcript / agent-store id | `0f44bc5d-c356-450a-87ca-2a9d9f6c1460` (Current agent store / this Root chat lineage) |
| slug | `alvasar-root` |
| extract path | `docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/alvasar-root-extract.md` |
| Suggested HTML card | `id="alvasar-root"` · `data-title="Alvasar Root"` · `data-role="Root"` |

Restore-console card **Present** in [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html) (~L127–185).  
Peer bridge under `analysis/dialog-bridges/`: **Absent** (`alvasar-root-bridge.md` not verified this turn).

**Operator focus (overlay):** `$topic` / `$focusModule` = all across backend, ui, gpt.

---

## Bootstrap SSOT (orientation init)

| Item | Path |
|------|------|
| Orientation prompt | `docs/methodology/Zeya888-builder-queue/prompts/architect/client-product-root-orientation.md` |
| Supporting `@` | `guides/client-tenancy.md` · `specs/clients.yaml` · `specs/profiles.yaml` · `.cursor/rules/analysis.mdc` |
| `$clientId` | `alvasar` |
| `$topic` / `$focusModule` in default fence | filled from operator (all across backend, ui, gpt) |

### Filled default paste block

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/client-tenancy.md
@docs/methodology/Zeya888-builder-queue/specs/clients.yaml
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
$clientId=alvasar
$topic=all across backend, ui, gpt
$focusModule=all across backend, ui, gpt

Client product root orientation (Architect Studio pre-PA — client tenancy).
Resolve client from clients.yaml for $clientId (root, parent_requirements_dir, profiles[]).

MODE: read-only orientation + disk verify only.
STOP after Phase A–C tables in chat.
Do NOT: materialize EPIC/STORY/REQ/pkg; do NOT copy PA/P1; do NOT edit files;
      do NOT create app scaffold (pyproject / Expo / package.json) — name ≠ create.
Code claims: only after Read/Grep with path:line; else Unknown.
Wait for my explicit go-ahead before scatter / Studio / Builder.

Жёстко (analysis.mdc + MODE):
- Только факты из прочитанных файлов. Нет assumptions, нет silent invent.
- Doc claim — с path. Code claim — path:line после Read/Grep; иначе Unknown.
- Не edit; не materialize EPIC/STORY/child REQ/pkg в этом прогоне.
- Не путать $clientId с builder_project (profiles = keys listed under clients.yaml).

Reading order:
1) @guides/client-tenancy.md + @specs/clients.yaml — model + $clientId entry.
2) Parent REQ INDEX + files under client parent_requirements_dir (exists?).
3) Optional: client docs/analysis/ (scaffold starting points — name ≠ create).
4) For each profile key in clients.yaml → profiles.yaml: focus_folder, tasks_dir, plan_file, stack_label.
5) Per-MS bullrun «Актуальная точка» only if tasks_dir exists — status of bootstrap vs product work.

## Phase A — Client orientation (карта, не stories)
Выход:
1) Один абзац product concept из parent REQ (или Unknown).
2) Таблица MS: profile key | focus_folder | stack | role (backend/ui/…) | parent vs child REQ path.
3) Portable pack: `.cursor/plans/` under client root Present/Absent; dual-sync note from client-tenancy.
4) Verified vs Unknown.

## Phase B — Topic analytics ($topic)
1) Что уже сказано в parent REQ по $topic (path + §).
2) Что относится к какому profile key (без invent FR).
3) Gap table:
| Claim | Source path | Status (in-docs / missing / Unknown) | Owning profile(s) |

## Phase C — Next steps (in chat only; не запускай)
Таблица:
| Candidate next | Prompt / action | Notes |
| Client child REQs | cross-project-req-scatter with $targetProjects=<csv from clients.yaml profiles> | parent = client REQ path |
| Tech architecture per MS | target-tech-architecture | after child REQ |
| Builder session | session-starter / migration-* with builder_project=<profile key> | not $clientId |

Suggested intake = метка, НЕ «открой Builder сейчас».
```

---

## Context transfer

### Mission

Долгоживущий **client_tenancy Root** для Alvasar: карта multi-MS (`alvasar-backend` · `alvasar-ui` · `alvasar-gpt`) под `clients/Alvasar/`, parent REQ cascade (REQ0…REQ14), стыки cabinet / Bridge / GPT pack — **не** single `builder_project` O/V role-lock и **не** DOGE classic-four Cross. Init после wipe = client-product-root orientation fence выше.

### Dialog arc (ordered)

**Historical (closed waves — confirmed this lineage + disk):**

1. **Closed — Parent REQ14 cabinet target + children:** UI `08` · backend `13` · gpt `01` Draft/Verified fences; IA v2 Подключения/Анкеты.  
2. **Closed — gpt ALVG-01…03 fence Done:** authorship/manifest/packaging · bodies Absent · O5 Open · tip pkg-000003.  
3. **Closed — backend ALVB-85…88 fence Done** then **89…96 Soft/Open/PA wave Done P8** · tip **ALVB-96** pkg-000098 · tip closed · Soft≠Live Named.  
4. **Closed — UI ADMIN-CTS-01…06 Done** · JOIN [`CTS-BRIDGE-BACKEND-JOIN.md`](../../../../../clients/Alvasar/ui/docs/tasks/backlog-stories/cabinet-target-state-wa-profiles-ai/CTS-BRIDGE-BACKEND-JOIN.md) · STORY-ALVU-CTS-01…18 product/gallery waves.  
5. **Closed — Questionnaire UX handoff** + seam sync docs (analysis.mdc).  

**Current tip (now) — disk Meta this turn:**

| MS | Current tip | Note |
|----|-------------|------|
| alvasar-backend | ALVB-96 **Done P8** tip closed · Soft≠Live | do not invent/activate next ALVB |
| alvasar-ui | ALVU-CTS-18 **Done** tip Active pkg-000042 · Soft≠Live | next authored **CTS-19 Todo** |
| alvasar-gpt | ALVG-03 **Done** tip pkg-000003 · O5 Open | bodies Absent · no invent create without order |

Parent **REQ14** Status: Draft · not implementation Done.

### Verified state (commands + disk)

| Check | Result |
|-------|--------|
| `clients.yaml` alvasar | Present · root `clients/Alvasar` · profiles backend/ui/gpt |
| Parent REQ dir | Present · REQ0…REQ14 under `clients/Alvasar/docs/requirements/` |
| Portable plans under `clients/Alvasar/.cursor/plans/` | Present · Alvasar-Backend/UI/GPT_builder.plan.md |
| backend current tip pointer | `pkg-000098` … `alvb-96-anketa-values-read-host` · activation active |
| ui current tip pointer | `pkg-000042` … `alvu-cts-18-gallery2-ank-combinations` · activation active |
| gpt current tip pointer | `pkg-000003` … `alvg-03-packaging-env-handoff` · activation active |
| Restore HTML card Alvasar Root | Present `id=alvasar-root` |

### Tip honesty (current)

| Tip path | Meta Status | Finish Line / Delivery | Next | UTC of Meta / re-read |
|----------|-------------|------------------------|------|------------------------|
| `clients/Alvasar/backend/docs/tasks/backlog-stories/cabinet-refresh-people-ai-host/STORY-ALVB-96-anketa-values-read-host.md` | **Done (Product)** · **P8 closed** · pkg-000098 · Named Open/PA (Info) · tip closed | Soft docs/suite · **≠ Live Named** · do not invent/activate next · push=no | **Not** CODE Todo on 96 · residual Live after PA → [RESIDUAL-LIVE-PRESENT-AFTER-PA.md](../../../../../clients/Alvasar/backend/docs/tasks/backlog-stories/cabinet-refresh-people-ai-host/RESIDUAL-LIVE-PRESENT-AFTER-PA.md) · operator pick | P8 `2026-11-17T08:42:02Z` · re-read 2026-11-18T14:40:25Z |
| `clients/Alvasar/ui/docs/tasks/backlog-stories/cabinet-target-state-wa-profiles-ai/STORY-ALVU-CTS-18-gallery2-ank-combinations.md` | **Done (Product)** · tip Active pkg-000042 · gate PASS · Soft≠Live | Gallery 2 ANK combos Present · Mock≠Live | **STORY-ALVU-CTS-19** Status **Todo** (PR/EDIT combos) · then CTS-20 Todo | P3 `2026-11-18T11:41:58Z` · re-read 2026-11-18T14:40:25Z |
| `clients/Alvasar/gpt/docs/tasks/backlog-stories/questionnaire-instruction-pack/STORY-ALVG-03-packaging-env-handoff.md` | **Done** · tip pkg-000003 · P3 gate PASS · **O5 Open** | Fence packaging/env handoff · bodies Absent | **Not** invent instruction bodies / O5 Done · create-wave only on operator order | P3 `2026-11-16T07:29:45Z` · re-read 2026-11-18T14:40:25Z |
| `clients/Alvasar/docs/requirements/REQ14-cabinet-target-state-wa-profiles-ai.md` | **Draft** · not implementation Done | Target + cascade feed | Soft parent amend residual (IA lag vs UI `08`) · no claim Done | Amend 2026-11-16 · re-read 2026-11-18T14:40:25Z |

### Map Present/Absent (client_tenancy)

| profile key | focus_folder | stack_label | role | parent vs child REQ |
|-------------|--------------|-------------|------|---------------------|
| `alvasar-backend` | `clients/Alvasar/backend` | Python (API; scaffold deferred) | backend | Parent: `clients/Alvasar/docs/requirements/` · Child: `backend/docs/requirements/` (e.g. `13`) |
| `alvasar-ui` | `clients/Alvasar/ui` | React Native Web (scaffold deferred) | ui | Child: `ui/docs/requirements/` (e.g. `08`) |
| `alvasar-gpt` | `clients/Alvasar/gpt` | GPT Instructions | gpt | Child: `gpt/docs/requirements/` (e.g. `01`) |

| Artifact | Verdict |
|----------|---------|
| Portable `.cursor/plans/` under client root | **Present** (Backend/UI/GPT builder plans) |
| JOIN handoff UI↔backend | **Present** `CTS-BRIDGE-BACKEND-JOIN.md` |
| Live refresh/people/loader/confirm Named on Port | **Absent** (Soft ALVB 85…96 ≠ Live) |
| gpt instruction bodies | **Absent** until create-wave |
| ADMIN-CTS 01…06 | **Done** 6/6 |

### Decisions locked · Forbidden

- **Locked:** clientId `alvasar` · three MS profiles · REQ14 cabinet target · IA v2 · Soft≠Live Named honesty · JOIN as seams explanation (not REQ) · Gallery Soft≠Live.  
- **Forbidden:** invent Named/HTTP/DTO · claim ALVB/ALVU Soft Done as Live Port bind · scatter/Studio/Builder without go-ahead · name ≠ create bodies/scaffold · conflate Historical arc with tip Meta · reopen ALVB-96 as CODE Todo.

### Focus paths ($topic / $focusModule)

- Backend: `clients/Alvasar/backend/docs/requirements/13-cabinet-refresh-people-ai-host.md` · package `cabinet-refresh-people-ai-host/` · residual Live-after-PA.  
- UI: `clients/Alvasar/ui/docs/requirements/08-…` · package `cabinet-target-state-wa-profiles-ai/` · JOIN · Gallery 2 · CTS-19/20 Todo.  
- GPT: `clients/Alvasar/gpt/docs/requirements/01-questionnaire-instruction-pack.md` · ALVG tip · bodies Absent.

---

## Starting focus packet

### 1) Default filled orientation

Same **FULL** fence as Bootstrap SSOT above (Phase A–C complete).

### 2) Overlay — append after orientation Phase A–C (never replace init)

```text
<!-- OVERLAY: Alvasar Root — append AFTER orientation Phase A–C completes -->
@docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/alvasar-root-extract.md

Alvasar Root — context overlay (disk tip honesty 2026-11-18T14:40:25Z).

KEEP:
- client_tenancy alvasar · MS: alvasar-backend / alvasar-ui / alvasar-gpt
- Parent REQ14 Draft · children 08 / 13 / 01
- Soft≠Live: ALVB-85…96 Done fence/Open/PA ≠ Port Named Present
- UI ADMIN-CTS 6/6 Done · JOIN = CTS-BRIDGE-BACKEND-JOIN.md
- Gallery tip ALVU-CTS-18 Done Active pkg-000042 Soft≠Live
- gpt ALVG-03 Done · O5 Open · bodies Absent
- Tip closed backend: do not invent/activate next ALVB without operator

OPEN / NEXT SAFE ASK (from Tip honesty only — pick one):
1) Re-orient cold map — re-run Phase A–C with $topic/$focusModule as filled.
2) Continue alvasar-ui next authored story: STORY-ALVU-CTS-19 (Todo) Gallery 2 PR/EDIT — Builder session builder_project=alvasar-ui (not $clientId). Do NOT reopen CTS-18 as CODE Todo.
3) Host Live-Present residual after PA — read RESIDUAL-LIVE-PRESENT-AFTER-PA.md; no invent next ALVB tip (96 tip closed).
4) gpt create-wave / O5 — only if operator explicitly orders; ALVG-03 Done ≠ bodies Present.
5) Other named topic (operator fills) — no invent Accepted/live SUCCESS.

Do NOT frame OPEN as «continue CODE Todo» on ALVB-96 or ALVU-CTS-18 or ALVG-03.
```

**Overlay bullets count:** 6 KEEP + 5 OPEN picks = **11**.

---

## Smoke checklist

- [x] Title matches sidebar / restore card (`Alvasar Root`)
- [x] rootKind ↔ orientation path (`client_tenancy` → client-product-root-orientation)
- [x] clientId substituted (`alvasar`); not empty
- [x] Orientation fence complete (Phase A–C present, not shortened)
- [x] Starting focus = orientation + overlay
- [x] Tip honesty table Present (4 rows)
- [x] Overlay OPEN consistent with Meta (no stale Todo on 96/18/03)
- [x] Historical arc ≠ current tip conflated
- [x] No invent beyond disk + confirmed arc

---

## Notes for later HTML merge

- Card id / data-role: `alvasar-root` · **Root**
- Paste strategy: keep full orientation init in `<pre id="pre-alvasar-root">`; append `@` this extract after «AFTER orientation Phase A–C completes…»
- Optional: inject `$topic`/`$focusModule` into HTML default if operator wants non-empty defaults (today HTML has `$topic=` empty)
- Peer bridge path: Absent this turn — do not invent
