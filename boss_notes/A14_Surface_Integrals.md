[← Previous: A13 Line Integrals](A13_Line_Integrals.md) | [Index](00_Index.md) | [Next: A15 Volume Integrals →](A15_Volume_Integrals.md)

---

# A14: Surface Integrals

> **Exam Weight**: Tier 3 | **Appeared in**: 2017, 2020 | **Typical Marks**: 6

A surface integral calculates the total flux of a vector field passing through a surface. It is the 2D equivalent of a line integral. Most surface integrals in exams are evaluated using the Divergence Theorem or Stokes' Theorem, but occasionally you must calculate them directly.

---

## The Formula

The flux of a vector field $\vec{A}$ through a surface $S$ is:

$$
\text{Flux} = \iint_S \vec{A} \cdot \hat{n} dS
$$

where $\hat{n}$ is the unit outward normal vector to the surface.

### Evaluation by Projection

To evaluate this directly, we project the surface $S$ onto one of the coordinate planes (e.g., the $xy$-plane).

Let $R$ be the projected region in the $xy$-plane. The differential area $dS$ on the surface relates to the area $dx dy$ on the plane by:

$$
dS = \frac{dx dy}{|\hat{n} \cdot \hat{k}|}
$$

If projecting onto the $yz$-plane:

$$
dS = \frac{dy dz}{\lvert \hat{n} \cdot \hat{i} \rvert}.
$$

If projecting onto the $zx$-plane:

$$
dS = \frac{dz dx}{\lvert \hat{n} \cdot \hat{j} \rvert}.
$$

---

## Must-Know Problem: Cylinder Surface (PYQ 2017, 2020)

**Problem**: Evaluate

$$
\iint_S \vec{A} \cdot \hat{n} dS
$$

where

$$
\vec{A} = z\hat{i} + x\hat{j} - 3y^2z\hat{k}
$$

and $S$ is the surface of the cylinder

$$
x^2 + y^2 = 16
$$

included in the first octant between $z=0$ and $z=5$.

**Solution**:

**Step 1**: Find the normal vector $\hat{n}$.
The surface is

$$
g(x,y,z) = x^2 + y^2 - 16 = 0.
$$

Gradient:

$$
\nabla g = 2x\hat{i} + 2y\hat{j}.
$$

Magnitude:

$$
\lvert \nabla g \rvert = \sqrt{4x^2 + 4y^2} = 2\sqrt{16} = 8.
$$

Unit normal:

$$
\hat{n} = \frac{2x\hat{i} + 2y\hat{j}}{8} = \frac{x\hat{i} + y\hat{j}}{4}
$$

**Step 2**: Calculate $\vec{A} \cdot \hat{n}$.

$$
\vec{A} \cdot \hat{n} = (z\hat{i} + x\hat{j} - 3y^2z\hat{k}) \cdot \left( \frac{x\hat{i} + y\hat{j}}{4} \right) = \frac{xz + xy}{4}
$$

**Step 3**: Choose a projection plane.
We project the cylinder onto the $yz$-plane. The region $R$ is bounded by $y \in [0, 4]$ and $z \in [0, 5]$.
The area element is:

$$
dS = \frac{dy dz}{|\hat{n} \cdot \hat{i}|} = \frac{dy dz}{|x/4|} = \frac{4}{x} dy dz
$$

**Step 4**: Set up and evaluate the integral.

$$
\iint_S (\vec{A} \cdot \hat{n}) dS = \iint_R \left( \frac{xz + xy}{4} \right) \left( \frac{4}{x} dy dz \right)
$$

The $x$ and $4$ cancel perfectly:

$$
\iint_R (z + y) dy dz
$$

Integrate over the rectangular region $R$:

$$
\int_0^4 \int_0^5 (y + z) dz dy
$$

Integrate with respect to $z$:

$$
\int_0^4 \left[ yz + \frac{z^2}{2} \right]_0^5 dy = \int_0^4 \left( 5y + \frac{25}{2} \right) dy
$$

Integrate with respect to $y$:

$$
\left[ \frac{5y^2}{2} + \frac{25}{2}y \right]_0^4 = \frac{5(16)}{2} + \frac{25(4)}{2} = 40 + 50 = 90
$$

The surface integral value is $90$.

---

## Exam Patterns

- Direct evaluation of surface integrals is rare. This single cylinder problem appeared identically in 2017 and 2020.
- The projection method is crucial. If the surface equation contains $x$ and $y$ but no $z$, projecting onto the $yz$ or $zx$ plane is usually easier than projecting onto the $xy$ plane.
- Most surface integrals in exams will ask you to use Gauss's Divergence Theorem or Stokes' Theorem instead of direct evaluation.

---

[← Previous: A13 Line Integrals](A13_Line_Integrals.md) | [Index](00_Index.md) | [Next: A15 Volume Integrals →](A15_Volume_Integrals.md)
