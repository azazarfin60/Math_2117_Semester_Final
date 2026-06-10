[ignoring loop detection]
*(start)* | [🏠 Index](00-index.md) | [2020_answer ➡](2020_answer.md)

---

# B.Sc. Engineering 2nd Year Odd Semester Examination 2019
**Course No: Math 2117**
**Course Title: Vector Analysis & Linear Algebra**
**Time: 3 Hours**
**Full Marks: 72**

---

### SECTION - A

### Q1(a) Find an equation for the plane perpendicular to the vector $\bar{A} = 2\hat{i} + 3\hat{j} + 6\hat{k}$ and passing through the terminal point of the vector $\bar{B} = \hat{i} + 5\hat{j} + 3\hat{k}$. (04)

**Answer:**

We assume the vector $\vec{B}$ starts at the origin. Its terminal point is $P(1, 5, 3)$.

The equation of a plane passing through a point $P(x_0, y_0, z_0)$ and perpendicular to a normal vector $\vec{A} = a\hat{i} + b\hat{j} + c\hat{k}$ is:

$$
a(x - x_0) + b(y - y_0) + c(z - z_0) = 0
$$

Substitute the point $(1, 5, 3)$ and the components of $\vec{A} = 2\hat{i} + 3\hat{j} + 6\hat{k}$:

$$
2(x - 1) + 3(y - 5) + 6(z - 3) = 0
$$

Expand the equation:

$$
2x - 2 + 3y - 15 + 6z - 18 = 0
$$

$$
2x + 3y + 6z - 35 = 0 \implies 2x + 3y + 6z = 35
$$

So the equation of the plane is $2x + 3y + 6z = 35$.

---

### Q1(b) Find the volume of the parallelepiped whose edges are represented by the vector $\bar{A} = 2\hat{i} - 3\hat{j} + 4\hat{k}$, $\bar{B} = \hat{i} + 2\hat{j} - \hat{k}$ and $\bar{C} = 3\hat{i} - \hat{j} + 2\hat{k}$. (04)

**Answer:**

The volume $V$ of a parallelepiped with adjacent edges represented by vectors $\vec{A}$, $\vec{B}$, and $\vec{C}$ is given by the absolute value of their scalar triple product:

$$
V = | \vec{A} \cdot (\vec{B} \times \vec{C}) |
$$

We calculate the scalar triple product using the determinant:

$$
\vec{A} \cdot (\vec{B} \times \vec{C}) = \begin{vmatrix} 2 & -3 & 4 \\ 1 & 2 & -1 \\ 3 & -1 & 2 \end{vmatrix}
$$

Expand along the first row:

$$
= 2 \begin{vmatrix} 2 & -1 \\ -1 & 2 \end{vmatrix} - (-3) \begin{vmatrix} 1 & -1 \\ 3 & 2 \end{vmatrix} + 4 \begin{vmatrix} 1 & 2 \\ 3 & -1 \end{vmatrix}
$$

$$
= 2 [ 4 - 1 ] + 3 [ 2 - (-3) ] + 4 [ -1 - 6 ]
$$

$$
= 2(3) + 3(5) + 4(-7) = 6 + 15 - 28 = -7
$$

Taking the absolute value:

$$
V = |-7| = 7 \text{ cubic units}
$$

---

### Q1(c) Find the acute angles which the line joining the points $(1, -3, 2)$ and $(3, -5, 1)$ makes with the coordinate axes. (04)

**Answer:**

Let the points be $P(1, -3, 2)$ and $Q(3, -5, 1)$. The vector $\vec{PQ}$ representing the line segment is:

$$
\vec{PQ} = (3 - 1)\hat{i} + (-5 - (-3))\hat{j} + (1 - 2)\hat{k} = 2\hat{i} - 2\hat{j} - \hat{k}
$$

Find the magnitude of the vector $\vec{PQ}$:

$$
|\vec{PQ}| = \sqrt{2^2 + (-2)^2 + (-1)^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3
$$

The direction cosines of this vector are:

$$
\cos\alpha = \frac{2}{3}, \quad \cos\beta = -\frac{2}{3}, \quad \cos\gamma = -\frac{1}{3}
$$

where $\alpha, \beta, \gamma$ are the angles made with the positive directions of the $x$, $y$, and $z$ axes respectively.

For the acute angles, the cosines must be positive:

$$
\cos\alpha = \frac{2}{3} \implies \alpha = \cos^{-1}\left(\frac{2}{3}\right) \approx 48.19^\circ
$$

$$
\cos\beta = \frac{2}{3} \implies \beta = \cos^{-1}\left(\frac{2}{3}\right) \approx 48.19^\circ
$$

$$
\cos\gamma = \frac{1}{3} \implies \gamma = \cos^{-1}\left(\frac{1}{3}\right) \approx 70.53^\circ
$$

---

### Q2(a) A particle moves along the curve $x = 2t^2, y = t^2 - 4t, z = 3t - 5$, where $t$ is the time. Find the components of its velocity and acceleration at time $t=1$ in the direction $\hat{i} - 3\hat{j} + 2\hat{k}$. (04)

**Answer:**

Let the direction vector be $\vec{d} = \hat{i} - 3\hat{j} + 2\hat{k}$. The unit direction vector $\hat{u}$ is:

$$
\hat{u} = \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{1^2 + (-3)^2 + 2^2}} = \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{14}}
$$

The position vector of the particle is:

$$
\vec{r}(t) = 2t^2\hat{i} + (t^2 - 4t)\hat{j} + (3t - 5)\hat{k}
$$

#### 1. Velocity Component

