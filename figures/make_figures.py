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


# --- Proposition 4.5: the greatest ambit -----------------------------------------------

def greatest_ambit():
    body = []
    # S(G), with G dense in it and the base point 1.
    body.append(ellipse(170, 140, 130, 95, fill=BLUE_FILL, stroke=BLUE, width=1.8, opacity=0.5))
    body.append(math(60, 62, "S(G)", 19, anchor="start"))
    for k, (x, y) in enumerate([(110, 115), (150, 95), (205, 110), (240, 150), (120, 175),
                                (175, 190), (215, 200), (90, 145), (185, 145), (145, 140)]):
        body.append(circle(x, y, 2.6, fill=BLUE, stroke=BLUE, width=1))
    body.append(text(170, 258, "<tspan font-style=\"italic\">G</tspan>, dense in "
                     "<tspan font-style=\"italic\">S</tspan>(<tspan font-style=\"italic\">G</tspan>)",
                     14, color=BLUE))
    one = (150, 140)
    body.append(circle(*one, 5, fill=INK, stroke=INK))
    body.append(text(one[0] - 12, one[1] + 5, "1", 17, anchor="end"))
    # The ambit (X, x0).
    body.append(ellipse(540, 140, 105, 80, stroke=INK, width=1.8))
    body.append(math(630, 70, "X", 19))
    x0 = (525, 135)
    body.append(circle(*x0, 5, fill=INK, stroke=INK))
    body.append(math(x0[0] + 12, x0[1] + 6, "x<tspan baseline-shift=\"sub\" font-size=\"12\">0</tspan>",
                     17, anchor="start"))
    g, gx0 = (205, 110), (570, 100)
    body.append(circle(*gx0, 3, fill=INK, stroke=INK))
    body.append(math(gx0[0] + 9, gx0[1] - 6, "gx<tspan baseline-shift=\"sub\" font-size=\"12\">0</tspan>",
                     16, anchor="start"))
    body.append(math(g[0] + 6, g[1] - 9, "g", 16, anchor="start"))
    body.append(path(f"M{one[0] + 8},{one[1] + 2} C300,175 400,170 {x0[0] - 9},{x0[1] + 3}",
                     ORANGE, 1.8, arrow=True))
    body.append(path(f"M{g[0] + 5},{g[1] - 2} C320,60 470,60 {gx0[0] - 6},{gx0[1] - 2}",
                     ORANGE, 1.5, arrow=True, dash="5 4"))
    body.append(text(355, 198, "the unique morphism of ambits", 14, color=ORANGE))
    body.append(text(355, 216, "(<tspan font-style=\"italic\">S</tspan>(<tspan font-style=\"italic\">G</tspan>), 1) "
                     "→ (<tspan font-style=\"italic\">X</tspan>, <tspan font-style=\"italic\">x</tspan>"
                     "<tspan baseline-shift=\"sub\" font-size=\"11\">0</tspan>)", 14, color=ORANGE))
    return svg(680, 270, "\n".join(body),
               "The greatest ambit S(G), with G dense in it, and its morphism onto an ambit (X, x0), "
               "sending 1 to x0 and g to gx0")


# --- Theorem 9.3 (Pestov): the circle -------------------------------------------------

