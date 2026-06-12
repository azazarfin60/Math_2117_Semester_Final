*(start)* | [🏠 Index](00-index.md) | [2018 ➡](2018_answer.md)

---

# B.Sc. Engineering 2nd Year Odd Semester Examination 2017
**Course No: Math 2117**
**Course Title: Vector Analysis and Linear Algebra**
**Time: 3 Hours**
**Full Marks: 72**

---

## SECTION - A

### Q1(a) Find the angle between the surfaces $x^2 + y^2 + z^2 = 9$ and $z = x^2 + y^2 - 3$ at the point $(2, -1, 2)$. (04)

**Answer:**

Let the first surface be defined by the function:

$$
f_1(x, y, z) = x^2 + y^2 + z^2 - 9 = 0
$$

The gradient of $f\_1$ gives the normal vector to this surface:

$$
\vec{\nabla}f_1 = 2x\hat{i} + 2y\hat{j} + 2z\hat{k}
$$

At the point $P(2, -1, 2)$, the normal vector $\vec{n}\_1$ is:

$$
\vec{n}_1 = 2(2)\hat{i} + 2(-1)\hat{j} + 2(2)\hat{k} = 4\hat{i} - 2\hat{j} + 4\hat{k}
$$

Let the second surface be defined by the function:

$$
f_2(x, y, z) = x^2 + y^2 - z - 3 = 0
$$

The gradient of $f\_2$ gives the normal vector to this surface:

$$
\vec{\nabla}f_2 = 2x\hat{i} + 2y\hat{j} - \hat{k}
$$

At the point $P(2, -1, 2)$, the normal vector $\vec{n}\_2$ is:

$$
\vec{n}_2 = 2(2)\hat{i} + 2(-1)\hat{j} - \hat{k} = 4\hat{i} - 2\hat{j} - \hat{k}
$$

Let $\theta$ be the angle between these two surfaces. We use the dot product of their normal vectors:

$$
\cos\theta = \frac{\vec{n}_1 \cdot \vec{n}_2}{|\vec{n}_1||\vec{n}_2|}
$$

Calculate the dot product:

$$
\vec{n}_1 \cdot \vec{n}_2 = (4)(4) + (-2)(-2) + (4)(-1) = 16 + 4 - 4 = 16
$$

Calculate the magnitudes of the normal vectors:

$$
|\vec{n}_1| = \sqrt{4^2 + (-2)^2 + 4^2} = \sqrt{16 + 4 + 16} = \sqrt{36} = 6
$$

$$
|\vec{n}_2| = \sqrt{4^2 + (-2)^2 + (-1)^2} = \sqrt{16 + 4 + 1} = \sqrt{21}
$$

Substitute these values back into the cosine equation:

$$
\cos\theta = \frac{16}{6\sqrt{21}} = \frac{8}{3\sqrt{21}}
$$

So the angle $\theta$ is:

$$
\theta = \cos^{-1}\left(\frac{8}{3\sqrt{21}}\right)
$$

---

### Q1(b) If 

$$
\vec{F} = 3xy\hat{i} - y^2\hat{j}
$$

Then evaluate

$$
\int_C \vec{F} \cdot d\vec{r}
$$

When $C$ is the curve in the $xy$ plane, $y = 2x^2$ from $(0,0)$ to $(1,2)$. (04)

**Answer:**

The position vector in the $xy$-plane is 

$$
\vec{r} = x\hat{i} + y\hat{j}
$$

. So we have:

$$
d\vec{r} = dx\hat{i} + dy\hat{j}
$$

We can write the line integral as:

$$
\int_C \vec{F} \cdot d\vec{r} = \int_C (3xy\hat{i} - y^2\hat{j}) \cdot (dx\hat{i} + dy\hat{j}) = \int_C \left( 3xy dx - y^2 dy \right)
$$

The path $C$ is defined by $y = 2x^2$. This gives:

$$
dy = 4x dx
$$

We substitute these terms into our integral. The limit for $x$ goes from $0$ to $1$:

$$
\int_C \vec{F} \cdot d\vec{r} = \int_0^1 \left[ 3x(2x^2) - (2x^2)^2 (4x) \right] dx
$$

Simplify the integrand:

$$
\int_C \vec{F} \cdot d\vec{r} = \int_0^1 \left( 6x^3 - 16x^5 \right) dx
$$

Now integrate term by term:

$$
\int_C \vec{F} \cdot d\vec{r} = \left[ \frac{6x^4}{4} - \frac{16x^6}{6} \right]_0^1 = \left[ \frac{3}{2}x^4 - \frac{8}{3}x^6 \right]_0^1
$$

Evaluate at the limits:

$$
\int_C \vec{F} \cdot d\vec{r} = \left( \frac{3}{2} - \frac{8}{3} \right) - 0 = \frac{9 - 16}{6} = -\frac{7}{6}
$$

So the value of the line integral is $-\frac{7}{6}$.

---

### Q1(c) Find the directional derivative of $\phi = 4e^{2x - y + z}$ at $(1, 1, -1)$ in a direction toward the point $(-3, 5, 6)$. (04)

**Answer:**

Let $P$ be the point $(1, 1, -1)$ and $Q$ be the point $(-3, 5, 6)$.

The direction vector from $P$ to $Q$ is:

$$
\vec{d} = \vec{PQ} = (-3 - 1)\hat{i} + (5 - 1)\hat{j} + (6 - (-1))\hat{k} = -4\hat{i} + 4\hat{j} + 7\hat{k}
$$

We find the unit vector $\hat{u}$ in this direction:

