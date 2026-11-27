(sec-proofs-unital-kirchberg-af)=
# Proofs: unital Kirchberg and AF algebras

This section reproduces, from the preprint of the editor {cite}`LupiniUnital2026` in its version of 15 September 2026, the
proofs of the results stated in [](#sec-operator-algebras). The text is that of the
preprint, with British spelling: its sections appear as subsections, its macros
are expanded and its labels renamed, and of its introduction only the
statements of the main results are kept. Citations of the companion preprints
point to their own proof pages where the cited statement is reproduced there.
The preprint has not been refereed. The last subsection derives the statements
of [](#sec-operator-algebras) from those of the preprint.

(sec-un-main-results)=
## Main results of the preprint

:::{prf:theorem} Unital Kirchberg automorphisms
:label: thm-un-main-kirchberg

For every unital Kirchberg algebra $A$,

$$
M(\operatorname{Aut}(A))\cong S(A)\times M(Q_A^0),
$$ (eq-un-main-kirchberg)

where $\alpha\cdot(\rho,x)=(\rho\circ\alpha^{-1},q_A^0(\alpha)\cdot x)$.
Moreover $M(N_A^0)=S(A)$, and $S(A)$ is the Furstenberg boundary
of $N_A^0$. If $\varphi$ is pure, the restriction

$$
\operatorname{Aut}(A,\varphi)\longrightarrow Q_A^0
$$

is an open surjection with whirly amenable kernel. If $A$ satisfies
the UCT and $K_1(A)=0$, then

$$
Q_A^0\cong\operatorname{Aut}(K_0(A),[1_A])
$$

with pointwise convergence on the countable discrete group $K_0(A)$.
:::

:::{prf:theorem} Unital AF automorphisms
:label: thm-un-main-af

Suppose that $A$ is separable, unital and AF, and has no nonzero
finite-dimensional representations. Then $U(A)$ is whirly amenable
in norm, $\overline{\operatorname{Inn}(A)}$ is whirly amenable in the point-norm
topology, and

$$
M(\operatorname{Aut}(A))\cong q_A^*M(\Gamma_A),
 \qquad q_A(\alpha)=K_0(\alpha).
$$ (eq-un-main-af)

In particular {eq}`eq-un-main-af` applies to every infinite-dimensional
simple separable unital AF algebra.
Moreover, $\operatorname{Aut}(A)$ is whirly amenable if and only if $\Gamma_A=1$.
:::

(sec-un-prelim)=
## Dynamical inputs

We use continuous actions on nonempty compact Hausdorff spaces. Extreme
amenability means that every such action has a fixed point. Whirly
amenability adds amenability to the requirement that every invariant
regular probability measure have support in the fixed-point set.
The following permanence and quotient principles are used in the forms established
in {cite}`LupiniCuntz2026`, Section 2 and
{cite}`LupiniStable2026`, Section 2; they are recalled as inputs.

:::{prf:proposition} Permanence and quotient principles
:label: prop-un-dynamical-inputs

1. Continuous homomorphisms with dense image preserve extreme and
   whirly amenability. Products with the product topology preserve these
   properties, as do dense directed unions of subgroups with the property.
2. An open continuous quotient $q:G\to Q$ with extremely amenable
   kernel satisfies $M(G)=q^*M(Q)$ and $bG=bQ$; amenability transfers
   in both directions. If the kernel is whirly amenable, whirly amenability
   also transfers in both directions. When the kernel is whirly amenable,
   any invariant measure on a compact $G$-flow has support fixed by the
   kernel, and the action on that support descends to $Q$.
3. For a compact group $K$,
   $M(K\times L)=K\times M(L)$. A locally compact Polish group has
   metrizable universal minimal flow exactly when it is compact.
4. A non-Archimedean Polish group is whirly amenable exactly when it
   is trivial.
5. An infinite permutation wreath product
   $E^I\rtimes\operatorname{Sym}(I)$, with product and pointwise topologies, has
   trivial Bohr compactification.
:::

The right uniformity of $G$ compares $vg$ with $g$ for small
$v$. We use the corresponding quotient uniformity on $G/H$.
The Samuel compactification is defined by bounded uniformly continuous
functions; for a group it is the greatest right ambit $S_R(G)$.
Here a UEB family consists of bounded right uniformly continuous
functions that are uniformly bounded and share a modulus of uniform
continuity. UEB convergence to left invariance means that, for each
$g\in G$, the differences between integration against $\mu_i$ and
against $g\mu_i$ tend to zero uniformly over each such family.
Schneider's criterion {cite}`Schneider2019`, Corollary 5.7 implies that every
Polish Lévy group is whirly amenable: the Haar measures of its increasing
compact subgroups concentrate and UEB-converge to invariance.

:::{prf:lemma} Samuel-space criterion
:label: lem-un-samuel

Let $H\leq G$ be extremely amenable. Every minimal subflow of
$\operatorname{Samuel}(G/H)$ is a model of $M(G)$.
In particular, if the right-uniform completion of $G/H$ is compact
and minimal, that completion is $M(G)$.
:::

:::{prf:proof}
Every compact $G$-flow $X$ has an $H$-fixed point $x$.
The map $gH\mapsto gx$ is right uniformly continuous: for each
entourage of $X$, compactness and joint continuity supply an
identity neighbourhood moving every point by that entourage.
The orbit map extends to the Samuel compactification.
If $X$ is minimal, the image of any nonempty minimal subflow is
all of $X$. This proves universality. In the precompact case the
Samuel compactification is the compact uniform completion.
:::

Polish automorphism groups and their closed quotients obey the open
mapping theorem: a continuous surjective homomorphism is open
{cite}`BeckerKechris1996`. This will determine the topology of each
classification quotient.

(sec-un-alignment)=
## The alignment input from the Cuntz paper

The uniform alignment theorem
{prf:ref}`thm-cu-alignment` applies to every simple, separable,
unital, infinite-dimensional nuclear algebra. For each finite
$F\subset A$ and $\varepsilon>0$, it supplies finite
$E\subset A$ and $\delta>0$, independent of the pure states,
such that pure states $\rho_0,\rho_1$ that are $\delta$-close on $E$
can be aligned by an automorphism moving $F$ by less than
$\varepsilon$.

We use the identity-component refinement of this input:

$$
\rho_1=\rho_0\circ v^{-1},\qquad
 \max_{a\in F}\left\lVert v(a)-a\right\rVert<\varepsilon,
 \qquad v\in N_A^0.
$$

It follows from the cited construction: the corrections produced by
{prf:ref}`prop-cu-approx-alignment` are endpoints of unitary paths
starting at one, hence lie in $U_0(A)$, and the automorphisms of
{prf:ref}`thm-cu-alignment` are point-norm limits of adjoint
actions of finite products of such unitaries. Its limiting adjoint
actions therefore lie in $N_A^0$. This observation records the subgroup needed below;
the UCP-row, Gram-matrix, and alternating-construction proofs remain
in the Cuntz paper. For unitarily equivalent states we also use the
exact unitary correction of {prf:ref}`prop-cu-approx-alignment`,
or equivalently Property 1.2 of {cite}`KishimotoOzawaSakai2003`, which holds for every
$C^*$-algebra by Theorems 3.1 and 4.3 of that paper.

(sec-un-kirchberg-stabilizer)=
## Pure-state stabilisers of unital Kirchberg algebras

Fix a unital Kirchberg algebra $A$ and a pure state $\varphi$, with
GNS triple $(\pi,\mathcal H,\xi)$. Use the notation

$$
\begin{gathered}
 G=\operatorname{Aut}(A),\quad N^0=\overline{\operatorname{Ad} U_0(A)},\quad Q=G/N^0,\\
 q=q_A^0:G\longrightarrow Q,\\
 H=\operatorname{Aut}(A,\varphi),\qquad H^0=H\cap N^0,\\
 D_\varphi=\{a\in A:\varphi(a^*a)=\varphi(aa^*)=0\}.
 \end{gathered}
$$

The notation $H^0$ denotes this intersection; it is not a definition
of the identity component of $H$.

For $A=\mathcal O_2$, the following hereditary-algebra identification
is {prf:ref}`lem-cu-hereditary`; the point here is its form for every
unital Kirchberg algebra.

:::{prf:lemma}
:label: lem-un-hereditary

The hereditary algebra $D_\varphi$ is a full, nonunital, stable
Kirchberg algebra, and

$$
D_\varphi\cong A\otimes\mathcal K.
$$

Its inclusion in $A$ induces isomorphisms on $K$-theory.
Furthermore, viewing $D_\varphi^+=D_\varphi+\mathbb C1_A$ inside $A$,

$$
U_1(D_\varphi)
   =\{u\in U(A):\pi(u)\xi=\xi\},\qquad
 U_1(D_\varphi)_0=U_1(D_\varphi)\cap U_0(A).
$$
:::

:::{prf:proof}
The algebra $D_\varphi$ is hereditary. Kadison transitivity applied
on a two-dimensional subspace gives a nonzero selfadjoint element
annihilating $\xi$, so $D_\varphi\neq0$; simplicity makes it full.
The support of a pure state is a minimal projection in $A^{**}$.
If $D_\varphi$ had an identity $e$, its bidual support would give
$e=1-s_\varphi$. Thus $s_\varphi=1-e$ would be a nonzero minimal
projection in $A$, contrary to pure infiniteness.
Zhang's dichotomy {cite}`Zhang1992`, Theorem 1.2 makes the nonunital,
$\sigma$-unital, purely infinite simple algebra $D_\varphi$ stable.
Brown's full-hereditary theorem {cite}`Brown1977`, Theorem 2.8 then gives
the displayed isomorphism and the $K$-theory equivalence.

For a unitary, $\pi(u)\xi=\xi$ is equivalent to
$u-1\in D_\varphi$; the condition also gives $\pi(u^*)\xi=\xi$.
The stable component identification gives

$$
U_1(D_\varphi)/U_1(D_\varphi)_0\cong K_1(D_\varphi).
$$

On the other hand, purely infinite $K_1$-injectivity gives
$U(A)/U_0(A)\cong K_1(A)$ {cite}`Cuntz1981`; see also {cite}`Blackadar1998`, Proposition 8.1.4.
Since the inclusion induces a $K_1$-isomorphism, the final equality
follows.
:::

:::{prf:lemma} Relative inner approximation
:label: lem-un-marked-inner

One has

$$
H^0=\overline{\operatorname{Ad} U_1(D_\varphi)_0}.
$$
:::

:::{prf:proof}
Let $\alpha\in H^0$, and fix a finite test set $F\subset A$ and a
tolerance. Choose the state tests $E,\delta$ in the exact unitary
correction recalled in [](#sec-un-alignment), with small movement
on $F$. Take $v\in U_0(A)$ such that $\operatorname{Ad} v$ approximates
$\alpha$ on $F\cup E$. Since $\varphi\alpha=\varphi$,
the equivalent pure states $\varphi\circ\operatorname{Ad} v$ and $\varphi$ are
$\delta$-close on $E$.
That correction {prf:ref}`prop-cu-approx-alignment` supplies
$w\in U_0(A)$, almost central on $F$,
such that $\varphi\circ\operatorname{Ad} v=\varphi\circ\operatorname{Ad} w$.
Then $z=vw^*\in U_0(A)$ preserves $\varphi$, and $\operatorname{Ad} z$
approximates $\alpha$ on $F$.

Equality of the vector states of $\xi$ and $\pi(z^*)\xi$ in an
irreducible representation makes these vectors scalar multiples:
the intertwiner they define lies in the scalar commutant.
After multiplying $z$ by a scalar, which does not change
$\operatorname{Ad} z$ or its component, we have $\pi(z)\xi=\xi$.
{prf:ref}`lem-un-hereditary` puts $z$ in $U_1(D_\varphi)_0$.
The reverse inclusion in the asserted equality is immediate.
:::

:::{prf:theorem}
:label: thm-un-marked-whirly

The group $H^0=\operatorname{Aut}(A,\varphi)\cap\overline{\operatorname{Ad} U_0(A)}$
is whirly amenable in the point-norm topology, and hence extremely
amenable.
:::

:::{prf:proof}
By {prf:ref}`lem-un-hereditary` and the stable nuclear norm-unitary theorem
{prf:ref}`thm-st-v`,
$U_1(D_\varphi)_0$ is whirly amenable in norm.
Its adjoint map to the point-norm automorphism group is continuous,
since
$\left\lVert uau^*-vav^*\right\rVert\leq2\left\lVert a\right\rVert\left\lVert u-v\right\rVert$.
Its image has dense closure $H^0$ by {prf:ref}`lem-un-marked-inner`.
{prf:ref}`prop-un-dynamical-inputs`1 gives whirly amenability of
$H^0$.
:::

The hereditary algebra $D_\varphi$ identifies the connected
unitaries fixing the chosen GNS vector with a stabilised norm-unitary
group. Its dense adjoint image gives the pure-state stabiliser in
$N^0$.

(sec-un-kirchberg-product)=
## The state space and the Kirchberg product formula

:::{prf:lemma}
:label: lem-un-state-minimal

The action $N^0\curvearrowright S(A)$,
$\alpha\cdot\rho=\rho\circ\alpha^{-1}$, is minimal and strongly
proximal. Its pure states form a comeager orbit.
:::

:::{prf:proof}
Fix $\rho\in S(A)$, a pure state $\sigma$, a finite subset $F$
of the unit ball, and $\varepsilon>0$. Pure-state excision
{cite}`AkemannAndersonPedersen1986` and real rank zero {cite}`Zhang1992`, Theorem 1.2 give a nonzero proper projection $p$
such that

$$
\left\lVert pap-\sigma(a)p\right\rVert<\varepsilon\qquad(a\in F).
$$

For detail, excise by a norm-one positive contraction $h$, and take
a nonzero projection in the hereditary algebra generated by
$(h-(1-\gamma))_+$. Then $\left\lVert hp-p\right\rVert\leq\gamma$.
Choosing the excision and $\gamma$ errors small gives the estimate;
a proper nonzero subprojection preserves it.

Choose $m\geq2$ mutually orthogonal nonzero projections in $A$.
One of them, $z$, has $\rho(z)\leq1/m$.
Pure infiniteness gives $r\leq z$ with $r\sim1-p$.
Set $q=1-r$. Both $q,r$ are nonzero and
$[q]=[p]$. Classification of nonzero projections in a purely
infinite simple algebra gives $q\sim p$
{cite}`Blackadar1998`, Corollary 6.11.9.
The two equivalences combine to a unitary $v$ with $vpv^*=q$.

We can choose $v\in U_0(A)$. Indeed the full corner $pAp$ has
the same $K_1$-group as $A$, and its unitary group surjects onto
$K_1$. Choose $w\in U(pAp)$ with
$[w+(1-p)]=-[v]$ and replace $v$ by $v(w+(1-p))$.
This keeps $vpv^*=q$, and $K_1$-injectivity puts the new
unitary in $U_0(A)$.

For $\rho'=\rho\circ\operatorname{Ad} v$, we have
$t=\rho'(1-p)=\rho(r)\leq1/m$. The two off-diagonal corners are
bounded by Cauchy–Schwarz, so

$$
|\rho'(a)-\sigma(a)|
 \leq \varepsilon+2\sqrt t+2t
 \leq \varepsilon+2m^{-1/2}+2m^{-1}\qquad(a\in F).
$$

Every $N^0$-orbit therefore approaches every pure state.
Pure states are weak-* dense by Glimm approximation, as used in {prf:ref}`lem-cu-glimm-avoid` in a
faithful essential irreducible representation. This proves minimality.

For strong proximality, move the barycenter of a probability measure
on $S(A)$ towards a pure state. Any cluster point of the translated
measures has that pure barycenter, so it must be the corresponding
Dirac measure. Finally, pure-state homogeneity by asymptotically
inner automorphisms implemented by paths starting at $1$
{cite}`KishimotoOzawaSakai2003`, Theorem 2.1 makes the pure states one $N^0$-orbit.
Extreme points of a compact metrizable convex set form a $G_\delta$.
Their density then makes this orbit comeager.
:::

:::{prf:proposition}
:label: prop-un-state-completion

The orbit map

$$
N^0/H^0\longrightarrow P(A),\qquad
 nH^0\longmapsto\varphi\circ n^{-1},
$$

is a uniform isomorphism for quotient right uniformity and weak-*
uniformity. Its compact completion is $S(A)$.
Consequently $M(N^0)=S(A)$.
:::

:::{prf:proof}
Pure-state homogeneity gives bijectivity. For every state $\rho$
and every automorphism $v$,

$$
|(\rho\circ v^{-1})(a)-\rho(a)|
 \leq\left\lVert v^{-1}(a)-a\right\rVert=\left\lVert v(a)-a\right\rVert.
$$

This gives forward uniform continuity.
The alignment input in [](#sec-un-alignment), including $v\in N^0$, gives
inverse uniform continuity with tests independent of the base state.
Weak-* density of pure states identifies the completion with $S(A)$.
Now use {prf:ref}`thm-un-marked-whirly`,
{prf:ref}`lem-un-state-minimal`, and {prf:ref}`lem-un-samuel`.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-un-main-kirchberg`.* The preceding proposition gives $M(N^0)=S(A)$.
Since this flow is strongly proximal, it is also the Furstenberg
boundary of $N^0$.
Pure-state transitivity under $N^0$ gives $G=N^0H$. Hence
$q|_H:H\to Q$ is a continuous surjection, with kernel $H^0$.
Both groups are Polish, so the Polish open mapping theorem makes
it open. {prf:ref}`prop-un-dynamical-inputs`2 gives $M(H)=q^*M(Q)$.

We verify the additional uniformity needed for the full-group product.
The map

$$
G/H^0\longrightarrow P(A)\times Q,\qquad
 gH^0\longmapsto(g\cdot\varphi,q(g))
$$ (eq-un-quotient-product)

is an equivariant bijection. For surjectivity, first choose an element
with the prescribed quotient and then correct its state using $N^0$.
For injectivity, equality of both coordinates gives a difference
in $H\cap N^0$.
The state estimate above and uniform continuity of the group quotient
give forward uniform continuity.

For the converse fix an identity neighbourhood $V$ in $G$, and
choose $V_1V_2\subseteq V$. Uniform alignment gives a weak-*
entourage $\mathcal U$ such that pairs of pure states in
$\mathcal U$ can be aligned by $V_1\cap N^0$.
Choose a symmetric $\mathcal U_0$ with
$\mathcal U_0\circ\mathcal U_0\subseteq\mathcal U$.
Compactness of $S(A)$ gives $V_3\subseteq V_2$ moving every
state by $\mathcal U_0$. Since $q$ is open, $q(V_3)$ is an
identity neighbourhood in $Q$.
If $(\rho',\rho)\in\mathcal U_0$ and $t't^{-1}\in q(V_3)$,
lift the latter difference to $v\in V_3$, and then choose
$n\in V_1\cap N^0$ with $nv\cdot\rho=\rho'$.
The element $nv\in V$ carries one corresponding coset to the
other. This proves inverse uniform continuity.

It follows that

$$
\operatorname{Samuel}(G/H^0)\cong S(A)\times S_R(Q).
$$ (eq-un-samuel-product)

Here is a justification of the compactification step. A bounded
uniformly continuous function on $P(A)\times Q$ extends to
$S(A)\times Q$, uniformly in the second coordinate.
A finite partition of unity on $S(A)$ approximates it, uniformly,
by sums $h_i(\rho)f_i(q)$ with $f_i$ right uniformly continuous.
These sums extend to $S(A)\times S_R(Q)$.
Conversely, Stone–Weierstrass gives uniform approximation of every
continuous function on the compact product by such sums.

{prf:ref}`thm-un-marked-whirly` and {prf:ref}`lem-un-samuel` make every
minimal subflow of {eq}`eq-un-samuel-product` universal.
The group $N^0$ acts minimally on $S(A)$ and trivially on
$S_R(Q)$. Thus every nonempty closed $G$-invariant subset of
the product is $S(A)\times Y$, with $Y$ closed and
$Q$-invariant: each nonempty fiber contains a dense $N^0$-orbit
in the first coordinate. It is minimal exactly when $Y$ is
$Q$-minimal. This proves the product formula and its action.
The UCT assertion follows from {prf:ref}`thm-un-uct` below.
:::

:::{prf:corollary} Invariant measures for pure-state stabilisers
:label: cor-un-marked-measures

Let $A$ be a unital Kirchberg algebra and $\varphi$ a pure state.
Put $H=\operatorname{Aut}(A,\varphi)$ and $H^0=H\cap N_A^0$.
In every compact $H$-flow $X$, any invariant regular probability
measure has support in $X^{H^0}$, and the action on its support
descends to $Q_A^0$ through $q_A^0|_H$. Moreover,

$$
H\text{ is whirly amenable}
 \quad\Longleftrightarrow\quad Q_A^0\text{ is whirly amenable}.
$$

In particular, if $Q_A^0=1$, the entire pure-state stabiliser $H$
is whirly amenable.
If $Q_A^0$ is non-Archimedean, then $H$ is whirly amenable
exactly when $Q_A^0=1$. In particular, when $A$ satisfies the UCT
and $K_1(A)=0$, this is equivalent to
$\operatorname{Aut}(K_0(A),[1_A])=1$.
:::

:::{prf:proof}
The preceding proof shows that $q_A^0|_H$ is an open surjection
with kernel $H^0$. Apply {prf:ref}`thm-un-marked-whirly` and
{prf:ref}`prop-un-dynamical-inputs`2.
For the final assertions use {prf:ref}`prop-un-dynamical-inputs`4 and the
quotient identification in {prf:ref}`thm-un-main-kirchberg`.
:::

:::{prf:corollary}
:label: cor-un-kirchberg-dynamics

For a unital Kirchberg algebra $A$:

1. $\operatorname{Aut}(A)$ and $N_A^0$ are not amenable.
2. $bN_A^0=1$, and $b\operatorname{Aut}(A)\cong bQ_A^0$.
3. $M(\operatorname{Aut}(A))$ is metrizable if and only if $M(Q_A^0)$ is.
   If $Q_A^0$ is locally compact, this is equivalent to its
   compactness, and then $M(\operatorname{Aut}(A))=S(A)\times Q_A^0$.
:::

:::{prf:proof}
A nontrivial minimal strongly proximal flow has no invariant
probability measure: translating one would leave it unchanged,
while strong proximality would make it a Dirac mass at a fixed point.
The state space here is nontrivial, so (i) follows for either group.
Every compact group image of $N_A^0$ is a factor of its UMF,
hence strongly proximal; a compact group translation flow is
strongly proximal only when trivial. This proves (ii), using the
open quotient to factor continuous homomorphisms.
For (iii), use the product formula and compact metrizability of
$S(A)$. A noncompact locally compact group has nonmetrizable
UMF, whereas a compact group is its own UMF {cite}`Pestov2006`.
:::

(sec-un-uct)=
## The residual unital quotient under the UCT

Assume in this section that $A$ is a unital UCT Kirchberg algebra.
Write $G_i=K_i(A)$, $u=[1_A]$, and

$$
N_A=\overline{\operatorname{Ad} U(A)},\qquad N_A^0=\overline{\operatorname{Ad} U_0(A)}.
$$

For a subgroup $F\subseteq G_0$ containing $u$, write

$$
H_u(F,G_1)=\{f(u):f\in\operatorname{Hom}(F,G_1)\}.
$$

Choose increasing finitely generated subgroups $F_n\subseteq G_0$
containing $u$, with union $G_0$, and define

$$
H_n=H_u(F_n,G_1),\qquad
 L_A=\varprojlim_n G_1/H_n.
$$ (eq-un-l)

Restriction gives $H_{n+1}\subseteq H_n$, so the bonding maps
are the quotient maps. Each coordinate is discrete. Thus $L_A$
is an abelian Polish group. The map

$$
\delta:G_1\longrightarrow L_A,\qquad
 x\longmapsto(x+H_n)_n
$$

has dense image: a compatible finite list of coordinates is realised
by any representative of its last coordinate.

Let $\underline K(A)$ denote the ordinary graded $K$-groups
and the finite-coefficient $K$-groups, with their coefficient
and Bockstein operations. Put

$$
T_A=\operatorname{Aut}_\Lambda(\underline K(A),u).
$$

Its topology is pointwise convergence on this countable collection
of countable discrete groups. Preservation of operations and of the
unit is closed, so $T_A$ is a non-Archimedean Polish group.

:::{prf:theorem} The unit obstruction
:label: thm-un-uct

There is an exact sequence of Polish groups

$$
1\longrightarrow L_A\longrightarrow Q_A^0
 \longrightarrow T_A\longrightarrow1.
$$ (eq-un-uct-sequence)

The last map is open. The first identifies $L_A$ homeomorphically
with the closed subgroup $N_A/N_A^0$, by

$$
\delta([v])\longmapsto \operatorname{Ad} v\,N_A^0\qquad(v\in U(A)).
$$

If $\alpha\in\operatorname{Aut}(A)$, conjugation by its class on $L_A$ is

$$
(x_n+H_n)_n\longmapsto
 (K_1(\alpha)(x_n)+H_n)_n.
$$ (eq-un-l-action)

In particular, if $G_1=0$, then
$Q_A^0\cong\operatorname{Aut}(G_0,u)$ topologically.
:::

:::{prf:proof}
Ng–Ruiz prove Property (C) for unital simple nuclear separable UCT
purely infinite algebras {cite}`NgRuiz2008`, Theorem 3, and identify
$N_A/N_A^0$ with {eq}`eq-un-l` through precisely the displayed dense map
{cite}`NgRuiz2008`, Theorem 2. The latter assumes in addition that the natural map
$U(A)/U_0(A)\to K_1(A)$ is an isomorphism; this holds here by pure
infiniteness, as they note, by {cite}`Cuntz1981` and
{cite}`Blackadar1998`, Proposition 8.1.4.
The identification of $\operatorname{Aut}(A)/N_A$ with $T_A$ is the unital
Kirchberg classification theorem {cite}`Phillips2000`, Theorem 4.2.1 and
Corollary 4.2.2 together with the universal multicoefficient
theorem {cite}`DadarlatLoring1996` and the uniqueness theorem
{cite}`Dadarlat2005`, Theorem 5.1(a); the positivity condition appearing in
the stably finite formulations is vacuous in the purely infinite simple
case.
These statements give algebraic exactness in {eq}`eq-un-uct-sequence`.
The action on total $K$-theory is continuous, since sufficiently
close projection and unitary representatives have the same class.
The induced surjection of Polish groups is open.
The topology on $N_A/N_A^0$ agrees with its subspace topology in $Q_A^0$,
since $N_A$ is closed and contains $N_A^0$.

Every automorphism $a_1$ of $G_1$ preserves every $H_n$, by
composing homomorphisms $F_n\to G_1$ with $a_1$ and its inverse.
The identity
$\alpha\circ\operatorname{Ad} v\circ\alpha^{-1}=\operatorname{Ad}(\alpha(v))$ proves
{eq}`eq-un-l-action` on $\delta(G_1)$, and continuity extends it.
The intrinsic identification with $N_A/N_A^0$ also proves independence
of the exhaustion $F_n$.
When $G_1=0$, $L_A=0$, and both even UCT extension terms
vanish. The multicoefficient invariant therefore has precisely the
unit-preserving $G_0$-automorphisms. Equivalently this follows
directly from unital Kirchberg classification {cite}`RosenbergSchochet1987,Phillips2000`.
:::

:::{prf:remark}
:label: rem-un-remark-1

We cite the theorem numbering of the published Ng–Ruiz paper:
Theorems 2 and 3 correspond to Theorems 2.7 and 3.1, respectively,
in the linked 2007 preprint. In that paper the notation for
the approximately inner group denotes a closure; it does not mean only
the algebraically inner automorphisms.
Sequence {eq}`eq-un-uct-sequence` is an extension with specified
topology and conjugation action. These data alone do not supply a
splitting or determine its extension class.
:::

:::{prf:proposition} Computing $L_A$
:label: prop-un-l-computation

If $G_0$ is finitely generated, then

$$
L_A=G_1/H_u(G_0,G_1)
$$

discretely. More explicitly, if

$$
G_0=\mathbb Z^r\oplus\bigoplus_{j=1}^s\mathbb Z/n_j,\qquad
 u=(a_1,\ldots,a_r;b_1,\ldots,b_s),
$$

then

$$
H_u(G_0,G_1)=\sum_{i=1}^r a_iG_1+
             \sum_{j=1}^s b_jG_1[n_j],
$$ (eq-un-h-formula)

where $G_1[n]=\{x:nx=0\}$.
For arbitrary countable $G_0$, $L_A=0$ if $u$ generates
a free direct summand, and $L_A=G_1$ discretely if $u=0$.
:::

:::{prf:proof}
A finite set of generators eventually lies in $F_n$, after which
the inverse system is constant. Evaluation of homomorphisms on
the indicated generators gives {eq}`eq-un-h-formula`.
If a homomorphism $r:G_0\to\mathbb Z$ satisfies $r(u)=1$, the maps
$g\mapsto r(g)x$ realise every $x\in G_1$, already after
restriction to each $F_n$. If $u=0$, all $H_n=0$.
:::

:::{prf:proposition} Finite $K$-groups
:label: prop-un-finite-k

If $G_0,G_1$ are finite, $Q_A^0$ is finite, with

$$
\begin{split}
 |Q_A^0|={}&|G_1/H_u(G_0,G_1)|\,
 |\operatorname{Aut}(G_0,u)|\,|\operatorname{Aut}(G_1)|\\
 &{}\cdot|\operatorname{Ext}^1(G_0,G_1)|\,|\operatorname{Ext}^1(G_1,G_0)|.
 \end{split}
$$

In this case

$$
M(\operatorname{Aut}(A))=S(A)\times Q_A^0.
$$

The order formula is not a description of the multiplication in $Q_A^0$.
:::

:::{prf:proof}
The even UCT kernel is the square-zero ideal

$$
E=\operatorname{Ext}^1(G_0,G_1)\oplus\operatorname{Ext}^1(G_1,G_0).
$$

Pure extensions from finitely generated groups split, so the
pure-extension subgroup is zero here. The multicoefficient theorem
{cite}`DadarlatLoring1996,Dadarlat2005` identifies the kernel of
$T_A\to\operatorname{Aut}(G_0,u)\times\operatorname{Aut}(G_1)$ with $1+E$, whose group
law is addition in $E$.
Every lift of a graded automorphism is invertible: lift its inverse,
and correct the errors $1+e$ by $1-e$, using $E^2=0$.
Counting this exact sequence and {eq}`eq-un-uct-sequence` gives
the formula. The UMF assertion follows from {prf:ref}`thm-un-main-kirchberg`.
:::

:::{prf:example} Two different component effects
:label: ex-un-two-components

The range theorem for UCT Kirchberg algebras {cite}`Phillips2000`, Theorem 4.2.5(1) realises
$(G_0,u,G_1)=(0,0,\mathbb Z/2)$. Here $T_A=1$, while $L_A=\mathbb Z/2$.
All automorphisms are approximately inner, but $N_A^0$ has index two:

$$
M(\operatorname{Aut}(A))=S(A)\times\mathbb Z/2.
$$

The example shows why $\overline{\operatorname{Inn}(A)}$ cannot simply replace
$\overline{\operatorname{Ad} U_0(A)}$ in the unital Kirchberg product formula.
:::

:::{prf:example} A profinite unit obstruction
:label: ex-un-profinite

Let $p$ be prime, and take

$$
(G_0,u,G_1)=(\mathbb Z[1/p],1,\mathbb Z).
$$

For $F_n=p^{-n}\mathbb Z$, a homomorphism $F_n\to\mathbb Z$ takes $1$
to a multiple of $p^n$. Hence

$$
L_A=\varprojlim_n\mathbb Z/p^n\mathbb Z=\mathbb Z_p.
$$

The group $\mathbb Z[1/p]$ is torsion free, so every extension from it
by $\mathbb Z$ is pure: the quotient has no torsion.
Also $\operatorname{Ext}^1(\mathbb Z,\mathbb Z[1/p])=0$.
Thus the Hausdorff UCT kernel vanishes and $T_A=\{\pm1\}$,
acting by signs on $G_1$.
Conjugation on $L_A$ is inversion for the nontrivial element.
If $s$ is any lift of that element, $s^2\in L_A$.
It commutes with $s$, so $s^2=-s^2$ in the additive notation
on $L_A$. The group $\mathbb Z_p$ has no two-torsion, whence $s^2=1$.
Therefore

$$
Q_A^0\cong\mathbb Z_p\rtimes\{\pm1\}.
$$

It is compact. The automorphism UMF is the metrizable space
$S(A)\times(\mathbb Z_p\rtimes\{\pm1\})$. The unit obstruction is compact even though its defining dense group $\mathbb Z$ is discrete and infinite.
:::

(sec-un-af)=
## Unital AF algebras and dimension groups

### Concentration with arbitrarily many matrix blocks

The AF argument uses the following estimate, whose independence of the
number of factors is essential.

:::{prf:lemma} Product concentration
:label: lem-un-product-concentration

For positive integers $d_1,\ldots,d_k$, put

$$
K=\prod_{j=1}^k U(d_j),\quad d_*=\min_jd_j,\quad
 d_2(P,Q)=\left(\sum_j\left\lVert P_j-Q_j\right\rVert_{\mathrm{HS}}^2\right)^{1/2}.
$$

If $f:K\to\mathbb R$ is $1$-Lipschitz for $d_2$, Haar probability $h$
satisfies, for $d_*>2$ and $t>0$,

$$
h\{|f-\textstyle\int f\,dh|\geq t\}
 \leq2\exp\bigl(-(d_*-2)t^2/24\bigr).
$$ (eq-un-product-concentration)

Consequently, as $d_*\to\infty$, these groups with Haar measure
are a Lévy family for the maximum operator-norm metric, with
no restriction on $k$.
:::

:::{prf:proof}
The estimate follows by applying {cite}`Meckes2019`, Theorem 5.17
to $f$ and $-f$. Its proof uses the logarithmic
Sobolev inequality for each matrix group and its tensorization
with the maximum of the factor constants.
To obtain the assertion about operator norm, observe

$$
\max_j\left\lVert P_j-Q_j\right\rVert_{\mathrm{op}}\leq d_2(P,Q).
$$

Thus distance from any set in the maximum norm is $1$-Lipschitz
for $d_2$. If the set has measure at least $a>0$, the lower
tail estimate forces the mean of that distance to tend to zero;
the upper tail estimate makes the measure outside any fixed
positive neighbourhood tend to zero.
:::

:::{prf:lemma} Growing block sizes
:label: lem-un-block-growth

Let $A=\overline{\bigcup_n F_n}$ be a unital AF algebra, with
$F_n\subseteq F_{n+1}$ finite dimensional and containing $1_A$.
Write $F_n=\bigoplus_{j=1}^{k_n}M_{d_{n,j}}$.
Then $A$ has no nonzero finite-dimensional representations if
and only if

$$
\min_j d_{n,j}\longrightarrow\infty.
$$
:::

:::{prf:proof}
A unital representation of $A$ into $M_d$ restricts to a unital
representation of each $F_n$, so at least one block of $F_n$
has size at most $d$.
Conversely, if the displayed limit fails, pass to a sequence of
levels with a block of the same size $d$, for some fixed $d$.
Projection onto that block gives unital homomorphisms
$\pi_\ell:F_{n_\ell}\to M_d$.
For each fixed $m$, the unital homomorphisms $F_m\to M_d$
form a compact space: there are finitely many multiplicity types,
and each type is a compact unitary orbit.
A diagonal subsequence makes $\pi_\ell|_{F_m}$ converge for
every $m$. The limits are compatible unital homomorphisms.
Their union extends by continuity to a unital homomorphism $A\to M_d$,
a contradiction. A nonzero finite-dimensional representation can
always be restricted to its support and regarded as unital.
:::

:::{figure} ../../figures/bratteli.svg
:name: fig-bratteli
:figclass: enc-figure
:alt: Two Bratteli diagrams with their block sizes: in one every block grows, in the other a block of size 1 survives at every level
:width: 100%

Bratteli diagrams of two unital AF algebras $\overline{\bigcup_nF_n}$, where each $F_n$ has two matrix blocks, labelled by their sizes $d_{n,j}$; every edge has multiplicity one. (a) Every block grows, so by {prf:ref}`lem-un-block-growth` the algebra has no nonzero finite-dimensional representations. (b) A block of size $1$ survives at every level and receives an edge only from the block of size $1$ above it, so the projections onto it are compatible and give a one-dimensional representation. (Illustration added for the encyclopaedia.)
:::

:::{prf:theorem}
:label: thm-un-af-unitary

For a separable unital AF algebra $A$, the following are equivalent:

1. $A$ has no nonzero finite-dimensional representations;
2. the norm group $U(A)$ is a Lévy group;
3. $U(A)$ is whirly amenable in norm;
4. $U(A)$ is extremely amenable in norm.
:::

:::{prf:proof}
Choose $F_n$ as in {prf:ref}`lem-un-block-growth`. The compact groups

$$
K_n=U(F_n)\cong\prod_jU(d_{n,j})
$$

are increasing. Their union is norm dense in $U(A)$, by approximating
a unitary in $F_n$ and taking its polar part.
Under (i), the minimum block size tends to infinity.
{prf:ref}`lem-un-product-concentration` shows that the Haar measures
of $K_n$, viewed in $U(A)$, form a Lévy sequence. This is
(ii). For completeness, any increasing sequence of compact groups
with dense union has asymptotically invariant Haar measures in the
UEB topology: given $u\in U(A)$, approximate it by $v\in K_m$.
For $n\geq m$, Haar invariance under $v$, together with
$\left\lVert ux-vx\right\rVert=\left\lVert u-v\right\rVert$, bounds the error by the common
continuity modulus. The concentration criterion {cite}`Schneider2019`, Corollary 5.7 proves
(ii)$\Rightarrow$(iii), and (iii) implies (iv).

If $\pi:A\to M_d$ is a nonzero irreducible finite-dimensional
representation, its image is $M_d$. Its unitary map is onto:
every matrix unitary is $e^{ih}$, and a selfadjoint lift of $h$
can be exponentiated in $A$.
Thus $U(A)$ has a continuous surjection onto the nontrivial
compact group $U(d)$. Its translation action has no fixed point,
contradicting (iv). Any nonzero finite-dimensional representation
has an irreducible summand. This proves (iv)$\Rightarrow$(i).
:::

The concentration arguments for the UHF and fixed-width AF examples
treated in {cite}`EFHKKL2016`, Proposition 5.1 are special cases.
Here the number of summands at the $n$-th stage may grow arbitrarily
fast. An estimate obtained by a union bound over those summands
would not suffice; the tensorized concentration bound does.

### Automorphisms and the scaled dimension group

For every separable unital AF algebra $A$, Elliott classification and
finite-dimensional uniqueness give a surjection

$$
q_A:\operatorname{Aut}(A)\longrightarrow\Gamma_A=\operatorname{Aut}(\mathsf D_A),\qquad
 q_A(\alpha)=K_0(\alpha),
$$ (eq-un-af-quotient)

with kernel

$$
N_A=\overline{\operatorname{Inn}(A)}
 =\overline{\{\operatorname{Ad}(u):u\in U(A)\}}
$$

{cite}`Elliott1976`; see also {cite}`Blackadar1998`, Exercise 7.7.5. In particular the inner groups used in
this formula are not equipped with their discrete topology.

:::{prf:proposition}
:label: prop-un-af-quotient

The map {eq}`eq-un-af-quotient` is continuous and open.
Its target is a non-Archimedean Polish group. Its kernel is always
amenable. If $A$ has no nonzero finite-dimensional representations,
that kernel is whirly amenable in the point-norm topology.
:::

:::{prf:proof}
Represent $K_0$-classes by projections in matrix algebras over $A$.
Sufficiently close projections are equivalent, so their classes are
locally constant under point-norm changes in the automorphism.
This proves continuity.
The countable dimension group, with its addition, order and distinguished unit,
is a countable structure; its automorphism group is a closed
permutation group. Surjectivity and the kernel description are
the existence and uniqueness parts of AF classification. The
Polish open mapping theorem gives openness.

The unitary group $U(A)$ is the norm closure of an
increasing union of compact finite-dimensional unitary groups,
and hence is amenable. Passing through the adjoint map and taking its
closure proves amenability of $N_A$. When $A$ has no nonzero
finite-dimensional representations, use
{prf:ref}`thm-un-af-unitary` and the continuous adjoint map
$U(A)\to N_A$, whose image is dense. {prf:ref}`prop-un-dynamical-inputs`1
gives whirly amenability of $N_A$.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-un-main-af`.* Combine {prf:ref}`prop-un-af-quotient` with
{prf:ref}`prop-un-dynamical-inputs`2;
for the whirly-amenability criterion also use
{prf:ref}`prop-un-dynamical-inputs`4.
If $A$ is simple, unital and infinite dimensional, any nonzero
finite-dimensional representation would be injective, which is
impossible; thus the representation hypothesis holds.
:::

:::{prf:corollary}
:label: cor-un-af-consequences

For the unital AF algebras in {prf:ref}`thm-un-main-af`,

$$
b\operatorname{Aut}(A)\cong b\Gamma_A,\qquad
\operatorname{Aut}(A)\text{ amenable}\ \Longleftrightarrow\
\Gamma_A\text{ amenable}.
$$

In every compact $\operatorname{Aut}(A)$-flow $X$, an invariant regular
probability measure has support in $X^{N_A}$, and the action on its
support descends to $\Gamma_A$ through $q_A$.
If $\Gamma_A$ is compact, $M(\operatorname{Aut}(A))$ is its translation
flow through $q_A$. If $\Gamma_A$ is infinite discrete, that
UMF is nonmetrizable.
:::

:::{prf:proof}
Apply {prf:ref}`prop-un-dynamical-inputs`2–3.
:::

### Finite-dimensional algebras and finite sums of simple algebras

:::{prf:lemma}
:label: lem-un-finite-af

Let $A$ be finite dimensional and write
$A=\bigoplus_{d\in J}M_d(\mathbb C)^{m_d}$, where $J$ is a finite set of
distinct positive integers. Then

$$
\operatorname{Aut}(A)\cong
 \prod_{d\in J}\left(\operatorname{PU}(d)^{m_d}
                    \rtimes\operatorname{Sym}(m_d)\right)
$$

topologically, and in particular $\operatorname{Aut}(A)$ is compact.
:::

:::{prf:proof}
An automorphism permutes isomorphic simple summands. On each
matrix summand it is inner, with unitary implementer unique up
to a scalar. This gives the indicated continuous isomorphism;
both sides are compact Hausdorff.
:::

The finite-dimensional case of the next proposition then returns
$M(\operatorname{Aut}(A))=\operatorname{Aut}(A)$ itself, a compact group acting on itself by left
translation.

:::{prf:proposition} Finite sums of simple unital AF algebras
:label: prop-un-finite-simple-sum

Let

$$
A=\bigoplus_{t=1}^s B_t^{m_t}
$$

where the $B_t$ are pairwise nonisomorphic simple unital AF
algebras. Define

$$
R_t=
 \begin{cases}
 \operatorname{PU}(d),& B_t=M_d(\mathbb C),\\
 \operatorname{Aut}(\mathsf D_{B_t}),& B_t\text{ infinite dimensional}.
 \end{cases}
$$

There is an open continuous quotient with whirly amenable kernel
from $\operatorname{Aut}(A)$ onto

$$
R_A=\prod_{t=1}^s (R_t^{m_t}\rtimes\operatorname{Sym}(m_t)).
$$

Thus $M(\operatorname{Aut}(A))=q^*M(R_A)$.
If all the $R_t$ are compact, the answer is $R_A$ itself.
:::

:::{prf:proof}
Permuting isomorphic simple summands identifies
$\operatorname{Aut}(A)=\prod_t(\operatorname{Aut}(B_t)^{m_t}\rtimes\operatorname{Sym}(m_t))$.
For an infinite-dimensional $B_t$, take the dimension-group
quotient from {prf:ref}`thm-un-main-af`; for a matrix algebra,
take its identity quotient, $\operatorname{Aut}(M_d(\mathbb C))=\operatorname{PU}(d)$ being
{prf:ref}`lem-un-finite-af`.
Their product respects the permutations. Its kernel is a finite
product of whirly amenable groups, hence whirly amenable by
{prf:ref}`prop-un-dynamical-inputs`1.
It is open, and {prf:ref}`prop-un-dynamical-inputs`2 applies.
:::

(sec-un-af-gap)=
## What remains for arbitrary separable unital AF automorphisms

The representation hypothesis in {prf:ref}`thm-un-af-unitary` has an
exact meaning for unitary groups. For automorphism groups it is a
sufficient hypothesis for discarding the approximately inner kernel,
but it is not necessary. Commutative AF algebras have trivial inner
groups, despite having many characters. At the other extreme,
matrix algebras retain nontrivial compact inner groups.
In general these behaviours occur over a nontrivial space of ideals.

:::{prf:proposition} A finite-dimensional obstruction in the kernel
:label: prop-un-fd-obstruction

If a unital AF algebra $A$ has an irreducible representation
$\pi:A\to M_d$ with $d\geq2$, then $N_A=\overline{\operatorname{Inn}(A)}$
has a continuous surjection onto $\operatorname{PU}(d)$.
In particular $N_A$ is not extremely amenable.
:::

:::{prf:proof}
Every inner automorphism preserves $I=\ker\pi$.
A point-norm limit of inner automorphisms, and its inverse, preserve
$I$, so every element of $N_A$ induces an automorphism of $A/I$.
This gives a continuous map $N_A\to\operatorname{Aut}(M_d)=\operatorname{PU}(d)$:
to test convergence on a matrix, choose any lift in $A$.
It is onto because every matrix unitary lifts to a unitary of $A$,
by lifting a selfadjoint logarithm and exponentiating.
A nontrivial compact translation quotient prevents extreme amenability.
:::

Even this obstruction does not describe all residual dynamics of
$N_A$. A basic test class is a continuous matrix bundle over a
zero-dimensional compact space.

:::{prf:proposition} The homogeneous AF test class
:label: prop-un-gauge

Let $X$ be a nonempty compact metrizable zero-dimensional space
and $d\geq2$. For $A=C(X,M_d)$, one has topological isomorphisms

$$
\operatorname{Aut}(A)\cong C(X,\operatorname{PU}(d))\rtimes\operatorname{Homeo}(X),
 \qquad
 \Gamma_A\cong\operatorname{Homeo}(X),
$$

and $N_A=C(X,\operatorname{PU}(d))$.
The function group has the uniform topology, and the homeomorphism
group has the compact-open topology.
:::

:::{prf:proof}
The action of an automorphism on the centre $C(X)$ specifies a
homeomorphism. After composing with its inverse action on the base,
the automorphism acts fiberwise by a continuous map
$X\to\operatorname{Aut}(M_d)=\operatorname{PU}(d)$.
Continuity can be tested on a finite matrix-unit basis, which also
identifies the uniform topology on this kernel with its point-norm
topology on $A$.
Conversely these data give an automorphism, continuously in both
coordinates, with multiplication given by the indicated semidirect
product.
The dimension group is $C(X,\mathbb Z)$ with pointwise order and order
unit the constant function $d$. Its order-unit automorphisms are
the homeomorphisms of $X$: they preserve the unique element $1$
with $d1=u$, and hence the Boolean algebra of characteristic
functions in the interval $[0,1]$. Stone duality gives the claim.
Finally, finite locally constant $\operatorname{PU}(d)$-valued
maps lift to unitary-valued maps. They are uniformly dense in
$C(X,\operatorname{PU}(d))$, by zero dimensionality and compactness.
They act by inner automorphisms, proving the kernel assertion.
:::

When $X$ is infinite, the uniform function group in
{prf:ref}`prop-un-gauge` is not compact. Choose infinitely
many pairwise disjoint nonempty clopen subsets of $X$, and
functions taking a fixed nonidentity value on one of them and
the identity elsewhere. They are uniformly separated.
Thus the residual issue cannot in general be handled merely by
adjoining a finite-dimensional compact inner factor.

:::{prf:remark} Question
:label: rem-un-general-af

Compute the universal minimal flow of $\operatorname{Aut}(A)$ for every separable
unital AF algebra that has finite-dimensional representations.
Already for $A=C(X,M_d)$, find an effective description of

$$
M\bigl(C(X,\operatorname{PU}(d))
             \rtimes\operatorname{Homeo}(X)\bigr)
$$

for arbitrary compact metrizable zero-dimensional $X$.
Describe how this information combines with the dimension-group
quotient in a general Bratteli system.
:::

Thus Problem {prf:ref}`rem-un-general-af` is precisely the part of the
arbitrary-unital-AF case not covered by {prf:ref}`thm-un-main-af`;
the general realisation of a UMF as a minimal Samuel subflow does
not resolve this AF-specific problem.

(sec-un-encyclopaedia-proofs)=
## Proofs of statements in [](#sec-operator-algebras)

:::{prf:proof}
*Proof of {prf:ref}`thm-lupini-unital`.* This is part of {prf:ref}`thm-un-main-kirchberg`.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-lupini-af`.* The first assertions, including the case of infinite-dimensional simple
separable unital AF algebras, are {prf:ref}`thm-un-main-af`. Let
$A=M_d(\mathbb{C})$ with $d\geq2$. Its scaled dimension group is
$(\mathbb{Z},\mathbb{Z}_{\geq0},d)$, whose only automorphism is the identity,
so $\Gamma_A$ is trivial. Every automorphism of $M_d(\mathbb{C})$ is inner, so
$\mathrm{Aut}(A)=PU(d)$, and {prf:ref}`prop-un-finite-simple-sum`, with
a single summand, gives $M(\mathrm{Aut}(A))\cong PU(d)$, which is not a
point.
:::
