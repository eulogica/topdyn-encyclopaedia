// Map of the encyclopaedia: the entries by strand, and for each strand a map of its
// results. Both versions use this module on their front page: the MyST version through
// the anywidget directive (myst/tools/site_map.py writes it into index.md at build
// time), the LaTeX version through a module script (latex/tools/postprocess.py). The
// data come from latex/tools/site_map.py.

const CSS = `
.em{--bg:#fff;--paper:#f7f7f3;--ink:#18212b;--soft:#4f5b66;--faint:#8a949c;--rule:#d9dde0;
  --box:#fff;--box-line:#aab4bb;--def:#eef1ec;--def-line:#a6b1a3;--main:#1f3f8f;--main-ink:#fff;
  --cited:#f6efdf;--cited-line:#b6a27a;--dep:#1f55c8;--dep-wash:#e7eefc;--use:#c2461f;--use-wash:#fbebe4;
  --edge:#9aa5ad;font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);margin:.5rem 0 1.5rem}
.em.dark{--bg:#14171b;--paper:#1b1f24;--ink:#e8eaec;--soft:#b5bcc2;--faint:#7d868d;--rule:#353b42;
  --box:#1d2227;--box-line:#5f6a73;--def:#222a24;--def-line:#5d6b5a;--main:#4f74d6;--main-ink:#fff;
  --cited:#2b2619;--cited-line:#8a7a55;--dep:#7da2ff;--dep-wash:#1f2a46;--use:#ff8c66;--use-wash:#43241a;--edge:#68737b}
.em *{box-sizing:border-box}
.em-intro{color:var(--soft);margin:0 0 .6rem;max-width:62em}
.em-tabs{display:flex;flex-wrap:wrap;gap:.2rem 1.2rem;border-bottom:1px solid var(--rule);margin-bottom:.4rem}
.em-tabs button{font-weight:600;font-size:14px;line-height:1.3;font-family:inherit;color:var(--soft);background:none;border:0;
  border-bottom:3px solid transparent;padding:.5rem 0 .45rem;cursor:pointer}
.em-tabs button[aria-pressed=true]{color:var(--ink);border-bottom-color:var(--main)}
.em-tabs button:hover{color:var(--ink)}
.em button:focus-visible,.em a:focus-visible,.em input:focus-visible{outline:2px solid var(--dep);outline-offset:2px}
.em-controls{display:flex;flex-wrap:wrap;gap:.4rem 1.2rem;align-items:center;min-height:2rem;color:var(--soft);font-size:14px}
.em-controls label{display:inline-flex;gap:.4rem;align-items:center;cursor:pointer}
.em-controls input{width:16px;height:16px;accent-color:var(--main)}
.em-scroll{overflow-x:auto;border:1px solid var(--rule);border-radius:6px;background:var(--bg)}
.em-scroll svg{display:block;width:100%;height:auto}
.em-n{cursor:pointer;text-decoration:none}
.em-n rect{fill:var(--box);stroke:var(--box-line);stroke-width:1.2}
.em-n .k{fill:var(--soft);font:600 11.5px system-ui,sans-serif;letter-spacing:.02em}
.em-n .t{fill:var(--ink);font:600 13.5px system-ui,sans-serif}
.em-n .p{fill:var(--soft);font:400 11.5px system-ui,sans-serif}
.em-n.def rect{fill:var(--def);stroke:var(--def-line)}
.em-n.cited rect{fill:var(--cited);stroke:var(--cited-line);stroke-dasharray:4 2}
.em-n.stub rect{stroke-dasharray:2 3;stroke:var(--faint)}
.em-n.stub .t,.em-n.stub .k{fill:var(--soft)}
.em-n .stripe{fill:var(--main);stroke:none}.em-n.has-main .k{fill:var(--main)}
.em.dark .em-n.has-main .k{fill:#9db4ff}
.em-n.main rect{fill:var(--main);stroke:var(--main)}
.em-n.main .t,.em-n.main .k,.em-n.main .p{fill:var(--main-ink)}
.em-n:hover rect,.em-n:focus rect,.em-n.on rect{stroke:var(--ink);stroke-width:2.6}
.em-n.dep rect{stroke:var(--dep);stroke-width:2.4}.em-n.dep:not(.main) rect{fill:var(--dep-wash)}
.em-n.use rect{stroke:var(--use);stroke-width:2.4}.em-n.use:not(.main) rect{fill:var(--use-wash)}
.em-n:focus{outline:none}
.em-e{fill:none;stroke:var(--edge);stroke-width:1.3;opacity:.75}
.em-e.dep{stroke:var(--dep);stroke-width:2.2;opacity:1}.em-e.use{stroke:var(--use);stroke-width:2.2;opacity:1}
.em-a{fill:var(--edge)}.em-a.dep{fill:var(--dep)}.em-a.use{fill:var(--use)}
.em-dim{opacity:.18}
.em-lane{fill:var(--soft);font:700 12.5px system-ui,sans-serif;letter-spacing:.03em;cursor:pointer}
.em-lane:hover{fill:var(--ink)}
.em-rule{stroke:var(--rule);stroke-dasharray:3 5}
.em-band{fill:var(--paper)}
.em-row{fill:var(--faint);font:600 11px system-ui,sans-serif;letter-spacing:.04em;text-transform:uppercase}
.em-info{min-height:3em;margin:.55rem 0 .2rem;color:var(--soft);font-size:14px}
.em-info b{color:var(--ink)}
.em-info a{color:var(--dep)}
.em-legend{display:flex;flex-wrap:wrap;gap:.3rem 1.1rem;color:var(--soft);font-size:13px;margin:.2rem 0 0}
.em-legend i{display:inline-block;width:.95em;height:.95em;border:1px solid var(--box-line);border-radius:2px;
  vertical-align:-.12em;margin-right:.35em;background:var(--box)}
.em-legend i.main{background:var(--main);border-color:var(--main)}.em-legend i.stripe{border-left:4px solid var(--main)}.em-legend i.def{background:var(--def);border-color:var(--def-line)}
.em-legend i.cited{background:var(--cited);border:1px dashed var(--cited-line)}.em-legend i.stub{border:1px dashed var(--faint)}
.em details{margin-top:.5rem;color:var(--soft);font-size:14px}
.em summary{cursor:pointer;width:fit-content}
.em details ul{margin:.4rem 0 0;padding-left:1.2em;columns:2 300px}
.em details li{break-inside:avoid;margin-bottom:.3rem}
.em details a{color:var(--dep)}
@media (prefers-reduced-motion:no-preference){.em-n rect,.em-e{transition:opacity .12s,stroke .12s,fill .12s}}
`;

