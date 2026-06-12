[⬅ 2017](2017_answer.md) | [🏠 Index](00-index.md) | [2019 ➡](2019_answer.md)

---

# B.Sc. Engineering 2nd Year Odd Semester Examination 2018
**Course No: Math 2117**
**Course Title: Vector Analysis & Linear Algebra**
**Time: 3 Hours**
**Full Marks: 72**

---

## SECTION - A

### Q1(a) Show that the vectors 

$$
\bar{A} = 2\hat{i} + \hat{j} - 3\hat{k}, \quad \bar{B} = \hat{i} - 4\hat{k}, \quad \bar{C} = 4\hat{i} + 3\hat{j} - \hat{k}
$$

 are linearly dependent and determine a relation between them and hence show that the terminal points are collinear. (06)

**Answer:**

#### 1. Show Linear Dependence

We set up a matrix with the given vectors as its rows. The vectors are linearly dependent if the determinant of this matrix is zero:

$$
D = \begin{vmatrix}
2 & 1 & -3 \\
1 & 0 & -4 \\
4 & 3 & -1
\end{vmatrix}
$$

We expand the determinant along the first row:

$$
D = 2(0( -1) - (-4)(3)) - 1(1( -1) - (-4)(4)) - 3(1(3) - 0(4))
$$

$$
D = 2(12) - 1(-1 + 16) - 3(3) = 24 - 15 - 9 = 0
$$

Since the determinant is zero, the vectors are coplanar. So they are linearly dependent.

#### 2. Determine the Relation

We write the linear combination equal to the zero vector:

$$
x\bar{A} + y\bar{B} + z\bar{C} = 0
$$

Substitute the vectors:

$$
x(2\hat{i} + \hat{j} - 3\hat{k}) + y(\hat{i} - 4\hat{k}) + z(4\hat{i} + 3\hat{j} - \hat{k}) = 0
$$

This gives a system of three equations:

$$
2x + y + 4z = 0 \quad \dots \text{(1)}
$$

$$
x + 3z = 0 \implies x = -3z \quad \dots \text{(2)}
$$

$$
-3x - 4y - z = 0 \quad \dots \text{(3)}
$$

We substitute $x = -3z$ into equation (1):

$$
2(-3z) + y + 4z = 0 \implies -6z + y + 4z = 0 \implies y = 2z
$$

Let $z = 1$. This gives:

$$
x = -3, \quad y = 2, \quad z = 1
$$

Substitute these values into the linear combination:

$$
-3\bar{A} + 2\bar{B} + \bar{C} = 0 \implies \bar{C} = 3\bar{A} - 2\bar{B}
$$

This is the required relation.

#### 3. Show Terminal Points are Collinear

Let $P, Q, R$ be the terminal points of the position vectors $\bar{A}, \bar{B}, \bar{C}$ from the origin. We find the vectors representing the line segments:

$$
\vec{PQ} = \bar{B} - \bar{A} = (\hat{i} - 4\hat{k}) - (2\hat{i} + \hat{j} - 3\hat{k}) = -\hat{i} - \hat{j} - \hat{k}
$$

$$
\vec{PR} = \bar{C} - \bar{A} = (4\hat{i} + 3\hat{j} - \hat{k}) - (2\hat{i} + \hat{j} - 3\hat{k}) = 2\hat{i} + 2\hat{j} + 2\hat{k}
$$

We see that:

$$
\vec{PR} = -2\vec{PQ}
$$

So the vectors $\vec{PR}$ and $\vec{PQ}$ are parallel. Since they share the common point $P$, the terminal points $P, Q, R$ are collinear.

---

### Q1(b) Find the constants $a, b, c$ so that 

$$
\bar{V} = (x + 2y + az)\hat{i} + (bx - 3y - z)\hat{j} + (4x + cy + 2z)\hat{k}
$$

 is irrotational. (03)

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

So the constants are 

$$
a = 4, \quad b = 2, \quad c = -1
$$

---

### Q1(c) If $\bar{A}$ is a constant vector, then prove that $\nabla(\bar{r} \cdot \bar{A}) = \bar{A}$. (03)

**Answer:**

Let the constant vector be:

$$
\bar{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}
$$

Let the position vector be:

$$
\bar{r} = x\hat{i} + y\hat{j} + z\hat{k}
$$

Calculate the dot product:

$$
\bar{r} \cdot \bar{A} = A_1x + A_2y + A_3z
$$

Now calculate the gradient:

$$
\nabla(\bar{r} \cdot \bar{A}) = \frac{\partial}{\partial x}(A_1x + A_2y + A_3z)\hat{i} + \frac{\partial}{\partial y}(A_1x + A_2y + A_3z)\hat{j} + \frac{\partial}{\partial z}(A_1x + A_2y + A_3z)\hat{k}
$$

