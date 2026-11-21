# Dialog restore extract — Alvasar GPT V

**UTC:** 2026-11-18T12:23:49Z  
**Prompt:** [`../../prompts/migration/migration-dialog-restore-extract.md`](../../prompts/migration/migration-dialog-restore-extract.md)

## Identity

| Field | Value |
|-------|-------|
| dialogTitle | `Alvasar GPT V` |
| dialogType | `validator` (operator shorthand `$dialogType=V`) |
| builderProject | `alvasar-gpt` |
| clientId | — (not client_root) |
| workspace_root | `/Users/eslinko/Development/DOGEstonia` |
| focus_folder | `clients/Alvasar/gpt` ([`../../specs/profiles.yaml`](../../specs/profiles.yaml)) |
| agent-store id | `113aa2cf-0b8f-4ca0-a181-dd60cdf3c271` (this Composer lineage; full JSONL filename Unknown) |
| slug | `alvasar-gpt-v` |
| extract path | `docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/alvasar-gpt-v-extract.md` |

Restore-console card Present: `id="alvasar-gpt-v"` · `data-title="Alvasar GPT V"` · `data-role="V"` in [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html).

## Bootstrap SSOT

| Item | Path |
|------|------|
| Wrapper | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-validator.md` |
| Role bootstrap | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md` |
| Role skill | `.cursor/skills/validator/SKILL.md` |
| Operator contract | `docs/methodology/Zeya888-builder-queue/contracts/alvasar-gpt-operator-contract.md` |

### Filled default paste block

```text
@.cursor/skills/validator/SKILL.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

builder_project: alvasar-gpt
focus_role: validator
workspace_root: /Users/eslinko/Development/DOGEstonia

Запусти migration bootstrap строго для validator-роли.
Load validator skill role-lock; then role-bootstrap restore packet.
```

## Context transfer

### Mission

Диалог **Alvasar GPT V** — validator / analysis-контур профиля `alvasar-gpt` (focus `clients/Alvasar/gpt/`): authorship SSOT instruction pack (REQ `01`), target tech-arch, backlog STORY-ALVG-* и Nested docs/fence — **без** invent instruction bodies и без product Platform SoT. P4 только по явному OP; create-wave bodies — только по explicit create order (`analysis.mdc` name ≠ create).

### Dialog arc (ordered)

1. **Closed — VAL migration bootstrap:** role-lock validator; profile `alvasar-gpt` enabled; P4 subject initially Absent (bootstrap tip) → hold, не подменять P4 на t00.  
2. **Closed — Target tech-arch REQ `01`:** Architect Studio Phase 0–2; operator mode auto-accept recommendations (UX + arch consistency); packaging = staged bundle; provisional `ALVASAR_INSTRUCTIONS_*`; materialize on «запиши» → arch `questionnaire-instruction-pack/` `00`/`10`/`20` + interview report `zeya888.target-tech-arch-interview-questionnaire-instruction-pack-2026-11-15.md`; thin links on REQ/README.  
3. **Closed — req → backlog stories:** Phase 0 NEW package `questionnaire-instruction-pack/`; materialize STORY-ALVG-01…03 + root INDEX + `alvasar-gpt-mvp-dashboard.md`; create-wave **out of package**.  
4. **Closed — Nested technical subtasks (docs-only):** ALVG-01 T01–T04 · ALVG-02 T01–T05 · ALVG-03 T01–T05; package INDEX nested Present; **no** task folders in that Nested wave.  
5. **Closed on disk (after Nested) — P1.3/P3 tip:** EPIC-ALVG-01 · pkg-000001…000003 · ALVG-01…03 **Done** · tip pkg-000003 · gates PASS · bodies **Absent** · O5 **Open** (bullrun / package INDEX as-of `2026-11-16T07:29:45Z`).  
6. **This ask — restore extract only:** write `alvasar-gpt-v-extract.md`; no HTML edit; no product code; no bridge rewrite.

### Verified state

| Check | Result |
|-------|--------|
| Package INDEX | ALVG-01…03 **Done** · tip pkg-000003 · nested Done (P3) · bodies Absent · O5 Open |
| Bullrun §Актуальная точка | Active pkg-000003 · STORY-ALVG-03 Done · next only on OP · Updated `2026-11-16T07:29:45Z` |
| Root backlog INDEX | package 3/3 Done |
| `instructions.manifest.json` | **Absent** (`test ! -f` this extract turn) |
| Tech-arch `00-overview.md` | Present |
| Restore card `alvasar-gpt-v` | Present in `dialog-restore-console.html` |
| Peer VAL-specific `*-bridge.md` | **Absent**; method peer Present: `analysis/dialog-bridges/alvasar-gpt-profile-bootstrap-bridge.md` (sidebar **Zeya888**, not this V card) |
| `--verify` this turn | **Unknown** (not re-run; path Present in bullrun) |

### File map