Differentiate the position vector to get the velocity vector:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt} = 4t\hat{i} + (2t - 4)\hat{j} + 3\hat{k}
$$

Evaluate velocity at $t=1$:

$$
\vec{v}(1) = 4\hat{i} - 2\hat{j} + 3\hat{k}
$$

The component of velocity in the direction of $\hat{u}$ is:

$$
v_d = \vec{v}(1) \cdot \hat{u} = (4\hat{i} - 2\hat{j} + 3\hat{k}) \cdot \left( \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{14}} \right) = \frac{4 + 6 + 6}{\sqrt{14}} = \frac{16}{\sqrt{14}}
$$

#### 2. Acceleration Component

Differentiate the velocity vector to get the acceleration vector:

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = 4\hat{i} + 2\hat{j}
$$

Evaluate acceleration at $t=1$:

$$
\vec{a}(1) = 4\hat{i} + 2\hat{j}
$$

The component of acceleration in the direction of $\hat{u}$ is:

$$
a_d = \vec{a}(1) \cdot \hat{u} = (4\hat{i} + 2\hat{j}) \cdot \left( \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{14}} \right) = \frac{4 - 6 + 0}{\sqrt{14}} = -\frac{2}{\sqrt{14}}
$$

---

### Q2(b) If $\bar{A}$ has a constant magnitude show that $\bar{A}$ and $\frac{d\bar{A}}{dt}$ are perpendicular provided $\left|\frac{d\bar{A}}{dt}\right| \neq 0$. (04)

**Answer:**

Let the constant magnitude of $\vec{A}$ be $|\vec{A}| = c$ (where $c$ is a constant).

Then we can write:

$$
\vec{A} \cdot \vec{A} = |\vec{A}|^2 = c^2
$$

Differentiate both sides with respect to $t$:

$$
\frac{d}{dt} (\vec{A} \cdot \vec{A}) = \frac{d}{dt} (c^2)
$$

Using the product rule for vector dot products:

$$
\vec{A} \cdot \frac{d\vec{A}}{dt} + \frac{d\vec{A}}{dt} \cdot \vec{A} = 0
$$

Since the dot product is commutative ($\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$):

$$
2 \left( \vec{A} \cdot \frac{d\vec{A}}{dt} \right) = 0 \implies \vec{A} \cdot \frac{d\vec{A}}{dt} = 0
$$

Since the dot product of $\vec{A}$ and $\frac{d\vec{A}}{dt}$ is zero, and neither vector is zero (given $\left|\frac{d\vec{A}}{dt}\right| \neq 0$ and magnitude of $\vec{A}$ is a non-zero constant), the vectors must be perpendicular.

---

### Q2(c) Find the directional derivative of $\phi = x^2yz + 4xz^2$ at $(1, -2, 1)$ in the direction $2\hat{i} - \hat{j} - 2\hat{k}$. (04)

**Answer:**

The gradient of $\phi$ is:

$$
\vec{\nabla}\phi = \frac{\partial\phi}{\partial x}\hat{i} + \frac{\partial\phi}{\partial y}\hat{j} + \frac{\partial\phi}{\partial z}\hat{k}
$$

$$
\vec{\nabla}\phi = (2xyz + 4z^2)\hat{i} + x^2z\hat{j} + (x^2y + 8xz)\hat{k}
$$

Evaluate this gradient at the point $(1, -2, 1)$:

*   $\frac{\partial\phi}{\partial x} = 2(1)(-2)(1) + 4(1)^2 = -4 + 4 = 0$
*   $\frac{\partial\phi}{\partial y} = (1)^2(1) = 1$
*   $\frac{\partial\phi}{\partial z} = (1)^2(-2) + 8(1)(1) = -2 + 8 = 6$

So the gradient vector is:

$$
\vec{\nabla}\phi(1, -2, 1) = \hat{j} + 6\hat{k}
$$

The direction vector is $\vec{d} = 2\hat{i} - \hat{j} - 2\hat{k}$. The unit vector $\hat{u}$ is:

$$
\hat{u} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{\sqrt{2^2 + (-1)^2 + (-2)^2}} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3}
$$

The directional derivative is the dot product of the gradient and the unit vector:

$$
D_{\hat{u}}\phi = \vec{\nabla}\phi \cdot \hat{u} = (\hat{j} + 6\hat{k}) \cdot \left( \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3} \right) = \frac{0(2) + 1(-1) + 6(-2)}{3} = -\frac{13}{3}
$$

---

### Q3(a) Find the angle between the surfaces $x^2 + y^2 + z^2 = 9$ and $z = x^2 + y^2 - 3$ at the point $(2, -1, 2)$. (04)

**Answer:**

The angle between two surfaces at a point is the angle between their normal vectors at that point.

#### 1. Normal to the First Surface

Let the surface be $F(x, y, z) = x^2 + y^2 + z^2 - 9 = 0$. The gradient is:

$$
\vec{\nabla}F = 2x\hat{i} + 2y\hat{j} + 2z\hat{k}
$$

At the point $(2, -1, 2)$, the normal vector is:

$$
\vec{n}_1 = 4\hat{i} - 2\hat{j} + 4\hat{k}
$$

#### 2. Normal to the Second Surface

Let the surface be $G(x, y, z) = x^2 + y^2 - z - 3 = 0$. The gradient is:

$$
\vec{\nabla}G = 2x\hat{i} + 2y\hat{j} - \hat{k}
$$

At the point $(2, -1, 2)$, the normal vector is:

$$
\vec{n}_2 = 4\hat{i} - 2\hat{j} - \hat{k}
$$

#### 3. Angle Calculation

Let $\theta$ be the angle between the two normal vectors:

