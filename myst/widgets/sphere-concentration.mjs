// Remark 8.3, interactively: choose n and ε, and see the distribution of the latitude of
// a random point of the sphere S^n, the measure of the ε-neighbourhood of a hemisphere,
// and the measure of the band of points within ε of the equator.
//
// The latitude is the geodesic distance from the equator, with a sign; for the
// rotation-invariant probability measure on S^n it has density proportional to
// cos(θ)^(n−1) on [−π/2, π/2]. The measures are computed from it numerically.
//
// Shown after Figure 8.1 on both sites: by an anywidget directive that
// myst/tools/site_map.py adds on the MyST site, and by latex/tools/postprocess.py on
// the LaTeX site. It needs no data from the page.

const NS = "http://www.w3.org/2000/svg";
const W = 680, H = 250, X0 = 50, X1 = 630, YB = 200, HT = 160, STEPS = 4000;
const NMAX = 2000;
const X = (t) => X0 + (t + Math.PI / 2) / Math.PI * (X1 - X0);

function el(tag, attrs, parent) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  if (parent) parent.appendChild(e);
  return e;
}

// The density of the latitude on a grid of STEPS intervals, normalised to total mass 1,
// and its distribution function F(t), the measure of the points of latitude at most t.
function latitude(n) {
  const h = Math.PI / STEPS;
  const ts = Array.from({ length: STEPS + 1 }, (_, i) => -Math.PI / 2 + i * h);
  const dens = ts.map((t) => {
    const c = Math.cos(t);
    return n === 1 ? 1 : c <= 0 ? 0 : Math.exp((n - 1) * Math.log(c));
  });
  const cum = [0];
  for (let i = 1; i <= STEPS; i++) cum.push(cum[i - 1] + (dens[i - 1] + dens[i]) * h / 2);
  const total = cum[STEPS];
  return { ts, dens: dens.map((d) => d / total), F: (t) => {
    const x = (t + Math.PI / 2) / h, i = Math.min(STEPS - 1, Math.max(0, Math.floor(x)));
    return (cum[i] + (cum[i + 1] - cum[i]) * (x - i)) / total;
  } };
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
                   --one: #2f63b8; --fill: #dbe6f7; --eps: #c4661f; --epsfill: #f8e3d2; }
      .box.dark  { --ink: #dde3e8; --soft: #a8b2bb; --rule: #3a4550; --bg: #1c2127;
                   --one: #7fa8ea; --fill: #253246; --eps: #f0a060; --epsfill: #4a3524; }
      .head { color: var(--soft); font-size: 14px; margin-bottom: .2em; }
      svg { width: 100%; height: auto; display: block; }
      .controls { display: grid; grid-template-columns: auto 1fr auto; gap: .2em .7em;
                  align-items: center; margin-top: .3em; }
      .controls span.v { min-width: 3.2em; text-align: right; font-variant-numeric: tabular-nums; }
      input[type=range] { width: 100%; accent-color: var(--one); }
      .out { color: var(--soft); font-size: 14px; min-height: 3em; margin-top: .4em; }
      .out b { color: var(--ink); font-weight: 600; font-variant-numeric: tabular-nums; }
    </style>
    <div class="box light">
      <div class="head">Interactive version: the distribution of the latitude of a random point
        of 𝕊<sup><i>n</i></sup>, computed numerically, with the points within <i>ε</i> of the
        equator shaded.</div>
      <svg viewBox="0 0 ${W} ${H}" role="img"
           aria-label="The density of the latitude of a random point of the n-sphere, with the band within epsilon of the equator shaded"></svg>
      <div class="controls">
        <label for="n"><i>n</i></label><input id="n" type="range" min="0" max="1000" value="500"><span class="v" id="nv"></span>
        <label for="e"><i>ε</i></label><input id="e" type="range" min="2" max="80" value="20"><span class="v" id="ev"></span>
      </div>
      <div class="out" aria-live="polite"></div>
    </div>`;
  const box = root.querySelector(".box");
  const svg = root.querySelector("svg");
  const out = root.querySelector(".out");
  const nIn = root.querySelector("#n"), eIn = root.querySelector("#e");
  const colour = (name) => getComputedStyle(box).getPropertyValue(name).trim();
  // The n slider is logarithmic, from 1 to NMAX.
  const nOf = (v) => Math.max(1, Math.round(Math.exp(Math.log(NMAX) * v / 1000)));
  const cache = new Map();
  const lat = (n) => { if (!cache.has(n)) cache.set(n, latitude(n)); return cache.get(n); };

  function update() {
    const n = nOf(Number(nIn.value)), eps = Number(eIn.value) / 100;
    root.querySelector("#nv").textContent = n;
    root.querySelector("#ev").textContent = eps.toFixed(2);
    const { ts, dens, F } = lat(n);
    const ink = colour("--ink"), soft = colour("--soft"), one = colour("--one"), fill = colour("--fill"),
          ec = colour("--eps"), ef = colour("--epsfill");
    svg.replaceChildren();
    const peak = Math.max(...dens);
    const Y = (d) => YB - HT * d / peak;
    const stride = 10;
    const pts = ts.filter((_, i) => i % stride === 0).map((t, j) => [X(t), Y(dens[j * stride])]);
    // The band within eps of the equator, shaded under the curve.
    const band = ts.map((t, i) => [t, dens[i]]).filter(([t], i) => Math.abs(t) <= eps && i % 2 === 0);
    if (band.length > 1) {
      el("path", { d: `M${X(band[0][0])},${YB} ` + band.map(([t, d]) => `L${X(t).toFixed(1)},${Y(d).toFixed(1)}`).join(" ")
                    + ` L${X(band[band.length - 1][0])},${YB} z`, fill: ef, stroke: "none" }, svg);
    }
    el("polyline", { points: pts.map(([x, y]) => `${x.toFixed(1)},${y.toFixed(1)}`).join(" "), fill: "none",
                     stroke: one, "stroke-width": 2 }, svg);
    el("line", { x1: X0, y1: YB, x2: X1, y2: YB, stroke: soft, "stroke-width": 1.2 }, svg);
    for (const [t, lab] of [[-Math.PI / 2, "−π/2"], [0, "0"], [Math.PI / 2, "π/2"]]) {
      el("line", { x1: X(t), y1: YB, x2: X(t), y2: YB + 5, stroke: soft, "stroke-width": 1.2 }, svg);
      el("text", { x: X(t), y: YB + 20, "text-anchor": "middle", "font-size": 13, fill: soft }, svg).textContent = lab;
    }
    for (const t of [-eps, eps])
      el("line", { x1: X(t), y1: YB, x2: X(t), y2: YB - HT - 8, stroke: ec, "stroke-width": 1.1, "stroke-dasharray": "4 3" }, svg);
    el("text", { x: (X0 + X1) / 2, y: YB + 40, "text-anchor": "middle", "font-size": 13, fill: soft }, svg)
      .textContent = "latitude";
    const hEps = F(eps), bandMass = Math.max(0, 2 * hEps - 1);
    const pct = (v) => (v > 0.9999 ? "> 99.99" : (100 * v).toFixed(2)) + "%";
    out.innerHTML = `On 𝕊<sup>${n}</sup>, the <i>ε</i>-neighbourhood of a hemisphere has measure
      <b>${pct(hEps)}</b>, and the points within <i>ε</i> = ${eps.toFixed(2)} of the equator have measure
      <b>${pct(bandMass)}</b>.`;
  }
  nIn.addEventListener("input", update);
  eIn.addEventListener("input", update);
  function theme() {
    const dark = document.documentElement.classList.contains("dark");
    box.classList.toggle("dark", dark); box.classList.toggle("light", !dark);
    update();
  }
  new MutationObserver(theme).observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
  theme();
}

export default { render };
