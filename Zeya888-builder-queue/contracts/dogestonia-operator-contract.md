# DOGEstonia Builder — operator contract

> **Plan (read-only unless operator asks):** [`.cursor/plans/DOGEstonia_builder.plan.md`](../../../.cursor/plans/DOGEstonia_builder.plan.md)  
> **Propagation:** [builder-session/SKILL.md](../../../.cursor/skills/builder-session/SKILL.md) · [builder-operator-habits.mdc](../../../.cursor/rules/builder-operator-habits.mdc) · [session-starter.md](../core/session-starter.md)

Process-reminder правила для `builder_project: dogestonia` (React Native / Expo app в `dogestonia-app/`). P1/PA промпты — только [workflow.md](../core/workflow.md); не дублировать в plan.

---

## 1. `resolve-start-from-index` — старт только из индекса + active pkg

**Перед** batch-run, Build window или P3 Execute:

**Fixed plan:** `@attach` [`.cursor/plans/DOGEstonia_builder.plan.md`](../../../.cursor/plans/DOGEstonia_builder.plan.md) + workflow §P3/P6 в **этом** чате — **не** Build / Execute plan на файле ([fixed-builder-plan-execution.md](../guides/fixed-builder-plan-execution.md)).

1. Прочитать [`dogestonia-app/docs/tasks/bullrun-launch-index.md`](../../../dogestonia-app/docs/tasks/bullrun-launch-index.md) §«Актуальная точка».
2. Прочитать [`dogestonia-active-package.current.yaml`](../../../dogestonia-app/docs/tasks/dogestonia-active-package.current.yaml) → `package_file`, `activation`.
3. Из корня workspace:  
   `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project dogestonia --verify`  
   При `FAIL` — **стоп**; запустить **P1** после авторства epic/story, не выдумывать очередь.
4. Следующую волну брать **только** из индекса, pkg/`--list`, или явной команды (`run_mode=…` из plan §safe-override).

**Запрещено:**

- Брать порядок из памяти или исполнять raw REQ без materialized story + task `README.md` + pkg.
- Invent `STORY-DOGE-*` / `EPIC-DOGE-*` без фактов из REQ-APP / CONTEXT.
- Смешивать dogestonia work с другими `builder_project` без явной команды.
- Путать nested `.git` в `dogestonia-app/` с корневым DOGEstonia git (как у `spa-app` / arweave).

---

## 2. `treat-missing-epic-as-not-decomposed` — эпик без task queue = не декомпозирован

Если `EPIC-DOGE-*` появится в `dogestonia-app/docs/tasks/epics/`, но в bullrun **нет** Builder Queue task queue:

- Считать эпик **не декомпозированным**.
- **Не** начинать P3 Execute.
- Запустить **P1.1** + [`bullrun-epic-decompose.md`](../../../.cursor/commands/bullrun-epic-decompose.md) или **P1.3** для backlog story.

**Primary intakes:**

- **P1.1** `epic_story` — keys `EPIC-DOGE-*` (confirm at first emit); default pkg kind `epic_story_tree`.
- **P1.3** `backlog_story` — keys `STORY-DOGE-*`.
- **`requirement`** — `$requirementDoc` = **REQ00** / **REQ01** / **REQ02** under [`docs/requirements/`](../../../dogestonia-app/docs/requirements/INDEX.md) (order: foundation → auth/interest → journeys); deferred operator = [`deferred-operator/`](../../../dogestonia-app/docs/requirements/deferred-operator/README.md) REQ-APP-* only when Product opens that wave.

---

## 3. `sync-index-after-each-task` — индекс в той же итерации

После **каждого** закрытого task или story gate (и при **emit** новых stories):

1. Обновить `bullrun-launch-index.md` и [`backlog-stories/INDEX.md`](../../../dogestonia-app/docs/tasks/backlog-stories/INDEX.md).
2. Обновить §«Актуальная точка».
3. Не откладывать sync на конец сессии.

---

## 4. `pick-input-mode-explicitly` — один режим входа на сессию

| `input_mode` | Якорь P1/P3/P4 | Когда (dogestonia) |
|--------------|----------------|--------------------|
| `epic_story` | `@$epicFile` (`EPIC-DOGE-*`) | **Default tree** (как gateway) |
| `backlog_story` | `@$storyFile` (`STORY-DOGE-*`); опц. `@$backlogIndex` | Doc-gap / backlog emit → P1.3 |
| `requirement` | `@$requirementDoc` (**REQ00→01→02**; or deferred REQ-APP-* / CONTEXT) | Default research order: foundation → auth → journeys |
| `run_mode=…` | gap list из `DOGEstonia_builder.plan.md` §safe-override | Post-audit; **не** менять active pkg |

