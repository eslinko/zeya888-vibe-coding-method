# Client tenancy — nested clients under workspace

> **Gap/triage:** [`../../../analysis/zeya888-multi-client-layout-gap-2026-10-24.md`](../../../analysis/zeya888-multi-client-layout-gap-2026-10-24.md) · [`../../../analysis/zeya888-multi-client-layout-triage-2026-10-24.md`](../../../analysis/zeya888-multi-client-layout-triage-2026-10-24.md)  
> **Claims:** [`.cursor/rules/analysis.mdc`](../../../../.cursor/rules/analysis.mdc)  
> **Не заменяет:** flat DOGEstonia / Floou / landing profiles · classic-four architect maps for DOGE

## 1. Model

| Layer | Path (from workspace root) | Role |
|-------|----------------------------|------|
| Client root | `clients/<ClientName>/` | Business docs, parent REQ, portable methodology pack, duplicated `*_builder.plan.md` |
| Microservice focus | `clients/<ClientName>/<ms>/` | One Builder Queue `focus_folder` (code + `docs/tasks/`) |
| Registry | [`../specs/clients.yaml`](../specs/clients.yaml) | Maps `client_id` → root path + profile keys |

**DOGEstonia and other flat peers stay at workspace root.** Do not relocate them into `clients/`.

## 2. Nested `focus_folder` (allowed)

`focus_folder` / `tasks_dir` may contain `/` (e.g. `clients/Alvasar/backend`).  
CLI joins `workspace_root / relative` ([`builder_resolve_queue.py`](../cli/builder_resolve_queue.py)).  
`test_command` must `cd` the same nested path.

See also [`add-builder-profile.md`](./add-builder-profile.md) §0 · [`profiles-fields.md`](../specs/profiles-fields.md).

## 3. Client root layout (convention)

```text
clients/<ClientName>/
  README.md
  CLIENT.yaml                 # local mirror of clients.yaml entry (optional but recommended)
  docs/
    requirements/             # parent / product REQs for this client
    business/                 # business-level notes
    analysis/                 # client-local analysis (e.g. scaffold starting points)
  backend/                    # example MS — profile focus (name may vary)
  ui/                         # example MS — profile focus
  .cursor/plans/              # copies of *_builder.plan.md for this client (portable)
  methodology/                # how to continue Zeya888 work if repo is opened alone
```

Minimum MS set for a typical client: **backend** + **ui** (names may differ; register each as its own `builder_project`).  
Optional third focus: **ai** / instruction pack folder — same profile rules when needed (`G6`).

## 4. Portable methodology in the client git

Client repo should contain enough to continue work after import into another IDE/workspace:

1. Duplicated `.cursor/plans/*_builder.plan.md` for each client profile (keep in sync with workspace `.cursor/plans/`).
2. `methodology/README.md` — pointers to Zeya888 method (or vendored snapshot if operator orders).
3. `docs/tasks` under each MS focus — bullrun, pkg, pipeline (as any profile).

**Dual plan sync:** edit workspace plan first (or both in one commit wave); copy identical bytes into `clients/<Client>/.cursor/plans/`.

Primary method SSOT remains `docs/methodology/Zeya888-builder-queue/` in the DOGEstonia workspace when present.

## 5. Architect notes (W5 lite / G3)

- DOGE classic-four scatter/bootstrap **unchanged** (`gateway` / `identity` / `spa` / `gpt` path maps).
- For a client: parent REQ under `clients/<Client>/docs/requirements/`; child REQs under `{focus}/docs/requirements/`; profiles = keys listed in `clients.yaml`.
- Do **not** force classic-four folder names onto client MS; use the client’s `backend` / `ui` / optional `ai` focuses.
- Cross-project orientation for a client = this guide + `clients.yaml` entry; not a rewrite of DOGE scatter prompts.
