# Migration — dialog restore extract (restore-HTML docking)

**Категория:** migration (живой диалог → restore extract pack)  
**Output home (default):** [`../../analysis/dialog-restore-extracts/`](../../analysis/dialog-restore-extracts/)  
**Naming:** `{sidebar-slug}-extract.md`  
**Peers:** [`migration-dialog-restore-extract-root-cross.md`](./migration-dialog-restore-extract-root-cross.md) (Root/Cross) · [`migration-dialog-restore-extract-fixup.md`](./migration-dialog-restore-extract-fixup.md) (доработка существующего) · [`migration-dialog-context-bridge.md`](./migration-dialog-context-bridge.md) · [`migration-role-bootstrap.md`](./migration-role-bootstrap.md) · [`migration-orchestrator.md`](./migration-orchestrator.md) · [`migration-validator.md`](./migration-validator.md) · [`../architect/client-product-root-orientation.md`](../architect/client-product-root-orientation.md) · [`../architect/cross-project-system-orientation.md`](../architect/cross-project-system-orientation.md)  
**UI consumer (later wave):** [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

Универсальный extract: оператор передаёт **title + profile + dialog type**; агент читает **дефолтный bootstrap** для класса, снимает полный контекст живого диалога и пишет pack со **starting focus packet** (bootstrap + overlays).  
**Root / Cross / system-root** → prefer [`migration-dialog-restore-extract-root-cross.md`](./migration-dialog-restore-extract-root-cross.md) (orientation init, not O/V).  
Не путать с [`migration-dialog-context-bridge.md`](./migration-dialog-context-bridge.md) → `analysis/dialog-bridges/` (handoff → чистый агент).

---

## When

| Use case | Да / нет |
|----------|----------|
| Выборочный живой O/V / role диалог → extract под restore HTML | **Да** |
| Root / Cross / system-root (Alvasar Root, Cross-project, …) | **Нет** → [`migration-dialog-restore-extract-root-cross.md`](./migration-dialog-restore-extract-root-cross.md) |
| Handoff → полностью чистый агент (topic meta / method layer) | **Нет** → [`migration-dialog-context-bridge.md`](./migration-dialog-context-bridge.md) |
| Только role bootstrap без диалоговой дуги | **Нет** → [`migration-role-bootstrap.md`](./migration-role-bootstrap.md) / O·V wrappers |
| Bulk export всех Composer чатов | **Нет** → [`migration-workspace-chat-export.md`](./migration-workspace-chat-export.md) |
| Регенерация `dialog-restore-console.html` из extracts | **Нет** — отдельный operator ask после заполнения папки |

---

## Classification → bootstrap SSOT

Агент **обязан** загрузить bootstrap с диска по `$dialogType` (не invent). Подставить `$builderProject` / `$clientId` в fence как в restore HTML.

| `$dialogType` | Default bootstrap (read from disk) | Role skill |
|---------------|------------------------------------|------------|
| `orchestrator` | [`migration-orchestrator.md`](./migration-orchestrator.md) fence → [`migration-role-bootstrap.md`](./migration-role-bootstrap.md) | `@.cursor/skills/orchestrator/SKILL.md` |
| `validator` | [`migration-validator.md`](./migration-validator.md) fence → role-bootstrap | `@.cursor/skills/validator/SKILL.md` |
| `client_root` | [`../architect/client-product-root-orientation.md`](../architect/client-product-root-orientation.md) | — |
| `cross_project` | [`../architect/cross-project-system-orientation.md`](../architect/cross-project-system-orientation.md) | — |
| `capybara_a` | [`capybara/docs/manuals/prompts/p1-operator-bootstrap.md`](../../../../../capybara/docs/manuals/prompts/p1-operator-bootstrap.md) + USER-MANUAL (если Present) | — |
| `method_ops` | [`.cursor/skills/zeya888/SKILL.md`](../../../../../.cursor/skills/zeya888/SKILL.md) + latest matching [`../../analysis/dialog-bridges/*-bridge.md`](../../analysis/dialog-bridges/) | `zeya888` |

Slug: kebab от `$dialogTitle` (точное sidebar имя). Пример: `AIBridge O` → `aibridge-o-extract.md`.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-dialog-restore-extract.md
@docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/README.md
@docs/methodology/Zeya888-builder-queue/MANIFEST.md

$dialogTitle=
$dialogType=
$builderProject=
$clientId=
$topic=
$extractOutDir=docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts

Migration — DIALOG RESTORE EXTRACT (restore-HTML docking).

MODE: analysis.mdc. Facts from disk + confirmed dialog arc only. No product code.
No commit/push unless explicitly ordered. Name ≠ create outside extract path.
Do NOT dump encyclopedia — pointers + filled bootstrap fence + overlays.
Do NOT write under analysis/dialog-bridges/ (that is bridge prompt).
Do NOT edit dialog-restore-console.html in this run.

## Identify

1) $dialogTitle = exact sidebar / restore-card title (required).
2) $dialogType = one of: orchestrator | validator | client_root | cross_project | capybara_a | method_ops
3) $builderProject = profile key for O/V (aibridge, alvasar-ui, telegram, …). Empty for client_root.
4) $clientId = required when dialogType=client_root (e.g. alvasar). Else empty.
5) Resolve bootstrap path from Classification table in THIS prompt; Read that file; fill builder_project / clientId / workspace_root.
6) slug = kebab-case of $dialogTitle; out = {$extractOutDir}/{slug}-extract.md

