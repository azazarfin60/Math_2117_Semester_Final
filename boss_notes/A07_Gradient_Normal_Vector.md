[← Previous: A06 Divergence and Curl](A06_Divergence_Curl.md) | [Index](00_Index.md) | [Next: A08 Directional Derivative →](A08_Directional_Derivative.md)

---

# A07: Gradient and Normal to a Surface

> **Exam Weight**: Tier 1 | **Appeared in**: 2017, 2018, 2019, 2020, 2021, 2024 (6 papers) | **Typical Marks**: 2–5

The gradient is the foundation of vector calculus. It appears directly (find the gradient) and indirectly (in directional derivatives, surface normals, angle between surfaces).

---

## The Del Operator

The del operator (nabla) is the vector differential operator:

$$
\nabla = \hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}
$$

It acts on scalar functions (gradient), dot-products with vectors (divergence), and cross-products with vectors (curl).

---

## The Gradient

### Definition

The gradient of a scalar function $\phi(x, y, z)$ is:

$$
\nabla\phi = \frac{\partial\phi}{\partial x}\hat{i} + \frac{\partial\phi}{\partial y}\hat{j} + \frac{\partial\phi}{\partial z}\hat{k}
$$

Input: a scalar function. Output: a vector field.

### Geometric Meaning

The gradient vector $\nabla\phi$ at any point is **perpendicular to the surface** $\phi(x, y, z) = c$ at that point.

The magnitude $\lvert \nabla\phi \rvert$ gives the maximum rate of change of $\phi$ at that point.

The direction of $\nabla\phi$ points toward the direction of greatest increase.

### Properties

1.

$$
\nabla(f \pm g) = \nabla f \pm \nabla g
$$

2.

$$
\nabla(fg) = f\nabla g + g\nabla f
$$

3.

$$
\nabla\left(\frac{f}{g}\right) = \frac{g\nabla f - f\nabla g}{g^2}
$$

4. $\nabla r^n$:

$$
\nabla r^n = nr^{n-2}\vec{r} \quad (\text{where } r = \lvert \vec{r} \rvert)
$$

---

## Proof: Gradient is Normal to a Surface (PYQ 2020)

### Statement

$\nabla\phi$ is perpendicular to the surface $\phi(x, y, z) = c$.

### Proof

Let

$$
\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}
$$

be any curve lying on the surface $\phi = c$.

Since all points of this curve satisfy $\phi(x(t), y(t), z(t)) = c$, differentiate with respect to $t$:

$$
\frac{\partial\phi}{\partial x}\frac{dx}{dt} + \frac{\partial\phi}{\partial y}\frac{dy}{dt} + \frac{\partial\phi}{\partial z}\frac{dz}{dt} = 0
$$

This is a dot product:

$$
\nabla\phi \cdot \frac{d\vec{r}}{dt} = 0
$$

Since $\frac{d\vec{r}}{dt}$ is tangent to the curve, and the dot product is zero, $\nabla\phi$ is perpendicular to every tangent vector on the surface. So $\nabla\phi$ is normal to the surface.

$$
\blacksquare
$$

---

## Unit Normal Vector

The unit normal to a surface $\phi = c$ at a point is:

$$
\hat{n} = \frac{\nabla\phi}{|\nabla\phi|}
$$

### Worked Example: Unit Normal (CT)

**Problem**: Find the unit outward normal to

$$
(x-1)^2 + y^2 + (z+2)^2 = 9
$$

at $(3, 1, -4)$.

**Solution**:

Let

$$
f = (x-1)^2 + y^2 + (z+2)^2 - 9.
$$

$$
\nabla f = 2(x-1)\hat{i} + 2y\hat{j} + 2(z+2)\hat{k}
$$

At $(3, 1, -4)$:

$$
\nabla f = 4\hat{i} + 2\hat{j} - 4\hat{k}.
$$

Magnitude:

$$
\lvert \nabla f \rvert = \sqrt{16 + 4 + 16} = 6.
$$

$$
\hat{n} = \frac{4\hat{i} + 2\hat{j} - 4\hat{k}}{6} = \frac{2}{3}\hat{i} + \frac{1}{3}\hat{j} - \frac{2}{3}\hat{k}
$$

---

## Angle Between Two Surfaces (PYQ 2017, 2019, 2021 — 3 Times)

### The Method

The angle between two surfaces

$$
\phi_1 = c_1
$$

and

$$
\phi_2 = c_2
$$

at a point is the angle between their normal vectors:

$$
\cos\theta = \frac{\nabla\phi_1 \cdot \nabla\phi_2}{|\nabla\phi_1||\nabla\phi_2|}
$$

### Must-Know Problem (Appeared 3 Times)

**Problem**: Find the angle between

$$
x^2 + y^2 + z^2 = 9
$$

and

$$
z = x^2 + y^2 - 3
$$

at $(2, -1, 2)$.

**Solution**:

Surface 1:

$$
f_1 = x^2 + y^2 + z^2 - 9
$$

. Gradient:

$$
\nabla f_1 = 2x\hat{i} + 2y\hat{j} + 2z\hat{k}.
$$

At $(2, -1, 2)$:

$$
\vec{n}_1 = 4\hat{i} - 2\hat{j} + 4\hat{k}.
$$

Surface 2:

$$
f_2 = x^2 + y^2 - z - 3
$$

. Gradient:

$$
\nabla f_2 = 2x\hat{i} + 2y\hat{j} - \hat{k}.
$$

At $(2, -1, 2)$:

$$
\vec{n}_2 = 4\hat{i} - 2\hat{j} - \hat{k}.
$$

Dot product:

$$
\vec{n}_1 \cdot \vec{n}_2 = 16 + 4 - 4 = 16.
$$

Magnitudes:

$$
\lvert \vec{n}_1 \rvert = 6,
$$

$$
\lvert \vec{n}_2 \rvert = \sqrt{21}.
$$

$$
\cos\theta = \frac{16}{6\sqrt{21}} = \frac{8}{3\sqrt{21}}
$$

$$
\theta = \cos^{-1}\left(\frac{8}{3\sqrt{21}}\right)
$$

---

## Finding the Gradient at a Point (PYQ 2024)

**Problem**: If

$$
Q = 3x^2y - y^3z^2
$$

, find $\nabla Q$ at $(1, -2, -1)$.

**Solution**:

$$
\frac{\partial Q}{\partial x} = 6xy, \quad \frac{\partial Q}{\partial y} = 3x^2 - 3y^2z^2, \quad \frac{\partial Q}{\partial z} = -2y^3z
$$

At $(1, -2, -1)$:

$$
\frac{\partial Q}{\partial x} = 6(1)(-2) = -12
$$

$$
\frac{\partial Q}{\partial y} = 3(1) - 3(4)(1) = -9
$$

$$
\frac{\partial Q}{\partial z} = -2(-8)(-1) = -16
$$

$$
\nabla Q = -12\hat{i} - 9\hat{j} - 16\hat{k}
$$

---

## Exam Patterns

- "Find the angle between two surfaces" has appeared 3 times (2017, 2019, 2021). The exact same surfaces. Memorize it.
- "Find the gradient at a point" is a 2-3 mark easy question.
- "Show that gradient is normal to the surface" appeared in 2020 for 3 marks.
- The gradient formula is used in directional derivative (A08) and tangent plane (A09) problems. It is foundational.

---

[← Previous: A06 Divergence and Curl](A06_Divergence_Curl.md) | [Index](00_Index.md) | [Next: A08 Directional Derivative →](A08_Directional_Derivative.md)
