// Definition 10.1, interactively: a linear order < on N, restricted to {1, ..., 6}, a
// permutation g of N that permutes {1, ..., 6} and fixes every other number, and the
// transported order g·<, in which a comes before b exactly when g⁻¹(a) < g⁻¹(b).
// Clicking two numbers in the top row swaps them in <; clicking two numbers in the
// bottom row swaps them in g·<, which replaces g by its composite with a transposition.
//
// Shown after Figure 10.1 on both sites: by an anywidget directive that
// myst/tools/site_map.py adds on the MyST site, and by latex/tools/postprocess.py on
// the LaTeX site. It needs no data from the page.

const NS = "http://www.w3.org/2000/svg";
const W = 680, H = 270, X0 = 190, DX = 76, Y1 = 60, Y2 = 180, RAD = 18;
const START_ORDER = [4, 1, 6, 3, 5, 2];
const START_G = { 1: 2, 2: 3, 3: 1, 4: 4, 5: 6, 6: 5 };

function el(tag, attrs, parent) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  if (parent) parent.appendChild(e);
  return e;
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
                   --one: #2f63b8; --fill: #dbe6f7; --g: #c4661f; --dot: #ffffff; }
      .box.dark  { --ink: #dde3e8; --soft: #a8b2bb; --rule: #3a4550; --bg: #1c2127;
                   --one: #7fa8ea; --fill: #253246; --g: #f0a060; --dot: #1c2127; }
      .head { color: var(--soft); font-size: 14px; margin-bottom: .2em; }
      svg { width: 100%; height: auto; display: block; user-select: none; }
      svg g.node { cursor: pointer; }
      svg g.node:focus { outline: none; }
      svg g.node:focus circle { stroke-width: 3; }
      .row { display: flex; gap: .6em; align-items: center; margin-top: .3em; flex-wrap: wrap; }
      button { font: inherit; font-size: 14px; color: var(--ink); background: var(--bg);
               border: 1px solid var(--rule); border-radius: 4px; padding: .1em .5em; cursor: pointer; }
      .out { color: var(--soft); font-size: 14px; min-height: 3em; margin-top: .4em; }
    </style>
    <div class="box light">
      <div class="head">Interactive version: click two numbers in the top row to swap them in
        &lt;, or two numbers in the bottom row to swap them in <i>g</i>·&lt; (this changes
        <i>g</i>).</div>
      <svg viewBox="0 0 ${W} ${H}" role="group" aria-label="An order on 1 to 6, a permutation g and the transported order"></svg>
      <div class="row"><button id="reset" type="button">Reset</button></div>
      <div class="out" aria-live="polite"></div>
    </div>`;
  const box = root.querySelector(".box");
  const svg = root.querySelector("svg");
  const out = root.querySelector(".out");
  const colour = (name) => getComputedStyle(box).getPropertyValue(name).trim();
  let order = [...START_ORDER], g = { ...START_G }, picked = null;   // picked: [row, index]

  function click(row, i) {
    if (!picked || picked[0] !== row) { picked = [row, i]; update(); return; }
    const j = picked[1];
    picked = null;
    if (i !== j) {
      if (row === 0) {
        [order[i], order[j]] = [order[j], order[i]];
      } else {
        // Swap the values g(order[i]) and g(order[j]): g becomes (them) ∘ g.
        const a = order[i], b = order[j];
        [g[a], g[b]] = [g[b], g[a]];
      }
    }
    update();
  }

  function node(x, y, label, row, i, styles) {
    const grp = el("g", { class: "node", tabindex: 0, role: "button",
                          "aria-label": `${row ? "g·<" : "<"}: ${label}` }, svg);
    el("circle", { cx: x, cy: y, r: RAD, ...styles }, grp);
    el("text", { x, y: y + 6, "text-anchor": "middle", "font-size": 17, fill: styles.textFill }, grp)
      .textContent = label;
    grp.addEventListener("click", () => click(row, i));
    grp.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); click(row, i); } });
  }

  function update() {
    const ink = colour("--ink"), soft = colour("--soft"), one = colour("--one"), fill = colour("--fill"),
          gc = colour("--g"), dot = colour("--dot");
    svg.replaceChildren();
    const defs = el("defs", {}, svg);
    const m = el("marker", { id: "to-arrow", viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 7,
                             markerHeight: 7, orient: "auto" }, defs);
    el("path", { d: "M0,0 L10,5 L0,10 z", fill: gc }, m);
    el("text", { x: 70, y: Y1 + 6, "text-anchor": "middle", "font-size": 20, "font-style": "italic", fill: ink }, svg)
      .textContent = "<";
    el("text", { x: 70, y: Y2 + 6, "text-anchor": "middle", "font-size": 20, "font-style": "italic", fill: ink }, svg)
      .textContent = "g·<";
    el("text", { x: X0 + DX * 2.5, y: Y1 - 32, "text-anchor": "middle", "font-size": 13, fill: soft }, svg)
      .textContent = "least  →  greatest";
    order.forEach((a, i) => {
      const x = X0 + DX * i;
      const sel0 = picked && picked[0] === 0 && picked[1] === i;
      const sel1 = picked && picked[0] === 1 && picked[1] === i;
      el("line", { x1: x, y1: Y1 + RAD + 3, x2: x, y2: Y2 - RAD - 5, stroke: gc, "stroke-width": 1.4,
                   "marker-end": "url(#to-arrow)" }, svg);
      if (i) {
        for (const y of [Y1, Y2])
          el("text", { x: x - DX / 2, y: y + 6, "text-anchor": "middle", "font-size": 15, fill: soft }, svg).textContent = "<";
      }
      node(x, Y1, String(a), 0, i, { fill: sel0 ? fill : dot, stroke: sel0 ? gc : ink, "stroke-width": sel0 ? 3 : 1.5, textFill: ink });
      node(x, Y2, String(g[a]), 1, i, { fill, stroke: sel1 ? gc : one, "stroke-width": sel1 ? 3 : 1.5, textFill: one });
    });
    el("text", { x: 120, y: (Y1 + Y2) / 2 + 5, "text-anchor": "middle", "font-size": 14, "font-style": "italic", fill: gc }, svg)
      .textContent = "a ↦ g(a)";
    // g in two-line notation.
    const gx = 190, gy = 240;
    el("text", { x: gx, y: gy + 5, "text-anchor": "end", "font-size": 17, "font-style": "italic", fill: ink }, svg).textContent = "g";
    el("text", { x: gx + 8, y: gy + 5, "font-size": 17, fill: ink }, svg).textContent = "=";
    el("path", { d: `M${gx + 32},${gy - 18} Q${gx + 24},${gy} ${gx + 32},${gy + 18}`, fill: "none", stroke: ink, "stroke-width": 1.2 }, svg);
    for (let k = 1; k <= 6; k++) {
      el("text", { x: gx + 30 + 18 * k, y: gy - 4, "text-anchor": "middle", "font-size": 14, fill: ink }, svg).textContent = k;
      el("text", { x: gx + 30 + 18 * k, y: gy + 14, "text-anchor": "middle", "font-size": 14, fill: one }, svg).textContent = g[k];
    }
    el("path", { d: `M${gx + 150},${gy - 18} Q${gx + 158},${gy} ${gx + 150},${gy + 18}`, fill: "none", stroke: ink, "stroke-width": 1.2 }, svg);
    el("text", { x: gx + 168, y: gy + 5, "font-size": 14, fill: soft }, svg).textContent = "on 1, …, 6; g fixes every other number";

    const inv = {};
    for (let k = 1; k <= 6; k++) inv[g[k]] = k;
    const a = g[order[0]], b = g[order[1]];
    out.innerHTML = picked
      ? `Now click another number in the ${picked[0] ? "bottom" : "top"} row to swap it with
         ${picked[0] ? g[order[picked[1]]] : order[picked[1]]}.`
      : `For example, ${a} comes before ${b} in <i>g</i>·&lt; because <i>g</i><sup>−1</sup>(${a}) = ${inv[a]}
         comes before <i>g</i><sup>−1</sup>(${b}) = ${inv[b]} in &lt;: by definition,
         <i>a</i> (<i>g</i>·&lt;) <i>b</i> if and only if <i>g</i><sup>−1</sup>(<i>a</i>) &lt; <i>g</i><sup>−1</sup>(<i>b</i>).`;
  }
  root.querySelector("#reset").addEventListener("click", () => {
    order = [...START_ORDER]; g = { ...START_G }; picked = null; update();
  });
  function theme() {
    const dark = document.documentElement.classList.contains("dark");
    box.classList.toggle("dark", dark); box.classList.toggle("light", !dark);
    update();
  }
  new MutationObserver(theme).observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
  theme();
}

export default { render };
