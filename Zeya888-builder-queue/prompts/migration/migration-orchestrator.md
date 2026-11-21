# Migration bootstrap — Orchestrator role

Обёртка над [`migration-role-bootstrap.md`](./migration-role-bootstrap.md) для роли `orchestrator`.  
Role skill: [`.cursor/skills/orchestrator/SKILL.md`](../../../../../.cursor/skills/orchestrator/SKILL.md).

```text
@.cursor/skills/orchestrator/SKILL.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

builder_project: <gateway|gpt|spa|taxonomy|identity|aibridge|scripts|capybara|landing|zeya888|arweave|dogestonia|zeya888-brand|threads|floou|alvasar-backend|alvasar-ui|alvasar-gpt|telegram>
focus_role: orchestrator
workspace_root: /Users/eslinko/Development/DOGEstonia

Запусти migration bootstrap строго для orchestrator-роли.
Load orchestrator skill role-lock; then role-bootstrap restore packet.
```
