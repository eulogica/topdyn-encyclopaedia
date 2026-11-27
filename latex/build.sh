#!/usr/bin/env bash
# Build the LaTeX version: PDF (pdflatex + bibtex) and website (plasTeX).
# Output: ../_site/latex/  (open index.html)
# Requirements: TeX Live, Graphviz, Python 3 with plasTeX, plastexdepgraph, beautifulsoup4.
set -euo pipefail
cd "$(dirname "$0")"
OUT="${1:-../_site/latex}"
export TEXINPUTS=".:" BIBINPUTS="..:"
# Figures: PDF copies of ../figures/*.svg for pdflatex, PNG copies for plasTeX (whose
# pages postprocess.py then points back to the SVG files).
mkdir -p _figures
for svg in ../figures/*.svg; do
  name="$(basename "$svg" .svg)"
  rsvg-convert -f pdf -o "_figures/$name.pdf" "$svg"
  rsvg-convert -f png -o "_figures/$name.png" "$svg"
done

python3 tools/tags.py assign          # gives new \label{...} a permanent tag (append-only)

# PDF, and the .bbl file that plasTeX reads for the bibliography.
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
bibtex main >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null

# Website.
rm -rf "$OUT"
plastex --renderer=HTML5 --dir="$OUT" --split-level=1 --plugins plastexdepgraph \
  --mathjax-url="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" main.tex >/dev/null
python3 tools/postprocess.py "$OUT"
cp main.pdf "$OUT/encyclopaedia.pdf"
echo "Built $OUT"
