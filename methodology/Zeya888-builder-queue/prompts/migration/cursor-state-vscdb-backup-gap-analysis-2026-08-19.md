# GAP-анализ: удаление `state.vscdb.backup` в Cursor

Date: 2026-08-19  
Scope: проверка потерь при удалении `~/Library/Application Support/Cursor/User/globalStorage/state.vscdb.backup` и сопоставление с уже вынесенным в файловые артефакты проекта.

## TL;DR

- По факту в `~/Library/Application Support/Cursor/User/globalStorage/` файла `state.vscdb.backup` сейчас нет.
- Backup-файл есть в профильном хранилище `Zeya888`: `~/Library/Application Support/Cursor/User/profiles/7c47acfe/globalStorage/state.vscdb.backup`.
- Удаление только `state.vscdb.backup` не удаляет рабочий `state.vscdb`, поэтому немедленной потери текущего состояния обычно нет.
- Главный риск: теряется точка отката локального state на момент создания backup (исторические UI/agent/chat-state записи, если они были только там).
- `plans`, `rules`, Builder Queue профиль `zeya888`, migration/start prompts, а также файлы транскриптов в project storage не зависят от этого backup и сохраняются.

## Что проверено (факты)

1. **User globalStorage**
   - Есть: `state.vscdb`, `state.vscdb-wal`, `state.vscdb-shm`, `storage.json`.
   - Нет: `state.vscdb.backup`.

2. **Profile globalStorage (Zeya888)**
   - Папка профиля: `~/Library/Application Support/Cursor/User/profiles/7c47acfe/`.
   - Есть: `globalStorage/state.vscdb`, `globalStorage/state.vscdb.backup`, `state.vscdb-wal`, `state.vscdb-shm`.
   - В backup SQLite есть таблицы `ItemTable`, `cursorDiskKV`; `ItemTable` содержит записи state-ключей (включая chat/composer view state).

3. **Связь текущего workspace с профилем**
   - `~/Library/Application Support/Cursor/User/globalStorage/storage.json` содержит:
     - `userDataProfiles: [{ "location": "7c47acfe", "name": "Zeya888" }]`
     - `profileAssociations` для `file:///Users/eslinko/Development/DOGEstonia` -> `7c47acfe`.
   - `~/Library/Application Support/Cursor/User/settings.json` содержит `window.newWindowProfile: "Zeya888"`.

4. **Артефакты проекта, не зависящие от Cursor state backup**
   - Правила: `.cursor/rules/builder-operator-habits.mdc` (и другие `.mdc`).
   - Планы: `.cursor/plans/*`, включая `.cursor/plans/Zeya888_builder.plan.md`.
   - Builder Queue профиль: `docs/methodology/Zeya888-builder-queue/specs/profiles.yaml`.
   - Prompt-стартеры/миграции: `docs/methodology/Zeya888-builder-queue/prompts/operator/*` и `prompts/migration/*`.
   - Локальные transcript-экспорты проекта: `~/.cursor/projects/Users-eslinko-Development-DOGEstonia/agent-transcripts/...`.

## Потери при удалении `state.vscdb.backup`

## Потеряете

- **Возможность локального rollback на backup-снимок** профильного SQLite state (если основной state повредится или потребуется восстановление из backup).
- **Историческое состояние UI/agent-pane/chat-pane**, если какая-то часть осталась только в backup и уже отсутствует в текущем `state.vscdb`.

## Не потеряете

- Файлы проекта в репозитории (`docs/**`, `.cursor/rules/**`, `.cursor/plans/**`, код, markdown, yaml).
- Ваш собранный style/meta-слой в `.cursor/rules/builder-operator-habits.mdc`.
- Prompt-стартеры трех типов диалогов и migration-prompts per profile.
- Builder Queue профиль `zeya888` в `profiles.yaml`.
- Git-историю/коммиты/ветки.
- Профильные настройки как файлы (`User/profiles/7c47acfe/settings.json`, `keybindings.json`, `extensions.json`) — они отдельны от backup.

## GAP-анализ относительно уже собранных артефактов

## Уже закрыто (persisted в файлах)

- **Контексты/процессы**: rules и prompts в репозитории.
- **Стартеры диалогов**: operator-root prompts и migration-prompts в `docs/methodology/Zeya888-builder-queue/prompts/`.
- **Операторский стиль**: `.cursor/rules/builder-operator-habits.mdc`.
- **Профиль Builder Queue `zeya888`**: `specs/profiles.yaml` + связанные contract/plan/docs.

