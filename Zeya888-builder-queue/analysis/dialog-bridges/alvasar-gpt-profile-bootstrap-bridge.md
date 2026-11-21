# Bridge — Zeya888 method-ops dialog (sidebar title: Zeya888)

**dialogName:** `alvasar-gpt-profile-bootstrap` (filename stable) · **sidebar / HTML card:** `Zeya888`  
**dialogKind:** `mixed` (method_ops dominant)  
**bridgeScope:** `full`  
**Файл:** `docs/methodology/Zeya888-builder-queue/analysis/dialog-bridges/alvasar-gpt-profile-bootstrap-bridge.md`  
**Prompt SSOT:** [`../../prompts/migration/migration-dialog-context-bridge.md`](../../prompts/migration/migration-dialog-context-bridge.md) · **Output home:** [`README.md`](./README.md)  
**UTC foundation:** `2026-11-15T14:32:00Z` · **bridge refreshed:** `2026-11-18T11:01:49Z`  
**Workspace:** `/Users/eslinko/Development/DOGEstonia`  
**Source dialog (transcript / agent store):** `f002f3d0-08b9-4e9d-8241-4bc30c1b0849`  
**Rules:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc) · [`.cursor/rules/builder-operator-habits.mdc`](../../../../../.cursor/rules/builder-operator-habits.mdc) · [`.cursor/rules/zeya888-operator-method.mdc`](../../../../../.cursor/rules/zeya888-operator-method.mdc)  
**Audience:** полностью чистый агент. Читать §0–§4 **до** instance §5–§7. Не сводить весь метод к Alvasar product.

**Mission:** method-ops чат **Zeya888** — как поднимать профили/client tenancy, dialog-bridges, dual-sync Cursor skills, UX package bootstrap в method pack, restore Agent-диалогов после wipe `state.vscdb`, triage `docs/analysis`.

---

## 0. Как пользоваться

1. Method map + entry paths (§1–§4).
2. Instance (§5–§7) — не повторять Done.
3. Smoke §10.
4. Paste-packet §11 или новый ask.
5. **Name ≠ create** / ask-scoped (`analysis.mdc`).
6. Product queue → skill [`builder-session`](../../../../../.cursor/skills/builder-session/SKILL.md). Method-ops → skill [`Zeya888`](../../../../../.cursor/skills/zeya888/SKILL.md).

---

## 1. Topic meta map

| Theme | Essence | Boundaries | SSOT |
|-------|---------|------------|------|
| Builder Queue method | PA / P0–P8, pkg, profiles | Not invent process | [`MANIFEST.md`](../../MANIFEST.md) · [`core/workflow.md`](../../core/workflow.md) |
| Profile / tenancy bootstrap | Paths A–D; nested `clients/<Client>/` | Name ≠ create instruction corpora | [`guides/add-builder-profile.md`](../../guides/add-builder-profile.md) · [`guides/client-tenancy.md`](../../guides/client-tenancy.md) |
| Dialog bridges | Handoff → clean agent | Outputs under `analysis/dialog-bridges/` not `docs/analysis/` | [`migration-dialog-context-bridge.md`](../../prompts/migration/migration-dialog-context-bridge.md) |
| Cursor skills dual-sync | Runtime `.cursor/skills/` ≡ portable `integration/cursor-skills/` | Edit both paths | [`integration/cursor-skills/README.md`](../../integration/cursor-skills/README.md) |
| UX ADMIN → artboards ZIP | After ADMIN-01 `UX-PROMPTS.md` | Not P3 UI-0..UI-3 | [`ux-package-bootstrap-universal.md`](../../prompts/architect/ux-package-bootstrap-universal.md) · [`req-to-ui-admin-layers.md`](../../prompts/architect/req-to-ui-admin-layers.md) |
| Dialog restore HTML | Recreate O/V/Root/special chats after wipe | No B / no invent missing chats | [`tools/dialog-restore-console.html`](../../tools/dialog-restore-console.html) |
| Analysis triage | KEEP/DELETE report | Mode A: no rm until ok | [`analysis-triage-2026-11-18.md`](./analysis-triage-2026-11-18.md) |

---

## 2. Method layer (thin)

Pointers: MANIFEST · workflow · session-starter · profiles.yaml · clients.yaml · contracts · `*_builder.plan.md` + fixed-plan rule · CLI `--verify` · VERSION/CHANGELOG · [`migration-self-restore-zeya888-method.md`](../../prompts/migration/migration-self-restore-zeya888-method.md) (optional companion).

---

## 3. Entry paths A–D (appendix — practiced)

| Path | Launch |
|------|--------|
| A | [`migration-add-builder-profile.md`](../../prompts/migration/migration-add-builder-profile.md) + guide §1 |
| B | [`migration-profile-from-checked-out-dir.md`](../../prompts/migration/migration-profile-from-checked-out-dir.md) |
| C | [`client-tenancy.md`](../../guides/client-tenancy.md) nested MS |
| D | guide §5 split |

---

## 4. Dialog arc (ordered)

