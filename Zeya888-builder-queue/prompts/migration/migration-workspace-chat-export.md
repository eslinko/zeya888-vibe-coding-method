# Migration — export workspace chats (file-first handoff)

**Категория:** migration (new workspace / lost sidebar continuity)  
**Скрипт:** [`../../tools/export-workspace-chats.py`](../../tools/export-workspace-chats.py)  
**Companion restore:** [`migration-self-restore-zeya888-method.md`](./migration-self-restore-zeya888-method.md)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

---

## When

| Use case | Да / нет |
|----------|----------|
| Новый workspace; нужны **контексты** активных Agent/Composer чатов как markdown | **Да** |
| Хотите «оживить» те же чаты в sidebar Cursor как продолжаемые composers | **Нет** — не поддерживается этим пакетом |
| Нужен только метод/роль без истории чатов | **Нет** → self-restore / role-bootstrap |

**Факт (локально проверено):** чаты привязаны к URI папки (`workspaceStorage` + `~/.cursor/projects/<slug>/agent-transcripts/`). Тот же Cursor-аккаунт и IDE-профиль **Zeya888** не переносят sidebar автоматически.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-workspace-chat-export.md
@docs/methodology/Zeya888-builder-queue/tools/export-workspace-chats.py

$oldWorkspace=/Users/eslinko/Development/DOGEstonia
$outDir=
$mode=selected
$ids=
$lastN=40

Migration — EXPORT workspace chats (read-only; markdown packs only).

MODE: analysis.mdc. No product code. Do NOT write Cursor state.vscdb / workspaceStorage.
Do NOT claim sidebar chats will reappear in a new folder.
Do NOT paste .env secrets into handoff files.

## Step 1 — Resolve
- Confirm $oldWorkspace exists.
- Default out: $oldWorkspace/docs/analysis/chat-handoff-<utc> if $outDir empty.
- mode: selected (composer.composerData + pinned) | all (also every transcript dir).
- If $ids set (CSV UUIDs) — export only those.

## Step 2 — Run export (shell)
From any cwd:

python3 docs/methodology/Zeya888-builder-queue/tools/export-workspace-chats.py \
  --workspace "$oldWorkspace" \
  --out "$outDir" \
  --mode $mode \
  --ids "$ids" \
  --last-n $lastN

If --out empty, omit --out (script picks docs/analysis/chat-handoff-<utc>).

## Step 3 — Report
Reply with: out path | INDEX.md path | count exported | any missing_transcript=yes rows.
List UUID + title lines from INDEX (no full message dump unless operator asks).

## Step 4 — Handoff to new workspace (instructions only)
1) Open new folder; ensure IDE profile Zeya888.
2) Copy the chat-handoff-* directory into the new root (or keep absolute path).
3) New chat: paste migration-self-restore-zeya888-method.md + @ INDEX.md + selected UUID .md files.
4) Continue work in NEW chats; use handoffs as evidence, not as live composer state.

STOP after report unless operator says «запиши» to place packs under a specific path.
```

---

## Примечания

- Скрипт **только читает** `state.vscdb` и jsonl; пишет только markdown.
- Лёгкий redact строк `*KEY*/*TOKEN*/*SECRET*/*PASSWORD*=` — не замена ручной проверке.
- IDE-профиль **Zeya888** ≠ Builder Queue ключ `zeya888` в `profiles.yaml`.
