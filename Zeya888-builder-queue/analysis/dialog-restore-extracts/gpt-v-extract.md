# Dialog restore extract — GPT V

**UTC:** 2026-11-18T12:13:15Z (`builder_resolve_queue.py --print-utc-now`)  
**Prompt:** [`../../prompts/migration/migration-dialog-restore-extract.md`](../../prompts/migration/migration-dialog-restore-extract.md)

## Identity

| Field | Value |
|-------|-------|
| dialogTitle | `GPT V` |
| dialogType | `validator` (operator shorthand `$dialogType=V`) |
| builderProject | `gpt` |
| clientId | — |
| workspace_root | `/Users/eslinko/Development/DOGEstonia` |
| focus_folder | `GPT UI` ([`../../specs/profiles.yaml`](../../specs/profiles.yaml) `gpt:`) |
| agent-store id | `18621530-a294-4a55-bcd2-3cd527e3537e` |
| slug | `gpt-v` |
| extract path | `docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/gpt-v-extract.md` |

Restore-console card Present: `id="gpt-v"` · `data-title="GPT V"` · `data-role="V"` in [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html).

## Bootstrap SSOT

| Item | Path |
|------|------|
| Wrapper | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-validator.md` |
| Role bootstrap | `docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md` |
| Role skill | `.cursor/skills/validator/SKILL.md` |
| Operator contract | `docs/methodology/Zeya888-builder-queue/contracts/gpt-operator-contract.md` |

### Filled default paste block

```text
@.cursor/skills/validator/SKILL.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

builder_project: gpt
focus_role: validator
workspace_root: /Users/eslinko/Development/DOGEstonia

Запусти migration bootstrap строго для validator-роли.
Load validator skill role-lock; then role-bootstrap restore packet.
```

## Context transfer

### Mission

Диалог **GPT V** — validator / Architect Studio analysis-контур профиля `gpt` (`GPT UI/`): выравнивание role-instruction SSOT под REQ-14/15 peers (aibridge/TG), без runtime Python/Telegram как владельца. В подтверждённой дуге: REQ-49/50 target-tech + backlog + deepen T* + (позже) P3 Apply на phantom ban; сейчас операторский ask = **dialog restore extract** (docs-only).

### Dialog arc (ordered)

1. **Closed — REQ-49 Architect Studio:** operator locks S1/O1/C2/E2/X1/D1 → materialize `architecture/req-49-role-orchestration-instruction-alignment/` `00`–`03` + interview report.  
2. **Closed — REQ-49 backlog + deepen:** ROL-08…12 stories + T*; package INDEX; Apply waves later marked Done (Awaiting Commits) on disk.  
3. **Closed — REQ-50:** tech-arch `req-50-citizen-session-reset-instruction-ack/` (T2/D1/C2/X1/V1) + ROL-13/14 backlog + T*; both Done (Awaiting Commits) · ROL-13/14 P3 Applied on disk.  
4. **Closed — ROL-15 deepen (docs):** arch sibling [`04-no-phantom-control-promises.md`](../../../../../GPT%20UI/docs/architecture/req-49-role-orchestration-instruction-alignment/04-no-phantom-control-promises.md) + story T01–T08 + INDEX note (plan wave 2026-11-16T18:45:58Z, Apply deferred **at deepen**).  
5. **Closed — ROL-15 P3 Apply (disk as-of extract):** Status **Done (Awaiting Commits)** · pkg-000078 GIM-537…544 · Delivery class PRODUCT phantom ban Applied `2026-11-16T18:58:47Z` · soft peer fence moved to **STORY-AIBRIDGE-90** Draft/Code Open (88 docs Closed).  
6. **Open — this turn:** Migration dialog-restore extract only; **no** HTML merge; **no** product/VAL audit unless operator asks next.

### Verified state

| Check | Result |
|-------|--------|
| Profile `gpt` | Present — `focus_folder: "GPT UI"` in `profiles.yaml` |
| Restore card `gpt-v` | Present — default VAL fence matches filled bootstrap |
| REQ-49 arch `00`–`04` | Present under `GPT UI/docs/architecture/req-49-…/` |
| REQ-49 stories ROL-08…12 + 15 | Present; INDEX Progress **6/6 Done** (Awaiting Commits) |
| ROL-15 phantom ban in `core.md` | Present — L31–32, Ownership table, Present-only / Forbidden lines |
| REQ-50 package ROL-13/14 | Present · **2/2 Done** (Awaiting Commits) |
| Export evidence path | Present — `GPT UI/docs/analysis/req-48-export-parity-evidence.md` (ROL-04/11/14/15 cites) |
| Peer dialog-bridge for **GPT V** | **Absent** under `analysis/dialog-bridges/` (only `alvasar-gpt-…` peer — different profile) |
| Soft peer aibridge **90** | Story Meta cites Draft · Code/AC Open (do not invent Done) |

**Honesty tension (cite, do not invent fix):** `core.md` Ownership still names **STORY-AIBRIDGE-88** as Code/AC Open fence in places, while ROL-15 Meta/INDEX fence **90** Draft / 88 docs Closed — residual prose drift for a later VAL ask.

### File map

**Present:** gpt contract · restore card · REQ-49 arch+backlog · REQ-50 arch+backlog · `instructions-roles/core.md` (+ interviewer) phantom ban · this extract.

**Absent / Unknown:** dedicated `gpt-v-bridge.md`; full transcript JSONL beyond agent-store id; whether operator wants next ask = VAL drift-audit (88→90) vs unrelated wave.

### Decisions locked

- GPT owns instruction **texts** only; server owns buttons/actions mint.  
- Present-only CTA naming · phantom ban · empty→honest wait.  
- Soft peers: **87** Present · TG-11/12 Done · **90** Code/AC Open (≠ live prepare-without-Looks-right).  
- Name ≠ create; packaging N/A for GPT Docker; export Pass ≠ orchestration Pass.  
- Do not confuse `builder_project: gpt` with `alvasar-gpt`.

### Forbidden (for restore VAL paste)

- Product code / aibridge / telegram patches unless operator orders.  
- Invent AC-90 / AC-62 / hybrid-88 Done.  
- Edit `dialog-restore-console.html` in extract-only runs.  
- Write under `analysis/dialog-bridges/` from this prompt.  
- Commit/push without explicit order.

### Focus paths

- `GPT UI/docs/requirements/REQ-49-req14-role-orchestration-instruction-alignment.md`  
- `GPT UI/docs/architecture/req-49-role-orchestration-instruction-alignment/00-overview.md` · `04-no-phantom-control-promises.md`  
- `GPT UI/docs/tasks/backlog-stories/req-49-role-orchestration-instruction-alignment/` (esp. ROL-15)  
- `GPT UI/docs/requirements/REQ-50-req15-citizen-session-reset-instruction-ack.md`  
- `GPT UI/docs/tasks/backlog-stories/req-50-citizen-session-reset-instruction-ack/`  
- `GPT UI/instructions-roles/core.md` · `interviewer.md`  
- `docs/methodology/Zeya888-builder-queue/contracts/gpt-operator-contract.md`

## Starting focus packet

### 1) Default filled bootstrap

(Same fence as Bootstrap SSOT above.)

### 2) Overlay — must not lose after wipe

```text
### OVERLAY — GPT V session (append after VAL bootstrap)