$$
\hat{u} = \frac{\vec{d}}{|\vec{d}|} = \frac{-4\hat{i} + 4\hat{j} + 7\hat{k}}{\sqrt{(-4)^2 + 4^2 + 7^2}} = \frac{-4\hat{i} + 4\hat{j} + 7\hat{k}}{\sqrt{16 + 16 + 49}} = \frac{-4\hat{i} + 4\hat{j} + 7\hat{k}}{\sqrt{81}} = \frac{-4\hat{i} + 4\hat{j} + 7\hat{k}}{9}
$$

Next we find the gradient of $\phi$:

$$
\vec{\nabla}\phi = \frac{\partial\phi}{\partial x}\hat{i} + \frac{\partial\phi}{\partial y}\hat{j} + \frac{\partial\phi}{\partial z}\hat{k}
$$

For $\phi = 4e^{2x - y + z}$, we calculate the partial derivatives:

$$
\frac{\partial\phi}{\partial x} = 8e^{2x - y + z}
$$

$$
\frac{\partial\phi}{\partial y} = -4e^{2x - y + z}
$$

$$
\frac{\partial\phi}{\partial z} = 4e^{2x - y + z}
$$

So the gradient vector is:

$$
\vec{\nabla}\phi = 4e^{2x - y + z} (2\hat{i} - \hat{j} + \hat{k})
$$

At the point $P(1, 1, -1)$, the exponent is $2(1) - 1 + (-1) = 0$. So we get:

$$
\vec{\nabla}\phi|_P = 4e^0 (2\hat{i} - \hat{j} + \hat{k}) = 8\hat{i} - 4\hat{j} + 4\hat{k}
$$

The directional derivative is the dot product of the gradient and the unit vector:

$$
D_{\hat{u}}\phi = \vec{\nabla}\phi|_P \cdot \hat{u} = (8\hat{i} - 4\hat{j} + 4\hat{k}) \cdot \left( \frac{-4\hat{i} + 4\hat{j} + 7\hat{k}}{9} \right)
$$

$$
D_{\hat{u}}\phi = \frac{(8)(-4) + (-4)(4) + (4)(7)}{9} = \frac{-32 - 16 + 28}{9} = \frac{-20}{9}
$$

So the directional derivative is $-\frac{20}{9}$.

---

### Q2(a) If 

$$
\vec{F} = (2x + y^2)\hat{i} + (3y - 4x)\hat{j}
$$

Then evaluate

$$
\oint_C \vec{F} \cdot d\vec{r}
$$

 around the curve $C$ of the following figure: (06)

> [!NOTE]
> **Figure Description:** The curve $C$ is a closed loop in the first quadrant of the $xy$-plane. It is bounded by the parabolas $y = x^2$ and $y^2 = x$. The curves intersect at the points $(0,0)$ and $(1,1)$. The boundary is traversed in the counterclockwise direction.

**Answer:**

We can solve this problem in two ways: using Green's Theorem or using direct line integration.

#### Method 1: Using Green's Theorem

Green's Theorem states:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA
$$

Here we identify the functions:

$$
P = 2x + y^2 \implies \frac{\partial P}{\partial y} = 2y
$$

$$
Q = 3y - 4x \implies \frac{\partial Q}{\partial x} = -4
$$

Substitute these into the integrand:

$$
\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = -4 - 2y
$$

The region $R$ lies between $y = x^2$ and $y = \sqrt{x}$ for $x$ from $0$ to $1$. We set up the double integral:

$$
\oint_C \vec{F} \cdot d\vec{r} = \int_{x=0}^1 \int_{y=x^2}^{\sqrt{x}} (-4 - 2y) dy dx
$$

Integrate with respect to $y$:

$$
\oint_C \vec{F} \cdot d\vec{r} = \int_0^1 \left[ -4y - y^2 \right]_{x^2}^{\sqrt{x}} dx
$$

$$
\oint_C \vec{F} \cdot d\vec{r} = \int_0^1 \left[ (-4\sqrt{x} - x) - (-4x^2 - x^4) \right] dx = \int_0^1 \left( -4x^{1/2} - x + 4x^2 + x^4 \right) dx
$$

Now integrate with respect to $x$:

$$
\oint_C \vec{F} \cdot d\vec{r} = \left[ -\frac{8}{3}x^{3/2} - \frac{1}{2}x^2 + \frac{4}{3}x^3 + \frac{1}{5}x^5 \right]_0^1
$$

$$
\oint_C \vec{F} \cdot d\vec{r} = -\frac{8}{3} - \frac{1}{2} + \frac{4}{3} + \frac{1}{5} = -\frac{4}{3} - \frac{1}{2} + \frac{1}{5}
$$

Find a common denominator of 30:

$$
\oint_C \vec{F} \cdot d\vec{r} = \frac{-40 - 15 + 6}{30} = -\frac{49}{30}
$$

#### Method 2: Direct Line Integration

The boundary curve $C$ consists of two paths:
1.  Path $C\_1$: Along the parabola $y = x^2$ from $(0,0)$ to $(1,1)$. Here $dy = 2x dx$.
2.  Path $C\_2$: Along the parabola $y^2 = x$ from $(1,1)$ to $(0,0)$. We can write this as $x = y^2$ from $y = 1$ to $y = 0$. Here $dx = 2y dy$.

Evaluate the integral along Path $C\_1$:

$$
\int_{C_1} \vec{F} \cdot d\vec{r} = \int_0^1 \left[ (2x + x^4)dx + (3x^2 - 4x)(2x dx) \right] = \int_0^1 \left( 2x + x^4 + 6x^3 - 8x^2 \right) dx
$$

