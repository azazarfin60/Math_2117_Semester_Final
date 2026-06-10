# Topic 07: Irrotational and Conservative Fields

This file contains the organized questions and answers for **Irrotational and Conservative Fields**, priority ranked as **Priority 7** based on frequency and exam weight.

---

## Q1. Find the constants $a, b, c$ so that $\bar{V} = (x + 2y + az)\hat{i} + (bx - 3y - z)\hat{j} + (4x + cy + 2z)\hat{k}$ is irrotational. (03)

| | |
|---|---|
| **ID** | PYQ-2018-1b |
| **Source** | 2018 Q1(b) [03 marks] |

**Answer:**

A vector field $\bar{V}$ is irrotational if its curl is zero:

$$
\bar{\nabla} \times \bar{V} = 0
$$

We set up the curl calculation:

$$
\bar{\nabla} \times \bar{V} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
x + 2y + az & bx - 3y - z & 4x + cy + 2z
\end{vmatrix} = 0
$$

Expand the determinant:

$$
\bar{\nabla} \times \bar{V} = \hat{i}\left( \frac{\partial}{\partial y}(4x + cy + 2z) - \frac{\partial}{\partial z}(bx - 3y - z) \right) - \hat{j}\left( \frac{\partial}{\partial x}(4x + cy + 2z) - \frac{\partial}{\partial z}(x + 2y + az) \right) + \hat{k}\left( \frac{\partial}{\partial x}(bx - 3y - z) - \frac{\partial}{\partial y}(x + 2y + az) \right) = 0
$$

Calculate the derivatives:

$$
\bar{\nabla} \times \bar{V} = \hat{i}(c - (-1)) - \hat{j}(4 - a) + \hat{k}(b - 2) = 0
$$

This gives the system:

$$
c + 1 = 0 \implies c = -1
$$

$$
4 - a = 0 \implies a = 4
$$

$$
b - 2 = 0 \implies b = 2
$$

So the constants are $a = 4$, $b = 2$, and $c = -1$.

---

## Q2. Prove that $\bar{F} = (y^2 \cos x + z^3)\hat{i} + (2y \sin x - 4)\hat{j} + (3xz^2 + 2)\hat{k}$ represents a conservative force field. Also find the scalar potential for $\bar{F}$. (06)

| | |
|---|---|
| **ID** | PYQ-2018-2a |
| **Source** | 2018 Q2(a) [06 marks] |

**Answer:**

#### 1. Prove Conservative

The force field is conservative if its curl is zero:

$$
\bar{\nabla} \times \bar{F} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
y^2 \cos x + z^3 & 2y \sin x - 4 & 3xz^2 + 2
\end{vmatrix}
$$

Calculate the components:
*   $\hat{i}$-component:

$$
\frac{\partial}{\partial y}(3xz^2 + 2) - \frac{\partial}{\partial z}(2y \sin x - 4) = 0 - 0 = 0
$$

*   $\hat{j}$-component:

$$
\frac{\partial}{\partial z}(y^2 \cos x + z^3) - \frac{\partial}{\partial x}(3xz^2 + 2) = 3z^2 - 3z^2 = 0
$$

*   $\hat{k}$-component:

$$
\frac{\partial}{\partial x}(2y \sin x - 4) - \frac{\partial}{\partial y}(y^2 \cos x + z^3) = 2y \cos x - 2y \cos x = 0
$$

Since the curl is the zero vector, the force field is conservative.

#### 2. Find Scalar Potential

We solve the relation $\bar{F} = \bar{\nabla}\phi$:

$$
\frac{\partial\phi}{\partial x} = y^2 \cos x + z^3 \quad \dots \text{(1)}
$$

$$
\frac{\partial\phi}{\partial y} = 2y \sin x - 4 \quad \dots \text{(2)}
$$

$$
\frac{\partial\phi}{\partial z} = 3xz^2 + 2 \quad \dots \text{(3)}
$$

Integrate equation (1) with respect to $x$:

$$
\phi = y^2 \sin x + xz^3 + g(y, z) \quad \dots \text{(4)}
$$

