[⬅ 2023](2023_answer.md) | [🏠 Index](00-index.md) | *(end)*

---

# B.Sc. Engineering 2nd Year Odd Semester Examination, 2024
**Course No: Math 2117**
**Course Title: Vector Analysis and Linear Algebra**
**Time: 03 Hours**
**Full Marks: 60**

---

## SECTION - A

### Q1(a) What is vector field? Graph the vector fields defined by: (05)
*   (i) $\vec{V}(x, y) = x\hat{i} + y\hat{j}$
*   (ii) $\vec{V}(x, y) = -x\hat{i} - y\hat{j}$

**Answer:**

#### 1. Definition of a Vector Field
A vector field is a function. It assigns a vector to every point in a given region. In a two-dimensional space, we write it as:

$$
\vec{V}(x, y) = P(x, y)\hat{i} + Q(x, y)\hat{j}
$$

Here, $P(x, y)$ and $Q(x, y)$ are scalar functions.

#### 2. Graphing the Vector Fields

##### (i) $\vec{V}(x, y) = x\hat{i} + y\hat{j}$
For any point $(x, y)$, the vector points directly away from the origin $(0, 0)$. The length of the vector equals the distance of the point from the origin, $r = \sqrt{x^2 + y^2}$.

We choose a few points to show the field:
*   At $(1, 0)$, the vector is $\hat{i}$. It points right with a length of 1.
*   At $(0, 1)$, the vector is $\hat{j}$. It points up with a length of 1.
*   At $(-1, 0)$, the vector is $-\hat{i}$. It points left with a length of 1.
*   At $(0, -1)$, the vector is $-\hat{j}$. It points down with a length of 1.
*   At $(2, 2)$, the vector is $2\hat{i} + 2\hat{j}$. It points diagonally outward with a length of $2\sqrt{2}$.

This field looks like a source. All vectors point radially outward from the center.

##### (ii) $\vec{V}(x, y) = -x\hat{i} - y\hat{j}$
For any point $(x, y)$, the vector points directly toward the origin $(0, 0)$. Its length equals the distance from the origin.

We choose a few points to show the field:
*   At $(1, 0)$, the vector is $-\hat{i}$. It points left with a length of 1.
*   At $(0, 1)$, the vector is $-\hat{j}$. It points down with a length of 1.
*   At $(-1, 0)$, the vector is $\hat{i}$. It points right with a length of 1.
*   At $(0, -1)$, the vector is $\hat{j}$. It points up with a length of 1.
*   At $(2, 2)$, the vector is $-2\hat{i} - 2\hat{j}$. It points diagonally inward with a length of $2\sqrt{2}$.

This field looks like a sink. All vectors point radially inward toward the center.

---

### Q1(b) Show that a necessary and sufficient condition that the vectors $\vec{A} = A\_1\hat{i} + A\_2\hat{j} + A\_3\hat{k}$, $\vec{B} = B\_1\hat{i} + B\_2\hat{j} + B\_3\hat{k}$, $\vec{C} = C\_1\hat{i} + C\_2\hat{j} + C\_3\hat{k}$ be linearly independent is that the determinant (05)

$$
\begin{vmatrix}
A_1 & A_2 & A_3 \\
B_1 & B_2 & B_3 \\
C_1 & C_2 & C_3
\end{vmatrix}
$$

be different from zero.

**Answer:**

Let $a$, $b$, and $c$ be scalars. We set their linear combination to zero:

$$
a\vec{A} + b\vec{B} + c\vec{C} = \vec{0}
$$

We substitute the vector components:

$$
a(A_1\hat{i} + A_2\hat{j} + A_3\hat{k}) + b(B_1\hat{i} + B_2\hat{j} + B_3\hat{k}) + c(C_1\hat{i} + C_2\hat{j} + C_3\hat{k}) = \vec{0}
$$

We group the components for $\hat{i}$, $\hat{j}$, and $\hat{k}$:

$$
(a A_1 + b B_1 + c C_1)\hat{i} + (a A_2 + b B_2 + c C_2)\hat{j} + (a A_3 + b B_3 + c C_3)\hat{k} = \vec{0}
$$

This gives a homogeneous system of three linear equations:

$$
\begin{aligned}
A_1 a + B_1 b + C_1 c &= 0 \\
A_2 a + B_2 b + C_2 c &= 0 \\
A_3 a + B_3 b + C_3 c &= 0
\end{aligned}
$$

The vectors $\vec{A}$, $\vec{B}$, and $\vec{C}$ are linearly independent if and only if the system has only the trivial solution:

$$
a = b = c = 0
$$

A homogeneous system has only the trivial solution if and only if the determinant of its coefficient matrix is not zero. We write this determinant:

$$
D = \begin{vmatrix}
A_1 & B_1 & C_1 \\
A_2 & B_2 & C_2 \\
A_3 & B_3 & C_3
\end{vmatrix}
$$

We know that transposing a matrix does not change its determinant. So we can swap rows and columns:

$$
\begin{vmatrix}
A_1 & B_1 & C_1 \\
A_2 & B_2 & C_2 \\
A_3 & B_3 & C_3
\end{vmatrix} = \begin{vmatrix}
A_1 & A_2 & A_3 \\
B_1 & B_2 & B_3 \\
C_1 & C_2 & C_3
\end{vmatrix}
$$

Therefore, the vectors are linearly independent if and only if:

$$
\begin{vmatrix}
A_1 & A_2 & A_3 \\
B_1 & B_2 & B_3 \\
C_1 & C_2 & C_3
\end{vmatrix} \neq 0
$$

This completes the proof.

---

### Q2(a) Find an equation for the plane perpendicular to the vector $\vec{A} = 2\hat{i} + 3\hat{j} + 6\hat{k}$ and passing through the terminal point of vector $\vec{B} = \hat{i} + 5\hat{j} + 3\hat{k}$. (04)

**Answer:**

We assume the vector $\vec{B}$ starts at the origin. Its terminal point is $P(1, 5, 3)$.

Let the position vector of any point $(x, y, z)$ on the plane be:

$$
\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}
$$

The vector from point $P$ to any point on the plane is:

$$
\vec{r} - \vec{B} = (x - 1)\hat{i} + (y - 5)\hat{j} + (z - 3)\hat{k}
$$

The plane is perpendicular to vector $\vec{A}$. So, the vector $\vec{r} - \vec{B}$ must be perpendicular to $\vec{A}$. Their dot product is zero:

$$
(\vec{r} - \vec{B}) \cdot \vec{A} = 0
$$

We substitute the components:

$$
((x - 1)\hat{i} + (y - 5)\hat{j} + (z - 3)\hat{k}) \cdot (2\hat{i} + 3\hat{j} + 6\hat{k}) = 0
$$

$$
2(x - 1) + 3(y - 5) + 6(z - 3) = 0
$$

$$
2x - 2 + 3y - 15 + 6z - 18 = 0
$$

$$
2x + 3y + 6z - 35 = 0
$$

So, the equation of the plane is:

$$
2x + 3y + 6z = 35
$$

---

### Q2(b) A particle moves so that its position vector is given by $\vec{r} = \cos \omega t \hat{i} + \sin \omega t \hat{j}$ where $\omega$ is constant. Show that the velocity $\vec{v}$ of the particle is perpendicular to $\vec{r}$, also show that $\vec{r} \times \vec{v} = \vec{a}$ constant vector. (04)

**Answer:**

#### 1. Show that Velocity is Perpendicular to Position
We find the velocity vector $\vec{v}$ by taking the derivative of $\vec{r}$ with respect to $t$:

$$
\vec{v} = \frac{d\vec{r}}{dt} = -\omega \sin \omega t \hat{i} + \omega \cos \omega t \hat{j}
$$

We calculate the dot product of $\vec{r}$ and $\vec{v}$:

$$
\vec{r} \cdot \vec{v} = (\cos \omega t)(-\omega \sin \omega t) + (\sin \omega t)(\omega \cos \omega t) = -\omega \sin \omega t \cos \omega t + \omega \sin \omega t \cos \omega t = 0
$$

The dot product is zero. So, the velocity vector $\vec{v}$ is perpendicular to $\vec{r}$.

#### 2. Show that $\vec{r} \times \vec{v}$ is a Constant Vector
We calculate the cross product:

$$
\vec{r} \times \vec{v} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\cos \omega t & \sin \omega t & 0 \\
-\omega \sin \omega t & \omega \cos \omega t & 0
\end{vmatrix}
$$

$$
\vec{r} \times \vec{v} = \hat{i}(0) - \hat{j}(0) + \hat{k} \left[ (\cos \omega t)(\omega \cos \omega t) - (\sin \omega t)(-\omega \sin \omega t) \right]
$$

$$
\vec{r} \times \vec{v} = \hat{k} \left( \omega \cos^2 \omega t + \omega \sin^2 \omega t \right) = \omega (\cos^2 \omega t + \sin^2 \omega t)\hat{k} = \omega\hat{k}
$$

The term $\omega$ is a constant. So, the vector $\omega\hat{k}$ is constant. Let $\vec{a} = \omega\hat{k}$. We get:

$$
\vec{r} \times \vec{v} = \vec{a}
$$

This is a constant vector.

---

### Q2(c) If $Q = 3x^2y - y^3z^2$ find $\nabla Q$ at the point $(1, -2, -1)$. (02)

**Answer:**

The gradient of $Q$ is:

$$
\nabla Q = \frac{\partial Q}{\partial x}\hat{i} + \frac{\partial Q}{\partial y}\hat{j} + \frac{\partial Q}{\partial z}\hat{k}
$$

We calculate the partial derivatives:

$$
\frac{\partial Q}{\partial x} = \frac{\partial}{\partial x}(3x^2y - y^3z^2) = 6xy
$$

$$
\frac{\partial Q}{\partial y} = \frac{\partial}{\partial y}(3x^2y - y^3z^2) = 3x^2 - 3y^2z^2
$$

$$
\frac{\partial Q}{\partial z} = \frac{\partial}{\partial z}(3x^2y - y^3z^2) = -2y^3z
$$

We substitute $x = 1$, $y = -2$, and $z = -1$:

$$
\frac{\partial Q}{\partial x} = 6(1)(-2) = -12
$$

$$
\frac{\partial Q}{\partial y} = 3(1)^2 - 3(-2)^2(-1)^2 = 3 - 3(4)(1) = 3 - 12 = -9
$$

$$
\frac{\partial Q}{\partial z} = -2(-2)^3(-1) = -2(-8)(-1) = -16
$$

So, the gradient at $(1, -2, -1)$ is:

$$
\nabla Q = -12\hat{i} - 9\hat{j} - 16\hat{k}
$$

---

### Q3(a) Evaluate $\nabla(\vec{A} \times \vec{r})$ if $\nabla \times \vec{A} = 0$. (03)

**Answer:**

We assume that the expression $\nabla(\vec{A} \times \vec{r})$ refers to the divergence:

$$
\nabla \cdot (\vec{A} \times \vec{r})
$$

Here, $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ is the position vector.

We use the vector identity for the divergence of a cross product:

$$
\nabla \cdot (\vec{A} \times \vec{r}) = \vec{r} \cdot (\nabla \times \vec{A}) - \vec{A} \cdot (\nabla \times \vec{r})
$$

We are given that $\nabla \times \vec{A} = 0$. So, the first term is zero.

Next, we calculate the curl of the position vector $\vec{r}$:

$$
\nabla \times \vec{r} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
x & y & z
\end{vmatrix} = \hat{i}(0) - \hat{j}(0) + \hat{k}(0) = \vec{0}
$$

So, the second term is also zero:

$$
\vec{A} \cdot (\nabla \times \vec{r}) = \vec{A} \cdot \vec{0} = 0
$$

Thus, we find:

$$
\nabla \cdot (\vec{A} \times \vec{r}) = 0
$$

If the question meant the curl $\nabla \times (\vec{A} \times \vec{r})$, we use another identity:

$$
\nabla \times (\vec{A} \times \vec{r}) = (\vec{r} \cdot \nabla)\vec{A} - (\vec{A} \cdot \nabla)\vec{r} + \vec{A}(\nabla \cdot \vec{r}) - \vec{r}(\nabla \cdot \vec{A})
$$