$$
\int_{C_1} \vec{F} \cdot d\vec{r} = \left[ x^2 + \frac{1}{5}x^5 + \frac{3}{2}x^4 - \frac{8}{3}x^3 \right]_0^1 = 1 + \frac{1}{5} + \frac{3}{2} - \frac{8}{3}
$$

$$
\int_{C_1} \vec{F} \cdot d\vec{r} = \frac{30 + 6 + 45 - 80}{30} = \frac{1}{30}
$$

Evaluate the integral along Path $C\_2$:

$$
\int_{C_2} \vec{F} \cdot d\vec{r} = \int_1^0 \left[ (2y^2 + y^2)(2ydy) + (3y - 4y^2)dy \right] = \int_1^0 \left( 6y^3 + 3y - 4y^2 \right) dy
$$

$$
\int_{C_2} \vec{F} \cdot d\vec{r} = \left[ \frac{3}{2}y^4 + \frac{3}{2}y^2 - \frac{4}{3}y^3 \right]_1^0 = 0 - \left( \frac{3}{2} + \frac{3}{2} - \frac{4}{3} \right) = -\left( 3 - \frac{4}{3} \right) = -\frac{5}{3} = -\frac{50}{30}
$$

Add the two line integrals together:

$$
\oint_C \vec{F} \cdot d\vec{r} = \int_{C_1} + \int_{C_2} = \frac{1}{30} - \frac{50}{30} = -\frac{49}{30}
$$

Both methods yield the same result of $-\frac{49}{30}$.

---

### Q2(b) Evaluate 

$$
\iint_S \vec{A} \cdot \hat{n} dS
$$

Where

$$
\vec{A} = z\hat{i} + x\hat{j} - 3y^2z\hat{k}
$$

 and $S$ is the surface of the cylinder $x^2 + y^2 = 16$ included in the first octant between $z=0$ and $z=5$. (06)

**Answer:**

Let the cylinder surface be defined by the function:

$$
g(x, y, z) = x^2 + y^2 - 16 = 0
$$

The gradient of $g$ points normal to this surface:

$$
\vec{\nabla}g = 2x\hat{i} + 2y\hat{j}
$$

We find the unit outward normal vector $\hat{n}$:

$$
\hat{n} = \frac{\vec{\nabla}g}{|\vec{\nabla}g|} = \frac{2x\hat{i} + 2y\hat{j}}{\sqrt{4x^2 + 4y^2}} = \frac{2x\hat{i} + 2y\hat{j}}{2\sqrt{16}} = \frac{x\hat{i} + y\hat{j}}{4}
$$

Now calculate the dot product $\vec{A} \cdot \hat{n}$:

$$
\vec{A} \cdot \hat{n} = (z\hat{i} + x\hat{j} - 3y^2z\hat{k}) \cdot \left( \frac{x\hat{i} + y\hat{j}}{4} \right) = \frac{xz + xy}{4}
$$

Next we project the cylinder surface $S$ onto the $yz$-plane. The projection region $R$ is bounded by:

$$
y \in [0, 4], \quad z \in [0, 5]
$$

For this projection, the surface area element $dS$ is related to $dy dz$ by:

$$
dS = \frac{dydz}{|\hat{n} \cdot \hat{i}|} = \frac{dydz}{|x/4|} = \frac{4}{x} dydz
$$

Now we set up the surface integral over the region $R$:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \iint_R \left( \frac{xz + xy}{4} \right) \left( \frac{4}{x} dydz \right)
$$

Simplify the integrand:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \iint_R (z + y) dydz
$$

Set up the limits of integration:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \int_{y=0}^4 \int_{z=0}^5 (y + z) dz dy
$$

Integrate with respect to $z$:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \int_0^4 \left[ yz + \frac{z^2}{2} \right]_0^5 dy = \int_0^4 \left( 5y + \frac{25}{2} \right) dy
$$

Now integrate with respect to $y$:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \left[ \frac{5y^2}{2} + \frac{25}{2}y \right]_0^4 = \frac{5(16)}{2} + \frac{25(4)}{2} = 40 + 50 = 90
$$

So the value of the surface integral is $90$.

---

### Q3(a) State and prove Green's theorem in the plane. (06)

**Answer:**

#### Statement

Let $R$ be a closed, flat region bounded by a simple, closed curve $C$ in the $xy$-plane. If $P(x,y)$ and $Q(x,y)$ are continuous functions with continuous first-order partial derivatives in $R$, then:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$

Here the curve $C$ is traversed in the counterclockwise (positive) direction.

#### Proof

We will prove the theorem for a simple region $R$ that is bounded by curves. We split the theorem into two parts:

$$
\text{Part 1: } \oint_C P dx = -\iint_R \frac{\partial P}{\partial y} dx dy
$$

$$
\text{Part 2: } \oint_C Q dy = \iint_R \frac{\partial Q}{\partial x} dx dy
$$

##### Proof of Part 1

Let the region $R$ be bounded by the curves $y = y\_1(x)$ (lower boundary) and $y = y\_2(x)$ (upper boundary) for $x$ from $a$ to $b$.

Evaluate the double integral on the right-hand side:

$$
\iint_R \frac{\partial P}{\partial y} dx dy = \int_a^b \left[ \int_{y_1(x)}^{y_2(x)} \frac{\partial P}{\partial y} dy \right] dx = \int_a^b \left[ P(x, y_2(x)) - P(x, y_1(x)) \right] dx \quad \dots \text{(1)}
$$

