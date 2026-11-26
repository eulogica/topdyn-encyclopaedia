# Contributing to the encyclopaedia

The encyclopaedia at <https://topologicaldynamics.org> is built from this
repository. Every change goes through a pull request. The editor, Martino
Lupini, reviews it, and the site is rebuilt automatically when the change is
merged into `main`. Comments, corrections and new entries are welcome from
invited collaborators and from anyone with a GitHub account.

Before writing, read [AGENTS.md](AGENTS.md). It is the shared brief for human
and AI contributors. It explains the rules for attributions and references,
labels and permanent tags, and how to keep the two versions in sync.

## Where each page comes from

Every page links to its sources:

* **MyST version** (the site root). The pencil icon next to the title opens the
  page's Markdown file in the GitHub editor. The footer of each page links to
  the MyST file, to its LaTeX twin, and to their histories.
* **LaTeX version** (`/latex/`). Each section page shows its `.tex` and `.md`
  files under the title, with links to their histories and to the GitHub
  editor. Each tag page links to the exact line where the statement is
  written.

The two versions of an entry share a file name:
`latex/entries/04-universal-minimal-flow.tex` and
`myst/entries/04-universal-minimal-flow.md`. The About section is
`latex/entries/00-about.tex` and `myst/index.md`. The bibliography for both is
`references.bib`.

## Proposing a change

### Small corrections, in the browser

1. Click the pencil icon, or an "edit" link in the source links of the page.
2. Make the change on GitHub. Make the same change in the twin file of the
   other version.
3. Choose **Propose changes**, then **Create pull request**. Describe what you
   changed and why, with references for any new mathematical claim.

If you are not a collaborator, GitHub first makes a copy (a fork) of the
repository under your account, and the pull request comes from there.

### Larger changes, on your computer

```sh
git clone https://github.com/eulogica/topdyn-encyclopaedia.git
cd topdyn-encyclopaedia
git switch -c my-change          # one branch per topic
# edit latex/entries/*.tex, myst/entries/*.md and references.bib
(cd latex && ./build.sh)         # LaTeX site and PDF; also assigns new permanent tags
(cd myst && ./build.sh)          # quick check of the MyST files with Sphinx
git add -A && git commit -m "Describe the change"
git push -u origin my-change     # collaborators; others push to their fork
```

Then open a pull request on GitHub. The requirements for the builds are in the
[README](README.md). New statements get permanent tags when `latex/build.sh`
runs. Commit the updated `latex/tags` file with your change, and never edit or
delete its existing lines.

### What happens next

* The build workflow runs on every pull request. It must pass before merging.
  Its log shows any LaTeX error, any missing tag, and the MyST build.
* The editor reviews the pull request. Discussion happens in its comments, and
  line-by-line suggestions can be accepted with one click.
* Once merged, the change is live on the website within a few minutes.

To suggest a new entry or report an error without writing it yourself, open an
issue.

## Comparing revisions

* **In a pull request**, the *Files changed* tab shows every change. For
  Markdown files, choose the rich diff to see the rendered text.
* **For one file**, open it on GitHub and choose *History* to list every change
  with its author and date, or *Blame* to see when each line was last changed.
  The history links on the website lead to the same list.
* **Between two points in time**, use the compare view, for example
  <https://github.com/eulogica/topdyn-encyclopaedia/compare/OLD...NEW>, where
  `OLD` and `NEW` are commits, branches or tags.
* **Locally**, `git log -p -- myst/entries/04-universal-minimal-flow.md` shows
  the history of one entry. `git diff --word-diff OLD NEW -- latex/entries/`
  compares two revisions word by word, which suits prose better than
  line-by-line diffs.

## Collaborators

Invited collaborators can create branches in this repository, review pull
requests and be assigned issues. Others contribute from a fork in the same
way. The `main` branch is the published website, so nobody pushes to it
directly: every change is merged through a reviewed pull request.