We calculate the terms:
*   $\nabla \cdot \vec{r} = 1 + 1 + 1 = 3$. So, $\vec{A}(\nabla \cdot \vec{r}) = 3\vec{A}$.
*   $(\vec{A} \cdot \nabla)\vec{r} = \left( A\_1 \frac{\partial}{\partial x} + A\_2 \frac{\partial}{\partial y} + A\_3 \frac{\partial}{\partial z} \right)(x\hat{i} + y\hat{j} + z\hat{k}) = \vec{A}$.

This gives:

$$
\nabla \times (\vec{A} \times \vec{r}) = 2\vec{A} + (\vec{r} \cdot \nabla)\vec{A} - \vec{r}(\nabla \cdot \vec{A})
$$

If $\vec{A}$ is a constant vector field, then its derivatives are zero. In that case, the curl is:

$$
\nabla \times (\vec{A} \times \vec{r}) = 2\vec{A}
$$

---

### Q3(b) Find the work done in moving a particle in a force field given by $\vec{F} = 3xy\hat{i} - 5z\hat{j} + 10x\hat{k}$ along the curve $x = t^2 + 1, y = 2t^2, z = t^3$ from $t = 1$ to $t = 2$. (03)

**Answer:**

The work done is:

$$
W = \int_C \vec{F} \cdot d\vec{r} = \int_C (3xy dx - 5z dy + 10x dz)
$$

We express all terms using the parameter $t$:
*   $x = t^2 + 1 \implies dx = 2t dt$
*   $y = 2t^2 \implies dy = 4t dt$
*   $z = t^3 \implies dz = 3t^2 dt$

We substitute these into the integrand:
1.  $3xy dx = 3(t^2 + 1)(2t^2)(2t dt) = 12t^3(t^2 + 1) dt = (12t^5 + 12t^3) dt$
2.  $-5z dy = -5(t^3)(4t dt) = -20t^4 dt$
3.  $10x dz = 10(t^2 + 1)(3t^2 dt) = 30t^2(t^2 + 1) dt = (30t^4 + 30t^2) dt$

We sum these three parts:

$$
\vec{F} \cdot d\vec{r} = (12t^5 + 12t^3 - 20t^4 + 30t^4 + 30t^2) dt = (12t^5 + 10t^4 + 12t^3 + 30t^2) dt
$$

We integrate from $t = 1$ to $t = 2$:

$$
W = \int_1^2 (12t^5 + 10t^4 + 12t^3 + 30t^2) dt
$$

We find the antiderivative:

$$
\int (12t^5 + 10t^4 + 12t^3 + 30t^2) dt = 2t^6 + 2t^5 + 3t^4 + 10t^3
$$

We evaluate at the limits:
*   At $t = 2$:

    

$$
2(2^6) + 2(2^5) + 3(2^4) + 10(2^3) = 2(64) + 2(32) + 3(16) + 10(8) = 128 + 64 + 48 + 80 = 320
$$

*   At $t = 1$:

    

$$
2(1^6) + 2(1^5) + 3(1^4) + 10(1^3) = 2 + 2 + 3 + 10 = 17
$$

We subtract the values:

$$
W = 320 - 17 = 303
$$

So, the work done is 303.

---

### Q3(c) Evaluate: (04)

$$
\iint_R \sqrt{x^2 + y^2} dxdy
$$

over the region $R$ in the $xy$ plane bounded by $x^2 + y^2 = 36$.

**Answer:**

We switch to polar coordinates:

$$
x = r\cos\theta, \quad y = r\sin\theta, \quad dxdy = r dr d\theta
$$

The region $R$ is a disk of radius 6 centered at the origin, because $x^2 + y^2 = 36 = 6^2$.

The integration limits are:
*   $r$ goes from 0 to 6
*   $\theta$ goes from 0 to $2\pi$

The integrand is:

$$
\sqrt{x^2 + y^2} = r
$$

We rewrite the double integral:

$$
\iint_R \sqrt{x^2 + y^2} dxdy = \int_0^{2\pi} \int_0^6 r \cdot r dr d\theta = \int_0^{2\pi} \int_0^6 r^2 dr d\theta
$$

We integrate with respect to $r$:

$$
\int_0^6 r^2 dr = \left[ \frac{r^3}{3} \right]_0^6 = \frac{216}{3} = 72
$$

We integrate with respect to $\theta$:

$$
\int_0^{2\pi} 72 d\theta = 72 \cdot 2\pi = 144\pi
$$

The value of the integral is $144\pi$.

---

### Q4(a) State and prove Green's theorem in a plane. (05)

**Answer:**

#### 1. Statement
Let $R$ be a closed region in the $xy$-plane. Let $C$ be the boundary curve of $R$. Let $P(x, y)$ and $Q(x, y)$ be functions that are continuous and have continuous first-order partial derivatives in $R$. Then:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$

The boundary curve $C$ is traversed in the positive (counterclockwise) direction.

#### 2. Proof
We prove the theorem for a simple region $R$. We can write this region as:

$$
R = \{ (x, y) \mid a \leq x \leq b, \quad y_1(x) \leq y \leq y_2(x) \}
$$

and also as:

$$
R = \{ (x, y) \mid c \leq y \leq d, \quad x_1(y) \leq x \leq x_2(y) \}
$$

We split the proof into two parts:
*   **Part 1:** Show that $\oint\_C P dx = -\iint\_R \frac{\partial P}{\partial y} dx dy$
*   **Part 2:** Show that $\oint\_C Q dy = \iint\_R \frac{\partial Q}{\partial x} dx dy$

##### Part 1
We evaluate the double integral:

$$
\iint_R \frac{\partial P}{\partial y} dx dy = \int_a^b \left[ \int_{y_1(x)}^{y_2(x)} \frac{\partial P}{\partial y} dy \right] dx
$$

Using the Fundamental Theorem of Calculus on the inner integral:

$$
\iint_R \frac{\partial P}{\partial y} dx dy = \int_a^b [P(x, y_2(x)) - P(x, y_1(x))] dx \quad \dots (1)
$$