Differentiate equation (4) with respect to $y$ and equate it to equation (2):

$$
\frac{\partial\phi}{\partial y} = 2y \sin x + \frac{\partial g}{\partial y} = 2y \sin x - 4 \implies \frac{\partial g}{\partial y} = -4
$$

Integrate with respect to $y$:

$$
g(y, z) = -4y + h(z)
$$

Substitute this back into equation (4):

$$
\phi = y^2 \sin x + xz^3 - 4y + h(z) \quad \dots \text{(5)}
$$

Now differentiate equation (5) with respect to $z$ and equate it to equation (3):

$$
\frac{\partial\phi}{\partial z} = 3xz^2 + h'(z) = 3xz^2 + 2 \implies h'(z) = 2
$$

Integrate with respect to $z$:

$$
h(z) = 2z + C
$$

Substitute this back into equation (5) to get the final potential function:

$$
\phi(x, y, z) = y^2 \sin x + xz^3 - 4y + 2z + C
$$

---

## Q3. If $\bar{F}$ represents a conservative force field then show that $\nabla \times \bar{F} = 0$. (04)

| | |
|---|---|
| **ID** | PYQ-2019-3c |
| **Source** | 2019 Q3(c) [04 marks] |

**Answer:**

A force field $\vec{F}$ is conservative if the work done in moving a particle between two points is independent of the path. This implies that there exists a scalar potential function $\phi$ such that:

$$
\vec{F} = \vec{\nabla}\phi
$$

We calculate the curl of the field:

$$
\vec{\nabla} \times \vec{F} = \vec{\nabla} \times (\vec{\nabla}\phi)
$$

Writing this in determinant form:

$$
\vec{\nabla} \times \vec{F} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
\frac{\partial\phi}{\partial x} & \frac{\partial\phi}{\partial y} & \frac{\partial\phi}{\partial z}
\end{vmatrix}
$$

$$
= \hat{i}\left( \frac{\partial^2\phi}{\partial y \partial z} - \frac{\partial^2\phi}{\partial z \partial y} \right) - \hat{j}\left( \frac{\partial^2\phi}{\partial x \partial z} - \frac{\partial^2\phi}{\partial z \partial x} \right) + \hat{k}\left( \frac{\partial^2\phi}{\partial x \partial y} - \frac{\partial^2\phi}{\partial y \partial x} \right)
$$

Assuming the second-order partial derivatives of $\phi$ are continuous, mixed partial derivatives are equal:

$$
\frac{\partial^2\phi}{\partial y \partial z} = \frac{\partial^2\phi}{\partial z \partial y}, \quad \frac{\partial^2\phi}{\partial x \partial z} = \frac{\partial^2\phi}{\partial z \partial x}, \quad \frac{\partial^2\phi}{\partial x \partial y} = \frac{\partial^2\phi}{\partial y \partial x}
$$

So we get:

$$
\vec{\nabla} \times \vec{F} = 0\hat{i} - 0\hat{j} + 0\hat{k} = \vec{0}
$$

This completes the proof.

---

## Q4. Show that, $\bar{A} = (6xy + z^3)\hat{i} + (3x^2 - z)\hat{j} + (3xz^2 - y)\hat{k}$ is irrotational. Find $\Phi$ such that $\bar{A} = \nabla\Phi$. (06)

| | |
|---|---|
| **ID** | PYQ-2020-3a |
| **Source** | 2020 Q3(a) [06 marks] |

**Answer:**

#### 1. Prove Irrotational

The field is irrotational if its curl is zero:

$$
\bar{\nabla} \times \bar{A} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
6xy + z^3 & 3x^2 - z & 3xz^2 - y
\end{vmatrix}
$$

Calculate the components:
*   $\hat{i}$-component:

$$
\frac{\partial}{\partial y}(3xz^2 - y) - \frac{\partial}{\partial z}(3x^2 - z) = -1 - (-1) = 0
$$

*   $\hat{j}$-component:

$$
\frac{\partial}{\partial z}(6xy + z^3) - \frac{\partial}{\partial x}(3xz^2 - y) = 3z^2 - 3z^2 = 0
$$

