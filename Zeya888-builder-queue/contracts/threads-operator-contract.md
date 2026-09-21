# Threads Builder — operator contract

> **Plan (read-only unless operator asks):** [`.cursor/plans/Threads_builder.plan.md`](../../../.cursor/plans/Threads_builder.plan.md)  
> **Propagation:** [builder-session/SKILL.md](../../../.cursor/skills/builder-session/SKILL.md) · [builder-operator-habits.mdc](../../../.cursor/rules/builder-operator-habits.mdc) · [session-starter.md](../core/session-starter.md)

Process-reminder правила для `builder_project: threads` (focus `doge-threads/` ← https://github.com/DOGE-Complaints/doge-threads). P1/PA промпты — только [workflow.md](../core/workflow.md); не дублировать в plan.

**Alias ≠ folder:** `threads` → `doge-threads/`.

---

## 1. `resolve-start-from-index` — старт только из индекса + active pkg

**Перед** batch-run, Build window или P3 Execute:

**Fixed plan:** `@attach` [`.cursor/plans/Threads_builder.plan.md`](../../../.cursor/plans/Threads_builder.plan.md) + workflow §P3/P6 в **этом** чате — **не** Build / Execute plan на файле ([fixed-builder-plan-execution.md](../guides/fixed-builder-plan-execution.md)).

1. Прочитать [`doge-threads/docs/tasks/bullrun-launch-index.md`](../../../doge-threads/docs/tasks/bullrun-launch-index.md) §«Актуальная точка».
2. Прочитать [`threads-active-package.current.yaml`](../../../doge-threads/docs/tasks/threads-active-package.current.yaml) → `package_file`, `activation`.
3. Из корня workspace:  
   `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project threads --verify`  
   При `FAIL` — **стоп**; запустить **P1.3** / **PA+requirement** после авторства stories, не выдумывать очередь.
4. Следующую волну брать **только** из индекса, pkg/`--list`, или явной команды (`run_mode=…` из plan §safe-override).

**Запрещено:**

- Брать порядок из памяти или исполнять raw REQ без materialized story + task `README.md` + pkg.
- Invent `STORY-THREADS-*` / epics без фактов из backlog / REQ.
- Путать nested `.git` в `doge-threads/` с корневым DOGEstonia git.

---

## 2. `treat-missing-epic-as-not-decomposed` — эпик без task queue = не декомпозирован

Если `EPIC-THREADS-*` появится в `doge-threads/docs/tasks/epics/`, но в bullrun **нет** Builder Queue task queue:

- Считать эпик **не декомпозированным**.
- **Не** начинать P3 Execute.
- Запустить **P1.1** + [`bullrun-epic-decompose.md`](../../../.cursor/commands/bullrun-epic-decompose.md) или **P1.3** для backlog story.

**Primary intakes:**

- **P1.3** `backlog_story` — keys `STORY-THREADS-*` (confirm at first emit) from backlog INDEX.
- **`requirement`** — `$requirementDoc` under `doge-threads/docs/requirements/` when authored; parent framing may cite workspace `docs/requirements backlog/REQ7-…` without inventing stories.

---

## 3. `sync-index-after-each-task` — индекс в той же итерации

После **каждого** закрытого task или story gate (и при **emit** новых `STORY-THREADS-*`):

1. Обновить `bullrun-launch-index.md` и [`backlog-stories/INDEX.md`](../../../doge-threads/docs/tasks/backlog-stories/INDEX.md).
2. Обновить §«Актуальная точка».
3. Не откладывать sync на конец сессии.

---

## 4. `pick-input-mode-explicitly` — один режим входа на сессию

| `input_mode` | Якорь P1/P3/P4 | Когда (threads) |
|--------------|----------------|-----------------|
| `backlog_story` | `@$storyFile` (`STORY-THREADS-*`); опц. `@$backlogIndex` | **Primary default:** после авторства story |
| `requirement` | `@$requirementDoc` | Когда REQs существуют под `doge-threads/docs/requirements/` (или explicit parent REQ attach) |
| `epic_story` | `@$epicFile` (`EPIC-THREADS-*`) | Когда эпик materialize |
| `run_mode=…` | gap list из `Threads_builder.plan.md` §safe-override | Post-audit; **не** менять active pkg |

**Один режим на сессию.**

**Bootstrap marker t00:** methodology only — **не** P3 product work на marker.

**PA (до P1):** workflow §PA — shaping; без pkg и без P3.

**Stack:** Python 3.11 + FastAPI + uvicorn + httpx in `doge-threads/`; skill `python-pro` (etalon gateway/identity/aibridge).

**hasUxPipeline:** false — не spa UI-0..UI-3.

---

## 5. Date discipline (artifact dates)

```bash
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project threads --verify --check-dates
```

SSOT: [`guides/builder-artifact-dates.md`](../guides/builder-artifact-dates.md).

---

## Session checklist

```markdown
## Threads session resolve

- verify: ok N paths | FAIL (→ author STORY / REQ shaping + P1 first)
- check-dates: ok / WARN / FAIL
- index: bullrun-launch-index §Актуальная точка
- active pkg: threads-active-package.current.yaml → pkg-…
- input_mode: backlog_story | requirement | epic_story | run_mode=… (один)
- stack: Python 3.11 + FastAPI + uvicorn + httpx; skill python-pro
- focus: doge-threads/ (alias threads)
- next work: <из --list или backlog INDEX, не из памяти>
```

---

## SSOT order (threads)

1. `run_mode` override list (если оператор явно указал)  
2. Active `threads-active-packages/pkg-*.yaml` + `--verify`  
3. `bullrun-launch-index.md` + `backlog-stories/INDEX.md`  
4. **Backlog:** `backlog-stories/` · **Requirements:** `docs/requirements/` (intake, не очередь)  
5. Task `README.md` + acceptance-verification

Pipeline: [`threads-story-execution-pipeline.md`](../../../doge-threads/docs/tasks/threads-story-execution-pipeline.md).

---

## 6. Аудит P4 / P7 (якоря по `input_mode`)

Отчёты: `doge-threads/docs/analysis/` (создать при необходимости). Мышление: `@.cursor/rules/analysis.mdc`. Промпты — [workflow.md](../core/workflow.md) §P4 / §P7.

| Режим | Cursor P4 | External re-audit |
|-------|-----------|-------------------|
| `backlog_story` | Факт-код vs AC в `@$storyFile` | workflow §P4 |
| `requirement` | Факт vs `$requirementDoc` + AC | workflow §P4 |
| `epic_story` | Факт vs AC Stories в `$epicFile` | workflow §P4 |
| `run_mode=…` | Findings + AC тасков override | workflow §P7 |

Build plan **не** содержит таблицу P4 — только эта секция и workflow.

---

## 7. P1.3 `backlog_story` / requirement (threads appendix)

Используется с [workflow.md](../core/workflow.md) §P1.3 / §P1.2 (`$p13Appendix` для `builder_project: threads`).

| Параметр | Значение |
|----------|----------|
| Epic prefix (target) | `EPIC-THREADS-*` (when materialize) |
| Story prefix | `STORY-THREADS-*` |
| Materialize path | `doge-threads/docs/tasks/epics/` (after P1) |
| Execution skill | `python-pro` |
| Stack | Python 3.11 + FastAPI + uvicorn + httpx |
| Requirements SSOT | `doge-threads/docs/requirements/` (when authored) |

**hasUxPipeline:** false — не spa UI-0..UI-3.
