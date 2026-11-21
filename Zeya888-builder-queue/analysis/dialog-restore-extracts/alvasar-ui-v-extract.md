# Dialog restore extract — Alvasar UI V

**UTC:** 2026-11-18T17:57:01Z  
**Prompt:** [`../../prompts/migration/migration-dialog-restore-extract.md`](../../prompts/migration/migration-dialog-restore-extract.md)

## Identity

| Field | Value |
|-------|-------|
| dialogTitle | `Alvasar UI V` (operator · restore card `data-title="Alvasar UI V"`) |
| dialogType | `validator` (operator shorthand `$dialogType=V`) |
| builderProject | `alvasar-ui` |
| clientId | — (not client_root) |
| workspace_root | `/Users/eslinko/Development/DOGEstonia` |
| focus_folder | `clients/Alvasar/ui` ([`../../specs/profiles.yaml`](../../specs/profiles.yaml)) |
| agent-store id | `50e137e7-e1f8-40d2-a3a5-218924337c52` (session Current agent store) |
| slug | `alvasar-ui-v` |
| extract path | `docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/alvasar-ui-v-extract.md` |

Restore-console card Present: `id="alvasar-ui-v"` · `data-title="Alvasar UI V"` · `data-role="V"` in [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html).

## Bootstrap SSOT

| Item | Path |
|------|------|
| Wrapper | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-validator.md` |
| Role bootstrap | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md` |
| Role skill | `.cursor/skills/validator/SKILL.md` |
| Operator contract | `docs/methodology/Zeya888-builder-queue/contracts/alvasar-ui-operator-contract.md` |

### Filled default paste block

```text
@.cursor/skills/validator/SKILL.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

builder_project: alvasar-ui
focus_role: validator
workspace_root: /Users/eslinko/Development/DOGEstonia

Запусти migration bootstrap строго для validator-роли.
Load validator skill role-lock; then role-bootstrap restore packet.
```

## Context transfer

### Mission

Диалог **Alvasar UI V** — validator / analysis-контур профиля `alvasar-ui` (focus `clients/Alvasar/ui/`): сверка CTS-пакета (REQ08 · cabinet-target-state), честности Soft≠Live / Mock≠Live, fidelity kit+галерей к артбордам v2.3; **без** invent Named и без продуктовой реализации как основной роли extract-волны.

**Операторский фокус этой волны (keep after wipe):** подробно зафиксировать **метод галерей** — экраны CTS-01…06 сначала вышли «криво» без опоры на атомы; затем последовательно: kit → Gallery 1 (атомы) → fidelity gaps → Gallery 2 (комбинации) → сверка с артбордами → постоянный мануал. **Дальше:** переоткрыть/дописать CTS-01…06 (и родственные screen-stories), чтобы реализация экранов явно опиралась на `cts-kit` + комбинации галерей и не путала артборды с ad-hoc UI в другом диалоге.

### Dialog arc (ordered · this session + on-disk)

1. **Closed — ADMIN-CTS-01…06:** intake · UX-PROMPTS v2 · artboards v2.3 · icons · JOIN tip ALVB-96 · stories 01…06 authored · tech Nested lock.  
2. **Closed — Screen wave CTS-01…06 Product:** nav / WA preview / RF chrome / ANK / PR skeleton / fail-closed — **Done на диске**, но визуальная fidelity к артбордам оказалась недостаточной (оператор: «криво») → причина следующей волны kit/gallery.  
3. **Closed — CTS-07 kit + CTS-08 Gallery 1:** `ui/modules/cts-kit/` · Mock `?debug=cts-gallery` · atoms gallery Present.  
4. **Closed — Gaps → CTS-09…13:** nav atoms · field/lock/dirty · WA-D overflow · busy + ask-days dismiss · status secondary + skeleton; reaudit gaps **closed**.  
5. **Closed — Gallery 2 CTS-14…20:** host `?debug=cts-gallery-2` · switcher Атомы↔Комбинации · WA/RF/ANK/PR/NAV combos · tip **pkg-000044** · CTS-20 Done.  
6. **Closed — Puppeteer/DOM audits:** Gallery 1 reaudit · Gallery 2 vs artboards **CTS-14…20 pass** (browser CDP; Puppeteer MCP Absent).  
7. **Closed — Permanent manual:** [`clients/Alvasar/ui/docs/manuals/cts-debug-gallery-operator-manual.md`](../../../../../clients/Alvasar/ui/docs/manuals/cts-debug-gallery-operator-manual.md) · backlog HOW-TO = stub redirect · thin links INDEX/arch/README.  
8. **Open — Reopen screen stories via gallery SSOT:** CTS-01…06 (и chrome Done) нужно **переоткрыть / дописать**, как использовать kit + Gallery 1/2 groupings, состыковать содержимое галерей с артбордами **до** фазы реализации экранов в другом (BLD/OP) диалоге.  
9. **This ask — restore extract only:** write `alvasar-ui-v-extract.md`; no HTML edit; no product code.

