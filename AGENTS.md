# Instructions for authors and AI agents

This file is the shared brief for anyone, human or AI, who edits this
repository: Claude, Codex, Copilot, Cursor, Gemini or a coauthor. Read it before
changing anything. (CLAUDE.md and similar files should simply point here.)

## What this is

A living, hypertextual encyclopaedia of the topological dynamics of
topological groups, with an emphasis on universal minimal flows. Editor:
Martino Lupini. It is currently a **prototype with two parallel versions of the
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
  `thm:`, `prop:`, `cor:`, `lem:`, `rem:`, `ex:`, followed by a descriptive
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
* The same files build with two engines:
  * Sphinx (older engine, configured in `myst/conf.py`):
    `cd myst && ./build.sh` → `_site/myst/index.html`.
  * mystmd (newer engine, Jupyter Book 2, configured in `myst/myst.yml`):
    `cd myst && myst start` for a live preview, `myst build --html` for a
    static site in `myst/_build/html`. New entries must be added both to the
    toctree in `index.md` (Sphinx) and to `toc:` in `myst.yml` (mystmd).
    mystmd warns about the toctree directive in `index.md`; that warning is
    expected while both engines are used.

## Workflow

* The contributor workflow, for people, is in [CONTRIBUTING.md](CONTRIBUTING.md).
* Every published page links to its source files on GitHub. On the LaTeX site
  `latex/tools/postprocess.py` adds these links; on the mystmd site the
  `github:` field of `myst/myst.yml` adds an edit link and
  `myst/tools/source_links.py`, run by the workflow before `myst build`, adds
  a footer. Neither needs maintaining by hand, provided the two versions of an
  entry keep the same file name.
* **Every push to `main` is published** at <https://topologicaldynamics.org>
  (mystmd build at the root, LaTeX build at `/latex/`). Work on a branch and
  open a pull request; the build workflow in `.github/workflows/build.yml` must
  pass before merging.
* Do not commit build output (`_site/`, `*.aux`, `main.pdf`, ...).
