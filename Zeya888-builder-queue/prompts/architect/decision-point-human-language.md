# Decision-point — human language (ОЯЗ) + ethics/architecture fit

**Категория:** architect (companion to interview prompts)  
**Parent:** [`target-tech-architecture.md`](./target-tech-architecture.md) Decision-point protocol; usable from any Architect Studio interview  
**Не заменяет:** сам target-tech-architecture / scatter / consistency-audit  
**Не создаёт:** STORY, pkg, product code, arch docs on disk (unless parent prompt + «запиши»)  
**Метод:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc)

---

## When

Оператор просит **объяснить варианты по-человечески** (ОЯЗ), с понятной аналитикой и рекомендацией — особенно на Decision-point (A/B/C + Other) внутри CTO/CPO interview.

| Use case | Да / нет |
|----------|----------|
| Идёт interview; варианты уже названы; нужна ОЯЗ-расшифровка | **Да** |
| Нужно выровнять рекомендацию с **целевым состоянием** (REQ / tech-arch draft) + принципы DOGEstonia | **Да** |
| Оператор просит сразу implement / rename / secrets | **Нет** → вернуть в parent prompt / implement wave |
| Нужен новый STORY package | **Нет** → [`req-to-backlog-stories.md`](./req-to-backlog-stories.md) |

---

## Copy-paste

```text
@.cursor/rules/analysis.mdc
@docs/methodology/Zeya888-builder-queue/prompts/architect/decision-point-human-language.md
@$requirementDoc= (если есть целевое состояние)
@$decisionContext= (опц. — вставить последние варианты A/B/C из чата)

Architect Studio — Decision-point ОЯЗ (human language).

MODE: analysis.mdc. Chat only unless parent prompt already authorized «запиши».
Do NOT invent options beyond what was already offered + operator Other.
Do NOT write architecture/REQ/code unless this turn’s parent process explicitly materializes.
Do NOT paste secrets from .env.

Task:
1) Explain the pending decision in plain Russian (ОЯЗ): what we are choosing and why it matters now.
2) For EACH option: meaning in human words; what you gain; what you risk; how it helps or hurts the target state (cite REQ § / AC if @$requirementDoc set).
3) Map each option to DOGEstonia / Zeya888 principles below (fits | tension | conflicts | Unknown).
4) One recommendation + why; state «решение остаётся за оператором».
5) Re-ask the same decision (A/B/C/Other) in one short line. STOP.

## Principles checklist (cite when relevant; do not invent new doctrine)

Trust & boundaries
- Separate trust domains (user Bearer ≠ service token ≠ channel token).
- Browser never embeds service_role / SERVICE_API_TOKEN.
- Fail-closed when peer URL / token required and missing.

Honesty of claims
- analysis.mdc: path:line or Unknown; name ≠ create; no silent invent of APIs/backends.
- Product Story Done ≠ Draft REQ ≠ green local smoke alone.

Ops & naming hygiene (when REQ9-class target applies)
- One local start ritual for Python (`make serve`/`dev` → uvicorn).
- One grammar for peer URLs / S2S names; no third synonym for the same peer.
- Topology / living map stays coherent after renames.

Operator ethics
- Recommendation is advisory; operator decides.
- Prefer safe coexistence over blind speed when rename breaks live callers (Railway, n8n, peers).
- Do not expand scope into product features / invent waitlist / nginx.

If @$requirementDoc is set, prefer options that move AC toward Pass without violating Out of scope of that REQ.
```

---

## Agent output shape (chat)

1. **О чём выбор (ОЯЗ)** — 3–6 предложений, без жаргона или с мгновенным переводом термина.  
2. **Таблица / блоки по вариантам** — смысл · плюсы · минусы · связь с целевым состоянием · principles fit.  
3. **Рекомендация** — один вариант + почему; advisory.  
4. **Вопрос снова** — `A / B / C / Other?` STOP.

## Explicit not this prompt

- Materialize tech-arch / interview report (parent [`target-tech-architecture.md`](./target-tech-architecture.md) Phase 3).  
- Implement Makefile/env renames.  
- Rewrite REQ DoD unless operator asks.

End.
