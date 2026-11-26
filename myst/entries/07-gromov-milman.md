(sec-gromov-milman)=
# The Gromov–Milman theorem

The first natural example of an extremely amenable group came from asymptotic
geometric analysis: concentration of measure on high-dimensional spheres and
groups forces fixed points.

:::{prf:theorem} {cite:t}`GromovMilman1983`
:label: thm-gromov-milman

The unitary group $U(\ell^2)$ of an infinite-dimensional separable Hilbert
space, with the strong operator topology, is extremely amenable
({prf:ref}`def-ea`).
:::

:::{prf:remark} Lévy groups
:label: rem-levy

The proof shows that $U(\ell^2)$ is a *Lévy group*: roughly, it contains an
increasing chain of compact subgroups with dense union whose Haar measures
concentrate, in the sense of Lévy's concentration of measure phenomenon.
In {cite}`GromovMilman1983` the fixed point theorem is stated for increasing
unions of compact groups whose normalised Haar measures form a Lévy family,
acting equicontinuously on a compact space (Theorem 7.1 there), and it is
applied to the union of the groups $SO(n)$, to the group of finitary
permutations of $\mathbb{N}$ and to the union of the groups
$(\mathbb{Z}/2\mathbb{Z})^n$. Glasner observed that equicontinuity is not
needed {cite}`Glasner1998`, so every Lévy group is extremely amenable.
{prf:ref}`thm-gromov-milman` is the form in which the result is usually
quoted {cite}`Uspenskij2000,GiordanoPestov2007`. This mechanism, which Pestov
calls the Ramsey–Dvoretzky–Milman phenomenon, gives many further examples
{cite}`Pestov2006`.
:::
