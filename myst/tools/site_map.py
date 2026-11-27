#!/usr/bin/env python3
"""Number the MyST statements as in the LaTeX version, and draw the map of the
encyclopaedia on the front page.

Run by the build workflow, before `myst build`, on the checked-out working copy
(the workflow restores the files afterwards). The files in the repository never
contain what it adds, so authors do not maintain it. Running it twice does
nothing the second time.

  * Every statement whose label has a LaTeX twin gets that twin's number, as
    `:enumerator: 5.2`, so that both versions number it alike and a reference
    from another page reads "Proposition 3.2" rather than "Proposition 1".
    Proofs are left unnumbered, as in the LaTeX version.
  * The line "% map-of-the-encyclopaedia" in index.md becomes the map, drawn by
    widgets/encyclopaedia-map.mjs from data that latex/tools/site_map.py reads
    from the LaTeX sources.

Usage: python3 tools/site_map.py        (from the myst/ folder or anywhere)
"""
import json
import re
import sys
from pathlib import Path

MYST = Path(__file__).resolve().parent.parent
ROOT = MYST.parent
sys.path.insert(0, str(ROOT / "latex" / "tools"))
import site_map  # noqa: E402  (latex/tools/site_map.py)

MARK = "% map-of-the-encyclopaedia"
DIRECTIVE = re.compile(r"^:::\{prf:(\w+)\}")
OPTION = re.compile(r"^:(\w+):\s*(.*)$")


def number_statements(path, numbers):
    """Add :enumerator: to labelled statements and :enumerated: false to proofs."""
    lines = path.read_text().split("\n")
    out, changed, missing = [], 0, []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = DIRECTIVE.match(line)
        if not m:
            i += 1
            continue
        kind, j, options = m.group(1), i + 1, {}
        while j < len(lines) and OPTION.match(lines[j]):
            k, v = OPTION.match(lines[j]).groups()
            options[k] = v.strip()
            j += 1
        out += lines[i + 1:j]
        if kind == "proof":
            if "enumerated" not in options and "nonumber" not in options:
                out.append(":enumerated: false")
                changed += 1
        elif "label" in options and "enumerator" not in options:
            tex = options["label"].replace("-", ":", 1)
            if tex in numbers:
                out.append(f":enumerator: {numbers[tex]}")
                changed += 1
            else:
                missing.append(options["label"])
        i = j
    if changed:
        path.write_text("\n".join(out))
    return changed, missing


def main():
    src = site_map.read(ROOT / "latex")
    numbers = {s["label"]: s["num"] for s in src["statements"]}
    numbers.update({alias: numbers[label] for alias, label in src["aliases"].items()})
    total, missing = 0, []
    for path in sorted((MYST / "entries").glob("*.md")):
        changed, lost = number_statements(path, numbers)
        total += changed
        missing += lost
    print(f"Numbered {total} MyST statements and proofs as in the LaTeX version")
    if missing:
        print("No LaTeX twin, left as numbered by mystmd:", ", ".join(missing))

    index = MYST / "index.md"
    text = index.read_text()
    if MARK in text:
        data = json.dumps({"data": site_map.map_data(src, "myst")}, ensure_ascii=False)
        block = ("## Map of the encyclopaedia\n\n"
                 ":::{anywidget} ./widgets/encyclopaedia-map.mjs\n"
                 ":class: col-page-right\n" + data + "\n:::")
        index.write_text(text.replace(MARK, block, 1))
        print("Drew the map of the encyclopaedia in index.md")


if __name__ == "__main__":
    main()
