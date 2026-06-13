# Lecture 14: Concept of Green's Theorem

> **Series**: Vector Calculus
> **Lecture**: 14 of 14
> **Video**: https://www.youtube.com/watch?v=EiWb17ofMnA

---

**Navigation**
[< Previous Lecture](13_Gauss_Divergence_Theorem_Part2.md) | [Index](README.md)

---

## Prerequisites
We have completed our study of Stokes' Theorem (relating 3D line integrals to 3D surface integrals) and Gauss Divergence Theorem (relating 3D surface integrals to 3D volume integrals). We conclude our vector calculus series with **Green's Theorem**, which is essentially a specialized 2D case of Stokes' Theorem. It relates a line integral around a simple closed curve in a 2D plane to a double integral over the flat area enclosed by that curve.

---

## Green's Theorem in a Plane

### Statement
If $P(x, y)$ and $Q(x, y)$ are continuous functions with continuous partial derivatives in a region $S$ enclosed by a closed curve $C$ in the $xy$-plane, then:
$$
\oint_C (P \, dx + Q \, dy) = \iint_S \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx \, dy
$$
Where:
*   $C$ is traversed in the positive (anticlockwise) direction.
*   $P$ is the expression multiplied by $dx$.
*   $Q$ is the expression multiplied by $dy$.

### Why is this Theorem Useful?
Just like the other theorems, Green's Theorem allows us to bypass tedious boundary integrations. If a boundary $C$ consists of multiple line segments (like a triangle or a rectangle), evaluating $\oint_C$ directly requires calculating multiple separate integrals. By applying Green's Theorem, you can simply evaluate a single double integral over the bounded flat region $S$.

---

## Solved Problems

### Problem 1: Evaluating a Line Integral via Double Integral
**Question:** Evaluate by Green's Theorem the line integral $\oint_C (e^{-x} \sin y \, dx + e^{-x} \cos y \, dy)$, where $C$ is the rectangle with vertices $(0,0), (\pi, 0), (\pi, \frac{\pi}{2}), (0, \frac{\pi}{2})$.

**Solution:**
We identify the components $P$ and $Q$ from the integral form $\oint_C (P \, dx + Q \, dy)$:
*   $P = e^{-x} \sin y \implies \frac{\partial P}{\partial y} = e^{-x} \cos y$
*   $Q = e^{-x} \cos y \implies \frac{\partial Q}{\partial x} = -e^{-x} \cos y$

Compute the integrand for the double integral:
$$
\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = -e^{-x} \cos y - e^{-x} \cos y = -2e^{-x} \cos y
$$
Set up the double integral over the rectangular region $S$. The limits are clearly defined by the vertices: $x$ varies from $0$ to $\pi$, and $y$ varies from $0$ to $\frac{\pi}{2}$.
$$
\iint_S \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx \, dy = \int_0^\pi \int_0^{\frac{\pi}{2}} -2e^{-x} \cos y \, dy \, dx
$$
Since the limits are constants, we can separate the variables:
$$
= -2 \left( \int_0^\pi e^{-x} \, dx \right) \left( \int_0^{\frac{\pi}{2}} \cos y \, dy \right)
$$
Evaluate the $y$-integral:
$$
\int_0^{\frac{\pi}{2}} \cos y \, dy = [\sin y]_0^{\frac{\pi}{2}} = 1 - 0 = 1
$$
Evaluate the $x$-integral:
$$
\int_0^\pi e^{-x} \, dx = [-e^{-x}]_0^\pi = -e^{-\pi} - (-1) = 1 - e^{-\pi}
$$
Multiply them together with the constant $-2$:
$$
= -2(1 - e^{-\pi})(1) = 2(e^{-\pi} - 1)
$$
**Final Answer: $2(e^{-\pi} - 1)$**

---

### Problem 2: Verifying Green's Theorem on a Circle
**Question:** Verify Green's Theorem for the line integral $\oint_C (x + 2y) \, dx + (y + 3x) \, dy$ where $C$ is the unit circle $x^2 + y^2 = 1$.

**Solution:**
To verify, we must independently compute both the LHS (Line Integral) and the RHS (Double Integral).

