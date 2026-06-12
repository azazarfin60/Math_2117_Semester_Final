[⬅ 2020](2020_answer.md) | [🏠 Index](00-index.md) | [2023 ➡](2023_answer.md)

---

# B.Sc. Engineering 2nd Year Odd Examination, 2021
**Course No: Math 2117**
**Course Title: Vector Analysis & Linear Algebra**
**Time: 3 Hours**
**Full Marks: 72**

---

## SECTION - A

### Q1(a) What are the vector and scalar quantity? Give some examples. If 

$$
\vec{A} = 3\hat{i} - \hat{j} + 4\hat{k}
$$

$$
\vec{B} = -2\hat{i} + 4\hat{j} - 3\hat{k}
$$

 and 

$$
\vec{C} = \hat{i} + 2\hat{j} - \hat{k}
$$

Find the magnitude of $2\vec{A} - 3\vec{B} + 2\vec{C}$. (04)

**Answer:**

#### 1. Definitions and Examples

*   **Scalar Quantity:** A physical quantity that has only magnitude but no direction. Examples: Mass, Temperature, Time.
*   **Vector Quantity:** A physical quantity that has both magnitude and direction, and obeys vector addition rules. Examples: Velocity, Force, Acceleration.

#### 2. Find the Magnitude

We calculate the vector expression:

$$
\vec{V} = 2\vec{A} - 3\vec{B} + 2\vec{C}
$$

Substitute the given vectors:

$$
2\vec{A} = 6\hat{i} - 2\hat{j} + 8\hat{k}
$$

$$
-3\vec{B} = 6\hat{i} - 12\hat{j} + 9\hat{k}
$$

$$
2\vec{C} = 2\hat{i} + 4\hat{j} - 2\hat{k}
$$

Sum the components together:

$$
\vec{V} = (6 + 6 + 2)\hat{i} + (-2 - 12 + 4)\hat{j} + (8 + 9 - 2)\hat{k} = 14\hat{i} - 10\hat{j} + 15\hat{k}
$$

Find the magnitude:

$$
|\vec{V}| = \sqrt{14^2 + (-10)^2 + 15^2} = \sqrt{196 + 100 + 225} = \sqrt{521}
$$

So the magnitude is $\sqrt{521}$.

---

### Q1(b) What is meant by dot and cross product in vector analysis? Determine a unit vector perpendicular to the plane of 

$$
\vec{A} = 2\hat{i} - 6\hat{j} - 3\hat{k}
$$

 and 

$$
\vec{B} = 4\hat{i} + 3\hat{j} - \hat{k}
$$

(04)

**Answer:**

#### 1. Definitions

*   **Dot Product:** The scalar product of two vectors $\vec{A}$ and $\vec{B}$ is defined as $\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$, where $\theta$ is the angle between them.
*   **Cross Product:** The vector product of two vectors $\vec{A}$ and $\vec{B}$ is defined as 

$$
\vec{A} \times \vec{B} = |\vec{A}||\vec{B}|\sin\theta \hat{n}
$$

Where $\hat{n}$ is a unit vector perpendicular to the plane of the two vectors.

#### 2. Find the Perpendicular Unit Vector

We calculate the cross product of $\vec{A}$ and $\vec{B}$ to get a perpendicular vector:

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

### Q1(c) Find the area of a triangle with vertices at $(3, -1, 2)$, $(1, -1, -3)$ and $(4, -3, 1)$. (04)

**Answer:**

Let the vertices of the triangle be $P(3, -1, 2)$, $Q(1, -1, -3)$, and $R(4, -3, 1)$.

We construct two side vectors starting from point $P$:

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

### Q2(a) Find the directional derivative of the scalar function $f(x, y, z) = x^2 + xy + z^2$ at the point $A(1, -1, -1)$ in the direction of the line $AB$ where $B$ has co-ordinates $(3, 2, 1)$. (03)

**Answer:**

We construct the direction vector $\vec{AB}$:

$$
\vec{AB} = (3 - 1)\hat{i} + (2 - (-1))\hat{j} + (1 - (-1))\hat{k} = 2\hat{i} + 3\hat{j} + 2\hat{k}
$$

