[⬅ 2019](2019_answer.md) | [🏠 Index](00-index.md) | [2021 ➡](2021_answer.md)

---

# B.Sc. Engineering 2nd Year Odd Semester Examination 2020
**Course No: MATH 2117**
**Course Title: Vector Analysis & Linear Algebra**
**Time: 3 Hours**
**Full Marks: 72**

---

## SECTION - A

### Q1(a) What is the vector? Find a unit vector parallel to the resultant of vectors 

$$
\vec{r}_1 = 2\hat{i} + 4\hat{j} - 5\hat{k}
$$

$$
\vec{r}_2 = \hat{i} + 2\hat{j} + \hat{k}
$$

(04)

**Answer:**

#### 1. Definition of a Vector

A vector is a mathematical quantity that has both magnitude and direction. It also satisfies the parallelogram law of vector addition.

#### 2. Find the Unit Vector

We calculate the resultant vector $\vec{R}$ by adding the two given vectors:

$$
\vec{R} = \vec{r}_1 + \vec{r}_2 = (2\hat{i} + 4\hat{j} - 5\hat{k}) + (\hat{i} + 2\hat{j} + \hat{k}) = 3\hat{i} + 6\hat{j} - 4\hat{k}
$$

Find the magnitude of the resultant vector:

$$
|\vec{R}| = \sqrt{3^2 + 6^2 + (-4)^2} = \sqrt{9 + 36 + 16} = \sqrt{61}
$$

The unit vector parallel to $\vec{R}$ is:

$$
\hat{u} = \frac{\vec{R}}{|\vec{R}|} = \frac{3\hat{i} + 6\hat{j} - 4\hat{k}}{\sqrt{61}}
$$

---

### Q1(b) Define triple product of vectors. Show that, $\bar{A} \cdot (\bar{B} \times \bar{C})$ is in absolute value equal to the volume of a parallelepiped with sides $\bar{A}$, $\bar{B}$ and $\bar{C}$. (04)

**Answer:**

#### 1. Definition

A triple product is a product involving three vectors. There are two kinds:
*   **Scalar Triple Product:** The expression $\bar{A} \cdot (\bar{B} \times \bar{C})$, which results in a scalar.
*   **Vector Triple Product:** The expression $\bar{A} \times (\bar{B} \times \bar{C})$, which results in a vector.

#### 2. Geometric Proof

Let the three vectors $\bar{A}$, $\bar{B}$, and $\bar{C}$ represent the three adjacent edges of a parallelepiped.

The cross product vector $\bar{B} \times \bar{C}$ is perpendicular to the base face of the parallelepiped. The magnitude of this cross product is the area of the base parallelogram:

$$
\text{Area of Base} = |\bar{B} \times \bar{C}|
$$

Let $\theta$ be the angle between the vector $\bar{A}$ and the normal vector $\bar{B} \times \bar{C}$. The height $h$ of the parallelepiped is the projection of $\bar{A}$ along this normal vector:

$$
h = |\bar{A}| \cos\theta
$$

Now calculate the scalar triple product:

$$
\bar{A} \cdot (\bar{B} \times \bar{C}) = |\bar{A}| |\bar{B} \times \bar{C}| \cos\theta = h \times (\text{Area of Base}) = \text{Volume of Parallelepiped}
$$

Since a volume is always positive, we take the absolute value:

$$
\text{Volume} = |\bar{A} \cdot (\bar{B} \times \bar{C})|
$$

The proof is complete.

---

### Q1(c) If 

$$
\bar{A} = 2\hat{i} + \hat{j} - 3\hat{k}
$$

 and 

$$
\bar{B} = \hat{i} - 2\hat{j} + \hat{k}
$$

Find a vector of magnitude 5 perpendicular to both $\bar{A}$ and $\bar{B}$. (04)

**Answer:**

We calculate the cross product of the two vectors to find a perpendicular direction:

$$
\bar{A} \times \bar{B} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
2 & 1 & -3 \\
1 & -2 & 1
\end{vmatrix} = \hat{i}(1 - 6) - \hat{j}(2 - (-3)) + \hat{k}(-4 - 1) = -5\hat{i} - 5\hat{j} - 5\hat{k}
$$

We simplify the perpendicular direction to:

$$
\vec{v} = \hat{i} + \hat{j} + \hat{k}
$$

The unit normal vector $\hat{n}$ is:

