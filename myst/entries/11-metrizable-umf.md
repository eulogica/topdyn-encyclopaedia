(sec-metrizable)=
# Metrizable universal minimal flows

For Polish groups, a metrizable universal minimal flow is always of a very
concrete form: the completion of a homogeneous space by an extremely amenable
subgroup.

:::{prf:definition} Co-precompact subgroups
:label: def-coprecompact

Let $H$ be a closed subgroup of $G$. Equip $G/H$ with the uniformity whose
basic entourages are the sets $\{(gH,vgH) : g\in G,\ v\in V\}$, for $V$ a
neighbourhood of the identity, and let $\widehat{G/H}$ be its completion. The
subgroup $H$ is *co-precompact* if $\widehat{G/H}$ is compact. In that case
the action of $G$ on $G/H$ extends to $\widehat{G/H}$, which becomes a
$G$-flow.
:::

:::{prf:proposition}
:label: prop-coprecompact-ea

If $H\leq G$ is closed, co-precompact and extremely amenable, then every
minimal subflow of $\widehat{G/H}$ is isomorphic to $M(G)$.
:::

:::{prf:proof}
Let $X$ be a minimal $G$-flow. Since $H$ is extremely amenable
({prf:ref}`def-ea`), it fixes a point $x_0\in X$. The map $gH\mapsto gx_0$ is
well defined and uniformly continuous, so it extends to a $G$-map
$\widehat{G/H}\to X$, which maps every minimal subflow onto $X$. Thus every
minimal subflow of $\widehat{G/H}$ is a universal minimal flow, and
{prf:ref}`thm-ellis` identifies it with $M(G)$.
:::

:::{figure} ../../figures/completion-pattern.svg
:name: fig-completion-pattern
:figclass: enc-figure
:alt: From G to its quotient by H and the completion, and from both onto a minimal flow X
:width: 100%

The argument of {prf:ref}`prop-coprecompact-ea`. The extremely amenable subgroup $H$ fixes a point $x_0$ of a minimal flow $X$. The map $gH\mapsto gx_0$ is uniformly continuous, so it extends to a $G$-map from the completion $\widehat{G/H}$ to $X$. The image of every minimal subflow of $\widehat{G/H}$ is closed and invariant, hence all of $X$. Several other proofs use the same argument; their links name this figure.
:::

:::{prf:example}
:label: ex-lo-coprecompact

Identify $\mathbb{N}$ with $\mathbb{Q}$. Then $H=\mathrm{Aut}(\mathbb{Q},<)$ is
a closed, co-precompact, extremely amenable subgroup of $S_\infty$
({prf:ref}`thm-pestov-ea`), and $\widehat{S_\infty/H}$ is
$\mathrm{LO}(\mathbb{N})$, which is minimal. This recovers
{prf:ref}`thm-glasner-weiss`.
:::

:::{prf:theorem} {cite:t}`MNT2016`
:label: thm-mnt

Let $G$ be a Polish group. If $M(G)$ is metrizable and contains a $G_\delta$
orbit $Gx_0$, then the stabiliser $G_{x_0}$ is closed, co-precompact and
extremely amenable, and $M(G)$ is isomorphic to $\widehat{G/G_{x_0}}$.
:::

:::{prf:theorem} {cite:t}`BYMT2017`
:label: thm-bymt

Let $G$ be a Polish group with metrizable universal minimal flow. Then $M(G)$
has a comeagre orbit. Consequently, there is a closed, co-precompact,
extremely amenable subgroup $G^*\leq G$ such that
$M(G)\cong\widehat{G/G^*}$.
:::

:::{prf:remark} Zucker
:label: rem-zucker

For closed subgroups of $S_\infty$, Zucker had earlier characterised
combinatorially when $M(G)$ is metrizable, and showed that in that case every
minimal $G$-flow has a point with comeagre orbit, solving the Generic Point
Problem of Angel, Kechris and Lyons for these groups {cite}`Zucker2016`. He
later gave a direct proof of {prf:ref}`thm-bymt` {cite}`Zucker2018`.
:::
