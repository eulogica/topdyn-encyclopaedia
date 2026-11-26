(sec-kpt-umf)=
# Computing universal minimal flows with order expansions

Kechris, Pestov and Todorcevic turned the correspondence of
[](#sec-kpt) into a method for computing universal minimal flows:
expand a Fraïssé class by linear orders that have the Ramsey property and
the ordering property, and the universal minimal flow is the space of all
admissible orders. Throughout, $L$ is a relational signature that does not
contain the symbol $<$.

:::{prf:definition} Order expansions
:label: def-order-expansion

Let $\mathcal{K}$ be a Fraïssé class in $L$ with Fraïssé limit $\mathbf{F}$.
An *order expansion* of $\mathcal{K}$ is a class $\mathcal{K}^*$ of
structures in $L\cup\{<\}$, closed under isomorphism, in which $<$ is
interpreted as a linear order, and such that the $L$-reducts of the members
of $\mathcal{K}^*$ are exactly the members of $\mathcal{K}$. For
$\mathbf{A}\in\mathcal{K}$, an *admissible order* on $\mathbf{A}$ is a
linear order $\prec$ with $(\mathbf{A},\prec)\in\mathcal{K}^*$.

1. $\mathcal{K}^*$ is *reasonable* if for all
   $\mathbf{A},\mathbf{B}\in\mathcal{K}$ with $\mathbf{A}$ a substructure of
   $\mathbf{B}$, every admissible order on $\mathbf{A}$ extends to an
   admissible order on $\mathbf{B}$.
2. $\mathcal{K}^*$ has the *ordering property* if for every
   $\mathbf{A}\in\mathcal{K}$ there is $\mathbf{B}\in\mathcal{K}$ such that
   $(\mathbf{A},\prec)$ embeds into $(\mathbf{B},\prec')$ for every admissible
   order $\prec$ on $\mathbf{A}$ and every admissible order $\prec'$ on
   $\mathbf{B}$.

:::

:::{prf:definition} The flow of admissible orders
:label: def-admissible-orders

Let $\mathcal{K}^*$ be an order expansion of $\mathcal{K}$. Let
$X_{\mathcal{K}^*}$ be the set of linear orders $\prec$ on the universe of
$\mathbf{F}$ such that $(\mathbf{A},{\prec}|_{\mathbf{A}})\in\mathcal{K}^*$
for every finite substructure $\mathbf{A}$ of $\mathbf{F}$. It is a closed
subset of the space of all linear orders on $\mathbf{F}$, defined as in
{prf:ref}`def-lo`, and it is invariant under the action of
$\mathrm{Aut}(\mathbf{F})$ by transport of orders. Hence, when it is
nonempty, it is an $\mathrm{Aut}(\mathbf{F})$-flow.
:::

:::{prf:theorem} {cite:t}`KPT2005`
:label: thm-kpt-umf

Let $\mathcal{K}$ be a Fraïssé class with Fraïssé limit $\mathbf{F}$, and let
$\mathcal{K}^*$ be a reasonable order expansion of $\mathcal{K}$ that is itself
a Fraïssé order class.

1. The Fraïssé limit of $\mathcal{K}^*$ is of the form
   $(\mathbf{F},\prec_0)$ with $\prec_0\in X_{\mathcal{K}^*}$.
2. The $\mathrm{Aut}(\mathbf{F})$-flow $X_{\mathcal{K}^*}$ is minimal if
   and only if $\mathcal{K}^*$ has the ordering property.
3. If $\mathcal{K}^*$ has the Ramsey property and the ordering property,
   then $M(\mathrm{Aut}(\mathbf{F}))$ is $X_{\mathcal{K}^*}$. In particular it
   is metrizable.

:::

:::{prf:proof}
*Proof of (3) from (1) and (2).* Let $G=\mathrm{Aut}(\mathbf{F})$ and let $H\leq G$ be the stabiliser of
$\prec_0$, that is, the automorphism group of the Fraïssé limit of
$\mathcal{K}^*$. It is a closed subgroup, and it is extremely amenable by
{prf:ref}`thm-kpt`. The map $gH\mapsto g{\prec_0}$ is well defined and
injective. For a finite set $A$, let $V_A$ be its pointwise stabiliser in $G$.
Two orders $g{\prec_0}$ and $h{\prec_0}$ agree on $A$ if and only if
$hH=vgH$ for some $v\in V_A$: if they agree, the map $g^{-1}a\mapsto h^{-1}a$
($a\in A$) is an isomorphism between finite substructures of
$(\mathbf{F},\prec_0)$, so ultrahomogeneity gives $k\in H$ extending it, and
$v=hkg^{-1}$ works. So the map is a uniform isomorphism of $G/H$,
with the uniformity of {prf:ref}`def-coprecompact`, onto the orbit of
$\prec_0$. The orbit is dense: given $\prec\in X_{\mathcal{K}^*}$ and a
finite $A$, embed $(A,{\prec}|_A)$ into $(\mathbf{F},\prec_0)$ and use
ultrahomogeneity of $\mathbf{F}$ to find $g\in G$ such that $g{\prec_0}$
agrees with $\prec$ on $A$. Since $X_{\mathcal{K}^*}$ is compact, it is the
completion of $G/H$, so $H$ is co-precompact. By (2) the flow
$X_{\mathcal{K}^*}$ is minimal, and {prf:ref}`prop-coprecompact-ea`
identifies it with $M(G)$.
:::

:::{prf:example} Finite sets
:label: ex-kpt-sets

Let $\mathcal{K}$ be the class of finite sets, in the empty signature, so that
$\mathbf{F}=\mathbb{N}$ and $\mathrm{Aut}(\mathbf{F})=S_\infty$, and let
$\mathcal{K}^*$ be the class of finite linear orders. Every linear order is
admissible, so $\mathcal{K}^*$ is reasonable and $X_{\mathcal{K}^*}$ is
$\mathrm{LO}(\mathbb{N})$. The ordering property holds with
$\mathbf{B}=\mathbf{A}$, since any two linear orders on a finite set are
isomorphic, and the Ramsey property is the finite Ramsey theorem
({prf:ref}`ex-kpt-rationals`). {prf:ref}`thm-kpt-umf` therefore
recovers {prf:ref}`thm-glasner-weiss`.
:::

:::{prf:example} Computations of Kechris, Pestov and Todorcevic
:label: ex-kpt-computations

The following universal minimal flows are computed in Section 8 of
{cite}`KPT2005` with {prf:ref}`thm-kpt-umf`.

1. For the random graph, the random $K_n$-free graphs, and the random
   $r$-uniform hypergraphs, $M(\mathrm{Aut}(\mathbf{F}))$ is the space of
   *all* linear orders on $\mathbf{F}$. The same holds for the rational
   Urysohn space and its isometry group.
2. For the countable equivalence relation with infinitely many classes,
   all of them infinite, $M(\mathrm{Aut}(\mathbf{F}))$ is the space of
   *convex* linear orders, those in which every class is an interval.
3. For the countable atomless Boolean algebra and for the vector space of
   countably infinite dimension over a finite field,
   $M(\mathrm{Aut}(\mathbf{F}))$ is the space of *natural* orders, defined
   in {cite}`KPT2005` from antilexicographic orders. For the Boolean algebra this
   gives, by Stone duality, the universal minimal flow of the homeomorphism
   group of the Cantor set; see [](#sec-zero-dim).

In each case the automorphism group of the Fraïssé limit of $\mathcal{K}^*$
is extremely amenable ({prf:ref}`thm-kpt`). See also the survey
{cite}`NguyenVanThe2014`.
:::
