# Lecture 06: Concept of Vector Integration and Line Integration

> **Series**: Vector Calculus
> **Lecture**: 06 of 14
> **Video**: https://www.youtube.com/watch?v=0CRFlOOSA9c

---

**Navigation**
[< Previous Lecture](05_Curl_and_Divergence.md) | [Index](README.md) | [Next Lecture >](07_Surface_Integral_Part1.md)

---

## Prerequisites
We have thoroughly covered vector differentiation (Gradient, Divergence, and Curl). Now we move in the opposite direction: **Vector Integration**. There are three main types of integrals in vector calculus:
1.  **Line Integral**
2.  **Surface Integral**
3.  **Volume Integral**

A solid understanding of these integrals forms the foundation for three major theorems: Green's Theorem, Stokes' Theorem, and Gauss Divergence Theorem. We will start with standard vector integration and Line Integrals.

---

## 1. Integration of Vector Functions

Just like scalar functions, a vector point function $\vec{F}(t) = F_1(t)\hat{i} + F_2(t)\hat{j} + F_3(t)\hat{k}$ depending on a single scalar variable $t$ can be integrated.

### Indefinite Integral
To integrate indefinitely, integrate each component separately and add an arbitrary constant vector $\vec{c} = c_1\hat{i} + c_2\hat{j} + c_3\hat{k}$.
$$
\int \vec{F}(t) dt = \left(\int F_1(t) dt\right)\hat{i} + \left(\int F_2(t) dt\right)\hat{j} + \left(\int F_3(t) dt\right)\hat{k} + \vec{c}
$$

### Definite Integral
To integrate over an interval $[a, b]$, compute the integral and apply the upper and lower limits to each component.
$$
\int_a^b \vec{F}(t) dt = \left[ \vec{f}(t) \right]_a^b = \vec{f}(b) - \vec{f}(a)
$$

---

## 2. Solved Problems (Vector Integration)

### Problem 1: Basic Definite Integral
**Question:** If $\vec{F}(t) = (t - t^2)\hat{i} + 2t^3\hat{j} - 3\hat{k}$, find $\int_1^2 \vec{F}(t) dt$.

**Solution:**
Integrate each component with respect to $t$:
$$
\int_1^2 \left[ (t - t^2)\hat{i} + 2t^3\hat{j} - 3\hat{k} \right] dt = \left[ \left( \frac{t^2}{2} - \frac{t^3}{3} \right)\hat{i} + \frac{2t^4}{4}\hat{j} - 3t\hat{k} \right]_1^2
$$
Apply the upper limit ($t=2$):
$$
\left( \frac{4}{2} - \frac{8}{3} \right)\hat{i} + \frac{16}{2}\hat{j} - 6\hat{k} = -\frac{2}{3}\hat{i} + 8\hat{j} - 6\hat{k}
$$
Apply the lower limit ($t=1$):
$$
\left( \frac{1}{2} - \frac{1}{3} \right)\hat{i} + \frac{1}{2}\hat{j} - 3\hat{k} = \frac{1}{6}\hat{i} + \frac{1}{2}\hat{j} - 3\hat{k}
$$
Subtract the two:
$$
\left( -\frac{2}{3} - \frac{1}{6} \right)\hat{i} + \left( 8 - \frac{1}{2} \right)\hat{j} + (-6 - (-3))\hat{k} = -\frac{5}{6}\hat{i} + \frac{15}{2}\hat{j} - 3\hat{k}
$$

### Problem 2: Finding Velocity and Displacement
**Question:** The acceleration of a particle is $\vec{a} = 12\cos 2t\hat{i} - 8\sin 2t\hat{j} + 16t\hat{k}$. Find velocity $\vec{v}$ and displacement $\vec{r}$ given that at $t = 0$, $\vec{v} = 0$ and $\vec{r} = 0$.

