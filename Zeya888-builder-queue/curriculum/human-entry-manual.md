# Human entry manual — starting with Zeya888 Builder Queue

This is the **human entry point**. It does not start working phases (“ship code now”). Goal: pick a route, open short **training dialogues** with your AI, and know what to do next.

Why the method exists: [`00-guide-for-humans.md`](./00-guide-for-humans.md).  
Route map: [`learning-path.md`](./learning-path.md).  
Self-serve vs consultation boundary: [`../guides/consultation-positioning.md`](../guides/consultation-positioning.md).

---

## 0. What you need

- Cursor (or another AI chat that can read repo files via `@`).
- Access to the methodology folder in the workspace: `docs/methodology/Zeya888-builder-queue/` (copy or symlink — see [`../integration/cursor-setup.md`](../integration/cursor-setup.md)).
- Your project on disk (for route A — technical; for route B a written project goal is enough).

**Layout note (after client tenancy):** most DOGEstonia apps stay **flat** peers under the workspace root. Some products live under `clients/<Client>/` with nested Builder profiles — see [`../guides/client-tenancy.md`](../guides/client-tenancy.md). Training still starts the same; when you connect a **client** repo, use nested `focus_folder` and `client-product-root-orientation`, not the DOGE four-app map.

Terms like “phase P3” or “pkg” are **not required** before training dialogues — the AI will explain them as you go.

---

## 1. Choose your route (by expected outcome)

| Route | Who you are | What you want |
|-------|-------------|----------------|
| **A — technical** | Comfortable with git/repos and your own AI agents | Understand the system, connect it to your project, **run the full work cycle yourself** from the docs |
| **B — fintech / vibe-coder** | Strong domain expertise, little engineering experience | Understand the method’s value and shape, your role, prepare the project for **guided adoption** |

Both routes start the same (dialogs 1 and 2). They diverge at dialog 3.

**Important:** finishing a few training dialogues ≠ “I can now make every engineering decision alone.” Route B deliberately ends in preparation for consultation, not a claim of full independence.

---

## 2. Prepare sources for the AI

Each training prompt already lists files with `@`. Before you start, make sure the agent can see:

`docs/methodology/Zeya888-builder-queue/`

**Source priority on conflict** (rule for the AI):

1. **Normative:** `core/workflow.md`, `core/session-starter.md`, `contracts/`, `specs/`
2. **Teaching:** `curriculum/`, `prompts/training/`
3. **Legacy:** `core/workflow-legacy.md` — only if normative is silent; legacy phase numbering may differ

If a file is missing on disk, the AI must say **Unknown**, not invent.

---

## 3. Create the first training dialogue

1. Open a **new** Cursor chat (clean context).
2. Open [`../prompts/training/01-how-the-system-works.md`](../prompts/training/01-how-the-system-works.md).
3. Paste the entire **Copy-paste** block into the chat (including `@…` lines).
4. Answer briefly; do not ask to “configure my prod right now.”

Full dialog list and handoff rules: [`../prompts/training/INDEX.md`](../prompts/training/INDEX.md).

---

## 4. Move in small steps

In each dialogue the AI should:

- explain one chunk at a time;
- check understanding;
- **not** create code, packages, or work artifacts “for the demo.”

You may stop anytime and continue later using the previous dialogue’s **Learning summary**.

---

## 5. When you can move on

At the end of a dialogue, get (or ask for) a **Learning summary** like:

```text
Understood: …
Still unclear: …
Ready for: dialog N / not yet, because …
Route: A | B | not chosen yet
```

Paste that block at the **start** of the next chat together with the next prompt’s copy-paste.

---

## 6. Dialogue sequence

| Step | Dialogue | File |
|------|----------|------|
| 1 | How the system works | [`../prompts/training/01-how-the-system-works.md`](../prompts/training/01-how-the-system-works.md) |
| 2 | How the operator steers work | [`../prompts/training/02-how-the-operator-steers.md`](../prompts/training/02-how-the-operator-steers.md) |
| 3A | Connect your project (tech route) | [`../prompts/training/03a-connect-your-project-tech.md`](../prompts/training/03a-connect-your-project-tech.md) |
| 3B | Project brief (fintech route) | [`../prompts/training/03b-project-brief-fintech.md`](../prompts/training/03b-project-brief-fintech.md) |
| 4A | First managed work session (route A only, after your explicit go-ahead) | [`../prompts/training/04a-first-managed-work-session.md`](../prompts/training/04a-first-managed-work-session.md) |
| 5A | Markstack story intake (route A, optional — residual / screens → layered stories) | [`../prompts/training/05a-markstack-story-intake.md`](../prompts/training/05a-markstack-story-intake.md) |

After **3B** → read [`../guides/consultation-positioning.md`](../guides/consultation-positioning.md) and prepare to contact the author.  
After **4A** → operative starts: [`../core/session-starter.md`](../core/session-starter.md) and curriculum modules 01–06 via [`learning-path.md`](./learning-path.md).  
Optional **5A** when intake is live UI residual / screens+comments before Apply — then operative [`../prompts/architect/markstack-intake.md`](../prompts/architect/markstack-intake.md).

---

## 7. Document roles

| Role | Examples | Purpose |
|------|----------|---------|
| **Teaching** | this manual, `curriculum/*`, `prompts/training/*` | Learn and navigate |
| **Normative** | `core/workflow.md`, contracts, specs | Rules for real operator/agent work |
| **Legacy** | `core/workflow-legacy.md` | Historical full prompts; not the main entry |

On conflict, teaching AI follows **normative**.

---

## 8. Common mistake

Open README “Quick start” → jump straight to `session-starter` and verify, **skipping** training dialogues. Fine if you already know the method. If not — start here, with dialog 1.
