(sec-maximal-chains)=
# The flow of maximal chains

Uspenskij attached to every flow a second flow: the space of maximal chains of
closed sets. It shows that the action of a group on its universal minimal flow
is never highly transitive, and for several homeomorphism groups it is the
universal minimal flow itself.

:::{prf:definition} Hyperspace
:label: def-hyperspace

For a compact space $X$, let $\mathrm{Exp}(X)$ be the set of nonempty closed
subsets of $X$ with the *Vietoris topology*. Its basic open sets are
the sets $\langle U_1,\dots,U_k\rangle$, for $U_1,\dots,U_k$ open in $X$,
consisting of all $F\in\mathrm{Exp}(X)$ such that
$F\subseteq U_1\cup\dots\cup U_k$ and $F$ meets every $U_j$. It is a compact
space, metrizable if $X$ is.
If $X$ is a $G$-flow, then $gF=\{gx : x\in F\}$ makes $\mathrm{Exp}(X)$ a
$G$-flow.
:::

:::{prf:definition} Maximal chains
:label: def-maximal-chain

A *chain* in a compact space $X$ is a family $c\subseteq\mathrm{Exp}(X)$
that is linearly ordered by inclusion. It is *maximal* if it is not
properly contained in another chain. The set of maximal chains in $X$ is
denoted $\Phi(X)$. A maximal chain is *connected* if all its members are
connected.
:::

:::{prf:proposition}
:label: prop-maximal-chains

Let $X$ be a compact space.

1. Every maximal chain $c$ is a closed subset of $\mathrm{Exp}(X)$. It
   contains $X$, and it has a least element, which is a singleton
   $\{r(c)\}$. The point $r(c)$ is the *root* of $c$.
2. $\Phi(X)$ is a closed subset of $\mathrm{Exp}(\mathrm{Exp}(X))$, hence
   compact {cite}`Uspenskij2000`.
3. If $X$ is a $G$-flow, then $\Phi(X)$ is a subflow of
   $\mathrm{Exp}(\mathrm{Exp}(X))$, and the root map $r\colon\Phi(X)\to X$ is a
   surjective $G$-map.

:::

:::{prf:proof}
(1) The relation $A\subseteq B$ is closed in
$\mathrm{Exp}(X)\times\mathrm{Exp}(X)$, so the closure of a chain is a chain,
and a maximal chain is closed. The set $X$ is comparable with every member of
$c$, so $X\in c$. The intersection $F_0$ of all members of $c$ is nonempty by
compactness and comparable with every member, so $F_0\in c$. If $x\in F_0$,
then $\{x\}$ is contained in every member of $c$, so $\{x\}\in c$ and
$F_0=\{x\}$. Statement (2) is due to Uspenskij; see also
Section 1 of {cite}`GlasnerWeiss2003`.

(3) Homeomorphisms of $X$ preserve inclusion, so $\Phi(X)$ is invariant, and
$r(gc)=gr(c)$. If $c_i\to c$ and $U$ is a neighbourhood of $r(c)$, then
eventually some member $F_i$ of $c_i$ is contained in $U$, because
$\{r(c)\}\in c$; hence $r(c_i)\in F_i\subseteq U$, and $r$ is continuous. For
$x\in X$, Zorn's lemma extends the chain $\{\{x\},X\}$ to a maximal chain,
whose root is $x$.
:::

:::{prf:theorem} {cite:t}`Uspenskij2000`
:label: thm-uspenskij-chains

Let $X$ be a $G$-flow with at least three points on which $G$ acts
$3$-transitively, that is, transitively on triples of distinct points. Then
there is no $G$-map $X\to\Phi(X)$.
:::

:::{prf:proof}
Suppose $f\colon X\to\Phi(X)$ is a $G$-map and fix $x\in X$. The stabiliser
$G_x$ fixes $f(x)$, hence the root of $f(x)$. By $3$-transitivity, $G_x$ acts
transitively on $X\setminus\{x\}$, which has at least two points, so the root
of $f(x)$ is $x$. The chain $\{\{x\},X\}$ is not maximal, since a set
$\{x,y\}$ with $y\neq x$ can be added to it; so $f(x)$ has a member $F$ with
$\{x\}\subsetneq F\subsetneq X$. Pick $y\in F\setminus\{x\}$ and
$z\in X\setminus F$, and $g\in G$ with $g(x)=x$, $g(y)=z$ and $g(z)=y$. Then
$gF\in gf(x)=f(x)$, but $z\in gF\setminus F$ and $y\in F\setminus gF$, so $F$
and $gF$ are not comparable, a contradiction.
:::

:::{prf:corollary} {cite:t}`Uspenskij2000`
:label: cor-not-3-transitive

If $M(G)$ has at least three points, then $G$ does not act $3$-transitively on
$M(G)$.
:::

:::{prf:proof}
By {prf:ref}`prop-maximal-chains`, $\Phi(M(G))$ is a $G$-flow. It
contains a minimal subflow, and $M(G)$ maps onto it, which contradicts
{prf:ref}`thm-uspenskij-chains` if the action is $3$-transitive.
:::

:::{prf:remark}
:label: rem-not-natural-action

Consequently, if $X$ is a compact manifold of dimension greater than one, the
Hilbert cube or the Cantor set, the universal minimal flow of
$\mathrm{Homeo}(X)$ is not the natural action on $X$
{cite}`GlasnerWeiss2003`. This is the result recalled in
{prf:ref}`rem-uspenskij`.
:::

:::{prf:remark} Connected chains
:label: rem-connected-chains

If $X$ is connected, the connected maximal chains form a nonempty, closed,
invariant subset of $\Phi(X)$, so $\Phi(X)$ is not minimal. For the interval,
the circle and the Lelek fan, the universal minimal flow of the homeomorphism
group can be realised inside this subspace {cite}`GutmanTsankovZucker2021`; see
[](#sec-continua). For zero-dimensional spaces, $\Phi(X)$ itself can
be the universal minimal flow; see [](#sec-zero-dim).
:::
