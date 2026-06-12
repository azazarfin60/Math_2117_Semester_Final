# Lecture 03: Vector Calculus - Concept of Gradient and Geometric Meaning

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 03 of 14
> **Video**: https://www.youtube.com/watch?v=fqWikeRWBfk

---

**Navigation**
[< Previous Lecture](02_Vector_Differentiation.md) | [Index](README.md) | [Next Lecture >](04_Directional_Derivative.md)

---

## Prerequisites
We know that a scalar point function $\phi(x,y,z) = \text{Constant}$ defines a 3D surface. To study how these scalar fields change, we need a special operator that can take derivatives in all spatial directions at once.

---

## The Del Operator
In standard calculus, we use $\frac{d}{dx}$ to find derivatives. In vector calculus, we use the **Del Operator** (or Nabla), denoted by $\nabla$. It is a vector differential operator:

$$
\nabla = \hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}
$$

Because it contains the unit vectors $\hat{i}$, $\hat{j}$, and $\hat{k}$, it acts like a vector.
We apply this operator to functions to find their rates of change in 3D space.

## The Gradient
When we apply the del operator to a **scalar point function** $\phi$, we get the **gradient** of $\phi$. We write this as $\text{grad }\phi$ or $\nabla\phi$.

$$
\nabla\phi = \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right)\phi = \hat{i}\frac{\partial\phi}{\partial x} + \hat{j}\frac{\partial\phi}{\partial y} + \hat{k}\frac{\partial\phi}{\partial z}
$$

**Important**: The gradient of a scalar point function always results in a **vector quantity**. You input a scalar field, and you output a vector field.

### Geometric Meaning
What does this vector physically mean? The gradient $\nabla\phi$ is the **normal (perpendicular) vector** to the surface defined by $\phi(x,y,z) = c$ at any given point. If you draw a tangent plane to the surface at a point, the gradient vector points straight out of that plane at a exactly 90 degrees.

---

## Properties of Gradient
The gradient acts very much like a standard derivative. Let $f$ and $g$ be two scalar point functions, and $\vec{a}$ be a constant vector.

1.  **Sum/Difference Rule**:

$$
\nabla(f \pm g) = \nabla f \pm \nabla g
$$

2.  **Product Rule**:

$$
\nabla(fg) = f\nabla g + g\nabla f
$$

3.  **Quotient Rule**:

$$
\nabla\left(\frac{f}{g}\right) = \frac{g\nabla f - f\nabla g}{g^2}
$$

4.  **Operator on Position Vector**: If

$$
\vec{r} = x\hat{i} + y\hat{j} + z\hat{k},
$$

Then:

$$
(\vec{a} \cdot \nabla)\vec{r} = \vec{a}
$$

---

## Solved Problems

### Problem 1: Basic Gradient Calculation
**Question:** If $f = x^3 + y^3 + 3xy$, find $\text{grad } f$.

**Solution:**
Apply the del operator to the function:

$$
\text{grad } f = \hat{i}\frac{\partial}{\partial x}(x^3 + y^3 + 3xy) + \hat{j}\frac{\partial}{\partial y}(x^3 + y^3 + 3xy) + \hat{k}\frac{\partial}{\partial z}(x^3 + y^3 + 3xy)
$$

Differentiate each part:

$$
\text{grad } f = (3x^2 + 3y)\hat{i} + (3y^2 + 3x)\hat{j} + 0\hat{k}
$$

Simplify:

$$
\text{grad } f = 3(x^2 + y)\hat{i} + 3(y^2 + x)\hat{j}
$$

### Problem 2: Gradient Evaluation at a Point
**Question:** If $\phi(x,y,z) = 2x^2y^3 - 3y^2z^3$, find $\nabla\phi$ at the point $(1, -1, 1)$.

**Solution:**
First, calculate the partial derivatives:

$$
\frac{\partial\phi}{\partial x} = 4xy^3
$$

$$
\frac{\partial\phi}{\partial y} = 6x^2y^2 - 6yz^3
$$

$$
\frac{\partial\phi}{\partial z} = -9y^2z^2
$$