$$
\cos\theta = \frac{\vec{n}_1 \cdot \vec{n}_2}{|\vec{n}_1||\vec{n}_2|}
$$

Calculate the dot product:

$$
\vec{n}_1 \cdot \vec{n}_2 = 4(4) + (-2)(-2) + 4(-1) = 16 + 4 - 4 = 16
$$

Calculate the magnitudes:

$$
|\vec{n}_1| = \sqrt{4^2 + (-2)^2 + 4^2} = \sqrt{36} = 6
$$

$$
|\vec{n}_2| = \sqrt{4^2 + (-2)^2 + (-1)^2} = \sqrt{21}
$$

So we get:

$$
\cos\theta = \frac{16}{6\sqrt{21}} = \frac{8}{3\sqrt{21}} \implies \theta = \cos^{-1}\left( \frac{8}{3\sqrt{21}} \right) \approx 54.41^\circ
$$

---

### Q3(b) Prove that $\nabla^2(1/r) = 0$. (04)

**Answer:**

Let $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$, then $r = \sqrt{x^2 + y^2 + z^2}$.

The partial derivatives of $r$ with respect to coordinates are:

$$
\frac{\partial r}{\partial x} = \frac{x}{r}, \quad \frac{\partial r}{\partial y} = \frac{y}{r}, \quad \frac{\partial r}{\partial z} = \frac{z}{r}
$$

We find the gradient of $\frac{1}{r}$:

$$
\vec{\nabla}\left(\frac{1}{r}\right) = \hat{i}\frac{\partial}{\partial x}(r^{-1}) + \hat{j}\frac{\partial}{\partial y}(r^{-1}) + \hat{k}\frac{\partial}{\partial z}(r^{-1})
$$

Using the chain rule:

$$
\frac{\partial}{\partial x}(r^{-1}) = -r^{-2}\frac{\partial r}{\partial x} = -r^{-2}\left(\frac{x}{r}\right) = -\frac{x}{r^3}
$$

So the gradient vector is:

$$
\vec{\nabla}\left(\frac{1}{r}\right) = -\frac{x\hat{i} + y\hat{j} + z\hat{k}}{r^3} = -\frac{\vec{r}}{r^3}
$$

The Laplacian $\nabla^2\left(\frac{1}{r}\right)$ is the divergence of the gradient:

$$
\nabla^2\left(\frac{1}{r}\right) = \vec{\nabla} \cdot \vec{\nabla}\left(\frac{1}{r}\right) = -\left[ \frac{\partial}{\partial x}\left(\frac{x}{r^3}\right) + \frac{\partial}{\partial y}\left(\frac{y}{r^3}\right) + \frac{\partial}{\partial z}\left(\frac{z}{r^3}\right) \right]
$$

Using the quotient rule:

$$
\frac{\partial}{\partial x}\left(\frac{x}{r^3}\right) = \frac{r^3(1) - x(3r^2\frac{\partial r}{\partial x})}{r^6} = \frac{r^3 - 3x^2r}{r^6} = \frac{1}{r^3} - \frac{3x^2}{r^5}
$$

Similarly:

$$
\frac{\partial}{\partial y}\left(\frac{y}{r^3}\right) = \frac{1}{r^3} - \frac{3y^2}{r^5}
$$

$$
\frac{\partial}{\partial z}\left(\frac{z}{r^3}\right) = \frac{1}{r^3} - \frac{3z^2}{r^5}
$$

Summing these three partial derivatives:

$$
\nabla^2\left(\frac{1}{r}\right) = -\left[ \frac{3}{r^3} - \frac{3(x^2 + y^2 + z^2)}{r^5} \right] = -\left[ \frac{3}{r^3} - \frac{3r^2}{r^5} \right] = -\left[ \frac{3}{r^3} - \frac{3}{r^3} \right] = 0
$$

This completes the proof.

---

### Q3(c) If $\bar{F}$ represents a conservative force field then show that $\nabla \times \bar{F} = 0$. (04)

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
\vec{\nabla} \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ \frac{\partial\phi}{\partial x} & \frac{\partial\phi}{\partial y} & \frac{\partial\phi}{\partial z} \end{vmatrix}
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

### Q4(a) Evaluate $\iiint_V \nabla \cdot \bar{F} dV$ where $\bar{F} = (2x^2 - 3z)\hat{i} - 2xy\hat{j} - 4x\hat{k}$ and $V$ is the closed region bounded by the planes $x = 0, y = 0, z = 0$ and $2x + 2y + z = 4$. (06)

**Answer:**

First, we calculate the divergence of the vector field $\vec{F}$:

$$
\vec{\nabla} \cdot \vec{F} = \frac{\partial}{\partial x}(2x^2 - 3z) + \frac{\partial}{\partial y}(-2xy) + \frac{\partial}{\partial z}(-4x)
$$

$$
= 4x - 2x + 0 = 2x
$$

The region $V$ is a tetrahedron bounded by the coordinate planes and the plane $2x + 2y + z = 4$. We find the integration limits:

*   The variable $z$ goes from $0$ to $4 - 2x - 2y$.
*   For $z=0$, the boundary is $2x + 2y = 4 \implies y = 2 - x$. So $y$ goes from $0$ to $2 - x$.
*   For $y=z=0$, the boundary is $2x = 4 \implies x = 2$. So $x$ goes from $0$ to $2$.

We set up the triple integral:

$$
I = \iiint_V 2x \, dV = \int_{x=0}^2 \int_{y=0}^{2-x} \int_{z=0}^{4-2x-2y} 2x \, dz \, dy \, dx
$$

Integrate with respect to $z$:

