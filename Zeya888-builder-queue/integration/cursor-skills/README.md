# Cursor skills — portable copies in method pack

**Runtime (Cursor loads here):** `.cursor/skills/<name>/SKILL.md` (workspace root)  
**Portable SSOT (this pack):** `integration/cursor-skills/<name>/SKILL.md`

## Dual-sync (обязательно)

При любом изменении skill body править **оба** пути в одной волне (для каждого skill):

| Skill | Runtime | Portable |
|-------|---------|----------|
| `builder-session` | `.cursor/skills/builder-session/SKILL.md` | `integration/cursor-skills/builder-session/SKILL.md` |
| **Zeya888** (method-ops) | `.cursor/skills/zeya888/SKILL.md` | `integration/cursor-skills/zeya888/SKILL.md` |
| **orchestrator** (OP) | `.cursor/skills/orchestrator/SKILL.md` | `integration/cursor-skills/orchestrator/SKILL.md` |
| **validator** (VAL) | `.cursor/skills/validator/SKILL.md` | `integration/cursor-skills/validator/SKILL.md` |

Иначе локальный Cursor и method pack разъедутся.

## Restore

```bash
mkdir -p .cursor/skills/builder-session .cursor/skills/zeya888 \
  .cursor/skills/orchestrator .cursor/skills/validator
cp docs/methodology/Zeya888-builder-queue/integration/cursor-skills/builder-session/SKILL.md \
  .cursor/skills/builder-session/SKILL.md
cp docs/methodology/Zeya888-builder-queue/integration/cursor-skills/zeya888/SKILL.md \
  .cursor/skills/zeya888/SKILL.md
cp docs/methodology/Zeya888-builder-queue/integration/cursor-skills/orchestrator/SKILL.md \
  .cursor/skills/orchestrator/SKILL.md
cp docs/methodology/Zeya888-builder-queue/integration/cursor-skills/validator/SKILL.md \
  .cursor/skills/validator/SKILL.md
```

Ссылки внутри SKILL рассчитаны на runtime path `.cursor/skills/<name>/`.

Dialog wipe restore UI: [`../tools/dialog-restore-console.html`](../tools/dialog-restore-console.html)  
(O/V cards `@` orchestrator/validator skills + migration fences).

See also: [`../cursor-setup.md`](../cursor-setup.md).
