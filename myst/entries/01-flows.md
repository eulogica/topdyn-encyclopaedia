(sec-flows)=
# Flows

Abstract topological dynamics studies continuous actions of topological groups
on compact spaces. The basic objects and morphisms are the following.

:::{prf:definition} Flow
:label: def-flow

Let $G$ be a topological group. A *$G$-flow* is a compact space $X$ together
with a continuous action $G\times X\to X$, $(g,x)\mapsto gx$. If $X$ and $Y$
are $G$-flows, a *$G$-map* is a continuous map $\varphi\colon X\to Y$ such
that $\varphi(gx)=g\varphi(x)$ for all $g\in G$ and $x\in X$. A *subflow* of
$X$ is a nonempty closed $G$-invariant subset of $X$. A $G$-flow $Y$ is a
*factor* of $X$ if there is a surjective $G$-map $X\to Y$, and $X$ and $Y$ are
*isomorphic* if there is a bijective $G$-map $X\to Y$.
:::

:::{prf:remark}
:label: rem-flow-terminology

By compactness, the inverse of a bijective $G$-map is continuous, so
isomorphic flows are isomorphic in every reasonable sense. Flows are also
called compact $G$-spaces, $G$-systems or dynamical systems in the literature.
:::

:::{prf:example}
:label: ex-flows

1. A compact group $G$ acting on itself by left translation.
2. A $\mathbb{Z}$-flow is the same thing as a compact space together with a
   homeomorphism $T$, the action being $(n,x)\mapsto T^n x$.
3. The group $\mathrm{Homeo}_+(\mathbb{S}^1)$ of orientation-preserving
   homeomorphisms of the circle, with the compact-open topology, acting on
   $\mathbb{S}^1$; see [](#sec-pestov).
4. The group $S_\infty$ of all permutations of $\mathbb{N}$ acting on the space
   of linear orders on $\mathbb{N}$; see [](#sec-glasner-weiss).
:::
