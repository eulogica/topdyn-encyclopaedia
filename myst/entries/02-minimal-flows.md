(sec-minimal)=
# Minimal flows

Minimal flows are the irreducible objects of topological dynamics: they cannot
be shrunk to a smaller subflow.

:::{prf:definition} Minimal flow
:label: def-minimal

A $G$-flow $X$ ({prf:ref}`def-flow`) is *minimal* if its only subflow is $X$
itself; equivalently, the orbit $Gx$ is dense in $X$ for every $x\in X$.
:::

:::{prf:proposition}
:label: prop-minimal-subflow

Every $G$-flow contains a minimal subflow.
:::

:::{prf:proof}
Order the subflows of $X$ by reverse inclusion. The intersection of a chain of
subflows is closed and invariant, and it is nonempty by compactness, since the
chain has the finite intersection property. By Zorn's lemma there is a minimal
subflow.
:::

:::{prf:example}
:label: ex-minimal

A fixed point is a minimal subflow. The rotation of the circle by an irrational
multiple of $2\pi$ is a minimal $\mathbb{Z}$-flow, since every orbit is dense.
:::

:::{figure} ../../figures/irrational-rotation.svg
:name: fig-irrational-rotation
:figclass: enc-figure
:alt: The first 12 and the first 100 points of an orbit of the rotation of the circle by an irrational multiple of 2 pi
:width: 100%

{prf:ref}`ex-minimal`: the first $12$ and the first $100$ points $x$, $Rx$, $R^2x$, … of an orbit of the rotation $R$ of the circle by $2\pi\alpha$, where $\alpha=(\sqrt5-1)/2$ is irrational. Every orbit is dense, so the rotation is a minimal $\mathbb{Z}$-flow.
:::
