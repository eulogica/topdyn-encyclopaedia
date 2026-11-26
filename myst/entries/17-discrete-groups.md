(sec-discrete)=
# Discrete groups

For locally compact groups that are not compact, and in particular for
infinite discrete groups, the universal minimal flow is a large,
non-metrizable space. For countable discrete groups its topology is
nevertheless determined up to one cardinal parameter.

:::{prf:remark} Size
:label: rem-umf-size

If $G$ is locally compact and not compact, then $M(G)$ is not metrizable
{cite}`GlasnerWeiss2003,GiordanoPestov2007`; compare
{prf:ref}`rem-lc-metrizable`. By {prf:ref}`thm-veech`, $G$ acts freely
on it.
:::

:::{prf:example}
:label: ex-discrete-ambit

If $G$ is discrete, every bounded function on $G$ is right uniformly
continuous, so $\mathrm{RUC}_b(G)=\ell^\infty(G)$, and $S(G)$ is the
Stone–Čech compactification $\beta G$.
:::

:::{prf:proposition}
:label: prop-extremely-disconnected

If $G$ is discrete, then $M(G)$ is extremely disconnected: the closure of
every open subset is open.
:::

:::{prf:proof}
The space $\beta G$ is extremely disconnected, and by
{prf:ref}`prop-minimal-ideals` there is a retraction
$r\colon\beta G\to M$ onto a minimal subflow $M\cong M(G)$. Let $U\subseteq M$
be open and $V=r^{-1}(U)$, so that $U\subseteq V$ and $r(V)=U$. Then
$\overline{U}\subseteq\overline{V}\cap M\subseteq r(\overline{V})
\subseteq\overline{r(V)}=\overline{U}$, where the closure of $U$ is taken in
$M$. Hence $\overline{U}=\overline{V}\cap M$, which is open in $M$ because
$\overline{V}$ is open in $\beta G$.
:::

:::{prf:theorem} {cite:t}`BalcarBlaszczyk1990`
:label: thm-balcar-blaszczyk

Let $B$ be an infinite complete Boolean algebra which admits a countable family
$H$ of automorphisms such that the dynamical system $(B,H)$ is minimal. Then
$B$ is isomorphic to the completion of the free Boolean algebra on $\pi(B)$
generators, where $\pi(B)$ is the least cardinality of a dense subset of
$B\setminus\{0\}$.
:::

:::{prf:corollary}
:label: cor-discrete-cohen

Let $G$ be a countably infinite discrete group. Then $M(G)$ is homeomorphic to
the Stone space of the completion of a free Boolean algebra; equivalently, to
the Gleason cover (absolute) of a Cantor cube $\{0,1\}^\kappa$.
:::

:::{prf:proof}
By {prf:ref}`prop-extremely-disconnected`, the clopen subsets of $M(G)$
form a complete Boolean algebra $B$, whose Stone space is $M(G)$. It is
infinite, because $G$ is infinite and acts freely on $M(G)$
({prf:ref}`thm-veech`). The group $G$ acts on $B$ by automorphisms, and
minimality of $M(G)$ says that for every nonzero $b\in B$ finitely many
translates of $b$ cover $M(G)$, which is minimality of $(B,G)$ in the sense of
Balcar and Błaszczyk. {prf:ref}`thm-balcar-blaszczyk` applies. The
completion of the free Boolean algebra on $\kappa$ generators is the algebra
of regular open subsets of $\{0,1\}^\kappa$, whose Stone space is the Gleason
cover of $\{0,1\}^\kappa$.
:::

:::{prf:example} The integers
:label: ex-umf-integers

For $G=\mathbb{Z}$, the cardinal is the continuum: $M(\mathbb{Z})$ is the
Gleason cover of $\{0,1\}^{\mathfrak{c}}$, that is, the Stone space of the
Boolean algebra of regular open subsets of $\{0,1\}^{\mathfrak{c}}$
{cite}`BartosovaKwiatkowska2019`.
:::
