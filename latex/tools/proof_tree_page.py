#!/usr/bin/env python3
"""Write the interactive proof tree of the whole encyclopaedia, served at /proof-tree/.

postprocess.py calls write() once it has read the LaTeX site. The page draws every
statement and what it rests on, as declared with \\uses in the statements and their
proofs, together with the results of other works that they cite with a precise
locator. Main results sit at the top. Selecting a statement shows it, with its proof,
and links to it in both versions and to its tag page; "Show what it rests on" keeps
only its proof tree. Links of the form /proof-tree/#tree=thm:ellis open a proof tree,
and /proof-tree/#thm:ellis selects a statement.

The viewer is adapted from the proof-tree skill's interactive page.
"""

import html
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

FAMILY = {"Definition": "definition", "Notation": "definition", "Theorem": "result",
          "Proposition": "result", "Corollary": "result", "Lemma": "result", "Claim": "result",
          "Conjecture": "open", "Question": "open", "Remark": "aside", "Example": "aside"}
LOCATOR_ABBR = [("Theorems", "Thms"), ("Theorem", "Thm"), ("Propositions", "Props"),
                ("Proposition", "Prop"), ("Corollary", "Cor"), ("Corollaries", "Cors"),
                ("Lemma", "Lem"), ("Lemmas", "Lems"), ("Section", "§"), ("Remark", "Rem")]


def myst_slugs(myst_dir):
    """MyST label -> URL path of its page on the site."""
    out = {}
    for path in sorted((myst_dir / "entries").glob("*.md")) + [myst_dir / "index.md"]:
        if not path.exists():
            continue
        slug = "" if path.name == "index.md" else re.sub(r"^\d+-", "", path.stem) + "/"
        for m in re.finditer(r"^:label:\s*(\S+)", path.read_text(), re.M):
            out[m.group(1)] = slug
    return out


def clean(el, ids):
    """Inner HTML of a plasTeX block for the panel: in-graph links, site-relative others."""
    el = BeautifulSoup(str(el), "html.parser")
    for x in el.select(".tag-badge, .thm_header_hidden_extras, .expand-proof, .source-links, svg"):
        x.decompose()
    for a in el.find_all("a"):
        href = a.get("href", "")
        frag = href.split("#", 1)[1] if "#" in href else ""
        if frag in ids:
            a.attrs = {"class": ["ref"], "data-id": frag}
        elif href and not re.match(r"[a-z]+:|/|#", href):
            a["href"] = "../latex/" + href
    root = el.find(True)
    return root.decode_contents().strip() if root else ""


def plain(s):
    """A statement title as plain text: TeX in it reduced to its letters."""
    s = re.sub(r"\\[()\[\]]", "", s or "")
    s = re.sub(r"\\(?:mathcal|mathrm|mathbb|operatorname|mathfrak|textup|emph)\s*\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\([A-Za-z]+)\s*", r"\1", s).replace("{", "").replace("}", "")
    return " ".join(s.split())


def bibliography(pages):
    """Citation key -> plain text of its entry."""
    out = {}
    for soup in pages.values():
        for a in soup.select("dt a[name]"):
            dd = a.find_parent("dt").find_next_sibling("dd")
            if dd:
                out[a["name"]] = " ".join(dd.get_text(" ").split())
    return out