$$
I = \int_{x=0}^2 \int_{y=0}^{2-x} 2x [z]_0^{4-2x-2y} \, dy \, dx = \int_{x=0}^2 \int_{y=0}^{2-x} 2x(4 - 2x - 2y) \, dy \, dx
$$

$$
= \int_0^2 2x \left[ (4 - 2x)y - y^2 \right]_0^{2-x} \, dx
$$

Since $4 - 2x = 2(2 - x)$, we substitute:

$$
I = \int_0^2 2x \left[ 2(2-x)(2-x) - (2-x)^2 \right] \, dx = \int_0^2 2x (2-x)^2 \, dx
$$

$$
= \int_0^2 2x (4 - 4x + x^2) \, dx = \int_0^2 (8x - 8x^2 + 2x^3) \, dx
$$

Integrate with respect to $x$:

$$
I = \left[ 4x^2 - \frac{8}{3}x^3 + \frac{1}{2}x^4 \right]_0^2 = 4(4) - \frac{8}{3}(8) + \frac{1}{2}(16) = 16 - \frac{64}{3} + 8 = 24 - \frac{64}{3} = \frac{8}{3}
$$

So the value of the triple integral is $\frac{8}{3}$.

---

### Q4(b) Verify Green's theorem in the plane for $\oint_C (2x - y^2)dx - xydy$ where $C$ is the boundary of the region enclosed by the circles $x^2 + y^2 = 1$ and $x^2 + y^2 = 9$. (06)

**Answer:**

Green's Theorem states:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA
$$

Here we identify the functions:

$$
P = 2x - y^2 \implies \frac{\partial P}{\partial y} = -2y
$$

$$
Q = -xy \implies \frac{\partial Q}{\partial x} = -y
$$

Substitute these:

$$
\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = -y - (-2y) = y
$$

#### 1. Evaluate Double Integral

The region $R$ is the annulus between the circles $r=1$ and $r=3$. We convert to polar coordinates ($x = r\cos\theta$, $y = r\sin\theta$, $dA = r \, dr \, d\theta$):

$$
\iint_R y \, dA = \int_{\theta=0}^{2\pi} \int_{r=1}^3 (r\sin\theta) r \, dr \, d\theta = \left( \int_1^3 r^2 \, dr \right) \left( \int_0^{2\pi} \sin\theta \, d\theta \right)
$$

Calculate the angular integral:

$$
\int_0^{2\pi} \sin\theta \, d\theta = \left[ -\cos\theta \right]_0^{2\pi} = -1 - (-1) = 0
$$

So the double integral is:

$$
\iint_R y \, dA = 0
$$

#### 2. Evaluate Line Integral

The closed boundary $C$ consists of two circular paths: the outer circle $C_1$ ($r=3$, traversed counterclockwise) and the inner circle $C_2$ ($r=1$, traversed clockwise):

- **On Outer Circle $C_1$:** $x = 3\cos\theta, y = 3\sin\theta \implies dx = -3\sin\theta \, d\theta, dy = 3\cos\theta \, d\theta$ with $\theta$ from $0$ to $2\pi$:

$$
\int_{C_1} (2x - y^2)dx - xydy = \int_0^{2\pi} \left[ (6\cos\theta - 9\sin^2\theta)(-3\sin\theta) - 9\cos\theta\sin\theta(3\cos\theta) \right] d\theta
$$

$$
= \int_0^{2\pi} \left[ -18\cos\theta\sin\theta + 27\sin^3\theta - 27\cos^2\theta\sin\theta \right] d\theta = 0
$$

(since each component integrates to $0$ over the full period $[0, 2\pi]$).

- **On Inner Circle $C_2$:** $x = \cos\theta, y = \sin\theta \implies dx = -\sin\theta \, d\theta, dy = \cos\theta \, d\theta$ with $\theta$ from $2\pi$ to $0$:

$$
\int_{C_2} (2x - y^2)dx - xydy = \int_{2\pi}^0 \left[ (2\cos\theta - \sin^2\theta)(-\sin\theta) - \cos\theta\sin\theta(\cos\theta) \right] d\theta = 0
$$

The total line integral is:

$$
\oint_C = \int_{C_1} + \int_{C_2} = 0 + 0 = 0
$$

Both the double integral and the line integral equal $0$, so Green's theorem is verified.

---

### SECTION - B

### Q5(a) What is an inverse of a matrix? Find the inverse of the following matrix: (06)
$$
\begin{pmatrix}
1 & 3 & 3 \\
1 & 4 & 3 \\
1 & 3 & 4
\end{pmatrix}
$$

**Answer:**

#### 1. Definition of Inverse Matrix

Let $A$ be a square matrix of order $n$. If there exists a square matrix $B$ of order $n$ such that:

$$
AB = BA = I_n
$$

(where $I_n$ is the identity matrix of order $n$), then $B$ is called the inverse of $A$. The inverse matrix is unique and is denoted by $A^{-1}$.

#### 2. Find the Inverse

We set up the augmented matrix $[A | I]$:

$$
\begin{bmatrix}
1 & 3 & 3 & | & 1 & 0 & 0 \\
1 & 4 & 3 & | & 0 & 1 & 0 \\
1 & 3 & 4 & | & 0 & 0 & 1
\end{bmatrix}
$$

Apply row operations to clear the first column:
*   $R_2 \to R_2 - R_1$
*   $R_3 \to R_3 - R_1$

This gives:

$$
\begin{bmatrix}
1 & 3 & 3 & | & 1 & 0 & 0 \\
0 & 1 & 0 & | & -1 & 1 & 0 \\
0 & 0 & 1 & | & -1 & 0 & 1
\end{bmatrix}
$$

Apply row operation to clear the second column:
*   $R_1 \to R_1 - 3R_2$