Find the unit vector $\hat{u}$ in this direction:

$$
\hat{u} = \frac{2\hat{i} + 3\hat{j} + 2\hat{k}}{\sqrt{2^2 + 3^2 + 2^2}} = \frac{2\hat{i} + 3\hat{j} + 2\hat{k}}{\sqrt{17}}
$$

Calculate the gradient of the function $f = x^2 + xy + z^2$:

$$
\vec{\nabla}f = (2x + y)\hat{i} + x\hat{j} + 2z\hat{k}
$$

Evaluate the gradient at the point $A(1, -1, -1)$:

$$
\vec{\nabla}f(A) = (2(1) - 1)\hat{i} + (1)\hat{j} + 2(-1)\hat{k} = \hat{i} + \hat{j} - 2\hat{k}
$$

The directional derivative is the dot product of the gradient and the unit vector:

$$
D_{\hat{u}}f = \vec{\nabla}f \cdot \hat{u} = (\hat{i} + \hat{j} - 2\hat{k}) \cdot \left( \frac{2\hat{i} + 3\hat{j} + 2\hat{k}}{\sqrt{17}} \right) = \frac{2 + 3 - 4}{\sqrt{17}} = \frac{1}{\sqrt{17}}
$$

So the directional derivative is $\frac{1}{\sqrt{17}}$.

---

### Q2(b) Show that 

$$
\vec{F} = (y^2 + 2xz^2)\hat{i} + (2xy - z)\hat{j} + (2x^2z - y + 2z)\hat{k}
$$

 is irrotational vector and hence find corresponding scalar potential. (05)

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

### Q2(c) Show that $\bar{\nabla} \times (\bar{\nabla} \times \bar{V}) = \nabla(\nabla \cdot \bar{V}) - \nabla^2\bar{V}$. (04)

**Answer:**

We write the vector field in Cartesian components:

$$
\bar{V} = V_x\hat{i} + V_y\hat{j} + V_z\hat{k}
$$

Let us use the vector identity:

$$
\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}
$$

We apply this structure by letting 

$$
\vec{a} = \bar{\nabla}, \quad \vec{b} = \bar{\nabla}, \quad \vec{c} = \bar{V}
$$

Since $\bar{\nabla}$ acts as an operator, we write the components of the curl of the curl:

$$
\bar{\nabla} \times \bar{V} = \left(\frac{\partial V_z}{\partial y} - \frac{\partial V_y}{\partial z}\right)\hat{i} + \left(\frac{\partial V_x}{\partial z} - \frac{\partial V_z}{\partial x}\right)\hat{j} + \left(\frac{\partial V_y}{\partial x} - \frac{\partial V_x}{\partial y}\right)\hat{k}
$$

Now calculate the $\hat{i}$-component of $\bar{\nabla} \times (\bar{\nabla} \times \bar{V})$:

$$
[\bar{\nabla} \times (\bar{\nabla} \times \bar{V})]_x = \frac{\partial}{\partial y}\left(\frac{\partial V_y}{\partial x} - \frac{\partial V_x}{\partial y}\right) - \frac{\partial}{\partial z}\left(\frac{\partial V_x}{\partial z} - \frac{\partial V_z}{\partial x}\right)
$$

$$
[\bar{\nabla} \times (\bar{\nabla} \times \bar{V})]_x = \frac{\partial^2 V_y}{\partial y \partial x} - \frac{\partial^2 V_x}{\partial y^2} - \frac{\partial^2 V_x}{\partial z^2} + \frac{\partial^2 V_z}{\partial z \partial x}
$$

Add and subtract the term $\frac{\partial^2 V\_x}{\partial x^2}$:

$$
[\bar{\nabla} \times (\bar{\nabla} \times \bar{V})]_x = \left(\frac{\partial^2 V_x}{\partial x^2} + \frac{\partial^2 V_y}{\partial y \partial x} + \frac{\partial^2 V_z}{\partial z \partial x}\right) - \left(\frac{\partial^2 V_x}{\partial x^2} + \frac{\partial^2 V_x}{\partial y^2} + \frac{\partial^2 V_x}{\partial z^2}\right)
$$

