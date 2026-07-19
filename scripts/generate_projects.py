#!/usr/bin/env python3
"""Generate _data/projects.json from the project tables in index.md.

Runs before the Jekyll build (see .github/workflows/pages.yml). Each markdown
table row with a linked project becomes one entry; _includes/projects-jsonld.html
turns the entries into schema.org JSON-LD on the homepage. Rows without a URL
are skipped on purpose — search engines need something to anchor to.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "index.md"
OUTPUT = ROOT / "_data" / "projects.json"

# Below this, assume the table format drifted and the parser broke,
# rather than silently shipping a near-empty ItemList.
MIN_EXPECTED = 20

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
TAG_RE = re.compile(r"<[^>]+>")
SEPARATOR_RE = re.compile(r"^\|[\s|:-]+$")

# Tokens from a tech cell that count as a programmingLanguage (lowercased).
KNOWN_LANGUAGES = {
    "c#", "python", "javascript", "vanilla javascript", "java", "lua",
    "ruby", "kotlin", "haskell", "autohotkey",
}


def clean_text(cell: str) -> str:
    """Markdown/HTML cell -> plain text."""
    cell = IMAGE_RE.sub("", cell)
    cell = LINK_RE.sub(r"\1", cell)
    cell = TAG_RE.sub("", cell)
    return re.sub(r"\s+", " ", cell).strip()


def has_media(cell: str) -> bool:
    return "![" in cell or "<img" in cell.lower() or "<video" in cell.lower()


def parse_tech(cells: list[str]) -> list[str]:
    """The last cell, but only when it reads as a tech list rather than
    prose or images (several rows use the trailing cell as extra description)."""
    if len(cells) < 3:
        return []
    last = cells[-1]
    if has_media(last):
        return []
    text = clean_text(last)
    if not text or text.endswith("."):
        return []
    tokens = [t.strip() for t in re.split(r"[,·]", text) if t.strip()]
    if not tokens:
        return []
    if any(len(t.split()) > 6 for t in tokens):
        return []
    if len(tokens) == 1 and len(tokens[0].split()) > 3:
        return []
    return tokens


def schema_type(url: str) -> str:
    if "github.com" in url:
        return "SoftwareSourceCode"
    if "chrisandcodie.com" in url or "chrisincode.com" in url:
        return "WebSite"
    # Not SoftwareApplication: Google's rich-result rules demand offers/
    # ratings/OS for that type, which professional project entries can't honestly provide.
    return "CreativeWork"


def parse(lines: list[str]) -> list[dict]:
    projects: list[dict] = []
    seen_urls: set[str] = set()
    section = ""
    category = ""

    for i, raw in enumerate(lines):
        line = raw.strip()
        if line.startswith("## "):
            section = clean_text(line.lstrip("# "))
            continue
        if not line.startswith("|") or SEPARATOR_RE.match(line):
            continue

        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        if SEPARATOR_RE.match(nxt):  # header row: first cell names the table
            category = clean_text(line.strip("|").split("|")[0])
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]
        while cells and not cells[-1]:
            cells.pop()
        if not cells:
            continue

        link = LINK_RE.search(cells[0])
        if not link:
            continue  # URL-less rows (kiosk, member app, WIPs) are skipped
        url = link.group(2)
        if url in seen_urls:
            continue  # e.g. onepiece_dl is listed under both Manga and Discord BOT
        seen_urls.add(url)

        tech = parse_tech(cells)
        entry = {
            "name": clean_text(cells[0]),
            "url": url,
            "type": schema_type(url),
            "category": " / ".join(p for p in (section, category) if p),
        }
        description = clean_text(cells[1]) if len(cells) > 1 else ""
        if description:
            entry["description"] = description
        if tech:
            entry["tech"] = tech
            languages = [t for t in tech if t.lower() in KNOWN_LANGUAGES]
            if languages:
                entry["languages"] = languages
        projects.append(entry)

    return projects


def main() -> int:
    projects = parse(SOURCE.read_text(encoding="utf-8").splitlines())
    if len(projects) < MIN_EXPECTED:
        print(
            f"error: only parsed {len(projects)} projects from {SOURCE.name} "
            f"(expected at least {MIN_EXPECTED}) — did the table format change?",
            file=sys.stderr,
        )
        return 1
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(projects, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(projects)} projects to {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
