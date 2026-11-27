#!/usr/bin/env python3
"""Number the MyST statements as in the LaTeX version, link each statement to what
it rests on and what uses it, and draw the map of the encyclopaedia on the front page.

Run by the build workflow, before `myst build`, on the checked-out working copy
(the workflow restores the files afterwards). The files in the repository never
contain what it adds, so authors do not maintain it. Running it twice does
nothing the second time.

  * Every statement whose label has a LaTeX twin gets that twin's number, as
    `:enumerator: 5.2`, so that both versions number it alike and a reference
    from another page reads "Proposition 3.2" rather than "Proposition 1".
    Proofs are left unnumbered, as in the LaTeX version.
  * Every proof gets a label, proof-<label of the statement it proves>, taken
    from its LaTeX twin (the proofs of an entry come in the same order in both
    versions).
  * After every statement comes a short block of links, from the \\uses lists of
    the LaTeX sources: what the statement and its proof use, what uses it, where
    its proof is when that is in another entry, its tag and its proof tree.
  * The line "% map-of-the-encyclopaedia" in index.md becomes the map, drawn by
    widgets/encyclopaedia-map.mjs from data that latex/tools/site_map.py reads
    from the LaTeX sources.

Usage: python3 tools/site_map.py        (from the myst/ folder or anywhere)
"""
import json
import re
import sys
from pathlib import Path

MYST = Path(__file__).resolve().parent.parent
ROOT = MYST.parent
sys.path.insert(0, str(ROOT / "latex" / "tools"))
import site_map  # noqa: E402  (latex/tools/site_map.py)

SITE = "https://topologicaldynamics.org"
MARK = "% map-of-the-encyclopaedia"
DONE = "% statement-links"
DIRECTIVE = re.compile(r"^:::\{prf:(\w+)\}(.*)$")
OPTION = re.compile(r"^:(\w+):\s*(.*)$")
ABBR = {"definition": "Def.", "theorem": "Thm.", "proposition": "Prop.", "corollary": "Cor.",
        "lemma": "Lem.", "conjecture": "Conj.", "example": "Ex.", "remark": "Rem."}
LONGEST = 12  # longer lists end with a link to the tag page


def myst_label(label):
    return label.replace(":", "-", 1)


class Context:
    def __init__(self, src):
        self.st = {s["label"]: s for s in src["statements"]}
        self.numbers = {l: s["num"] for l, s in self.st.items()}
        self.aliases = src["aliases"]
        self.numbers.update({a: self.numbers[l] for a, l in self.aliases.items()})
        self.deps = src["deps"]
        self.used_by = {}
        for v, d in self.deps.items():
            for u in d["statement"] + d["proof"]:
                if u in self.st and v in self.st and u != v:
                    self.used_by.setdefault(u, set()).add(v)
        # Proofs of each entry, in order, and the label each will carry.
        self.proofs, self.proof_label, seen = {}, {}, {}
        for p in src["proofs"]:
            t = p["target"]
            seen[t] = seen.get(t, 0) + 1
            lab = "proof-" + myst_label(t) + ("" if seen[t] == 1 else f"-{seen[t]}")
            self.proofs.setdefault(p["file"], []).append((t, lab, p["section"]))
            self.proof_label.setdefault(t, (lab, p["section"]))
        self.tags = {}
        for line in (ROOT / "latex" / "tags").read_text().splitlines():
            parts = line.split()
            if len(parts) == 2 and not line.startswith("#"):
                self.tags[parts[1]] = parts[0]

    def ref(self, label):
        s = self.st[label]
        return f"{{prf:ref}}`{ABBR.get(s['kind'], s['kind'])} {s['num']} <{myst_label(label)}>`"

    def listing(self, labels, label):
        keys = sorted((l for l in labels if l in self.st and l != label),
                      key=lambda l: tuple(int(x) for x in self.st[l]["num"].split(".")))
        shown = ", ".join(self.ref(l) for l in keys[:LONGEST])
        if len(keys) > LONGEST and label in self.tags:
            shown += f", [and {len(keys) - LONGEST} more]({SITE}/latex/tag/{self.tags[label]}.html)"
        return shown

    def block(self, label):
        s, d = self.st[label], self.deps.get(label, {"statement": [], "proof": []})
        rows = []
        if self.listing(d["statement"], label):
            rows.append("**Uses** " + self.listing(d["statement"], label))
        if self.listing(d["proof"], label):
            rows.append("**Its proof uses** " + self.listing(d["proof"], label))
        if self.listing(self.used_by.get(label, ()), label):
            rows.append("**Used by** " + self.listing(self.used_by[label], label))
        last = []
        if label in self.proof_label and self.proof_label[label][1] != s["section"]:
            lab, sec = self.proof_label[label]
            last.append(f"**Proof** in {{prf:ref}}`Section {sec} <{lab}>`")
        last.append(f"[Proof tree]({SITE}/proof-tree/#tree={label})")
        if label in self.tags:
            tag = self.tags[label]
            last.append(f"[Tag {tag}]({SITE}/latex/tag/{tag}.html)")
        rows.append(" · ".join(last))
        return [":::{div}", ":class: dep-links", ""] + "\n\n".join(rows).split("\n") + [":::"]