## Остается уязвимым (не SSOT в repo)

- **Эфемерный IDE state Cursor**: window/layout/view-state, часть локальных связок чатов/панелей/recent state, которые живут в `state.vscdb`/`storage.json`.
- **Точки восстановления IDE state**: если удалить backup, останется только current state без запасного снимка.

## Ответ на вопрос про Zeya888 профиль

- **Builder Queue профиль `zeya888` (проектный)**: неприкасаем удалением `state.vscdb.backup`, т.к. это файл в репозитории (`profiles.yaml`).
- **Cursor UI профиль `Zeya888` (IDE-профиль)**: при удалении только backup обычно остается рабочим (используется `state.vscdb` + профильные json), но вы теряете резервный снимок его состояния.

## Нужно ли экспортировать

Рекомендуется сделать минимальный экспорт перед удалением backup:

1. Экспортировать UI-профиль `Zeya888` через меню Cursor `Export Profile (Zeya888)...`.
2. Скопировать папку `~/Library/Application Support/Cursor/User/profiles/7c47acfe/`.
3. Скопировать `~/Library/Application Support/Cursor/User/globalStorage/storage.json`.
4. Убедиться, что все критичные проектные артефакты закоммичены в git (rules/plans/prompts/specs).

## Практический вывод

Если удаляется **только** `state.vscdb.backup`, то проектная методология и ваш `zeya888` Builder Queue профиль не пострадают.  
Это операция про риск потери точки отката IDE-состояния, а не про потерю SSOT-артефактов репозитория.

## Safe-чеклист перед удалением backup

Выполнять при **закрытом Cursor** (чтобы не работать с открытым SQLite-файлом).

1. **Проверить текущий профиль и связь с workspace**
   - Убедиться, что workspace `DOGEstonia` ассоциирован с профилем `7c47acfe` (Zeya888):
   ```bash
   python3 - <<'PY'
   import json, pathlib
   p = pathlib.Path.home() / "Library/Application Support/Cursor/User/globalStorage/storage.json"
   data = json.loads(p.read_text())
   ws = "file:///Users/eslinko/Development/DOGEstonia"
   assoc = data.get("profileAssociations", {}).get("workspaces", {}).get(ws)
   profiles = data.get("userDataProfiles", [])
   print("workspace_profile:", assoc)
   print("profiles:", profiles)
   PY
   ```

2. **Сделать файловый snapshot profile storage (быстрый rollback)**
   ```bash
   TS="$(date +%Y%m%d-%H%M%S)"
   SRC="$HOME/Library/Application Support/Cursor/User/profiles/7c47acfe/globalStorage"
   DST="$HOME/Desktop/cursor-zeya888-globalStorage-backup-$TS"
   mkdir -p "$DST"
   cp -a "$SRC/." "$DST/"
   echo "Snapshot created: $DST"
   ```

3. **(Опционально) Экспорт профиля через UI**
   - Cursor -> Preferences -> Profile (Zeya888) -> `Profiles` -> Export.

4. **Проверить, что проектные SSOT-артефакты в repo на месте**
   ```bash
   ls -la "/Users/eslinko/Development/DOGEstonia/.cursor/rules/builder-operator-habits.mdc"
   ls -la "/Users/eslinko/Development/DOGEstonia/.cursor/plans/Zeya888_builder.plan.md"
   ls -la "/Users/eslinko/Development/DOGEstonia/docs/methodology/Zeya888-builder-queue/specs/profiles.yaml"
   ```

## Удаление backup (точечно)

```bash
rm "$HOME/Library/Application Support/Cursor/User/profiles/7c47acfe/globalStorage/state.vscdb.backup"
```

## Post-чеклист после удаления

1. **Файл backup действительно удален**
```bash
ls -la "$HOME/Library/Application Support/Cursor/User/profiles/7c47acfe/globalStorage" | rg "state\.vscdb(\.backup)?"
```

2. **Ассоциация workspace -> Zeya888 не изменилась**
```bash
python3 - <<'PY'
import json, pathlib
p = pathlib.Path.home() / "Library/Application Support/Cursor/User/globalStorage/storage.json"
data = json.loads(p.read_text())
ws = "file:///Users/eslinko/Development/DOGEstonia"
assoc = data.get("profileAssociations", {}).get("workspaces", {}).get(ws)
profiles = {x.get("location"): x.get("name") for x in data.get("userDataProfiles", [])}
print("workspace_profile_id:", assoc)
print("workspace_profile_name:", profiles.get(assoc))
PY
```