$$
[\bar{\nabla} \times (\bar{\nabla} \times \bar{V})]_x = \frac{\partial}{\partial x}\left(\frac{\partial V_x}{\partial x} + \frac{\partial V_y}{\partial y} + \frac{\partial V_z}{\partial z}\right) - \left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)V_x
$$

$$
[\bar{\nabla} \times (\bar{\nabla} \times \bar{V})]_x = \left[ \nabla(\nabla \cdot \bar{V}) - \nabla^2\bar{V} \right]_x
$$

Using the same steps for the $y$ and $z$ components, the relationship holds for all components:

$$
\bar{\nabla} \times (\bar{\nabla} \times \bar{V}) = \nabla(\nabla \cdot \bar{V}) - \nabla^2\bar{V}
$$

This completes the proof.

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
\cos\theta = \frac{16}{6\sqrt{21}} = \frac{8}{3\sqrt{21}} \implies \theta = \cos^{-1}\left( \frac{8}{3\sqrt{21}} \right)
$$

So the angle between the surfaces is $\cos^{-1}\left( \frac{8}{3\sqrt{21}} \right)$.

---

### Q3(b) If 

$$
\vec{A} = (3x^2 + 6y)\hat{i} - 14yz\hat{j} + 20xz^2\hat{k}
$$

Evaluate

$$
\int_C \vec{A} \cdot d\vec{r}
$$

 along the straight lines from $(0,0,0)$ to $(1, 0, 0)$ then to $(1, 1, 0)$, and then to $(1, 1, 1)$ along the paths $C$. (04)

**Answer:**

We write the line integral as:

$$
\int_C \vec{A} \cdot d\vec{r} = \int_C \left[ (3x^2 + 6y)dx - 14yz dy + 20xz^2 dz \right]
$$

We divide the path $C$ into three line segments:

#### 1. Segment $C\_1$: From $(0,0,0)$ to $(1,0,0)$

On this segment, $y=0$ and $z=0$, which means $dy=0$ and $dz=0$. The variable $x$ goes from $0$ to $1$:

$$
\int_{C_1} \vec{A} \cdot d\vec{r} = \int_{x=0}^1 (3x^2 + 0) dx = [x^3]_0^1 = 1
$$

#### 2. Segment $C\_2$: From $(1,0,0)$ to $(1,1,0)$

On this segment, $x=1$ and $z=0$, which means $dx=0$ and $dz=0$. The variable $y$ goes from $0$ to $1$:

$$
\int_{C_2} \vec{A} \cdot d\vec{r} = \int_{y=0}^1 -14y(0) dy = 0
$$

#### 3. Segment $C\_3$: From $(1,1,0)$ to $(1,1,1)$

On this segment, $x=1$ and $y=1$, which means $dx=0$ and $dy=0$. The variable $z$ goes from $0$ to $1$:

$$
\int_{C_3} \vec{A} \cdot d\vec{r} = \int_{z=0}^1 20(1)z^2 dz = \left[ \frac{20}{3}z^3 \right]_0^1 = \frac{20}{3}
$$

#### Total Line Integral

$$
\int_C \vec{A} \cdot d\vec{r} = \int_{C_1} + \int_{C_2} + \int_{C_3} = 1 + 0 + \frac{20}{3} = \frac{23}{3}
$$

So the value of the line integral is $\frac{23}{3}$.

---

### Q3(c) Let 

$$
\vec{F} = 2xz\hat{i} - x\hat{j} + y^2\hat{k}
$$

Evaluate

$$
\iiint_V \vec{F} dV
$$

Where $V$ is the region bounded by the surfaces $x=0, y=0, y=6, z=x^2, z=4$. (04)

**Answer:**

The boundaries of the region $V$ are $x$ from $0$ to $2$, $y$ from $0$ to $6$, and $z$ from $x^2$ to $4$.

We set up the triple integral:

$$
\iiint_V \vec{F} dV = \int_{y=0}^6 \int_{x=0}^2 \int_{z=x^2}^4 (2xz\hat{i} - x\hat{j} + y^2\hat{k}) dz dx dy
$$

We integrate each component separately:

#### 1. $\hat{i}$-component

