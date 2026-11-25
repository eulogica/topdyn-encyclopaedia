#!/usr/bin/env bash
# Build the MyST Markdown version with Sphinx (myst-parser + sphinx-proof).
# Output: ../_site/myst/  (open index.html)
# Requirements: Python 3 with sphinx, myst-parser, sphinx-proof, sphinx-book-theme,
#               sphinxcontrib-bibtex, sphinx-tippy.
#
# Note: the same Markdown can also be built with the newer `mystmd` engine
# (Jupyter Book 2) after small syntax changes; see ../AGENTS.md.
set -euo pipefail
cd "$(dirname "$0")"
OUT="${1:-../_site/myst}"
rm -rf "$OUT" _build
sphinx-build -q -b html -d _build/doctrees . "$OUT"
rm -rf _build
# sphinx-tippy typesets formulas in hover previews before the preview is on
# screen, which breaks MathJax's SVG output; typeset once it is shown instead.
find "$OUT/_static/tippy" -name '*.js' -exec \
  sed -i 's/onShow(instance) {MathJax.typesetPromise/onShown(instance) {MathJax.typesetPromise/' {} +
echo "Built $OUT"