const SVGNS = "http://www.w3.org/2000/svg";
const KIND_SHORT = { Theorem: "Thm.", Proposition: "Prop.", Corollary: "Cor.", Conjecture: "Conj.", Definition: "Def." };

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function measurer() {
  const ctx = document.createElement("canvas").getContext("2d");
  return (text, font) => { ctx.font = font; return ctx.measureText(text).width; };
}

// Split text into at most `max` lines of width at most `width`; the last line gets an ellipsis.
function wrap(text, width, font, measure, max) {
  // Break at spaces and after dashes; a piece that is still too wide is cut.
  const words = [];
  for (const w of String(text || "").split(/\s+/).filter(Boolean)) {
    for (const piece of w.split(/(?<=[–—-])/)) {
      let rest = piece;
      while (measure(rest, font) > width && rest.length > 1) {
        let k = rest.length - 1;
        while (k > 1 && measure(rest.slice(0, k) + "…", font) > width) k--;
        words.push({ text: rest.slice(0, k) + "…", glue: false });
        rest = "";
      }
      if (rest) words.push({ text: rest, glue: /[–—-]$/.test(rest) });
    }
  }
  const lines = [];
  let cur = "", glued = false;
  for (const w of words) {
    const next = cur ? cur + (glued ? "" : " ") + w.text : w.text;
    if (measure(next, font) <= width || !cur) cur = next;
    else { lines.push(cur); cur = w.text; }
    glued = w.glue;
  }
  if (cur) lines.push(cur);
  if (lines.length > max) {
    const kept = lines.slice(0, max);
    let last = kept[max - 1];
    while (last && measure(last + "…", font) > width) last = last.replace(/\s*\S+$/, "");
    kept[max - 1] = (last || kept[max - 1]) + "…";
    return kept;
  }
  return lines;
}

function el(tag, attrs = {}, parent) {
  const node = document.createElementNS(SVGNS, tag);
  for (const [k, v] of Object.entries(attrs)) if (v !== undefined && v !== null) node.setAttribute(k, v);
  if (parent) parent.appendChild(node);
  return node;
}