**Один режим на сессию** — не смешивать без явной команды оператора.

**Bootstrap marker t00:** methodology only — **не** P3 product work на marker.

**PA (до P1):** workflow §PA — shaping; без pkg и без P3.

**UI / visual:** `hasUxPipeline: true` — те же процессы, что spa: [`spa-ui-visual-pipeline.md`](../guides/spa-ui-visual-pipeline.md) UI-0..UI-3; mockup gates в P1.3 UX appendix (workflow).

---

## 5. Date discipline (artifact dates)

```bash
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project dogestonia --verify --check-dates
```

SSOT: [`guides/builder-artifact-dates.md`](../guides/builder-artifact-dates.md).

---

## Session checklist

```markdown
## DOGEstonia session resolve

- verify: ok N paths | FAIL (→ author epic/story / REQ shaping + P1 first)
- check-dates: ok / WARN / FAIL
- index: bullrun-launch-index §Актуальная точка
- active pkg: dogestonia-active-package.current.yaml → pkg-…
- input_mode: epic_story | backlog_story | requirement | run_mode=… (один)
- stack: React Native (Expo) iOS/Android/web; skill react-native-expert (fallback react-expert)
- UX: hasUxPipeline true — spa-ui-visual-pipeline when ui_scope ≠ none
- next work: <из --list или backlog INDEX / REQ map, не из памяти>
```

---

## SSOT order (dogestonia)

1. `run_mode` override list (если оператор явно указал)  
2. Active `dogestonia-active-packages/pkg-*.yaml` + `--verify`  
3. `bullrun-launch-index.md` + `backlog-stories/INDEX.md`  
4. **Epic:** `docs/tasks/epics/` · **Backlog:** `backlog-stories/` · **Requirements:** `docs/requirements/REQ00-*.md` / `REQ01-*.md` / `REQ02-*.md` (active) · `docs/requirements/deferred-operator/` (operator later)  
5. Task `README.md` + acceptance-verification

Pipeline: [`dogestonia-story-execution-pipeline.md`](../../../dogestonia-app/docs/tasks/dogestonia-story-execution-pipeline.md).

---

## 6. Аудит P4 / P7 (якоря по `input_mode`)

Отчёты: `dogestonia-app/docs/analysis/` (создать при необходимости). Мышление: `@.cursor/rules/analysis.mdc`. Промпты — [workflow.md](../core/workflow.md) §P4 / §P7.

| Режим | Cursor P4 | External re-audit |
|-------|-----------|-------------------|
| `epic_story` | Факт vs AC Stories в `$epicFile` | workflow §P4 |
| `backlog_story` | Факт-код vs AC в `@$storyFile` | workflow §P4 |
| `requirement` | Факт vs `$requirementDoc` + AC | workflow §P4 |
| `run_mode=…` | Findings + AC тасков override | workflow §P7 |

**Visual/mixed** (после P3 с screenshots): как spa — Phase A code + Phase B screenshots vs артборд (workflow §P4 spa UX).

Build plan **не** содержит таблицу P4 — только эта секция и workflow.

---

## 7. P1.3 / P1.1 appendix (dogestonia)

Используется с [workflow.md](../core/workflow.md) §P1.1 / §P1.3 (`$p13Appendix` для `builder_project: dogestonia`).

| Параметр | Значение |
|----------|----------|
| Epic prefix (target) | `EPIC-DOGE-*` |
| Story prefix | `STORY-DOGE-*` |
| Materialize path | `dogestonia-app/docs/tasks/epics/` |
| Task naming | `task-doge-*` |
| Execution skill | `react-native-expert`; fallback `react-expert` |
| Requirements SSOT | [`docs/requirements/INDEX.md`](../../../dogestonia-app/docs/requirements/INDEX.md) |
| REQ map | **REQ00→01→02** active; REQ-APP-01…04 in [`deferred-operator/`](../../../dogestonia-app/docs/requirements/deferred-operator/README.md) + CONTEXT |
| UI Visual | [`spa-ui-visual-pipeline.md`](../guides/spa-ui-visual-pipeline.md) |

**hasUxPipeline:** true — console UX branches как spa.
