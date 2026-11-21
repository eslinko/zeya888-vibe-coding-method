# Dialog restore extract — Scripts V

**UTC:** 2026-11-18T12:33:38Z  
**Prompt:** [`../../prompts/migration/migration-dialog-restore-extract.md`](../../prompts/migration/migration-dialog-restore-extract.md)

## Identity

| Field | Value |
|-------|-------|
| dialogTitle | `Scripts V` (operator + restore card `data-title="Scripts V"`) |
| dialogType | `validator` (operator shorthand `$dialogType=V`) |
| builderProject | `scripts` |
| clientId | — (not client_root) |
| workspace_root | `/Users/eslinko/Development/DOGEstonia` |
| focus_folder | `scripts` ([`../../specs/profiles.yaml`](../../specs/profiles.yaml)) |
| agent-store / transcript id | `3dad30d9-77c2-40bf-9705-6144ca12b661` |
| slug | `scripts-v` |
| extract path | `docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/scripts-v-extract.md` |

Restore-console card Present: `id="scripts-v"` · `data-title="Scripts V"` · `data-role="V"` in [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html).

## Bootstrap SSOT

| Item | Path |
|------|------|
| Wrapper | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-validator.md` |
| Role bootstrap | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md` |
| Role skill | `.cursor/skills/validator/SKILL.md` |
| Operator contract | `docs/methodology/Zeya888-builder-queue/contracts/scripts-operator-contract.md` |

### Filled default paste block

```text
@.cursor/skills/validator/SKILL.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

builder_project: scripts
focus_role: validator
workspace_root: /Users/eslinko/Development/DOGEstonia

Запусти migration bootstrap строго для validator-роли.
Load validator skill role-lock; then role-bootstrap restore packet.
```

## Context transfer

### Mission

Диалог **Scripts V** — validator / analysis + lightweight-follow-up контур профиля `scripts` (focus `scripts/`): tooling stop/start local-five, docs under `scripts/docs/`, без полного BQ mint Story для post-Done hygiene. Сессия также содержала ранние волны Capybara cutover (код в `capybara/` — contract: Capybara → `builder_project: capybara`); актуальный open focus после wipe — local-five telegram stop align + validate.

### Dialog arc (ordered)

1. **Closed (earlier) — Capybara scripts→package cutover:** implement MIG/DOC static gate; SSOT operator CLI in `capybara/`; mocha/live CLI out of that wave. Plan: `.cursor/plans/Capybara_scripts_to_package_cutover.plan.md`.  
2. **Closed — local-five-git-push skip analysis:** `local-five-git-push.sh` skips dirty trees by design; spa-app ahead 4 blocked by dirty.  
3. **Closed — telegram REUSE/orphan analysis + triage:** start knows telegram + REUSE; stop lacked telegram → orphan. Docs: `scripts/docs/analysis/local-five-telegram-reuse-orphan-2026-11-10.md`, `…/local-five-telegram-stop-orphan-triage-2026-11-10.md` (Medium/P2 ops-tooling).  
4. **Closed — track choice:** Zeya888 lightweight follow-up (**task**), **not** new STORY; LOCALFIVE-01 Done on five; gap outside AC. Plan decision: `.cursor/plans/telegram_stop_track_choice_*.plan.md`.  
5. **Closed — implement `local-five-telegram-stop-SERVICES-align`:** stop `SERVICES[]` + `user-manual.md` include telegram; static prove start/stop names MATCH. Plan: `.cursor/plans/telegram_stop_services_align_ae54a6e2.plan.md`.  
6. **Open — live validate wave:** stop-all → `:8090` not LISTEN; `stop telegram` known; next serve → `START telegram` not `REUSE`. No commit/push ordered.  
7. **This ask — restore extract only:** write `scripts-v-extract.md`; no HTML edit; no product code beyond extract path.

### Verified state

| Check | Result |
|-------|--------|
| stop SERVICES telegram entry | Present — `scripts/shell/local-five-stop.sh` L23 `telegram\|doge-telegram\|8090\|py` |
| start SERVICES telegram entry | Present — `scripts/shell/local-five-serve-and-health.sh` L24 same tuple |
| start↔stop name order | MATCH — identity, gateway, threads, aibridge, telegram, spa (static python assert 2026-11-10 implement + re-check 2026-11-18) |
| user-manual six + telegram | Present — `scripts/docs/local-five/user-manual.md` |
| orphan analysis + triage | Present under `scripts/docs/analysis/` |
| Restore card `scripts-v` | Present in `dialog-restore-console.html` |
| Peer `*-bridge.md` for Scripts V | **Absent** under `analysis/dialog-bridges/` |
| Live validate (kill/stop/serve smoke) | **Not run** in implement wave (OOS) |
| Commit of stop/manual patch | **Unknown** / not ordered in this dialog |