### Verified state

| Check | Result |
|-------|--------|
| Package tip | pkg-000044 · CTS-20 **Done (Product)** · tip Active (INDEX) |
| CTS-07…20 | **Done (Product)** on disk (INDEX rows) |
| CTS-01…06 | **Done (Product / chrome / skeleton)** on disk — **reopen intent Open** (operator overlay; not yet Todo flip on INDEX) |
| Gallery 1 URL | Mock ∧ `?debug=cts-gallery` · manual Present |
| Gallery 2 URL | Mock ∧ `?debug=cts-gallery-2` · audit pass 2026-11-18 |
| Operator manual SSOT | `docs/manuals/cts-debug-gallery-operator-manual.md` Present |
| Backlog HOW-TO | stub → manuals Present |
| Artboards SSOT | `clients/Alvasar/ui/docs/UX/artboards/` v2.3 |
| Restore card `alvasar-ui-v` | Present in `dialog-restore-console.html` |
| Peer `*-bridge.md` for Alvasar UI V | **Absent** under `analysis/dialog-bridges/` |

### File map

**Present:** REQ08 · arch `08/` (10 DS · 20 G1 · 30 G2) · package `cabinet-target-state-wa-profiles-ai/` CTS-01…20 · EPIC-ALVU-06 · manuals G1/G2 · audits G1/G2 · gallery-2 tech · `cts-kit/` · `cts-gallery2/` · restore card · this extract · agent-store id above.

**Absent / Unknown:** dedicated dialog-bridge for this chat; formal INDEX status flip CTS-01…06 → reopen/Todo (operator intent only until OP edits stories); exact which BLD dialog will own screen re-implementation; Live Named still Absent (Soft ALVB join).

### Decisions locked

- **Gallery method (order):** kit atoms (CTS-07) → Gallery 1 atoms (CTS-08…13) → Gallery 2 combinations (CTS-14…20) → **then** rework product screens using those building blocks; do not invent screen UI parallel to kit.  
- Mock-only galleries · Soft≠Live · no invent Named · fixture ≠ Live SoT · not in primary nav.  
- Artboards v2.3 = visual SSOT; Draft artboard ≠ Product Done.  
- Gallery audits pass ≠ screen stories already rewired to kit (01…06 reopen still required).  
- analysis.mdc: name ≠ create; extract ≠ product code / HTML edit.

### Forbidden (for restore VAL paste)

- Product code / pkg activate / commit/push unless operator explicitly orders.  
- Claim Live Named Present from Soft Done.  
- Implement screen rewrites in VAL extract restore without OP/BLD ask.  
- Edit `dialog-restore-console.html` in extract-only runs.  
- Write under `analysis/dialog-bridges/` from this prompt.  
- Encyclopedia dump — pointers + bootstrap + overlay only.

### Focus paths

