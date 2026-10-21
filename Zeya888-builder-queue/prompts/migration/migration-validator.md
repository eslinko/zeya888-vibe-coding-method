# Migration bootstrap — Validator role

Обёртка над [`migration-role-bootstrap.md`](./migration-role-bootstrap.md) для роли `validator`.

**Ветки VAL:**

| Ветка | Когда | Prompt |
|-------|-------|--------|
| Story audit P4/P7 | Очередь / story AC | role-bootstrap `focus_role: validator` |
| Lightweight follow-up | Done story + small gap; ?STORY | [`../operator/lightweight-followup-triage.md`](../operator/lightweight-followup-triage.md) → author |

```text
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

builder_project: <gateway|gpt|spa|taxonomy|identity|scripts|capybara|landing|zeya888|arweave|dogestonia|aibridge|zeya888-brand|threads|floou>
focus_role: validator
workspace_root: /Users/eslinko/Development/DOGEstonia

Запусти migration bootstrap строго для validator-роли.
```

Lightweight (после Done, без новой STORY) — сначала:

```text
@docs/methodology/Zeya888-builder-queue/prompts/operator/lightweight-followup-triage.md

builder_project: <key>
$gap=
$parentStoryOrPkg=
$ask=
```
