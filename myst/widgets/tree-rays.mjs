// Lemma 24.10, interactively: choose n and a vertex h of the tree of F_2, and see the
// first n vertices of the rays from 1 and from h toward a boundary point ξ, the
// vertices they share, and c_{n,h}(ξ), which the proof of the lemma computes as 1/n
// times the number of shared vertices.
//
// Shown after Figure 24.1 on both sites: by an anywidget directive that
// myst/tools/site_map.py adds on the MyST site, and by latex/tools/postprocess.py on
// the LaTeX site. It needs no data from the page.

const NS = "http://www.w3.org/2000/svg";
const W = 680, H = 270, X0 = 36, DX = 34, Y0 = 220, N = 18;
const ray = Array.from({ length: N }, (_, j) => [X0 + DX * j, Y0]);

function el(tag, attrs, parent) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  if (parent) parent.appendChild(e);
  return e;
}

// The vertex h: its path to the ray from 1 meets it at the k-th vertex v_k, after d
// edges, so that |h| = k + d. The ray from h toward ξ runs down that path and then
// along v_k, v_{k+1}, ...; its first n vertices, and those of the ray from 1.
function rays(n, k, d) {
  const path = Array.from({ length: d }, (_, j) => `u${d - j}`);       // h = u_d, ..., u_1
  const fromH = path.concat(Array.from({ length: Math.max(0, n - d) }, (_, j) => `v${k + j}`))
                    .slice(0, n);
  const from1 = Array.from({ length: n }, (_, j) => `v${j}`);
  const shared = fromH.filter(x => from1.includes(x));
  return { from1, fromH, shared };
}

