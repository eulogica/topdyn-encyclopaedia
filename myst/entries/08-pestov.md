(sec-pestov)=
# Pestov's theorems

Pestov found the first extremely amenable groups of homeomorphisms and
automorphisms, and with them the first nontrivial universal minimal flow
computed explicitly for a non-locally compact group.

:::{prf:theorem} {cite:t}`Pestov1998`
:label: thm-pestov-ea

The group $\mathrm{Aut}(\mathbb{Q},<)$ of order-preserving bijections of the
rationals, with the topology of pointwise convergence, and the group
$\mathrm{Homeo}_+[0,1]$ of orientation-preserving homeomorphisms of the unit
interval, with the compact-open topology, are extremely amenable
({prf:ref}`def-ea`).
:::

:::{prf:remark}
:label: rem-pestov-ramsey

Extreme amenability of $\mathrm{Aut}(\mathbb{Q},<)$ is a consequence of the
finite Ramsey theorem. This is the prototype of the
Kechris–Pestov–Todorcevic correspondence of [](#sec-kpt).
:::

:::{prf:theorem} {cite:t}`Pestov1998`
:label: thm-pestov-circle

The universal minimal flow of $\mathrm{Homeo}_+(\mathbb{S}^1)$ is the circle
$\mathbb{S}^1$ with the natural action.
:::

:::{prf:proof}
*Idea.* The stabiliser of a point $\theta\in\mathbb{S}^1$ is isomorphic to
$\mathrm{Homeo}_+[0,1]$, hence extremely amenable by
{prf:ref}`thm-pestov-ea`. If $X$ is a $\mathrm{Homeo}_+(\mathbb{S}^1)$-flow,
the stabiliser therefore fixes a point $x'\in X$, and one checks that
$g\theta\mapsto gx'$ is a well-defined continuous $G$-map
$\mathbb{S}^1\to X$. Since $\mathbb{S}^1$ is minimal, it maps onto every
minimal flow.
:::

:::{figure} ../../figures/pestov-circle.svg
:name: fig-pestov-circle
:figclass: enc-figure
:alt: The circle cut at a point theta becomes an interval, and the map from the circle to a flow X sending g theta to g x'
:width: 100%

The idea of the proof of {prf:ref}`thm-pestov-circle`. (a) Cutting the circle at $\theta$ turns the orientation-preserving homeomorphisms that fix $\theta$ into the increasing homeomorphisms of an interval, so the stabiliser of $\theta$ is isomorphic to $\mathrm{Homeo}_+[0,1]$. (b) The stabiliser fixes a point $x'$ of a flow $X$, and $g\theta\mapsto gx'$ is a $G$-map $\mathbb{S}^1\to X$. Since $\mathbb{S}^1$ is minimal, it maps onto every minimal flow.
:::

:::{prf:remark} Uspenskij
:label: rem-uspenskij

Uspenskij showed that the circle cannot be replaced here by the Hilbert cube
or by a compact manifold of dimension greater than one, answering a question
of Pestov, and that the action of a topological group on its universal minimal
flow is never 3-transitive {cite}`Uspenskij2000`.
:::
