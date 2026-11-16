# Alvasar GPT Builder — operator contract

> **Plan (read-only unless operator asks):** [`.cursor/plans/Alvasar-GPT_builder.plan.md`](../../../.cursor/plans/Alvasar-GPT_builder.plan.md)  
> **Propagation:** [builder-session/SKILL.md](../../../.cursor/skills/builder-session/SKILL.md) · [builder-operator-habits.mdc](../../../.cursor/rules/builder-operator-habits.mdc) · [session-starter.md](../core/session-starter.md)

Process-reminder правила для `builder_project: alvasar-gpt` (focus `clients/Alvasar/gpt/` ← https://github.com/eslinko/alvasar.git). P1/PA промпты — только [workflow.md](../core/workflow.md); не дублировать в plan.

---

## 1. `resolve-start-from-index` — старт только из индекса + active pkg

**Перед** batch-run, Build window или P3 Execute:

**Fixed plan:** `@attach` [`.cursor/plans/Alvasar-GPT_builder.plan.md`](../../../.cursor/plans/Alvasar-GPT_builder.plan.md) + workflow §P3/P6 в **этом** чате — **не** Build / Execute plan на файле ([fixed-builder-plan-execution.md](../guides/fixed-builder-plan-execution.md)).

1. Прочитать [`clients/Alvasar/gpt/docs/tasks/bullrun-launch-index.md`](../../../clients/Alvasar/gpt/docs/tasks/bullrun-launch-index.md) §«Актуальная точка».
2. Прочитать [`alvasar-gpt-active-package.current.yaml`](../../../clients/Alvasar/gpt/docs/tasks/alvasar-gpt-active-package.current.yaml) → `package_file`, `activation`.
3. Из корня workspace:  
   `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project alvasar-gpt --verify`  
   При `FAIL` — **стоп**; запустить **P1.3** / **PA+requirement** после авторства stories, не выдумывать очередь.
4. Следующую волну брать **только** из индекса, pkg/`--list`, или явной команды (`run_mode=…` из plan §safe-override).

**Запрещено:**

- Брать порядок из памяти или исполнять raw REQ без materialized story + task `README.md` + pkg.
- Invent `STORY-ALVG-*` / epics без фактов из backlog / REQ.
- Путать nested `.git` в `clients/Alvasar/` с корневым DOGEstonia git.
- Создавать `instructions.manifest.json` / instruction body `*.md` «чтобы путь существовал» ([analysis.mdc](../../../.cursor/rules/analysis.mdc) name ≠ create).

---

## 2. `treat-missing-epic-as-not-decomposed` — эпик без task queue = не декомпозирован

Если `EPIC-ALVG-*` появится в `clients/Alvasar/gpt/docs/tasks/epics/`, но в bullrun **нет** Builder Queue task queue:

- Считать эпик **не декомпозированным**.
- **Не** начинать P3 Execute.
- Запустить **P1.1** + [`bullrun-epic-decompose.md`](../../../.cursor/commands/bullrun-epic-decompose.md) или **P1.3** для backlog story.

**Primary intakes:**

- **P1.3** `backlog_story` — keys `STORY-ALVG-*` (confirm at first emit) from backlog INDEX.
- **`requirement`** — `$requirementDoc` under `clients/Alvasar/gpt/docs/requirements/` or parent `clients/Alvasar/docs/requirements/` when authored.

---

## 3. `sync-index-after-each-task` — индекс в той же итерации

После **каждого** закрытого task или story gate (и при **emit** новых `STORY-ALVG-*`):

1. Обновить `bullrun-launch-index.md` и [`backlog-stories/INDEX.md`](../../../clients/Alvasar/gpt/docs/tasks/backlog-stories/INDEX.md).
2. Обновить §«Актуальная точка».
3. Не откладывать sync на конец сессии.

---

## 4. `pick-input-mode-explicitly` — один режим входа на сессию

| `input_mode` | Якорь P1/P3/P4 | Когда (alvasar-gpt) |
|--------------|----------------|---------------------|
| `backlog_story` | `@$storyFile` (`STORY-ALVG-*`); опц. `@$backlogIndex` | **Primary default:** после авторства story |
| `requirement` | `@$requirementDoc` | Когда REQs существуют (focus или parent Alvasar docs) |
| `epic_story` | `@$epicFile` (`EPIC-ALVG-*`) | Когда эпик materialize |
| `run_mode=…` | gap list из `Alvasar-GPT_builder.plan.md` §safe-override | Post-audit; **не** менять active pkg |

**Один режим на сессию.**

**Bootstrap marker t00:** methodology only — **не** P3 product work на marker.

**PA (до P1):** workflow §PA — shaping; без pkg и без P3.

**Stack:** GPT Instructions in `clients/Alvasar/gpt/`; skill `openai-custom-gpt-builder` (same as flat `gpt` / GPT UI). Focus README is authorship SSOT; refine `test_command` when tooling lands. Parent: REQ14 §4.5.

**hasUxPipeline:** false — не spa UI-0..UI-3.

---

## 5. Date discipline (artifact dates)

```bash
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project alvasar-gpt --verify --check-dates
```

SSOT: [`guides/builder-artifact-dates.md`](../guides/builder-artifact-dates.md).

---

## Session checklist

```markdown
## Alvasar-gpt session resolve

- verify: ok N paths | FAIL (→ author STORY / REQ shaping + P1 first)
- check-dates: ok / WARN / FAIL
- index: bullrun-launch-index §Актуальная точка
- active pkg: alvasar-gpt-active-package.current.yaml → pkg-…
- input_mode: backlog_story | requirement | epic_story | run_mode=… (один)
- stack: GPT Instructions; skill openai-custom-gpt-builder
- next work: <из --list или backlog INDEX, не из памяти>
```

---

## SSOT order (alvasar-gpt)

1. `run_mode` override list (если оператор явно указал)  
2. Active `alvasar-gpt-active-packages/pkg-*.yaml` + `--verify`  
3. `bullrun-launch-index.md` + `backlog-stories/INDEX.md`  
4. **Backlog:** `backlog-stories/` · **Requirements:** parent/focus `docs/requirements/` (intake, не очередь)  
5. Task `README.md` + acceptance-verification

Pipeline: [`alvasar-gpt-story-execution-pipeline.md`](../../../clients/Alvasar/gpt/docs/tasks/alvasar-gpt-story-execution-pipeline.md).

---

## 6. Аудит P4 / P7 (якоря по `input_mode`)

Отчёты: `clients/Alvasar/gpt/docs/analysis/` (создать при необходимости). Мышление: `@.cursor/rules/analysis.mdc`. Промпты — [workflow.md](../core/workflow.md) §P4 / §P7.

| Режим | Cursor P4 | External re-audit |
|-------|-----------|-------------------|
| `backlog_story` | Факт-код vs AC в `@$storyFile` | workflow §P4 |
| `requirement` | Факт vs `$requirementDoc` + AC | workflow §P4 |
| `epic_story` | Факт vs AC Stories в `$epicFile` | workflow §P4 |
| `run_mode=…` | Findings + AC тасков override | workflow §P7 |

Build plan **не** содержит таблицу P4 — только эта секция и workflow.

---

## 7. P1.3 `backlog_story` / requirement (alvasar-gpt naming)

Используется с [workflow.md](../core/workflow.md) §P1.3 / §P1.2 (`$p13Appendix` для `builder_project: alvasar-gpt`).

| Параметр | Значение |
|----------|----------|
| Epic prefix (target) | `EPIC-ALVG-*` (when materialize) |
| Story prefix | `STORY-ALVG-*` |
| Materialize path | `clients/Alvasar/gpt/docs/tasks/epics/` (after P1) |
| Execution skill | `openai-custom-gpt-builder` |
| Requirements SSOT | parent `clients/Alvasar/docs/requirements/` · focus REQs when authored |

**hasUxPipeline:** false — не spa UI-0..UI-3 (bootstrap волна).
