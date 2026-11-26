(sec-maps-transformations)=
# Groups of maps and of measure-space transformations

Two elementary principles compute many universal minimal flows: a group
that is dense in a compact group has that compact group as its universal
minimal flow, and a closed normal extremely amenable subgroup can be divided
out. The computations in this section, apart from
{prf:ref}`prop-ea-normal`, are taken from a preprint of the editor
posted on Zenodo {cite}`LupiniPointwise2026`; it has not been refereed.

:::{prf:proposition}
:label: prop-ea-normal

Let $N$ be a closed normal subgroup of a topological group $G$.

1. If $N$ is extremely amenable, then $N$ acts trivially on every minimal
   $G$-flow, and $M(G)$ is $M(G/N)$ with $G$ acting through the quotient map.
2. If $G$ is a dense subgroup of a compact group $Q$, with the induced
   topology, then $M(G)$ is $Q$ with $G$ acting by left translation.

:::

:::{prf:proof}
(1) In a minimal $G$-flow $X$, the set of $N$-fixed points is nonempty by
extreme amenability, closed, and $G$-invariant because $N$ is normal, so it
is all of $X$. The action of $G$ therefore factors through $G/N$, and the
factored action is continuous because the quotient map $G\to G/N$ is open.
Thus minimal $G$-flows and minimal $G/N$-flows are the same. (2) The right
uniform structure of $G$ is the one induced by the unique uniform structure
of $Q$, so every bounded right uniformly continuous function on $G$ extends
uniquely to a continuous function on $Q$. Hence $S(G)=Q$, which is a minimal
$G$-flow because $G$ is dense, and {prf:ref}`cor-umf-in-ambit` gives
$M(G)=Q$. See also Lemma 2.1 of {cite}`LupiniPointwise2026`.
:::

:::{prf:theorem} {cite:t}`LupiniPointwise2026`
:label: thm-lupini-cp

Let $X$ be a Tychonoff space and $K$ a compact path-connected topological
group, and let $C_p(X,K)$ be the group of continuous maps $X\to K$, with
pointwise multiplication and the topology of pointwise convergence. Then
$M(C_p(X,K))\cong K^X$, with $C_p(X,K)$ acting by left translation.
:::

:::{prf:remark}
:label: rem-lupini-cp

Continuous maps can take any finitely many prescribed values, so
$C_p(X,K)$ is dense in $K^X$ and {prf:ref}`prop-ea-normal` applies.
The same argument computes, for the pointwise topology, the universal
minimal flows of path, loop and gauge groups of compact Lie groups, and of
groups of Lipschitz, Hölder, real-analytic and holomorphic maps. In the finer
natural topologies of path and loop groups the same compact group is still a
factor of the universal minimal flow, which is therefore not metrizable when
the target group has nontrivial identity component
(Section 2 of {cite}`LupiniPointwise2026`).
:::

:::{prf:theorem} {cite:t}`LupiniPointwise2026`
:label: thm-lupini-aut-measure

Let $(Y,\mu)$ be a standard probability space, let $A_\mu$ be its at most
countable set of atoms, let $R_\mu=\{\mu(\{a\}) : a\in A_\mu\}$, and for
$r\in R_\mu$ let $A_r$ be the finite set of atoms of mass $r$. With the weak
topologies,

$$
\begin{gathered}
M(\mathrm{Aut}(Y,\mu))\cong\prod_{r\in R_\mu}\mathrm{Sym}(A_r),\\
M(\mathrm{Aut}^*(Y,\mu))\cong\mathrm{LO}(A_\mu),
\end{gathered}
$$

where $\mathrm{Aut}(Y,\mu)$ is the group of measure-preserving automorphisms,
$\mathrm{Aut}^*(Y,\mu)$ is the group of nonsingular automorphisms, and
$\mathrm{LO}(A_\mu)$ is the space of linear orders on $A_\mu$.
:::

:::{prf:remark}
:label: rem-lupini-aut-measure

