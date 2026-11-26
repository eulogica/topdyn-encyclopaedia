(sec-operator-algebras)=
# Automorphism groups of C*-algebras

Automorphism groups of separable C*-algebras, with the point-norm topology
($\alpha_i\to\alpha$ if and only if $\alpha_i(a)\to\alpha(a)$ in norm for
every $a$), are Polish groups. For Kirchberg algebras and AF algebras their
universal minimal flows reduce to classification invariants, because a large
normal subgroup of approximately inner automorphisms is extremely amenable
and can be divided out ({prf:ref}`prop-ea-normal`). A *Kirchberg
algebra* is a separable, simple, nuclear, purely infinite C*-algebra. The
results in this section are taken from preprints of the editor posted on
Zenodo {cite}`LupiniCuntz2026,LupiniStable2026,LupiniUnital2026`; they have
not been refereed.

:::{prf:theorem} {cite:t}`LupiniCuntz2026`
:label: thm-lupini-cuntz

Let $\mathcal{O}_2$ be the Cuntz algebra, $\mathcal{K}$ the algebra of
compact operators and $D=\mathcal{O}_2\otimes\mathcal{K}$, with minimal
unitisation $D^+$.

1. The group $U_1(D)=\{u\in U(D^+) : u-1\in D\}$, with the norm topology,
   is extremely amenable.
2. For every pure state $\varphi$ of $\mathcal{O}_2$, the stabiliser
   $\{\alpha\in\mathrm{Aut}(\mathcal{O}_2) : \varphi\circ\alpha=\varphi\}$, with
   the point-norm topology, is extremely amenable.
3. With the point-norm topology, $M(\mathrm{Aut}(\mathcal{O}_2))$ is the
   state space $S(\mathcal{O}_2)$, with the weak* topology and the action
   $\alpha\cdot\rho=\rho\circ\alpha^{-1}$.
4. With the norm topology, $M(U(D^+))$ is the circle $\mathbb{T}$, on which
   $U(D^+)$ acts through the scalar character of $D^+$.

:::

:::{prf:remark}
:label: rem-lupini-cuntz

Since $\mathcal{O}_2$ is strongly self-absorbing and its state space is not a
point, part (3) answers negatively a question of Eagle, Farah, Hart, Kadets,
Kalashnyk and Lupini, whether the automorphism group of every strongly
self-absorbing C*-algebra is extremely amenable. Parts (1) and (4) settle, for
$n=2$, in the affirmative, the case of a conjecture of Alekseev, Schmidt and
Thom asking whether $U((\mathcal{O}_n\otimes\mathcal{K})^+)$ is amenable in
the norm topology {cite}`LupiniCuntz2026`. Part (3) is obtained from part (2) as in
{prf:ref}`prop-coprecompact-ea`: the stabiliser of a pure state is a
co-precompact subgroup whose completion is the whole state space.
:::

:::{prf:theorem} {cite:t}`LupiniStable2026`
:label: thm-lupini-stable

Let $A$ be a stable Kirchberg algebra, and let $N_A$ be the closure in
$\mathrm{Aut}(A)$ of the automorphisms $\mathrm{Ad}(u)$, for $u$ a unitary of
the multiplier algebra of $A$.

1. The group $N_A$ is extremely amenable, and the map
   $\mathrm{Aut}(A)\to KL(A,A)^\times$ to the group of invertible elements of
   $KL(A,A)$ is continuous, open and surjective, with kernel $N_A$. Hence
   $M(\mathrm{Aut}(A))$ is $M(KL(A,A)^\times)$ with $\mathrm{Aut}(A)$ acting
   through this map. No UCT assumption is needed.
2. If $A$ satisfies the UCT, the same holds with $KL(A,A)^\times$ replaced
   by the automorphism group of total K-theory $\underline{K}(A)$ with its
   coefficient operations, with the topology of pointwise convergence.
3. If $A$ satisfies the UCT and $G_i=K_i(A)$ are finite, then
   $M(\mathrm{Aut}(A))$ is the translation flow of a finite group of order
   $|\mathrm{Aut}(G_0)|\,|\mathrm{Aut}(G_1)|\,|\mathrm{Ext}(G_0,G_1)|\,|\mathrm{Ext}(G_1,G_0)|$.
   If the $G_i$ are finitely generated, then $M(\mathrm{Aut}(A))$ is metrizable
   if and only if $\mathrm{Aut}(A)$ is amenable, if and only if the free ranks
   of $G_0$ and $G_1$ are at most one.

