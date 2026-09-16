# AI Bridge Builder — operator contract

> **Plan (read-only unless operator asks):** [`.cursor/plans/aibridge_builder.plan.md`](../../../.cursor/plans/aibridge_builder.plan.md)  
> **Propagation:** [builder-session/SKILL.md](../../../.cursor/skills/builder-session/SKILL.md) · [builder-operator-habits.mdc](../../../.cursor/rules/builder-operator-habits.mdc) · [session-starter.md](../core/session-starter.md)

Process-reminder правила для `builder_project: aibridge` (Python runtime в `doge-ai-bridge/` — Responses → Story Intake bridge). P1/PA промпты — только [workflow.md](../core/workflow.md); не дублировать в plan.

---

## 1. `resolve-start-from-index` — старт только из индекса + active pkg

**Перед** batch-run, Build window или P3 Execute:

**Fixed plan:** `@attach` [`.cursor/plans/aibridge_builder.plan.md`](../../../.cursor/plans/aibridge_builder.plan.md) + workflow §P3/P6 в **этом** чате — **не** Build / Execute plan на файле ([fixed-builder-plan-execution.md](../guides/fixed-builder-plan-execution.md)).

1. Прочитать [`doge-ai-bridge/docs/tasks/bullrun-launch-index.md`](../../../doge-ai-bridge/docs/tasks/bullrun-launch-index.md) §«Актуальная точка».
2. Прочитать [`aibridge-active-package.current.yaml`](../../../doge-ai-bridge/docs/tasks/aibridge-active-package.current.yaml) → `package_file`, `activation`.
3. Из корня workspace:  
   `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project aibridge --verify`  
   При `FAIL` — **стоп**; запустить **P1** после авторства epic/story / requirement shaping, не выдумывать очередь.
4. Следующую волну брать **только** из индекса, pkg/`--list`, или явной команды (`run_mode=…` из plan §safe-override).

**Запрещено:**

- Брать порядок из памяти или исполнять raw REQ без materialized story + task `README.md` + pkg.
- Invent `STORY-AIBRIDGE-*` / `EPIC-AIBRIDGE-*` без фактов из REQ-01 / parent REQ-47.
- Смешивать aibridge work с `builder_project: gpt` без явной команды (protocol framing = GPT UI; runtime = this profile).
- Путать nested `.git` в `doge-ai-bridge/` с корневым DOGEstonia git.

---

## 2. `treat-missing-epic-as-not-decomposed` — эпик без task queue = не декомпозирован

Если `EPIC-AIBRIDGE-*` появится в `doge-ai-bridge/docs/tasks/epics/`, но в bullrun **нет** Builder Queue task queue:

- Считать эпик **не декомпозированным**.
- **Не** начинать P3 Execute.
- Запустить **P1.1** + [`bullrun-epic-decompose.md`](../../../.cursor/commands/bullrun-epic-decompose.md) или **P1.3** для backlog story.

**Primary intakes:**

- **`requirement`** — `$requirementDoc` = [REQ-01](../../../doge-ai-bridge/docs/requirements/REQ-01-doge-ai-bridge-runtime.md).
- **P1.3** `backlog_story` — keys `STORY-AIBRIDGE-*`.
- **P1.1** `epic_story` — keys `EPIC-AIBRIDGE-*`; default pkg kind `epic_story_tree`.

Parent protocol framing — [REQ-47](../../../GPT%20UI/docs/requirements/REQ-47-responses-api-https-bearer-bridge.md); **не** дублировать в child stories.

---

## 3. `sync-index-after-each-task` — индекс в той же итерации

После **каждого** закрытого task или story gate (и при **emit** новых stories):

1. Обновить `bullrun-launch-index.md` и [`backlog-stories/INDEX.md`](../../../doge-ai-bridge/docs/tasks/backlog-stories/INDEX.md).
2. Обновить §«Актуальная точка».
3. Не откладывать sync на конец сессии.

---

