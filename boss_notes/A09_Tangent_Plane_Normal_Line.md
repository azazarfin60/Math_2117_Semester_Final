[← Previous: A08 Directional Derivative](A08_Directional_Derivative.md) | [Index](00_Index.md) | [Next: A10 Divergence and Curl →](A10_Divergence_Curl.md)

---

# A09: Tangent Plane and Normal Line

> **Exam Weight**: Tier 2 | **Appeared in**: 2018 | **Typical Marks**: 3

The gradient vector $\nabla F$ is perpendicular to the surface $F(x, y, z) = C$. We use this fact to find the equations of the tangent plane and the normal line at a given point.

---

## Formulas

Let a surface be given by $F(x, y, z) = C$, and let $P(x_0, y_0, z_0)$ be a point on this surface.

The normal vector to the surface at $P$ is the gradient evaluated at $P$:

$$
\vec{n} = \nabla F|_P = \frac{\partial F}{\partial x}\hat{i} + \frac{\partial F}{\partial y}\hat{j} + \frac{\partial F}{\partial z}\hat{k}
$$

Let the components of this normal vector be

$$
\vec{n} = A\hat{i} + B\hat{j} + C\hat{k}.
$$


### Equation of the Tangent Plane

The tangent plane passes through $P$ and is perpendicular to $\vec{n}$. Its equation is:

$$
A(x - x_0) + B(y - y_0) + C(z - z_0) = 0
$$

Or, in terms of partial derivatives:

$$
\frac{\partial F}{\partial x}(x - x_0) + \frac{\partial F}{\partial y}(y - y_0) + \frac{\partial F}{\partial z}(z - z_0) = 0
$$

### Equation of the Normal Line

The normal line passes through $P$ and is parallel to $\vec{n}$. Its symmetric equations are:

$$
\frac{x - x_0}{A} = \frac{y - y_0}{B} = \frac{z - z_0}{C}
$$

---

## Worked Example 1 (PYQ 2018)

**Problem**: Find an equation for the tangent plane to the surface $2xz^2 - 3xy - 4x = 7$ at the point $(1, -1, 2)$.

**Solution**:

**Step 1**: Define the surface function $F(x, y, z)$.

$$
F(x, y, z) = 2xz^2 - 3xy - 4x - 7 = 0
$$

**Step 2**: Find the partial derivatives (the components of the gradient).

$$
\frac{\partial F}{\partial x} = 2z^2 - 3y - 4
$$

$$
\frac{\partial F}{\partial y} = -3x
$$

$$
\frac{\partial F}{\partial z} = 4xz
$$

**Step 3**: Evaluate the partial derivatives at the point $(1, -1, 2)$.

$$
A = \frac{\partial F}{\partial x}(1, -1, 2) = 2(2)^2 - 3(-1) - 4 = 8 + 3 - 4 = 7
$$

$$
B = \frac{\partial F}{\partial y}(1, -1, 2) = -3(1) = -3
$$

$$
C = \frac{\partial F}{\partial z}(1, -1, 2) = 4(1)(2) = 8
$$

The normal vector is

$$
\vec{n} = 7\hat{i} - 3\hat{j} + 8\hat{k}.
$$


**Step 4**: Write the equation of the tangent plane.

Using the formula $A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$:

$$
7(x - 1) - 3(y - (-1)) + 8(z - 2) = 0
$$

$$
7(x - 1) - 3(y + 1) + 8(z - 2) = 0
$$

$$
7x - 7 - 3y - 3 + 8z - 16 = 0
$$

$$
7x - 3y + 8z = 26
$$

The equation of the tangent plane is $7x - 3y + 8z = 26$.

*(Note: If the question also asked for the normal line, it would be: $\frac{x-1}{7} = \frac{y+1}{-3} = \frac{z-2}{8}$)*

---

## Exam Patterns

- "Find the equation of the tangent plane" is a straightforward 3-mark application of the gradient.
- Always bring all terms to one side to define $F(x, y, z) = 0$ before taking derivatives.
- The normal vector components $(A, B, C)$ become the coefficients of $x, y, z$ in the final plane equation.

---

[← Previous: A08 Directional Derivative](A08_Directional_Derivative.md) | [Index](00_Index.md) | [Next: A10 Divergence and Curl →](A10_Divergence_Curl.md)