Ожидаемо:
- `workspace_profile_id: 7c47acfe`
- `workspace_profile_name: Zeya888`

3. **Профильные файлы настроек существуют**
```bash
ls -la "$HOME/Library/Application Support/Cursor/User/profiles/7c47acfe/settings.json"
ls -la "$HOME/Library/Application Support/Cursor/User/profiles/7c47acfe/keybindings.json"
ls -la "$HOME/Library/Application Support/Cursor/User/profiles/7c47acfe/extensions.json"
```

4. **Проектные артефакты не затронуты**
```bash
ls -la "/Users/eslinko/Development/DOGEstonia/.cursor/rules/builder-operator-habits.mdc"
ls -la "/Users/eslinko/Development/DOGEstonia/.cursor/plans/Zeya888_builder.plan.md"
ls -la "/Users/eslinko/Development/DOGEstonia/docs/methodology/Zeya888-builder-queue/specs/profiles.yaml"
```

## Критерий успеха

- Cursor открывает `DOGEstonia` под профилем `Zeya888`.
- Файл `state.vscdb.backup` удален.
- Ассоциации в `storage.json` и проектные SSOT-файлы без изменений.

---

## Памятка: если удаляете не backup, а `state.vscdb` (из-за размера)

Ниже сценарий именно для удаления **основного** файла state (например, когда `state.vscdb` вырос до ~14 GB).

## Что изменится

- Cursor пересоздаст новый пустой `state.vscdb` при следующем запуске.
- Потеряется локальный IDE-runtime state из удаленного файла: часть UI layout/view-state/recent pane state, локальные ephemeral привязки pane/chat-state.
- Проектные SSOT-файлы в репозитории (`plans/rules/prompts/specs`) не удаляются этой операцией.

## Pre-delete (обязательно)

1. Полностью закрыть Cursor.
2. Сохранить `storage.json` и профильную папку `7c47acfe` (или минимум `globalStorage`), чтобы не потерять ассоциации/профильные метаданные.

```bash
TS="$(date +%Y%m%d-%H%M%S)"
BASE="$HOME/Library/Application Support/Cursor/User"
DST="$HOME/Desktop/cursor-user-safety-$TS"
mkdir -p "$DST"

cp -a "$BASE/globalStorage/storage.json" "$DST/storage.json"
cp -a "$BASE/profiles/7c47acfe" "$DST/profile-7c47acfe"
echo "Safety snapshot: $DST"
```

Выполнила (19.08.2026)
eslinko@Evgeniyas-MBP DOGEstonia % TS="$(date +%Y%m%d-%H%M%S)"
BASE="$HOME/Library/Application Support/Cursor/User"
DST="$HOME/Desktop/cursor-user-safety-$TS"
mkdir -p "$DST"

cp -a "$BASE/globalStorage/storage.json" "$DST/storage.json"
cp -a "$BASE/profiles/7c47acfe" "$DST/profile-7c47acfe"
echo "Safety snapshot: $DST"
Safety snapshot: /Users/eslinko/Desktop/cursor-user-safety-20260819-145217

3. Зафиксировать, какой файл удаляете:

```bash
ls -lah "$HOME/Library/Application Support/Cursor/User/globalStorage/state.vscdb"
ls -lah "$HOME/Library/Application Support/Cursor/User/profiles/7c47acfe/globalStorage/state.vscdb"
```

## Удаление `state.vscdb` (точечно)

Удаляйте только тот файл, который реально разросся.

```bash
# Вариант A: user-level state
rm "$HOME/Library/Application Support/Cursor/User/globalStorage/state.vscdb"

# Вариант B: profile-level state (Zeya888)
rm "$HOME/Library/Application Support/Cursor/User/profiles/7c47acfe/globalStorage/state.vscdb"
```

## Восстановление после удаления (runbook)

1. Запустить Cursor (файл `state.vscdb` будет создан заново).
2. Открыть workspace `DOGEstonia`.
3. Проверить, что workspace все еще привязан к `Zeya888`:

```bash
python3 - <<'PY'
import json, pathlib
p = pathlib.Path.home() / "Library/Application Support/Cursor/User/globalStorage/storage.json"
data = json.loads(p.read_text())
ws = "file:///Users/eslinko/Development/DOGEstonia"
assoc = data.get("profileAssociations", {}).get("workspaces", {}).get(ws)
profiles = {x.get("location"): x.get("name") for x in data.get("userDataProfiles", [])}
print("workspace_profile_id:", assoc)
print("workspace_profile_name:", profiles.get(assoc))
PY
```

