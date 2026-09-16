# Arweave Builder — operator contract

> **Plan (read-only unless operator asks):** [`.cursor/plans/Arweave_builder.plan.md`](../../../.cursor/plans/Arweave_builder.plan.md)  
> **Propagation:** [builder-session/SKILL.md](../../../.cursor/skills/builder-session/SKILL.md) · [builder-operator-habits.mdc](../../../.cursor/rules/builder-operator-habits.mdc) · [session-starter.md](../core/session-starter.md)

Process-reminder правила для `builder_project: arweave` (Node.js Arweave uploader sidecar в `dogestonia-arweave-uploader/`). P1/PA промпты — только [workflow.md](../core/workflow.md); не дублировать в plan.

---

## 1. `resolve-start-from-index` — старт только из индекса + active pkg

**Перед** batch-run, Build window или P3 Execute:

**Fixed plan:** `@attach` [`.cursor/plans/Arweave_builder.plan.md`](../../../.cursor/plans/Arweave_builder.plan.md) + workflow §P3/P6 в **этом** чате — **не** Build / Execute plan на файле ([fixed-builder-plan-execution.md](../guides/fixed-builder-plan-execution.md)).

1. Прочитать [`dogestonia-arweave-uploader/docs/tasks/bullrun-launch-index.md`](../../../dogestonia-arweave-uploader/docs/tasks/bullrun-launch-index.md) §«Актуальная точка».
2. Прочитать [`arweave-active-package.current.yaml`](../../../dogestonia-arweave-uploader/docs/tasks/arweave-active-package.current.yaml) → `package_file`, `activation`.
3. Из корня workspace:  
   `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project arweave --verify`  
   При `FAIL` — **стоп**; запустить **P1.3** / **PA+requirement** после авторства stories, не выдумывать очередь.
4. Следующую волну брать **только** из индекса, pkg/`--list`, или явной команды (`run_mode=…` из plan §safe-override).

**Запрещено:**

- Брать порядок из памяти или исполнять raw REQ без materialized story + task `README.md` + pkg.
- Invent `STORY-AU-*` / epics без фактов из REQ-AU / CONTEXT.
- Смешивать arweave work с другими `builder_project` без явной команды.
- Путать nested `.git` в `dogestonia-arweave-uploader/` с корневым DOGEstonia git (как у `spa-app`).

---

## 2. `treat-missing-epic-as-not-decomposed` — эпик без task queue = не декомпозирован

Если `EPIC-AU-*` появится в `dogestonia-arweave-uploader/docs/tasks/epics/`, но в bullrun **нет** Builder Queue task queue:

- Считать эпик **не декомпозированным**.
- **Не** начинать P3 Execute.
- Запустить **P1.1** + [`bullrun-epic-decompose.md`](../../../.cursor/commands/bullrun-epic-decompose.md) или **P1.3** для backlog story.

**Primary intakes:**

- **P1.3** `backlog_story` — keys `STORY-AU-*` (confirm at first emit) from backlog INDEX.
- **`requirement`** — `$requirementDoc` = `REQ-AU-01`…`04` / CONTEXT under [`docs/requirements/`](../../../dogestonia-arweave-uploader/docs/requirements/INDEX.md).

---

## 3. `sync-index-after-each-task` — индекс в той же итерации

После **каждого** закрытого task или story gate (и при **emit** новых `STORY-AU-*`):

1. Обновить `bullrun-launch-index.md` и [`backlog-stories/INDEX.md`](../../../dogestonia-arweave-uploader/docs/tasks/backlog-stories/INDEX.md).
2. Обновить §«Актуальная точка».
3. Не откладывать sync на конец сессии.

---

## 4. `pick-input-mode-explicitly` — один режим входа на сессию