Now we evaluate the line integral $\oint\_C P dx$ along the boundary $C$. The boundary has two parts:
*   $C\_1$ is the lower curve $y = y\_1(x)$ going from $x = a$ to $x = b$.
*   $C\_2$ is the upper curve $y = y\_2(x)$ going from $x = b$ to $x = a$.

So:

$$
\oint_C P dx = \int_{C_1} P dx + \int_{C_2} P dx
$$

$$
\oint_C P dx = \int_a^b P(x, y_1(x)) dx + \int_b^a P(x, y_2(x)) dx
$$

We swap the limits of the second integral:

$$
\oint_C P dx = \int_a^b P(x, y_1(x)) dx - \int_a^b P(x, y_2(x)) dx = -\int_a^b [P(x, y_2(x)) - P(x, y_1(x))] dx \quad \dots (2)
$$

Comparing equations (1) and (2) shows:

$$
\oint_C P dx = -\iint_R \frac{\partial P}{\partial y} dx dy
$$

##### Part 2
We evaluate the double integral using the second description of the region:

$$
\iint_R \frac{\partial Q}{\partial x} dx dy = \int_c^d \left[ \int_{x_1(y)}^{x_2(y)} \frac{\partial Q}{\partial x} dx \right] dy = \int_c^d [Q(x_2(y), y) - Q(x_1(y), y)] dy \quad \dots (3)
$$

Now we evaluate the line integral $\oint\_C Q dy$. The boundary curve $C$ consists of:
*   $C\_1$ is the left curve $x = x\_1(y)$ going from $y = d$ to $y = c$.
*   $C\_2$ is the right curve $x = x\_2(y)$ going from $y = c$ to $y = d$.

So:

$$
\oint_C Q dy = \int_d^c Q(x_1(y), y) dy + \int_c^d Q(x_2(y), y) dy
$$

$$
\oint_C Q dy = -\int_c^d Q(x_1(y), y) dy + \int_c^d Q(x_2(y), y) dy = \int_c^d [Q(x_2(y), y) - Q(x_1(y), y)] dy \quad \dots (4)
$$

Comparing equations (3) and (4) shows:

$$
\oint_C Q dy = \iint_R \frac{\partial Q}{\partial x} dx dy
$$

We add the results of Part 1 and Part 2:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$

The proof is complete.

---

### Q4(b) Verify Stoke's theorem for $\vec{A} = (y - z + 2)\hat{i} + (yz + 4)\hat{j} - xz\hat{k}$ where $S$ is the surface of the cube $x=y=z=0$; $x=y=z=2$ above xy plane. (05)

**Answer:**

Stokes' theorem states:

$$
\oint_C \vec{A} \cdot d\vec{r} = \iint_S (\nabla \times \vec{A}) \cdot \hat{n} dS
$$

The surface $S$ consists of the five faces of the cube above the $xy$-plane. The bottom face $z = 0$ is open.
The boundary curve $C$ is the square in the $xy$-plane ($z = 0$) bounded by $x=0$, $x=2$, $y=0$, and $y=2$.

#### 1. Evaluate the Line Integral
Along the boundary curve $C$ in the plane $z = 0$, we have $z = 0$ and $dz = 0$.
The vector field simplifies to:

$$
\vec{A} = (y + 2)\hat{i} + 4\hat{j}
$$

The line integral is:

$$
\oint_C \vec{A} \cdot d\vec{r} = \oint_C (y + 2) dx + 4 dy
$$

We evaluate the integral along the four segments of the square $C$:
*   **Path 1 ($C\_1$):** From $(0,0,0)$ to $(2,0,0)$. Here, $y = 0$ and $dy = 0$.

    

$$
\int_{C_1} = \int_0^2 2 dx = 4
$$

*   **Path 2 ($C\_2$):** From $(2,0,0)$ to $(2,2,0)$. Here, $x = 2$ and $dx = 0$.

    

$$
\int_{C_2} = \int_0^2 4 dy = 8
$$

*   **Path 3 ($C\_3$):** From $(2,2,0)$ to $(0,2,0)$. Here, $y = 2$ and $dy = 0$.

    

$$
\int_{C_3} = \int_2^0 4 dx = -8
$$

*   **Path 4 ($C\_4$):** From $(0,2,0)$ to $(0,0,0)$. Here, $x = 0$ and $dx = 0$.

    

$$
\int_{C_4} = \int_2^0 4 dy = -8
$$

We sum these line integrals:

$$
\oint_C \vec{A} \cdot d\vec{r} = 4 + 8 - 8 - 8 = -4
$$

#### 2. Evaluate the Surface Integral
First, we find the curl of $\vec{A}$:

$$
\nabla \times \vec{A} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
y-z+2 & yz+4 & -xz
\end{vmatrix}
$$

$$
= \hat{i} \left[ 0 - y \right] - \hat{j} \left[ -z - (-1) \right] + \hat{k} \left[ 0 - 1 \right] = -y\hat{i} + (z - 1)\hat{j} - \hat{k}
$$

The surface $S$ has five faces:
*   **Face 1 (Top, $z=2$):** $\hat{n} = \hat{k}$, $dS = dx dy$.

    

$$
(\nabla \times \vec{A}) \cdot \hat{n} = -1 \implies \iint_{\text{Top}} -1 dx dy = -1 \times \text{Area} = -4
$$

*   **Face 2 (Front, $x=2$):** $\hat{n} = \hat{i}$, $dS = dy dz$.

    

$$
(\nabla \times \vec{A}) \cdot \hat{n} = -y \implies \iint_{\text{Front}} -y dy dz = \int_0^2 dz \int_0^2 -y dy = 2 \left[ -\frac{y^2}{2} \right]_0^2 = -4
$$

*   **Face 3 (Back, $x=0$):** $\hat{n} = -\hat{i}$, $dS = dy dz$.

    

$$
(\nabla \times \vec{A}) \cdot \hat{n} = y \implies \iint_{\text{Back}} y dy dz = \int_0^2 dz \int_0^2 y dy = 2 \left[ \frac{y^2}{2} \right]_0^2 = 4
$$

*   **Face 4 (Right, $y=2$):** $\hat{n} = \hat{j}$, $dS = dx dz$.

    

