(sec-proofs-inductive-limits)=
# Proofs: inductive limits of compact Lie groups

This section reproduces, from the preprint of Codenotti and Lupini
{cite}`LupiniInductive2026` in its version of 13 September 2026, the proofs of
the results stated in [](#sec-inductive-limits). The text is that of
the preprint, with British spelling: its sections appear as subsections, its
macros are expanded and its labels renamed, and its introduction is reduced to
the statements of the main results and the notation they use. The preprint has
not been refereed. The last subsection derives the statements of
[](#sec-inductive-limits) from those of the preprint.

(sec-ind-main-results)=
## Main results of the preprint

:::{prf:theorem}
:label: thm-ind-main

Let $K_1\subseteq K_2\subseteq\cdots$ be compact Lie groups, and give
$G=\bigcup_nK_n$ the final topology. Suppose that, for some $j$,
$K_j^0$ is nonabelian or $K_j/K_j^0$ is nonsolvable. Then $G$ has a
jointly continuous action on a nonempty compact metrizable space $X$
such that $X^{K_j}=\varnothing$. In particular, $G$ is not extremely
amenable.
:::

Here $K^0$ denotes the identity component. For a compact Lie group,
$K/K^0$ is finite, and an abelian identity component is a torus, with
the trivial group allowed as a zero-dimensional torus. The hypothesis on
$K_j$ therefore says exactly that $K_j$ is not solvable.

:::{prf:corollary}
:label: cor-ind-classical-intro

With the standard block embeddings and final topologies, none of

$$
\varinjlim\operatorname{SU}(n),\qquad \varinjlim\operatorname{SO}(n),\qquad
\varinjlim\operatorname{Sp}(n),\qquad \varinjlim\operatorname{U}(n),\qquad
\varinjlim\operatorname{O}(n)
$$

is extremely amenable. The notation $\operatorname{Sp}(n)$ denotes the compact group
of quaternionic unitary matrices.
:::

Throughout, $\operatorname{SU}(\infty)$ denotes $\varinjlim\operatorname{SU}(n)$, and analogously
for $\operatorname{SO}(\infty)$, $\operatorname{Sp}(\infty)$, $\operatorname{U}(\infty)$, and $\operatorname{O}(\infty)$.
Unless another topology is explicitly specified, these symbols carry
the final topology for the standard block embeddings.

The proof of {prf:ref}`thm-ind-main` uses the full fixed-set prescription
in Oliver's Theorem 4 and Proposition 8, combined in his Theorem 5
{cite}`Oliver1976`. Its role is
to provide equivariant maps between successive disks. An inverse limit
then carries the action of the whole union. Ordinary existence of a
fixed-point-free disk for each stage would not by itself provide those
maps. [](#sec-ind-observables) gives a finite-observable version
of the obstruction.

Write $M(G)$ for the universal minimal flow and $bG$ for the Bohr
compactification of a topological group $G$; the definitions are recalled
in [](#sec-ind-bohr) and [](#sec-ind-umf).

:::{prf:theorem}
:label: thm-ind-dynamics-intro

For each of the five classical limits in
{prf:ref}`cor-ind-classical-intro`, $M(G)$ contains a homeomorphic copy
of the Stone–Čech compactification $\beta\mathbb N$ of the discrete natural
numbers. In particular, $M(G)$ is nonmetrizable. Moreover,

$$
\begin{gathered}
b\operatorname{SU}(\infty)=b\operatorname{SO}(\infty)=b\operatorname{Sp}(\infty)=\{1\},\\
b\operatorname{U}(\infty)\cong\mathbb T,\qquad b\operatorname{O}(\infty)\cong\{1,-1\},
\end{gathered}
$$

where the last two Bohr maps are the determinants.
:::

The Bohr calculation uses only finite-dimensional representations.
The assertion about $M(G)$ uses the compact metrizable actions above,
a separation lemma specific to the final topology, and a criterion of
Basso–Zucker valid for arbitrary topological groups
{cite}`BassoZucker2021`. A compact metrizable action without fixed points
alone would not imply nonmetrizability of $M(G)$.

The universal minimal actions also exhibit a distinction between
freeness everywhere and freeness on a large subset. In
[](#sec-ind-free-locus) we prove the following result, whose first
assertion answers Pestov's Question 4.

:::{prf:theorem}
:label: thm-ind-free-intro

For each of the five classical limits, every jointly continuous action
on a nonempty compact Hausdorff space has a point with nontrivial
stabiliser. Consequently, none of these $k_\omega$-groups admits a free
action on a compact space. Nevertheless, the free locus in $M(G)$ is a
proper dense $G_\delta$ and has full measure for every invariant Radon
probability measure.
:::

Question 4 asks whether Veech's theorem, that every locally compact
group admits a free action on a compact space, extends to
$k_\omega$-groups {cite}`Pestov2007`, p. 440;
{prf:ref}`thm-ind-free-intro` shows that it does not.
Nonfreeness follows from McGibbon's theorem on maps from infinite
loop spaces and the Zabrodsky lemma. The assertion about the free
locus uses the stage stabilisers supplied by the Oliver construction
and a generic-vector argument.

[](#sec-ind-relative)–11 of {cite}`LupiniInductive2026` and
[](#sec-ind-separation) compare these final-topology results with
a coarser trace-norm topology. Let
$G_{\mathrm{alg}}=\bigcup_n\operatorname{SU}(n)$ denote the canonical algebraic union. We write
$G_{\mathrm{fin}}$ for $G_{\mathrm{alg}}$ with the final topology and $G_{\mathrm{tr}}$ for
$G_{\mathrm{alg}}$ with the topology of the unnormalized trace-norm metric
$d_1(g,h)=\operatorname{Tr}\lvert g-h\rvert$. The completion of $G_{\mathrm{tr}}$ is

$$
\operatorname{SU}_1=\{u\in\operatorname{U}(\ell^2):u-I\in\mathcal S_1,\ \det_F(u)=1\},
$$ (eq-ind-suone)

where $\det_F$ is the Fredholm determinant.

Throughout we write $e$ for the identity element of a group and $I$ for
the identity operator on a Hilbert space. Identity components of compact
Lie groups are written $K^0$. The symbol $\mathcal F(K)$ is reserved for
Oliver's family of closed solvable subgroups. Averaging over a compact
subgroup $K$ is written $\operatorname{Avg}_K$; the orthogonal projection onto
$K$-fixed vectors in a unitary representation is written $\operatorname{P}^{\mathrm{fix}}_K$.

For a compact group $K$ with normalised Haar measure, we use

$$
\operatorname{Var}_{k\in K}\phi(k)
:=\int_K\lvert\phi(k)-\int_K\phi(k')\,\mathrm d k'\rvert^2\,\mathrm d k.
$$ (eq-ind-variance-convention)

:::{prf:theorem}
:label: thm-ind-trace-intro

The groups $G_{\mathrm{tr}}$ and $\operatorname{SU}_1$, each with its trace-norm topology, are
extremely amenable. More precisely, if
$N>m\ge2$ and $f:\operatorname{SU}(N)\to\mathbb R$ is $L$-Lipschitz for $d_1$, then

$$
\int_{\operatorname{SU}(N)}\operatorname{Var}_{k\in\operatorname{SU}(m)}f(kh)\,\mathrm d h
\le \frac{2mL^2}{N-m}.
$$ (eq-ind-variance-intro)

All Haar measures are normalised to have mass one.
:::

The estimate concerns variance along a fixed subgroup. It does not
assert concentration of $f$ around its mean over the entire large
group. The final topology in {prf:ref}`thm-ind-main` is strictly finer;
[](#sec-ind-separation) gives an explicit function separating
the two right uniformities.

(sec-ind-inverse)=
## Inverse limits of compact actions

We first isolate the topological construction. No smoothness is needed
in this section.

:::{prf:lemma}
:label: lem-ind-inverse-action

Let $G=\bigcup_{n\ge1}K_n$ be a topological group with the final
topology for an increasing sequence of topological groups. Suppose
that $X_n$ is a nonempty compact Hausdorff $K_n$-space and that

$$
p_n:X_{n+1}\longrightarrow X_n
$$

is continuous and $K_n$-equivariant, where the action on $X_{n+1}$ is
restricted from $K_{n+1}$. Then $X=\varprojlim(X_n,p_n)$ is a nonempty
compact Hausdorff $G$-space. The projection $X\to X_n$ is
$K_n$-equivariant. If every $X_n$ is metrizable, so is $X$.
:::

:::{prf:proof}
The compatibility equations $p_n(x_{n+1})=x_n$ define closed subsets
of the compact product $\prod_nX_n$. Every finite collection of these
equations is satisfiable: choose the largest relevant coordinate and
apply the bonding maps downwards, then fill later coordinates
arbitrarily. The finite intersection property gives $X\ne\varnothing$.
This argument does not require any bonding map to be surjective.

For $n<m$, write $p_{n,m}=p_n\circ\cdots\circ p_{m-1}$, and set
$p_{m,m}=\operatorname{id}$. If $g\in K_m$, define

$$
(g\cdot x)_n=
\begin{cases}
g\cdot x_n,&n\ge m,\\
p_{n,m}(g\cdot x_m),&n<m.
\end{cases}
$$ (eq-ind-tail-action)

For $n\ge m$, equivariance of $p_n$ preserves the compatibility
equations. At earlier coordinates compatibility follows by composition.
If $r\ge m$, then for $m\le n\le r$,

$$
p_{n,r}(g\cdot x_r)=g\cdot p_{n,r}(x_r)=g\cdot x_n.
$$

Thus the formula is independent of the chosen stage containing $g$.
To check the action law, choose a common stage containing two given
group elements and use the action law on all later coordinates;
earlier coordinates follow by applying the bonding maps.

For a fixed $m$, every coordinate of the map $K_m\times X\to X$ in
{eq}`eq-ind-tail-action` is continuous. Hence each stage action is
jointly continuous and induces a continuous homomorphism

$$
\rho_m:K_m\longrightarrow\operatorname{Homeo}(X),
$$

where $\operatorname{Homeo}(X)$ has the compact-open topology. For completeness,
if $C\subseteq X$ is compact, $U\subseteq X$ is open, and
$g_0C\subseteq U$, joint continuity and compactness of $C$ give a
neighbourhood $V$ of $g_0$ with $VC\subseteq U$. This proves
continuity for the subbasic compact-open sets.

The maps $\rho_m$ agree on overlaps, and finality makes the assembled
homomorphism $\rho:G\to\operatorname{Homeo}(X)$ continuous. Evaluation
$\operatorname{Homeo}(X)\times X\to X$ is continuous because $X$ is compact
Hausdorff. Therefore the action of $G$ is jointly continuous.
Projection to $X_n$ is $K_n$-equivariant by the formula. Finally, a
closed subspace of a countable product of compact metrizable spaces
is compact metrizable.
:::

:::{prf:remark}
:label: rem-ind-remark-1

Joint continuity above follows by passing through $\operatorname{Homeo}(X)$.
It is not inferred merely from continuity of individual orbit maps.
:::

(sec-ind-oliver)=
## Oliver disks and the general obstruction

For a compact Lie group $K$, define

$$
\mathcal F(K)=\{H\le K:H\text{ is closed},\ H^0\text{ is a torus},
\ H/H^0\text{ is solvable}\}.
$$ (eq-ind-family)

Equivalently, $\mathcal F(K)$ is the family of closed solvable subgroups of
$K$: a compact Lie group $H$ is solvable if and only if $H^0$ is a torus
and $H/H^0$ is solvable. The condition is intrinsic to $H$. In
particular, if $K\le L$ is a closed subgroup inclusion, then for every
closed $H\le K$,

$$
H\in\mathcal F(K)\quad\Longleftrightarrow\quad H\in\mathcal F(L).
$$ (eq-ind-intrinsic)

:::{prf:theorem} Oliver
:label: thm-ind-oliver

For every compact Lie group $K$, there is a smooth action on a compact
disk $D_K$ such that, for every closed subgroup $H\le K$,

$$
D_K^H\text{ is a disk if }H\in\mathcal F(K),
\qquad D_K^H=\varnothing\text{ otherwise}.
$$ (eq-ind-fixed-sets)
:::

:::{prf:proof}
*Reference.* We recall Oliver's terminology. A compact Lie group is *$p$-toral*
if its identity component is a torus and its component group is a
$p$-group, and *prime toral* if it is $p$-toral for some prime $p$
{cite}`Oliver1976`, p. 80. A family $\mathcal G$ of closed subgroups is
*separating* if, for every pair $H\trianglelefteq L$ of closed
subgroups with $L/H$ prime toral, either both $H$ and $L$ lie in
$\mathcal G$ or neither does; *closed* refers to the Hausdorff
topology on the space of closed subgroups, not to closure under passage
to subgroups {cite}`Oliver1976`, pp. 92–93. Proposition 8 of
{cite}`Oliver1976`, p. 95 states that {eq}`eq-ind-family` is a closed
separating family. It is nonempty because it contains the trivial
subgroup, and it is conjugation invariant because its defining condition
is intrinsic. Theorem 4 of {cite}`Oliver1976`, p. 94 gives precisely
{eq}`eq-ind-fixed-sets`. For $K$ as in {prf:ref}`thm-ind-main`, the two
statements are combined in Theorem 5 of {cite}`Oliver1976`, p. 96.
:::

:::{prf:lemma}
:label: lem-ind-bonding

If $K\le L$ are compact Lie groups and $D_K,D_L$ are chosen as in
{prf:ref}`thm-ind-oliver`, there is a continuous $K$-equivariant map
$D_L\to D_K$.
:::

:::{prf:proof}
The restricted smooth action of $K$ on $D_L$ admits a $K$-CW
structure, by equivariant triangulation for smooth compact Lie group
actions, including the boundary case
{cite}`Illman1983`, Section 7, especially Theorem 7.1 and Corollary 7.2.
Illman uses his own notion of an equivariant CW complex, which differs in
general from Matumoto's {cite}`Illman1983`, Remark 6.2; the two agree for a
smooth compact manifold, and all that is used below is the decomposition
into equivariant cells $K/H\times B^q$ with closed stabilisers $H$.
For a cell stabiliser $H$, the fixed set $D_L^H$ is nonempty. Hence
$H\in\mathcal F(L)$, and {eq}`eq-ind-intrinsic` gives $H\in\mathcal F(K)$.

Construct the map cell by cell. On a zero-dimensional equivariant
cell $K/H$, choose a point of the nonempty space $D_K^H$.
For a cell $K/H\times B^q$ with $q>0$, an equivariant map already
defined on its boundary is determined by a map
$\partial B^q\to D_K^H$. Since $D_K^H$ is contractible, this map
extends over $B^q$. The weak topology of the equivariant CW structure
gives a continuous map on the whole space. The resulting map need not
be surjective; {prf:ref}`lem-ind-inverse-action` does not require
surjective bonding maps.
:::

:::{prf:remark}
:label: rem-ind-remark-2

The two $K$-disks in {prf:ref}`lem-ind-bonding` have exactly the same
fixed-set prescription. Oliver observes, without proof, that two
disk actions corresponding to the same family are equivariantly homotopy
equivalent {cite}`Oliver1976`, p. 96. The cellular proof above spells out the
existence of the map needed here.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-ind-main`.* Discarding the finitely many stages before $K_j$ does not change the
union or its final topology. Choose $D_n=D_{K_n}$ for $n\ge j$.
{prf:ref}`lem-ind-bonding` provides $K_n$-equivariant maps
$p_n:D_{n+1}\to D_n$. {prf:ref}`lem-ind-inverse-action` yields a
nonempty compact metrizable $G$-space

$$
X=\varprojlim_{n\ge j}(D_n,p_n).
$$

By hypothesis $K_j\notin\mathcal F(K_j)$, so
$D_j^{K_j}=\varnothing$. The $K_j$-equivariant projection $X\to D_j$
implies $X^{K_j}=\varnothing$, and therefore $X^G=\varnothing$.
:::

:::{figure} ../../figures/inverse-limit-disks.svg
:name: fig-inverse-limit-disks
:figclass: enc-figure
:alt: The disks D_j, D_(j+1), D_(j+2) with the groups K_n acting on them and the maps p_n between them, their inverse limit X with the action of G, and the projection from X to D_j
:width: 100%

The proof of {prf:ref}`thm-ind-main`. {prf:ref}`lem-ind-bonding` gives $K_n$-equivariant maps $p_n\colon D_{n+1}\to D_n$ between the disks $D_n=D_{K_n}$ of {prf:ref}`thm-ind-oliver`, and {prf:ref}`lem-ind-inverse-action` makes $X=\varprojlim_{n\ge j}(D_n,p_n)$ a nonempty compact metrizable $G$-space whose projection to $D_j$ is $K_j$-equivariant. Since $D_j^{K_j}=\varnothing$, also $X^{K_j}=\varnothing$, and therefore $X^G=\varnothing$. (Illustration added for the encyclopaedia.)
:::

:::{prf:remark}
:label: rem-ind-sharpness

The hypothesis of {prf:ref}`thm-ind-main` says exactly that some stage is
not solvable, and it cannot be dropped from the present method. Let $K$ be
a solvable compact Lie group. The trivial subgroup lies in $\mathcal F(K)$, and
$K^0$ is a torus and therefore prime toral, so the separating property
places $K^0$ in $\mathcal F(K)$. The finite solvable group $K/K^0$ has a chief
series with elementary abelian factors; pulling it back gives a chain
$K^0=N_0\trianglelefteq\cdots\trianglelefteq N_m=K$ with each $N_{i+1}/N_i$
a finite elementary abelian $p$-group, hence prime toral. Applying the
separating property along the chain gives $K\in\mathcal F(K)$, so the disk of
{prf:ref}`thm-ind-oliver` satisfies $D_K^K\ne\varnothing$. This is the
observation recorded after Theorem 4 in {cite}`Oliver1976`, p. 94. It does
not say that a solvable compact Lie group admits no fixed-point-free smooth
action on a disk, only that no such action has all of its subgroup fixed
sets disks or empty.
:::

When every stage is solvable, extreme amenability can still fail for
unrelated reasons. For $G=\bigcup_n\mathbb T^n$ with the standard inclusions the
first coordinate $z\mapsto z_1$ is compatible with the inclusions and
defines a continuous surjective homomorphism $G\to\mathbb T$, so $G$ acts on $\mathbb T$
without a fixed point. This obstruction is absent as soon as $G$ is
minimally almost periodic.

:::{prf:remark} Question
:label: rem-ind-solvable-stages

Let $G=\bigcup_nK_n$ be an increasing union of solvable compact Lie groups
with the final topology, and suppose that $G$ is minimally almost periodic.
Is $G$ extremely amenable?
:::

The coordinate projection $\bigcup_n\mathbb T^n\to\mathbb T$ is excluded by the
minimal almost periodicity hypothesis, so the question is not settled
by that elementary quotient.

(sec-ind-classical)=
## The classical groups

The embeddings are the standard block inclusions over
$\mathbb R$, $\mathbb C$, or the quaternions, as appropriate.

:::{prf:corollary}
:label: cor-ind-semisimple-classical

The groups $\varinjlim\operatorname{SU}(n)$, $\varinjlim\operatorname{SO}(n)$, and
$\varinjlim\operatorname{Sp}(n)$, with their final topologies, are not extremely
amenable. They admit compact metrizable actions with no
$\operatorname{SU}(2)$-fixed point, no $\operatorname{SO}(3)$-fixed point, and no
$\operatorname{Sp}(1)$-fixed point, respectively.
:::

:::{prf:proof}
The compact Lie groups $\operatorname{SU}(2)$, $\operatorname{SO}(3)$, and
$\operatorname{Sp}(1)\cong\operatorname{SU}(2)$ are connected and nonabelian. Apply
{prf:ref}`thm-ind-main` at these stages. The real and quaternionic block
embeddings are smooth closed subgroup embeddings, so they satisfy the
same hypotheses.
:::

The special orthogonal and symplectic cases are instances of the
same obstruction. For the full unitary and orthogonal groups there
are simpler obstructions.

:::{prf:proposition}
:label: prop-ind-determinants

The final-topology groups $\varinjlim\operatorname{U}(n)$ and
$\varinjlim\operatorname{O}(n)$ are not extremely amenable.
:::

:::{prf:proof}
Compatibility with the embeddings gives surjective homomorphisms

$$
\det:\varinjlim\operatorname{U}(n)\longrightarrow\mathbb T,
\qquad
\det:\varinjlim\operatorname{O}(n)\longrightarrow\{1,-1\}.
$$

Both are continuous by finality, because their restrictions to every
finite stage are continuous. Acting by multiplication through the
first homomorphism on $\mathbb T$, or through the second on $\{1,-1\}$,
gives a jointly continuous compact action without a global fixed
point. In either case an element of determinant $-1$ fixes no point
of the indicated space.
:::

{prf:ref}`thm-ind-main` also applies directly to these two groups by
using $\operatorname{U}(2)$ and $\operatorname{O}(3)$. The determinant proof records the
elementary reason specific to the standard embeddings. The unitary
case was already noted in {cite}`CacciatoriUrsino2023`; these quotient
arguments are included for context rather than as novelty claims.

(sec-ind-bohr)=
## Bohr compactifications

The *Bohr compactification* of a topological group $G$ is a compact
Hausdorff group $bG$ with a continuous homomorphism $\eta_G:G\to bG$
having dense image, such that every continuous homomorphism from $G$
to a compact Hausdorff group factors uniquely through $\eta_G$ by a
continuous homomorphism. A group with $bG=\{1\}$ is called
*minimally almost periodic*.

:::{prf:lemma}
:label: lem-ind-no-finite-representations

Every continuous finite-dimensional unitary representation of
$\operatorname{SU}(\infty)$, $\operatorname{SO}(\infty)$, or $\operatorname{Sp}(\infty)$ is trivial.
The same conclusion holds for any topology on the algebraic union
for which all stage inclusions are continuous.
:::

:::{prf:proof}
Let $\rho:G\to\operatorname{U}(d)$ be such a representation. Its restriction to a
finite stage $K_n$ is a continuous homomorphism of Lie groups, hence
is smooth. For all sufficiently large $n$, the real Lie algebra
$\mathfrak k_n$ is simple and

$$
\dim\mathfrak k_n>d^2=\dim\mathfrak u(d).
$$

Here the dimensions of $\mathfrak{su}(n)$, $\mathfrak{so}(n)$, and
$\mathfrak{sp}(n)$ are respectively $n^2-1$, $n(n-1)/2$, and
$n(2n+1)$; in the orthogonal case we take $n\ge5$ to avoid the
low-dimensional exceptions. The kernel of
$d\rho_n:\mathfrak k_n\to\mathfrak u(d)$ is an ideal, so simplicity
makes $d\rho_n$ either zero or injective. The dimension inequality
excludes injectivity. Since $K_n$ is connected, $\rho|_{K_n}=1$.
Every element of $G$ belongs to an arbitrarily large stage, proving
the assertion.
:::

:::{prf:proposition}
:label: prop-ind-bohr-classical

For the standard classical limits with their final topologies,

$$
\begin{gathered}
b\operatorname{SU}(\infty)=b\operatorname{SO}(\infty)=b\operatorname{Sp}(\infty)=\{1\},\\
b\operatorname{U}(\infty)\cong\mathbb T,\qquad b\operatorname{O}(\infty)\cong\{1,-1\}.
\end{gathered}
$$

The last two Bohr maps are the determinants.
:::

:::{prf:proof}
If $G$ is one of the first three groups and $\phi:G\to C$ is a
continuous homomorphism to a compact Hausdorff group, compose $\phi$
with every finite-dimensional continuous unitary representation of
$C$. {prf:ref}`lem-ind-no-finite-representations` makes all these
compositions trivial. The Peter–Weyl theorem says that these
representations separate points of $C$, so $\phi$ is trivial.

For $G=\operatorname{U}(\infty)$, the same argument applied to the special unitary
subgroup shows that every such $\phi$ kills $\operatorname{SU}(\infty)$. The
inclusion of this subgroup, equipped with its own final topology, is
continuous by finality. Since
$\ker(\det:G\to\mathbb T)=\operatorname{SU}(\infty)$, the homomorphism factors uniquely
through $\det$. The factor is continuous because
$s(z)=\operatorname{diag}(z,1,1,\ldots)$ is a continuous section: the factor is
$\phi\circ s$. The determinant is continuous by finality and is
surjective, so it has the required universal property.

The orthogonal case is identical, using
$\ker(\det:\operatorname{O}(\infty)\to\{1,-1\})=\operatorname{SO}(\infty)$ and the section
$s(\varepsilon)=\operatorname{diag}(\varepsilon,1,1,\ldots)$.
:::

(sec-ind-umf)=
## Nonmetrizable universal minimal flows

A *minimal flow* is a nonempty compact Hausdorff $G$-space in
which every orbit is dense. The *universal minimal flow* $M(G)$
is the minimal flow admitting a continuous equivariant surjection onto
every minimal $G$-flow; it exists and is unique up to isomorphism.
We prove that the classical groups considered here have universal
minimal flows containing $\beta\mathbb N$. The embedding is topological;
no prescribed action on $\beta\mathbb N$ is asserted.

### Finite-stage orbits and commuting tails

:::{prf:lemma}
:label: lem-ind-compact-centralizer

Suppose a compact Hausdorff group $K$ acts transitively on a compact
Hausdorff space $Y$, and write $Y\cong K/L$ for a closed subgroup
$L\le K$. The centraliser of $K$ in $\operatorname{Homeo}(Y)$, with the compact-open
topology, is a compact group isomorphic to $N_K(L)/L$.
:::

:::{prf:proof}
A $K$-equivariant homeomorphism is determined by the image $aL$ of
$L$. Since a bijective equivariant map preserves stabilisers, we have
$aLa^{-1}=L$, so $a\in N_K(L)$. Conversely, each $a\in N_K(L)$
defines a $K$-equivariant homeomorphism by $kL\mapsto ka^{-1}L$.
This convention gives a homomorphism from $N_K(L)$ with kernel $L$.
The resulting map $N_K(L)/L\to\operatorname{Homeo}(Y)$ is continuous: the displayed
action is jointly continuous, and compactness of $Y$ gives continuity
into the compact-open topology. It is a bijection onto the centraliser.
Its domain is compact and its codomain Hausdorff, so it is a
homeomorphism onto that centraliser.
:::

For the rest of this subsection let $(G,G_{\mathrm{ss}},L_0)$ be one of the triples
in the following table. The middle column is a closed subgroup of $G$
isomorphic to one of $\operatorname{SU}(\infty)$, $\operatorname{SO}(\infty)$, or $\operatorname{Sp}(\infty)$.
All subgroups use the standard coordinate
blocks; $K_n$ denotes the corresponding full finite stage of $G$.

$$
\begin{array}{c|c|c}
G&G_{\mathrm{ss}}&L_0\\\hline
\operatorname{SU}(\infty)&\operatorname{SU}(\infty)&\operatorname{SU}(2)\\
\operatorname{SO}(\infty)&\operatorname{SO}(\infty)&\operatorname{SO}(3)\\
\operatorname{Sp}(\infty)&\operatorname{Sp}(\infty)&\operatorname{Sp}(1)\\
\operatorname{U}(\infty)&\operatorname{SU}(\infty)&\operatorname{SU}(2)\\
\operatorname{O}(\infty)&\operatorname{SO}(\infty)&\operatorname{SO}(3)
\end{array}
$$

:::{prf:lemma}
:label: lem-ind-stage-orbits-nowhere-dense

Let $Y$ be a minimal $G$-flow on which $G_{\mathrm{ss}}$ acts nontrivially.
Then $K_ny$ is nowhere dense in $Y$ for every $n$ and $y\in Y$.
:::

:::{prf:proof}
Suppose $A=\operatorname{Int}(K_ny)$ is nonempty. Minimality implies
that the translates $gA$, $g\in G$, cover $Y$. Choose a finite
subcover $g_1A,\ldots,g_rA$, and a stage $K_N$ containing $K_n$ and
all $g_i$. Then $Y=K_Ny$.

Let $T_N$ be the copy of $G_{\mathrm{ss}}$ acting on coordinates strictly after $N$
and fixing the first $N$ coordinates. Give it its own final topology.
Its inclusion into $G$ is continuous, since this holds on every stage.
The groups $T_N$ and $K_N$ commute, so the action of $T_N$ takes
values in the compact centraliser supplied by
{prf:ref}`lem-ind-compact-centralizer`. {prf:ref}`prop-ind-bohr-classical`
applies to this shifted copy of $G_{\mathrm{ss}}$ and makes its action trivial.

Every element of $G_{\mathrm{ss}}$ is conjugate in $G$ to an element of $T_N$:
move its finite coordinate block into the tail by a finitary
orthogonal, unitary, or quaternionic unitary matrix. In the special
orthogonal and special unitary cases, correct the determinant on an
additional unused coordinate if necessary. The kernel of the action
is normal in $G$, and hence contains all of $G_{\mathrm{ss}}$. This contradicts
the hypothesis. Finally, $K_ny$ is compact and therefore closed, so
empty interior implies that it is nowhere dense.
:::

:::{prf:lemma}
:label: lem-ind-semisimple-witness

For every triple above there is a nonempty compact metrizable minimal
$G$-flow $Y$ with $Y^{L_0}=\varnothing$.
:::

:::{prf:proof}
For $\operatorname{SU}(\infty)$, $\operatorname{SO}(\infty)$, and $\operatorname{Sp}(\infty)$, use the
actions in {prf:ref}`cor-ind-semisimple-classical` and take a minimal
subflow. For $\operatorname{U}(\infty)$, apply {prf:ref}`thm-ind-main` to the chain

$$
\operatorname{SU}(2)\subset\operatorname{U}(2)\subset\operatorname{U}(3)\subset\cdots.
$$

For $\operatorname{O}(\infty)$ use
$\operatorname{SO}(3)\subset\operatorname{O}(3)\subset\operatorname{O}(4)\subset\cdots$ instead.
Adding the first compact subgroup does not change the union or its
final topology: continuity of its inclusion into the next stage
makes its open-set condition redundant. The initial subgroup is
connected and nonabelian, so the resulting action has no $L_0$-fixed
point. Every nonempty compact flow has a minimal subflow; this
subflow remains metrizable and has no $L_0$-fixed point.
:::

### Separation in the final topology

The next lemma isolates the topological step. It does not require
minimality or any Lie structure on the stages.

:::{prf:lemma}
:label: lem-ind-final-open-separation

Let $G=\bigcup_{n\ge1}K_n$ be a topological group with the final
topology for an increasing sequence of compact subgroups. Suppose
$X$ is a compact metrizable $G$-space and $x\in X$ satisfies
$\operatorname{Int}(K_nx)=\varnothing$ for every $n$. Then there
exist an open identity neighbourhood $W\subseteq G$ and nonempty open
sets $A_n\subseteq X$ such that the sets $WA_n$ are pairwise disjoint.
:::

:::{prf:proof}
Fix a compatible metric on $X$. Being compact metrizable, $X$ is locally
compact, and the action is jointly continuous, so $K_nB$ is compact for
every compact $B\subseteq X$. Recursively choose nested open
neighbourhoods $V_n$ of $x$ with $\operatorname{diam}(V_n)\le2^{-n}$,
and compact sets $Q_n$ with nonempty interior, so that

$$
Q_n\subset V_n\setminus K_nx,\qquad
V_{n+1}\subset V_n\setminus K_nQ_n.
$$ (eq-ind-separation-recursion)

Indeed, $K_nx$ is closed with empty interior, so
$V_n\setminus K_nx$ contains a compact neighbourhood of some point.
Choose this as $Q_n$. Since $K_n$ is a group,
$Q_n\cap K_nx=\varnothing$ implies $x\notin K_nQ_n$; the latter
set is compact. Thus an appropriate $V_{n+1}$ exists. We obtain

$$
\sup_{z\in Q_n}d(z,x)\longrightarrow0,\qquad
K_iQ_i\cap Q_j=\varnothing\quad(i<j).
$$ (eq-ind-separation-compact-sets)

In particular, the $Q_n$ are pairwise disjoint and none contains $x$.

Define the set of forbidden group elements

$$
\begin{aligned}
E={}&\{g\in G:\text{there exist }i\ne j\text{ with }gQ_i\cap Q_j\ne\varnothing\}\\
&\quad\cup\{g\in G:\text{there exists }i\text{ with }gx\in Q_i
                    \text{ or }x\in gQ_i\}.
\end{aligned}
$$

Then $e\notin E$. We claim that $E\cap K_m$ is closed for every $m$.
For this purpose put

$$
C_i=\{x\}\cup\bigcup_{j\ne i}Q_j.
$$

Each $C_i$ is compact: any neighbourhood of $x$ contains all but
finitely many $Q_j$, and the remaining sets are compact. For compact
$B,C\subseteq X$, the set

$$
\mathcal T_m(B,C)=\{g\in K_m:gB\cap C\ne\varnothing\}
$$

is closed, as the projection of a closed subset of $K_m\times B$.
We have the finite-union identity

$$
E\cap K_m=\bigcup_{i<m}
\bigl(\mathcal T_m(Q_i,C_i)\cup\mathcal T_m(C_i,Q_i)\bigr).
$$ (eq-ind-forbidden-stage)

To check it, a transporter $gQ_i\cap Q_j\ne\varnothing$ with
$g\in K_m$ cannot have both $i,j\ge m$: use
{eq}`eq-ind-separation-compact-sets` with the smaller index, replacing
$g$ by $g^{-1}$ when necessary. Also, $gx\in Q_i$ or $x\in gQ_i$
is impossible for $i\ge m$, because $Q_i\cap K_ix=\varnothing$.
All remaining cases are exactly the terms in
{eq}`eq-ind-forbidden-stage`. Thus $E\cap K_m$ is closed.

The final topology now makes $E$ closed in $G$. Choose an open
identity neighbourhood $W$ such that $W^{-1}W\subseteq G\setminus E$,
and let $A_n=\operatorname{Int}(Q_n)$. If $w_i a_i=w_j a_j$ with
$w_i,w_j\in W$, $a_i\in A_i$, $a_j\in A_j$, and $i\ne j$, then
$w_j^{-1}w_iQ_i\cap Q_j\ne\varnothing$, contrary to the choice of
$W$. Hence the sets $WA_n$ are pairwise disjoint.
:::

:::{prf:proposition} Consequence of Basso–Zucker
:label: prop-ind-basso-zucker

Let $G$ be any topological group. Suppose some minimal $G$-flow $Y$
has nonempty open sets $A_n$ and an open identity neighbourhood $W$
such that the sets $WA_n$ are pairwise disjoint. Then $M(G)$ contains
a homeomorphic copy of $\beta\mathbb N$.
:::

:::{prf:proof}
Let $\pi:M(G)\to Y$ be an equivariant surjection. The sets
$B_n=\pi^{-1}(A_n)$ are nonempty and open, and the sets $WB_n$ are
pairwise disjoint, because $\pi(WB_n)\subseteq WA_n$.
Shrinking $W$, we may assume that it belongs to the base of symmetric
open identity neighbourhoods used in {cite}`BassoZucker2021`.
We follow the numbering of the accepted preprint
`arXiv:2008.08471v2`: Definition 5.1, Proposition 5.6 and
Corollary 5.7. Those statements give the conclusion. In their
terminology, the separated open sets imply that $G$ is not UEB, and
the corollary then embeds $\beta\mathbb N$ in $M(G)$. The statements
apply to arbitrary topological groups.
:::

:::{prf:theorem}
:label: thm-ind-classical-umf

With their standard block embeddings and final topologies, each of

$$
\operatorname{SU}(\infty),\quad\operatorname{SO}(\infty),\quad\operatorname{Sp}(\infty),\quad
\operatorname{U}(\infty),\quad\operatorname{O}(\infty)
$$

has a universal minimal flow containing a homeomorphic copy of
$\beta\mathbb N$. In particular, all five universal minimal flows are
nonmetrizable.
:::

:::{prf:proof}
Choose the compact metrizable minimal flow $Y$ from
{prf:ref}`lem-ind-semisimple-witness`. Its subgroup $G_{\mathrm{ss}}$ acts nontrivially,
since $L_0\le G_{\mathrm{ss}}$ and $Y^{L_0}=\varnothing$. Thus every finite-stage
orbit is nowhere dense by {prf:ref}`lem-ind-stage-orbits-nowhere-dense`.
Apply {prf:ref}`lem-ind-final-open-separation` at any point of $Y$, then
{prf:ref}`prop-ind-basso-zucker`. The compact space $\beta\mathbb N$ is
nonmetrizable, so no compact metrizable space can contain it.
:::

Together, {prf:ref}`prop-ind-bohr-classical` and
{prf:ref}`thm-ind-classical-umf` prove
{prf:ref}`thm-ind-dynamics-intro`. The Bohr calculation is independent
of the Oliver construction. In the unitary and orthogonal cases,
determinant actions alone would not suffice for the nonmetrizability
proof: the witnesses in {prf:ref}`lem-ind-semisimple-witness` detect
$\operatorname{SU}(2)$ and $\operatorname{SO}(3)$ inside the determinant kernels.

(sec-ind-free-locus)=
## Nonfreeness and the free locus

For a $G$-flow $Z$, write $G_z=\{g\in G:g\cdot z=z\}$ and

$$
\operatorname{Free}(Z)=\{z\in Z:G_z=\{e\}\}.
$$

We call a Borel subset of $Z$ *universally invariant-conull* if
it has measure one for every $G$-invariant Radon probability measure
on $Z$. The invariance qualification is essential: a proper subset
cannot have full measure for every Radon probability measure.

:::{prf:theorem}
:label: thm-ind-classical-free-locus

Let $G$ be any of the five classical limits in
{prf:ref}`cor-ind-classical-intro`, with its standard final topology.
Then $\operatorname{Free}(M(G))$ is a proper dense $G_\delta$ and is
universally invariant-conull. Invariant Radon probability measures
on $M(G)$ exist. The nonfree locus is an invariant dense meager
$F_\sigma$ and is null for every such measure.
:::

### An involution with fixed points in every compact flow

We first prove nonfreeness. For a nilpotent finite CW complex $P$,
write $\widehat P$ for its Sullivan profinite completion.
McGibbon's theorem states that

$$
\operatorname{Map}_*(W,\widehat P)\simeq_w *
$$ (eq-ind-mcgibbon-null)

whenever $W$ is a connected infinite loop space with torsion
fundamental group {cite}`McGibbon1996`, Theorem 3; the precise
formulation is also recorded in
{cite}`KiharaOda2012`, Example 1.6(iii), p. 68.
Here $\operatorname{Map}_*$ denotes the pointed mapping space,
and weak contractibility includes the assertion that it has only
one path component. We also use the Zabrodsky lemma in the following
form: if $F\to E\to B$ is a fibration with $B$ of connected CW
homotopy type and $\operatorname{Map}_*(F,Y)$ is weakly contractible,
then

$$
\operatorname{Map}_*(B,Y)\longrightarrow\operatorname{Map}_*(E,Y)
$$ (eq-ind-zabrodsky-mapping)

is a weak equivalence {cite}`CenceljEtAl2007`, Lemma 2.1.
This formulation requires neither $B$ nor $Y$ to be simply connected.

:::{prf:lemma}
:label: lem-ind-no-odd-stable-su

Put $a=\operatorname{diag}(-1,-1,1,\ldots)\in\operatorname{SU}(\infty)$. There is no
continuous map $f:\operatorname{SU}(\infty)\to S^d$, for any finite $d\ge0$,
such that $f(ag)=-f(g)$ for every $g\in\operatorname{SU}(\infty)$.
:::

:::{prf:proof}
Let

$$
T=\operatorname{Tel}\bigl(\operatorname{SU}(2)\hookrightarrow\operatorname{SU}(3)
\hookrightarrow\cdots\bigr)
$$

be the mapping telescope. The compatible left actions of
$C_2=\langle a\rangle$ give a free action on $T$ and a canonical
continuous equivariant map $T\to\operatorname{SU}(\infty)$. The telescope has
the usual stable special-unitary homotopy type. In particular, it
is simply connected and has the homotopy type of an infinite loop
space: the stable unitary space is an infinite loop space by Bott
periodicity, and its simply connected cover is again an infinite
loop space. The telescope allows us to work with CW homotopy types
without making any assertion about the literal quotient of the
final-topology group.

Suppose $f$ exists. Compose with the map from $T$ and an equivariant
equatorial inclusion to obtain an odd map $T\to S^m$, where
$m\ge3$ is odd. Set

$$
E=EC_2\times_{C_2}T,\qquad P=\mathbb{RP}^m.
$$

The finite CW complex $P$ is nilpotent. Its universal cover is
$S^m$, and the antipodal deck transformation has degree $+1$, hence
is homotopic to the identity. Thus $\pi_1(P)=C_2$ acts trivially
on every higher homotopy group.

Both $T$ and $BC_2=K(C_2,1)$ satisfy the hypothesis of
{eq}`eq-ind-mcgibbon-null`. Apply {eq}`eq-ind-zabrodsky-mapping` to
the Borel fibration

$$
T\longrightarrow E\longrightarrow BC_2.
$$

It follows that

$$
\operatorname{Map}_*(E,\widehat P)\simeq_w *.
$$ (eq-ind-borel-completion-null)

On the other hand, the odd map induces a map of Borel fibrations
over $BC_2$ and hence a map

$$
\bar f:E\longrightarrow EC_2\times_{C_2}S^m\simeq P.
$$

Both projections to $BC_2$ induce isomorphisms on fundamental
groups, because their fibres $T$ and $S^m$ are simply connected.
Therefore $\bar f_*$ is an isomorphism $C_2\to C_2$.

Completion preserves the finite fundamental group of the nilpotent
complex $P$. Consequently the composite $E\to P\to\widehat P$
still induces a nontrivial map on fundamental groups, contradicting
{eq}`eq-ind-borel-completion-null`. Equivalently, completion
naturality factors the covering classifier $P\to BC_2$ through
$\widehat P\to\widehat{BC_2}\simeq BC_2$; a null composite
$E\to\widehat P$ would make the projection $E\to BC_2$ null.
:::

:::{prf:remark}
:label: rem-ind-index-three

{prf:ref}`lem-ind-no-odd-stable-su` cannot be obtained from the usual
cohomological index of the involution. Let $w$ generate
$H^1(BC_2;\mathcal F_2)$ and let $i:C_2\to\operatorname{SU}(\infty)$ send the generator to
$a$. The Borel fibration $T\to E\to BC_2$ maps to the universal
fibration over $B\operatorname{SU}$ along $Bi$, and $c_2$ transgresses to the
generator $x_3$ of $H^3(T;\mathcal F_2)$ there, so the transgression of $x_3$
is $(Bi)^*c_2$ by naturality. The representation underlying $i$ is
$\sigma\oplus\sigma$, with $\sigma$ the sign character, so its total
Chern class is $(1+t)^2$ for $t=c_1(\sigma)$, giving
$(Bi)^*c_2=t^2$, whose mod $2$ reduction is $w^4$. Hence $w^4=0$ in
$H^4(E;\mathcal F_2)$, while $w^3\ne0$ because $\operatorname{SU}(2)=S^3$ sits inside
$\operatorname{SU}(\infty)$ equivariantly for the antipodal action. The largest
$k$ with $w^k\ne0$ is therefore $3$, and no argument based on the
height of $w$ can exclude an odd map to a finite-dimensional sphere.
The homotopy-theoretic input above is not a convenience.
:::

:::{prf:proposition}
:label: prop-ind-involution-fixed

Let $G$ be any of the five classical limits. Every nonempty compact
Hausdorff $G$-flow has a point fixed by a nonidentity involution. For
$\operatorname{SU}(\infty)$ one may take $a=\operatorname{diag}(-1,-1,1,\ldots)$, and for the
other groups one may take its image under the embeddings used below.
Consequently, none of the five groups admits a free compact action, and
their universal minimal actions are nonfree.
:::

:::{prf:proof}
Let $Z$ be a nonempty compact $\operatorname{SU}(\infty)$-flow and suppose $Z^a$ is
empty. Continuous real functions separate points. Compactness
therefore supplies $u_1,\ldots,u_r\in C(Z,\mathbb R)$ such that

$$
D(z)=\bigl(u_1(az)-u_1(z),\ldots,u_r(az)-u_r(z)\bigr)\ne0
\qquad(z\in Z).
$$

The map $F(z)=D(z)/\lVert D(z)\rVert$ takes values in $S^{r-1}$ and
satisfies $F(az)=-F(z)$. For any $z_0\in Z$, the continuous map
$g\mapsto F(gz_0)$ contradicts {prf:ref}`lem-ind-no-odd-stable-su`.

For the other groups, use the compatible stagewise embeddings

$$
\operatorname{SU}(n)\hookrightarrow\operatorname{U}(n),\qquad
\operatorname{SU}(n)\hookrightarrow\operatorname{Sp}(n),\qquad
\operatorname{SU}(n)\hookrightarrow\operatorname{SO}(2n)\hookrightarrow\operatorname{O}(2n).
$$

The second views complex matrices as quaternionic matrices, and
the third is realification. They induce continuous injective
homomorphisms on the final-topology unions. Restricting any compact
flow along one of these homomorphisms gives a fixed point for the
nonidentity image of $a$. In the real groups this image is
$\operatorname{diag}(-I_4,I,\ldots)$. Apply the assertion to the universal
minimal flow of each group.
:::

:::{prf:remark}
:label: rem-ind-pestov-question-four

The final-topology group $\operatorname{SU}(\infty)=\bigcup_n\operatorname{SU}(n)$ is a
$k_\omega$-space, since the stages are compact and determine its closed
sets. {prf:ref}`prop-ind-involution-fixed` therefore gives a negative
answer to Pestov's Question 4 {cite}`Pestov2007`, p. 440: this
$k_\omega$-group admits no free action on a nonempty compact Hausdorff
space. The proof gives the same conclusion for all five classical
limits. Thus the paper answers Question 4 in addition to Question 19.
:::

### Generic vectors and stage stabilisers

:::{prf:lemma}
:label: lem-ind-generic-free-vectors

Let $L\le\operatorname{U}(V)$ be a compact subgroup whose identity component is
a torus, where $V$ is a finite-dimensional complex inner-product
space. Almost every vector of $V$, and almost every vector of its
unit sphere, has trivial $L$-stabiliser. If $L\le\operatorname{O}(W)$ has the
same property and $\dim_{\mathbb R}W\ge2$, then almost every ordered
orthonormal two-frame in $W$ has trivial pointwise $L$-stabiliser.
The measures on spheres and frame spaces are the invariant
probability measures.
:::

:::{prf:proof}
Put $T=L^0$ and decompose $V$ into its $T$-weight spaces,
$V=\bigoplus_\chi V_\chi$. Choose representatives $b$ of the
finite quotient $L/T$. Outside a set of Lebesgue measure zero,
the components $v_\chi$ of a vector $v$ are all nonzero and have
pairwise distinct norms. If $b$ permutes the weight spaces
nontrivially, these norm conditions prevent $btv=v$ for every
$t\in T$. If $b$ preserves every weight space but is nonscalar
on some $V_\chi$, the equation $btv=v$ forces $v_\chi$ into an
eigenspace of $b|_{V_\chi}$. Exclude these finitely many proper
eigenspaces for each such representative. Finally, if $b$ acts
scalarly on every weight space, $btv=v$ forces $bt$ to act as the
identity on all of $V$, so $bt=e$. The same argument covers the
identity coset. All excluded sets are cones of measure zero, so
their intersections with the unit sphere also have measure zero.

For the real assertion, apply the complex assertion to the faithful
complexification of the representation on $W$. If $u,v$ are
independent standard real Gaussian vectors, then $u+iv$ has trivial
stabiliser almost surely. Its stabiliser is precisely the common
stabiliser of $u$ and $v$. The pair is linearly independent almost
surely, and Gram–Schmidt preserves this common stabiliser while
giving the invariant distribution on ordered orthonormal
two-frames.
:::

:::{prf:lemma}
:label: lem-ind-compact-free-open

For a continuous action of a compact Lie group $K$ on a compact
Hausdorff space $Z$, the $K$-free locus is open.
:::

:::{prf:proof}
Let $z$ be $K$-free and choose a faithful unitary representation
$\rho:K\to\operatorname{U}(d)$. The matrix function $kz\mapsto\rho(k)$ is
continuous on the closed orbit $Kz$. Extend its real and imaginary
entries by the Tietze extension theorem to a continuous
$A:Z\to M_d(\mathbb C)$, and put

$$
B(y)=\int_K\rho(k)^{-1}A(ky)\,\mathrm d k.
$$

Then $B$ is continuous, $B(z)=I$, and
$B(hy)=\rho(h)B(y)$. If $B(y)$ is invertible and $hy=y$, this
identity implies $\rho(h)=I$, hence $h=e$. Invertibility therefore
provides the required open neighbourhood of $z$.
:::

:::{prf:proposition}
:label: prop-ind-generic-free-locus

Let $G$ be one of the five classical final-topology unions, with
standard stages $K_n$. Suppose that a nonempty compact Hausdorff
$G$-flow $Z$ satisfies

$$
(G_z\cap K_m)^0\text{ is a torus}\qquad(z\in Z,\ m\in\mathbb N).
$$

Then $\operatorname{Free}(Z)$ is a dense $G_\delta$ and is
universally invariant-conull.
:::

:::{prf:proof}
Put $F_n=\{z\in Z:G_z\cap K_n=\{e\}\}$. These sets are open
by {prf:ref}`lem-ind-compact-free-open`. Fix $z\in Z$ and $n$.
For the unitary and symplectic chains take $m=n+1$ and let $b=e_m$
be the last coordinate vector. For the orthogonal chains take
$m=n+2$ and let $b=(e_{m-1},e_m)$ be the last ordered two-frame.
In each case $K_n$ fixes $b$ pointwise and $K_m$ is transitive on
the relevant sphere or frame space. Haar probability under
$k\mapsto k^{-1}b$ is its invariant probability measure.

Apply {prf:ref}`lem-ind-generic-free-vectors` to $L=G_z\cap K_m$.
For the symplectic chain use its standard complex unitary
representation on $\mathbb C^{2m}$, whose unit sphere is the unit sphere
of $\mathbb H^m$. For Haar-almost every $k\in K_m$, the vector
or frame $k^{-1}b$ has trivial $L$-stabiliser. If
$h\in G_{kz}\cap K_n$, then $k^{-1}hk\in L$ fixes $k^{-1}b$,
so $h=e$. We have proved

$$
\int_{K_m}\mathbf1_{F_n}(kz)\,\mathrm d k=1\qquad(z\in Z).
$$ (eq-ind-haar-stage-free)

Every identity neighbourhood in $K_m$ has positive Haar measure.
Thus, by continuity of the orbit map at the identity, every
neighbourhood of $z$ meets $F_n$. Hence $F_n$ is dense. Since $Z$
is compact Hausdorff, it is Baire, and

$$
\operatorname{Free}(Z)=\bigcap_n F_n
$$

is a dense $G_\delta$.

If $\mu$ is any $G$-invariant Radon probability measure, Fubini and
{eq}`eq-ind-haar-stage-free` give

$$
1=\int_Z\int_{K_m}\mathbf1_{F_n}(kz)\,\mathrm d k\,\mathrm d\mu(z)
=\int_{K_m}\mu(k^{-1}F_n)\,\mathrm d k=\mu(F_n).
$$

The integrand is product measurable even if $Z$ is nonmetrizable:
the inverse image of $F_n$ under the action map is open in
$K_m\times Z$, and every such open set is a countable union of
open rectangles because $K_m$ has a countable base. Taking the
countable intersection gives $\mu(\operatorname{Free}(Z))=1$.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-ind-classical-free-locus`.* Let $X=\varprojlim D_m$ be the Oliver flow constructed in the proof
of {prf:ref}`thm-ind-main`. A minimal subflow of $X$ is a factor of
$M(G)$, so there is a $G$-map $q:M(G)\to X$. For $z\in M(G)$,
the compact subgroup $L=G_z\cap K_m$ fixes $\pi_m(q(z))$.
The fixed-set prescription {eq}`eq-ind-fixed-sets` implies that
$L$ is solvable, and hence $L^0$ is a torus. If the construction
discarded some initial stages, handle them inside a later stage.
{prf:ref}`prop-ind-generic-free-locus` gives density, the
$G_\delta$ property, and universal invariant-conullness.

For completeness, invariant Radon probability measures exist on
every nonempty compact $G$-flow. For each $n$, Haar averaging gives
a $K_n$-invariant probability measure. The sets of such measures
are nonempty weak-* compact subsets of the space of Radon
probabilities, and are nested as $n$ increases. Their intersection
is nonempty and consists of $G$-invariant measures. On $M(G)$ every
such measure has full support by minimality.

{prf:ref}`prop-ind-involution-fixed` shows that the free locus
is proper. Its complement is invariant, meager, $F_\sigma$, and
null for every invariant Radon probability. It is dense as well:
the orbit of a nonfree point consists of nonfree points and is
dense by minimality.
:::

Together, {prf:ref}`prop-ind-involution-fixed` and
{prf:ref}`thm-ind-classical-free-locus` prove
{prf:ref}`thm-ind-free-intro`.

:::{prf:remark}
:label: rem-ind-remark-3

{prf:ref}`thm-ind-classical-free-locus` concerns the five classical
chains and their specified topologies. It does not hold for every
chain covered by {prf:ref}`thm-ind-main`: for a constant chain at
a compact Lie group $K$, the universal minimal flow is $K$ with
its free translation action. Also, the existence of a fixed point
for each individual involution does not give a common fixed point
for different involutions.
:::

(sec-ind-observables)=
## A finite family of obstructing observables

We use the convention

$$
f\in\operatorname{RUCB}(G)
\quad\Longleftrightarrow\quad
f\text{ is bounded and }
\sup_{h\in G}\lvert f(uh)-f(h)\rvert\longrightarrow0\quad(u\to e).
$$ (eq-ind-ruc-convention)

All functions in this section are real-valued.

:::{prf:proposition}
:label: prop-ind-obstructing-observables

Under the hypotheses of {prf:ref}`thm-ind-main`, there are finitely
many $f_1,\ldots,f_d\in\operatorname{RUCB}(G)$ and a constant $\delta>0$ such that

$$
\sum_{i=1}^d\operatorname{Var}_{k\in K_j}f_i(kh)\ge\delta
\qquad(h\in G).
$$ (eq-ind-variance-obstruction)
:::

:::{prf:proof}
Identify the ordinary compact disk $D_j$ with a closed ball in
$\mathbb R^d$, and let $a_1,\ldots,a_d$ be its coordinate functions. Define

$$
v(y)=\sum_{i=1}^d\operatorname{Var}_{k\in K_j}a_i(k\cdot y),\qquad y\in D_j.
$$

This is a continuous nonnegative function. If $v(y)=0$, each
continuous orbit function $k\mapsto a_i(k\cdot y)$ is constant,
because Haar measure has full support. The coordinates separate
points, so the orbit of $y$ is a singleton. This contradicts
$D_j^{K_j}=\varnothing$. Thus compactness gives
$\delta=\min_{D_j}v>0$.

For the inverse-limit action constructed above, fix $x_*\in X$, put
$A_i=a_i\circ\pi_j\in C(X)$, and define $f_i(g)=A_i(g\cdot x_*)$.
Joint continuity and compactness of $X$ imply

$$
\sup_{h\in G}\lvert f_i(uh)-f_i(h)\rvert
\le\sup_{x\in X}\lvert A_i(u\cdot x)-A_i(x)\rvert\longrightarrow0.
$$

Hence $f_i\in\operatorname{RUCB}(G)$. Equivariance of $\pi_j$ gives

$$
\sum_i\operatorname{Var}_{k\in K_j}f_i(kh)
=v\bigl(\pi_j(h\cdot x_*)\bigr)\ge\delta.
$$
:::

The obstruction is uniform over every translate $K_jh$. In particular,
failure of extreme amenability is witnessed by a fixed finite family
of observables, rather than by a family whose size grows with the
ambient stage.

(sec-ind-relative)=
## A relative variance estimate in trace norm

We now work in the compact group $\operatorname{SU}(N)$ with
$d_1(g,h)=\operatorname{Tr}\lvert g-h\rvert$, without normalising by $N$. Fix $N>m\ge2$
and write $K=\operatorname{SU}(m)$ for the upper-left block subgroup.

### A representation inequality

Let $e_{ij}$ be matrix units. In a finite-dimensional unitary
representation $\pi$ of $\operatorname{SU}(N)$, extend the differential complex
linearly to $\mathfrak{sl}_N(\mathbb C)$ and write
$E_{ij}=d\pi(e_{ij})$ for $i\ne j$. Then
$E_{ij}^*=E_{ji}$. Define

$$
Q=\sum_{i=1}^m\sum_{a=m+1}^N
\bigl(E_{ia}E_{ai}+E_{ai}E_{ia}\bigr).
$$ (eq-ind-cross-casimir)

The operator is positive and commutes with $K$: its summands form the
sum of squares over an orthonormal basis of the cross-block subspace,
which is invariant under conjugation by $K$.

:::{prf:lemma}
:label: lem-ind-relative-gap

Let $\operatorname{P}^{\mathrm{fix}}_K$ be the orthogonal projection onto the $K$-fixed vectors.
Then

$$
Q\ge(N-m)(I-\operatorname{P}^{\mathrm{fix}}_K).
$$ (eq-ind-relative-gap)

More precisely, on a $K$-isotypic component of highest weight
$\lambda$, $Q\ge(N-m)R$, where
$R=\lambda_1-\lambda_m$ is the highest-weight spread.
:::

:::{prf:proof}
Set $Z=d\pi(e_{11}-e_{mm})$. Matrix-unit commutators give the
following identity of self-adjoint operators:

$$
\begin{aligned}
Q-(N-m)Z
={}&2\sum_{a>m}\bigl(E_{a1}E_{1a}+E_{ma}E_{am}\bigr)\\
&+\sum_{i=2}^{m-1}\sum_{a>m}
\bigl(E_{ia}E_{ai}+E_{ai}E_{ia}\bigr)\ge0.
\end{aligned}
$$ (eq-ind-positive-identity)

The second sum is empty if $m=2$. Each term on the right is of the
form $T^*T$ or $TT^*$. For example, the identity follows by subtracting

$$
\sum_{a>m}\bigl([E_{1a},E_{a1}]-[E_{ma},E_{am}]\bigr)=(N-m)Z
$$

from {eq}`eq-ind-cross-casimir`.

On a highest-weight vector of an irreducible $K$-type, $Z$ acts by
$R=\lambda_1-\lambda_m$. For a nontrivial type, $R$ is a positive
integer. Since $Q$ is self-adjoint and commutes with $K$, each
eigenspace of $Q$ is $K$-invariant. Apply
{eq}`eq-ind-positive-identity` to a highest-weight vector in each
irreducible summand of each eigenspace. It follows that the
corresponding eigenvalue of $Q$ is at least $(N-m)R$. This also
handles multiplicities. Positivity on the trivial type completes
{eq}`eq-ind-relative-gap`.
:::

### Cross-block energy

For $i\le m<a$, put

$$
X_{ia}=\frac{e_{ia}-e_{ai}}{\sqrt2},\qquad
Y_{ia}=\frac{\mathrm i(e_{ia}+e_{ai})}{\sqrt2}.
$$

These are Hilbert–Schmidt orthonormal in $\mathfrak{su}(N)$ for
$\langle X,Y\rangle=-\operatorname{Tr}(XY)$. Write
$D_Xf(g)=\left.\frac{\mathrm d}{\mathrm dt}\right|_{t=0}f(e^{tX}g)$.

:::{prf:lemma}
:label: lem-ind-energy

If $f$ is smooth, real, and $L$-Lipschitz for $d_1$, then at every
$g\in\operatorname{SU}(N)$,

$$
\sum_{i\le m<a}\bigl(\lvert D_{X_{ia}}f(g)\rvert^2+
\lvert D_{Y_{ia}}f(g)\rvert^2\bigr)\le2mL^2.
$$ (eq-ind-energy-bound)
:::

:::{prf:proof}
For traceless Hermitian $A$,
$\lvert df_g(\mathrm iAg)\rvert\le L\lVert A\rVert_1$.
Extend this real linear functional from the traceless Hermitian
subspace by Hahn–Banach. Trace-norm duality gives a Hermitian
matrix $B$ with

$$
df_g(\mathrm iAg)=\operatorname{Tr}(BA),\qquad \lVert B\rVert_{\mathrm{op}}\le L.
$$

The extension is determined only up to adding a real multiple of the
identity, since the trace annihilates the traceless Hermitian subspace;
the entries $B_{ia}$ with $i\le m<a$, which are the only ones used
below, are the same for every admissible extension. The choice of $B$ is
pointwise; no measurable choice is required.
Let $P_m$ be projection onto the first $m$ coordinates. Direct
calculation gives

$$
\begin{aligned}
\sum_{i\le m<a}\bigl(\lvert D_{X_{ia}}f(g)\rvert^2+
\lvert D_{Y_{ia}}f(g)\rvert^2\bigr)
&=2\sum_{i\le m<a}\lvert B_{ia}\rvert^2\\
&=2\lVert P_mB(I-P_m)\rVert_{\mathrm{HS}}^2\le2mL^2.
\end{aligned}
$$
:::

:::{prf:theorem}
:label: thm-ind-variance

Every real $L$-Lipschitz $f$ on $(\operatorname{SU}(N),d_1)$ satisfies

$$
\int_{\operatorname{SU}(N)}\operatorname{Var}_{k\in K}f(kh)\,\mathrm d h\le\frac{2mL^2}{N-m}.
$$ (eq-ind-variance)

For a finite collection $f_1,\ldots,f_r$ with respective Lipschitz
constants $L_1,\ldots,L_r$, some $h\in\operatorname{SU}(N)$ satisfies

$$
\sum_{i=1}^r\operatorname{Var}_{k\in K}f_i(kh)
\le\frac{2m}{N-m}\sum_{i=1}^rL_i^2.
$$ (eq-ind-finite-variance)
:::

:::{prf:proof}
Use the left regular representation $U(k)f(g)=f(k^{-1}g)$.
Its differential is $-D_X$, so the operator in
{eq}`eq-ind-cross-casimir` is

$$
Q=-\sum_{i\le m<a}(D_{X_{ia}}^2+D_{Y_{ia}}^2).
$$

Peter–Weyl decomposition applies {prf:ref}`lem-ind-relative-gap` to
each finite-dimensional summand. Summing the resulting quadratic-form
inequality and integrating by parts gives, for smooth $f$,

$$
\lVert f-\operatorname{Avg}_Kf\rVert_2^2\le\frac{1}{N-m}
\int_{\operatorname{SU}(N)}\sum_{i\le m<a}
\bigl(\lvert D_{X_{ia}}f\rvert^2+\lvert D_{Y_{ia}}f\rvert^2\bigr)\,\mathrm d g.
$$ (eq-ind-form-bound)

Here $(\operatorname{Avg}_Kf)(g)=\int_Kf(kg)\,\mathrm d k$, which is the projection
$\operatorname{P}^{\mathrm{fix}}_K$ of {prf:ref}`lem-ind-relative-gap` for the left regular
representation. Haar invariance shows that

$$
\lVert f-\operatorname{Avg}_Kf\rVert_2^2=\int_{\operatorname{SU}(N)}\operatorname{Var}_{k\in K}f(kg)\,\mathrm d g.
$$

{prf:ref}`lem-ind-energy` proves {eq}`eq-ind-variance` for smooth functions.
The quadratic-form passage can equivalently be obtained first for
finite Peter–Weyl sums and then by their convergence in the relevant
first-order Sobolev norm.

For general Lipschitz $f$, pass to the right convolutions
$f_\varepsilon(g)=\int_{\operatorname{SU}(N)}f(gu)\varphi_\varepsilon(u)\,\mathrm d u$ with a
smooth nonnegative Haar approximate identity $\varphi_\varepsilon$.
Right convolution is smooth in the left translation directions
differentiated above. Right invariance of $d_1$ preserves the Lipschitz
constant, and the convolutions converge uniformly. Their variances
therefore converge uniformly, proving {eq}`eq-ind-variance`. Sum the
inequality over $i$ and choose a point where the sum is no greater
than its average to obtain {eq}`eq-ind-finite-variance`.
:::

In particular, if

$$
\Delta_{m,r}(N)=
\sup_{\substack{f_i:\operatorname{SU}(N)\to[0,1]\\\operatorname{Lip}_{d_1}(f_i)\le1}}
\min_{h\in\operatorname{SU}(N)}\sum_{i=1}^r\operatorname{Var}_{k\in\operatorname{SU}(m)}f_i(kh),
$$

then $\Delta_{m,r}(N)\le2mr/(N-m)$. The functions in the supremum
may depend on $N$.

(sec-ind-trace-ea)=
## Extreme amenability in trace norm

The following elementary dynamical lemma makes the passage from
finite observables to fixed points explicit.

:::{prf:lemma}
:label: lem-ind-variance-to-fixed

Let a metrizable topological group $\Gamma$ have a compatible right-invariant
metric and contain an increasing sequence of compact subgroups $K_m$
with dense union. Suppose that for each $m$ and every finite family
of bounded real Lipschitz functions $b_1,\ldots,b_r$ on $\Gamma$,

$$
\inf_{h\in\Gamma}\sum_i\operatorname{Var}_{k\in K_m}b_i(kh)=0.
$$ (eq-ind-flatness-hyp)

Then $\Gamma$ is extremely amenable.
:::

:::{prf:proof}
Consider a continuous action of $\Gamma$ on a nonempty compact Hausdorff
space $Z$, and fix $z_*\in Z$. If $A\in C(Z,\mathbb R)$, the orbit
function $a(g)=A(gz_*)$ is bounded and right-uniformly continuous,
since

$$
\sup_g\lvert a(ug)-a(g)\rvert\le
\sup_{z\in Z}\lvert A(uz)-A(z)\rvert\longrightarrow0.
$$

For a compatible right-invariant metric this is ordinary uniform
continuity, since $d(ug,g)=d(u,e)$ for all $g$. Every bounded uniformly continuous real function on a
metric space is uniformly approximable by bounded Lipschitz
functions. For example, the functions
$a_L(x)=\inf_y\{a(y)+L d(x,y)\}$ are bounded and $L$-Lipschitz
and converge uniformly to $a$ as $L\to\infty$. Uniform continuity
controls points with $d(x,y)$ small, and boundedness excludes all
other points once $L$ is large.

Fix a finite subset $S\subseteq K_m$, finitely many
$A_1,\ldots,A_r\in C(Z,\mathbb R)$, and $\varepsilon>0$. Approximate the
associated orbit functions $a_i$ uniformly by bounded Lipschitz
functions $b_i$. Given $h$, let $c_i=\int_{K_m}b_i(kh)\,\mathrm d k$.
For $s\in S$, Haar invariance and $\lvert v-w\rvert^2\le
2\lvert v-c_i\rvert^2+2\lvert w-c_i\rvert^2$ give

$$
\int_{K_m}\sum_{s\in S}\sum_i
\lvert b_i(skh)-b_i(kh)\rvert^2\,\mathrm d k
\le4\lvert S\rvert\sum_i\operatorname{Var}_{k\in K_m}b_i(kh).
$$

By {eq}`eq-ind-flatness-hyp`, choose $h$ making the right side
arbitrarily small and then a $k$ where the integrand is small.
Choosing the uniform approximations sufficiently accurate produces
$z=khz_*$ such that

$$
\lvert A_i(sz)-A_i(z)\rvert<\varepsilon\qquad(s\in S,\ 1\le i\le r).
$$

Every finite subset of $\bigcup_mK_m$ lies in a common stage.
Compactness of $Z$, applied to the closed finite sets of approximate
fixed-point conditions, now gives a point at which
$A(sz)=A(z)$ for every $A\in C(Z,\mathbb R)$ and every
$s\in\bigcup_mK_m$. Continuous real functions separate points of
$Z$, so this point is fixed by the dense union. Continuity makes it
fixed by all of $\Gamma$.
:::

:::{prf:lemma}
:label: lem-ind-density

The trace-norm completion of $G_{\mathrm{tr}}$ is $\operatorname{SU}_1$.
:::

:::{prf:proof}
The set $\operatorname{SU}_1$ is closed in $I+\mathcal S_1$ for the trace norm:
unitarity is closed under operator-norm convergence, and the
Fredholm determinant is trace-norm continuous. Thus it is complete.

Let $u\in\operatorname{SU}_1$. Functional calculus gives $u=e^{\mathrm iA}$
with $A=A^*\in\mathcal S_1$: choose principal arguments for the eigenvalues
of $u$, which accumulate only at $1$ because $u-I$ is compact
(so only finitely many eigenvalues can lie near $-1$), using
$\lvert t\rvert\le(\pi/2)\lvert e^{\mathrm it}-1\rvert$ for $\lvert t\rvert\le\pi$.
The identity $\det_F(e^{\mathrm iA})=e^{\mathrm i\operatorname{Tr} A}$ gives
$\operatorname{Tr} A\in2\pi\mathbb Z$.

Let $P_n$ be the standard coordinate projection and put
$A_n=P_nAP_n$. Define $h_n$ on the first $n+1$ coordinates by

$$
h_n=e^{\mathrm iA_n|_{P_n\ell^2}}
\oplus e^{-\mathrm i\operatorname{Tr} A_n},
$$

and extend it by the identity. Then $h_n\in\operatorname{SU}(n+1)$.
Since $A_n\to A$ in trace norm, the integral formula for the
difference of two exponentials gives
$\lVert e^{\mathrm iA_n}-e^{\mathrm iA}\rVert_1\le\lVert A_n-A\rVert_1$.
Also $e^{-\mathrm i\operatorname{Tr} A_n}\to1$. The triangle inequality therefore
gives $h_n\to u$ in trace norm.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-ind-trace-intro`.* The estimate is {prf:ref}`thm-ind-variance`. For either
$\Gamma=G_{\mathrm{tr}}$ or $\Gamma=\operatorname{SU}_1$, restrict any finite
family of bounded Lipschitz functions on $\Gamma$ to $\operatorname{SU}(N)$.
For each fixed $m$, inequality {eq}`eq-ind-finite-variance` tends to
zero as $N\to\infty$. Thus {eq}`eq-ind-flatness-hyp` holds.
The trace-norm metric is bi-invariant, in particular right-invariant,
and the compact subgroups
$\operatorname{SU}(m)$ have dense union in $\Gamma$, by {prf:ref}`lem-ind-density` in
the second case. {prf:ref}`lem-ind-variance-to-fixed` proves extreme
amenability.
:::

(sec-ind-separation)=
## An explicit separation of the right uniformities

The difference between the final and trace-norm topologies on $G_{\mathrm{alg}}$
can be seen directly at
the level of bounded right-uniformly continuous functions. On

$$
E=\left\{x:\sum_{j\ge1}2^{-j}\lvert x_j\rvert^2<\infty\right\},
$$

let $T_g$ be the finitary matrix action of $g\in G_{\mathrm{alg}}$.
Each $T_g$ is a bounded invertible operator on $E$. On every finite
stage, $g\mapsto T_g$ is continuous in operator norm, so it is
continuous for the final topology. Put

$$
\ell(g)=\log\max\{\lVert T_g\rVert_{\mathrm{op}},\lVert T_g^{-1}\rVert_{\mathrm{op}}\},
\qquad f(g)=\min\{1,\ell(g)\}.
$$

The function $\ell$ is nonnegative, symmetric, continuous, and
subadditive. Hence
$\lvert f(ug)-f(g)\rvert\le\ell(u)$ uniformly in $g$, and
$f\in\operatorname{RUCB}(G_{\mathrm{fin}})$.

For $n\ge2$, let $u_n$ be a real determinant-one rotation on the
plane of coordinates $1,n$, through the angle
$\theta_n=4\,2^{-(n-1)/2}$, and the identity elsewhere. Then

$$
\lVert u_n-I\rVert_1=4\sin(\theta_n/2)\longrightarrow0.
$$

In an orthonormal basis of this plane for the weighted norm of $E$,
one off-diagonal entry of $T_{u_n}$ has absolute value

$$
2^{(n-1)/2}\sin\theta_n\longrightarrow4.
$$

Thus $\ell(u_n)>1$ eventually, and $f(u_n)=1$ while $f(e)=0$.
The function $f$ is not trace-norm continuous. In particular, the final
topology is strictly finer than the trace-norm topology, and final-RUC
functions need not be uniformly approximable by trace-Lipschitz
functions.

This example separates uniformities; the actual fixed-point
obstruction is {prf:ref}`prop-ind-obstructing-observables`.

(sec-ind-encyclopaedia-proofs)=
## Proofs of the statements in [](#sec-inductive-limits)

:::{prf:proof}
*Proof of {prf:ref}`cor-ind-classical-intro`.* {prf:ref}`cor-ind-semisimple-classical` covers $\varinjlim\operatorname{SU}(n)$,
$\varinjlim\operatorname{SO}(n)$ and $\varinjlim\operatorname{Sp}(n)$, and
{prf:ref}`prop-ind-determinants` covers $\varinjlim\operatorname{U}(n)$ and
$\varinjlim\operatorname{O}(n)$.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-ind-dynamics-intro`.* Together, {prf:ref}`prop-ind-bohr-classical` and
{prf:ref}`thm-ind-classical-umf` prove the theorem.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-ind-free-intro`.* Together, {prf:ref}`prop-ind-involution-fixed` and
{prf:ref}`thm-ind-classical-free-locus` prove the theorem.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-lupini-inductive`.* This is {prf:ref}`thm-ind-main`. The two forms of the hypothesis agree: as
noted after {eq}`eq-ind-family`, a compact Lie group $H$ is solvable if and
only if $H^0$ is a torus and $H/H^0$ is solvable, and a compact connected Lie
group is abelian exactly when it is a torus.
:::

:::{prf:proof}
*Proof of {prf:ref}`cor-lupini-inductive`.* This is {prf:ref}`cor-ind-classical-intro`, with
$\operatorname{SU}(\infty)=\varinjlim\operatorname{SU}(n)$ and so on, as in
[](#sec-ind-main-results).
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-lupini-inductive-umf`.* This is {prf:ref}`thm-ind-dynamics-intro`.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-lupini-inductive-free`.* By {prf:ref}`prop-ind-involution-fixed`, every action of $G$ on a nonempty
compact Hausdorff space has a point fixed by an element of order two; so no
such action is free, and in particular the action on $M(G)$ is not free. The
assertions about the points with trivial stabiliser, and the existence of
invariant Radon probability measures on $M(G)$, are
{prf:ref}`thm-ind-classical-free-locus`.
:::

:::{prf:proof}
*Proof of {prf:ref}`thm-lupini-trace-class`.* This is the first assertion of {prf:ref}`thm-ind-trace-intro`: the group
$G_{\mathrm{tr}}$ is $\bigcup_n\operatorname{SU}(n)$ with the trace-norm metric,
and $\operatorname{SU}_1$ is its completion {eq}`eq-ind-suone`.
:::
