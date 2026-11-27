#!/usr/bin/env python3
"""Turn the plasTeX output into the encyclopaedia website.

Adds, on top of plasTeX + plastexdepgraph:
  * a permanent-tag badge on every tagged section and statement;
  * one page per tag, tag/XXXX.html: the statement, what it uses and what uses
    it (in its statement or in its proof), its proof tree, and how to cite it.
    The proof tree of a definition or result draws everything it rests on,
    directly or through other statements, as declared with \\uses in the
    statements and their proofs, together with the results of other works
    that these statements and proofs cite with a precise locator;
  * tags.html, an index of all tags with a lookup box;
  * graph.html, a static dependency graph (SVG drawn by Graphviz at build
    time, so it needs no WebAssembly in the browser);
  * links from every section page and tag page to its source files on GitHub
    (LaTeX and MyST twins), their history and the GitHub editor;
  * extra navigation links and a small stylesheet;
  * the interactive proof tree of the whole encyclopaedia, written by
    proof_tree_page.py to proof-tree/index.html beside SITE_DIR (so at
    /proof-tree/ when SITE_DIR is the site's latex/ folder), and the proof
    trees of the main results at proof-tree/main/index.html.

Usage: python3 tools/postprocess.py SITE_DIR
"""
import copy
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup

import proof_tree_page
import site_map

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/eulogica/topdyn-encyclopaedia"
BRANCH = "main"
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
TITLE = "Topological dynamics of topological groups"
SITE = Path(sys.argv[1])
SKIP = {"dep_graph_document.html", "graph.html", "tags.html"}
KIND_ABBR = {"Definition": "Def.", "Theorem": "Thm.", "Proposition": "Prop.",
             "Corollary": "Cor.", "Lemma": "Lem.", "Remark": "Rem.",
             "Example": "Ex.", "Conjecture": "Conj.", "Figure": "Fig."}
KIND_FILL = {"Definition": "#e8f0e3", "Theorem": "#f6e3d3",
             "Proposition": "#e4ebf4", "Corollary": "#efe6f2",
             "Lemma": "#e4ebf4", "Conjecture": "#f4f0d8"}

CSS = """
.tag-badge{display:inline-block;margin-left:.6em;padding:0 .45em;border:1px solid #8a9bb0;
  border-radius:3px;font:600 .75em/1.6 ui-monospace,Menlo,Consolas,monospace;color:#2e4a6b;
  text-decoration:none;vertical-align:.15em;background:#f3f6fa}
.tag-badge:hover{background:#2e4a6b;color:#fff}
.tag-page .context{color:#555;margin:.2em 0 1.2em}
.tag-page h2{font-size:1.05em;margin:1.6em 0 .4em}
.tag-page .cite-as{background:#f6f6f2;border-left:3px solid #b9b39a;padding:.6em .9em;font-size:.95em}
.tag-index{border-collapse:collapse;width:100%;font-size:.95em}
.tag-index th,.tag-index td{text-align:left;padding:.35em .6em;border-bottom:1px solid #e3e3e3;vertical-align:top}
.tag-index td:first-child{white-space:nowrap}
.tag-lookup{margin:1em 0 1.5em}
.tag-lookup input{font:1em ui-monospace,Menlo,Consolas,monospace;width:6em;padding:.3em .4em;text-transform:uppercase}
.tag-lookup button{padding:.3em .8em}
.graph-wrap{overflow:auto;border:1px solid #e3e3e3;background:#fff;padding:.5em}
.graph-wrap svg{display:block;margin:auto;max-width:none;height:auto}
div.content-wrapper.wide{max-width:none}
.graph-legend span{display:inline-block;margin-right:1.2em}
.graph-legend i{display:inline-block;width:1em;height:1em;border:1px solid #888;vertical-align:-.15em;margin-right:.3em}
nav.toc ul.extra-nav{margin-top:1.2em;padding-top:.8em;border-top:1px solid rgba(0,0,0,.12)}
.source-links{font-size:.85em;color:#666;margin:.3em 0 1.2em}
.source-links a{color:#2e4a6b}
.tag-page .tree-note{font-size:.9em;color:#555;margin:.2em 0 .6em}
.tag-page .graph-wrap{max-height:80vh}
.graph-wrap svg a{text-decoration:none}
.dep-links{font-size:.85em;line-height:1.5;color:#4a5560;background:#f3f5f8;border-left:3px solid #a9b8c9;
  padding:.3em .8em;margin:.3em 0 1.2em}
.dep-links p{margin:.15em 0}.dep-links b{color:#2b3540;font-weight:600}
.dep-links.proved-here{margin:.8em 0 1.4em}
figure{margin:1.2em 0 1.4em}
figure img{display:block;margin:0 auto}
figure>.tag-badge{align-self:center;margin:.4em 0 0}
.enc-widget{margin:.4em 0 1.6em}
.dep-links button.all-proofs{font:inherit;color:inherit;background:none;border:1px solid #a9b8c9;
  border-radius:3px;padding:.05em .5em;cursor:pointer}
.graph-legend i.cited{background:#fff;border-style:dashed}
.graph-legend i.this{background:#fff;border:2px solid #2e4a6b}
"""

