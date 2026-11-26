# Sphinx configuration for the MyST Markdown version of the encyclopaedia.
# Build: ./build.sh   (output in ../_site/myst)
project = "Topological dynamics of topological groups"
author = "Martino Lupini (editor)"
copyright = "2026"

extensions = [
    "myst_parser",          # MyST Markdown
    "sphinx_proof",         # {prf:theorem}, {prf:definition}, ... blocks
    "sphinxcontrib.bibtex", # {cite} roles and the bibliography
    "sphinx_tippy",         # hover previews of cross-references
]

myst_enable_extensions = ["dollarmath", "amsmath", "colon_fence", "deflist"]
myst_heading_anchors = 2

bibtex_bibfiles = ["../references.bib"]
bibtex_default_style = "plain"
bibtex_reference_style = "label"

# One counter for all statement types, as in the LaTeX version.
prf_realtyp_to_countertyp = {
    "definition": "theorem", "proposition": "theorem", "corollary": "theorem",
    "lemma": "theorem", "remark": "theorem", "example": "theorem", "theorem": "theorem",
    "conjecture": "theorem",
}

numfig = True
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"
tippy_enable_mathjax = True
tippy_anchor_parent_selector = "article.bd-article"

html_theme = "sphinx_book_theme"
html_title = "Topological dynamics of topological groups"
html_theme_options = {
    "show_toc_level": 1,
    "home_page_in_toc": True,
}
html_static_path = []
exclude_patterns = ["_build", "build.sh"]

# SVG output needs no web fonts (the preview pages' security policy blocks them);
# a local font cache keeps formulas intact inside hover previews.
mathjax3_config = {"svg": {"fontCache": "local"}}
