#!/usr/bin/env python3
"""Data for the map of the encyclopaedia, read from the LaTeX sources.

Both versions show the same map on their front page, drawn by the widget
myst/widgets/encyclopaedia-map.mjs: the MyST version through myst/tools/site_map.py,
which runs before `myst build`, and the LaTeX version through postprocess.py. This
module reads latex/main.tex and latex/entries/*.tex (standard library only, so it
runs before anything is built) and returns:

  * the entries, grouped into the strands below, with their section numbers;
  * every statement with its LaTeX number (one counter for all statements of a
    section), title, kind and the section where its proof is;
  * what each statement and each proof declares with \\uses;
  * the proofs in document order, with the statement each one proves and whether
    the proof comes straight after it;
  * the figures, with their numbers, captions and images, and the statements whose
    proofs each one illustrates (\\illustrates);
  * the subsections, and the subsection of each statement and each proof.

map_data() turns these into the widget's data, with links for either version, and
roadmap() the data of the roadmap at the top of each Proofs entry
(myst/widgets/entry-roadmap.mjs).
myst/tools/site_map.py also gives the statements of the MyST version these
numbers, so that both versions number every statement alike.
"""

import re
import unicodedata
from pathlib import Path

# The strands of the map: each begins at the entry named here and runs to the next.
# A new entry joins the strand of the entry before it.
STRANDS = [
    ("01-flows", "Foundations"),
    ("07-gromov-milman", "Extreme amenability and Ramsey theory"),
    ("11-metrizable-umf", "Computing universal minimal flows"),
    ("18-ea-catalogue", "Groups from analysis and operator algebras"),
    ("22-proofs-maps-and-transformations", "Proofs"),
]
PROOF_STRAND = "Proofs"

KINDS = ("definition", "theorem", "proposition", "corollary", "lemma", "conjecture",
         "example", "remark")
RESULTS = ("theorem", "proposition", "corollary", "conjecture")
TOKEN = re.compile(r"\\section\{|\\begin\{(%s|proof)\}" % "|".join(KINDS))
LABEL = re.compile(r"\\label\{([^}]*)\}")
USES = re.compile(r"\\uses\{([^}]*)\}")
PROVES = re.compile(r"\\proves\{([^}]*)\}")
FIGURE = re.compile(r"\\begin\{figure\}(.*?)\\end\{figure\}", re.S)
ILLUSTRATES = re.compile(r"\\illustrates\{([^}]*)\}")
IMAGE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}")
SUBSECTION = re.compile(r"\\subsection\{")
NESTED = re.compile(r"\\begin\{")


def balanced(text, i):
    """The text between the brace at text[i] and its match, and the index after it."""
    depth, j = 0, i
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
        j += 1
    return text[i + 1:], len(text)


def optional_arg(text, i):
    """The optional argument [ ... ] at text[i], if any; brackets inside braces are skipped."""
    while i < len(text) and text[i] in " \t":
        i += 1
    if i >= len(text) or text[i] != "[":
        return ""
    depth, j = 0, i + 1
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        elif c == "]" and depth == 0:
            return text[i + 1:j]
        j += 1
    return ""


SYMBOLS = {"infty": "∞", "omega": "ω", "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ",
           "varepsilon": "ε", "epsilon": "ε", "lambda": "λ", "Lambda": "Λ", "mu": "μ", "pi": "π",
           "sigma": "σ", "tau": "τ", "varphi": "φ", "phi": "φ", "Phi": "Φ", "ast": "*",
           "times": "×", "otimes": "⊗", "rtimes": "⋊", "le": "≤", "leq": "≤", "ge": "≥",
           "geq": "≥", "to": "→", "colon": ":", "ldots": "…", "cdots": "⋯", "lt": "<", "gt": ">",
           "cong": "≅", "subseteq": "⊆", "in": "∈"}
BLACKBOARD = {"Z": "ℤ", "N": "ℕ", "Q": "ℚ", "R": "ℝ", "C": "ℂ", "T": "𝕋", "S": "𝕊"}
SCRIPT = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"))
WRAPPERS = r"mathrm|operatorname|mathcal|mathfrak|mathbf|mathsf|mathit|text|textup|textrm|" \
           r"textit|textbf|emph|boldsymbol|underline|overline"
