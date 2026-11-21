# Dialog restore extract — Capybara V

**UTC:** 2026-11-18T11:50:17Z (`builder_resolve_queue.py --print-utc-now`)  
**Prompt:** [`../../prompts/migration/migration-dialog-restore-extract.md`](../../prompts/migration/migration-dialog-restore-extract.md)

## Identity

| Field | Value |
|-------|-------|
| dialogTitle | `Capybara V` |
| dialogType | `validator` (operator shorthand `$dialogType=V`) |
| builderProject | `capybara` |
| clientId | — |
| workspace_root | `/Users/eslinko/Development/DOGEstonia` |
| focus_folder | `capybara/` ([`../../specs/profiles.yaml`](../../specs/profiles.yaml)) |
| agent-store id | `e2850328-636e-4df9-b003-9c86e54f7752` |
| slug | `capybara-v` |
| extract path | `docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/capybara-v-extract.md` |

Restore-console card Present: `id="capybara-v"` · `data-title="Capybara V"` · `data-role="V"` in [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html).

## Bootstrap SSOT

| Item | Path |
|------|------|
| Wrapper | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-validator.md` |
| Role bootstrap | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md` |
| Role skill | `.cursor/skills/validator/SKILL.md` |

### Filled default paste block

```text
@.cursor/skills/validator/SKILL.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

builder_project: capybara
focus_role: validator
workspace_root: /Users/eslinko/Development/DOGEstonia

Запусти migration bootstrap строго для validator-роли.
Load validator skill role-lock; then role-bootstrap restore packet.
```

## Context transfer

### Mission

Диалог **Capybara V** — validator / analysis-контур профиля `capybara`: сверка фактов по коду и артефактам (REQ → tech-arch → backlog ADV → CLI/мануал), без продуктовой реализации как основной роли. В этой сессии фактически шли architect/analysis волны advance (REQ-02, tech-arch, stories) и post-Done валидация ADV + актуализация USER-MANUAL; live CLI показал fail-closed на отсутствующий limits-файл.

### Dialog arc (ordered)

1. **Closed — Debt follow-through:** DEBT-08/09 Done; Tristan summary verify analysis; open_debts/limit факты.  
2. **Closed — REQ-02:** продуктовое интервью advance → `capybara/docs/requirements/02-activity-payout-advance.md`.  
3. **Closed — Target tech-arch:** Phase 0–2 interview (Twin Debt, journal mirror, preflight+formula, limits twin, verify/JSON) → materialize `docs/architecture/02-activity-payout-advance/` + interview report `2026-11-10`.  
4. **Closed — Backlog ADV:** plan-only → «запиши» → package `capybara-advance/` ADV-01…06 + root INDEX + dashboard recount.  
5. **Closed — Wave execute (operator waves / bullrun):** ADV-01…06 marked Done (pipeline/gates); code under `packages/core/src/advance/` + action 7 + action 4 hook.  
6. **Closed — Post-ship validate + manual:** code/tests grep+`npm test -- --grep advance` (41 passing as-of that turn); USER-MANUAL / `.env.example` / package INDEX synced to Done.  
7. **Open / residual — live CLI limits:** terminal (2026-11-11) `CAPYBARA_ACTION=7` in `gfl_reality` failed: `advance limits file is missing: …/capybara/config/advance-limits.json`. As-of this extract UTC **2026-11-18**, that working file is **Present** on disk (gitignore); example template Present. Operator may still need confirm contents/limits before next live issue.

### Verified state