# Proof trees on tag pages.
ENV_RE = re.compile(r"\\begin\{(definition|theorem|proposition|corollary|lemma|conjecture|"
                    r"example|remark|proof)\}(.*?)\\end\{\1\}", re.S)
USES_RE = re.compile(r"\\uses\{([^}]*)\}")
PROVES_RE = re.compile(r"\\proves\{([^}]*)\}")
CITE_RE = re.compile(r"\\cite\[([^\]]*)\]\{([^}]*)\}")
RESULT_LOCATOR = re.compile(r"\b(Theorems?|Lemmas?|Propositions?|Corollar(?:y|ies)|Facts?|Claims?)\b")
POINTER_BEFORE = re.compile(r"see also|compare|\bcf\.|fuller|for (?:a|another) (?:different|second)|"
                            r"history|in contrast|unlike", re.I)
TREE_SKIP = {"Section", "Remark", "Example", "Figure"}
LONGEST_LIST = 12  # longer lists of links after a statement end with a link to its tag page
MAX_TREE = 120


def read_tags():
    pairs = []
    for line in (ROOT / "tags").read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            tag, label = line.split()
            pairs.append((tag, label))
    return pairs


def load_pages():
    pages = {}
    for path in sorted(SITE.glob("*.html")):
        if path.name not in SKIP:
            pages[path.name] = BeautifulSoup(path.read_text(), "html.parser")
    return pages


def describe(el):
    """(kind, number, title) of a statement block, a figure or a section heading."""
    if el.name == "figure":
        ref = el.find("span", class_="caption_ref")
        return "Figure", ref.get_text(strip=True) if ref else "", ""
    classes = " ".join(el.get("class", []))
    if "_thmwrapper" in classes:
        def part(suffix):
            span = el.find("span", class_=lambda c: c and c.endswith(suffix))
            return " ".join(span.get_text(" ").split()) if span else ""
        title = re.sub(r"\s*\[\s*\d+(\s*,\s*\d+)*\s*\]", "", part("_thmtitle")).strip()
        return part("_thmcaption"), part("_thmlabel"), title
    text = " ".join(el.get_text(" ").split())
    m = re.match(r"(\d+)\s+(.*)", text)
    return ("Section", m.group(1), m.group(2)) if m else ("Section", "", text)


def uses_of(el):
    ul = el.find("ul", class_="uses")
    if not ul:
        return []
    return [a["href"].split("#", 1)[1] for a in ul.find_all("a", href=True) if "#" in a["href"]]


def prefix_relative(soup, prefix):
    for tag, attr in (("a", "href"), ("link", "href"), ("script", "src"), ("img", "src"),
                      ("use", "xlink:href")):
        for node in soup.find_all(tag):
            v = node.get(attr)
            if v and not re.match(r"^(https?:|mailto:|#|/|data:)", v):
                node[attr] = prefix + v


def set_main(soup, nodes, doc_title):
    main = soup.find("div", class_="main-text")
    main.clear()
    for n in nodes:
        main.append(n)
    if soup.title:
        soup.title.string = site_map.untex(f"{TITLE}: {doc_title}")
    for li in soup.select("nav.toc li"):
        li["class"] = [c for c in li.get("class", []) if c not in ("active", "current")]
    pun = soup.find("nav", class_="prev_up_next")
    if pun:
        pun.decompose()


def frag(markup):
    return list(BeautifulSoup(markup, "html.parser").contents)


def add_chrome(soup, depth):
    p = "../" * depth
    head = soup.head
    if not head.find("link", href=f"{p}styles/encyclopaedia.css"):
        head.append(soup.new_tag("link", rel="stylesheet", href=f"{p}styles/encyclopaedia.css"))
    toc = soup.find("nav", class_="toc")
    if toc and not toc.find("ul", class_="extra-nav"):
        for a in toc.find_all("a", href=re.compile(r"dep_graph_document\.html$")):
            a.parent.decompose() if a.parent.name == "li" else a.decompose()
        extra = BeautifulSoup(
            f'<ul class="sub-toc-0 extra-nav">'
            f'<li><a href="{p}graph.html"><span class="toc_entry">Dependency graph</span></a></li>'
            f'<li><a href="{p}dep_graph_document.html"><span class="toc_entry">Interactive graph</span></a></li>'
            f'<li><a href="{p}tags.html"><span class="toc_entry">All tags</span></a></li>'
            f'<li><a href="{p}encyclopaedia.pdf"><span class="toc_entry">PDF version</span></a></li>'
            f'<li><a href="https://topologicaldynamics.org/"><span class="toc_entry">MyST version</span></a></li>'
            f'<li><a href="{REPO}"><span class="toc_entry">Source on GitHub</span></a></li>'
            f'<li><a href="{REPO}/blob/{BRANCH}/CONTRIBUTING.md"><span class="toc_entry">How to contribute</span></a></li>'
            f'</ul>', "html.parser")
        toc.append(extra)


def source_locations():
    """Map every LaTeX label to (path in the repository, line number)."""
    locs = {}
    for path in sorted((ROOT / "entries").glob("*.tex")):
        for i, line in enumerate(path.read_text().splitlines(), 1):
            for m in LABEL_RE.finditer(line):
                locs[m.group(1)] = (f"latex/entries/{path.name}", i)
    return locs


