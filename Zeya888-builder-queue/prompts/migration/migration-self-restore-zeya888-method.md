# Migration self-restore — Zeya888 method context

**Категория:** migration / self-restore  
**Цель:** быстро восстановить мой рабочий контекст после потери state/chat-памяти и продолжить работу в контракте Zeya888 Builder Queue без фантазий.

## Когда использовать

- После удаления `state.vscdb`/reset Cursor state.
- После миграции в новый workspace/новое окно.
- Когда нужно заново подгрузить не только роль/профиль, но и сам смысл метода Zeya888: что это, зачем, где SSOT и как именно мы работаем.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@.cursor/rules/zeya888-operator-method.mdc
@.cursor/rules/builder-operator-habits.mdc
@docs/methodology/Zeya888-builder-queue/MANIFEST.md
@docs/methodology/Zeya888-builder-queue/core/workflow.md
@docs/methodology/Zeya888-builder-queue/core/session-starter.md
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
@docs/methodology/Zeya888-builder-queue/prompts/INDEX.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md

workspace_root: /Users/eslinko/Development/DOGEstonia
builder_project: <gateway|gpt|spa|taxonomy|identity|scripts|capybara|landing|zeya888|arweave|dogestonia|aibridge|zeya888-brand|threads>
focus_role: <builder|validator|orchestrator>
context_sources: <список ключевых файлов/линков задачи, если уже есть>

SELF-RESTORE MODE.
Нужно восстановить мой рабочий контекст в методе Zeya888 Builder Queue строго по файлам на диске.
Никаких product-правок, коммитов, push.
Claims только path-based; если не найдено — Unknown.

Сделай 5 блоков:

1) METHOD SNAPSHOT (что это и зачем)
- Кратко: что такое Zeya888 Builder Queue и для чего он применяется в этом workspace.
- Распиши роли OP/BLD/VAL и цикл PA/P0–P8.
- Покажи, где читать SSOT по методу (файлы/пути).

2) PROJECT SNAPSHOT (где работаем)
- Разреши `builder_project` через profiles.yaml.
- Верни: focus_folder, tasks_dir, plan_file, pipeline_doc, test_command, execution_skill_primary.
- Укажи verify-команду для проекта.

3) ROLE LOCK SNAPSHOT (как работаем сейчас)
- Зафиксируй границы для `focus_role`:
  - builder: execution only по README/pkg;
  - validator: read-only audit;
  - orchestrator: routing/session/wave, без product-кода.
- Дай hard bans для роли (что запрещено делать в этом режиме).

4) HOW WE WORK (операционный контракт)
- Сформулируй рабочие инварианты команды:
  - file-first memory;
  - immutable pkg discipline;
  - один input_mode на волну;
  - verify/date gates;
  - sync index/dashboard в той же итерации закрытия;
  - no assumptions/no invented AC.
- Дай ссылки на источники каждого инварианта.

5) READY HANDOFF PACKET
- Верни ready packet:
  - role
  - project
  - resolved_paths
  - verify_command
  - first_safe_next_step (одно конкретное действие)
  - unknowns (если есть)

Формат ответа:
- Коротко, структурно, на русском.
- Без markdown-таблиц.
- Без общих фраз вне найденных фактов.
```

---

## Ожидаемый результат

После запуска этого prompt у меня должен быть восстановлен:
- смысл метода Zeya888 (что это и для чего),
- конкретный проектный контур (какие файлы и команды использовать),
- role-lock текущей волны,
- безопасный первый шаг продолжения работы.