Now evaluate the line integral 

$$
\oint_C P dx
$$

. The closed boundary curve $C$ consists of two parts:
*   Path $C\_1$: Along the curve $y = y\_1(x)$ from $x=a$ to $x=b$.
*   Path $C\_2$: Along the curve $y = y\_2(x)$ from $x=b$ to $x=a$.

We calculate the line integral over each path:

$$
\oint_C P dx = \int_{C_1} P dx + \int_{C_2} P dx = \int_a^b P(x, y_1(x)) dx + \int_b^a P(x, y_2(x)) dx
$$

Reverse the limits on the second integral:

$$
\oint_C P dx = \int_a^b P(x, y_1(x)) dx - \int_a^b P(x, y_2(x)) dx = -\int_a^b \left[ P(x, y_2(x)) - P(x, y_1(x)) \right] dx \quad \dots \text{(2)}
$$

Comparing equations (1) and (2), we get:

$$
\oint_C P dx = -\iint_R \frac{\partial P}{\partial y} dx dy
$$

##### Proof of Part 2

Let the region $R$ be bounded by the curves $x = x\_1(y)$ (left boundary) and $x = x\_2(y)$ (right boundary) for $y$ from $c$ to $d$. By using the same steps, we get:

$$
\oint_C Q dy = \iint_R \frac{\partial Q}{\partial x} dx dy
$$

Adding the equations from Part 1 and Part 2 gives:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$

The proof is complete.

---

### Q3(b) Evaluate 

$$
\oint_C (y - \sin x)dx + \cos y dy
$$

 where $C$ is the triangle of the adjoining figure: (06)

> [!NOTE]
> **Figure Description:** The curve $C$ is a triangle in the $xy$-plane with vertices at $(0,0)$, $(\pi/2, 0)$, and $(\pi/2, 1)$. The boundary is traversed in the counterclockwise direction.

**Answer:**

We can solve this problem in two ways: using Green's Theorem or using direct line integration.

#### Method 1: Using Green's Theorem

We identify the functions:

$$
P = y - \sin x \implies \frac{\partial P}{\partial y} = 1
$$

$$
Q = \cos y \implies \frac{\partial Q}{\partial x} = 0
$$

Substitute these into Green's Theorem formula:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \iint_R (0 - 1) dA = -\iint_R dA
$$

The integral 

$$
\iint_R dA
$$

 is simply the area of the triangular region $R$:

$$
\text{Area}(R) = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times \frac{\pi}{2} \times 1 = \frac{\pi}{4}
$$

So we get:

$$
\oint_C (y - \sin x)dx + \cos y dy = -\text{Area}(R) = -\frac{\pi}{4}
$$

#### Method 2: Direct Line Integration

The boundary curve $C$ consists of three straight paths:
1.  Path $C\_1$: Along the x-axis ($y = 0$, $dy = 0$) from $(0,0)$ to $(\pi/2, 0)$.
2.  Path $C\_2$: Along the vertical line $x = \pi/2$ ($dx = 0$) from $(\pi/2, 0)$ to $(\pi/2, 1)$.
3.  Path $C\_3$: Along the line $y = \frac{2}{\pi}x$ (or $x = \frac{\pi}{2}y$, $dx = \frac{\pi}{2}dy$) from $(\pi/2, 1)$ to $(0,0)$.

Evaluate the integral along Path $C\_1$:

$$
\int_{C_1} (y - \sin x)dx + \cos y dy = \int_0^{\pi/2} (0 - \sin x) dx = \left[ \cos x \right]_0^{\pi/2} = \cos\left(\frac{\pi}{2}\right) - \cos(0) = 0 - 1 = -1
$$

Evaluate the integral along Path $C\_2$:

$$
\int_{C_2} (y - \sin x)dx + \cos y dy = \int_0^1 \cos y dy = \left[ \sin y \right]_0^1 = \sin(1)
$$

Evaluate the integral along Path $C\_3$:

Here we integrate with respect to $y$ from $y = 1$ to $y = 0$:

$$
\int_{C_3} (y - \sin x)dx + \cos y dy = \int_1^0 \left[ \left( \frac{\pi}{2}y - \sin\left(\frac{\pi}{2}y\right) \right) \frac{\pi}{2} + \cos y \right] dy
$$

$$
\int_{C_3} (y - \sin x)dx + \cos y dy = \left[ \frac{\pi}{4}y^2 + \cos\left(\frac{\pi}{2}y\right) + \sin y \right]_1^0
$$

$$
\int_{C_3} (y - \sin x)dx + \cos y dy = (0 + 1 + 0) - \left( \frac{\pi}{4} + 0 + \sin(1) \right) = 1 - \frac{\pi}{4} - \sin(1)
$$

Add the three line integrals together:

$$
\oint_C = \int_{C_1} + \int_{C_2} + \int_{C_3} = -1 + \sin(1) + 1 - \frac{\pi}{4} - \sin(1) = -\frac{\pi}{4}
$$

Both methods yield the same result of $-\frac{\pi}{4}$.

---

### Q4(a) Define vector space and subspace. (04)

**Answer:**

#### Vector Space

Let $V$ be a non-empty set of objects called vectors. Let $K$ be a field of scalars. We define two operations on this set: vector addition ($u + v$) and scalar multiplication ($k u$). The set $V$ is called a vector space over the field $K$ if it satisfies these ten rules:

