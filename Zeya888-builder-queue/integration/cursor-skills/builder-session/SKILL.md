---
name: builder-session
description: >-
  Zeya888 Builder Queue session workflow for gateway, GPT UI, doge-identity-service,
  spa-app, scripts (tooling), capybara (Vue+Node), landing (Astro), zeya888 (WordPress), arweave (Node/Arweave), dogestonia (RN/Expo), aibridge (Python Responses bridge), zeya888-brand (focus zeya888/), threads (focus doge-threads/), floou (focus Floou/), alvasar-backend / alvasar-ui / alvasar-gpt (nested clients/Alvasar/), telegram (focus doge-telegram/), amanita-bot / amanita-contracts / amanita-scripts / amanita-arweave (nested peer amanita/*, not clients.yaml), and other workspace projects. Use when the operator mentions builder_project,
  pkg-, build window, REQ-, EPIC-IDS-, STORY-SCR-, STORY-SCR-CAPY, STORY-LAND, STORY-AU, REQ-AU, STORY-DOGE, REQ-APP, STORY-AIBRIDGE, STORY-ZBRAND, REQ-01, builder_resolve_queue, bullrun,
  Gateway_builder, GPT_builder, ID_builder, Scripts_builder, Capybara_builder, Landing_builder, Arweave_builder, DOGEstonia_builder, aibridge_builder, Zeya888-Brand_builder, or starts a clean dev session.
  Triggers onboarding Phase 0 then P1-P8 from
  docs/methodology/Zeya888-builder-queue/core/workflow.md.
---

# Builder session

Full operator contract: [session-starter.md](../../../docs/methodology/Zeya888-builder-queue/core/session-starter.md).

## When to apply

- Work under a project in `profiles.yaml` (`doge-complaints-gateway`, `GPT UI`, `doge-identity-service`, `spa-app`, `scripts`, `capybara`, `landing`, `zeya888.me` / `zeya888`, `zeya888/` / `zeya888-brand`, `doge-threads/` / `threads`, `Floou/` / `floou`, `clients/Alvasar/backend` / `alvasar-backend`, `clients/Alvasar/ui` / `alvasar-ui`, `clients/Alvasar/gpt` / `alvasar-gpt`, `doge-telegram/` / `telegram`, `amanita/bot` / `amanita-bot`, `amanita/contracts` / `amanita-contracts`, `amanita/scripts` / `amanita-scripts`, `amanita/arweave-uploader` / `amanita-arweave`, `dogestonia-arweave-uploader` / `arweave`, `dogestonia-app` / `dogestonia`, `doge-ai-bridge` / `aibridge`, …).
- Operator set `builder_project: gateway|gpt|identity|spa|scripts|capybara|landing|zeya888|zeya888-brand|threads|floou|alvasar-backend|alvasar-ui|alvasar-gpt|telegram|amanita-bot|amanita-contracts|amanita-scripts|amanita-arweave|arweave|dogestonia|aibridge|…` or `pipeline_profile: builder_full`.
- **`identity`:** три входа P1 — `requirement` | `epic_story` | `backlog_story` (один на сессию) — [workflow.md](../../../docs/methodology/Zeya888-builder-queue/core/workflow.md) §P1.2/P1.1/P1.3 + **обязательный контракт:** [identity-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/identity-operator-contract.md). Runtime P3/P6 — @attach [.cursor/plans/ID_builder.plan.md](../../../.cursor/plans/ID_builder.plan.md) (не Build на файле; см. [fixed-builder-plan-execution.md](../../../docs/methodology/Zeya888-builder-queue/guides/fixed-builder-plan-execution.md)).
- **Fixed `*_builder.plan.md`:** @attach in the **current** project chat + workflow §P3/P6 — **not** Build / Execute plan on the file ([fixed-builder-plan-execution.md](../../../docs/methodology/Zeya888-builder-queue/guides/fixed-builder-plan-execution.md)).
- New chat / «старт сессии» — run **Phase 0** first (read code, docs, tests; no code changes).

## Phase 0 (mandatory if onboarding not done)

1. Load paths from [profiles.yaml](../../../docs/methodology/Zeya888-builder-queue/specs/profiles.yaml) for `builder_project`.
2. Confirm `focus_root`, git root, stack, tests (`test_command` in profile).
3. For `builder_full`: skim pipeline doc, bullrun index, `*-active-package.current.yaml`.
4. **Artifact dates:** before P1 scaffold / gate / run-summary — `--print-utc-now`; after scaffold — `--verify --check-dates`. SSOT: [builder-artifact-dates.md](../../../docs/methodology/Zeya888-builder-queue/guides/builder-artifact-dates.md).
5. Reply with **Onboarding summary** + **Ready for: P1|P2|P3|…** — wait for operator phase.

## Execution skill resolution

SSOT данных: [`profiles.yaml`](../../../docs/methodology/Zeya888-builder-queue/specs/profiles.yaml) — `execution_skill_primary`, `execution_skill_fallback` (опц.), `execution_skill_path`, `stack_label`.

**Два уровня skill:**
- **builder-session** (этот файл) — процесс pkg, verify, фазы P1–P8; один для всех проектов.
- **execution skill** — языковой/доменный эксперт (`python-pro`, `react-expert`, …); отдельный SKILL.md, подгружается при декомпозиции и правках кода.

### Алгоритм

1. **Phase 0:** прочитать profile по `builder_project` → в Onboarding summary обязательно:  
   `Execution skill: <execution_skill_primary> (@<execution_skill_path>)`; если есть `execution_skill_fallback` — указать fallback slug.
2. **P1 (decompose):** в каждом task README: `Skill declared: <execution_skill_primary>` (или fallback, если оператор явно указал).
3. **P3/P6 (execute):** перед правками кода — прочитать `@<execution_skill_path>` из profile; если в **текущем** task README другой `Skill declared` — **побеждает README таска**.
4. **Запрет:** не предлагать `python-pro` для `spa` / `scripts` / `react-expert` для `gateway` без явной команды оператора.

P1.3 epic/task naming по проекту — operator contract §6/§7 (`spa` / `identity` / `scripts` / `capybara` / `landing` / `zeya888` / `arweave` / `dogestonia` / `aibridge` / `zeya888-brand` / `threads` / `floou` / `alvasar-backend` / `alvasar-ui` / `alvasar-gpt` / `telegram` / `amanita-bot` / `amanita-contracts` / `amanita-scripts` / `amanita-arweave`), не дублировать здесь.

## Pipeline phases (operator picks one)

SSOT prompts: [workflow.md](../../../docs/methodology/Zeya888-builder-queue/core/workflow.md).

| Phase | Agent mode |
|-------|------------|
| P1 | Plan — decompose requirement **or epic** (`identity`); task-standard; analysis.mdc |
| P2 | Build window — `$verifyCmd` + `--write-build-window` → `$buildWindowFile` (`build_window_file:` / `cursor_attach:` в stdout) |
| P3/P6 | Execute — `*_builder.plan` + `@$buildWindowFile`; step 0 `--verify`; bullrun-start + run-task |
| P4/P7 | Audit — fact report in `docs/analysis/`; **P4b/P7b** — Claude external cross-audit (`identity`) |
| P5 | **Scaffold only** — gap tasks + index + plan override; **do not implement** |
| P8 | Commits per [git-commit.md](../../../docs/methodology/git-commit.md); no push unless asked |

## Gateway (`builder_project: gateway`)

Перед batch-run / P3/P6 — [gateway-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/gateway-operator-contract.md):

1. **Index + pkg** — `bullrun-launch-index.md` §«Актуальная точка» + `gateway-active-package.current.yaml` + `--verify`; стартовый эпик только из индекса.
2. **Missing epic** — `EPIC-M2-*` без task queue в индексе → не декомпозирован → P1 + `bullrun-epic-decompose`.
3. **Sync index** — после каждого закрытого task/story обновлять индекс в той же итерации.
4. **`run_mode`** — audit override (`gw_l10n_01_audit_followup`, …) только по явной команде; не менять active pkg.
5. Runtime P3/P6 — [.cursor/plans/Gateway_builder.plan.md](../../../.cursor/plans/Gateway_builder.plan.md).

## GPT (`builder_project: gpt`)

Перед batch-run / P3/P6 — [gpt-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/gpt-operator-contract.md):

1. **Index + pkg** — `bullrun-launch-index.md` + `gpt-active-package.current.yaml` + `--verify`; не выдумывать порядок вне `--list` / индекса.
2. **Missing epic** — `EPIC-M1-*` без task queue в индексе → не декомпозирован → P1 + `bullrun-epic-decompose`.
3. **Sync index** — после каждого закрытого task/story обновлять индекс в той же итерации.
4. **`run_mode`** — audit override (`req36_audit_followup`, `req33_audit_followup`, …) только по явной команде; не менять active pkg.

## Identity (`builder_project: identity`)

Перед batch-run / P3 — [identity-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/identity-operator-contract.md):

1. **Index + pkg** — `bullrun-launch-index.md` + `identity-active-package.current.yaml` + `--verify`; не выдумывать `EPIC-IDS-*` вне `docs/tasks/epics/`.
2. **Missing epic** — файл эпика без task queue в индексе → не декомпозирован → P1 + `bullrun-epic-decompose`.
3. **Sync index** — после каждого закрытого task/story обновлять индекс в той же итерации.
4. **`input_mode`** — оператор явно: `epic_story` | `requirement` | `run_mode=…`; не смешивать без решения.

## Spa (`builder_project: spa`)

Перед batch-run / P3 — [spa-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/spa-operator-contract.md):

1. **Index + pkg** — `bullrun-launch-index.md` + `spa-active-package.current.yaml` + `--verify`; до первого P1 ожидаемо FAIL (bootstrap).
2. **Primary intake** — **P1.3** `backlog_story` из `backlog-stories/STORY-SPA-*.md`; опционально **PA.3** shaping.
3. **Sync index** — после каждого закрытого task/story обновлять bullrun + `backlog-stories/INDEX.md`.
4. **Два трека** — doc-gap backlog (primary) vs legacy `EPIC-DASH-01` / DASH-P*; не смешивать без решения оператора.
5. Runtime P3/P6 — [.cursor/plans/Spa_builder.plan.md](../../../.cursor/plans/Spa_builder.plan.md).

## Scripts (`builder_project: scripts`)

Перед batch-run / P3 — [scripts-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/scripts-operator-contract.md):

1. **Scope** — только `EPIC-SCR-02-tooling` / `STORY-SCR-WFCONSOLE*`; capybara work → profile `capybara`.
2. **Index + pkg** — `scripts/docs/tasks/bullrun-launch-index.md` + `scripts-active-package.current.yaml` + `--verify`.
3. Runtime P3/P6 — @attach [.cursor/plans/Scripts_builder.plan.md](../../../.cursor/plans/Scripts_builder.plan.md).

## Capybara (`builder_project: capybara`)

Перед batch-run / P3 — [capybara-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/capybara-operator-contract.md):

1. **Index + pkg** — `capybara/docs/tasks/bullrun-launch-index.md` + `capybara-active-package.current.yaml` + `--verify`.
2. **Primary intake** — **P1.3** `STORY-SCR-CAPY*` / `STORY-SCR-CAPYUI*`; shaping из `scripts/docs/runtime-infrastructure/`.
3. **Stack** — Vue 3 + Node monolith (`capybara-ui/`) + CLI (`scripts/lib/capybara/`); skills `vue-expert` / `javascript-pro`.
4. **Cross-profile** — не вести capybara через `builder_project: scripts`.

## Landing (`builder_project: landing`)

Перед batch-run / P3 — [landing-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/landing-operator-contract.md):

1. **Index + pkg** — `landing/docs/tasks/bullrun-launch-index.md` + `landing-active-package.current.yaml` + `--verify`.
2. **Primary intake** — **P1.1** epic from living `bullrun-landing-index.md` / `epics/epic-0N-*`; optional P1.3 `STORY-LAND-*`.
3. **Stack** — Astro + TypeScript + Tailwind; skill `typescript-pro` / fallback `javascript-pro`.
4. **Do not** execute raw `story.md` without materialized task README + pkg.
5. **Runtime P3/P6** — @attach `.cursor/plans/Landing_builder.plan.md` (не Build на файле).
6. New profile SSOT — [add-builder-profile.md](../../../docs/methodology/Zeya888-builder-queue/guides/add-builder-profile.md).

## Zeya888 (`builder_project: zeya888`)

Перед batch-run / P3 — [zeya888-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/zeya888-operator-contract.md):

1. **Index + pkg** — `zeya888.me/docs/tasks/bullrun-launch-index.md` + `zeya888-active-package.current.yaml` + `--verify`.
2. **Primary intake** — **P1.3** `STORY-ZEYA-BUG-*` (schema + audit); **не** invent stories; **не** exploit/PoC.
3. **Stack** — WordPress (PHP) in `zeya888.me/`; skill `wordpress-pro` / fallback `php-pro`.
4. **Bootstrap marker t00** — methodology only; product next = author stories → P1.3.
5. **Runtime P3/P6** — @attach `.cursor/plans/Zeya888_builder.plan.md` (не Build на файле).
6. **Dashboard recount** after emit/close (`zeya888-mvp-dashboard.md`).

## Arweave (`builder_project: arweave`)

Перед batch-run / P3 — [arweave-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/arweave-operator-contract.md):

1. **Index + pkg** — `dogestonia-arweave-uploader/docs/tasks/bullrun-launch-index.md` + `arweave-active-package.current.yaml` + `--verify`.
2. **Primary intake** — **P1.3** `STORY-AU-*` или **requirement** `REQ-AU-*` (один режим на сессию); **не** invent stories.
3. **Stack** — Node.js (Arweave / cryptography) in `dogestonia-arweave-uploader/`; skill `javascript-pro`.
4. **Bootstrap marker t00** — methodology only; product next = author stories / REQ shaping → P1.
5. **Runtime P3/P6** — @attach `.cursor/plans/Arweave_builder.plan.md` (не Build на файле).

## DOGEstonia (`builder_project: dogestonia`)

Перед batch-run / P3 — [dogestonia-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/dogestonia-operator-contract.md):

1. **Index + pkg** — `dogestonia-app/docs/tasks/bullrun-launch-index.md` + `dogestonia-active-package.current.yaml` + `--verify`.
2. **Primary intake** — **P1.1** epic / **P1.3** `STORY-DOGE-*` / **requirement** `REQ-APP-*` (один режим); **не** invent.
3. **Stack** — React Native (Expo) iOS/Android/web in `dogestonia-app/`; skill `react-native-expert` / fallback `react-expert`.
4. **UX** — `hasUxPipeline: true`; UI-0..UI-3 = [spa-ui-visual-pipeline.md](../../../docs/methodology/Zeya888-builder-queue/guides/spa-ui-visual-pipeline.md).
5. **Bootstrap marker t00** — methodology only; product next = author epic/story → P1.
6. **Runtime P3/P6** — @attach `.cursor/plans/DOGEstonia_builder.plan.md` (не Build на файле).

## AI Bridge (`builder_project: aibridge`)

Перед batch-run / P3 — [aibridge-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/aibridge-operator-contract.md):

1. **Index + pkg** — `doge-ai-bridge/docs/tasks/bullrun-launch-index.md` + `aibridge-active-package.current.yaml` + `--verify`.
2. **Primary intake** — `requirement` REQ-01 или P1.3 `STORY-AIBRIDGE-*` (не смешивать с `gpt`).
3. **Stack** — Python in `doge-ai-bridge/`; skill `python-pro`.
4. **Runtime P3/P6** — @attach `.cursor/plans/aibridge_builder.plan.md` (не Build на файле).

## Zeya888-Brand (`builder_project: zeya888-brand`)

Перед batch-run / P3 — [zeya888-brand-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/zeya888-brand-operator-contract.md):

1. **Index + pkg** — `zeya888/docs/tasks/bullrun-launch-index.md` + `zeya888-brand-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-ZBRAND-*` (не invent).
3. **Stack** — Astro + TypeScript + Tailwind in `zeya888/`; skill `typescript-pro` / fallback `javascript-pro`.
4. **Не путать** с `builder_project: zeya888` / `zeya888.me`.
5. **Runtime P3/P6** — @attach `.cursor/plans/Zeya888-Brand_builder.plan.md` (не Build на файле).

## Threads (`builder_project: threads`)

Перед batch-run / P3 — [threads-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/threads-operator-contract.md):

1. **Index + pkg** — `doge-threads/docs/tasks/bullrun-launch-index.md` + `threads-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-THREADS-*` (не invent).
3. **Stack** — Python 3.11 + FastAPI + uvicorn + httpx; skill `python-pro`.
4. **Alias ≠ folder** — `threads` → `doge-threads/`.
5. **Runtime P3/P6** — @attach `.cursor/plans/Threads_builder.plan.md` (не Build на файле).

## Floou (`builder_project: floou`)

Перед batch-run / P3 — [floou-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/floou-operator-contract.md):

1. **Index + pkg** — `Floou/docs/tasks/bullrun-launch-index.md` + `floou-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-FLOOU-*` (не invent).
3. **Stack** — Solidity (LSP7 token); skill `solidity-auditor`.
4. **Alias ≠ folder** — `floou` → `Floou/`.
5. **Runtime P3/P6** — @attach `.cursor/plans/Floou_builder.plan.md` (не Build на файле).

## Alvasar backend (`builder_project: alvasar-backend`)

Перед batch-run / P3 — [alvasar-backend-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/alvasar-backend-operator-contract.md):

1. **Index + pkg** — `clients/Alvasar/backend/docs/tasks/bullrun-launch-index.md` + `alvasar-backend-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-ALVB-*` (не invent).
3. **Stack** — Python API (scaffold deferred); skill `python-pro`.
4. **Nested focus** — `clients/Alvasar/backend/` ([client-tenancy.md](../../../docs/methodology/Zeya888-builder-queue/guides/client-tenancy.md)).
5. **Runtime P3/P6** — @attach `.cursor/plans/Alvasar-Backend_builder.plan.md` (portable copy under `clients/Alvasar/.cursor/plans/`).

## Alvasar UI (`builder_project: alvasar-ui`)

Перед batch-run / P3 — [alvasar-ui-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/alvasar-ui-operator-contract.md):

1. **Index + pkg** — `clients/Alvasar/ui/docs/tasks/bullrun-launch-index.md` + `alvasar-ui-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-ALVU-*` (не invent).
3. **Stack** — React Native Web (scaffold deferred); skill `react-native-expert`; **hasUxPipeline** false.
4. **Nested focus** — `clients/Alvasar/ui/`.
5. **Runtime P3/P6** — @attach `.cursor/plans/Alvasar-UI_builder.plan.md` (portable copy under `clients/Alvasar/.cursor/plans/`).

## Alvasar GPT (`builder_project: alvasar-gpt`)

Перед batch-run / P3 — [alvasar-gpt-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/alvasar-gpt-operator-contract.md):

1. **Index + pkg** — `clients/Alvasar/gpt/docs/tasks/bullrun-launch-index.md` + `alvasar-gpt-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-ALVG-*` (не invent).
3. **Stack** — GPT Instructions; skill `openai-custom-gpt-builder` (same as flat `gpt` / GPT UI); **hasUxPipeline** false.
4. **Nested focus** — `clients/Alvasar/gpt/` (instruction pack authorship; name ≠ create bodies).
5. **Runtime P3/P6** — @attach `.cursor/plans/Alvasar-GPT_builder.plan.md` (portable copy under `clients/Alvasar/.cursor/plans/`).

## Telegram (`builder_project: telegram`)

Перед batch-run / P3 — [telegram-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/telegram-operator-contract.md):

1. **Index + pkg** — `doge-telegram/docs/tasks/bullrun-launch-index.md` + `telegram-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-TELEGRAM-*` (не invent).
3. **Stack** — Python Telegram transport → doge-ai-bridge `/v1/channel/*`; skill `python-pro`; no model keys in this focus.
4. **Focus** — `doge-telegram/` (product doge-telegram-channel).
5. **Runtime P3/P6** — @attach `.cursor/plans/Telegram_builder.plan.md`.


## Amanita Bot (`builder_project: amanita-bot`)

Перед batch-run / P3 — [amanita-bot-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/amanita-bot-operator-contract.md):

1. **Index + pkg** — `amanita/bot/docs/tasks/bullrun-launch-index.md` + `amanita-bot-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-AMBOT-*` (не invent).
3. **Stack** — skill `python-pro`.
4. **Nested peer** — `amanita/bot/` (**not** `clients.yaml` / Root card; ≠ flat `scripts`/`arweave` keys).
5. **Runtime P3/P6** — @attach `.cursor/plans/Amanita-Bot_builder.plan.md` (не Build на файле).

## Amanita Contracts (`builder_project: amanita-contracts`)

Перед batch-run / P3 — [amanita-contracts-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/amanita-contracts-operator-contract.md):

1. **Index + pkg** — `amanita/contracts/docs/tasks/bullrun-launch-index.md` + `amanita-contracts-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-AMCTR-*` (не invent).
3. **Stack** — skill `solidity-auditor`.
4. **Nested peer** — `amanita/contracts/` (**not** `clients.yaml` / Root card; ≠ flat `scripts`/`arweave` keys).
5. **Runtime P3/P6** — @attach `.cursor/plans/Amanita-Contracts_builder.plan.md` (не Build на файле).

## Amanita Scripts (`builder_project: amanita-scripts`)

Перед batch-run / P3 — [amanita-scripts-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/amanita-scripts-operator-contract.md):

1. **Index + pkg** — `amanita/scripts/docs/tasks/bullrun-launch-index.md` + `amanita-scripts-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-AMSCR-*` (не invent).
3. **Stack** — skill `javascript-pro`.
4. **Nested peer** — `amanita/scripts/` (**not** `clients.yaml` / Root card; ≠ flat `scripts`/`arweave` keys).
5. **Runtime P3/P6** — @attach `.cursor/plans/Amanita-Scripts_builder.plan.md` (не Build на файле).

## Amanita Arweave (`builder_project: amanita-arweave`)

Перед batch-run / P3 — [amanita-arweave-operator-contract.md](../../../docs/methodology/Zeya888-builder-queue/contracts/amanita-arweave-operator-contract.md):

1. **Index + pkg** — `amanita/arweave-uploader/docs/tasks/bullrun-launch-index.md` + `amanita-arweave-active-package.current.yaml` + `--verify`.
2. **Primary intake** — P1.3 `STORY-AMARW-*` (не invent).
3. **Stack** — skill `javascript-pro`.
4. **Nested peer** — `amanita/arweave-uploader/` (**not** `clients.yaml` / Root card; ≠ flat `scripts`/`arweave` keys).
5. **Runtime P3/P6** — @attach `.cursor/plans/Amanita-Arweave_builder.plan.md` (не Build на файле).

## Hard rules

- **analysis.mdc** — every claim cites a file path.
- **Before Build:** from workspace root:
  `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project <builder_project> --verify`
  Stop on FAIL.
- **Artifact dates (P1/P3):** never invent dates — run `--print-utc-now` before writing pkg/gate/run-summary; after P1 scaffold and before story Done run `--verify --check-dates` (stop on FAIL).
- **YAML default** — active `pkg-*.yaml`; `run_mode=…` only when operator explicitly requests.
- **Do not edit** `.cursor/plans/*.plan.md` unless operator asks. При правке `GPT_builder.plan.md` после изменений в `Gateway_builder.plan.md` — сверка [`gpt-vs-gateway-builder-plan-gaps.md`](../../../docs/methodology/Zeya888-builder-queue/archive/gpt-vs-gateway-plan-gaps.md).
- **Commits** — exclude `docs/tasks/**`, BULLRUN, acceptance-verification, run-summary by default.

## SSOT order (conflicts)

1. Active `pkg-*.yaml` queue  
2. `bullrun-launch-index.md`  
3. Decision / interview requirements  
4. Task README + acceptance-verification

## Related role skills (not this file)

- OP routing → [`orchestrator`](../orchestrator/SKILL.md)  
- VAL audit → [`validator`](../validator/SKILL.md)  
- Method-ops root → [`Zeya888`](../zeya888/SKILL.md)

## References

- [queue-manual.md](../../../docs/methodology/Zeya888-builder-queue/cli/queue-manual.md)
- [input-package-spec.md](../../../docs/methodology/Zeya888-builder-queue/specs/input-package-spec.md)
- [gpt-vs-gateway-builder-plan-gaps.md](../../../docs/methodology/Zeya888-builder-queue/archive/gpt-vs-gateway-plan-gaps.md) (GPT plan vs Gateway)