**Present:** REQ `01` · arch `questionnaire-instruction-pack/` · interview report · package `questionnaire-instruction-pack/` ALVG-01…03 · EPIC-ALVG-01 pipeline stories · pkgs 000000…000003 · dashboard · contract · restore card · this extract · method bridge `alvasar-gpt-profile-bootstrap-bridge.md`.

**Absent / Unknown:** instruction bodies / manifest; dedicated dialog-bridge for **Alvasar GPT V**; whether OP already scheduled P4 or create-wave; live `--verify` stdout this turn.

### Decisions locked

- Authorship SSOT under `clients/Alvasar/gpt/`; README entry; name ≠ create bodies.  
- Tech-arch three layers: authorship → staged DIR → backend consumer; Git ≠ image packaging.  
- Module-1 manifest shape; no request-time GitHub fetch.  
- Provisional env `ALVASAR_INSTRUCTIONS_DIR` / `_MANIFEST` / optional `_CONTENT_SOURCE_COMMIT`; O5 product lock still Open.  
- Package ALVG-01…03 Done ≠ create-wave; next wave / P4 / bodies only on OP/create order.

### Forbidden (for restore VAL paste)

- Create `instructions.manifest.json` / prompt bodies «so paths exist».  
- Claim extraction Done / O5 Done / Platform SoT.  
- Product code / pkg invent / commit/push unless operator explicitly orders.  
- Run P4 as substitute for missing subject or for create-wave.  
- Edit `dialog-restore-console.html` in extract-only runs.  
- Write under `analysis/dialog-bridges/` from this prompt.  
- Confuse `alvasar-gpt` with flat `gpt` / GPT UI.

### Focus paths

- `clients/Alvasar/gpt/docs/requirements/01-questionnaire-instruction-pack.md`  
- `clients/Alvasar/gpt/docs/architecture/questionnaire-instruction-pack/00-overview.md` (+ `10` / `20`)  
- `clients/Alvasar/gpt/docs/analysis/zeya888.target-tech-arch-interview-questionnaire-instruction-pack-2026-11-15.md`  
- `clients/Alvasar/gpt/docs/tasks/backlog-stories/questionnaire-instruction-pack/`  
- `clients/Alvasar/gpt/docs/tasks/bullrun-launch-index.md`  
- `docs/methodology/Zeya888-builder-queue/contracts/alvasar-gpt-operator-contract.md`  
- Soft siblings: backend `13` / `07` · UI `08` · parent REQ14

## Starting focus packet

### 1) Default filled bootstrap

(Same fence as Bootstrap SSOT above.)

### 2) Overlay — must not lose after wipe

```text
### OVERLAY — Alvasar GPT V session (append after VAL bootstrap)

Profile: alvasar-gpt · focus: clients/Alvasar/gpt/ · Role: validator / docs-fence analysis.

DONE (keep):
- Target tech-arch questionnaire-instruction-pack (00/10/20) + interview 2026-11-15
- Backlog package questionnaire-instruction-pack: STORY-ALVG-01…03 Done · tip pkg-000003
- Nested T01–T04/T05 executed on disk (P3); EPIC-ALVG-01 materialized
- Instruction bodies / instructions.manifest.json still Absent (name ≠ create)
- O5 env names still Open (provisional ALVASAR_INSTRUCTIONS_* in arch only)
- Restore card id=alvasar-gpt-v already in dialog-restore-console.html

OPEN / NEXT SAFE VAL ASK:
- Honesty check: Done package ≠ create-wave; bodies Absent until explicit create order
- P4 only if OP names subject/story; do not invent P4 on tip Done as busywork
- Create-wave (manifest + system/user md) only on explicit operator create
- Optional lightweight triage only if operator names a post-Done hygiene gap (no new STORY)
- Soft: sibling backend load/env still Open O5 — do not invent env Done

Hard bans: no product code this restore; name ≠ create bodies; no HTML edit; analysis.mdc path:line or Unknown.
Do not confuse with builder_project: gpt (GPT UI).
```

## Smoke checklist

- [x] Title matches sidebar / restore card `Alvasar GPT V`
- [x] dialogType `validator` ↔ migration-validator → role-bootstrap
- [x] builderProject `alvasar-gpt` substituted; clientId N/A
- [x] Starting focus = bootstrap + overlay
- [x] No invent beyond disk + confirmed arc

## Notes for later HTML merge

| Item | Suggestion |
|------|------------|
| Card id / title | Keep `alvasar-gpt-v` / **Alvasar GPT V** |
| Paste strategy | Keep default VAL fence; append overlay via link/collapsible to this extract (do **not** replace default bootstrap) |
| Peer bridge | Method peer Present: `analysis/dialog-bridges/alvasar-gpt-profile-bootstrap-bridge.md` (Zeya888 card) — **do not** copy body into V card; VAL-specific bridge Absent |
| HTML edit | Separate operator ask after more extracts land |