def myst_twin(tex_path):
    """The MyST file with the same content as a LaTeX entry file."""
    stem = Path(tex_path).stem
    return "myst/index.md" if stem == "00-about" else f"myst/entries/{stem}.md"


def file_links(path, line=None):
    anchor = f"#L{line}" if line else ""
    return (f'<a href="{REPO}/blob/{BRANCH}/{path}{anchor}">{html.escape(path)}</a> '
            f'(<a href="{REPO}/commits/{BRANCH}/{path}">history</a>, '
            f'<a href="{REPO}/edit/{BRANCH}/{path}">edit</a>)')


def section_source_note(tex_path):
    twin = myst_twin(tex_path)
    twin_part = (f" and {file_links(twin)}" if (ROOT.parent / twin).exists() else "")
    return frag(f'<p class="source-links">Source of this section: {file_links(tex_path)}'
                f'{twin_part}. To propose a change, see '
                f'<a href="{REPO}/blob/{BRANCH}/CONTRIBUTING.md">how to contribute</a>.</p>')


def extract_dot():
    page = (SITE / "dep_graph_document.html").read_text()
    m = re.search(r"renderDot\(`(.*?)`\)", page, re.S)
    return m.group(1) if m else None


def skip_optional_arg(body):
    """The body of an environment without its optional [title], which may nest brackets."""
    s = body.lstrip()
    if not s.startswith("["):
        return body
    depth = 0
    for i, ch in enumerate(s):
        depth += ch == "["
        depth -= ch == "]"
        if depth == 0:
            return s[i + 1:]
    return body


def result_cites(text):
    """(key, locator) of each citation of a numbered result of another work, not of pointers."""
    out = []
    for m in CITE_RE.finditer(text):
        loc = " ".join(m.group(1).replace("~", " ").split())
        if not RESULT_LOCATOR.search(loc):
            continue
        before = text[max(0, m.start() - 60):m.start()]
        before = before[max(before.rfind(". "), before.rfind(";")) + 1:]
        if POINTER_BEFORE.search(before):
            continue
        for key in m.group(2).split(","):
            if key.strip():
                out.append((key.strip(), loc))
    return out


def source_dependencies():
    """For each statement label: the labels its statement and its proof declare with
    \\uses, and the results of other works that they cite."""
    deps = {}
    for path in sorted((ROOT / "entries").glob("*.tex")):
        last = None
        for m in ENV_RE.finditer(path.read_text()):
            env, body = m.group(1), m.group(2)
            if env != "proof":
                lab = LABEL_RE.search(body)
                if not lab:
                    continue
                last = target = lab.group(1)
                where, text = "statement", skip_optional_arg(body)
            else:
                pv = PROVES_RE.search(body)
                target = pv.group(1).strip() if pv else last
                if target is None:
                    continue
                where, text = "proof", body
            d = deps.setdefault(target, {"statement": [], "proof": [], "cites": []})
            for u in USES_RE.findall(text):
                for x in u.split(","):
                    x = x.strip()
                    if x and x != target and x not in d[where]:
                        d[where].append(x)
            for c in result_cites(text):
                if c not in d["cites"]:
                    d["cites"].append(c)
    return deps


def bibliography_links(pages):
    """Citation key -> (href of its bibliography entry, its number)."""
    out = {}
    for soup in pages.values():
        for span in soup.find_all("span", class_="cite"):
            for a in span.find_all("a", href=True):
                if "#" in a["href"]:
                    out.setdefault(a["href"].split("#", 1)[1], (a["href"], a.get_text(strip=True)))
    return out


def dot_text(s):
    """A statement title as plain text for a Graphviz label."""
    s = re.sub(r"\\[()\[\]]", "", s)
    s = re.sub(r"\\(?:mathcal|mathrm|mathbb|operatorname|mathfrak|textup|emph)\s*\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\([A-Za-z]+)", r"\1", s).replace("{", "").replace("}", "")
    words, lines, cur = s.split(), [], ""
    for w in words:
        if cur and len(cur) + len(w) > 24:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return "\\n".join(x.replace("\\", "").replace('"', "'") for x in lines)


def transitive_reduction(edges):
    """The edges (u, v) of a small graph through which v is not reached from u another way."""
    succ = {}
    for u, v in edges:
        succ.setdefault(u, set()).add(v)

    def reaches(start, goal, skip):
        seen, stack = set(), [start]
        while stack:
            x = stack.pop()
            for y in succ.get(x, ()):
                if (x, y) == skip or y in seen:
                    continue
                if y == goal:
                    return True
                seen.add(y)
                stack.append(y)
        return False

    return {(u, v) for u, v in edges if not reaches(u, v, (u, v))}