| `input_mode` | Якорь P1/P3/P4 | Когда (arweave) |
|--------------|----------------|-----------------|
| `backlog_story` | `@$storyFile` (`STORY-AU-*`); опц. `@$backlogIndex` | **Primary default:** после авторства story |
| `requirement` | `@$requirementDoc` (`REQ-AU-*` / CONTEXT) | Инкремент по numbered REQ |
| `epic_story` | `@$epicFile` (`EPIC-AU-*`) | Когда эпик materialize |
| `run_mode=…` | gap list из `Arweave_builder.plan.md` §safe-override | Post-audit; **не** менять active pkg |

**Один режим на сессию** — не смешивать `backlog_story` и `requirement` в одном pkg без явной команды оператора.

**Bootstrap marker t00:** methodology only — **не** P3 product work на marker.

**PA (до P1):** workflow §PA — shaping; без pkg и без P3.

**Domain note:** cryptography / ANS-104 / wallet signing — follow REQ-AU + `javascript-pro`; no dedicated crypto skill in workspace.

---

## 5. Date discipline (artifact dates)

```bash
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project arweave --verify --check-dates
```

SSOT: [`guides/builder-artifact-dates.md`](../guides/builder-artifact-dates.md).

---

## Session checklist

```markdown
## Arweave session resolve

- verify: ok N paths | FAIL (→ author STORY / REQ shaping + P1 first)
- check-dates: ok / WARN / FAIL
- index: bullrun-launch-index §Актуальная точка
- active pkg: arweave-active-package.current.yaml → pkg-…
- input_mode: backlog_story | requirement | epic_story | run_mode=… (один)
- stack: Node.js (Arweave / cryptography); skill javascript-pro
- next work: <из --list или backlog INDEX / REQ map, не из памяти>
```

---

## SSOT order (arweave)

1. `run_mode` override list (если оператор явно указал)  
2. Active `arweave-active-packages/pkg-*.yaml` + `--verify`  
3. `bullrun-launch-index.md` + `backlog-stories/INDEX.md`  
4. **Backlog:** `backlog-stories/` · **Requirements:** `docs/requirements/REQ-AU-*` (intake, не очередь)  
5. Task `README.md` + acceptance-verification

Pipeline: [`arweave-story-execution-pipeline.md`](../../../dogestonia-arweave-uploader/docs/tasks/arweave-story-execution-pipeline.md).

---

## 6. Аудит P4 / P7 (якоря по `input_mode`)

Отчёты: `dogestonia-arweave-uploader/docs/analysis/` (создать при необходимости). Мышление: `@.cursor/rules/analysis.mdc`. Промпты — [workflow.md](../core/workflow.md) §P4 / §P7.

| Режим | Cursor P4 | External re-audit |
|-------|-----------|-------------------|
| `backlog_story` | Факт-код vs AC в `@$storyFile` | workflow §P4 |
| `requirement` | Факт vs `$requirementDoc` + AC | workflow §P4 |
| `epic_story` | Факт vs AC Stories в `$epicFile` | workflow §P4 |
| `run_mode=…` | Findings + AC тасков override | workflow §P7 |

Build plan **не** содержит таблицу P4 — только эта секция и workflow.

---

## 7. P1.3 `backlog_story` / requirement (arweave appendix)

Используется с [workflow.md](../core/workflow.md) §P1.3 / §P1.2 (`$p13Appendix` для `builder_project: arweave`).

| Параметр | Значение |
|----------|----------|
| Epic prefix (target) | `EPIC-AU-*` (when materialize) |
| Story prefix | `STORY-AU-*` |
| Materialize path | `dogestonia-arweave-uploader/docs/tasks/epics/` (after P1) |
| Execution skill | `javascript-pro` (`execution_skill_primary`) |
| Requirements SSOT | [`docs/requirements/INDEX.md`](../../../dogestonia-arweave-uploader/docs/requirements/INDEX.md) |
| REQ map | REQ-AU-01…04 + CONTEXT-heritage |

**hasUxPipeline:** false — не spa UI-0..UI-3.
