# Lecture 03: Concept of Gradient and Geometric Meaning

> **Series**: Vector Calculus
> **Lecture**: 03 of 14
> **Video**: https://www.youtube.com/watch?v=fqWikeRWBfk

---

**Navigation**
[< Previous Lecture](02_Vector_Differentiation.md) | [Index](README.md) | [Next Lecture >](04_Directional_Derivative.md)

---

## Prerequisites
We know that a scalar point function $\phi(x,y,z) = \text{Constant}$ defines a 3D **Surface**. For example, $\phi(x,y,z) = x^2 + xyz + 2 = \text{Constant}$. To study how these scalar fields change, we need a special operator that can take derivatives in all spatial directions at once.

---

## 1. The Del Operator and Gradient

### The Del Operator ($\nabla$)
In vector calculus, we use the **Del Operator** (or Nabla), denoted by $\nabla$. It is a vector differential operator:
$$
\nabla = \hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}
$$
It functions as a vector differential operator, analogous to the scalar differential operator $\frac{d}{dx}$.

### The Gradient ($\text{grad }\phi$)
When we apply the del operator to a scalar point function $\phi$, we get the **gradient** of $\phi$:
$$
\nabla\phi = \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right)\phi = \hat{i}\frac{\partial\phi}{\partial x} + \hat{j}\frac{\partial\phi}{\partial y} + \hat{k}\frac{\partial\phi}{\partial z}
$$
**Crucial Characteristic**: The gradient of a scalar point function always results in a **vector quantity**.

### Geometric Meaning
$\nabla\phi$ is the **normal (perpendicular) vector** to the surface defined by $\phi(x,y,z) = \text{Constant}$ at any given point $(x,y,z)$.

---

## 2. Properties of Gradient (With Proofs)

Let $f$ and $g$ be two scalar point functions, and $\vec{a}$ be a constant vector.

### Property I: Gradient of Sum/Difference
**Statement:** $\nabla(f \pm g) = \nabla f \pm \nabla g$

**Proof:**
$$
\nabla(f \pm g) = \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right)(f \pm g)
$$
$$
= \hat{i}\left(\frac{\partial f}{\partial x} \pm \frac{\partial g}{\partial x}\right) + \hat{j}\left(\frac{\partial f}{\partial y} \pm \frac{\partial g}{\partial y}\right) + \hat{k}\left(\frac{\partial f}{\partial z} \pm \frac{\partial g}{\partial z}\right)
$$
$$
= \left(\hat{i}\frac{\partial f}{\partial x} + \hat{j}\frac{\partial f}{\partial y} + \hat{k}\frac{\partial f}{\partial z}\right) \pm \left(\hat{i}\frac{\partial g}{\partial x} + \hat{j}\frac{\partial g}{\partial y} + \hat{k}\frac{\partial g}{\partial z}\right) = \nabla f \pm \nabla g \quad \text{(Proved)}
$$

### Property II: Gradient of Product
**Statement:** $\nabla(fg) = f\nabla g + g\nabla f$

**Proof:**
$$
\nabla(fg) = \hat{i}\frac{\partial}{\partial x}(fg) + \hat{j}\frac{\partial}{\partial y}(fg) + \hat{k}\frac{\partial}{\partial z}(fg)
$$
$$
= \hat{i}\left[f\frac{\partial g}{\partial x} + g\frac{\partial f}{\partial x}\right] + \hat{j}\left[f\frac{\partial g}{\partial y} + g\frac{\partial f}{\partial y}\right] + \hat{k}\left[f\frac{\partial g}{\partial z} + g\frac{\partial f}{\partial z}\right]
$$
$$
= f\left[\hat{i}\frac{\partial g}{\partial x} + \hat{j}\frac{\partial g}{\partial y} + \hat{k}\frac{\partial g}{\partial z}\right] + g\left[\hat{i}\frac{\partial f}{\partial x} + \hat{j}\frac{\partial f}{\partial y} + \hat{k}\frac{\partial f}{\partial z}\right] = f\nabla g + g\nabla f \quad \text{(Proved)}
$$

### Property III: Gradient of Quotient
**Statement:** $\nabla\left(\frac{f}{g}\right) = \frac{g\nabla f - f\nabla g}{g^2}, \quad g \neq 0$

