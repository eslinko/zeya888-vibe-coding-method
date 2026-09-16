# Operator identity harvest — universal prompt

**Категория:** operator (meta-layer aggregation)  
**Target rule:** [`.cursor/rules/builder-operator-habits.mdc`](../../../../../.cursor/rules/builder-operator-habits.mdc)  
**Method SSOT:** [`.cursor/rules/zeya888-operator-method.mdc`](../../../../../.cursor/rules/zeya888-operator-method.mdc)  
**Claims rule:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Profiles registry:** [`../../specs/profiles.yaml`](../../specs/profiles.yaml)

## Юзкейсы (когда этот промпт)

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | Нужно извлечь из фокусного диалога устойчивые привычки оператора | Harvest → кандидаты + dedup + patch в `builder-operator-habits.mdc` |
| 2 | Нужно собрать «пазл» мета-слоя из нескольких диалогов | Повторить prompt по каждому scope и агрегировать через один target rule |
| 3 | Нужно отсеять одноразовые/шумные наблюдения | Использовать REJECTED + NEEDS_MORE_EVIDENCE gate |

**Вход:** `focus_dialog_scope` (один диалог или пакет диалогов), `target_rule_file` (по умолчанию `.cursor/rules/builder-operator-habits.mdc`).

**Не этот промпт:**  
- создание/переписывание `workflow.md` или `contracts/*`  
- продуктовая реализация P3/P6  
- коммиты/push без явной команды

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@.cursor/rules/builder-operator-habits.mdc
@.cursor/rules/zeya888-operator-method.mdc
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml

focus_dialog_scope: <какой диалог или пакет диалогов анализировать>
target_rule_file: .cursor/rules/builder-operator-habits.mdc
mode: identity-harvest

Задача: извлечь из focus_dialog_scope устойчивые рабочие инварианты оператора и подготовить точечные дополнения в target_rule_file.

MODE: only verified synthesis. No product coding.
Claims: facts from dialog artifacts / files only; else Unknown.
Do NOT rewrite whole target file; apply minimal gap-fill patches.

Жёсткие правила:
1) Только факты из диалога/артефактов на диске; без предположений.
2) Не дублировать то, что уже есть в target_rule_file.
3) Не переписывать структуру файла целиком; только gap-fill.
4) Одноразовые, локальные или спорные наблюдения не добавлять.
5) Для каждого кандидата дать evidence (пути/фразы/артефакты).
6) Не конфликтовать с SSOT из zeya888-operator-method.mdc.
7) Не менять `workflow.md`, `contracts/*`, `profiles.yaml` в этой задаче.

Классификация (обязательно):
- method
- style_architecture
- naming
- preferred_patterns
- never_always
- project_specific

Сначала выведи анализ:
A) CANDIDATES
- id
- category
- proposed_rule (1 строка)
- why_persistent
- evidence
- target_section_in_mdc

B) REJECTED
- item
- reason (duplicate | one-off | weak evidence | SSOT conflict)

C) NEEDS_MORE_EVIDENCE
- item
- what is missing

D) PATCH_PLAN
- минимальный список изменений в target_rule_file

После анализа:
- Внеси только согласованные gap-fill правки в target_rule_file.
- Сохрани лаконичный стиль существующего .mdc.
- Другие файлы не трогай, если это не нужно для ссылочной целостности.

Финальный отчёт:
1) Что добавлено
2) Что отклонено
3) Diff summary
4) Residual gaps
```

---

## Примечания

- Этот prompt проект-агностичен: профили и стек берутся из `profiles.yaml`.
- Если scope пустой/нечитаемый — остановиться и запросить уточнение, не патчить `.mdc`.
- Если найден конфликт с `zeya888-operator-method.mdc` — не писать правило, вынести в `REJECTED`.