This gives:

$$
\begin{bmatrix}
1 & 0 & 3 & | & 4 & -3 & 0 \\
0 & 1 & 0 & | & -1 & 1 & 0 \\
0 & 0 & 1 & | & -1 & 0 & 1
\end{bmatrix}
$$

Apply row operation to clear the third column:
*   $R_1 \to R_1 - 3R_3$

This yields:

$$
\begin{bmatrix}
1 & 0 & 0 & | & 7 & -3 & -3 \\
0 & 1 & 0 & | & -1 & 1 & 0 \\
0 & 0 & 1 & | & -1 & 0 & 1
\end{bmatrix}
$$

So the inverse matrix is:

$$
A^{-1} = \begin{pmatrix}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{pmatrix}
$$

---

### Q5(b) What is the normal form of a matrix? Find the rank of the following matrix reducing it to the normal form: (06)
$$
\begin{pmatrix}
3 & -2 & 0 & -7 \\
0 & 2 & 1 & -5 \\
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6
\end{pmatrix}
$$

**Answer:**

#### 1. Definition of Normal Form

By applying a finite sequence of elementary row and column operations, any non-zero matrix $A$ of rank $r$ can be reduced to one of the following forms:

$$
[I_r], \quad [I_r \quad | \quad 0], \quad \begin{bmatrix} I_r \\ -- \\ 0 \end{bmatrix}, \quad \begin{bmatrix} I_r & | & 0 \\ -- & - & -- \\ 0 & | & 0 \end{bmatrix}
$$

where $I_r$ is the identity matrix of order $r$. This form is called the **normal form** (or **canonical form**) of the matrix. The rank of the matrix is equal to the order of the identity matrix $I_r$ in this form.

#### 2. Reduction to Normal Form

We write the matrix:

$$
A = \begin{pmatrix}
3 & -2 & 0 & -7 \\
0 & 2 & 1 & -5 \\
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6
\end{pmatrix}
$$

Swap row 1 and row 3 ($R_1 \leftrightarrow R_3$):

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 2 & 1 & -5 \\
3 & -2 & 0 & -7 \\
0 & 1 & 1 & -6
\end{pmatrix}
$$

Apply row operation:
*   $R_3 \to R_3 - 3R_1$

This gives:

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 2 & 1 & -5 \\
0 & 4 & 6 & -10 \\
0 & 1 & 1 & -6
\end{pmatrix}
$$

Swap row 2 and row 4 ($R_2 \leftrightarrow R_4$):

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6 \\
0 & 4 & 6 & -10 \\
0 & 2 & 1 & -5
\end{pmatrix}
$$

Apply row operations:
*   $R_3 \to R_3 - 4R_2$
*   $R_4 \to R_4 - 2R_2$

This yields:

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6 \\
0 & 0 & 2 & 14 \\
0 & 0 & -1 & 7
\end{pmatrix}
$$

Scale row 3 ($R_3 \to \frac{1}{2}R_3$):

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6 \\
0 & 0 & 1 & 7 \\
0 & 0 & -1 & 7
\end{pmatrix}
$$

Add row 3 to row 4 ($R_4 \to R_4 + R_3$):

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6 \\
0 & 0 & 1 & 7 \\
0 & 0 & 0 & 14
\end{pmatrix}
$$

Scale row 4 ($R_4 \to \frac{1}{14}R_4$):

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6 \\
0 & 0 & 1 & 7 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

Now apply column operations to clear the off-diagonal elements. First, clear elements in row 1:
*   $C_2 \to C_2 + 2C_1$
*   $C_3 \to C_3 + 2C_1$
*   $C_4 \to C_4 - C_1$

This gives:

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & -6 \\
0 & 0 & 1 & 7 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

Clear elements in row 2:
*   $C_3 \to C_3 - C_2$
*   $C_4 \to C_4 + 6C_2$

This gives:

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 7 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

Clear elements in row 3:
*   $C_4 \to C_4 - 7C_3$

This yields the identity matrix of order 4:

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} = I_4
$$

So the normal form is $I_4$, and the rank of the matrix is:

$$
\text{Rank} = 4
$$

---

### Q6(a) Discuss about the consistency of a system and then find the solution set of the system: (06)
$$
\begin{aligned}
x + 2y + 2z &= 1 \\
2x + y + z &= 2 \\
3x + 2y + 2z &= 3 \\
y + z &= 0
\end{aligned}
$$

**Answer:**

#### 1. Discuss Consistency

A system of linear equations $AX = B$ is consistent if there exists at least one set of values for the unknowns that satisfies all equations simultaneously. In terms of rank:
*   The system is consistent if $\text{Rank}(A) = \text{Rank}([A|B])$, where $A$ is the coefficient matrix and $[A|B]$ is the augmented matrix.
*   If $\text{Rank}(A) = \text{Rank}([A|B]) = n$ (number of variables), the system has a unique solution.
*   If $\text{Rank}(A) = \text{Rank}([A|B]) < n$, the system has infinitely many solutions (with $n - r$ free parameters).
*   If $\text{Rank}(A) \neq \text{Rank}([A|B])$, the system is inconsistent (no solution).

#### 2. Solve the System

We write the augmented matrix $[A|B]$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
2 & 1 & 1 & | & 2 \\
3 & 2 & 2 & | & 3 \\
0 & 1 & 1 & | & 0
\end{bmatrix}
$$

Apply row operations to clear the first column:
*   $R_2 \to R_2 - 2R_1$
*   $R_3 \to R_3 - 3R_1$

This gives:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
0 & -3 & -3 & | & 0 \\
0 & -4 & -4 & | & 0 \\
0 & 1 & 1 & | & 0
\end{bmatrix}
$$

