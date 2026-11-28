# Instructions for authors and AI agents

This file is the shared brief for anyone, human or AI, who edits this
repository: Claude, Codex, Copilot, Cursor, Gemini or a coauthor. Read it before
changing anything. (CLAUDE.md and similar files should simply point here.)

## What this is

A living, hypertextual encyclopaedia of the topological dynamics of
topological groups, with an emphasis on universal minimal flows. Editor:
LogicArtificialis. It is currently a **prototype with two parallel versions of the
same entries**, kept so the two toolchains can be compared:

| Folder   | Source format  | Built with                         | Extras                                         |
|----------|----------------|------------------------------------|------------------------------------------------|
| `latex/` | LaTeX          | plasTeX + plastexdepgraph, pdflatex | permanent tags, dependency graph, proof trees, PDF |
| `myst/`  | MyST Markdown  | Sphinx + myst-parser + sphinx-proof | hover previews of references, search           |

Both use `references.bib`. When one version is chosen, delete the other and
this table.

## Rules for content

1. **Never invent mathematics or attributions.** Every theorem attributed to
   someone must be checked against the original paper (statement, hypotheses,
   year) and cited with a key from `references.bib`. If you cannot check a
   claim, do not add it; write it in an issue instead.
2. **Bibliography.** Add a BibTeX entry only after checking it against the
   publisher, MathSciNet, zbMATH or arXiv. Give a DOI only if you confirmed it.
3. **Keep the two versions in sync** while both exist: the same entry, the same
   statements, the same wording.
4. Language: British English ("neighbourhood", "colouring", "encyclopaedia").
5. Conventions fixed in the entries: topological groups and compact spaces are
   Hausdorff; actions are left actions; uniformities as in the definition of
   right uniformly continuous functions (`def:ruc` / `def-ruc`).
6. Seed entries were drafted with AI assistance and are marked as not yet
   reviewed in the About section. Keep that note accurate.

## LaTeX version (`latex/`)

* One file per entry in `latex/entries/`, included from `latex/main.tex`.
* Every section and statement has a `\label`. Prefixes: `sec:`, `def:`,
  `thm:`, `prop:`, `cor:`, `lem:`, `rem:`, `ex:` (and `fig:` for figures),
  followed by a descriptive
  slug (`thm:ellis`, not `thm:5-2`).
* Every statement lists what it depends on with `\uses{label1, label2}` right
  after `\label`, and a proof lists what it uses with its own `\uses` (after
  `\proves{label}` when it does not follow its statement). These build the
  dependency graph and, on tag pages, the "Uses / Used by" lists and the
  proof tree. The proof tree also shows the results of other works that a
  statement or proof cites with a locator, as in `\cite[Theorem~2.1]{Key}`;
  a citation after "see also" or "compare" counts as a pointer and is left
  out. The same data build the interactive proof tree of the whole
  encyclopaedia at `/proof-tree/` (`latex/tools/proof_tree_page.py`, called by
  `postprocess.py`), and the page `/proof-tree/main/` of the proof trees of the
  main results, the theorems that no other statement uses. A theorem that is
  really a step in a later proof becomes a main result if that proof does not
  list it in its `\uses`.
* Only standard LaTeX and AMS commands inside math. Do **not** define macros
  for use in formulas: the web version is rendered by MathJax, which does not
  see the preamble.
* Environments: `definition`, `theorem`, `proposition`, `corollary`, `lemma`
  (add with `\newtheorem` if needed), `remark`, `example`, `proof`.
* **Permanent tags** (`latex/tags`). Each label gets a four-character tag such
  as `000I`, assigned automatically by `latex/tools/tags.py assign` (run by
  `build.sh`). The file is **append-only**: never edit, reorder, reuse or
  delete a line, even if a statement is moved, renumbered, reworded or
  removed. Commit the updated `tags` file together with the new labels.
* **One `\label` per item.** plasTeX keeps only the last label of an item, so a
  `\uses` of another one is lost and the dependency drops out of the proof
  trees. `tags.py check` fails on an item with two labels.
