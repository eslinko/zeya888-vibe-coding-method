# Bridge — Zeya888 profile / tenancy bootstrap (dialog practice)

**dialogName:** `alvasar-gpt-profile-bootstrap` (filename stable; content = method-first)  
**bridgeScope:** `full`  
**Файл:** `docs/methodology/Zeya888-builder-queue/analysis/dialog-bridges/alvasar-gpt-profile-bootstrap-bridge.md`  
**Prompt SSOT:** [`../../prompts/migration/migration-dialog-context-bridge.md`](../../prompts/migration/migration-dialog-context-bridge.md) · **Output home:** [`README.md`](./README.md)  
**UTC foundation:** `2026-11-15T14:32:00Z` (re-check with `--print-utc-now` before new artifact dates)  
**Workspace:** `/Users/eslinko/Development/DOGEstonia`  
**Source dialog (transcript / agent store):** `f002f3d0-08b9-4e9d-8241-4bc30c1b0849`  
**Rules:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc) · [`.cursor/rules/builder-operator-habits.mdc`](../../../../../.cursor/rules/builder-operator-habits.mdc) · [`.cursor/rules/zeya888-operator-method.mdc`](../../../../../.cursor/rules/zeya888-operator-method.mdc)  
**Audience:** полностью чистый агент. Читать §0–§4 **до** instance §5–§7. Не сводить весь метод к Alvasar.

**Appendix:** ранний meta-ask «сделай bridge» в этом же диалоге породил prompt + output home; operative смысл диалога шире — **как поднимать профили и client tenancy в Zeya888 BQ**.

---

## 0. Как пользоваться

1. Прочитать Method map + Entry paths (§1–§4).
2. Прочитать Instance practice (§5–§7) — что уже сделано; **не** повторять.
3. Smoke §10 с диска.
4. Действовать по paste-packet §11 (режим A–E) или новому ask оператора.
5. **Name ≠ create** / ask-scoped delivery (`analysis.mdc`).
6. Method self-restore без диалоговой практики → [`migration-self-restore-zeya888-method.md`](../../prompts/migration/migration-self-restore-zeya888-method.md) (можно `@` рядом).

---

## 1. Method snapshot — Zeya888 Builder Queue

**Что это:** методология вайб-кодинга с жёстким контрактом оператор ↔ агент: Requirement/Epic/Story → immutable `pkg-*.yaml` → Build window → фазы **PA / P0–P8**. SSOT процесса не в памяти чата, а на диске.

**Роли (не смешивать в одном агенте без OP):**

| Роль | Фокус |
|------|--------|
| **OP** (orchestrator) | очередь, session, wave / subagent run |
| **BLD** (builder) | P3/P6 execute по pkg |
| **VAL** (validator) | P4/P7 audit, lightweight follow-up triage |

**Жёсткие правила мышления:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc) — только факты с диска; **ask-scoped** deliverable; **name ≠ create** (путь в REQ ≠ создать файл).

**Фиксированный runtime plan:** `@attach` `*_builder.plan.md` + workflow §P3/P6 — **не** Build/Execute на файле плана ([`guides/fixed-builder-plan-execution.md`](../../guides/fixed-builder-plan-execution.md)).

---

## 2. SSOT map (pointers — не копировать тела)

| Слой | Path |
|------|------|
| Manifest / что такое BQ | [`MANIFEST.md`](../../MANIFEST.md) |
| Phases PA/P0–P8 | [`core/workflow.md`](../../core/workflow.md) |
| Phase 0 / session | [`core/session-starter.md`](../../core/session-starter.md) |
| Profile registry | [`specs/profiles.yaml`](../../specs/profiles.yaml) · fields [`specs/profiles-fields.md`](../../specs/profiles-fields.md) |
| Client tenancy registry | [`specs/clients.yaml`](../../specs/clients.yaml) · guide [`guides/client-tenancy.md`](../../guides/client-tenancy.md) |
| Add profile checklist | [`guides/add-builder-profile.md`](../../guides/add-builder-profile.md) (§0 intake, §1 = 13 steps, §2 Gateway clone, §5 split) |
| Input packages | [`specs/input-package-spec.md`](../../specs/input-package-spec.md) |
| Intake pending/done | [`specs/profile-intakes/`](../../specs/profile-intakes/) |
| Operator contracts | [`contracts/`](../../contracts/) |
| Useful prompts index | [`prompts/INDEX.md`](../../prompts/INDEX.md) |
| Console UI | [`tools/workflow-console.html`](../../tools/workflow-console.html) |
| CLI | `python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project <key> --verify` |
| Curriculum connect | [`curriculum/05-connect-your-project.md`](../../curriculum/05-connect-your-project.md) |
| Method version (as of this dialog) | [`VERSION`](../../VERSION) = `1.4.64` · [`CHANGELOG.md`](../../CHANGELOG.md) |
| Builder session skill | [`.cursor/skills/builder-session/SKILL.md`](../../../../../.cursor/skills/builder-session/SKILL.md) |
| Structural plan etalon | [`.cursor/plans/Gateway_builder.plan.md`](../../../../../.cursor/plans/Gateway_builder.plan.md) |