1.  **Closure under Addition:** If $u, v \in V$, then $u + v \in V$.
2.  **Commutative Law:** $u + v = v + u$ for all $u, v \in V$.
3.  **Associative Law:** $(u + v) + w = u + (v + w)$ for all $u, v, w \in V$.
4.  **Additive Identity:** There is a zero vector $0 \in V$ such that $u + 0 = u$ for all $u \in V$.
5.  **Additive Inverse:** For each $u \in V$, there is a vector $-u \in V$ such that $u + (-u) = 0$.
6.  **Closure under Scalar Multiplication:** If $u \in V$ and $k \in K$, then $k u \in V$.
7.  **Distributive Law 1:** $k(u + v) = ku + kv$ for all $u, v \in V$ and $k \in K$.
8.  **Distributive Law 2:** $(a + b)u = au + bu$ for all $u \in V$ and $a, b \in K$.
9.  **Associativity of Multiplication:** $a(bu) = (ab)u$ for all $u \in V$ and $a, b \in K$.
10. **Unitary Identity:** $1u = u$ for all $u \in V$, where $1$ is the multiplicative identity in $K$.

#### Subspace

Let $W$ be a non-empty subset of a vector space $V$ over a field $K$. We call $W$ a subspace of $V$ if $W$ is itself a vector space under the same operations defined on $V$.

In practice, $W$ is a subspace if and only if it satisfies these two closure properties:
1.  **Closed under Addition:** If $u, v \in W$, then $u + v \in W$.
2.  **Closed under Scalar Multiplication:** If $u \in W$ and $k \in K$, then $k u \in W$.

---

### Q4(b) Let $V$ be a vector space over a field $k$, prove that: (08)
*   **i)** $k0 = 0$
*   **ii)** $0u = 0$
*   **iii)** If $ku = 0$, then $k = 0$ or $u = 0$
*   **iv)** $(-k)u = k(-u) = -ku$

**Answer:**

#### Proof of i): $k0 = 0$

Using properties of the zero vector, we know:

$$
0 + 0 = 0
$$

Multiply both sides by the scalar $k$:

$$
k(0 + 0) = k0
$$

Use the distributive property of vector spaces:

$$
k0 + k0 = k0
$$

Now add the additive inverse vector $-k0$ to both sides:

$$
(k0 + k0) + (-k0) = k0 + (-k0)
$$

Apply the associative law of addition:

$$
k0 + (k0 + (-k0)) = 0
$$

$$
k0 + 0 = 0 \implies k0 = 0
$$

This completes the proof.

#### Proof of ii): $0u = 0$

Using properties of scalar addition in the field $k$, we know:

$$
0 + 0 = 0
$$

Multiply both sides by the vector $u$:

$$
(0 + 0)u = 0u
$$

Use the distributive property:

$$
0u + 0u = 0u
$$

Now add the additive inverse vector $-0u$ to both sides:

$$
(0u + 0u) + (-0u) = 0u + (-0u)
$$

Apply the associative law of addition:

$$
0u + (0u + (-0u)) = 0
$$

$$
0u + 0 = 0 \implies 0u = 0
$$

This completes the proof.

#### Proof of iii): If $ku = 0$, then $k = 0$ or $u = 0$

Assume $ku = 0$. If the scalar $k = 0$, then the statement is already true.

But if $k \neq 0$, then its multiplicative inverse $k^{-1}$ exists in the field $k$. We multiply both sides of the equation by $k^{-1}$:

$$
k^{-1}(ku) = k^{-1}0
$$

Use the associative property of scalar multiplication and the fact that $k^{-1}0 = 0$ (from property i):

$$
(k^{-1}k)u = 0
$$

$$
1u = 0
$$

Since $1u = u$ (unitary property):

$$
u = 0
$$

So either $k = 0$ or $u = 0$. This completes the proof.

#### Proof of iv): $(-k)u = k(-u) = -ku$

The vector $-ku$ is the unique additive inverse of $ku$, which means $ku + (-ku) = 0$.

To show $(-k)u = -ku$, we add them together and show the result is the zero vector:

$$
ku + (-k)u = (k + (-k))u = 0u = 0 \quad \text{(using property ii)}
$$

Since the sum is zero, $(-k)u$ is indeed the additive inverse of $ku$:

$$
(-k)u = -ku
$$

To show $k(-u) = -ku$, we do the same:

$$
ku + k(-u) = k(u + (-u)) = k0 = 0 \quad \text{(using property i)}
$$

So $k(-u)$ is also the additive inverse of $ku$:

$$
k(-u) = -ku
$$

So we have shown that $(-k)u = k(-u) = -ku$.

---

## SECTION - B

### Q5(a) If 

$$
A_\alpha = \begin{pmatrix}
\cos\alpha & \sin\alpha \\
-\sin\alpha & \cos\alpha
\end{pmatrix}
$$

Then show that $A\_\alpha \cdot A\_\beta = A\_{\alpha+\beta} = A\_\beta \cdot A\_\alpha$. (03)

**Answer:**

Let us multiply the two matrices $A\_\alpha$ and $A\_\beta$:

$$
A_\alpha \cdot A_\beta = \begin{pmatrix}
\cos\alpha & \sin\alpha \\
-\sin\alpha & \cos\alpha
\end{pmatrix} \begin{pmatrix}
\cos\beta & \sin\beta \\
-\sin\beta & \cos\beta
\end{pmatrix}
$$

Multiply rows by columns:

