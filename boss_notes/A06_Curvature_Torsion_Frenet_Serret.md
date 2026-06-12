[← Previous: A05 Velocity and Acceleration](A05_Velocity_Acceleration_Particle_Motion.md) | [Index](00_Index.md) | [Next: C01 Vector Space Fundamentals →](C01_Field_Axioms_Vector_Space.md)

---

# A06: Curvature, Torsion, and Frenet-Serret

> **Exam Weight**: Tier 3 | **Appeared in**: 2020, 2023, CT | **Typical Marks**: 4–5

This section analyzes the geometric properties of a 3D curve in space. It relies heavily on taking multiple derivatives and cross products of the position vector $\vec{r}(t)$.

---

## Formulas for Curvature and Torsion

Let $\vec{r}(t)$ be the position vector of a curve parameterized by $t$. You need the first three derivatives:
1. $\vec{r}'$ (Velocity)
2. $\vec{r}''$ (Acceleration)
3. $\vec{r}'''$ (Jerk)

**Curvature ($K$)**: Measures how sharply a curve bends.

$$
K = \frac{\lvert \vec{r}' \times \vec{r}'' \rvert}{\lvert \vec{r}' \rvert^3}
$$

**Torsion ($T$)**: Measures how sharply a curve twists out of its plane.

$$
T = \frac{(\vec{r}' \times \vec{r}'') \cdot \vec{r}'''}{\lvert \vec{r}' \times \vec{r}'' \rvert^2}
$$

*(Note: The numerator is a scalar triple product).*

---

## Frenet-Serret Formulas

The Frenet-Serret formulas describe the kinematic properties of a particle moving along a continuous, differentiable curve in 3D space.

Let $s$ be the arc length along a space curve. 
- $\vec{T}$ = unit tangent vector
- $\vec{N}$ = unit principal normal vector
- $\vec{B}_b$ = unit binormal vector
- $\kappa$ = curvature
- $\tau$ = torsion

The three formulas are:
1.

$$
\frac{d\vec{T}}{ds} = \kappa \vec{N}
$$

2.

$$
\frac{d\vec{N}}{ds} = -\kappa \vec{T} + \tau \vec{B}_b
$$

3.

$$
\frac{d\vec{B}_b}{ds} = -\tau \vec{N}
$$

---

## Worked Example: Calculating and (PYQ 2020, 2023)

**Problem**: For the space curve $x = t, y = t^2, z = \frac{2}{3}t^3$, find the curvature $K$ and the torsion $T$.

**Solution**:
**Step 1: Find Derivatives**

$$
\vec{r}(t) = t\hat{i} + t^2\hat{j} + \frac{2}{3}t^3\hat{k}
$$

$$
\vec{r}' = \hat{i} + 2t\hat{j} + 2t^2\hat{k}
$$

$$
\vec{r}'' = 2\hat{j} + 4t\hat{k}
$$

$\vec{r}''' = 4\hat{k}$

**Step 2: Cross Product and Magnitudes**

$$
\vec{r}' \times \vec{r}'' = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2t & 2t^2 \\ 0 & 2 & 4t \end{vmatrix} = \hat{i}(8t^2 - 4t^2) - \hat{j}(4t - 0) + \hat{k}(2 - 0) = 4t^2\hat{i} - 4t\hat{j} + 2\hat{k}
$$

Magnitude $\lvert \vec{r}' \rvert$:

$$
\lvert \vec{r}' \rvert = \sqrt{1^2 + (2t)^2 + (2t^2)^2} = \sqrt{1 + 4t^2 + 4t^4} = \sqrt{(2t^2 + 1)^2} = 2t^2 + 1
$$

Magnitude $\lvert \vec{r}' \times \vec{r}'' \rvert$:

$$
\lvert \vec{r}' \times \vec{r}'' \rvert = \sqrt{(4t^2)^2 + (-4t)^2 + 2^2} = \sqrt{16t^4 + 16t^2 + 4} = \sqrt{4(4t^4 + 4t^2 + 1)} = 2(2t^2 + 1)
$$

**Step 3: Calculate Curvature ($K$)**

$$
K = \frac{\lvert \vec{r}' \times \vec{r}'' \rvert}{\lvert \vec{r}' \rvert^3} = \frac{2(2t^2 + 1)}{(2t^2 + 1)^3} = \frac{2}{(2t^2 + 1)^2}
$$

**Step 4: Calculate Torsion ($T$)**
Calculate the scalar triple product $(\vec{r}' \times \vec{r}'') \cdot \vec{r}'''$:

$$
(4t^2\hat{i} - 4t\hat{j} + 2\hat{k}) \cdot (4\hat{k}) = 8
$$

$$
T = \frac{(\vec{r}' \times \vec{r}'') \cdot \vec{r}'''}{\lvert \vec{r}' \times \vec{r}'' \rvert^2} = \frac{8}{[2(2t^2 + 1)]^2} = \frac{8}{4(2t^2 + 1)^2} = \frac{2}{(2t^2 + 1)^2}
$$

In this specific curve, curvature equals torsion!

---

## Exam Patterns
- This specific problem ($x=t, y=t^2, z=\frac{2}{3}t^3$) is practically the only curvature/torsion problem asked. The trick is recognizing that $1 + 4t^2 + 4t^4$ is a perfect square $(2t^2 + 1)^2$.
- Be able to state the Frenet-Serret formulas verbatim.

---

[← Previous: A05 Velocity and Acceleration](A05_Velocity_Acceleration_Particle_Motion.md) | [Index](00_Index.md) | [Next: C01 Vector Space Fundamentals →](C01_Field_Axioms_Vector_Space.md)
