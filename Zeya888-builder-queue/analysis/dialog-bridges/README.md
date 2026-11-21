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

**Peer (не путать):** [`../dialog-restore-extracts/`](../dialog-restore-extracts/) — стыковка под [`../../tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html). Bridges = clean-agent handoff; extracts = restore-card docking.  

**Zeya888 method-ops:** bridge file [`alvasar-gpt-profile-bootstrap-bridge.md`](./alvasar-gpt-profile-bootstrap-bridge.md) remains peer SSOT; HTML Method card stage-2 uses [`../dialog-restore-extracts/zeya888-extract.md`](../dialog-restore-extracts/zeya888-extract.md) (bridge→extract transform; do not delete this bridge without explicit ask).