Scale row 2 and row 3:
*   $R_2 \to -\frac{1}{3} R_2$
*   $R_3 \to -\frac{1}{4} R_3$

This gives:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
0 & 1 & 1 & | & 0 \\
0 & 1 & 1 & | & 0 \\
0 & 1 & 1 & | & 0
\end{bmatrix}
$$

Apply row operations:
*   $R_3 \to R_3 - R_2$
*   $R_4 \to R_4 - R_2$

This yields the row echelon form:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
0 & 1 & 1 & | & 0 \\
0 & 0 & 0 & | & 0 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

The rank of the coefficient matrix $A$ is 2, and the rank of the augmented matrix $[A|B]$ is also 2. Since $\text{Rank}(A) = \text{Rank}([A|B]) = 2$, the system is consistent.

Since there are 3 variables ($x, y, z$) and the rank is 2, there is $3 - 2 = 1$ free variable.

From row 2:

$$
y + z = 0 \implies y = -z
$$

From row 1:

$$
x + 2y + 2z = 1 \implies x + 2(-z) + 2z = 1 \implies x = 1
$$

Let $z = k$ (where $k \in \mathbb{R}$ is a parameter). The solution set is:

$$
x = 1, \quad y = -k, \quad z = k \quad (k \in \mathbb{R})
$$

---

### Q6(b) Find the trivial solution of: (06)
$$
\begin{aligned}
x + y + z + w &= 0 \\
x + 3y - 2z + 4w &= 0 \\
2x + y - z - w &= 0
\end{aligned}
$$

**Answer:**

For any homogeneous linear system $AX = 0$, the trivial solution is the solution where all variables are zero:

$$
x = 0, \quad y = 0, \quad z = 0, \quad w = 0
$$

To find if there are non-trivial solutions (which is the mathematical intent of the question), we write the coefficient matrix:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 3 & -2 & 4 \\
2 & 1 & -1 & -1
\end{bmatrix}
$$

Apply row operations:
*   $R_2 \to R_2 - R_1$
*   $R_3 \to R_3 - 2R_1$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 3 \\
0 & -1 & -3 & -3
\end{bmatrix}
$$

Swap row 2 and row 3 ($R_2 \leftrightarrow R_3$) and multiply the new row 2 by $-1$ ($R_2 \to -R_2$):

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 3 & 3 \\
0 & 2 & -3 & 3
\end{bmatrix}
$$

Apply row operation:
*   $R_3 \to R_3 - 2R_2$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 3 & 3 \\
0 & 0 & -9 & -3
\end{bmatrix}
$$

Scale row 3 ($R_3 \to -\frac{1}{3} R_3$):

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 3 & 3 \\
0 & 0 & 3 & 1
\end{bmatrix}
$$

The rank of the matrix is 3. Since there are 4 variables ($x, y, z, w$) and the rank is 3, there is $4 - 3 = 1$ free variable.

From row 3:

$$
3z + w = 0 \implies w = -3z
$$

From row 2:

$$
y + 3z + 3w = 0 \implies y + 3z + 3(-3z) = 0 \implies y - 6z = 0 \implies y = 6z
$$

From row 1:

$$
x + y + z + w = 0 \implies x + 6z + z - 3z = 0 \implies x + 4z = 0 \implies x = -4z
$$

Let $z = k$ (where $k \in \mathbb{R}$ is a parameter). The complete solution set is:

$$
x = -4k, \quad y = 6k, \quad z = k, \quad w = -3k \quad (k \in \mathbb{R})
$$

*   The **trivial solution** corresponds to $k = 0$, giving $(0, 0, 0, 0)$.
*   For any $k \neq 0$, we obtain **non-trivial solutions**.

---

### Q7(a) Find the eigen vectors of the following matrix: (06)
$$
\begin{pmatrix}
1 & 3 & 0 \\
3 & -2 & -1 \\
0 & -1 & 1
\end{pmatrix}
$$

**Answer:**

#### 1. Find the Eigenvalues

We solve the characteristic equation $|A - \lambda I| = 0$:

$$
\begin{vmatrix}
1 - \lambda & 3 & 0 \\
3 & -2 - \lambda & -1 \\
0 & -1 & 1 - \lambda
\end{vmatrix} = 0
$$

Expand the determinant along row 1:

$$
(1 - \lambda) \left[ (-2 - \lambda)(1 - \lambda) - (-1)(-1) \right] - 3 \left[ 3(1 - \lambda) - 0 \right] = 0
$$

$$
(1 - \lambda) \left[ (\lambda + 2)(\lambda - 1) - 1 \right] - 9(1 - \lambda) = 0
$$

$$
(1 - \lambda) \left[ \lambda^2 + \lambda - 2 - 1 - 9 \right] = 0
$$

$$
(1 - \lambda) \left[ \lambda^2 + \lambda - 12 \right] = 0
$$

Factor the quadratic term:

$$
(1 - \lambda)(\lambda + 4)(\lambda - 3) = 0
$$

So the eigenvalues are:

$$
\lambda_1 = 1, \quad \lambda_2 = 3, \quad \lambda_3 = -4
$$

#### 2. Find the Eigenvectors

We solve the system $(A - \lambda I)X = 0$ for each eigenvalue:

##### Case 1: For $\lambda_1 = 1$

$$
\begin{bmatrix}
0 & 3 & 0 \\
3 & -3 & -1 \\
0 & -1 & 0
\end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$

From row 1 and row 3, we get $y = 0$. Substitute $y=0$ into row 2:

$$
3x - 3(0) - z = 0 \implies z = 3x
$$

