# Life-sim node load run (промпт2 — интервью)

**Категория:** architect / cross-project Operator  
**Не заменяет:** Gateway Builder P1–P8  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

**Роль этого файла:** **не** opener диалога. Opener = [`cross-project-system-orientation.md`](./cross-project-system-orientation.md) (ссылка из мануала).  
Этот промпт — **глубокое интервью** по всем входящим переменным life-sim (manual §4), затем (только по «execute») следование [`Life_sim_load.plan.md`](../../../../../.cursor/plans/Life_sim_load.plan.md).

**Когда:** нужно с нуля (или после wipe) наполнить демо-ноду: interview → wipe → provision → replay → cluster → threads → SPA.

**SSOT деталей (не реплицировать в ответ):**  
[`doge-complaints-gateway/docs/runtime-docs/manuals/life-sim-demo-node-load-manual-ru.md`](../../../../../doge-complaints-gateway/docs/runtime-docs/manuals/life-sim-demo-node-load-manual-ru.md)

**Reusable plan (execute):** [`.cursor/plans/Life_sim_load.plan.md`](../../../../../.cursor/plans/Life_sim_load.plan.md)

**Opener диалога:** [`cross-project-system-orientation.md`](./cross-project-system-orientation.md)

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/architect/cross-project-system-orientation.md
@docs/methodology/Zeya888-builder-queue/prompts/architect/life-sim-node-load-run.md
@doge-complaints-gateway/docs/runtime-docs/manuals/life-sim-demo-node-load-manual-ru.md
@.cursor/plans/Life_sim_load.plan.md

Life-sim node load — промпт2 (интервью → execute).

MODE:
1) Если диалог ещё не открыт через orientation — сначала Phase A из orientation, затем продолжай здесь.
2) Этот файл НЕ открывает диалог. Он проводит глубокое интервью по manual §4
   (проработка параметров, не форма «заполни YAML»). SSOT замысла/locks/runbook = мануал;
   product REQ в этот ход не подключать.
3) MUST закрыть interview ДО любого wipe/load. Accept осознанные "defaults" только после
   короткой проработки смысла ноды (хотя бы node_social_direction).
4) После согласия: зафиксируй params (чат + ops history path из manual §4.5). STOP — жди
   «execute» / «загружай». Не invent pack-generator CLI.
5) On execute: следуй только Life_sim_load.plan. Wipe — Present tooling из manual §5 (REQ11-06)
   или operator wipe + --wipe-confirmed. Не пиши wipe/код в этом диалоге (name ≠ create).
6) analysis.mdc: verified paths only; secrets gitignored; STOP на блокере с evidence.
7) Не paste/replicate тело мануала — @ и цитируй секции.
```

---

## Phase I — Глубокое интервью (обязательно)

Цель: **проработать** с оператором каждый блок params из manual §4 так, чтобы замысел ноды был ясным и согласованным. Это не чеклист «введи значения».

### Как вести

- Один смысловой блок за раз; уточняющие вопросы; примеры «что получится на доске».
- Trade-offs: scale locks vs скорость прогона; foci vs Present sample `*_v0_1` (Partial если тексты не совпадут).
- Defaults — только **осознанно** («оставляем scale locks из manual §4.1, направление такое-то»).
- Пока interview не закрыт — **не** wipe, **не** provision, **не** simulate.

### Блоки (порядок)

1. **Профиль и замысел** — `profile_id` (local / uus-veerenni); зачем эта нода сейчас.
2. **`node_social_direction`** — 1–3 предложения о социальной линии (двор, конфликт, сезон). Проработай формулировку вместе с оператором.
3. **Scale locks** — оставить значения из manual §4.1 (200 / Gauss 8.5 / 60·30·10 / calendar) или осознанно сузить (LIMIT / MAX_STORIES → Partial).
4. **`user_context`** — personas / neighbourhood_tags / notes: нужны ли роли и микрогеография, или нейтральные Resident N.
5. **`story_foci.themes`** — темы+веса+blurbs et/ru/en, или civic defaults; если foci сильнее sample — предупреди Partial на Present fixtures.
6. **Pipeline knobs** — `cluster_force` / `threads_seed` / `spa_verify` (обычно все on).
7. **`pack_id`** — предложи `ls-<YYYYMMDD>T<HHMM>Z-<sense-slug>` из UTC + смысл `node_social_direction`; подтверди путь `life_sim_packs/<pack_id>/` (manual §4.5).

### Выход interview

Краткая таблица согласованных params + путь истории прогона + явная пометка Full vs Partial (sample).  
Затем **STOP** — ждать оператора **execute**.

---

## Phase II — Execute (только по команде)

Следуй todos / фазам в `Life_sim_load.plan.md` **без** повторного интервью.

- Wipe: только Present tooling из manual §5; иначе STOP или operator wipe + runner `--wipe-confirmed`.
- Identity / admin **не** трогать.
- Fixtures: Present sample / generator из manual §8 + `make simulate-life-sim`; interview params — направляющие.
- Отчёт: Pass / Partial / STOP + evidence paths.

---

## Hard rules

- Orientation = старт диалога; этот файл = интервью + gate на execute.
- Мануал = SSOT params/wipe/runbook; plan = оркестратор команд; этот файл не дублирует таблицы мануала.
- Нет STORY-07 / pack-generator ветки.
- Не invent HTTP wipe / force-cluster; force cluster = cron path `process_all_pending`.
- Live wipe/fill — только после явного «execute».