**Solution:**
Integrate acceleration to find velocity $\vec{v}(t)$:
$$
\vec{v}(t) = \int \vec{a}(t) dt = \int (12\cos 2t\hat{i} - 8\sin 2t\hat{j} + 16t\hat{k}) dt
$$
$$
\vec{v}(t) = 6\sin 2t\hat{i} + 4\cos 2t\hat{j} + 8t^2\hat{k} + \vec{c}_1
$$
Apply boundary condition $\vec{v}(0) = 0$:
$$
0 = 0\hat{i} + 4\hat{j} + 0\hat{k} + \vec{c}_1 \implies \vec{c}_1 = -4\hat{j}
$$
$$
\vec{v}(t) = 6\sin 2t\hat{i} + (4\cos 2t - 4)\hat{j} + 8t^2\hat{k}
$$
Integrate velocity to find displacement $\vec{r}(t)$:
$$
\vec{r}(t) = \int \vec{v}(t) dt = \int \left[ 6\sin 2t\hat{i} + (4\cos 2t - 4)\hat{j} + 8t^2\hat{k} \right] dt
$$
$$
\vec{r}(t) = -3\cos 2t\hat{i} + (2\sin 2t - 4t)\hat{j} + \frac{8}{3}t^3\hat{k} + \vec{c}_2
$$
Apply boundary condition $\vec{r}(0) = 0$:
$$
0 = -3\hat{i} + 0\hat{j} + 0\hat{k} + \vec{c}_2 \implies \vec{c}_2 = 3\hat{i}
$$
$$
\vec{r}(t) = (3 - 3\cos 2t)\hat{i} + (2\sin 2t - 4t)\hat{j} + \frac{8}{3}t^3\hat{k}
$$

### Problem 3: Integration Involving Dot Product
**Question:** Given $\vec{r}(t) = 2\hat{i} - \hat{j} + 2\hat{k}$ at $t = 2$ and $\vec{r}(t) = 4\hat{i} - 2\hat{j} + 3\hat{k}$ at $t = 3$, prove that $\int_2^3 \left( \vec{r} \cdot \frac{d\vec{r}}{dt} \right) dt = 10$.

**Solution:**
Calculate the magnitudes of $\vec{r}$ at the boundaries:
At $t = 2$: $r_1 = |\vec{r}| = \sqrt{2^2 + (-1)^2 + 2^2} = \sqrt{9} = 3$
At $t = 3$: $r_2 = |\vec{r}| = \sqrt{4^2 + (-2)^2 + 3^2} = \sqrt{29}$
Using the identity $\vec{r} \cdot \frac{d\vec{r}}{dt} = \frac{1}{2}\frac{d}{dt}(r^2)$:
$$
\int_2^3 \left( \vec{r} \cdot \frac{d\vec{r}}{dt} \right) dt = \frac{1}{2} \int_2^3 \frac{d}{dt}(r^2) dt = \frac{1}{2} [r^2]_{t=2}^{t=3} = \frac{1}{2} (r_2^2 - r_1^2)
$$
$$
= \frac{1}{2} (29 - 9) = \frac{1}{2}(20) = 10 \quad \text{(Proved)}
$$

---

## 3. Line Integration

A line integral computes the integral of a vector field $\vec{F}$ along a specific curve $C$ in space.
Let $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ be the position vector of any point on curve $C$. The differential displacement vector is $d\vec{r} = dx\hat{i} + dy\hat{j} + dz\hat{k}$.
The line integral of $\vec{F}$ along curve $C$ is defined by the dot product:
$$
\int_C \vec{F} \cdot d\vec{r} = \int_C (F_1 dx + F_2 dy + F_3 dz)
$$

### How to Evaluate Line Integrals
You cannot integrate directly when $x, y,$ and $z$ are all mixed together. **The curve $C$ provides the relationship between the variables.** 
The most reliable method is to use parametric equations. If the curve $C$ is described by $x = x(t)$, $y = y(t)$, and $z = z(t)$ as $t$ varies from $t_1$ to $t_2$:
$$
\int_C \vec{F} \cdot d\vec{r} = \int_{t_1}^{t_2} \left( F_1 \frac{dx}{dt} + F_2 \frac{dy}{dt} + F_3 \frac{dz}{dt} \right) dt
$$
If $C$ is a closed curve (like a circle or rectangle), the line integral is called the **circulation** of $\vec{F}$, denoted as $\oint_C \vec{F} \cdot d\vec{r}$. By standard convention, closed paths are traversed in the anti-clockwise direction.

---

## 4. Solved Problems (Line Integration)

### Problem 4: Line Integration on a Parametric Curve
**Question:** Evaluate $\int_C \vec{F} \cdot d\vec{r}$ where $\vec{F} = xy\hat{i} + yz\hat{j} + zx\hat{k}$ and $C$ is $\vec{r} = t\hat{i} + t^2\hat{j} + t^3\hat{k}$ from $t=-1$ to $1$.

