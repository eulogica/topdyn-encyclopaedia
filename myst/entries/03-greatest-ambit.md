(sec-ambit)=
# The greatest ambit

Every topological group has a largest flow with a distinguished point of dense
orbit. It is the Samuel compactification of the group, and it is where the
universal minimal flow lives.

:::{prf:definition} Ambit
:label: def-ambit

A *$G$-ambit* is a pair $(X,x_0)$ consisting of a $G$-flow $X$ and a point
$x_0\in X$ whose orbit $Gx_0$ is dense in $X$. A *morphism of ambits*
$(X,x_0)\to(Y,y_0)$ is a $G$-map sending $x_0$ to $y_0$. There is at most one
such morphism, since $Gx_0$ is dense, and it is surjective.
:::

:::{prf:definition} Right uniformly continuous functions
:label: def-ruc

A bounded function $f\colon G\to\mathbb{C}$ is *right uniformly continuous* if
for every $\varepsilon>0$ there is a neighbourhood $V$ of the identity such
that $|f(vg)-f(g)|<\varepsilon$ for all $g\in G$ and $v\in V$. These functions
form a unital C*-subalgebra $\mathrm{RUC}_b(G)$ of $\ell^\infty(G)$.
:::

:::{prf:remark} Conventions
:label: rem-ruc-conventions

These are the functions that are uniformly continuous for the uniform structure
with basic entourages $\{(x,y) : xy^{-1}\in V\}$. This structure is called the
right uniformity by Bourbaki and Pestov and the left uniformity by Ellis and
several other authors, so the same algebra appears in the literature under
both names. Check each source's convention before comparing statements.
:::

:::{prf:definition} Samuel compactification
:label: def-samuel

The *Samuel compactification* $S(G)$ of $G$ is the Gelfand spectrum of
$\mathrm{RUC}_b(G)$ ({prf:ref}`def-ruc`): the space of characters of
$\mathrm{RUC}_b(G)$ with the weak* topology. For $f\in\mathrm{RUC}_b(G)$ and
$h\in G$ the function $f^h(g)=f(hg)$ is again right uniformly continuous, and
$(h\varphi)(f)=\varphi(f^h)$ defines a continuous action of $G$ on $S(G)$.
Evaluation at points embeds $G$ equivariantly as a dense subset of $S(G)$, so
$(S(G),1)$ is a $G$-ambit ({prf:ref}`def-ambit`).
:::

:::{prf:proposition} Universal property
:label: prop-greatest-ambit

For every $G$-ambit $(X,x_0)$ there is a unique morphism of ambits
$(S(G),1)\to(X,x_0)$. For this reason $S(G)$ is called the *greatest ambit*
of $G$.
:::

:::{prf:proof}
Continuity of the action and compactness of $X$ give, for every $f\in C(X)$
and $\varepsilon>0$, a neighbourhood $V$ of the identity with
$|f(vx)-f(x)|<\varepsilon$ for all $x\in X$ and $v\in V$. Hence
$g\mapsto f(gx_0)$ lies in $\mathrm{RUC}_b(G)$. This defines a unital
*-homomorphism $C(X)\to\mathrm{RUC}_b(G)=C(S(G))$, whose dual map
$S(G)\to X$ is the required morphism. Uniqueness holds because $G$ is dense in
$S(G)$. See {cite}`Auslander1988,Pestov2006`.
:::
