# Retrospective: catalog-driven image generation (as-is)

> **Status:** retrospective / **as-is** / **not normative**  
> **Date:** 2026-08-16  
> **Method:** [analysis.mdc](../../../../.cursor/rules/analysis.mdc) — observed practice from DOGEstonia agent sessions + artifacts on disk; not a redesign of the process.  
> **Related (normative / tooling — do not confuse with this doc):**  
> [`tools/ui-story-icons-catalog.md`](../tools/ui-story-icons-catalog.md) · [`guides/spa-ui-visual-pipeline.md`](../guides/spa-ui-visual-pipeline.md) · spa [`ICON-GENERATION-INDEX.md`](../../../../spa-app/docs/tasks/backlog-stories/icons/ICON-GENERATION-INDEX.md) · spa [`SPA-ICON-STYLE-PROMPTS.md`](../../../../spa-app/docs/UX/SPA-ICON-STYLE-PROMPTS.md) (late fence) · landing [`STORY-LAND-image-style-prompts.md`](../../../../landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-style-prompts.md)

---

## 1. What “input” meant in practice

Operator / story work typically handed the agent **one catalog markdown** (sometimes plus a style-prompts sibling or a short blocker/gen-prompts pack), not a free-form art brief.

Typical columns / sections in those catalogs:

| Field | Role in practice |
|-------|------------------|
| Sense / mockup context | What the asset means on the artboard |
| Fixed filename (`ic-*.png` or landing `save_to`) | Path contract for code / drop-in |
| Color role | `#f5f7fa` / accent / success / error, or landing palette |
| EN “prompt” row | Human-readable Depict; often **not** executed as AI for SPA `ic-*` |
| §Reuse / §Skip / §Viz | What **not** to generate |

Master index for SPA catalogs: [`spa-app/docs/tasks/backlog-stories/icons/ICON-GENERATION-INDEX.md`](../../../../spa-app/docs/tasks/backlog-stories/icons/ICON-GENERATION-INDEX.md).  
Feedback that catalogs became mandatory beside L10N: [`tools/ui-story-icons-catalog.md`](../tools/ui-story-icons-catalog.md).

Two execution contours actually ran from that kind of input. They were **not** the same tool chain.

---

## 2. Contour A — SPA functional `ic-*` (Lucide pipeline)

### 2.1 Input artifacts

- Story catalogs such as:
  - [`STORY-SPA-ID-12-icon-assets.md`](../../../../spa-app/docs/tasks/backlog-stories/identity-auth/STORY-SPA-ID-12-icon-assets.md)
  - CAB / EPIC-SPA-04 / PH catalogs (indexed from ICON-GENERATION-INDEX)
  - ID-14 missing CTA pair in [`STORY-SPA-ID-14-post-submit-path-choice.md`](../../../../spa-app/docs/tasks/backlog-stories/identity-auth/STORY-SPA-ID-14-post-submit-path-choice.md)
  - Later ES catalog [`STORY-SPA-ES-icon-assets.md`](../../../../spa-app/docs/tasks/backlog-stories/early-signal-dashboard/STORY-SPA-ES-icon-assets.md) (catalog Done; PNG wave may still be pending)
- Conventions repeated in catalogs: PNG RGBA **256×256**, ~15% padding, stroke ~2px, Lucide-like, dark civic UI, dirs under `public/icons/<scope>/`.

### 2.2 What the agent actually did with the EN prompts

Observed pattern:

1. Read the table; split **NEW** vs **Reuse**.
2. For Reuse: verify files on disk; **do not** regenerate.
3. For NEW functional icons: treat EN prompts as **meaning documentation**, not as `GenerateImage` scripts.
4. Map each NEW row → Lucide id + color → rows in [`spa-app/scripts/icons/icon-manifest.yaml`](../../../../spa-app/scripts/icons/icon-manifest.yaml).
5. Run `npm run icons:generate` (or filtered `--catalog` / `--file`), then `icons:validate`, often `icons:contact-sheet`.
6. Write bytes to `public/icons/<out_dir>/ic-*.png`.

Executable defaults observed in manifest: `size: 256`, `padding: 0.15`, `stroke_width: 2`; colors `neutral #f5f7fa`, `accent #f5c542`, `success #4ade80`, `error #f87171`, `amber #fbbf24`.

### 2.3 Special cases inside Contour A

| Case | As observed |
|------|-------------|
| ID-14 `ic-go-to-board` / `ic-my-stories` | Manifest entries (`layout-grid`, `circle-user`) + Lucide generate; status docs marked ON DISK |
| PH `etm-*` | **Not** Lucide; photo refs → `npm run icons:etm` / `generate-etm-from-refs.py` |
| Brand logo / flags | Always Reuse under `public/assets/` |

### 2.4 Output

- Functional PNGs under `spa-app/public/icons/{story-handoff,user-cabinet,identity,public-home}/` (and planned `early-signal-dashboard/`).
- Docs sometimes updated (ON DISK, index row); commits only when operator ran git-commit methodology.

---

