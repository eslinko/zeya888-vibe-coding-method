# Migration — Zeya888-Brand landing infra transfer (1A)

**Категория:** migration (one-shot product scaffold under existing profile)  
**Profile:** `zeya888-brand` · focus `zeya888/`  
**Plan SSOT:** [`.cursor/plans/zeya888-brand_landing_infra_transfer.plan.md`](../../../../../.cursor/plans/zeya888-brand_landing_infra_transfer.plan.md)  
**Contract:** [`../../contracts/zeya888-brand-operator-contract.md`](../../contracts/zeya888-brand-operator-contract.md)  
**Claims:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Не путать** с `builder_project: zeya888` / focus `zeya888.me` (WordPress).

## Юзкейсы

| # | Ситуация | Действие |
|---|----------|----------|
| 1 | Фокусный чат `zeya888-brand` — перенести инфру landing (DS, секции, i18n) без NC | Copy-paste ниже → execute plan |
| 2 | Нужны локали en/et/ru + es/fr/de/is на static Astro | Следовать locks плана |
| 3 | `landing/` должен остаться параллельным продуктом | Hard ban: не менять `landing/` product |

**Scope lock:** только `builder_project: zeya888-brand` и paths под `zeya888/` (+ methodology profile gate updates named in the plan).  
**Out of scope:** node-customization / Volume; deprecate landing; invent final brand copy; Build on `Zeya888-Brand_builder.plan.md`.

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-zeya888-brand-landing-infra-transfer.md
@.cursor/plans/zeya888-brand_landing_infra_transfer.plan.md
@.cursor/plans/Zeya888-Brand_builder.plan.md
@docs/methodology/Zeya888-builder-queue/contracts/zeya888-brand-operator-contract.md
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml

builder_project: zeya888-brand
workspace_root: /Users/eslinko/Development/DOGEstonia
focus_folder: zeya888

Execute the transfer plan:
@.cursor/plans/zeya888-brand_landing_infra_transfer.plan.md

Locks (do not reopen):
- Scope 1A: Astro+Tailwind+DS+sections+i18n shell from landing → zeya888
- NO node-customization / Volume / NC schemas
- Parallel: do not change landing/ product
- Locales: en, et, ru, es, fr, de, is
- Astro output: static

Rules:
- Do NOT edit the transfer plan file itself
- Do NOT Build / Execute on Zeya888-Brand_builder.plan.md (attach-only)
- Do NOT invent final brand copy (placeholders OK for build)
- Do NOT commit/push unless I explicitly ask
- Todos from the plan are already created — mark in_progress as you go; complete all
- Claims: path-based (analysis.mdc)

Start with todo req-arch, then scaffold → UI/sections → i18n×7 → brand-strip → profile-gate → verify-build.
When done: report paths changed + `cd zeya888 && npm run build` result + `--project zeya888-brand --verify`.
```

---

## Примечания

- Profile bootstrap (`migration-add-builder-profile.md`) для `zeya888-brand` уже сделан — этот prompt **не** создаёт профиль заново.
- После scaffold: обновить `profiles.yaml` stack/`test_command` по плану (Astro + `npm run build`).
- Role restore для того же профиля: [`migration-role-bootstrap.md`](./migration-role-bootstrap.md) с `builder_project: zeya888-brand`.
