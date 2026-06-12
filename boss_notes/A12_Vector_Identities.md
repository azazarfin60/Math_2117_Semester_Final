[← Previous: A11 Irrotational and Conservative Fields](A11_Irrotational_Conservative_Fields.md) | [Index](00_Index.md) | [Next: A13 Line Integrals →](A13_Line_Integrals.md)

---

# A12: Vector Identities and Proofs

> **Exam Weight**: Tier 2 | **Appeared in**: 2018, 2019, 2021, 2024 | **Typical Marks**: 3–5

Vector identity proofs test your ability to apply the Del operator systematically using the chain, product, and quotient rules.

---

## The Four Fundamental Identities

You should memorize these results, as they often simplify complex problems:

1. **Curl of Gradient is Zero**: $\nabla \times (\nabla\phi) = \vec{0}$
2. **Divergence of Curl is Zero**: $\nabla \cdot (\nabla \times \vec{A}) = 0$
3. **Curl of Curl**: $\nabla \times (\nabla \times \vec{A}) = \nabla(\nabla \cdot \vec{A}) - \nabla^2\vec{A}$
4. **Divergence of Gradient is Laplacian**: $\nabla \cdot (\nabla\phi) = \nabla^2\phi$

---

## Proof 1: (PYQ 2018)

**Statement**: If $\vec{A}$ is a constant vector, then $\nabla(\vec{r} \cdot \vec{A}) = \vec{A}$.

**Proof**:

Let the constant vector be

$$
\vec{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}.
$$

Let the position vector be

$$
\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}.
$$

Calculate the dot product:

$$
\vec{r} \cdot \vec{A} = A_1x + A_2y + A_3z
$$

Now calculate the gradient of this scalar:

$$
\nabla(\vec{r} \cdot \vec{A}) = \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right)(A_1x + A_2y + A_3z)
$$

$$
\nabla(\vec{r} \cdot \vec{A}) = \hat{i}\frac{\partial}{\partial x}(A_1x + A_2y + A_3z) + \hat{j}\frac{\partial}{\partial y}(A_1x + A_2y + A_3z) + \hat{k}\frac{\partial}{\partial z}(A_1x + A_2y + A_3z)
$$

$$
\nabla(\vec{r} \cdot \vec{A}) = A_1\hat{i} + A_2\hat{j} + A_3\hat{k} = \vec{A} \qquad \blacksquare
$$

---

## Proof 2: Curl of Curl Identity (PYQ 2018, 2021)

**Statement**: $\nabla \times (\nabla \times \vec{A}) = \nabla(\nabla \cdot \vec{A}) - \nabla^2\vec{A}$.

**Proof**:

Let

$$
\vec{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}.
$$

Let $\vec{V} = \nabla \times \vec{A}$. The components of $\vec{V}$ are:

$$
V_x = \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z}, \quad V_y = \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}, \quad V_z = \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}
$$

We want $\nabla \times \vec{V}$. Evaluate its x-component:

$$
(\nabla \times \vec{V})_x = \frac{\partial V_z}{\partial y} - \frac{\partial V_y}{\partial z}
$$

Substitute $V_z$ and $V_y$:

$$
(\nabla \times \vec{V})_x = \frac{\partial}{\partial y}\left( \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} \right) - \frac{\partial}{\partial z}\left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right)
$$

$$
(\nabla \times \vec{V})_x = \frac{\partial^2 A_y}{\partial y \partial x} - \frac{\partial^2 A_x}{\partial y^2} - \frac{\partial^2 A_x}{\partial z^2} + \frac{\partial^2 A_z}{\partial z \partial x}
$$

Add and subtract

$$
\frac{\partial^2 A_x}{\partial x^2}
$$

:

$$
(\nabla \times \vec{V})_x = \left( \frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_y}{\partial y \partial x} + \frac{\partial^2 A_z}{\partial z \partial x} \right) - \left( \frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_x}{\partial y^2} + \frac{\partial^2 A_x}{\partial z^2} \right)
$$

Factor out the operators:

$$
(\nabla \times \vec{V})_x = \frac{\partial}{\partial x}\left( \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z} \right) - \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} \right)A_x
$$

$$
(\nabla \times \vec{V})_x = \frac{\partial}{\partial x}(\nabla \cdot \vec{A}) - \nabla^2 A_x
$$

By symmetry for y and z components, assembling the vector gives:

$$
\nabla \times (\nabla \times \vec{A}) = \nabla(\nabla \cdot \vec{A}) - \nabla^2\vec{A} \qquad \blacksquare
$$

---

## Proof 3: (PYQ 2019)

**Statement**: Prove that the Laplacian of $1/r$ is zero (except at origin).

**Proof**:

Let $r = \sqrt{x^2 + y^2 + z^2}$. We know

$$
\frac{\partial r}{\partial x} = \frac{x}{r}
$$

, etc.

First, find the gradient of $r^{-1}$:

$$
\frac{\partial}{\partial x}(r^{-1}) = -r^{-2}\frac{\partial r}{\partial x} = -r^{-2}\left(\frac{x}{r}\right) = -\frac{x}{r^3}
$$

So,

$$
\nabla(r^{-1}) = -\frac{x\hat{i} + y\hat{j} + z\hat{k}}{r^3} = -\frac{\vec{r}}{r^3}.
$$

Now find the divergence of this gradient (which is $\nabla^2$):

$$
\nabla^2(r^{-1}) = \nabla \cdot \left(-\frac{\vec{r}}{r^3}\right) = -\left[ \frac{\partial}{\partial x}\left(\frac{x}{r^3}\right) + \frac{\partial}{\partial y}\left(\frac{y}{r^3}\right) + \frac{\partial}{\partial z}\left(\frac{z}{r^3}\right) \right]
$$

Using the quotient rule on the x-component:

$$
\frac{\partial}{\partial x}\left(\frac{x}{r^3}\right) = \frac{r^3(1) - x(3r^2\frac{\partial r}{\partial x})}{r^6} = \frac{r^3 - 3x^2r}{r^6} = \frac{1}{r^3} - \frac{3x^2}{r^5}
$$

Summing the x, y, and z terms:

$$
\nabla^2(r^{-1}) = -\left[ \left(\frac{1}{r^3} - \frac{3x^2}{r^5}\right) + \left(\frac{1}{r^3} - \frac{3y^2}{r^5}\right) + \left(\frac{1}{r^3} - \frac{3z^2}{r^5}\right) \right]
$$

$$
\nabla^2(r^{-1}) = -\left[ \frac{3}{r^3} - \frac{3(x^2 + y^2 + z^2)}{r^5} \right]
$$

Since $x^2 + y^2 + z^2 = r^2$:

$$
\nabla^2(r^{-1}) = -\left[ \frac{3}{r^3} - \frac{3r^2}{r^5} \right] = -\left[ \frac{3}{r^3} - \frac{3}{r^3} \right] = 0 \qquad \blacksquare
$$

---

## Exam Patterns

- The $\nabla \times (\nabla \times \vec{A})$ identity proof is tedious but important (appeared in 2018 and 2021). Write out the x-component clearly, then use symmetry.
- $\nabla^2(1/r) = 0$ is a classic vector calculus result. The trick is using

$$
\frac{\partial r}{\partial x} = \frac{x}{r}
$$

correctly with the quotient rule.

---

[← Previous: A11 Irrotational and Conservative Fields](A11_Irrotational_Conservative_Fields.md) | [Index](00_Index.md) | [Next: A13 Line Integrals →](A13_Line_Integrals.md)
