#!/usr/bin/env python3
"""Fail if raw TeX shows anywhere on the built site.

Readers should never see TeX source. Maths is typeset by KaTeX on the MyST site and
by MathJax on the LaTeX site, and the places that show text as it is (browser-tab
titles, tooltips, labels for screen readers) carry Unicode instead (see untex in
site_map.py). This check reads every page of the built site, both versions and the
proof trees, and lists any TeX left where readers see it:

  * the browser-tab title, the page description, and the title, aria-label and alt
    attributes;
  * the text, outside typeset maths, code and scripts. On the pages that use
    MathJax (the LaTeX site and the proof trees) the maths is still TeX in the HTML,
    between \\( \\) or in displayed environments, until MathJax typesets it in the
    browser, so that is left out too.

It catches, for instance, maths in a MyST page title, a stray \\label left in a
MyST file, or a bibliography entry whose maths the citation renderer prints as TeX.

Usage: python3 latex/tools/check_site.py SITE    (the folder the workflow publishes)
"""
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

# A command (\label, \mathbb), \( \) or \[ \], $...$, or a braced sub- or superscript.
TEX = re.compile(r"\\[A-Za-z]{2,}|\\[()\[\]]|\$(?!\s)[^$]+?(?<!\s)\$|[_^]\{")
# Maths that MathJax typesets on the LaTeX site.
MATHJAX = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]|\$\$.*?\$\$|"
                     r"\\begin\{([a-z]+\*?)\}.*?\\end\{\1\}", re.S)
NOT_TEXT = "head, script, style, code, pre, textarea, .katex, mjx-container, .displaymath"
ATTRIBUTES = ("title", "aria-label", "alt")
LONGEST = 40  # problems listed in full; the rest are counted


def problems(path):
    html = path.read_text(errors="replace")
    mathjax = "mathjax" in html.lower()
    soup = BeautifulSoup(html, "html.parser")
    found = []
    shown = []
    if soup.title and soup.title.string:
        shown.append(("tab title", soup.title.string))
    for meta in soup.find_all("meta", content=True):
        if re.search(r"title|description", meta.get("name", "") + meta.get("property", "")):
            shown.append((meta.get("name") or meta.get("property"), meta["content"]))
    for el in soup.find_all(True):
        for attr in ATTRIBUTES:
            if isinstance(el.get(attr), str):
                shown.append((f"{attr} of <{el.name}>", el[attr]))
    for where, value in shown:
        if TEX.search(value):
            found.append(f"{where}: {value.strip()[:100]}")
    for el in soup.select(NOT_TEXT):
        el.decompose()
    for node in soup.find_all(string=True):
        text = MATHJAX.sub(" ", str(node)) if mathjax else str(node)
        m = TEX.search(text)
        if m:
            found.append("text: …" + text[max(0, m.start() - 50):m.end() + 40].strip()
                         .replace("\n", " ") + "…")
    return found


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    site = Path(sys.argv[1])
    pages = sorted(site.rglob("*.html"))
    report = []
    for path in pages:
        rel = path.relative_to(site)
        for problem in problems(path):
            report.append(f"{rel}: {problem}")
    if report:
        print(f"Raw TeX on {len({r.split(':')[0] for r in report})} of {len(pages)} pages:")
        for line in report[:LONGEST]:
            print("  " + line)
        if len(report) > LONGEST:
            print(f"  … and {len(report) - LONGEST} more")
        print("Write maths in titles and references.bib as TeX; see AGENTS.md for where "
              "the build turns it into Unicode.")
        sys.exit(1)
    print(f"No raw TeX on the {len(pages)} pages of {site}")


if __name__ == "__main__":
    main()
