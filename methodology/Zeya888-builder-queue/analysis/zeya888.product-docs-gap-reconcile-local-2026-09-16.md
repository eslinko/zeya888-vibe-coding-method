# zeya888. — Product docs gap reconcile (local vs snapshot) · 2026-09-16

> **Rule:** [`.cursor/rules/analysis.mdc`](../../../../.cursor/rules/analysis.mdc)  
> **Scope:** documentation layer only — teaching / navigation / audience split. Not method efficacy.

## Snapshot findings → local

| Finding | Local before wave | After this wave |
|---------|-------------------|-----------------|
| Entry jumps to install/verify | [`README.md`](../README.md) “Quick start” | Closed via [`../curriculum/human-entry-manual.md`](../curriculum/human-entry-manual.md) as first entry |
| No AI learning-dialog prompts | No `prompts/training/` | Closed: [`../prompts/training/`](../prompts/training/) |
| Single audience path | [`learning-path.md`](../curriculum/learning-path.md) modules 0–6 only | Closed: routes A (tech) / B (fintech) |
| P4 naming conflict | starter §3.5 “P4 Scaffold” vs workflow P4 audit | Closed: §3.5 → P5 scaffold |
| No consultation memo | Missing | Closed: [`../guides/consultation-positioning.md`](../guides/consultation-positioning.md) |
| Verify FAIL semantics | queue-manual vs starter “FAIL=stop” underspecified for learners | Closed: note in curriculum/04 |
| Delivery composition | cursor-setup assumed author workspace paths | Soft closed: “Delivery composition” in cursor-setup |
| Language | Learning layer drafted in Russian | Closed: learning entry layer translated to **English** (v1.4.44) |

## Explicitly still open / out of this wave

- Real author contact details in consultation memo (placeholder only)
- Full English rewrite of older Russian curriculum modules 00–06 body text
- Full rewrite of `workflow-legacy.md`
- Demo pkg/code for teaching
