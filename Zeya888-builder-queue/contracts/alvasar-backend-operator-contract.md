# Alvasar Backend Builder — operator contract

> **Plan (read-only unless operator asks):** [`.cursor/plans/Alvasar-Backend_builder.plan.md`](../../../.cursor/plans/Alvasar-Backend_builder.plan.md)  
> **Propagation:** [builder-session/SKILL.md](../../../.cursor/skills/builder-session/SKILL.md) · [builder-operator-habits.mdc](../../../.cursor/rules/builder-operator-habits.mdc) · [session-starter.md](../core/session-starter.md)

Process-reminder правила для `builder_project: alvasar-backend` (focus `clients/Alvasar/backend/` ← https://github.com/eslinko/alvasar.git). P1/PA промпты — только [workflow.md](../core/workflow.md); не дублировать в plan.

---

## 1. `resolve-start-from-index` — старт только из индекса + active pkg

**Перед** batch-run, Build window или P3 Execute:

**Fixed plan:** `@attach` [`.cursor/plans/Alvasar-Backend_builder.plan.md`](../../../.cursor/plans/Alvasar-Backend_builder.plan.md) + workflow §P3/P6 в **этом** чате — **не** Build / Execute plan на файле ([fixed-builder-plan-execution.md](../guides/fixed-builder-plan-execution.md)).

1. Прочитать [`clients/Alvasar/backend/docs/tasks/bullrun-launch-index.md`](../../../clients/Alvasar/backend/docs/tasks/bullrun-launch-index.md) §«Актуальная точка».
2. Прочитать [`alvasar-backend-active-package.current.yaml`](../../../clients/Alvasar/backend/docs/tasks/alvasar-backend-active-package.current.yaml) → `package_file`, `activation`.
3. Из корня workspace:  
   `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project alvasar-backend --verify`  
   При `FAIL` — **стоп**; запустить **P1.3** / **PA+requirement** после авторства stories, не выдумывать очередь.
4. Следующую волну брать **только** из индекса, pkg/`--list`, или явной команды (`run_mode=…` из plan §safe-override).

**Запрещено:**

- Брать порядок из памяти или исполнять raw REQ без materialized story + task `README.md` + pkg.
- Invent `STORY-ALVB-*` / epics без фактов из backlog / REQ.
- Путать nested `.git` в `clients/Alvasar/` с корневым DOGEstonia git.

---

## 2. `treat-missing-epic-as-not-decomposed` — эпик без task queue = не декомпозирован

Если `EPIC-ALVB-*` появится в `clients/Alvasar/backend/docs/tasks/epics/`, но в bullrun **нет** Builder Queue task queue:

- Считать эпик **не декомпозированным**.
- **Не** начинать P3 Execute.
- Запустить **P1.1** + [`bullrun-epic-decompose.md`](../../../.cursor/commands/bullrun-epic-decompose.md) или **P1.3** для backlog story.

**Primary intakes:**

- **P1.3** `backlog_story` — keys `STORY-ALVB-*` (confirm at first emit) from backlog INDEX.
- **`requirement`** — `$requirementDoc` under `clients/Alvasar/backend/docs/requirements/` when authored.

---

## 3. `sync-index-after-each-task` — индекс в той же итерации

После **каждого** закрытого task или story gate (и при **emit** новых `STORY-ALVB-*`):

1. Обновить `bullrun-launch-index.md` и [`backlog-stories/INDEX.md`](../../../clients/Alvasar/backend/docs/tasks/backlog-stories/INDEX.md).
2. Обновить §«Актуальная точка».
3. Не откладывать sync на конец сессии.

---

## 4. `pick-input-mode-explicitly` — один режим входа на сессию

| `input_mode` | Якорь P1/P3/P4 | Когда (alvasar-backend) |
|--------------|----------------|----------------|
| `backlog_story` | `@$storyFile` (`STORY-ALVB-*`); опц. `@$backlogIndex` | **Primary default:** после авторства story |
| `requirement` | `@$requirementDoc` | Когда REQs существуют под `clients/Alvasar/backend/docs/requirements/` |
| `epic_story` | `@$epicFile` (`EPIC-ALVB-*`) | Когда эпик materialize |
| `run_mode=…` | gap list из `Alvasar-Backend_builder.plan.md` §safe-override | Post-audit; **не** менять active pkg |

**Один режим на сессию.**

**Bootstrap marker t00:** methodology only — **не** P3 product work на marker.

**PA (до P1):** workflow §PA — shaping; без pkg и без P3.

**Stack:** Python API in `clients/Alvasar/backend/`; skill `python-pro`. App scaffold deferred — refine `test_command` when tooling lands. Parent REQ: `clients/Alvasar/docs/requirements/REQ0-…`.

**hasUxPipeline:** false — не spa UI-0..UI-3.

---

## 5. Date discipline (artifact dates)

```bash
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project alvasar-backend --verify --check-dates
```

SSOT: [`guides/builder-artifact-dates.md`](../guides/builder-artifact-dates.md).

---

## Session checklist

```markdown
## Alvasar-backend session resolve

- verify: ok N paths | FAIL (→ author STORY / REQ shaping + P1 first)
- check-dates: ok / WARN / FAIL
- index: bullrun-launch-index §Актуальная точка
- active pkg: alvasar-backend-active-package.current.yaml → pkg-…
- input_mode: backlog_story | requirement | epic_story | run_mode=… (один)
- stack: Python API; skill python-pro
- next work: <из --list или backlog INDEX, не из памяти>
```

---

## SSOT order (alvasar-backend)

1. `run_mode` override list (если оператор явно указал)  
2. Active `alvasar-backend-active-packages/pkg-*.yaml` + `--verify`  
3. `bullrun-launch-index.md` + `backlog-stories/INDEX.md`  
4. **Backlog:** `backlog-stories/` · **Requirements:** `docs/requirements/` (intake, не очередь)  
5. Task `README.md` + acceptance-verification

Pipeline: [`alvasar-backend-story-execution-pipeline.md`](../../../clients/Alvasar/backend/docs/tasks/alvasar-backend-story-execution-pipeline.md).

---

## 6. Аудит P4 / P7 (якоря по `input_mode`)

Отчёты: `clients/Alvasar/backend/docs/analysis/` (создать при необходимости). Мышление: `@.cursor/rules/analysis.mdc`. Промпты — [workflow.md](../core/workflow.md) §P4 / §P7.

| Режим | Cursor P4 | External re-audit |
|-------|-----------|-------------------|
| `backlog_story` | Факт-код vs AC в `@$storyFile` | workflow §P4 |
| `requirement` | Факт vs `$requirementDoc` + AC | workflow §P4 |
| `epic_story` | Факт vs AC Stories в `$epicFile` | workflow §P4 |
| `run_mode=…` | Findings + AC тасков override | workflow §P7 |

Build plan **не** содержит таблицу P4 — только эта секция и workflow.

---

## 7. P1.3 `backlog_story` / requirement (alvasar-backend appendix)

Используется с [workflow.md](../core/workflow.md) §P1.3 / §P1.2 (`$p13Appendix` для `builder_project: alvasar-backend`).

| Параметр | Значение |
|----------|----------|
| Epic prefix (target) | `EPIC-ALVB-*` (when materialize) |
| Story prefix | `STORY-ALVB-*` |
| Materialize path | `clients/Alvasar/backend/docs/tasks/epics/` (after P1) |
| Execution skill | `python-pro` |
| Requirements SSOT | `clients/Alvasar/backend/docs/requirements/` (when authored) |

**hasUxPipeline:** false — не spa UI-0..UI-3.
