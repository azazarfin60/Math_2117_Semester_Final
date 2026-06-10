[⬅ CT-1 (Vector) Answer](CT1_Vector_answer.md) | [🏠 Index](00-index.md) | [CT-1 (Matrix) Answer ➡](CT1_Matrix_answer.md)

---

# CT 2 (Vector) Answers — ECE'23

---

### Q1. Find constants $a, b, c$ so that $\vec{F} = (x + 2y + az)\hat{i} + (bx - 3y - z)\hat{j} + (4x + cy + 2z)\hat{k}$ is a conservative force field. Also obtain the scalar potential. (03+06)

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

### Q2. Find the unit outward drawn normal to the surface $(x - 1)^2 + y^2 + (z + 2)^2 = 9$ at the point $(3, 1, -4)$. (05)

**Answer:**

Let the surface function be:

$$
f(x, y, z) = (x - 1)^2 + y^2 + (z + 2)^2 - 9
$$

The gradient of $f$ gives a vector normal to the surface. We calculate this gradient:

$$
\vec{\nabla}f = \frac{\partial f}{\partial x}\hat{i} + \frac{\partial f}{\partial y}\hat{j} + \frac{\partial f}{\partial z}\hat{k}
$$

$$
\vec{\nabla}f = 2(x - 1)\hat{i} + 2y\hat{j} + 2(z + 2)\hat{k}
$$

We evaluate the gradient at $(3, 1, -4)$:

$$
\vec{\nabla}f|_{(3, 1, -4)} = 2(3 - 1)\hat{i} + 2(1)\hat{j} + 2(-4 + 2)\hat{k}
$$

$$
\vec{\nabla}f|_{(3, 1, -4)} = 4\hat{i} + 2\hat{j} - 4\hat{k}
$$

Now we find the magnitude of this normal vector:

$$
|\vec{\nabla}f| = \sqrt{4^2 + 2^2 + (-4)^2} = \sqrt{16 + 4 + 16} = \sqrt{36} = 6
$$

We divide the normal vector by its magnitude. This gives the unit outward normal vector $\hat{n}$:

$$
\hat{n} = \frac{4\hat{i} + 2\hat{j} - 4\hat{k}}{6} = \frac{2}{3}\hat{i} + \frac{1}{3}\hat{j} - \frac{2}{3}\hat{k}
$$

---

### Q3. If $\vec{F} = (5xy - 6x^2)\hat{i} + (2y - 4x)\hat{j}$, evaluate $\int_C \vec{F} \cdot d\vec{r}$ along the curve $C$ in the $xy$ plane, $y = x^3$ from the point $(1, 1)$ to $(2, 8)$. (06)

**Answer:**

We write the line integral:

$$
\int_C \vec{F} \cdot d\vec{r} = \int_C [(5xy - 6x^2)dx + (2y - 4x)dy]
$$

We are given the curve relation:

$$
y = x^3
$$

We find the differential $dy$:

$$
dy = 3x^2 dx
$$

We substitute $y = x^3$ and $dy = 3x^2 dx$ into the line integral. The variable $x$ goes from 1 to 2:

$$
\int_C \vec{F} \cdot d\vec{r} = \int_1^2 [(5x(x^3) - 6x^2)dx + (2(x^3) - 4x)(3x^2 dx)]
$$

$$
\int_C \vec{F} \cdot d\vec{r} = \int_1^2 [(5x^4 - 6x^2) + (6x^5 - 12x^3)] dx
$$

$$
\int_C \vec{F} \cdot d\vec{r} = \int_1^2 (6x^5 + 5x^4 - 12x^3 - 6x^2) dx
$$

We integrate each term with respect to $x$:

$$
\int_C \vec{F} \cdot d\vec{r} = \left[ x^6 + x^5 - 3x^4 - 2x^3 \right]_1^2
$$

We evaluate at the upper limit $x = 2$:

$$
2^6 + 2^5 - 3(2^4) - 2(2^3) = 64 + 32 - 48 - 16 = 32
$$

We evaluate at the lower limit $x = 1$:

$$
1^6 + 1^5 - 3(1^4) - 2(1^3) = 1 + 1 - 3 - 2 = -3
$$

We subtract the lower limit value from the upper limit value:

$$
\int_C \vec{F} \cdot d\vec{r} = 32 - (-3) = 35
$$

So, the value of the line integral is 35.

---

[⬅ CT-1 (Vector) Answer](CT1_Vector_answer.md) | [🏠 Index](00-index.md) | [CT-1 (Matrix) Answer ➡](CT1_Matrix_answer.md)
