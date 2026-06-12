[← Previous: A14 Surface Integrals](A14_Surface_Integrals.md) | [Index](00_Index.md) | [Next: A16 Green's Theorem →](A16_Greens_Theorem.md)

---

# A15: Volume Integrals

> **Exam Weight**: Tier 2-3 | **Appeared in**: 2018, 2019, 2021 | **Typical Marks**: 4–6

Volume integrals (triple integrals) are used to sum a quantity over a 3D region. You must carefully determine the limits of integration for $x$, $y$, and $z$.

---

## The Formula

The volume integral of a scalar function $\phi(x,y,z)$ over a volume $V$ is:

$$
\iiint_V \phi \, dV = \iiint_V \phi \, dx \, dy \, dz
$$

For a vector field

$$
\vec{F} = F_1\hat{i} + F_2\hat{j} + F_3\hat{k},
$$

You integrate each component separately:

$$
\iiint_V \vec{F} \, dV = \left(\iiint_V F_1 \, dV\right)\hat{i} + \left(\iiint_V F_2 \, dV\right)\hat{j} + \left(\iiint_V F_3 \, dV\right)\hat{k}
$$

---

## Setting Up Integration Limits

The hardest part is finding the limits. For a region bounded by planes:
1. **Inner integral ($z$)**: Express $z$ in terms of $x$ and $y$ using the top and bottom bounding surfaces.
2. **Middle integral ($y$)**: Set $z=0$ (or analyze the projection on the $xy$-plane) to find $y$ in terms of $x$.
3. **Outer integral ($x$)**: Find the absolute minimum and maximum constant values for $x$.

---

## Worked Example 1: Scalar Volume Integral (PYQ 2018)

**Problem**: Let

$$
\phi = 45x^2y
$$

. Evaluate

$$
\iiint_V \phi \, dV
$$

where $V$ is the closed region bounded by planes $4x + 2y + z = 8, x = 0, y = 0, z = 0$.

**Solution**:

**Step 1**: Find limits.
- $z$ goes from $0$ to $8 - 4x - 2y$.
- In the $xy$-plane ($z=0$), the boundary is $4x + 2y = 8 \implies y = 4 - 2x$. So $y$ goes from $0$ to $4 - 2x$.
- Set $y=0$ to find $x$: $4x = 8 \implies x = 2$. So $x$ goes from $0$ to $2$.

**Step 2**: Set up integral.

$$
\int_0^2 \int_0^{4-2x} \int_0^{8-4x-2y} 45x^2y \, dz \, dy \, dx
$$

**Step 3**: Integrate $z$.

$$
45 \int_0^2 x^2 \int_0^{4-2x} y [z]_0^{8-4x-2y} dy dx = 45 \int_0^2 x^2 \int_0^{4-2x} (8y - 4xy - 2y^2) dy dx
$$

**Step 4**: Integrate $y$.

$$
45 \int_0^2 x^2 \left[ 4y^2 - 2xy^2 - \frac{2}{3}y^3 \right]_0^{4-2x} dx
$$

Notice

$$
4y^2 - 2xy^2 = y^2(4 - 2x).
$$

Substitute upper limit $y = 4-2x$:

$$
45 \int_0^2 x^2 \left[ (4-2x)^2(4-2x) - \frac{2}{3}(4-2x)^3 \right] dx = 45 \int_0^2 x^2 \left[ \frac{1}{3}(4-2x)^3 \right] dx
$$

**Step 5**: Integrate $x$.

$$
15 \int_0^2 x^2 (4-2x)^3 dx = 120 \int_0^2 x^2 (2-x)^3 dx
$$

Expand

$$
(2-x)^3 = 8 - 12x + 6x^2 - x^3:
$$

$$
120 \int_0^2 (8x^2 - 12x^3 + 6x^4 - x^5) dx
$$

$$
120 \left[ \frac{8}{3}x^3 - 3x^4 + \frac{6}{5}x^5 - \frac{x^6}{6} \right]_0^2 = 120 \left( \frac{64}{3} - 48 + \frac{192}{5} - \frac{64}{6} \right) = 128
$$

---

## Worked Example 2: Integral of Divergence (PYQ 2019)

**Problem**: Evaluate

$$
\iiint_V \nabla \cdot \vec{F} \, dV
$$

where

$$
\vec{F} = (2x^2 - 3z)\hat{i} - 2xy\hat{j} - 4x\hat{k}
$$

and $V$ is bounded by $x=0, y=0, z=0, 2x+2y+z=4$.

**Solution**:

**Step 1**: Find divergence.

$$
\nabla \cdot \vec{F} = \frac{\partial}{\partial x}(2x^2 - 3z) + \frac{\partial}{\partial y}(-2xy) + \frac{\partial}{\partial z}(-4x) = 4x - 2x + 0 = 2x
$$

**Step 2**: Find limits.
$z$ from $0$ to $4 - 2x - 2y$.
$y$ from $0$ to $2 - x$.
$x$ from $0$ to $2$.

**Step 3**: Integrate.

$$
\int_0^2 \int_0^{2-x} \int_0^{4-2x-2y} 2x \, dz \, dy \, dx = \int_0^2 \int_0^{2-x} 2x(4 - 2x - 2y) dy dx
$$

$$
= \int_0^2 2x \left[ (4-2x)y - y^2 \right]_0^{2-x} dx = \int_0^2 2x \left[ 2(2-x)(2-x) - (2-x)^2 \right] dx
$$

$$
= \int_0^2 2x (2-x)^2 dx = \int_0^2 (8x - 8x^2 + 2x^3) dx = \left[ 4x^2 - \frac{8}{3}x^3 + \frac{1}{2}x^4 \right]_0^2 = \frac{8}{3}
$$

---

## Exam Patterns

- Volume integrals in this course are mostly an exercise in polynomial integration and algebra. Make sure your expansions are careful.
- Setting up limits from an intersecting plane like $ax + by + cz = d$ is a recurring pattern. Always work from $z \to y \to x$.
- You will also compute volume integrals as the right-hand side of the Gauss Divergence Theorem.

---

[← Previous: A14 Surface Integrals](A14_Surface_Integrals.md) | [Index](00_Index.md) | [Next: A16 Green's Theorem →](A16_Greens_Theorem.md)
