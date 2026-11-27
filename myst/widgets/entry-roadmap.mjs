// Roadmap of a Proofs entry: its subsections in order, with an arrow from one
// subsection to each later or earlier subsection that uses one of its results. Both
// versions put it at the top of each Proofs entry: the MyST version through the
// anywidget directive (myst/tools/site_map.py), the LaTeX version through a module
// script (latex/tools/postprocess.py). The data come from roadmap() in
// latex/tools/site_map.py.

const CSS = `
.er{--bg:#fff;--ink:#18212b;--soft:#4f5b66;--rule:#d9dde0;--box:#fff;--box-line:#c3cbd1;
  --main:#1f3f8f;--main-wash:#eef2fb;--dep:#1f55c8;--dep-wash:#e7eefc;--use:#c2461f;--use-wash:#fbebe4;
  --edge:#9aa5ad;font:15px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);margin:.4rem 0 1.6rem}
.er.dark{--bg:#14171b;--ink:#e8eaec;--soft:#b5bcc2;--rule:#353b42;--box:#1d2227;--box-line:#4d5760;
  --main:#7d9cf0;--main-wash:#1c2540;--dep:#7da2ff;--dep-wash:#1f2a46;--use:#ff8c66;--use-wash:#43241a;--edge:#68737b}
.er *{box-sizing:border-box}
.er-head{font-weight:650;margin:0 0 .15rem}
.er-intro{color:var(--soft);font-size:14px;margin:0 0 .6rem;max-width:60em}
.er-body{position:relative}
.er-arcs{position:absolute;left:0;top:0;overflow:visible;pointer-events:none}
.er-rows{list-style:none;margin:0;padding:0}
.er-row{border:1px solid var(--box-line);border-radius:6px;background:var(--box);padding:.35rem .7rem .4rem;
  margin:0 0 .45rem;outline:none}
.er-row.main{border-left:4px solid var(--main);background:var(--main-wash)}
.er-row:hover,.er-row:focus-within,.er-row.on{border-color:var(--ink)}
.er-row.dep{border-color:var(--dep);background:var(--dep-wash)}
.er-row.use{border-color:var(--use);background:var(--use-wash)}
.er-row.dim{opacity:.45}
.er-title{font-weight:600;color:var(--ink);text-decoration:none}
.er-title:hover{text-decoration:underline}
.er-num{color:var(--soft);font-weight:600;margin-right:.45em}
.er-meta{color:var(--soft);font-size:13.5px}
.er-meta a{color:var(--dep)}
.er-proves{color:var(--main);font-weight:600}
.er-e{fill:none;stroke:var(--edge);stroke-width:1.4}
.er-e.dep{stroke:var(--dep);stroke-width:2.3}.er-e.use{stroke:var(--use);stroke-width:2.3}
.er-e.dim{opacity:.2}
.er-a{fill:var(--edge)}.er-a.dep{fill:var(--dep)}.er-a.use{fill:var(--use)}
.er a:focus-visible{outline:2px solid var(--dep);outline-offset:2px}
@media (prefers-reduced-motion:no-preference){.er-row,.er-e{transition:opacity .12s,border-color .12s,background .12s,stroke .12s}}
`;

const SVGNS = "http://www.w3.org/2000/svg";

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function links(items) {
  return items.map(x => `<a href="${esc(x.href)}">${esc(x.text).replace(/ /, "&nbsp;")}</a>`).join(", ");
}

function svg(tag, attrs, parent) {
  const node = document.createElementNS(SVGNS, tag);
  for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, v);
  if (parent) parent.appendChild(node);
  return node;
}