*   $\hat{k}$-component:

$$
\frac{\partial}{\partial x}(3x^2 - z) - \frac{\partial}{\partial y}(6xy + z^3) = 6x - 6x = 0
$$

The curl is the zero vector, so the field is irrotational.

#### 2. Find Potential Function

We solve the relation $\bar{A} = \bar{\nabla}\Phi$:

$$
\frac{\partial\Phi}{\partial x} = 6xy + z^3 \implies \Phi = 3x^2y + xz^3 + g(y, z) \quad \dots \text{(1)}
$$

Differentiate equation (1) with respect to $y$:

$$
\frac{\partial\Phi}{\partial y} = 3x^2 + \frac{\partial g}{\partial y} = 3x^2 - z \implies \frac{\partial g}{\partial y} = -z
$$

Integrate with respect to $y$:

$$
g(y, z) = -yz + h(z)
$$

Substitute this back into equation (1):

$$
\Phi = 3x^2y + xz^3 - yz + h(z) \quad \dots \text{(2)}
$$

Differentiate equation (2) with respect to $z$:

$$
\frac{\partial\Phi}{\partial z} = 3xz^2 - y + h'(z) = 3xz^2 - y \implies h'(z) = 0 \implies h(z) = C
$$

So the scalar potential is:

$$
\Phi = 3x^2y + xz^3 - yz + C
$$

---

## Q5. Show that $\vec{F} = (y^2 + 2xz^2)\hat{i} + (2xy - z)\hat{j} + (2x^2z - y + 2z)\hat{k}$ is irrotational vector and hence find corresponding scalar potential. (05)

| | |
|---|---|
| **ID** | PYQ-2021-2b |
| **Source** | 2021 Q2(b) [05 marks] |

**Answer:**

#### 1. Show Irrotational

A vector field $\vec{F}$ is irrotational if its curl is zero:

$$
\vec{\nabla} \times \vec{F} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
y^2 + 2xz^2 & 2xy - z & 2x^2z - y + 2z
\end{vmatrix}
$$

Calculate the components of the curl:
*   $\hat{i}$-component:

$$
\frac{\partial}{\partial y}(2x^2z - y + 2z) - \frac{\partial}{\partial z}(2xy - z) = -1 - (-1) = 0
$$

*   $\hat{j}$-component:

$$
\frac{\partial}{\partial z}(y^2 + 2xz^2) - \frac{\partial}{\partial x}(2x^2z - y + 2z) = 4xz - 4xz = 0
$$

*   $\hat{k}$-component:

$$
\frac{\partial}{\partial x}(2xy - z) - \frac{\partial}{\partial y}(y^2 + 2xz^2) = 2y - 2y = 0
$$

The curl is the zero vector, so the field is irrotational.

#### 2. Find Potential Function

We solve the relation $\vec{\nabla}\Phi = \vec{F}$:

$$
\frac{\partial\Phi}{\partial x} = y^2 + 2xz^2 \implies \Phi = xy^2 + x^2z^2 + g(y, z) \quad \dots \text{(1)}
$$

Differentiate equation (1) with respect to $y$:

$$
\frac{\partial\Phi}{\partial y} = 2xy + \frac{\partial g}{\partial y} = 2xy - z \implies \frac{\partial g}{\partial y} = -z
$$

Integrate with respect to $y$:

$$
g(y, z) = -yz + h(z)
$$

Substitute this back into equation (1):

$$
\Phi = xy^2 + x^2z^2 - yz + h(z) \quad \dots \text{(2)}
$$

Differentiate equation (2) with respect to $z$:

$$
\frac{\partial\Phi}{\partial z} = 2x^2z - y + h'(z) = 2x^2z - y + 2z \implies h'(z) = 2z \implies h(z) = z^2 + C
$$

So the scalar potential is:

$$
\Phi = xy^2 + x^2z^2 - yz + z^2 + C
$$

---

## Q6. Find constants $a, b, c$ so that $\vec{F} = (x + 2y + az)\hat{i} + (bx - 3y - z)\hat{j} + (4x + cy + 2z)\hat{k}$ is a conservative force field. Also obtain the scalar potential. (03+06)

