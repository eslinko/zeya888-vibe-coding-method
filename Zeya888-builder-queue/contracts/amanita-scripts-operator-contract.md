        # Amanita Scripts Builder — operator contract

        > **Plan (read-only unless operator asks):** [`.cursor/plans/Amanita-Scripts_builder.plan.md`](../../../.cursor/plans/Amanita-Scripts_builder.plan.md)  
        > **Propagation:** [builder-session/SKILL.md](../../../.cursor/skills/builder-session/SKILL.md) · [builder-operator-habits.mdc](../../../.cursor/rules/builder-operator-habits.mdc) · [session-starter.md](../core/session-starter.md)

        Process-reminder правила для `builder_project: amanita-scripts` (focus `amanita/scripts/`).  
        **Layout class:** nested peer monorepo under `amanita/` — **not** `clients.yaml` / client tenancy (no Root card, no dual-plan under `clients/`).  
        P1/PA промпты — только [workflow.md](../core/workflow.md); не дублировать в plan.

        ---

        ## 1. `resolve-start-from-index` — старт только из индекса + active pkg

        **Перед** batch-run, Build window или P3 Execute:

        **Fixed plan:** `@attach` [`.cursor/plans/Amanita-Scripts_builder.plan.md`](../../../.cursor/plans/Amanita-Scripts_builder.plan.md) + workflow §P3/P6 в **этом** чате — **не** Build / Execute plan на файле ([fixed-builder-plan-execution.md](../guides/fixed-builder-plan-execution.md)).

        1. Прочитать [`amanita/scripts/docs/tasks/bullrun-launch-index.md`](../../../amanita/scripts/docs/tasks/bullrun-launch-index.md) §«Актуальная точка».
        2. Прочитать [`amanita-scripts-active-package.current.yaml`](../../../amanita/scripts/docs/tasks/amanita-scripts-active-package.current.yaml) → `package_file`, `activation`.
        3. Из корня workspace:  
           `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project amanita-scripts --verify`  
           При `FAIL` — **стоп**; запустить **P1.3** / **PA+requirement** после авторства stories, не выдумывать очередь.
        4. Следующую волну брать **только** из индекса, pkg/`--list`, или явной команды (`run_mode=…` из plan §safe-override).

        **Запрещено:**

        - Брать порядок из памяти или исполнять raw REQ без materialized story + task `README.md` + pkg.
        - Invent `STORY-AMSCR-*` / epics без фактов из backlog / REQ.
        - Путать nested `.git` в `amanita/` с корневым DOGEstonia git.
        - Добавлять `clients.yaml` / Root card / `clients/Amanita/` для этого профиля.
        - Путать с flat keys `scripts` / `arweave` (другие корни).

        ---

        ## 2. `treat-missing-epic-as-not-decomposed` — эпик без task queue = не декомпозирован

        Если `EPIC-AMSCR-*` появится в `amanita/scripts/docs/tasks/epics/`, но в bullrun **нет** Builder Queue task queue:

        - Считать эпик **не декомпозированным**.
        - **Не** начинать P3 Execute.
        - Запустить **P1.1** + [`bullrun-epic-decompose.md`](../../../.cursor/commands/bullrun-epic-decompose.md) или **P1.3** для backlog story.

        **Primary intakes:**

        - **P1.3** `backlog_story` — keys `STORY-AMSCR-*` (confirm at first emit) from backlog INDEX.
        - **`requirement`** — `$requirementDoc` under `amanita/scripts/docs/requirements/` when authored.

        ---

        ## 3. `sync-index-after-each-task` — индекс в той же итерации

        После **каждого** закрытого task или story gate (и при **emit** новых `STORY-AMSCR-*`):

        1. Обновить `bullrun-launch-index.md` и [`backlog-stories/INDEX.md`](../../../amanita/scripts/docs/tasks/backlog-stories/INDEX.md).
        2. Обновить §«Актуальная точка».
        3. Не откладывать sync на конец сессии.

        ---

        ## 4. `pick-input-mode-explicitly` — один режим входа на сессию

        | `input_mode` | Якорь P1/P3/P4 | Когда (amanita-scripts) |
        |--------------|----------------|----------------|
        | `backlog_story` | `@$storyFile` (`STORY-AMSCR-*`); опц. `@$backlogIndex` | **Primary default:** после авторства story |
        | `requirement` | `@$requirementDoc` | Когда REQs существуют под `amanita/scripts/docs/requirements/` |
        | `epic_story` | `@$epicFile` (`EPIC-AMSCR-*`) | Когда эпик materialize |
        | `run_mode=…` | gap list из `Amanita-Scripts_builder.plan.md` §safe-override | Post-audit; **не** менять active pkg |

        **Один режим на сессию.**

        **Bootstrap marker t00:** methodology only — **не** P3 product work на marker.

        **PA (до P1):** workflow §PA — shaping; без pkg и без P3.

        **Stack:** Node deploy/catalog tooling in `amanita/scripts/`; skill `javascript-pro`. Amanita scripts under amanita/scripts/.