def pestov_circle():
    import math as m
    body = []
    # (a) The circle cut at theta, and the interval it becomes.
    c, r = (130, 130), 70
    body.append(circle(*c, r, fill="none", stroke=INK, width=2))
    th = (c[0], c[1] - r)
    body.append(circle(*th, 5, fill=ORANGE, stroke=ORANGE))
    body.append(math(th[0], th[1] - 12, "θ", 18))
    # An orientation-preserving homeomorphism fixing theta moves the other points along.
    for a0, a1 in ((40, 70), (150, 185), (250, 275)):
        p0 = (c[0] + (r + 12) * m.sin(m.radians(a0)), c[1] - (r + 12) * m.cos(m.radians(a0)))
        p1 = (c[0] + (r + 12) * m.sin(m.radians(a1)), c[1] - (r + 12) * m.cos(m.radians(a1)))
        body.append(path(f"M{p0[0]:.1f},{p0[1]:.1f} A{r + 12},{r + 12} 0 0 1 {p1[0]:.1f},{p1[1]:.1f}",
                         BLUE, 1.5, arrow=True))
    body.append(line(225, 130, 275, 130, arrow=True))
    body.append(text(250, 118, "cut at <tspan font-style=\"italic\">θ</tspan>", 13, color=SOFT))
    body.append(line(292, 130, 402, 130, INK, 2))
    for x in (292, 402):
        body.append(circle(x, 130, 5, fill=ORANGE, stroke=ORANGE))
    body.append(math(292, 155, "θ", 17))
    body.append(math(402, 155, "θ", 17))
    body.append(path("M310,118 Q330,100 350,116", BLUE, 1.5, arrow=True))
    body.append(path("M360,118 Q373,106 386,116", BLUE, 1.5, arrow=True))
    body.append(text(240, 236, "(a) the stabiliser of <tspan font-style=\"italic\">θ</tspan> "
                     "≅ Homeo<tspan baseline-shift=\"sub\" font-size=\"11\">+</tspan>[0, 1]",
                     15, color=SOFT))
    # (b) The map onto a flow X.
    c2 = (535, 130)
    body.append(circle(c2[0] - 55, c2[1], 38, fill="none", stroke=INK, width=1.8))
    body.append(circle(c2[0] - 55, c2[1] - 38, 4, fill=ORANGE, stroke=ORANGE))
    body.append(math(c2[0] - 55, c2[1] - 50, "θ", 16))
    body.append(math(c2[0] - 55, c2[1] + 62, "\U0001d54a<tspan baseline-shift=\"super\" font-size=\"11\">1</tspan>",
                     17))
    body.append(ellipse(c2[0] + 80, c2[1], 50, 40, stroke=INK, width=1.8))
    body.append(math(c2[0] + 80, c2[1] + 62, "X", 17))
    body.append(circle(c2[0] + 72, c2[1] - 8, 4, fill=INK, stroke=INK))
    body.append(math(c2[0] + 84, c2[1] - 12, "x′", 16, anchor="start"))
    body.append(path(f"M{c2[0] - 50},{c2[1] - 40} C{c2[0]},{c2[1] - 75} {c2[0] + 35},{c2[1] - 50} "
                     f"{c2[0] + 66},{c2[1] - 13}", ORANGE, 1.7, arrow=True))
    body.append(text(c2[0] + 18, c2[1] - 66, "<tspan font-style=\"italic\">gθ</tspan> ↦ "
                     "<tspan font-style=\"italic\">gx′</tspan>", 15, color=ORANGE))
    body.append(text(c2[0] + 18, 236, "(b) onto every minimal flow", 15, color=SOFT))
    return svg(680, 250, "\n".join(body),
               "The circle cut at a point theta becomes an interval, and the map from the circle to a "
               "flow X sending g theta to g x'")


# --- Definition 11.2: the Ramsey property, for finite linear orders -------------------------

RAMSEY_POINTS = 6
RAMSEY_TRIPLE = (0, 2, 4)              # the copy B' of B, drawn in the colour of its pairs


def ramsey_colouring():
    """A colouring of the pairs of {0, ..., 5} in two colours, with RAMSEY_TRIPLE
    monochromatic in colour 0. Fixed, so that the figure does not change."""
    pattern = "011010101101001"            # one digit per pair, in lexicographic order
    pairs = [(i, j) for i in range(RAMSEY_POINTS) for j in range(i + 1, RAMSEY_POINTS)]
    colour = dict(zip(pairs, (int(d) for d in pattern)))
    for i in RAMSEY_TRIPLE:
        for j in RAMSEY_TRIPLE:
            if i < j:
                colour[i, j] = 0
    return colour


def ramsey_property():
    body = []
    colour = ramsey_colouring()
    x0, dx, y = 110, 92, 220
    X = lambda i: x0 + dx * i
    triple = set(RAMSEY_TRIPLE)
    for (i, j), col in sorted(colour.items(), key=lambda e: (e[0][0] in triple and e[0][1] in triple)):
        hot = i in triple and j in triple
        rx = (X(j) - X(i)) / 2
        ry = 26 + 26 * (j - i)
        stroke = BLUE if col == 0 else ORANGE
        body.append(path(f"M{X(i)},{y - 8} A{rx:.1f},{ry} 0 0 1 {X(j)},{y - 8}", stroke,
                         3.2 if hot else 1.2, dash=None if col == 0 else "6 4"))
    body.append(line(X(0) - 30, y, X(RAMSEY_POINTS - 1) + 30, y, SOFT, 1.2))
    for i in range(RAMSEY_POINTS):
        hot = i in triple
        body.append(circle(X(i), y, 7, fill=BLUE if hot else "#fff", stroke=BLUE if hot else INK, width=1.6))
        body.append(text(X(i), y + 28, str(i + 1), 15, color=SOFT))
    body.append(math(X(RAMSEY_POINTS - 1) + 48, y + 6, "C", 19, anchor="start"))
    # Legend.
    body.append(line(40, 26, 74, 26, BLUE, 2))
    body.append(text(82, 31, "colour 1", 14, anchor="start"))
    body.append(line(160, 26, 194, 26, ORANGE, 2, dash="6 4"))
    body.append(text(202, 31, "colour 2", 14, anchor="start"))
    body.append(line(300, 26, 334, 26, BLUE, 3.2))
    body.append(text(342, 31, "the pairs of a copy <tspan font-style=\"italic\">B</tspan>′ of "
                     "<tspan font-style=\"italic\">B</tspan>: one colour", 14, anchor="start"))
    return svg(680, 268, "\n".join(body),
               "A colouring of the pairs of a six-element linear order C in two colours, and three points "
               "whose three pairs have the same colour")