export default {
  render({ model, el }) {
    const D = model.get("data");
    if (!D || !D.rows) return;
    const span = Math.max(1, ...D.edges.map(([a, b]) => Math.abs(a - b)));
    const gutter = Math.min(150, 26 + 13 * span);
    const root = document.createElement("div");
    root.className = "er";
    // The styles go with the widget: on the MyST site it is drawn in a shadow root.
    root.innerHTML = `<style>${CSS}</style>
      <p class="er-head">Roadmap of this entry</p>
      <p class="er-intro">Its parts in order, with an arrow from a part to each part that uses
        one of its results. A result stated in one part and proved in another counts as part of
        the one with its proof. Hover over or focus a part to see what it rests on (blue) and
        what rests on it (red).</p>
      <div class="er-body"><svg class="er-arcs" aria-hidden="true"></svg>
        <ol class="er-rows" style="margin-left:${gutter}px"></ol></div>`;
    el.replaceChildren(root);
    const list = root.querySelector(".er-rows");
    const arcs = root.querySelector(".er-arcs");
    const body = root.querySelector(".er-body");

    const rows = D.rows.map((r, i) => {
      const li = document.createElement("li");
      li.className = "er-row" + (r.states.length ? " main" : "");
      const meta = [];
      if (r.states.length)
        meta.push(`States the main results ${links(r.states)}; each is proved in the part that says so.`);
      else if (r.statements) meta.push(`${r.statements} statement${r.statements > 1 ? "s" : ""}`);
      if (r.proves.length) meta.push(`<span class="er-proves">Proves ${links(r.proves)}</span>`);
      if (r.provesElsewhere.length)
        meta.push(`${r.proves.length ? "also proves" : "Proves"} ${links(r.provesElsewhere)}`);
      const num = r.num ? `<span class="er-num">${esc(r.num)}</span>` : "";
      const title = r.href ? `<a class="er-title" href="${esc(r.href)}">${num}${esc(r.title)}</a>`
                           : `<span class="er-title">${num}${esc(r.title)}</span>`;
      li.innerHTML = `${title}${meta.length ? `<div class="er-meta">${meta.join(" · ")}</div>` : ""}`;
      li.tabIndex = -1;
      li.addEventListener("mouseenter", () => focus(i));
      li.addEventListener("mouseleave", () => focus(null));
      li.addEventListener("focusin", () => focus(i));
      li.addEventListener("focusout", () => focus(null));
      list.appendChild(li);
      return li;
    });

    let paths = [];
    function draw() {
      const box = body.getBoundingClientRect();
      arcs.setAttribute("width", Math.max(1, box.width));
      arcs.setAttribute("height", Math.max(1, box.height));
      arcs.replaceChildren();
      const defs = svg("defs", {}, arcs);
      for (const k of ["", "dep", "use"]) {
        const m = svg("marker", { id: `er-arrow-${k || "plain"}`, viewBox: "0 0 10 10", refX: 9, refY: 5,
                                  markerWidth: 7, markerHeight: 7, orient: "auto" }, defs);
        svg("path", { d: "M0,0 L10,5 L0,10 z", class: `er-a ${k}` }, m);
      }
      const mid = rows.map(li => {
        const r = li.getBoundingClientRect();
        return r.top - box.top + Math.min(r.height / 2, 14);
      });
      const x = gutter - 2;
      paths = D.edges.map(([a, b]) => {
        const bulge = Math.min(gutter - 8, 14 + 12 * Math.abs(a - b));
        const ya = mid[a] - 3, yb = mid[b] + 3;
        const p = svg("path", {
          d: `M${x},${ya} C${x - bulge},${ya} ${x - bulge},${yb} ${x},${yb}`,
          class: "er-e", "marker-end": "url(#er-arrow-plain)" }, arcs);
        return { a, b, p };
      });
    }

    function focus(i) {
      rows.forEach((li, k) => li.classList.remove("on", "dep", "use", "dim"));
      for (const e of paths) {
        e.p.setAttribute("class", "er-e");
        e.p.setAttribute("marker-end", "url(#er-arrow-plain)");
      }
      if (i === null) return;
      const near = new Set([i]);
      for (const e of paths) {
        const kind = e.b === i ? "dep" : e.a === i ? "use" : null;
        if (kind) {
          e.p.setAttribute("class", `er-e ${kind}`);
          e.p.setAttribute("marker-end", `url(#er-arrow-${kind})`);
          const other = kind === "dep" ? e.a : e.b;
          rows[other].classList.add(kind);
          near.add(other);
        } else e.p.setAttribute("class", "er-e dim");
      }
      rows[i].classList.add("on");
      rows.forEach((li, k) => { if (!near.has(k)) li.classList.add("dim"); });
    }

    const theme = () => root.classList.toggle("dark", document.documentElement.classList.contains("dark"));
    theme();
    new MutationObserver(theme).observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
    draw();
    if (typeof ResizeObserver !== "undefined") new ResizeObserver(draw).observe(body);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
  },
};
