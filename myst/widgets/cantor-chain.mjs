// The standard chain of Example 15.3, interactively: move t and see the member
// E ∩ [0, t] of the chain, where E is the ternary Cantor set.
//
// Shown after Figure 15.1 on both sites: by an anywidget directive that
// myst/tools/site_map.py adds on the MyST site, and by latex/tools/postprocess.py on
// the LaTeX site. It needs no data from the page.

const DEPTH = 7;           // intervals drawn: 2^7 of length 3^-7
const STEPS = 2000;        // t runs through the fractions n/2000
const W = 680, H = 120, X0 = 40, X1 = 640;
const X = (t) => X0 + (X1 - X0) * t;
const NS = "http://www.w3.org/2000/svg";

function intervals(depth) {
  let ivs = [[0, 1]];
  for (let k = 0; k < depth; k++) {
    ivs = ivs.flatMap(([a, b]) => [[a, a + (b - a) / 3], [b - (b - a) / 3, b]]);
  }
  return ivs;
}

// For t = n/STEPS: the largest point s of E with s <= t, and the gap (open interval of
// [0, 1] \ E) that contains t, if any. Reads the ternary digits of t exactly: a digit 1
// that is not the last nonzero digit means that t lies in the middle third of the current
// interval, and the point of E sought is the left end of that middle third. The digits
// of n/STEPS are eventually periodic, so the loop ends.
function locate(n) {
  if (n === STEPS) return { s: 1, gap: null, k: 0 };
  let r = n, a = 0, scale = 1, k = 0;
  const seen = new Set();
  while (!seen.has(r)) {
    seen.add(r);
    r *= 3; scale /= 3; k++;
    const d = Math.floor(r / STEPS);
    r -= d * STEPS;
    if (d === 1) {
      const left = a + scale;
      return r === 0 ? { s: left, gap: null, k } : { s: left, gap: [left, a + 2 * scale], k };
    }
    a += d * scale;
  }
  return { s: n / STEPS, gap: null, k };
}

// A point a/3^k as a fraction when the denominator is small, otherwise as a decimal.
function show(x) {
  if (x === 0 || x === 1) return String(x);
  for (let k = 1; k <= 7; k++) {
    const m = Math.round(x * 3 ** k);
    if (Math.abs(m / 3 ** k - x) < 1e-12) return `${m}/${3 ** k}`;
  }
  return x.toFixed(5);
}

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
                   --on: #2f63b8; --off: #c9d0d6; --mark: #c4661f; }
      .box.dark  { --ink: #dde3e8; --soft: #a8b2bb; --rule: #3a4550; --bg: #1c2127;
                   --on: #7fa8ea; --off: #46515c; --mark: #f0a060; }
      .head { color: var(--soft); font-size: 14px; margin-bottom: .2em; }
      svg { width: 100%; height: auto; display: block; }
      label { display: flex; align-items: center; gap: .6em; font-style: italic; }
      input[type=range] { flex: 1; accent-color: var(--on); }
      .out { color: var(--soft); font-size: 14px; min-height: 2.9em; margin-top: .3em; }
    </style>
    <div class="box light">
      <div class="head">Interactive version: move <i>t</i> to run through the members
        <i>E</i>&nbsp;∩&nbsp;[0,&nbsp;<i>t</i>] of the standard chain. The dot marks the
        largest point of the member.</div>
      <svg viewBox="0 0 ${W} ${H}" role="img"
           aria-label="The Cantor set, with the member E ∩ [0, t] of the standard chain highlighted"></svg>
      <label><i>t</i><input type="range" min="0" max="${STEPS}" step="1" value="1250"
        aria-label="t"></label>
      <div class="out" aria-live="polite"></div>
    </div>`;
  const box = root.querySelector(".box");
  const svg = root.querySelector("svg");
  const input = root.querySelector("input");
  const out = root.querySelector(".out");

  const id = "cc" + Math.random().toString(36).slice(2, 8);
  const clip = el("rect", { x: 0, y: 0, height: H, width: 0 },
                  el("clipPath", { id }, el("defs", {}, svg)));
  const offLayer = el("g", {}, svg), onLayer = el("g", { "clip-path": `url(#${id})` }, svg);
  for (const [a, b] of intervals(DEPTH)) {
    const w = Math.max(X(b) - X(a), 0.8);
    el("rect", { x: X(a), y: 40, width: w, height: 26 }, offLayer);
    el("rect", { x: X(a), y: 40, width: w, height: 26 }, onLayer);
  }
  const gapLine = el("line", { y1: 80, y2: 80, "stroke-width": 3, "stroke-linecap": "round" }, svg);
  const dot = el("circle", { r: 5, cy: 53 }, svg);
  const marker = el("path", {}, svg);
  const labels = [];
  for (const [t, s] of [[0, "0"], [1, "1"]]) {
    const tx = el("text", { x: X(t), y: 104, "text-anchor": "middle", "font-size": 14 }, svg);
    tx.textContent = s; labels.push(tx);
  }
  const tlabel = el("text", { y: 16, "text-anchor": "middle", "font-size": 15,
                              "font-style": "italic" }, svg);
  tlabel.textContent = "t"; labels.push(tlabel);

  const colour = (name) => getComputedStyle(box).getPropertyValue(name).trim();
  function update() {
    const n = Number(input.value), t = n / STEPS;
    const { s, gap } = locate(n);
    const on = colour("--on"), off = colour("--off"), mark = colour("--mark"), ink = colour("--ink");
    offLayer.setAttribute("fill", off);
    onLayer.setAttribute("fill", on);
    clip.setAttribute("width", X(s));
    dot.setAttribute("cx", X(s)); dot.setAttribute("fill", on);
    dot.setAttribute("stroke", colour("--bg")); dot.setAttribute("stroke-width", 1.5);
    if (gap) {
      gapLine.setAttribute("x1", X(gap[0])); gapLine.setAttribute("x2", X(gap[1]));
      gapLine.setAttribute("stroke", mark); gapLine.setAttribute("visibility", "visible");
    } else gapLine.setAttribute("visibility", "hidden");
    marker.setAttribute("d", `M${X(t)},32 l-6,-9 h12 z`);
    marker.setAttribute("fill", mark);
    tlabel.setAttribute("x", X(t));
    for (const tx of labels) tx.setAttribute("fill", ink);
    const tt = `<i>t</i> = ${t.toFixed(4)}`;
    out.innerHTML = n === 0
      ? `${tt}: the member is the root {0}.`
      : n === STEPS ? `${tt}: the member is <i>E</i> itself.`
      : gap
        ? `${tt} lies in the gap (${show(gap[0])}, ${show(gap[1])})` +
          (gap[1] - gap[0] < 3 ** -DEPTH ? ", too short to draw" : "") +
          `, so the member is <i>E</i>&nbsp;∩&nbsp;[0,&nbsp;${show(s)}], the same for every ` +
          `<i>t</i> in the gap.`
        : `${tt} lies in <i>E</i>, so the member is <i>E</i>&nbsp;∩&nbsp;[0,&nbsp;<i>t</i>] ` +
          `and its largest point is <i>t</i> itself.`;
  }
  function theme() {
    const dark = document.documentElement.classList.contains("dark");
    box.classList.toggle("dark", dark); box.classList.toggle("light", !dark);
    update();
  }
  input.addEventListener("input", update);
  new MutationObserver(theme).observe(document.documentElement,
                                      { attributes: true, attributeFilter: ["class"] });
  theme();
}

export default { render };
