#!/usr/bin/env python3
"""Build dialog-restore-work-catalog.js from prompts/ + architect/prompts-manual.md.

Run from anywhere:
  python3 docs/methodology/Zeya888-builder-queue/tools/build-dialog-restore-work-catalog.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
METHOD = TOOLS.parent
PROMPTS = METHOD / "prompts"
OUT_JS = TOOLS / "dialog-restore-work-catalog.js"
MANUAL = PROMPTS / "architect" / "prompts-manual.md"

CATEGORIES = ("architect", "operator", "migration", "ux", "training")
SKIP_NAMES = {
    "INDEX.md",
    "prompts-manual.md",
}
SKIP_SUBSTRINGS = ("gap-analysis",)


def rel_workspace(path: Path) -> str:
    # Prefer path from method pack root for display
    try:
        return str(path.relative_to(METHOD.parent.parent.parent))  # docs/
    except ValueError:
        pass
    try:
        return str(path.relative_to(METHOD))
    except ValueError:
        return str(path)


def method_rel(path: Path) -> str:
    try:
        return f"docs/methodology/Zeya888-builder-queue/{path.relative_to(METHOD)}"
    except ValueError:
        return str(path)


def first_h1(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def extract_copy_paste(text: str) -> str | None:
    """First fenced block after ## Copy-paste (any language tag)."""
    m = re.search(r"(?im)^##\s+Copy-paste\s*$", text)
    if not m:
        return None
    rest = text[m.end() :]
    fm = re.search(r"```(?:text|markdown|md)?\s*\n(.*?)```", rest, re.S)
    if not fm:
        return None
    return fm.group(1).rstrip("\n")


def extract_params_from_table(text: str) -> list[dict]:
    """Parse markdown table rows under Подстановка / Параметры-like sections."""
    params: list[dict] = []
    # Table rows: | `$foo=` | description |
    for m in re.finditer(
        r"\|\s*`?\$([A-Za-z0-9_]+)=?`?\s*\|\s*([^|\n]+)\|",
        text,
    ):
        name = m.group(1).strip()
        desc = m.group(2).strip()
        if name.lower() in ("поле", "field", "var", "параметр"):
            continue
        if desc.lower().startswith("---") or desc.lower() in ("значение", "value"):
            continue
        params.append({"name": f"${name}", "desc": desc})
    # Dedup by name preserving order
    seen = set()
    out = []
    for p in params:
        if p["name"] in seen:
            continue
        seen.add(p["name"])
        out.append(p)
    return out


def extract_params_from_fence(paste: str | None) -> list[dict]:
    if not paste:
        return []
    found = re.findall(r"\$([A-Za-z0-9_]+)=?", paste)
    out = []
    seen = set()
    for name in found:
        key = f"${name}"
        if key in seen:
            continue
        seen.add(key)
        out.append({"name": key, "desc": "подставь значение перед отправкой"})
    return out


def blurb_from_body(text: str, title: str) -> str:
    """First useful prose line after H1."""
    lines = text.splitlines()
    started = False
    chunks: list[str] = []
    for line in lines:
        if line.startswith("# "):
            started = True
            continue
        if not started:
            continue
        s = line.strip()
        if not s or s.startswith("```") or s.startswith("|"):
            if chunks:
                break
            continue
        if s.startswith("**Категория:**") or s.startswith("**Метод:**") or s.startswith("**Guide:**"):
            continue
        if s.startswith("**Когда:**"):
            return s.replace("**Когда:**", "").strip()
        if s.startswith("**Не ") or s.startswith("> "):
            continue
        if s.startswith("## "):
            break
        # strip bold markers lightly
        s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
        chunks.append(s)
        if len(" ".join(chunks)) > 160:
            break
    blurb = " ".join(chunks).strip()
    if not blurb:
        return title
    if len(blurb) > 220:
        blurb = blurb[:217].rstrip() + "…"
    return blurb


def parse_prompt_file(path: Path, category: str) -> dict:
    text = path.read_text(encoding="utf-8")
    title = first_h1(text) or path.stem
    paste = extract_copy_paste(text)
    params = extract_params_from_table(text)
    if not params:
        params = extract_params_from_fence(paste)
    # Prefer **Вход:** / **Подстановка** mentions in prose for blurb params already handled
    slug = f"{category}-{path.stem}".lower().replace(" ", "-")
    return {
        "id": slug,
        "title": title,
        "category": category,
        "path": method_rel(path),
        "blurb": blurb_from_body(text, title),
        "params": params,
        "paste": paste,
        "hasPaste": paste is not None,
    }


def parse_manual(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    # Split on ## headings (skip H1)
    parts = re.split(r"(?m)^##\s+", text)
    frequent: list[dict] = []
    idx = 0
    for part in parts[1:]:
        lines = part.splitlines()
        if not lines:
            continue
        title = lines[0].strip()
        body = "\n".join(lines[1:])
        when_m = re.search(r"\*\*Когда:\*\*\s*(.+)", body)
        params_line_m = re.search(r"\*\*Параметры:\*\*\s*(.+)", body)
        fence_m = re.search(r"```(?:text)?\s*\n(.*?)```", body, re.S)
        paste = fence_m.group(1).rstrip("\n") if fence_m else None
        params: list[dict] = []
        if params_line_m:
            pl = params_line_m.group(1).strip()
            if pl.lower() not in ("нет.", "нет", "none", "—", "-"):
                # `$foo` — desc; `$bar` — desc
                for pm in re.finditer(
                    r"`?\$([A-Za-z0-9_]+)`?(?:\s*[—\-–:]\s*([^;`]+))?",
                    pl,
                ):
                    desc = (pm.group(2) or "подставь значение").strip().rstrip(";")
                    params.append({"name": f"${pm.group(1)}", "desc": desc})
        if not params:
            params = extract_params_from_fence(paste)
        # Stable unique ids — RU titles strip to empty under ascii-only slug
        fid = f"frequent-{idx:02d}"
        idx += 1
        frequent.append(
            {
                "id": fid,
                "title": title,
                "category": "frequent",
                "path": method_rel(path),
                "blurb": when_m.group(1).strip() if when_m else title,
                "params": params,
                "paste": paste,
                "hasPaste": paste is not None,
            }
        )
    return frequent


def should_skip(path: Path) -> bool:
    name = path.name
    if name in SKIP_NAMES:
        return True
    low = name.lower()
    return any(s in low for s in SKIP_SUBSTRINGS)


def build_catalog() -> dict:
    categories: dict[str, list] = {c: [] for c in CATEGORIES}
    for cat in CATEGORIES:
        d = PROMPTS / cat
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            if should_skip(path):
                continue
            categories[cat].append(parse_prompt_file(path, cat))
    # drop empty categories from output keys but keep order list
    return {
        "version": 1,
        "generatedFrom": "prompts/ + architect/prompts-manual.md",
        "frequent": parse_manual(MANUAL),
        "categoryOrder": list(CATEGORIES),
        "categories": categories,
    }


def main() -> int:
    catalog = build_catalog()
    payload = json.dumps(catalog, ensure_ascii=False, indent=2)
    OUT_JS.write_text(
        "/* auto-generated by build-dialog-restore-work-catalog.py — do not edit by hand */\n"
        "window.ZEYA888_WORK_CATALOG = "
        + payload
        + ";\n",
        encoding="utf-8",
    )
    n_freq = len(catalog["frequent"])
    n_cat = sum(len(v) for v in catalog["categories"].values())
    print(f"Wrote {OUT_JS} (frequent={n_freq}, prompts={n_cat})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