- `clients/Alvasar/ui/docs/requirements/08-cabinet-target-state-wa-profiles-ai.md`  
- `clients/Alvasar/ui/docs/tasks/backlog-stories/cabinet-target-state-wa-profiles-ai/INDEX.md`  
- `clients/Alvasar/ui/docs/manuals/cts-debug-gallery-operator-manual.md`  
- `clients/Alvasar/ui/docs/architecture/08-cabinet-target-state-wa-profiles-ai/20-cts-debug-gallery-fixtures.md`  
- `clients/Alvasar/ui/docs/architecture/08-cabinet-target-state-wa-profiles-ai/30-cts-gallery-2-composites.md`  
- `clients/Alvasar/ui/docs/analysis/alvu-cts-gallery-vs-artboards-reaudit-2026-11-18.md`  
- `clients/Alvasar/ui/docs/analysis/alvu-cts-gallery-2-vs-artboards-2026-11-18.md`  
- `clients/Alvasar/ui/docs/analysis/alvu-cts-gallery-2-tech-solution-2026-11-18.md`  
- `clients/Alvasar/ui/docs/UX/artboards/` (v2.3)  
- Stories to reopen (intent): `STORY-ALVU-CTS-01`…`06` (+ chrome residual honesty)  
- Gallery SSOT stories: `STORY-ALVU-CTS-07`…`20`  
- `docs/methodology/Zeya888-builder-queue/contracts/alvasar-ui-operator-contract.md`

## Starting focus packet

### 1) Default filled bootstrap

(Same fence as Bootstrap SSOT above.)

### 2) Overlay — must not lose after wipe

```text
### OVERLAY — Alvasar UI V session (append after VAL bootstrap)

Profile: alvasar-ui · focus: clients/Alvasar/ui/ · Role: validator / gallery-method analysis.

TOPIC (operator): как делаем галереи — текущий пакет стори; сначала экраны CTS-01…06 вышли криво; затем kit→G1→gaps→G2→artboard align; потом снова экраны с опорой на компоненты/группировки галерей (переоткрыть 01…06 + прописать использование kit/combos), чтобы BLD-диалог не путал артборды.

DONE (keep):
- ADMIN-CTS-01…06 Done · tip pkg-000044 · CTS-07…20 Done (Product)
- Gallery 1: ?debug=cts-gallery · Gallery 2: ?debug=cts-gallery-2 · switcher CTS-15
- Audits: G1 reaudit gaps closed · G2 vs artboards CTS-14…20 pass (2026-11-18)
- Permanent manual: clients/Alvasar/ui/docs/manuals/cts-debug-gallery-operator-manual.md
  (кликабельно: http://127.0.0.1:5280/?debug=cts-gallery · …/cts-gallery-2)
- Soft≠Live · Mock-only galleries · artboards v2.3 SSOT
- Restore card id=alvasar-ui-v already in dialog-restore-console.html

OPEN / NEXT SAFE VAL ASK:
- Plan/docs to REOPEN CTS-01…06 (and chrome Done residuals): cite kit atoms + G2 combinations + artboard mapping per screen
- Do not start BLD screen rewrite until reopen AC/method text locked (OP order)
- Validate any reopen draft against gallery DOM + artboards (analysis.mdc)
- Live residual BLOCKED / Soft ALVB join — fail-closed honesty unchanged

Hard bans: no product code this restore; name ≠ create; no HTML edit; analysis.mdc path:line or Unknown.
```

## Smoke checklist

- [x] Title matches sidebar / restore card `Alvasar UI V`
- [x] dialogType `validator` ↔ migration-validator → role-bootstrap
- [x] builderProject `alvasar-ui` substituted; clientId N/A
- [x] Starting focus = bootstrap + overlay
- [x] No invent beyond disk + confirmed arc

## Notes for later HTML merge

| Item | Suggestion |
|------|------------|
| Card id / title | Keep `alvasar-ui-v` / **Alvasar UI V** |
| Paste strategy | Keep default VAL fence; append overlay via link/collapsible to this extract (do **not** replace default bootstrap) |
| Peer bridge | None Present — skip |
| HTML edit | Separate operator ask after more extracts land |