* Build: `cd latex && ./build.sh` → `_site/latex/index.html` and
  `latex/main.pdf`.

## MyST version (`myst/`)

* One Markdown file per entry in `myst/entries/`, listed in the toctree of
  `myst/index.md`.
* Statements are `:::{prf:theorem} Title` blocks (also `prf:definition`,
  `prf:proposition`, `prf:corollary`, `prf:lemma`, `prf:remark`,
  `prf:example`, `prf:proof`) with a `:label:` line. Labels use the LaTeX label
  with `-` instead of `:` (`thm-ellis`).
* Cross-references: ``{prf:ref}`thm-ellis` `` for statements, `[](#sec-umf)`
  for sections. Citations: ``{cite}`Ellis1960` ``.
* Math between `$...$` or `$$...$$`, standard LaTeX only.
* There are no dependency lists or permanent tags in this version.
* Do not write numbers in the MyST files. Before `myst build`,
  `myst/tools/site_map.py` gives every statement the number of its LaTeX twin
  (`:enumerator: 5.2`) and leaves proofs unnumbered, so that both versions
  number statements alike and a reference to another page reads
  "Proposition 3.2". A statement whose label has no LaTeX twin keeps mystmd's
  own numbering, which starts again on every page.
* Do not write lists of dependencies or links to proofs by hand either. The
  same step labels every proof `proof-<label>` (from its LaTeX twin: the proofs
  of an entry come in the same order in both versions) and adds after every
  statement a short block of links, from the `\uses` lists: what the statement
  and its proof use, what uses it, where its proof is when that is in another
  entry, its tag and its proof tree. On the LaTeX site `postprocess.py` adds
  the same block. Its style is in `myst/encyclopaedia.css`.
* In the Proofs entries, a proof that comes straight after its statement is
  folded (click "Proof" to open it), while the proofs placed elsewhere, such as
  those of an entry's main results, stay open. Each Proofs entry opens with the
  statements of other entries that it proves, with links to their proofs and
  proof trees, and with its roadmap: its subsections in order, with an arrow
  from one subsection to each subsection that uses one of its results
  (`myst/widgets/entry-roadmap.mjs`, from `roadmap()` in
  `latex/tools/site_map.py`). A result stated in one subsection and proved in
  another, such as a main result, counts as part of the subsection of its proof.
  All of this is added at build time from the LaTeX sources, by
  `myst/tools/site_map.py` and `postprocess.py`: do not add `:class: dropdown`
  or such lists by hand. Give every subsection of a Proofs entry a `\label`, so
  that the roadmap can link to it.
* Write maths in titles and in `references.bib` as TeX, as everywhere else.
  mystmd shows page titles and bibliography entries as plain text, so the same
  step writes the maths in MyST page titles in Unicode ("S∞") and has the build
  read a copy of `references.bib` with its maths in Unicode. `postprocess.py`
  does the same for browser-tab titles and tooltips on the LaTeX site. Never
  put Unicode maths in `references.bib` itself: pdflatex rejects characters
  such as 𝕊 or ∞.
* The front page of both versions shows the map of the encyclopaedia, drawn by
  `myst/widgets/encyclopaedia-map.mjs`: the entries by strand, and for each
  strand a map of its results. Its data come from the LaTeX sources through
  `latex/tools/site_map.py`, whose `STRANDS` list names the first entry of each
  strand; a new entry joins the strand of the entry before it. In
  `myst/index.md` the line `% map-of-the-encyclopaedia` marks where the map
  goes; on the LaTeX site `postprocess.py` puts it under the title.
* The same files build with two engines:
  * Sphinx (older engine, configured in `myst/conf.py`):
    `cd myst && ./build.sh` → `_site/myst/index.html`.
  * mystmd (newer engine, Jupyter Book 2, configured in `myst/myst.yml`):
    `cd myst && myst start` for a live preview, `myst build --html` for a
    static site in `myst/_build/html`. New entries must be added both to the
    toctree in `index.md` (Sphinx) and to `toc:` in `myst.yml` (mystmd).
    mystmd warns about the toctree directive in `index.md`; that warning is
    expected while both engines are used.

