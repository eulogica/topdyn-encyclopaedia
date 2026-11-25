# Topological dynamics of topological groups

A living, hypertextual encyclopaedia of the topological dynamics of
topological groups, with an emphasis on universal minimal flows.
Editor: Martino Lupini. **Prototype**: the seed entries were drafted with AI
assistance from the cited literature and still await expert review.

The same entries currently exist in two formats, so that the two toolchains
can be compared before one is chosen:

* `latex/`: LaTeX source, built into a website with
  [plasTeX](https://github.com/plastex/plastex) and Patrick Massot's
  dependency-graph plugin, plus a PDF. Every statement has a permanent
  four-character tag (Stacks project style), a tag page with its dependencies,
  and a node in the dependency graph.
* `myst/`: MyST Markdown source, built with Sphinx, myst-parser and
  sphinx-proof. Cross-references show a preview when you hover over them.

Both share `references.bib`.

## Entries

Flows · Minimal flows · The greatest ambit · The universal minimal flow ·
Extreme amenability · Veech's theorem · The Gromov–Milman theorem · Pestov's
theorems · The universal minimal flow of S∞ · The Kechris–Pestov–Todorcevic
correspondence · Metrizable universal minimal flows.

## Building locally

Requirements: TeX Live, Graphviz (with development headers), Python 3.

```sh
pip install plastex plastexdepgraph beautifulsoup4 \
            sphinx myst-parser sphinx-proof sphinx-book-theme sphinxcontrib-bibtex sphinx-tippy
(cd latex && ./build.sh)   # -> _site/latex/index.html and latex/main.pdf
(cd myst && ./build.sh)    # -> _site/myst/index.html
```

The MyST files also build with the newer MyST engine, mystmd (Jupyter Book 2),
which needs Node.js 22 or later:

```sh
pip install mystmd           # or: conda install -c conda-forge mystmd, or: npm install -g mystmd
cd myst
myst start                   # live preview at http://localhost:3000
myst build --html            # static site in myst/_build/html
```

The GitHub workflow builds all three on every push and keeps the result as a
downloadable artifact. Once the repository is public, it also publishes the
site on GitHub Pages.

## Contributing

Read [AGENTS.md](AGENTS.md) first. It gives the rules for content (no
unverified attributions), labels, dependencies, permanent tags and
bibliography, for human and AI contributors alike.
