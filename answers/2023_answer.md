[⬅ 2021](2021_answer.md) | [🏠 Index](00-index.md) | [2024 ➡](2024_answer.md)

---

# B.Sc. Engineering 2nd Year Odd Semester Examination, 2023
**Course No: Math 2117**
**Course Title: Vector Analysis & Linear Algebra**
**Time: 03 Hours**
**Full Marks: 60**

---

## SECTION - A

### Q1(a) Determine a unit vector perpendicular to the plane of 

$$
\bar{A} = 2\hat{i} - 6\hat{j} - 3\hat{k}
$$

 and 

$$
\bar{B} = 4\hat{i} + 3\hat{j} - \hat{k}
$$

(03)

**Answer:**

We calculate the cross product of $\bar{A}$ and $\bar{B}$ to get a perpendicular vector:

$$
\vec{A} \times \vec{B} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
2 & -6 & -3 \\
4 & 3 & -1
\end{vmatrix} = \hat{i}(6 - (-9)) - \hat{j}(-2 - (-12)) + \hat{k}(6 - (-24)) = 15\hat{i} - 10\hat{j} + 30\hat{k}
$$

Find the magnitude of this cross product:

$$
|\vec{A} \times \vec{B}| = \sqrt{15^2 + (-10)^2 + 30^2} = \sqrt{225 + 100 + 900} = \sqrt{1225} = 35
$$

The unit vector perpendicular to the plane is:

$$
\hat{n} = \pm \frac{15\hat{i} - 10\hat{j} + 30\hat{k}}{35} = \pm \left( \frac{3}{7}\hat{i} - \frac{2}{7}\hat{j} + \frac{6}{7}\hat{k} \right)
$$

---

### Q1(b) Find the area of a triangle with vertices at $(3, -1, 2)$, $(1, -1, -3)$ and $(4, -3, 1)$. (03)

**Answer:**

Let the vertices of the triangle be $P(3, -1, 2)$, $Q(1, -1, -3)$, and $R(4, -3, 1)$. We construct two side vectors starting from point $P$:

$$
\vec{PQ} = (1 - 3)\hat{i} + (-1 - (-1))\hat{j} + (-3 - 2)\hat{k} = -2\hat{i} - 5\hat{k}
$$

$$
\vec{PR} = (4 - 3)\hat{i} + (-3 - (-1))\hat{j} + (1 - 2)\hat{k} = \hat{i} - 2\hat{j} - \hat{k}
$$

Calculate the cross product of these side vectors:

$$
\vec{PQ} \times \vec{PR} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
-2 & 0 & -5 \\
1 & -2 & -1
\end{vmatrix} = \hat{i}(0 - 10) - \hat{j}(2 - (-5)) + \hat{k}(4 - 0) = -10\hat{i} - 7\hat{j} + 4\hat{k}
$$

Find the magnitude of the cross product:

$$
|\vec{PQ} \times \vec{PR}| = \sqrt{(-10)^2 + (-7)^2 + 4^2} = \sqrt{100 + 49 + 16} = \sqrt{165}
$$

The area of the triangle is:

$$
\text{Area} = \frac{1}{2}|\vec{PQ} \times \vec{PR}| = \frac{1}{2}\sqrt{165}
$$

---

### Q1(c) Given the space curve $x = t, y = t^2, z = \frac{2}{3}t^3$, find the torsion $\tau$. (04)

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
\end{vmatrix} = 4t^2\hat{i} - 4t\hat{j} + 2\hat{k}
$$

Find the magnitudes:

$$
|\vec{r}' \times \vec{r}''| = \sqrt{16t^4 + 16t^2 + 4} = 2\sqrt{4t^4 + 4t^2 + 1} = 2(2t^2 + 1)
$$

Calculate the scalar triple product:

