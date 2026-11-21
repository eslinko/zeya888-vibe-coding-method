# Dialog restore extract — Threads V

**UTC:** 2026-11-18T13:06:45Z  
**Prompt:** [`../../prompts/migration/migration-dialog-restore-extract.md`](../../prompts/migration/migration-dialog-restore-extract.md)

## Identity

| Field | Value |
|-------|-------|
| dialogTitle | `Threads V` |
| dialogType | `validator` (operator shorthand `$dialogType=V`) |
| builderProject | `threads` |
| clientId | — (not client_root) |
| workspace_root | `/Users/eslinko/Development/DOGEstonia` |
| focus_folder | `doge-threads` ([`../../specs/profiles.yaml`](../../specs/profiles.yaml)) |
| agent-store id | `e9ae8981-6238-43c0-8e40-0aee60773804` |
| slug | `threads-v` |
| extract path | `docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/threads-v-extract.md` |

Restore-console card Present: `id="threads-v"` · `data-title="Threads V"` · `data-role="V"` in [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html).

## Bootstrap SSOT

| Item | Path |
|------|------|
| Wrapper | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-validator.md` |
| Role bootstrap | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md` |
| Role skill | `.cursor/skills/validator/SKILL.md` |
| Profile | `threads` → focus `doge-threads/` |

### Filled default paste block

```text
@.cursor/skills/validator/SKILL.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

builder_project: threads
focus_role: validator
workspace_root: /Users/eslinko/Development/DOGEstonia

Запусти migration bootstrap строго для validator-роли.
Load validator skill role-lock; then role-bootstrap restore packet.
```

## Context transfer

### Mission

Диалог **Threads V** — validator / analysis-контур профиля `threads` (focus `doge-threads/`): сверка AC/кода/доков публичного social HTTP и attach residual (REQ-05 · HTTP-07/08 · arch `comment-attachments-bytes`), без invent CDN/vendor и без продуктовой реализации как основной роли extract-волны. В подтверждённой дуге этой agent-store сессии: target-tech-arch → REQ→backlog → L2 → Done-валидация runtime → sync api-reference.

### Dialog arc (ordered)

1. **Closed — target-tech-arch REQ-05:** Hybrid blob port · gated GET Bearer · `published_url` = threads GET (not public CDN). Arch `comment-attachments-bytes/` + interview + REQ-05 locks. Operator: stories **не** трогать в arch-only wave (rollback scope creep).  
2. **Closed — REQ→backlog materialize:** reuse package `02-public-social-http/`; rewrite HTTP-07/08 bodies; GET inside HTTP-08 (no HTTP-09); INDEX + dashboard.  
3. **Closed — L2 anti-drift:** HTTP-08 t01–t06 · HTTP-07 t01–t04 из arch 01–03; Status L1/L1.5/L2 Ready → later Apply Done on disk.  
4. **Closed on disk — P3 tip:** HTTP-07 pkg-000045 Done · HTTP-08 pkg-000046 Done (package INDEX / story Meta Closed stamps). Package `02-public-social-http` **8/8 Done**.  
5. **Closed — runtime + VAL:** boot fail = missing `python-multipart` in `.venv` (declared in `pyproject.toml`); after install — HTTP-07/08 tests 15 passed · `/health` `/ready` 200. Report: `doge-threads/docs/analysis/analysis-threads-http-07-08-runtime-multipart-2026-10-21.md`. Product handler gaps **0**.  
6. **Closed — api-reference hygiene:** `API_REFERENCE.md` + `openapi.yaml` synced (HTTP-02…08 headings · floor_class form · GET dual 200 bytes|ErrorEnvelope · multipart note).  
7. **This ask — restore extract only:** write `threads-v-extract.md`; no HTML edit; no product code.

### Verified state

| Check | Result |
|-------|--------|
| STORY-THREADS-HTTP-07 Meta | **Done** · Closed 2026-10-21T12:02:07Z · pkg-000045 |
| STORY-THREADS-HTTP-08 Meta | **Done** · Closed 2026-10-21T12:49:53Z · pkg-000046 |
| Package `02-public-social-http` INDEX | 8/8 Done (HTTP-01…08) |
| Dashboard Remaining | REQ9-01 Todo only (orthogonal); HTTP-07/08 closed |
| REQ-05 | Draft — HTTP-07/08 Done · spa CT-30 OOS |
| api-reference attach paths | Present in API_REF + openapi (inventory align) |
| Runtime multipart analysis | Present — `analysis-threads-http-07-08-runtime-multipart-2026-10-21.md` |
| Restore card `threads-v` | Present in `dialog-restore-console.html` |
| Peer `*-bridge.md` for Threads V | **Absent** under `analysis/dialog-bridges/` |

