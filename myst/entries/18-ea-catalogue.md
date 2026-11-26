(sec-ea-catalogue)=
# A catalogue of extremely amenable groups

Extremely amenable groups arise from concentration of measure, from structural
Ramsey theory, and as stabilisers inside groups whose universal minimal flow
is metrizable. This section collects the main examples; groups and
topologies are as in the cited sources.

:::{prf:theorem} {cite:t}`Pestov2002`
:label: thm-pestov-urysohn

The isometry group $\mathrm{Iso}(\mathbb{U})$ of the Urysohn universal
complete separable metric space $\mathbb{U}$, with the compact-open topology, is
extremely amenable. The same holds for sufficiently homogeneous generalised
Urysohn metric spaces, and together with a theorem of Uspenskij this shows that
every topological group embeds into an extremely amenable group.
:::

:::{prf:theorem} {cite:t}`GiordanoPestov2007`
:label: thm-giordano-pestov

1. The group of measure-preserving automorphisms of a standard Lebesgue
   space with a non-atomic measure, with the weak topology, is extremely
   amenable.
2. The isometry groups of the spaces $L^p(0,1)$, $1\leq p<\infty$, are
   extremely amenable. This extends the case $p=2$ of
   {prf:ref}`thm-gromov-milman`.
3. A measure class preserving equivalence relation $R$ on a standard Borel
   space is amenable if and only if its full group $[R]$, with the uniform
   topology, is extremely amenable.
4. A von Neumann algebra is approximately finite-dimensional if and only if
   its unitary group, with the strong topology, is the product of an extremely
   amenable group and a compact group.

:::

:::{prf:remark} Groups of measurable maps
:label: rem-l0

The group $L^0(I,U(1))$ of measurable maps from the unit interval to the circle
group, with the topology of convergence in measure, is extremely amenable. This
was proved by Glasner and, independently and unpublished, by Furstenberg and
Weiss; see {cite}`GiordanoPestov2007`. Glasner also constructed an
infinite monothetic extremely amenable Polish group
({prf:ref}`thm-glasner-monothetic`).
:::

:::{prf:remark} Summary of the examples in this encyclopaedia
:label: rem-ea-summary

1. The groups of Herer and Christensen ({prf:ref}`rem-herer-christensen`),
   historically the first examples.
2. The unitary group of $\ell^2$ with the strong operator topology
   ({prf:ref}`thm-gromov-milman`), and more generally Lévy groups
   ({prf:ref}`rem-levy`).
3. $\mathrm{Aut}(\mathbb{Q},<)$ and $\mathrm{Homeo}_+[0,1]$
   ({prf:ref}`thm-pestov-ea`).
4. Automorphism groups of Fraïssé limits of Fraïssé order classes with the
   Ramsey property ({prf:ref}`thm-kpt`), such as the order expansions in
   {prf:ref}`ex-kpt-computations`.
5. The stabiliser of the standard chain in $\mathrm{Homeo}(E)$, for $E$ the
   Cantor set ({prf:ref}`ex-standard-chain`), and the stabiliser of a
   generic connected chain in the homeomorphism group of the Lelek fan
   ({prf:ref}`rem-lelek-method`).

By {prf:ref}`cor-lc-not-ea`, none of these groups is locally compact;
according to {cite}`GiordanoPestov2007`, this was first shown by Granirer and
Lau.
:::
