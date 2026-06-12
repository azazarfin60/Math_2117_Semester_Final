[← Previous: A09 Tangent Plane and Normal Line](A09_Tangent_Plane_Normal_Line.md) | [Index](00_Index.md) | [Next: A11 Irrotational and Conservative Fields →](A11_Irrotational_Conservative_Fields.md)

---

# A10: Divergence and Curl

> **Exam Weight**: Tier 1 | **Appeared in**: Core concept used in almost every vector calculus question.

While gradient operates on scalars, divergence and curl operate on vector fields. They describe the physical behavior of the field (expansion/compression and rotation).

---

## Divergence (Dot Product)

### Definition

The divergence of a vector field

$$
\vec{F} = F_1\hat{i} + F_2\hat{j} + F_3\hat{k}
$$

is the dot product of the Del operator and $\vec{F}$:

$$
\text{div }\vec{F} = \nabla \cdot \vec{F} = \left(\hat{i}\frac{\partial}{\partial x} + \hat{j}\frac{\partial}{\partial y} + \hat{k}\frac{\partial}{\partial z}\right) \cdot (F_1\hat{i} + F_2\hat{j} + F_3\hat{k})
$$

$$
\text{div }\vec{F} = \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial y} + \frac{\partial F_3}{\partial z}
$$

Input: Vector field. Output: **Scalar quantity**.

### Physical Significance

Divergence represents the net outward flux (flow) per unit volume from a point. 
- **Positive divergence**: The point is a source (fluid expanding outward).
- **Negative divergence**: The point is a sink (fluid compressing inward).

### Solenoidal Vector

If $\nabla \cdot \vec{F} = 0$ everywhere, the vector field is called **solenoidal**. It behaves like an incompressible fluid with no sources or sinks.

---

## Curl (Cross Product)

### Definition

The curl of a vector field $\vec{F}$ is the cross product of the Del operator and $\vec{F}$:

$$
\text{curl }\vec{F} = \nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_1 & F_2 & F_3 \end{vmatrix}
$$

Expanding this gives:

$$
\nabla \times \vec{F} = \hat{i}\left( \frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z} \right) - \hat{j}\left( \frac{\partial F_3}{\partial x} - \frac{\partial F_1}{\partial z} \right) + \hat{k}\left( \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} \right)
$$

Input: Vector field. Output: **Vector quantity**.

### Physical Significance

Curl measures the rotational tendency or "spin" of the vector field at a point (like a vortex or whirlpool). The direction of the curl vector is the axis of rotation, given by the right-hand rule.

### Irrotational Vector

If $\nabla \times \vec{F} = \vec{0}$ everywhere, the vector field is called **irrotational**. This means the field has absolutely no rotational flow or twisting motion.

---

## Properties of Position Vector

Let the position vector be

$$
\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}.
$$

Then $r = \lvert \vec{r} \rvert = \sqrt{x^2 + y^2 + z^2}$.

Two absolute must-know facts:

1. **Divergence of $\vec{r}$ is 3**:

$$
\nabla \cdot \vec{r} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 1 + 1 + 1 = 3
$$

2. **Curl of $\vec{r}$ is zero**:

$$
\nabla \times \vec{r} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ x & y & z \end{vmatrix} = \hat{i}(0) - \hat{j}(0) + \hat{k}(0) = \vec{0}
$$

---

## Worked Example 1: Solenoidal Condition

**Problem**: Determine $a$ such that the vector

$$
\vec{F} = (x + 3y)\hat{i} + (y - 2z)\hat{j} + (x - az)\hat{k}
$$

is solenoidal.

**Solution**:

For $\vec{F}$ to be solenoidal, $\nabla \cdot \vec{F} = 0$.

$$
\frac{\partial}{\partial x}(x + 3y) + \frac{\partial}{\partial y}(y - 2z) + \frac{\partial}{\partial z}(x - az) = 0
$$

$$
1 + 1 - a = 0 \implies a = 2
$$

---

## Worked Example 2: Evaluating Divergence

**Problem**: Prove that $\text{div}(r^n \vec{r}) = (n + 3)r^n$. For what value of $n$ is it solenoidal?

**Solution**:

We know $\frac{\partial r}{\partial x} = \frac{x}{r}$, and similarly for $y$ and $z$.

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

[← Previous: A09 Tangent Plane and Normal Line](A09_Tangent_Plane_Normal_Line.md) | [Index](00_Index.md) | [Next: A11 Irrotational and Conservative Fields →](A11_Irrotational_Conservative_Fields.md)