$$
\hat{n} = \pm \frac{\hat{i} + \hat{j} + \hat{k}}{\sqrt{1^2 + 1^2 + 1^2}} = \pm \frac{\hat{i} + \hat{j} + \hat{k}}{\sqrt{3}}
$$

The vector with a magnitude of 5 is:

$$
\vec{P} = \pm 5 \hat{n} = \pm \frac{5}{\sqrt{3}} (\hat{i} + \hat{j} + \hat{k})
$$

---

### Q2(a) A particle moves along a curve whose parametric equations are $x = e^{-t}, y = 2\cos 3t, z = 2\sin 3t$, where $t$ is the time. Find the magnitudes of the velocity and acceleration at $t=0$. (04)

**Answer:**

The position vector of the particle is:

$$
\vec{r}(t) = e^{-t}\hat{i} + 2\cos 3t\hat{j} + 2\sin 3t\hat{k}
$$

#### 1. Magnitude of Velocity

Differentiate the position vector to find the velocity vector:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt} = -e^{-t}\hat{i} - 6\sin 3t\hat{j} + 6\cos 3t\hat{k}
$$

At $t=0$:

$$
\vec{v}(0) = -\hat{i} - 0\hat{j} + 6\hat{k} = -\hat{i} + 6\hat{k}
$$

The magnitude is:

$$
|\vec{v}(0)| = \sqrt{(-1)^2 + 6^2} = \sqrt{1 + 36} = \sqrt{37}
$$

#### 2. Magnitude of Acceleration

Differentiate the velocity vector to find the acceleration vector:

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = e^{-t}\hat{i} - 18\cos 3t\hat{j} - 18\sin 3t\hat{k}
$$

At $t=0$:

$$
\vec{a}(0) = \hat{i} - 18\hat{j} - 0\hat{k} = \hat{i} - 18\hat{j}
$$

The magnitude is:

$$
|\vec{a}(0)| = \sqrt{1^2 + (-18)^2} = \sqrt{1 + 324} = \sqrt{325} = 5\sqrt{13}
$$

---

### Q2(b) For the space curve $x = t, y = t^2, z = \frac{2}{3}t^3$, find the curvature $K$ and the torsion $T$. (05)

**Answer:**

We write the curve as a vector function:

$$
\vec{r}(t) = t\hat{i} + t^2\hat{j} + \frac{2}{3}t^3\hat{k}
$$

Calculate the first three derivatives of $\vec{r}$:

$$
\vec{r}'(t) = \hat{i} + 2t\hat{j} + 2t^2\hat{k}
$$

$$
\vec{r}''(t) = 2\hat{j} + 4t\hat{k}
$$

$$
\vec{r}'''(t) = 4\hat{k}
$$

Calculate the cross product of the first two derivatives:

$$
\vec{r}' \times \vec{r}'' = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
1 & 2t & 2t^2 \\
0 & 2 & 4t
\end{vmatrix} = \hat{i}(8t^2 - 4t^2) - \hat{j}(4t - 0) + \hat{k}(2 - 0) = 4t^2\hat{i} - 4t\hat{j} + 2\hat{k}
$$

Find the magnitudes:

$$
|\vec{r}'| = \sqrt{1 + 4t^2 + 4t^4} = \sqrt{(2t^2 + 1)^2} = 2t^2 + 1
$$

$$
|\vec{r}' \times \vec{r}''| = \sqrt{16t^4 + 16t^2 + 4} = 2\sqrt{4t^4 + 4t^2 + 1} = 2(2t^2 + 1)
$$

#### 1. Curvature $K$

$$
K = \frac{|\vec{r}' \times \vec{r}''|}{|\vec{r}'|^3} = \frac{2(2t^2 + 1)}{(2t^2 + 1)^3} = \frac{2}{(2t^2 + 1)^2}
$$

#### 2. Torsion $T$

Calculate the scalar triple product:

$$
(\vec{r}' \times \vec{r}'') \cdot \vec{r}''' = (4t^2\hat{i} - 4t\hat{j} + 2\hat{k}) \cdot 4\hat{k} = 8
$$