# --- Proposition 17.3: minimal left ideals of the greatest ambit --------------------------

def minimal_ideals():
    body = []
    body.append(ellipse(330, 140, 290, 112, fill="none", stroke=INK, width=2))
    body.append(math(62, 52, "S(G)", 19, anchor="start"))
    body.append(circle(110, 150, 5, fill=INK, stroke=INK))
    body.append(text(98, 155, "1", 16, anchor="end"))
    # Two minimal left ideals: the minimal subflows, each a copy of M(G).
    body.append(ellipse(420, 125, 95, 58, fill=BLUE_FILL, stroke=BLUE, width=1.7, opacity=0.6))
    body.append(math(470, 88, "M", 18, color=BLUE))
    body.append(ellipse(235, 195, 62, 34, fill=BLUE_FILL, stroke=BLUE, width=1.4, opacity=0.6))
    body.append(math(268, 182, "M′", 17, color=BLUE))
    body.append(text(235, 202, "≅ <tspan font-style=\"italic\">M</tspan>(<tspan font-style=\"italic\">G</tspan>)",
                     14, color=BLUE))
    u = (400, 130)
    body.append(circle(*u, 5, fill=ORANGE, stroke=ORANGE))
    body.append(math(u[0] - 12, u[1] + 5, "u", 17, anchor="end"))
    body.append(text(u[0], u[1] + 26, "<tspan font-style=\"italic\">u</tspan> = <tspan font-style=\"italic\">uu</tspan>",
                     13, color=ORANGE))
    # The retraction p -> pu.
    p, pu = (170, 105), (455, 140)
    body.append(circle(*p, 4, fill=INK, stroke=INK))
    body.append(math(p[0] - 10, p[1] + 5, "p", 17, anchor="end"))
    body.append(circle(*pu, 4, fill=INK, stroke=INK))
    body.append(math(pu[0] + 10, pu[1] + 18, "pu", 16, anchor="start"))
    body.append(path(f"M{p[0] + 7},{p[1] - 3} C260,55 380,60 {pu[0] - 3},{pu[1] - 8}", ORANGE, 1.7, arrow=True))
    return svg(680, 270, "\n".join(body),
               "The greatest ambit S(G) with two minimal left ideals M and M', an idempotent u in M, "
               "and the retraction of S(G) onto M sending p to pu")


# --- Example 3.3: an irrational rotation of the circle -----------------------------------

ROTATION_ALPHA = (5 ** 0.5 - 1) / 2        # irrational: the rotation is by 2*pi*alpha
ROTATION_DENSE = 100


def irrational_rotation():
    import math as m
    body = []
    labels = ["x", "Rx", "R²x", "R³x"]
    dots = []
    for panel, (cx, count) in enumerate(((170, 12), (510, ROTATION_DENSE))):
        cy, r = 135, 92
        body.append(circle(cx, cy, r, fill="none", stroke=INK, width=1.6))
        for k in range(count):
            a = 2 * m.pi * ((k * ROTATION_ALPHA) % 1)
            x, y = cx + r * m.sin(a), cy - r * m.cos(a)
            if panel == 0:
                hot = k == 0
                body.append(circle(x, y, 5.5 if hot else 4.5, fill=ORANGE if hot else BLUE,
                                   stroke=ORANGE if hot else BLUE, width=1))
                rr = r + (20 if k < 4 else 15)
                lx, ly = cx + rr * m.sin(a), cy - rr * m.cos(a) + 5
                if k < 4:
                    body.append(math(lx, ly, labels[k], 15))
                else:
                    body.append(text(lx, ly, str(k), 12, color=SOFT))
            else:
                dots.append(f"M{x:.1f},{y:.1f}h0")
        if panel == 1:
            body.append(f'<path d="{" ".join(dots)}" stroke="{BLUE}" stroke-width="4.4" '
                        f'stroke-linecap="round" fill="none"/>')
        if panel == 0:
            # The rotation by 2*pi*alpha, from x to Rx, drawn inside the circle.
            a1 = 2 * m.pi * ROTATION_ALPHA
            rr = r - 16
            p0 = (cx, cy - rr)
            p1 = (cx + rr * m.sin(a1), cy - rr * m.cos(a1))
            body.append(path(f"M{p0[0]:.1f},{p0[1]:.1f} A{rr},{rr} 0 1 1 {p1[0]:.1f},{p1[1]:.1f}",
                             ORANGE, 1.4, arrow=True))
            body.append(math(cx, cy + 6, "R", 17, color=ORANGE))
    body.append(text(170, 268, "(a) the first 12 points of the orbit", 15, color=SOFT))
    body.append(text(510, 268, f"(b) the first {ROTATION_DENSE} points", 15, color=SOFT))
    return svg(680, 280, "\n".join(body),
               f"The first 12 and the first {ROTATION_DENSE} points of an orbit of the rotation of the circle by an "
               "irrational multiple of 2 pi")


# --- Remark 8.3: concentration of measure on spheres ------------------------------------