SUB_FROM, SUB_TO = "0123456789+-=()aeoxhklmnpstij", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜᵢⱼ"
SUP_FROM, SUP_TO = "0123456789+-=()ni*", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱ*"
ACCENTS = {"'": "\u0301", "`": "\u0300", "^": "\u0302", '"': "\u0308", "~": "\u0303",
           "=": "\u0304", ".": "\u0307", "v": "\u030c", "u": "\u0306", "H": "\u030b",
           "c": "\u0327", "r": "\u030a"}


def _subscript(t):
    if all(c in SUB_FROM for c in t):
        return t.translate(str.maketrans(SUB_FROM, SUB_TO))
    return t if len(t) == 1 and not t.isascii() else "_" + t


def _superscript(t, unicode=True):
    if t == "*":
        return "*"
    if unicode and all(c in SUP_FROM for c in t):
        return t.translate(str.maketrans(SUP_FROM, SUP_TO))
    return "^" + t


def _math(t, superscripts=True):
    t = re.sub(r"\\mathbb\{(\w)\}", lambda k: BLACKBOARD.get(k.group(1), k.group(1)), t)
    t = re.sub(r"\\mathcal\{(\w)\}", lambda k: SCRIPT.get(k.group(1), k.group(1)), t)
    t = re.sub(r"\\(?:%s)\s*\{([^{}]*)\}" % WRAPPERS, r"\1", t)
    t = re.sub(r"\\([A-Za-z]+)", lambda k: SYMBOLS.get(k.group(1), k.group(1)), t)
    t = re.sub(r"_\{([^{}]*)\}|_(\S)", lambda k: _subscript(k.group(1) or k.group(2)), t)
    t = re.sub(r"\^\{([^{}]*)\}|\^(\S)",
               lambda k: _superscript(k.group(1) or k.group(2), superscripts), t)
    return t.replace("{", "").replace("}", "").replace(" ", "").replace("\\", "")


def untex(text, superscripts=True):
    """The text with each piece of maths ($...$ or \\(...\\)) written in Unicode and the rest
    left alone: for places that show text as it is, such as browser tab titles, the MyST
    page titles and the MyST bibliography. With superscripts=False, superscripts stay as
    "^1" (mystmd's bibliographies print "¹" as a plain "1")."""
    return re.sub(r"\$(?!\s)([^$]+?)(?<!\s)\$|\\\((.*?)\\\)",
                  lambda m: _math(m.group(1) or m.group(2), superscripts), text)


def plain(tex):
    """A title as plain text: citations dropped, TeX reduced to letters and symbols."""
    s = re.sub(r"~?(?:\\protect\s*)?\\cite[pt]?\*?(?:\[[^\]]*\])*\{[^}]*\}", "", tex or "")
    s = re.sub(r"\\protect\b\s*", "", s)
    s = re.sub(r"\\([`'^\"~=.]|[vuHcr](?=[{\s]))\s*\{?([A-Za-z])\}?",
               lambda m: unicodedata.normalize("NFC", m.group(2) + ACCENTS[m.group(1)]), s)
    s = s.replace("---", "—").replace("--", "–").replace("~", " ")
    s = re.sub(r"\$([^$]*)\$|\\\((.*?)\\\)", lambda m: _math(m.group(1) or m.group(2) or ""), s)
    s = re.sub(r"\\(?:%s)\s*\{([^{}]*)\}" % WRAPPERS, r"\1", s)
    s = re.sub(r"\\([A-Za-z]+)", lambda k: SYMBOLS.get(k.group(1), k.group(1)), s)
    s = s.replace("{", "").replace("}", "").replace("\\", "").replace("'", "’")
    s = re.sub(r"\(\s*\)", "", re.sub(r"\s+", " ", s))
    return s.strip().rstrip(",;").strip()