---

## 3. Entry paths — как создавать / подключать профиль

Материализация = checklist в [`add-builder-profile.md`](../../guides/add-builder-profile.md) §1 (**не** дублировать 13 шагов здесь). Ниже — **какой prompt запускать**.

| Path | Когда | Launch |
|------|--------|--------|
| **A** | Intake YAML уже в `specs/profile-intakes/<key>.yaml` (не в `done/`) | [`migration-add-builder-profile.md`](../../prompts/migration/migration-add-builder-profile.md) + guide §1; plan-only until «запиши» |
| **B** | Папка уже в workspace **или** нужен `$git_repo` → clone в `$focus_folder`; intake ещё нет | [`migration-profile-from-checked-out-dir.md`](../../prompts/migration/migration-profile-from-checked-out-dir.md) (inspect → intake → затем A materialize) |
| **C** | Nested MS под `clients/<Client>/` (backend/ui/gpt/…) | [`client-tenancy.md`](../../guides/client-tenancy.md): `focus_folder` с `/`; `clients.yaml` + `CLIENT.yaml`; **dual** `.cursor/plans/*_builder.plan.md` (workspace + `clients/<Client>/.cursor/plans/`); tasks = `{focus}/docs/tasks` (не quirk GPT UI `docs/analysis/tasks` unless flat `gpt`) |
| **D** | Split от существующего профиля | intake `source_profile` / `source_split` + guide **§5 Split-from-existing**; пример эталон: `capybara` ← `scripts` |

**Derived defaults** (если не override): `tasks_dir={focus}/docs/tasks`, `plan_file=.cursor/plans/{TitleCase}_builder.plan.md`, packages/pointer/pipeline naming от `profile_key` — guide §0.

**После успешного verify:** intake → `specs/profile-intakes/done/`; bump `VERSION`/`CHANGELOG`; **не** Build на plan; **не** commit `docs/tasks/**` / methodology без явного приказа.

**Flat DOGE peers** (`gateway`, `gpt`/`GPT UI`, `identity`, `spa`, …) остаются в корне workspace — **не** переносить в `clients/`.

---

## 4. Client tenancy rules (кратко)

- `client_id` (напр. `alvasar`) ≠ `builder_project` (`alvasar-backend` / `alvasar-ui` / `alvasar-gpt`).
- Parent REQ: `clients/<Client>/docs/requirements/`; child REQ: `{focus}/docs/requirements/` when authored.
- Portable method: dual plans + `methodology/` pointers в client git ([client-tenancy.md](../../guides/client-tenancy.md)).
- Architect client root chat: [`prompts/architect/client-product-root-orientation.md`](../../prompts/architect/client-product-root-orientation.md) — не путать с DOGE classic-four orientation.

---

## 5. Instance practice — что отработал ЭТОТ диалог

| Wave | Что | Outcome |
|------|-----|---------|
| Multi-client tenancy B+C | guides/clients.yaml/training/anti-drift dual plans | Client model Present; DOGE flat peers untouched |
| `telegram` | Path B-ish (clone `doge-telegram`) + materialize | Profile `telegram`; method **1.4.63** |
| `alvasar-gpt` | Path C nested `clients/Alvasar/gpt`; skill как flat `gpt` | Profile `alvasar-gpt`; method **1.4.64**; client commit `b0bf056` pushed `dev` |
| Dialog-bridge SSOT | prompt `migration-dialog-context-bridge` + `analysis/dialog-bridges/` | Output home Present; this file |

