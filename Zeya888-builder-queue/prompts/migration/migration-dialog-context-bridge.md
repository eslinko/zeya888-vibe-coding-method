# Migration — dialog context bridge (clean-agent handoff)

**Категория:** migration (session / dialog continuity → новый чистый агент)  
**Output home (default):** [`../../analysis/dialog-bridges/`](../../analysis/dialog-bridges/)  
**Naming:** `{dialogName}-bridge.md`  
**Peers:** [`migration-self-restore-zeya888-method.md`](./migration-self-restore-zeya888-method.md) · [`migration-role-bootstrap.md`](./migration-role-bootstrap.md) · [`migration-workspace-chat-export.md`](./migration-workspace-chat-export.md) · [`migration-dialog-restore-extract.md`](./migration-dialog-restore-extract.md) (restore-HTML docking — different out dir)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

Универсальный handoff: **фокусный проектный** или **кросс-проектный** диалог. Цель — сохранить не только хвост чата, а **мета-понимание фокусных тем** (SSOT на диске) + operative state.  
Не заточен под bootstrap профилей; Path A–D — только conditional appendix.

---

## When

| Use case | Да / нет |
|----------|----------|
| Handoff диалога → чистый агент с topic meta + thin method + instance | **Да** (`$bridgeScope=full`, default) |
| Узкий snapshot одной волны | Только явно `$bridgeScope=operative` |
| Bulk export всех Composer/Agent чатов | **Нет** → [`migration-workspace-chat-export.md`](./migration-workspace-chat-export.md) |
| Только restore роли BLD/VAL/OP | **Нет** → [`migration-role-bootstrap.md`](./migration-role-bootstrap.md) |
| Только METHOD SNAPSHOT без дуги диалога | **Нет** → [`migration-self-restore-zeya888-method.md`](./migration-self-restore-zeya888-method.md) (можно `@` рядом) |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-dialog-context-bridge.md
@docs/methodology/Zeya888-builder-queue/analysis/dialog-bridges/README.md
@docs/methodology/Zeya888-builder-queue/MANIFEST.md

$dialogName=
$dialogKind=mixed
$bridgeOutDir=docs/methodology/Zeya888-builder-queue/analysis/dialog-bridges
$bridgeScope=full
$topic=
$focusProjects=
$doneHint=
$nextHint=

Migration — DIALOG CONTEXT BRIDGE (clean-agent handoff).

MODE: analysis.mdc. Facts from disk only. No product code unless operator later asks.
No commit/push unless explicitly ordered. Name ≠ create / ask-scoped.
Do NOT dump full workflow.md / Gateway plan / encyclopedia — pointers + tables.
Do NOT hard-require profile bootstrap paths A–D unless dialogKind=method_ops OR this dialog practiced profile bootstrap.

$dialogKind (default mixed if empty):
  project_focus  — one builder_project / one client MS focus
  cross_project  — multi-profile, parent/child REQ, scatter/audit, client root
  method_ops     — methodology / profile registry / tenancy / console (ops on the method itself)
  mixed          — combination; state which parts dominate

$bridgeScope:
  full (DEFAULT) = Topic meta map + Dialog arc + thin Method layer + verified instance + kind-derived launch recipes
  operative      = narrow last-wave snapshot only (ONLY if operator set this)

## Deliverables (strict order)

1) Mirror in chat (5–10 sentences): understood ask + key vectors + out-of-scope.
2) Improved operator prompt (v2) in chat — reusable; point at THIS migration prompt + $bridgeOutDir + $bridgeScope=full + $dialogKind=…
3) Write bridge file:
   path = {$bridgeOutDir}/{$dialogName}-bridge.md
   If $dialogName empty → short kebab from $topic / mission; state chosen name.
   If $bridgeOutDir empty → default above.
   Load extra @ paths from disk by dialogKind (profiles.yaml, focus REQs/arch, architect prompts, client-tenancy, add-builder-profile, etc.) — do not invent.

## Bridge file — required sections

### Always (both scopes)
- Identity: dialogName, dialogKind, bridgeScope, workspace root, transcript/agent-store id if known, UTC (--print-utc-now)
- Mission: why the dialog exists (themes + goal), not only last ticket
- Verified state (commands + on-disk results relevant to focus)
- File map Present/Absent · Decisions locked · Forbidden · Next default
- Smoke checklist · Paste-packet

### When $bridgeScope=full — ALSO required

1) **Topic meta map** (core of wide transfer)
   For each focus theme in this dialog (from $topic / $focusProjects / dialog arc):
   - Essence (what it is / why it matters) — from disk docs, not chat memory alone
   - Boundaries / taboos / name≠create locks
   - SSOT paths: REQ, architecture, contracts, interviews/analysis, pipelines (path-based; Unknown ok)
   Prefer reading focus `docs/requirements/`, `docs/architecture/`, `docs/analysis/`, contracts — not only the latest message.

2) **Dialog arc**
   Ordered waves/decisions across the WHOLE dialog (not only the tail). What closed vs deferred.

3) **Method layer (thin)**
   Pointers only: MANIFEST.md, core/workflow.md, core/session-starter.md, specs/profiles.yaml,
   contracts pattern, *_builder.plan.md + fixed-plan rule, CLI --verify, VERSION/CHANGELOG.
   Optional @ migration-self-restore-zeya888-method.md — do not duplicate its body.

4) **Launch / next recipes** — derived from $dialogKind (examples, pick what fits; do not invent new process):
   - project_focus → continue builder_project Phase 0 / P1.3 / P3; @ builder-session + profile contract + bullrun
   - cross_project → architect prompts (parent-requirement-to-project-reqs, cross-project-*, client-product-root-orientation) as applicable
   - method_ops → add-builder-profile / profile-from-checked-out-dir / client-tenancy / console — only as needed
   - mixed → list 2–4 concrete next modes matching actual themes

5) **Conditional appendix — Profile entry paths A–D**
   Include ONLY if dialogKind=method_ops OR dialog practiced profile bootstrap.
   Then link guides/add-builder-profile.md + migration-add-builder-profile.md +
   migration-profile-from-checked-out-dir.md + client-tenancy.md (Path C) + guide §5 split (Path D).
   Do NOT paste a second 13-step checklist — pointer to guide §1.

### When $bridgeScope=operative
- Skip Topic meta map / Method layer / kind-derived multi-recipes / profile appendix.
- Keep one next mode + last-wave verified state.

## Paste-packet modes (full)

Always offer:
- continue focus topic(s) from Topic meta map + arc
- switch dialogKind / new ask
- method commit (only if operator later orders)
- other: <operator fill>

Add profile-bootstrap modes (Path A|B|C|D) ONLY if conditional appendix is present.

## Operator context (fill)

- dialogName=
- dialogKind=project_focus|cross_project|method_ops|mixed
- bridgeScope=full|operative
- topic=
- focusProjects= (optional CSV of builder_project / client paths)
- already Done=
- clean agent should do next=

## Report

Reply: mirror ok | bridge path | dialogName | dialogKind | bridgeScope | topic count in meta map | appendix profile paths yes/no | Unknowns.
STOP unless operator asks follow-up.
```

---

## Примечания

- Hard `@` in paste = analysis.mdc + this prompt + dialog-bridges README + MANIFEST only; rest resolved by kind from disk.
- Outputs live under `$bridgeOutDir` (default `analysis/dialog-bridges/`), not under `prompts/`.
- Topic meta map > last-chat paraphrase: prefer REQ/arch/contracts/analysis paths.
- Profile Path A–D and add-builder-profile `@` are **not** default full-bridge requirements.
- Paste-packet `@` must use the written bridge path.
