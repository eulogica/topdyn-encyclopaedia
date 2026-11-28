(sec-gromov-milman)=
# The Gromov–Milman theorem

The first natural example of an extremely amenable group came from asymptotic
geometric analysis: concentration of measure on high-dimensional spheres and
groups forces fixed points.

:::{prf:theorem} {cite:t}`GromovMilman1983`
:label: thm-gromov-milman

The unitary group $U(\ell^2)$ of an infinite-dimensional separable Hilbert
space, with the strong operator topology, is extremely amenable
({prf:ref}`def-ea`).
:::

:::{prf:remark} Lévy groups
:label: rem-levy

The proof shows that $U(\ell^2)$ is a *Lévy group*: roughly, it contains an
increasing chain of compact subgroups with dense union whose Haar measures
concentrate, in the sense of Lévy's concentration of measure phenomenon.
In {cite}`GromovMilman1983` the fixed point theorem is stated for increasing
unions of compact groups whose normalised Haar measures form a Lévy family,
acting equicontinuously on a compact space (Theorem 7.1 there), and it is
applied to the union of the groups $SO(n)$, to the group of finitary
permutations of $\mathbb{N}$ and to the union of the groups
$(\mathbb{Z}/2\mathbb{Z})^n$. Glasner observed that equicontinuity is not
needed {cite}`Glasner1998`, so every Lévy group is extremely amenable.
{prf:ref}`thm-gromov-milman` is the form in which the result is usually
quoted {cite}`Uspenskij2000,GiordanoPestov2007`. This mechanism, which Pestov
calls the Ramsey–Dvoretzky–Milman phenomenon, gives many further examples
{cite}`Pestov2006`.
:::

:::{prf:remark} Concentration on spheres
:label: rem-sphere-concentration

A metric space $(X,d)$ with a Borel probability measure $\mu$ is an
*mm-space*. For $A\subseteq X$ and $\varepsilon>0$, let $A_\varepsilon$ be the
$\varepsilon$-neighbourhood of $A$. The *concentration function* of $X$ is

$$
\alpha_X(\varepsilon)=1-\inf\{\mu(A_\varepsilon): A\subseteq X\text{ Borel},\
\mu(A)\geq\tfrac12\}\qquad(\varepsilon>0),
$$

and a sequence of mm-spaces $X_n$ is a *Lévy family* if
$\alpha_{X_n}(\varepsilon)\to0$ for every $\varepsilon>0$. The model example is
the sequence of unit spheres $\mathbb{S}^n\subseteq\mathbb{R}^{n+1}$, with the
geodesic distance and the rotation-invariant probability measures. Pestov
attributes this to Paul Lévy, whose proof, based on the isoperimetric
inequality, was made rigorous by Gromov (Definitions 2 and 3 and Example 1 of
{cite}`PestovMM2002`). Since a hemisphere $H$ of $\mathbb{S}^n$ has measure
$\frac12$, the measure of $H_\varepsilon$ tends to $1$ as $n\to\infty$. Applied
to the two hemispheres bounded by an equator, this shows that for large $n$
almost all of the measure of $\mathbb{S}^n$ lies within $\varepsilon$ of the
equator.
:::

:::{figure} ../../figures/sphere-concentration.svg
:name: fig-sphere-concentration
:figclass: enc-figure
:alt: A hemisphere of the sphere and its epsilon-neighbourhood, and the distribution of the latitude of a random point of the n-sphere for n = 2, 10 and 100
:width: 100%

{prf:ref}`rem-sphere-concentration`. (a) A hemisphere $H$ of $\mathbb{S}^n$ and its $\varepsilon$-neighbourhood $H_\varepsilon$ in the geodesic distance. (b) The distribution of the latitude of a random point of $\mathbb{S}^n$, its geodesic distance from the equator taken with a sign, for $n=2$, $10$ and $100$; the three curves enclose the same area. As $n$ grows, almost all of the measure lies within $\varepsilon$ of the equator.
:::