$$
(\nabla \times \vec{A}) \cdot \hat{n} = z - 1 \implies \iint_{\text{Right}} (z - 1) dx dz = \int_0^2 dx \int_0^2 (z - 1) dz = 2 \left[ \frac{z^2}{2} - z \right]_0^2 = 2(2 - 2) = 0
$$

*   **Face 5 (Left, $y=0$):** $\hat{n} = -\hat{j}$, $dS = dx dz$.

    

$$
(\nabla \times \vec{A}) \cdot \hat{n} = -(z - 1) \implies \iint_{\text{Left}} (1 - z) dx dz = \int_0^2 dx \int_0^2 (1 - z) dz = 2 \left[ z - \frac{z^2}{2} \right]_0^2 = 2(2 - 2) = 0
$$

We sum the integrals over all five faces:

$$
\iint_S (\nabla \times \vec{A}) \cdot \hat{n} dS = -4 - 4 + 4 + 0 + 0 = -4
$$

Both integrals yield $-4$. Stokes' theorem is verified.

---

## SECTION - B

### Q5(a) Define rank of a matrix. Find the rank of: (05)

$$
A = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 3 & -2 & 1 \\
2 & 0 & -3 & 2 \\
3 & 3 & -3 & 3
\end{bmatrix}
$$

**Answer:**

#### 1. Definition of Rank
The rank of a matrix is the maximum number of linearly independent row vectors in the matrix. This is also equal to the maximum number of linearly independent column vectors.

#### 2. Find the Rank of Matrix $A$
We write the matrix:

$$
A = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 3 & -2 & 1 \\
2 & 0 & -3 & 2 \\
3 & 3 & -3 & 3
\end{bmatrix}
$$

We apply row operations to reduce it to echelon form:
*   $R\_2 \to R\_2 - R\_1$
*   $R\_3 \to R\_3 - 2R\_1$
*   $R\_4 \to R\_4 - 3R\_1$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 0 \\
0 & -2 & -5 & 0 \\
0 & 0 & -6 & 0
\end{bmatrix}
$$

Next, we apply:
*   $R\_3 \to R\_3 + R\_2$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 0 \\
0 & 0 & -8 & 0 \\
0 & 0 & -6 & 0
\end{bmatrix}
$$

We scale the third row ($R\_3 \to -\frac{1}{8}R\_3$):

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & -6 & 0
\end{bmatrix}
$$

Now we apply:
*   $R\_4 \to R\_4 + 6R\_3$

This yields:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

There are 3 non-zero rows in the echelon form. Thus, the rank of the matrix is 3.

---

### Q5(b) Investigate for what values of $\lambda$ and $\mu$ the simultaneous equations $x + y + z = 6, x + 2y + 3z = 10$ and $x + 2y + \lambda z = \mu$ have (i) no solution (ii) unique solution (iii) infinite solutions. (05)

**Answer:**

We write the system of equations in augmented matrix form $[A | B]$:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 6 \\
1 & 2 & 3 & | & 10 \\
1 & 2 & \lambda & | & \mu
\end{bmatrix}
$$

We apply row operations:
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

Now, we perform:
*   $R\_3 \to R\_3 - R\_2$

This yields:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 6 \\
0 & 1 & 2 & | & 4 \\
0 & 0 & \lambda - 3 & | & \mu - 10
\end{bmatrix}
$$

We analyze the system using the last row:

#### (i) No Solution
The system has no solution if the rank of the coefficient matrix $A$ is less than the rank of the augmented matrix $[A | B]$. This happens when:

$$
\lambda - 3 = 0 \quad \text{and} \quad \mu - 10 \neq 0
$$

So, the conditions are:

$$
\lambda = 3 \quad \text{and} \quad \mu \neq 10
$$

#### (ii) Unique Solution
The system has a unique solution if the rank of $A$ equals the rank of $[A | B]$ and equals the number of variables (which is 3). This happens when:

$$
\lambda - 3 \neq 0
$$

So, the condition is:

$$
\lambda \neq 3 \quad (\text{for any value of } \mu)
$$

#### (iii) Infinite Solutions
The system has infinitely many solutions if the rank of $A$ equals the rank of $[A | B]$ but is less than the number of variables. This happens when:

$$
\lambda - 3 = 0 \quad \text{and} \quad \mu - 10 = 0
$$

So, the conditions are:

$$
\lambda = 3 \quad \text{and} \quad \mu = 10
$$

---

### Q6(a) Verify Cayley Hamilton's theorem for the matrix: (05)

$$
A = \begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix}
$$

Hence compute $A^{-1}$.

**Answer:**

#### 1. Characteristic Equation
We find the characteristic equation $|A - \lambda I| = 0$:

$$
\begin{vmatrix}
2 - \lambda & 2 & 1 \\
1 & 3 - \lambda & 1 \\
1 & 2 & 2 - \lambda
\end{vmatrix} = 0
$$

We expand the determinant:

$$
(2 - \lambda) \left[ (3 - \lambda)(2 - \lambda) - 2 \right] - 2 \left[ 1(2 - \lambda) - 1 \right] + 1 \left[ 2 - (3 - \lambda) \right] = 0
$$

$$
(2 - \lambda) \left[ \lambda^2 - 5\lambda + 4 \right] - 2 \left[ 1 - \lambda \right] + 1 \left[ \lambda - 1 \right] = 0
$$

$$
(2\lambda^2 - 10\lambda + 8 - \lambda^3 + 5\lambda^2 - 4\lambda) - (2 - 2\lambda) + (\lambda - 1) = 0
$$

$$
-\lambda^3 + 7\lambda^2 - 14\lambda + 8 - 2 + 2\lambda + \lambda - 1 = 0
$$

$$
-\lambda^3 + 7\lambda^2 - 11\lambda + 5 = 0
$$

We multiply by $-1$:

$$
\lambda^3 - 7\lambda^2 + 11\lambda - 5 = 0
$$

#### 2. Verification of Cayley-Hamilton Theorem
We show that matrix $A$ satisfies this equation:

$$
A^3 - 7A^2 + 11A - 5I = 0
$$

First, we calculate $A^2$:

