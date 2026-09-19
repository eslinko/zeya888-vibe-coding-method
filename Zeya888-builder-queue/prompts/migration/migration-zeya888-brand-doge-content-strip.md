# Migration — Zeya888-Brand strip foreign (DOGEstonia/landing) content

**Категория:** migration (one-shot cleanup under existing profile)  
**Profile:** `zeya888-brand` · focus `zeya888/`  
**Plan SSOT:** [`.cursor/plans/zeya888-brand_doge-content-strip.plan.md`](../../../../../.cursor/plans/zeya888-brand_doge-content-strip.plan.md)  
**Contract:** [`../../contracts/zeya888-brand-operator-contract.md`](../../contracts/zeya888-brand-operator-contract.md)  
**Claims:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Не путать** с `builder_project: zeya888` / focus `zeya888.me` (WordPress).

После 1A (`migration-zeya888-brand-landing-infra-transfer.md`) в `zeya888/src` остались фото и копирайт landing. Эта волна меняет **значения и байты файлов**, не схему компонентов.

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | Нужно убрать контент другого проекта из `zeya888/` | Copy-paste ниже → execute plan |
| 2 | Лейаут может разъехаться | Ожидаемо: заглушки PNG + короткие `[TODO locale]` строки |
| 3 | `landing/` параллельный продукт | Не менять `landing/` |

**Scope lock:** `builder_project: zeya888-brand`, правки под `zeya888/src/**` + thin REQ + analysis note.  
**Out of scope:** финальный бренд; invent `STORY-ZBRAND-*`; NC; Build на `Zeya888-Brand_builder.plan.md`.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-zeya888-brand-doge-content-strip.md
@.cursor/plans/zeya888-brand_doge-content-strip.plan.md
@.cursor/plans/Zeya888-Brand_builder.plan.md
@docs/methodology/Zeya888-builder-queue/contracts/zeya888-brand-operator-contract.md
@zeya888/docs/analysis/zeya888-brand-landing-infra-transfer-validation-2026-09-18.md

builder_project: zeya888-brand
workspace_root: /Users/eslinko/Development/DOGEstonia
focus_folder: zeya888

Execute the content-strip plan:
@.cursor/plans/zeya888-brand_doge-content-strip.plan.md

Locks (do not reopen):
- Runtime zeya888/src must not keep DOGEstonia/landing product copy or photos
- Keep JSON keys and array lengths (LandingCopy)
- Placeholder strings and stub PNGs of the same filenames are OK
- Layout will change — expected
- Do not invent final brand copy
- Do not change landing/
- Do not invent STORY-ZBRAND-*
- NO node-customization

Rules:
- Do NOT edit the plan file itself except todo status in_progress/completed
- Do NOT Build / Execute on Zeya888-Brand_builder.plan.md (attach-only)
- Do NOT commit/push unless I explicitly ask
- Todos from the plan are already created — mark in_progress as you go; complete all
- Claims: path-based (analysis.mdc)

Start with todo req-note, then stub-assets → placeholder-copy → strip-src-comments → verify-build.
When done: report paths changed + `cd zeya888 && npm run build` + `--project zeya888-brand --verify` + grep result under zeya888/src.
```

---

## Примечания

- 1A transfer уже на диске; этот prompt **не** повторяет scaffold Astro.
- Role restore: [`migration-role-bootstrap.md`](./migration-role-bootstrap.md) с `builder_project: zeya888-brand`.
