(sec-inductive-limits)=
# Inductive limits of compact Lie groups

Increasing unions of compact Lie groups, such as the infinite unitary group,
can carry several natural group topologies, and extreme amenability depends on
the choice. Concentration of measure gives extreme amenability for the
coarser operator topologies ([](#sec-gromov-milman)); for the finest
topology the answer is negative. The results in this section are taken from
a preprint of Codenotti and the editor posted on Zenodo
{cite}`LupiniInductive2026`; it has not been refereed.

:::{prf:definition} Final topology
:label: def-final-topology

Let $K_1\subseteq K_2\subseteq\cdots$ be compact Lie groups, each a closed
subgroup of the next. The *final topology* on $G=\bigcup_nK_n$ declares
$A\subseteq G$ open if and only if $A\cap K_n$ is open in $K_n$ for every $n$.
It is a Hausdorff group topology. For the standard block embeddings
$u\mapsto\mathrm{diag}(u,1)$ this defines the groups $SU(\infty)$,
$SO(\infty)$, $Sp(\infty)$, $U(\infty)$ and $O(\infty)$.
:::

:::{prf:theorem} {cite:t}`LupiniInductive2026`
:label: thm-lupini-inductive

Let $G=\bigcup_nK_n$ have the final topology, and suppose that, for some $j$,
the identity component $K_j^0$ is nonabelian or the finite group $K_j/K_j^0$
is not solvable; equivalently, $K_j$ is not solvable, since a compact
connected solvable Lie group is a torus. Then $G$ acts continuously on a
nonempty compact metrizable space $X$ in which no point is fixed by $K_j$. In
particular, $G$ is not extremely amenable.
:::

The proof is in [](#sec-proofs-inductive-limits).

:::{prf:corollary} {cite:t}`LupiniInductive2026`
:label: cor-lupini-inductive

With the final topology, none of $SU(\infty)$, $SO(\infty)$, $Sp(\infty)$,
$U(\infty)$ and $O(\infty)$ is extremely amenable.
:::

The proof is in [](#sec-proofs-inductive-limits).

:::{prf:remark}
:label: rem-lupini-inductive

For $SU(\infty)$ this answers negatively Question 19 in Pestov's list of open
problems on large topological groups {cite}`LupiniInductive2026`. The proof of
{prf:ref}`thm-lupini-inductive` uses Oliver's smooth actions of compact Lie
groups on disks with prescribed fixed-point sets, joined into an inverse
system of equivariant maps. For $U(\infty)$ and $O(\infty)$ the determinant
already gives a nontrivial compact quotient. The preprint leaves open the
case of solvable stages: if every $K_n$ is solvable and $G$ is minimally
almost periodic, is $G$ extremely amenable?
:::

:::{prf:theorem} {cite:t}`LupiniInductive2026`
:label: thm-lupini-inductive-umf

For each of $SU(\infty)$, $SO(\infty)$, $Sp(\infty)$, $U(\infty)$ and
$O(\infty)$, with the final topology, the universal minimal flow contains a
homeomorphic copy of $\beta\mathbb{N}$, and is therefore not metrizable. The
Bohr compactifications of $SU(\infty)$, $SO(\infty)$ and $Sp(\infty)$ are
trivial, and those of $U(\infty)$ and $O(\infty)$ are $\mathbb{T}$ and
$\{1,-1\}$, through the determinant.
:::

The proof is in [](#sec-proofs-inductive-limits).

:::{prf:theorem} {cite:t}`LupiniInductive2026`
:label: thm-lupini-inductive-free

Let $G$ be one of $SU(\infty)$, $SO(\infty)$, $Sp(\infty)$, $U(\infty)$ and
$O(\infty)$, with the final topology. Every continuous action of $G$ on a
nonempty compact Hausdorff space has a point fixed by an element of order
two; in particular, $G$ admits no free action on a compact space, and the
action of $G$ on $M(G)$ is not free. Nevertheless, the points of $M(G)$ with
trivial stabiliser form a dense $G_\delta$ set, which has full measure for
every invariant Radon probability measure on $M(G)$, and such measures exist.
:::

The proof is in [](#sec-proofs-inductive-limits).

:::{prf:remark}
:label: rem-lupini-inductive-free

These groups are $k_\omega$-groups: each carries the final topology of an
increasing sequence of compact subsets that cover it. Pestov's Question 4 asks whether
Veech's theorem, that every locally compact group acts freely on a compact
space, extends to $k_\omega$-groups; {prf:ref}`thm-lupini-inductive-free`
answers it negatively {cite}`LupiniInductive2026`.
:::

:::{prf:theorem} {cite:t}`LupiniInductive2026`
:label: thm-lupini-trace-class

The group

$$
SU_1=\{u\in U(\ell^2) : u-I \text{ is trace class and } \det(u)=1\},
$$

where $\det$ is the Fredholm determinant, is extremely amenable in the
topology of the trace norm $\|u-v\|_1=\mathrm{Tr}|u-v|$, and so is its dense
subgroup $\bigcup_nSU(n)$ with the same topology.
:::

The proof is in [](#sec-proofs-inductive-limits).

:::{prf:remark}
:label: rem-lupini-trace-class

The final topology on $\bigcup_nSU(n)$ is strictly finer than the trace-norm
topology. The determinant-one condition is needed in
{prf:ref}`thm-lupini-trace-class`: on the full group of trace-class
perturbations of the identity, the Fredholm determinant is a nontrivial
compact quotient {cite}`LupiniInductive2026`.
:::
