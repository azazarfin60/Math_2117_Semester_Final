[← Previous: A16 Green's Theorem](A16_Greens_Theorem.md) | [Index](00_Index.md) | [Next: A18 Gauss Divergence Theorem →](A18_Gauss_Divergence_Theorem.md)

---

# A17: Stokes' Theorem

> **Exam Weight**: Tier 2 | **Appeared in**: 2023, 2024 | **Typical Marks**: 5

Stokes' theorem is the 3D extension of Green's theorem. It relates a line integral around a closed curve in 3D space to a surface integral over any surface bounded by that curve.

---

## Statement of the Theorem

Let $S$ be an open, two-sided surface bounded by a closed, non-self-intersecting curve $C$. If $\vec{A}$ is a vector field with continuous first-order partial derivatives, then:

$$
\oint_C \vec{A} \cdot d\vec{r} = \iint_S (\nabla \times \vec{A}) \cdot \hat{n} dS
$$

Here the boundary curve $C$ is traversed in the positive direction (determined by the right-hand rule with respect to the normal vector $\hat{n}$).

---

## Must-Know Proof (PYQ 2023)

You must be able to prove Stokes' theorem by projecting the surface onto a coordinate plane and using Green's theorem.

Let the surface equation be $z = f(x, y)$ over a region $R$ in the $xy$-plane.
Let $\vec{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$. We prove it for $A_1$ first:

$$
\oint_C A_1 dx = \iint_S [\nabla \times (A_1\hat{i})] \cdot \hat{n} dS.
$$

**Step 1: The Line Integral**
Project the curve $C$ onto the $xy$-plane as $C'$.

$$
\oint_C A_1(x, y, z) dx = \oint_{C'} A_1(x, y, f(x, y)) dx
$$

Apply Green's theorem to $C'$:

$$
= \iint_R -\frac{\partial}{\partial y} [A_1(x, y, f(x, y))] dA
$$

Using the chain rule:

$$
\oint_C A_1 dx = \iint_R \left( -\frac{\partial A_1}{\partial y} - \frac{\partial A_1}{\partial z}\frac{\partial z}{\partial y} \right) dx dy \quad \text{--- (Eq 1)}
$$

**Step 2: The Surface Integral**
Calculate the curl of $A_1\hat{i}$:

$$
\nabla \times (A_1\hat{i}) = \frac{\partial A_1}{\partial z}\hat{j} - \frac{\partial A_1}{\partial y}\hat{k}
$$

For surface $z - f(x, y) = 0$, the normal vector gives:

$$
\hat{n} dS = \left( -\frac{\partial z}{\partial x}\hat{i} - \frac{\partial z}{\partial y}\hat{j} + \hat{k} \right) dx dy
$$

Calculate the dot product:

$$
[\nabla \times (A_1\hat{i})] \cdot \hat{n} dS = \left( -\frac{\partial A_1}{\partial z}\frac{\partial z}{\partial y} - \frac{\partial A_1}{\partial y} \right) dx dy \quad \text{--- (Eq 2)}
$$

Comparing (Eq 1) and (Eq 2) proves the theorem for $A_1$. The process is identical for $A_2$ and $A_3$. Adding them together yields Stokes' theorem.

---

## Worked Example: Verification (PYQ 2024)

**Problem**: Verify Stokes' theorem for $\vec{A} = (y - z + 2)\hat{i} + (yz + 4)\hat{j} - xz\hat{k}$ where $S$ is the surface of the cube $x=0, y=0, z=0, x=2, y=2, z=2$ above the $xy$ plane (i.e., open at the bottom).

**Solution**:

**Step 1: The Line Integral**
The boundary curve $C$ is the square in the $z=0$ plane from $x=0$ to $x=2$ and $y=0$ to $y=2$.
On $z=0, dz=0$, the vector field is $\vec{A} = (y + 2)\hat{i} + 4\hat{j}$.
$\oint_C \vec{A} \cdot d\vec{r} = \oint_C (y + 2) dx + 4 dy$

Path 1 ($y=0, dy=0, x$ from 0 to 2):

$$
\int_0^2 2 dx = 4
$$

Path 2 ($x=2, dx=0, y$ from 0 to 2):

$$
\int_0^2 4 dy = 8
$$

Path 3 ($y=2, dy=0, x$ from 2 to 0):

$$
\int_2^0 4 dx = -8
$$

Path 4 ($x=0, dx=0, y$ from 2 to 0):

$$
\int_2^0 4 dy = -8
$$

Total Line Integral = $4 + 8 - 8 - 8 = -4$.

**Step 2: The Surface Integral**
Calculate Curl:

$$
\nabla \times \vec{A} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ y-z+2 & yz+4 & -xz \end{vmatrix} = -y\hat{i} + (z - 1)\hat{j} - \hat{k}
$$

Evaluate over the 5 faces of the cube above $z=0$:
1. **Top ($z=2, \hat{n}=\hat{k}$)**: $(\nabla \times \vec{A}) \cdot \hat{n} = -1$. Integral:

$$
\iint (-1) dxdy = -4.
$$

2. **Front ($x=2, \hat{n}=\hat{i}$)**: $(\nabla \times \vec{A}) \cdot \hat{n} = -y$. Integral:

$$
\int_0^2\int_0^2 -y dydz = 2\left[-\frac{y^2}{2}\right]_0^2 = -4.
$$

3. **Back ($x=0, \hat{n}=-\hat{i}$)**: $(\nabla \times \vec{A}) \cdot \hat{n} = y$. Integral:

$$
\int_0^2\int_0^2 y dydz = 2\left[\frac{y^2}{2}\right]_0^2 = 4.
$$

4. **Right ($y=2, \hat{n}=\hat{j}$)**: $(\nabla \times \vec{A}) \cdot \hat{n} = z-1$. Integral:

$$
\int_0^2\int_0^2 (z-1) dxdz = 2\left[\frac{z^2}{2}-z\right]_0^2 = 0.
$$

5. **Left ($y=0, \hat{n}=-\hat{j}$)**: $(\nabla \times \vec{A}) \cdot \hat{n} = -(z-1)$. Integral:

$$
\int_0^2\int_0^2 (1-z) dxdz = 2\left[z-\frac{z^2}{2}\right]_0^2 = 0.
$$

Total Surface Integral = $-4 - 4 + 4 + 0 + 0 = -4$.

Both integrals yield $-4$. Stokes' theorem is verified.

---

## Exam Patterns

- Verifying Stokes' theorem over a cube involves 5 surface integrals (if open at the bottom) or 6 surface integrals. Be extremely meticulous with your normal vectors ($\hat{i}, -\hat{i}, \hat{j}, -\hat{j}, \hat{k}, -\hat{k}$) for each face.
- When asked to "evaluate using Stokes' theorem", you can choose whichever side of the equation is easier. Usually, converting a complex line integral into a surface integral via curl is the intended path.

---

[← Previous: A16 Green's Theorem](A16_Greens_Theorem.md) | [Index](00_Index.md) | [Next: A18 Gauss Divergence Theorem →](A18_Gauss_Divergence_Theorem.md)
