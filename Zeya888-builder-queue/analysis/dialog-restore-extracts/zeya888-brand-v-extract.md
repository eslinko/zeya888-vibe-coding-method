# Dialog restore extract — zeya888-brand V

**UTC:** 2026-11-18T13:19:34Z  
**Prompt:** [`../../prompts/migration/migration-dialog-restore-extract.md`](../../prompts/migration/migration-dialog-restore-extract.md)

## Identity

| Field | Value |
|-------|-------|
| dialogTitle | `zeya888-brand V` |
| dialogType | `validator` (operator shorthand `$dialogType=V`) |
| builderProject | `zeya888-brand` |
| clientId | — (not client_root) |
| workspace_root | `/Users/eslinko/Development/DOGEstonia` |
| focus_folder | `zeya888` ([`../../specs/profiles.yaml`](../../specs/profiles.yaml)) |
| agent-store id | `76fa67a7-55d1-42d0-9841-ae2e13334374` |
| slug | `zeya888-brand-v` |
| extract path | `docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/zeya888-brand-v-extract.md` |

Restore-console card Present: `id="zeya888-brand-v"` · `data-title="zeya888-brand V"` · `data-role="V"` in [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html).

## Bootstrap SSOT

| Item | Path |
|------|------|
| Wrapper | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-validator.md` |
| Role bootstrap | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md` |
| Role skill | `.cursor/skills/validator/SKILL.md` |
| Operator contract | `docs/methodology/Zeya888-builder-queue/contracts/zeya888-brand-operator-contract.md` |

### Filled default paste block

```text
@.cursor/skills/validator/SKILL.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

builder_project: zeya888-brand
focus_role: validator
workspace_root: /Users/eslinko/Development/DOGEstonia

Запусти migration bootstrap строго для validator-роли.
Load validator skill role-lock; then role-bootstrap restore packet.
```

## Context transfer

### Mission

Диалог **zeya888-brand V** — validator / findings-only контур профиля `zeya888-brand` (focus `zeya888/`): restore VAL после wipe, аудит готовности 1A (Astro+Tailwind+DS+L01–L08+i18n×7, no NC), планирование/валидация strip чужого landing/DOGEstonia контента, runbook local-run+env. Не путать с `builder_project: zeya888` / `zeya888.me` (WordPress). P4/P7 product stories ещё не стартовали (`STORY-ZBRAND-*` Absent).

### Dialog arc (ordered)

1. **Closed — VAL migration restore:** role-lock validator; profile enabled; active pkg t00 methodology marker; verify skipped for VAL restore claims-constraint; next product = author stories (not invent); bans: no OP/BLD/fix/pkg.
2. **Closed — 1A landing infra transfer validation:** findings-only vs plan `zeya888-brand_landing_infra_transfer.plan.md`; verdict **READY**; report `zeya888/docs/analysis/zeya888-brand-landing-infra-transfer-validation-2026-09-18.md`; build/static×7/`--verify` ok; `landing/` parallel intact.
3. **Closed — human gap triage:** residuals non-critical (JSON leftover keys, section PNGs from landing, plan todos pending UI, empty backlog); intentional deltas OK (static vs server, 7 locales).
4. **Closed — strip plan + launch prompt (no product execute in VAL chat):** plan `.cursor/plans/zeya888-brand_doge-content-strip.plan.md` + prompt `migration-zeya888-brand-doge-content-strip.md` (+ INDEX row). Execute was other dialog.
5. **Closed — strip validation:** verdict **PASS**; report `zeya888/docs/analysis/zeya888-brand-doge-content-strip-validation-2026-09-18.md`; imported PNGs stubs; social PNG absent; JSON `[TODO locale]`; listed grep clean; residual comment ids (`STORY-LAND-*` / `STORY-LF-*`) non-AC.
6. **Closed — local-run manual:** `zeya888/docs/manuals/local-run.md` (+ manuals README); links from `zeya888/README.md` / arch 00/02; env fact = `PUBLIC_SITE_ORIGIN` via `.env.example`.
7. **This ask — restore extract only:** write `zeya888-brand-v-extract.md`; no HTML edit; no product code.

### Verified state

| Check | Result |
|-------|--------|
| Profile `zeya888-brand` | enabled · focus `zeya888` · stack Astro+TS+Tailwind · `test_command: cd zeya888 && npm run build` · skill `typescript-pro` |
| Active pkg | pkg-000000 bootstrap t00 · pointer Present · **не** P3 product на marker |
| Bullrun next | Author `STORY-ZBRAND-*` → P1.3 (INDEX: *No stories authored yet*) |
| 1A VAL note | Present — READY |
| Strip VAL note | Present — PASS |
| Manual local-run | Present — `zeya888/docs/manuals/local-run.md` |
| `.env.example` | Present — `PUBLIC_SITE_ORIGIN` only |
| Restore card `zeya888-brand-v` | Present in `dialog-restore-console.html` |
| Peer `*-bridge.md` for this chat | **Absent** under `analysis/dialog-bridges/` |
| REQ filenames on disk (as-of extract UTC) | `REQ01-ZBRAND-landing-infra-transfer.md` · `REQ02-ZBRAND-placeholder-content.md` · `REQ03-ASTRO-LANDING-TRANSFORMATION.md` (older `REQ-ZBRAND-01/02` names **Absent**) |

