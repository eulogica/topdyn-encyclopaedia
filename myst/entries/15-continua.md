(sec-continua)=
# Homeomorphism groups of continua

For connected spaces the flow of all maximal chains is not minimal. For the
interval, the circle and the Lelek fan, the universal minimal flow of the
homeomorphism group can be realised as a flow of connected chains, while for
manifolds of dimension at least two it is not metrizable. A *continuum* is a compact connected metrizable space;
homeomorphism groups of compact metrizable spaces carry the compact-open
topology, which is the topology of uniform convergence.

:::{prf:remark} The interval and the circle
:label: rem-interval-circle

The group $\mathrm{Homeo}_+[0,1]$ is extremely amenable, and
$M(\mathrm{Homeo}_+(\mathbb{S}^1))$ is the circle ([](#sec-pestov)).
:::

:::{prf:definition} The Lelek fan
:label: def-lelek-fan

Let $C$ be the Cantor set. The *Cantor fan* is the quotient of
$C\times[0,1]$ obtained by collapsing $C\times\{0\}$ to a point $v$, the
*top* of the fan. A point $x$ of a continuum $X$ is an *endpoint* if
$x\in\{h(0),h(1)\}$ for every embedding $h\colon[0,1]\to X$ whose image
contains $x$. The *Lelek fan* $L$ is the unique subcontinuum of the
Cantor fan with more than one point whose endpoints are dense in it
{cite}`BartosovaKwiatkowska2019`.
:::

:::{figure} ../../figures/lelek-fan.svg
:name: fig-lelek-fan
:figclass: enc-figure
:alt: The Cantor fan, drawn with finitely many blades from its top v, and a fan whose blades have different lengths, with their endpoints marked
:width: 100%

Schematic pictures of {prf:ref}`def-lelek-fan`, with finitely many blades. (a) The Cantor fan: each segment is the image of $\{c\}\times[0,1]$ for a point $c$ of $C$, and $C\times\{0\}$ is collapsed to the top $v$. (b) A subcontinuum of the Cantor fan whose blades have different lengths; the dots are its endpoints. In the Lelek fan $L$ the endpoints are dense, which no picture with finitely many blades can show.
:::

:::{prf:theorem} {cite:t}`BartosovaKwiatkowska2019`
:label: thm-lelek

Let $Y^*\subseteq\Phi(L)$ be the set of connected maximal chains in the Lelek
fan $L$ all of whose members contain the top $v$. Then $Y^*$ is a subflow of
$\Phi(L)$, and the universal minimal flow of $\mathrm{Homeo}(L)$ is $Y^*$. In
particular it is metrizable.
:::

:::{prf:remark} Method
:label: rem-lelek-method

Bartošová and Kwiatkowska show that the stabiliser $H$ of a generic chain in
$Y^*$ is extremely amenable and co-precompact, and that the universal minimal
flow is the completion of $\mathrm{Homeo}(L)/H$; compare
{prf:ref}`prop-coprecompact-ea`. They realise $L$ as a quotient of a
projective Fraïssé limit, compute the universal minimal flow of its
automorphism group with the methods of Kechris, Pestov and Todorcevic and a
new Ramsey theorem proved with the dual Ramsey theorem, and then pass from the
projective limit to $L$ {cite}`BartosovaKwiatkowska2019`.
:::

:::{prf:definition} Generalised Ważewski dendrites
:label: def-wazewski

A *dendrite* is a locally connected continuum containing no simple
closed curve. The *order* of a point $x$ is the number of connected
components of $X\setminus\{x\}$, and $x$ is a *ramification point* if its
order is at least $3$. For $P\subseteq\{3,4,\dots,\omega\}$, a
*generalised Ważewski dendrite* $W_P$ is a dendrite in which every
ramification point has order in $P$ and, for every $p\in P$, every arc contains
a ramification point of order $p$. It is unique up to homeomorphism; see
{cite}`Kwiatkowska2018`.
:::

:::{figure} ../../figures/wazewski-dendrites.svg
:name: fig-wazewski-dendrites
:figclass: enc-figure
:alt: The first stages of two generalised Wazewski dendrites: one with ramification points of order 3, one with ramification points of orders 3 and 4
:width: 100%

Schematic pictures of the first stages of two generalised Ważewski dendrites ({prf:ref}`def-wazewski`): (a) $W_{\{3\}}$, in which every ramification point has order $3$; (b) $W_{\{3,4\}}$, with ramification points of order $3$ (circles) and of order $4$ (squares). Only the first ramification points are marked. In $W_P$ every arc contains a ramification point of order $p$ for every $p\in P$, which a picture with finitely many branches can only suggest.
:::

:::{prf:theorem} {cite:t}`Kwiatkowska2018`
:label: thm-wazewski

Let $P\subseteq\{3,4,\dots,\omega\}$ be nonempty.

1. If $P$ is finite, the universal minimal flow of $\mathrm{Homeo}(W_P)$ is
   metrizable, and it is computed explicitly. This answers a question of
   Duchesne.
2. If $P$ is infinite, the universal minimal flow of $\mathrm{Homeo}(W_P)$
   is not metrizable. These groups are Roelcke precompact, and their universal
   minimal flows have a comeagre orbit.

:::

:::{prf:remark}
:label: rem-wazewski

By {prf:ref}`thm-bymt`, a metrizable universal minimal flow of a Polish
group has a comeagre orbit. Part (2) shows that the converse fails
{cite}`GutmanTsankovZucker2021`. Kwiatkowska works with an identification,
which follows from work of Duchesne and Monod, of $\mathrm{Homeo}(W_P)$ with
the automorphism group of a countable structure whose universe is the set of
ramification points of $W_P$ {cite}`Kwiatkowska2018`.
:::

:::{prf:theorem} {cite:t}`GutmanTsankovZucker2021`
:label: thm-gtz

Let $X$ be a closed manifold of dimension at least $2$, or the Hilbert cube.
Then the universal minimal flow of $\mathrm{Homeo}(X)$ is not metrizable. If
$X$ is a closed manifold of dimension at least $3$, the connected maximal
chains in $X$ form a minimal $\mathrm{Homeo}(X)$-flow all of whose orbits are
meagre.
:::

:::{prf:remark}
:label: rem-gtz

This answers a question of Uspenskij (Question 1.2 of {cite}`Uspenskij2000`).
As explained in
{cite}`GutmanTsankovZucker2021`, {prf:ref}`thm-bymt` implies that if the
universal minimal flow of a Polish group $G$ is metrizable, then every minimal
$G$-flow is metrizable and has a comeagre orbit. So a single metrizable minimal
flow with meagre orbits shows that $M(G)$ is not metrizable.
:::

:::{prf:remark} The pseudo-arc
:label: rem-pseudo-arc

Uspenskij asked whether the universal minimal flow of the homeomorphism group
of the pseudo-arc $\mathbf{P}$ can be identified with $\mathbf{P}$
(Question 1.3 of {cite}`Uspenskij2000`). The subcontinua of $\mathbf{P}$
containing a point $p$ form a maximal chain fixed by the stabiliser of $p$, so
the argument of {prf:ref}`thm-uspenskij-chains` does not rule this out
(Remark 2.4 of {cite}`Uspenskij2000`). Gutman, Tsankov and Zucker also ask
whether this universal minimal flow is metrizable, and note that, since
$\mathbf{P}$ is hereditarily indecomposable, its space of connected maximal
chains is isomorphic to $\mathbf{P}$ itself {cite}`GutmanTsankovZucker2021`.
The question was still open when {cite}`BartosovaKwiatkowska2019` and
{cite}`GutmanTsankovZucker2021` were written.
:::