### File map

**Present:** REQ-05 · arch `comment-attachments-bytes/` · package `02-public-social-http/` HTTP-01…08 · api-reference · multipart analysis · restore card · this extract · agent-store id above.

**Absent / Unknown:** dedicated dialog-bridge for Threads V; whether operator already ran full offline `pytest` suite beyond HTTP-07/08 modules after multipart install; live spa CT-30 status (OOS threads Apply).

### Decisions locked

- Storage **Hybrid** (in-memory + object-store adapters); vendor brand **not** Accepted.  
- Access model **C**: bytes only via threads gated GET + Bearer (`product_write_bearer`).  
- `published_url` = absolute GET path or honest `null` (no invent CDN).  
- Slice: GET download **inside HTTP-08**; tree join = HTTP-07.  
- Absolute URL base Open — default `THREADS_PUBLIC_BASE_URL` or request origin.  
- ASGI multipart upload requires `python-multipart` in `doge-threads/.venv`.  
- Spa CT-30 / front wire = **separate** spa wave.

### Forbidden (for restore VAL paste)

- Product code / invent CDN·vendor·404 / pkg activate / commit/push unless operator explicitly orders.  
- Rewrite STORY bodies without explicit ask (arch-only waves stay docs/arch).  
- Edit `dialog-restore-console.html` in extract-only runs.  
- Write under `analysis/dialog-bridges/` from this prompt.  
- Encyclopedia dump — pointers + bootstrap + overlay only.

### Focus paths

- `doge-threads/docs/requirements/05-comment-attachment-refs-in-tree-read.md`  
- `doge-threads/docs/architecture/comment-attachments-bytes/00-overview.md` (+ 01–03)  
- `doge-threads/docs/tasks/backlog-stories/02-public-social-http/` (INDEX · HTTP-07 · HTTP-08)  
- `doge-threads/docs/runtime-docs/api-reference/API_REFERENCE.md` · `openapi.yaml`  
- `doge-threads/docs/analysis/analysis-threads-http-07-08-runtime-multipart-2026-10-21.md`  
- `doge-threads/docs/tasks/threads-mvp-dashboard.md`  
- spa sibling (cite only): `spa-app/docs/tasks/backlog-stories/component-thread/STORY-SPA-CT-30-live-attach-ref-wire.md`

## Starting focus packet

### 1) Default filled bootstrap

(Same fence as Bootstrap SSOT above.)

### 2) Overlay — must not lose after wipe

```text
### OVERLAY — Threads V session (append after VAL bootstrap)

Profile: threads · focus: doge-threads/ · Role: validator / analysis.

DONE (keep):
- REQ-05 tech locks + arch comment-attachments-bytes (Hybrid · gated GET · published_url model C)
- HTTP-07/08 materialize + L2 from arch · Done on disk (pkg-000045 / pkg-000046)
- Runtime root cause: python-multipart missing in .venv → ASGI import crash; fixed by pip install; analysis report Present
- api-reference sync HTTP-07/08 (floor_class · GET ErrorEnvelope@200 · multipart note)
- Restore card id=threads-v already in dialog-restore-console.html

OPEN / NEXT SAFE VAL ASK:
- Optional: confirm .venv still has python-multipart before local-five threads boot
- Remaining backlog tip: REQ9-01 Todo (orthogonal docs) — only if OP points VAL there
- Spa CT-30 attach live wire = spa package (do not Apply in threads VAL without OP)
- Soft: full pytest suite beyond HTTP-07/08 modules if reclaiming CI green

Hard bans: no product code this restore; name ≠ create; no HTML edit; analysis.mdc path:line or Unknown.
```

## Smoke checklist

- [x] Title matches sidebar / restore card `Threads V`
- [x] dialogType `validator` ↔ migration-validator → role-bootstrap
- [x] builderProject `threads` substituted; clientId N/A
- [x] Starting focus = bootstrap + overlay
- [x] No invent beyond disk + confirmed arc

## Notes for later HTML merge

| Item | Suggestion |
|------|------------|
| Card id / title | Keep `threads-v` / **Threads V** |
| Paste strategy | Keep default VAL fence; append overlay via link/collapsible to this extract (do **not** replace default bootstrap) |
| Peer bridge | None Present — skip |
| HTML edit | Separate operator ask after more extracts land |