**Proof:**
$$
\nabla\left(\frac{f}{g}\right) = \hat{i}\frac{\partial}{\partial x}\left(\frac{f}{g}\right) + \hat{j}\frac{\partial}{\partial y}\left(\frac{f}{g}\right) + \hat{k}\frac{\partial}{\partial z}\left(\frac{f}{g}\right)
$$
$$
= \hat{i}\left[\frac{g\frac{\partial f}{\partial x} - f\frac{\partial g}{\partial x}}{g^2}\right] + \hat{j}\left[\frac{g\frac{\partial f}{\partial y} - f\frac{\partial g}{\partial y}}{g^2}\right] + \hat{k}\left[\frac{g\frac{\partial f}{\partial z} - f\frac{\partial g}{\partial z}}{g^2}\right]
$$
$$
= \frac{g\left[\hat{i}\frac{\partial f}{\partial x} + \hat{j}\frac{\partial f}{\partial y} + \hat{k}\frac{\partial f}{\partial z}\right] - f\left[\hat{i}\frac{\partial g}{\partial x} + \hat{j}\frac{\partial g}{\partial y} + \hat{k}\frac{\partial g}{\partial z}\right]}{g^2} = \frac{g\nabla f - f\nabla g}{g^2} \quad \text{(Proved)}
$$

### Property IV: Operator Action on Position Vector
**Statement:** $(\vec{a} \cdot \nabla)\vec{r} = \vec{a}$

**Proof:**
Let $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ and constant vector $\vec{a} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$.
Expand the operator:
$$
\vec{a} \cdot \nabla = (a_1\hat{i} + a_2\hat{j} + a_3\hat{k}) \cdot \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right) = a_1\frac{\partial}{\partial x} + a_2\frac{\partial}{\partial y} + a_3\frac{\partial}{\partial z}
$$
Apply to $\vec{r}$:
$$
(\vec{a} \cdot \nabla)\vec{r} = \left(a_1\frac{\partial}{\partial x} + a_2\frac{\partial}{\partial y} + a_3\frac{\partial}{\partial z}\right)(x\hat{i} + y\hat{j} + z\hat{k})
$$
$$
= a_1(\hat{i}) + a_2(\hat{j}) + a_3(\hat{k}) = \vec{a} \quad \text{(Proved)}
$$

---

## 3. Solved Problems

### Problem 1: Basic Gradient Calculation
**Question:** If $f = x^3 + y^3 + 3xy$, find $\text{grad } f$.

**Solution:**
$$
\text{grad } f = \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right)(x^3 + y^3 + 3xy)
$$
$$
\text{grad } f = (3x^2 + 3y)\hat{i} + (3y^2 + 3x)\hat{j} + 0\hat{k}
$$
$$
\text{grad } f = 3(x^2 + y)\hat{i} + 3(y^2 + x)\hat{j}
$$

### Problem 2: Gradient Evaluation at a Point
**Question:** If $\phi(x,y,z) = 2x^2y^3 - 3y^2z^3$, find $\nabla\phi$ at the point $(1, -1, 1)$.

**Solution:**
Calculate partial derivatives:
$$
\frac{\partial\phi}{\partial x} = 4xy^3, \quad \frac{\partial\phi}{\partial y} = 6x^2y^2 - 6yz^3, \quad \frac{\partial\phi}{\partial z} = -9y^2z^2
$$
Combine to form gradient $\nabla\phi$:
$$
\nabla\phi = 4xy^3\hat{i} + (6x^2y^2 - 6yz^3)\hat{j} - 9y^2z^2\hat{k}
$$
Evaluate at point $(1, -1, 1)$:
$$
\left.\frac{\partial\phi}{\partial x}\right|_{(1,-1,1)} = 4(1)(-1)^3 = -4
$$
$$
\left.\frac{\partial\phi}{\partial y}\right|_{(1,-1,1)} = 6(1)^2(-1)^2 - 6(-1)(1)^3 = 6 + 6 = 12
$$
$$
\left.\frac{\partial\phi}{\partial z}\right|_{(1,-1,1)} = -9(-1)^2(1)^2 = -9
$$
Therefore:
$$
\nabla\phi\Big|_{(1,-1,1)} = -4\hat{i} + 12\hat{j} - 9\hat{k}
$$

### Problem 3: Gradient of a Scalar Triple Product
**Question:** If $\vec{a}$ and $\vec{b}$ are constant vectors, prove that $\nabla[\vec{r}\ \vec{a}\ \vec{b}] = \vec{a} \times \vec{b}$.

