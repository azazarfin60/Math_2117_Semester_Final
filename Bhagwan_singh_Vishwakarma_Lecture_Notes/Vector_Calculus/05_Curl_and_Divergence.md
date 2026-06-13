# Lecture 05: Concept of Curl and Divergence

> **Series**: Vector Calculus
> **Lecture**: 05 of 14
> **Video**: https://www.youtube.com/watch?v=Zdd8Tf5tkvM

---

**Navigation**
[< Previous Lecture](04_Directional_Derivative.md) | [Index](README.md) | [Next Lecture >](06_Line_Integration.md)

---

## Prerequisites
We have seen that applying the Del operator ($\nabla$) to a scalar function produces the gradient (a vector). In this lecture, we apply the Del operator to a **vector point function** $\vec{F}(x, y, z) = F_1\hat{i} + F_2\hat{j} + F_3\hat{k}$. Because it is a vector operator acting on a vector function, we can do this in two ways: via a dot product (Divergence) or a cross product (Curl).

---

## 1. Divergence of a Vector

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

## 2. Curl of a Vector

The **curl** of a vector field $\vec{F}$ is defined as the cross product of the Del operator and $\vec{F}$. It is written as $\text{curl }\vec{F}$ or $\nabla \times \vec{F}$. We compute this using the standard cross product determinant:
$$
\text{curl }\vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_1 & F_2 & F_3 \end{vmatrix}
$$
Expanding this gives:
$$
\text{curl }\vec{F} = \hat{i}\left( \frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z} \right) + \hat{j}\left( \frac{\partial F_1}{\partial z} - \frac{\partial F_3}{\partial x} \right) + \hat{k}\left( \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} \right)
$$

Because it is a cross product, the curl is a **vector quantity**. Physically, it measures the rotational tendency or "spin" of the vector field at a point (like a vortex or whirlpool).

### Irrotational Vectors
If the curl of a vector field is the zero vector everywhere, i.e., $\nabla \times \vec{F} = \vec{0}$, the vector is called **irrotational**. This means the field has absolutely no rotational flow or twisting motion.

---

## 3. Important Vector Identities

### Identity 1: Divergence of Curl is Zero
The divergence of the curl of any vector field is always exactly zero:
$$
\text{div }(\text{curl }\vec{F}) = \nabla \cdot (\nabla \times \vec{F}) = 0
$$
*Proof Outline*: Evaluating $\nabla \cdot (\nabla \times \vec{F})$ produces mixed partial derivatives like $\frac{\partial^2 F_3}{\partial x \partial y} - \frac{\partial^2 F_3}{\partial y \partial x}$. Assuming continuity, these mixed partials are equal and cancel out in pairs, resulting in exactly $0$.

### Identity 2: Curl of Curl
The curl of the curl is related to the gradient of divergence and the Laplacian:
$$
\text{curl }(\text{curl }\vec{F}) = \text{grad }(\text{div }\vec{F}) - \nabla^2\vec{F}
$$

---

## 4. Solved Problems

### Problem 1: Solenoidal Condition
**Question:** Determine $a$ such that the vector $\vec{F} = (x + 3y)\hat{i} + (y - 2z)\hat{j} + (x + az)\hat{k}$ is solenoidal.

**Solution:**
Since the vector is solenoidal, $\nabla \cdot \vec{F} = 0$.
$$
\frac{\partial}{\partial x}(x + 3y) + \frac{\partial}{\partial y}(y - 2z) + \frac{\partial}{\partial z}(x + az) = 0
$$
$$
1 + 1 + a = 0 \implies a = -2
$$

### Problem 2: Divergence at a Point
**Question:** If $\vec{F} = xy\sin z\hat{i} + y^2\sin x\hat{j} + z^2\sin xy\hat{k}$, find $\text{div }\vec{F}$ at $(0, \pi/2, \pi/2)$.

**Solution:**
$$
\text{div }\vec{F} = \frac{\partial}{\partial x}(xy\sin z) + \frac{\partial}{\partial y}(y^2\sin x) + \frac{\partial}{\partial z}(z^2\sin xy)
$$
$$
\text{div }\vec{F} = y\sin z + 2y\sin x + 2z\sin xy
$$
Evaluate at $x = 0, y = \pi/2, z = \pi/2$:
$$
\text{div }\vec{F} = \left(\frac{\pi}{2}\right)\sin\left(\frac{\pi}{2}\right) + 2\left(\frac{\pi}{2}\right)\sin(0) + 2\left(\frac{\pi}{2}\right)\sin(0) = \frac{\pi}{2}(1) + 0 + 0 = \frac{\pi}{2}
$$

### Problem 3: Properties of Position Vector
**Question:** If $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$, prove that $\text{div }\vec{r} = 3$ and $\text{curl }\vec{r} = \vec{0}$.

**Solution:**
For divergence:
$$
\nabla \cdot \vec{r} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(y) + \frac{\partial}{\partial z}(z) = 1 + 1 + 1 = 3
$$
For curl:
$$
\nabla \times \vec{r} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ x & y & z \end{vmatrix} = \hat{i}(0-0) + \hat{j}(0-0) + \hat{k}(0-0) = \vec{0}
$$

### Problem 4: Finding Divergence and Curl
**Question:** Find the divergence and curl of $\vec{F} = (x^2 - y^2)\hat{i} + 2xy\hat{j} + (y^2 - xy)\hat{k}$.