## 4. `pick-input-mode-explicitly` — один режим входа на сессию

| `input_mode` | Якорь P1/P3/P4 | Когда (aibridge) |
|--------------|----------------|------------------|
| `requirement` | `@$requirementDoc` (REQ-01) | **Primary** до backlog emit |
| `backlog_story` | `@$storyFile` (`STORY-AIBRIDGE-*`); опц. `@$backlogIndex` | После авторства story → P1.3 |
| `epic_story` | `@$epicFile` (`EPIC-AIBRIDGE-*`) | Декомпозиция эпика |
| `run_mode=…` | gap list из `aibridge_builder.plan.md` §safe-override | Post-audit; **не** менять active pkg |

**Один режим на сессию.**

**Bootstrap marker t00:** methodology only — **не** P3 product work на marker.

**PA (до P1):** workflow §PA — shaping; без pkg и без P3.

**hasUxPipeline:** false — не spa UI-0..UI-3.

---

## 5. Date discipline (artifact dates)

```bash
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project aibridge --verify --check-dates
```

SSOT: [`guides/builder-artifact-dates.md`](../guides/builder-artifact-dates.md).

---

## Session checklist

```markdown
## AI Bridge session resolve

- verify: ok N paths | FAIL (→ REQ shaping / author STORY + P1 first)
- check-dates: ok / WARN / FAIL
- index: bullrun-launch-index §Актуальная точка
- active pkg: aibridge-active-package.current.yaml → pkg-…
- input_mode: requirement | backlog_story | epic_story | run_mode=… (один)
- stack: Python; skill python-pro
- REQ: REQ-01 (`doge-ai-bridge/docs/requirements/`) — do not invent AC
- next work: <из --list или backlog INDEX / REQ, не из памяти>
```

---

## SSOT order (aibridge)

1. `run_mode` override list (если оператор явно указал)  
2. Active `aibridge-active-packages/pkg-*.yaml` + `--verify`  
3. `bullrun-launch-index.md` + `backlog-stories/INDEX.md`  
4. **Requirement:** REQ-01 (+ parent REQ-47 framing only) · **Backlog:** `STORY-AIBRIDGE-*` · **Epic:** `EPIC-AIBRIDGE-*`  
5. Task `README.md` + acceptance-verification

Pipeline: [`aibridge-story-execution-pipeline.md`](../../../doge-ai-bridge/docs/tasks/aibridge-story-execution-pipeline.md).

---

## 6. Аудит P4 / P7 (якоря по `input_mode`)

Отчёты: `doge-ai-bridge/docs/analysis/` (создать при необходимости). Мышление: `@.cursor/rules/analysis.mdc`. Промпты — [workflow.md](../core/workflow.md) §P4 / §P7.

| Режим | Cursor P4 | External re-audit |
|-------|-----------|-------------------|
| `requirement` | Факт vs `$requirementDoc` + AC | workflow §P4 |
| `backlog_story` | Факт-код vs AC в `@$storyFile` | workflow §P4 |
| `epic_story` | Факт vs AC Stories в `$epicFile` | workflow §P4 |
| `run_mode=…` | Findings + AC тасков override | workflow §P7 |

Build plan **не** содержит таблицу P4 — только эта секция и workflow.

---

## 7. P1.3 / P1.1 appendix (aibridge)

| Параметр | Значение |
|----------|----------|
| Epic prefix | `EPIC-AIBRIDGE-*` |
| Story prefix | `STORY-AIBRIDGE-*` |
| Materialize path | `doge-ai-bridge/docs/tasks/epics/` |
| Task naming | `task-aibridge-*` |
| Execution skill | `python-pro` |
| Requirement | [`REQ-01`](../../../doge-ai-bridge/docs/requirements/REQ-01-doge-ai-bridge-runtime.md) |
| Parent protocol | [`REQ-47`](../../../GPT%20UI/docs/requirements/REQ-47-responses-api-https-bearer-bridge.md) |

**hasUxPipeline:** false.