### File map

**Present:** profiles `scripts` · scripts-operator-contract · LOCALFIVE-01 story · local-five start/stop · user-manual · orphan + triage analysis · implement plan align · restore card · this extract · agent-store id above.

**Absent / Unknown:** dedicated dialog-bridge for Scripts V; whether stop/manual changes committed; live PID state of `:8090` at extract time; full Capybara post-cutover mocha/CLI status (separate profile).

### Decisions locked

- analysis.mdc: name ≠ create; claims from disk or Unknown.  
- Post-Done LOCALFIVE-01 hygiene → **lightweight**, not `STORY-SCR-LOCALFIVE-02` (unless OP ESCALATE for INDEX trail).  
- Stop **includes** telegram (mirror start); not document-only exclude.  
- Start REUSE semantics unchanged this wave.  
- Validate = sibling wave after implement (anti mega-plan).  
- Capybara product/CLI work → prefer `builder_project: capybara` per scripts-operator-contract.  
- Extract/HTML: no `dialog-restore-console.html` edit in extract-only runs.

### Forbidden (for restore VAL paste)

- Product code / pkg activate / commit/push unless operator explicitly orders.  
- Mint new LOCALFIVE Story for one-line SERVICES append (inflation).  
- Kill live telegram PID without explicit ask.  
- Edit `dialog-restore-console.html` in extract-only runs.  
- Write under `analysis/dialog-bridges/` from this prompt.  
- Encyclopedia dump — pointers + bootstrap + overlay only.  
- Claim live validate PASS without running smoke.

### Focus paths

- `scripts/shell/local-five-stop.sh`  
- `scripts/shell/local-five-serve-and-health.sh`  
- `scripts/docs/local-five/user-manual.md`  
- `scripts/docs/analysis/local-five-telegram-reuse-orphan-2026-11-10.md`  
- `scripts/docs/analysis/local-five-telegram-stop-orphan-triage-2026-11-10.md`  
- `scripts/docs/tasks/backlog-stories/local-five/STORY-SCR-LOCALFIVE-01-local-five-stop.md`  
- `docs/methodology/Zeya888-builder-queue/guides/lightweight-followup.md`  
- `docs/methodology/Zeya888-builder-queue/contracts/scripts-operator-contract.md`  
- `.cursor/plans/telegram_stop_services_align_ae54a6e2.plan.md`

## Starting focus packet

### 1) Default filled bootstrap

(Same fence as Bootstrap SSOT above.)

### 2) Overlay — must not lose after wipe

```text
### OVERLAY — Scripts V session (append after VAL bootstrap)

Profile: scripts · focus: scripts/ · Role: validator / lightweight follow-up.

Locked track: lightweight (task), NOT new STORY-SCR-LOCALFIVE-02.

Done this dialog:
- Implement local-five-telegram-stop-SERVICES-align
  - stop SERVICES[] includes telegram|doge-telegram|8090|py (after aibridge, before spa)
  - user-manual.md = six profiles; stop-all lists telegram
  - static prove start/stop SERVICES names MATCH

Analysis anchors:
- scripts/docs/analysis/local-five-telegram-reuse-orphan-2026-11-10.md
- scripts/docs/analysis/local-five-telegram-stop-orphan-triage-2026-11-10.md

Open next (operator must order):
1) Live validate wave: ./scripts/shell/local-five-stop.sh → :8090 not LISTEN;
   ./scripts/shell/local-five-stop.sh telegram = known;
   serve → START telegram (not REUSE).
2) Commit stop.sh + user-manual only if explicitly asked.
3) Do NOT change start REUSE / kill-on-reuse unless new ask.

Earlier session note (context only): Capybara cutover static gate was also in this chat;
route further Capybara product work to builder_project: capybara.

Agent-store / transcript: 3dad30d9-77c2-40bf-9705-6144ca12b661
```

**Overlay bullet count (for report):** 8 (locked track; implement done; 2 analysis anchors; 3 open next; agent-store note — counted as discrete must-keep lines in overlay body).

## Smoke checklist

- [x] Title matches sidebar / restore card `Scripts V`
- [x] dialogType `validator` ↔ bootstrap `migration-validator.md` → role-bootstrap
- [x] builderProject `scripts` substituted; clientId empty
- [x] Starting focus = bootstrap + overlay
- [x] No invent beyond disk + confirmed dialog arc

## Notes for later HTML merge

- Suggested card: keep existing `id="scripts-v"` / title `Scripts V` (already Present).  
- Prefer **keep default O/V paste** in card body + **link** this extract for overlay (or append OVERLAY fence under pre). Do not replace bootstrap fence.  
- Peer bridge: **Absent** — no `scripts-v-bridge.md` to merge.  
- Separate ask required to edit `dialog-restore-console.html`.