$$
A^2 = A \cdot A = \begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix} \begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix} = \begin{bmatrix}
7 & 12 & 6 \\
6 & 13 & 6 \\
6 & 12 & 7
\end{bmatrix}
$$

Next, we calculate $A^3$:

$$
A^3 = A^2 \cdot A = \begin{bmatrix}
7 & 12 & 6 \\
6 & 13 & 6 \\
6 & 12 & 7
\end{bmatrix} \begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix} = \begin{bmatrix}
32 & 62 & 31 \\
31 & 63 & 31 \\
31 & 62 & 32
\end{bmatrix}
$$

Now we compute $A^3 - 7A^2 + 11A - 5I$:

$$
\begin{bmatrix}
32 & 62 & 31 \\
31 & 63 & 31 \\
31 & 62 & 32
\end{bmatrix} - 7\begin{bmatrix}
7 & 12 & 6 \\
6 & 13 & 6 \\
6 & 12 & 7
\end{bmatrix} + 11\begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix} - 5\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

$$
= \begin{bmatrix}
32-49+22-5 & 62-84+22 & 31-42+11 \\
31-42+11 & 63-91+33-5 & 31-42+11 \\
31-42+11 & 62-84+22 & 32-49+22-5
\end{bmatrix}
= \begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}
$$

All entries are zero. Cayley-Hamilton's Theorem is verified.

#### 3. Compute $A^{-1}$
We multiply the characteristic equation by $A^{-1}$:

$$
A^{-1}(A^3 - 7A^2 + 11A - 5I) = 0
$$

$$
A^2 - 7A + 11I - 5A^{-1} = 0 \implies 5A^{-1} = A^2 - 7A + 11I
$$

$$
A^{-1} = \frac{1}{5}(A^2 - 7A + 11I)
$$

We compute the right side:

$$
A^2 - 7A + 11I = \begin{bmatrix}
7 & 12 & 6 \\
6 & 13 & 6 \\
6 & 12 & 7
\end{bmatrix} - \begin{bmatrix}
14 & 14 & 7 \\
7 & 21 & 7 \\
7 & 14 & 14
\end{bmatrix} + \begin{bmatrix}
11 & 0 & 0 \\
0 & 11 & 0 \\
0 & 0 & 11
\end{bmatrix}
$$

$$
= \begin{bmatrix}
7-14+11 & 12-14+0 & 6-7+0 \\
6-7+0 & 13-21+11 & 6-7+0 \\
6-7+0 & 12-14+0 & 7-14+11
\end{bmatrix}
= \begin{bmatrix}
4 & -2 & -1 \\
-1 & 3 & -1 \\
-1 & -2 & 4
\end{bmatrix}
$$

So, the inverse is:

$$
A^{-1} = \frac{1}{5} \begin{bmatrix}
4 & -2 & -1 \\
-1 & 3 & -1 \\
-1 & -2 & 4
\end{bmatrix}
$$

---

### Q6(b) Find the eigen vectors of the matrix: (05)

$$
A = \begin{bmatrix}
3 & 1 & 1 \\
1 & 5 & 1 \\
1 & 1 & 3
\end{bmatrix}
$$

**Answer:**

#### 1. Find the Eigenvalues
We solve the characteristic equation $|A - \lambda I| = 0$:

$$
\begin{vmatrix}
3 - \lambda & 1 & 1 \\
1 & 5 - \lambda & 1 \\
1 & 1 & 3 - \lambda
\end{vmatrix} = 0
$$

We expand the determinant:

$$
(3 - \lambda) \left[ (5 - \lambda)(3 - \lambda) - 1 \right] - 1 \left[ (3 - \lambda) - 1 \right] + 1 \left[ 1 - (5 - \lambda) \right] = 0
$$

$$
(3 - \lambda) \left[ \lambda^2 - 8\lambda + 14 \right] - (2 - \lambda) + (\lambda - 4) = 0
$$

$$
(3\lambda^2 - 24\lambda + 42 - \lambda^3 + 8\lambda^2 - 14\lambda) - 2 + \lambda + \lambda - 4 = 0
$$

$$
-\lambda^3 + 11\lambda^2 - 36\lambda + 36 = 0
$$

We multiply by $-1$:

$$
\lambda^3 - 11\lambda^2 + 36\lambda - 36 = 0
$$

We find the roots of this polynomial. We test $\lambda = 2$:

$$
2^3 - 11(2^2) + 36(2) - 36 = 8 - 44 + 72 - 36 = 0
$$

So, $\lambda = 2$ is a root. We factor it out:

$$
(\lambda - 2)(\lambda^2 - 9\lambda + 18) = 0
$$

We factor the quadratic term:

$$
(\lambda - 2)(\lambda - 3)(\lambda - 6) = 0
$$

The eigenvalues are:

$$
\lambda = 2, \quad \lambda = 3, \quad \lambda = 6
$$

#### 2. Find the Eigenvectors

##### Case 1: For $\lambda = 2$
We solve $(A - 2I)X = 0$:

$$
\begin{bmatrix}
1 & 1 & 1 \\
1 & 3 & 1 \\
1 & 1 & 1
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

We apply row operations:
*   $R\_2 \to R\_2 - R\_1$
*   $R\_3 \to R\_3 - R\_1$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 \\
0 & 2 & 0 \\
0 & 0 & 0
\end{bmatrix}
$$

From the second row, we get $2y = 0 \implies y = 0$.
From the first row, we get $x + y + z = 0 \implies x + z = 0 \implies x = -z$.

Let $z = 1$. The eigenvector is:

$$
X_1 = \begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix}
$$

##### Case 2: For $\lambda = 3$
We solve $(A - 3I)X = 0$:

$$
\begin{bmatrix}
0 & 1 & 1 \\
1 & 2 & 1 \\
1 & 1 & 0
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

From the first row, we get $y + z = 0 \implies y = -z$.
From the third row, we get $x + y = 0 \implies x = -y = z$.

Let $z = 1$. The eigenvector is:

$$
X_2 = \begin{bmatrix}
1 \\
-1 \\
1
\end{bmatrix}
$$

##### Case 3: For $\lambda = 6$
We solve $(A - 6I)X = 0$:

$$
\begin{bmatrix}
-3 & 1 & 1 \\
1 & -1 & 1 \\
1 & 1 & -3
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

We swap rows $R\_1 \leftrightarrow R\_2$:

$$
\begin{bmatrix}
1 & -1 & 1 \\
-3 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix}
$$

We apply row operations:
*   $R\_2 \to R\_2 + 3R\_1$
*   $R\_3 \to R\_3 - R\_1$

This gives:

$$
\begin{bmatrix}
1 & -1 & 1 \\
0 & -2 & 4 \\
0 & 2 & -4
\end{bmatrix}
$$

We scale the second row ($R\_2 \to -\frac{1}{2}R\_2$):

$$
\begin{bmatrix}
1 & -1 & 1 \\
0 & 1 & -2 \\
0 & 2 & -4
\end{bmatrix}
$$

We perform $R\_3 \to R\_3 - 2R\_2$:

$$
\begin{bmatrix}
1 & -1 & 1 \\
0 & 1 & -2 \\
0 & 0 & 0
\end{bmatrix}
$$

From the second row, we get $y - 2z = 0 \implies y = 2z$.
From the first row, we get $x - y + z = 0 \implies x - 2z + z = 0 \implies x = z$.

Let $z = 1$. The eigenvector is:

$$
X_3 = \begin{bmatrix}
1 \\
2 \\
1
\end{bmatrix}
$$

---

### Q7(a) Express the polynomial $v = 3t^2 + 5t - 5$ as a linear combination of the polynomials $P\_1 = t^2 + 2t + 1$, $P\_2 = 2t^2 + 5t + 4$ and $P\_3 = t^2 + 3t + 6$. (03)

**Answer:**

We write $v$ as a linear combination:

$$
v = c_1 P_1 + c_2 P_2 + c_3 P_3
$$

We substitute the polynomials:

$$
3t^2 + 5t - 5 = c_1(t^2 + 2t + 1) + c_2(2t^2 + 5t + 4) + c_3(t^2 + 3t + 6)
$$

We expand the terms and group them by powers of $t$:

$$
3t^2 + 5t - 5 = (c_1 + 2c_2 + c_3)t^2 + (2c_1 + 5c_2 + 3c_3)t + (c_1 + 4c_2 + 6c_3)
$$

We match the coefficients of $t^2$, $t$, and the constant terms:
1.  $c\_1 + 2c\_2 + c\_3 = 3$
2.  $2c\_1 + 5c\_2 + 3c\_3 = 5$
3.  $c\_1 + 4c\_2 + 6c\_3 = -5$

We solve this system. From equation (1):

$$
c_1 = 3 - 2c_2 - c_3
$$

We substitute this expression for $c\_1$ into equations (2) and (3):

In equation (2):

$$
2(3 - 2c_2 - c_3) + 5c_2 + 3c_3 = 5
$$

$$
6 - 4c_2 - 2c_3 + 5c_2 + 3c_3 = 5 \implies c_2 + c_3 = -1 \implies c_2 = -1 - c_3 \quad \dots (4)
$$

In equation (3):

$$
(3 - 2c_2 - c_3) + 4c_2 + 6c_3 = -5
$$

$$
3 + 2c_2 + 5c_3 = -5 \implies 2c_2 + 5c_3 = -8 \quad \dots (5)
$$

We substitute equation (4) into equation (5):

$$
2(-1 - c_3) + 5c_3 = -8
$$

$$
-2 - 2c_3 + 5c_3 = -8
$$

$$
3c_3 = -6 \implies c_3 = -2
$$

We use $c\_3 = -2$ in equation (4):

$$
c_2 = -1 - (-2) = 1
$$

We use $c\_2 = 1$ and $c\_3 = -2$ to find $c\_1$:

$$
c_1 = 3 - 2(1) - (-2) = 3
$$

Thus, the linear combination is:

$$
v = 3P_1 + P_2 - 2P_3
$$

---

### Q7(b) Define direct sum. Give an example of direct sum. (02)

**Answer:**

#### 1. Definition
Let $V$ be a vector space. Let $U$ and $W$ be subspaces of $V$. We say $V$ is the direct sum of $U$ and $W$, written as $V = U \oplus W$, if:
*   $V = U + W$. This means every vector $v \in V$ can be written as $v = u + w$ for some $u \in U$ and $w \in W$.
*   $U \cap W = \{0\}$. This means the intersection of $U$ and $W$ contains only the zero vector.

Equivalently, every vector $v \in V$ can be written uniquely as $v = u + w$, where $u \in U$ and $w \in W$.

#### 2. Example
Let $V = \mathbb{R}^2$ be the two-dimensional real plane.
Let $U$ be the x-axis, which is the subspace of all vectors of the form $(x, 0)$:

$$
U = \{ (x, 0) \mid x \in \mathbb{R} \}
$$

Let $W$ be the y-axis, which is the subspace of all vectors of the form $(0, y)$:

$$
W = \{ (0, y) \mid y \in \mathbb{R} \}
$$

We show that $\mathbb{R}^2 = U \oplus W$:
*   Any vector $v = (a, b) \in \mathbb{R}^2$ can be written as $(a, b) = (a, 0) + (0, b)$, where $(a, 0) \in U$ and $(0, b) \in W$.
*   The only vector that lies on both the x-axis and the y-axis is the origin $(0, 0)$. So, $U \cap W = \{(0, 0)\}$.

Thus, $V$ is the direct sum of $U$ and $W$.

---

### Q7(c) What is a linearly independent vector? Determine whether the vectors are linearly independent or not: (05)
*   (i) $u = (1, 1, 0), v = (1, 3, 2), w = (4, 9, 5)$
*   (ii) $u = (1, 2, 3), v = (2, 5, 7), w = (1, 3, 5)$

**Answer:**

#### 1. Definition of Linearly Independent Vectors
A set of vectors $\{v\_1, v\_2, \dots, v\_n\}$ is linearly independent if the equation:

$$
c_1 v_1 + c_2 v_2 + \dots + c_n v_n = 0
$$

has only the trivial solution $c\_1 = c\_2 = \dots = c\_n = 0$. If there is a solution with some non-zero coefficients, the vectors are linearly dependent.

#### 2. Determine Linear Independence

