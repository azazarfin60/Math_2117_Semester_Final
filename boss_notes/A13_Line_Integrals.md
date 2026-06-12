[← Previous: A12 Vector Identities](A12_Vector_Identities.md) | [Index](00_Index.md) | [Next: A14 Surface Integrals →](A14_Surface_Integrals.md)

---

# A13: Line Integrals and Work Done

> **Exam Weight**: Tier 1-2 | **Appeared in**: 2017, 2018, 2020, 2021, 2024, CT | **Typical Marks**: 4–6

A line integral evaluates a function along a curve. The most common application is calculating the work done by a force field along a path.

---

## Formula for Work Done

The work done by a force field $\vec{F}$ in moving a particle along a curve $C$ is:

$$
W = \int_C \vec{F} \cdot d\vec{r}
$$

If

$$
\vec{F} = F_1\hat{i} + F_2\hat{j} + F_3\hat{k}
$$

 and

$$
d\vec{r} = dx\hat{i} + dy\hat{j} + dz\hat{k}:
$$

:

$$
W = \int_C (F_1 dx + F_2 dy + F_3 dz)
$$

### How to Evaluate

Convert everything to a single variable (a parameter like $t$, or $x$ if the path is $y = f(x)$). Then integrate normally.

---

## Worked Example 1: Parametric Path (PYQ 2024)

**Problem**: Find the work done in a force field

$$
\vec{F} = 3xy\hat{i} - 5z\hat{j} + 10x\hat{k}
$$

along the curve $x = t^2 + 1, y = 2t^2, z = t^3$ from $t = 1$ to $t = 2$.

**Solution**:

**Step 1**: Find differentials.
$x = t^2 + 1 \implies dx = 2t dt$
$y = 2t^2 \implies dy = 4t dt$
$z = t^3 \implies dz = 3t^2 dt$

**Step 2**: Substitute into the dot product $\vec{F} \cdot d\vec{r} = 3xy dx - 5z dy + 10x dz$.
- $3xy dx = 3(t^2 + 1)(2t^2)(2t dt) = (12t^5 + 12t^3) dt$
- $-5z dy = -5(t^3)(4t dt) = -20t^4 dt$
- $10x dz = 10(t^2 + 1)(3t^2 dt) = (30t^4 + 30t^2) dt$

**Step 3**: Sum and integrate.

$$
W = \int_1^2 (12t^5 + 10t^4 + 12t^3 + 30t^2) dt
$$

$$
W = \left[ 2t^6 + 2t^5 + 3t^4 + 10t^3 \right]_1^2
$$

Upper limit ($t=2$): $2(64) + 2(32) + 3(16) + 10(8) = 128 + 64 + 48 + 80 = 320$
Lower limit ($t=1$): $2 + 2 + 3 + 10 = 17$

$$
W = 320 - 17 = 303
$$

---

## Worked Example 2: Planar Path (PYQ 2017)

**Problem**: Evaluate

$$
\int_C (3xy\hat{i} - y^2\hat{j}) \cdot d\vec{r}
$$

when $C$ is $y = 2x^2$ from $(0,0)$ to $(1,2)$.

**Solution**:

We have $\vec{F} \cdot d\vec{r} = 3xy dx - y^2 dy$.

Path: $y = 2x^2 \implies dy = 4x dx$.
Limits for $x$: 0 to 1.

Substitute $y$ and $dy$:

$$
\int_0^1 \left[ 3x(2x^2)dx - (2x^2)^2(4x)dx \right] = \int_0^1 (6x^3 - 16x^5) dx
$$

$$
= \left[ \frac{3}{2}x^4 - \frac{8}{3}x^6 \right]_0^1 = \frac{3}{2} - \frac{8}{3} = \frac{9 - 16}{6} = -\frac{7}{6}
$$

---

## Worked Example 3: Segmented Path (PYQ 2021)

**Problem**: Evaluate

$$
\int_C \vec{A} \cdot d\vec{r}
$$

where

$$
\vec{A} = (3x^2 + 6y)\hat{i} - 14yz\hat{j} + 20xz^2\hat{k}
$$

along straight lines from $(0,0,0)$ to $(1,0,0)$ to $(1,1,0)$ to $(1,1,1)$.

**Solution**:

Break into three paths: $C_1, C_2, C_3$.
$\vec{A} \cdot d\vec{r} = (3x^2 + 6y)dx - 14yz dy + 20xz^2 dz$.

**Path $C_1$**: $(0,0,0)$ to $(1,0,0)$.
$y=0, z=0 \implies dy=0, dz=0$. $x$ goes 0 to 1.

$$
\int_{C_1} = \int_0^1 (3x^2 + 0) dx = [x^3]_0^1 = 1
$$

**Path $C_2$**: $(1,0,0)$ to $(1,1,0)$.
$x=1, z=0 \implies dx=0, dz=0$. $y$ goes 0 to 1.

$$
\int_{C_2} = \int_0^1 -14y(0) dy = 0
$$

**Path $C_3$**: $(1,1,0)$ to $(1,1,1)$.
$x=1, y=1 \implies dx=0, dy=0$. $z$ goes 0 to 1.

$$
\int_{C_3} = \int_0^1 20(1)z^2 dz = \left[\frac{20}{3}z^3\right]_0^1 = \frac{20}{3}
$$

Total Integral =

$$
1 + 0 + \frac{20}{3} = \frac{23}{3}
$$

.

---

## Exam Patterns

- Parametric path questions (like Example 1) are very common. Substitute $x, y, z$ and $dx, dy, dz$ perfectly. Watch your algebra.
- Segmented straight line paths (Example 3) are simple but test your logic. On each segment, two variables are constant (so their differentials are zero).
- Always explicitly write the dot product $\vec{F} \cdot d\vec{r} = F_1 dx + F_2 dy + F_3 dz$ first.

---

[← Previous: A12 Vector Identities](A12_Vector_Identities.md) | [Index](00_Index.md) | [Next: A14 Surface Integrals →](A14_Surface_Integrals.md)