$$
(\vec{r}' \times \vec{r}'') \cdot \vec{r}''' = (4t^2\hat{i} - 4t\hat{j} + 2\hat{k}) \cdot 4\hat{k} = 8
$$

The torsion $\tau$ is:

$$
\tau = \frac{(\vec{r}' \times \vec{r}'') \cdot \vec{r}'''}{|\vec{r}' \times \vec{r}''|^2} = \frac{8}{4(2t^2 + 1)^2} = \frac{2}{(2t^2 + 1)^2}
$$

So the torsion is

$$
\tau = \frac{2}{(2t^2 + 1)^2}.
$$

---

### Q2(a) Determine the angles $\alpha, \beta$, and $\gamma$ which the vector 

$$
\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}
$$

makes with the positive directions of the coordinate axes and show that

$$
\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1
$$

. (03)

**Answer:**

Let the magnitude of the position vector $\vec{r}$ be:

$$
r = |\vec{r}| = \sqrt{x^2 + y^2 + z^2}
$$

The cosine of the angles made with the coordinate axes are given by:

$$
\cos\alpha = \frac{\vec{r} \cdot \hat{i}}{r} = \frac{x}{r}
$$

$$
\cos\beta = \frac{\vec{r} \cdot \hat{j}}{r} = \frac{y}{r}
$$

$$
\cos\gamma = \frac{\vec{r} \cdot \hat{k}}{r} = \frac{z}{r}
$$

Sum the squares of these cosines:

$$
\cos^2\alpha + \cos^2\beta + \cos^2\gamma = \frac{x^2}{r^2} + \frac{y^2}{r^2} + \frac{z^2}{r^2} = \frac{x^2 + y^2 + z^2}{r^2} = \frac{r^2}{r^2} = 1
$$

This completes the proof.

---

### Q2(b) Find the constant 'a' such that the vectors 

$$
2\hat{i} - \hat{j} + \hat{k}
$$

$$
\hat{i} + 2\hat{j} - 3\hat{k}
$$

 and 

$$
3\hat{i} + a\hat{j} + 5\hat{k}
$$

 are coplanar. (03)

**Answer:**

Three vectors are coplanar if and only if their scalar triple product is zero. We set up the determinant:

$$
\begin{vmatrix}
2 & -1 & 1 \\
1 & 2 & -3 \\
3 & a & 5
\end{vmatrix} = 0
$$

Expand this determinant along the first row:

$$
2(10 - (-3a)) - (-1)(5 - (-9)) + 1(a - 6) = 0
$$

$$
2(10 + 3a) + 14 + a - 6 = 0
$$

$$
20 + 6a + 14 + a - 6 = 0
$$

$$
7a + 28 = 0 \implies 7a = -28 \implies a = -4
$$

So the constant is $a = -4$.

---

### Q2(c) A particle moves along the curve $x = 2t^2, y = t^2 - 4t, z = 3t - 5$, where $t$ is the time. Find the components of its velocity and acceleration at time $t=1$ in the direction 

$$
\hat{i} - 3\hat{j} + 2\hat{k}
$$

(04)

**Answer:**

Let the direction vector be 

$$
\vec{d} = \hat{i} - 3\hat{j} + 2\hat{k}
$$

The unit direction vector $\hat{u}$ is:

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

### Q3(a) State and Prove Stokes' theorem. (05)

**Answer:**

#### Statement

Let $S$ be an open, two-sided surface bounded by a closed, non-self-intersecting curve $C$. If $\vec{A}$ has continuous first-order partial derivatives, then:

$$
\oint_C \vec{A} \cdot d\vec{r} = \iint_S (\vec{\nabla} \times \vec{A}) \cdot \hat{n} dS
$$

Here the boundary curve $C$ is traversed in the positive (counterclockwise) direction.

#### Proof

Let us prove this for a surface $S$ which can be projected uniquely onto coordinate planes. Let the surface equation be $z = f(x, y)$ over a region $R$ in the $xy$-plane.

Let the vector field be:

$$
\vec{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}
$$

We prove the identity for the component $A\_1$:

$$
\oint_C A_1 dx = \iint_S \left[ \vec{\nabla} \times (A_1\hat{i}) \right] \cdot \hat{n} dS \quad \dots \text{(1)}
$$

Since the curve $C$ is the boundary of the surface $z = f(x, y)$, we project the line integral onto the $xy$-plane:

$$
\oint_C A_1(x, y, z) dx = \oint_{C'} A_1(x, y, f(x, y)) dx
$$

Apply Green's theorem in the plane to the projected curve $C'$:

$$
\oint_{C'} A_1(x, y, f(x, y)) dx = \iint_R -\frac{\partial}{\partial y} \left[ A_1(x, y, f(x, y)) \right] dA
$$

Using the chain rule, we compute:

$$
\frac{\partial}{\partial y} \left[ A_1(x, y, f(x, y)) \right] = \frac{\partial A_1}{\partial y} + \frac{\partial A_1}{\partial z}\frac{\partial z}{\partial y}
$$

So the integral becomes:

$$
\oint_C A_1 dx = \iint_R \left( -\frac{\partial A_1}{\partial y} - \frac{\partial A_1}{\partial z}\frac{\partial z}{\partial y} \right) dx dy \quad \dots \text{(2)}
$$

Now calculate the term

$$
\vec{\nabla} \times (A\_1\hat{i}):
$$

$$
\vec{\nabla} \times (A_1\hat{i}) = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
A_1 & 0 & 0
\end{vmatrix} = \frac{\partial A_1}{\partial z}\hat{j} - \frac{\partial A_1}{\partial y}\hat{k}
$$

For the surface $z - f(x, y) = 0$, the normal vector gives the relation:

$$
\hat{n} dS = \left( -\frac{\partial z}{\partial x}\hat{i} - \frac{\partial z}{\partial y}\hat{j} + \hat{k} \right) dx dy
$$

Calculate the dot product:

$$
\left[ \vec{\nabla} \times (A_1\hat{i}) \right] \cdot \hat{n} dS = \left( \frac{\partial A_1}{\partial z}\hat{j} - \frac{\partial A_1}{\partial y}\hat{k} \right) \cdot \left( -\frac{\partial z}{\partial x}\hat{i} - \frac{\partial z}{\partial y}\hat{j} + \hat{k} \right) dx dy
$$

$$
\left[ \vec{\nabla} \times (A_1\hat{i}) \right] \cdot \hat{n} dS = \left( -\frac{\partial A_1}{\partial z}\frac{\partial z}{\partial y} - \frac{\partial A_1}{\partial y} \right) dx dy \quad \dots \text{(3)}
$$

Comparing equations (2) and (3) shows that they are equal.

By applying the same projection method for the components $A\_2$ and $A\_3$, we get:

$$
\oint_C A_2 dy = \iint_S \left[ \vec{\nabla} \times (A_2\hat{j}) \right] \cdot \hat{n} dS
$$

$$
\oint_C A_3 dz = \iint_S \left[ \vec{\nabla} \times (A_3\hat{k}) \right] \cdot \hat{n} dS
$$

Adding these three relations gives:

$$
\oint_C \vec{A} \cdot d\vec{r} = \iint_S (\vec{\nabla} \times \vec{A}) \cdot \hat{n} dS
$$

The proof is complete.

---

### Q3(b) Verify Green's theorem in the plane for 

$$
\oint_C (xy + y^2)dx + x^2dy
$$

Where $C$ is the closed curve of the region bounded by $y = x$ and

$$
y = x^2
$$

. (05)

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
1.  Path $C\_1$ (

$$
y = x^2
$$

, $dy = 2x dx$) from $(0,0)$ to $(1,1)$.
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

### Q4(a) Define commutative, idempotent and involutory matrix. (02)

**Answer:**

*   **Commutative Matrices:** Two square matrices $A$ and $B$ are commutative if $AB = BA$.
*   **Idempotent Matrix:** A square matrix $A$ is idempotent if its square equals itself:

$$
A^2 = A.
$$

*   **Involutory Matrix:** A square matrix $A$ is involutory if its square equals the identity matrix:

$$
A^2 = I.
$$

---

### Q4(b) Prove that $(AB)^{-1} = B^{-1}A^{-1}$. (02)

**Answer:**

By definition of the inverse matrix, if a matrix $X$ is the inverse of $AB$, then:

$$
(AB)X = I \quad \text{and} \quad X(AB) = I
$$

We check the candidate matrix $B^{-1}A^{-1}$ by multiplication:

$$
(AB)(B^{-1}A^{-1}) = A(B B^{-1})A^{-1} = A I A^{-1} = A A^{-1} = I
$$

Now check multiplication in the reverse order:

$$
(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1} I B = B^{-1} B = I
$$

Since

$$
(AB)(B^{-1}A^{-1}) = (B^{-1}A^{-1})(AB) = I
$$

, the matrix $B^{-1}A^{-1}$ is the inverse of $AB$. So we write:

$$
(AB)^{-1} = B^{-1}A^{-1}
$$

---

### Q4(c) Reduce the following matrix to the canonical form: (03)

$$
A = \begin{bmatrix}
0 & 0 & 1 & 3 & -2 \\
0 & 1 & 2 & 6 & 0 \\
0 & 2 & 3 & 9 & 2 \\
0 & 1 & 1 & 3 & 2
\end{bmatrix}
$$

**Answer:**

We write the matrix:

$$
A = \begin{bmatrix}
0 & 0 & 1 & 3 & -2 \\
0 & 1 & 2 & 6 & 0 \\
0 & 2 & 3 & 9 & 2 \\
0 & 1 & 1 & 3 & 2
\end{bmatrix}
$$

Swap row 1 and row 2 ($R\_1 \leftrightarrow R\_2$):

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & 3 & -2 \\
0 & 2 & 3 & 9 & 2 \\
0 & 1 & 1 & 3 & 2
\end{bmatrix}
$$

Apply row operations:
*   $R\_3 \to R\_3 - 2R\_1$
*   $R\_4 \to R\_4 - R\_1$

This gives:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & 3 & -2 \\
0 & 0 & -1 & -3 & 2 \\
0 & 0 & -1 & -3 & 2
\end{bmatrix}
$$

Apply row operations:
*   $R\_3 \to R\_3 + R\_2$
*   $R\_4 \to R\_4 + R\_2$

This yields:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & 3 & -2 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

Clear columns using column operations:
*   $C\_3 \to C\_3 - 2C\_2$
*   $C\_4 \to C\_4 - 6C\_2$

This gives:

$$
\begin{bmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 3 & -2 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

Clear column elements using column 3:
*   $C\_4 \to C\_4 - 3C\_3$
*   $C\_5 \to C\_5 + 2C\_3$

This gives:

$$
\begin{bmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

Now swap columns to group the identity matrix blocks. Swap $C\_1 \leftrightarrow C\_2$:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

Swap $C\_2 \leftrightarrow C\_3$:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

This is the canonical form $[I\_2 | 0]$:

$$
\begin{pmatrix}
I_2 & | & 0 \\
-- & - & -- \\
0 & | & 0
\end{pmatrix}
$$

---

### Q4(d) Find the rank of the following matrix: (03)

$$
A = \begin{bmatrix}
1 & 2 & 3 & 2 \\
2 & 3 & 5 & 1 \\
1 & 3 & 4 & 5
\end{bmatrix}
$$

**Answer:**

We write the matrix:

$$
A = \begin{bmatrix}
1 & 2 & 3 & 2 \\
2 & 3 & 5 & 1 \\
1 & 3 & 4 & 5
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 2R\_1$
*   $R\_3 \to R\_3 - R\_1$

This gives:

$$
\begin{bmatrix}
1 & 2 & 3 & 2 \\
0 & -1 & -1 & -3 \\
0 & 1 & 1 & 3
\end{bmatrix}
$$

Add row 2 to row 3 ($R\_3 \to R\_3 + R\_2$):

$$
\begin{bmatrix}
1 & 2 & 3 & 2 \\
0 & -1 & -1 & -3 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

There are 2 non-zero rows in the echelon form. So the rank of the matrix is:

$$
\text{Rank} = 2
$$

---

## SECTION - B

### Q5(a) Show that every square matrix can be expressed as the sum of a Hermitian matrix and a Skew-Hermitian matrix. (05)

**Answer:**

Let $A$ be a square matrix. We write $A$ as:

$$
A = \frac{1}{2}(A + A^\dagger) + \frac{1}{2}(A - A^\dagger)
$$

where

$$
A^\dagger = (\bar{A})^T
$$

is the conjugate transpose of $A$. Let:

$$
P = \frac{1}{2}(A + A^\dagger) \quad \text{and} \quad Q = \frac{1}{2}(A - A^\dagger)
$$

#### 1. Show $P$ is Hermitian

$$
P^\dagger = \left[ \frac{1}{2}(A + A^\dagger) \right]^\dagger = \frac{1}{2}(A^\dagger + (A^\dagger)^\dagger) = \frac{1}{2}(A^\dagger + A) = P
$$

So $P$ is a Hermitian matrix.

#### 2. Show $Q$ is Skew-Hermitian

$$
Q^\dagger = \left[ \frac{1}{2}(A - A^\dagger) \right]^\dagger = \frac{1}{2}(A^\dagger - (A^\dagger)^\dagger) = \frac{1}{2}(A^\dagger - A) = -Q
$$

So $Q$ is a Skew-Hermitian matrix.

So $A = P + Q$ is the sum of a Hermitian matrix and a Skew-Hermitian matrix.

---

### Q5(b) Find the inverse of the matrix 

$$
A = \begin{bmatrix}
1 & 3 & 5 \\
2 & 4 & 5 \\
3 & 7 & 6
\end{bmatrix}
$$

 using row transformation. (05)

**Answer:**

We set up the augmented matrix $[A | I]$:

$$
\begin{bmatrix}
1 & 3 & 5 & | & 1 & 0 & 0 \\
2 & 4 & 5 & | & 0 & 1 & 0 \\
3 & 7 & 6 & | & 0 & 0 & 1
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 2R\_1$
*   $R\_3 \to R\_3 - 3R\_1$

This gives:

$$
\begin{bmatrix}
1 & 3 & 5 & | & 1 & 0 & 0 \\
0 & -2 & -5 & | & -2 & 1 & 0 \\
0 & -2 & -9 & | & -3 & 0 & 1
\end{bmatrix}
$$

Subtract row 2 from row 3 ($R\_3 \to R\_3 - R\_2$):

$$
\begin{bmatrix}
1 & 3 & 5 & | & 1 & 0 & 0 \\
0 & -2 & -5 & | & -2 & 1 & 0 \\
0 & 0 & -4 & | & -1 & -1 & 1
\end{bmatrix}
$$

Multiply row 2 by $-1/2$ and row 3 by $-1/4$:
*   $R\_2 \to -1/2 R\_2$
*   $R\_3 \to -1/4 R\_3$

This gives:

$$
\begin{bmatrix}
1 & 3 & 5 & | & 1 & 0 & 0 \\
0 & 1 & 5/2 & | & 1 & -1/2 & 0 \\
0 & 0 & 1 & | & 1/4 & 1/4 & -1/4
\end{bmatrix}
$$

Perform the operation

$$
R\_2 \to R\_2 - \frac{5}{2}R\_3:
$$

$$
\begin{bmatrix}
1 & 3 & 5 & | & 1 & 0 & 0 \\
0 & 1 & 0 & | & 3/8 & -9/8 & 5/8 \\
0 & 0 & 1 & | & 1/4 & 1/4 & -1/4
\end{bmatrix}
$$

Perform the operation $R\_1 \to R\_1 - 5R\_3$:

$$
\begin{bmatrix}
1 & 3 & 0 & | & -1/4 & -5/4 & 5/4 \\
0 & 1 & 0 & | & 3/8 & -9/8 & 5/8 \\
0 & 0 & 1 & | & 1/4 & 1/4 & -1/4
\end{bmatrix}
$$

Perform the operation $R\_1 \to R\_1 - 3R\_2$:

$$
\begin{bmatrix}
1 & 0 & 0 & | & -11/8 & 17/8 & -5/8 \\
0 & 1 & 0 & | & 3/8 & -9/8 & 5/8 \\
0 & 0 & 1 & | & 1/4 & 1/4 & -1/4
\end{bmatrix}
$$

So the inverse is:

$$
A^{-1} = \frac{1}{8} \begin{bmatrix}
-11 & 17 & -5 \\
3 & -9 & 5 \\
2 & 2 & -2
\end{bmatrix}
$$

---

### Q6(a) Find the eigen values and eigen vectors of the matrix: (05)

$$
A = \begin{bmatrix}
2 & 1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{bmatrix}
$$

**Answer:**

#### 1. Find Eigenvalues

We solve the characteristic equation $|A - \lambda I| = 0$:

$$
\begin{vmatrix}
2-\lambda & 1 & 1 \\
-1 & 2-\lambda & -1 \\
1 & -1 & 2-\lambda
\end{vmatrix} = 0
$$

The expansion of this determinant yields:

$$
(2-\lambda)(\lambda-1)(\lambda-3) = 0
$$

So the eigenvalues are:

$$
\lambda = 1, \quad \lambda = 2, \quad \lambda = 3
$$

#### 2. Find Eigenvectors

##### Case 1: For $\lambda = 1$

We solve $(A - I)X = 0$:

$$
\begin{bmatrix}
1 & 1 & 1 \\
-1 & 1 & -1 \\
1 & -1 & 1
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

Perform operations $R\_2 \to R\_2 + R\_1$, $R\_3 \to R\_3 - R\_1$:

$$
\begin{bmatrix}
1 & 1 & 1 \\
0 & 2 & 0 \\
0 & -2 & 0
\end{bmatrix} \implies y = 0 \quad \text{and} \quad x + z = 0 \implies x = -z
$$

Let $z = 1$. The eigenvector is:

$$
X_1 = \begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix}
$$

##### Case 2: For $\lambda = 2$

We solve $(A - 2I)X = 0$:

$$
\begin{bmatrix}
0 & 1 & 1 \\
-1 & 0 & -1 \\
1 & -1 & 0
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

From row 1: $y + z = 0 \implies y = -z$. From row 2: $-x - z = 0 \implies x = -z$.

Let $z = -1$. The eigenvector is:

$$
X_2 = \begin{bmatrix}
1 \\
1 \\
-1
\end{bmatrix}
$$

##### Case 3: For $\lambda = 3$

We solve $(A - 3I)X = 0$:

$$
\begin{bmatrix}
-1 & 1 & 1 \\
-1 & -1 & -1 \\
1 & -1 & -1
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

Subtract row 1 from row 2 ($R\_2 \to R\_2 - R\_1$):

$$
\begin{bmatrix}
-1 & 1 & 1 \\
0 & -2 & -2 \\
1 & -1 & -1
\end{bmatrix} \implies y + z = 0 \implies y = -z \quad \text{and} \quad x = 0
$$

Let $z = 1$. The eigenvector is:

$$
X_3 = \begin{bmatrix}
0 \\
-1 \\
1
\end{bmatrix}
$$

---

### Q6(b) Solve the following system of linear equations: (05)

$$
x + 2y - z = 2
$$

$$
2x + y + z = 1
$$

$$
x + 5y - 4z = 5
$$

**Answer:**

We write the augmented matrix:

$$
\begin{bmatrix}
1 & 2 & -1 & | & 2 \\
2 & 1 & 1 & | & 1 \\
1 & 5 & -4 & | & 5
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 2R\_1$
*   $R\_3 \to R\_3 - R\_1$

This gives:

$$
\begin{bmatrix}
1 & 2 & -1 & | & 2 \\
0 & -3 & 3 & | & -3 \\
0 & 3 & -3 & | & 3
\end{bmatrix}
$$

Perform the operation $R\_3 \to R\_3 + R\_2$:

$$
\begin{bmatrix}
1 & 2 & -1 & | & 2 \\
0 & -3 & 3 & | & -3 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

Scale row 2 ($R\_2 \to -1/3 R\_2$):

$$
\begin{bmatrix}
1 & 2 & -1 & | & 2 \\
0 & 1 & -1 & | & 1 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

This system is consistent. From row 2:

$$
y - z = 1 \implies y = 1 + z
$$

From row 1:

$$
x + 2y - z = 2 \implies x + 2(1 + z) - z = 2 \implies x + 2 + z = 2 \implies x = -z
$$

Let $z = t$ be a parameter. The general solution is:

$$
x = -t, \quad y = 1 + t, \quad z = t
$$

---

### Q7(a) Consider the vectors $v\_1 = (2, 1, 4), v\_2 = (1, -1, 3)$ and $v\_3 = (3, 2, 5)$ in $\mathbb{R}^3$. Show that $v = (5, 9, 5)$ is a linear combination of $v\_1, v\_2$, and $v\_3$. (05)

**Answer:**

We set up the relation:

$$
v = c_1 v_1 + c_2 v_2 + c_3 v_3 \implies (5, 9, 5) = c_1(2, 1, 4) + c_2(1, -1, 3) + c_3(3, 2, 5)
$$

This gives the system:

$$
2c_1 + c_2 + 3c_3 = 5
$$

$$
c_1 - c_2 + 2c_3 = 9
$$

$$
4c_1 + 3c_2 + 5c_3 = 5
$$

We write the augmented matrix and swap row 1 and row 2 ($R\_1 \leftrightarrow R\_2$):

$$
\begin{bmatrix}
1 & -1 & 2 & | & 9 \\
2 & 1 & 3 & | & 5 \\
4 & 3 & 5 & | & 5
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 2R\_1$
*   $R\_3 \to R\_3 - 4R\_1$

This gives:

$$
\begin{bmatrix}
1 & -1 & 2 & | & 9 \\
0 & 3 & -1 & | & -13 \\
0 & 7 & -3 & | & -31
\end{bmatrix}
$$

Perform the operation $R\_3 \to 3R\_3 - 7R\_2$:

$$
\begin{bmatrix}
1 & -1 & 2 & | & 9 \\
0 & 3 & -1 & | & -13 \\
0 & 0 & -2 & | & -2
\end{bmatrix}
$$

Now solve for the coefficients by back substitution:
*   From row 3:

$$
-2c\_3 = -2 \implies c\_3 = 1.
$$

*   From row 2:

$$
3c\_2 - 1 = -13 \implies 3c\_2 = -12 \implies c\_2 = -4.
$$

*   From row 1:

$$
c\_1 - (-4) + 2(1) = 9 \implies c\_1 + 6 = 9 \implies c\_1 = 3.
$$

So we can write $v$ as:

$$
v = 3v_1 - 4v_2 + v_3
$$

This shows that the vector is a linear combination of the given vectors.

---

### Q7(b) Let $U$ be the subspace of $\mathbb{R}^3$ spanned by the vectors $(1, 2, 1), (0, -1, 0)$ and $(2, 0, 2)$. Find a basis and the dimension of $U$. (05)

**Answer:**

We write the spanning vectors as the rows of a matrix:

$$
\begin{bmatrix}
1 & 2 & 1 \\
0 & -1 & 0 \\
2 & 0 & 2
\end{bmatrix}
$$

Perform the operation $R\_3 \to R\_3 - 2R\_1$:

$$
\begin{bmatrix}
1 & 2 & 1 \\
0 & -1 & 0 \\
0 & -4 & 0
\end{bmatrix}
$$

Perform the operation $R\_3 \to R\_3 - 4R\_2$:

$$
\begin{bmatrix}
1 & 2 & 1 \\
0 & -1 & 0 \\
0 & 0 & 0
\end{bmatrix}
$$

The non-zero rows of the echelon matrix form a basis:

$$
\text{Basis} = \{ (1, 2, 1), \quad (0, 1, 0) \}
$$

The number of vectors in the basis is 2, so the dimension is:

$$
\text{Dimension} = 2
$$

---

### Q8(a) Define sum and direct sum with examples. (02)

**Answer:**

*   **Sum of Subspaces:** Let $U$ and $W$ be subspaces of a vector space $V$. The sum $U + W$ is the set of all vectors $u + w$ where $u \in U$ and $w \in W$.
*Example:* In $\mathbb{R}^2$, let $U$ be the $x$-axis and $W$ be the $y$-axis. Then

$$
U + W = \mathbb{R}^2.
$$

*   **Direct Sum of Subspaces:** Let $U$ and $W$ be subspaces of $V$. The sum $U + W$ is a direct sum (written $U \oplus W$) if every element in the sum can be written uniquely as $u + w$. This occurs if and only if $U \cap W = \{0\}$.
*Example:* In $\mathbb{R}^2$, let $U$ be the $x$-axis and $W$ be the $y$-axis. Their intersection is only the origin $\{(0, 0)\}$. So

$$
U \oplus W = \mathbb{R}^2.
$$

---

### Q8(b) Let $w$ be the space generated by the polynomials: (04)

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

### Q8(c) Identify that the following mappings $F$ are linear or not linear: (04)
*   **(i)**

$$
F : \mathbb{R}^3 \rightarrow \mathbb{R}
$$

defined by $F(x, y, z) = 2x - 3y + 4z$
*   **(ii)**

$$
F : \mathbb{R}^2 \rightarrow \mathbb{R}^3
$$

defined by $F(x, y) = (x+1, 2y, x+y)$

**Answer:**

#### (i) Mapping $F(x, y, z) = 2x - 3y + 4z$

Let

$$
u = (x\_1, y\_1, z\_1)
$$

and

$$
v = (x\_2, y\_2, z\_2)
$$

be vectors in $\mathbb{R}^3$.
*   **Check Addition:**

$$
F(u + v) = F(x_1 + x_2, y_1 + y_2, z_1 + z_2) = 2(x_1 + x_2) - 3(y_1 + y_2) + 4(z_1 + z_2)
$$

$$
F(u + v) = (2x_1 - 3y_1 + 4z_1) + (2x_2 - 3y_2 + 4z_2) = F(u) + F(v)
$$

*   **Check Scalar Multiplication:**

$$
F(ku) = F(kx_1, ky_1, kz_1) = 2(kx_1) - 3(ky_1) + 4(kz_1) = k(2x_1 - 3y_1 + 4z_1) = kF(u)
$$

So the mapping is **linear**.

#### (ii) Mapping $F(x, y) = (x+1, 2y, x+y)$

A linear mapping must map the zero vector to the zero vector. We check the image of $(0, 0)$:

$$
F(0, 0) = (0 + 1, 2(0), 0 + 0) = (1, 0, 0) \neq (0, 0, 0)
$$

Since the image of the zero vector is not the zero vector, this mapping is **not linear**.

---

[⬅ 2021](2021_answer.md) | [🏠 Index](00-index.md) | [2024 ➡](2024_answer.md)
