(sec-ea)=
# Extreme amenability

The simplest possible universal minimal flow is a single point. Groups with
this property are far from locally compact, and they arise from concentration
of measure and from structural Ramsey theory.

:::{prf:definition} Extremely amenable group
:label: def-ea

A topological group $G$ is *extremely amenable* if every $G$-flow has a fixed
point, that is, a point $x$ with $gx=x$ for all $g\in G$. This is also called
the *fixed point on compacta property*.
:::

:::{prf:proposition}
:label: prop-ea-trivial-umf

A topological group $G$ is extremely amenable if and only if $M(G)$
({prf:ref}`thm-ellis`) is a single point.
:::

:::{prf:proof}
If $G$ is extremely amenable, a fixed point of $M(G)$ is a subflow, so $M(G)$
is a point by minimality. Conversely, if $M(G)$ is a point, let $X$ be a
$G$-flow. By {prf:ref}`prop-minimal-subflow` it contains a minimal subflow
$Y$, which is a factor of $M(G)$ and hence a single fixed point.
:::

:::{prf:remark}
:label: rem-ea-amenable

A topological group is *amenable* if every $G$-flow carries a $G$-invariant
regular Borel probability measure. Extremely amenable groups are amenable: the
Dirac measure at a fixed point is invariant.
:::

:::{prf:remark} The first examples
:label: rem-herer-christensen

Historically, the first extremely amenable groups were the groups
$L^0(\varphi,\mathbb{R})$ of Herer and Christensen
{cite}`HererChristensen1975`, built from a pathological submeasure $\varphi$.
They have no nontrivial continuous unitary representations; being abelian,
they are amenable, and together the two properties make them extremely
amenable. Natural examples came later: see [](#sec-gromov-milman),
[](#sec-pestov) and [](#sec-kpt), and the monograph {cite}`Pestov2006`.
:::