Ожидаемо:
- `workspace_profile_id: 7c47acfe`
- `workspace_profile_name: Zeya888`

4. Проверить, что проектные SSOT на месте:

```bash
ls -la "/Users/eslinko/Development/DOGEstonia/.cursor/rules/builder-operator-habits.mdc"
ls -la "/Users/eslinko/Development/DOGEstonia/.cursor/plans/Zeya888_builder.plan.md"
ls -la "/Users/eslinko/Development/DOGEstonia/docs/methodology/Zeya888-builder-queue/specs/profiles.yaml"
```

5. Если привязка профиля слетела:
   - вручную выбрать профиль `Zeya888` в Cursor;
   - при необходимости восстановить `storage.json` из safety snapshot и перезапустить Cursor.

### Команда восстановления из временной папки (ваш случай)

Для snapshot `"/Users/eslinko/Desktop/cursor-user-safety-20260819-145217"`:

```bash
SNAP="/Users/eslinko/Desktop/cursor-user-safety-20260819-145217"
BASE="$HOME/Library/Application Support/Cursor/User"

# 1) Восстановить profile storage (включая profile globalStorage)
rm -rf "$BASE/profiles/7c47acfe"
cp -a "$SNAP/profile-7c47acfe" "$BASE/profiles/7c47acfe"

# 2) Восстановить storage.json с ассоциациями
cp -a "$SNAP/storage.json" "$BASE/globalStorage/storage.json"

echo "Restore done from $SNAP"
```

После этого запустите Cursor заново.

### Как зафиксировать привязку DOGEstonia -> Zeya888 «глобально»

`profileAssociations` в Cursor хранится на уровне workspace, а не «для всех папок сразу».  
Глобально можно зафиксировать:
- профиль по умолчанию для новых окон (`window.newWindowProfile = "Zeya888"`),
- и конкретную привязку `DOGEstonia -> 7c47acfe` в `storage.json`.

Один скрипт (idempotent), который делает оба шага:

```bash
python3 - <<'PY'
import json
from pathlib import Path

home = Path.home()
user_dir = home / "Library/Application Support/Cursor/User"
settings_path = user_dir / "settings.json"
storage_path = user_dir / "globalStorage/storage.json"

workspace_uri = "file:///Users/eslinko/Development/DOGEstonia"
profile_id = "7c47acfe"
profile_name = "Zeya888"

# 1) Default profile for new windows
settings = {}
if settings_path.exists():
    settings = json.loads(settings_path.read_text() or "{}")
settings["window.newWindowProfile"] = profile_name
settings_path.write_text(json.dumps(settings, ensure_ascii=False, indent=4) + "\n")

# 2) Workspace association
storage = json.loads(storage_path.read_text())
storage.setdefault("profileAssociations", {}).setdefault("workspaces", {})[workspace_uri] = profile_id

profiles = storage.setdefault("userDataProfiles", [])
if not any(p.get("location") == profile_id for p in profiles):
    profiles.append({"location": profile_id, "name": profile_name, "icon": "flame"})

storage_path.write_text(json.dumps(storage, ensure_ascii=False, indent=4) + "\n")

print("window.newWindowProfile =", profile_name)
print("workspace association set:", workspace_uri, "->", profile_id)
PY
```

Проверка:

```bash
python3 - <<'PY'
import json, pathlib
base = pathlib.Path.home() / "Library/Application Support/Cursor/User"
settings = json.loads((base / "settings.json").read_text())
storage = json.loads((base / "globalStorage/storage.json").read_text())
ws = "file:///Users/eslinko/Development/DOGEstonia"
assoc = storage.get("profileAssociations", {}).get("workspaces", {}).get(ws)
profiles = {x.get("location"): x.get("name") for x in storage.get("userDataProfiles", [])}
print("window.newWindowProfile:", settings.get("window.newWindowProfile"))
print("workspace_profile_id:", assoc)
print("workspace_profile_name:", profiles.get(assoc))
PY
```

## Минимальный критерий восстановления

- Cursor открывает `DOGEstonia` под профилем `Zeya888`.
- Новый `state.vscdb` создан.
- Методологические SSOT-файлы проекта доступны и без изменений.