$$
\nabla(\bar{r} \cdot \bar{A}) = A_1\hat{i} + A_2\hat{j} + A_3\hat{k} = \bar{A}
$$

This completes the proof.

---

### Q2(a) Prove that 

$$
\bar{F} = (y^2 \cos x + z^3)\hat{i} + (2y \sin x - 4)\hat{j} + (3xz^2 + 2)\hat{k}
$$

 represents a conservative force field. Also find the scalar potential for $\bar{F}$. (06)

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

### Q2(b) If 

$$
\bar{A} = (3x^2 + 6y)\hat{i} - 14yz\hat{j} + 20xz^2\hat{k}
$$

Then evaluate

$$
\int_C \bar{A} \cdot d\bar{r}
$$

 from $(0,0,0)$ to $(1,1,1)$ along the following paths $C$: (06)
*   **(i)** $x = t, y = t^2, z = t^3$
*   **(ii)** the straight line joining $(0,0,0)$ to $(1,1,1)$.

**Answer:**

We write the line integral as:

$$
\int_C \bar{A} \cdot d\bar{r} = \int_C \left[ (3x^2 + 6y)dx - 14yz dy + 20xz^2 dz \right]
$$

#### Path (i): $x = t, y = t^2, z = t^3$

Here we calculate the differentials:

$$
dx = dt, \quad dy = 2t dt, \quad dz = 3t^2 dt
$$

As the path goes from $(0,0,0)$ to $(1,1,1)$, the parameter $t$ goes from $0$ to $1$. Substitute these into the integral:

$$
\int_C \bar{A} \cdot d\bar{r} = \int_0^1 \left[ (3t^2 + 6t^2)dt - 14(t^2)(t^3)(2t dt) + 20(t)(t^3)^2 (3t^2 dt) \right]
$$

$$
\int_C \bar{A} \cdot d\bar{r} = \int_0^1 \left( 9t^2 - 28t^6 + 60t^9 \right) dt
$$

Integrate the terms:

$$
\int_C \bar{A} \cdot d\bar{r} = \left[ 3t^3 - 4t^7 + 6t^{10} \right]_0^1 = 3 - 4 + 6 = 5
$$

So the integral along this path is $5$.

#### Path (ii): The straight line

The straight line from $(0,0,0)$ to $(1,1,1)$ is defined by:

$$
x = t, \quad y = t, \quad z = t
$$

with $t$ from $0$ to $1$. The differentials are:

$$
dx = dt, \quad dy = dt, \quad dz = dt
$$

Substitute these into the integral:

$$
\int_C \bar{A} \cdot d\bar{r} = \int_0^1 \left[ (3t^2 + 6t)dt - 14(t)(t)dt + 20(t)(t)^2 dt \right]
$$

$$
\int_C \bar{A} \cdot d\bar{r} = \int_0^1 \left( 20t^3 - 11t^2 + 6t \right) dt
$$

Integrate the terms:

$$
\int_C \bar{A} \cdot d\bar{r} = \left[ 5t^4 - \frac{11}{3}t^3 + 3t^2 \right]_0^1 = 5 - \frac{11}{3} + 3 = 8 - \frac{11}{3} = \frac{13}{3}
$$

So the integral along this path is $\frac{13}{3}$.

---

### Q3(a) Let $\Phi = 45x^2y$ and let $V$ denote the closed region bounded by the planes $4x + 2y + z = 8$, $x = 0, y = 0, z = 0$. Evaluate 

$$
\iiint_V \Phi dV
$$

(06)

**Answer:**

We set up the limits of integration for the region $V$:
*   The variable $z$ goes from the plane $z = 0$ to the plane $z = 8 - 4x - 2y$.
*   For $z=0$, the boundary is $4x + 2y = 8 \implies y = 4 - 2x$. So $y$ goes from $0$ to $4 - 2x$.
*   For $y=z=0$, the boundary is $4x = 8 \implies x = 2$. So $x$ goes from $0$ to $2$.

We write the triple integral:

$$
\iiint_V \Phi dV = \int_{x=0}^2 \int_{y=0}^{4-2x} \int_{z=0}^{8-4x-2y} 45x^2y dz dy dx
$$

Integrate with respect to $z$:

$$
\iiint_V \Phi dV = 45 \int_0^2 x^2 \int_0^{4-2x} y [z]_0^{8-4x-2y} dy dx = 45 \int_0^2 x^2 \int_0^{4-2x} y (8 - 4x - 2y) dy dx
$$

$$
\iiint_V \Phi dV = 45 \int_0^2 x^2 \int_0^{4-2x} \left[ (8 - 4x)y - 2y^2 \right] dy dx
$$

Integrate with respect to $y$:

$$
\iiint_V \Phi dV = 45 \int_0^2 x^2 \left[ (8 - 4x)\frac{y^2}{2} - \frac{2y^3}{3} \right]_0^{4-2x} dx
$$