def latitude_density(n, theta):
    """The density of the latitude of a random point of the sphere S^n (n >= 1), in the
    geodesic distance from the equator: proportional to cos(theta)^(n-1)."""
    import math as m
    c = m.cos(theta)
    return 0.0 if c <= 0 else c ** (n - 1)


def sphere_concentration():
    import math as m
    body = []
    # (a) A hemisphere H of the sphere and its epsilon-neighbourhood.
    cx, cy, r, eps = 140, 138, 90, 0.32
    h = r * m.sin(eps)                       # the edge of H_eps, above the equator
    w = (r * r - h * h) ** 0.5
    body.append(path(f"M{cx - r},{cy} A{r},{r} 0 0 0 {cx + r},{cy} A{r},{r * 0.28} 0 0 1 {cx - r},{cy} z",
                     BLUE, 0, fill=BLUE_FILL))
    body.append(path(f"M{cx - r},{cy} A{r},{r * 0.28} 0 0 0 {cx + r},{cy} "
                     f"A{r},{r} 0 0 0 {cx + w:.1f},{cy - h:.1f} A{w:.1f},{w * 0.28:.1f} 0 0 1 {cx - w:.1f},{cy - h:.1f} "
                     f"A{r},{r} 0 0 0 {cx - r},{cy} z", ORANGE, 0, fill=ORANGE_FILL))
    body.append(circle(cx, cy, r, fill="none", stroke=INK, width=1.8))
    body.append(ellipse(cx, cy, r, r * 0.28, stroke=INK, width=1.2))
    body.append(ellipse(cx, cy - h, w, w * 0.28, stroke=ORANGE, width=1.2))
    body.append(math(cx, cy + 58, "H", 18, color=BLUE))
    bx = cx + r + 14
    body.append(path(f"M{bx - 5},{cy + r} L{bx},{cy + r} L{bx},{cy - h:.1f} L{bx - 5},{cy - h:.1f}", ORANGE, 1.3))
    body.append(text(bx + 6, cy + 6, "<tspan font-style=\"italic\">H</tspan>"
                     "<tspan baseline-shift=\"sub\" font-size=\"12\" font-style=\"italic\">ε</tspan>",
                     17, anchor="start", color=ORANGE))
    ra = r + 10
    body.append(path(f"M{cx - ra},{cy} A{ra},{ra} 0 0 1 {cx - ra * m.cos(eps):.1f},{cy - ra * m.sin(eps):.1f}",
                     ORANGE, 1.6))
    for t in (0, eps):
        body.append(line(cx - (r + 5) * m.cos(t), cy - (r + 5) * m.sin(t),
                         cx - (r + 15) * m.cos(t), cy - (r + 15) * m.sin(t), ORANGE, 1.3))
    body.append(math(cx - ra * m.cos(eps / 2) - 8, cy - ra * m.sin(eps / 2) + 5, "ε", 15, anchor="end",
                     color=ORANGE))
    body.append(text(cx, 266, "(a) a hemisphere <tspan font-style=\"italic\">H</tspan> and its "
                     "<tspan font-style=\"italic\">ε</tspan>-neighbourhood", 15, color=SOFT))
    # (b) The distribution of the latitude for three values of n.
    x0, x1, yb, ht = 330, 650, 196, 150
    X = lambda t: x0 + (t + m.pi / 2) / m.pi * (x1 - x0)
    body.append(line(x0, yb, x1, yb, SOFT, 1.2))
    for t, lab in ((-m.pi / 2, "−π/2"), (0, "0"), (m.pi / 2, "π/2")):
        body.append(line(X(t), yb, X(t), yb + 5, SOFT, 1.2))
        body.append(text(X(t), yb + 19, lab, 13, color=SOFT))
    body.append(text((x0 + x1) / 2, yb + 37, "latitude (geodesic distance from the equator, with a sign)",
                     12, color=SOFT))
    curves = ((2, FAINT, "5 3"), (10, SOFT, None), (100, BLUE, None))
    steps = 160
    peak = None
    for n, colour, dash in curves:
        ts = [-m.pi / 2 + m.pi * i / steps for i in range(steps + 1)]
        vals = [latitude_density(n, t) for t in ts]
        total = sum(vals) * m.pi / steps
        dens = [v / total for v in vals]
        if peak is None:
            peak = max(latitude_density(100, t) for t in ts) / (
                sum(latitude_density(100, t) for t in ts) * m.pi / steps)
        pts = " ".join(f"{X(t):.1f},{yb - ht * d / peak:.1f}" for t, d in zip(ts, dens))
        body.append(f'<polyline points="{pts}" fill="none" stroke="{colour}" stroke-width="1.8"'
                    + (f' stroke-dasharray="{dash}"' if dash else "") + "/>")
    for t in (-eps, eps):
        body.append(line(X(t), yb, X(t), yb - ht - 6, ORANGE, 1.1, dash="4 3"))
    body.append(text(X(eps) + 4, yb - ht + 6, "<tspan font-style=\"italic\">ε</tspan>", 14,
                     anchor="start", color=ORANGE))
    body.append(text(X(-eps) - 4, yb - ht + 6, "−<tspan font-style=\"italic\">ε</tspan>", 14,
                     anchor="end", color=ORANGE))
    for n, colour, y in ((100, BLUE, 52), (10, SOFT, 72), (2, FAINT, 92)):
        body.append(line(x1 - 92, y - 4, x1 - 66, y - 4, colour, 1.8, dash="5 3" if n == 2 else None))
        body.append(text(x1 - 60, y, f"<tspan font-style=\"italic\">n</tspan> = {n}", 13,
                         anchor="start", color=INK))
    body.append(text((x0 + x1) / 2, 266, "(b) the latitude of a random point of "
                     "\U0001d54a<tspan baseline-shift=\"super\" font-size=\"10\" font-style=\"italic\">n</tspan>",
                     15, color=SOFT))
    return svg(680, 280, "\n".join(body),
               "A hemisphere of the sphere and its epsilon-neighbourhood, and the distribution of the "
               "latitude of a random point of the n-sphere for n = 2, 10 and 100")