**Solution:**
From the curve equation, $x = t, y = t^2, z = t^3$.
Differentiating gives $dx = dt, dy = 2t dt, dz = 3t^2 dt$.
Substitute $x, y, z$ into $\vec{F}$:
$$
\vec{F} = (t)(t^2)\hat{i} + (t^2)(t^3)\hat{j} + (t^3)(t)\hat{k} = t^3\hat{i} + t^5\hat{j} + t^4\hat{k}
$$
The displacement vector is $d\vec{r} = (\hat{i} + 2t\hat{j} + 3t^2\hat{k}) dt$.
Take the dot product $\vec{F} \cdot d\vec{r}$:
$$
\vec{F} \cdot d\vec{r} = (t^3)(1) + (t^5)(2t) + (t^4)(3t^2) = (t^3 + 2t^6 + 3t^6) dt = (t^3 + 5t^6) dt
$$
Integrate from $-1$ to $1$:
$$
\int_{-1}^1 (t^3 + 5t^6) dt = \left[ \frac{t^4}{4} + \frac{5t^7}{7} \right]_{-1}^1 = \left( \frac{1}{4} + \frac{5}{7} \right) - \left( \frac{1}{4} - \frac{5}{7} \right) = \frac{10}{7}
$$

### Problem 5: Line Integration on a Parabola
**Question:** Evaluate $\int_C \vec{F} \cdot d\vec{r}$ where $\vec{F} = x^2 y^2\hat{i} + y\hat{j}$ and $C$ is the parabola $y^2 = 4x$ from $(0,0)$ to $(4,4)$.

**Solution:**
The integrand is $\vec{F} \cdot d\vec{r} = x^2 y^2 dx + y dy$.
Using the curve equation $y^2 = 4x \implies x = \frac{y^2}{4}$, we substitute it into the $dx$ term. Both $x$ and $y$ vary from $0$ to $4$.
$$
\int_C \vec{F} \cdot d\vec{r} = \int_0^4 x^2(4x) dx + \int_0^4 y dy = \int_0^4 4x^3 dx + \int_0^4 y dy
$$
$$
= \left[ x^4 \right]_0^4 + \left[ \frac{y^2}{2} \right]_0^4 = (256) + \left(\frac{16}{2}\right) = 256 + 8 = 264
$$

### Problem 6: Line Integration on an Arbitrary Path
**Question:** Evaluate $\int_C \left[ yz dx + (zx+1) dy + xy dz \right]$ where $C$ is any path from $(1,0,0)$ to $(2,1,4)$.

**Solution:**
Since the integral is path-independent (it specifies "any path"), we choose the straight line connecting the two points.
The equation of the line is $\frac{x - 1}{2 - 1} = \frac{y - 0}{1 - 0} = \frac{z - 0}{4 - 0} = t$.
Parametric equations: $x = t + 1, y = t, z = 4t \implies dx = dt, dy = dt, dz = 4dt$.
At $(1,0,0)$, $t = 0$. At $(2,1,4)$, $t = 1$. Substitute these into the integrand:
$$
(t)(4t)dt + ((4t)(t+1) + 1)dt + (t+1)(t)(4dt) = (4t^2 + 4t^2 + 4t + 1 + 4t^2 + 4t) dt = (12t^2 + 8t + 1) dt
$$
Integrate from $0$ to $1$:
$$
\int_0^1 (12t^2 + 8t + 1) dt = \left[ 4t^3 + 4t^2 + t \right]_0^1 = 4(1) + 4(1) + 1 = 9
$$

### Problem 7: Circulation Around a Rectangle (1)
**Question:** Find the circulation of $\vec{F} = e^x\sin y\hat{i} + e^x\cos y\hat{j}$ along the rectangle with vertices $(0,0), (1,0), (1, \frac{\pi}{2}), (0, \frac{\pi}{2})$.

**Solution:**
The integral is $\oint_C \vec{F} \cdot d\vec{r} = \oint_C (e^x\sin y dx + e^x\cos y dy)$. We split it into four segments:
1.  **$OA$ from $(0,0)$ to $(1,0)$**: $y=0 \implies dy=0$. $x$ from $0$ to $1$.
    $\int_{OA} = \int_0^1 e^x(0)dx = 0$
2.  **$AB$ from $(1,0)$ to $(1, \frac{\pi}{2})$**: $x=1 \implies dx=0$. $y$ from $0$ to $\frac{\pi}{2}$.
    $\int_{AB} = \int_0^{\pi/2} e^1 \cos y dy = e[\sin y]_0^{\pi/2} = e$
3.  **$BC$ from $(1, \frac{\pi}{2})$ to $(0, \frac{\pi}{2})$**: $y=\frac{\pi}{2} \implies dy=0$. $x$ from $1$ to $0$.
    $\int_{BC} = \int_1^0 e^x \sin(\frac{\pi}{2}) dx = \int_1^0 e^x dx = [e^x]_1^0 = 1 - e$
4.  **$CO$ from $(0, \frac{\pi}{2})$ to $(0,0)$**: $x=0 \implies dx=0$. $y$ from $\frac{\pi}{2}$ to $0$.
    $\int_{CO} = \int_{\pi/2}^0 e^0 \cos y dy = [\sin y]_{\pi/2}^0 = 0 - 1 = -1$