$$
A_\alpha \cdot A_\beta = \begin{pmatrix}
\cos\alpha\cos\beta - \sin\alpha\sin\beta & \cos\alpha\sin\beta + \sin\alpha\cos\beta \\
-\sin\alpha\cos\beta - \cos\alpha\sin\beta & -\sin\alpha\sin\beta + \cos\alpha\cos\beta
\end{pmatrix}
$$

We apply standard trigonometric addition formulas:

$$
\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta
$$

$$
\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta
$$

Substitute these identities back into the product matrix:

$$
A_\alpha \cdot A_\beta = \begin{pmatrix}
\cos(\alpha+\beta) & \sin(\alpha+\beta) \\
-\sin(\alpha+\beta) & \cos(\alpha+\beta)
\end{pmatrix} = A_{\alpha+\beta}
$$

Since addition of angles is commutative ($\alpha + \beta = \beta + \alpha$), we also have:

$$
A_{\alpha+\beta} = A_{\beta+\alpha} = A_\beta \cdot A_\alpha
$$

So we have shown that $A\_\alpha \cdot A\_\beta = A\_{\alpha+\beta} = A\_\beta \cdot A\_\alpha$.

---

### Q5(b) Find the adjoint and inverse of 

$$
\begin{pmatrix}
0 & 1 & 2 \\
1 & 2 & 3 \\
3 & 1 & 1
\end{pmatrix}
$$

. (05)

**Answer:**

Let the matrix be:

$$
A = \begin{pmatrix}
0 & 1 & 2 \\
1 & 2 & 3 \\
3 & 1 & 1
\end{pmatrix}
$$

First we find the determinant of $A$:

$$
|A| = 0(2-3) - 1(1-9) + 2(1-6) = 0 + 8 - 10 = -2
$$

Since the determinant is not zero, the inverse exists.

Next we find the cofactor elements $C\_{ij}$ of the matrix:

$$
C_{11} = +(2-3) = -1, \quad C_{12} = -(1-9) = 8, \quad C_{13} = +(1-6) = -5
$$

$$
C_{21} = -(1-2) = 1, \quad C_{22} = +(0-6) = -6, \quad C_{23} = -(0-3) = 3
$$

$$
C_{31} = +(3-4) = -1, \quad C_{32} = -(0-2) = 2, \quad C_{33} = +(0-1) = -1
$$

This gives the cofactor matrix $C$:

$$
C = \begin{pmatrix}
-1 & 8 & -5 \\
1 & -6 & 3 \\
-1 & 2 & -1
\end{pmatrix}
$$

The adjoint of $A$ is the transpose of the cofactor matrix:

$$
\text{adj}(A) = C^T = \begin{pmatrix}
-1 & 1 & -1 \\
8 & -6 & 2 \\
-5 & 3 & -1
\end{pmatrix}
$$

Now we find the inverse matrix $A^{-1}$:

$$
A^{-1} = \frac{1}{|A|} \text{adj}(A) = -\frac{1}{2} \begin{pmatrix}
-1 & 1 & -1 \\
8 & -6 & 2 \\
-5 & 3 & -1
\end{pmatrix} = \begin{pmatrix}
1/2 & -1/2 & 1/2 \\
-4 & 3 & -1 \\
5/2 & -3/2 & 1/2
\end{pmatrix}
$$

---

### Q5(c) Determine the characteristic roots of 

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & -4 & 2 \\
0 & 0 & 7
\end{pmatrix}
$$

. (04)

**Answer:**

Let the matrix be:

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
0 & -4 & 2 \\
0 & 0 & 7
\end{pmatrix}
$$

The characteristic equation is defined by $|A - \lambda I| = 0$:

$$
\begin{vmatrix}
1-\lambda & 2 & 3 \\
0 & -4-\lambda & 2 \\
0 & 0 & 7-\lambda
\end{vmatrix} = 0
$$

Since this is an upper triangular matrix, its determinant is simply the product of its diagonal elements:

$$
(1-\lambda)(-4-\lambda)(7-\lambda) = 0
$$

This equation has three roots:

$$
\lambda = 1, \quad \lambda = -4, \quad \lambda = 7
$$

So the characteristic roots (or eigenvalues) are $1$, $-4$, and $7$.

---

### Q6(a) What is the rank of a matrix? Find it for 

$$
\begin{bmatrix}
0 & 0 & 1 & -3 & -2 \\
0 & 1 & 2 & 6 & 0 \\
0 & 2 & 3 & 9 & 2 \\
0 & 1 & 1 & 3 & 2
\end{bmatrix}
$$

. (06)

**Answer:**

#### Rank of a Matrix

The rank of a matrix is the maximum number of linearly independent row vectors (or column vectors) in it. It equals the number of non-zero rows when the matrix is reduced to its row-echelon form.

#### Finding the Rank

Let the matrix be:

$$
A = \begin{bmatrix}
0 & 0 & 1 & -3 & -2 \\
0 & 1 & 2 & 6 & 0 \\
0 & 2 & 3 & 9 & 2 \\
0 & 1 & 1 & 3 & 2
\end{bmatrix}
$$

We swap the first and second rows ($R\_1 \leftrightarrow R\_2$) to place a non-zero leading entry in the first row:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & -3 & -2 \\
0 & 2 & 3 & 9 & 2 \\
0 & 1 & 1 & 3 & 2
\end{bmatrix}
$$

Now we perform row operations to make the entries below the leading entry of $R\_1$ zero:
*   $R\_3 \to R\_3 - 2R\_1$
*   $R\_4 \to R\_4 - R\_1$

This gives:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & -3 & -2 \\
0 & 0 & -1 & -3 & 2 \\
0 & 0 & -1 & -3 & 2
\end{bmatrix}
$$