def proof_tree_svg(root, items, uses, cites, bib, name_of, tag_prefix="", bib_prefix="../"):
    """SVG of what the statement `root` rests on, or None if it rests on nothing. Its boxes
    link to tag_prefix + "XXXX.html" and to bib_prefix + the bibliography entry; the
    defaults suit the tag pages."""
    order = {label: i for i, label in enumerate(items)}
    seen, stack = set(), [root]
    while stack:
        for u in uses.get(stack.pop(), ()):
            if u in items and u != root and u not in seen and items[u]["kind"] not in TREE_SKIP:
                seen.add(u)
                stack.append(u)
    if len(seen) > MAX_TREE:
        return None
    nodes = [root] + sorted(seen, key=lambda l: order[l])
    cited = []
    for v in nodes:
        for key, loc in cites.get(v, ()):
            if key in bib:
                cited.append((f"cite:{key}:{loc}", key, loc, v))
    if not seen and not cited:
        return None
    lines = ['digraph G {',
             'graph [bgcolor=transparent, rankdir=TB, nodesep=0.25, ranksep=0.4];',
             'node [fontname="Helvetica", fontsize=10, margin="0.08,0.03"];',
             'edge [color="#6b7785", arrowsize=0.6];']
    for label in nodes:
        it = items[label]
        text = f'{KIND_ABBR.get(it["kind"], it["kind"])} {it["num"]}'
        if it["title"]:
            text += "\\n" + dot_text(it["title"])
        shape = "box" if it["kind"] == "Definition" else "ellipse"
        extra = ', penwidth=2.2, color="#2e4a6b"' if label == root else ""
        tip = name_of(label).replace('"', "'").replace("\\", "")
        lines.append(f'"{label}" [label="{text}", shape={shape}, style=filled, '
                     f'fillcolor="{KIND_FILL.get(it["kind"], "#ffffff")}", URL="{tag_prefix}{it["tag"]}.html", '
                     f'target="_top", tooltip="{tip} - Tag {it["tag"]}"{extra}];')
    edges = {(u, v) for v in nodes for u in uses.get(v, ()) if u in seen}
    edges |= {(cid, v) for cid, _, _, v in cited}
    for cid, key, loc in dict.fromkeys(c[:3] for c in cited):
        href, num = bib[key]
        lines.append(f'"{cid}" [label="[{num}, {loc}]", shape=box, style="dashed", '
                     f'URL="{bib_prefix}{href}", target="_top", tooltip="Cited result: [{num}, {loc}]"];')
    for u, v in sorted(transitive_reduction(edges)):
        lines.append(f'"{u}" -> "{v}"{" [style=dashed]" if u.startswith("cite:") else ""};')
    lines.append("}")
    dot = "\n".join(lines)
    drawn = subprocess.run(["dot", "-Tsvg"], input=dot, capture_output=True, text=True)
    if drawn.returncode != 0:
        print(f"warning: no proof tree for {root}: {drawn.stderr.strip()}", file=sys.stderr)
        return None
    return drawn.stdout[drawn.stdout.find("<svg"):]


