# Topic 04: Green's Theorem

This file contains the organized questions and answers for **Green's Theorem**, priority ranked as **Priority 4** based on frequency and exam weight.

---

## Q1 (06)

If 

$$
\vec{F} = (2x + y^2)\hat{i} + (3y - 4x)\hat{j}
$$

, then evaluate 

$$
\oint_C \vec{F} \cdot d\vec{r}
$$

 around the curve $C$ of the following figure:

| | |
|---|---|
| **ID** | PYQ-2017-2a |
| **Source** | 2017 Q2(a) [06 marks] |

**Answer:**

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

## Q2. State and prove Green's theorem in the plane. (06)

| | |
|---|---|
| **ID** | PYQ-2017-3a | PYQ-2021-4a | PYQ-2024-4a |
| **Appeared in** | 2017 Q3(a) [06 marks], 2021 Q4(a) [06 marks], 2024 Q4(a) [05 marks] |
| **Frequency** | ⭐⭐⭐ (3 times) |

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

## Q3 (06)

Evaluate 

$$
\oint_C (y - \sin x)dx + \cos y dy
$$

 where $C$ is the triangle of the adjoining figure:

| | |
|---|---|
| **ID** | PYQ-2017-3b |
| **Source** | 2017 Q3(b) [06 marks] |

**Answer:**

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

## Q4 (06)

Verify Green's theorem in the plane for 

$$
\oint_C (2x - y^2)dx - xydy
$$

 where $C$ is the boundary of the region enclosed by the circles $x^2 + y^2 = 1$ and $x^2 + y^2 = 9$.

| | |
|---|---|
| **ID** | PYQ-2019-4b |
| **Source** | 2019 Q4(b) [06 marks] |

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

The region $R$ is the annulus between the circles $r=1$ and $r=3$. We convert to polar coordinates (

$$
x = r\cos\theta, \quad y = r\sin\theta, \quad dA = r \, dr \, d\theta
$$

):

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

The closed boundary $C$ consists of two circular paths: the outer circle $C\_1$ ($r=3$, traversed counterclockwise) and the inner circle $C\_2$ ($r=1$, traversed clockwise):

- **On Outer Circle $C\_1$:** $x = 3\cos\theta, y = 3\sin\theta \implies dx = -3\sin\theta \, d\theta, dy = 3\cos\theta \, d\theta$ with $\theta$ from $0$ to $2\pi$:

$$
\int_{C_1} (2x - y^2)dx - xydy = \int_0^{2\pi} \left[ (6\cos\theta - 9\sin^2\theta)(-3\sin\theta) - 9\cos\theta\sin\theta(3\cos\theta) \right] d\theta
$$

$$
= \int_0^{2\pi} \left[ -18\cos\theta\sin\theta + 27\sin^3\theta - 27\cos^2\theta\sin\theta \right] d\theta = 0
$$

(since each component integrates to $0$ over the full period $[0, 2\pi]$).

- **On Inner Circle $C\_2$:** $x = \cos\theta, y = \sin\theta \implies dx = -\sin\theta \, d\theta, dy = \cos\theta \, d\theta$ with $\theta$ from $2\pi$ to $0$:

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

---

## Q5 (06)

Verify Green's theorem in the plane for 

$$
\oint_C (xy + y^2)dx + x^2dy
$$

 where $C$ is a closed region bounded by $y = x$ and $y = x^2$.

| | |
|---|---|
| **ID** | PYQ-2020-4b | PYQ-2023-3b |
| **Appeared in** | 2020 Q4(b) [06 marks], 2023 Q3(b) [05 marks] |
| **Frequency** | ⭐⭐ (2 times) |

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

---

