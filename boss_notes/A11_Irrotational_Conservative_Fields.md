[← Previous: A10 Divergence and Curl](A10_Divergence_Curl.md) | [Index](00_Index.md) | [Next: A12 Vector Identities →](A12_Vector_Identities.md)

---

# A11: Irrotational and Conservative Fields

> **Exam Weight**: Tier 1 | **Appeared in**: 2018 (twice), 2019, 2020, 2021, CT | **Typical Marks**: 3–9

This is one of the most frequently tested topics in the entire course. You must know how to prove a field is irrotational (curl = 0) and how to find its scalar potential.

---

## Conservative Force Fields

### Definition

A force field $\vec{F}$ is **conservative** if the work done in moving a particle between two points is independent of the path taken.

Mathematical equivalent: A vector field $\vec{F}$ is conservative (or irrotational) if and only if its curl is zero:

$$
\nabla \times \vec{F} = \vec{0}
$$

### Scalar Potential

If $\vec{F}$ is a conservative field, it can be written as the gradient of a scalar function $\phi$:

$$
\vec{F} = \nabla\phi
$$

This function $\phi(x, y, z)$ is called the **scalar potential** of $\vec{F}$.

*(Note: $\nabla \times (\nabla\phi) = \vec{0}$ is a fundamental vector identity. The curl of a gradient is always zero).*

---

## The Method: Finding Scalar Potential

To find $\phi$ such that $\vec{F} = \nabla\phi$, where

$$
\vec{F} = F_1\hat{i} + F_2\hat{j} + F_3\hat{k}:
$$

:

1. Set up three equations:

$$
\frac{\partial\phi}{\partial x} = F_1 \quad \text{(1)}
$$

$$
\frac{\partial\phi}{\partial y} = F_2 \quad \text{(2)}
$$

$$
\frac{\partial\phi}{\partial z} = F_3 \quad \text{(3)}
$$

2. Integrate (1) with respect to $x$. Add a function $g(y, z)$ instead of a constant $C$.
3. Differentiate your result with respect to $y$, and equate it to (2) to find $\frac{\partial g}{\partial y}$.
4. Integrate to find $g(y, z)$, adding a function $h(z)$.
5. Substitute $g(y, z)$ back into your $\phi$ equation.
6. Differentiate with respect to $z$, equate to (3) to find $h'(z)$.
7. Integrate to find $h(z)$, adding a final constant $C$.

---

## Must-Know Problem 1 (PYQ 2020)

**Problem**: Show that

$$
\vec{A} = (6xy + z^3)\hat{i} + (3x^2 - z)\hat{j} + (3xz^2 - y)\hat{k}
$$

is irrotational. Find $\phi$ such that $\vec{A} = \nabla\phi$.

**Solution**:

**Step 1**: Show Irrotational.

$$
\nabla \times \vec{A} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ 6xy + z^3 & 3x^2 - z & 3xz^2 - y \end{vmatrix}
$$

- $\hat{i}$-component: $\frac{\partial}{\partial y}(3xz^2 - y) - \frac{\partial}{\partial z}(3x^2 - z) = -1 - (-1) = 0$
- $\hat{j}$-component: $\frac{\partial}{\partial z}(6xy + z^3) - \frac{\partial}{\partial x}(3xz^2 - y) = 3z^2 - 3z^2 = 0$
- $\hat{k}$-component: $\frac{\partial}{\partial x}(3x^2 - z) - \frac{\partial}{\partial y}(6xy + z^3) = 6x - 6x = 0$

Curl is zero. It is irrotational.

**Step 2**: Find Potential.

$$
\frac{\partial\phi}{\partial x} = 6xy + z^3 \implies \phi = 3x^2y + xz^3 + g(y, z) \quad \text{(Eq A)}
$$

Differentiate (Eq A) w.r.t $y$:

$$
\frac{\partial\phi}{\partial y} = 3x^2 + \frac{\partial g}{\partial y} = 3x^2 - z \implies \frac{\partial g}{\partial y} = -z
$$

Integrate w.r.t $y$: $g(y, z) = -yz + h(z)$. Substitute back into (Eq A):

$$
\phi = 3x^2y + xz^3 - yz + h(z) \quad \text{(Eq B)}
$$

Differentiate (Eq B) w.r.t $z$:

$$
\frac{\partial\phi}{\partial z} = 3xz^2 - y + h'(z) = 3xz^2 - y \implies h'(z) = 0 \implies h(z) = C
$$

Final Potential: $\phi = 3x^2y + xz^3 - yz + C$

---

## Must-Know Problem 2 (PYQ 2021)

**Problem**: Show that

$$
\vec{F} = (y^2 + 2xz^2)\hat{i} + (2xy - z)\hat{j} + (2x^2z - y + 2z)\hat{k}
$$

is irrotational and find scalar potential.

**Solution**:

**Step 1**: Show Irrotational.

$$
\nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ y^2 + 2xz^2 & 2xy - z & 2x^2z - y + 2z \end{vmatrix}
$$

- $\hat{i}$: $(-1) - (-1) = 0$
- $\hat{j}$: $(4xz) - (4xz) = 0$
- $\hat{k}$: $(2y) - (2y) = 0$

**Step 2**: Find Potential.

$$
\frac{\partial\phi}{\partial x} = y^2 + 2xz^2 \implies \phi = xy^2 + x^2z^2 + g(y, z)
$$

$$
\frac{\partial\phi}{\partial y} = 2xy + \frac{\partial g}{\partial y} = 2xy - z \implies \frac{\partial g}{\partial y} = -z \implies g(y, z) = -yz + h(z)
$$

$$
\phi = xy^2 + x^2z^2 - yz + h(z)
$$

$$
\frac{\partial\phi}{\partial z} = 2x^2z - y + h'(z) = 2x^2z - y + 2z \implies h'(z) = 2z \implies h(z) = z^2 + C
$$

Final Potential: $\phi = xy^2 + x^2z^2 - yz + z^2 + C$

---

## Must-Know Problem 3: Finding Unknown Constants (PYQ 2018)

**Problem**: Find constants $a, b, c$ so that

$$
\vec{V} = (x + 2y + az)\hat{i} + (bx - 3y - z)\hat{j} + (4x + cy + 2z)\hat{k}
$$

is irrotational.

**Solution**:

Set $\nabla \times \vec{V} = 0$:

$$
\begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ x + 2y + az & bx - 3y - z & 4x + cy + 2z \end{vmatrix} = 0
$$

- $\hat{i}$-component: $\frac{\partial}{\partial y}(4x + cy + 2z) - \frac{\partial}{\partial z}(bx - 3y - z) = c - (-1) = c + 1 = 0 \implies c = -1$
- $\hat{j}$-component: $\frac{\partial}{\partial z}(x + 2y + az) - \frac{\partial}{\partial x}(4x + cy + 2z) = a - 4 = 0 \implies a = 4$
- $\hat{k}$-component: $\frac{\partial}{\partial x}(bx - 3y - z) - \frac{\partial}{\partial y}(x + 2y + az) = b - 2 = 0 \implies b = 2$

Constants are $a = 4, b = 2, c = -1$.

---

## Exam Patterns

- "Show $\vec{F}$ is conservative and find scalar potential" is a 6-mark staple.
- "Find $a, b, c$ such that $\vec{F}$ is irrotational" is a 3-mark easy question.
- Always write the final potential function with the integration constant $+ C$.
- The determinant calculation for curl must be shown explicitly to get full marks.

---

[← Previous: A10 Divergence and Curl](A10_Divergence_Curl.md) | [Index](00_Index.md) | [Next: A12 Vector Identities →](A12_Vector_Identities.md)
