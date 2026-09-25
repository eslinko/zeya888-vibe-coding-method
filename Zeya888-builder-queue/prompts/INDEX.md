# Useful prompts — index

Каталог **копируемых** промптов вне happy-path PA/P*. Curriculum и contracts **не** дублируют текст промптов — только ссылки сюда или в `core/workflow.md`.

## Taxonomy

| Категория | Когда | Где |
|-----------|-------|-----|
| **architect/** | До PA / cross-project analytics / system map | [`architect/`](./architect/) |
| **operator/** | Root OP bootstrap / wave / subagent overnight | [`operator/`](./operator/) |
| **migration/** | Быстрый restore контекста роли (BLD/VAL/OP) по `builder_project` | [`migration/`](./migration/) |
| **training/** | Training dialogues (teaching; not operative) | [`training/`](./training/) |
| **operator-wave** | P0–P8 + PA.1–PA.3 happy path fences | SSOT: [`../core/workflow.md`](../core/workflow.md) (не мигрировать сюда без явного решения) |
| **housekeeping** | Dashboard focus, git commit plan | см. таблицу ниже |

## architect/

| Prompt | Назначение |
|--------|------------|
| [`architect/cross-project-system-orientation.md`](./architect/cross-project-system-orientation.md) | Read-only STOP: карта 4 проектов + docs analytics + candidates in chat; без PA/P1 handoff |
| [`architect/cross-project-requirements-backlog-bootstrap.md`](./architect/cross-project-requirements-backlog-bootstrap.md) | Стартовый lock чата: аналитика parent REQ из `docs/requirements backlog/` across gateway/identity/spa/gpt; без pkg/P3 |
| [`architect/parent-requirement-to-project-reqs.md`](./architect/parent-requirement-to-project-reqs.md) | Parent → child REQs + link matrix; materialize + mvp-dashboard sync → PA.2 |
| [`architect/cross-project-req-scatter.md`](./architect/cross-project-req-scatter.md) | Parent → child REQs в `{project}/docs/requirements/` (write after impact; Parent/Siblings; без STORY/pkg) |
| [`architect/cross-project-req-consistency-audit.md`](./architect/cross-project-req-consistency-audit.md) | Чистый диалог: аудит parent+child REQ vs операторская цель; реализуемость; отчёт в `docs/analysis/`; обязательный доспрос |
| [`architect/target-tech-architecture.md`](./architect/target-tech-architecture.md) | REQ and/or story package/list → целевая tech-архитектура фокуса (+ interview); packaging — пакет тем |
| [`architect/decision-point-human-language.md`](./architect/decision-point-human-language.md) | Companion: ОЯЗ-разбор вариантов Decision-point + ethics/architecture fit + advisory recommend |
| [`architect/req-to-backlog-stories.md`](./architect/req-to-backlog-stories.md) | Non-UI REQ → STORY package (reuse\|new); INDEX + mvp-dashboard sync → P1.3 |
| [`architect/req-to-ui-admin-layers.md`](./architect/req-to-ui-admin-layers.md) | UI REQ → ADMIN-01…06 (always NEW pkg); INDEX + mvp-dashboard sync; STORY via ADMIN-05 |
| [`architect/req-to-frontend-mixed-package.md`](./architect/req-to-frontend-mixed-package.md) | FE mixed REQ → classify ui_first/tech_first; ADMIN projected + STORY in one NEW pkg |

**Human guide (EN):** [`../guides/from-cross-project-req-to-story-packages.md`](../guides/from-cross-project-req-to-story-packages.md) — sequence parent → child REQ → tech arch → STORY/ADMIN. REQ7 ready fences (RU): [`../../../requirements backlog/REQ7-architect-copy-paste-process.md`](../../../requirements%20backlog/REQ7-architect-copy-paste-process.md).

## operator/

| Prompt | Назначение |
|--------|------------|
| [`operator/operator-root-start.md`](./operator/operator-root-start.md) | OP chat: только `$builderProject=` → role + session bind (reuse\|create\|task) |
| [`operator/operator-root-wave.md`](./operator/operator-root-wave.md) | OP chat: story links → wave MD + handoff packets для BLD/VAL/CLI (MVP paste) |
| [`operator/operator-root-subagent-run.md`](./operator/operator-root-subagent-run.md) | OP chat: `$builderProject` + `$queueSpec` → новый `.cursor/plans/OP-…plan.md` (transpose эталона) + два субагента overnight |
| [`operator/operator-identity-harvest.md`](./operator/operator-identity-harvest.md) | Универсальный harvest фокусных диалогов → evidence/dedup patch в `builder-operator-habits.mdc` |
| [`operator/lightweight-followup-triage.md`](./operator/lightweight-followup-triage.md) | VAL: complexity gate PASS\|ESCALATE для low-complexity follow-up (no STORY) |
| [`operator/lightweight-followup-author.md`](./operator/lightweight-followup-author.md) | После triage PASS: dual plans + LAUNCH (+ thin Task); BLD implement → VAL validate |

## migration/

| Prompt | Назначение |
|--------|------------|
| [`migration/migration-role-bootstrap.md`](./migration/migration-role-bootstrap.md) | Универсальный restore prompt: `builder_project` + `focus_role` (`builder|validator|orchestrator`) |
| [`migration/migration-builder.md`](./migration/migration-builder.md) | Role wrapper для быстрого BLD bootstrap |
| [`migration/migration-validator.md`](./migration/migration-validator.md) | Role wrapper для быстрого VAL bootstrap |
| [`migration/migration-orchestrator.md`](./migration/migration-orchestrator.md) | Role wrapper для быстрого OP bootstrap |
| [`migration/migration-self-restore-zeya888-method.md`](./migration/migration-self-restore-zeya888-method.md) | Self-restore контекста метода Zeya888: что это, зачем, где SSOT, как работать в роли/проекте |
| [`migration/migration-spa-images-generation-bootstrap.md`](./migration/migration-spa-images-generation-bootstrap.md) | Универсальный SPA-only bootstrap для Images generation: catalog classify + Contour A Lucide + Contour B mascot GenerateImage |
| [`migration/migration-landing-images-generation-bootstrap.md`](./migration/migration-landing-images-generation-bootstrap.md) | Универсальный landing-only bootstrap для Images generation: Contour A `icons:land-ui` + Contour B style-locked GenerateImage/crop_or_ai |
| [`migration/migration-add-builder-profile.md`](./migration/migration-add-builder-profile.md) | Intake `profile_key`+`focus_folder` → bootstrap профиля с нуля (profiles.yaml, console, tasks SSOT, Gateway clone) |
| [`migration/migration-profile-from-checked-out-dir.md`](./migration/migration-profile-from-checked-out-dir.md) | Папка уже в workspace → inspect → intake → materialize (wrapper над add-builder-profile) |
| [`migration/migration-zeya888-brand-landing-infra-transfer.md`](./migration/migration-zeya888-brand-landing-infra-transfer.md) | `zeya888-brand`: перенос инфры landing→`zeya888` (1A, static, 7 locales, no NC); plan attach |
| [`migration/migration-zeya888-brand-doge-content-strip.md`](./migration/migration-zeya888-brand-doge-content-strip.md) | `zeya888-brand`: убрать landing/DOGEstonia copy+photos из `zeya888/src`; PNG stubs + `[TODO]` JSON; plan attach |

## training/

| Prompt | Purpose |
|--------|---------|
| [`training/INDEX.md`](./training/INDEX.md) | Dialog order, routes A/B, transition rules |
| [`training/01-how-the-system-works.md`](./training/01-how-the-system-works.md) | Training: how the system works |
| [`training/02-how-the-operator-steers.md`](./training/02-how-the-operator-steers.md) | Training: steering a wave |
| [`training/03a-connect-your-project-tech.md`](./training/03a-connect-your-project-tech.md) | Tech: project adaptation plan |
| [`training/03b-project-brief-fintech.md`](./training/03b-project-brief-fintech.md) | Fintech: brief for guided adoption |
| [`training/04a-first-managed-work-session.md`](./training/04a-first-managed-work-session.md) | Tech: first managed session |

## operator-wave

Короткие fences: [`../core/workflow.md`](../core/workflow.md). Полные: [`../core/workflow-legacy.md`](../core/workflow-legacy.md). UI copy: [`../tools/workflow-console.html`](../tools/workflow-console.html).

## housekeeping/

| Prompt | Назначение |
|--------|------------|
| [`../workflow/build-scope-dashboard-prompt.md`](../workflow/build-scope-dashboard-prompt.md) | Focus-диалог Layer-2 backlog dashboard (`/build-scope-dashboard`) |
| [`../../git-commit-prompt.md`](../../git-commit-prompt.md) | План коммитов на согласование (корневая methodology) |

## SSOT rules

1. Новые useful prompts **вне** PA/P* → `prompts/<category>/` + строка в этой INDEX.
2. Изменение PA/P* → править `core/workflow.md` (+ console, если fence).
3. Не копировать полный текст промпта в curriculum / operator contracts — thin pointer only.
