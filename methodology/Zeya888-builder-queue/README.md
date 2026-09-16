# Zeya888 Builder Queue

Author methodology **Zeya888** for managed development with an AI agent in Cursor: machine-readable queue (`pkg-*.yaml`), phases P0–P8, build windows, and operator contracts.

**Brand:** Zeya888 · **Version:** see [`VERSION`](./VERSION) · **Map:** [`MANIFEST.md`](./MANIFEST.md)

## Document roles

| Role | Examples | Rule |
|------|----------|------|
| **Teaching** | `curriculum/`, `prompts/training/` | Learning and navigation |
| **Normative** | `core/workflow.md`, `session-starter.md`, `contracts/`, `specs/` | Canon for operator and agent |
| **Legacy** | `core/workflow-legacy.md` | Historical full prompts; phase numbering may differ |

On conflict, teaching AI follows **normative**.

## First entry (human)

1. Entry manual — [`curriculum/human-entry-manual.md`](./curriculum/human-entry-manual.md)
2. Training dialogues — [`prompts/training/INDEX.md`](./prompts/training/INDEX.md)
3. Two routes (tech / fintech) — [`curriculum/learning-path.md`](./curriculum/learning-path.md)
4. Guided adoption — [`guides/consultation-positioning.md`](./guides/consultation-positioning.md)

Method meaning: [`curriculum/00-guide-for-humans.md`](./curriculum/00-guide-for-humans.md).

## Quick start (operative — already familiar with the method)

1. Install Cursor integration — [`integration/cursor-setup.md`](./integration/cursor-setup.md)
2. Configure project profile — [`specs/profiles.yaml`](./specs/profiles.yaml)
3. New chat: `@docs/methodology/Zeya888-builder-queue/core/session-starter.md` + `builder_project: …`
4. Verify: `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project gateway --verify`

## Structure

| Directory | Purpose |
|-----------|---------|
| [`core/`](./core/) | Workflow P1–P8, session starter, legacy prompts |
| [`cli/`](./cli/) | `builder_resolve_queue.py`, queue manual |
| [`specs/`](./specs/) | Input package contract, `profiles.yaml` |
| [`contracts/`](./contracts/) | Operator contracts (gateway, gpt, identity, …) |
| [`templates/`](./templates/) | Builder plan template |
| [`examples/`](./examples/) | Reference plans (teaching) + sample profiles |
| [`curriculum/`](./curriculum/) | Learning path + human entry |
| [`prompts/training/`](./prompts/training/) | Training dialogues (not operative) |
| [`integration/`](./integration/) | Cursor wiring |
| [`analysis/`](./analysis/) | Reconcile / unification notes |

## Runtime vs teaching

| Layer | SSOT | Purpose |
|-------|------|---------|
| Method | `core/workflow.md`, contracts | Operator prompts and rules |
| CLI | `cli/builder_resolve_queue.py` | Verify, list, build window |
| Project | `.cursor/plans/*_builder.plan.md` | Operative execution (P3/P6) |
| Examples | `examples/reference-plans/` | Course snapshots — **not** P3 attach |

**Cursor:** [`.cursor/skills/builder-session/SKILL.md`](../../.cursor/skills/builder-session/SKILL.md), [`.cursor/rules/builder-operator-habits.mdc`](../../.cursor/rules/builder-operator-habits.mdc).

## Profiles (DOGEstonia)

| `--project` | Status |
|-------------|--------|
| `gateway` | active |
| `gpt` | active |
| `identity` | active |
| `spa` | active |
| `taxonomy` | active (**queueless** — `--verify` only; meta-script TC0–TC7, no `pkg-*.yaml`) |

Also see `landing`, `capybara`, `scripts`, `zeya888`, `arweave`, `dogestonia`, `aibridge` in [`specs/profiles.yaml`](./specs/profiles.yaml).

## Learning

**Start:** [`curriculum/human-entry-manual.md`](./curriculum/human-entry-manual.md) · meaning: [`curriculum/00-guide-for-humans.md`](./curriculum/00-guide-for-humans.md)

Routes A/B + modules 0–6: [`curriculum/learning-path.md`](./curriculum/learning-path.md) · PA + Studio: [`curriculum/06-architect-studio-and-p1-intakes.md`](./curriculum/06-architect-studio-and-p1-intakes.md) · operative §PA: [`core/workflow.md`](./core/workflow.md)
