(sec-proofs-stable-kirchberg)=
# Proofs: stable Kirchberg algebras and norm-unitary groups

This section reproduces, from the preprint of the editor {cite}`LupiniStable2026` in its version of 15 September 2026, the
proofs of the results stated in [](#sec-operator-algebras). The text is that of the
preprint, with British spelling: its sections appear as subsections, its macros
are expanded and its labels renamed, and of its introduction only the
statements of the main results are kept. Citations of the companion preprints
point to their own proof pages where the cited statement is reproduced there.
The preprint has not been refereed. The last subsection derives the statements
of [](#sec-operator-algebras) from those of the preprint.

(sec-st-main-results)=
## Main results of the preprint

:::{prf:theorem}
:label: thm-st-kk

Let $A$ be a stable Kirchberg algebra, with no UCT
assumption, and put

$$
\begin{aligned}
 \mathsf G_A&=\operatorname{Aut}(A), & J_A&=\{\alpha:KK(\alpha)=1\},\\
 \operatorname{Inn}_M(A)&=\{\operatorname{Ad}(u):u\in U(M(A))\}, &
 N_A&=\overline{\operatorname{Inn}_M(A)}.
 \end{aligned}
$$

Then $J_A$ is the identity path component of $\mathsf G_A$, it is a Borel Polish
subgroup of $\mathsf G_A$, and $\overline{J_A}=N_A$. The natural map identifies $\mathsf G_A/J_A$ definably with $KK(A,A)^\times$ in its witnessed Cuntz
presentation. The homomorphism

$$
\kappa_A:\mathsf G_A\longrightarrow R_A^\times,\qquad  \alpha\longmapsto[\alpha]_{KL},
$$

is continuous, open, and surjective, with whirly amenable kernel $N_A$.
Thus $R_A^\times$ is the maximal Hausdorff quotient of $\mathsf G_A/J_A$ with its
quotient topology, and

$$
M(\mathsf G_A)\cong\kappa_A^*M(R_A^\times),\qquad b\mathsf G_A\cong bR_A^\times.
$$ (eq-st-main-kl)

Moreover, $\mathsf G_A$ is whirly amenable if and only if $R_A^\times$ is whirly
amenable.
:::

:::{prf:theorem}
:label: thm-st-nuclear-norm

If $C$ is unital and nuclear, $V_{C\otimes\mathcal K}$ is whirly amenable in
norm, and

$$
M(U((C\otimes\mathcal K)^+))\cong\mathbb T\times M(K_1(C)).
$$

The action is through scalar evaluation and the stable component class.
For arbitrary unital $C$, put $B=C\otimes\mathcal K$. Nuclearity of $B$ is equivalent to norm
amenability of $U(B^+)$, and to amenability, extreme amenability, or
whirly amenability of $U_1(B)_0$.
:::

:::{prf:theorem}
:label: thm-st-geometric

Let $B$ be a stable Kirchberg algebra such that $\operatorname{Aut} (B)$ is extremely amenable. For a nonempty finite set $I$, for $\mathbb{N}$,
and for the Cantor set $X$, respectively,

$$
\begin{aligned}
M(\operatorname{Aut}(c_0(I,B)))&\cong\operatorname{Sym}(I), \\
M(\operatorname{Aut}(c_0(\mathbb{N},B)))&\cong\operatorname{LO}(\mathbb{N}), \\
M(\operatorname{Aut}(C(X)\otimes B))&\cong\Phi(X).
\end{aligned}
$$

Their Bohr compactifications are

$$
\begin{aligned}
b\operatorname{Aut}(c_0(I,B))&\cong\operatorname{Sym}(I), \\
b\operatorname{Aut}(c_0(\mathbb{N},B))&=1, \\
b\operatorname{Aut}(C(X)\otimes B)&=1.
\end{aligned}
$$

The actions are induced by the permutations of summand ideals and the
homeomorphisms of $X$. In particular the formulas apply to both $B=\mathcal{O}_2\otimes\mathcal{K}$ and $B=\mathcal{O}_3\otimes\mathcal{K}$. Here $\operatorname{LO}(\mathbb{N})$ is the space of linear orders, and $\Phi(X)$ the space of
maximal chains of nonempty closed subsets. The computations also hold after
unitisation. The groups $\operatorname{Aut}(c_0(I,B))$, for finite nonempty $I$ and for $I=\mathbb{N}$, are amenable and their universal minimal flows are uniquely
ergodic; on $\operatorname{LO}(\mathbb{N})$ the unique measure is the uniform random-order
measure. In contrast, $\operatorname{Aut}(C(X)\otimes B)$ is nonamenable. Thus the two
infinite geometric groups are both minimally almost periodic, although only
the direct-sum group is amenable. The direct-sum Bohr conclusion also extends beyond this class: {prf:ref}`cor-st-direct-sum-bohr-general`
computes it for every nonzero simple stable $C^*$-algebra $C$ and every index set $I
$. It is $(b\operatorname{Aut}(C))^I\rtimes\operatorname{Sym}(I)$ for finite $I$ and trivial for
infinite $I$, without separability, nuclearity, or amenability assumptions. Moreover, amenability of $\operatorname{Aut}(C)$ implies amenability of the
direct-sum automorphism group.
:::

:::{prf:theorem}
:label: thm-st-stable-stabilizer

Let $A$ be a stable Kirchberg algebra,
without UCT, and let $\varphi$ be a pure state. Then

$$
\operatorname{Aut}(A,\varphi)\cap N_A
$$

is whirly amenable. Restriction of the quotient map to $H_\varphi=\operatorname{Aut} (A,\varphi)$ is an open surjection onto $Q_A=\operatorname{Aut}(A)/N_A\cong KL(A,A)^\times$, and

$$
M(H_\varphi)\cong(q_A|_{H_\varphi})^*M(Q_A),\qquad  bH_\varphi\cong bQ_A.
$$

In particular, restricting $M(\operatorname{Aut}(A))$ to $H_\varphi$ gives its universal
minimal flow.
The groups $H_\varphi$, $\operatorname{Aut}(A)$, and $Q_A$ are simultaneously whirly
amenable. Under UCT, this occurs exactly when $Q_A$ is trivial.
:::

(sec-st-dynamics)=
## Minimal flows and whirly amenable kernels

 All compact spaces are nonempty and Hausdorff. A $G$-flow is a compact space with a jointly continuous $G$-action. It is minimal
if every orbit is dense. Every flow contains a minimal subflow, by
compactness and Zorn's lemma. The universal minimal flow exists and is
unique up to equivariant homeomorphism. A group is extremely amenable if
every compact flow has a fixed point, equivalently if its universal minimal
flow is a singleton.

Call a topological group *whirly* if every invariant regular Borel
probability measure in every continuous action on a compact Hausdorff space
has support contained in the fixed-point set. It is *whirly amenable*
if it is also amenable; the terminology is Schneider's
{cite}`Schneider2019`, Corollary 5.7. Whirly amenability implies extreme amenability,
since amenability provides an invariant probability measure and its
nonempty support consists of fixed points. Whirliness alone does not imply
amenability {cite}`HollSchneider2026`.

We use the following *dense-image principle*. If a continuous
homomorphism $f:H\to G$ has dense image, then amenability, extreme
amenability and whirliness pass from $H$ to $G$. Indeed, restrict
any compact $G$-flow to $H$. By continuity and density, every
$H$-fixed point is $G$-fixed, and every $H$-invariant regular
probability is $G$-invariant. These observations prove the first two
assertions. If $H$ is whirly, a $G$-invariant regular probability
has support fixed by $H$, hence by $G$, proving the third.
In particular, whirly amenability passes to continuous dense images.

:::{prf:lemma}
:label: lem-st-products

Finite products of extremely amenable groups are
extremely amenable. A group with a dense directed union of extremely
amenable subgroups is extremely amenable. Consequently arbitrary products,
with the product topology, preserve extreme amenability.
The same statements hold for whirly amenability.
:::

:::{prf:proof}
For an $E\times F$-action on $X$, the nonempty closed set $\operatorname{Fix}_E(X)$ is $F$-invariant and contains an $F$-fixed point. Induction gives finite products.
For a directed family $(E_j)$, the nonempty closed sets $\operatorname{Fix}_{E_j}(X)$ have
the finite intersection property. A point in their intersection is fixed by
the dense union, hence by the whole group. Apply this to the subgroups
supported on finitely many coordinates of an arbitrary product.
For whirly amenability, the preceding argument supplies extreme amenability
and hence amenability. If $\mu$ is an invariant regular probability measure
on a compact action, its support is fixed by each whirly amenable factor or
subgroup. It is therefore fixed by the subgroup they generate and its
closure, proving whirliness in every case.
:::

A Polish group is a *Lévy group* if it has increasing compact
subgroups with dense union whose Haar probabilities form a concentrating
family for its group uniformity. Every Polish Lévy group is whirly
amenable by {cite}`GlasnerTsirelsonWeiss2005`, Theorem 1.1 and Remark 1.4, and hence extremely
amenable. We will use the following finite-dimensional input.

The matrix concentration input is the classical Haar concentration
on $U(n)$. Its Hilbert–Schmidt form is recorded in
{prf:ref}`lem-st-unitary-levy`, and implies operator-norm concentration.

:::{prf:lemma}
:label: lem-st-nonarch-whirly

A Polish non-Archimedean group is whirly
amenable if and only if it is trivial.
:::

:::{prf:proof}
A Polish non-Archimedean group $Q$ has a faithful continuous permutation
action on a countable discrete set $D$: take the disjoint union of the
countable coset spaces for a countable basis of open subgroups. Its induced
action on $\{0,1\}^D$ is jointly continuous and preserves the fair product
probability measure, which has full support. Whirliness would force every
configuration to be fixed, so the faithful action and $Q$ must be trivial.
The converse is immediate.
:::

:::{prf:proposition}
:label: prop-st-transfer

The minimal-flow assertion is {prf:ref}`lem-cu-kernel`; the additional consequences are recorded together here. Let $q:G\to Q$ be a continuous open surjective
homomorphism, and suppose $N=\ker q$ is extremely amenable. Every minimal $G$-flow factors through $q$, and

$$
M(G)\cong q^*M(Q).
$$ (eq-st-transfer)

Consequently, $G$ is extremely amenable, respectively amenable, if and only
if $Q$ is, and $M(G)$ is metrizable if and only if $M(Q)$ is metrizable. The
universal minimal flow of $G$ carries a unique invariant probability measure
if and only if that of $Q$ does. Moreover, writing $bG$ for the Bohr
compactification, $q$ induces an isomorphism

$$
bG\cong bQ.
$$ (eq-st-transfer-bohr)

If, in addition, $N$ is whirly amenable, then $G$ is whirly amenable if and
only if $Q$ is whirly amenable.
:::

:::{prf:proof}
For a minimal $G$-flow $X$, $\operatorname{Fix}_N(X)$ is nonempty and closed. Normality
makes it invariant: for $n\in N$, $g\in G$, and $x\in\operatorname{Fix}_N(X)$, $n(gx)=g(g^{-1}ng)x=gx$. Minimality implies $\operatorname{Fix}_N(X)=X$. The descended
action on $Q\times X$ is continuous because $q\times\mathrm{id}_X$ is an
open quotient map. Conversely a minimal $Q$-flow remains minimal after
pullback. Factor maps are unchanged, proving universality in {eq}`eq-st-transfer`. The assertions about extreme amenability and
metrizability are immediate. A group is amenable exactly when its universal
minimal flow carries an invariant regular probability measure: such a
measure maps onto a minimal subflow of any compact action. Under {eq}`eq-st-transfer`, invariance under $G$ is the same as invariance under $Q$, which also proves the unique-measure assertion.

Finally, let $f:G\to C$ be a continuous homomorphism into a compact group.
The closure of $f(N)$, with the left-translation action pulled back to $N$,
is a compact minimal $N$-flow. Extreme amenability forces it to be trivial.
Thus $f$ factors continuously through the open quotient $q$, and {eq}`eq-st-transfer-bohr` follows from the universal property of the Bohr
compactification.
For the additional assertion, the forward implication follows by pulling
compact actions and invariant measures back from $Q$; amenability also
passes to quotients. Conversely, suppose $N$ and $Q$ are whirly amenable.
The preceding amenability equivalence makes $G$ amenable. For an invariant
regular probability measure $\mu$ on a compact $G$-flow $X$, whirliness of
$N$ gives $\operatorname{supp}\mu\subseteq X^N$. This closed $G$-invariant subspace
carries a continuous $Q$-action, and $\mu$, viewed as a regular probability
on $X^N$, is $Q$-invariant. Whirliness of $Q$ therefore gives
$\operatorname{supp}\mu\subseteq (X^N)^Q=X^G$.
:::

:::{prf:lemma}
:label: lem-st-amenable-extensions

Let $N$ be a closed normal subgroup of a
topological group $G$. If $N$ and $G/N$ are amenable, then $G$ is amenable.
:::

:::{prf:proof}
Let $G$ act continuously on a compact space $X$. Amenability of $N$ makes
the compact convex set

$$
\mathcal{P}(X)^N=\{\mu\in\mathcal{P}(X):n\mu=\mu\text{ for all }n\in N\}
$$

nonempty. Normality makes it $G$-invariant, and $N$ acts trivially on it, so
the continuous affine action factors through $G/N$. Amenability of $G/N$, in
its equivalent affine fixed-point form, gives a fixed point in $\mathcal{P}(X)^N$. This is a $G$-invariant probability measure on $X$.
:::

:::{prf:lemma}
:label: lem-st-amenable-products

A topological group with a dense directed
union of amenable subgroups is amenable. Consequently arbitrary products of
amenable topological groups are amenable.
:::

:::{prf:proof}
Let $(H_j)$ be directed with dense union in $G$, and let $G$ act
continuously on a compact space $X$. The nonempty closed subsets $\mathcal{P}(X)^{H_j}$ of $H_j$-invariant probability measures have the finite
intersection property. A measure in their intersection is fixed by the dense
union and hence by $G$.

Finite products of amenable groups are amenable by repeated application of
{prf:ref}`lem-st-amenable-extensions`. In an arbitrary product, the
finite-coordinate subgroups form a dense directed union of such finite
products, so the first assertion applies.
:::

Call a topological group *minimally almost periodic* if its Bohr
compactification is trivial. Equivalently, it has no nontrivial continuous
finite-dimensional unitary representation.

:::{prf:corollary}
:label: cor-st-finite-dimensional-representations

Under the hypotheses of
{prf:ref}`prop-st-transfer`, pullback along $q$ gives an equivalence
between the categories of continuous finite-dimensional unitary
representations of $Q$ and of $G$. In particular,

$$
G\text{ is minimally almost periodic}  \quad\Longleftrightarrow\quad  Q\text{
is minimally almost periodic}.
$$
:::

:::{prf:proof}
If $\pi:G\to U(n)$ is continuous, the closure of $\pi(N)$, with its
left-translation action pulled back to $N$, is a compact minimal $N$-flow.
Thus $\pi(N)=1$, and $\pi$ factors uniquely and continuously through the
open quotient $q$. The converse and the assertion about intertwiners follow
from surjectivity of $q$.
:::

:::{prf:lemma}
:label: lem-st-minap-tools

The following statements hold.

1. An arbitrary product of minimally almost periodic groups is minimally
   almost periodic.
2. Suppose that $H$ is a dense subgroup of $G$ and that, for every $h\in H
$, there are $g_n\in G$ such that $g_nhg_n^{-1}\to1$. Then $G$ is minimally
   almost periodic.
:::

:::{prf:proof}
For (i), let $\pi:\prod_iG_i\to U(n)$ be continuous. Choose an identity
neighbourhood in $U(n)$ containing no nontrivial subgroup. The preimage
contains a basic product neighbourhood, so $\pi$ is trivial on every
coordinate group outside a finite set. It therefore factors through a finite
product, where it is trivial on each factor.

For (ii), unitary invariance of the operator norm gives

$$
\|\pi(h)-1\|=\|\pi(g_nhg_n^{-1})-1\|\longrightarrow0
$$

for every continuous finite-dimensional unitary representation $\pi$. Thus $\pi$ is trivial on $H$, and hence on $G$. The Peter–Weyl theorem identifies
this with triviality of the Bohr compactification.
:::

:::{prf:lemma}
:label: lem-st-bohr-finite-products

For finitely many topological groups $G_1,\ldots,G_n$, the canonical map induces

$$
b(G_1\times\cdots\times G_n)\cong bG_1\times\cdots\times bG_n.
$$
:::

:::{prf:proof}
It is enough to consider two factors. Given a continuous homomorphism $f:G_1\times G_2\to K$ into a compact group, the restrictions to the two
factors have commuting images. Their extensions to $bG_1$ and $bG_2$ still
have commuting images, by density, and their product is the unique
continuous extension of $f$ to $bG_1\times bG_2$. The universal property and
induction prove the assertion.
:::

:::{prf:corollary}
:label: cor-st-wreath-minap

For every topological group $E$ and every infinite
set $I$, with the product topology on $E^I$ and the pointwise topology on $\operatorname{Sym}(I)$,

$$
E^I\rtimes\operatorname{Sym}(I)
$$

is minimally almost periodic. Here $\operatorname{Sym}(I)$ permutes the coordinates of $E^I
$.
:::

:::{prf:proof}
The subgroup $E^{(I)}\rtimes\operatorname{Sym}_{\mathrm{fin}}(I)$ is dense. Each of its
elements is supported on a finite set of coordinates. Conjugating by
permutations that move this support through pairwise disjoint finite subsets
of $I$ makes the conjugates converge to the identity in the product and
pointwise topologies. Apply {prf:ref}`lem-st-minap-tools`(ii).
:::

The canonical quotient map by a closed normal subgroup is open. For Polish
groups, the quotient is again Polish.

For compact $C$, minimal flows are homogeneous translation quotients,
and the compact-factor rule from {prf:ref}`lem-cu-kernel` gives

$$
M(C\times L)=C\times M(L).
$$ (eq-st-compact-product)

The Bohr counterpart follows from {prf:ref}`lem-st-bohr-finite-products`:

$$
b(C\times L)=C\times bL.
$$ (eq-st-compact-product-bohr)

:::{prf:lemma}
:label: lem-st-locally-compact-umf

For a locally compact Polish group $L$, the
universal minimal flow $M(L)$ is metrizable if and only if $L$ is compact.
:::

:::{prf:proof}
The action of a locally compact group on its universal minimal flow is free;
see the discussion following Corollary 3.9 in {cite}`BYMT2017`. Thus, if $M(L)$
is metrizable, {cite}`BYMT2017`, Corollary 3.9 implies that $L$ is compact. The
converse follows from the compact-group facts recalled above.
:::

:::{prf:corollary}
:label: cor-st-compact-quotient-minimal

Under the hypotheses of {prf:ref}`prop-st-transfer`, suppose in addition that $Q$ is compact. Then every minimal
$G$-flow is, through $q$, a homogeneous space $Q/L$ for a closed subgroup $L\leq Q$. In particular, every minimal $G$-flow is equicontinuous and
uniquely ergodic, and

$$
M(G)\cong Q,\qquad bG\cong Q.
$$
:::

:::{prf:proof}
{prf:ref}`prop-st-transfer` makes every minimal $G$-flow a minimal $Q$-flow. The compact-group facts recalled above give the dynamical properties and the
formula for $M(G)$; the Bohr formula follows from {eq}`eq-st-transfer-bohr`
and $bQ\cong Q$.
:::

We also use the Polish open mapping theorem: a continuous surjective
homomorphism between Polish groups is open {cite}`BeckerKechris1996`. The
point-norm automorphism group of a separable $C^*$-algebra is Polish; a
complete compatible metric is obtained by testing automorphisms and their
inverses on a countable dense subset of its unit ball. Checking openness
will ensure that the algebraic quotients below carry precisely the required
topology.

(sec-st-kernel)=
## The approximately inner subgroup

 For nonunital $A$, write $M(A)$ for the multiplier
algebra and $A^+$ for the minimal unitisation. The strict topology on $M(A)$
is generated by

$$
u\longmapsto\left\|ua\right\|+\left\|au\right\|\qquad(a\in A).
$$

Its restriction makes $U(M(A))$ a topological group. Set

$$
\operatorname{Inn}_M(A)=\{\operatorname{Ad}(u):u\in U(M(A))\},\qquad  N_A=\overline{\operatorname{Inn}_M(A)}.
$$

This notation fixes the implementer convention for nonunital algebras.

The stable nuclear norm-unitary theorem proved in
[](#sec-st-unitaries) gives the multiplier conclusion through
strict approximation. Its proof uses stable uniqueness and Haar
concentration and does not depend on the present section.

:::{prf:theorem} Strict multiplier unitaries
:label: thm-st-multiplier-whirly

If $B$ is unital, separable, simple, and
nuclear, put $A=B\otimes\mathcal K$. The inclusion

$$
\bigl(U_1(A)_0\bigr)_{\|\cdot\|}\longrightarrow U(M(A))_{\mathrm{strict}}
$$

is continuous with dense image. The target is a Polish group and is
whirly amenable, hence extremely amenable.
:::

:::{prf:proof}
The strict multiplier-unitary group is Polish because $A$ is separable,
and norm convergence implies strict convergence. Cuntz–Higson's Kuiper
theorem makes $U(M(A))$ norm contractible {cite}`CuntzHigson1987`. Thus every
$u\in U(M(A))$ is a finite product
$u=\prod_{j=1}^k\exp(ih_j)$, with $h_j=h_j^*\in M(A)$.
Let $e_n=1_B\otimes\sum_{\ell=1}^n e_{\ell\ell}$ be the canonical
projection approximate identity of $A$. For each $j$,
$e_nh_je_n\to h_j$ strictly and $\|e_nh_je_n\|\leq\|h_j\|$.
Multiplication is jointly strictly continuous on bounded sets, so
polynomial approximation to the exponential gives

$$
u_n:=\prod_{j=1}^k\exp(ie_nh_je_n)\longrightarrow u
 \qquad\text{strictly}.
$$

The path $t\mapsto\prod_{j=1}^k\exp(it e_nh_je_n)$ lies in $U_1(A)$
and joins $1$ to $u_n$. Hence $u_n\in U_1(A)_0$, proving density.
{prf:ref}`thm-st-v` makes $U_1(A)_0$ whirly amenable in norm.
The dense-image principle now gives the assertion for the strict group.
:::

:::{prf:remark}
:label: rem-st-remark-1

The strict-density argument above uses stability and the canonical
projection approximate identity; nuclearity enters only through
{prf:ref}`thm-st-v`. Ng–Ruiz establish strict AF approximation and
unitary density {cite}`NgRuiz2012`, Theorem 3.3 and Proposition 4.1(vi).
The proof here obtains whirly amenability directly from the norm group.
Whether a concentrating family of compact subgroups realises the strict
multiplier group as a Lévy group requires a separate construction.
:::

:::{prf:lemma}
:label: lem-st-adjoint

The homomorphism $\operatorname{Ad}:U(M(A))_{\mathrm{strict}}\to\operatorname{Aut}(A)
$ is continuous, and $N_A$ is closed and normal.
:::

:::{prf:proof}
For unitaries $u,v$ and $a\in A$,

$$
uau^*-vav^*=(u-v)au^*+va(u^*-v^*),
$$

whence

$$
\left\|uau^*-vav^*\right\|
\leq\left\|(u-v)a\right\|+\left\|(u-v)a^*\right\|.
$$

This proves continuity. Every $\alpha\in\operatorname{Aut}(A)$ extends uniquely to $\widetilde\alpha\in\operatorname{Aut}(M(A))$, and $\alpha\operatorname{Ad}(u)\alpha^{-1}=\operatorname{Ad} (\widetilde\alpha(u))$. Thus the image and its closure are normal.
:::

:::{prf:theorem}
:label: thm-st-kernel-ea

If $A\cong B\otimes\mathcal{K}$ for a unital separable
simple nuclear algebra $B$, then $N_A$ is whirly amenable. In particular
for every stable Kirchberg algebra, without a UCT assumption, $N_A$ is
whirly amenable, and

$$
M(\operatorname{Aut}(A))\cong M(\operatorname{Aut}(A)/N_A)
$$ (eq-st-general-quotient)

with the quotient action.
:::

:::{prf:proof}
{prf:ref}`thm-st-multiplier-whirly` and {prf:ref}`lem-st-adjoint` and the dense-image principle prove
the first assertion. A stable Kirchberg algebra contains a nonzero
projection $p$. Simplicity makes it full, and $B=pAp$ is unital, separable,
simple, and nuclear. Brown's full hereditary subalgebra theorem {cite}`Brown1977`, Theorem 2.8
gives $B\otimes\mathcal{K}\cong A\otimes\mathcal{K}\cong A$. Apply the first
assertion to obtain whirly amenability of $N_A$.

Finally,
{prf:ref}`prop-st-transfer` gives the quotient-flow formula. A second
argument for whirliness of $N_A$ in the Kirchberg case is recorded
in {prf:ref}`rem-st-alternative-whirly` below.
:::

:::{prf:remark}
:label: rem-st-no-norm

The adjoint map here has the strict topology on its
multiplier-unitary source and point-norm convergence on its automorphism
target. The norm-topology assertion used in its proof concerns the
scalar-one identity component $U_1(A)_0$, as stated in
{prf:ref}`thm-st-v`. Passing to a finer group topology enlarges the class
of continuous compact actions.
:::

(sec-st-definable-kk)=
## Definable $KK$-units and the Hausdorff
quotient

 Throughout this section $A$ is a stable Kirchberg
algebra; no UCT assumption is made. We use the degree-zero Kasparov group
and the composition convention for its product, so that $\alpha\mapsto
KK(\alpha)$ is a homomorphism on automorphism groups. Put

$$
\mathsf G_A=\operatorname{Aut}(A),\qquad  J_A=\{\alpha\in \mathsf G_A:KK(\alpha)=1\},\qquad
R_A=KL(A,A)=KK(A,A)/\overline{\{0\}}.
$$

The closure of zero is taken in the natural topology on $KK(A,A)$. It is an
ideal by continuity of multiplication. Dadarlat proves that $R_A$ is a
Polish additive group and that Kasparov products are continuous
{cite}`Dadarlat2005`, Proposition 2.8 and Theorem 3.5. Point-norm convergence
of homomorphisms induces convergence of their classes: if
$\varphi_n\to\varphi$ point-norm, then
$a\mapsto(\varphi_n(a))_{n\in\overline{\mathbb N}}$, with $\varphi(a)$ in
the coordinate at infinity, is a $^*$-homomorphism into
$C(\overline{\mathbb N})\otimes B$, so {cite}`Dadarlat2005`, Theorem 3.3 gives
$[\varphi_n]\to[\varphi]$.

### The topology and realisation of $KL$-units

For a unital Polish topological ring $R$, endow $R^\times$ with the topology
of the inverse-pair space

$$
\{(x,y)\in R\times R:xy=yx=1\}, \qquad x\longleftrightarrow(x,x^{-1}).
$$ (eq-st-inverse-pair)

The displayed space is closed in $R^2$. Multiplication is $(x,y)(x^{\prime
},y^{\prime })=(xx^{\prime },y^{\prime }y)$, and inversion interchanges the
two coordinates. Thus $R^\times$ is a Polish group. We use this topology on $R_A^\times$, including when inversion has not separately been shown
continuous for the subspace topology from $R_A$.

We recall the classification inputs needed without UCT. Every invertible $KK$-class of a stable Kirchberg algebra is represented by an automorphism {cite}`Phillips2000`, Theorem 4.2.1, and two such automorphisms with the same $KK$-class are isotopic {cite}`Phillips2000`, Theorem 4.1.4(2). Here an isotopy is a
point-norm continuous path consisting of automorphisms. For unital Kirchberg
algebras, equality of $KL$-classes of unital homomorphisms is equivalent to
approximate unitary equivalence {cite}`Dadarlat2005`, Theorem 5.1(a), the
converse implication being {cite}`Dadarlat2005`, Theorem 3.3.

:::{prf:lemma}
:label: lem-st-stable-kl-uniqueness

For $\alpha,\beta\in\operatorname{Aut}(A)$, equality of
their $KL$-classes is equivalent to approximate unitary equivalence by
multiplier unitaries. Consequently the continuous homomorphism

$$
\kappa_A:\mathsf G_A\longrightarrow R_A^\times,\qquad  \alpha\longmapsto[\alpha]_{KL},
$$

has kernel $N_A$.
:::

:::{prf:proof}
It suffices to compare an automorphism $\gamma$ with the identity. Write $A=B\otimes\mathcal{K}$ for a unital Kirchberg algebra $B$, and let $e_{ij}=1_B\otimes e_{ij}^{\mathcal{K}}$. Equality of $KL$-classes implies $[\gamma(e_{11})]=[e_{11}]$ in $K_0(A)$. Nonzero projections with the same $K_0$-class in a purely infinite simple algebra are Murray–von Neumann
equivalent. We record explicitly why the equivalence extends to a multiplier
unitary. The strictly convergent sum

$$
s=\sum_{i\geq1}e_{i+1,i}\in M(A)
$$

satisfies $s^*s=1$ and $ss^*=1-e_{11}$. The automorphism $\gamma$ has a
strictly continuous extension $\bar\gamma$ to $M(A)$, so $\bar\gamma(s)\bar\gamma(s)^*=1-\gamma(e_{11})$. Thus the two complementary
multiplier projections are both Murray–von Neumann equivalent to $1$.
Adding a partial isometry between the complements to one between $\gamma(e_{11})$ and $e_{11}$ gives a multiplier unitary carrying $\gamma(e_{11})$ to $e_{11}$. After the corresponding multiplier-inner
perturbation, assume $\gamma(e_{11})=e_{11}$.

The strict sum

$$
w=\sum_{i\geq1}e_{i1}\gamma(e_{1i})
$$

is a multiplier unitary, and $\operatorname{Ad}(w)\gamma$ fixes every $e_{ij}$. Indeed the
summands have pairwise orthogonal initial projections $\gamma(e_{ii})$ and
final projections $e_{ii}$, both summing strictly to one. Hence $\operatorname{Ad} (w)\gamma=\theta\otimes\mathrm{id}_{\mathcal{K}}$ for a unital automorphism $\theta$ of $B$. Passing to the full corner preserves equality of $KL$-classes, since the Morita equivalence and its inverse act continuously by
Kasparov product. Dadarlat's unital uniqueness theorem makes $\theta$
approximately inner. The implementing unitaries $v_n\in U(B)$ give
multiplier unitaries $v_n\otimes1$, proving the stable assertion.

Conversely, every multiplier-inner automorphism has $KK$-class one: left
multiplication by the implementing unitary's adjoint intertwines its
Kasparov correspondence with the identity correspondence. Continuity into
the Hausdorff group $R_A$ then implies equality of $KL$-classes under
approximate unitary equivalence. Continuity of $\kappa_A$ for {eq}`eq-st-inverse-pair` follows by applying continuity of the class map to
both $\alpha$ and $\alpha^{-1}$.
:::

:::{prf:lemma}
:label: lem-st-kl-realization

Every unit of $R_A$ is represented by an
automorphism of $A$.
:::

:::{prf:proof}
Choose a full corner $B=pAp$ with $[p]=0$ in $K_0(A)$. To find $p$, take an
infinite nonzero projection $e$ and a proper subprojection $f<e$ equivalent
to $e$; then $p=e-f\ne0$ has class zero and is full. Brown's theorem gives $B\otimes\mathcal{K}\cong A$. Thus $B$ is a unital Kirchberg algebra in
standard form, meaning $[1_B]=0$.

Transport a given unit $x\in R_A$, and its inverse, to $KL(B,B)$. Choose $KK$-lifts of these two classes. The Kirchberg–Phillips existence theorem
{cite}`RordamStormer2002`, Theorem 8.2.1(i) realises these lifts by full
homomorphisms into $B\otimes\mathcal{K}$, and
{cite}`RordamStormer2002`, Proposition 4.1.4 cuts them down to unital
homomorphisms $\varphi,\psi:B\to B$, the unit-class condition being
automatic in standard form. This is precisely the existence step used in
{cite}`Dadarlat2005`, proof of Theorem 5.1(a). Their composites have the identity $KL$-class,
so the uniqueness theorem gives $\psi\varphi\approx_u\mathrm{id}_B$ and $\varphi\psi\approx_u\mathrm{id}_B$.

Here are the intertwining details. Choose summable positive numbers $\varepsilon_n$ and increasing finite selfadjoint subsets $F_n$ of the unit
ball whose union is dense. We enlarge the sets during the construction by
finitely many images, without changing these properties. Starting with $\varphi_1=\varphi$, construct maps $\varphi_n,\psi_n$ such that every $\varphi_n$ is an inner perturbation of $\varphi$, every $\psi_n$ is an inner
perturbation of $\psi$, and

$$
\left\|\psi_n\varphi_n(a)-a\right\|<\varepsilon_n  (a\in F_n),
$$ (eq-st-kl-intertwining-one)

$$
\left\|\varphi_{n+1}\psi_n(b)-b\right\|<\varepsilon_n  (b\in
F_n\cup\varphi_n(F_n)).
$$ (eq-st-kl-intertwining-two)

Indeed, if $\varphi_n=\operatorname{Ad}(u)\varphi$, then $\psi\varphi_n=\operatorname{Ad} (\psi(u))\psi\varphi$ is approximately unitarily equivalent to the identity,
so a post-inner perturbation of $\psi$ gives {eq}`eq-st-kl-intertwining-one`.
Similarly, after $\psi_n=\operatorname{Ad}(v)\psi$ has been chosen, $\varphi\psi_n=\operatorname{Ad} (\varphi(v))\varphi\psi$ is approximately unitarily equivalent to the
identity, and a post-inner perturbation of $\varphi$ gives {eq}`eq-st-kl-intertwining-two`. Before the next step, enlarge $F_{n+1}$ so
that it contains $F_n\cup\psi_n(F_n)$.

For $a\in F_n$, the two displayed estimates give

$$
\left\|\varphi_{n+1}(a)-\varphi_n(a)\right\|<2\varepsilon_n.
$$

At the next half-step, for $b\in F_n$, applying $\psi_{n+1}$ to {eq}`eq-st-kl-intertwining-two` and using $\psi_n(b)\in F_{n+1}$ gives

$$
\left\|\psi_{n+1}(b)-\psi_n(b)\right\|  <\varepsilon_n+\varepsilon_{n+1}.
$$

Thus $\varphi_n$ and $\psi_n$ converge point-norm, on a dense union and
hence on all of $B$, to unital homomorphisms $\theta$ and $\eta$. Passing to
the limit in {eq}`eq-st-kl-intertwining-one`–{eq}`eq-st-kl-intertwining-two`
yields $\eta\theta=\mathrm{id}_B$ and $\theta\eta=\mathrm{id}_B$.
Consequently $\theta$ is an automorphism.

Every $\varphi_n$ has the prescribed $KL$-class, and the class map is
continuous with Hausdorff target. Thus $[\theta]_{KL}=x$, after the chosen
transport. Stabilisation and the fixed Morita identification return an
automorphism of $A$ with the original class. The proof does not require the
two initially chosen $KK$-lifts to be inverse to one another.
:::

### Path components as Polish subgroups

In this paper, a subgroup $H$ of a Polish group $G$ is called a *Polish
subgroup* if it admits a Polish group topology whose Borel sets are exactly
those inherited from $G$; this topology need not be the subspace topology. A
quotient $G/H$, where $H$ is a normal Borel Polish subgroup, is called a
*group with a Polish cover*; its quotient topology need not be
Hausdorff {cite}`LupiniDefinableKHomology2020`, Remark 1.17. This category was introduced by
Bergfalk–Lupini–Panagiotopoulos in the first part of their work on
definable homological invariants {cite}`BergfalkLupiniPanagiotopoulos2024a` and developed further in the
second {cite}`BergfalkLupiniPanagiotopoulos2024b`. Its full subcategory of abelian groups with a Polish
cover is the left heart of the derived category of the quasi-abelian
category of abelian Polish groups {cite}`Lupini2024Heart`, while the category of
groups with a Polish cover and Borel-definable homomorphisms is the exact
completion, as a regular category, of the homological category of Polish
groups and continuous homomorphisms {cite}`LupiniExactCompletion2026`.

:::{prf:lemma}
:label: lem-st-path-polish

The identity path component $G_{\mathrm{path}}$ of
every Polish group $G$ is a normal Borel Polish subgroup.
:::

:::{prf:proof}
With pointwise multiplication and the compact-open topology,

$$
P_eG=\{\gamma\in C([0,1],G):\gamma(0)=e\}
$$

is a Polish group. Endpoint evaluation is a continuous homomorphism, with
image $G_{\mathrm{path}}$ and closed kernel $L_eG$. The induced continuous
injection $P_eG/L_eG\to G$ has Borel image by the Lusin–Souslin theorem and
is a Borel isomorphism onto that image. Transporting the Polish group
topology of $P_eG/L_eG$ proves that $G_{\mathrm{path}}$ is a Polish
subgroup. Normality follows by conjugating paths.
:::

:::{prf:proposition}
:label: prop-st-kk-path-cover

One has

$$
J_A=(\mathsf G_A)_{\mathrm{path}},\qquad \overline{J_A}=N_A.
$$

The map $\alpha\mapsto KK(\alpha)$ induces an algebraic isomorphism $\mathsf G_A/J_A\cong KK(A,A)^\times$, giving the latter a group-with-a-Polish-cover
presentation. The maximal Hausdorff quotient of $\mathsf G_A/J_A$, with its quotient
topology, is $\mathsf G_A/N_A$.
:::

:::{prf:proof}
The isotopy theorem recalled above and homotopy invariance of $KK$-theory
give $J_A=(\mathsf G_A)_{\mathrm{path}}$. Classification realises every $KK$-unit,
giving the algebraic isomorphism, and {prf:ref}`lem-st-path-polish` supplies
the Polish cover. {prf:ref}`lem-st-stable-kl-uniqueness` gives $J_A\subseteq
N_A$. Multiplier inners have $KK$-class one, so $\operatorname{Inn}_M(A)\subseteq J_A$,
whence $\overline{J_A}=N_A$. Finally, the closure of the identity in $\mathsf G_A/J_A
$ is $N_A/J_A$. Quotienting by it gives $\mathsf G_A/N_A$; every continuous
homomorphism to a Hausdorff group annihilates this closure and therefore
factors through that quotient.
:::

### Compatibility with the Cuntz presentation

The preceding Polish cover agrees definably with the natural cycle
presentation of the $KK$-unit group. We give the details because this
conclusion does not require a definable theory of all additive groups $KK(A,B)$.

We use the terminology of {cite}`LupiniDefinableKHomology2020`, Sections 1.3–1.5. A *semidefinable set* is a quotient of a standard Borel space by an analytic
equivalence relation. It is *definable* when the relation is Borel and
idealistic. A relation is idealistic if its classes admit an assignment of
proper sigma-filters, with the Borel measurability condition of {cite}`LupiniDefinableKHomology2020`, Definition 1.6; coset relations of Polish subgroups have this
property. A map between quotient sets is *definable* if it admits a
Borel lift to the representative spaces. We use the following transfer
principle:

:::{prf:theorem} {{cite}`LupiniDefinableKHomology2020`, Corollary 1.14}
:label: thm-st-definable-transfer

A definable bijection from a definable set to
a semidefinable set is a definable isomorphism, and its target is definable.
:::

Let $qA=\ker(A*A\to A)$, where the map is the identity on both free-product
copies, and put $C_A=\mathcal{K}\otimes qA$. The stabilised Cuntz picture
identifies

$$
KK(A,A)\cong[C_A,C_A],
$$ (eq-st-cuntz-endomorphism)

where brackets denote homotopy classes of homomorphisms and composition
represents the Kasparov product {cite}`LupiniDefinableKHomology2020`, Section 5.6. The same
source constructs $KK(A,B)$ as a semidefinable group, with Borel-lifted
product, but leaves definability for arbitrary coefficient algebras open.

Write $\mathcal{H}_A=\operatorname{Hom}_*(C_A,C_A)$ for the Polish space of all, possibly
nonunital, $^*$-homomorphisms, with point-norm topology. Composition is
jointly continuous: on a fixed $c$,

$$
\|f_n(g_n(c))-f(g(c))\|  \leq\|g_n(c)-g(c)\|+\|f_n(g(c))-f(g(c))\|.
$$

Consider the closed Polish subspace

$$
\begin{split}
\mathcal{W}_A=\{(f,g,h,k)\in \mathcal{H}_A^2\times C([0,1],\mathcal{H}_A)^2:\quad& \\
h(0)=gf,\ h(1)=\mathrm{id}_{C_A},\quad k(0)=fg,\ k(1)=\mathrm{id}_{C_A}&\}.
\end{split}
$$ (eq-st-unit-witnesses)

Two quadruples are equivalent when their first coordinates are homotopic.
This relation is analytic, since a homotopy is a witness in the Polish path
space. The quotient represents exactly the units of $[C_A,C_A]$: $g$
represents the inverse of $f$. It is a semidefinable group. Inversion swaps $f,g$ and $h,k$. For multiplication, the representatives are $ff^{\prime }$
and $g^{\prime }g$; concatenating the paths $g^{\prime }hf^{\prime }$ and $h^{\prime }$, and the paths $fk^{\prime }g$ and $k$, gives the required
inverse witnesses. These operations have Borel, in fact continuous, lifts.

:::{prf:proposition}
:label: prop-st-definable-kk-units

The unit group $KK(A,A)^\times$, with the
witnessed Cuntz presentation $\mathcal{W}_A/{\sim}$, is definable. The
natural isomorphism

$$
\mathsf G_A/J_A\longrightarrow KK(A,A)^\times
$$

is a definable isomorphism.
:::

:::{prf:proof}
An automorphism $\alpha$ induces the automorphism $f_\alpha=\mathrm{id}_{\mathcal{K}}\otimes q\alpha$ of $C_A$. The map

$$
\alpha\longmapsto  (f_\alpha,f_{\alpha^{-1}},\mathrm{const}_{\mathrm{id}},
\mathrm{const}_{\mathrm{id}})
$$

is Borel, indeed continuous. Naturality of {eq}`eq-st-cuntz-endomorphism`
identifies its class with $KK(\alpha)$. {prf:ref}`prop-st-kk-path-cover`
shows that the induced map on quotients is bijective and that its source is
definable. Apply {prf:ref}`thm-st-definable-transfer`.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-st-kk`.* {prf:ref}`lem-st-stable-kl-uniqueness` and {prf:ref}`lem-st-kl-realization` make $\kappa_A$ a continuous surjective homomorphism of Polish groups with kernel $N_A$. It is open by the Polish open mapping theorem. {prf:ref}`thm-st-kernel-ea` gives whirly amenability of $N_A$, and
{prf:ref}`prop-st-transfer` gives the universal-minimal-flow and Bohr
formulas. {prf:ref}`prop-st-kk-path-cover` and {prf:ref}`prop-st-definable-kk-units` prove the assertions
about the definable unit group and its Hausdorff quotient.
The whirly-amenability equivalence is the additional assertion of
{prf:ref}`prop-st-transfer`.
:::

Throughout the paper $Q_A=\mathsf G_A/N_A$ denotes this Hausdorff
quotient. {prf:ref}`thm-st-kk` identifies it with
$R_A^\times=KL(A,A)^\times$, and [](#sec-st-total) identifies it,
under UCT, with $\operatorname{Aut}_\Lambda(\underline K(A))$; the single symbol $Q_A$
is used for all three descriptions. The kernel $N_A$ is the closure of
the multiplier-inner automorphisms; the companion unital paper
{cite}`LupiniUnital2026` instead divides by the closure of
$\operatorname{Ad} U_0(A)$, and its quotient is written $Q_A^0$ there.

:::{prf:corollary}
:label: cor-st-kirchberg-fd-representations

For every stable Kirchberg algebra $A$, without a UCT assumption, pullback along $\kappa_A$ gives an equivalence

$$
\operatorname{Rep}_{\mathrm{fd}}(KL(A,A)^\times)  \simeq  \operatorname{Rep}_{\mathrm{fd}}(\operatorname{Aut}(A))
$$

between continuous finite-dimensional unitary representation categories. In
particular, $\operatorname{Aut}(A)$ is minimally almost periodic if and only if $KL(A,A)^\times$ is. Under UCT, the latter group is $\operatorname{Aut}_\Lambda(\underline
K(A))$.
:::

:::{prf:proof}
Apply {prf:ref}`cor-st-finite-dimensional-representations` to $\kappa_A$,
and then the UCT identification of [](#sec-st-total) under UCT.
:::

View $KK(A,A)^\times$ as the quotient topological group $\mathsf G_A/J_A$ in
{prf:ref}`prop-st-kk-path-cover`. Although this topology need not be
Hausdorff, amenability still has its usual compact-dynamical meaning: every
continuous action on a compact Hausdorff space admits an invariant
probability measure.

:::{prf:corollary} UCT-free amenability criterion
:label: cor-st-kirchberg-amenability-no-uct

For every stable Kirchberg algebra $A$, without a UCT assumption, the following are equivalent:

1. $\operatorname{Aut}(A)$ is amenable;
2. $KL(A,A)^\times$ is amenable;
3. the definable group $KK(A,A)^\times$, with its
   group-with-a-Polish-cover topology, is amenable.

Equivalently, every compact Hausdorff action of the definable $KK$-unit
group has an invariant probability measure.
:::

:::{prf:proof}
The equivalence of (i) and (ii) follows from {prf:ref}`thm-st-kk`, or
directly from {prf:ref}`prop-st-transfer`. The closure of the identity
in $\mathsf G_A/J_A$ is $N_A/J_A$. It acts trivially in every continuous action on a
Hausdorff space: for each point, continuity of its orbit map identifies the
action of every element in that closure with the action of the identity.
Hence every compact Hausdorff action of $\mathsf G_A/J_A$ factors through its
maximal Hausdorff quotient $\mathsf G_A/N_A\cong KL(A,A)^\times$, and conversely
every action of the latter pulls back to the former. This proves the
equivalence of (ii) and (iii).
:::

:::{prf:corollary} Locally compact $KL$-quotients
:label: cor-st-locally-compact-kl

Let $A$ be a stable Kirchberg algebra,
without a UCT assumption, and suppose that $KL(A,A)^\times$ is locally
compact. Then the following are equivalent:

1. $M(\operatorname{Aut}(A))$ is metrizable;
2. $KL(A,A)^\times$ is compact.

When these conditions hold,

$$
M(\operatorname{Aut}(A))\cong\kappa_A^*KL(A,A)^\times,  \qquad b\operatorname{Aut}(A)\cong
KL(A,A)^\times,
$$

where the quotient acts on itself by left translation. In particular, $\operatorname{Aut} (A)$ is amenable and its universal minimal flow is uniquely ergodic, with
Haar measure on the displayed quotient.
:::

:::{prf:proof}
{prf:ref}`thm-st-kk` and {prf:ref}`lem-st-locally-compact-umf` prove the
equivalence. When it holds, the displayed formulas follow from {prf:ref}`thm-st-kk` and the compact-group facts in [](#sec-st-dynamics); Haar measure is the unique invariant
probability measure on the left-translation flow.
:::

(sec-st-total)=
## Total $K$-theory and the automorphism quotient

 Throughout this section $A$ is a stable UCT Kirchberg
algebra. We identify the quotient of [](#sec-st-definable-kk) in terms
of total $K$-theory and then describe its phantom kernel. The UCT of
Rosenberg and Schochet {cite}`RosenbergSchochet1987` gives the degree-zero exact sequence

$$
\begin{split}
0\longrightarrow \operatorname{Ext}^1_\mathbb{Z}(K_0(A),K_1(A))\oplus \operatorname{Ext}^1_\mathbb{Z}(K_1(A),K_0(A)) \longrightarrow KK(A,A) \\
\longrightarrow \operatorname{Hom}(K_0(A),K_0(A))\oplus \operatorname{Hom}(K_1(A),K_1(A))
\longrightarrow0.
\end{split}
$$ (eq-st-uct)

We retain the composition convention for the Kasparov product.

Total $K$-theory retains the coefficient exact sequences

$$
K_i(A)\xrightarrow{n}K_i(A) \xrightarrow{\rho_n}K_i(A;\mathbb{Z}/n) \xrightarrow{\beta_n}K_{i-1}(A) \xrightarrow{n}K_{i-1}(A),
$$ (eq-st-bockstein)

as well as all coefficient-change operations. The notation $\Lambda$
includes these operations and their compositions, not only the maps in a
single displayed sequence.

The universal multicoefficient theorem of Dadarlat–Loring {cite}`DadarlatLoring1996`
identifies

$$
KL(A,A)\cong\operatorname{Hom}_\Lambda(\underline K(A),\underline K(A)),
$$ (eq-st-umct)

where

$$
KL(A,A)=KK(A,A)/P_A,\qquad  P_A=\operatorname{Pext}^1_\mathbb{Z}(K_0(A),K_1(A))  \oplus \operatorname{Pext}^1_\mathbb{Z}(K_1(A),K_0(A)).
$$

Here pure extensions are those whose restrictions to finitely generated
subgroups of the quotient split; $P_A$ is embedded by the UCT. We use
exactness, not a splitting of the multicoefficient sequence: contrary to the
statement in {cite}`DadarlatLoring1996`, it need not split, as recorded in the discussion
following {cite}`EilersRestorffRuiz2011`, Theorem 1.3. Dadarlat identifies the topology in {eq}`eq-st-umct` with pointwise
convergence and, for $A$ in the UCT class, $P_A$ with the closure of zero
in the natural $KK$-topology {cite}`Dadarlat2005`, Theorem 4.1 and p. 411. On
units the topology of {eq}`eq-st-inverse-pair` is exactly the pointwise
automorphism topology: if bijections converge pointwise to a bijection,
their inverses also converge pointwise. Thus the $KL$-unit quotient in
{prf:ref}`thm-st-kk` is precisely the group appearing in {prf:ref}`thm-cu-stable-general`.

For the UCT presentation we use the topological identification from
{prf:ref}`thm-cu-stable-general`:

$$
q_A:\operatorname{Aut}(A)\longrightarrow Q_A\cong\operatorname{Aut}_\Lambda(\underline K(A)),
 \qquad \ker q_A=N_A.
$$

The map is continuous, surjective, and open. Its realisation and
uniqueness proof, including continuity on coefficient classes, belongs
to the cited theorem. The strengthened whirly-kernel conclusion follows
from the norm-unitary theorem and strict approximation, as proved in
[](#sec-st-kernel).

:::{prf:proposition}
:label: prop-st-pure-state-quotient

Let $A$ be a stable UCT Kirchberg algebra,
let $\varphi$ be a pure state, and put $H_\varphi=\operatorname{Aut}(A,\varphi)$.
Restriction gives a continuous open surjection

$$
q_A|_{H_\varphi}:H_\varphi\longrightarrow  \operatorname{Aut}_\Lambda(\underline
K(A))
$$

with whirly amenable kernel $H_\varphi\cap N_A$. Consequently,

$$
\begin{split}
M(H_\varphi)&\cong (q_A|_{H_\varphi})^*M(\operatorname{Aut}_\Lambda(\underline
K(A))), \\
bH_\varphi&\cong b\operatorname{Aut}_\Lambda(\underline K(A)).
\end{split}
$$

The restriction of $M(\operatorname{Aut}(A))$ to $H_\varphi$ is universal minimal.
Amenability and extreme amenability of these two groups are equivalent to
the corresponding properties of the total-$K$ quotient.
Both groups are whirly amenable exactly when that quotient is trivial.
:::

:::{prf:proof}
Apply {prf:ref}`cor-st-stable-stabilizer-umf`, proved in [](#sec-st-stable-stabilizers), and the topological total-$K$ identification
above. Its kernel theorem is independent of UCT and does not use the present
proposition.
The whirly criterion follows from {prf:ref}`prop-st-transfer` and
{prf:ref}`lem-st-nonarch-whirly`.
:::

:::{prf:corollary}
:label: cor-st-aut-bohr

For a stable UCT Kirchberg
algebra $A$, extreme amenability, amenability, and metrizability of the
universal minimal flow hold for $\operatorname{Aut}(A)$ exactly when they hold for
$\operatorname{Aut}_\Lambda(\underline K(A))$, respectively, and

$$
b\operatorname{Aut}(A)\cong b\operatorname{Aut}_\Lambda(\underline K(A)).
$$

Furthermore, $\operatorname{Aut}(A)$ is whirly amenable exactly when
$\operatorname{Aut}_\Lambda(\underline K(A))=1$, equivalently when $\operatorname{Aut}(A)=N_A$.
:::

:::{prf:proof}
Apply {prf:ref}`prop-st-transfer` and {eq}`eq-st-transfer-bohr` to
$q_A$; for the whirly assertion also use {prf:ref}`lem-st-nonarch-whirly`,
since the total-$K$ quotient is a closed permutation group on a countable
discrete invariant.
:::

:::{prf:corollary}
:label: cor-st-closed-preimages

Let $L$ be a closed subgroup of $Q_A=\operatorname{Aut} _\Lambda(\underline K(A))$, and put

$$
G_{A,L}=q_A^{-1}(L).
$$

Then the restriction $q_A:G_{A,L}\to L$ is a continuous open surjection with
whirly amenable kernel $N_A$. Consequently

$$
M(G_{A,L})\cong M(L),\qquad bG_{A,L}\cong bL,
$$

where the first action is pulled back along $q_A$.
Moreover, $G_{A,L}$ is whirly amenable if and only if $L=1$.
:::

:::{prf:proof}
Only openness requires comment. If $U=V\cap G_{A,L}$, where $V$ is open in $\operatorname{Aut}(A)$, then

$$
q_A(U)=q_A(V)\cap L,
$$

which is open in $L$. The kernel is $N_A$, so {prf:ref}`prop-st-transfer`
applies.
For the additional assertion, apply its whirly-amenability part and
{prf:ref}`lem-st-nonarch-whirly` to the Polish non-Archimedean group $L$.
:::

### The extension term invisible to ordinary $K$-theory

Put $G_i=K_i(A)$ and

$$
E_A=\operatorname{Ext}^1_\mathbb{Z}(G_0,G_1)\oplus\operatorname{Ext}^1_\mathbb{Z}(G_1,G_0).
$$

Restriction gives a continuous open surjection

$$
r:Q_A\longrightarrow\operatorname{Aut}(G_0)\times\operatorname{Aut}(G_1).
$$

Surjectivity follows by lifting a graded isomorphism through the UCT and
using classification; openness follows from the Polish open mapping theorem.

We recall the algebraic extension from
{cite}`LupiniCuntz2026`, Section 8.1:

$$
1\longrightarrow E_A/P_A\longrightarrow Q_A
 \xrightarrow{r}\operatorname{Aut}(G_0)\times\operatorname{Aut}(G_1)\longrightarrow1.
$$ (eq-st-ext-kernel)

The kernel is additive, with its inherited topology. No general
splitting or discreteness is assumed. The square-zero argument belongs
to the cited proof. We use this sequence to obtain the following
amenability consequence.

:::{prf:corollary} Ordinary $K$-theory amenability criterion
:label: cor-st-amenability-k-groups

For every stable UCT Kirchberg algebra $A$,

$$
\operatorname{Aut}(A)\text{ is amenable}  \quad\Longleftrightarrow\quad  \operatorname{Aut}(K_0(A))\text{
and }\operatorname{Aut}(K_1(A))\text{ are amenable}.
$$

The automorphism groups of the $K$-groups carry pointwise convergence on the
underlying countable discrete groups.
:::

:::{prf:proof}
The kernel $E_A/P_A$ in {eq}`eq-st-ext-kernel` is an abelian topological
group and hence is amenable, by the Markov–Kakutani fixed-point theorem.
Therefore {prf:ref}`lem-st-amenable-extensions` shows that $Q_A$ is amenable
whenever $\operatorname{Aut}(G_0)\times\operatorname{Aut}(G_1)$ is amenable. Conversely, amenability
passes to continuous quotients, so amenability of $Q_A$ implies amenability
of both factors. Finally apply {prf:ref}`cor-st-aut-bohr`.
:::

:::{prf:corollary} Vanishing Hausdorff extension kernel
:label: cor-st-vanishing-ext

If $E_A=P_A$, restriction induces a topological isomorphism

$$
Q_A\cong\operatorname{Aut}(G_0)\times\operatorname{Aut}(G_1).
$$
:::

:::{prf:proof}
In {eq}`eq-st-ext-kernel`, restriction is then a continuous bijective
homomorphism of Polish groups, hence an isomorphism by the open mapping
theorem. This criterion permits both degrees to be nonzero.
:::

When one $K$-group vanishes, the reduction to automorphisms of the
other is {prf:ref}`cor-cu-k1zero`; the four-point
$K_0=K_1=\mathbb Z/2$ example is its Example 8.7. These existing computations
are not reproved here. Phantom information, which disappears from the
Hausdorff quotient, is considered next.

(sec-st-computations)=
## Explicit $K$-theoretic computations

### The existing finitely generated computation

The discreteness, finite-rank criterion, and finite cardinality formula
for finitely generated $K$-groups are
{prf:ref}`prop-cu-finite-k`. The stabilised Cuntz flows and
their table are {prf:ref}`cor-cu-cuntz-stable`; we do not reproduce
them. The additional amenability criterion here is
{prf:ref}`cor-st-amenability-k-groups`: in the finitely generated
family amenability is equivalent to both free ranks being at most one.
We now turn to infinite invariants and extensions of the existing
Prüfer and vector-space examples.

(sec-st-stable-stabilizers)=
## Pure-state stabilisers of stable Kirchberg algebras

We now return to a stable Kirchberg algebra $A$, without UCT. Write $H=\operatorname{Aut} (A,\varphi)$, $N=N_A$, and $L=H\cap N$. The norm-unitary theorem gives a direct proof once the relative inner density is established.

:::{prf:lemma}
:label: lem-st-stable-u0-density

For every stable Kirchberg algebra $A$,

$$
N_A=\overline{\operatorname{Ad} U_0(1+A)},
$$

where $U_0(1+A)$ denotes the component of one in the scalar-part-one
unitaries of the minimal unitisation.
:::

:::{prf:proof}
As in the proof of {prf:ref}`thm-st-kernel-ea`, write
$A\cong B\otimes\mathcal K$ with $B$ a unital Kirchberg algebra.
The strict-density assertion of {prf:ref}`thm-st-multiplier-whirly`
makes $U_0(1+A)=U_1(A)_0$ strictly dense in $U(M(A))$.
Continuity of the adjoint map, {prf:ref}`lem-st-adjoint`, then gives
the equality of the two point-norm closures. Only the strict-density
part of that theorem is used here.
:::

:::{prf:lemma}
:label: lem-st-state-projections

For every pure state $\varphi$ of $A$, there
is an increasing projection approximate identity $(e_n)$ with $\varphi(e_n)=1
$.
:::

:::{prf:proof}
Choose a nonzero projection $p\in A$. The irreducible GNS representation is
faithful. Kadison unitary transitivity in $A^+$ therefore gives a unitary
moving the cyclic vector into the range of $\pi_\varphi(p)$. Conjugating $p$
back gives a projection $e_0\in A$ with $\varphi(e_0)=1$. The hereditary
algebra $(1-e_0)A(1-e_0)$ has real rank zero and an increasing projection
approximate identity $(f_n)$. Set $e_n=e_0+f_n$. These projections
approximate the diagonal corners of every element. For an off-diagonal
corner $x=e_0a(1-e_0)$, one has

$$
\left\|x(1-f_n)\right\|^2
=\left\|(1-f_n)x^*x(1-f_n)\right\|\longrightarrow0.
$$

The other corner is similar. Thus $(e_n)$ is an approximate identity of $A$,
and every $e_n$ fixes the cyclic vector.
:::

:::{prf:lemma}
:label: lem-st-stable-marked-inner

Put

$$
D_\varphi=\{a\in A:\varphi(aa^*)=\varphi(a^*a)=0\},\qquad  W^{(0)}=\{u\in
U_1(D_\varphi):[u]=0\in K_1(D_\varphi)\}.
$$

Then $L=\overline{\operatorname{Ad} W^{(0)}}$.
:::

:::{prf:proof}
Fix $\alpha\in L$, a finite test set $F\subset A$, and a tolerance. Apply
Property 1.2 of {cite}`KishimotoOzawaSakai2003`, which holds for every $C^*$-algebra by
Theorems 3.1 and 4.3 of that paper, to $(F,\varphi)$, obtaining additional tests and a
tolerance for exact correction of equivalent pure states. The essentiality
hypothesis holds: the faithful irreducible image of a simple purely infinite
algebra contains no nonzero compact operators. By {prf:ref}`lem-st-stable-u0-density`, choose $v\in U_0(1+A)$ whose conjugation
approximates $\alpha$ on both sets of tests. Property 1.2 supplies $w\in
U_0(1+A)$ such that

$$
\varphi\operatorname{Ad} v=\varphi\operatorname{Ad} w,\qquad  \operatorname{Ad} w\approx\mathrm{id}\text{ on }F.
$$

A unitary path in $A^+$ can be normalised continuously by its scalar
quotient, so the scalar part can be kept equal to one. Then $z=vw^*$ lies in
$U_0(1+A)$, its conjugation fixes $\varphi$, and $\operatorname{Ad} z$ approximates $\alpha
$ on $F$. Purity gives $\pi_\varphi(z)\xi_\varphi=e^{it}\xi_\varphi$ for
some real $t$.

Use the projections from {prf:ref}`lem-st-state-projections` and put

$$
q_n=\exp(-it e_n),\qquad u_n=zq_n.
$$

The unitaries $u_n$ have scalar part one, belong to $U_0(1+A)$, and fix $\xi_\varphi$. Moreover, $q_n\to e^{-it}1$ strictly, so $\operatorname{Ad} u_n\to\operatorname{Ad} z$
point-norm. Both $u_n-1$ and its adjoint annihilate $\xi_\varphi$; hence $u_n-1\in D_\varphi$. The nonzero hereditary algebra $D_\varphi$ is full in $A
$, and its inclusion induces a $K_1$-isomorphism. Thus $[u_n]=0$ also in $K_1(D_\varphi)$, proving the required density. Conversely, every element of $\operatorname{Ad} W^{(0)}$ fixes $\varphi$ and is multiplier inner, so belongs to $L$.
:::

:::{prf:theorem}
:label: thm-st-stable-marked-kernel

For every stable Kirchberg algebra $A$ and
every pure state $\varphi$, the group $\operatorname{Aut}(A,\varphi)\cap N_A$ is whirly
amenable.
:::

:::{prf:proof}
Kadison transitivity makes $D_\varphi$ nonzero, and simplicity
makes this hereditary algebra full. It is $\sigma$-unital by
separability. If it had an identity $e$, its bidual support would be
$1-s_\varphi$, where $s_\varphi$ is the minimal support projection
of the pure state. For $a\in A$ with $\varphi(a)\ne0$,

$$
(1-e)a(1-e)=\varphi(a)(1-e)\in A.
$$

Thus $1-e\in A$ and $1\in A$, contradicting nonzero stability.
So $D_\varphi$ is nonunital. Zhang's dichotomy {cite}`Zhang1992`, Theorem 1.2(i) makes it stable, and
Brown's theorem {cite}`Brown1977`, Theorem 2.8 identifies it stably with
$A$. Choosing a
nonzero projection in $D_\varphi$ expresses it as $C\otimes\mathcal K$
for a unital nuclear Kirchberg corner $C$. The stable component
identification makes $W^{(0)}=U_1(D_\varphi)_0$. {prf:ref}`thm-st-v`
therefore makes $W^{(0)}$ whirly amenable in norm. Its continuous
adjoint image is point-norm dense in $L$ by
{prf:ref}`lem-st-stable-marked-inner`. Dense-image permanence proves the
assertion. No extension of a corner automorphism is required.
:::

:::{prf:corollary}
:label: cor-st-stable-stabilizer-umf

Let $A$ be a stable Kirchberg algebra, $Q_A=\operatorname{Aut}(A)/N_A$, and $H=\operatorname{Aut}(A,\varphi)$ for a pure state $\varphi$.
Restriction of the quotient map is an open continuous surjection $H\to Q_A$
with whirly amenable kernel. In particular,

$$
M(H)\cong(q_A|_H)^*M(Q_A),\qquad bH\cong bQ_A.
$$

The restriction of $M(\operatorname{Aut}(A))$ to $H$ is itself universal minimal. The
groups $H$, $\operatorname{Aut}(A)$, and $Q_A$ are simultaneously extremely amenable, and
simultaneously amenable.
They are also simultaneously whirly amenable; if $Q_A$ is
non-Archimedean, in particular under UCT, this occurs exactly when $Q_A=1$.
:::

:::{prf:proof}
For $\alpha\in\operatorname{Aut}(A)$, pure-state homogeneity {cite}`KishimotoOzawaSakai2003`, Theorem 2.1
gives $\beta\in\operatorname{AInn}_0(A)\subseteq N_A$ with $\varphi\alpha\beta=\varphi$. Thus $\alpha\beta\in H$ represents
the same quotient element as $\alpha$, proving surjectivity. The Polish open
mapping theorem gives openness. Apply {prf:ref}`thm-st-stable-marked-kernel`
and {prf:ref}`prop-st-transfer`, including its whirly-amenability
assertion. {prf:ref}`lem-st-nonarch-whirly` gives the criterion when $Q_A$
is non-Archimedean. The same transfer theorem for $\operatorname{Aut}(A)$
identifies both minimal flows with the indicated pullbacks. Surjectivity of $H\to Q_A$ gives the assertion about restriction.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-st-stable-stabilizer`.* Combine {prf:ref}`thm-st-stable-marked-kernel` and {prf:ref}`cor-st-stable-stabilizer-umf`.
:::

(sec-st-geometric)=
## Direct sums and zero-dimensional fields

 Throughout this section, $B$ is a stable
Kirchberg algebra such that $E=\operatorname{Aut}(B)$ is extremely amenable. By {prf:ref}`thm-st-kk`, this is equivalent to extreme amenability of $KL(B,B)^\times$; under UCT it is equivalent to extreme amenability of $\operatorname{Aut} _\Lambda(\underline K(B))$. The hypothesis holds, in particular, for $B=\mathcal{O}_2\otimes\mathcal{K}$ and $B=\mathcal{O}_3\otimes\mathcal{K}$.
These two examples have $E=N_B$ whirly amenable. More generally, whenever
$E$ is whirly amenable the coordinate and field kernels below have that
stronger property. We retain the extreme-amenability hypothesis for the
general UMF formulas.

### Permutations of summand ideals

:::{prf:proposition}
:label: prop-st-direct-sum

For a nonempty finite or countable set $I$,

$$
\operatorname{Aut}(c_0(I,B))\cong E^I\rtimes\operatorname{Sym}(I)
$$

as topological groups, with the product topology on $E^I$ and the pointwise
topology on $\operatorname{Sym}(I)$. Consequently

$$
M(\operatorname{Aut}(c_0(I,B)))\cong M(\operatorname{Sym}(I)).
$$

If $E$ is whirly amenable, then the normal coordinate kernel $E^I$ is
whirly amenable.
:::

:::{prf:proof}
The coordinate ideals are exactly the minimal nonzero ideals, so an
automorphism permutes them. After specifying a permutation $\sigma$, the
restrictions are automorphisms $\gamma_j\in E$, and the formula is

$$
(\alpha a)_j=\gamma_j(a_{\sigma^{-1}(j)}).
$$ (eq-st-sum-action)

Conversely this formula defines an automorphism for any such data.

For a norm-one element supported in a single coordinate, images supported in
different coordinates have distance one. Thus point-norm convergence forces
eventual agreement on the image of each coordinate, proving continuity of
the permutation map. Once the relevant permutation coordinates agree,
testing supported elements gives point-norm convergence of each $\gamma_j$.
Conversely, coordinate convergence and eventual agreement of the
permutations give convergence on finitely supported elements. These are
dense in $c_0(I,B)$, and the maps are isometric, so convergence holds
everywhere. This proves the topological identification.

The kernel $E^I$ is extremely amenable by {prf:ref}`lem-st-products`. Apply
{prf:ref}`prop-st-transfer`.
The whirly assertion follows from the stronger part of {prf:ref}`lem-st-products`.
:::

:::{prf:corollary}
:label: cor-st-direct-sum-bohr-general

For every nonzero simple stable $C^*$-algebra $C
$ and every nonempty set $I$, put $E=\operatorname{Aut}(C)$. With the
coordinate-permutation action on $(bE)^I$, one has

$$
b\operatorname{Aut}(c_0(I,C))\cong
\begin{cases}
(bE)^I\rtimes\operatorname{Sym}(I), & I\text{ finite}, \\
1, & I\text{ infinite}.\end{cases}
$$

Thus every infinite direct sum is minimally almost periodic, with no
separability, nuclearity, or amenability assumption. If $E$ is
amenable, then $\operatorname{Aut}(c_0(I,C))$ is amenable for every $I$. When $C$ is a
stable Kirchberg algebra, this last hypothesis is equivalent to amenability
of $KL(C,C)^\times$.
:::

:::{prf:proof}
The algebraic and topological parts of the proof of {prf:ref}`prop-st-direct-sum` use only that $C$ is nonzero and simple; using nets in the
possibly nonmetrizable case, they give

$$
\operatorname{Aut}(c_0(I,C))\cong E^I\rtimes\operatorname{Sym}(I)
$$

for every nonempty $I$. If $I$ is infinite, apply {prf:ref}`cor-st-wreath-minap`.

Suppose that $I$ is finite. The canonical homomorphism

$$
E^I\rtimes\operatorname{Sym}(I)\longrightarrow(bE)^I\rtimes\operatorname{Sym}(I)
$$

has dense image and compact target. To verify its universal property, let $\rho:E^I\rtimes\operatorname{Sym}(I)\to K$ be a continuous homomorphism to a compact
group. By {prf:ref}`lem-st-bohr-finite-products`, the restriction of $\rho$ to
$E^I$ extends uniquely to a continuous homomorphism $\bar\rho:(bE)^I\to K$.
The conjugacy relations with the finite coordinate-permutation subgroup
continue to hold on $(bE)^I$, by density. Consequently

$$
(x,\sigma)\longmapsto  \bar\rho(x)\rho(1,\sigma)
$$

is the unique extension of $\rho$ to $(bE)^I\rtimes\operatorname{Sym}(I)$, proving the
finite formula.

Finally, if $E$ is amenable, then $E^I$ is amenable by {prf:ref}`lem-st-amenable-products`. The finitary permutations form a dense directed
union of finite groups in $\operatorname{Sym}(I)$, so that group is amenable by the same
lemma. {prf:ref}`lem-st-amenable-extensions` now proves amenability of the
semidirect product. The last assertion is {prf:ref}`cor-st-kirchberg-amenability-no-uct`.
:::

For finite $I$, the UMF is the regular $|I|!$-point flow of $\operatorname{Sym}(I)$. For $I=\mathbb{N}$, Glasner–Weiss {cite}`GlasnerWeiss2002,Glasner2002Orders` identify $M(\operatorname{Sym}(\mathbb{N}))$ with the compact subspace $\operatorname{LO}(\mathbb{N})\subseteq2^{\mathbb{N}\times\mathbb{N}}$ of strict linear orders. The action is

$$
i<_{\alpha\cdot L}j  \quad\Longleftrightarrow\quad
\sigma_\alpha^{-1}(i)<_L\sigma_\alpha^{-1}(j).
$$

This also specifies the action of the full algebra automorphism group.

For any closed subgroup $P\leq\operatorname{Sym}(\mathbb{N})$, its preimage under the
permutation map is a closed Polish group $E^\mathbb{N}\rtimes P$ with UMF $M(P)$. Thus the construction transfers other known permutation-group
computations.

### Continuous fields over zero-dimensional spaces

:::{prf:lemma}
:label: lem-st-continuous-maps

If $X$ is compact and zero-dimensional and $E$
is extremely amenable, respectively whirly amenable, then $C(X,E)$, with
the compact-open group topology, has the corresponding property.
:::

:::{prf:proof}
For each finite clopen partition $\mathcal{P}$ of $X$, the maps constant on
its parts form a subgroup isomorphic to $E^{|\mathcal{P}|}$. These subgroups
are extremely amenable and directed by refinement. They have dense union:
uniform continuity and a finite clopen refinement allow a continuous map to
be approximated by choosing its value at one point of each part. Apply {prf:ref}`lem-st-products`.
If $E$ is whirly amenable, those finite products are whirly amenable, so
the stronger part of the same lemma applies.
:::

:::{prf:proposition}
:label: prop-st-field

For nonempty compact metrizable zero-dimensional $X$,

$$
\operatorname{Aut}(C(X)\otimes B)  \cong C(X,E)\rtimes\operatorname{Homeo}(X)
$$

topologically. Hence

$$
M(\operatorname{Aut}(C(X)\otimes B))\cong M(\operatorname{Homeo}(X)).
$$

If $E$ is whirly amenable, then the normal field kernel $C(X,E)$ is
whirly amenable.
:::

:::{prf:proof}
Write $C(X)\otimes B=C(X,B)$. Since $B$ is simple, the primitive ideals are
the kernels of the evaluations at points of $X$. An automorphism induces a
homeomorphism $h$ of $X$. Its fiber maps give

$$
(\alpha f)(x)=\gamma_x(f(h^{-1}(x))),\qquad  \gamma_x\in E.
$$

For a constant section $a$, the function $x\mapsto\gamma_x(a)=\alpha(a)(x)$
is continuous. Thus $x\mapsto\gamma_x$ is point-norm continuous. Conversely
this formula for continuous $\gamma$ and $h$ defines an automorphism.

We check the topology. If $U$ is clopen and $\left\|a\right\|=1$, then

$$
\left\|\alpha(1_Ua)(x)\right\|=1_{h(U)}(x).
$$

Point-norm closeness less than one forces equality of these supports.
Agreement on finite clopen partitions describes the topology of $\operatorname{Homeo}(X)$,
so the quotient map is continuous. The pullback map $h\mapsto(f\mapsto
f\circ h^{-1})$ is a continuous section.

On the kernel, convergence is uniform on $X$ in each point-norm test $a\in B$, by constant sections. These tests describe the compact-open topology on $C(X,E)$. They also imply convergence on arbitrary sections: approximate the
compact range of a section by finitely many values in $B$, and use the
isometry of all fiber maps. The semidirect product identification is
therefore topological. {prf:ref}`lem-st-continuous-maps` makes the kernel
extremely amenable, so {prf:ref}`prop-st-transfer` applies.
The same lemma gives whirly amenability of the kernel when $E$ is whirly
amenable.
:::

If $X$ is the Cantor set, let $\mathcal{F}(X)$ be the Vietoris hyperspace of
nonempty closed subsets. Let $\Phi(X)\subseteq\mathcal{F}(\mathcal{F}(X))$
be the space of chains maximal under inclusion. Glasner–Weiss {cite}`GlasnerWeiss2003`, Theorem
6.1 prove that $\Phi(X)$ is the universal minimal flow of $\operatorname{Homeo} (X)$. Thus the flow in {prf:ref}`prop-st-field` is

$$
\alpha\cdot\mathcal{C}=\{h_\alpha(F):F\in\mathcal{C}\}.
$$

This is a compact metrizable flow. Zero-dimensionality was used essentially
in the kernel argument; no extension to arbitrary compact bases is asserted.

:::{prf:corollary}
:label: cor-st-geometric-bohr

Under the hypotheses of this section, one has

$$
b\operatorname{Aut}(c_0(I,B))\cong\operatorname{Sym}(I)  \quad\text{for finite nonempty }I,
$$

while

$$
b\operatorname{Aut}(c_0(\mathbb{N},B))=1,  \qquad  b\operatorname{Aut}(C(2^{\mathbb{N}})\otimes B)=1.
$$

Thus the last two automorphism groups have nontrivial universal minimal
flows but no nontrivial continuous homomorphisms to compact groups.
:::

:::{prf:proof}
{prf:ref}`prop-st-transfer` reduces the three Bohr compactifications to
those of $\operatorname{Sym}(I)$, $\operatorname{Sym}(\mathbb{N})$, and $\operatorname{Homeo}(2^{\mathbb{N}})$,
respectively. The finite case is immediate.

The countable direct-sum assertion also follows, without the extreme-amenability hypothesis, from {prf:ref}`cor-st-direct-sum-bohr-general`. For the Cantor-field group, use Tsankov's description of the irreducible
continuous unitary representations of the automorphism group of an
$\omega$-categorical structure with weak elimination of imaginaries: each is
induced from an irreducible representation of the automorphism group of a
finite algebraically closed substructure {cite}`Tsankov2012`, Corollary 5.2. The countable atomless Boolean algebra, whose
automorphism group is $\operatorname{Homeo}(2^{\mathbb{N}})$, is one of the structures
covered there, as the discussion following that corollary records. An
induced representation is finite dimensional only if the inducing subgroup
has finite index; every finite subalgebra larger than $\{0,1\}$ has
infinitely many conjugates, while the subalgebra $\{0,1\}$ gives only the
trivial representation. Hence the group has no nontrivial finite-dimensional
continuous unitary representation. By the Peter–Weyl theorem its Bohr
compactification is trivial.
:::

:::{prf:corollary}
:label: cor-st-geometric-amenability

For every nonempty finite or countable set
$I$, the group $\operatorname{Aut}(c_0(I,B))$ is amenable and its universal minimal flow
is uniquely ergodic. For $I=\mathbb{N}$, the unique measure on $\operatorname{LO}(\mathbb{N})$ is the uniform random-order measure, characterised by

$$
\mu\{L:L|_F=\ell\}=\frac1{|F|!}
$$

for every finite $F\subseteq\mathbb{N}$ and every linear order $\ell$ on $F$. In contrast, $\operatorname{Aut}(C(2^{\mathbb{N}})\otimes B)$ is nonamenable. Thus the
two infinite geometric examples in {prf:ref}`cor-st-geometric-bohr` are
both minimally almost periodic, but lie on opposite sides of amenability.
:::

:::{prf:proof}
The finitary permutations form a dense directed union of finite groups in $\operatorname{Sym}(\mathbb{N})$, so $\operatorname{Sym}(\mathbb{N})$ is amenable. Invariance forces all $|F|!$ orders on each finite set $F$ to have equal mass; these compatible
finite distributions define the random-order measure and determine it
uniquely. The finite symmetric-group case is Haar measure on the regular
finite flow. The group $\operatorname{Homeo}(2^{\mathbb{N}})$ is nonamenable {cite}`Tsankov2012`, remark
following Theorem 6.7. Apply {prf:ref}`prop-st-transfer`, including its unique-measure assertion, to {prf:ref}`prop-st-direct-sum` and {prf:ref}`prop-st-field`.
:::

### Unitisation

:::{prf:lemma}
:label: lem-st-unitization

If $B$ is nonunital and has no characters,
restriction induces a topological isomorphism

$$
\operatorname{Aut}(B^+)\cong\operatorname{Aut}(B).
$$
:::

:::{prf:proof}
The scalar quotient $B^+\to\mathbb{C}$ is the unique character: every
character restricts to either zero or a character on $B$, and the latter is
excluded. Its kernel $B$ is therefore characteristic. Restriction is inverse
to $\alpha(b+\lambda1)=\alpha(b)+\lambda1$. Both operations are point-norm
continuous.
:::

Stable Kirchberg algebras, their sums and fields here, and nonzero
stable AF algebras have no characters. Their automorphism conclusions
therefore persist for minimal unitisations. In particular this verifies
the unitisation assertion in {prf:ref}`thm-st-geometric`. Weighted
states on sums of unital fibers are treated in {cite}`LupiniUnital2026`.

:::{prf:proof}
*Proof of {prf:ref}`thm-st-geometric`.* The hypothesis holds for
$B=\mathcal{O}_2\otimes\mathcal{K}$ and $B=\mathcal{O}_3\otimes\mathcal{K}$, as recorded at the
start of this section. By {prf:ref}`prop-st-direct-sum` and {prf:ref}`prop-st-field`, the
universal minimal flows of $\operatorname{Aut}(c_0(I,B))$ and $\operatorname{Aut}(C(X)\otimes B)$ are those of
$\operatorname{Sym}(I)$ and $\operatorname{Homeo}(X)$, through the permutation of summand ideals and the
induced homeomorphism of $X$. For finite $I$ this is the regular flow of
$\operatorname{Sym}(I)$. For $I=\mathbb{N}$ and for the Cantor set it is $\operatorname{LO}(\mathbb{N})$ and
$\Phi(X)$, by the results of Glasner and Weiss recalled above
{cite}`GlasnerWeiss2002,Glasner2002Orders` and {cite}`GlasnerWeiss2003`, Theorem 6.1.
The Bohr compactifications are computed in {prf:ref}`cor-st-geometric-bohr`, and
amenability, unique ergodicity and nonamenability in
{prf:ref}`cor-st-geometric-amenability`. {prf:ref}`lem-st-unitization` and the paragraph
following it give the statements after unitisation. The final assertions, for
nonzero simple stable $C$, are {prf:ref}`cor-st-direct-sum-bohr-general`.
:::

(sec-st-unitaries)=
## Stable nuclear norm-unitary groups

For this section $A$ denotes a unital coefficient algebra and
$B=A\otimes\mathcal K$ its stabilisation. No separability of $A$ is
assumed. In the notation of Section 1 of {cite}`LupiniStable2026`, the group under
study is $V_B=U_1(B)_0$; the coefficient
algebra supplies the finite matrix corners, not a claim about norm
amenability of $U(A)$.

We use throughout two standard identifications, valid for every stable
$C^*$-algebra $B$. Writing $\lambda:B^+\to\mathbb C$ for the scalar quotient,
evaluation and normalization give the topological direct product

$$
U(B^+)\cong\mathbb T\times W_B,\qquad
 u\longmapsto(\lambda(u),\lambda(u)^{-1}u),
$$ (eq-st-scalar-splitting)

with inverse $(z,w)\mapsto zw$; and stability identifies the component
group of $W_B$ with $K$-theory,

$$
W_B/V_B\cong K_1(B)_{\mathrm{disc}}
$$ (eq-st-component-identification)

{cite}`Blackadar1998`, Section 8.1, the quotient being discrete because $V_B$
is open: every sufficiently small norm neighbourhood of the identity
consists of unitaries admitting logarithms in $B$. When $B=A\otimes\mathcal K$ we
write $K_1(B)=K_1(A)$.

For the norm metric $d(u,v)=\left\|u-v\right\|$, multiplication on either
side and inversion are isometries. A bounded family $\mathcal F$ of
functions is uniformly equicontinuous and bounded (UEB) if it is
bounded in supremum norm and has a common modulus of uniform continuity.
For a general topological group, UEB means uniformly bounded and
equicontinuous for the right uniformity: for each $\varepsilon>0$
there is an identity neighbourhood $V$ such that
$\left|f(vg)-f(g)\right|<\varepsilon$ for all $f\in\mathcal F$,
$v\in V$, and $g\in G$.
A net $\mu_i$ of Borel probabilities is asymptotically left invariant
in the UEB topology if, for each $g$ and each such $\mathcal F$,

$$
\sup_{f\in\mathcal F}
 \left|\int f(gx)\,d\mu_i(x)-\int f(x)\,d\mu_i(x)\right|\longrightarrow0.
$$

A net $(\mu_i)$ is a Lévy net if, for every open identity
neighbourhood $V$ and every net of Borel sets $B_i$ with
$\liminf_i\mu_i(B_i)>0$, one has $\mu_i(VB_i)\to1$.
In a metric group this is the usual concentration property at every
fixed positive radius. A Lévy group is a group admitting an increasing
directed family of compact subgroups with dense union whose normalised
Haar probabilities form a Lévy net; for Polish groups and sequences
this is the notion already used in [](#sec-st-dynamics).

:::{prf:theorem} Concentration criterion
:label: thm-st-schneider

If a Hausdorff topological group admits a Lévy net of Borel
probability measures converging to invariance in the UEB topology,
then it is whirly amenable.
:::

:::{prf:proof}
The general assertion is {cite}`Schneider2019`, Corollary 5.7.
We give a direct proof for the compactly supported regular probabilities
used in this paper, including the assertion about all invariant measures.

First, compactness and joint continuity of a compact $G$-flow $X$
imply that, for every real $f\in C(X)$, the orbit functions
$g\mapsto f(gx)$, as $x$ varies over $X$, form a UEB family.
Fix $x_0\in X$ and push $\mu_i$ forward by $g\mapsto gx_0$.
UEB convergence to left invariance makes every weak-* cluster point
of these probabilities $G$-invariant. Such a cluster point exists
by compactness of the space of regular probabilities on $X$.
This proves amenability.

We next record the consequence of concentration that, for every
real UEB family $\mathcal F$,

$$
\sup_{a\in\mathcal F}
 \int\left|a-\int a\,d\mu_i\right|^2d\mu_i\longrightarrow0.
$$ (eq-st-levy-variance)

Indeed, choose a median $m_i(a)$ of each $a$. The two sets
$\{a\leq m_i(a)\}$ and $\{a\geq m_i(a)\}$ have measure at least
$1/2$. Given $\varepsilon>0$, choose an identity neighbourhood
$V$ for which the oscillation of every $a\in\mathcal F$ on each
pair $(vg,g)$ is below $\varepsilon$. The Lévy property makes
the measures of both $V$-neighbourhoods tend to one, uniformly
over all these sets. This convergence is uniform: otherwise, for some
$c>0$, choose at a cofinal set of indices Borel sets $B_i$ with
$\mu_i(B_i)\geq1/2$ and $\mu_i(VB_i)\leq1-c$, and put
$B_i=G$ at the remaining indices, contradicting the Lévy-net
condition. Hence
$\mu_i\{|a-m_i(a)|>\varepsilon\}\to0$ uniformly in $a$.
Uniform boundedness gives convergence of the second moment about
the median to zero. The variance is no larger than that second
moment, proving {eq}`eq-st-levy-variance`.

Now let $\nu$ be any invariant regular probability measure on $X$,
fix $h\in G$ and real $f\in C(X)$, and put

$$
a_x(g)=f(gx),\qquad b_x(g)=f(hgx).
$$

These functions, for all $x\in X$, form a single UEB family.
By left UEB invariance,

$$
\sup_{x\in X}\left|\int b_x\,d\mu_i-\int a_x\,d\mu_i\right|\longrightarrow0.
$$

Equation {eq}`eq-st-levy-variance` and

$$
\int|b_x-a_x|^2d\mu_i
 \leq2\operatorname{Var}_{\mu_i}(a_x)
      +2\operatorname{Var}_{\mu_i}(b_x)
      +\left|\int b_x\,d\mu_i-\int a_x\,d\mu_i\right|^2
$$

therefore give $\sup_x\int|f(hgx)-f(gx)|^2d\mu_i(g)\to0$.
Integrate over $\nu$. Integration of the continuous function on
$\operatorname{supp}\mu_i\times X$ can be interchanged, and
$G$-invariance of $\nu$ yields

$$
\int_X|f(hx)-f(x)|^2d\nu(x)
 =\int_G\int_X|f(hgx)-f(gx)|^2d\nu(x)d\mu_i(g)
 \longrightarrow0.
$$

The left side is independent of $i$, so it is zero.
A continuous nonnegative function with zero integral vanishes on
$\operatorname{supp}\nu$. Since real continuous functions separate
points and $h$ was arbitrary, every point of this support is fixed
by $G$. This proves whirly amenability.
Extreme amenability follows because every compact flow has an
invariant probability with nonempty support.
:::

### A finite-dimensional correction

We use the following form of published stable uniqueness.

:::{prf:theorem} Dadarlat–Eilers
:label: thm-st-de

Let $E$ be separable, unital and residually finite dimensional, and
let $D$ be unital. Choose separating finite-dimensional unital
representations $\pi_k$ of $E$, each repeated infinitely often,
and put $\gamma_n=\bigoplus_{k\leq n}\pi_k:E\to M_{r_n}(\mathbb C)$.
If unital nuclear homomorphisms $\varphi,\psi:E\to D$ have equal
classes in $KK_{\mathrm{nuc}}(E,D)$, there are
$t_n\in U(M_{r_n+1}(D))$ such that

$$
\left\|t_n(\varphi(a)\oplus(\gamma_n(a)\otimes1_D))t_n^*
       -(\psi(a)\oplus(\gamma_n(a)\otimes1_D))\right\|\longrightarrow0
$$

for every $a\in E$.
:::

:::{prf:proof}
This is {cite}`DadarlatEilers2002`, Corollary 4.6, in its published formulation.
Nuclearity of the source is not a hypothesis. Nuclear homotopies give
equal $KK_{\mathrm{nuc}}$-classes; when either algebra is nuclear,
$KK_{\mathrm{nuc}}$ agrees with $KK$, as explained in
{cite}`DadarlatEilers2002`, Section 3.1.
:::

:::{prf:lemma} Simultaneous scalar-matrix correction
:label: lem-st-correction

Let $D$ be unital and nuclear. Given $u_1,\ldots,u_m\in U_0(D)$,
$\varepsilon>0$, and $R\in\mathbb N$, there exist $r\geq R$,
$q_1,\ldots,q_m\in U(r)$, and $t\in U(M_{r+1}(D))$ such that,
on writing

$$
\lambda_r(P)=\operatorname{diag}(1_D,P\otimes1_D),\qquad
 U_j=\operatorname{diag}(u_j,1_r\otimes1_D),
$$

one has

$$
\max_j\left\|t^*\lambda_r(q_j)tU_j-\lambda_r(q_j)\right\|<\varepsilon.
$$ (eq-st-correction)
:::

:::{prf:proof}
Take the *full* free-group algebra $E=C^*(\mathbb F_m)$, with
canonical generators $g_j$. It is residually finite dimensional:
{cite}`Choi1980`, Theorem 7 proves this for $m=2$, and the general case
reduces to it: $\mathbb F_m$ embeds as a subgroup of $\mathbb F_2$ for every finite
$m$, full group $C^*$-algebras of subgroups embed, and residual finite
dimensionality passes to $C^*$-subalgebras. For $m=1$ the algebra is
$C(\mathbb T)$, whose evaluations separate points. Define
$\varphi(g_j)=u_j^*$ and $\psi(g_j)=1_D$.
The universal property gives unital homomorphisms, and nuclearity
of the target makes both maps nuclear. Paths $u_j(s)$ from $1$
to $u_j$ define a homotopy

$$
\Phi:E\longrightarrow C([0,1],D),\qquad
 \Phi(g_j)(s)=u_j(s)^*.
$$

Its target is nuclear, so it is a nuclear homotopy.
Apply {prf:ref}`thm-st-de` to the generators. With
$q_j=\gamma_n(g_j)$ and $t=t_n$, the conclusion is

$$
\left\|t\operatorname{diag}(u_j^*,q_j\otimes1_D)t^*-\lambda_r(q_j)\right\|
 <\varepsilon.
$$

Conjugate back and multiply on the right by $U_j$ to obtain
{eq}`eq-st-correction`. Finally, replacing $q_j$ by $q_j\oplus1_s$
and $t$ by $t\oplus(1_s\otimes1_D)$ preserves this estimate.
Thus $r$ can be made arbitrarily large.
:::

### Haar averaging by commutators

For the data in {prf:ref}`lem-st-correction`, define

$$
z_P=t^*\lambda_r(P)t\lambda_r(P)^*\qquad(P\in U(r)).
$$ (eq-st-z)

The map is continuous and $z_1=1$. Connectedness of $U(r)$
therefore puts its entire image in $U_0(M_{r+1}(D))$.
No connectedness assumption on $t$ is needed.

:::{prf:lemma} Haar coupling
:label: lem-st-haar

Let $\mu$ be the image of Haar probability on $U(r)$ under
{eq}`eq-st-z`. For every $j$, $\mu$ and its right $U_j$-translate
admit a coupling supported on pairs at norm distance less than
$\varepsilon$. Also

$$
\left\|z_P-z_Q\right\|\leq 2\left\|P-Q\right\|_{\mathrm{op}}
                  \leq2\left\|P-Q\right\|_{\mathrm{HS}}.
$$ (eq-st-lipschitz)

The Hilbert–Schmidt norm here is unnormalized.
:::

:::{prf:proof}
Each $U_j$ commutes with every $\lambda_r(P)$. Direct multiplication
therefore gives

$$
\begin{split}
 z_P^*z_{Pq_j}U_j
 &=\lambda_r(P)t^*\lambda_r(q_j)t\lambda_r(Pq_j)^*U_j\\
 &=\lambda_r(P)\bigl(t^*\lambda_r(q_j)tU_j\bigr)\lambda_r(Pq_j)^*.
 \end{split}
$$

Equation {eq}`eq-st-correction` makes this element
$\varepsilon$-close to $1$. Consequently

$$
\sup_P\left\|z_{Pq_j}U_j-z_P\right\|<\varepsilon.
$$ (eq-st-coupling)

Since $P$ and $Pq_j$ have the same Haar law,
$(z_P,z_{Pq_j}U_j)$ is the required coupling.
For {eq}`eq-st-lipschitz`, change the two occurrences of $P$
one at a time and use the norm-one unitary factors.
Scalar matrix inclusion in $M_r(D)$ is isometric, independently
of $D$.
:::

:::{prf:lemma}
:label: lem-st-unitary-levy

Haar probability on $U(r)$, with unnormalized Hilbert–Schmidt
distance, is a Lévy family as $r\to\infty$.
:::

:::{prf:proof}
The assertion for $SU(r)$ is the classical concentration theorem;
see {cite}`GiordanoPestov2007`, Example 2.5, and {cite}`Meckes2019`, Theorem 5.17 for a
quantitative form that covers $U(r)$ directly. Let $S$ be Haar in $SU(r)$ and let
$\theta$ be independent and uniform on $[-\pi,\pi]$.
Then $P=e^{i\theta/r}S$ is Haar in $U(r)$. Indeed its determinant
is uniform and, conditionally on it, its law is Haar on the
corresponding determinant coset. Moreover

$$
\left\|P-S\right\|_{\mathrm{HS}}
 =\sqrt r\,|e^{i\theta/r}-1|\leq\pi/\sqrt r.
$$

This coupling transfers concentration to $U(r)$.
:::

### The stable group

:::{prf:theorem}
:label: thm-st-v

For every unital nuclear $A$, the norm group
$V_B=U_1(A\otimes\mathcal K)_0$ is whirly amenable.
:::

:::{prf:proof}
Put $B=A\otimes\mathcal K$ and
$e_k=1_A\otimes\sum_{\ell=1}^k e_{\ell\ell}$.
Fix $v_1,\ldots,v_m\in V_B$, and choose paths $v_j(s)$ from
$1$ to $v_j$. The set of all $v_j(s)-1$ is norm compact in $B$.
It follows that

$$
x_{j,k}(s)=1+e_k(v_j(s)-1)e_k\longrightarrow v_j(s)
$$

uniformly in $j,s$. For large $k$ these elements are invertible,
and their polar parts have the form

$$
b_{j,k}(s)=x_{j,k}(s)(x_{j,k}(s)^*x_{j,k}(s))^{-1/2}
          =1-e_k+a_{j,k}(s).
$$

They converge uniformly to $v_j(s)$, start at $1$, and
$a_{j,k}(s)\in U(M_k(A))$. In particular, the endpoints
$a_j=a_{j,k}(1)$ lie in $U_0(M_k(A))$.

Given $\eta>0$, choose $k$ so that
$\left\|1-e_k+a_j-v_j\right\|<\eta/2$.
Apply {prf:ref}`lem-st-correction` and {prf:ref}`lem-st-haar` with
$D=M_k(A)$ and error below $\eta/2$.
The matrix algebra $M_{r+1}(D)$ is a larger corner of $B$, with
its first $D$-block equal to the chosen $e_k$-corner.
Extend each $z_P$ by the identity outside this larger corner.
Its compact image lies in $V_B$.
Equation {eq}`eq-st-coupling` now gives, for each $j$, a coupling
of its Haar image $\mu$ with the right $v_j$-translate of $\mu$
at distance below $\eta$.

Direct the construction by triples $(F,\eta,R)$, with finite
$F\subset V_B$ increasing, $\eta\downarrow0$, and $R\to\infty$,
and require $r\geq R$. For a UEB family with common modulus
$\omega$, the preceding couplings bound the translation error
by $\omega(\eta)$. Thus the resulting net is asymptotically right
invariant in the UEB topology.

The maps defining its measures are uniformly $2$-Lipschitz for
unnormalized Hilbert–Schmidt distance by
{eq}`eq-st-lipschitz`. {prf:ref}`lem-st-unitary-levy` and $r\to\infty$
show that their images form a Lévy net for the norm uniformity
of $V_B$. Push the measures forward by inversion.
Inversion is an isometry and converts right invariance into left
invariance (with $g$ replaced by $g^{-1}$).
{prf:ref}`thm-st-schneider` applies.

The auxiliary source $C^*(\mathbb F_m)$ in {prf:ref}`lem-st-correction`
is separable even when $A$ is not; {prf:ref}`thm-st-de` permits an
arbitrary unital target $D=M_k(A)$. The corner approximation uses
norm compactness of finitely many paths, and the concentrating
probabilities are indexed by a net. Thus the proof requires no
separability assumption on $A$.
:::

:::{prf:remark}
:label: rem-st-stable-essential

The argument takes place in arbitrarily large finite corners of
$A\otimes\mathcal K$. It does not give norm amenability of $U(A)$ or
of a fixed $U(M_k(A))$. Also the matrices $q_j$ represent
$C^*(\mathbb F_m)$; they need not respect additional joint relations
of the original $u_j$. For example, a null-homotopic symmetry
$1-2p$ need not be supplemented by another symmetry.
There is consequently no assertion that projection $K_0$-classes
can be discarded in a fixed matrix corner.
:::

:::{prf:corollary} Nuclearity of stabilisations of unital algebras
:label: cor-st-nuclearity

Let $B=A\otimes\mathcal K$, with $A$ unital. The following are equivalent:

1. $B$ is nuclear;
2. $V_B$ is norm amenable;
3. $V_B$ is extremely amenable in norm;
4. $V_B$ is whirly amenable in norm;
5. $U((A\otimes\mathcal K)^+)$ is norm amenable.
:::

:::{prf:proof}
Nuclearity passes between $A$ and $A\otimes\mathcal K$, so {prf:ref}`thm-st-v` proves (i)$\Rightarrow$(iv), and
(iv)$\Rightarrow$(iii)$\Rightarrow$(ii) are immediate.
By {eq}`eq-st-scalar-splitting` and {eq}`eq-st-component-identification`
the two quotients of $U(B^+)$ by $V_B$ are abelian, so amenability of
$V_B$ implies (v) by extension stability.
Put $D=(A\otimes\mathcal K)^+$. Norm amenability of $U(D)$ makes $D$
strongly amenable by {cite}`AlekseevSchmidtThom2025`, Theorem 2.6, hence nuclear by Ozawa's
theorem {cite}`AlekseevSchmidtThom2025`, Theorem 2.2. Its ideal $A\otimes\mathcal K$ is nuclear, proving
(v)$\Rightarrow$(i). Alternatively, and directly: the norm
metric on $U(D)$ is bi-invariant, so inversion turns a left-invariant
mean on bounded norm-uniformly continuous functions into a
right-invariant mean on the same space; Paterson's invariant function
space $B_{22}(D)$ consists of functions uniformly continuous for the
relative weak topology {cite}`Paterson1991`, Proposition 3(d), hence also for
the norm topology, and restricting the right-invariant mean to
$B_{22}(D)$ and applying {cite}`Paterson1991`, Theorem 1 makes $D$
nuclear. Paterson's criterion is stated for the weak topology on the
unitary group; the norm topology is finer, so the restriction is
legitimate.
:::

:::{prf:remark}
:label: rem-st-ast

{prf:ref}`cor-st-nuclearity` proves the implication from nuclearity to
norm amenability of the unitary group, which is the open direction of
{cite}`AlekseevSchmidtThom2025`, Conjecture 1.1, for every algebra of the form
$D=(A\otimes\mathcal K)^+$ with $A$ unital and nuclear. For such a $D$ the
quotient tracial state property is automatic. Put $B=A\otimes\mathcal K$,
and let $I$ be a proper closed ideal of $D$. If $I\not\subseteq B$,
then $D=B+I$, so $D/I\cong B/(I\cap B)$ is stable. This is
impossible for the nonzero unital algebra $D/I$. Hence $I\subseteq B$,
and the scalar character $D\to\mathbb C$ descends to a tracial state on
$D/I$. Strong amenability of $(\mathcal O_n\otimes\mathcal K)^+$ was
already observed by Rosenberg {cite}`Rosenberg1977`; the norm
amenability of its unitary group is asked in {cite}`AlekseevSchmidtThom2025`, Section 4.1 and in
{cite}`LupiniCuntz2026`, Question 9.3, and
{prf:ref}`cor-st-cuntz-norm` answers both.
:::

(sec-st-unitary-flow)=
### The scalar-and-component flow

Applied to $B=A\otimes\mathcal K$, the identifications
{eq}`eq-st-scalar-splitting` and {eq}`eq-st-component-identification` read

$$
U(B^+)\cong\mathbb T\times W_B,\qquad W_B/V_B\cong K_1(A)_{\mathrm{disc}};
$$

the first is also recalled in {cite}`LupiniCuntz2026`, Section 5, and the
second can be seen directly by compressing compact paths into finite
matrix corners as in the proof of {prf:ref}`thm-st-v`.

:::{prf:proof}
*Proof of {prf:ref}`thm-st-nuclear-norm`.* These two identifications give the continuous open map

$$
q_U:U((A\otimes\mathcal K)^+)\longrightarrow\mathbb T\times K_1(A),\qquad
 q_U(u)=(\lambda(u),[\lambda(u)^{-1}u]),
$$

with kernel $V_B$. {prf:ref}`thm-st-v`, the kernel reduction in
{prf:ref}`prop-st-transfer`, and the compact-factor rule give

$$
M(U((A\otimes\mathcal K)^+))=\mathbb T\times M(K_1(A)).
$$

The action is $u\cdot(z,x)=(\lambda(u)z,[\lambda(u)^{-1}u]\cdot x)$.
{prf:ref}`cor-st-nuclearity` gives the nuclearity equivalences.
:::

:::{prf:corollary}
:label: cor-st-unitary-consequences

Let $A$ be unital and nuclear.

1. $W_B$ is whirly amenable exactly when it is extremely amenable,
   and exactly when $K_1(A)=0$.
2. $M(U((A\otimes\mathcal K)^+))$ is metrizable exactly when $K_1(A)$
   is finite. In that case it is $\mathbb T\times K_1(A)$, with translation
   through $q_U$.
3. $bU((A\otimes\mathcal K)^+)\cong\mathbb T\times b(K_1(A))$.
4. The full group $U((A\otimes\mathcal K)^+)$ is amenable and is never
   extremely amenable or whirly amenable.
5. For every compact $U((A\otimes\mathcal K)^+)$-flow $X$ and every
   invariant regular probability measure $\nu$,
   $\operatorname{supp}\nu\subseteq X^{V_B}$; the action on its support
   descends through $q_U$ to $\mathbb T\times K_1(A)$.
:::

:::{prf:proof}
For (i), if $K_1(A)=0$, then $W_B=V_B$, so use
{prf:ref}`thm-st-v`. Conversely, use the quotient by $V_B$;
a nontrivial discrete abelian
group has a nontrivial compact character and cannot be extremely
amenable. For (ii), a finite group is its own UMF, whereas an
infinite discrete group has nonmetrizable UMF {cite}`Pestov2006`.
Statement (iii) follows from
{prf:ref}`prop-st-transfer`. Amenability in (iv) follows by
extensions, and the nontrivial scalar quotient $\mathbb T$ excludes
extreme amenability and hence whirly amenability.
Statement (v) is the whirly-kernel part of {prf:ref}`prop-st-transfer`.
:::

:::{prf:example}
:label: ex-st-example-1

For a UCT Kirchberg algebra with $K_1(A)=\mathbb Z/2$, the stabilised
norm-unitary UMF is
$\mathbb T\times\mathbb Z/2$; with $K_1(A)=\mathbb Z$ it is
$\mathbb T\times M(\mathbb Z_{\mathrm{disc}})$.
The latter is not the Bohr compactification of $\mathbb Z$.
:::

### The real-rank-zero framework beyond nuclearity

The conditional component-and-flow theorem for stabilisations of
Kirchberg algebras is {cite}`LupiniCuntz2026`, Theorem 9.1. The theorem below
extends that framework to every separable stable real-rank-zero algebra,
including nonnuclear algebras, and adds the whirly-amenability equivalence
together with separate metrizability and Bohr conclusions. Its whirliness
input is recalled from {prf:ref}`lem-cu-stable-whirly`.

Here $A$ is again a stable algebra, and $W_A=U_1(A)$, $V_A=(W_A)_0$ in
the notation fixed in Section 1 of {cite}`LupiniStable2026`; the scalar splitting
{eq}`eq-st-scalar-splitting` and the component identification
{eq}`eq-st-component-identification` apply to it verbatim.

Polish Lévy groups are whirly by Glasner–Tsirelson–Weiss
{cite}`GlasnerTsirelsonWeiss2005`, Theorem 1.1 and Remark 1.4. Whirliness passes to topological
groups generated by continuous images of whirly groups: for an invariant
probability $\mu$, the same closed set $\operatorname{supp}\mu$ is fixed by each image and
then by the generated closure. This support argument avoids intersections of
arbitrarily many measurable sets of full measure.

:::{prf:proposition}
:label: prop-st-whirly

If $A$ is a separable stable $C^*$-algebra of real rank
zero, then the norm group $V_A=U_1(A)_0$ is whirly.
:::

:::{prf:proof}
The proof of {prf:ref}`lem-cu-stable-whirly` uses only stability to
place each projection circle in a copy of $U_1(\mathcal K)$, and real rank
zero to generate the identity component by those circles. These
hypotheses hold for the present algebra; nuclearity and simplicity
are not used. The same fixed-support argument applies.
:::

:::{prf:remark}
:label: rem-st-alternative-whirly

{prf:ref}`prop-st-whirly`, together
with the strict-density argument in [](#sec-st-kernel), gives a
second proof of the whirliness half of {prf:ref}`thm-st-kernel-ea`.
Let $A$ be a stable Kirchberg algebra. It has
real rank zero {cite}`Zhang1992`, Theorem 1.2(ii), so
{prf:ref}`prop-st-whirly` makes $V_A$ whirly in norm, and
{prf:ref}`lem-st-stable-u0-density` gives $N_A=\overline{\operatorname{Ad}(V_A)}$ in the
point-norm topology. The adjoint map $V_A\to N_A$ is continuous, since
norm convergence of unitaries implies point-norm convergence of their
conjugations. If $X$ is a compact Hausdorff $N_A$-flow with invariant
regular Borel probability measure $\mu$, pulling the action back along
$\operatorname{Ad}$ gives a continuous $V_A$-action preserving $\mu$, so whirliness of
$V_A$ gives

$$
\operatorname{supp}\mu\subseteq\operatorname{Fix}_{\operatorname{Ad}(V_A)}(X)=\operatorname{Fix}_{N_A}(X),
$$

the equality by density and closedness of point stabilisers. Amenability
of $N_A$ is not supplied by this argument, and is taken from
{prf:ref}`thm-st-kernel-ea`.
:::

:::{prf:theorem}
:label: thm-st-norm-dichotomy

Let $A$ be a separable stable $C^*$-algebra of
real rank zero. The following are equivalent:

1. $V_A$ is whirly amenable;
2. $V_A$ is extremely amenable;
3. $V_A$ is amenable;
4. $W_A$ is amenable;
5. $U(A^+)$ is amenable.

When these conditions hold,

$$
\begin{aligned}
M(W_A)&\cong M(K_1(A)_{\mathrm{disc}}),   \\
M(U(A^+))&\cong \mathbb{T}\times M(K_1(A)_{\mathrm{disc}}),
\end{aligned}
$$ (eq-st-norm-umf-k1)

with action through the scalar and component quotients. Moreover,

$$
\begin{split}
M(V_A)\text{ is metrizable} &\quad\Longleftrightarrow\quad V_A\text{ is
amenable} \\
&\quad\Longleftrightarrow\quad V_A\text{ is extremely amenable}
\\
&\quad\Longleftrightarrow\quad V_A\text{ is whirly amenable}
\quad\Longleftrightarrow\quad M(V_A)=\{*\},
\end{split}
$$ (eq-st-va-dichotomy)

and

$$
M(W_A)\text{ is metrizable} \quad\Longleftrightarrow\quad \bigl[K_1(A)\text{
is finite and }W_A\text{ is amenable}\bigr].
$$ (eq-st-wa-metrizability)

Finally,

$$
M(U(A^+))\text{ is metrizable} \quad\Longleftrightarrow\quad \bigl[K_1(A)\text{ is finite and }U(A^+)\text{ is amenable}\bigr].
$$ (eq-st-norm-metrizability)

In the metrizable case the flow in {eq}`eq-st-norm-umf-k1` is the compact
left-translation flow $\mathbb{T}\times K_1(A)$.
Furthermore, $W_A$ is whirly amenable if and only if it is extremely
amenable, and these conditions are equivalent to $K_1(A)=0$ and
amenability of $V_A$.
:::

:::{prf:proof}
The scalar splitting {eq}`eq-st-scalar-splitting` shows that $U(A^+)$ is amenable
exactly when $W_A$ is amenable. Amenability passes to open subgroups and is
preserved under extensions by amenable groups {cite}`AlekseevSchmidtThom2025`, Theorem 2.8. Since
$V_A$ is open in $W_A$ and the quotient in {eq}`eq-st-component-identification` is
abelian, $W_A$ is amenable exactly when $V_A$ is amenable. {prf:ref}`prop-st-whirly` makes the latter equivalent to whirly amenability of $V_A$,
which implies extreme amenability. Conversely, extreme amenability implies
amenability, proving all five equivalences.

Under these conditions, the whirly amenable normal-kernel reduction and {eq}`eq-st-component-identification` give

$$
M(W_A)\cong M(K_1(A)_{\mathrm{disc}}),  \qquad  M(U(A^+))\cong M(\mathbb{T}\times K_1(A)_{\mathrm{disc}}).
$$

The compact-factor rule recalled in [](#sec-st-dynamics) gives {eq}`eq-st-norm-umf-k1`.

The norm metric makes both $V_A$ and $W_A$ Polish SIN groups. If $M(V_A)$ is
metrizable, then $V_A$ is amenable by {cite}`BYMT2017`, Corollary 3.4; the
equivalences already proved and the definition of extreme amenability give {eq}`eq-st-va-dichotomy`. If $M(W_A)$ is metrizable, the same result makes $W_A$ amenable, while the universal minimal flow of its discrete quotient $K_1(A)$ is a metrizable factor and hence $K_1(A)$ is finite. Conversely,
amenability of $W_A$ makes $V_A$ whirly amenable, and finiteness of the
quotient makes the displayed formula for $M(W_A)$ metrizable. This proves {eq}`eq-st-wa-metrizability`.

For {eq}`eq-st-norm-metrizability`, first suppose the universal minimal flow
is metrizable. The norm metric makes $U(A^+)$ a Polish SIN group, so it is
amenable by {cite}`BYMT2017`, Corollary 3.4. The universal minimal flow of the
discrete quotient $K_1(A)$ is a factor. Since $K_1(A)$ is discrete, {prf:ref}`lem-st-locally-compact-umf` shows that metrizability forces it to be
finite. Conversely, amenability and finiteness of $K_1(A)$ make {eq}`eq-st-norm-umf-k1` the compact metrizable flow $\mathbb{T}\times K_1(A)$.
Finally, if $W_A$ is extremely amenable, it is amenable and its discrete
quotient $K_1(A)$ is extremely amenable. A discrete group with this property
is trivial, by {prf:ref}`lem-st-locally-compact-umf` and the compact-group
case. Thus $K_1(A)=0$ and $V_A$ is amenable. Conversely, those conditions
give $W_A=V_A$, which is whirly amenable by the equivalences above.
Whirly amenability implies extreme amenability, completing the last claim.
:::

:::{prf:corollary}
:label: cor-st-norm-bohr

Under the hypotheses of {prf:ref}`thm-st-norm-dichotomy`, the Bohr compactifications are

$$
bV_A=1,\qquad  bW_A\cong b(K_1(A)_{\mathrm{disc}}),\qquad  bU(A^+)\cong b(K_1(A)_{\mathrm{disc}})\times\mathbb{T}.
$$

These conclusions do not require amenability.
:::

:::{prf:proof}
Let $f:V_A\to C$ be a continuous homomorphism into a compact group, and
replace $C$ by the closure of its image. Haar probability on $C$, for the
left-translation action pulled back along $f$, has support all of $C$.
Whirliness therefore forces every point of $C$ to be fixed, so $f$ is
trivial. Thus every compact group image of $W_A$ factors through {eq}`eq-st-component-identification`. The first two formulas follow from the
universal property of the Bohr compactification, and the last follows from
the scalar splitting {eq}`eq-st-scalar-splitting`.
:::

:::{prf:corollary} The remaining stabilised Cuntz cases
:label: cor-st-cuntz-norm

For $3\leq n<\infty$, and for $n=\infty$, the norm group
$U_1(\mathcal O_n\otimes\mathcal K)$ is whirly amenable and

$$
M(U((\mathcal O_n\otimes\mathcal K)^+))=\mathbb T.
$$
:::

:::{prf:proof}
Each coefficient algebra is unital nuclear with $K_1=0$, so apply
{prf:ref}`thm-st-nuclear-norm`. The $n=2$ calculation remains the
existing result {prf:ref}`thm-cu-main`.
:::

Every stable Kirchberg algebra has a full unital nuclear corner.
Brown's theorem therefore lets {prf:ref}`thm-st-nuclear-norm` apply
to all of them, without UCT. Norm amenability is no longer an unresolved
input for this class. The conditional real-rank-zero formulation above
retains its purpose for algebras outside the nuclear class.

(sec-st-encyclopaedia-proofs)=
## Proofs of statements in [](#sec-operator-algebras)

:::{prf:proof}
*Proof of {prf:ref}`thm-lupini-stable`.* Part (1) is {prf:ref}`thm-st-kk`; whirly amenability of $N_A$ implies its
extreme amenability. Part (2) is {prf:ref}`cor-st-closed-preimages` with
$L=Q_A$. For part (3), the quotient in (2) is the group $Q_B$ of
{prf:ref}`thm-cu-stable-general`, and {prf:ref}`prop-cu-finite-k`
shows that it is countable and discrete, finite exactly when both free ranks
are at most one, and gives the order of the finite group and the
nonmetrizability in the other case. When $Q_B$ is finite,
$M(\mathrm{Aut}(A))$ is the translation flow of $Q_B$, by
{prf:ref}`thm-cu-stable-general` and {prf:ref}`prop-ea-normal`.
Finally, $\mathrm{Aut}(A)$ is amenable if and only if
$\mathrm{Aut}(K_0(A))$ and $\mathrm{Aut}(K_1(A))$ are, by
{prf:ref}`cor-st-amenability-k-groups`; for finitely generated groups
this means that both free ranks are at most one, as recorded in
[](#sec-st-computations).
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-lupini-stable-geometric`.* By {prf:ref}`prop-st-direct-sum`,
$M(\mathrm{Aut}(c_0(I,B)))\cong M(\mathrm{Sym}(I))$. For finite $I$ this is
$\mathrm{Sym}(I)$, as for every compact group
({prf:ref}`prop-ea-normal`), and for $I=\mathbb{N}$ it is
$\mathrm{LO}(\mathbb{N})$ by {prf:ref}`thm-glasner-weiss`. By
{prf:ref}`prop-st-field`,
$M(\mathrm{Aut}(C(X)\otimes B))\cong M(\mathrm{Homeo}(X))$, which is $\Phi(X)$
for the Cantor set $X$ by {prf:ref}`thm-gw-cantor`.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-lupini-stable-norm`.* The first two assertions are {prf:ref}`thm-st-nuclear-norm`. For
$C=\mathcal{O}_n$ one has $K_1(\mathcal{O}_n)=0$ {cite}`Cuntz1981`, so the
second factor is a point.
:::