# --- Definition 10.1: transporting a linear order by a permutation -------------------------

ORDER_EXAMPLE = [4, 1, 6, 3, 5, 2]          # a linear order on {1, ..., 6}, least first
PERM_EXAMPLE = {1: 2, 2: 3, 3: 1, 4: 4, 5: 6, 6: 5}


def transported_order():
    body = []
    g = PERM_EXAMPLE
    x0, dx, y1, y2 = 200, 72, 70, 190
    body.append(math(60, y1 + 6, "&lt;", 20))
    body.append(math(60, y2 + 6, "g·&lt;", 20))
    for i, a in enumerate(ORDER_EXAMPLE):
        x = x0 + dx * i
        body.append(circle(x, y1, 16, fill="#fff", stroke=INK, width=1.5))
        body.append(text(x, y1 + 6, str(a), 17))
        body.append(circle(x, y2, 16, fill=BLUE_FILL, stroke=BLUE, width=1.5))
        body.append(text(x, y2 + 6, str(g[a]), 17, color=BLUE))
        body.append(line(x, y1 + 19, x, y2 - 21, ORANGE, 1.4, arrow=True))
        if i:
            body.append(text(x - dx / 2, y1 + 6, "&lt;", 15, color=SOFT))
            body.append(text(x - dx / 2, y2 + 6, "&lt;", 15, color=SOFT))
    body.append(text(x0 + dx * 2.5, y1 - 30, "least  →  greatest", 13, color=SOFT))
    body.append(text(118, (y1 + y2) / 2 + 5, "<tspan font-style=\"italic\">a</tspan> ↦ "
                     "<tspan font-style=\"italic\">g</tspan>(<tspan font-style=\"italic\">a</tspan>)",
                     14, color=ORANGE))
    # The permutation g, in two-line notation.
    gx, gy = 200, 248
    body.append(math(gx, gy + 5, "g", 17, anchor="end"))
    body.append(text(gx + 8, gy + 5, "=", 17, anchor="start"))
    body.append(path(f"M{gx + 32},{gy - 18} Q{gx + 24},{gy} {gx + 32},{gy + 18}", INK, 1.2))
    for k in range(1, 7):
        body.append(text(gx + 30 + 18 * k, gy - 4, str(k), 14))
        body.append(text(gx + 30 + 18 * k, gy + 14, str(g[k]), 14, color=BLUE))
    body.append(path(f"M{gx + 150},{gy - 18} Q{gx + 158},{gy} {gx + 150},{gy + 18}", INK, 1.2))
    body.append(text(gx + 168, gy + 5, "on 1, …, 6, and <tspan font-style=\"italic\">g</tspan> fixes every "
                     "other number", 14, anchor="start", color=SOFT))
    return svg(680, 280, "\n".join(body),
               "A linear order on the numbers 1 to 6, listed from least to greatest, and the order "
               "transported by a permutation g, which lists g(a) where the first order lists a")


# --- Example 13.5 (2): convex orders on an equivalence relation -------------------------------

def class_mark(x, y, k, size=9):
    """Element of the k-th class: a circle, a square or a triangle, each in its colour."""
    if k == 0:
        return circle(x, y, size, fill=BLUE_FILL, stroke=BLUE, width=1.6)
    if k == 1:
        return (f'<rect x="{x - size:.1f}" y="{y - size:.1f}" width="{2 * size}" height="{2 * size}" '
                f'fill="{ORANGE_FILL}" stroke="{ORANGE}" stroke-width="1.6"/>')
    s = size * 1.25
    return (f'<polygon points="{x:.1f},{y - s:.1f} {x + s:.1f},{y + s * 0.75:.1f} '
            f'{x - s:.1f},{y + s * 0.75:.1f}" fill="#eef0f2" stroke="{INK}" stroke-width="1.6"/>')


