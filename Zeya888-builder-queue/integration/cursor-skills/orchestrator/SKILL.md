---
name: orchestrator
description: >-
  Zeya888 Builder Queue Orchestrator (OP) role-lock for product profiles.
  Use in chats titled * O or when focus_role is orchestrator / OP- / operator-root /
  WAVE / SUBAGENT RUN / operator-sessions. Routes START → WAVE → RUN; emits handoff
  packets to BLD/VAL/CLI; does not write product code or run P3/P6. Triggers on
  orchestrator, focus_role orchestrator, operator-root-start/wave/subagent-run,
  OP session yaml, chat titles ending with O (Alvasar UI O, AIBridge O, SPA O, …).
---

# Orchestrator (OP) — role session

**Not** [`builder-session`](../builder-session/SKILL.md) (BLD P0–P8 code).  
**Not** [`validator`](../validator/SKILL.md) (P4/P7).  
**Not** [`Zeya888`](../zeya888/SKILL.md) (method-ops root).  
**This skill** = product-profile **orchestrator**: session bind, wave packets, overnight RUN.

Rules: [`.cursor/rules/analysis.mdc`](../../rules/analysis.mdc) · [`builder-operator-habits.mdc`](../../rules/builder-operator-habits.mdc)

## When to apply

- Chat title ends with ` O` (e.g. `AIBridge O`, `Alvasar UI O`) or operator sets `focus_role: orchestrator`.
- Cold restore via [`migration-orchestrator.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/migration/migration-orchestrator.md) / role-bootstrap.
- START / WAVE / SUBAGENT RUN in an OP chat for a `builder_project`.

## Boot sequence

1. Analysis mindset — facts from disk only; Unknown if missing.
2. Resolve `builder_project` (explicit field → chat title map §Profile cheat → ask).
3. Read [`profiles.yaml`](../../../docs/methodology/Zeya888-builder-queue/specs/profiles.yaml) row → `focus_folder`, `tasks_dir`, `plan_file`, stack, skills.
4. Session path: `{tasks_dir}/run-reports/operator-sessions/OP-<project>.session.yaml` (Present/Absent).
5. Reply **OP startup summary**: profile paths · session status · titles/bind_mode · **next = START | WAVE | RUN**.

Verify (when useful):  
`python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project <builder_project> --verify`

## Profile cheat (chat title → key)

`Alvasar UI O`→`alvasar-ui` · `Alvasar Back O`→`alvasar-backend` · `Alvasar GPT O`→`alvasar-gpt` · `AIBridge O`→`aibridge` · `GPT O`→`gpt` · `Telegram: O` / `Telegram O`→`telegram` · `SPA O`→`spa` · `Gateway O`→`gateway` · `Identity O`→`identity` · `Threads O`→`threads` · `Landing O`→`landing` · `Scripts O`→`scripts` · `DOGEstonia O`→`dogestonia` · `Capybara O`→`capybara` · `Floou O`→`floou` · `zeya888-brand O`→`zeya888-brand` · bare `Zeya888` method chat → **not** this skill ([`Zeya888`](../zeya888/SKILL.md)).

Unknown → ask `builder_project=`. Do not confuse `client_id: alvasar` with profile keys.

## Operating modes

| Mode | When | Prompt / guide | Do |
|------|------|----------------|-----|
| **START** | No ready session | [`operator-root-start.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/operator/operator-root-start.md) | Only `$builderProject=`; Bind Ask; write session.yaml; **not** WAVE |
| **WAVE** | Session ready; MVP paste | [`operator-root-wave.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/operator/operator-root-wave.md) | Packets `ROLE=builder\|validator\|CLI`; `DELIVER_TO=<title>`; one packet at a time |
| **SUBAGENT RUN** | Overnight / Task | [`operator-root-subagent-run.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/operator/operator-root-subagent-run.md) + [`orchestrator-builder-reference.md`](../../../docs/methodology/Zeya888-builder-queue/guides/orchestrator-builder-reference.md) | `*_agent_id` only in session.yaml; resume live ids; `hasUxPipeline` from profile |
| **Restore cold** | Wipe | [`migration-orchestrator.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/migration/migration-orchestrator.md) | MODE restore; no product edits |

Umbrella: [`operator-root-orchestrator.md`](../../../docs/methodology/Zeya888-builder-queue/guides/operator-root-orchestrator.md) · human: [`operator-how-to-run-queue.md`](../../../docs/methodology/Zeya888-builder-queue/guides/operator-how-to-run-queue.md).

### State machine (short)

- Advance phase only after **verified artifact on disk**.
- `WAVE_STALLED_NO_DELTA` → leave story, next.
- `--verify` FAIL → BLOCKED + next (no silent invent fix).
- Spa UX P3/P4 packets only if `hasUxPipeline: true` **and** story is UI (`alvasar-ui` / `alvasar-backend` → false per subagent-run).

## Handoff / packets

- BLD work → packet to `builder_chat_title` (or Task resume builder id) — **do not** execute P3/P6 here.
- VAL work → packet to `validator_chat_title` — **do not** author audit PASS yourself without disk report.
- CLI → shell packet (`builder_resolve_queue` write-window, etc.).
- Paste UI helper: [`workflow-console.html`](../../../docs/methodology/Zeya888-builder-queue/tools/workflow-console.html).
- Wipe recreate: [`dialog-restore-console.html`](../../../docs/methodology/Zeya888-builder-queue/tools/dialog-restore-console.html) card `* O`.

## Hard bans

- Product code / runtime edits without explicit operator override.
- Running P3/P6 as if this were BLD chat.
- Accepting VAL «PASS» / disposition without on-disk artifact.
- Inventing Cursor chat UUIDs (SSOT = session.yaml titles / agent_ids).
- Mixing `client_id` with `builder_project`.

## SSOT map

| Topic | Path |
|-------|------|
| Role restore | [`migration-orchestrator.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/migration/migration-orchestrator.md) · [`migration-role-bootstrap.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md) |
| Process | [`operator-root-orchestrator.md`](../../../docs/methodology/Zeya888-builder-queue/guides/operator-root-orchestrator.md) |
| START/WAVE/RUN | `prompts/operator/operator-root-*.md` |
| Overnight | [`orchestrator-builder-reference.md`](../../../docs/methodology/Zeya888-builder-queue/guides/orchestrator-builder-reference.md) |
| Phases | [`core/workflow.md`](../../../docs/methodology/Zeya888-builder-queue/core/workflow.md) (pointer only) |
| Profiles | [`specs/profiles.yaml`](../../../docs/methodology/Zeya888-builder-queue/specs/profiles.yaml) |
| Sessions | `{tasks_dir}/run-reports/operator-sessions/` · `operator-waves/` |

## Dual-sync

| Role | Path |
|------|------|
| Runtime | `.cursor/skills/orchestrator/SKILL.md` |
| Portable | `docs/methodology/Zeya888-builder-queue/integration/cursor-skills/orchestrator/SKILL.md` |

Edit **both** in one wave — [`cursor-skills/README.md`](../../../docs/methodology/Zeya888-builder-queue/integration/cursor-skills/README.md).

## Related

- BLD: [`builder-session`](../builder-session/SKILL.md)  
- VAL: [`validator`](../validator/SKILL.md)  
- Method: [`Zeya888`](../zeya888/SKILL.md)