##### (i) $u = (1, 1, 0), v = (1, 3, 2), w = (4, 9, 5)$
We set up a matrix with these vectors as rows and check its determinant:

$$
D = \begin{vmatrix}
1 & 1 & 0 \\
1 & 3 & 2 \\
4 & 9 & 5
\end{vmatrix}
$$

We calculate the determinant:

$$
D = 1(15 - 18) - 1(5 - 8) + 0 = -3 - (-3) = 0
$$

The determinant is zero. So, the vectors are **linearly dependent**.
We can find a non-trivial linear combination:

$$
3u + 5v - 2w = 3(1, 1, 0) + 5(1, 3, 2) - 2(4, 9, 5) = (3+5-8, 3+15-18, 0+10-10) = (0, 0, 0)
$$

##### (ii) $u = (1, 2, 3), v = (2, 5, 7), w = (1, 3, 5)$
We set up a matrix with these vectors as rows and check its determinant:

$$
D = \begin{vmatrix}
1 & 2 & 3 \\
2 & 5 & 7 \\
1 & 3 & 5
\end{vmatrix}
$$

We calculate the determinant:

$$
D = 1(25 - 21) - 2(10 - 7) + 3(6 - 5) = 4 - 6 + 3 = 1
$$

The determinant is 1, which is not zero. So, the vectors are **linearly independent**.

---

### Q8(a) What is vector space? Also define the basis and dimension of a vector space. (02)

**Answer:**

#### 1. Vector Space
A vector space $V$ over a field $F$ is a set of elements (called vectors) together with two operations: vector addition and scalar multiplication. These operations must satisfy the following eight axioms for all vectors $u, v, w \in V$ and scalars $a, b \in F$:
*   **Associativity of addition:** $u + (v + w) = (u + v) + w$
*   **Commutativity of addition:** $u + v = v + u$
*   **Identity element of addition:** There exists a zero vector $0 \in V$ such that $u + 0 = u$.
*   **Inverse elements of addition:** For every $u \in V$, there exists an element $-u \in V$ such that $u + (-u) = 0$.
*   **Compatibility of scalar multiplication:** $a(bu) = (ab)u$
*   **Identity element of scalar multiplication:** $1u = u$, where $1$ is the multiplicative identity in $F$.
*   **Distributivity of scalar multiplication over vector addition:** $a(u + v) = au + av$
*   **Distributivity of scalar multiplication over field addition:** $(a + b)u = au + bu$

#### 2. Basis of a Vector Space
A subset $B = \{v\_1, v\_2, \dots, v\_n\}$ of a vector space $V$ is a basis of $V$ if:
*   The set $B$ is linearly independent.
*   The set $B$ spans $V$. This means any vector in $V$ can be written as a linear combination of vectors in $B$.

#### 3. Dimension of a Vector Space
The dimension of a vector space $V$ is the number of vectors in any basis of $V$.

---

### Q8(b) Let $U$ consists of all vectors in $\mathbb{R}^3$ whose entries are equal that is $u = \{(a, b, c) \mid a = b = c\}$, prove that $U$ is a vector space over $\mathbb{R}$. (04)

**Answer:**

Since $U$ is a subset of the vector space $\mathbb{R}^3$, we can show it is a subspace. A subspace of $\mathbb{R}^3$ is itself a vector space. We check the three subspace criteria:

#### 1. Contains the Zero Vector
The zero vector of $\mathbb{R}^3$ is $(0, 0, 0)$. Since $0 = 0 = 0$, we have:

$$
(0, 0, 0) \in U
$$

#### 2. Closed Under Vector Addition
Let $u\_1 = (a\_1, a\_1, a\_1) \in U$ and $u\_2 = (a\_2, a\_2, a\_2) \in U$, where $a\_1, a\_2 \in \mathbb{R}$.
We add these vectors:

$$
u_1 + u_2 = (a_1 + a_2, a_1 + a_2, a_1 + a_2)
$$

All three components of the sum vector are equal to $a\_1 + a\_2$. So, the sum vector is in $U$.

#### 3. Closed Under Scalar Multiplication
Let $u = (a, a, a) \in U$ and $k \in \mathbb{R}$ be a scalar.
We multiply the vector by the scalar:

$$
k u = (ka, ka, ka)
$$

All three components of the resulting vector are equal to $ka$. So, this vector is in $U$.

Since $U$ satisfies all three conditions, it is a subspace of $\mathbb{R}^3$. Therefore, $U$ is a vector space over $\mathbb{R}$.

---

### Q8(c) Determine whether or not the vectors $(1, 1, 1, 1), (1, 2, 3, 2), (2, 5, 6, 4)$ and $(2, 6, 8, 5)$ form a basis of $\mathbb{R}^4$. (04)

**Answer:**

The vector space $\mathbb{R}^4$ has a dimension of 4. A set of four vectors forms a basis of $\mathbb{R}^4$ if and only if they are linearly independent.

We set up a matrix with these vectors as rows:

$$
M = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 2 & 3 & 2 \\
2 & 5 & 6 & 4 \\
2 & 6 & 8 & 5
\end{bmatrix}
$$

We apply row operations to find its echelon form:
*   $R\_2 \to R\_2 - R\_1$
*   $R\_3 \to R\_3 - 2R\_1$
*   $R\_4 \to R\_4 - 2R\_1$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 2 & 1 \\
0 & 3 & 4 & 2 \\
0 & 4 & 6 & 3
\end{bmatrix}
$$

Next, we apply:
*   $R\_3 \to R\_3 - 3R\_2$
*   $R\_4 \to R\_4 - 4R\_2$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 2 & 1 \\
0 & 0 & -2 & -1 \\
0 & 0 & -2 & -1
\end{bmatrix}
$$

Now, we perform:
*   $R\_4 \to R\_4 - R\_3$

This yields:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 2 & 1 \\
0 & 0 & -2 & -1 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

The last row is all zeros. So, the rank of the matrix is 3, not 4.
This means the four vectors are linearly dependent.

Therefore, these vectors do not form a basis of $\mathbb{R}^4$.

---

[⬅ 2023](2023_answer.md) | [🏠 Index](00-index.md) | *(end)*