## Figures (both versions)

* Figures are SVG files in `figures/`, shared by both versions and drawn by
  `figures/make_figures.py` (standard library only; run
  `python3 figures/make_figures.py` and commit the SVGs it writes). Edit the
  script, not the SVGs. Each SVG has a `<title>`, used as the alt text on both
  sites.
* LaTeX: a `figure` environment with `\includegraphics[width=\linewidth]{NAME}`,
  a `\caption`, `\label{fig:NAME}` and `\illustrates{label1, label2}`, the
  statements it illustrates (their proofs, or the statements themselves for a
  definition or an example). `build.sh` converts the SVGs to PDF
  and PNG with `rsvg-convert` in `latex/_figures/` (not committed) for pdflatex
  and plasTeX, and `postprocess.py` puts the SVG back on the web pages.
  Figures are numbered by section (Figure 12.1).
* MyST: the twin is a `:::{figure} ../../figures/NAME.svg` block with
  `:name: fig-NAME`, `:figclass: enc-figure`, `:alt:` (the SVG's title) and
  `:width: 100%`, and the same caption. `myst/tools/site_map.py` gives it the
  number of its LaTeX twin. Do not write numbers.
* Do not link figures from the statements by hand: both builds add "Illustrated
  in Fig. N" to the links block of every statement in its `\illustrates`.
* A figure `fig:NAME` gets an interactive version when there is a widget
  `myst/widgets/NAME.mjs` (an anywidget module that needs no data): both builds
  put it under the figure. The figure must make sense without it, as in the PDF.
* The Proofs entries reproduce preprints. A figure there is a supplement placed
  after the proof it illustrates, never a change to the reproduced text, and
  its caption ends with "(Illustration added for the encyclopaedia.)".
* Figures follow the rules for content: they show what the text says, with its
  notation, and add no claims of their own.
* The editor's mark, monogram, seal and emblem are not figures: they are images in
  `images/logicartificialis/`, taken from <https://logicartificialis.org> and
  resized, with no number, label or tag. The mark (`mark.svg`, and `mark.ico`
  drawn from it, since mystmd serves its favicon as `favicon.ico`) is the
  favicon and the logo in the header of both sites; the monogram is under the
  editor's name on the front page and the title page; the seal and the
  "Meaning guides" emblem stand side by side, without captions, at the end of
  the front page (MyST: a `list-table` with class `la-emblems`; LaTeX:
  `\emblem{file}{alt}`, whose alt text `postprocess.py` puts on the web page).

## Workflow

* The contributor workflow, for people, is in [CONTRIBUTING.md](CONTRIBUTING.md).
* Every published page links to its source files on GitHub. On the LaTeX site
  `latex/tools/postprocess.py` adds these links; on the mystmd site the
  `github:` field of `myst/myst.yml` adds an edit link and
  `myst/tools/source_links.py`, run by the workflow before `myst build`, adds
  a footer. Neither needs maintaining by hand, provided the two versions of an
  entry keep the same file name. The workflow runs `myst/tools/site_map.py` at
  the same point, then restores the MyST files, so the Sphinx check sees them
  as they are in the repository.
* **Every push to `main` is published** at <https://topologicaldynamics.org>
  (mystmd build at the root, LaTeX build at `/latex/`). Work on a branch and
  open a pull request; the build workflow in `.github/workflows/build.yml` must
  pass before merging.
* Besides building, the workflow fails if a label has no tag or an item has two
  labels (`latex/tools/tags.py check`); if a MyST statement has no LaTeX twin or
  the proofs of an entry are not in the LaTeX order (`myst/tools/site_map.py`);
  or if raw TeX shows anywhere on the built site, such as maths in a MyST page
  title or a stray `\label` in a MyST file (`latex/tools/check_site.py`).
* Do not commit build output (`_site/`, `*.aux`, `main.pdf`, ...).
