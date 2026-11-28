(sec-kpt)=
# The Kechris–Pestov–Todorcevic correspondence

For automorphism groups of countable homogeneous structures, extreme
amenability is equivalent to a purely combinatorial property of the finite
substructures: the Ramsey property. For simplicity we restrict to relational
signatures.

:::{prf:definition} Fraïssé classes
:label: def-fraisse

Let $L$ be a relational signature. A class $\mathcal{K}$ of finite
$L$-structures, closed under isomorphism, is a *Fraïssé class* if it contains
only countably many structures up to isomorphism, contains structures of
arbitrarily large finite cardinality, and has the hereditary property, the
joint embedding property and the amalgamation property. By Fraïssé's theorem
there is a unique, up to isomorphism, countable ultrahomogeneous structure
$\mathbf{F}=\mathrm{Flim}(\mathcal{K})$ whose finite substructures are, up to
isomorphism, exactly the members of $\mathcal{K}$. Its automorphism group
$\mathrm{Aut}(\mathbf{F})$, with the topology of pointwise convergence, is a
closed subgroup of $S_\infty$. The class $\mathcal{K}$ is a *Fraïssé order
class* if $L$ contains a binary relation symbol $<$ that is interpreted as a
linear order in every member of $\mathcal{K}$.
:::

:::{prf:definition} Ramsey property
:label: def-ramsey

For $\mathbf{A},\mathbf{B}\in\mathcal{K}$, write
$\binom{\mathbf{B}}{\mathbf{A}}$ for the set of substructures of $\mathbf{B}$
isomorphic to $\mathbf{A}$. The class $\mathcal{K}$ has the *Ramsey property*
if for all $\mathbf{A},\mathbf{B}\in\mathcal{K}$ such that $\mathbf{A}$ embeds
in $\mathbf{B}$, and every $k\geq 1$, there is $\mathbf{C}\in\mathcal{K}$ such
that for every colouring $c\colon\binom{\mathbf{C}}{\mathbf{A}}\to\{1,\dots,k\}$
there is $\mathbf{B}'\in\binom{\mathbf{C}}{\mathbf{B}}$ on which $c$ is
constant, in the sense that $c$ is constant on
$\binom{\mathbf{B}'}{\mathbf{A}}$.
:::

:::{prf:theorem} {cite:t}`KPT2005`
:label: thm-kpt

Let $\mathcal{K}$ be a Fraïssé order class ({prf:ref}`def-fraisse`) with
Fraïssé limit $\mathbf{F}$. Then $\mathrm{Aut}(\mathbf{F})$ is extremely
amenable ({prf:ref}`def-ea`) if and only if $\mathcal{K}$ has the Ramsey
property ({prf:ref}`def-ramsey`).
:::

:::{prf:example}
:label: ex-kpt-rationals

The finite linear orders form a Fraïssé order class with Fraïssé limit
$(\mathbb{Q},<)$, and their Ramsey property is the finite Ramsey theorem.
{prf:ref}`thm-kpt` thus recovers the extreme amenability of
$\mathrm{Aut}(\mathbb{Q},<)$ ({prf:ref}`thm-pestov-ea`).
:::

:::{figure} ../../figures/ramsey-property.svg
:name: fig-ramsey-property
:figclass: enc-figure
:alt: A colouring of the pairs of a six-element linear order C in two colours, and three points whose three pairs have the same colour
:width: 100%

{prf:ref}`def-ramsey` for the finite linear orders of {prf:ref}`ex-kpt-rationals`, with $\mathbf{A}$ the linear order with two elements, $\mathbf{B}$ the one with three, and $k=2$. The copies of $\mathbf{A}$ in a linear order $\mathbf{C}$ with six elements are its pairs, drawn as arcs and coloured by $c$; the points $1$, $3$ and $5$ form a copy $\mathbf{B}'$ of $\mathbf{B}$ whose three pairs have the same colour.
:::

:::{prf:remark}
:label: rem-kpt-general

More generally, for any Fraïssé structure $\mathbf{F}$, the group
$\mathrm{Aut}(\mathbf{F})$ is extremely amenable if and only if the class of
finite substructures of $\mathbf{F}$ has the Ramsey property and consists of
rigid structures; see {cite}`NguyenVanThe2014`. Since every closed subgroup of
$S_\infty$ is the automorphism group of a Fraïssé structure, this
characterises the extremely amenable closed subgroups of $S_\infty$.
Kechris, Pestov and Todorcevic also developed a method for computing universal
minimal flows from order expansions with the Ramsey property and the ordering
property {cite}`KPT2005`.
:::