Let $x = 1$. The first eigenvector is:

$$
X_1 = \begin{bmatrix} 1 \\ 0 \\ 3 \end{bmatrix}
$$

##### Case 2: For $\lambda_2 = 3$

$$
\begin{bmatrix}
-2 & 3 & 0 \\
3 & -5 & -1 \\
0 & -1 & -2
\end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$

From row 1:

$$
-2x + 3y = 0 \implies x = \frac{3}{2}y
$$

From row 3:

$$
-y - 2z = 0 \implies z = -\frac{1}{2}y
$$

Let $y = 2$. Then $x = 3$ and $z = -1$. The second eigenvector is:

$$
X_2 = \begin{bmatrix} 3 \\ 2 \\ -1 \end{bmatrix}
$$

##### Case 3: For $\lambda_3 = -4$

$$
\begin{bmatrix}
5 & 3 & 0 \\
3 & 2 & -1 \\
0 & -1 & 5
\end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$

From row 1:

$$
5x + 3y = 0 \implies y = -\frac{5}{3}x
$$

From row 3:

$$
-y + 5z = 0 \implies z = \frac{1}{5}y = \frac{1}{5}\left(-\frac{5}{3}x\right) = -\frac{1}{3}x
$$

Let $x = 3$. Then $y = -5$ and $z = -1$. The third eigenvector is:

$$
X_3 = \begin{bmatrix} 3 \\ -5 \\ -1 \end{bmatrix}
$$

---

### Q7(b) Verify Cayley-Hamilton's theorem for $A = \begin{pmatrix} 2 & -1 & 1 \\ -1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix}$ and hence find $A^{-1}$. (06)

**Answer:**

#### 1. Find characteristic equation

The characteristic equation is $|A - \lambda I| = 0$:

$$
\begin{vmatrix} 2-\lambda & -1 & 1 \\ -1 & 2-\lambda & -1 \\ 1 & -1 & 2-\lambda \end{vmatrix} = 0
$$

Calculate the determinant:

$$
(2-\lambda)\left[ (2-\lambda)^2 - 1 \right] - (-1)\left[ -(2-\lambda) - (-1) \right] + 1\left[ 1 - (2-\lambda) \right] = 0
$$

$$
(2-\lambda)(\lambda^2 - 4\lambda + 3) + (\lambda - 1) + (\lambda - 1) = 0
$$

$$
-\lambda^3 + 6\lambda^2 - 9\lambda + 4 = 0 \implies \lambda^3 - 6\lambda^2 + 9\lambda - 4I = 0
$$

#### 2. Verification of Cayley-Hamilton Theorem

According to the theorem, the matrix $A$ satisfies its own characteristic equation:

$$
A^3 - 6A^2 + 9A - 4I = 0
$$

We calculate $A^2$ and $A^3$:

$$
A^2 = \begin{pmatrix} 2 & -1 & 1 \\ -1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix} \begin{pmatrix} 2 & -1 & 1 \\ -1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix} = \begin{pmatrix} 6 & -5 & 5 \\ -5 & 6 & -5 \\ 5 & -5 & 6 \end{pmatrix}
$$

$$
A^3 = A^2 A = \begin{pmatrix} 6 & -5 & 5 \\ -5 & 6 & -5 \\ 5 & -5 & 6 \end{pmatrix} \begin{pmatrix} 2 & -1 & 1 \\ -1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix} = \begin{pmatrix} 22 & -21 & 21 \\ -21 & 22 & -21 \\ 21 & -21 & 22 \end{pmatrix}
$$

Now substitute $A^3$, $A^2$, $A$, and $I$ into the expression:

$$
A^3 - 6A^2 + 9A - 4I = \begin{pmatrix} 22 & -21 & 21 \\ -21 & 22 & -21 \\ 21 & -21 & 22 \end{pmatrix} - \begin{pmatrix} 36 & -30 & 30 \\ -30 & 36 & -30 \\ 30 & -30 & 36 \end{pmatrix} + \begin{pmatrix} 18 & -9 & 9 \\ -9 & 18 & -9 \\ 9 & -9 & 18 \end{pmatrix} - \begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix}
$$

Calculate the matrix elements:
*   Diagonal elements: $22 - 36 + 18 - 4 = 0$
*   Off-diagonal elements (e.g. Row 1 Col 2): $-21 - (-30) + (-9) - 0 = 0$

All entries are zero. Cayley-Hamilton's Theorem is verified.

#### 3. Find $A^{-1}$

Multiply the equation by $A^{-1}$:

$$
A^2 - 6A + 9I - 4A^{-1} = 0 \implies 4A^{-1} = A^2 - 6A + 9I
$$

$$
4A^{-1} = \begin{pmatrix} 6 & -5 & 5 \\ -5 & 6 & -5 \\ 5 & -5 & 6 \end{pmatrix} - \begin{pmatrix} 12 & -6 & 6 \\ -6 & 12 & -6 \\ 6 & -6 & 12 \end{pmatrix} + \begin{pmatrix} 9 & 0 & 0 \\ 0 & 9 & 0 \\ 0 & 0 & 9 \end{pmatrix}
$$

$$
4A^{-1} = \begin{pmatrix} 3 & 1 & -1 \\ 1 & 3 & 1 \\ -1 & 1 & 3 \end{pmatrix} \implies A^{-1} = \frac{1}{4} \begin{pmatrix} 3 & 1 & -1 \\ 1 & 3 & 1 \\ -1 & 1 & 3 \end{pmatrix}
$$

---

### Q8(a) Prove that the vector space $V$ is the direct sum of its subspaces $U$ and $W$ if and only if (i) $V = U + W$, (ii) $U \cap W = \{0\}$. (06)

