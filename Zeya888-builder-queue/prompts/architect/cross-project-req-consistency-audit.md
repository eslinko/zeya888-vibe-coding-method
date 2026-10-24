# Architect — consistency audit (parent + project REQs vs operator target)

**Категория:** architect (findings-only, write report)  
**Scope default:** **DOGE classic-four** (`$targetProjects=gateway,identity,spa,gpt`). For **client** packages set `$targetProjects=` from [`../../specs/clients.yaml`](../../specs/clients.yaml) (Alvasar: `alvasar-backend,alvasar-ui`); parent under `clients/<Client>/docs/requirements/`. Client root first: [`client-product-root-orientation.md`](./client-product-root-orientation.md).  
**Не заменяет:** PA.2 / P1 / P4 code-vs-AC / scatter / orientation  
**Не создаёт:** STORY, pkg, task folders, правки parent/child REQ (кроме явной отдельной команды)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)  
**Даты отчёта:** [`../../guides/builder-artifact-dates.md`](../../guides/builder-artifact-dates.md) — live `--print-utc-now`

**Когда:** чистый диалог. Нужен аудит **пакета требований** (parent + per-project children) на: согласованность, реализуемость, соответствие короткой операторской цели (проецируемое состояние системы). Типично после scatter, до story package.

**Эталон структуры отчёта (не копировать содержание):** [`docs/analysis/req3-semantic-schema-runtime-hard-audit-2026-08-27.md`](../../../../../docs/analysis/req3-semantic-schema-runtime-hard-audit-2026-08-27.md) — Verdict / что пакет даёт / где молчит / достаточность документов / as-is appendix.

**Не этот промпт:** карта системы без пакета REQ → [`cross-project-system-orientation.md`](./cross-project-system-orientation.md) (DOGE) или [`client-product-root-orientation.md`](./client-product-root-orientation.md) (client); запись children → [`cross-project-req-scatter.md`](./cross-project-req-scatter.md).

**Подстановка оператором:**

| Поле | Значение |
|------|----------|
| `$parentReq=` | обязателен: path parent |
| `$childReqs=` | опц. CSV путей children; пусто → resolve с диска |
| `$targetState=` | обязателен: 2–8 предложений своими словами (целевое проецируемое состояние) |
| `$targetProjects=` | дефолт `gateway,identity,spa,gpt`. **Client cheat (Alvasar):** `alvasar-backend,alvasar-ui` |
| `$slice=` | опц. сужение parent (§§ / blocks) |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/modules/dashboard/search-matching-interviews/00-architecture-primer.md
@docs/methodology/Zeya888-builder-queue/guides/builder-artifact-dates.md
$parentReq=
$childReqs=
$targetState=
$targetProjects=gateway,identity,spa,gpt
$slice=

workspace_root: /Users/eslinko/Development/DOGEstonia

Architect Studio — CROSS-PROJECT REQ CONSISTENCY AUDIT (findings-only, write report).
@$parentReq
@$childReqs
$targetState=
@$slice (если задан — только эти §§/blocks)

MODE: analysis.mdc. No product code. No STORY/pkg/P3. No edits to parent/child REQ files.
No invented AC, APIs, fields, or the other side of a contract.
Code claim = path:line after Read/Grep; else Unknown. Doc claim = path.
Write one report this turn AFTER clarify gate passes. Product Story Done ≠ this audit.

## Clarify gate (обязательный доспрос — до inventory и до файла)
If $targetState is empty, one vague slogan, or mixes «сейчас в коде» with «когда пакет сделан» without saying which column to score:
STOP. Ask (human language; Other-протокол: answer operator counter-question first, then re-ask):
1) Score the PACKAGE as if fully implemented, as-is CODE now, or BOTH as explicit columns?
2) Which cases / nodes / channels count as success? (do not infer silently from REQ)
3) What is consciously OUT of the goal?
Do not fill gaps with product logic. Do not start the report until answers exist in this chat.

## Resolve children
If $childReqs set: Read those paths; missing file → STOP Ask.
If empty: from $parentReq section ## Derived project requirements AND/OR Glob/Grep files under
  doge-complaints-gateway|doge-identity-service|spa-app|GPT UI|doge-threads /docs/requirements/
  whose header Parent: matches $parentReq.
Zero children → STOP Ask. Do not invent child REQs.

## Phase 1 — Inventory
List: parent path; each child path + project; Parent-id; Siblings; which of $targetProjects has no child (out of scope vs missing — only from text).

## Phase 2 — Consistency (parent ↔ children)
Findings only, with paths:
- parent claim vs child scope (conflict / child silent / child invents extra)
- child missing Parent: / Parent-id
- Siblings row without reciprocal sibling or without contract: seam|TBD-question
- two children claiming one seam with no contract
- AC that cannot be tested even in principle
Do not propose implementation.

## Phase 3 — Target vs package projection
From REQ text only (DoD/AC/out-of-scope/later phases):
- what the package WOULD give if fully implemented
- what the package explicitly forbids or defers
- operator $targetState vs that projection: sufficient / insufficient / Unknown
If operator chose package-projection: do NOT score success against as-is code as the main verdict.
If operator chose as-is: main verdict is code vs target; package gaps still listed separately.

## Phase 4 — Implementability (code appendix, not a substitute for Phase 3)
For material REQ claims in scope: in-docs / in-code (path:line) / missing.
Respect primer privacy invariant (gateway anonymized submitter vs identity PII).
Do not invent endpoints to make a claim «implementable».

## Write report (same turn, after phases)
1) From workspace root: python3 docs/methodology/Zeya888-builder-queue/cli/builder_resolve_queue.py --print-utc-now
   Use utc_date / utc_now from stdout only.
2) Path: docs/analysis/<slug>-req-consistency-audit-<utc_date>.md
   slug = Parent-id or parent filename stem; do not invent a new REQ number.
3) Sections (adapt, do not hardcode a named feature): inputs + verbatim $targetState; inventory; consistency; target vs package; implementability appendix; verdict; Unknowns/questions.
4) Reply: report path | verdict | remaining Unknowns | STOP (no STORY/pkg handoff unless operator asks).
```

---

## Примечания (не в copy-paste)

- После scatter: этот audit, затем PA.2 / [`req-to-backlog-stories.md`](./req-to-backlog-stories.md) только по команде.
- Human layer: [`../../curriculum/06-architect-studio-and-p1-intakes.md`](../../curriculum/06-architect-studio-and-p1-intakes.md).
