# Lecture 05: Vector Calculus - Concept of Curl and Divergence

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 05 of 14
> **Video**: https://www.youtube.com/watch?v=Zdd8Tf5tkvM

---

**Navigation**
[< Previous Lecture](04_Directional_Derivative.md) | [Index](README.md) | [Next Lecture >](06_Line_Integration.md)

---

## Prerequisites
We have seen that applying the Del operator ($\nabla$) to a scalar function produces the gradient (a vector). In this lecture, we apply the Del operator to a **vector point function**

$$
\vec{F}(x, y, z) = F_1\hat{i} + F_2\hat{j} + F_3\hat{k}.
$$

. Because it is a vector operator acting on a vector function, we can do this in two ways: via a dot product (Divergence) or a cross product (Curl).

---

## Divergence of a Vector

The **divergence** of a vector field $\vec{F}$ is defined as the dot product of the Del operator and $\vec{F}$. It is written as $\text{div }\vec{F}$ or $\nabla \cdot \vec{F}$.

$$
\text{div }\vec{F} = \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right) \cdot (F_1\hat{i} + F_2\hat{j} + F_3\hat{k})
$$

$$
\text{div }\vec{F} = \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial y} + \frac{\partial F_3}{\partial z}
$$

Because it is a dot product, the divergence is a **scalar quantity**. Physically, it represents the net flux per unit volume emitting from a point (e.g., heat radiating from a source, or fluid expanding outward).

### Solenoidal Vectors
If the divergence of a vector field is zero everywhere ($\nabla \cdot \vec{F} = 0$), the vector is called **solenoidal**. This means there is no net expansion or compression. It behaves like an incompressible fluid with no sources or sinks.

---

## Curl of a Vector

The **curl** of a vector field $\vec{F}$ is defined as the cross product of the Del operator and $\vec{F}$. It is written as $\text{curl }\vec{F}$ or $\nabla \times \vec{F}$.

We compute this using the standard cross product determinant:

$$
\text{curl }\vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_1 & F_2 & F_3 \end{vmatrix}
$$

Expanding this gives:

$$
\text{curl }\vec{F} = \hat{i}\left( \frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z} \right) - \hat{j}\left( \frac{\partial F_3}{\partial x} - \frac{\partial F_1}{\partial z} \right) + \hat{k}\left( \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} \right)
$$

Because it is a cross product, the curl is a **vector quantity**. Physically, it measures the rotational tendency or "spin" of the vector field at a point (like a vortex or whirlpool).

### Irrotational Vectors
If the curl of a vector field is the zero vector everywhere ($\nabla \times \vec{F} = \vec{0}$), the vector is called **irrotational**. This means the field has absolutely no rotational flow or twisting motion.

---

## Important Vector Identities
There are two critical identities involving these operations:
1.  **Divergence of Curl is Zero**: The divergence of the curl of any vector field is always exactly zero. 

$$
    \text{div }(\text{curl }\vec{F}) = \nabla \cdot (\nabla \times \vec{F}) = 0
$$

2.  **Curl of Gradient is Zero**: The curl of the gradient of any scalar field is always the zero vector.

$$
    \text{curl }(\text{grad }\phi) = \nabla \times (\nabla \phi) = \vec{0}
$$

---

## Solved Problems

### Problem 1: Solenoidal Condition
**Question:** Determine $a$ such that the vector

$$
\vec{F} = (x + 3y)\hat{i} + (y - 2z)\hat{j} + (x - az)\hat{k}
$$

is solenoidal.

**Solution:**
Since the vector is solenoidal, $\nabla \cdot \vec{F} = 0$.

$$
\frac{\partial}{\partial x}(x + 3y) + \frac{\partial}{\partial y}(y - 2z) + \frac{\partial}{\partial z}(x - az) = 0
$$

$$
1 + 1 - a = 0 \implies a = 2
$$

### Problem 2: Divergence at a Point
**Question:** If

$$
\vec{F} = xy\sin z\hat{i} + y^2\sin x\hat{j} + z^2\sin xy\hat{k},
$$

Find $\text{div }\vec{F}$ at the point $(0, \pi/2, \pi/2)$.

**Solution:**
First, compute the divergence:

$$
\text{div }\vec{F} = \frac{\partial}{\partial x}(xy\sin z) + \frac{\partial}{\partial y}(y^2\sin x) + \frac{\partial}{\partial z}(z^2\sin xy)
$$

$$
\text{div }\vec{F} = y\sin z + 2y\sin x + 2z\sin xy
$$

Substitute $x = 0, y = \pi/2, z = \pi/2$:

$$
\text{div }\vec{F} = \left(\frac{\pi}{2}\right)\sin\left(\frac{\pi}{2}\right) + 2\left(\frac{\pi}{2}\right)\sin(0) + 2\left(\frac{\pi}{2}\right)\sin(0)
$$

$$
\text{div }\vec{F} = \frac{\pi}{2}(1) + 0 + 0 = \frac{\pi}{2}
$$

### Problem 3: Properties of Position Vector
**Question:** If

$$
\vec{r} = x\hat{i} + y\hat{j} + z\hat{k},
$$