function render({ el: host }) {
  const root = host.attachShadow ? host.attachShadow({ mode: "open" }) : host;
  root.innerHTML = `
    <style>
      :host { display: block; }
      .box { font-family: inherit; font-size: 15px; line-height: 1.45; color: var(--ink);
             border: 1px solid var(--rule); border-radius: 6px; padding: .6em .9em .8em;
             background: var(--bg); max-width: 680px; margin: 0 auto; box-sizing: border-box; }
      .box.light { --ink: #25303b; --soft: #5d6873; --rule: #d9dde0; --bg: #fafbfc;
                   --one: #2f63b8; --h: #c4661f; --off: #b7bfc6; --dot: #ffffff; }
      .box.dark  { --ink: #dde3e8; --soft: #a8b2bb; --rule: #3a4550; --bg: #1c2127;
                   --one: #7fa8ea; --h: #f0a060; --off: #56616c; --dot: #1c2127; }
      .head { color: var(--soft); font-size: 14px; margin-bottom: .2em; }
      svg { width: 100%; height: auto; display: block; }
      .controls { display: grid; grid-template-columns: auto 1fr auto; gap: .2em .7em;
                  align-items: center; margin-top: .3em; }
      .controls span.v { min-width: 1.5em; text-align: right; font-variant-numeric: tabular-nums; }
      input[type=range] { width: 100%; accent-color: var(--one); }
      .out { color: var(--soft); font-size: 14px; min-height: 4.2em; margin-top: .4em; }
      .ok { color: var(--one); font-weight: 600; }
    </style>
    <div class="box light">
      <div class="head">Interactive version: choose <i>n</i> and the vertex <i>h</i>, whose path to
        the ray from 1 meets it at its <i>k</i>-th vertex after <i>d</i> edges, so that
        |<i>h</i>| = <i>k</i> + <i>d</i>.</div>
      <svg viewBox="0 0 ${W} ${H}" role="img"
           aria-label="The rays from 1 and from h toward a boundary point of the tree, with their first n vertices marked"></svg>
      <div class="controls">
        <label for="n"><i>n</i></label><input id="n" type="range" min="1" max="10" value="6"><span class="v" id="nv"></span>
        <label for="k"><i>k</i></label><input id="k" type="range" min="0" max="7" value="1"><span class="v" id="kv"></span>
        <label for="d"><i>d</i></label><input id="d" type="range" min="0" max="5" value="2"><span class="v" id="dv"></span>
      </div>
      <div class="out" aria-live="polite"></div>
    </div>`;
  const box = root.querySelector(".box");
  const svg = root.querySelector("svg");
  const out = root.querySelector(".out");
  const inputs = ["n", "k", "d"].map(id => root.getElementById ? root.getElementById(id)
                                                              : root.querySelector("#" + id));
  const colour = (name) => getComputedStyle(box).getPropertyValue(name).trim();

  function update() {
    const [n, k, d] = inputs.map(i => Number(i.value));
    for (const [id, v] of [["nv", n], ["kv", k], ["dv", d]]) root.querySelector("#" + id).textContent = v;
    const { from1, fromH, shared } = rays(n, k, d);
    const one = colour("--one"), hc = colour("--h"), off = colour("--off"), ink = colour("--ink"),
          dot = colour("--dot");
    svg.replaceChildren();
    const defs = el("defs", {}, svg);
    const m = el("marker", { id: "tr-arrow", viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 7,
                             markerHeight: 7, orient: "auto" }, defs);
    el("path", { d: "M0,0 L10,5 L0,10 z", fill: ink }, m);
    // The path from h to v_k, and the ray from 1 toward ξ.
    const pos = {};
    ray.forEach(([x, y], j) => { pos[`v${j}`] = [x, y]; });
    for (let j = 1; j <= d; j++) pos[`u${j}`] = [ray[k][0] + 20 * j, Y0 - 34 * j];
    for (const [x, y] of ray) el("line", { x1: x, y1: y, x2: x - 10, y2: y + 18, stroke: off, "stroke-width": 1.2 }, svg);
    el("line", { x1: ray[0][0] - 24, y1: Y0, x2: ray[N - 1][0] + 18, y2: Y0, stroke: ink, "stroke-width": 2,
                 "marker-end": "url(#tr-arrow)" }, svg);
    el("text", { x: ray[N - 1][0] + 26, y: Y0 + 6, "font-size": 19, "font-style": "italic", fill: ink }, svg)
      .textContent = "ξ";
    let prev = pos[`v${k}`];
    for (let j = 1; j <= d; j++) {
      const p = pos[`u${j}`];
      el("line", { x1: prev[0], y1: prev[1], x2: p[0], y2: p[1], stroke: ink, "stroke-width": 2 }, svg);
      prev = p;
    }
    // Vertices: the first n of the ray from 1 filled, those of the ray from h ringed.
    for (const [name, [x, y]] of Object.entries(pos)) {
      const first = from1.includes(name);
      el("circle", { cx: x, cy: y, r: 6.5, fill: first ? one : dot, stroke: first ? one : ink, "stroke-width": 1.4 }, svg);
      if (fromH.includes(name))
        el("circle", { cx: x, cy: y, r: 11, fill: "none", stroke: hc, "stroke-width": 2.2 }, svg);
    }
    el("text", { x: ray[0][0], y: Y0 + 36, "text-anchor": "middle", "font-size": 16, fill: ink }, svg).textContent = "1";
    const h = d ? pos[`u${d}`] : pos[`v${k}`];
    el("text", { x: h[0] + (d ? 16 : 0), y: h[1] + (d ? 5 : -18), "text-anchor": d ? "start" : "middle",
                 "font-size": 17, "font-style": "italic", fill: hc }, svg).textContent = "h";
    // Legend.
    el("circle", { cx: 360, cy: 26, r: 6.5, fill: one, stroke: one }, svg);
    el("text", { x: 374, y: 31, "font-size": 14, fill: ink }, svg).textContent = `first n = ${n} vertices of the ray from 1`;
    el("circle", { cx: 360, cy: 52, r: 10, fill: "none", stroke: hc, "stroke-width": 2.2 }, svg);
    el("text", { x: 374, y: 57, "font-size": 14, fill: ink }, svg).textContent = `first n = ${n} vertices of the ray from h`;

    const len = k + d, s = shared.length;
    const frac = (a, b) => (a === 0 ? "0" : a === b ? "1" : `${a}/${b}`);
    const bound = len >= n ? "1" : frac(len, n);
    const first = n === 1 ? "The first vertices of the two rays" : `The first ${n} vertices of the two rays`;
    const c = `<i>c</i><sub><i>n</i>,<i>h</i></sub>`;
    out.innerHTML =
      `|<i>h</i>| = ${len}. ${first} ${s === 0 ? "are all different" : n === 1 ? "coincide" : `share ${s}`}, ` +
      `so ${c}(<i>ξ</i>) = ${frac(s, n)}` + (s && s !== n ? ` ≈ ${(s / n).toFixed(3).replace(/0+$/, "")}` : "") +
      `. Lemma 24.10 bounds 1 − ${c} by min{|<i>h</i>|/<i>n</i>, 1} = ${bound}, and here ` +
      `1 − ${c}(<i>ξ</i>) = ${frac(n - s, n)}` +
      (1 - s / n <= Math.min(len / n, 1) + 1e-12 ? ` <span class="ok">≤ ${bound}</span>.` : ".");
  }
  function theme() {
    const dark = document.documentElement.classList.contains("dark");
    box.classList.toggle("dark", dark); box.classList.toggle("light", !dark);
    update();
  }
  for (const i of inputs) i.addEventListener("input", update);
  new MutationObserver(theme).observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
  theme();
}

export default { render };