CONVEX_ORDER = [0, 0, 0, 1, 1, 1, 2, 2, 2]
NONCONVEX_ORDER = [0, 1, 0, 2, 1, 0, 2, 2, 1]


def convex_orders():
    body = []
    x0, dx = 150, 52
    for row, (order, y, label) in enumerate(((CONVEX_ORDER, 80, "(a) convex: every class is an interval"),
                                             (NONCONVEX_ORDER, 200, "(b) not convex"))):
        body.append(line(x0 - 30, y, x0 + dx * 8 + 30, y, FAINT, 1.2, arrow=True))
        for i, k in enumerate(order):
            body.append(class_mark(x0 + dx * i, y, k))
        body.append(text(x0 + dx * 4, y + 52, label, 15, color=SOFT))
        if row == 0:
            for k in range(3):
                a, b = x0 + dx * 3 * k - 16, x0 + dx * (3 * k + 2) + 16
                body.append(path(f"M{a},{y - 20} L{a},{y - 27} L{b},{y - 27} L{b},{y - 20}", SOFT, 1.2))
        else:
            first = order.index(0)
            last = len(order) - 1 - order[::-1].index(0)
            a, b = x0 + dx * first - 16, x0 + dx * last + 16
            body.append(path(f"M{a},{y - 20} L{a},{y - 27} L{b},{y - 27} L{b},{y - 20}", BLUE, 1.2))
            body.append(text((a + b) / 2, y - 34, "the circles, with other points between them", 13,
                             color=BLUE))
    body.append(text(x0 + dx * 8 + 30, 30, "least → greatest", 13, anchor="end", color=SOFT))
    return svg(680, 270, "\n".join(body),
               "Nine points in three classes, drawn as circles, squares and triangles, in an order where "
               "each class is an interval and in an order where it is not")


# --- Definition 16.2: the Cantor fan and the Lelek fan -----------------------------------

def cantor_points(depth, left, width):
    """One point of the middle-thirds Cantor set in each of the 2^depth intervals of its
    depth-th stage (the left end in the left half, the right end in the right half, so
    that the picture is symmetric), scaled to [left, left + width]."""
    pts = [0.0]
    size = 1.0
    for _ in range(depth):
        size /= 3
        pts = [p for q in pts for p in (q, q + 2 * size)]
    return [left + width * (p if p < 0.5 else p + size) for p in pts]


def van_der_corput(k, bits):
    return sum(((k >> i) & 1) / 2 ** (i + 1) for i in range(bits))


def lelek_fan():
    body = []
    depth = 5
    for panel, (cx, label) in enumerate(((170, "(a) the Cantor fan"),
                                         (510, "(b) shorter blades, in the Cantor fan"))):
        top, bottom, width = 40, 222, 280
        xs = cantor_points(depth, cx - width / 2, width)
        body.append(circle(cx, top, 4, fill=INK, stroke=INK))
        body.append(math(cx, top - 10, "v", 17))
        if panel == 1:
            body.append(path(" ".join(f"M{cx} {top}L{x:.1f} {bottom}" for x in xs), FAINT, 0.7))
        blades, ends = [], []
        for k, x in enumerate(xs):
            t = 1.0 if panel == 0 else 0.18 + 0.82 * van_der_corput(k * 7 % 32, depth)
            ex, ey = cx + (x - cx) * t, top + (bottom - top) * t
            blades.append(f"M{cx} {top}L{ex:.1f} {ey:.1f}")
            ends.append(f"M{ex:.1f} {ey:.1f}h0")
        body.append(path(" ".join(blades), INK if panel == 0 else BLUE, 0.9))
        if panel == 1:
            body.append(f'<path d="{" ".join(ends)}" stroke="{ORANGE}" stroke-width="5" '
                        f'stroke-linecap="round" fill="none"/>')
        if panel == 0:
            body.append(text(cx + width / 2 + 6, bottom + 4, "<tspan font-style=\"italic\">C</tspan> × {1}",
                             13, anchor="start", color=SOFT))
        body.append(text(cx, 262, label, 15, color=SOFT))
    return svg(680, 275, "\n".join(body),
               "The Cantor fan, drawn with finitely many blades from its top v, and a fan whose blades have "
               "different lengths, with their endpoints marked")


# --- Definition 16.5: generalised Wazewski dendrites -------------------------------------