$$
\iiint_V \Phi dV = 45 \int_0^2 x^2 \left[ (4 - 2x)(4-2x)^2 - \frac{2}{3}(4-2x)^3 \right] dx
$$

$$
\iiint_V \Phi dV = 45 \int_0^2 x^2 \left[ (4-2x)^3 - \frac{2}{3}(4-2x)^3 \right] dx = 45 \int_0^2 x^2 \left[ \frac{1}{3}(4-2x)^3 \right] dx
$$

Factor out $2^3 = 8$ from $(4-2x)^3$:

$$
\iiint_V \Phi dV = 15 \int_0^2 x^2 \left[ 8(2-x)^3 \right] dx = 120 \int_0^2 x^2 (2-x)^3 dx
$$

Expand $(2-x)^3 = 8 - 12x + 6x^2 - x^3$:

$$
\iiint_V \Phi dV = 120 \int_0^2 (8x^2 - 12x^3 + 6x^4 - x^5) dx
$$

Now integrate with respect to $x$:

$$
\iiint_V \Phi dV = 120 \left[ \frac{8}{3}x^3 - 3x^4 + \frac{6}{5}x^5 - \frac{x^6}{6} \right]_0^2
$$

$$
\iiint_V \Phi dV = 120 \left( \frac{64}{3} - 48 + \frac{192}{5} - \frac{64}{6} \right) = 120 \left( \frac{32}{3} - 48 + \frac{192}{5} \right)
$$

$$
\iiint_V \Phi dV = 120 \left( \frac{160 - 720 + 576}{15} \right) = 120 \left( \frac{16}{15} \right) = 8 \times 16 = 128
$$

So the value of the triple integral is $128$.

---

### Q3(b) Verify the divergence theorem for 

$$
\bar{A} = 4x\hat{i} - 2y^2\hat{j} + z^2\hat{k}
$$

 taken over the region bounded by 

$$
x^2 + y^2 = 4, \quad z = 0, \quad z = 3
$$

(06)

**Answer:**

The divergence theorem states:

$$
\iiint_V \bar{\nabla} \cdot \bar{A} dV = \iint_S \bar{A} \cdot \hat{n} dS
$$

#### 1. Evaluate Volume Integral

Calculate the divergence of $\bar{A}$:

$$
\bar{\nabla} \cdot \bar{A} = \frac{\partial}{\partial x}(4x) + \frac{\partial}{\partial y}(-2y^2) + \frac{\partial}{\partial z}(z^2) = 4 - 4y + 2z
$$

We use cylindrical coordinates: 

$$
x = r\cos\phi, \quad y = r\sin\phi, \quad z = z
$$

And $dV = r dr d\phi dz$. The limits are:

$$
r \in [0, 2], \quad \phi \in [0, 2\pi], \quad z \in [0, 3]
$$

Set up the integral:

$$
\iiint_V \bar{\nabla} \cdot \bar{A} dV = \int_{z=0}^3 \int_{\phi=0}^{2\pi} \int_{r=0}^2 (4 - 4r\sin\phi + 2z) r dr d\phi dz
$$

Integrate with respect to $\phi$ first:

$$
\int_0^{2\pi} (4r - 4r^2\sin\phi + 2rz) d\phi = \left[ (4r + 2rz)\phi + 4r^2\cos\phi \right]_0^{2\pi} = 2\pi(4r + 2rz)
$$

Now integrate with respect to $r$:

$$
2\pi \int_0^2 (4r + 2rz) dr = 2\pi \left[ 2r^2 + r^2 z \right]_0^2 = 2\pi(8 + 4z)
$$

Now integrate with respect to $z$:

$$
2\pi \int_0^3 (8 + 4z) dz = 2\pi \left[ 8z + 2z^2 \right]_0^3 = 2\pi(24 + 18) = 84\pi
$$

#### 2. Evaluate Surface Integral

The cylinder surface $S$ has three parts:
1.  Top surface $S\_1$ ($z=3$): The normal vector is 

$$
\hat{n} = \hat{k}
$$

2.  Bottom surface $S\_2$ ($z=0$): The normal vector is 

$$
\hat{n} = -\hat{k}
$$

3.  Curved wall $S\_3$ ($x^2 + y^2 = 4$): The normal vector is 

$$
\hat{n} = \frac{x\hat{i} + y\hat{j}}{2}
$$

Evaluate the top surface integral:

$$
\bar{A} \cdot \hat{n} = \bar{A} \cdot \hat{k} = z^2 = 9
$$

$$
\iint_{S_1} \bar{A} \cdot \hat{n} dS = 9 \iint_{S_1} dS = 9 \times \pi(2)^2 = 36\pi
$$

Evaluate the bottom surface integral:

$$
\bar{A} \cdot \hat{n} = \bar{A} \cdot (-\hat{k}) = -z^2 = 0
$$

$$
\iint_{S_2} \bar{A} \cdot \hat{n} dS = 0
$$

