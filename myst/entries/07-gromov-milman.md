(sec-gromov-milman)=
# The Gromov–Milman theorem

The first natural example of an extremely amenable group came from asymptotic
geometric analysis: concentration of measure on high-dimensional spheres and
groups forces fixed points.

:::{prf:theorem} Gromov–Milman {cite}`GromovMilman1983`
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
Gromov and Milman proved that every Lévy group is extremely amenable. This
mechanism, which Pestov calls the Ramsey–Dvoretzky–Milman phenomenon, gives
many further examples {cite}`Pestov2006`.
:::
