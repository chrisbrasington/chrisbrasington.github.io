#!/usr/bin/env python3
"""Compile index.template.html into a single self-contained index.html.

Everything that used to cost a round-trip (stylesheet, three scripts, two icons)
gets inlined, and the link list is rendered to static markup instead of being
built by JavaScript after load. One request, nothing to reflow.

Edit the sources - _build/index.template.html, scripts/*.js, static/styles/style.css -
then run `python3 _build/build.py` from home/. Do not hand-edit index.html;
it is generated and will be overwritten.
"""

import base64
import hashlib
import html
import json
import re
import sys
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent          # home/_build
ROOT = HERE.parent                              # home
TEMPLATE = HERE / "index.template.html"
OUTPUT = ROOT / "index.html"
SW_TEMPLATE = HERE / "sw.template.js"
SW_OUTPUT = ROOT / "sw.js"

STYLE = ROOT / "static/styles/style.css"
LINKS = ROOT / "scripts/links.js"
SEARCH = ROOT / "scripts/get_search_engine.js"
COLORSCHEME = ROOT / "scripts/set_colorscheme.js"
IMAGE_DIR = ROOT / "static/images"
ICON_DIR = ROOT / "static/icons"

IMAGE_SUFFIXES = {".webp", ".jpg", ".jpeg", ".png", ".avif", ".gif"}


def read(path):
    if not path.exists():
        sys.exit(f"build: missing source file {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def indent(text, spaces):
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else line for line in text.splitlines())


def parse_links():
    """Pull the linkData object literal out of links.js and parse it as JSON."""
    source = read(LINKS)
    start = source.index("{")
    end = source.rindex("}") + 1
    body = source[start:end]
    body = re.sub(r",(\s*[}\]])", r"\1", body)  # tolerate trailing commas
    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        sys.exit(f"build: could not parse linkData in links.js - {exc}")


def render_links(link_data):
    out = []
    for section, links in link_data.items():
        out.append("<ul>")
        out.append(f"    <li>{html.escape(section)}</li>")
        for link in links:
            cls = ' class="hidden-link"' if link.get("hidden") else ""
            url = html.escape(link["url"], quote=True)
            name = html.escape(link["name"])
            out.append(f'    <li{cls}><a href="{url}">{name}</a></li>')
        out.append("</ul>")
    return "\n".join(out)


def list_images():
    files = sorted(
        p.name for p in IMAGE_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES
    )
    if not files:
        sys.exit(f"build: no images found in {IMAGE_DIR.relative_to(ROOT)}")
    return files


def inline_svg(name):
    """Return an svg file as a data URI, so icons cost no extra request."""
    svg = read(ICON_DIR / name)
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.DOTALL).strip()
    svg = re.sub(r"\s+", " ", svg)
    if len(svg) > 4096:  # big enough that base64 beats percent-encoding
        encoded = base64.b64encode(svg.encode()).decode()
        return f"data:image/svg+xml;base64,{encoded}"
    return "data:image/svg+xml," + urllib.parse.quote(svg, safe="")


def build_service_worker(images):
    """Precache the font, icons and every hero image, keyed by their content."""
    precache = ["./"]
    precache += [f"static/images/{name}" for name in images]
    precache += ["static/fonts/hack.woff2", "static/icons/icon.svg"]

    digest = hashlib.sha256()
    for asset in precache[1:]:
        digest.update((ROOT / asset).read_bytes())
    digest.update(OUTPUT.read_bytes())

    sw = read(SW_TEMPLATE)
    sw = sw.replace("{{VERSION}}", digest.hexdigest()[:12])
    sw = sw.replace("{{PRECACHE}}", json.dumps(precache, indent=4))
    SW_OUTPUT.write_text(sw, encoding="utf-8")


def main():
    page = read(TEMPLATE)

    replacements = {
        "{{STYLE}}": indent(read(STYLE).strip(), 8),
        "{{SCRIPT_COLORSCHEME}}": indent(read(COLORSCHEME).strip(), 8),
        "{{SCRIPT_SEARCH}}": indent(read(SEARCH).strip(), 12),
        "{{LINKS}}": indent(render_links(parse_links()), 12),
        "{{IMAGES}}": json.dumps(list_images()),
        "{{ICON_CLOSE}}": inline_svg("close.svg"),
        "{{ICON_SETTINGS}}": inline_svg("settings.svg"),
    }

    for token, value in replacements.items():
        if token not in page:
            sys.exit(f"build: {token} is not in index.template.html")
        page = page.replace(token, value)

    leftover = re.findall(r"\{\{[A-Z_]+\}\}", page)
    if leftover:
        sys.exit(f"build: unfilled placeholders {leftover}")

    OUTPUT.write_text(page, encoding="utf-8")

    images = list_images()
    build_service_worker(images)

    print(f"built {OUTPUT.relative_to(ROOT)}  ({len(page.encode()) / 1024:.1f} KB, "
          f"{len(images)} images)")
    print(f"built {SW_OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