function longestPathLayers(ids, preds) {
  const layer = new Map();
  const visit = (v, stack = new Set()) => {
    if (layer.has(v)) return layer.get(v);
    if (stack.has(v)) return 0;
    stack.add(v);
    let l = 0;
    for (const u of preds.get(v) || []) l = Math.max(l, visit(u, stack) + 1);
    stack.delete(v);
    layer.set(v, l);
    return l;
  };
  for (const v of ids) visit(v);
  return layer;
}

export default {
  render({ model, el: host }) {
    const D = model.get("data");
    const measure = measurer();
    const root = document.createElement("div");
    root.className = "em";
    root.innerHTML = `<style>${CSS}</style>
      <p class="em-intro"></p>
      <div class="em-tabs"></div>
      <div class="em-controls"></div>
      <div class="em-scroll" tabindex="0"></div>
      <p class="em-info" aria-live="polite"></p>
      <p class="em-legend"></p>
      <details><summary>Text version of this map</summary><ul></ul></details>`;
    host.appendChild(root);
    const $ = s => root.querySelector(s);

    // Follow the page's light or dark theme (the MyST theme sets class="dark" on <html>).
    const theme = () => root.classList.toggle("dark", document.documentElement.classList.contains("dark"));
    theme();
    new MutationObserver(theme).observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });

    const entries = new Map(D.entries.map(e => [e.n, e]));
    const nodes = new Map(D.nodes.map(n => [n.id, n]));
    const strandOf = n => entries.get(n.entry).strand;
    const proofStrand = D.strands.findIndex(s => s.title === "Proofs");
    // The Proofs entries' results are shown with the strand before them.
    const viewStrand = n => (strandOf(n) === proofStrand ? proofStrand - 1 : strandOf(n));
    const label = n => `${n.kind} ${n.num}`;
    const views = [{ id: "overview", title: "Overview" }].concat(
      D.strands.map((s, i) => ({ id: "s" + i, title: s.title, strand: i })).filter(v => v.strand !== proofStrand));
    let current = "overview", showDefs = false, selected = null;

    const tabs = $(".em-tabs");
    for (const v of views) {
      const b = document.createElement("button");
      b.type = "button";
      b.textContent = v.title;
      b.dataset.view = v.id;
      b.addEventListener("click", () => show(v.id));
      tabs.appendChild(b);
    }

    function show(id) {
      current = id;
      selected = null;
      for (const b of tabs.children) b.setAttribute("aria-pressed", String(b.dataset.view === id));
      const v = views.find(x => x.id === id);
      if (v.id === "overview") overview(); else strand(v);
    }

    // Highlighting: what the hovered or focused box rests on (blue) and what uses it (red).
    function wire(svg, preds, succs, describe) {
      const boxes = new Map([...svg.querySelectorAll(".em-n")].map(g => [g.dataset.id, g]));
      const edges = [...svg.querySelectorAll(".em-e")];
      const clear = () => {
        for (const g of boxes.values()) g.classList.remove("on", "dep", "use", "em-dim");
        for (const e of edges) e.classList.remove("dep", "use", "em-dim");
        for (const a of svg.querySelectorAll(".em-a")) a.classList.remove("dep", "use", "em-dim");
      };
      const light = id => {
        clear();
        const ps = preds.get(id) || new Set(), ss = succs.get(id) || new Set();
        for (const [k, g] of boxes) {
          if (k === id) g.classList.add("on");
          else if (ps.has(k)) g.classList.add("dep");
          else if (ss.has(k)) g.classList.add("use");
          else g.classList.add("em-dim");
        }
        for (const e of edges) {
          const cls = e.dataset.t === id && ps.has(e.dataset.s) ? "dep" : e.dataset.s === id && ss.has(e.dataset.t) ? "use" : null;
          if (cls) { e.classList.add(cls); e.nextSibling?.classList?.add(cls); }
          else { e.classList.add("em-dim"); e.nextSibling?.classList?.add("em-dim"); }
        }
        $(".em-info").innerHTML = describe(id);
      };
      for (const [id, g] of boxes) {
        g.addEventListener("mouseenter", () => light(id));
        g.addEventListener("focus", () => light(id));
        g.addEventListener("mouseleave", () => { clear(); restore(); });
        g.addEventListener("blur", () => { clear(); restore(); });
      }
    }

    function restore() {
      $(".em-info").innerHTML = current === "overview"
        ? "Hover over or focus an entry to see the entries it rests on (blue) and those that rest on it (red). Click to open it; click a strand's name to see its results."
        : "Hover over or focus a statement to see what it rests on (blue) and what uses it (red). Click to open it.";
    }

    // how: "down" (bottom to top), "right" or "left" (side to side), "bulge" (right side to right side).
    function arrow(svg, x1, y1, x2, y2, s, t, how = "down") {
      let d, dx = 0, dy = 1;
      if (how === "bulge") {
        const b = 16 + Math.min(30, Math.abs(y2 - y1) / 12);
        d = `M${x1} ${y1} C${x1 + b} ${y1}, ${x2 + b} ${y2}, ${x2 + 6} ${y2}`;
        dx = -1; dy = 0;
      } else if (how === "right" || how === "left") {
        const sg = how === "right" ? 1 : -1, c = Math.max(24, Math.abs(x2 - x1) / 3);
        d = `M${x1} ${y1} C${x1 + sg * c} ${y1}, ${x2 - sg * c} ${y2}, ${x2 - sg * 6} ${y2}`;
        dx = sg; dy = 0;
      } else {
        const my = (y1 + y2) / 2;
        d = `M${x1} ${y1} C${x1} ${my}, ${x2} ${my}, ${x2} ${y2 - 6}`;
      }
      el("path", { d, class: "em-e", "data-s": s, "data-t": t }, svg);
      // Arrowhead: a small triangle at the target, pointing along the final tangent.
      const ax = x2, ay = y2;
      const w = 4.5, l = 7;
      const px = -dy, py = dx;
      el("path", { class: "em-a", d: `M${ax} ${ay} L${ax - dx * l + px * w} ${ay - dy * l + py * w} L${ax - dx * l - px * w} ${ay - dy * l - py * w} Z` }, svg);
    }

    function textList(items) {
      $("details ul").innerHTML = items.join("");
    }

    function legend(html) { $(".em-legend").innerHTML = html; }

    // ----- Overview: one column per strand, the entries in order, arrows between entries.
    function overview() {
      $(".em-intro").innerHTML = "The entries of the encyclopaedia, by strand. An arrow runs from an entry to each entry with a statement or proof that uses one of its statements. A coloured edge marks the entries with main results: theorems that no other statement uses.";
      $(".em-controls").innerHTML = "";
      const L = D.strands.length, laneW = 196, gap = 26, pad = 16, top = 56, vgap = 26;
      const W = pad * 2 + L * laneW + (L - 1) * gap;
      const kickFont = "600 11.5px system-ui,sans-serif", titleFont = "600 13.5px system-ui,sans-serif";
      const preds = new Map(), succs = new Map();
      for (const [a, b] of D.entryEdges) {
        if (!preds.has(b)) preds.set(b, new Set()); preds.get(b).add(a);
        if (!succs.has(a)) succs.set(a, new Set()); succs.get(a).add(b);
      }
      const pos = new Map(), laneBottom = new Array(L).fill(top - vgap);
      for (const e of [...D.entries].sort((a, b) => a.n - b.n)) {
        const lines = wrap(e.title, laneW - 28, titleFont, measure, 3);
        const h = 30 + lines.length * 17 + 8;
        const y = laneBottom[e.strand] + vgap;
        const x = pad + e.strand * (laneW + gap);
        pos.set(e.n, { x, y, w: laneW, h, lines });
        laneBottom[e.strand] = y + h;
      }
      const H = Math.max(...laneBottom) + pad + 4;
      const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": "Map of the entries by strand" });
      svg.style.minWidth = "860px";
      for (let i = 0; i < L; i++) {
        const x = pad + i * (laneW + gap);
        if (i > 0) el("line", { x1: x - gap / 2, x2: x - gap / 2, y1: 14, y2: H - 8, class: "em-rule" }, svg);
        const title = wrap(D.strands[i].title.toUpperCase(), laneW, "700 12.5px system-ui,sans-serif", measure, 2);
        const t = el("text", { x, y: 22, class: "em-lane", role: i === proofStrand ? null : "button", tabindex: i === proofStrand ? null : "0" }, svg);
        title.forEach((line, k) => { const s = el("tspan", { x, dy: k ? 15 : 0 }, t); s.textContent = line; });
        if (i !== proofStrand) {
          const go = () => show("s" + i);
          t.addEventListener("click", go);
          t.addEventListener("keydown", ev => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); go(); } });
        } else t.style.cursor = "default";
      }
      const sorted = [...D.entries].sort((a, b) => a.n - b.n);
      const laneIndex = new Map();
      for (const e of sorted) { const arr = laneIndex.get(e.strand) || []; arr.push(e.n); laneIndex.set(e.strand, arr); }
      for (const [a, b] of D.entryEdges) {
        const p = pos.get(a), q = pos.get(b);
        const ea = entries.get(a), eb = entries.get(b);
        const lane = laneIndex.get(ea.strand);
        const [sa, sb] = [String(a), String(b)];
        if (ea.strand < eb.strand) arrow(svg, p.x + p.w, p.y + p.h / 2, q.x, q.y + q.h / 2, sa, sb, "right");
        else if (ea.strand > eb.strand) arrow(svg, p.x, p.y + p.h / 2, q.x + q.w, q.y + q.h / 2, sa, sb, "left");
        else if (lane.indexOf(b) - lane.indexOf(a) === 1) arrow(svg, p.x + p.w / 2, p.y + p.h, q.x + q.w / 2, q.y, sa, sb);
        else arrow(svg, p.x + p.w, p.y + p.h / 2, q.x + q.w, q.y + q.h / 2, sa, sb, "bulge");
      }
      for (const e of D.entries) {
        const p = pos.get(e.n);
        const a = el("a", { href: e.href, class: "em-n" + (e.mains ? " has-main" : ""), "data-id": String(e.n),
          "aria-label": `Section ${e.n}, ${e.title}${e.mains ? `, ${e.mains} main result${e.mains > 1 ? "s" : ""}` : ""}` }, svg);
        el("title", {}, a).textContent = `Section ${e.n}: ${e.title}`;
        el("rect", { x: p.x, y: p.y, width: p.w, height: p.h, rx: 5 }, a);
        if (e.mains) el("rect", { x: p.x + 0.6, y: p.y + 0.6, width: 5, height: p.h - 1.2, rx: 2, class: "stripe" }, a);
        const k = el("text", { x: p.x + 14, y: p.y + 19, class: "k" }, a);
        k.textContent = `SECTION ${e.n}` + (e.mains ? ` · ${e.mains} MAIN RESULT${e.mains > 1 ? "S" : ""}` : "");
        p.lines.forEach((line, i) => { const t = el("text", { x: p.x + 14, y: p.y + 38 + i * 17, class: "t" }, a); t.textContent = line; });
      }
      const box = $(".em-scroll"); box.replaceChildren(svg);
      const name = n => `Section ${n} (${entries.get(n).title})`;
      wire(svg, new Map([...preds].map(([k, v]) => [String(k), new Set([...v].map(String))])),
        new Map([...succs].map(([k, v]) => [String(k), new Set([...v].map(String))])), id => {
          const n = Number(id), e = entries.get(n);
          const ps = [...(preds.get(n) || [])].sort((x, y) => x - y), ss = [...(succs.get(n) || [])].sort((x, y) => x - y);
          return `<b>Section ${n}: ${esc(e.title)}</b>. ${e.statements} statement${e.statements === 1 ? "" : "s"}` +
            (e.mains ? `, ${e.mains} main result${e.mains > 1 ? "s" : ""}` : "") + ". " +
            (ps.length ? `Rests on Section${ps.length > 1 ? "s" : ""} ${ps.join(", ")}, and on what ${ps.length > 1 ? "they rest" : "it rests"} on. ` : "Rests on no other entry. ") +
            (ss.length ? `Used by Sections ${ss.join(", ")}.` : "No other entry uses it.");
        });
      legend('<span><i class="stripe"></i>Entry with main results</span><span><i></i>Entry</span><span>Arrows lead from an entry to the entries that use it; implied arrows are left out.</span>');
      textList(sorted.map(e => {
        const ps = [...(preds.get(e.n) || [])].sort((x, y) => x - y);
        return `<li><a href="${esc(e.href)}">${esc(name(e.n))}</a>` + (ps.length ? ` uses ${ps.map(n => `<a href="${esc(entries.get(n).href)}">Section ${n}</a>`).join(", ")}.` : " uses no other entry.") + "</li>";
      }));
      restore();
    }

    // ----- One strand: its results (and definitions, if chosen), with what they rest on.
    function strand(v) {
      const s = D.strands[v.strand];
      $(".em-intro").innerHTML = `The results of the entries in <b>${esc(s.title)}</b>` +
        (v.strand === proofStrand - 1 ? ", with the main results stated in the Proofs entries" : "") +
        ". An arrow runs from a statement to each statement that rests on it, directly or through statements not shown here; implied arrows are left out. Boxes with a dotted border are results from other strands that these rest on.";
      $(".em-controls").innerHTML = `<label><input type="checkbox"${showDefs ? " checked" : ""}> Show definitions</label>`;
      $(".em-controls input").addEventListener("change", ev => { showDefs = ev.target.checked; strand(v); });
      const visible = n => showDefs || n.kind !== "Definition";
      const inView = new Set(D.nodes.filter(n => viewStrand(n) === v.strand && visible(n)).map(n => n.id));
      const E = (showDefs ? D.edgesWithDefs : D.edges).filter(([a, b]) => inView.has(b) && nodes.has(a) && visible(nodes.get(a)));
      const stubs = new Set(E.map(([a]) => a).filter(a => !inView.has(a)));
      const ids = [...inView, ...stubs];
      const preds = new Map(), succs = new Map();
      for (const [a, b] of E) {
        if (!preds.has(b)) preds.set(b, new Set()); preds.get(b).add(a);
        if (!succs.has(a)) succs.set(a, new Set()); succs.get(a).add(b);
      }
      const layerOf = longestPathLayers(ids, preds);
      for (const id of stubs) layerOf.set(id, 0);
      // Statements of the strand sit below the borrowed ones.
      if (stubs.size) for (const id of inView) layerOf.set(id, Math.max(1, layerOf.get(id) + (preds.has(id) ? 0 : 1)));
      const fix = () => { let moved = true; while (moved) { moved = false; for (const [a, b] of E) if (layerOf.get(b) <= layerOf.get(a)) { layerOf.set(b, layerOf.get(a) + 1); moved = true; } } };
      fix();
      const nLayers = Math.max(0, ...layerOf.values()) + 1;
      const layers = Array.from({ length: nLayers }, () => []);
      const byNum = (a, b) => { const x = nodes.get(a).num.split(".").map(Number), y = nodes.get(b).num.split(".").map(Number); return x[0] - y[0] || x[1] - y[1]; };
      for (const id of ids) layers[layerOf.get(id)].push(id);
      for (const l of layers) l.sort(byNum);
      // A few barycentre sweeps to reduce crossings.
      const idx = new Map();
      const reindex = () => layers.forEach(l => l.forEach((id, i) => idx.set(id, i / Math.max(1, l.length - 1))));
      reindex();
      for (let sweep = 0; sweep < 4; sweep++) {
        const down = sweep % 2 === 0;
        const seq = down ? layers.slice(1) : layers.slice(0, -1).reverse();
        for (const l of seq) {
          const bary = id => { const nb = [...(down ? preds.get(id) || [] : succs.get(id) || [])]; return nb.length ? nb.reduce((t, u) => t + idx.get(u), 0) / nb.length : idx.get(id); };
          const b = new Map(l.map(id => [id, bary(id)]));
          l.sort((x, y) => b.get(x) - b.get(y) || byNum(x, y));
          l.forEach((id, i) => idx.set(id, i / Math.max(1, l.length - 1)));
        }
      }
      const bw = 172, bgap = 14, perRow = 6, pad = 16, rowGap = 34;
      const W = pad * 2 + perRow * bw + (perRow - 1) * bgap;
      const kickFont = "600 11.5px system-ui,sans-serif", titleFont = "600 13.5px system-ui,sans-serif";
      const pos = new Map();
      let y = pad + 4;
      const bands = [];
      layers.forEach((l, li) => {
        for (let start = 0; start < l.length; start += perRow) {
          const row = l.slice(start, start + perRow);
          const geo = row.map(id => {
            const n = nodes.get(id);
            const lines = n.title ? wrap(n.title, bw - 22, titleFont, measure, 2) : [];
            const extra = (n.proofIn && !stubs.has(id)) || stubs.has(id) ? 1 : 0;
            return { id, lines, h: 30 + lines.length * 17 + extra * 15 + 6 };
          });
          const h = Math.max(...geo.map(g => g.h));
          const width = row.length * bw + (row.length - 1) * bgap;
          let x = (W - width) / 2;
          for (const g of geo) { pos.set(g.id, { x, y, w: bw, h, lines: g.lines }); x += bw + bgap; }
          if (li === 0 && stubs.size) bands.push([y, h]);
          y += h + rowGap;
        }
      });
      const H = y - rowGap + pad + 4;
      const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": `Map of the results in ${s.title}` });
      svg.style.minWidth = "860px";
      if (stubs.size) {
        const y0 = Math.min(...bands.map(b => b[0])) - 8, y1 = Math.max(...bands.map(b => b[0] + b[1])) + 8;
        el("rect", { x: 0, y: y0, width: W, height: y1 - y0, class: "em-band" }, svg);
        const t = el("text", { x: 8, y: y1 + 14, class: "em-row" }, svg); t.textContent = "From other strands";
      }
      for (const [a, b] of E) {
        const p = pos.get(a), q = pos.get(b);
        arrow(svg, p.x + p.w / 2, p.y + p.h, q.x + q.w / 2, q.y, a, b);
      }
      for (const id of ids) {
        const n = nodes.get(id), p = pos.get(id), stub = stubs.has(id);
        const cls = ["em-n", n.kind === "Definition" ? "def" : "", n.main ? "main" : "", n.cited && !n.main ? "cited" : "", stub ? "stub" : ""].filter(Boolean).join(" ");
        const a = el("a", { href: n.href, class: cls, "data-id": id,
          "aria-label": `${label(n)}${n.title ? ", " + n.title : ""}${n.main ? ", main result" : ""}` }, svg);
        el("title", {}, a).textContent = `${label(n)}${n.title ? " (" + n.title + ")" : ""}`;
        el("rect", { x: p.x, y: p.y, width: p.w, height: p.h, rx: 5 }, a);
        const k = el("text", { x: p.x + 11, y: p.y + 19, class: "k" }, a);
        k.textContent = label(n).toUpperCase();
        p.lines.forEach((line, i) => { const t = el("text", { x: p.x + 11, y: p.y + 38 + i * 17, class: "t" }, a); t.textContent = line; });
        const note = stub ? `in Section ${n.entry}` : n.proofIn ? `proof in Section ${n.proofIn}` : "";
        if (note) { const t = el("text", { x: p.x + 11, y: p.y + 38 + p.lines.length * 17 + (p.lines.length ? 0 : -2), class: "p" }, a); t.textContent = note; }
      }
      $(".em-scroll").replaceChildren(svg);
      const short = id => { const n = nodes.get(id); return `${KIND_SHORT[n.kind] || n.kind} ${n.num}`; };
      const list = set => [...set].sort(byNum).map(id => `<a href="${esc(nodes.get(id).href)}">${esc(short(id))}</a>`).join(", ");
      wire(svg, preds, succs, id => {
        const n = nodes.get(id), ps = preds.get(id) || new Set(), ss = succs.get(id) || new Set();
        return `<b>${esc(label(n))}${n.title ? " (" + esc(n.title) + ")" : ""}</b>` +
          (n.main ? ", a main result" : n.cited ? ", quoted from the literature" : "") + `, in Section ${n.entry}. ` +
          (ps.length ? `Rests on ${list(ps)}. ` : "") + (ss.length ? `Used by ${list(ss)}. ` : "") +
          (n.proofIn ? `Its proof is in Section ${n.proofIn}. ` : "") +
          (n.kind !== "Definition" ? `<a href="${esc(D.proofTree)}#tree=${encodeURIComponent(id)}">Its full proof tree</a>.` : "");
      });
      legend('<span><i class="main"></i>Main result</span><span><i></i>Result</span>' +
        (showDefs ? '<span><i class="def"></i>Definition</span>' : "") +
        '<span><i class="cited"></i>Quoted from the literature</span><span><i class="stub"></i>From another strand</span>');
      textList([...inView].sort(byNum).map(id => {
        const ps = preds.get(id);
        return `<li><a href="${esc(nodes.get(id).href)}">${esc(label(nodes.get(id)))}${nodes.get(id).title ? " (" + esc(nodes.get(id).title) + ")" : ""}</a>` +
          (ps && ps.size ? ` rests on ${list(ps)}.` : " rests on no statement shown here.") + "</li>";
      }));
      restore();
    }

    show("overview");
  },
};
