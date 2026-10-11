#!/usr/bin/env python3
"""Export Cursor Agent/Composer chats for a workspace folder → markdown packs.

Read-only against Cursor state.vscdb. Never writes IDE state.
Bodies come from ~/.cursor/projects/<slug>/agent-transcripts/<uuid>/*.jsonl.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

SECRET_LINE = re.compile(
    r"(?i)^(\s*(?:export\s+)?)([A-Z0-9_]*(?:KEY|TOKEN|SECRET|PASSWORD|PASS|PRIVATE|SERVICE_ROLE)[A-Z0-9_]*)\s*=\s*.+$"
)
USER_QUERY = re.compile(r"<user_query>\s*(.*?)\s*</user_query>", re.DOTALL | re.IGNORECASE)


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def path_to_file_uri(path: Path) -> str:
    return path.resolve().as_uri()


def workspace_slug(folder: Path) -> str:
    """Match Cursor project slug: absolute path with / → - (no leading slash)."""
    resolved = str(folder.resolve())
    if resolved.startswith("/"):
        resolved = resolved[1:]
    return resolved.replace("/", "-")


def find_workspace_storage(folder: Path, user_dir: Path) -> Path | None:
    target = path_to_file_uri(folder)
    root = user_dir / "workspaceStorage"
    if not root.is_dir():
        return None
    for d in root.iterdir():
        wf = d / "workspace.json"
        if not wf.is_file():
            continue
        try:
            data = json.loads(wf.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        folder_uri = data.get("folder") or ""
        if folder_uri == target or unquote(folder_uri) == target:
            return d
        # also accept path equality via urlparse
        if folder_uri.startswith("file://"):
            try:
                p = Path(urlparse(unquote(folder_uri)).path)
                if p.resolve() == folder.resolve():
                    return d
            except OSError:
                pass
    return None


def read_item(db: Path, key: str) -> Any | None:
    if not db.is_file():
        return None
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        row = con.execute("SELECT value FROM ItemTable WHERE key = ?", (key,)).fetchone()
    finally:
        con.close()
    if not row:
        return None
    raw = row[0]
    if isinstance(raw, bytes):
        raw = raw.decode("utf-8", errors="replace")
    if not isinstance(raw, str):
        return raw
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def extract_text(message: Any) -> str:
    if message is None:
        return ""
    if isinstance(message, str):
        return message
    if not isinstance(message, dict):
        return str(message)
    content = message.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(str(block.get("text") or ""))
            elif isinstance(block, str):
                parts.append(block)
        return "\n".join(parts)
    return json.dumps(message, ensure_ascii=False)[:2000]


def first_user_title(text: str, limit: int = 100) -> str:
    m = USER_QUERY.search(text)
    body = (m.group(1) if m else text).strip()
    body = re.sub(r"\s+", " ", body)
    if len(body) > limit:
        body = body[: limit - 1] + "…"
    return body or "(empty)"


def redact(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if SECRET_LINE.match(line):
            lines.append(SECRET_LINE.sub(r"\1\2=<REDACTED>", line))
        else:
            lines.append(line)
    return "\n".join(lines)


def load_transcript(transcripts_root: Path, composer_id: str) -> list[dict[str, Any]]:
    d = transcripts_root / composer_id
    if not d.is_dir():
        return []
    files = sorted(d.glob("*.jsonl"))
    if not files:
        return []
    # prefer same-named file
    preferred = d / f"{composer_id}.jsonl"
    path = preferred if preferred.is_file() else files[0]
    out: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def collect_ids(
    composer_data: Any,
    pinned: Any,
    transcripts_root: Path,
    *,
    mode: str,
    explicit_ids: list[str],
) -> list[str]:
    selected: list[str] = []
    last_focused: list[str] = []
    if isinstance(composer_data, dict):
        selected = [str(x) for x in (composer_data.get("selectedComposerIds") or [])]
        last_focused = [str(x) for x in (composer_data.get("lastFocusedComposerIds") or [])]
    pinned_ids = [str(x) for x in pinned] if isinstance(pinned, list) else []

    if explicit_ids:
        return explicit_ids
    if mode == "selected":
        ordered = list(dict.fromkeys(last_focused + selected + pinned_ids))
        return ordered
    if mode == "all":
        disk = sorted([p.name for p in transcripts_root.iterdir() if p.is_dir()]) if transcripts_root.is_dir() else []
        return list(dict.fromkeys(last_focused + selected + pinned_ids + disk))
    raise ValueError(f"unknown mode {mode}")


def write_chat_md(
    path: Path,
    *,
    composer_id: str,
    title: str,
    events: list[dict[str, Any]],
    last_n: int,
    max_chars: int,
    source_jsonl: str,
) -> dict[str, Any]:
    total = len(events)
    slice_events = events[-last_n:] if last_n > 0 else events
    lines = [
        f"# Chat handoff — `{composer_id}`",
        "",
        f"- **Title (first user snippet):** {title}",
        f"- **Events total:** {total}",
        f"- **Exported last:** {len(slice_events)}",
        f"- **Source:** `{source_jsonl}`",
        f"- **Note:** Export for file-first restore. Does **not** rehydrate Cursor sidebar.",
        "",
        "## Messages",
        "",
    ]
    used = 0
    exported = 0
    for ev in slice_events:
        role = str(ev.get("role") or "unknown")
        text = redact(extract_text(ev.get("message")))
        if max_chars > 0 and used + len(text) > max_chars:
            remain = max(0, max_chars - used)
            if remain < 80:
                lines.append(f"_…truncated: char budget {max_chars}_")
                break
            text = text[:remain] + "\n\n_…truncated_"
        lines.append(f"### {role}")
        lines.append("")
        lines.append(text if text.strip() else "_(empty)_")
        lines.append("")
        used += len(text)
        exported += 1
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "composer_id": composer_id,
        "title": title,
        "events_total": total,
        "events_exported": exported,
        "missing_transcript": total == 0,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--workspace",
        type=Path,
        default=Path.cwd(),
        help="Workspace folder path (default: cwd)",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output directory (default: <workspace>/docs/analysis/chat-handoff-<utc>)",
    )
    ap.add_argument(
        "--mode",
        choices=("selected", "all"),
        default="selected",
        help="selected = composer.composerData (+ pinned); all = also every transcript dir",
    )
    ap.add_argument(
        "--ids",
        default="",
        help="Comma-separated composer UUIDs (overrides --mode selection)",
    )
    ap.add_argument("--last-n", type=int, default=40, help="Last N transcript events per chat (0 = all)")
    ap.add_argument("--max-chars", type=int, default=120_000, help="Max chars per chat file (0 = unlimited)")
    ap.add_argument(
        "--user-dir",
        type=Path,
        default=Path.home() / "Library/Application Support/Cursor/User",
        help="Cursor User data dir (macOS default)",
    )
    ap.add_argument(
        "--projects-dir",
        type=Path,
        default=Path.home() / ".cursor/projects",
        help="Cursor projects dir (agent-transcripts root)",
    )
    args = ap.parse_args()

    folder = args.workspace.expanduser().resolve()
    if not folder.is_dir():
        print(f"ERROR: workspace not a directory: {folder}", file=sys.stderr)
        return 2

    ws_storage = find_workspace_storage(folder, args.user_dir.expanduser())
    if ws_storage is None:
        print(
            f"ERROR: no workspaceStorage match for {path_to_file_uri(folder)} under {args.user_dir}",
            file=sys.stderr,
        )
        return 2

    db = ws_storage / "state.vscdb"
    composer_data = read_item(db, "composer.composerData")
    pinned = read_item(db, "cursor/pinnedComposers")

    slug = workspace_slug(folder)
    transcripts_root = args.projects_dir.expanduser() / slug / "agent-transcripts"
    explicit = [x.strip() for x in args.ids.split(",") if x.strip()]
    ids = collect_ids(composer_data, pinned, transcripts_root, mode=args.mode, explicit_ids=explicit)
    if not ids:
        print("ERROR: no composer ids to export", file=sys.stderr)
        return 2

    out = args.out
    if out is None:
        out = folder / "docs" / "analysis" / f"chat-handoff-{utc_stamp()}"
    else:
        out = out.expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = []
    for cid in ids:
        events = load_transcript(transcripts_root, cid)
        first_user = ""
        for ev in events:
            if ev.get("role") == "user":
                first_user = extract_text(ev.get("message"))
                break
        title = first_user_title(first_user)
        src = str(transcripts_root / cid / f"{cid}.jsonl")
        meta = write_chat_md(
            out / f"{cid}.md",
            composer_id=cid,
            title=title,
            events=events,
            last_n=args.last_n,
            max_chars=args.max_chars,
            source_jsonl=src,
        )
        rows.append(meta)

    index_lines = [
        f"# Chat handoff — {folder.name}",
        "",
        f"- **Exported (UTC):** {datetime.now(timezone.utc).isoformat()}",
        f"- **Workspace:** `{folder}`",
        f"- **workspaceStorage:** `{ws_storage}`",
        f"- **transcripts:** `{transcripts_root}`",
        f"- **Mode:** `{args.mode}`" + (f" + explicit ids" if explicit else ""),
        f"- **last_n / max_chars:** {args.last_n} / {args.max_chars}",
        "",
        "## Important",
        "",
        "- This pack is for **file-first restore** in a new workspace (`@` files + self-restore prompt).",
        "- It does **not** rehydrate Cursor Agent sidebar as live composers.",
        "- Do **not** paste secrets; script redacts common KEY/TOKEN/SECRET/PASSWORD lines only.",
        "",
        "## Chats",
        "",
        "| UUID | Title | Events | Missing transcript |",
        "|------|-------|--------|--------------------|",
    ]
    for r in rows:
        miss = "yes" if r["missing_transcript"] else "no"
        title = str(r["title"]).replace("|", "\\|")
        index_lines.append(
            f"| `{r['composer_id']}` | {title} | {r['events_total']}→{r['events_exported']} | {miss} |"
        )
    index_lines.extend(
        [
            "",
            "## Next (new workspace)",
            "",
            "1. Open new folder with IDE profile **Zeya888**.",
            "2. Copy this handoff directory into the new root (or keep path and `@` it).",
            "3. Paste `prompts/migration/migration-self-restore-zeya888-method.md` + `@` needed `*.md` from this pack.",
            "",
        ]
    )
    (out / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")

    print(f"ok {len(rows)} chats → {out}")
    print(f"INDEX {out / 'INDEX.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
