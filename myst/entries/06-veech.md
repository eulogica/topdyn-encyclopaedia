(sec-veech)=
# Veech's theorem

For locally compact groups the universal minimal flow is as large as it can
be: the group acts on it freely.

:::{prf:theorem} Veech {cite}`Veech1977`
:label: thm-veech

Every locally compact group $G$ acts freely on its greatest ambit $S(G)$
({prf:ref}`prop-greatest-ambit`): $gx\neq x$ for all $x\in S(G)$ and all
$g\neq 1$. In particular, $G$ acts freely on $M(G)$
({prf:ref}`cor-umf-in-ambit`).
:::

:::{prf:remark}
:label: rem-veech-history

Veech's theorem shows in particular that every locally compact group admits a
free action on a compact space; for discrete groups this was proved earlier by
Ellis. Pestov's paper {cite}`Pestov1998` starts from the question of which
other topological groups admit such actions.
:::

:::{prf:corollary}
:label: cor-lc-not-ea

A nontrivial locally compact group is not extremely amenable.
:::

:::{prf:proof}
If $M(G)$ is a single point and $G$ acts freely on it, then $G$ is trivial
({prf:ref}`prop-ea-trivial-umf`).
:::

:::{prf:remark}
:label: rem-lc-metrizable

Kechris, Pestov and Todorcevic observed that a locally compact Polish group
with metrizable universal minimal flow is compact {cite}`KPT2005`; see also
{cite}`BYMT2017`. Compare [](#sec-metrizable), where metrizable universal
minimal flows of Polish groups are described.
:::
