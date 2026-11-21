# Dialog restore extracts — output home

**Назначение:** стыковочные packs «живой диалог → restore HTML».  
Полный перенос контекста + **стартовый фокус** из дефолтного bootstrap по классификации диалога.  
**HTML:** [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html) — mode **Восстановить workspace** = init + stage-2 `@extract`; **Запустить новый** = bootstrap only. Manual: [`../../tools/dialog-restore-console.md`](../../tools/dialog-restore-console.md).

**Naming:** `{sidebar-slug}-extract.md`  
Slug = kebab от точного sidebar title (`AIBridge V` → `aibridge-v-extract.md`, `Zeya888` → `zeya888-extract.md`).

**Prompt SSOT:**
- O/V / role: [`../../prompts/migration/migration-dialog-restore-extract.md`](../../prompts/migration/migration-dialog-restore-extract.md)
- Root / Cross / system-root: [`../../prompts/migration/migration-dialog-restore-extract-root-cross.md`](../../prompts/migration/migration-dialog-restore-extract-root-cross.md) (`$rootKind=client_tenancy|doge_platform`; tip-honesty)
- Already-written pack fixup: [`../../prompts/migration/migration-dialog-restore-extract-fixup.md`](../../prompts/migration/migration-dialog-restore-extract-fixup.md)
- Method **Zeya888:** extract authored from peer bridge (see below); class `method_ops`

**Rules:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

## vs dialog-bridges/

| | [`../dialog-bridges/`](../dialog-bridges/) | **this folder** |
|--|---------------------------------------------|-----------------|
| Job | Handoff → **чистый агент** / method meta | Стыковка под **dialog-restore** карточки |
| Naming | `{dialogName}-bridge.md` | `{sidebar-slug}-extract.md` |
| Prompt | `migration-dialog-context-bridge.md` | restore-extract (+ root-cross / fixup) |

**Zeya888:** peer bridge [`../dialog-bridges/alvasar-gpt-profile-bootstrap-bridge.md`](../dialog-bridges/alvasar-gpt-profile-bootstrap-bridge.md) kept; restore card uses [`zeya888-extract.md`](./zeya888-extract.md).  
Still **without** extract (init-only in HTML): `dogestonia-v`, `floou-v`, most O cards.

## Operator flow

1. Copy-paste extract prompt in live dialog → `{slug}-extract.md` here.  
2. Tip drift → fixup prompt `$extractPath=`.  
3. HTML cards with extract: Copy = init + `@this/{slug}-extract.md`.