**Collision guard:** CLI `--project amanita-scripts` ≠ `--project scripts` (workspace `scripts/`).

        **hasUxPipeline:** false — не spa UI-0..UI-3.

        ---

        ## 5. Date discipline (artifact dates)

        ```bash
        python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
        python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project amanita-scripts --verify --check-dates
        ```

        SSOT: [`guides/builder-artifact-dates.md`](../guides/builder-artifact-dates.md).

        ---

        ## Session checklist

        ```markdown
        ## Amanita Scripts session resolve

        - verify: ok N paths | FAIL (→ author STORY / REQ shaping + P1 first)
        - check-dates: ok / WARN / FAIL
        - index: bullrun-launch-index §Актуальная точка
        - active pkg: amanita-scripts-active-package.current.yaml → pkg-…
        - input_mode: backlog_story | requirement | epic_story | run_mode=… (один)
        - layout: nested peer amanita/ — not clients.yaml
        - stack: Node deploy/catalog tooling; skill javascript-pro
        - next work: <из --list или backlog INDEX, не из памяти>
        ```

        ---

        ## SSOT order (amanita-scripts)

        1. `run_mode` override list (если оператор явно указал)  
        2. Active `amanita-scripts-active-packages/pkg-*.yaml` + `--verify`  
        3. `bullrun-launch-index.md` + `backlog-stories/INDEX.md`  
        4. **Backlog:** `backlog-stories/` · **Requirements:** `docs/requirements/` (intake, не очередь)  
        5. Task `README.md` + acceptance-verification

        Pipeline: [`amanita-scripts-story-execution-pipeline.md`](../../../amanita/scripts/docs/tasks/amanita-scripts-story-execution-pipeline.md).

        ---

        ## 6. Аудит P4 / P7 (якоря по `input_mode`)

        Отчёты: `amanita/scripts/docs/analysis/` (создать при необходимости). Мышление: `@.cursor/rules/analysis.mdc`. Промпты — [workflow.md](../core/workflow.md) §P4 / §P7.

        | Режим | Cursor P4 | External re-audit |
        |-------|-----------|-------------------|
        | `backlog_story` | Факт-код vs AC в `@$storyFile` | workflow §P4 |
        | `requirement` | Факт vs `$requirementDoc` + AC | workflow §P4 |
        | `epic_story` | Факт vs AC Stories в `$epicFile` | workflow §P4 |
        | `run_mode=…` | Findings + AC тасков override | workflow §P7 |

        Build plan **не** содержит таблицу P4 — только эта секция и workflow.

        ---

        ## 7. P1.3 `backlog_story` / requirement (amanita-scripts appendix)

        Используется с [workflow.md](../core/workflow.md) §P1.3 / §P1.2 (`$p13Appendix` для `builder_project: amanita-scripts`).

        | Параметр | Значение |
        |----------|----------|
        | Epic prefix (target) | `EPIC-AMSCR-*` (when materialize) |
        | Story prefix | `STORY-AMSCR-*` |
        | Materialize path | `amanita/scripts/docs/tasks/epics/` (after P1) |
        | Execution skill | `javascript-pro` |
        | Requirements SSOT | `amanita/scripts/docs/requirements/` (when authored) |

        **hasUxPipeline:** false — не spa UI-0..UI-3.