Both groups split as the product of the corresponding group of the atomless
part, which is extremely amenable by Giordano and Pestov, and a permutation
group of the atoms; {prf:ref}`prop-ea-normal` and
{prf:ref}`thm-glasner-weiss` do the rest. The same decomposition gives the
universal minimal flows of measurable wreath products, of full groups of
measured equivalence relations whose atomless part has an extremely amenable
full group, which are products of spaces of linear orders over the atomic
classes, and of automorphism groups of von Neumann algebras such as the
hyperfinite factors (Sections 4 and 5 of {cite}`LupiniPointwise2026`).
:::

:::{prf:theorem} {cite:t}`LupiniPointwise2026`
:label: thm-lupini-lp

Let $(Y,\mu)$ be a standard probability space with set of atoms $A_\mu$, let
$\mathbb{F}$ be $\mathbb{R}$ or $\mathbb{C}$, let $S_{\mathbb{F}}$ be the
group of scalars of modulus one, and let $1\leq p<\infty$ with $p\neq2$. The
universal minimal flow of the group of surjective linear isometries of
$L^p(Y,\mu;\mathbb{F})$, with the strong operator topology, has phase space
$S_{\mathbb{F}}^{A_\mu}\times\mathrm{LO}(A_\mu)$, with the skew action of the
group $S_{\mathbb{F}}^{A_\mu}\rtimes\mathrm{Sym}(A_\mu)$ of monomial
isometries of the atomic part; the isometries of the atomless part act
trivially.
In particular, the isometry group is extremely amenable when $\mu$ has no
atoms.
:::

:::{prf:theorem} {cite:t}`LupiniPointwise2026`
:label: thm-lupini-wreath

Let $F$ be a Polish group whose universal minimal flow $X=M(F)$ is
metrizable, and let $\Omega$ be a countable set. Give $F^\Omega$ the product
topology and $\mathrm{Sym}(\Omega)$ the topology of pointwise convergence.
Then

$$
M\bigl(F^\Omega\rtimes\mathrm{Sym}(\Omega)\bigr)\cong X^\Omega\times\mathrm{LO}(\Omega),
$$

with the skew action
$((f_a)_a,\sigma)\cdot((x_a)_a,<)=((f_a x_{\sigma^{-1}(a)})_a,\sigma\cdot{<})$.
:::

:::{prf:remark}
:label: rem-lupini-wreath

The proof combines {prf:ref}`thm-bymt`, which provides a co-precompact
extremely amenable subgroup $F^*\leq F$, with the extremely amenable subgroup
$(F^*)^\Omega\rtimes\mathrm{Aut}(\Omega,<_0)$ for an order $<_0$ of type
$\mathbb{Q}$. Applied to the automorphism groups of the Gurarij space and of
the noncommutative Gurarij space, which are extremely amenable, and of the
Poulsen simplex and the noncommutative Poulsen simplex, whose universal
minimal flows are known, it gives explicit wreath-product formulas; the
preprint makes no separate priority claim for them
(Theorem 4.5 and Corollary 4.6 of {cite}`LupiniPointwise2026`).
:::

:::{prf:theorem} {cite:t}`LupiniPointwise2026`
:label: thm-lupini-nuclear

Let $A$ be a unital separable nuclear C*-algebra, and give its unitary group
$U(A)$ the relative weak topology $\sigma(A,A^*)$. Then

$$
M(U(A))\cong\prod_{[\pi]}U(H_\pi),
$$

where $[\pi]$ ranges over the unitary equivalence classes of
finite-dimensional irreducible representations $\pi\colon A\to B(H_\pi)$, and
$u\in U(A)$ acts through the coordinates $\pi(u)$. In particular, $U(A)$ is
extremely amenable in this topology when $A$ has no finite-dimensional
irreducible representations, and $M(U(C(X)))\cong\mathbb{T}^X$ for every
compact metrizable space $X$.
:::