**Part 1: Line Integral (LHS)**
Convert the circle $x^2+y^2=1$ to parametric coordinates: $x = \cos\theta, dx = -\sin\theta d\theta$ and $y = \sin\theta, dy = \cos\theta d\theta$, for $\theta \in [0, 2\pi]$.
$$
\oint_C = \int_0^{2\pi} \left[ (\cos\theta + 2\sin\theta)(-\sin\theta) + (\sin\theta + 3\cos\theta)(\cos\theta) \right] d\theta
$$
$$
= \int_0^{2\pi} \left( -\sin\theta\cos\theta - 2\sin^2\theta + \sin\theta\cos\theta + 3\cos^2\theta \right) d\theta
$$
The $\sin\theta\cos\theta$ terms cancel:
$$
= \int_0^{2\pi} (3\cos^2\theta - 2\sin^2\theta) \, d\theta
$$
Using double-angle formulas ($\cos^2\theta = \frac{1+\cos 2\theta}{2}$ and $\sin^2\theta = \frac{1-\cos 2\theta}{2}$):
$$
= \int_0^{2\pi} \left[ 3\left(\frac{1+\cos 2\theta}{2}\right) - 2\left(\frac{1-\cos 2\theta}{2}\right) \right] d\theta = \int_0^{2\pi} \left( \frac{1}{2} + \frac{5}{2}\cos 2\theta \right) d\theta
$$
$$
= \left[ \frac{\theta}{2} + \frac{5}{4}\sin 2\theta \right]_0^{2\pi} = \frac{2\pi}{2} + 0 = \pi
$$
**LHS = $\pi$**

**Part 2: Double Integral (RHS)**
Identify $P = x + 2y$ and $Q = y + 3x$.
$$
\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 3 - 2 = 1
$$
The integral becomes:
$$
\iint_S 1 \, dx \, dy = \text{Area of region } S
$$
Since $S$ is a circle of radius $R=1$, its area is $\pi R^2 = \pi$.
**RHS = $\pi$**

Since **LHS = RHS = $\pi$**, Green's Theorem is verified.

---

### Problem 3: Verifying Green's Theorem between Curves
**Question:** Verify Green's Theorem for $\oint_C (xy + y^2) \, dx + x^2 \, dy$ where $C$ is the closed curve bounded by $y = x^2$ and $y = x$.

**Solution:**
The intersection points of $y = x^2$ and $y = x$ are $(0,0)$ and $(1,1)$.

**Part 1: Line Integral (LHS)**
The boundary $C$ has two paths traversed in an anticlockwise loop:
1.  **$C_1$ (Lower Curve):** Along $y = x^2$ from $x=0$ to $x=1$. ($dy = 2x \, dx$)
$$
I_1 = \int_0^1 \left[ (x(x^2) + (x^2)^2) + x^2(2x) \right] dx = \int_0^1 (3x^3 + x^4) \, dx = \left[ \frac{3}{4}x^4 + \frac{1}{5}x^5 \right]_0^1 = \frac{19}{20}
$$
2.  **$C_2$ (Upper Curve):** Along $y = x$ from $x=1$ to $x=0$. ($dy = dx$)
$$
I_2 = \int_1^0 \left[ (x^2 + x^2) + x^2 \right] dx = \int_1^0 3x^2 \, dx = [x^3]_1^0 = -1
$$
Summing the paths: $\text{LHS} = \frac{19}{20} - 1 = -\frac{1}{20}$.

**Part 2: Double Integral (RHS)**
$$
P = xy + y^2 \implies \frac{\partial P}{\partial y} = x + 2y.
$$
$$
Q = x^2 \implies \frac{\partial Q}{\partial x} = 2x.
$$
$$
\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 2x - (x + 2y) = x - 2y
$$
Set up the bounds: For a given $x \in [0, 1]$, $y$ ranges from the lower curve ($y=x^2$) to the upper curve ($y=x$).
$$
\text{RHS} = \int_0^1 \int_{x^2}^x (x - 2y) \, dy \, dx = \int_0^1 [xy - y^2]_{x^2}^x \, dx
$$
$$
= \int_0^1 \left[ (x^2 - x^2) - (x^3 - x^4) \right] dx = \int_0^1 (x^4 - x^3) \, dx
$$
$$
= \left[ \frac{x^5}{5} - \frac{x^4}{4} \right]_0^1 = \frac{1}{5} - \frac{1}{4} = -\frac{1}{20}
$$
Since **LHS = RHS = $-\frac{1}{20}$**, Green's Theorem is verified.

---

## Conclusion
This marks the conclusion of our Vector Calculus series! From basic scalar and vector point functions, to the differential operators Gradient, Curl, and Divergence, and finally the monumental theorems of Stokes, Gauss, and Green that unify vector integration. We are now fully equipped to transition into Complex Analysis.

---

**Navigation**
[< Previous Lecture](13_Gauss_Divergence_Theorem_Part2.md) | [Index](README.md)