Evaluate the curved wall integral:

$$
\bar{A} \cdot \hat{n} = (4x\hat{i} - 2y^2\hat{j} + z^2\hat{k}) \cdot \left( \frac{x\hat{i} + y\hat{j}}{2} \right) = 2x^2 - y^3
$$

We use cylindrical coordinates: 

$$
x = 2\cos\phi, \quad y = 2\sin\phi, \quad dS = 2 d\phi dz
$$

$$
\iint_{S_3} \bar{A} \cdot \hat{n} dS = \int_0^3 \int_0^{2\pi} \left[ 2(4\cos^2\phi) - 8\sin^3\phi \right] 2 d\phi dz
$$

We use the standard integral properties: 

$$
\int_0^{2\pi} \cos^2\phi d\phi = \pi
$$

 and 

$$
\int_0^{2\pi} \sin^3\phi d\phi = 0
$$

$$
\iint_{S_3} \bar{A} \cdot \hat{n} dS = \int_0^3 16\pi dz = 48\pi
$$

Add the three surface integrals:

$$
\iint_S \bar{A} \cdot \hat{n} dS = 36\pi + 0 + 48\pi = 84\pi
$$

Both the volume and surface integrals equal $84\pi$. The divergence theorem is verified.

---

### Q4(a) Show that $\nabla \times (\nabla \times \bar{A}) = -\nabla^2\bar{A} + \nabla(\nabla \cdot \bar{A})$. (05)

**Answer:**

Let the vector be 

$$
\bar{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}
$$

We calculate the curl of $\bar{A}$:

$$
\nabla \times \bar{A} = \left( \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z} \right)\hat{i} + \left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right)\hat{j} + \left( \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} \right)\hat{k}
$$

Let this vector be $\bar{V} = \nabla \times \bar{A}$. Now we find the curl of $\bar{V}$:

$$
\nabla \times (\nabla \times \bar{A}) = \nabla \times \bar{V} = \left( \frac{\partial V_z}{\partial y} - \frac{\partial V_y}{\partial z} \right)\hat{i} + \left( \frac{\partial V_x}{\partial z} - \frac{\partial V_z}{\partial x} \right)\hat{j} + \left( \frac{\partial V_y}{\partial x} - \frac{\partial V_x}{\partial y} \right)\hat{k}
$$

We evaluate the x-component:

$$
(\nabla \times \bar{V})_x = \frac{\partial}{\partial y}\left( \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} \right) - \frac{\partial}{\partial z}\left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right)
$$

$$
(\nabla \times \bar{V})_x = \frac{\partial^2 A_y}{\partial y \partial x} - \frac{\partial^2 A_x}{\partial y^2} - \frac{\partial^2 A_x}{\partial z^2} + \frac{\partial^2 A_z}{\partial z \partial x}
$$

We add and subtract

$$
\frac{\partial^2 A\_x}{\partial x^2}
$$

to the expression:

$$
(\nabla \times \bar{V})_x = \left( \frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_y}{\partial y \partial x} + \frac{\partial^2 A_z}{\partial z \partial x} \right) - \left( \frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_x}{\partial y^2} + \frac{\partial^2 A_x}{\partial z^2} \right)
$$

$$
(\nabla \times \bar{V})_x = \frac{\partial}{\partial x}\left( \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z} \right) - \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} \right)A_x
$$

$$
(\nabla \times \bar{V})_x = \frac{\partial}{\partial x}(\nabla \cdot \bar{A}) - \nabla^2 A_x
$$

By using the same steps for the y and z-components, we get the vector identity:

$$
\nabla \times (\nabla \times \bar{A}) = \nabla(\nabla \cdot \bar{A}) - \nabla^2\bar{A}
$$

---

### Q4(b) Find an equation for the tangent plane to the surface $2xz^2 - 3xy - 4x = 7$ at the point $(1, -1, 2)$. (03)

**Answer:**

Let the surface be defined by the function:

$$
F(x, y, z) = 2xz^2 - 3xy - 4x - 7 = 0
$$

The gradient of $F$ gives the normal vector to the surface:

$$
\vec{\nabla}F = \frac{\partial F}{\partial x}\hat{i} + \frac{\partial F}{\partial y}\hat{j} + \frac{\partial F}{\partial z}\hat{k}
$$

Calculate the partial derivatives:

$$
\frac{\partial F}{\partial x} = 2z^2 - 3y - 4
$$

$$
\frac{\partial F}{\partial y} = -3x
$$

$$
\frac{\partial F}{\partial z} = 4xz
$$

At the point $(1, -1, 2)$, the gradient vector is:

$$
\vec{\nabla}F = (2(4) - 3(-1) - 4)\hat{i} - 3(1)\hat{j} + 4(1)(2)\hat{k} = 7\hat{i} - 3\hat{j} + 8\hat{k}
$$

