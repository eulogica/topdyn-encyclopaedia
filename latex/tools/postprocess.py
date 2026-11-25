#!/usr/bin/env python3
"""Turn the plasTeX output into the encyclopaedia website.

Adds, on top of plasTeX + plastexdepgraph:
  * a permanent-tag badge on every tagged section and statement;
  * one page per tag, tag/XXXX.html: the statement, what it uses, what uses it,
    and how to cite it;
  * tags.html, an index of all tags with a lookup box;
  * graph.html, a static dependency graph (SVG drawn by Graphviz at build
    time, so it needs no WebAssembly in the browser);
  * extra navigation links and a small stylesheet.

Usage: python3 tools/postprocess.py SITE_DIR
"""
import copy
import html
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
TITLE = "Topological dynamics of topological groups"
SITE = Path(sys.argv[1])
SKIP = {"dep_graph_document.html", "graph.html", "tags.html"}
KIND_ABBR = {"Definition": "Def.", "Theorem": "Thm.", "Proposition": "Prop.",
             "Corollary": "Cor.", "Lemma": "Lem.", "Remark": "Rem.",
             "Example": "Ex."}
KIND_FILL = {"Definition": "#e8f0e3", "Theorem": "#f6e3d3",
             "Proposition": "#e4ebf4", "Corollary": "#efe6f2",
             "Lemma": "#e4ebf4"}

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
"""


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
    """(kind, number, title) of a statement block or a section heading."""
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
        soup.title.string = f"{TITLE}: {doc_title}"
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
            f'</ul>', "html.parser")
        toc.append(extra)


def extract_dot():
    page = (SITE / "dep_graph_document.html").read_text()
    m = re.search(r"renderDot\(`(.*?)`\)", page, re.S)
    return m.group(1) if m else None


def main():
    pairs = read_tags()
    tag_of = {label: tag for tag, label in pairs}
    pages = load_pages()

    # Locate every tagged item.
    items = {}  # label -> dict
    for name, soup in pages.items():
        for el in soup.find_all(id=True):
            label = el["id"]
            if label in tag_of and label not in items:
                kind, num, title = describe(el)
                items[label] = dict(tag=tag_of[label], page=name, kind=kind, num=num,
                                    title=title, uses=uses_of(el))
    used_by = {label: [] for label in items}
    for label, it in items.items():
        for u in it["uses"]:
            if u in used_by and label not in used_by[u]:
                used_by[u].append(label)
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
        def listing(labels, heading):
            if not labels:
                return f"<h2>{heading}</h2><p>Nothing yet.</p>"
            lis = "".join(f'<li><a href="tag/{items[l]["tag"]}.html">Tag {items[l]["tag"]}</a>: '
                          f'{html.escape(name_of(l))}</li>' for l in labels if l in items)
            return f"<h2>{heading}</h2><ul>{lis}</ul>"
        nodes += frag(listing(it["uses"], "Uses"))
        nodes += frag(listing(used_by[label], "Used by"))
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

    (SITE / "styles" / "encyclopaedia.css").write_text(CSS)
    for name, soup in pages.items():
        (SITE / name).write_text(str(soup))
    print(f"{len(items)} tagged items, {len(pages)} pages, tag pages in {SITE / 'tag'}")


if __name__ == "__main__":
    main()