| | |
|---|---|
| **ID** | CT2V-1 |
| **Source** | CT2V Q1 [03+06 marks] |

**Answer:**

#### 1. Find Constants $a, b, c$
A vector field $\vec{F}$ is conservative if its curl is zero:

$$
\vec{\nabla} \times \vec{F} = 0
$$

We calculate the curl of $\vec{F}$:

$$
\vec{\nabla} \times \vec{F} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
x + 2y + az & bx - 3y - z & 4x + cy + 2z
\end{vmatrix} = 0
$$

Let us expand this determinant:

$$
\vec{\nabla} \times \vec{F} = \hat{i}\left[ \frac{\partial}{\partial y}(4x + cy + 2z) - \frac{\partial}{\partial z}(bx - 3y - z) \right] - \hat{j}\left[ \frac{\partial}{\partial x}(4x + cy + 2z) - \frac{\partial}{\partial z}(x + 2y + az) \right] + \hat{k}\left[ \frac{\partial}{\partial x}(bx - 3y - z) - \frac{\partial}{\partial y}(x + 2y + az) \right] = 0
$$

We calculate the partial derivatives:

$$
\vec{\nabla} \times \vec{F} = \hat{i}(c - (-1)) - \hat{j}(4 - a) + \hat{k}(b - 2) = 0
$$

$$
\vec{\nabla} \times \vec{F} = \hat{i}(c + 1) + \hat{j}(a - 4) + \hat{k}(b - 2) = 0
$$

We equate the components to zero:

$$
c + 1 = 0 \implies c = -1
$$

$$
a - 4 = 0 \implies a = 4
$$

$$
b - 2 = 0 \implies b = 2
$$

So, the constants are $a = 4$, $b = 2$, and $c = -1$.

#### 2. Find Scalar Potential
We substitute $a$, $b$, and $c$ back into $\vec{F}$:

$$
\vec{F} = (x + 2y + 4z)\hat{i} + (2x - 3y - z)\hat{j} + (4x - y + 2z)\hat{k}
$$

Let $\phi$ be the scalar potential such that $\vec{F} = \vec{\nabla}\phi$. This gives three partial differential equations:

$$
\frac{\partial\phi}{\partial x} = x + 2y + 4z \quad \dots \text{(1)}
$$

$$
\frac{\partial\phi}{\partial y} = 2x - 3y - z \quad \dots \text{(2)}
$$

$$
\frac{\partial\phi}{\partial z} = 4x - y + 2z \quad \dots \text{(3)}
$$

We integrate equation (1) with respect to $x$:

$$
\phi = \frac{1}{2}x^2 + 2xy + 4xz + g(y, z) \quad \dots \text{(4)}
$$

Here, $g(y, z)$ is an arbitrary integration function.

Now we differentiate equation (4) with respect to $y$. We equate it to equation (2):

$$
\frac{\partial\phi}{\partial y} = 2x + \frac{\partial g}{\partial y} = 2x - 3y - z
$$

$$
\frac{\partial g}{\partial y} = -3y - z
$$

We integrate this with respect to $y$:

$$
g(y, z) = -\frac{3}{2}y^2 - yz + h(z)
$$

Here, $h(z)$ is an arbitrary integration function.

We substitute $g(y, z)$ back into equation (4):

$$
\phi = \frac{1}{2}x^2 + 2xy + 4xz - \frac{3}{2}y^2 - yz + h(z) \quad \dots \text{(5)}
$$

Now we differentiate equation (5) with respect to $z$. We equate it to equation (3):

$$
\frac{\partial\phi}{\partial z} = 4x - y + h'(z) = 4x - y + 2z
$$

$$
h'(z) = 2z
$$

We integrate this with respect to $z$:

$$
h(z) = z^2 + C
$$

Here, $C$ is a constant.

We substitute $h(z)$ back into equation (5) to get the final potential:

$$
\phi = \frac{1}{2}x^2 - \frac{3}{2}y^2 + z^2 + 2xy + 4xz - yz + C
$$

---