Plan UI Apply (alvasar-gpt): `/Users/eslinko/.cursor/plans/alvasar_gpt_profile_e3e504e7.plan.md` — Apply done; **не** править без приказа.

---

## 6. Instance locked decisions + verified state

### 6.1 `alvasar-gpt` (последний profile bootstrap)

| Field | Value |
|-------|--------|
| `profile_key` | `alvasar-gpt` |
| `focus_folder` | `clients/Alvasar/gpt` |
| `tasks_dir` | `clients/Alvasar/gpt/docs/tasks` |
| Skill | `openai-custom-gpt-builder` (как GPT UI) |
| `test_command` | `cd clients/Alvasar/gpt && ls` |
| Stories | `STORY-ALVG-*` / `EPIC-ALVG-*` (target; none authored) |
| Active pkg | `pkg-000000-20261115-bootstrap.yaml` (t00 marker) |
| Instruction corpora | **Absent** (name ≠ create) |

### 6.2 `telegram` (prior in same dialog)

| Field | Value |
|-------|--------|
| `profile_key` | `telegram` |
| `focus_folder` | `doge-telegram` |
| Skill | `python-pro` |
| Boundary | channel → doge-ai-bridge `/v1/channel/*` only |

### 6.3 Re-verify (cold start)

```bash
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project alvasar-gpt --verify
# expect: ok 1 paths … pkg-000000-20261115-bootstrap.yaml

cat docs/methodology/Zeya888-builder-queue/VERSION   # 1.4.64
test -f docs/methodology/Zeya888-builder-queue/specs/profile-intakes/done/alvasar-gpt.yaml && echo intake=done
test ! -f clients/Alvasar/gpt/instructions.manifest.json && echo manifest_absent=ok
cd clients/Alvasar && git log -1 --oneline -- gpt/ CLIENT.yaml .cursor/plans/Alvasar-GPT_builder.plan.md
# expect: b0bf056 chore(gpt): bootstrap Builder Queue profile alvasar-gpt
```

Peers (cheap): `--project alvasar-ui --verify`, `--project telegram --verify`, `--project gpt --verify`.

---

## 7. File map (highlights)

### Method (workspace; methodology git commit for 1.4.64 — **не** делался в Apply-волне alvasar-gpt)

Present: `VERSION`/`CHANGELOG` 1.4.64 · `profiles.yaml` (`alvasar-gpt`, `telegram`, …) · `clients.yaml` · contracts · console · workflow/session-starter/queue-manual · `builder-session` / habits · `Alvasar-GPT_builder.plan.md` · `Telegram_builder.plan.md` · `prompts/migration/migration-dialog-context-bridge.md` · `analysis/dialog-bridges/`.

### Client `alvasar` (`dev`, pushed bootstrap gpt)

Present: `CLIENT.yaml` · `gpt/README.md` · `gpt/docs/tasks/**` (pkg-000000, bullrun, pipeline) · portable `Alvasar-GPT_builder.plan.md` · (also Present under gpt: `docs/requirements/01-questionnaire-instruction-pack.md` — REQ doc, **не** instruction body corpus).

### Explicitly Absent

- `clients/Alvasar/gpt/instructions.manifest.json` and instruction body `*.md` corpora  
- Product code changes for gpt bootstrap wave  
- Second checklist forked from `add-builder-profile.md`

---

## 8. Forbidden

- Повторять bootstrap `alvasar-gpt` / `telegram` при зелёном `--verify`.
- Создавать instruction corpora «под AC».
- Путать `builder_project: gpt` (GPT UI) с `alvasar-gpt`.
- Путать `client_id: alvasar` с profile keys.
- Класть nested client tasks в `docs/analysis/tasks` (quirk только flat `gpt`).
- Silent methodology / `docs/tasks/**` commit.
- Scope inflation / plan-over-ask (`analysis.mdc`).
- Копировать полный `workflow.md` в новые bridges вместо pointers.

---

## 9. How to launch next

