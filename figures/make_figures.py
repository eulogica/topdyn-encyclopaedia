#!/usr/bin/env python3
"""Draw the figures of the encyclopaedia as SVG files, in this folder.

Both versions use these files: the MyST pages show them directly, the LaTeX site
shows them in place of the PDF copies that latex/build.sh makes for pdflatex.
Edit a figure here and run the script again; commit the SVG files with it.

Usage: python3 figures/make_figures.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
INK, SOFT, FAINT = "#25303b", "#5d6873", "#b7bfc6"
BLUE, BLUE_FILL, ORANGE, ORANGE_FILL = "#2f63b8", "#dbe6f7", "#c4661f", "#f8e3d2"
SERIF = "'STIX Two Text','Times New Roman',Times,serif"


def svg(width, height, body, title, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-label="{title}">\n'
            f'<title>{title}</title>\n'
            '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/>'
            f'</marker>{defs}</defs>\n'
            f'<g font-family="{SERIF}" font-size="17" fill="{INK}">\n{body}\n</g>\n</svg>\n')


def text(x, y, s, size=17, anchor="middle", italic=False, color=INK, weight="normal"):
    style = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
            f'fill="{color}" font-weight="{weight}"{style}>{s}</text>')


def math(x, y, s, size=18, anchor="middle", color=INK):
    """A formula: letters in italic, everything else upright (pass <tspan> for mixtures)."""
    return text(x, y, s, size, anchor, italic=True, color=color)


def line(x1, y1, x2, y2, color=INK, width=1.5, dash=None, arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    a = ' marker-end="url(#arrow)"' if arrow else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
            f'stroke-width="{width}"{d}{a}/>')


def circle(x, y, r, fill="#fff", stroke=INK, width=1.5):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{width}"/>')


def ellipse(cx, cy, rx, ry, fill="none", stroke=INK, width=1.5, rotate=0, opacity=1):
    t = f' transform="rotate({rotate} {cx:.1f} {cy:.1f})"' if rotate else ""
    return (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" '
            f'fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{width}"{t}/>')


def path(d, color=INK, width=1.5, fill="none", dash=None, arrow=False, arrow_start=False):
    s = f' stroke-dasharray="{dash}"' if dash else ""
    a = (' marker-end="url(#arrow)"' if arrow else "") + \
        (' marker-start="url(#arrow)"' if arrow_start else "")
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}"{s}{a}/>'


def hat(x, y, w):
    """A wide hat over a formula centred at x, whose letters top out near y."""
    return path(f"M{x - w / 2:.1f},{y + 4:.1f} L{x:.1f},{y - 3:.1f} L{x + w / 2:.1f},{y + 4:.1f}",
                width=1.2)


# --- Proposition 14.3 and Theorem 14.4 (Uspenskij) -------------------------------------

def uspenskij_chains():
    body = []
    # (a) A maximal chain of closed sets, shrinking to its root.
    root, centre = (120.0, 205.0), (175.0, 150.0)
    for k in range(7):
        s = 1 - k / 7
        cx = root[0] + s * (centre[0] - root[0])
        cy = root[1] + s * (centre[1] - root[1])
        fill = BLUE_FILL if k else "none"
        body.append(ellipse(cx, cy, 8 + 130 * s, 6 + 100 * s, fill=fill, stroke=INK if k == 0 else BLUE,
                            width=2 if k == 0 else 1.2, opacity=0.35 if k else 1))
    body.append(circle(*root, 4, fill=INK, stroke=INK))
    body.append(line(root[0] - 4, root[1] + 4, 62, 262, SOFT, 1))
    body.append(math(50, 280, "r(c)", 17))
    body.append(math(285, 70, "X", 19))
    body.append(text(175, 290, "(a)", 16, color=SOFT))
    # (b) The contradiction: F and gF both lie in the chain f(x), but are not comparable.
    body.append(ellipse(510, 160, 160, 115, stroke=INK, width=2))
    body.append(math(655, 70, "X", 19))
    body.append(ellipse(465, 165, 78, 58, fill=BLUE_FILL, stroke=BLUE, width=1.6, opacity=0.6))
    body.append(ellipse(555, 165, 78, 58, fill=ORANGE_FILL, stroke=ORANGE, width=1.6, opacity=0.6))
    body.append(math(420, 112, "F", 19, color=BLUE))
    body.append(math(612, 112, "gF", 19, color=ORANGE))
    x, y, z = (510, 150), (440, 185), (582, 185)
    for (px, py), name in ((x, "x"), (y, "y"), (z, "z")):
        body.append(circle(px, py, 3.5, fill=INK, stroke=INK))
    body.append(math(x[0], x[1] - 10, "x", 17))
    body.append(math(y[0] - 10, y[1] + 22, "y", 17))
    body.append(math(z[0] + 10, z[1] + 22, "z", 17))
    body.append(path(f"M{y[0] + 6},{y[1] + 10} Q510,250 {z[0] - 6},{z[1] + 10}", width=1.3,
                     arrow=True, arrow_start=True))
    body.append(math(510, 246, "g", 17))
    body.append(text(510, 290, "(b)", 16, color=SOFT))
    return svg(680, 300, "\n".join(body),
               "A maximal chain of closed sets with its root; and two members F and gF of one "
               "chain, neither containing the other")


# --- Example 15.3: the standard chain on the Cantor set -----------------------------

def cantor_intervals(depth):
    ivs = [(0.0, 1.0)]
    for _ in range(depth):
        ivs = [p for a, b in ivs for p in ((a, a + (b - a) / 3), (b - (b - a) / 3, b))]
    return ivs


def cantor_chain():
    ivs = cantor_intervals(6)
    x0, x1 = 120.0, 640.0
    X = lambda t: x0 + (x1 - x0) * t
    rows = [(0, "0"), (1 / 9, "1/9"), (1 / 3, "1/3"), (2 / 3, "2/3"), (7 / 9, "7/9"), (1, "1")]
    # The intervals are drawn once, in <defs>, and every row reuses them: in grey, and in
    # blue clipped at t, which colours exactly the intervals that end by t.
    cantor = "".join(f'<rect x="{X(a):.2f}" y="-4" width="{max(X(b) - X(a), 0.6):.2f}" height="8"/>'
                     for a, b in ivs)
    defs = [f'<g id="cantor">{cantor}</g>']
    body = []
    y = 40.0
    body.append(text(64, y + 5, "E", 18, italic=True))
    body.append(f'<use xlink:href="#cantor" transform="translate(0 {y}) scale(1 1.25)" fill="{INK}"/>')
    body.append(text(X(0), y + 26, "0", 14, color=SOFT))
    body.append(text(X(1), y + 26, "1", 14, color=SOFT))
    # The first gap of E.
    body.append(path(f"M{X(1 / 3) + 2},{y + 14} q0,8 8,8 L{X(2 / 3) - 10},{y + 22} q8,0 8,-8",
                     color=SOFT, width=1.1))
    body.append(text(X(0.5), y + 40, 'a gap: <tspan font-style="italic">E</tspan> ∩ [0, '
                     '<tspan font-style="italic">t</tspan>] is the same for every '
                     '<tspan font-style="italic">t</tspan> in it', 13, color=SOFT))
    y = 105.0
    for k, (t, label) in enumerate(rows):
        body.append(text(64, y + 5, f'<tspan font-style="italic">t</tspan> = {label}', 15))
        body.append(f'<use xlink:href="#cantor" transform="translate(0 {y})" fill="{FAINT}"/>')
        if t > 0:
            defs.append(f'<clipPath id="upto{k}"><rect x="0" y="-10" width="{X(t) + 0.3:.2f}" '
                        f'height="20"/></clipPath>')
            body.append(f'<use xlink:href="#cantor" transform="translate(0 {y})" fill="{BLUE}" '
                        f'clip-path="url(#upto{k})"/>')
        # t itself, when it is the left end of a surviving interval: E ∩ [0, t] gains one point.
        if any(abs(a - t) < 1e-12 for a, b in ivs):
            body.append(circle(X(t), y, 4.5, fill=BLUE, stroke=BLUE))
        y += 26
    return svg(680, 270, "\n".join(body),
               "The Cantor set E and the members E ∩ [0, t] of the standard chain for six values of t",
               defs="".join(defs))


# --- Lemma 24.10: rays in the tree of the free group ---------------------------------

def tree_rays():
    body = []
    n, step, y0 = 6, 58.0, 210.0
    ray = [(70 + step * k, y0) for k in range(10)]           # v_0 = 1, v_1, ... toward xi
    u1, h = (ray[1][0] + 30, y0 - 62), (ray[1][0] + 60, y0 - 124)   # h = v_1 u_1 h, |h| = 3
    # Faint stubs: the rest of the four-valent tree.
    for k, (x, y) in enumerate(ray):
        for dx, dy in ((-18, 30), (18, 30)) if k != 1 else ((18, 30),):
            body.append(line(x, y, x + dx, y + dy, FAINT, 1.2))
        if k != 1:
            body.append(line(x, y, x - 14, y - 30, FAINT, 1.2))
    body.append(line(ray[0][0], y0, ray[0][0] - 40, y0, FAINT, 1.2))
    for (x, y) in (u1, h):
        for dx, dy in ((-24, -10), (22, -14), (-6, -30)):
            body.append(line(x, y, x + dx, y + dy, FAINT, 1.2))
    # The ray from 1 toward xi, and the path from h onto it.
    body.append(line(ray[0][0], y0, ray[-1][0] + 40, y0, INK, 2, arrow=True))
    body.append(math(ray[-1][0] + 52, y0 + 6, "ξ", 20, anchor="start"))
    body.append(line(ray[1][0], y0, u1[0], u1[1], INK, 2))
    body.append(line(u1[0], u1[1], h[0], h[1], INK, 2))
    first_1 = ray[:n]
    first_h = [h, u1] + ray[1:n - 1]
    shared = [p for p in first_1 if p in first_h]
    for p in ray + [u1, h]:
        filled = p in first_1
        body.append(circle(p[0], p[1], 7, fill=BLUE if filled else "#fff",
                           stroke=BLUE if filled else INK, width=1.5))
    for p in first_h:
        body.append(circle(p[0], p[1], 12, fill="none", stroke=ORANGE, width=2.2))
    body.append(text(ray[0][0], y0 + 30, "1", 17))
    body.append(math(h[0] + 20, h[1] + 5, "h", 18, anchor="start"))
    # Legend.
    lx, ly = 400, 50
    body.append(circle(lx, ly, 7, fill=BLUE, stroke=BLUE))
    body.append(text(lx + 18, ly + 5, f'first <tspan font-style="italic">n</tspan> = {n} vertices of '
                     'the ray from 1', 15, anchor="start"))
    body.append(circle(lx, ly + 28, 11, fill="none", stroke=ORANGE, width=2.2))
    body.append(text(lx + 18, ly + 33, f'first <tspan font-style="italic">n</tspan> = {n} vertices of '
                     'the ray from <tspan font-style="italic">h</tspan>', 15, anchor="start"))
    body.append(text(lx - 10, ly + 66, f'shared: {len(shared)}, at least <tspan font-style="italic">n'
                     f'</tspan> − |<tspan font-style="italic">h</tspan>| = {n - 3}', 15,
                     anchor="start", color=SOFT))
    return svg(680, 280, "\n".join(body),
               "Rays toward a boundary point of the tree of the free group, from 1 and from h, "
               "and the vertices their first n vertices share")


# --- Lemma 26.19: Bratteli diagrams ---------------------------------------------------

def bratteli():
    body = []
    def diagram(x0, sizes, edges, keep, label, tag):
        dy, dx = 62.0, 120.0
        pos = {}
        for lvl, row in enumerate(sizes):
            for j, d in enumerate(row):
                pos[lvl, j] = (x0 + j * dx, 46 + lvl * dy)
        for lvl in range(len(sizes) - 1):
            for j, k in edges:
                (xa, ya), (xb, yb) = pos[lvl, j], pos[lvl + 1, k]
                hot = keep is not None and j == keep and k == keep
                body.append(line(xa, ya + 15, xb, yb - 15, ORANGE if hot else INK, 2.2 if hot else 1.4))
        for (lvl, j), (x, y) in pos.items():
            hot = keep is not None and j == keep
            body.append(circle(x, y, 15, fill=ORANGE_FILL if hot else BLUE_FILL,
                               stroke=ORANGE if hot else BLUE, width=1.6))
            body.append(text(x, y + 6, str(sizes[lvl][j]), 16))
        body.append(text(x0 + dx / 2, 46 + len(sizes) * dy - 8, "⋮", 18, color=SOFT))
        body.append(text(x0 + dx / 2, 46 + len(sizes) * dy + 22, label, 15, color=SOFT))
        body.append(text(x0 + dx / 2, 46 + len(sizes) * dy + 44, tag, 16, color=SOFT))
    for lvl in range(4):
        body.append(math(40, 52 + lvl * 62, f"F<tspan baseline-shift='sub' font-size='12'>{lvl + 1}</tspan>",
                         17))
    diagram(110, [(1, 1), (2, 2), (4, 4), (8, 8)], [(0, 0), (0, 1), (1, 0), (1, 1)], None,
            "every block grows", "(a)")
    diagram(430, [(1, 1), (1, 2), (1, 3), (1, 4)], [(0, 0), (0, 1), (1, 1)], 0,
            "a block of size 1 at every level", "(b)")
    return svg(680, 345, "\n".join(body),
               "Two Bratteli diagrams with their block sizes: in one every block grows, in the "
               "other a block of size 1 survives at every level")


# --- Proposition 12.2: the completion argument ----------------------------------------

def completion_pattern():
    body = []
    G, GH, C, X = (90, 70), (300, 70), (540, 70), (420, 210)
    body.append(math(*G, "G", 20))
    body.append(math(*GH, "G/H", 20))
    body.append(math(*C, "G/H", 20))
    body.append(hat(C[0], C[1] - 18, 38))
    body.append(math(X[0], X[1], "X", 20))
    body.append(line(G[0] + 22, G[1] - 6, GH[0] - 34, GH[1] - 6, arrow=True))
    body.append(line(GH[0] + 34, GH[1] - 6, C[0] - 34, C[1] - 6, arrow=True, dash="5 4"))
    body.append(text(420, 50, "dense", 14, color=SOFT))
    body.append(line(GH[0] + 14, GH[1] + 14, X[0] - 22, X[1] - 22, BLUE, 1.8, arrow=True))
    body.append(text(300, 168, '<tspan font-style="italic">gH</tspan> ↦ '
                     '<tspan font-style="italic">g</tspan><tspan font-style="italic">x</tspan>'
                     '<tspan baseline-shift="sub" font-size="12">0</tspan>', 17, color=BLUE))
    body.append(line(C[0] - 12, C[1] + 14, X[0] + 22, X[1] - 22, ORANGE, 1.8, arrow=True))
    body.append(text(590, 150, "extends; onto,", 14, color=ORANGE))
    body.append(text(590, 168, "by minimality", 14, color=ORANGE))
    body.append(text(420, 248, "a minimal flow, with a point "
                     '<tspan font-style="italic">x</tspan><tspan baseline-shift="sub" font-size="12">0</tspan>'
                     ' fixed by the extremely amenable subgroup '
                     '<tspan font-style="italic">H</tspan>', 14, color=SOFT))
    return svg(680, 270, "\n".join(body),
               "From G to its quotient by H and the completion, and from both onto a minimal flow X")


# --- Proposition 20.1: an extremely amenable normal subgroup ---------------------------

def kernel_pattern():
    body = []
    xs = [80, 200, 340, 480, 600]
    labels = ["1", "N", "G", "G/N", "1"]
    for x, s in zip(xs, labels):
        body.append(math(x, 62, s, 20) if s != "1" else text(x, 62, s, 20))
    for a, b in zip(xs, xs[1:]):
        body.append(line(a + 22, 56, b - 26, 56, arrow=True))
    body.append(text(200, 90, "extremely amenable", 14, color=SOFT))
    X = (410, 215)
    body.append(ellipse(X[0], X[1], 70, 34, fill=BLUE_FILL, stroke=BLUE, opacity=0.6))
    body.append(math(X[0], X[1] + 6, "X", 20))
    body.append(path(f"M{xs[2]},{78} Q{xs[2] - 10},{150} {X[0] - 58},{X[1] - 18}", BLUE, 1.6, arrow=True))
    body.append(path(f"M{xs[3]},{78} Q{xs[3] + 10},{150} {X[0] + 58},{X[1] - 18}", ORANGE, 1.6,
                     arrow=True))
    body.append(text(272, 150, "acts", 14, color=BLUE))
    body.append(text(555, 150, "acts through", 14, color=ORANGE))
    body.append(text(555, 168, "the quotient", 14, color=ORANGE))
    body.append(text(410, 272, "every point of a minimal flow is fixed by "
                     '<tspan font-style="italic">N</tspan>', 14, color=SOFT))
    return svg(680, 290, "\n".join(body),
               "An exact sequence with extremely amenable kernel N, and a minimal flow X on which "
               "G acts through the quotient G/N")


FIGURES = {
    "uspenskij-chains": uspenskij_chains,
    "cantor-chain": cantor_chain,
    "tree-rays": tree_rays,
    "bratteli": bratteli,
    "completion-pattern": completion_pattern,
    "kernel-pattern": kernel_pattern,
}

if __name__ == "__main__":
    for name, draw in FIGURES.items():
        (HERE / f"{name}.svg").write_text(draw())
    print(f"Wrote {len(FIGURES)} figures in {HERE}")