def read(latex_dir):
    """Entries, statements, dependencies and proof locations, from the LaTeX sources."""
    latex_dir = Path(latex_dir)
    files = re.findall(r"\\input\{entries/([^}]+)\}", (latex_dir / "main.tex").read_text())
    entries, statements, deps, proved_in, aliases, proofs = [], [], {}, {}, {}, []
    figures, subsections = [], []
    raw = []  # (label, where, uses) before aliases are resolved
    section = 0
    for stem in files:
        text = (latex_dir / "entries" / f"{stem}.tex").read_text()
        text = re.sub(r"(?<!\\)%.*", "", text)
        # Figures are numbered within their section, as \\numberwithin{figure}{section}.
        for k, fm in enumerate(FIGURE.finditer(text), 1):
            body = fm.group(1)
            cap = body.find("\\caption{")
            caption = balanced(body, cap + len("\\caption"))[0] if cap >= 0 else ""
            lab, img, ill = LABEL.search(body), IMAGE.search(body), ILLUSTRATES.search(body)
            figures.append(dict(label=lab.group(1) if lab else "", num=f"{section + 1}.{k}",
                                file=stem, section=section + 1, caption=caption,
                                image=img.group(1) if img else "",
                                illustrates=[x.strip() for x in ill.group(1).split(",")
                                             if x.strip()] if ill else []))
        # The subsections of the file, numbered within their section; the file's
        # section starts at its \\section, whose number is the one after the current.
        subs = []
        for k, sm in enumerate(SUBSECTION.finditer(text), 1):
            title, after = balanced(text, sm.end() - 1)
            lab = re.match(r"\s*\\label\{([^}]*)\}", text[after:])
            subs.append(sm.start())
            subsections.append(dict(label=lab.group(1) if lab else "", title=title.strip(),
                                    num=f"{section + 1}.{k}", file=stem, section=section + 1))
        first_sub = len(subsections) - len(subs)

        def subsection_at(pos):
            k = sum(1 for start in subs if start <= pos)
            return first_sub + k - 1 if k else None

        counter, last = 0, None
        prev_end, prev_label = 0, None  # the statement environment just closed
        for m in TOKEN.finditer(text):
            if m.group(0) == "\\section{":
                title, after = balanced(text, m.end() - 1)
                section += 1
                counter = 0
                prev_label = None
                lab = LABEL.match(text, after)
                entries.append(dict(file=stem, n=section, title=plain(title),
                                    label=lab.group(1) if lab else ""))
                continue
            env = m.group(1)
            end = text.find(f"\\end{{{env}}}", m.end())
            body = text[m.end():end if end >= 0 else len(text)]
            if env == "proof":
                pv = PROVES.search(body)
                target = pv.group(1).strip() if pv else last
                if target:
                    raw.append((target, "proof", USES.findall(body), section))
                follows = (target is not None and target == prev_label
                           and not text[prev_end:m.start()].strip())
                proofs.append(dict(file=stem, target=target, section=section, follows=follows,
                                   subsection=subsection_at(m.start()),
                                   uses=[x.strip() for u in USES.findall(body)
                                         for x in u.split(",") if x.strip()]))
                continue
            counter += 1
            title = optional_arg(text, m.end())
            nested = NESTED.search(body)
            own = body[:nested.start()] if nested else body
            labels = LABEL.findall(own)
            prev_end = end + len(f"\\end{{{env}}}") if end >= 0 else len(text)
            prev_label = labels[-1] if labels else None
            if not labels:
                continue
            # Several labels: the statement is known by the last, as on the LaTeX site.
            label = last = labels[-1]
            for other in labels[:-1]:
                aliases[other] = label
            raw.append((label, "statement", USES.findall(own), section))
            statements.append(dict(label=label, kind=env, num=f"{section}.{counter}",
                                   title=plain(title), cited="\\cite" in title,
                                   section=section, file=stem,
                                   subsection=subsection_at(m.start())))
    for label, where, found, sec in raw:
        label = aliases.get(label, label)
        d = deps.setdefault(label, {"statement": [], "proof": []})
        if where == "proof":
            proved_in.setdefault(label, sec)
        for u in found:
            d[where] += [aliases.get(x.strip(), x.strip()) for x in u.split(",") if x.strip()]
    for d in deps.values():
        d["statement"] = list(dict.fromkeys(d["statement"]))
        d["proof"] = [u for u in dict.fromkeys(d["proof"]) if u not in d["statement"]]
    for p in proofs:
        p["target"] = aliases.get(p["target"], p["target"])
        p["uses"] = list(dict.fromkeys(aliases.get(u, u) for u in p["uses"]))
    return dict(entries=entries, statements=statements, deps=deps, proved_in=proved_in,
                aliases=aliases, proofs=proofs, figures=figures,
                subsections=subsections)


def proof_entries(src):
    """The files of the entries in the Proofs strand."""
    starts, strand, files = dict(STRANDS), None, set()
    for e in src["entries"]:
        strand = starts.get(e["file"], strand)
        if strand == PROOF_STRAND:
            files.add(e["file"])
    return files


