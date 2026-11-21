# Migration — dialog restore extract (Root / Cross / system-root)

**Категория:** migration (живой Root/Cross диалог → restore extract pack)  
**Output home (default):** [`../../analysis/dialog-restore-extracts/`](../../analysis/dialog-restore-extracts/)  
**Naming:** `{sidebar-slug}-extract.md`  
**Peers:** [`migration-dialog-restore-extract.md`](./migration-dialog-restore-extract.md) (O/V / role) · [`migration-dialog-restore-extract-fixup.md`](./migration-dialog-restore-extract-fixup.md) (доработка существующего pack) · [`../architect/client-product-root-orientation.md`](../architect/client-product-root-orientation.md) · [`../architect/cross-project-system-orientation.md`](../architect/cross-project-system-orientation.md) · [`migration-dialog-context-bridge.md`](./migration-dialog-context-bridge.md)  
**UI consumer (later wave):** [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

Универсальный extract для **рутовых / кросс-проектных** диалогов под проект-систему: client tenancy (`Alvasar Root`, future `{Client} Root`) или DOGE platform (`Cross-project system analysis`).  
Init = **полный orientation fence** (как в restore HTML), не OP/VAL skill.  
Не путать с O/V extract → [`migration-dialog-restore-extract.md`](./migration-dialog-restore-extract.md); не путать с bridge → `analysis/dialog-bridges/`.  
Уже написанный extract с tip-drift → [`migration-dialog-restore-extract-fixup.md`](./migration-dialog-restore-extract-fixup.md) (не полный re-extract).

---

## When

| Use case | Да / нет |
|----------|----------|
| Живой Root / Cross / system-root диалог → extract под restore HTML | **Да** |
| O / V / role-bootstrap dialog extract | **Нет** → [`migration-dialog-restore-extract.md`](./migration-dialog-restore-extract.md) |
| Уже есть `*-extract.md`, нужна доработка tip honesty | **Нет** → [`migration-dialog-restore-extract-fixup.md`](./migration-dialog-restore-extract-fixup.md) |
| Handoff → полностью чистый агент | **Нет** → [`migration-dialog-context-bridge.md`](./migration-dialog-context-bridge.md) |
| Регенерация HTML из extracts | **Нет** — отдельный operator ask |

---

## Tip / Status honesty (hard)

Applies to **both** `$rootKind` (parent→child may close; residual tip still needs Meta re-read).

1. **Disk beats chat memory** for any story/REQ tip Status, Finish Line, Delivery class, next phase.
2. If arc or Overlay names a STORY/REQ tip → **mandatory Read** of that file’s Meta (or REQ Status line) **in this extract turn**; cite path + Status / Finish Line / next (or Unknown).
3. Forbidden: copy «Todo / CODE_REQUIRED / Layer-1» from conversation if Meta says Met / Done / next P5 (etc.).
4. Two clocks in Dialog arc:
   - **Historical** — state at wave time (ok as history)
   - **Current tip (now)** — must match today’s Meta; feeds Verified Tip honesty table + Overlay OPEN

---

## Classification → orientation SSOT

Агент **обязан** загрузить init с диска по `$rootKind` (не invent). Подставить `$clientId` / `$topic` / `$focusModule` как в restore HTML. В extract — **полный** filled fence (не truncate).

| `$rootKind` | Default init (read from disk) | Typical HTML card |
|-------------|-------------------------------|-------------------|
| `client_tenancy` | [`../architect/client-product-root-orientation.md`](../architect/client-product-root-orientation.md) + `@` tenancy / `clients.yaml` / `profiles.yaml` (как Root card) | `Alvasar Root` · future `{Client} Root` |
| `doge_platform` | [`../architect/cross-project-system-orientation.md`](../architect/cross-project-system-orientation.md) + primer / `docs/modules/` / `docs/analysis/` `@` (как Cross card) | `Cross-project system analysis` |

Slug: kebab от `$dialogTitle`. Примеры: `Alvasar Root` → `alvasar-root-extract.md`; `Cross-project system analysis` → `cross-project-system-analysis-extract.md`.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-dialog-restore-extract-root-cross.md
@docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/README.md
@docs/methodology/Zeya888-builder-queue/MANIFEST.md

$dialogTitle=
$rootKind=
$clientId=
$topic=
$focusModule=
$extractOutDir=docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts

Migration — DIALOG RESTORE EXTRACT (Root / Cross / system-root).

MODE: analysis.mdc. Facts from disk + confirmed dialog arc only. No product code.
No commit/push unless explicitly ordered. Name ≠ create outside extract path.
Do NOT dump encyclopedia — pointers + FULL orientation fence + overlays.
Do NOT write under analysis/dialog-bridges/.
Do NOT edit dialog-restore-console.html in this run.
Do NOT use OP/VAL migration-role-bootstrap as init for this prompt.
TIP HONESTY: disk Meta beats chat memory for Status / Finish Line / next (see Tip / Status honesty above).

## Identify

1) $dialogTitle = exact sidebar / restore-card title (required).
2) $rootKind = client_tenancy | doge_platform (required).
3) $clientId = required when rootKind=client_tenancy (e.g. alvasar). Empty for doge_platform.
4) $topic= / $focusModule= optional focus for overlay.
5) Resolve orientation SSOT from Classification table; Read that architect prompt; build filled paste matching restore-HTML Root or Cross card for this title (same @ paths + Phase A–C body).
6) slug = kebab-case of $dialogTitle; out = {$extractOutDir}/{slug}-extract.md
7) Before write: for every STORY/REQ tip you will name in arc Overlay → Read Meta/Status this turn.

