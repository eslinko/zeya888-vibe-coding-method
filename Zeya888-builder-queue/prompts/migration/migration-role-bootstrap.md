# Migration bootstrap — role x profile (universal)

**Категория:** migration (session restore after chat reset)  
**Profiles SSOT:** [`../../specs/profiles.yaml`](../../specs/profiles.yaml)  
**Phase SSOT:** [`../../core/workflow.md`](../../core/workflow.md)  
**Claims rule:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | Чаты удалены, нужно быстро восстановить рабочий контекст | Запустить этот prompt с `builder_project` + `focus_role` |
| 2 | Нужен старт строго под роль (BLD/VAL/OP), не смешивая фазы | `focus_role` выбирает role-lock и набор артефактов |
| 3 | Нужен перенос на новый workspace с тем же методом | prompt читает SSOT с диска и выдаёт ready bootstrap |

**Поддерживаемые профили (`builder_project`):** `gateway`, `gpt`, `spa`, `taxonomy`, `identity`, `scripts`, `capybara`, `landing`, `zeya888` (из `profiles.yaml`).

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
@docs/methodology/Zeya888-builder-queue/core/workflow.md
@docs/methodology/Zeya888-builder-queue/core/session-starter.md

builder_project: <gateway|gpt|spa|taxonomy|identity|scripts|aibridge|capybara|landing|zeya888>
focus_role: <builder|validator|orchestrator>
workspace_root: /Users/eslinko/Development/DOGEstonia

Migration bootstrap. Restore role-specific context from SSOT files on disk.

MODE: restore only. No product edits, no commits, no push.
Claims: Read/Glob only; else Unknown.
Use profiles.yaml as single source for paths/plan/stack/skill.

## Step 1 — Resolve profile
From profiles.yaml for builder_project:
- enabled/queueless
- focus_folder, tasks_dir, plan_file, pipeline_doc
- test_command, stack_label, execution skill
- verify command:
  python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project <builder_project> --verify

If unknown/disabled profile: STOP + ask.

## Step 2 — Role lock
Apply exactly one role:

### builder
- Goal: restore BLD context for P0/P1/P2/P3/P5/P6/P8.
- Read: bullrun index + active pointer + pipeline doc + plan_file.
- Run verify command; if FAIL -> report fail path and stop.
- Output:
  1) BLD startup summary (paths + next phase candidates),
  2) strict bans (no OP routing, no VAL decisions),
  3) ready-to-run phase fence selector (P1/P2/P3/P6/P8).

### validator
- Goal: restore VAL context for P4/P7 only.
- Read: operator contract for profile + latest audit/reaudit paths from tasks/docs/analysis.
- No code changes, no pkg edits, no commit actions.
- Output:
  1) VAL startup summary,
  2) audit scope anchors (AC sources),
  3) report contract (facts + paths + disposition consistency checks).

### orchestrator
- Goal: restore OP context (START/WAVE/RUN routing).
- Read: operator guides + session artifacts under
  {tasks_dir}/run-reports/operator-sessions/ and operator-waves/.
- If no session file: propose START bootstrap.
- Output:
  1) OP startup summary (session bind state),
  2) next action (START vs WAVE vs SUBAGENT RUN),
  3) packet routing table (BLD/VAL/CLI) without executing packets.

## Step 3 — Deliver only restore packet
Return exactly:
1) role: <focus_role>
2) profile: <builder_project>
3) resolved paths (tasksRoot, planFile, pipelineDoc, pointer, bullrun)
4) verify result status (or reason skipped for taxonomy/role constraints)
5) first safe next command/message for this role
6) hard bans for this role
```

---

## Примечания

- `taxonomy` профайл queueless: нет pkg queue; restore-пакет должен это явно фиксировать.
- Этот prompt универсальный: роль выбирается инпутом, а не хардкодом файла.
