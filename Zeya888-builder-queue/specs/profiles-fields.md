# Поля `profiles.yaml`

Реестр: [`profiles.yaml`](./profiles.yaml). Ключ `--project` в CLI = ключ в `projects:`.

| Поле | Назначение |
|------|------------|
| `enabled` | `true` / `false` — профиль доступен в CLI |
| `focus_folder` | Корень кодовой базы проекта (путь от корня workspace; см. nested ниже) |
| `tasks_dir` | Каталог tasks/docs (pkg, index, pipeline) |
| `active_packages_dir` | Подкаталог `*-active-packages/` |
| `current_pointer` | Файл `*-active-package.current.yaml` |
| `build_windows_subdir` | Относительно `tasks_dir`: куда писать окна |
| `build_window_prefix` | Префикс имени файла окна |
| `next_readme_dotfile` | Pointer `.gateway-next-readme` и аналоги |
| `pkg_path_prefix` | Префикс путей в pkg YAML |
| `plan_file` | Operative builder plan (обычно `.cursor/plans/`) |
| `pipeline_doc` | Epic/story execution pipeline |
| `ui_visual_pipeline_doc` | Опционально (spa): полный SSOT UI Visual Pipeline (UI-0..UI-3, классификация, P1.3 fields) |
| `default_input_kind` | `epic_story_tree` \| `task_list_linear` |
| `input_package_yaml_key` | Ключ metadata в pkg |
| `artifact_kind` | Тип build window artifact |
| `build_window_title` | Заголовок в генерируемом окне |
| `test_command` | Команда тестов для Phase 0 |
| `stack_label` | Человекочитаемый стек (Python, React/JS, GPT Actions) |
| `execution_skill_primary` | Slug execution skill для P1/P3 (напр. `python-pro`, `react-expert`) |
| `execution_skill_fallback` | Опционально: запасной slug (напр. `javascript-pro` для spa) |
| `execution_skill_path` | Путь к SKILL.md от корня workspace — SSOT для `@` attach при code changes |
| `queueless` | `true` — только `--verify` (напр. `taxonomy`) |
| `verify_paths` | Список файлов для queueless verify |

**Execution skill:** данные в `profiles.yaml`; логика резолва и override task README — [builder-session/SKILL.md](../../../../.cursor/skills/builder-session/SKILL.md) §Execution skill resolution.

## Nested paths (G8 / W0)

CLI [`builder_resolve_queue.py`](../cli/builder_resolve_queue.py) resolves `tasks_dir` / `pipeline_doc` / pkg paths as `workspace_root / relative` (`Path` join). A relative value **may contain `/`** (e.g. `clients/Alvasar/backend/docs/tasks`).  

| Fact | Implication |
|------|-------------|
| Live DOGEstonia profiles stay **flat** single-segment (or `"GPT UI"`) peers | Nested is additive; do not relocate gateway/spa/… |
| `test_command` is a shell string | Must `cd` the same nested path as `focus_folder` |
| `pkg_path_prefix` / `linear_paths` | Use full relative paths from workspace root matching nested `tasks_dir` |

Client layout convention: [`../guides/client-tenancy.md`](../guides/client-tenancy.md) · registry [`clients.yaml`](./clients.yaml).

## Добавление нового проекта

**Куда писать alias + path:** [`profile-intakes/<profile_key>.yaml`](./profile-intakes/) (`profile_key` + `focus_folder`).  
**Operative:** [`../prompts/migration/migration-add-builder-profile.md`](../prompts/migration/migration-add-builder-profile.md).  
**Checklist SSOT:** [`../guides/add-builder-profile.md`](../guides/add-builder-profile.md).

Кратко: intake YAML → migration prompt → `profiles.yaml` + bootstrap `{tasks_dir}` → operator contract → Gateway-clone plan → `--verify` → intake в `profile-intakes/done/`.