Prove that $\text{div }\vec{r} = 3$ and $\text{curl }\vec{r} = \vec{0}$.

**Solution:**
For divergence:

$$
\nabla \cdot \vec{r} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(y) + \frac{\partial}{\partial z}(z) = 1 + 1 + 1 = 3
$$

For curl:

$$
\nabla \times \vec{r} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ x & y & z \end{vmatrix}
$$

Evaluating the determinant gives

$$
\hat{i}(0-0) - \hat{j}(0-0) + \hat{k}(0-0) = \vec{0}.
$$

. Both properties are proven.

### Problem 4: Evaluating Irrotational Flow
**Question:** Show that

$$
\vec{F} = (\sin y + z)\hat{i} + (x\cos y - z)\hat{j} + (x - y)\hat{k}
$$

is irrotational.

**Solution:**
Compute the curl:

$$
\nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ \sin y + z & x\cos y - z & x - y \end{vmatrix}
$$

Evaluate the $\hat{i}$ component:

$$
\frac{\partial}{\partial y}(x - y) - \frac{\partial}{\partial z}(x\cos y - z) = -1 - (-1) = 0
$$

Evaluate the $\hat{j}$ component:

$$
\frac{\partial}{\partial z}(\sin y + z) - \frac{\partial}{\partial x}(x - y) = 1 - 1 = 0
$$

Evaluate the $\hat{k}$ component:

$$
\frac{\partial}{\partial x}(x\cos y - z) - \frac{\partial}{\partial y}(\sin y + z) = \cos y - \cos y = 0
$$

Since

$$
\nabla \times \vec{F} = 0\hat{i} + 0\hat{j} + 0\hat{k} = \vec{0},
$$

The vector is irrotational.

### Problem 5: Curl of a Cross Product Identity
**Question:** If $\vec{a}$ is a constant vector and $\vec{r}$ is the position vector, prove that $\text{curl }(\vec{r} \times \vec{a}) = -2\vec{a}$.

**Solution:**
Use the vector identity:

$$
\nabla \times (\vec{A} \times \vec{B}) = \vec{A}(\nabla \cdot \vec{B}) - \vec{B}(\nabla \cdot \vec{A}) + (\vec{B} \cdot \nabla)\vec{A} - (\vec{A} \cdot \nabla)\vec{B}
$$

Let $\vec{A} = \vec{r}$ and $\vec{B} = \vec{a}$. 
Since $\vec{a}$ is constant, $\nabla \cdot \vec{a} = 0$ and $(\vec{r} \cdot \nabla)\vec{a} = \vec{0}$.
From earlier problems, we know $\nabla \cdot \vec{r} = 3$.
Finally, applying $(\vec{a} \cdot \nabla)$ to $\vec{r}$ yields $\vec{a}$.
Substitute these into the identity:

$$
\text{curl }(\vec{r} \times \vec{a}) = \vec{r}(0) - \vec{a}(3) + \vec{a} - \vec{0} = -3\vec{a} + \vec{a} = -2\vec{a}
$$

### Problem 6: Operations on
**Question:** Prove that $\text{div}(r^n \vec{r}) = (n + 3)r^n$. For what value of $n$ is it solenoidal?

**Solution:**
First, note that $\frac{\partial r}{\partial x} = \frac{x}{r}$, and similarly for $y$ and $z$.
Compute the divergence:

$$
\nabla \cdot (r^n x\hat{i} + r^n y\hat{j} + r^n z\hat{k}) = \frac{\partial}{\partial x}(r^n x) + \frac{\partial}{\partial y}(r^n y) + \frac{\partial}{\partial z}(r^n z)
$$

Apply the product rule to the $x$ term:

$$
\frac{\partial}{\partial x}(r^n x) = r^n(1) + x\left(nr^{n-1}\frac{\partial r}{\partial x}\right) = r^n + n x r^{n-1}\left(\frac{x}{r}\right) = r^n + n x^2 r^{n-2}
$$

Summing the terms for $x, y, z$:

$$
\text{div}(r^n \vec{r}) = 3r^n + n r^{n-2}(x^2 + y^2 + z^2)
$$

Since $x^2 + y^2 + z^2 = r^2$:

$$
\text{div}(r^n \vec{r}) = 3r^n + n r^{n-2}(r^2) = 3r^n + n r^n = (n + 3)r^n
$$

For the vector to be solenoidal, the divergence must be zero:

$$
(n + 3)r^n = 0 \implies n = -3
$$

---

## Key Takeaways
*   **Divergence ($\nabla \cdot \vec{F}$)** is a dot product that measures the outward flux or expansion of a vector field (scalar output).
*   **Curl ($\nabla \times \vec{F}$)** is a cross product that measures the rotation or spin of a vector field (vector output).
*   A field with zero divergence is **solenoidal**; a field with zero curl is **irrotational**.

## What Comes Next
We have completed our study of vector differential operators (Gradient, Divergence, and Curl). The next major topic in vector calculus is **Vector Integration**, starting with Line Integrals and calculating work done by a force.

---

**Navigation**
[< Previous Lecture](04_Directional_Derivative.md) | [Index](README.md) | [Next Lecture >](06_Line_Integration.md)