$$
T = \frac{(\vec{r}' \times \vec{r}'') \cdot \vec{r}'''}{|\vec{r}' \times \vec{r}''|^2} = \frac{8}{4(2t^2 + 1)^2} = \frac{2}{(2t^2 + 1)^2}
$$

So the curvature and the torsion are equal:

$$
K = T = \frac{2}{(2t^2 + 1)^2}
$$

---

### Q2(c) Show that, $\nabla\Phi$ is a vector perpendicular to the surface $\Phi(x, y, z) = C$, where $C$ is a constant. (03)

**Answer:**

Let $P$ be a point on the surface $\Phi(x, y, z) = C$. Let the vector function:

$$
\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}
$$

define any curve that lies entirely on the surface and passes through $P$.

Since all points of the curve lie on the surface, they satisfy the surface equation:

$$
\Phi(x(t), y(t), z(t)) = C
$$

Differentiate this equation with respect to $t$ using the chain rule:

$$
\frac{\partial\Phi}{\partial x}\frac{dx}{dt} + \frac{\partial\Phi}{\partial y}\frac{dy}{dt} + \frac{\partial\Phi}{\partial z}\frac{dz}{dt} = 0
$$

We can write this as a dot product:

$$
\left( \frac{\partial\Phi}{\partial x}\hat{i} + \frac{\partial\Phi}{\partial y}\hat{j} + \frac{\partial\Phi}{\partial z}\hat{k} \right) \cdot \left( \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j} + \frac{dz}{dt}\hat{k} \right) = 0
$$

$$
\vec{\nabla}\Phi \cdot \frac{d\vec{r}}{dt} = 0
$$

Here the vector $\frac{d\vec{r}}{dt}$ is a tangent vector to the curve. Because the dot product is zero, $\vec{\nabla}\Phi$ is perpendicular to this tangent vector.

Since this relation holds for any curve on the surface passing through $P$, the gradient vector $\vec{\nabla}\Phi$ is perpendicular to the surface.

---

### Q3(a) Show that, 

$$
\bar{A} = (6xy + z^3)\hat{i} + (3x^2 - z)\hat{j} + (3xz^2 - y)\hat{k}
$$

 is irrotational. Find $\Phi$ such that $\bar{A} = \nabla\Phi$. (06)

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

### Q3(b) Find the work done in moving a particle in the force field 

$$
\vec{F} = (3x^2 + 6y)\hat{i} - 14yz\hat{j} + 20xz^2\hat{k}
$$

 along: (06)
*   **(i)** The curve defined by $x = t, y = t^2, z = t^3$ from $t=0$ to $t=1$.
*   **(ii)** The straight line joining $(0, 0, 0)$ and $(1, 1, 1)$.

**Answer:**

We write the line integral representing the work done:

$$
W = \int_C \vec{F} \cdot d\vec{r} = \int_C \left[ (3x^2 + 6y)dx - 14yz dy + 20xz^2 dz \right]
$$

#### Path (i): Parametric Curve

The differentials are:

$$
dx = dt, \quad dy = 2t dt, \quad dz = 3t^2 dt
$$

Substitute the variables and differentials into the integral:

$$
W = \int_0^1 \left[ (3t^2 + 6t^2)dt - 14(t^2)(t^3)(2t dt) + 20(t)(t^3)^2 (3t^2 dt) \right]
$$

$$
W = \int_0^1 \left( 9t^2 - 28t^6 + 60t^9 \right) dt
$$

Integrate the terms:

$$
W = \left[ 3t^3 - 4t^7 + 6t^{10} \right]_0^1 = 3 - 4 + 6 = 5
$$

So the work done along this curve is $5$.

#### Path (ii): Straight Line

The path is defined by $x = t, y = t, z = t$ from $t=0$ to $1$. The differentials are $dx = dy = dz = dt$. Substitute these:

$$
W = \int_0^1 \left[ (3t^2 + 6t)dt - 14(t)(t)dt + 20(t)(t)^2 dt \right]
$$

$$
W = \int_0^1 \left( 20t^3 - 11t^2 + 6t \right) dt
$$

Integrate the terms:

$$
W = \left[ 5t^4 - \frac{11}{3}t^3 + 3t^2 \right]_0^1 = 5 - \frac{11}{3} + 3 = 8 - \frac{11}{3} = \frac{13}{3}
$$

So the work done along this straight line is $\frac{13}{3}$.

---

### Q4(a) Evaluate 

$$
\iint_S \bar{A} \cdot \hat{n} dS
$$

 where, 

$$
\bar{A} = z\hat{i} + x\hat{j} - 3y^2z\hat{k}
$$

 and $S$ is the surface of the cylinder $x^2 + y^2 = 16$ included in the first octant between $z=0$ and $z=5$. (06)

**Answer:**

Let the surface be defined by the function:

$$
g(x, y, z) = x^2 + y^2 - 16 = 0
$$

The gradient of $g$ gives:

$$
\vec{\nabla}g = 2x\hat{i} + 2y\hat{j}
$$

