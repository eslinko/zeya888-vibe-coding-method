# Architect — scatter parent REQ → per-project children (write after impact)

**Категория:** architect (pre-PA.2, write-after-impact)  
**Scope default:** **DOGE classic-four** (`$targetProjects=gateway,identity,spa,gpt`). For **client tenancy** override CSV from [`../../specs/clients.yaml`](../../specs/clients.yaml) (Alvasar: `alvasar-backend,alvasar-ui`); parent path under `clients/<Client>/docs/requirements/`. Root client chat first: [`client-product-root-orientation.md`](./client-product-root-orientation.md).  
**Фазы A–C / стиль child:** SSOT [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md) — **не** дублировать полный текст.  
**Не заменяет:** PA.2 / P1.2; **не** создаёт STORY/pkg ([`req-to-backlog-stories.md`](./req-to-backlog-stories.md) / [`req-to-ui-admin-layers.md`](./req-to-ui-admin-layers.md) / [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md) — отдельный следующий шаг).  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

**Когда:** этот чат — разложить **один** parent requirement на дочерние REQ в `{focus}/docs/requirements/` целевых профилей и **записать файлы в том же прогоне** после impact map.

**Не этот промпт:** chat-first drafts без записи → [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md); session lock без parent → [`cross-project-requirements-backlog-bootstrap.md`](./cross-project-requirements-backlog-bootstrap.md).

**Подстановка оператором:**

| Поле | Значение |
|------|----------|
| `$parentReq=` | обязателен: `docs/requirements backlog/…` **или** client parent `clients/…/docs/requirements/…` **или** per-project REQ |
| `$slice=` | опц. сужение (§§ / blocks) |
| `$targetProjects=` | дефолт `gateway,identity,spa,gpt`; CSV сужает список. **Client cheat (Alvasar):** `alvasar-backend,alvasar-ui`. Threads-фичи: включи `threads` |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/modules/dashboard/search-matching-interviews/00-architecture-primer.md
@docs/methodology/Zeya888-builder-queue/prompts/architect/parent-requirement-to-project-reqs.md
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
$parentReq=
$slice=
$targetProjects=gateway,identity,spa,gpt

workspace_root: /Users/eslinko/Development/DOGEstonia

Architect Studio — CROSS-PROJECT REQ SCATTER (write after impact).
@$parentReq
@$slice (если задан — только эти §§/blocks)

Follow Phase A–C + child header/body from @parent-requirement-to-project-reqs.md.
OVERRIDE materialize: after Phase C write files in THIS turn. Do NOT wait for «запиши».
Do NOT run Phase D dashboard sync. Do NOT create EPIC/STORY/pkg/task folders. Do NOT P3. No commits/push.

MODE: analysis.mdc. Claims path-based; code = path:line after Read/Grep; else Unknown.
No invented AC, APIs, fields, or the other side of a contract.
UX-only parent slice without a named backend contract → spa child + Open question; do not invent endpoint.

## Paths (analogous docs/requirements/)
- gateway → doge-complaints-gateway/docs/requirements/{NN}-{slug}.md + README-index.md
- identity → doge-identity-service/docs/requirements/{NN}-{slug}.md + README-index.md
- spa → spa-app/docs/requirements/{NN}-{slug}.md + README-index.md
- gpt → GPT UI/docs/requirements/REQ-{NN}-{slug}.md + README.md
- threads → doge-threads/docs/requirements/{NN}-{slug}.md (+ README-index.md if present)
Эталон header: doge-complaints-gateway/docs/requirements/48-early-signal-pre-cluster-data-readiness.md

Ownership addendum (when parent text says so):
- Thread CRUD / reactions / votes / sanction signals → threads
- Civic Issue ThreadContext adapter → gateway

## Numbering (live Glob this run — do not use training memory)
Per owning project: next free = max existing NN + 1.
Do NOT copy parent number into another project (GPT REQ-43 ≠ gateway 43-institution-json-story-column.md).
GPT: do not fill vacant REQ-37 unless operator explicitly orders it.
If $parentReq already lives in one of these dirs: do NOT write a duplicate child in that same folder; scatter only to other owning projects.

$targetProjects default gateway,identity,spa,gpt. Do not AskQuestion for owners when default applies.
Project with no impact from parent text → skip file; say out-of-scope with why. Never write an empty/invented child.

STOP before write if $parentReq missing/unreadable, or Unknown blocks ownership and scope cannot be honestly cut — ask once.

## Same-turn write (after A–C)
1) Write each owning child to the proposed path (header: Parent, Parent-id, Siblings with contract: seam or TBD-question, Status: Draft — awaiting PA.2; body: Goal, Scope/Out of scope, Verified current state, Target, AC, Open questions, Dependencies).
2) Update that project's requirements index (README-index.md or GPT README.md).
3) In parent add ## Derived project requirements with child paths; if parent must not be edited → sibling <parent-stem>-derived-index.md after one ask.
4) Reply: written paths | skipped projects | link matrix | Unknowns.
Handoff: Draft children only. Next = PA.2 per child in a project chat; story package only via req-to-backlog-stories / req-to-ui-admin-layers / req-to-frontend-mixed-package when operator asks. Product Story Done ≠ files exist.
```

---

## Примечания (не в copy-paste)

- Chat-first (без записи): [`parent-requirement-to-project-reqs.md`](./parent-requirement-to-project-reqs.md).
- Session lock: [`cross-project-requirements-backlog-bootstrap.md`](./cross-project-requirements-backlog-bootstrap.md).
- Optional next (чистый чат): [`cross-project-req-consistency-audit.md`](./cross-project-req-consistency-audit.md) — parent+children vs операторская цель.
- Human layer: [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md).
