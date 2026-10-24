# Client product root orientation

**Категория:** architect (pre-PA) — **client tenancy**, not DOGE classic-four  
**Не заменяет:** [`cross-project-system-orientation.md`](./cross-project-system-orientation.md) (DOGEstonia four apps) · PA.1–PA.3 / P1.x in [`../../core/workflow.md`](../../core/workflow.md)  
**Model SSOT:** [`../../guides/client-tenancy.md`](../../guides/client-tenancy.md) · [`../../specs/clients.yaml`](../../specs/clients.yaml)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc) — только verified claims; name ≠ create app scaffold

**Когда:** нужен root / «кросс-MS» диалог по **одному клиенту** под `clients/<Client>/` (parent REQ, границы backend/ui, следующий шаг architect) — без карты gateway/identity/spa/gpt.

**Не этот промпт:** DOGE platform map → [`cross-project-system-orientation.md`](./cross-project-system-orientation.md); DOGE parent backlog lock → [`cross-project-requirements-backlog-bootstrap.md`](./cross-project-requirements-backlog-bootstrap.md).

**Подстановка оператором:**

| Поле | Значение |
|------|----------|
| `$clientId=` | ключ из `clients.yaml` (напр. `alvasar`) |
| `$topic=` | тема аналитики (опц.; иначе Phase B спросит) |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/client-tenancy.md
@docs/methodology/Zeya888-builder-queue/specs/clients.yaml
@docs/methodology/Zeya888-builder-queue/specs/profiles.yaml
$clientId=
$topic=

Client product root orientation (Architect Studio pre-PA — client tenancy).
Resolve client from clients.yaml for $clientId (root, parent_requirements_dir, profiles[]).

MODE: read-only orientation + disk verify only.
STOP after Phase A–C tables in chat.
Do NOT: materialize EPIC/STORY/REQ/pkg; do NOT copy PA/P1; do NOT edit files;
      do NOT create app scaffold (pyproject / Expo / package.json) — name ≠ create.
Code claims: only after Read/Grep with path:line; else Unknown.
Wait for my explicit go-ahead before scatter / Studio / Builder.

Жёстко (analysis.mdc + MODE):
- Только факты из прочитанных файлов. Нет assumptions, нет silent invent.
- Doc claim — с path. Code claim — path:line после Read/Grep; иначе Unknown.
- Не edit; не materialize EPIC/STORY/child REQ/pkg в этом прогоне.
- Не путать $clientId с builder_project (profiles = keys listed under clients.yaml).

Reading order:
1) @guides/client-tenancy.md + @specs/clients.yaml — model + $clientId entry.
2) Parent REQ INDEX + files under client parent_requirements_dir (exists?).
3) Optional: client docs/analysis/ (scaffold starting points — name ≠ create).
4) For each profile key in clients.yaml → profiles.yaml: focus_folder, tasks_dir, plan_file, stack_label.
5) Per-MS bullrun «Актуальная точка» only if tasks_dir exists — status of bootstrap vs product work.

## Phase A — Client orientation (карта, не stories)
Выход:
1) Один абзац product concept из parent REQ (или Unknown).
2) Таблица MS: profile key | focus_folder | stack | role (backend/ui/…) | parent vs child REQ path.
3) Portable pack: `.cursor/plans/` under client root Present/Absent; dual-sync note from client-tenancy.
4) Verified vs Unknown.

## Phase B — Topic analytics ($topic)
1) Что уже сказано в parent REQ по $topic (path + §).
2) Что относится к какому profile key (без invent FR).
3) Gap table:
| Claim | Source path | Status (in-docs / missing / Unknown) | Owning profile(s) |

## Phase C — Next steps (in chat only; не запускай)
Таблица:
| Candidate next | Prompt / action | Notes |
| Client child REQs | cross-project-req-scatter with $targetProjects=<csv from clients.yaml profiles> | parent = client REQ path |
| Tech architecture per MS | target-tech-architecture | after child REQ |
| Builder session | session-starter / migration-* with builder_project=<profile key> | not $clientId |

Suggested intake = метка, НЕ «открой Builder сейчас».
```

---

## После STOP

Оператор явно выбирает: scatter (`$targetProjects=` = CSV profile keys из `clients.yaml`) · consistency audit · target-tech-architecture · или Builder Queue на одном `builder_project`.
