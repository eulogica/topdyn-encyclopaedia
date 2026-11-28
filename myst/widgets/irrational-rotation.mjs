// Example 3.3, interactively: choose an irrational number α and a number of steps N, and
// see the first N points x, Rx, R²x, ... of an orbit of the rotation R of the circle by
// 2πα, and the longest arc of the circle that contains none of them.
//
// Shown after Figure 3.1 on both sites: by an anywidget directive that
// myst/tools/site_map.py adds on the MyST site, and by latex/tools/postprocess.py on
// the LaTeX site. It needs no data from the page.

const NS = "http://www.w3.org/2000/svg";
const W = 680, H = 300, CX = 230, CY = 150, R = 118;
const ALPHAS = [
  ["(√5 − 1)/2", (Math.sqrt(5) - 1) / 2],
  ["√2 − 1", Math.SQRT2 - 1],
  ["e − 2", Math.E - 2],
  ["π − 3", Math.PI - 3],
];
const NMAX = 1000;

function el(tag, attrs, parent) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  if (parent) parent.appendChild(e);
  return e;
}

// The positions k·α mod 1 of the first n points, in turns, and the longest gap between
// consecutive positions around the circle.
function orbit(alpha, n) {
  const pos = Array.from({ length: n }, (_, k) => (k * alpha) % 1);
  const sorted = [...pos].sort((a, b) => a - b);
  let gap = 1 - sorted[sorted.length - 1] + sorted[0];
  for (let i = 1; i < sorted.length; i++) gap = Math.max(gap, sorted[i] - sorted[i - 1]);
  return { pos, gap };
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
                   --one: #2f63b8; --x: #c4661f; }
      .box.dark  { --ink: #dde3e8; --soft: #a8b2bb; --rule: #3a4550; --bg: #1c2127;
                   --one: #7fa8ea; --x: #f0a060; }
      .head { color: var(--soft); font-size: 14px; margin-bottom: .2em; }
      svg { width: 100%; height: auto; display: block; }
      .controls { display: grid; grid-template-columns: auto 1fr auto; gap: .3em .7em;
                  align-items: center; margin-top: .3em; }
      .controls span.v { min-width: 2.5em; text-align: right; font-variant-numeric: tabular-nums; }
      input[type=range] { width: 100%; accent-color: var(--one); }
      select, button { font: inherit; font-size: 14px; color: var(--ink); background: var(--bg);
                       border: 1px solid var(--rule); border-radius: 4px; padding: .1em .4em; }
      button { cursor: pointer; }
      .out { color: var(--soft); font-size: 14px; min-height: 3em; margin-top: .4em; }
    </style>
    <div class="box light">
      <div class="head">Interactive version: the first <i>N</i> points of the orbit of <i>x</i>
        under the rotation <i>R</i> by 2π<i>α</i>, for an irrational <i>α</i>.</div>
      <svg viewBox="0 0 ${W} ${H}" role="img"
           aria-label="The first N points of an orbit of an irrational rotation of the circle"></svg>
      <div class="controls">
        <label for="n"><i>N</i></label><input id="n" type="range" min="1" max="${NMAX}" value="12"><span class="v" id="nv"></span>
        <label for="a"><i>α</i></label>
        <span><select id="a">${ALPHAS.map(([s], i) => `<option value="${i}">${s}</option>`).join("")}</select></span>
        <button id="play" type="button">Play</button>
      </div>
      <div class="out" aria-live="polite"></div>
    </div>`;
  const box = root.querySelector(".box");
  const svg = root.querySelector("svg");
  const out = root.querySelector(".out");
  const nIn = root.querySelector("#n"), aIn = root.querySelector("#a"), play = root.querySelector("#play");
  const colour = (name) => getComputedStyle(box).getPropertyValue(name).trim();
  let timer = null;

  function update() {
    const n = Number(nIn.value), [label, alpha] = ALPHAS[Number(aIn.value)];
    root.querySelector("#nv").textContent = n;
    const { pos, gap } = orbit(alpha, n);
    const ink = colour("--ink"), one = colour("--one"), xc = colour("--x"), soft = colour("--soft");
    svg.replaceChildren();
    el("circle", { cx: CX, cy: CY, r: R, fill: "none", stroke: ink, "stroke-width": 1.6 }, svg);
    const at = (t, rr = R) => [CX + rr * Math.sin(2 * Math.PI * t), CY - rr * Math.cos(2 * Math.PI * t)];
    const rad = n <= 30 ? 5 : n <= 200 ? 3.2 : 2.2;
    pos.forEach((t, k) => {
      const [x, y] = at(t);
      el("circle", { cx: x, cy: y, r: k === 0 ? rad + 1.5 : rad, fill: k === 0 ? xc : one, stroke: "none" }, svg);
      if (n <= 30 && k < 4) {
        const [lx, ly] = at(t, R + 20);
        el("text", { x: lx, y: ly + 5, "text-anchor": "middle", "font-size": 15, "font-style": "italic", fill: ink }, svg)
          .textContent = ["x", "Rx", "R²x", "R³x"][k];
      }
    });
    // The rotation, from x to Rx.
    const [p0x, p0y] = at(0, R - 18), [p1x, p1y] = at(alpha, R - 18);
    el("path", { d: `M${p0x},${p0y} A${R - 18},${R - 18} 0 ${alpha > 0.5 ? 1 : 0} 1 ${p1x},${p1y}`,
                 fill: "none", stroke: xc, "stroke-width": 1.3, "stroke-dasharray": "4 3" }, svg);
    el("text", { x: CX, y: CY + 6, "text-anchor": "middle", "font-size": 17, "font-style": "italic", fill: xc }, svg)
      .textContent = "R";
    // The share of the circle in the longest empty arc, as a bar.
    const bx = 420, by = 132, bw = 220;
    el("text", { x: bx, y: by - 14, "font-size": 14, fill: soft }, svg).textContent = "longest arc with no point of the orbit";
    el("rect", { x: bx, y: by, width: bw, height: 12, fill: "none", stroke: soft, "stroke-width": 1 }, svg);
    el("rect", { x: bx, y: by, width: Math.max(1, bw * gap), height: 12, fill: one }, svg);
    el("text", { x: bx, y: by + 32, "font-size": 14, fill: ink }, svg)
      .textContent = `${(gap * 100).toFixed(gap < 0.01 ? 2 : 1)}% of the circle`;
    out.innerHTML = `α = ${label} ≈ ${alpha.toFixed(6)}. ${n === 1 ? "Shown: the first point, <i>x</i> itself."
      : `Shown: the first ${n} points <i>x</i>, <i>Rx</i>, …, <i>R</i><sup>${n - 1}</sup><i>x</i>.`}`;
  }
  function stop() { if (timer) { clearInterval(timer); timer = null; play.textContent = "Play"; } }
  play.addEventListener("click", () => {
    if (timer) return stop();
    if (Number(nIn.value) >= NMAX) nIn.value = 1;
    play.textContent = "Pause";
    timer = setInterval(() => {
      const n = Number(nIn.value);
      if (n >= NMAX) return stop();
      nIn.value = Math.min(NMAX, n + Math.max(1, Math.round(n / 40)));
      update();
    }, 60);
  });
  nIn.addEventListener("input", () => { stop(); update(); });
  aIn.addEventListener("change", update);
  function theme() {
    const dark = document.documentElement.classList.contains("dark");
    box.classList.toggle("dark", dark); box.classList.toggle("light", !dark);
    update();
  }
  new MutationObserver(theme).observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
  theme();
}

export default { render };
