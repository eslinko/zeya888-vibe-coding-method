# profile-intakes — alias + path → bootstrap

**Назначение:** тонкий intake для нового Builder Queue профиля. Оператор пишет **два обязательных поля** (`profile_key` + `focus_folder`); agent по [`migration-add-builder-profile.md`](../../prompts/migration/migration-add-builder-profile.md) создаёт профиль с нуля по checklist [`add-builder-profile.md`](../../guides/add-builder-profile.md) §1.

**Не** runtime SSOT для CLI. CLI читает только [`../profiles.yaml`](../profiles.yaml).

## Как пользоваться

1. Скопировать [`_TEMPLATE.yaml`](./_TEMPLATE.yaml) → `<profile_key>.yaml` в этой папке (не в `done/`).
2. Заполнить `profile_key` (alias = `--project`) и `focus_folder` (путь от корня workspace).
3. Опционально — overrides в том же файле.
4. Запустить copy-paste из [`migration-add-builder-profile.md`](../../prompts/migration/migration-add-builder-profile.md) с `@` на intake.
5. Review plan → «запиши» → `--verify` ok.
6. После успеха agent **переносит** файл в [`done/`](./done/).

## Правила

- Один pending intake = один профиль. Не держать materialized файлы в корне `profile-intakes/`.
- Derived поля (`tasks_dir`, `plan_file`, …) **не** дублировать — считаются по guide §0 из `profile_key` + `focus_folder`.
- `profile_key` может отличаться от имени папки (`spa` / `spa-app`) — тогда `focus_folder` обязателен и явен.
- `done/` — архив materialized intakes; не запускать migration повторно на них без явной команды.

## Связанные

- Guide: [`../../guides/add-builder-profile.md`](../../guides/add-builder-profile.md)
- Поля registry: [`../profiles-fields.md`](../profiles-fields.md)
- Curriculum: [`../../curriculum/05-connect-your-project.md`](../../curriculum/05-connect-your-project.md) шаг 3