The unit outward normal vector $\hat{n}$ is:

$$
\hat{n} = \frac{2x\hat{i} + 2y\hat{j}}{\sqrt{4x^2 + 4y^2}} = \frac{x\hat{i} + y\hat{j}}{4}
$$

Find the dot product $\vec{A} \cdot \hat{n}$:

$$
\vec{A} \cdot \hat{n} = (z\hat{i} + x\hat{j} - 3y^2z\hat{k}) \cdot \left( \frac{x\hat{i} + y\hat{j}}{4} \right) = \frac{xz + xy}{4}
$$

We project the cylinder surface $S$ onto the $yz$-plane. The projection region $R$ is:

$$
y \in [0, 4], \quad z \in [0, 5]
$$

The surface area element $dS$ is:

$$
dS = \frac{dydz}{|\hat{n} \cdot \hat{i}|} = \frac{dydz}{|x/4|} = \frac{4}{x} dydz
$$

Set up the double integral over the region $R$:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \iint_R \left( \frac{xz + xy}{4} \right) \left( \frac{4}{x} dydz \right) = \iint_R (z + y) dydz
$$

Set up the limits:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \int_{y=0}^4 \int_{z=0}^5 (y + z) dz dy
$$

Integrate with respect to $z$:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \int_0^4 \left[ yz + \frac{z^2}{2} \right]_0^5 dy = \int_0^4 \left( 5y + \frac{25}{2} \right) dy
$$

Integrate with respect to $y$:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \left[ \frac{5y^2}{2} + \frac{25}{2}y \right]_0^4 = 40 + 50 = 90
$$

So the value of the surface integral is $90$.

---

### Q4(b) Verify Green's theorem in the plane for 

$$
\oint_C (xy + y^2)dx + x^2dy
$$

 where $C$ is a closed region bounded by $y = x$ and $y = x^2$. (06)

**Answer:**

Green's Theorem states:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA
$$

We identify the functions:

$$
P = xy + y^2 \implies \frac{\partial P}{\partial y} = x + 2y
$$

$$
Q = x^2 \implies \frac{\partial Q}{\partial x} = 2x
$$

Substitute these:

$$
\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 2x - (x + 2y) = x - 2y
$$

#### 1. Evaluate Double Integral

The boundaries intersect at $(0,0)$ and $(1,1)$. We integrate:

$$
\iint_R (x - 2y) dA = \int_{x=0}^1 \int_{y=x^2}^x (x - 2y) dy dx
$$

Integrate with respect to $y$:

$$
\iint_R (x - 2y) dA = \int_0^1 \left[ xy - y^2 \right]_{x^2}^x dx = \int_0^1 \left[ 0 - (x^3 - x^4) \right] dx = \int_0^1 (x^4 - x^3) dx
$$

Integrate with respect to $x$:

$$
\iint_R (x - 2y) dA = \left[ \frac{x^5}{5} - \frac{x^4}{4} \right]_0^1 = \frac{1}{5} - \frac{1}{4} = -\frac{1}{20}
$$

#### 2. Evaluate Line Integral

The closed path $C$ has two parts:
1.  Path $C\_1$ ($y = x^2$, $dy = 2x dx$) from $(0,0)$ to $(1,1)$.
2.  Path $C\_2$ ($y = x$, $dy = dx$) from $(1,1)$ to $(0,0)$.

Evaluate along Path $C\_1$:

$$
\int_{C_1} (xy + y^2)dx + x^2dy = \int_0^1 \left[ (x^3 + x^4)dx + x^2(2x dx) \right] = \int_0^1 (3x^3 + x^4) dx
$$

$$
\int_{C_1} = \left[ \frac{3}{4}x^4 + \frac{x^5}{5} \right]_0^1 = \frac{3}{4} + \frac{1}{5} = \frac{19}{20}
$$

Evaluate along Path $C\_2$:

$$
\int_{C_2} (xy + y^2)dx + x^2dy = \int_1^0 \left[ (x^2 + x^2)dx + x^2 dx \right] = \int_1^0 3x^2 dx = \left[ x^3 \right]_1^0 = -1
$$

Add the line integrals together:

$$
\oint_C = \frac{19}{20} - 1 = -\frac{1}{20}
$$

Both integrals give $-\frac{1}{20}$. So Green's theorem is verified.

---

## SECTION - B

### Q5(a) For two matrices $A$ and $B$, prove that $(AB)' = B'A'$. (03)

**Answer:**