def main():
    pairs = read_tags()
    tag_of = {label: tag for tag, label in pairs}
    pages = load_pages()

    # Figures: plasTeX shows a PNG copy, with the \\includegraphics command as alt text.
    # Show the SVG instead (from ../figures, drawn by figures/make_figures.py), and give it
    # the figure's own description as alt text.
    figures_dir = ROOT.parent / "figures"
    for soup in pages.values():
        for fig in soup.find_all("figure"):
            img = fig.find("img")
            m = re.search(r"\{([^{}]*)\}\s*$", img.get("alt", "")) if img else None
            svg_file = figures_dir / f"{m.group(1)}.svg" if m else None
            if not svg_file or not svg_file.exists():
                continue
            (SITE / "figures").mkdir(exist_ok=True)
            shutil.copy(svg_file, SITE / "figures" / svg_file.name)
            title = re.search(r"<title>(.*?)</title>", svg_file.read_text(), re.S)
            img["src"] = f"figures/{svg_file.name}"
            img["alt"] = html.unescape(title.group(1)) if title else ""
            img["style"] = "width:100%;max-width:680px;height:auto"
    locs = source_locations()

    # Locate every tagged item.
    items = {}  # label -> dict
    for name, soup in pages.items():
        for el in soup.find_all(id=True):
            label = el["id"]
            if label in tag_of and label not in items:
                kind, num, title = describe(el)
                items[label] = dict(tag=tag_of[label], page=name, kind=kind, num=num,
                                    title=title, uses=uses_of(el))
    # What each statement uses, in its statement and in its proof. plastexdepgraph
    # shows only the first on the pages, so both are read from the sources.
    src = source_dependencies()
    bib = bibliography_links(pages)
    for label, it in items.items():
        d = src.get(label, {})
        stmt = [u for u in it["uses"] + d.get("statement", []) if u in items and u != label]
        it["uses"] = list(dict.fromkeys(stmt))
        it["uses_proof"] = [u for u in dict.fromkeys(d.get("proof", []))
                            if u in items and u != label and u not in it["uses"]]
    uses_all = {label: it["uses"] + it["uses_proof"] for label, it in items.items()}
    cites = {label: d["cites"] for label, d in src.items()}
    used_by = {label: [] for label in items}
    in_proof_of = set()
    for label, it in items.items():
        for u in uses_all[label]:
            if label not in used_by[u]:
                used_by[u].append(label)
            if u in it["uses_proof"]:
                in_proof_of.add((u, label))
    section_of = {}
    for label, it in items.items():
        if it["kind"] == "Section":
            for other in items.values():
                if other["page"] == it["page"]:
                    section_of.setdefault(other["page"], (it["num"], it["title"]))

    def name_of(label):
        it = items[label]
        if it["kind"] == "Section":
            return f"Section {it['num']}: {it['title']}"
        t = f" ({it['title']})" if it["title"] else ""
        return f"{it['kind']} {it['num']}{t}"

    # Badges on the pages.
    for name, soup in pages.items():
        for el in soup.find_all(id=True):
            label = el["id"]
            if label not in items or el.find("a", class_="tag-badge"):
                continue
            tag = items[label]["tag"]
            badge = soup.new_tag("a", href=f"tag/{tag}.html", title=f"Permanent tag {tag}")
            badge["class"] = ["tag-badge"]
            badge.string = f"Tag {tag}"
            heading = el.find("div", class_=lambda c: c and c.endswith("_thmheading")) or el
            heading.append(badge)
        add_chrome(soup, 0)

    # Tag pages.
    (SITE / "tag").mkdir(exist_ok=True)
    for label, it in items.items():
        src = pages[it["page"]]
        soup = copy.deepcopy(src)
        block = copy.deepcopy(soup.find(id=label))
        if it["kind"] == "Section":
            block = soup.new_tag("p")
            block.string = it["title"]
        for b in block.find_all("a", class_="tag-badge"):
            b.decompose()
        sec = section_of.get(it["page"], ("", ""))
        ctx = (f'Appears as <a href="{it["page"]}#{label}">{html.escape(name_of(label))}</a>'
               + (f' in Section {sec[0]}, <a href="{it["page"]}">{html.escape(sec[1])}</a>.'
                  if it["kind"] != "Section" else "."))
        nodes = frag(f'<h1>Tag {it["tag"]}</h1><p class="context">{ctx}</p>')
        nodes.append(block)
        if label in locs:
            path, line = locs[label]
            nodes += frag(f'<p class="source-links">Source: {file_links(path, line)}, line {line}.</p>')
        def listing(labels, heading, in_proof):
            if not labels:
                return f"<h2>{heading}</h2><p>Nothing yet.</p>"
            lis = "".join(f'<li><a href="tag/{items[l]["tag"]}.html">Tag {items[l]["tag"]}</a>: '
                          f'{html.escape(name_of(l))}{" (in the proof)" if in_proof(l) else ""}</li>'
                          for l in labels if l in items)
            return f"<h2>{heading}</h2><ul>{lis}</ul>"
        nodes += frag(listing(uses_all[label], "Uses", lambda l: l in it["uses_proof"]))
        nodes += frag(listing(used_by[label], "Used by", lambda l: (label, l) in in_proof_of))
        if it["kind"] not in TREE_SKIP:
            svg = proof_tree_svg(label, items, uses_all, cites, bib, name_of)
            if svg:
                heading = "Proof tree" if it["kind"] not in ("Definition", "Conjecture") else "What it rests on"
                legend = "".join(f'<span><i style="background:{c}"></i>{k}</span>'
                                 for k, c in KIND_FILL.items() if k != "Lemma")
                legend += ('<span><i class="cited"></i>Cited result</span>'
                           '<span><i class="this"></i>This statement</span>')
                nodes += frag(
                    f'<h2>{heading}</h2><p class="tree-note">Everything this statement rests on, '
                    'directly or through other statements, as declared in its source and in the '
                    'sources of its proof. An arrow means that the second item uses the first; '
                    'implied arrows are left out. Dashed boxes are results of other works that '
                    'these statements and proofs cite. Click a node to open its tag, or '
                    f'<a href="../proof-tree/#tree={html.escape(label)}">open this tree in the '
                    'interactive proof tree</a>.</p>'
                    f'<p class="graph-legend">{legend}</p>')
                wrap = soup.new_tag("div")
                wrap["class"] = ["graph-wrap"]
                wrap.append(BeautifulSoup(svg, "html.parser"))
                nodes.append(wrap)
                # A wide tree scrolls sideways: start with this statement in view.
                nodes += frag(
                    '<script>{const w=document.currentScript.previousElementSibling;'
                    'const n=[...w.querySelectorAll("g.node")].find(g=>{const t=g.querySelector("title");'
                    f'return t&&t.textContent==={json.dumps(label)};}});'
                    'if(n){const r=n.getBoundingClientRect(),b=w.getBoundingClientRect();'
                    'w.scrollLeft+=r.left+r.width/2-b.left-b.width/2;w.scrollTop=w.scrollHeight;}}</script>')
        nodes += frag(f'<h2>How to cite</h2><p class="cite-as">{html.escape(TITLE)}, '
                      f'Tag {it["tag"]} ({html.escape(name_of(label))}).</p>')
        set_main(soup, nodes, f"Tag {it['tag']}")
        soup.find("div", class_="main-text")["class"] = ["main-text", "tag-page"]
        for b in soup.select("nav.toc ul.extra-nav"):
            b.decompose()
        prefix_relative(soup, "../")
        add_chrome(soup, 1)
        (SITE / "tag" / f"{it['tag']}.html").write_text(str(soup))

    # Tag index.
    soup = copy.deepcopy(pages["index.html"])
    rows = "".join(
        f'<tr><td><a href="tag/{it["tag"]}.html">{it["tag"]}</a></td>'
        f'<td>{html.escape(name_of(l))}</td>'
        f'<td><a href="{it["page"]}#{l}">in context</a></td></tr>'
        for l, it in sorted(items.items(), key=lambda kv: kv[1]["tag"]))
    nodes = frag(
        '<h1>All tags</h1>'
        '<p>Every section and statement has a permanent four-character tag. Tags never '
        'change and are never reused, so they are the way to cite items of this '
        'encyclopaedia.</p>'
        '<form class="tag-lookup" id="tag-lookup"><label>Look up a tag: '
        '<input id="tag-input" maxlength="4" autocomplete="off" placeholder="0001"></label> '
        '<button type="submit">Go</button></form>'
        f'<table class="tag-index"><thead><tr><th>Tag</th><th>Item</th><th></th></tr></thead>'
        f'<tbody>{rows}</tbody></table>'
        '<script>{const f=document.getElementById("tag-lookup");f.addEventListener("submit",'
        'e=>{e.preventDefault();const v=document.getElementById("tag-input").value.trim().toUpperCase();'
        'if(/^[0-9A-Z]{4}$/.test(v))location.href="tag/"+v+".html";});}</script>')
    set_main(soup, nodes, "All tags")
    add_chrome(soup, 0)
    (SITE / "tags.html").write_text(str(soup))

    # Static dependency graph.
    dot = extract_dot()
    if dot:
        def relabel(m):
            label = m.group(1)
            if label not in items:
                return m.group(0)
            it = items[label]
            text = f'{KIND_ABBR.get(it["kind"], it["kind"])} {it["num"]}'
            if it["title"]:
                text += "\\n" + it["title"]
            fill = KIND_FILL.get(it["kind"], "#ffffff")
            shape = "box" if it["kind"] == "Definition" else "ellipse"
            tip = name_of(label).replace('"', "'")
            return (f'"{label}" [label="{text}", shape={shape}, style=filled, fillcolor="{fill}", '
                    f'URL="{it["page"]}#{label}", target="_top", tooltip="{tip} - Tag {it["tag"]}", '
                    f'fontname="Helvetica", fontsize=10, margin="0.08,0.03"]')
        dot = re.sub(r'"([^"]+)"\s*\[label=[^\]]*\]', relabel, dot)
        dot = dot.replace("graph [bgcolor=transparent];",
                          "graph [bgcolor=transparent, rankdir=TB, nodesep=0.25, ranksep=0.45];")
        svg = subprocess.run(["dot", "-Tsvg"], input=dot, capture_output=True, text=True,
                             check=True).stdout
        svg = svg[svg.find("<svg"):]
        soup = copy.deepcopy(pages["index.html"])
        legend = "".join(f'<span><i style="background:{c}"></i>{k}</span>'
                         for k, c in KIND_FILL.items() if k != "Lemma")
        nodes = frag(
            '<h1>Dependency graph</h1>'
            '<p>An arrow from one statement to another means that the second uses the '
            'first. Click a node to open the statement. Remarks and examples are not '
            'shown.</p>'
            f'<p class="graph-legend">{legend}</p>')
        wrap = soup.new_tag("div")
        wrap["class"] = ["graph-wrap"]
        wrap.append(BeautifulSoup(svg, "html.parser"))
        nodes.append(wrap)
        set_main(soup, nodes, "Dependency graph")
        soup.find("div", class_="content-wrapper")["class"] = ["content-wrapper", "wide"]
        add_chrome(soup, 0)
        (SITE / "graph.html").write_text(str(soup))

    # The plugin's interactive graph page gets the same navigation.
    dg = SITE / "dep_graph_document.html"
    if dg.exists():
        soup = BeautifulSoup(dg.read_text(), "html.parser")
        add_chrome(soup, 0)
        dg.write_text(str(soup))

    # Links from each section page to its source files.
    for label, it in items.items():
        if it["kind"] != "Section" or label not in locs:
            continue
        main_text = pages[it["page"]].find("div", class_="main-text")
        if not main_text or main_text.find("p", class_="source-links"):
            continue
        heading = main_text.find(["h1", "h2"])
        note = section_source_note(locs[label][0])
        if heading:
            for node in reversed(note):
                heading.insert_after(node)
        else:
            for node in reversed(note):
                main_text.insert(0, node)

    # The interactive proof tree of the whole encyclopaedia, next to the LaTeX
    # version: _site/proof-tree/ when this is _site/latex/, and the proof trees of
    # the main results, drawn as on the tag pages, at _site/proof-tree/main/.
    out = SITE.resolve().parent / "proof-tree" / "index.html"
    tree_legend = "".join(f'<span><i style="background:{c}"></i>{k}</span>'
                          for k, c in KIND_FILL.items() if k != "Lemma")
    tree_legend += ('<span><i class="cited"></i>Cited result</span>'
                    '<span><i class="this"></i>The main result</span>')
    count = proof_tree_page.write(
        out, items, {l: it["uses"] for l, it in items.items()},
        {l: it["uses_proof"] for l, it in items.items()}, cites, bib, pages, locs,
        ROOT.parent / "myst", KIND_ABBR,
        trees=lambda label: proof_tree_svg(label, items, uses_all, cites, bib, name_of,
                                           tag_prefix="../../latex/tag/", bib_prefix="../../latex/"),
        legend=tree_legend, sections=section_of)
    print("interactive proof tree: %d nodes, %d dependencies, %d main results, in %s" % (count + (out,)))

    # Links after every statement on the section pages: what the statement and its
    # proof use, what uses it, where its proof is when that is on another page, and its
    # proof tree. (Added last, so that tag pages and the proof tree pages, which copy
    # the statements, do not repeat them.)
    def number_key(label):
        return tuple(int(x) for x in re.findall(r"\d+", items[label]["num"])) or (0,)

    def ref(label):
        it = items[label]
        return (f'<a href="{it["page"]}#{label}">'
                f'{KIND_ABBR.get(it["kind"], it["kind"])}&nbsp;{it["num"]}</a>')

    def listing(labels, label):
        keys = sorted({l for l in labels if l in items and l != label}, key=number_key)
        shown = ", ".join(ref(l) for l in keys[:LONGEST_LIST])
        if len(keys) > LONGEST_LIST:
            shown += f', <a href="tag/{items[label]["tag"]}.html">and {len(keys) - LONGEST_LIST} more</a>'
        return shown

    # The figures that illustrate each statement's proof (\\illustrates in the sources).
    illustrated = {}
    for f in site_map.read(ROOT)["figures"]:
        for target in f["illustrates"]:
            if f["label"] in items:
                illustrated.setdefault(target, []).append(f["label"])

    for label, it in items.items():
        if it["kind"] in ("Section", "Figure"):
            continue
        el = pages[it["page"]].find(id=label)
        nxt = el.find_next_sibling() if el else None
        if not el or (nxt is not None and "dep-links" in (nxt.get("class") or [])):
            continue
        rows = [f"<b>{title}</b> {listing(ls, label)}" for title, ls in (
            ("Uses", it["uses"]), ("Its proof uses", it["uses_proof"]), ("Used by", used_by[label]))
            if listing(ls, label)]
        last = []
        for a in el.select(".thm_header_hidden_extras a[href]"):
            if a.find("svg") is None and "icon-cogs" not in str(a):
                continue
            target = a["href"].split("#")[0] or it["page"]
            if target != it["page"] and target in section_of:
                last.append(f'<b>Proof</b> in <a href="{html.escape(a["href"])}">Section {section_of[target][0]}</a>')
            break
        figs = [f'<a href="{items[fig]["page"]}#{html.escape(fig)}">Fig.&nbsp;{items[fig]["num"]}</a>'
                for fig in illustrated.get(label, [])]
        if figs:
            last.insert(0, "Illustrated in " + " and ".join([", ".join(figs[:-1]), figs[-1]] if len(figs) > 1 else figs))
        last.append(f'<a href="../proof-tree/#tree={html.escape(label)}">Proof tree</a>')
        rows.append(" · ".join(last))
        nav = frag(f'<nav class="dep-links" aria-label="Links for {html.escape(site_map.untex(name_of(label)))}">'
                   + "".join(f"<p>{r}</p>" for r in rows) + "</nav>")
        el.insert_after(nav[0])

    # The Proofs entries: a proof that comes straight after its statement starts
    # folded (click its heading to open it), so that the statements can be scanned;
    # the proofs of an entry's main results, which come later, stay open. Each entry
    # opens with the statements of other entries that it proves. The same proofs are
    # folded on the MyST site (myst/tools/site_map.py).
    src = site_map.read(ROOT)
    page_of_file = {e["file"]: e["label"].replace(":", "-") + ".html" for e in src["entries"]}
    folded = 0
    for stem in sorted(site_map.proof_entries(src)):
        soup = pages.get(page_of_file.get(stem))
        if soup is None:
            continue
        wrappers = soup.select("div.proof_wrapper")
        proofs = [p for p in src["proofs"] if p["file"] == stem]
        if len(wrappers) != len(proofs):
            print(f"{stem}: {len(wrappers)} proofs on the page, {len(proofs)} in the source; "
                  "none folded")
            continue
        for w, p in zip(wrappers, proofs):
            if p["follows"]:
                w["class"] = w.get("class", []) + ["folded"]
                content = w.find("div", class_="proof_content")
                arrow = w.find("span", class_="expand-proof")
                if content is not None:
                    content["style"] = "display:none"
                if arrow is not None:
                    arrow.string = "▶"
                folded += 1
        rows = []
        here = site_map.proved_here(src).get(stem, [])
        if here:
            links = []
            for label in here:
                proof = next((a["href"] for a in pages[items[label]["page"]].find(id=label)
                              .select(".thm_header_hidden_extras a.proof[href]")
                              if a.find("svg") is not None), None)
                extra = f'<a href="{html.escape(proof)}">proof</a> · ' if proof else ""
                links.append(f'{ref(label)} ({extra}<a href="../proof-tree/#tree='
                             f'{html.escape(label)}">proof tree</a>)')
            rows.append("<b>Proved in this entry</b> " + ", ".join(links))
        rows.append('Proofs that follow their statement are folded: click “Proof” to open one, '
                    'or <button type="button" class="all-proofs">open all proofs</button>')
        nav = frag('<nav class="dep-links proved-here" aria-label="About this entry">'
                   + "".join(f"<p>{r}</p>" for r in rows) + "</nav>")
        main_text = soup.find("div", class_="main-text")
        first = main_text.find("h2") if main_text else None
        if first is not None and not soup.find("nav", class_="proved-here"):
            first.insert_before(nav[0])
        script = soup.new_tag("script")
        script.string = (
            'document.addEventListener("DOMContentLoaded",function(){'
            'function set(w,open){var c=w.querySelector(".proof_content"),'
            'a=w.querySelector(".expand-proof");if(c)c.style.display=open?"":"none";'
            'if(a)a.textContent=open?"▼":"▶";}'
            'var b=document.querySelector("button.all-proofs");'
            'if(b)b.addEventListener("click",function(){var open=b.dataset.open!=="1";'
            'document.querySelectorAll("div.proof_wrapper.folded").forEach(function(w){set(w,open)});'
            'b.dataset.open=open?"1":"";b.textContent=open?"fold them again":"open all proofs";});'
            'function reveal(id){var t=id&&document.getElementById(id);'
            'var w=t&&t.closest("div.proof_wrapper");if(w)set(w,true);}'
            'reveal(decodeURIComponent(location.hash.slice(1)));'
            'window.addEventListener("hashchange",function(){'
            'reveal(decodeURIComponent(location.hash.slice(1)))});'
            'document.querySelectorAll("a.proof[href]").forEach(function(a){'
            'a.addEventListener("click",function(){reveal(a.getAttribute("href").split("#")[1])})});'
            '});')
        soup.body.append(script)
    print(f"folded {folded} proofs in the Proofs entries")

    # Interactive figures: a figure fig:NAME is followed by the widget
    # myst/widgets/NAME.mjs when there is one, as on the MyST site (tools/site_map.py).
    for soup in pages.values():
        for fig in soup.find_all("figure", id=True):
            name = fig["id"].split(":", 1)[-1]
            widget = ROOT.parent / "myst" / "widgets" / f"{name}.mjs"
            if not fig["id"].startswith("fig:") or not widget.exists() \
                    or soup.find(id=f"widget-{name}"):
                continue
            (SITE / "widgets").mkdir(exist_ok=True)
            shutil.copy(widget, SITE / "widgets" / widget.name)
            block = frag(f'<div class="enc-widget" id="widget-{name}"></div>'
                         f'<script type="module">import w from "./widgets/{widget.name}";'
                         f'w.render({{model:{{get:()=>undefined}},'
                         f'el:document.getElementById("widget-{name}")}});</script>')
            for node in reversed(block):
                fig.insert_after(node)

    # The map of the encyclopaedia on the front page, drawn by the widget that the
    # MyST front page also uses (myst/widgets/encyclopaedia-map.mjs).
    widget = ROOT.parent / "myst" / "widgets" / "encyclopaedia-map.mjs"
    if widget.exists():
        (SITE / "widgets").mkdir(exist_ok=True)
        shutil.copy(widget, SITE / "widgets" / widget.name)
        data = json.dumps(site_map.map_data(site_map.read(ROOT), "latex"), ensure_ascii=False)
        data = data.replace("</", "<\\/")
        front = pages["index.html"]
        title = front.find("div", class_="titlepage")
        block = frag(
            '<h2 class="map-title">Map of the encyclopaedia</h2>'
            '<div id="encyclopaedia-map" style="max-width:1180px"></div>'
            f'<script type="application/json" id="encyclopaedia-map-data">{data}</script>'
            '<script type="module">import map from "./widgets/encyclopaedia-map.mjs";'
            'const data=JSON.parse(document.getElementById("encyclopaedia-map-data").textContent);'
            'map.render({model:{get:k=>k==="data"?data:undefined},el:document.getElementById("encyclopaedia-map")});'
            '</script>')
        if title and not front.find(id="encyclopaedia-map"):
            for node in reversed(block):
                title.insert_after(node)
            wrapper = front.find("div", class_="content-wrapper")
            if wrapper:
                wrapper["class"] = ["content-wrapper", "wide"]
        print("map of the encyclopaedia on the front page")

    (SITE / "styles" / "encyclopaedia.css").write_text(CSS)
    for name, soup in pages.items():
        # Browser tabs and tooltips (such as those of the arrows to the previous and
        # next sections) show titles as they are, so write their maths in Unicode.
        if soup.title and soup.title.string:
            soup.title.string = site_map.untex(soup.title.string)
        for el in soup.find_all(title=True):
            el["title"] = site_map.untex(el["title"])
        (SITE / name).write_text(str(soup))
    print(f"{len(items)} tagged items, {len(pages)} pages, tag pages in {SITE / 'tag'}")


if __name__ == "__main__":
    main()