def annotate(path, ctx):
    """Numbers, proof labels and link blocks for one entry."""
    lines = path.read_text().split("\n")
    if DONE in lines:
        return 0, 0, []
    proofs = list(ctx.proofs.get(path.stem, []))
    out, numbered, linked, missing = [], 0, 0, []
    i = 0
    while i < len(lines):
        m = DIRECTIVE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        kind, j, options = m.group(1), i + 1, {}
        while j < len(lines) and OPTION.match(lines[j]):
            k, v = OPTION.match(lines[j]).groups()
            options[k] = v.strip()
            j += 1
        out += lines[i:j]
        end = j
        while end < len(lines) and lines[end].strip() != ":::":
            end += 1
        tex = options.get("label", "").replace("-", ":", 1)
        if kind == "proof":
            target, lab, _ = proofs.pop(0) if proofs else (None, None, None)
            if "label" not in options and lab:
                out.append(f":label: {lab}")
            if "enumerated" not in options and "nonumber" not in options:
                out.append(":enumerated: false")
            out += lines[j:end + 1]
        else:
            if "label" in options and "enumerator" not in options:
                if tex in ctx.numbers:
                    out.append(f":enumerator: {ctx.numbers[tex]}")
                    numbered += 1
                else:
                    missing.append(options["label"])
            out += lines[j:end + 1]
            label = tex if tex in ctx.st else ctx.aliases.get(tex)
            if label:
                out += [""] + ctx.block(label)
                linked += 1
        i = end + 1
    out += ["", DONE]
    path.write_text("\n".join(out))
    if proofs:
        missing.append(f"{len(proofs)} LaTeX proofs of {path.stem} without a MyST twin")
    return numbered, linked, missing


def check_proofs(path, ctx):
    """The proof labels taken from the LaTeX twins, against the MyST text: each MyST
    proof should follow its statement or name it in its title."""
    lines, expected = path.read_text().split("\n"), list(ctx.proofs.get(path.stem, []))
    last, odd = None, []
    for k, line in enumerate(lines):
        m = DIRECTIVE.match(line)
        if not m:
            lab = OPTION.match(line)
            if lab and lab.group(1) == "label" and not lab.group(2).startswith("proof-"):
                last = lab.group(2).strip().replace("-", ":", 1)
            continue
        if m.group(1) == "proof" and expected:
            target = expected.pop(0)[0]
            # A proof away from its statement names it: "*Proof of {prf:ref}`thm-x`.*"
            first = next((x for x in lines[k + 1:k + 6] if x.strip() and not OPTION.match(x)), "")
            named = re.findall(r"prf:ref\}`([^`<]+)`", m.group(2) + " " + first.split(".*")[0])
            if target != last and myst_label(target) not in [n.strip() for n in named]:
                odd.append(f"{path.stem}: proof of {target} follows {last}")
    return odd


def main():
    src = site_map.read(ROOT / "latex")
    ctx = Context(src)
    entries = sorted((MYST / "entries").glob("*.md"))
    odd = [x for path in entries for x in check_proofs(path, ctx)]
    total_n = total_l = 0
    missing = []
    for path in entries:
        n, l, lost = annotate(path, ctx)
        total_n += n
        total_l += l
        missing += lost
    print(f"Numbered {total_n} MyST statements as in the LaTeX version and linked {total_l}")
    if missing:
        print("Not matched with the LaTeX version:", ", ".join(missing))
    if odd:
        print("Proofs to check (labels follow the LaTeX order):", "; ".join(odd))

    index = MYST / "index.md"
    text = index.read_text()
    if MARK in text:
        data = json.dumps({"data": site_map.map_data(src, "myst")}, ensure_ascii=False)
        block = ("## Map of the encyclopaedia\n\n"
                 ":::{anywidget} ./widgets/encyclopaedia-map.mjs\n"
                 ":class: col-page-right\n" + data + "\n:::")
        index.write_text(text.replace(MARK, block, 1))
        print("Drew the map of the encyclopaedia in index.md")


if __name__ == "__main__":
    main()