Let $A$ be an $m \times n$ matrix and $B$ be an $n \times p$ matrix. Let the product matrix be $C = AB$.

The $(i, j)$-th element of $C$ is:

$$
c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}
$$

The transpose element $(C')\_{ij}$ is defined as the $(j, i)$-th element of $C$:

$$
(C')_{ij} = c_{ji} = \sum_{k=1}^n a_{jk} b_{ki}
$$

Now look at the product of the transposes $B' A'$. The $(i, j)$-th element of this product is:

$$
(B'A')_{ij} = \sum_{k=1}^n (B')_{ik} (A')_{kj}
$$

Using the transpose definitions $(B')\_{ik} = b\_{ki}$ and $(A')\_{kj} = a\_{jk}$, we substitute:

$$
(B'A')_{ij} = \sum_{k=1}^n b_{ki} a_{jk} = \sum_{k=1}^n a_{jk} b_{ki}
$$

Since $(AB)'\_{ij} = (B'A')\_{ij}$ for all indices, we get:

$$
(AB)' = B'A'
$$

The proof is complete.

---

### Q5(b) Show that every square matrix can be uniquely expressed as the sum of a symmetric and a skew symmetric matrices. (04)

**Answer:**

Let $A$ be a square matrix. We can decompose $A$ as:

$$
A = \frac{1}{2}(A + A^T) + \frac{1}{2}(A - A^T)
$$

Let $P = \frac{1}{2}(A + A^T)$ and $Q = \frac{1}{2}(A - A^T)$.

#### 1. Show $P$ is symmetric

Calculate the transpose of $P$:

$$
P^T = \left[ \frac{1}{2}(A + A^T) \right]^T = \frac{1}{2}(A^T + (A^T)^T) = \frac{1}{2}(A^T + A) = P
$$

So $P$ is symmetric.

#### 2. Show $Q$ is skew-symmetric

Calculate the transpose of $Q$:

$$
Q^T = \left[ \frac{1}{2}(A - A^T) \right]^T = \frac{1}{2}(A^T - (A^T)^T) = \frac{1}{2}(A^T - A) = -Q
$$

So $Q$ is skew-symmetric.

#### 3. Prove Uniqueness

Suppose there is another decomposition:

$$
A = P' + Q'
$$

where $P'$ is symmetric and $Q'$ is skew-symmetric. Taking the transpose:

$$
A^T = (P' + Q')^T = P'^T + Q'^T = P' - Q'
$$

We solve the equations:
1.  $P' + Q' = A$
2.  $P' - Q' = A^T$

Adding them gives:

$$
2P' = A + A^T \implies P' = \frac{1}{2}(A + A^T) = P
$$

Subtracting them gives:

$$
2Q' = A - A^T \implies Q' = \frac{1}{2}(A - A^T) = Q
$$

The decomposition is unique.

---

### Q5(c) Define inverse of a matrix. Find the adjoint of matrix $A$ and hence find $A^{-1}$, where: (05)

$$
A = \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

**Answer:**

#### 1. Definition

Let $A$ be a square matrix. If there is a matrix $B$ such that $AB = BA = I$, then $B$ is the inverse of $A$ (written as $A^{-1}$).

#### 2. Find Adjoint and Inverse

We find the determinant of $A$:

$$
|A| = 1(\cos^2\theta - (-\sin^2\theta)) = \cos^2\theta + \sin^2\theta = 1
$$

Find the cofactors $C\_{ij}$:

$$
C_{11} = \cos\theta, \quad C_{12} = -\sin\theta, \quad C_{13} = 0
$$

$$
C_{21} = \sin\theta, \quad C_{22} = \cos\theta, \quad C_{23} = 0
$$

$$
C_{31} = 0, \quad C_{32} = 0, \quad C_{33} = 1
$$

This gives the cofactor matrix $C$:

$$
C = \begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

The adjoint matrix is the transpose of the cofactor matrix:

$$
\text{adj}(A) = C^T = \begin{bmatrix}
\cos\theta & \sin\theta & 0 \\
-\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Since the determinant is 1, the inverse is:

$$
A^{-1} = \frac{1}{|A|} \text{adj}(A) = \begin{bmatrix}
\cos\theta & \sin\theta & 0 \\
-\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

---

### Q6(a) What is the rank of a matrix? Find the rank of the matrix, 

$$
A = \begin{bmatrix}
6 & 1 & 8 & 3 \\
2 & 1 & 0 & 2 \\
4 & -1 & -8 & -3
\end{bmatrix}
$$

(05)

**Answer:**

#### 1. Definition of Rank

The rank of a matrix is the maximum number of linearly independent row vectors in the matrix.

#### 2. Find the Rank

Let the matrix be:

$$
A = \begin{bmatrix}
6 & 1 & 8 & 3 \\
2 & 1 & 0 & 2 \\
4 & -1 & -8 & -3
\end{bmatrix}
$$

We swap row 1 and row 2 ($R\_1 \leftrightarrow R\_2$):

$$
\begin{bmatrix}
2 & 1 & 0 & 2 \\
6 & 1 & 8 & 3 \\
4 & -1 & -8 & -3
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 3R\_1$
*   $R\_3 \to R\_3 - 2R\_1$

This gives:

$$
\begin{bmatrix}
2 & 1 & 0 & 2 \\
0 & -2 & 8 & -3 \\
0 & -3 & -8 & -7
\end{bmatrix}
$$

Perform the operation $R\_3 \to 2R\_3 - 3R\_2$:

$$
\begin{bmatrix}
2 & 1 & 0 & 2 \\
0 & -2 & 8 & -3 \\
0 & 0 & -40 & -5
\end{bmatrix}
$$

All three rows are non-zero. So the rank of the matrix is $3$.

---

### Q6(b) Investigate for what values of $\lambda$ and $\mu$ the following system of equations have (i) no solution, (ii) unique solution, (iii) infinite number of solutions: (07)

$$
x + y + z = 6
$$

$$
x + 2y + 3z = 10
$$

$$
x + 2y + \lambda z = \mu
$$

**Answer:**

We write the augmented matrix of the system:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 6 \\
1 & 2 & 3 & | & 10 \\
1 & 2 & \lambda & | & \mu
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - R\_1$
*   $R\_3 \to R\_3 - R\_1$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 6 \\
0 & 1 & 2 & | & 4 \\
0 & 1 & \lambda - 1 & | & \mu - 6
\end{bmatrix}
$$

Now eliminate row 3 using row 2 ($R\_3 \to R\_3 - R\_2$):

$$
\begin{bmatrix}
1 & 1 & 1 & | & 6 \\
0 & 1 & 2 & | & 4 \\
0 & 0 & \lambda - 3 & | & \mu - 10
\end{bmatrix}
$$

Now we investigate:

#### (i) No Solution

A contradiction occurs if the last row is of the form $[0, 0, 0 | c]$ with $c \neq 0$:

$$
\lambda - 3 = 0 \quad \text{and} \quad \mu - 10 \neq 0 \implies \lambda = 3 \quad \text{and} \quad \mu \neq 10
$$

#### (ii) Unique Solution

A unique solution exists if the rank of the coefficient matrix is 3:

$$
\lambda - 3 \neq 0 \implies \lambda \neq 3
$$

for any value of $\mu$.

#### (iii) Infinite Solutions

Infinite solutions exist if the last row is entirely zero:

$$
\lambda - 3 = 0 \quad \text{and} \quad \mu - 10 = 0 \implies \lambda = 3 \quad \text{and} \quad \mu = 10
$$

---

### Q7(a) Find the eigen values and the corresponding eigen vectors for the matrix 

$$
A = \begin{bmatrix}
1 & 1 & -2 \\
-1 & 2 & 1 \\
0 & 1 & -1
\end{bmatrix}
$$

(06)

**Answer:**

#### 1. Find Eigenvalues

We solve the characteristic equation $|A - \lambda I| = 0$:

$$
\begin{vmatrix}
1-\lambda & 1 & -2 \\
-1 & 2-\lambda & 1 \\
0 & 1 & -1-\lambda
\end{vmatrix} = 0
$$

Expanding the determinant yields the equation:

$$
\lambda^3 - 2\lambda^2 - \lambda + 2 = 0
$$

Factor the expression:

$$
(\lambda - 1)(\lambda + 1)(\lambda - 2) = 0
$$

So the eigenvalues are:

$$
\lambda = 1, \quad \lambda = -1, \quad \lambda = 2
$$

#### 2. Find Eigenvectors

##### Case 1: For $\lambda = 1$

We solve $(A - I)X = 0$:

$$
\begin{bmatrix}
0 & 1 & -2 \\
-1 & 1 & 1 \\
0 & 1 & -2
\end{bmatrix} \begin{bmatrix}
x \\
y \\
z
\end{bmatrix} = \begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$

From row 1:

$$
y - 2z = 0 \implies y = 2z
$$

From row 2:

$$
-x + y + z = 0 \implies x = y + z = 3z
$$

Let $z = 1$. The eigenvector is:

$$
X_1 = \begin{bmatrix}
3 \\
2 \\
1
\end{bmatrix}
$$

##### Case 2: For $\lambda = -1$

We solve $(A + I)X = 0$:

$$
\begin{bmatrix}
2 & 1 & -2 \\
-1 & 3 & 1 \\
0 & 1 & 0
\end{bmatrix} \begin{bmatrix}
x \\
y \\
z
\end{bmatrix} = \begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$

From row 3:

$$
y = 0
$$

From row 1:

$$
2x - 2z = 0 \implies x = z
$$

Let $z = 1$. The eigenvector is:

$$
X_2 = \begin{bmatrix}
1 \\
0 \\
1
\end{bmatrix}
$$

##### Case 3: For $\lambda = 2$

We solve $(A - 2I)X = 0$:

$$
\begin{bmatrix}
-1 & 1 & -2 \\
-1 & 0 & 1 \\
0 & 1 & -3
\end{bmatrix} \begin{bmatrix}
x \\
y \\
z
\end{bmatrix} = \begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$

From row 2:

$$
-x + z = 0 \implies x = z
$$

From row 3:

$$
y - 3z = 0 \implies y = 3z
$$

Let $z = 1$. The eigenvector is:

$$
X_3 = \begin{bmatrix}
1 \\
3 \\
1
\end{bmatrix}
$$

---

### Q7(b) Solve the following system of differential equations by matrix method: (06)

$$
\frac{dx}{dt} = 6x - 3y
$$

$$
\frac{dy}{dt} = 2x + y
$$

**Answer:**

We write the system in matrix form:

$$
\frac{dX}{dt} = M X, \quad \text{where } M = \begin{bmatrix}
6 & -3 \\
2 & 1
\end{bmatrix}
$$

First we find the eigenvalues of $M$ by solving $|M - \lambda I| = 0$:

$$
\begin{vmatrix}
6-\lambda & -3 \\
2 & 1-\lambda
\end{vmatrix} = 0 \implies (6-\lambda)(1-\lambda) + 6 = \lambda^2 - 7\lambda + 12 = 0
$$

$$
(\lambda - 3)(\lambda - 4) = 0 \implies \lambda = 3 \quad \text{or} \quad \lambda = 4
$$

Now find the eigenvectors:
*   **For $\lambda = 3$:**

$$
M - 3I = \begin{bmatrix}
3 & -3 \\
2 & -2
\end{bmatrix} \implies 3x - 3y = 0 \implies x = y
$$

The eigenvector is:

$$
v_1 = \begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

*   **For $\lambda = 4$:**

$$
M - 4I = \begin{bmatrix}
2 & -3 \\
2 & -3
\end{bmatrix} \implies 2x - 3y = 0 \implies x = \frac{3}{2}y
$$

The eigenvector (for $y=2$) is:

$$
v_2 = \begin{bmatrix}
3 \\
2
\end{bmatrix}
$$

The general solution is a linear combination of the fundamental solutions:

$$
\begin{bmatrix}
x(t) \\
y(t)
\end{bmatrix} = C_1 e^{3t} \begin{bmatrix}
1 \\
1
\end{bmatrix} + C_2 e^{4t} \begin{bmatrix}
3 \\
2
\end{bmatrix}
$$

So the system solution is:

$$
x(t) = C_1 e^{3t} + 3C_2 e^{4t}
$$

$$
y(t) = C_1 e^{3t} + 2C_2 e^{4t}
$$

---

### Q8(a) Write the vector $v = (1, -2, 5)$ as a linear combination of the vectors $e\_1 = (1, 1, 1)$, $e\_2 = (1, 2, 3)$ and $e\_3 = (2, -1, 1)$. (04)

**Answer:**

We write the relation:

$$
v = c_1 e_1 + c_2 e_2 + c_3 e_3 \implies (1, -2, 5) = c_1(1, 1, 1) + c_2(1, 2, 3) + c_3(2, -1, 1)
$$

This gives the system of equations:

$$
c_1 + c_2 + 2c_3 = 1
$$

$$
c_1 + 2c_2 - c_3 = -2
$$

$$
c_1 + 3c_2 + c_3 = 5
$$

We write the augmented matrix of this system:

$$
\begin{bmatrix}
1 & 1 & 2 & | & 1 \\
1 & 2 & -1 & | & -2 \\
1 & 3 & 1 & | & 5
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - R\_1$
*   $R\_3 \to R\_3 - R\_1$

This gives:

$$
\begin{bmatrix}
1 & 1 & 2 & | & 1 \\
0 & 1 & -3 & | & -3 \\
0 & 2 & -1 & | & 4
\end{bmatrix}
$$

Now perform the operation $R\_3 \to R\_3 - 2R\_2$:

$$
\begin{bmatrix}
1 & 1 & 2 & | & 1 \\
0 & 1 & -3 & | & -3 \\
0 & 0 & 5 & | & 10
\end{bmatrix}
$$

By back substitution, we solve the coefficients:
*   From the third row: $5c\_3 = 10 \implies c\_3 = 2$.
*   From the second row: $c\_2 - 3(2) = -3 \implies c\_2 = 3$.
*   From the first row: $c\_1 + 3 + 2(2) = 1 \implies c\_1 = -6$.

So the linear combination is:

$$
v = -6e_1 + 3e_2 + 2e_3
$$

---

### Q8(b) Suppose the vectors $u, v, w$ are linearly independent. Show that the vectors $u + v, u - v, u - 2v + w$ are also linearly independent. (04)

**Answer:**

We set a linear combination of these vectors equal to the zero vector:

$$
c_1 (u + v) + c_2 (u - v) + c_3 (u - 2v + w) = 0
$$

Group the terms by vectors $u, v,$ and $w$:

$$
(c_1 + c_2 + c_3) u + (c_1 - c_2 - 2c_3) v + c_3 w = 0
$$

Since the vectors $u, v, w$ are linearly independent, their coefficients must equal zero:

$$
c_1 + c_2 + c_3 = 0 \quad \dots \text{(1)}
$$

$$
c_1 - c_2 - 2c_3 = 0 \quad \dots \text{(2)}
$$

$$
c_3 = 0 \quad \dots \text{(3)}
$$

Substitute $c\_3 = 0$ from equation (3) into equations (1) and (2):

$$
c_1 + c_2 = 0
$$

$$
c_1 - c_2 = 0
$$

Adding these equations gives $2c\_1 = 0 \implies c\_1 = 0$. This then gives $c\_2 = 0$.

Since the only solution is $c\_1 = c\_2 = c\_3 = 0$, the vectors $u + v$, $u - v$, and $u - 2v + w$ are linearly independent.

---

### Q8(c) Let $w$ be the space generated by the polynomials: (04)

$$
v_1 = t^3 - 2t^2 + 4t + 1
$$

$$
v_2 = 2t^3 - 3t^2 + 9t - 1
$$

$$
v_3 = t^3 + 6t - 5
$$

$$
v_4 = 2t^3 - 5t^2 + 7t + 5
$$

Find a basis and the dimension of $w$.

**Answer:**

We represent each polynomial as a coordinate vector in the standard basis $\{t^3, t^2, t, 1\}$:

$$
v_1 = (1, -2, 4, 1), \quad v_2 = (2, -3, 9, -1), \quad v_3 = (1, 0, 6, -5), \quad v_4 = (2, -5, 7, 5)
$$

We write these vectors as the rows of a matrix:

$$
\begin{bmatrix}
1 & -2 & 4 & 1 \\
2 & -3 & 9 & -1 \\
1 & 0 & 6 & -5 \\
2 & -5 & 7 & 5
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 2R\_1$
*   $R\_3 \to R\_3 - R\_1$
*   $R\_4 \to R\_4 - 2R\_1$

This gives:

$$
\begin{bmatrix}
1 & -2 & 4 & 1 \\
0 & 1 & 1 & -3 \\
0 & 2 & 2 & -6 \\
0 & -1 & -1 & 3
\end{bmatrix}
$$

Now perform operations on row 3 and row 4:
*   $R\_3 \to R\_3 - 2R\_2$
*   $R\_4 \to R\_4 + R\_2$

This gives the echelon form:

$$
\begin{bmatrix}
1 & -2 & 4 & 1 \\
0 & 1 & 1 & -3 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

The non-zero rows form the basis vectors for the subspace:

$$
\text{Basis} = \{ t^3 - 2t^2 + 4t + 1, \quad t^2 + t - 3 \}
$$

The number of polynomials in the basis is 2, so the dimension is:

$$
\text{Dimension} = 2
$$

---

[⬅ 2019](2019_answer.md) | [🏠 Index](00-index.md) | [2021 ➡](2021_answer.md)