The equation of the tangent plane at $(x\_0, y\_0, z\_0) = (1, -1, 2)$ is:

$$
7(x - 1) - 3(y - (-1)) + 8(z - 2) = 0
$$

$$
7x - 7 - 3y - 3 + 8z - 16 = 0 \implies 7x - 3y + 8z = 26
$$

So the equation of the tangent plane is $7x - 3y + 8z = 26$.

---

### Q4(c) What is directional derivative? Find the directional derivative of $\phi = x^2yz + 4xz^2$ at $(1, -2, -1)$ in the direction 

$$
2\hat{i} - \hat{j} - 2\hat{k}
$$

(04)

**Answer:**

#### 1. Definition

The directional derivative is the rate of change of a scalar function at a given point in a specific direction. It equals the dot product of the function's gradient and the unit direction vector.

#### 2. Calculation

Let the direction vector be 

$$
\vec{d} = 2\hat{i} - \hat{j} - 2\hat{k}
$$

The unit direction vector $\hat{u}$ is:

$$
\hat{u} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{\sqrt{2^2 + (-1)^2 + (-2)^2}} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{\sqrt{9}} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3}
$$

Next we find the gradient of $\phi = x^2yz + 4xz^2$:

$$
\vec{\nabla}\phi = (2xyz + 4z^2)\hat{i} + x^2z\hat{j} + (x^2y + 8xz)\hat{k}
$$

At the point $(1, -2, -1)$, the gradient vector is:

$$
\vec{\nabla}\phi = (2(1)(-2)(-1) + 4(1))\hat{i} + (1)(-1)\hat{j} + ((1)(-2) + 8(1)(-1))\hat{k}
$$

$$
\vec{\nabla}\phi = (4 + 4)\hat{i} - \hat{j} + (-2 - 8)\hat{k} = 8\hat{i} - \hat{j} - 10\hat{k}
$$

The directional derivative is:

$$
D_{\hat{u}}\phi = \vec{\nabla}\phi \cdot \hat{u} = (8\hat{i} - \hat{j} - 10\hat{k}) \cdot \left( \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3} \right)
$$

$$
D_{\hat{u}}\phi = \frac{8(2) + (-1)(-1) + (-10)(-2)}{3} = \frac{16 + 1 + 20}{3} = \frac{37}{3}
$$

So the directional derivative is $\frac{37}{3}$.

---

## SECTION - B

### Q5(a) Define symmetric, skew-symmetric, and Hermitian matrices with examples. (03)

**Answer:**

#### Symmetric Matrix

A square matrix $A$ is symmetric if it equals its transpose:

$$
A^T = A
$$

*Example:*

$$
\begin{pmatrix}
1 & 2 \\
2 & 5
\end{pmatrix}
$$

#### Skew-Symmetric Matrix

A square matrix $A$ is skew-symmetric if its transpose equals its negative:

$$
A^T = -A
$$

The diagonal elements of a skew-symmetric matrix are always zero.

*Example:*

$$
\begin{pmatrix}
0 & -3 \\
3 & 0
\end{pmatrix}
$$

#### Hermitian Matrix

A square matrix $A$ with complex entries is Hermitian if it equals its conjugate transpose:

$$
A^\dagger = (\bar{A})^T = A
$$

*Example:*

$$
\begin{pmatrix}
2 & 1+i \\
1-i & 3
\end{pmatrix}
$$

---

### Q5(b) Define singular matrix. If $A$ and $B$ are non-singular matrices of the same order, then show that $(AB)^{-1} = B^{-1}A^{-1}$. Hence prove that $(A^{-1})^n = (A^n)^{-1}$ for any positive integer. (05)

**Answer:**

#### 1. Singular Matrix

A square matrix is singular if its determinant is zero. It has no inverse.

#### 2. Prove $(AB)^{-1} = B^{-1}A^{-1}$

We multiply $AB$ by $B^{-1}A^{-1}$:

$$
(AB)(B^{-1}A^{-1}) = A(B B^{-1})A^{-1} = A I A^{-1} = A A^{-1} = I
$$

$$
(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1} I B = B^{-1} B = I
$$

Since the product in both directions is the identity matrix, we get:

$$
(AB)^{-1} = B^{-1}A^{-1}
$$

#### 3. Prove $(A^{-1})^n = (A^n)^{-1}$

We use mathematical induction on $n$:

*   **Base Case ($n=1$):** $(A^{-1})^1 = (A^1)^{-1}$, which is true.
*   **Inductive Step:** Assume the statement is true for $n=k$:

$$
(A^{-1})^k = (A^k)^{-1}
$$

We test for $n = k+1$:

$$
(A^{k+1})^{-1} = (A^k \cdot A)^{-1}
$$

Using the product inverse property shown above:

$$
(A^k \cdot A)^{-1} = A^{-1} \cdot (A^k)^{-1}
$$