Summing all segments:
$$
\oint_C \vec{F} \cdot d\vec{r} = 0 + e + (1 - e) - 1 = 0
$$

### Problem 8: Circulation Around a Rectangle (2)
**Question:** Evaluate $\int_C \vec{F} \cdot d\vec{r}$ where $\vec{F} = (x^2 + y^2)\hat{i} - 2xy\hat{j}$ and $C$ is the rectangle bounded by $y=0, x=a, y=b, x=0$.

**Solution:**
The integral is $\int_C ((x^2+y^2)dx - 2xy dy)$. Splitting into four segments $OA, AC, CB, BO$:
1.  **$OA$ ($y=0 \implies dy=0$, $x$ from $0$ to $a$)**:
    $\int_{OA} = \int_0^a x^2 dx = \frac{a^3}{3}$
2.  **$AC$ ($x=a \implies dx=0$, $y$ from $0$ to $b$)**:
    $\int_{AC} = \int_0^b -2ay dy = -2a[\frac{y^2}{2}]_0^b = -ab^2$
3.  **$CB$ ($y=b \implies dy=0$, $x$ from $a$ to $0$)**:
    $\int_{CB} = \int_a^0 (x^2+b^2) dx = [\frac{x^3}{3} + b^2x]_a^0 = -\frac{a^3}{3} - ab^2$
4.  **$BO$ ($x=0 \implies dx=0$, $y$ from $b$ to $0$)**:
    $\int_{BO} = \int_b^0 (0) dy = 0$

Summing all segments:
$$
\int_C \vec{F} \cdot d\vec{r} = \frac{a^3}{3} - ab^2 - \frac{a^3}{3} - ab^2 + 0 = -2ab^2
$$

### Problem 9: Line Integration on a Helix
**Question:** Evaluate $\int_C \vec{F} \cdot d\vec{r}$ where $\vec{F} = yz\hat{i} + zx\hat{j} + xy\hat{k}$ and $C$ is the curve $\vec{r} = (a\cos t)\hat{i} + (b\sin t)\hat{j} + (ct)\hat{k}$ from $t=0$ to $t=\pi/2$.

**Solution:**
The parametric equations are $x = a\cos t, y = b\sin t, z = ct$.
Differentials: $dx = -a\sin t dt, dy = b\cos t dt, dz = c dt$.
Substitute into $\vec{F}$:
$$
\vec{F} = (bct\sin t)\hat{i} + (act\cos t)\hat{j} + (ab\sin t\cos t)\hat{k}
$$
Dot product with $d\vec{r} = (-a\sin t\hat{i} + b\cos t\hat{j} + c\hat{k}) dt$:
$$
\vec{F} \cdot d\vec{r} = (-abc t\sin^2 t + abc t\cos^2 t + abc\sin t\cos t) dt
$$
$$
= abc [t(\cos^2 t - \sin^2 t) + \sin t\cos t] dt = abc \left(t\cos 2t + \frac{\sin 2t}{2}\right) dt
$$
Integrate from $0$ to $\pi/2$:
$$
\int_C \vec{F} \cdot d\vec{r} = abc \int_0^{\pi/2} \left(t\cos 2t + \frac{\sin 2t}{2}\right) dt
$$
Using integration by parts on $\int t\cos 2t dt = \frac{t\sin 2t}{2} - \int \frac{\sin 2t}{2} dt$:
$$
\int \left(t\cos 2t + \frac{\sin 2t}{2}\right) dt = \frac{t\sin 2t}{2}
$$
Evaluate limits:
$$
abc \left[\frac{t\sin 2t}{2}\right]_0^{\pi/2} = abc\left(\frac{\frac{\pi}{2}\sin\pi}{2} - 0\right) = abc(0) = 0
$$

---

## Key Takeaways
*   The curve $C$ provides the critical constraints (relationship between variables) needed to evaluate a line integral.
*   By substituting the curve's parametric equations into the line integral $\int_C (F_1 dx + F_2 dy + F_3 dz)$, you can convert the entire integral into a single variable $t$.
*   For line integrals over segmented paths (like a rectangle or triangle), split the integral into a sum of integrals for each segment, defining the unique bounds and constant variables for each.

## What Comes Next
We have seen how to calculate the integral over a one-dimensional path (Line Integration). Next, we will expand this into two dimensions with **Surface Integration**, where we will integrate over a 2D surface in 3D space.

---

**Navigation**
[< Previous Lecture](05_Curl_and_Divergence.md) | [Index](README.md) | [Next Lecture >](07_Surface_Integral_Part1.md)
