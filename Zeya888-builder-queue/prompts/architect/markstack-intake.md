# Markstack intake — self-unpacking agent brief

> **Attach this file + raw OP residual** (marks list, screenshots, short comments, optional locks).  
> No extra copy-paste block required. Agent runs the pipeline below end-to-end.  
> **Guide SSOT:** [`../../guides/markstack.md`](../../guides/markstack.md) · **Claims:** [`.cursor/rules/analysis.mdc`](../../../../../.cursor/rules/analysis.mdc) · **profiles:** [`../../specs/profiles.yaml`](../../specs/profiles.yaml)

**Не заменяет:** Builder Queue P1.3–P8 · overnight OP · [`../operator/lightweight-followup-triage.md`](../operator/lightweight-followup-triage.md)

---

## 0. Identity

You are running **Markstack**: residual → Interview → **Sufficiency (UX / REQ)** → **L1 → L1.5 → L2** story intake. Docs-only until materialize verb. Layers stay tagged **L1 / L1.5 / L2**.

---

## 1. Auto-derive (do not ask unless blocked)

From the attached residual + repo + `profiles.yaml`:

| Var | How |
|-----|-----|
| `builder_project` | Infer from paths (`spa-app` → `spa`, `doge-threads` → threads profile, etc.) or explicit OP key |
| `$residual` | This chat’s marks / shots / notes · or path to existing Interview/analysis |
| `$locks` | Explicit OP locks if any · else default **1A docs-only** · else `Unknown` |
| `$packageDir` | Allocation after probe · may be multi-package |

State derived vars once at the top of the first reply.

---

## 2. Hard locks (always)

- **MODE:** docs-only intake. No product code. No invent OP PASS. No empty epic pipeline trees (**name ≠ create**).
- **Claims:** Read/Grep/Glob with paths; else **Unknown**.
- **Default delivery:** plan + drafts **in chat**. Write Interview / UX-PROMPTS / STORY / ARCH / INDEX **only** after operator «запиши» / «materialize».
- **Language:** follow user rules (e.g. Russian replies if required).

---

## 3. Pipeline (run in order — do not skip)

### Step 0 — Route

| If | Then |
|----|------|
| Parent story Done · small hygiene · **no** new STORY | **STOP** → lightweight-followup |
| Pure REQ→package · no residual | Prefer req-to-backlog-stories / ui-admin / mixed |
| Else | **Continue Markstack** |

### Step 1 — Code probe

For each OP symptom: **Present | Partial | Absent** + path evidence.

### Step 2 — Interview SSOT

Locks + mark→story allocation + explicit non-goals.  
On materialize: write `INTERVIEW-*.md` (or extend existing Interview if `$residual` already is one).

### Step 3 — Sufficiency (**gate before L1**)

For **each** allocated story/mark, classify:

| Class | Criterion | Next |
|-------|-----------|------|
| **UX** | Visual Absent / wrong asset / layout Apply would invent without artboard (logo light plate, new page composition, strip residual not covered by existing M\*, content+layout rework) | Draft **UX-PROMPTS-*.md** · cite existing artboards if Partial · **do not** author L1 FR that invent pixels |
| **REQ** | New service contract needed | Sibling REQ path · link only |
| **CSS/code** | Measurable token/CSS/handler lock enough | Skip UX gen for that mark |

**Hard rule:** Interview → **Sufficiency UX table** → (UX prompts drafted / cited) → **only then** L1/L1.5/L2 for marks that needed UX.  
Skipping UX when class=UX is an **intake failure** (historical miss: plan said “UX gen No” then jumped to stories).

On materialize: write UX-PROMPTS files for UX-class marks; gen/intake PASS is a **later** wave — stories may stay `visual BLOCK` until intake PASS, but FR must **cite** the prompt/artboard tip.

### Step 4 — L1 (per story)

Numbered FR · AC · OOS · DoD · Meta: `structure | visual | gate`. Product language. Cite Interview + UX tip when visual.

### Step 5 — L1.5

ARCH § or ARCH-DELTA · ownership table · explicit supersede.

### Step 6 — L2

3–5 tasks · Order · FR links · skill · Status **Await**.

### Step 7 — Cross-links

INDEX · sibling packages · depends (HTTP before SPA wire when applicable).

### Step 8 — Stop

After materialize: artifacts on disk. Apply / P1.3 **separately**.  
Do not invent Present=PASS; later validation wave = Present table vs L1 + OP eye.

---

## 4. First reply shape (chat, before materialize)

1. Derived vars  
2. Step 0 route  
3. Probe table  
4. Interview draft (locks + allocation)  
5. **Sufficiency table** (mark → UX | REQ | CSS) · list planned UX-PROMPTS paths  
6. L1/L1.5/L2 story drafts (FR titles enough if long)  
7. Paths planned · blockers · skipped (name≠create)  
8. Await «запиши» unless OP already said materialize in the same message  

---

## 5. Materialize checklist

On «запиши» / «materialize»:

1. Evidence archive for OP shots (if any)  
2. INTERVIEW  
3. UX-PROMPTS for every UX-class mark (name ≠ invent gen PNG)  
4. STORY L1+L2 + ARCH L1.5 + INDEX  
5. No pipeline epic folders  
6. Return paths created · blockers · skipped  

---

## 6. Anti-patterns (experience)

1. Interview → L1 **without** Sufficiency UX table.  
2. “CSS lock only” for logo/page/layout when OP asks new visual.  
3. Invent OP PASS / citizen-ready after docs wave.  
4. Empty pipeline trees so paths exist.  
5. Markstack for post-Done one-line hygiene (use lightweight-followup).  
6. Confusing L\* intake with P\* Builder Queue.  
7. Asking OP to paste a second prompt block when this file + residual are already attached.

---

## 7. Related

- Guide: [`../../guides/markstack.md`](../../guides/markstack.md)  
- Training: [`../training/05a-markstack-story-intake.md`](../training/05a-markstack-story-intake.md)  
- REQ packages: [`req-to-backlog-stories.md`](./req-to-backlog-stories.md) · [`req-to-ui-admin-layers.md`](./req-to-ui-admin-layers.md) · [`req-to-frontend-mixed-package.md`](./req-to-frontend-mixed-package.md)  
- Post-Done: [`../operator/lightweight-followup-triage.md`](../operator/lightweight-followup-triage.md)
