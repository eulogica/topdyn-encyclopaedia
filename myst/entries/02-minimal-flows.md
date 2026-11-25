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
