# Zeya888 Method — operator manual (dialog restore console)

**UI brand:** **Zeya888 Method** (HTML `<title>` / `<h1>`).  
**HTML:** [`dialog-restore-console.html`](./dialog-restore-console.html)  
**Work catalog:** [`dialog-restore-work-catalog.js`](./dialog-restore-work-catalog.js) (generated)  
**Rebuild catalog:** `python3 docs/methodology/Zeya888-builder-queue/tools/build-dialog-restore-work-catalog.py`  
**Frequent snips SSOT:** [`../prompts/architect/prompts-manual.md`](../prompts/architect/prompts-manual.md)  
**Extracts:** [`../analysis/dialog-restore-extracts/`](../analysis/dialog-restore-extracts/)  
**Peers:** [`../guides/add-builder-profile.md`](../guides/add-builder-profile.md) · [`../prompts/migration/migration-orchestrator.md`](../prompts/migration/migration-orchestrator.md) · [`../prompts/migration/migration-validator.md`](../prompts/migration/migration-validator.md)  
**Rules:** [`.cursor/rules/analysis.mdc`](../../../../.cursor/rules/analysis.mdc)

## Purpose

Один HTML (**Zeya888 Method**) для двух поверхностей:

1. **Инициализация** — после wipe Cursor `state.vscdb` (или cold-start роли): скопировать paste карточки в новый Agent-чат с тем же именем.
2. **Рабочие промпты** — каталог methodology `prompts/` + частые snip’ы из `prompts-manual.md`, без беготни по файлам.

## Root surface

| Surface | UI label | Contents |
|---------|----------|----------|
| `init` (default) | **Инициализация** | Nested restore/fresh + init cards (Method/Root/O/V/…) + Post-init сверка |
| `work` | **Рабочие промпты** | **Markstack spotlight** (top) → Frequent (manual) → architect / operator / migration / ux / training |

## Init modes (только на surface=init)

| Mode | UI label | Paste contents |
|------|----------|----------------|
| `restore` (default) | **Восстановить workspace** | Full Stage1 init + stage-2 `@…/dialog-restore-extracts/{slug}-extract.md` when Present |
| `fresh` | **Запустить новый** | **Bootstrap only** (Stage1) — no extract `@` |

Cards without extract (most **O**, `dogestonia-v`, `floou-v`, …): both modes show the same bootstrap fence.

**Method Zeya888:** restore = skill init + `@zeya888-extract.md`; fresh = skill Stage1 only. Peer bridge under `analysis/dialog-bridges/` stays for clean-agent handoff — not Stage1 `@` in restore mode.

## Work surface

- **Markstack spotlight** (`#method-spotlight`, top of Work only): method pin — residual/screens → L1→L1.5→L2 stories; Guide/Prompt links (`a.ms-doc-link`) **copy** workspace `@path` to clipboard and try `window.open` `_blank` (console stays open); ⎘ copies short attach-fence (not full catalog paste).
- **Section jumps:** ▴ / ▾ on Markstack head and each Work `section-bar` (`Частые…`, `prompts/<folder>/`) — anchors on headings (`#sec-markstack`, `h2.section-h[id=sec-…]`); smooth scroll with sticky-header offset so the **section title** sits below the toolbar (first card not clipped); ends disabled.
- Cards rendered from `dialog-restore-work-catalog.js` (`window.ZEYA888_WORK_CATALOG`).
- Each card: human blurb + `$params` + scrollable Copy-paste fence; ⎘ copies the fence only.
- **Frequent** order = section order in `prompts-manual.md`.
- After editing prompts or manual → re-run `build-dialog-restore-work-catalog.py` (same directory as HTML for `file://` load).
- PA/P* fences remain in [`workflow-console.html`](./workflow-console.html) / `core/workflow.md` — not duplicated here.

## Card roles (init)

| `data-role` | Typical paste |
|-------------|---------------|
| Method | skill `zeya888` (+ extract in restore) |
| Root / Cross | orientation fence (+ extract in restore) |
| A | Capybara A bootstrap |
| O / V | `@orchestrator` / `@validator` + `migration-role-bootstrap` + `builder_project:` |
| Shared | Post-init verify snip |

Do **not** invent Builder (**B**) cards unless operator explicitly asks.

## Extract docking

- Packs live in `analysis/dialog-restore-extracts/{slug}-extract.md` (`slug` = card `id`).
- Stage-2 appears **only** in restore paste (`pre-{slug}`).
- Bootstrap paste (`pre-{slug}-bootstrap`) is always Stage1 before `\n---\nAFTER`.
- Author extracts via migration restore-extract / root-cross / fixup prompts — not by inventing packs for silent HTML completeness.

## Adding a new profile → O + V cards

After [`add-builder-profile.md`](../guides/add-builder-profile.md) materializes `profiles.yaml` + contract (+ workflow-console §1.1):

1. Choose sidebar titles (e.g. `Foo O` / `Foo V`) and kebab `id`s (`foo-o` / `foo-v`).
2. Add two `<details class="card">` in the HTML (`#init-main`):
   - `data-title` / `data-role="O"|"V"` / `id="{slug}"`
   - **Bootstrap** fence from migration-orchestrator / migration-validator wrappers: `@.cursor/skills/{orchestrator|validator}/SKILL.md` + `@…/migration-role-bootstrap.md` + `builder_project: {profile_key}` + `focus_role` + `workspace_root`.
   - Dual `<pre>`: `paste-restore` and `paste-bootstrap` — initially **identical** (no extract yet).
3. Bump method VERSION/CHANGELOG when shipping the HTML change.
4. Optional later: run extract prompt in the live V/O dialog → write `{slug}-extract.md` → append stage-2 **only** to restore `<pre>`; regenerate bootstrap `<pre>` from Stage1 (split on `\n---\nAFTER`).

## Forbidden

- Invent extract files «so the path exists».
- One-sided Cursor skill dual-sync edits.
- Claiming restore mode without disk extract Present.
- Mixing `$clientId` Root cards with `builder_project` O/V keys.
- Hand-editing `dialog-restore-work-catalog.js` (regenerate instead).

## Smoke

- Header shows **Zeya888 Method** (not «Dialog console»).
- Toggle surface init ↔ work; work shows Markstack → Frequent then folder sections.
- Markstack Guide/Prompt click: toast with `@docs/methodology/…`; console page not replaced.
- Work section ▴/▾: jumps to section **heading** below sticky toolbar (title fully visible; first card not clipped); Markstack ↔ Frequent ↔ `prompts/…`; first ▴ / last ▾ disabled.
- Toggle restore ↔ fresh; V-with-extract: fresh has no `@dialog-restore-extracts`.
- Copy uses the visible paste for the active mode (init) or work fence (work).
- New profile: O+V bootstrap cards Copy works in **Запустить новый** before any extract exists.
- After manual edit: rebuild catalog; refresh HTML; Frequent order matches manual headings.