### 9.A — Новый профиль Path A (intake already)

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/add-builder-profile.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-add-builder-profile.md
@docs/methodology/Zeya888-builder-queue/specs/profile-intakes/<profile_key>.yaml
@.cursor/plans/Gateway_builder.plan.md

$profile_key=
$focus_folder=
Migration: add Builder Queue profile from intake. Plan first; disk only on «запиши».
```

### 9.B — Path B (folder or clone)

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-profile-from-checked-out-dir.md
@docs/methodology/Zeya888-builder-queue/guides/add-builder-profile.md

$profile_key=
$focus_folder=
$git_repo=
$git_branch=dev
Migration: profile from checked-out dir or clone. Inspect → intake → materialize.
```

### 9.C — Path C (nested client MS)

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/client-tenancy.md
@docs/methodology/Zeya888-builder-queue/guides/add-builder-profile.md
@docs/methodology/Zeya888-builder-queue/specs/clients.yaml

$profile_key=
$focus_folder=clients/<Client>/<ms>
$client_id=
Migration: nested client MS profile. Dual plans + clients.yaml/CLIENT.yaml + tasks under focus/docs/tasks.
```

### 9.D — Continue Alvasar GPT product (не bootstrap)

Phase 0 + `builder_project: alvasar-gpt` · bullrun · contract · `gpt/README.md` · parent REQ14 §4.5 · **не** P3 на t00 · author `STORY-ALVG-*` only after explicit product ask · instruction bodies only on explicit create.

### 9.E — Methodology commit 1.4.64

Только по явному приказу; только method files; не тащить несвязанный dirty tree.

---

## 10. Smoke checklist

```bash
cd /Users/eslinko/Development/DOGEstonia
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
test -f docs/methodology/Zeya888-builder-queue/MANIFEST.md
test -f docs/methodology/Zeya888-builder-queue/guides/add-builder-profile.md
test -f docs/methodology/Zeya888-builder-queue/prompts/migration/migration-add-builder-profile.md
test -f docs/methodology/Zeya888-builder-queue/prompts/migration/migration-profile-from-checked-out-dir.md
test -f docs/methodology/Zeya888-builder-queue/guides/client-tenancy.md
test -f docs/methodology/Zeya888-builder-queue/prompts/migration/migration-dialog-context-bridge.md
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project alvasar-gpt --verify
python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --project alvasar-gpt --verify --check-dates
rg -n "^  alvasar-gpt:|^  telegram:" docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
test ! -f clients/Alvasar/gpt/instructions.manifest.json
```

---

## 11. Paste-packet — чистому агенту

```markdown
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/analysis/dialog-bridges/alvasar-gpt-profile-bootstrap-bridge.md
@docs/methodology/Zeya888-builder-queue/prompts/migration/migration-self-restore-zeya888-method.md

Ты чистый агент. bridgeScope=full.
1) Прочитай bridge §1–§4 (method + entry paths), затем §5–§7 (instance).
2) Выполни smoke §10; отрапортуй: VERSION / alvasar-gpt verify / intake done / manifest Absent / method prompt paths Present.
3) Не повторяй bootstrap alvasar-gpt / telegram.

Дальше — один режим по моей следующей строке (если нет — STOP и спроси):
A) Bootstrap NEW profile — Path A (intake already): $profile_key= $focus_folder=
B) Bootstrap NEW profile — Path B (folder/clone): $profile_key= $focus_folder= $git_repo=
C) Bootstrap NEW nested client MS — Path C: $client_id= $profile_key= $focus_folder=
D) Continue alvasar-gpt product (Phase 0 + next STORY/REQ proposal; no instruction bodies)
E) Methodology commit 1.4.64 (method files only)
F) Other: <ask>
```

---

## 12. Unknowns

- Когда materialize Alvasar instruction pack (manifest + bodies) — до явного приказа.
- Exact Alvasar env keys for instruction DIR/MANIFEST — lock later (gpt README).
- Methodology remote commit of `1.4.64` — ждать приказа.
- Нужен ли Path D split в ближайшей волне — Unknown.

---

## 13. End state one-liner

Method + entry paths A–D documented for cold agent; this dialog practiced multi-client tenancy, `telegram` (1.4.63), `alvasar-gpt` Path C (1.4.64, client `b0bf056` pushed), and dialog-bridges SSOT; instruction corpora remain Absent.