| Check | Result |
|-------|--------|
| Action 7 registry | Present — `capybara/packages/core/src/actions/index.js` map `[7, action7AdvanceLedger]` |
| Advance domain | Present — `capybara/packages/core/src/advance/*.js` |
| AdvanceLedgerAction ops | `issue\|forgive\|settle\|summary\|show` |
| Action 4 hook | Present — `CAPYBARA_ADVANCE_ID` + preflight in `ActivityPayoutAction.js` |
| Unit tests | Present — `tests/unit/advance-*.js`; prior run grepped advance → 41 passing |
| REQ / arch / stories | Present — REQ-02, `02-activity-payout-advance/`, ADV-01…06 Meta/INDEX Done |
| USER-MANUAL § action 7 / ADVANCE_ID | Present (post-validate edits) |
| `config/advance-limits.example.json` | Present |
| `config/advance-limits.json` | Present **as-of 2026-11-18** (was missing in 2026-11-11 terminal log) |
| Peer dialog-bridge for Capybara V | Absent under `analysis/dialog-bridges/` |

### File map

**Present:** REQ-02 · tech-arch package · interview report · ADV package + epic · advance runtime + tests · USER-MANUAL / LOGGING / ARCHITECTURE pointers · restore card `capybara-v` · this extract.

**Absent / Unknown:** dedicated `*-bridge.md` for this dialog; whether live `gfl_reality` issue was re-run successfully after limits file appeared; transcript JSONL path beyond agent-store id.

### Decisions locked

- Twin Debt architecture; journal under `logs/capybara/advance/`; packaging N/A.  
- Action candidate **7**; embedded path: preflight `balance_now + payout ≥ remainder` + one combined preview.  
- Separate advance limits SSOT (not inside debt-limits).  
- ADV-01…06 Done; no new STORY invented in validate wave.

### Forbidden (for restore VAL paste)

- Product code / pkg activate / commit/push unless operator explicitly orders.  
- P3 as substitute for VAL; invent APIs beyond REQ/arch/stories.  
- Edit `dialog-restore-console.html` in extract-only runs.  
- Write under `analysis/dialog-bridges/` from this prompt.

### Focus paths

- `capybara/docs/requirements/02-activity-payout-advance.md`  
- `capybara/docs/architecture/02-activity-payout-advance/00-overview.md`  
- `capybara/docs/tasks/backlog-stories/capybara-advance/`  
- `capybara/docs/manuals/USER-MANUAL.md` (§ action 4 ADVANCE_ID, § action 7)  
- `capybara/config/advance-limits.example.json` · working `advance-limits.json`  
- `docs/methodology/Zeya888-builder-queue/contracts/capybara-operator-contract.md`

## Starting focus packet

### 1) Default filled bootstrap

(Same fence as Bootstrap SSOT above.)

### 2) Overlay — must not lose after wipe

```text
### OVERLAY — Capybara V session (append after VAL bootstrap)

Profile: capybara · Role context: validator / analysis (this chat also ran architect waves).

DONE (keep):
- REQ-02 activity payout advance + tech-arch 02-activity-payout-advance + interview 2026-11-10
- Backlog ADV-01…06 Done (package capybara-advance); action 7 + advance/* + action4 ADVANCE_ID hook
- USER-MANUAL / .env.example synced to code; package INDEX all Done
- Prior validate: npm test -- --grep advance → 41 passing (re-run if reclaiming)

OPEN / NEXT SAFE VAL ASK:
- Confirm working `capybara/config/advance-limits.json` is intentional (Present 2026-11-18; was missing → CLI fail 2026-11-11)
- Optional: lightweight live smoke mock action 7 summary/issue (no invent new stories)
- Do not activate pkg / do not P3 unless OP routes

Hard bans: no product scope creep; name ≠ create; analysis.mdc claims only path:line or Unknown.
```

## Smoke checklist

- [x] Title matches sidebar / restore card `Capybara V`
- [x] dialogType `validator` ↔ migration-validator → role-bootstrap
- [x] builderProject `capybara` substituted; clientId N/A
- [x] Starting focus = bootstrap + overlay
- [x] No invent beyond disk + confirmed arc

## Notes for later HTML merge

| Item | Suggestion |
|------|------------|
| Card id / title | Keep `capybara-v` / **Capybara V** |
| Paste strategy | Keep default O/V fence; add link or collapsible note to this extract for overlay (do not replace default VAL bootstrap) |
| Peer bridge | None Present — skip |
| HTML edit | Separate operator ask after more extracts land |