:::

:::{prf:example}
:label: ex-lupini-stable-cuntz

For $n\geq1$, the stabilised Cuntz algebra $\mathcal{O}_{n+1}\otimes\mathcal{K}$
satisfies the UCT, with $K_0=\mathbb{Z}/n$ and $K_1=0$. When $K_1(A)=0$ the
total K-theory quotient reduces to $\mathrm{Aut}(K_0(A))$
{cite}`LupiniStable2026`, so $M(\mathrm{Aut}(\mathcal{O}_{n+1}\otimes\mathcal{K}))$
is the translation flow of the group of units of $\mathbb{Z}/n$. In
particular, the automorphism groups of $\mathcal{O}_2\otimes\mathcal{K}$ and
$\mathcal{O}_3\otimes\mathcal{K}$ are extremely amenable.
:::

:::{prf:theorem} {cite:t}`LupiniStable2026`
:label: thm-lupini-stable-geometric

Let $B$ be a stable Kirchberg algebra whose automorphism group is extremely
amenable, such as $\mathcal{O}_2\otimes\mathcal{K}$. For a nonempty finite set
$I$ and for the Cantor set $X$,

$$
\begin{gathered}
M(\mathrm{Aut}(c_0(I,B)))\cong\mathrm{Sym}(I),\qquad
M(\mathrm{Aut}(c_0(\mathbb{N},B)))\cong\mathrm{LO}(\mathbb{N}),\\
M(\mathrm{Aut}(C(X)\otimes B))\cong\Phi(X),
\end{gathered}
$$

with the actions induced by permutations of the summands and by
homeomorphisms of $X$.
:::

:::{prf:theorem} {cite:t}`LupiniUnital2026`
:label: thm-lupini-unital

Let $A$ be a unital Kirchberg algebra, let $N^0_A$ be the closure of the
group of automorphisms $\mathrm{Ad}(u)$ with $u$ in the identity component
of the unitary group of $A$, and let $q\colon\mathrm{Aut}(A)\to
Q^0_A=\mathrm{Aut}(A)/N^0_A$ be the quotient map. Then

$$
M(\mathrm{Aut}(A))\cong S(A)\times M(Q^0_A),
\qquad \alpha\cdot(\rho,x)=(\rho\circ\alpha^{-1},q(\alpha)x),
$$

and $M(N^0_A)=S(A)$. No UCT assumption is needed. If $A$ satisfies the UCT
and $K_1(A)=0$, then $Q^0_A$ is the group of automorphisms of $K_0(A)$
fixing the class of the unit, with the topology of pointwise convergence.
:::

:::{prf:theorem} {cite:t}`LupiniUnital2026`
:label: thm-lupini-af

Let $A$ be a separable unital AF algebra with no nonzero finite-dimensional
representations, and let $\Gamma_A$ be the group of automorphisms of the
scaled dimension group $(K_0(A),K_0(A)^+,[1_A])$, with the topology of
pointwise convergence. Then the group of inner automorphisms of $A$ is
extremely amenable, and $M(\mathrm{Aut}(A))$ is $M(\Gamma_A)$ with
$\mathrm{Aut}(A)$ acting through $\alpha\mapsto K_0(\alpha)$. This applies to
every infinite-dimensional simple separable unital AF algebra. The hypothesis
on representations cannot be dropped: for the matrix algebra $M_d(\mathbb{C})$
with $d\geq2$ the group $\Gamma_A$ is trivial, while $\mathrm{Aut}(A)$ is the
nontrivial compact group $PU(d)$.
:::

:::{prf:remark}
:label: rem-lupini-unital

For $A=\mathcal{O}_2$ the group $Q^0_A$ is trivial, and
{prf:ref}`thm-lupini-unital` recovers part (3) of
{prf:ref}`thm-lupini-cuntz`. The proofs give more
{cite}`LupiniUnital2026`. In the AF case the unitary group, in the norm
topology, and the inner automorphism group are *whirly amenable*, a
property stronger than extreme amenability. In the Kirchberg case $N^0_A$ is
not amenable; the whirly amenable kernel is the stabiliser in $N^0_A$ of a
pure state, and the state space, the universal minimal flow of $N^0_A$,
accounts for the rest.
:::
