(sec-glasner-weiss)=
# The universal minimal flow of $S_\infty$

The group of all permutations of the integers has a metrizable, explicitly
described universal minimal flow: the space of linear orders.

:::{prf:definition} The flow of linear orders
:label: def-lo

Let $S_\infty$ be the group of all permutations of $\mathbb{N}$, with the
topology of pointwise convergence. Let $\mathrm{LO}(\mathbb{N})$ be the set of
linear orders on $\mathbb{N}$, viewed as a closed, hence compact, subset of
$\{0,1\}^{\mathbb{N}\times\mathbb{N}}$. The group $S_\infty$ acts on
$\mathrm{LO}(\mathbb{N})$ by transporting orders: $a\mathrel{(g\cdot{<})}b$ if
and only if $g^{-1}(a)<g^{-1}(b)$. This makes $\mathrm{LO}(\mathbb{N})$ an
$S_\infty$-flow.
:::

:::{figure} ../../figures/transported-order.svg
:name: fig-transported-order
:figclass: enc-figure
:alt: A linear order on the numbers 1 to 6, listed from least to greatest, and the order transported by a permutation g, which lists g(a) where the first order lists a
:width: 100%

{prf:ref}`def-lo`: a linear order $<$ on $\mathbb{N}$, restricted to $\{1,\dots,6\}$ and listed from least to greatest, a permutation $g\in S_\infty$ that permutes $\{1,\dots,6\}$ and fixes every other number, and the transported order $g\cdot{<}$. Since $a\mathrel{(g\cdot{<})}b$ if and only if $g^{-1}(a)<g^{-1}(b)$, the order $g\cdot{<}$ lists $g(a)$ where $<$ lists $a$.
:::

:::{prf:theorem} {cite:t}`GlasnerWeiss2002`
:label: thm-glasner-weiss

The universal minimal flow of $S_\infty$ is $\mathrm{LO}(\mathbb{N})$.
:::

:::{prf:remark}
:label: rem-glasner-weiss

Glasner and Weiss also showed that this flow is uniquely ergodic
{cite}`GlasnerWeiss2002`. A short modern proof derives the theorem from
extreme amenability of $\mathrm{Aut}(\mathbb{Q},<)$; see
{prf:ref}`ex-lo-coprecompact`.
:::