def proved_here(src):
    """For each entry, the statements of other entries whose proofs it holds, in the
    order of the proofs."""
    st = {s["label"]: s for s in src["statements"]}
    here = {}
    for p in src["proofs"]:
        s = st.get(p["target"])
        if s and s["section"] != p["section"] and p["target"] not in here.get(p["file"], []):
            here.setdefault(p["file"], []).append(p["target"])
    return here


def transitive_reduction(edges):
    succ = {}
    for u, v in edges:
        succ.setdefault(u, set()).add(v)

    def reaches(a, b, skip):
        seen, stack = set(), [a]
        while stack:
            x = stack.pop()
            for y in succ.get(x, ()):
                if (x, y) == skip or y in seen:
                    continue
                if y == b:
                    return True
                seen.add(y)
                stack.append(y)
        return False
    return sorted((u, v) for u, v in edges if not reaches(u, v, (u, v)))


def induced(keep, pred):
    """Edges (u, v) between kept statements such that v rests on u through statements
    that are not kept, transitively reduced."""
    edges = set()
    for v in keep:
        seen, stack = set(), list(pred.get(v, ()))
        while stack:
            u = stack.pop()
            if u in seen or u == v:
                continue
            seen.add(u)
            if u in keep:
                edges.add((u, v))
            else:
                stack.extend(pred.get(u, ()))
    return transitive_reduction(edges)


KIND_NAME = {"theorem": "Theorem", "proposition": "Proposition", "corollary": "Corollary",
             "lemma": "Lemma", "definition": "Definition", "conjecture": "Conjecture",
             "example": "Example", "remark": "Remark"}


def reduce_edges(edges):
    """The edges whose ends no other path joins, removed one at a time, so that what
    reaches what is kept even where the edges form cycles."""
    kept = set(edges)

    def reaches(a, b):
        seen, stack = {a}, [a]
        while stack:
            x = stack.pop()
            for u, v in kept:
                if u == x and v not in seen:
                    if v == b:
                        return True
                    seen.add(v)
                    stack.append(v)
        return False

    for e in sorted(edges):
        kept.discard(e)
        if not reaches(*e):
            kept.add(e)
    return kept


def roadmap(src, stem, version):
    """The roadmap of a Proofs entry: its subsections in order, and an edge from one
    subsection to another when a statement or proof in the second uses a statement of
    the first. A statement whose proof is in another subsection of the entry, such as
    a main result stated at the start, counts as part of the subsection of its proof,
    which is said to prove it. version is "myst" or "latex", as for map_data()."""
    entries = {e["n"]: e for e in src["entries"]}
    by_label = {e["label"]: e for e in src["entries"] if e["label"]}
    subs = [k for k, sub in enumerate(src["subsections"]) if sub["file"] == stem]
    if not subs:
        return None
    st = {x["label"]: x for x in src["statements"]}
    mine = {l: x for l, x in st.items() if x["file"] == stem}
    proofs = [q for q in src["proofs"] if q["file"] == stem and q["subsection"] is not None]
    home = {l: x["subsection"] for l, x in mine.items() if x["subsection"] is not None}
    moved = {}
    for q in proofs:
        t = q["target"]
        if t in mine and home.get(t) is not None and q["subsection"] != home[t] and t not in moved:
            moved[t] = home[t]
            home[t] = q["subsection"]

    def page(n):
        e = entries[n]
        if version == "myst":
            return "/" + myst_slug(e["file"]).rstrip("/")
        return e["label"].replace(":", "-") + ".html"

    def link(label):
        x = st[label]
        anchor = label.replace(":", "-", 1) if version == "myst" else label
        here = x["file"] == stem
        name = f'{KIND_NAME.get(x["kind"], x["kind"].capitalize())} {x["num"]}'
        return dict(text=name, href=("" if here else page(x["section"])) + "#" + anchor)

    def title(sub):
        t = re.sub(r"Section~?\\ref\{([^}]*)\}",
                   lambda m: f'Section {by_label[m.group(1)]["n"]}' if m.group(1) in by_label
                   else "another section", sub["title"])
        return plain(untex(t))

    # Remarks and examples are left out: they comment on the results rather than
    # build on them.
    edges = set()
    for l, x in mine.items():
        if x["kind"] in ("remark", "example"):
            continue
        for u in src["deps"].get(l, {}).get("statement", []):
            if u in home and l in home and home[u] != home[l]:
                edges.add((home[u], home[l]))
    for q in proofs:
        if q["target"] in st and st[q["target"]]["kind"] in ("remark", "example"):
            continue
        for u in q["uses"]:
            if u in home and home[u] != q["subsection"]:
                edges.add((home[u], q["subsection"]))
    rows = []
    for k in subs:
        sub = src["subsections"][k]
        anchor = sub["label"].replace(":", "-", 1) if version == "myst" else sub["label"]
        stated = [l for l, x in mine.items() if x["subsection"] == k]
        others = []
        for q in proofs:
            if (q["subsection"] == k and q["target"] in st and q["target"] not in mine
                    and q["target"] not in others):
                others.append(q["target"])
        rows.append(dict(
            title=title(sub), num=sub["num"] if version == "latex" else "",
            href="#" + anchor if sub["label"] else "",
            statements=sum(1 for l in stated if st[l]["kind"] not in ("remark", "example")),
            states=[link(l) for l in stated if l in moved],
            proves=[link(l) for l, h in home.items() if h == k and l in moved],
            provesElsewhere=[link(l) for l in others]))
    index = {k: i for i, k in enumerate(subs)}
    return dict(version=version, rows=rows,
                edges=sorted([index[a], index[b]] for a, b in reduce_edges(edges)))