**Solution:**
Let the cross product $\vec{A} = \vec{a} \times \vec{b}$. Since $\vec{a}, \vec{b}$ are constant, $\vec{A}$ is a constant vector.
The scalar triple product is a dot product:
$$
[\vec{r}\ \vec{a}\ \vec{b}] = \vec{r} \cdot (\vec{a} \times \vec{b}) = \vec{r} \cdot \vec{A}
$$
Let $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ and $\vec{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$.
$$
\vec{r} \cdot \vec{A} = A_1 x + A_2 y + A_3 z
$$
Differentiating:
$$
\nabla(\vec{r} \cdot \vec{A}) = \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right)(A_1 x + A_2 y + A_3 z)
$$
$$
= A_1\hat{i} + A_2\hat{j} + A_3\hat{k} = \vec{A} = \vec{a} \times \vec{b} \quad \text{(Proved)}
$$

### Problem 4: Gradient of $r^n$
**Question:** If $r^2 = x^2 + y^2 + z^2$, find $\text{grad } r^n$.

**Solution (Chain Rule Method):**
Differentiating $r^2 = x^2 + y^2 + z^2$ with respect to $x$:
$$
2r\frac{\partial r}{\partial x} = 2x \implies \frac{\partial r}{\partial x} = \frac{x}{r}
$$
Now apply the chain rule:
$$
\nabla r^n = \hat{i}\frac{\partial (r^n)}{\partial x} + \hat{j}\frac{\partial (r^n)}{\partial y} + \hat{k}\frac{\partial (r^n)}{\partial z} = \sum \hat{i}\left(n r^{n-1} \frac{\partial r}{\partial x}\right)
$$
$$
\nabla r^n = \sum \hat{i}\left(n r^{n-1} \frac{x}{r}\right) = n r^{n-2} \sum x\hat{i} = n r^{n-2}(x\hat{i} + y\hat{j} + z\hat{k}) = n r^{n-2}\vec{r}
$$

### Problem 5: Cross Product of Gradient of $f(r)$ and Position Vector
**Question:** If $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ and $|\vec{r}| = r$, prove that $\nabla f(r) \times \vec{r} = 0$.

**Solution:**
Differentiate $f(r)$ using the chain rule:
$$
\nabla f(r) = \sum \hat{i}\frac{\partial f(r)}{\partial x} = \sum \hat{i} f'(r)\frac{\partial r}{\partial x} = \sum \hat{i} f'(r)\frac{x}{r}
$$
$$
\nabla f(r) = \frac{f'(r)}{r} (x\hat{i} + y\hat{j} + z\hat{k}) = \frac{f'(r)}{r}\vec{r}
$$
Take the cross product with $\vec{r}$:
$$
\nabla f(r) \times \vec{r} = \left(\frac{f'(r)}{r}\vec{r}\right) \times \vec{r} = \frac{f'(r)}{r} (\vec{r} \times \vec{r})
$$
Since the cross product of any vector with itself is zero:
$$
\nabla f(r) \times \vec{r} = 0 \quad \text{(Proved)}
$$

---

## 4. Homework Problems

1. If $\phi = 3x^2y - y^3z^2$, find $\text{grad }\phi$ at the point $(1, -2, -1)$.
   **Answer:** $-12\hat{i} - 9\hat{j} - 16\hat{k}$
2. If $f = x^3 + y^3 + 3xyz$, find $\text{grad } f$.
   **Answer:** $3(x^2 + yz)\hat{i} + 3(y^2 + zx)\hat{j} + 3(z^2 + xy)\hat{k}$
3. If $\vec{a} = 2x^2\hat{i} - 3yz\hat{j} + xz^2\hat{k}$ and $\phi = 2z^2 - x^3y$, find $\vec{a} \times \nabla\phi$ at the point $(1, -1, 1)$.
   **Answer:** $13\hat{i} - 5\hat{j} - 11\hat{k}$
4. If $r^2 = x^2 + y^2 + z^2$, find $\text{grad } r$.
   **Answer:** $\hat{r}$ (or $\frac{\vec{r}}{r}$)
5. Evaluate $\text{grad } e^{r^2}$, where $r^2 = x^2 + y^2 + z^2$.
   **Answer:** $2e^{r^2}\vec{r}$

---

## What Comes Next
We now know that $\nabla\phi$ gives the normal vector. We can project this normal vector onto any specific direction. In the next lecture, we will study the **Directional Derivative**, which tells us the rate of change of a scalar field in a specific chosen direction.

---

**Navigation**
[< Previous Lecture](02_Vector_Differentiation.md) | [Index](README.md) | [Next Lecture >](04_Directional_Derivative.md)
