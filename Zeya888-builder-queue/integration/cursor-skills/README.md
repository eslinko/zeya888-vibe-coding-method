# Cursor skills — portable copies in method pack

**Runtime (Cursor loads here):** `.cursor/skills/<name>/SKILL.md` (workspace root)  
**Portable SSOT (this pack):** `integration/cursor-skills/<name>/SKILL.md`

## Dual-sync (обязательно)

При любом изменении skill body править **оба** пути в одном волне:

1. `.cursor/skills/builder-session/SKILL.md` — локальный runtime  
2. `docs/methodology/Zeya888-builder-queue/integration/cursor-skills/builder-session/SKILL.md` — перенос/restore с методологией  

Иначе локальный Cursor и method pack разъедутся.

## Restore

```bash
mkdir -p .cursor/skills/builder-session
cp docs/methodology/Zeya888-builder-queue/integration/cursor-skills/builder-session/SKILL.md \
  .cursor/skills/builder-session/SKILL.md
```

Ссылки внутри SKILL рассчитаны на runtime path `.cursor/skills/builder-session/`.

See also: [`../cursor-setup.md`](../cursor-setup.md).
