[← Previous: A07 Gradient and Normal Vector](A07_Gradient_Normal_Vector.md) | [Index](00_Index.md) | [Next: A09 Tangent Plane →](A09_Tangent_Plane.md)

---

# A08: Directional Derivative

> **Exam Weight**: Tier 1 | **Appeared in**: 2017, 2018, 2019, 2021 | **Typical Marks**: 3–4

The directional derivative measures how fast a scalar function changes in a specific direction. It builds directly on the gradient.

---

## Definition

The directional derivative of $\phi$ at point $P$ in the direction of unit vector $\hat{u}$ is:

$$
D_{\hat{u}}\phi = \nabla\phi \cdot \hat{u}
$$

It gives the rate of change of $\phi$ at $P$ in the direction $\hat{u}$.

### Key Facts

- Maximum value of $D_{\hat{u}}\phi$ is $\lvert \nabla\phi \rvert$, achieved in the direction of $\nabla\phi$ itself.
- Minimum value is $-\lvert \nabla\phi \rvert$, in the opposite direction.
- $D_{\hat{u}}\phi = 0$ when $\hat{u}$ is perpendicular to $\nabla\phi$ (moving along the level surface).

---

## The Three-Step Method

1. **Find the gradient** $\nabla\phi$ and evaluate at the given point.
2. **Find the unit direction vector** $\hat{u} = \frac{\vec{d}}{\lvert \vec{d} \rvert}$.
3. **Dot product**: $D_{\hat{u}}\phi = \nabla\phi \cdot \hat{u}$.

---

## Worked Example 1 (PYQ 2018)

**Problem**: Find the directional derivative of $\phi = x^2yz + 4xz^2$ at $(1, -2, -1)$ in the direction $2\hat{i} - \hat{j} - 2\hat{k}$.

**Solution**:

**Step 1**: Gradient.

$$
\nabla\phi = (2xyz + 4z^2)\hat{i} + x^2z\hat{j} + (x^2y + 8xz)\hat{k}
$$

At $(1, -2, -1)$:

$$
\nabla\phi = (4 + 4)\hat{i} + (1)(-1)\hat{j} + (-2 - 8)\hat{k} = 8\hat{i} - \hat{j} - 10\hat{k}
$$

**Step 2**: Unit vector.

$$
\hat{u} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{\sqrt{4 + 1 + 4}} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3}
$$

**Step 3**: Dot product.

$$
D_{\hat{u}}\phi = \frac{8(2) + (-1)(-1) + (-10)(-2)}{3} = \frac{16 + 1 + 20}{3} = \frac{37}{3}
$$

---

## Worked Example 2 (PYQ 2017)

**Problem**: Find the directional derivative of $\phi = 4e^{2x-y+z}$ at $(1, 1, -1)$ toward $(-3, 5, 6)$.

**Solution**:

**Step 1**: Direction from $P(1,1,-1)$ to $Q(-3,5,6)$:

$$
\vec{d} = -4\hat{i} + 4\hat{j} + 7\hat{k}, \quad |\vec{d}| = \sqrt{16+16+49} = 9
$$

$$
\hat{u} = \frac{-4\hat{i} + 4\hat{j} + 7\hat{k}}{9}
$$

**Step 2**: Gradient of $\phi = 4e^{2x-y+z}$:

$$
\nabla\phi = 4e^{2x-y+z}(2\hat{i} - \hat{j} + \hat{k})
$$

At $(1,1,-1)$: exponent = $2-1-1 = 0$, so $e^0 = 1$:

$$
\nabla\phi = 8\hat{i} - 4\hat{j} + 4\hat{k}
$$

**Step 3**:

$$
D_{\hat{u}}\phi = \frac{8(-4) + (-4)(4) + 4(7)}{9} = \frac{-32 - 16 + 28}{9} = -\frac{20}{9}
$$

---

## Worked Example 3 (PYQ 2021)

**Problem**: Find the directional derivative of $f = x^2 + xy + z^2$ at $A(1,-1,-1)$ in the direction of $AB$ where $B(3, 2, 1)$.

**Solution**:

Direction: $\vec{AB} = 2\hat{i} + 3\hat{j} + 2\hat{k}$. Unit vector: $\hat{u} = \frac{2\hat{i}+3\hat{j}+2\hat{k}}{\sqrt{17}}$.

Gradient: $\nabla f = (2x+y)\hat{i} + x\hat{j} + 2z\hat{k}$.

At $(1,-1,-1)$: $\nabla f = \hat{i} + \hat{j} - 2\hat{k}$.

$$
D_{\hat{u}}f = \frac{2 + 3 - 4}{\sqrt{17}} = \frac{1}{\sqrt{17}}
$$

---

## Worked Example 4 (PYQ 2019)

**Problem**: Find directional derivative of $\phi = x^2yz + 4xz^2$ at $(1, -2, 1)$ in direction $2\hat{i} - \hat{j} - 2\hat{k}$.

**Solution**:

At $(1,-2,1)$: $\nabla\phi = 0\hat{i} + \hat{j} + 6\hat{k}$.

$$
D_{\hat{u}}\phi = \frac{0(2) + 1(-1) + 6(-2)}{3} = \frac{-13}{3}
$$

---

## Exam Patterns

- Directional derivative appears in about 4 out of 7 papers.
- The same function $\phi = x^2yz + 4xz^2$ has appeared in 2018 and 2019 with different points.
- Always show the three steps clearly: gradient, unit vector, dot product.
- The direction is sometimes given as a vector (just normalize it) and sometimes as "toward point Q" (compute $\vec{PQ}$ first, then normalize).

---

[← Previous: A07 Gradient and Normal Vector](A07_Gradient_Normal_Vector.md) | [Index](00_Index.md) | [Next: A09 Tangent Plane →](A09_Tangent_Plane.md)
