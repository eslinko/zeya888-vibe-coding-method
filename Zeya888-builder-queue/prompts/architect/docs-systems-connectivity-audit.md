# Architect — docs systems connectivity / fitness audit

**Категория:** architect (findings-only, write report)  
**Scope:** **универсальный** — любой набор ≥2 корней документации (REQ, architecture, maps, primers, client/focus packages). Не привязан к DOGE classic-four и не к конкретному client.  
**Не заменяет:** PA.2 / P1 / P4 code-vs-AC / REQ consistency vs `$targetState` / product orientation  
**Не создаёт:** STORY, pkg, правки аудируемых docs (кроме явной отдельной команды)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Даты отчёта:** [`../../guides/builder-artifact-dates.md`](../../guides/builder-artifact-dates.md) — live `--print-utc-now`

**Когда:** в **любом** чате, куда вставили copy-paste. Нужна оценка **нескольких систем документации** на: соответствие стилей, удобство, логичность структуры, масштабируемость и **качественную связность** друг с другом (можно ли дальше опираться на их стыки без dual-SSOT / orphan stubs / битого cascade). Не смешивать с той же волной Builder implement / правкой аудируемых файлов — MODE = findings-only + report (fix = отдельный order).

**Не этот промпт:**

| Ситуация | Куда |
|----------|------|
| Parent + child REQ vs операторская цель / реализуемость | [`cross-project-req-consistency-audit.md`](./cross-project-req-consistency-audit.md) |
| Карта продукта DOGE / client root | [`cross-project-system-orientation.md`](./cross-project-system-orientation.md) · [`client-product-root-orientation.md`](./client-product-root-orientation.md) |
| Запись child REQs / stories / tech-arch materialize | scatter / `req-to-*` / `target-tech-architecture` |

**Подстановка оператором:**

| Поле | Значение |
|------|----------|
| `$docSystems=` | **обязателен:** CSV корней. Элемент = `Label\|path` или `path` (Label = basename). Минимум **2**. Path = файл **или** каталог (`…/requirements`, `…/architecture`, пакет `01-…`, …) |
| `$lens=` | опц. CSV: `style,convenience,structure,scalability,connectivity` — default = все |
| `$reportDir=` | опц. каталог отчёта. Default: ближайший `…/docs/analysis/` к **первой** системе; иначе `docs/analysis/` от workspace root |
| `$slug=` | опц. префикс имени; default `docs-systems-connectivity` |
| `$verifyCode=` | опц. `on` = для doc-claims со ссылкой на код можно Verify path:line. **Default off** — только docs↔docs |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/guides/builder-artifact-dates.md
$docSystems=
$lens=
$reportDir=
$slug=docs-systems-connectivity
$verifyCode=

workspace_root: /Users/eslinko/Development/DOGEstonia

Architect Studio — DOCS SYSTEMS CONNECTIVITY / FITNESS AUDIT (findings-only, write report).
$docSystems=
$lens= (empty = style,convenience,structure,scalability,connectivity)
$reportDir= (empty = resolve default)
$slug=
$verifyCode= (empty|off = docs-only; on = optional code verify for cited claims)

MODE: analysis.mdc. Findings-only.
No product code edits. No STORY/pkg/P3. No edits to audited documentation trees.
No invented Role/SSOT/Home if not stated in files. No silent invent of missing links.
Doc claim = path (quote Role/SSOT banners). Code claim only if $verifyCode=on AND after Read/Grep path:line; else Unknown.
Do not "fix" structure in this wave — report only.
Product Story Done ≠ this audit.

## Clarify gate (до inventory / до файла)
STOP and Ask if:
1) $docSystems empty OR after parse/Glob fewer than 2 existing paths.
2) Any listed path does not exist.
3) Operator mixed «исправь структуру / выровняй» into this paste → confirm: this wave = report only; fixes = separate order.
Do not invent Role/SSOT when INDEX/README/00 banner absent → mark Unknown.
Do not start Phase 1 until gate passes.