Next we make the entries below the leading entry of $R\_2$ zero:
*   $R\_3 \to R\_3 + R\_2$
*   $R\_4 \to R\_4 + R\_2$

This gives:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & -3 & -2 \\
0 & 0 & 0 & -6 & 0 \\
0 & 0 & 0 & -6 & 0
\end{bmatrix}
$$

Now eliminate the last entry in row 4 using row 3 ($R\_4 \to R\_4 - R\_3$):

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & -3 & -2 \\
0 & 0 & 0 & -6 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

Divide row 3 by $-6$:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & -3 & -2 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

This matrix is now in row-echelon form. The number of non-zero rows is $3$.

So the rank of the matrix is $3$.

---

### Q6(b) Solve by elementary transformation: (06)

$$
2x_1 + 2x_2 + x_3 = 2
$$

$$
3x_1 + x_2 - 2x_3 = 1
$$

$$
4x_1 - 3x_2 - x_3 = 3
$$

**Answer:**

We write the augmented matrix of the system:

$$
\begin{bmatrix}
2 & 2 & 1 & | & 2 \\
3 & 1 & -2 & | & 1 \\
4 & -3 & -1 & | & 3
\end{bmatrix}
$$

We perform row operations to reduce it:
*   $R\_2 \to 2R\_2 - 3R\_1$
*   $R\_3 \to R\_3 - 2R\_1$

This gives:

$$
\begin{bmatrix}
2 & 2 & 1 & | & 2 \\
0 & -4 & -7 & | & -4 \\
0 & -7 & -3 & | & -1
\end{bmatrix}
$$

Multiply the second and third rows by $-1$:

$$
\begin{bmatrix}
2 & 2 & 1 & | & 2 \\
0 & 4 & 7 & | & 4 \\
0 & 7 & 3 & | & 1
\end{bmatrix}
$$

Now perform row operation $R\_3 \to 4R\_3 - 7R\_2$:

$$
\begin{bmatrix}
2 & 2 & 1 & | & 2 \\
0 & 4 & 7 & | & 4 \\
0 & 0 & -37 & | & -24
\end{bmatrix}
$$

Now we solve the variables by back substitution. From the third row:

$$
-37x_3 = -24 \implies x_3 = \frac{24}{37}
$$

From the second row:

$$
4x_2 + 7x_3 = 4 \implies 4x_2 + 7\left( \frac{24}{37} \right) = 4
$$

$$
4x_2 = 4 - \frac{168}{37} = \frac{148 - 168}{37} = -\frac{20}{37} \implies x_2 = -\frac{5}{37}
$$

From the first row:

$$
2x_1 + 2x_2 + x_3 = 2 \implies 2x_1 + 2\left( -\frac{5}{37} \right) + \frac{24}{37} = 2
$$

$$
2x_1 - \frac{10}{37} + \frac{24}{37} = 2 \implies 2x_1 + \frac{14}{37} = 2
$$

$$
2x_1 = 2 - \frac{14}{37} = \frac{74 - 14}{37} = \frac{60}{37} \implies x_1 = \frac{30}{37}
$$

So the unique solution is:

$$
x_1 = \frac{30}{37}, \quad x_2 = -\frac{5}{37}, \quad x_3 = \frac{24}{37}
$$

---

### Q7 What are the eigen-values and eigen-vectors? Find them for the matrix 

$$
\begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix}
$$

. (12)

**Answer:**

#### Definitions

Let $A$ be a square matrix of order $n$. If there exists a non-zero vector $X$ and a scalar $\lambda$ such that:

$$
AX = \lambda X
$$

then $\lambda$ is called an **eigenvalue** of $A$, and $X$ is called the corresponding **eigenvector**.

#### Finding eigenvalues

Let the matrix be:

$$
A = \begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix}
$$

We solve the characteristic equation $|A - \lambda I| = 0$:

$$
\begin{vmatrix}
2-\lambda & 2 & 1 \\
1 & 3-\lambda & 1 \\
1 & 2 & 2-\lambda
\end{vmatrix} = 0
$$

Expanding the determinant:

$$
(2-\lambda)\left[ (3-\lambda)(2-\lambda) - 2 \right] - 2\left[ (2-\lambda) - 1 \right] + 1\left[ 2 - (3-\lambda) \right] = 0
$$

$$
(2-\lambda)\left[ \lambda^2 - 5\lambda + 4 \right] - 2[1-\lambda] + [\lambda - 1] = 0
$$

$$
-\lambda^3 + 7\lambda^2 - 11\lambda + 5 = 0 \implies \lambda^3 - 7\lambda^2 + 11\lambda - 5 = 0
$$

For $\lambda = 1$, the equation holds ($1 - 7 + 11 - 5 = 0$). Dividing by $\lambda - 1$ gives:

$$
(\lambda-1)(\lambda^2 - 6\lambda + 5) = 0 \implies (\lambda-1)(\lambda-1)(\lambda-5) = 0
$$

So the eigenvalues are:

$$
\lambda = 5, \quad \lambda = 1, \quad \lambda = 1
$$

#### Finding eigenvectors

We solve the system $(A - \lambda I)X = 0$ for each eigenvalue:

##### Case 1: For $\lambda = 5$

The system is:

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

We apply row operations:
*   Swap $R\_1 \leftrightarrow R\_2$:

$$
\begin{bmatrix}
1 & -2 & 1 \\
-3 & 2 & 1 \\
1 & 2 & -3
\end{bmatrix}
$$

