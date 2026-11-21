# Migration — dialog restore extract fixup (доработка уже написанного pack)

**Категория:** migration (уже написанный `*-extract.md` → сверка Meta vs claims + thin patch)  
**Input:** существующий pack под [`../../analysis/dialog-restore-extracts/`](../../analysis/dialog-restore-extracts/)  
**Peers:** [`migration-dialog-restore-extract-root-cross.md`](./migration-dialog-restore-extract-root-cross.md) (новый Root/Cross) · [`migration-dialog-restore-extract.md`](./migration-dialog-restore-extract.md) (новый O/V)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

Не полный re-extract. Промпт **доработки**: прочитать pack + Meta на диске; при FAIL — патч только tip / Verified / Overlay OPEN. Orientation/bootstrap fence не трогать.  
**First intended use:** [`../../analysis/dialog-restore-extracts/cross-project-system-analysis-extract.md`](../../analysis/dialog-restore-extracts/cross-project-system-analysis-extract.md) (STORY-96 tip honesty).

---

## When

| Use case | Да / нет |
|----------|----------|
| Pack уже Written; нужна доработка tip Status / Overlay OPEN | **Да** |
| Новый extract с нуля (Root/Cross) | **Нет** → [`migration-dialog-restore-extract-root-cross.md`](./migration-dialog-restore-extract-root-cross.md) |
| Новый extract с нуля (O/V) | **Нет** → [`migration-dialog-restore-extract.md`](./migration-dialog-restore-extract.md) |
| HTML concat | **Нет** — отдельный ask |

---

## Tip / Status honesty (same as root-cross)

1. **Disk beats chat memory** (and beats stale text inside the extract).  
2. Every STORY/REQ tip named in arc/Overlay/`$tipFocus` → **Read Meta/Status this turn**.  
3. Forbidden: leave «Todo / CODE_REQUIRED» in extract if Meta says Met / Done / next P5.  
4. Historical arc bullets may stay; **Current tip (now)** + Overlay OPEN must match Meta.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-dialog-restore-extract-fixup.md
@docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/README.md

$extractPath=
$dialogTitle=
$tipFocus=

Migration — DIALOG RESTORE EXTRACT FIXUP (доработка существующего pack).

MODE: analysis.mdc. Disk Meta beats extract text and chat memory.
Name ≠ create outside $extractPath. No product code. No HTML edit. No dialog-bridges write.
Do NOT rewrite the full orientation / bootstrap fence. Do NOT full re-extract.

## Identify

1) $extractPath = required path to existing *-extract.md
2) Read the extract. List STORY/REQ tips named in Dialog arc + Overlay (+ $tipFocus if set).
3) For each tip: Read Meta (or REQ Status) on disk this turn — Status, Finish Line/Delivery, Next, UTC if present.
4) Compare extract claims vs disk → PASS/FAIL per tip (and OPEN consistency).

## Deliverables (strict order)

1) Short status in chat (5–10 sentences): extract path · tips checked · disk vs extract · PASS/FAIL list.
2) If any FAIL:
   Patch ONLY drifted lines in $extractPath:
   - Add/update **Tip honesty (current)** table under Verified
   - Fix Verified tip row / arc «Current tip (now)» bullet
   - Fix Overlay DONE/OPEN so OPEN ≠ stale CODE Todo when Meta is Met/next P5
   Keep FULL orientation / bootstrap fence byte-stable (do not truncate or replace init).
3) If all PASS:
   Report ok. Write only if Tip honesty table missing and no tip named → add one N/A row; else no write.
4) Report: extract path | FAIL count | patched yes/no | Unknowns. STOP.

## Smoke (after patch or PASS)

- [ ] Disk Meta Read for every named tip
- [ ] Overlay OPEN consistent with Meta
- [ ] Orientation / bootstrap fence unchanged
- [ ] No invent Accepted / live SUCCESS

## Operator context (fill)

- extractPath=docs/methodology/Zeya888-builder-queue/analysis/dialog-restore-extracts/
- dialogTitle=
- tipFocus=
```

---

## Примечания

- Same honesty rules as root-cross authoring; this is the **fixup lane** for packs already on disk.  
- Usable on O/V extracts if tip drift appears (optional `$tipFocus`).  
- After PASS on Cross/Root packs → safe for HTML concat wave.
