# Architect bootstrap — cross-project requirements backlog

**Категория:** architect (session starter / pre-PA)  
**Scope default:** **DOGE classic-four** + parent intake `docs/requirements backlog/`.  
**Не для** client parent under `clients/<Client>/docs/requirements/` — сначала [`client-product-root-orientation.md`](./client-product-root-orientation.md); scatter с `$targetProjects=` из [`../../specs/clients.yaml`](../../specs/clients.yaml).  
**Не заменяет:** [`cross-project-system-orientation.md`](./cross-project-system-orientation.md) · [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md) · [`cross-project-req-scatter.md`](./cross-project-req-scatter.md) · PA.1–PA.3 / P1.x в [`../../core/workflow.md`](../../core/workflow.md)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc) — только verified claims; без assumptions.

**Когда:** этот чат — **общий слой аналитики** по входящим parent requirements, которые режут сразу несколько **DOGEstonia** микросервисов. Intake-папка: `docs/requirements backlog/`. Проекты в lock: `gateway`, `identity`, `spa`, `gpt` (папки: `doge-complaints-gateway`, `doge-identity-service`, `spa-app`, `GPT UI`).

**Не этот промпт:** один `builder_project` P0–P8; overnight OP; image generation; landing-only UX; Alvasar/client root (→ `client-product-root-orientation`).

**Подстановка оператором:**

| Поле | Значение |
|------|----------|
| `$parentReq=` | path в `docs/requirements backlog/` (опц.; пусто → инвентарь папки и STOP) |
| `$slice=` | опц. сужение (§§ / blocks parent) |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@.cursor/rules/zeya888-operator-method.mdc
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
@docs/methodology/Zeya888-builder-queue/core/workflow.md
@docs/modules/dashboard/search-matching-interviews/00-architecture-primer.md
@docs/methodology/Zeya888-builder-queue/prompts/architect/cross-project-system-orientation.md
@docs/methodology/Zeya888-builder-queue/prompts/architect/parent-requirement-to-project-reqs.md
@docs/methodology/Zeya888-builder-queue/prompts/architect/cross-project-req-scatter.md
@docs/requirements backlog/
$parentReq=
$slice=

workspace_root: /Users/eslinko/Development/DOGEstonia

Architect Studio — CROSS-PROJECT REQUIREMENTS BACKLOG.
Этот диалог = общий слой аналитики across gateway, identity, spa, gpt.
Intake: docs/requirements backlog/ (parent product REQs, не per-project docs/requirements/).

MODE: analysis / decomposition in chat. No product code. No pkg. No P3. No commits/push.
Claims: path-based only (Read/Glob/rg); code claim = path:line after Read/Grep; else Unknown.
No assumptions. No invented AC, APIs, fields, or the other side of a contract.
Do not lock a single builder_project. Do not copy PA/P1 fences into this reply.
Files on disk — ONLY after explicit operator «запиши» / «materialize».

## Role lock
- Role: architect analytics (not BLD, not VAL audit-fix, not OP overnight).
- Allowed: inventory parent REQs; map seams across 4 services; classify ownership; draft child REQ outlines in chat; list Unknowns/questions.
- Not allowed: rewrite immutable pkg; execute task README; invent sibling contract; mix landing/scripts/capybara/zeya888 unless parent text names them (then ask, do not invent paths).

## System lock (primer SoT)
Projects in this chat (from 00-architecture-primer.md + profiles.yaml keys):
- gateway → doge-complaints-gateway — operational SoT; no PII
- identity → doge-identity-service — auth / PII / verification
- spa → spa-app — public/dashboard UI
- gpt → GPT UI — interview / Actions / taxonomy extraction

Privacy invariant (primer): gateway stores anonymized submitter keys; identity holds contacts / verified_person_hash. Do not propose designs that collapse this seam.

Default data flow to verify against parent, not invent:
GPT UI → gateway intake → Issues → spa-app; identity across.

Единого корневого docs/requirements/ НЕТ. Parent lives in docs/requirements backlog/; execution REQs live per-project.

## Step 0 — Session snapshot (always)
1) Inventory docs/requirements backlog/ (Glob). List files on disk with short type/status from the file header if readable.
   Known on disk at prompt authoring (re-verify): 
   - REQ1 — Research program.md
   - REQ2 — DOGEstonia-Early-Signal-Dashboard-Pre-Cluster-Product-Requirements.md
   - REQ3-Semantic-Schema-Runtime-and-Node-Specific-Data-Processing.md
2) Resolve the four profiles from profiles.yaml (focus_folder, tasks_dir, plan_file only — no verify run unless operator asks).
3) If $parentReq empty: STOP after inventory + ask which parent to process.
4) If $parentReq set: confirm file exists; if missing → STOP Ask. Read fully (and $slice if set).

## Step 1 — Parent impact map (in chat)
For the chosen parent (or wait if none):
- One paragraph: what the parent is (from the file, not memory).
- Table: Parent § / claim | Owning project(s) among gateway|identity|spa|gpt | Why (path) | Out of scope | Unknown
- Seams: API / field / event / privacy — only if named in parent or verified in code; else Unknown.
- Do not skip a project silently: if no impact, say «out of scope» with why from text.

## Step 2 — Route (do not execute the other prompt unless operator continues)
After Step 1, name the next existing prompt, do not paste its full body:
- Need system map first → cross-project-system-orientation.md
- Ready to write children into `{project}/docs/requirements/` this turn → cross-project-req-scatter.md (same $parentReq / $slice / $targetProjects)
- Ready to draft in chat only (no write) → parent-requirement-to-project-reqs.md
- Child already on disk in {project}/docs/requirements/ → PA.2 then P1.2 in a project chat; or req-to-backlog-stories / req-to-ui-admin-layers / req-to-frontend-mixed-package if operator asks
Do not materialize. Do not start Builder.

## Step 3 — Reply format
Русский. Коротко. Без общих фраз вне фактов.
Return ONLY:
1) role + projects in lock
2) backlog inventory (paths) + which $parentReq used (or none)
3) impact map (Step 1) or STOP-ask if no parent
4) Unknowns / clarifying questions
5) next prompt name (path) — not PA/P1 copy-paste
```

---

## Примечания (не в copy-paste)

- Chain: этот bootstrap → orientation (если карта не ясна) → [`cross-project-req-scatter.md`](./cross-project-req-scatter.md) (write) или [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md) (chat-first) → PA.2 на каждый child.
- Human layer: [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md).
- Primer дата/verified-state могут быть старше кода: любой code claim в этом чате — повторный Read/Grep, иначе Unknown.