Profile: gpt · focus: GPT UI/ · Role: validator / Architect Studio analysis (this chat also ran target-tech + backlog deepen).

DONE (keep):
- REQ-49 arch 00–04 + ROL-08…12 Done (Awaiting Commits)
- REQ-50 arch + ROL-13/14 Done (Awaiting Commits) · reset prose Applied
- ROL-15 tech deepen + P3 phantom ban Applied (pkg-000078) · arch 04 Present
- Soft peers honesty: 87 Present · TG-11/12 Done · fence 90 Code/AC Open · ≠ invent Done

OPEN / NEXT SAFE VAL ASK:
- Optional: audit core.md 88-vs-90 fence wording drift vs ROL-15 Meta (docs-only unless OP orders Apply)
- Do not start new STORY / invent 90 Code without aibridge OP
- This extract wave: no HTML edit; restore card gpt-v already Present

Hard bans: no product/runtime code; name ≠ create; no dialog-bridges write; analysis.mdc path:line or Unknown.
Must keep after wipe: agent-store 18621530-a294-4a55-bcd2-3cd527e3537e · extract gpt-v-extract.md · soft-peer fence 90 Open.
```

**Overlay bullets count:** 12 (4 DONE + 3 OPEN + 4 Hard bans/must-keep lines + 1 profile header treated as context — countable operator overlay items: **11** content bullets under DONE/OPEN/Hard).

## Smoke checklist

- [x] Title matches sidebar / restore card `GPT V`
- [x] dialogType `validator` ↔ migration-validator → role-bootstrap
- [x] builderProject `gpt` substituted; clientId N/A
- [x] Starting focus = bootstrap + overlay
- [x] No invent beyond disk + confirmed arc

## Notes for later HTML merge

| Item | Suggestion |
|------|------------|
| Card id / title | Keep `gpt-v` / **GPT V** |
| Paste strategy | Keep default VAL fence; append overlay via link/collapsible to this extract (do **not** replace default bootstrap) |
| Peer bridge | None Present for GPT V — skip (`alvasar-gpt-profile-bootstrap-bridge.md` is **other** profile) |
| HTML edit | Separate operator ask after more extracts land |

## Operator context (filled)

- dialogTitle=`GPT V`
- dialogType=`validator`
- builderProject=`gpt`
- clientId=
- topic=`dialog restore extract` (live ask) · prior arc REQ-49/50/ROL-15
- already Done=`REQ-49 ROL-08…12+15` · `REQ-50 ROL-13/14` · phantom ban Applied
- must keep after wipe=`soft peer 90 Open` · `arch 04` · `gpt-v` card · this extract