1. Multi-client tenancy + `telegram` (1.4.63) + `alvasar-gpt` Path C (1.4.64, client `b0bf056`)
2. Dialog-bridge SSOT + prompt materialize
3. Method push `b5dc8e7` (1.4.64)
4. Vendor `builder-session` dual-sync **1.4.65** (`b2d2e47`); bridge refresh `38da863`
5. UX package bootstrap universal **1.4.66** (`afba6bd`); prompts-manual `007a01f`
6. Dialog restore HTML + skill **Zeya888** dual-sync + analysis triage report (this wave → **1.4.67**)

---

## 5. Verified state (disk)

```bash
cat docs/methodology/Zeya888-builder-queue/VERSION   # expect 1.4.67 after this wave bump
test -f docs/methodology/Zeya888-builder-queue/tools/dialog-restore-console.html
test -f .cursor/skills/zeya888/SKILL.md
cmp -s .cursor/skills/zeya888/SKILL.md \
  docs/methodology/Zeya888-builder-queue/integration/cursor-skills/zeya888/SKILL.md
cmp -s .cursor/skills/builder-session/SKILL.md \
  docs/methodology/Zeya888-builder-queue/integration/cursor-skills/builder-session/SKILL.md
test -f docs/methodology/Zeya888-builder-queue/prompts/architect/ux-package-bootstrap-universal.md
test -f docs/methodology/Zeya888-builder-queue/analysis/analysis-triage-2026-11-18.md
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project alvasar-gpt --verify
```

Present: profiles include `alvasar-gpt`; dialog-bridges; cursor-skills `builder-session` + `zeya888`; restore HTML; triage report (no deletes done).

---

## 6. File map highlights

| Item | Status |
|------|--------|
| `VERSION` / CHANGELOG | bump **1.4.67** this wave |
| `tools/dialog-restore-console.html` | Present |
| `.cursor/skills/zeya888/` + portable | Present dual-sync |
| `ux-package-bootstrap-universal.md` | Present (1.4.66) |
| `analysis-triage-2026-11-18.md` | Present; DELETE candidates need operator ok |
| Alvasar gpt instruction corpora | **Absent** |

---

## 7. Forbidden

- Repeat bootstrap alvasar-gpt / telegram / vendor 1.4.65–66 when green.
- Create instruction corpora without explicit create ask.
- Confuse `builder_project: gpt` vs `alvasar-gpt`; `client_id: alvasar` vs profile keys.
- Put dialog-bridges under workspace `docs/analysis/`.
- Edit only one side of skill dual-sync.
- `rm` analysis from triage without explicit ok.
- Recreate Builder (B) dialogs in restore HTML (operator excluded).

---

## 8. Launch / next recipes

- method_ops → add-builder-profile / client-tenancy / dual-sync skill edit
- restore wipe → open dialog-restore-console.html
- UX → ADMIN-01 → UX-PROMPTS → ux-package-bootstrap → ADMIN-02
- product → builder-session + profile contract
- triage → review DELETE? then «ок удаляй» with scope

---

## 9. Smoke checklist

```bash
cd /Users/eslinko/Development/DOGEstonia
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
test -f docs/methodology/Zeya888-builder-queue/tools/dialog-restore-console.html
test -f .cursor/skills/zeya888/SKILL.md
cmp -s .cursor/skills/zeya888/SKILL.md docs/methodology/Zeya888-builder-queue/integration/cursor-skills/zeya888/SKILL.md
test -f docs/methodology/Zeya888-builder-queue/analysis/analysis-triage-2026-11-18.md
grep -E '^1\.4\.67$' docs/methodology/Zeya888-builder-queue/VERSION
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project alvasar-gpt --verify
```

---

## 10. Paste-packet — чистому агенту (карточка HTML **Zeya888**)

```markdown
@.cursor/rules/analysis.mdc
@.cursor/skills/zeya888/SKILL.md
@docs/methodology/Zeya888-builder-queue/analysis/dialog-bridges/alvasar-gpt-profile-bootstrap-bridge.md
@docs/methodology/Zeya888-builder-queue/tools/dialog-restore-console.html
@docs/methodology/Zeya888-builder-queue/integration/cursor-skills/README.md

Ты чистый агент. Sidebar title = Zeya888. bridgeScope=full · dialogKind=mixed · skill Zeya888 (method-ops).
1) Прочитай bridge §1–§7, затем skill Zeya888.
2) Smoke §9; отрапортуй: VERSION(=1.4.67) / zeya888 dual_sync / dialog-restore HTML Present / triage report Present / alvasar-gpt verify.
3) Не повторяй Done волны 1.4.64–1.4.67.

Дальше — один режим по моей следующей строке (если нет — STOP и спроси):
A) Bootstrap NEW profile Path A/B/C: $profile_key= $focus_folder= …
B) Open/use dialog-restore-console for other chats
C) UX package bootstrap / ADMIN layers
D) Analysis DELETE after explicit ok + scope
E) Edit skill dual-sync (zeya888 or builder-session)
F) Methodology commit/push
G) Other: <ask>
```

---

## 11. Unknowns

- Operator ok scope for analysis DELETE candidates.
- Whether rename bridge filename away from `alvasar-gpt-profile-bootstrap` — Unknown (filename stable for now).

---

## 12. End state one-liner

Method-ops dialog **Zeya888** practiced tenancy + alvasar-gpt + dialog-bridges + skill dual-sync (builder-session 1.4.65, Zeya888 skill 1.4.67) + UX bootstrap 1.4.66 + dialog-restore HTML + analysis triage report (no rm yet).
