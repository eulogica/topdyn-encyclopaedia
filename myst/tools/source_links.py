#!/usr/bin/env python3
"""Add links to the GitHub source of every MyST page.

Run by the build workflow, before `myst build`, on the checked-out working
copy. It appends to each page a short footer that links to the page's MyST
file and to its LaTeX twin on GitHub, with their history and the GitHub
editor. The files in the repository never contain the footer, so authors do
not need to maintain it. Running the script twice does nothing the second time.

Usage: python3 tools/source_links.py        (from the myst/ folder or anywhere)
"""
import os
from pathlib import Path

MYST = Path(__file__).resolve().parent.parent
ROOT = MYST.parent
if os.environ.get("GITHUB_REPOSITORY"):
    REPO = f"https://github.com/{os.environ['GITHUB_REPOSITORY']}"
else:
    REPO = "https://github.com/eulogica/topdyn-encyclopaedia"
BRANCH = "main"
MARK = "<!-- source-links -->"


def links(path):
    return (f"[`{path}`]({REPO}/blob/{BRANCH}/{path}) "
            f"([history]({REPO}/commits/{BRANCH}/{path}), "
            f"[edit]({REPO}/edit/{BRANCH}/{path}))")


def main():
    pages = [MYST / "index.md"] + sorted((MYST / "entries").glob("*.md"))
    added = 0
    for page in pages:
        text = page.read_text()
        if MARK in text:
            continue
        added += 1
        rel = page.relative_to(ROOT).as_posix()
        stem = "00-about" if page.name == "index.md" else page.stem
        tex = f"latex/entries/{stem}.tex"
        sources = links(rel)
        if (ROOT / tex).exists():
            sources += f" and {links(tex)}"
        footer = (f"\n\n{MARK}\n\n---\n\n"
                  f"*Source of this page:* {sources}. To propose a change, see "
                  f"[how to contribute]({REPO}/blob/{BRANCH}/CONTRIBUTING.md).\n")
        page.write_text(text.rstrip("\n") + footer)
    print(f"Added source links to {added} of {len(pages)} pages")


if __name__ == "__main__":
    main()