def dendrite_segments(p, q, depth, orders, out, marks, level=0):
    """Segments of a schematic dendrite on the arc from p to q: each arc gets one
    ramification point of each order in `orders`, at evenly spaced places; a point of
    order k carries k - 2 new branches. Recurse on all the pieces."""
    import math as m
    if depth == 0:
        out.append((p, q))
        return
    k = len(orders)
    pts = [(p[0] + (q[0] - p[0]) * i / (k + 1), p[1] + (q[1] - p[1]) * i / (k + 1)) for i in range(k + 2)]
    for i in range(k + 1):
        dendrite_segments(pts[i], pts[i + 1], depth - 1, orders, out, marks, level + 1)
    dx, dy = q[0] - p[0], q[1] - p[1]
    length = m.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    for i, order in enumerate(orders, start=1):
        c = pts[i]
        marks.append((c, order, level))
        branch = length * 0.42 / (k + 1) * 2
        sides = [1] if order == 3 else [1, -1]
        for j, s in enumerate(sides):
            sign = s * (1 if (level + i) % 2 == 0 else -1)
            ang = m.radians(64) * sign
            bx = ux * m.cos(ang) - uy * m.sin(ang)
            by = ux * m.sin(ang) + uy * m.cos(ang)
            dendrite_segments(c, (c[0] + bx * branch, c[1] + by * branch), depth - 1, orders, out, marks,
                              level + 1)


def wazewski():
    body = []
    for panel, (cx, orders, depth, label) in enumerate(
            ((170, [3], 5, "(a) <tspan font-style=\"italic\">W</tspan>"
                           "<tspan baseline-shift=\"sub\" font-size=\"11\">{3}</tspan>"),
             (510, [3, 4], 3, "(b) <tspan font-style=\"italic\">W</tspan>"
                              "<tspan baseline-shift=\"sub\" font-size=\"11\">{3,4}</tspan>"))):
        segs, marks = [], []
        dendrite_segments((cx - 150, 150), (cx + 150, 150), depth, orders, segs, marks)
        body.append(path(" ".join(f"M{a[0]:.0f} {a[1]:.0f}L{b[0]:.0f} {b[1]:.0f}" for a, b in segs),
                         INK, 1.0))
        for (x, y), order, level in marks:
            if level > 1:
                continue
            if order == 3:
                body.append(circle(x, y, 4.2, fill=BLUE, stroke=BLUE, width=1))
            else:
                body.append(f'<rect x="{x - 4:.1f}" y="{y - 4:.1f}" width="8" height="8" fill="{ORANGE}" '
                            f'stroke="{ORANGE}" stroke-width="1"/>')
        body.append(text(cx, 268, label, 15, color=SOFT))
    body.append(circle(232, 28, 4.2, fill=BLUE, stroke=BLUE, width=1))
    body.append(text(242, 33, "order 3", 13, anchor="start", color=SOFT))
    body.append(f'<rect x="{348 - 4}" y="{28 - 4}" width="8" height="8" fill="{ORANGE}" stroke="{ORANGE}"/>')
    body.append(text(358, 33, "order 4", 13, anchor="start", color=SOFT))
    return svg(680, 280, "\n".join(body),
               "The first stages of two generalised Wazewski dendrites: one with ramification points of "
               "order 3, one with ramification points of orders 3 and 4")


# --- Proposition 23.12 and Theorem 23.19: the atoms of a measure space -----------------------

def atoms():
    body = []
    groups = [("r₁", 3, 15), ("r₂", 2, 11), ("r₃", 4, 7.5)]
    rows = ((62, "(a) measure-preserving automorphisms permute each <tspan font-style=\"italic\">A</tspan>"
                 "<tspan baseline-shift=\"sub\" font-size=\"11\" font-style=\"italic\">r</tspan>"),
            (196, "(b) nonsingular automorphisms may permute all the atoms"))
    for row, (y, label) in enumerate(rows):
        # The atomless part.
        body.append(f'<rect x="40" y="{y - 22}" width="190" height="44" rx="6" fill="{BLUE_FILL}" '
                    f'stroke="{BLUE}" stroke-width="1.4"/>')
        body.append(text(135, y + 6, "<tspan font-style=\"italic\">Y</tspan>"
                         "<tspan baseline-shift=\"sub\" font-size=\"12\">c</tspan>", 18, color=BLUE))
        body.append(text(135, y + 42, "atomless part", 13, color=BLUE))
        x = 268
        centres = []
        for name, count, rad in groups:
            start = x
            mine = []
            for i in range(count):
                cx = x + rad
                mine.append((cx, rad))
                body.append(circle(cx, y, rad, fill=ORANGE_FILL, stroke=ORANGE, width=1.4))
                x += 2 * rad + 12
            centres += mine
            end = x - 12
            if row == 0:
                (p, pr), (q, qr) = mine[0], mine[-1]
                body.append(path(f"M{p:.1f},{y - pr - 4:.1f} Q{(p + q) / 2:.1f},{y - 40:.1f} "
                                 f"{q:.1f},{y - qr - 4:.1f}", ORANGE, 1.3, arrow=True, arrow_start=True))
            body.append(path(f"M{start},{y + 26} L{start},{y + 31} L{end},{y + 31} L{end},{y + 26}", SOFT, 1.1))
            body.append(text((start + end) / 2, y + 48, f"<tspan font-style=\"italic\">A</tspan>"
                             f"<tspan baseline-shift=\"sub\" font-size=\"11\" font-style=\"italic\">{name}</tspan>",
                             15, color=SOFT))
            x += 20
        body.append(text(x + 2, y + 6, "…", 18, anchor="start", color=SOFT))
        if row == 1:
            for (p, pr), (q, qr), h in ((centres[2], centres[3], 18), (centres[0], centres[7], 50)):
                body.append(path(f"M{p:.1f},{y - pr - 4:.1f} Q{(p + q) / 2:.1f},{y - h - 14:.1f} "
                                 f"{q:.1f},{y - qr - 4:.1f}", ORANGE, 1.3, arrow=True, arrow_start=True,
                                 dash="5 3"))
        body.append(text(340, y + 74, label, 14, color=SOFT))
    return svg(680, 290, "\n".join(body),
               "A measure space split into its atomless part and its atoms, grouped by mass; measure-preserving "
               "automorphisms permute atoms of equal mass, nonsingular ones may permute all atoms")


