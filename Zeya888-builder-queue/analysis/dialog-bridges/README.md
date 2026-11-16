# Dialog bridges — output home

**Назначение:** handoff «диалог → полностью чистый агент».  
**Naming:** `{dialogName}-bridge.md`  
**Prompt SSOT:** [`../../prompts/migration/migration-dialog-context-bridge.md`](../../prompts/migration/migration-dialog-context-bridge.md)  
**Default `$bridgeScope`:** `full` = **Topic meta map** (суть фокусных тем с диска) + thin Zeya888 method pointers + dialog arc / instance.  
**`$dialogKind`:** `project_focus` | `cross_project` | `method_ops` | `mixed`.  
**Rules:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

Profile entry paths A–D — **не** default; только appendix при `method_ops` или если диалог реально поднимал профили.  
Узкий `operative` — только по явному сужению.  
Не класть product REQ/code stubs. Override пути — `$bridgeOutDir=`.