def myst_slug(stem):
    return re.sub(r"^\d+-", "", stem) + "/"


def map_data(src, version):
    """The widget's data. version is "myst" (links relative to the MyST front page) or
    "latex" (links relative to the LaTeX front page)."""
    starts = dict(STRANDS)
    strands, strand_of = [], {}
    for e in src["entries"]:
        if e["file"] in starts:
            strands.append(dict(title=starts[e["file"]], entries=[]))
        if strands:
            strands[-1]["entries"].append(e["n"])
            strand_of[e["n"]] = len(strands) - 1
    entry = {e["n"]: e for e in src["entries"]}
    st = {s["label"]: s for s in src["statements"]}

    def href(e, label=None):
        if version == "myst":
            return myst_slug(e["file"]) + (f"#{label.replace(':', '-', 1)}" if label else "")
        page = e["label"].replace(":", "-") + ".html"
        return page + (f"#{label}" if label else "")

    pred, users = {}, {}
    for v, d in src["deps"].items():
        for u in d["statement"] + d["proof"]:
            if u in st and v in st and u != v:
                pred.setdefault(v, set()).add(u)
                users.setdefault(u, set()).add(v)
    main = {l for l, s in st.items() if s["kind"] == "theorem" and not any(
        st[w]["kind"] in ("theorem", "proposition", "corollary", "lemma", "definition")
        for w in users.get(l, ()))}
    in_proofs = {l for l, s in st.items() if s["section"] in strand_of
                 and strands[strand_of[s["section"]]]["title"] == PROOF_STRAND}
    topical = {l for l, s in st.items() if s["section"] in strand_of} - in_proofs
    # The main results stated in the Proofs entries are drawn with the strand whose
    # proofs those entries hold (the widget shows the Proofs strand's results there).
    results = {l for l in topical if st[l]["kind"] in RESULTS} | (main & in_proofs)
    with_defs = results | {l for l in topical if st[l]["kind"] == "definition"}
    nodes = []
    for s in src["statements"]:
        if s["label"] not in with_defs:
            continue
        p = src["proved_in"].get(s["label"])
        nodes.append(dict(id=s["label"], kind=s["kind"].capitalize(), num=s["num"],
                          title=s["title"], entry=s["section"], main=s["label"] in main,
                          cited=s["cited"] and p is None,
                          proofIn=p if p and p != s["section"] else None,
                          href=href(entry[s["section"]], s["label"])))
    eedges = set()
    for v, us in pred.items():
        for u in us:
            a, b = st[u]["section"], st[v]["section"]
            if a != b and a in strand_of and b in strand_of:
                eedges.add((a, b))
    entries = [dict(n=e["n"], title=e["title"], href=href(e), strand=strand_of[e["n"]],
                    mains=sum(1 for l in main if st[l]["section"] == e["n"]),
                    statements=sum(1 for s in src["statements"] if s["section"] == e["n"]))
               for e in src["entries"] if e["n"] in strand_of]
    return dict(strands=strands, entries=entries, entryEdges=transitive_reduction(eedges),
                nodes=nodes, edges=induced(results, pred), edgesWithDefs=induced(with_defs, pred),
                proofTree="proof-tree/" if version == "myst" else "../proof-tree/",
                version=version)