### File map

**Present:** contract · pipeline · `Zeya888-Brand_builder.plan.md` · transfer + strip plans · migration prompts (infra transfer + doge strip) · analysis 1A/strip implementer+VAL notes · manuals · `.env.example` · pkg-000000 · restore card · this extract · agent-store id above.

**Absent / Unknown:** `STORY-ZBRAND-*` backlog files; product P4/P7 audit reports keyed to stories; dedicated dialog-bridge for this chat; whether OP already scheduled first brand/copy story wave; exact other-dialog transcript id for strip execute.

### Decisions locked

- Scope 1A: Astro+Tailwind+DS+sections+i18n; **no** NC/Volume; parallel `landing/` untouched.
- Locales: en/et/ru/es/fr/de/is; Astro `output: static`.
- Strip wave: keep JSON keys/array lengths; placeholders + stub PNGs; layout may change.
- VAL: findings-only unless operator says «почини»; no invent stories; no Build on `Zeya888-Brand_builder.plan.md`.
- Env: only `PUBLIC_SITE_ORIGIN` (placeholder `https://example.com`).

### Forbidden (for restore VAL paste)

- Product code / invent `STORY-ZBRAND-*` / rewrite immutable pkg / commit/push unless operator explicitly orders.
- P3 on t00 marker; OP routing; BLD execute in this role.
- Edit `dialog-restore-console.html` in extract-only runs.
- Write under `analysis/dialog-bridges/` from this prompt.
- Encyclopedia dump — pointers + bootstrap + overlay only.
- Confuse with profile `zeya888` / `zeya888.me`.

### Focus paths

- `docs/methodology/Zeya888-builder-queue/contracts/zeya888-brand-operator-contract.md`
- `zeya888/docs/requirements/REQ01-ZBRAND-landing-infra-transfer.md`
- `zeya888/docs/requirements/REQ02-ZBRAND-placeholder-content.md`
- `zeya888/docs/requirements/REQ03-ASTRO-LANDING-TRANSFORMATION.md`
- `.cursor/plans/zeya888-brand_landing_infra_transfer.plan.md`
- `.cursor/plans/zeya888-brand_doge-content-strip.plan.md`
- `.cursor/plans/Zeya888-Brand_builder.plan.md`
- `zeya888/docs/analysis/zeya888-brand-landing-infra-transfer-validation-2026-09-18.md`
- `zeya888/docs/analysis/zeya888-brand-doge-content-strip-validation-2026-09-18.md`
- `zeya888/docs/manuals/local-run.md`
- `zeya888/docs/tasks/bullrun-launch-index.md`
- `zeya888/docs/tasks/backlog-stories/INDEX.md`

## Starting focus packet

### 1) Default filled bootstrap

(Same fence as Bootstrap SSOT above.)

### 2) Overlay — must not lose after wipe

```text
### OVERLAY — zeya888-brand V session (append after VAL bootstrap)

Profile: zeya888-brand · focus: zeya888/ · Role: validator · NOT zeya888.me WordPress.

DONE (keep):
- VAL restore: t00 bootstrap pkg-000000 only; no invent STORY-ZBRAND-*
- 1A transfer validated READY (analysis note Present)
- Doge/landing content strip plan+prompt authored; strip validated PASS (stubs + [TODO] JSON)
- Local-run manual Present (PUBLIC_SITE_ORIGIN / .env.example)
- Restore card id=zeya888-brand-v already in dialog-restore-console.html
- REQ files on disk now: REQ01 / REQ02 / REQ03-ASTRO-LANDING-TRANSFORMATION (not old REQ-ZBRAND-01 naming)

OPEN / NEXT SAFE VAL ASK:
- After OP/BLD authors STORY-ZBRAND-* → P1.3/P3: ready for P4 vs story AC (do not invent stories here)
- Optional: residual comment-id cleanup (STORY-LAND/LF) / missing public ornament — non-blocking, only if operator asks «почини»
- Do not P3 on t00; do not claim product Story Done from empty backlog INDEX

Hard bans: no product code this restore; name ≠ create; no HTML edit; analysis.mdc path cites or Unknown.
```

## Smoke checklist

- [x] Title matches sidebar / restore card `zeya888-brand V`
- [x] dialogType `validator` ↔ migration-validator → role-bootstrap
- [x] builderProject `zeya888-brand` substituted; clientId N/A
- [x] Starting focus = bootstrap + overlay
- [x] No invent beyond disk + confirmed arc

## Notes for later HTML merge

| Item | Suggestion |
|------|------------|
| Card id / title | Keep `zeya888-brand-v` / **zeya888-brand V** |
| Paste strategy | Keep default VAL fence; append overlay via link/collapsible to this extract (do **not** replace default bootstrap) |
| Peer bridge | None Present — skip |
| HTML edit | Separate operator ask after more extracts land |
