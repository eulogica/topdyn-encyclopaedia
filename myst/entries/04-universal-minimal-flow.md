(sec-umf)=
# The universal minimal flow

Every topological group has a canonical minimal flow that maps onto all
others. Computing it, or deciding whether it is trivial or metrizable, is one
of the central problems of the subject.

:::{prf:definition} Universal minimal flow
:label: def-umf

A minimal $G$-flow $M$ ({prf:ref}`def-minimal`) is *universal* if every
minimal $G$-flow is a factor of $M$.
:::

:::{prf:theorem} Ellis {cite}`Ellis1960`
:label: thm-ellis

Every topological group $G$ has a universal minimal flow, and any two
universal minimal flows of $G$ are isomorphic. It is denoted $M(G)$.
:::

:::{prf:proof}
*Existence.* By {prf:ref}`prop-minimal-subflow`, $S(G)$ contains a minimal
subflow $M$. Let $Y$ be a minimal $G$-flow and $y\in Y$. Then $(Y,y)$ is an
ambit, so {prf:ref}`prop-greatest-ambit` gives a $G$-map
$\pi\colon S(G)\to Y$. The image $\pi(M)$ is a subflow of $Y$, so $\pi(M)=Y$
by minimality. Uniqueness is the subtle part; see {cite}`Ellis1960`, and
{cite}`GutmanLi2013` for a short proof.
:::

:::{prf:corollary}
:label: cor-umf-in-ambit

Every minimal subflow of the greatest ambit $S(G)$ is isomorphic to $M(G)$.
:::

:::{prf:example}
:label: ex-umf-compact

If $G$ is compact, then $M(G)$ is $G$ acting on itself by left translation.
Indeed, this flow is minimal, and for a minimal $G$-flow $Y$ and $y\in Y$ the
map $g\mapsto gy$ is a $G$-map onto the orbit $Gy$, which is compact and dense,
hence equal to $Y$.
:::

:::{prf:remark} Ellis's problem
:label: rem-ellis-problem

The greatest ambit maps canonically onto the enveloping (Ellis) semigroup
$E(M(G))$ of the universal minimal flow. Ellis asked, in his 1969 *Lectures on
Topological Dynamics*, whether this map is always an isomorphism. Pestov
observed that every nontrivial extremely amenable group ([](#sec-ea)) answers
this in the negative, since its universal minimal flow, and hence its
enveloping semigroup, is trivial {cite}`Pestov1998`.
:::