**Answer:**

#### 1. Forward Direction ($\implies$)

Assume $V$ is the direct sum of $U$ and $W$ ($V = U \oplus W$).

By definition of direct sum, every vector $v \in V$ can be uniquely written as:

$$
v = u + w \quad \text{where } u \in U \text{ and } w \in W
$$

*   Since every $v \in V$ can be written as $u+w$, we have:

$$
V = U + W
$$

*   Now let us prove $U \cap W = \{0\}$. Let $v \in U \cap W$.
    *   Since $v \in U$, we can write $v = v + 0$ (where $v \in U$ and $0 \in W$).
    *   Since $v \in W$, we can write $v = 0 + v$ (where $0 \in U$ and $v \in W$).
    *   But by uniqueness of the decomposition of $v$, these two expressions must be identical:

$$
v = 0 \quad \text{and} \quad 0 = v \implies v = 0
$$

Thus, $U \cap W = \{0\}$.

#### 2. Reverse Direction ($\impliedby$)

Assume (i) $V = U + W$ and (ii) $U \cap W = \{0\}$.

Since $V = U + W$, every vector $v \in V$ can be written as:

$$
v = u + w \quad \text{where } u \in U \text{ and } w \in W
$$

We must show that this representation is unique.

Suppose $v$ can be represented in two ways:

$$
v = u_1 + w_1 \quad \text{and} \quad v = u_2 + w_2
$$

where $u_1, u_2 \in U$ and $w_1, w_2 \in W$.

Equating the two expressions:

$$
u_1 + w_1 = u_2 + w_2 \implies u_1 - u_2 = w_2 - w_1
$$

*   Since $U$ is a subspace, $u_1 - u_2 \in U$.
*   Since $W$ is a subspace, $w_2 - w_1 \in W$.

Since $u_1 - u_2 = w_2 - w_1$, this vector belongs to both $U$ and $W$:

$$
u_1 - u_2 \in U \cap W \quad \text{and} \quad w_2 - w_1 \in U \cap W
$$

But we are given $U \cap W = \{0\}$. Therefore:

$$
u_1 - u_2 = 0 \implies u_1 = u_2
$$

$$
w_2 - w_1 = 0 \implies w_1 = w_2
$$

Since $u_1 = u_2$ and $w_1 = w_2$, the representation is unique. Thus, $V$ is the direct sum of $U$ and $W$ ($V = U \oplus W$).

---

### Q8(b) Define Kernel and image of a linear mapping. Let $F : V \rightarrow U$ be a linear mapping. Show that the Kernel of $F$ is a subspace of $V$ and the image of $F$ is a subspace of $U$. (06)

**Answer:**

#### 1. Definitions

*   **Kernel of $F$:** The set of all vectors in $V$ that map to the zero vector in $U$. It is denoted by $\text{Ker}(F)$:

$$
\text{Ker}(F) = \{ v \in V \mid F(v) = 0_U \}
$$

*   **Image of $F$:** The set of all vectors in $U$ that are mapped to by at least one vector in $V$. It is denoted by $\text{Im}(F)$:

$$
\text{Im}(F) = \{ u \in U \mid \exists v \in V \text{ such that } F(v) = u \}
$$

#### 2. Prove $\text{Ker}(F)$ is a subspace of $V$

To show that $\text{Ker}(F)$ is a subspace of $V$, we must verify three properties:

1.  **Non-emptiness / Zero Vector:** Since $F$ is linear:

$$
F(0_V) = 0_U \implies 0_V \in \text{Ker}(F)
$$

2.  **Closure under Addition:** Let $v_1, v_2 \in \text{Ker}(F)$. Then $F(v_1) = 0_U$ and $F(v_2) = 0_U$.

$$
F(v_1 + v_2) = F(v_1) + F(v_2) = 0_U + 0_U = 0_U \implies v_1 + v_2 \in \text{Ker}(F)
$$

3.  **Closure under Scalar Multiplication:** Let $v \in \text{Ker}(F)$ and let $k$ be a scalar in the field. Then $F(v) = 0_U$.

$$
F(k v) = k F(v) = k (0_U) = 0_U \implies k v \in \text{Ker}(F)
$$

Since all three properties are satisfied, $\text{Ker}(F)$ is a subspace of $V$.

#### 3. Prove $\text{Im}(F)$ is a subspace of $U$

To show that $\text{Im}(F)$ is a subspace of $U$, we verify the three properties:

1.  **Non-emptiness / Zero Vector:** Since $F(0_V) = 0_U$, the zero vector $0_U$ has a pre-image in $V$:

$$
0_U \in \text{Im}(F)
$$

2.  **Closure under Addition:** Let $u_1, u_2 \in \text{Im}(F)$. Then there exist $v_1, v_2 \in V$ such that $F(v_1) = u_1$ and $F(v_2) = u_2$.

$$
u_1 + u_2 = F(v_1) + F(v_2) = F(v_1 + v_2)
$$

Since $v_1 + v_2 \in V$ (as $V$ is a vector space), $u_1 + u_2$ is the image of $v_1 + v_2$, so:

$$
u_1 + u_2 \in \text{Im}(F)
$$

3.  **Closure under Scalar Multiplication:** Let $u \in \text{Im}(F)$ and let $k$ be a scalar. Then there exists $v \in V$ such that $F(v) = u$.

$$
k u = k F(v) = F(k v)
$$

Since $k v \in V$, $k u$ is the image of $k v$, so:

$$
k u \in \text{Im}(F)
$$

Since all three properties are satisfied, $\text{Im}(F)$ is a subspace of $U$.