Substitute the induction assumption:

$$
A^{-1} \cdot (A^k)^{-1} = A^{-1} \cdot (A^{-1})^k = (A^{-1})^{k+1}
$$

So the statement is true for $n=k+1$. The proof is complete.

---

### Q5(c) What is rank of a matrix? Find the rank of 

$$
A = \begin{pmatrix}
1 & -2 & 1 & -1 \\
1 & 1 & -2 & 3 \\
4 & 1 & -5 & 8 \\
5 & -7 & 2 & -1
\end{pmatrix}
$$

(04)

**Answer:**

#### Rank of a Matrix

The rank of a matrix is the maximum number of linearly independent rows in it. It equals the number of non-zero rows in its row-echelon form.

#### Finding the Rank

Let the matrix be:

$$
A = \begin{pmatrix}
1 & -2 & 1 & -1 \\
1 & 1 & -2 & 3 \\
4 & 1 & -5 & 8 \\
5 & -7 & 2 & -1
\end{pmatrix}
$$

We apply row operations:
*   $R\_2 \to R\_2 - R\_1$
*   $R\_3 \to R\_3 - 4R\_1$
*   $R\_4 \to R\_4 - 5R\_1$

This gives:

$$
\begin{pmatrix}
1 & -2 & 1 & -1 \\
0 & 3 & -3 & 4 \\
0 & 9 & -9 & 12 \\
0 & 3 & -3 & 4
\end{pmatrix}
$$

Now perform operations on rows 3 and 4:
*   $R\_3 \to R\_3 - 3R\_2$
*   $R\_4 \to R\_4 - R\_2$

This gives:

$$
\begin{pmatrix}
1 & -2 & 1 & -1 \\
0 & 3 & -3 & 4 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

The matrix is now in echelon form. The number of non-zero rows is $2$.

So the rank of the matrix is $2$.

---

### Q6(a) Find the value of $\lambda$ so that the following equations have a solution and solve completely in each case: (06)

$$
x + y + z = 1
$$

$$
x + 2y + 4z = \lambda
$$

$$
x + 4y + 10z = \lambda^2
$$

**Answer:**

We write the augmented matrix of the system:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
1 & 2 & 4 & | & \lambda \\
1 & 4 & 10 & | & \lambda^2
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - R\_1$
*   $R\_3 \to R\_3 - R\_1$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 3 & | & \lambda - 1 \\
0 & 3 & 9 & | & \lambda^2 - 1
\end{bmatrix}
$$

Now eliminate row 3 using row 2 ($R\_3 \to R\_3 - 3R\_2$):

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 3 & | & \lambda - 1 \\
0 & 0 & 0 & | & \lambda^2 - 3\lambda + 2
\end{bmatrix}
$$

A solution exists if the system is consistent:

$$
\lambda^2 - 3\lambda + 2 = 0 \implies (\lambda - 1)(\lambda - 2) = 0 \implies \lambda = 1 \quad \text{or} \quad \lambda = 2
$$

We solve the system for each case:

#### Case 1: For $\lambda = 1$

The augmented matrix is:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 3 & | & 0 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

From row 2:

$$
y + 3z = 0 \implies y = -3z
$$

From row 1:

$$
x + y + z = 1 \implies x - 3z + z = 1 \implies x = 2z + 1
$$

Let $z = t$ be a parameter. The general solution is:

$$
x = 2t + 1, \quad y = -3t, \quad z = t
$$

#### Case 2: For $\lambda = 2$

The augmented matrix is:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 3 & | & 1 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

From row 2:

$$
y + 3z = 1 \implies y = 1 - 3z
$$

From row 1:

$$
x + y + z = 1 \implies x + (1 - 3z) + z = 1 \implies x = 2z
$$

Let $z = t$ be a parameter. The general solution is:

$$
x = 2t, \quad y = 1 - 3t, \quad z = t
$$

---

### Q6(b) Solve: (06)

$$
2x_1 - x_2 + x_3 = 0
$$

$$
3x_1 + 2x_2 + x_3 = 0
$$

$$
x_1 - 3x_2 + 5x_3 = 0
$$

**Answer:**

We write the augmented matrix of this homogeneous system:

$$
\begin{bmatrix}
2 & -1 & 1 & | & 0 \\
3 & 2 & 1 & | & 0 \\
1 & -3 & 5 & | & 0
\end{bmatrix}
$$

We swap row 1 and row 3 ($R\_1 \leftrightarrow R\_3$):

$$
\begin{bmatrix}
1 & -3 & 5 & | & 0 \\
3 & 2 & 1 & | & 0 \\
2 & -1 & 1 & | & 0
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 3R\_1$
*   $R\_3 \to R\_3 - 2R\_1$

This gives:

$$
\begin{bmatrix}
1 & -3 & 5 & | & 0 \\
0 & 11 & -14 & | & 0 \\
0 & 5 & -9 & | & 0
\end{bmatrix}
$$