$$
\int_0^6 \int_0^2 \int_{x^2}^4 2xz dz dx dy = \left( \int_0^6 dy \right) \int_0^2 \left[ xz^2 \right]_{x^2}^4 dx = 6 \int_0^2 (16x - x^5) dx
$$

$$
= 6 \left[ 8x^2 - \frac{x^6}{6} \right]_0^2 = 6 \left( 32 - \frac{64}{6} \right) = 192 - 64 = 128
$$

#### 2. $\hat{j}$-component

$$
\int_0^6 \int_0^2 \int_{x^2}^4 -x dz dx dy = 6 \int_0^2 -x(4 - x^2) dx = 6 \int_0^2 (x^3 - 4x) dx
$$

$$
= 6 \left[ \frac{x^4}{4} - 2x^2 \right]_0^2 = 6(4 - 8) = -24
$$

#### 3. $\hat{k}$-component

$$
\int_0^6 \int_0^2 \int_{x^2}^4 y^2 dz dx dy = \left( \int_0^6 y^2 dy \right) \left( \int_0^2 (4 - x^2) dx \right)
$$

$$
= \left[ \frac{y^3}{3} \right]_0^6 \times \left[ 4x - \frac{x^3}{3} \right]_0^2 = 72 \times \left( 8 - \frac{8}{3} \right) = 72 \times \frac{16}{3} = 384
$$

#### Combine Components

$$
\iiint_V \vec{F} dV = 128\hat{i} - 24\hat{j} + 384\hat{k}
$$

---

### Q4(a) State and prove Green's theorem in the plane. (06)

**Answer:**

#### Statement

Let $R$ be a closed, flat region bounded by a simple, closed curve $C$ in the $xy$-plane. If $P(x,y)$ and $Q(x,y)$ are continuous functions with continuous first-order partial derivatives in $R$, then:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$

Here the curve $C$ is traversed in the counterclockwise (positive) direction.

#### Proof

We prove the theorem for a simple region $R$ bounded by curves. We split the theorem into two parts:

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

The closed boundary curve $C$ consists of two parts:
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

### Q4(b) Verify the divergence theorem for 

$$
\vec{A} = 4x\hat{i} - 2y^2\hat{j} + z^2\hat{k}
$$

Taken over the region bounded by $x^2 + y^2 = 4$, $z=0$ and $z=3$. (06)

**Answer:**

The Divergence Theorem states:

$$
\iiint_V \vec{\nabla} \cdot \vec{A} dV = \iint_S \vec{A} \cdot \hat{n} dS
$$

Calculate the divergence of $\vec{A}$:

$$
\vec{\nabla} \cdot \vec{A} = \frac{\partial}{\partial x}(4x) + \frac{\partial}{\partial y}(-2y^2) + \frac{\partial}{\partial z}(z^2) = 4 - 4y + 2z
$$

#### 1. Evaluate Volume Integral

We use cylindrical coordinates: 

$$
x = r\cos\theta, \quad y = r\sin\theta, \quad z = z
$$

 with Jacobian $r$. The limits are $r \in [0, 2]$, $\theta \in [0, 2\pi]$, and $z \in [0, 3]$:

$$
\iiint_V (4 - 4y + 2z) dV = \int_0^2 \int_0^{2\pi} \int_0^3 (4 - 4r\sin\theta + 2z) r dz d\theta dr
$$

Integrate with respect to $z$:

$$
\int_0^3 (4 - 4r\sin\theta + 2z) dz = \left[ 4z - 4rz\sin\theta + z^2 \right]_0^3 = 12 - 12r\sin\theta + 9 = 21 - 12r\sin\theta
$$

Multiply by $r$ and integrate with respect to $\theta$:

$$
\int_0^{2\pi} (21r - 12r^2\sin\theta) d\theta = \left[ 21r\theta + 12r^2\cos\theta \right]_0^{2\pi} = 42\pi r
$$

Now integrate with respect to $r$:

$$
\int_0^2 42\pi r dr = \left[ 21\pi r^2 \right]_0^2 = 84\pi
$$

#### 2. Evaluate Surface Integral

The surface $S$ consists of three parts:
*   **Bottom cap $S\_1$:** $z=0$, 