Combine to form the gradient vector:

$$
\nabla\phi = 4xy^3\hat{i} + (6x^2y^2 - 6yz^3)\hat{j} - 9y^2z^2\hat{k}
$$

Now, evaluate at $x=1$, $y=-1$, $z=1$:

$$
\left.\frac{\partial\phi}{\partial x}\right|_{(1,-1,1)} = 4(1)(-1)^3 = -4
$$

$$
\left.\frac{\partial\phi}{\partial y}\right|_{(1,-1,1)} = 6(1)^2(-1)^2 - 6(-1)(1)^3 = 6 + 6 = 12
$$

$$
\left.\frac{\partial\phi}{\partial z}\right|_{(1,-1,1)} = -9(-1)^2(1)^2 = -9
$$

The final vector is:

$$
\nabla\phi = -4\hat{i} + 12\hat{j} - 9\hat{k}
$$

### Problem 3: Gradient of a Scalar Triple Product
**Question:** If $\vec{a}$ and $\vec{b}$ are constant vectors, prove that $\nabla[\vec{r}\ \vec{a}\ \vec{b}] = \vec{a} \times \vec{b}$.

**Solution:**
Let the cross product $\vec{A} = \vec{a} \times \vec{b}$.
Since $\vec{a}$ and $\vec{b}$ are constant, $\vec{A}$ is also a constant vector.
The scalar triple product becomes a simple dot product:

$$
[\vec{r}\ \vec{a}\ \vec{b}] = \vec{r} \cdot (\vec{a} \times \vec{b}) = \vec{r} \cdot \vec{A}
$$

Let

$$
\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}
$$

 and

$$
\vec{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}.
$$

Expand the dot product:

$$
\vec{r} \cdot \vec{A} = A_1 x + A_2 y + A_3 z
$$

Now find the gradient of this scalar:

$$
\nabla(\vec{r} \cdot \vec{A}) = \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right)(A_1 x + A_2 y + A_3 z)
$$

$$
\nabla(\vec{r} \cdot \vec{A}) = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}
$$

This perfectly recreates vector $\vec{A}$. Therefore:

$$
\nabla(\vec{r} \cdot \vec{A}) = \vec{a} \times \vec{b}
$$

### Problem 4: Gradient of
**Question:** If $r^2 = x^2 + y^2 + z^2$, find $\text{grad } r^n$.

**Solution:**
First, note that differentiating $r^2 = x^2 + y^2 + z^2$ with respect to $x$ gives:

$$
2r\frac{\partial r}{\partial x} = 2x \implies \frac{\partial r}{\partial x} = \frac{x}{r}
$$

Now apply the chain rule to find the gradient of $r^n$:

$$
\nabla r^n = \hat{i}\frac{\partial (r^n)}{\partial x} + \hat{j}\frac{\partial (r^n)}{\partial y} + \hat{k}\frac{\partial (r^n)}{\partial z}
$$

Look at just the $x$ component:

$$
\hat{i}\left(n r^{n-1} \frac{\partial r}{\partial x}\right) = \hat{i}\left(n r^{n-1} \frac{x}{r}\right) = \hat{i}(n x r^{n-2})
$$

By symmetry, the $y$ and $z$ components will be similar. Adding them all up gives:

$$
\nabla r^n = n r^{n-2} (x\hat{i} + y\hat{j} + z\hat{k}) = n r^{n-2}\vec{r}
$$

---

## Key Takeaways
*   The del operator ($\nabla$) is a vector differential operator.
*   The gradient takes a scalar point function and outputs a vector field.
*   The gradient vector is geometrically normal (perpendicular) to the original scalar surface.

## What Comes Next
We now know that $\nabla\phi$ gives the normal vector. We can project this normal vector onto any specific direction. In the next lecture, we will study the **Directional Derivative**, which tells us the rate of change of a scalar field in a specific chosen direction.

---

**Navigation**
[< Previous Lecture](02_Vector_Differentiation.md) | [Index](README.md) | [Next Lecture >](04_Directional_Derivative.md)