# --- Theorem 27.1: the inverse limit of Oliver disks ---------------------------------------

def inverse_limit_disks():
    body = []
    y = 110
    xs = [110, 250, 390]
    names = ["j", "j+1", "j+2"]
    sub = lambda letter, nm, size=16: (f"<tspan font-style=\"italic\">{letter}</tspan><tspan baseline-shift=\"sub\" "
                                       f"font-size=\"{size - 5}\" font-style=\"italic\">{nm}</tspan>")
    for x, nm in zip(xs, names):
        body.append(circle(x, y, 40, fill=BLUE_FILL, stroke=BLUE, width=1.6))
        body.append(text(x, y + 6, sub("D", nm, 18), 18))
        body.append(path(f"M{x - 26},{y - 52} A30,14 0 1 1 {x + 26},{y - 52}", INK, 1.2, arrow=True))
        body.append(text(x, y - 74, sub("K", nm), 16))
    for xa, xb in ((110, 250), (250, 390)):
        body.append(text((xa + xb) / 2, y - 74, "⊂", 16, color=SOFT))
    body.append(text(462, y - 74, "⊂ …", 16, color=SOFT))
    for (xa, xb), nm in zip(((110, 250), (250, 390)), names):
        body.append(line(xb - 46, y, xa + 46, y, INK, 1.4, arrow=True))
        body.append(text((xa + xb) / 2, y - 8, sub("p", nm, 15), 15))
    body.append(line(474, y, 436, y, INK, 1.4, arrow=True))
    body.append(text(490, y + 6, "…", 18, anchor="start", color=SOFT))
    # The inverse limit, and its projection to D_j.
    xX = 600
    body.append(ellipse(xX, y, 52, 40, fill=ORANGE_FILL, stroke=ORANGE, width=1.6))
    body.append(math(xX, y + 6, "X", 19))
    body.append(path(f"M{xX - 26},{y - 52} A30,14 0 1 1 {xX + 26},{y - 52}", INK, 1.2, arrow=True))
    body.append(text(xX, y - 74, "<tspan font-style=\"italic\">G</tspan> = ⋃ " + sub("K", "n"), 16))
    body.append(path(f"M{xX - 36},{y + 29} C{xX - 120},{y + 78} 240,{y + 78} 146,{y + 24}", ORANGE, 1.5,
                     arrow=True))
    body.append(text(370, y + 92, "the projection is " + sub("K", "j", 14) + "-equivariant", 14, color=ORANGE))
    body.append(text(96, y + 62, "no " + sub("K", "j", 13) + "-fixed point", 13, color=SOFT))
    body.append(text(xX + 6, y + 62, "so no " + sub("K", "j", 13) + "-fixed point,", 13, color=SOFT))
    body.append(text(xX + 6, y + 79, "and no <tspan font-style=\"italic\">G</tspan>-fixed point", 13, color=SOFT))
    return svg(680, 220, "\n".join(body),
               "The disks D_j, D_(j+1), D_(j+2) with the groups K_n acting on them and the maps p_n between "
               "them, their inverse limit X with the action of G, and the projection from X to D_j")

FIGURES = {
    "uspenskij-chains": uspenskij_chains,
    "cantor-chain": cantor_chain,
    "tree-rays": tree_rays,
    "bratteli": bratteli,
    "completion-pattern": completion_pattern,
    "kernel-pattern": kernel_pattern,
    "greatest-ambit": greatest_ambit,
    "pestov-circle": pestov_circle,
    "ramsey-property": ramsey_property,
    "minimal-ideals": minimal_ideals,
    "irrational-rotation": irrational_rotation,
    "sphere-concentration": sphere_concentration,
    "transported-order": transported_order,
    "convex-orders": convex_orders,
    "lelek-fan": lelek_fan,
    "wazewski-dendrites": wazewski,
    "atoms": atoms,
    "inverse-limit-disks": inverse_limit_disks,
}

if __name__ == "__main__":
    for name, draw in FIGURES.items():
        (HERE / f"{name}.svg").write_text(draw())
    print(f"Wrote {len(FIGURES)} figures in {HERE}")