Perform the operation $R\_3 \to 11R\_3 - 5R\_2$:

$$
\begin{bmatrix}
1 & -3 & 5 & | & 0 \\
0 & 11 & -14 & | & 0 \\
0 & 0 & -29 & | & 0
\end{bmatrix}
$$

By back substitution, we solve the system:
*   From the third row: $-29x\_3 = 0 \implies x\_3 = 0$.
*   From the second row: $11x\_2 - 14(0) = 0 \implies x\_2 = 0$.
*   From the first row: $x\_1 - 3(0) + 5(0) = 0 \implies x\_1 = 0$.

So the system only has the trivial solution:

$$
x_1 = 0, \quad x_2 = 0, \quad x_3 = 0
$$

---

### Q7(a) Define eigen values and eigen vectors. Find the eigen values and associated eigen vectors of 

$$
B = \begin{pmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{pmatrix}
$$

(06)

**Answer:**

#### 1. Definitions

Let $B$ be a square matrix. If there is a scalar $\lambda$ and a non-zero vector $X$ such that $BX = \lambda X$, then $\lambda$ is called an eigenvalue and $X$ is the corresponding eigenvector.

#### 2. Find Eigenvalues

We solve the characteristic equation $|B - \lambda I| = 0$:

$$
\begin{vmatrix}
2-\lambda & 2 & 1 \\
1 & 3-\lambda & 1 \\
1 & 2 & 2-\lambda
\end{vmatrix} = 0
$$

The expansion of this determinant gives the polynomial:

$$
\lambda^3 - 7\lambda^2 + 11\lambda - 5 = 0
$$

$$
(\lambda-1)^2(\lambda-5) = 0
$$

So the eigenvalues are:

$$
\lambda = 5, \quad \lambda = 1, \quad \lambda = 1
$$

#### 3. Find Eigenvectors

##### Case 1: For $\lambda = 5$

We solve $(B - 5I)X = 0$:

$$
\begin{bmatrix}
-3 & 2 & 1 \\
1 & -2 & 1 \\
1 & 2 & -3
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

Reducing the matrix yields:

$$
y = z, \quad x = z
$$

Let $z = 1$. The eigenvector is:

$$
X_1 = \begin{pmatrix}
1 \\
1 \\
1
\end{pmatrix}
$$

##### Case 2: For $\lambda = 1$

We solve $(B - I)X = 0$:

$$
\begin{bmatrix}
1 & 2 & 1 \\
1 & 2 & 1 \\
1 & 2 & 1
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

This reduces to:

$$
x + 2y + z = 0 \implies x = -2y - z
$$

Let $y = s$ and $z = t$. The eigenvectors are:

$$
X = s \begin{pmatrix}
-2 \\
1 \\
0
\end{pmatrix} + t \begin{pmatrix}
-1 \\
0 \\
1
\end{pmatrix}
$$

So the two eigenvectors are:

$$
X_2 = \begin{pmatrix}
-2 \\
1 \\
0
\end{pmatrix}, \quad X_3 = \begin{pmatrix}
-1 \\
0 \\
1
\end{pmatrix}
$$

---

### Q7(b) State and prove Cayley-Hamilton theorem. (06)

**Answer:**

#### Statement

Every square matrix satisfies its own characteristic equation. If the characteristic polynomial of a matrix $A$ of order $n$ is:

$$
p(\lambda) = (-1)^n \lambda^n + c_{n-1} \lambda^{n-1} + \dots + c_0 = 0
$$

then we have:

$$
p(A) = (-1)^n A^n + c_{n-1} A^{n-1} + \dots + c_0 I = 0
$$

#### Proof

The characteristic matrix is $A - \lambda I$. The adjoint matrix $\text{adj}(A - \lambda I)$ contains polynomial elements in $\lambda$ of degree at most $n-1$. We can write it as:

$$
\text{adj}(A - \lambda I) = B_{n-1} \lambda^{n-1} + B_{n-2} \lambda^{n-2} + \dots + B_0
$$

where $B\_i$ are constant matrices of order $n$. We use the fundamental matrix relation:

$$
(A - \lambda I) \text{adj}(A - \lambda I) = |A - \lambda I| I
$$

Let the characteristic polynomial be $|A - \lambda I| = c\_0 + c\_1 \lambda + \dots + (-1)^n \lambda^n$. Substitute this and the adjoint expression:

$$
(A - \lambda I)(B_{n-1} \lambda^{n-1} + B_{n-2} \lambda^{n-2} + \dots + B_0) = (c_0 + c_1 \lambda + \dots + (-1)^n \lambda^n) I
$$

Multiply the terms on the left side:

$$
A B_{n-1} \lambda^{n-1} + \dots + A B_0 - B_{n-1} \lambda^n - \dots - B_0 \lambda = c_0 I + c_1 I \lambda + \dots + (-1)^n I \lambda^n
$$

Equating the coefficients of like powers of $\lambda$:

$$
A B_0 = c_0 I
$$

$$
A B_1 - B_0 = c_1 I
$$

$$
A B_2 - B_1 = c_2 I
$$

$$
\dots
$$

$$
A B_{n-1} - B_{n-2} = c_{n-1} I
$$

$$
-B_{n-1} = (-1)^n I
$$

Now we pre-multiply these equations by $I, A, A^2, \dots, A^n$ respectively:

$$
A B_0 = c_0 I
$$

$$
A^2 B_1 - A B_0 = c_1 A
$$

$$
A^3 B_2 - A^2 B_1 = c_2 A^2
$$

$$
\dots
$$

$$
A^n B_{n-1} - A^{n-1} B_{n-2} = c_{n-1} A^{n-1}
$$

$$
-A^n B_{n-1} = (-1)^n A^n
$$

Add all these equations together. The terms on the left side cancel out to zero:

$$
0 = c_0 I + c_1 A + c_2 A^2 + \dots + (-1)^n A^n = p(A)
$$

So $p(A) = 0$. The theorem is proven.

---

### Q8(a) Define vector space and subspace with examples. (03)

**Answer:**

#### Vector Space

Let $V$ be a non-empty set of vectors and $K$ be a field of scalars. $V$ is a vector space if it satisfies closure, commutative, associative, identity, inverse, and distributive properties under vector addition and scalar multiplication.

*Example:* The space $\mathbb{R}^3$ of all real triples under standard addition and multiplication.

#### Subspace

A non-empty subset $W$ of a vector space $V$ is a subspace if $W$ is closed under addition ($u,v \in W \implies u+v \in W$) and closed under scalar multiplication ($u \in W, k \in K \implies ku \in W$).

*Example:* The plane $z = 0$ in $\mathbb{R}^3$, defined by $W = \{(x, y, 0) \mid x, y \in \mathbb{R}\}$.

---

### Q8(b) Define linearly dependent and independent vectors. Determine whether or not the vectors in $\mathbb{R}^3$ are linearly dependent: $(1, 2, -3)$, $(1, -3, 2)$, $(2, -1, 5)$. (04)

**Answer:**

#### 1. Definitions

*   **Linearly Dependent:** A set of vectors is linearly dependent if a non-trivial linear combination of them equals the zero vector.
*   **Linearly Independent:** A set of vectors is linearly independent if the only linear combination that equals the zero vector is the trivial one (where all coefficients are zero).

#### 2. Check the given vectors

We set up a matrix with these vectors as its columns and calculate its determinant:

$$
D = \begin{vmatrix}
1 & 1 & 2 \\
2 & -3 & -1 \\
-3 & 2 & 5
\end{vmatrix}
$$

Expand along the first row:

$$
D = 1((-3)(5) - (-1)(2)) - 1(2(5) - (-1)(-3)) + 2(2(2) - (-3)(-3))
$$

$$
D = 1(-15 + 2) - 1(10 - 3) + 2(4 - 9) = -13 - 7 - 10 = -30
$$

Since the determinant is not zero ($D = -30 \neq 0$), the vectors are linearly independent. So they are not linearly dependent.

---

### Q8(c) Define basis and dimension. Let $w$ be the subspace of $\mathbb{R}^4$ generated by the vectors $(1, -2, 5, -3)$, $(2, 3, 1, -4)$ and $(3, 8, -3, -5)$. Find a basis and the dimension of $w$. (05)

**Answer:**

#### 1. Definitions

*   **Basis:** A set of vectors in a space is a basis if they are linearly independent and span the space.
*   **Dimension:** The dimension of a space is the number of vectors in its basis.

#### 2. Find Basis and Dimension of $w$

We write the generating vectors as rows of a matrix:

$$
\begin{bmatrix}
1 & -2 & 5 & -3 \\
2 & 3 & 1 & -4 \\
3 & 8 & -3 & -5
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 2R\_1$
*   $R\_3 \to R\_3 - 3R\_1$

This gives:

$$
\begin{bmatrix}
1 & -2 & 5 & -3 \\
0 & 7 & -9 & 2 \\
0 & 14 & -18 & 4
\end{bmatrix}
$$

Now eliminate row 3 using row 2 ($R\_3 \to R\_3 - 2R\_2$):

$$
\begin{bmatrix}
1 & -2 & 5 & -3 \\
0 & 7 & -9 & 2 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

The non-zero rows of this echelon matrix form a basis for $w$:

$$
\text{Basis} = \{ (1, -2, 5, -3), (0, 7, -9, 2) \}
$$

The number of vectors in the basis is 2, so the dimension is:

$$
\text{Dimension} = 2
$$

---

[⬅ 2017](2017_answer.md) | [🏠 Index](00-index.md) | [2019 ➡](2019_answer.md)