## Deliverables (strict order)

1) Mirror in chat (5–10 sentences): title / rootKind / clientId-or-platform + orientation path + tip honesty summary (or none) + out path.
2) Write extract file at `out` with REQUIRED sections below.
3) Report: extract path | slug | rootKind | orientation path | tip honesty rows | Unknowns. STOP.

## Extract file — required sections

### Identity
- dialogTitle, rootKind, clientId (if any), workspace root
- transcript/agent-store id if known, UTC
- slug, extract path
- Suggested HTML card id / data-role (Root | Cross)

### Bootstrap SSOT (orientation init)
- Absolute/repo-relative path of orientation prompt used
- Supporting @ paths (tenancy/clients/profiles OR primer/modules/analysis)
- **Filled default paste block** — FULL orientation fence with substitutions ($clientId / $topic / $focusModule). Do NOT truncate Phase A–C.

### Context transfer
- Mission (why this root/cross dialog exists — system map / client multi-MS, not a single builder_project role)
- Dialog arc (ordered waves; mark **Historical** vs **Current tip (now)**; closed vs open; parent REQ / primer decisions)
- Verified state (commands + on-disk results)
- **Tip honesty (current)** — mandatory table (at least one row if Overlay/arc names a tip; else one row «no tip named — N/A»):
  | Tip path | Meta Status | Finish Line / Delivery | Next | UTC of Meta / re-read |
- Map Present/Absent:
  - client_tenancy → MS table (profile keys, focus_folder, parent vs child REQ), portable plans
  - doge_platform → classic-four components, data-flow, FR layer map (modules / analysis / per-project REQ)
- Decisions locked · Forbidden (no scatter/Studio/Builder without go-ahead; name ≠ create)
- Focus paths relevant to $topic / $focusModule if set

### Starting focus packet
Ready first paste for recreate after wipe:
1) Default filled orientation (same FULL fence as Bootstrap SSOT)
2) **Overlay** — must not lose: active system/client topics, open asks, parent REQ / primer locks
   - **OPEN / NEXT SAFE ASK** — derive **only** from Tip honesty table + operator fills
   - If Finish Line Met / next P5 (or Done) → do **not** frame OPEN as «continue CODE Todo» on that story
   - Offer operator pick: re-orient cold map | continue next phase from Meta | other named topic — no invent Accepted/live SUCCESS
Mark overlay clearly for later HTML merge (append after init; never replace init).

### Smoke checklist
- [ ] Title matches sidebar / restore card
- [ ] rootKind ↔ orientation path correct
- [ ] clientId substituted when client_tenancy; empty when doge_platform
- [ ] Orientation fence complete (Phase A–C present, not shortened)
- [ ] Starting focus = orientation + overlay
- [ ] Tip honesty table Present when Overlay names STORY/REQ (or N/A row)
- [ ] Overlay OPEN consistent with Meta (no stale Todo if Met)
- [ ] Historical arc ≠ current tip conflated
- [ ] No invent beyond disk + confirmed arc

### Notes for later HTML merge
- Card id / data-role Root|Cross
- Paste strategy: keep full orientation init; append @ this extract after «AFTER orientation Phase A–C completes…»
- Peer bridge path if Present (do not copy bridge body unless needed for overlay)

## Operator context (fill)

- dialogTitle=
- rootKind=client_tenancy|doge_platform
- clientId=
- topic=
- focusModule=
- already Done=
- must keep after wipe=

## Report

Reply: mirror ok | extract path | slug | rootKind | orientation path | tip honesty rows | overlay bullets count | Unknowns.
STOP unless operator asks follow-up.
```

---

## Примечания

- Hard `@` in paste = analysis.mdc + this prompt + restore-extracts README + MANIFEST; orientation body resolved by `$rootKind` from disk.
- Outputs under `$extractOutDir` (default `analysis/dialog-restore-extracts/`).
- Prefer **this** prompt over generic restore-extract when dialog is Root / Cross / system-root.
- Existing pack tip-drift → fixup prompt, not silent invent in HTML.
- HTML актуализация — только по отдельному ask после заполнения папки.