**Solution:**
**Divergence:**
$$
\text{div }\vec{F} = \frac{\partial}{\partial x}(x^2 - y^2) + \frac{\partial}{\partial y}(2xy) + \frac{\partial}{\partial z}(y^2 - xy) = 2x + 2x + 0 = 4x
$$
**Curl:**
$$
\text{curl }\vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ x^2 - y^2 & 2xy & y^2 - xy \end{vmatrix}
$$
$$
= \hat{i}(2y - 0) + \hat{j}(0 - (-y)) + \hat{k}(2y - (-2y)) = (2y - x)\hat{i} + y\hat{j} + 4y\hat{k}
$$

### Problem 5: Curl of Exponential Field
**Question:** If $\vec{V} = e^{xyz}(\hat{i} + \hat{j} + \hat{k})$, find $\text{curl }\vec{V}$.

**Solution:**
$$
\text{curl }\vec{V} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ e^{xyz} & e^{xyz} & e^{xyz} \end{vmatrix}
$$
Evaluate the $\hat{i}$ component:
$$
\frac{\partial}{\partial y}(e^{xyz}) - \frac{\partial}{\partial z}(e^{xyz}) = xz e^{xyz} - xy e^{xyz} = x(z-y)e^{xyz}
$$
Similarly for $\hat{j}$ and $\hat{k}$:
$$
\text{curl }\vec{V} = e^{xyz} [ x(z - y)\hat{i} + y(x - z)\hat{j} + z(y - x)\hat{k} ]
$$

### Problem 6: Evaluating Irrotational Flow
**Question:** Show that $\vec{F} = (\sin y + z)\hat{i} + (x\cos y - z)\hat{j} + (x - y)\hat{k}$ is irrotational.

**Solution:**
Compute the curl:
$$
\nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ \sin y + z & x\cos y - z & x - y \end{vmatrix}
$$
$$
= \hat{i}(-1 - (-1)) + \hat{j}(1 - 1) + \hat{k}(\cos y - \cos y) = \vec{0}
$$
Since $\nabla \times \vec{F} = \vec{0}$, the vector is irrotational.

### Problem 7: Curl of a Cross Product Identity
**Question:** If $\vec{a}$ is a constant vector and $\vec{r}$ is the position vector, prove that $\text{curl }(\vec{r} \times \vec{a}) = -2\vec{a}$.

**Solution:**
Use the vector identity $\nabla \times (\vec{A} \times \vec{B}) = \vec{A}(\nabla \cdot \vec{B}) - \vec{B}(\nabla \cdot \vec{A}) + (\vec{B} \cdot \nabla)\vec{A} - (\vec{A} \cdot \nabla)\vec{B}$.
Let $\vec{A} = \vec{r}$ and $\vec{B} = \vec{a}$. Since $\vec{a}$ is constant, $\nabla \cdot \vec{a} = 0$ and $(\vec{r} \cdot \nabla)\vec{a} = \vec{0}$.
From earlier, $\nabla \cdot \vec{r} = 3$ and $(\vec{a} \cdot \nabla)\vec{r} = \vec{a}$.
Substitute these into the identity:
$$
\text{curl }(\vec{r} \times \vec{a}) = \vec{r}(0) - \vec{a}(3) + \vec{a} - \vec{0} = -3\vec{a} + \vec{a} = -2\vec{a} \quad \text{(Proved)}
$$

### Problem 8: Operations on $r^n \vec{r}$
**Question:** Prove that $\text{div}(r^n \vec{r}) = (n + 3)r^n$ and $\text{curl}(r^n \vec{r}) = \vec{0}$. For what value of $n$ is it solenoidal?

**Solution:**
First, note $\frac{\partial r}{\partial x} = \frac{x}{r}$, similarly for $y$ and $z$.
**Divergence:**
$$
\nabla \cdot (r^n x\hat{i} + r^n y\hat{j} + r^n z\hat{k}) = \frac{\partial}{\partial x}(r^n x) + \frac{\partial}{\partial y}(r^n y) + \frac{\partial}{\partial z}(r^n z)
$$
Apply product rule:
$$
\frac{\partial}{\partial x}(r^n x) = r^n + x\left(nr^{n-1}\frac{x}{r}\right) = r^n + n x^2 r^{n-2}
$$
Summing $x, y, z$:
$$
\text{div}(r^n \vec{r}) = 3r^n + n r^{n-2}(x^2 + y^2 + z^2) = 3r^n + n r^{n-2}(r^2) = (n + 3)r^n
$$
For solenoidal, $\text{div} = 0 \implies (n + 3)r^n = 0 \implies n = -3$.

**Curl:**
$$
\text{curl}(r^n \vec{r}) = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ r^n x & r^n y & r^n z \end{vmatrix}
$$
$\hat{i}$ component: $\frac{\partial}{\partial y}(r^n z) - \frac{\partial}{\partial z}(r^n y) = z(nr^{n-1}\frac{y}{r}) - y(nr^{n-1}\frac{z}{r}) = nzyr^{n-2} - nyzr^{n-2} = 0$.
By symmetry, all components are $0$, so $\text{curl}(r^n \vec{r}) = \vec{0}$.

---

## What Comes Next
We have completed our study of vector differential operators (Gradient, Divergence, and Curl). The next major topic in vector calculus is **Vector Integration**, starting with Line Integrals and calculating work done by a force.

---

**Navigation**
[< Previous Lecture](04_Directional_Derivative.md) | [Index](README.md) | [Next Lecture >](06_Line_Integration.md)