## Deliverables (strict order)

1) Mirror in chat (5–10 sentences): identified title/type/profile|client + which bootstrap path loaded + out path.
2) Write extract file at `out` with REQUIRED sections below.
3) Report: extract path | slug | dialogType | bootstrap path | Unknowns. STOP.

## Extract file — required sections

### Identity
- dialogTitle, dialogType, builderProject and/or clientId
- workspace root, transcript/agent-store id if known, UTC
- slug, extract path

### Bootstrap SSOT
- Absolute/repo-relative path of default bootstrap used
- Role skill path if any
- **Filled default paste block** — full fence from bootstrap SSOT with substitutions applied (do not truncate)

### Context transfer
- Mission (why this dialog exists)
- Dialog arc (ordered waves / decisions; closed vs open)
- Verified state (commands + on-disk results)
- File map Present/Absent · Decisions locked · Forbidden
- Focus paths (REQ/story/plan/contracts) relevant to $topic if set

### Starting focus packet
Ready first paste for recreate after wipe:
1) Default filled bootstrap (same as Bootstrap SSOT fence)
2) **Overlay** — what must not be lost: active stories, open asks, session paths, last agreed next step
Mark overlay clearly so a later HTML merge can append or replace card body.

### Smoke checklist
- [ ] Title matches sidebar
- [ ] dialogType ↔ bootstrap path correct
- [ ] builderProject / clientId substituted
- [ ] Starting focus = bootstrap + overlay
- [ ] No invent beyond disk + confirmed arc

### Notes for later HTML merge
- Suggested restore-console card id / title
- Whether card should replace default O/V/Root paste or keep default + link extract
- Peer bridge path if one exists (do not copy bridge body unless needed for overlay)

## Operator context (fill)

- dialogTitle=
- dialogType=orchestrator|validator|client_root|cross_project|capybara_a|method_ops
- builderProject=
- clientId=
- topic=
- already Done=
- must keep after wipe=

## Report

Reply: mirror ok | extract path | slug | dialogType | bootstrap path | overlay bullets count | Unknowns.
STOP unless operator asks follow-up.
```

---

## Примечания

- Hard `@` in paste = analysis.mdc + this prompt + restore-extracts README + MANIFEST; bootstrap path resolved by `$dialogType` from disk.
- Outputs live under `$extractOutDir` (default `analysis/dialog-restore-extracts/`), not under `prompts/` or `tools/`.
- Name ≠ create: do not materialize product stubs because extract names them.
- HTML актуализация — только по отдельному ask после заполнения папки.
