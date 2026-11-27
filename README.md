# Topological dynamics of topological groups

**Website: <https://topologicaldynamics.org>** (MyST version; the LaTeX version
is at <https://topologicaldynamics.org/latex/>, the interactive proof tree of
all statements at <https://topologicaldynamics.org/proof-tree/>, and the proof
trees of the main results at <https://topologicaldynamics.org/proof-tree/main/>).
Every page links to its source file in this repository. To propose a change,
see [CONTRIBUTING.md](CONTRIBUTING.md).

A living, hypertextual encyclopaedia of the topological dynamics of
topological groups, with an emphasis on universal minimal flows.
Editor: Martino Lupini. **Prototype**: the seed entries were drafted with AI
assistance from the cited literature and still await expert review.

The same entries currently exist in two formats, so that the two toolchains
can be compared before one is chosen:

* `latex/`: LaTeX source, built into a website with
  [plasTeX](https://github.com/plastex/plastex) and Patrick Massot's
  dependency-graph plugin, plus a PDF. Every statement has a permanent
  four-character tag (Stacks project style), a tag page with its dependencies
  and its proof tree, and a node in the dependency graph.
* `myst/`: MyST Markdown source, built with Sphinx, myst-parser and
  sphinx-proof. Cross-references show a preview when you hover over them.

Both share `references.bib`, number every statement alike, and show on their
front page the same map of the encyclopaedia: the entries by strand, with the
entries each one rests on, and for each strand a map of its results.

## Entries

One file per entry in `latex/entries/` and `myst/entries/`, with the same file
name in both; the list of entries is the table of contents of the website.

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

The GitHub workflow builds everything on every push and publishes the `main`
branch to <https://topologicaldynamics.org> through GitHub Pages: the mystmd
build at the root and the LaTeX build under `/latex/`.

## Contributing

Changes are proposed by pull request and reviewed by the editor; see
[CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and for how to compare
revisions. Read [AGENTS.md](AGENTS.md) first. It gives the rules for content
(no unverified attributions), labels, dependencies, permanent tags and
bibliography, for human and AI contributors alike.