*   $R\_2 \to R\_2 + 3R\_1$
*   $R\_3 \to R\_3 - R\_1$

This gives:

$$
\begin{bmatrix}
1 & -2 & 1 \\
0 & -4 & 4 \\
0 & 4 & -4
\end{bmatrix}
$$

*   $R\_3 \to R\_3 + R\_2$
*   Divide row 2 by $-4$:

$$
\begin{bmatrix}
1 & -2 & 1 \\
0 & 1 & -1 \\
0 & 0 & 0
\end{bmatrix}
$$

This gives the relationships:

$$
y - z = 0 \implies y = z
$$

$$
x - 2y + z = 0 \implies x - 2z + z = 0 \implies x = z
$$

Let $z = 1$. This gives the eigenvector:

$$
X_1 = \begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix}
$$

##### Case 2: For $\lambda = 1$

The system is:

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

This reduces to a single equation:

$$
x + 2y + z = 0 \implies x = -2y - z
$$

Here we have two free variables. Let $y = s$ and $z = t$. The eigenvectors are:

$$
X = \begin{bmatrix}
-2s - t \\
s \\
t
\end{bmatrix} = s \begin{bmatrix}
-2 \\
1 \\
0
\end{bmatrix} + t \begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix}
$$

So the two linearly independent eigenvectors for $\lambda = 1$ are:

$$
X_2 = \begin{bmatrix}
-2 \\
1 \\
0
\end{bmatrix}, \quad X_3 = \begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix}
$$

---

### Q8 Diagonalize the matrix 

$$
A = \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$

. Hence evaluate $e^A$, and then solve $\frac{dx\_1}{dt} = x\_2$, $\frac{dx\_2}{dt} = x\_1$. (12)

**Answer:**

#### 1. Diagonalization check

Let 

$$
A = \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$

. Its eigenvalues are the diagonal entries:

$$
\lambda_1 = 1, \quad \lambda_2 = 1
$$

To check if $A$ is diagonalizable, we find the eigenvectors by solving $(A - I)X = 0$:

$$
\begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix} \begin{bmatrix}
x \\
y
\end{bmatrix} = \begin{bmatrix}
0 \\
0
\end{bmatrix} \implies y = 0
$$

The eigenvectors are of the form 

$$
\begin{bmatrix}
x \\
0
\end{bmatrix}
$$

. So there is only one linearly independent eigenvector:

$$
X_1 = \begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

Since the geometric multiplicity (1) is less than the algebraic multiplicity (2), **the matrix $A$ is not diagonalizable**.

#### 2. Evaluation of $e^A$

Even though $A$ is not diagonalizable, we can evaluate $e^A$ using the power series definition. We decompose $A$ into:

$$
A = I + B, \quad \text{where } B = \begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix}
$$

Since the identity matrix $I$ commutes with any matrix ($IB = BI$), we can write:

$$
e^A = e^{I + B} = e^I \cdot e^B = e \cdot e^B
$$

Note that 

$$
B^2 = \begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix} \begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix} = \begin{bmatrix}
0 & 0 \\
0 & 0
\end{bmatrix}
$$

. So $B^n = 0$ for all $n \geq 2$.

Using the series definition for $e^B$:

$$
e^B = I + B + \frac{B^2}{2!} + \dots = I + B = \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$

Therefore:

$$
e^A = e \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
e & e \\
0 & e
\end{bmatrix}
$$

#### 3. Solving the differential equations

We solve the systems in two different interpretations:

##### Interpretation 1: Solving the system as printed

The printed system is:

$$
\frac{dx_1}{dt} = x_2, \quad \frac{dx_2}{dt} = x_1
$$

We differentiate the first equation:

$$
\frac{d^2x_1}{dt^2} = \frac{dx_2}{dt} = x_1 \implies \frac{d^2x_1}{dt^2} - x_1 = 0
$$

The characteristic equation is $r^2 - 1 = 0$, which gives $r = \pm 1$. So the general solution for $x\_1(t)$ is:

$$
x_1(t) = C_1 e^t + C_2 e^{-t}
$$

Then we find $x\_2(t)$ using the first relation:

$$
x_2(t) = \frac{dx_1}{dt} = C_1 e^t - C_2 e^{-t}
$$

##### Interpretation 2: Solving the intended system $\frac{dX}{dt} = AX$

The intended system associated with matrix $A$ is:

$$
\frac{dx_1}{dt} = x_1 + x_2, \quad \frac{dx_2}{dt} = x_2
$$

The solution to a system of the form $\frac{dX}{dt} = AX$ is:

$$
X(t) = e^{At} X(0)
$$

We calculate the matrix exponential $e^{At}$ by decomposing $At = It + Bt$:

$$
e^{At} = e^t e^{Bt} = e^t (I + Bt) = e^t \begin{bmatrix}
1 & t \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
e^t & t e^t \\
0 & e^t
\end{bmatrix}
$$

So the solution is:

$$
\begin{bmatrix}
x_1(t) \\
x_2(t)
\end{bmatrix} = \begin{bmatrix}
e^t & t e^t \\
0 & e^t
\end{bmatrix} \begin{bmatrix}
x_1(0) \\
x_2(0)
\end{bmatrix}
$$

This gives the general solution:

$$
x_1(t) = (C_1 + C_2 t) e^t
$$

$$
x_2(t) = C_2 e^t
$$

where $C\_1 = x\_1(0)$ and $C\_2 = x\_2(0)$.

---

*(start)* | [🏠 Index](00-index.md) | [2018 ➡](2018_answer.md)
