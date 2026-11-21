---
name: Zeya888
description: >-
  Zeya888 methodology / method-ops dialog (not product builder_project P0–P8).
  Use when the operator works in the method root chat named Zeya888, restores
  after state.vscdb wipe, runs dialog-context-bridge, vendors Cursor skills
  dual-sync, bootstraps builder profiles / client tenancy, wires UX ADMIN →
  UX-PROMPTS → ux-package-bootstrap, or triages docs/analysis. Triggers on
  Zeya888 method chat, dialog-restore-console, migration-dialog-context-bridge,
  integration/cursor-skills, add-builder-profile, client-tenancy, analysis triage.
---

# Zeya888 — method-ops session

**Not** [`builder-session`](../builder-session/SKILL.md) (that = product `builder_project` → Phase 0 / P1–P8).  
**This skill** = methodology operator dialog: method pack SSOT, restore, profile/tenancy ops, dialog bridges, UX method prompts, analysis hygiene.

Rules: [`.cursor/rules/analysis.mdc`](../../rules/analysis.mdc) · [`builder-operator-habits.mdc`](../../rules/builder-operator-habits.mdc) · [`zeya888-operator-method.mdc`](../../rules/zeya888-operator-method.mdc)

## When to apply

- Chat titled **Zeya888** (method root) or operator says method-ops / methodology restore.
- After Cursor `state.vscdb` wipe — recreate dialogs via [`dialog-restore-console.html`](../../../docs/methodology/Zeya888-builder-queue/tools/dialog-restore-console.html).
- Dialog handoff → clean agent: [`migration-dialog-context-bridge.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/migration/migration-dialog-context-bridge.md) → [`analysis/dialog-bridges/`](../../../docs/methodology/Zeya888-builder-queue/analysis/dialog-bridges/).
- Profile bootstrap Paths A–D / client tenancy / portable skill dual-sync.
- UX method chain: `req-to-ui-admin-layers` → `UX-PROMPTS.md` → [`ux-package-bootstrap-universal.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/architect/ux-package-bootstrap-universal.md).
- Analysis triage (KEEP/DELETE report) — **no** bulk delete without explicit ok.

## Dual-sync (skills in method pack)

| Role | Path |
|------|------|
| Runtime | `.cursor/skills/zeya888/SKILL.md` |
| Portable | `docs/methodology/Zeya888-builder-queue/integration/cursor-skills/zeya888/SKILL.md` |

Edit **both** in one wave. Same rule for [`builder-session`](../builder-session/SKILL.md) — see [`integration/cursor-skills/README.md`](../../../docs/methodology/Zeya888-builder-queue/integration/cursor-skills/README.md).

## SSOT map (pointers only)

| Topic | Path |
|-------|------|
| Manifest / what is BQ | [`MANIFEST.md`](../../../docs/methodology/Zeya888-builder-queue/MANIFEST.md) |
| VERSION / CHANGELOG | [`VERSION`](../../../docs/methodology/Zeya888-builder-queue/VERSION) · [`CHANGELOG.md`](../../../docs/methodology/Zeya888-builder-queue/CHANGELOG.md) |
| Profiles / clients | [`specs/profiles.yaml`](../../../docs/methodology/Zeya888-builder-queue/specs/profiles.yaml) · [`specs/clients.yaml`](../../../docs/methodology/Zeya888-builder-queue/specs/clients.yaml) |
| Add profile | [`guides/add-builder-profile.md`](../../../docs/methodology/Zeya888-builder-queue/guides/add-builder-profile.md) |
| Client tenancy | [`guides/client-tenancy.md`](../../../docs/methodology/Zeya888-builder-queue/guides/client-tenancy.md) |
| Cursor wiring | [`integration/cursor-setup.md`](../../../docs/methodology/Zeya888-builder-queue/integration/cursor-setup.md) |
| Dialog restore HTML | [`tools/dialog-restore-console.html`](../../../docs/methodology/Zeya888-builder-queue/tools/dialog-restore-console.html) |
| Role migrate O/V/B | [`migration-orchestrator.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/migration/migration-orchestrator.md) · [`migration-validator.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/migration/migration-validator.md) · [`migration-role-bootstrap.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/migration/migration-role-bootstrap.md) |
| This dialog bridge | [`analysis/dialog-bridges/`](../../../docs/methodology/Zeya888-builder-queue/analysis/dialog-bridges/) — use newest `*-bridge.md` paste-packet |
| Useful prompts index | [`prompts/INDEX.md`](../../../docs/methodology/Zeya888-builder-queue/prompts/INDEX.md) |

## Hard bans

- Do not run product P3/P6 from this skill unless operator switches to `builder-session` + `builder_project`.
- Do not invent profiles, instruction corpora, or analysis deletes.
- Name ≠ create; ask-scoped delivery (`analysis.mdc`).
- Do not shorten migration prompt fences when filling restore HTML / paste packets.

## Restore this method chat after wipe

1. Open [`dialog-restore-console.html`](../../../docs/methodology/Zeya888-builder-queue/tools/dialog-restore-console.html).
2. Expand card **Zeya888** → copy paste-packet → new Agent chat → rename **Zeya888**.
3. Or `@` latest bridge under `analysis/dialog-bridges/` and follow its paste-packet.
4. Smoke: `VERSION`, dual-sync `cmp` for skills, `--verify` only for profiles operator cares about.

## Related skills

- Product BLD queue → [`builder-session`](../builder-session/SKILL.md)  
- Product OP chats (`* O`) → [`orchestrator`](../orchestrator/SKILL.md)  
- Product VAL chats (`* V`) → [`validator`](../validator/SKILL.md)