## 3. Contour B — Landing marketing assets + bug drop-ins (GenerateImage)

### 3.1 Input artifacts

- Gen list / runtime catalog: [`STORY-LAND-image-assets.md`](../../../../landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-assets.md)
- Style SSOT: [`STORY-LAND-image-style-prompts.md`](../../../../landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-style-prompts.md)
- Operator refs under `landing/docs/UX/references/` (character sheet, floral/skirt refs) and continuity mascots under `landing/src/assets/sections/...`
- Bug-wave path pin + paste prompts:
  - [`image-blockers-20260812.md`](../../../../landing/docs/tasks/run-reports/operator-waves/image-blockers-20260812.md)
  - [`image-blockers-20260812-gen-prompts.md`](../../../../landing/docs/tasks/run-reports/operator-waves/image-blockers-20260812-gen-prompts.md)

### 3.2 What the agent actually did

Observed pattern for illustrated / composite / ornament / head-avatar assets:

1. Read Shared lock + per-asset Depict (verbatim from gen-prompts or style_type + gen list).
2. Attach `reference_image_paths` (character / floral / existing mascot / mockup composition).
3. Call Cursor **GenerateImage**.
4. Copy to pinned `save_to` / Drop-in path (exact filename).
5. Often post-process with Pillow: knock near-white plate → real alpha; sometimes square crop/resize (e.g. head avatar).
6. Visual QA against checklist in Depict; reject/regen that slot only if needed.
7. Update operator Log `On disk?` when that was in scope; **Astro wire (T03+)** frequently stayed a separate blocked story phase.

### 3.3 Hybrid inside landing

Observed split:

| Kind | Method used |
|------|-------------|
| Trust / social UI glyphs | Lucide-like land pipeline (`npm run icons:land-ui`, land manifest) |
| Brand mark for landing logo | Adaptation from spa `DOGEstonia-logo-big.png` (Pillow), not AI redraw |
| Hero/CTA/examples/process/value scenes | GenerateImage + refs |
| BUG-15 / 17 / 20 drop-ins | GenerateImage + pinned `public/images/...` or `src/assets/brand/...` |

### 3.4 Output

- Production under `landing/src/assets/...` and/or pinned `landing/public/images/...`.
- Drop-in alone did **not** change live UI until builder wired imports (documented in image-blockers / bug stories).

---

## 4. Common agent loop (both contours)

As actually performed when the only product input was “catalog + prompts”:

```text
1. Read catalog → classify NEW / Reuse / Skip|Viz
2. Disk-check Reuse + refs (Pillow or ls)
3. Choose method by asset class (Lucide vs GenerateImage vs photo-ETM vs logo adapt)
4. Build executable step:
   - SPA: manifest row + icons:generate
   - Landing AI: Shared + Depict + reference_image_paths
5. Write to canonical path (never invent alternate filenames if catalog pinned one)
6. QA: exists, size/mode, alpha corners when required, visual vs Depict
7. Optional doc/log status; commit only after git-commit plan approval
```

Dedup rule used in practice (SPA): prefer catalog §Reuse and ICON-GENERATION-INDEX over “file missing on disk ⇒ regenerate.”

---

## 5. Style fencing (timeline note)

- Early SPA catalogs already described Lucide/Linear stroke language; landing catalogs used soft illustrated Shared locks.
- Mixing risks existed when the same agent handled both products.
- Later explicit SPA fence doc (2026-08-16): [`spa-app/docs/UX/SPA-ICON-STYLE-PROMPTS.md`](../../../../spa-app/docs/UX/SPA-ICON-STYLE-PROMPTS.md) — anti-landing Shared LOCK for functional icons.  
  **As-is claim:** that file documents the intended separation; it was **not** a prerequisite for the earlier Lucide and landing gen waves listed above.

---

## 6. What this retrospective is not

- Not a new operator contract or P3 appendix.
- Not instructions to change Lucide pipeline, landing gen-prompts, or ES generation.
- Not a claim that every catalog EN prompt was ever pasted into GenerateImage (SPA functional waves generally were not).

---

## 7. Pointers for readers who want “current” process

| Need | Where |
|------|--------|
| Must every UI story have an icon catalog? | [`tools/ui-story-icons-catalog.md`](../tools/ui-story-icons-catalog.md) |
| SPA UI DOM/mockup/puppeteer gates | [`guides/spa-ui-visual-pipeline.md`](../guides/spa-ui-visual-pipeline.md) |
| SPA generate commands / catalog index | [`ICON-GENERATION-INDEX.md`](../../../../spa-app/docs/tasks/backlog-stories/icons/ICON-GENERATION-INDEX.md) |
| SPA stroke Shared LOCK | [`SPA-ICON-STYLE-PROMPTS.md`](../../../../spa-app/docs/UX/SPA-ICON-STYLE-PROMPTS.md) |
| Landing style Shared LOCK | [`STORY-LAND-image-style-prompts.md`](../../../../landing/docs/tasks/backlog-stories/marketing-landing/STORY-LAND-image-style-prompts.md) |