$$
\hat{n} = -\hat{k}
$$

Since $z=0$,

$$
\vec{A} \cdot \hat{n} = -z^2 = 0
$$

*   **Top cap $S\_2$:** $z=3$, 

$$
\hat{n} = \hat{k}
$$

Here

$$
\vec{A} \cdot \hat{n} = z^2 = 9
$$

:

$$
\iint_{S_2} \vec{A} \cdot \hat{n} dS = 9 \times \text{Area}(S_2) = 9 \times \pi(2^2) = 36\pi
$$

*   **Curved side $S\_3$:** $x^2 + y^2 = 4$, 

$$
\hat{n} = \frac{x\hat{i} + y\hat{j}}{2}
$$

Calculate the dot product:

$$
\vec{A} \cdot \hat{n} = (4x\hat{i} - 2y^2\hat{j} + z^2\hat{k}) \cdot \left( \frac{x\hat{i} + y\hat{j}}{2} \right) = 2x^2 - y^3
$$

On the cylinder boundary $r=2$, we have $x = 2\cos\theta$ and $y = 2\sin\theta$. The area element is $dS = 2 d\theta dz$:

$$
\iint_{S_3} (2x^2 - y^3) dS = \int_0^3 \int_0^{2\pi} \left[ 8\cos^2\theta - 8\sin^3\theta \right] 2 d\theta dz = 6 \int_0^{2\pi} (8\cos^2\theta - 8\sin^3\theta) d\theta
$$

Since 

$$
\int_0^{2\pi} \cos^2\theta d\theta = \pi
$$

 and 

$$
\int_0^{2\pi} \sin^3\theta d\theta = 0
$$

:

$$
\iint_{S_3} \vec{A} \cdot \hat{n} dS = 6 [ 8\pi - 0 ] = 48\pi
$$

#### Total Surface Integral

$$
\iint_S \vec{A} \cdot \hat{n} dS = 0 + 36\pi + 48\pi = 84\pi
$$

Both sides equal $84\pi$. The divergence theorem is verified.

---

## SECTION - B

### Q5(a) What are the symmetric and skew-symmetric matrices? Show that every square matrix can be uniquely expressed as the sum of a symmetric and a skew-symmetric matrix. (06)

**Answer:**

#### 1. Definitions

*   **Symmetric Matrix:** A square matrix $A$ is symmetric if it equals its transpose: $A^T = A$.
*   **Skew-Symmetric Matrix:** A square matrix $A$ is skew-symmetric if its transpose equals its negative: $A^T = -A$.

#### 2. Decomposition and Uniqueness Proof

Let $A$ be a square matrix. We can write $A$ as:

$$
A = \frac{1}{2}(A + A^T) + \frac{1}{2}(A - A^T)
$$

Let $P = \frac{1}{2}(A + A^T)$ and $Q = \frac{1}{2}(A - A^T)$.

##### Show $P$ is symmetric

$$
P^T = \left[ \frac{1}{2}(A + A^T) \right]^T = \frac{1}{2}(A^T + A) = P
$$

##### Show $Q$ is skew-symmetric

$$
Q^T = \left[ \frac{1}{2}(A - A^T) \right]^T = \frac{1}{2}(A^T - A) = -Q
$$

##### Prove Uniqueness

Suppose there is another decomposition $A = P' + Q'$, where $P'$ is symmetric and $Q'$ is skew-symmetric.

Taking the transpose gives:

$$
A^T = (P' + Q')^T = P'^T + Q'^T = P' - Q'
$$

We solve the system:
1.  $P' + Q' = A$
2.  $P' - Q' = A^T$

Adding the two equations yields:

$$
2P' = A + A^T \implies P' = \frac{1}{2}(A + A^T) = P
$$

Subtracting the second equation from the first yields:

$$
2Q' = A - A^T \implies Q' = \frac{1}{2}(A - A^T) = Q
$$

So the decomposition is unique.

---

### Q5(b) Find the rank of the following matrix and hence reduce it to the canonical form: (06)

$$
A = \begin{pmatrix}
2 & 3 & -1 & -1 \\
1 & -1 & -2 & -4 \\
3 & 1 & 3 & -2 \\
6 & 3 & 0 & -7
\end{pmatrix}
$$