def write(out_file, items, uses_stmt, uses_proof, cites, bib_links, pages, locs, myst_dir, kind_abbr):
    """items: label -> dict(tag, page, kind, num, title); uses_*: label -> [labels];
    cites: label -> [(key, locator)]; bib_links: key -> (href, number)."""
    slugs = myst_slugs(myst_dir)
    bib_text = bibliography(pages)
    keep = [l for l, it in items.items() if it["kind"] in FAMILY]
    order = sorted(keep, key=lambda l: (locs.get(l, ("~", 0)), l))
    ids = set(keep)
    edges, users = [], {}
    for v in keep:
        for via, src in (("statement", uses_stmt), ("proof", uses_proof)):
            for u in src.get(v, []):
                if u in ids and u != v:
                    edges.append(dict(s=u, t=v, via=via, basis="declared", ev="", decl=True))
                    users.setdefault(u, set()).add(v)
    ext = {}
    for v in keep:
        for key, loc in cites.get(v, []):
            if key not in bib_links:
                continue
            nid = f"cite:{key}:{loc}"
            href, num = bib_links[key]
            if nid not in ext:
                short = loc
                for a, b in LOCATOR_ABBR:
                    short = re.sub(rf"\b{a}\b", b, short)
                ext[nid] = dict(id=nid, kind="cited", fam="external", name=f"[{num}, {loc}]",
                                short=f"[{num}, {short}]", title="", main=False, origin="external",
                                order=10 ** 6 + len(ext), links=[[f"Bibliography entry [{num}]", f"../latex/{href}"]],
                                html=f"<p>{html.escape(loc)} of <a href=\"../latex/{html.escape(href)}\">[{html.escape(num)}]</a>: "
                                     f"{html.escape(bib_text.get(key, key))}</p>", proof="")
            edges.append(dict(s=nid, t=v, via="proof", basis="cite", ev="", decl=False))
    nodes = []
    for i, label in enumerate(order):
        it = items[label]
        page = pages[it["page"]]
        el = page.find(id=label)
        content = el.find("div", class_=lambda c: c and c.endswith("_thmcontent")) if el else None
        proof_html, proved = "", False
        for a in (el.select(".thm_header_hidden_extras a[href]") if el else []):
            if a.find("svg") is None and "icon-cogs" not in str(a):
                continue
            pid = a["href"].split("#", 1)[-1]
            p = pages.get(a["href"].split("#")[0], page).find(id=pid)
            body = p.find("div", class_="proof_content") if p else None
            if body:
                proof_html, proved = clean(body, ids)[:20000], True
        fam = FAMILY[it["kind"]]
        cited = bool(el and el.select_one('[class$="_thmtitle"] .cite'))
        mlabel = label.replace(":", "-", 1)
        links = []
        if mlabel in slugs:
            links.append(["In the encyclopaedia", f"../{slugs[mlabel]}#{mlabel}"])
        links.append(["LaTeX version", f"../latex/{it['page']}#{label}"])
        links.append([f"Tag {it['tag']}", f"../latex/tag/{it['tag']}.html"])
        nodes.append(dict(
            id=label, kind=it["kind"].lower(), fam=fam,
            name=f"{it['kind']} {it['num']}".strip(), short=f"{kind_abbr.get(it['kind'], it['kind'])} {it['num']}".strip(),
            title=plain(it["title"]), main=False,
            origin="proved" if proved else ("cited" if cited else "stated"),
            order=i, links=links, html=clean(content, ids)[:12000] if content else "", proof=proof_html))
    # Main results: theorems that nothing else uses.
    for n in nodes:
        if n["kind"] == "theorem" and not any(items[u]["kind"] in ("Theorem", "Proposition", "Corollary", "Lemma", "Definition")
                                             for u in users.get(n["id"], ())):
            n["main"] = True
    nodes += list(ext.values())
    data = dict(title="Proof tree of the encyclopaedia", nodes=nodes, edges=edges)
    page = VIEWER.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    out_file = Path(out_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(page)
    return len(nodes), len(edges), sum(n["main"] for n in nodes)


VIEWER = r'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Proof tree · Topological dynamics of topological groups</title>
<style>
:root{color-scheme:light dark;--bg:light-dark(#ffffff,#121417);--paper:light-dark(#f6f6f2,#1a1d21);--ink:light-dark(#141414,#ecebe6);--soft:light-dark(#4a4a48,#b9b8b2);--faint:light-dark(#8a8a86,#7d7d78);--rule:light-dark(#d9d9d3,#33363b);--def:light-dark(#ecece6,#262a2f);--accent:light-dark(#1f3fb8,#7d97ff);--accent-wash:light-dark(#e6ebfb,#1f2a52);--warm:light-dark(#d2461e,#ff8a65);--warm-wash:light-dark(#fbe9e3,#4a2219)}
*{box-sizing:border-box;min-width:0}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 "STIX Two Text","STIX Two",Georgia,serif;overflow-x:clip}
button,input,label.tg,nav{font:500 14px/1.2 system-ui,-apple-system,"Segoe UI",sans-serif}
nav{padding:12px max(4vw,16px) 0;display:flex;flex-wrap:wrap;gap:6px 18px}nav a{color:var(--accent);text-decoration:none}nav a:hover{text-decoration:underline}
header{padding:14px max(4vw,16px) 12px;display:flex;flex-wrap:wrap;gap:8px 32px;align-items:end;justify-content:space-between}
h1{font-size:clamp(24px,2.6vw,34px);line-height:1.12;margin:0;font-weight:600;max-width:32em}
.sub{font:400 14px/1.45 system-ui,sans-serif;color:var(--soft);margin:6px 0 0;max-width:62em}
.counts{display:flex;gap:22px;flex-wrap:wrap;font:400 13px/1.2 system-ui,sans-serif;color:var(--soft)}
.counts b{display:block;font:600 26px/1.1 Georgia,serif;color:var(--ink)}
.bar{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;padding:8px max(4vw,16px);border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);background:var(--paper);position:sticky;top:0;z-index:3}
.bar input[type=search]{min-height:40px;padding:6px 12px;border:1px solid var(--rule);border-radius:8px;background:var(--bg);color:var(--ink);font-size:16px;width:min(260px,100%)}
label.tg{display:inline-flex;gap:6px;align-items:center;min-height:40px;color:var(--soft);cursor:pointer}
label.tg input{width:18px;height:18px;accent-color:var(--accent)}
.btn{min-height:40px;min-width:40px;padding:6px 12px;border:1px solid var(--rule);border-radius:8px;background:var(--bg);color:var(--ink);cursor:pointer}
.btn:hover{border-color:var(--ink)}.btn:focus-visible,label.tg input:focus-visible,.bar input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.focus{display:none;gap:10px;align-items:center;font:500 14px system-ui,sans-serif;color:var(--accent)}.focus.on{display:inline-flex}
main{display:grid;grid-template-columns:minmax(0,1fr) minmax(320px,32%);min-height:72vh}
.map{position:relative;border-right:1px solid var(--rule);overflow:hidden;min-height:72vh;touch-action:none;background:var(--bg)}
.map svg{position:absolute;inset:0;width:100%;height:100%;cursor:grab}.map svg.drag{cursor:grabbing}
.zoom{position:absolute;right:12px;bottom:12px;display:flex;gap:6px}
.legend{position:absolute;left:12px;bottom:12px;display:flex;flex-wrap:wrap;gap:6px 14px;max-width:70%;font:400 12px/1.3 system-ui,sans-serif;color:var(--soft);background:color-mix(in srgb,var(--bg) 88%,transparent);padding:8px 10px;border-radius:8px;border:1px solid var(--rule)}
.legend i{display:inline-block;width:18px;height:11px;border-radius:3px;border:1px solid var(--soft);vertical-align:-1px;margin-right:5px}
.legend i.m{background:var(--accent);border-color:var(--accent)}.legend i.d{background:var(--def);border-color:var(--faint)}.legend i.x{border-style:dashed}.legend i.o{border-style:dotted;border-width:2px}
.legend s{display:inline-block;width:22px;border-top:1.5px solid var(--faint);vertical-align:3px;margin-right:5px}.legend s.st{border-top-style:dashed}
.n rect{fill:var(--bg);stroke:var(--soft);stroke-width:1}.n text{font:500 12px system-ui,sans-serif;fill:var(--ink);pointer-events:none}.n text.t{font:italic 400 11.5px Georgia,serif;fill:var(--soft)}
.n.k-theorem rect{stroke:var(--ink);stroke-width:1.6}.n.f-definition rect{fill:var(--def);stroke:var(--faint)}.n.f-external rect{stroke-dasharray:4 3}.n.f-open rect{stroke-dasharray:1.5 2.5;stroke-width:1.8}
.n.f-aside rect{stroke:var(--rule)}.n.f-aside text{fill:var(--faint)}
.n.main rect{fill:var(--accent);stroke:var(--accent)}.n.main text{fill:#fff;font-weight:600}.n.main text.t{fill:#dfe5ff}
.n{cursor:pointer}.n:hover rect{stroke:var(--accent);stroke-width:2}.n:focus{outline:none}.n:focus-visible rect{stroke:var(--accent);stroke-width:3}
.n.sel rect{stroke:var(--ink);stroke-width:3}.n.dep rect{stroke:var(--accent);stroke-width:2.4;fill:var(--accent-wash)}.n.use rect{stroke:var(--warm);stroke-width:2.4;fill:var(--warm-wash)}
.n.main.dep rect,.n.main.use rect{fill:var(--accent)}.n.hit rect{stroke:var(--warm);stroke-width:2.6}
.e{fill:none;stroke:var(--faint);stroke-width:1.1;opacity:.85}.e.st{stroke-dasharray:5 4}.e.ci{stroke-dasharray:1.5 3}.e.hid{stroke-dasharray:2 5;opacity:.6}
.e.dep{stroke:var(--accent);stroke-width:2;opacity:1}.e.use{stroke:var(--warm);stroke-width:2;opacity:1}.dim{opacity:.16}
#arw path{fill:var(--faint)}#arw-d path{fill:var(--accent)}#arw-u path{fill:var(--warm)}
aside{padding:20px 22px 28px;overflow:auto;max-height:calc(100vh - 60px);position:sticky;top:57px}
aside h2{font-size:24px;line-height:1.15;margin:0 0 4px;font-weight:600}aside .meta{font:400 13px/1.45 system-ui,sans-serif;color:var(--soft);margin:0 0 6px}
.links{font:500 13px/1.5 system-ui,sans-serif;margin:0 0 14px;display:flex;flex-wrap:wrap;gap:4px 14px}.links a{color:var(--accent)}
.badge{display:inline-block;font:500 12px/1 system-ui,sans-serif;padding:4px 8px;border-radius:99px;border:1px solid var(--rule);margin-right:6px;color:var(--soft)}
.badge.m{background:var(--accent);color:#fff;border-color:var(--accent)}
.stmt{font-size:17px;line-height:1.6;overflow-x:auto}.stmt a.ref,.proof a.ref,.chips button{color:var(--accent);cursor:pointer;text-decoration:underline;text-underline-offset:2px}
.stmt a,.proof a{color:var(--accent)}.equation_label{display:none}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 12px}.chips button{font:500 13px system-ui,sans-serif;text-decoration:none;border:1px solid var(--rule);background:var(--bg);border-radius:6px;padding:6px 9px;min-height:34px}
.chips button.u{color:var(--warm)}.via{font:400 12px system-ui,sans-serif;color:var(--faint);margin-top:4px}.chips .none{font:400 13px system-ui,sans-serif;color:var(--faint)}
h3{font:600 12.5px/1.3 system-ui,sans-serif;color:var(--soft);margin:18px 0 4px;letter-spacing:.01em}
details{margin-top:12px}summary{cursor:pointer;font:500 14px system-ui,sans-serif;color:var(--soft);min-height:32px}
.proof{font-size:15.5px;color:var(--soft);border-left:2px solid var(--rule);padding-left:12px;overflow-x:auto}
.empty{color:var(--soft);font:400 15px/1.6 system-ui,sans-serif}.empty b{color:var(--ink)}
.below{padding:18px max(4vw,16px) 40px;border-top:1px solid var(--rule);display:grid;grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr));gap:12px 36px;font:400 14px/1.5 system-ui,sans-serif;color:var(--soft)}
.below h3{margin-top:0}.below .chips button{font-size:12.5px}.below a{color:var(--accent)}
@media(max-width:900px){main{grid-template-columns:1fr}.map{border-right:0;border-bottom:1px solid var(--rule);min-height:62vh}aside{position:static;max-height:none}.legend{max-width:calc(100% - 120px)}}
@media(prefers-reduced-motion:no-preference){.n rect,.e{transition:opacity .15s,stroke .15s,fill .15s}}
</style></head><body>
<nav><a href="../">Topological dynamics of topological groups</a><a href="../latex/">LaTeX version</a><a href="../latex/graph.html">Dependency graph</a></nav>
<header><div><h1 id="ttl"></h1><p class="sub" id="sub"></p></div><div class="counts" id="counts"></div></header>
<div class="bar"><input type="search" id="q" placeholder="Find a statement" aria-label="Find a statement">
<label class="tg"><input type="checkbox" id="t-def"> Definitions</label><label class="tg"><input type="checkbox" id="t-aside"> Remarks and examples</label>
<label class="tg"><input type="checkbox" id="t-ext" checked> Cited results</label><label class="tg"><input type="checkbox" id="t-all"> Implied edges</label>
<span class="focus" id="focus"><span id="focus-t"></span><button class="btn" id="unfocus" type="button">Show all</button></span></div>
<main><div class="map" id="map"><svg id="svg" role="img" aria-label="Dependency graph"><defs>
<marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0.5 L9.5,5 L0,9.5 Z"/></marker>
<marker id="arw-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0.5 L9.5,5 L0,9.5 Z"/></marker>
<marker id="arw-u" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0.5 L9.5,5 L0,9.5 Z"/></marker></defs><g id="vp"><g id="eg"></g><g id="ng"></g></g></svg>
<div class="legend"><span><i class="m"></i>main result</span><span><i></i>result</span><span><i class="d"></i>definition</span><span><i class="x"></i>cited result</span><span><i class="o"></i>conjecture</span><span><s></s>used in a proof</span><span><s class="st"></s>used in a statement</span></div>
<div class="zoom"><button class="btn" id="zi" type="button" aria-label="Zoom in">+</button><button class="btn" id="zo" type="button" aria-label="Zoom out">−</button><button class="btn" id="zf" type="button">Fit</button></div></div>
<aside id="panel" aria-live="polite"></aside></main>
<section class="below" id="below"></section>
<script>
window.MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['\\[','\\]']],processEnvironments:true},svg:{fontCache:'global'},startup:{typeset:false},options:{enableMenu:false}};
</script>
<script id="pt-data" type="application/json">__DATA__</script>
<script>{
const D=JSON.parse(document.getElementById('pt-data').textContent);
const $=s=>document.querySelector(s),esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const N=new Map(D.nodes.map(n=>[n.id,n]));
const S={def:false,aside:false,ext:true,all:false,focus:null,sel:null,k:1,x:0,y:0};
const nRes=D.nodes.filter(n=>n.fam==='result').length,nDef=D.nodes.filter(n=>n.fam==='definition').length,nExt=D.nodes.filter(n=>n.fam==='external').length;
$('#ttl').textContent=D.title;
$('#sub').textContent='Every statement of the encyclopaedia and what it rests on. An arrow runs from an item to each statement whose statement or proof uses it, as declared in the LaTeX sources; cited results are results of other works that the statements and proofs cite with a precise locator. Main results, the theorems nothing else uses, sit at the top. The page is rebuilt at every update.';
const mains=D.nodes.filter(n=>n.main);
$('#counts').innerHTML=[[mains.length,'main results'],[nRes,'results'],[nDef,'definitions'],[nExt,'cited results'],[D.edges.length,'dependencies']].map(([v,l])=>`<div><b>${v}</b>${l}</div>`).join('');
const users={},deps={};for(const e of D.edges){(users[e.s]??=[]).push(e);(deps[e.t]??=[]).push(e)}
const cv=document.createElement('canvas').getContext('2d');
function tw(t,f){cv.font=f;return cv.measureText(t).width}
function visibleBase(n){if(n.fam==='definition')return S.def;if(n.fam==='aside')return S.aside;if(n.fam==='external')return S.ext;return true}
function closure(id,dir){const seen=new Set([id]),st=[id];while(st.length){const u=st.pop();for(const e of(dir==='up'?deps[u]:users[u])||[]){const w=dir==='up'?e.s:e.t;if(!seen.has(w)){seen.add(w);st.push(w)}}}return seen}
function graph(){
  let ids=new Set(D.nodes.filter(visibleBase).map(n=>n.id));
  if(S.focus){const c=closure(S.focus.id,S.focus.dir);ids=new Set([...ids].filter(i=>c.has(i)));ids.add(S.focus.id)}
  const E=[],seen=new Set();
  for(const id of ids){
    const st=[[id,false]],vis=new Set([id]);
    while(st.length){const[u,hid]=st.pop();for(const e of deps[u]||[]){const w=e.s;if(vis.has(w))continue;vis.add(w);
      if(ids.has(w)){const k=w+'\u0001'+id;if(!seen.has(k)){seen.add(k);E.push({s:w,t:id,via:e.via,basis:e.basis,hid:hid||u!==id})}}
      else st.push([w,true])}}
  }
  let F=E;if(!S.all){const adj={};for(const e of E)(adj[e.s]??=new Set()).add(e.t);
    F=E.filter(e=>{const st=[...(adj[e.s]||[])].filter(w=>w!==e.t),seen=new Set([e.s]);while(st.length){const w=st.pop();if(w===e.t)return false;if(seen.has(w))continue;seen.add(w);for(const x of adj[w]||[])if(!seen.has(x))st.push(x)}return true})}
  return{V:[...ids].map(i=>N.get(i)).sort((a,b)=>a.order-b.order),E:F,All:E}
}
function layout(V,E){
  const P=new Map(V.map(n=>[n.id,{n,id:n.id,w:0,h:0,r:0,x:0,ins:[],outs:[]}]));
  for(const n of V){const p=P.get(n.id);const a=tw(n.short,'600 12px system-ui'),b=n.title?Math.min(tw(n.title,'italic 11.5px Georgia'),190):0;p.w=Math.max(54,Math.max(a,b)+22);p.h=n.title&&n.fam!=='external'?38:26;p.t=n.title&&n.fam!=='external'?fitT(n.title,150):''}
  for(const e of E){P.get(e.s).outs.push(e.t);P.get(e.t).ins.push(e.s)}
  const state=new Map(),rank=new Map();
  const R=id=>{if(rank.has(id))return rank.get(id);if(state.get(id))return 0;state.set(id,1);const p=P.get(id);let r=0;for(const s of p.ins)r=Math.max(r,R(s)+1);rank.set(id,r);return r};
  for(const n of V)R(n.id);
  for(let it=0;it<2;it++)for(const n of[...V].sort((a,b)=>rank.get(b.id)-rank.get(a.id))){const p=P.get(n.id);if(!p.outs.length)continue;const up=Math.min(...p.outs.map(o=>rank.get(o)))-1;const lo=p.ins.length?Math.max(...p.ins.map(i=>rank.get(i)))+1:0;if(up>rank.get(n.id)&&up>=lo)rank.set(n.id,up)}
  const maxR=Math.max(0,...rank.values());
  const L=[];for(let r=0;r<=maxR;r++)L.push([]);
  for(const n of V){const p=P.get(n.id);p.r=rank.get(n.id);L[p.r].push(p)}
  const segs=[];let dn=0;
  for(const e of E){let a=P.get(e.s),b=P.get(e.t);if(b.r<=a.r){segs.push({e,pts:[a,b]});continue}const pts=[a];for(let r=a.r+1;r<b.r;r++){const d={id:'~'+(dn++),w:10,h:0,r,dummy:true,ins:[],outs:[]};L[r].push(d);pts.push(d)}pts.push(b);
    for(let i=0;i+1<pts.length;i++){pts[i].outs2=(pts[i].outs2||[]);pts[i].outs2.push(pts[i+1]);pts[i+1].ins2=(pts[i+1].ins2||[]);pts[i+1].ins2.push(pts[i])}segs.push({e,pts})}
  L.forEach(l=>l.forEach((p,i)=>p.o=i));
  const bc=(p,nb)=>{const xs=(nb||[]).map(q=>q.o);return xs.length?xs.reduce((a,b)=>a+b,0)/xs.length:p.o};
  for(let s=0;s<10;s++){const down=s%2===0;const order=down?[...L.keys()]:[...L.keys()].reverse();
    for(const r of order){const l=L[r];l.forEach(p=>p.b=bc(p,down?p.ins2:p.outs2));l.sort((a,b)=>a.b-b.b);l.forEach((p,i)=>p.o=i)}}
  const GAP=14,RH=70,box=$('#map').getBoundingClientRect(),cap=Math.max(4,Math.round(Math.sqrt(V.length)*1.15*Math.max(.75,Math.min(1.5,box.width/Math.max(box.height,1)/1.4))));
  const rows=[];for(let r=0;r<=maxR;r++){const l=L[r],k=Math.ceil(l.length/cap);if(k<=1){rows.push(l);continue}const sub=[];for(let j=0;j<k;j++)sub.push([]);l.forEach((p,i)=>sub[i%k].push(p));for(const sr of sub)rows.push(sr)}
  rows.forEach((l,ri)=>l.forEach((p,i)=>{p.o=i;p.row=ri}));
  L.length=0;for(const l of rows)L.push(l);
  for(const l of L){let x=0;for(const p of l){p.x=x+p.w/2;x+=p.w+GAP}}
  for(let it=0;it<24;it++){const down=it%2===0;
    for(const l of(down?L:[...L].reverse())){for(const p of l){const nb=[...(p.ins2||[]),...(p.outs2||[])];if(nb.length)p.want=nb.reduce((a,q)=>a+q.x,0)/nb.length;else p.want=p.x}
      for(let i=0;i<l.length;i++){const p=l[i];const minX=i?l[i-1].x+l[i-1].w/2+GAP+p.w/2:-1e9;p.x=Math.max(minX,(p.x+p.want)/2)}
      for(let i=l.length-2;i>=0;i--){const p=l[i],q=l[i+1];const maxX=q.x-q.w/2-GAP-p.w/2;if(p.x>maxX)p.x=Math.max(maxX,(i?l[i-1].x+l[i-1].w/2+GAP+p.w/2:-1e9))}}}
  const nr=L.length;L.forEach((l,ri)=>l.forEach(p=>p.y=(nr-1-ri)*RH));
  return{P,L,segs}
}
function fitT(t,max){if(tw(t,'italic 11.5px Georgia')<=max)return t;let s=t;while(s.length>4&&tw(s+'…','italic 11.5px Georgia')>max)s=s.slice(0,-1);return s+'…'}
let G=null,LY=null,drawn=false;
function draw(){
  G=graph();LY=layout(G.V,G.E);
  const eg=[],ng=[];
  for(const{e,pts}of LY.segs){
    const ps=pts.map((p,i)=>({x:p.x,y:i===0?p.y-p.h/2:i===pts.length-1?p.y+p.h/2+2:p.y}));
    let d=`M${ps[0].x},${ps[0].y}`;for(let i=1;i<ps.length;i++){const p=ps[i-1],q=ps[i],m=(p.y-q.y)/2;d+=` C${p.x},${p.y-m} ${q.x},${q.y+m} ${q.x},${q.y}`}
    const c=['e',e.via==='statement'?'st':'',e.basis==='cite'?'ci':'',e.hid?'hid':''].join(' ');
    eg.push(`<path class="${c}" data-s="${esc(e.s)}" data-t="${esc(e.t)}" d="${d}" marker-end="url(#arw)"></path>`)}
  for(const p of LY.P.values()){const n=p.n;const c=['n','k-'+n.kind,'f-'+n.fam,n.main?'main':''].join(' ');
    ng.push(`<g class="${c}" data-id="${esc(n.id)}" tabindex="0" role="button" aria-label="${esc(n.name+(n.title?' ('+n.title+')':''))}" transform="translate(${p.x},${p.y})"><title>${esc(n.name+(n.title?' — '+n.title:''))}</title><rect x="${-p.w/2}" y="${-p.h/2}" width="${p.w}" height="${p.h}" rx="${n.fam==='definition'?12:5}"></rect><text text-anchor="middle" y="${p.t?-3:4}">${esc(n.short)}</text>${p.t?`<text class="t" text-anchor="middle" y="12">${esc(p.t)}</text>`:''}</g>`)}
  $('#eg').innerHTML=eg.join('');$('#ng').innerHTML=ng.join('');
  fit(!drawn&&!S.focus);drawn=true;paint();
  const f=$('#focus');f.classList.toggle('on',!!S.focus);if(S.focus){const n=N.get(S.focus.id);$('#focus-t').textContent=(S.focus.dir==='up'?'What ':'What uses ')+n.short+(S.focus.dir==='up'?' rests on':'')+` · ${G.V.length} items`}
}
function bbox(){let a=1e9,b=1e9,c=-1e9,d=-1e9;for(const p of LY.P.values()){a=Math.min(a,p.x-p.w/2);c=Math.max(c,p.x+p.w/2);b=Math.min(b,p.y-p.h/2);d=Math.max(d,p.y+p.h/2)}return a>c?[0,0,1,1]:[a,b,c,d]}
function fit(first){const r=$('#map').getBoundingClientRect(),[a,b,c,d]=bbox(),pad=40;S.k=Math.min((r.width-pad*2)/(c-a||1),(r.height-pad*2-50)/(d-b||1),1.5);S.x=r.width/2-(a+c)/2*S.k;S.y=(r.height-50)/2-(b+d)/2*S.k;
  if(first&&S.k<.45){const ms=[...LY.P.values()].filter(p=>p.n.main);const pts=ms.length?ms:[...LY.P.values()].filter(p=>p.y<=b+80);const cx=pts.reduce((s,p)=>s+p.x,0)/pts.length,cy=Math.min(...pts.map(p=>p.y));S.k=.7;S.x=r.width/2-cx*S.k;S.y=90-cy*S.k}
  apply()}
function apply(){$('#vp').setAttribute('transform',`translate(${S.x},${S.y}) scale(${S.k})`)}
function zoom(f,cx,cy){const r=$('#map').getBoundingClientRect();cx??=r.width/2;cy??=r.height/2;const k=Math.max(.08,Math.min(4,S.k*f));S.x=cx-(cx-S.x)*k/S.k;S.y=cy-(cy-S.y)*k/S.k;S.k=k;apply()}
function centre(id){const p=LY&&LY.P.get(id);if(!p)return;const r=$('#map').getBoundingClientRect();if(S.k<.7)S.k=.9;S.x=r.width/2-p.x*S.k;S.y=r.height/2-p.y*S.k;apply()}
function setHash(){const h=S.focus&&S.focus.dir==='up'?'tree='+S.focus.id:(S.sel||'');try{history.replaceState(null,'',h?'#'+h:location.pathname+location.search)}catch(e){}}
function paint(){
  const sel=S.sel,dset=new Set(),uset=new Set();
  if(sel){for(const e of G.All){if(e.t===sel)dset.add(e.s);if(e.s===sel)uset.add(e.t)}}
  for(const g of document.querySelectorAll('#ng .n')){const id=g.dataset.id;g.classList.toggle('sel',id===sel);g.classList.toggle('dep',dset.has(id));g.classList.toggle('use',uset.has(id));g.classList.toggle('dim',!S.focus&&!!sel&&id!==sel&&!dset.has(id)&&!uset.has(id))}
  for(const p of document.querySelectorAll('#eg .e')){const s=p.dataset.s,t=p.dataset.t;const d=sel&&t===sel,u=sel&&s===sel;p.classList.toggle('dep',!!d);p.classList.toggle('use',!!u);p.classList.toggle('dim',!S.focus&&!!sel&&!d&&!u);p.setAttribute('marker-end',d?'url(#arw-d)':u?'url(#arw-u)':'url(#arw)')}
  panel();setHash();
}
function origin(n){return{proved:'Proved here',cited:'Quoted from the literature',stated:n.fam==='result'?'No proof here':'',external:'Cited, not proved here'}[n.origin]||''}
function chip(id,cls){const n=N.get(id);if(!n)return'';return`<button type="button" class="${cls}" data-go="${esc(id)}" title="${esc(n.name+(n.title?' — '+n.title:''))}">${esc(n.short)}</button>`}
function chipGroups(es,key,cls,stLabel,prLabel){if(!es.length)return'<div class="chips"><span class="none">nothing</span></div>';const st=es.filter(e=>e.via==='statement'),pr=es.filter(e=>e.via!=='statement');
  const row=(xs,l)=>xs.length?`${st.length&&pr.length?`<div class="via">${l}</div>`:''}<div class="chips">${xs.map(e=>chip(e[key],cls)).join('')}</div>`:'';return row(st,stLabel)+row(pr,prLabel)}
function panel(){
  const n=S.sel&&N.get(S.sel),el=$('#panel');
  if(!n){const m=mains.map(x=>chip(x.id,'')).join('')||'<span class="none">none</span>';
    el.innerHTML=`<h2>Reading the map</h2><p class="empty">Main results sit at the top, the statements they rest on below them. <b>Select a box</b> to read the statement: what it rests on turns blue, what uses it turns red. <b>Double-click</b> a box, or choose "Show what it rests on", to keep only its proof tree. Definitions and remarks are hidden until you tick them above.</p><h3>Main results</h3><div class="chips">${m}</div>`;return}
  const ds=(deps[n.id]||[]).filter(e=>N.get(e.s)),us=(users[n.id]||[]).filter(e=>N.get(e.t));
  const links=(n.links||[]).map(([t,h])=>`<a href="${esc(h)}">${esc(t)}</a>`).join('');
  el.innerHTML=`<h2>${esc(n.name)}${n.title?` <span style="font-weight:400;font-style:italic">(${esc(n.title)})</span>`:''}</h2>
  <p class="meta">${n.main?'<span class="badge m">Main result</span>':''}${origin(n)?`<span class="badge">${esc(origin(n))}</span>`:''}</p>
  ${links?`<p class="links">${links}</p>`:''}
  <div class="stmt">${n.html||''}</div>
  <div style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap"><button class="btn" type="button" id="f-up">Show what it rests on</button><button class="btn" type="button" id="f-dn">Show what uses it</button></div>
  <h3>Rests on (${ds.length})</h3>${chipGroups(ds,'s','','In the statement','In the proof')}
  <h3>Used by (${us.length})</h3>${chipGroups(us,'t','u','In their statements','In their proofs')}
  ${n.proof?`<details><summary>Proof</summary><div class="proof">${n.proof}</div></details>`:''}`;
  $('#f-up').onclick=()=>{S.focus={id:n.id,dir:'up'};draw()};$('#f-dn').onclick=()=>{S.focus={id:n.id,dir:'down'};draw()};
  if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([el]).catch(()=>{});
}
function select(id,c){S.sel=id;if(id&&!LY.P.has(id)){S.focus=null;const n=N.get(id);if(n.fam==='definition'){S.def=true;$('#t-def').checked=true}if(n.fam==='aside'){S.aside=true;$('#t-aside').checked=true}if(n.fam==='external'){S.ext=true;$('#t-ext').checked=true}draw()}paint();if(c)centre(id)}
function fromHash(){let h='';try{h=decodeURIComponent(location.hash.slice(1))}catch(e){}const m=h.match(/^tree=(.+)$/),id=m?m[1]:h;if(!id||!N.has(id))return false;const n=N.get(id);
  if(n.fam==='definition'){S.def=true;$('#t-def').checked=true}if(n.fam==='aside'){S.aside=true;$('#t-aside').checked=true}
  if(m){S.focus={id,dir:'up'};S.sel=id;draw()}else{S.focus=null;draw();select(id,true)}return true}
const svg=$('#svg');let drag=null,lastNode=null;
svg.addEventListener('pointerdown',ev=>{const g=ev.target.closest('.n');lastNode=g?g.dataset.id:null;drag={x:ev.clientX,y:ev.clientY,sx:S.x,sy:S.y,moved:false,node:lastNode,pid:ev.pointerId}});
svg.addEventListener('pointermove',ev=>{if(!drag)return;const dx=ev.clientX-drag.x,dy=ev.clientY-drag.y;if(!drag.moved&&Math.abs(dx)+Math.abs(dy)>4){drag.moved=true;svg.classList.add('drag');try{svg.setPointerCapture(drag.pid)}catch(e){}}if(drag.moved){S.x=drag.sx+dx;S.y=drag.sy+dy;apply()}});
svg.addEventListener('pointerup',ev=>{if(drag&&!drag.moved){if(drag.node)select(drag.node);else select(null)}drag=null;svg.classList.remove('drag')});
svg.addEventListener('dblclick',ev=>{const id=(ev.target.closest&&ev.target.closest('.n')||{dataset:{}}).dataset.id||lastNode;if(id){S.focus={id,dir:'up'};S.sel=id;draw()}});
svg.addEventListener('wheel',ev=>{ev.preventDefault();const r=svg.getBoundingClientRect();zoom(Math.exp(-ev.deltaY*.0015),ev.clientX-r.left,ev.clientY-r.top)},{passive:false});
svg.addEventListener('keydown',ev=>{const g=ev.target.closest&&ev.target.closest('.n');if(g&&(ev.key==='Enter'||ev.key===' ')){ev.preventDefault();select(g.dataset.id)}});
document.addEventListener('keydown',ev=>{if(ev.target.tagName==='INPUT')return;if(ev.key==='Escape'){S.sel=null;paint()}if(ev.key==='+'||ev.key==='=')zoom(1.25);if(ev.key==='-')zoom(.8);if(ev.key==='f')fit()});
$('#zi').onclick=()=>zoom(1.25);$('#zo').onclick=()=>zoom(.8);$('#zf').onclick=()=>fit();
$('#unfocus').onclick=()=>{S.focus=null;draw()};
for(const[id,key]of[['#t-def','def'],['#t-aside','aside'],['#t-ext','ext'],['#t-all','all']])$(id).onchange=e=>{S[key]=e.target.checked;draw()};
document.addEventListener('click',ev=>{const b=ev.target.closest('[data-go],a.ref[data-id]');if(!b)return;ev.preventDefault();select(b.dataset.go||b.dataset.id,true)});
const q=$('#q');const hits=()=>{const s=q.value.trim().toLowerCase();return s?D.nodes.filter(n=>(n.name+' '+n.short+' '+(n.title||'')+' '+n.id).toLowerCase().includes(s)):[]};
q.oninput=()=>{const h=new Set(hits().map(n=>n.id));for(const g of document.querySelectorAll('#ng .n'))g.classList.toggle('hit',h.has(g.dataset.id))};
q.onkeydown=ev=>{if(ev.key==='Enter'){const h=hits();if(h.length)select(h[0].id,true)}};
function below(){
  const ext=D.nodes.filter(n=>n.fam==='external');
  $('#below').innerHTML=`<div><h3>Results of other works that the proofs rely on (${ext.length})</h3><div class="chips">${ext.map(n=>chip(n.id,'')).join('')||'<span class="none">none</span>'}</div></div>`+
   `<div><h3>How this page is made</h3><p>Each statement lists what it uses with <code>\\uses</code> in the LaTeX sources, in its statement or in its proof. The build reads these lists, and the citations with a precise locator, at every update of the encyclopaedia. The same data give the proof tree on each <a href="../latex/">tag page</a> and the <a href="../latex/graph.html">dependency graph</a>.</p></div>`;
}
let lastW=0;new ResizeObserver(()=>{const w=$('#map').getBoundingClientRect().width;if(LY&&Math.abs(w-lastW)>40){lastW=w;fit(true)}}).observe($('#map'));
draw();below();if(!fromHash())panel();
window.addEventListener('hashchange',fromHash);
}</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" async></script>
</body></html>'''