## Parse $docSystems
Split CSV. For each item:
- If contains `|` → Label = left, path = right (trim).
- Else Label = basename(path), path = item.
Resolve relative to workspace_root. Missing → STOP Ask.
Type: file | tree (directory).

## Resolve $reportDir
If set: use it (must exist or createable under a docs/analysis pattern — create only the report file's parent if missing and clearly under */docs/analysis/ or operator path).
If empty:
1) Start from first system's path; walk up until a directory named `docs` is found; sibling `analysis/` → use that.
2) Else workspace_root/docs/analysis/
Report file: $reportDir/$slug-<utc_date>.md

## Phase 1 — Inventory (each system)
For each Label|path (Read/Glob/wc as needed):
| Label | Path | Type | Entry points | Claimed Role/SSOT (quote+path or Unknown) | Size (md count / wc -l) | Neighbors (_archive/_backup) as fact only |
Entry points prefer: INDEX.md, README.md, 00-overview.md, sole .md if file-root.
Do not treat _archive/_backup as SSOT.

## Phase 2 — Style concordance (skip if lens excludes style)
Across systems, findings with paths:
- Section templates (e.g. Goal/Scope/Verified/Target/AC vs numbered guides 00/10/…)
- Banners (Role, Not SSOT, redirect-only, Profile)
- Voice / bilingual mix
- Naming & slug collisions across roots (same slug, different homes)
- Header dates/versions drift that confuses "which is current"

## Phase 3 — Structure logic (skip if lens excludes structure)
- what vs how vs map/redirect separation (or collapse)
- Home/owner columns or equivalent ownership signals
- Expand prohibitions; orphan stub vs redirect-only
- Duplicate normative bodies (same topic fully restated in two systems)

## Phase 4 — Cross-system connectivity (core; skip if lens excludes connectivity)
Build link matrix LabelA → LabelB: present | missing | broken | one-way.
Findings:
- Dual SSOT for one topic
- Parent/sibling cites without reciprocal or without explicit "cite only"
- Thin/map/redirect systems that still hold normative how
- Broken cascade (points at sibling home that is Absent / garbage / wrong role) — finding only, no restore
Grep relative links between the listed roots; verify targets exist.

## Phase 5 — Convenience + scalability (skip if lens excludes those)
- Operator/agent reading route across the N systems (one short recommended order)
- Where a new ID / guide / appendix should land without forking SSOT
- Same-slug risk across roots
- Migration noise (value maps, pre-align backups) that hurts long-term reading

## Phase 6 — Scorecard + write report
Scores per system × applicable lens criteria: Сильно | Средне | Слабо | Unknown.
Plus inter-system connectivity verdict.

1) python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
   Use utc_date / utc_now from stdout only.
2) Write $reportDir/$slug-<utc_date>.md with sections:
   - Inputs (verbatim $docSystems, $lens, $reportDir, $slug, $verifyCode)
   - Inventory
   - Style
   - Structure
   - Connectivity matrix + findings
   - Convenience / scalability
   - Scorecard + connectivity verdict
   - Residual risks
   - Unknowns / clarifying questions
   - Out of scope / recommended next orders (labels only — do not implement)
3) Reply: report path | connectivity verdict | top risks | STOP
   No fix wave / STORY / pkg unless operator explicitly asks next.
```

---

## Примечания (не в copy-paste)

- **Vs REQ consistency audit:** тот промпт = parent+children REQ vs `$targetState` + implementability. Этот = **fitness + стыковка произвольных docs-корней** (REQ, arch, maps, …) без обязательной product-цели.
- **Эталон глубины (не копировать содержание):** чатовая оценка «четырёх осей» после docs-align — scorecard + трение + маршрут + риски; алгоритм выше обобщает это на N систем.
- **Пример подстановки (Alvasar infra axes — иллюстрация):**

```text
$docSystems=RootREQ|clients/Alvasar/docs/requirements/REQ01-technical-infrastructure.md,RootArch|clients/Alvasar/docs/architecture,BackREQ|clients/Alvasar/backend/docs/requirements/01-desktop-runtime-bridge.md,BackArch|clients/Alvasar/backend/docs/architecture
```

- Human layer: [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md).