**Answer:**

We write the matrix:

$$
A = \begin{pmatrix}
2 & 3 & -1 & -1 \\
1 & -1 & -2 & -4 \\
3 & 1 & 3 & -2 \\
6 & 3 & 0 & -7
\end{pmatrix}
$$

Swap row 1 and row 2 ($R\_1 \leftrightarrow R\_2$):

$$
\begin{pmatrix}
1 & -1 & -2 & -4 \\
2 & 3 & -1 & -1 \\
3 & 1 & 3 & -2 \\
6 & 3 & 0 & -7
\end{pmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 2R\_1$
*   $R\_3 \to R\_3 - 3R\_1$
*   $R\_4 \to R\_4 - 6R\_1$

This gives:

$$
\begin{pmatrix}
1 & -1 & -2 & -4 \\
0 & 5 & 3 & 7 \\
0 & 4 & 9 & 10 \\
0 & 9 & 12 & 17
\end{pmatrix}
$$

Apply operations:
*   $R\_3 \to 5R\_3 - 4R\_2$
*   $R\_4 \to 5R\_4 - 9R\_2$

This gives:

$$
\begin{pmatrix}
1 & -1 & -2 & -4 \\
0 & 5 & 3 & 7 \\
0 & 0 & 33 & 22 \\
0 & 0 & 33 & 22
\end{pmatrix}
$$

Simplify row 3 and row 4 ($R\_3 \to \frac{1}{11}R\_3$, $R\_4 \to \frac{1}{11}R\_4$):

$$
\begin{pmatrix}
1 & -1 & -2 & -4 \\
0 & 5 & 3 & 7 \\
0 & 0 & 3 & 2 \\
0 & 0 & 3 & 2
\end{pmatrix}
$$

Subtract row 3 from row 4 ($R\_4 \to R\_4 - R\_3$):

$$
\begin{pmatrix}
1 & -1 & -2 & -4 \\
0 & 5 & 3 & 7 \\
0 & 0 & 3 & 2 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

Since there are 3 non-zero rows in the echelon form, the rank is:

$$
\text{Rank} = 3
$$

#### Reduce to Canonical Form

We apply column operations to clear the first row:
*   $C\_2 \to C\_2 + C\_1$
*   $C\_3 \to C\_3 + 2C\_1$
*   $C\_4 \to C\_4 + 4C\_1$

This gives:

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 5 & 3 & 7 \\
0 & 0 & 3 & 2 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

Scale row 2 ($R\_2 \to \frac{1}{5}R\_2$):

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 3/5 & 7/5 \\
0 & 0 & 3 & 2 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

Clear the second row using column operations:
*   $C\_3 \to C\_3 - \frac{3}{5}C\_2$
*   $C\_4 \to C\_4 - \frac{7}{5}C\_2$

This gives:

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 3 & 2 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

Scale row 3 ($R\_3 \to \frac{1}{3}R\_3$):

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 2/3 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

Clear the third column element ($C\_4 \to C\_4 - \frac{2}{3}C\_3$):

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

This is the canonical form $[I\_3 | 0]$:

$$
\begin{pmatrix}
I_3 & | & 0 \\
-- & - & -- \\
0 & | & 0
\end{pmatrix}
$$

---

### Q6(a) Find the inverse of the following matrix by using row operation: (06)

$$
A = \begin{pmatrix}
2 & 1 & 2 \\
2 & 2 & 1 \\
1 & 2 & 2
\end{pmatrix}
$$

**Answer:**

We write the augmented matrix $[A | I]$:

$$
\begin{bmatrix}
2 & 1 & 2 & | & 1 & 0 & 0 \\
2 & 2 & 1 & | & 0 & 1 & 0 \\
1 & 2 & 2 & | & 0 & 0 & 1
\end{bmatrix}
$$

Swap row 1 and row 3 ($R\_1 \leftrightarrow R\_3$):

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
2 & 2 & 1 & | & 0 & 1 & 0 \\
2 & 1 & 2 & | & 1 & 0 & 0
\end{bmatrix}
$$

Apply row operations:
*   $R\_2 \to R\_2 - 2R\_1$
*   $R\_3 \to R\_3 - 2R\_1$

This gives:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
0 & -2 & -3 & | & 0 & 1 & -2 \\
0 & -3 & -2 & | & 1 & 0 & -2
\end{bmatrix}
$$

Multiply row 2 by $-1/2$ ($R\_2 \to -1/2 R\_2$):

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
0 & 1 & 3/2 & | & 0 & -1/2 & 1 \\
0 & -3 & -2 & | & 1 & 0 & -2
\end{bmatrix}
$$

Eliminate the third row element ($R\_3 \to R\_3 + 3R\_2$):

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
0 & 1 & 3/2 & | & 0 & -1/2 & 1 \\
0 & 0 & 5/2 & | & 1 & -3/2 & 1
\end{bmatrix}
$$

Multiply row 3 by $2/5$ ($R\_3 \to 2/5 R\_3$):

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
0 & 1 & 3/2 & | & 0 & -1/2 & 1 \\
0 & 0 & 1 & | & 2/5 & -3/5 & 2/5
\end{bmatrix}
$$

Perform the operation $R\_2 \to R\_2 - \frac{3}{2}R\_3$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
0 & 1 & 0 & | & -3/5 & 2/5 & 2/5 \\
0 & 0 & 1 & | & 2/5 & -3/5 & 2/5
\end{bmatrix}
$$

Perform the operation $R\_1 \to R\_1 - 2R\_3$:

$$
\begin{bmatrix}
1 & 2 & 0 & | & -4/5 & 6/5 & 1/5 \\
0 & 1 & 0 & | & -3/5 & 2/5 & 2/5 \\
0 & 0 & 1 & | & 2/5 & -3/5 & 2/5
\end{bmatrix}
$$

Perform the operation $R\_1 \to R\_1 - 2R\_2$:

$$
\begin{bmatrix}
1 & 0 & 0 & | & 2/5 & 2/5 & -3/5 \\
0 & 1 & 0 & | & -3/5 & 2/5 & 2/5 \\
0 & 0 & 1 & | & 2/5 & -3/5 & 2/5
\end{bmatrix}
$$

So the inverse is:

$$
A^{-1} = \frac{1}{5} \begin{pmatrix}
2 & 2 & -3 \\
-3 & 2 & 2 \\
2 & -3 & 2
\end{pmatrix}
$$

---

### Q6(b) Discuss for what values of $\lambda$ the following system of equations have (i) no solution (ii) unique solution and (iii) infinite number of solutions: (06)

$$
\lambda x + y + z = 1
$$

$$
x + \lambda y + z = \lambda
$$

$$
x + y + \lambda z = \lambda^2
$$

**Answer:**

We write the determinant of the coefficient matrix:

$$
D = \begin{vmatrix}
\lambda & 1 & 1 \\
1 & \lambda & 1 \\
1 & 1 & \lambda
\end{vmatrix}
$$

Add rows 2 and 3 to row 1:

$$
D = \begin{vmatrix}
\lambda+2 & \lambda+2 & \lambda+2 \\
1 & \lambda & 1 \\
1 & 1 & \lambda
\end{vmatrix} = (\lambda + 2) \begin{vmatrix}
1 & 1 & 1 \\
1 & \lambda & 1 \\
1 & 1 & \lambda
\end{vmatrix}
$$

Apply column operations ($C\_2 \to C\_2 - C\_1$, $C\_3 \to C\_3 - C\_1$):

$$
D = (\lambda + 2) \begin{vmatrix}
1 & 0 & 0 \\
1 & \lambda-1 & 0 \\
1 & 0 & \lambda-1
\end{vmatrix} = (\lambda + 2)(\lambda - 1)^2
$$

We investigate the cases:

#### (i) Unique Solution

A unique solution exists if the determinant is not zero:

$$
D \neq 0 \implies \lambda \neq 1 \quad \text{and} \quad \lambda \neq -2
$$

#### (ii) Infinite Solutions

If $\lambda = 1$, the system of equations becomes:

$$
x + y + z = 1
$$

$$
x + y + z = 1
$$

$$
x + y + z = 1
$$

All three equations are identical. The system is consistent and has an infinite number of solutions.

#### (iii) No Solution

If $\lambda = -2$, the system becomes:

$$
-2x + y + z = 1 \quad \dots \text{(1)}
$$

$$
x - 2y + z = -2 \quad \dots \text{(2)}
$$

$$
x + y - 2z = 4 \quad \dots \text{(3)}
$$

Add these three equations:

$$
(-2x + x + x) + (y - 2y + y) + (z + z - 2z) = 1 - 2 + 4 \implies 0 = 3
$$

This is a contradiction. So there is no solution when $\lambda = -2$.

---

### Q7(a) Find the eigenvalues and the corresponding eigen vectors of the matrix 

$$
A = \begin{bmatrix}
2 & 3 \\
1 & 4
\end{bmatrix}
$$

(06)

**Answer:**

#### 1. Find Eigenvalues

We solve the characteristic equation $|A - \lambda I| = 0$:

$$
\begin{vmatrix}
2-\lambda & 3 \\
1 & 4-\lambda
\end{vmatrix} = 0 \implies (2-\lambda)(4-\lambda) - 3 = 0
$$

$$
\lambda^2 - 6\lambda + 5 = 0 \implies (\lambda - 1)(\lambda - 5) = 0
$$

So the eigenvalues are:

$$
\lambda = 1, \quad \lambda = 5
$$

#### 2. Find Eigenvectors

##### Case 1: For $\lambda = 1$

We solve $(A - I)X = 0$:

$$
\begin{bmatrix}
1 & 3 \\
1 & 3
\end{bmatrix} \begin{bmatrix}
x \\
y
\end{bmatrix} = \begin{bmatrix}
0 \\
0
\end{bmatrix} \implies x + 3y = 0 \implies x = -3y
$$

Let $y = 1$. The eigenvector is:

$$
X_1 = \begin{bmatrix}
-3 \\
1
\end{bmatrix}
$$

##### Case 2: For $\lambda = 5$

We solve $(A - 5I)X = 0$:

$$
\begin{bmatrix}
-3 & 3 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
x \\
y
\end{bmatrix} = \begin{bmatrix}
0 \\
0
\end{bmatrix} \implies x - y = 0 \implies x = y
$$

Let $y = 1$. The eigenvector is:

$$
X_2 = \begin{bmatrix}
1 \\
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

### Q8(a) Express $V=(1, -2, 5)$ in $\mathbb{R}^3$ as a linear combination of the vectors $U\_1 = (1, 1, 1)$, $U\_2 = (1, 2, 3)$ and $U\_3 = (2, -1, 1)$. (04)

**Answer:**

We write the relation:

$$
V = c_1 U_1 + c_2 U_2 + c_3 U_3 \implies (1, -2, 5) = c_1(1, 1, 1) + c_2(1, 2, 3) + c_3(2, -1, 1)
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
V = -6U_1 + 3U_2 + 2U_3
$$

---

### Q8(b) Determine whether $(1, 1, 1, 1)$, $(1, 2, 3, 2)$, $(2, 5, 6, 4)$, $(2, 6, 8, 5)$ form a basis of $\mathbb{R}^4$. If not, find the dimension of the subspace they span. (04)

**Answer:**

We write the vectors as rows of a matrix:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 2 & 3 & 2 \\
2 & 5 & 6 & 4 \\
2 & 6 & 8 & 5
\end{bmatrix}
$$

Apply row operations:
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

Apply operations:
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

Subtract row 3 from row 4 ($R\_4 \to R\_4 - R\_3$):

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 2 & 1 \\
0 & 0 & -2 & -1 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

Since the last row is zero, the vectors are linearly dependent. Therefore, they do not form a basis of $\mathbb{R}^4$.

The number of non-zero rows is 3. So the dimension of the subspace they span is:

$$
\text{Dimension} = 3
$$

---

### Q8(c) Suppose the vectors $(u, v, w)$ are linearly independent. Show that the vectors $u + v, u - v, u - 2v + w$ are also linearly independent. (04)

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

[⬅ 2020](2020_answer.md) | [🏠 Index](00-index.md) | [2023 ➡](2023_answer.md)
