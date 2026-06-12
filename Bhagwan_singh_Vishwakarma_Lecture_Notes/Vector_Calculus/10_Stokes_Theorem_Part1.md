# Lecture 10: Vector Calculus - Concept of Stokes' Theorem (Part 1)

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 10 of 14
> **Video**: https://www.youtube.com/watch?v=uuWw4hG0s3Q

---

**Navigation**
[< Previous Lecture](09_Volume_Integral.md) | [Index](README.md) | [Next Lecture >](11_Stokes_Theorem_Part2.md)

---

## Prerequisites
We have extensively studied both Line Integrals

$$
\oint_C \mathbf{F} \cdot d\mathbf{r}
$$

And Surface Integrals (

$$
\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS
$$

). We are now ready to establish a powerful relationship between these two types of integrals using **Stokes' Theorem**.

---

## Stokes' Theorem

### Statement
Let $S$ be an open, two-sided surface bounded by a closed, non-intersecting curve $C$. If a vector point function $\mathbf{F}$ is continuous and differentiable over a region containing $S$ and $C$, then:

$$
\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} \, dS
$$

Where:
*   **$\oint_C$** denotes the line integral around the closed boundary curve $C$.
*   **$\iint_S$** denotes the surface integral over the surface $S$ bounded by $C$.
*   **$\nabla \times \mathbf{F}$** is the curl of the vector field $\mathbf{F}$.
*   **$\hat{\mathbf{n}}$** is the outward unit normal vector to the surface $S$.

### Orientation (The Right-Hand Screw Rule)
The theorem requires a strict convention between the direction you traverse the boundary curve $C$ and the direction of the outward unit normal $\hat{\mathbf{n}}$. 

If you traverse the boundary curve $C$ in the **anticlockwise (positive) direction**, and you curl the fingers of your right hand in that direction, your thumb points in the direction of the outward unit normal $\hat{\mathbf{n}}$. For example, if a surface lies flat in the $xy$-plane and you traverse its boundary anticlockwise, the outward normal points "upward" along the positive $z$-axis ($\hat{\mathbf{n}} = \hat{\mathbf{k}}$).

### Why is this Theorem Useful?
Stokes' Theorem allows you to swap a difficult line integral for an easier surface integral, or vice versa. 
For example, integrating a vector field along a rectangular boundary requires calculating $4$ separate line integrals and summing them up. Using Stokes' theorem, you can simply calculate the curl of the vector field and evaluate a *single* surface integral over the flat rectangular area.

---

## Solved Problems

### Problem 1: Verifying Stokes' Theorem on a Rectangle
**Question:** Verify Stokes' Theorem for

$$
\mathbf{F} = (x^2 + y^2)\hat{\mathbf{i}} - 2xy\hat{\mathbf{j}}
$$

taken round the rectangle bounded by $x = \pm a, y = 0, y = b$.

**Solution:**
To "verify" the theorem, we must independently calculate both the Left-Hand Side (Line Integral) and the Right-Hand Side (Surface Integral) and prove they yield the exact same result.

#### Part 1: Evaluating the Line Integral (LHS)
Let's define the rectangular boundary $C$ in the $xy$-plane with vertices: $C(-a, 0)$, $B(a, 0)$, $A(a, b)$, and $D(-a, b)$.
We will traverse this boundary in the **anticlockwise direction**. This divides the boundary into $4$ line segments:
1.  **$C_3$ (Bottom):** From $C(-a, 0)$ to $B(a, 0)$. Here, $y = 0 \implies dy = 0$. $x$ goes from $-a$ to $a$.
2.  **$C_4$ (Right):** From $B(a, 0)$ to $A(a, b)$. Here, $x = a \implies dx = 0$. $y$ goes from $0$ to $b$.
3.  **$C_1$ (Top):** From $A(a, b)$ to $D(-a, b)$. Here, $y = b \implies dy = 0$. $x$ goes from $a$ to $-a$.
4.  **$C_2$ (Left):** From $D(-a, b)$ to $C(-a, 0)$. Here, $x = -a \implies dx = 0$. $y$ goes from $b$ to $0$.

The general line integrand is $\mathbf{F} \cdot d\mathbf{r} = (x^2 + y^2)dx - 2xy \, dy$. Let's evaluate this for each segment:

**On $C_3$ (Bottom):**

$$
I_3 = \int_{-a}^a (x^2 + 0) \, dx = \left[ \frac{x^3}{3} \right]_{-a}^a = \frac{a^3}{3} - \left( -\frac{a^3}{3} \right) = \frac{2a^3}{3}
$$

**On $C_4$ (Right):**

$$
I_4 = \int_0^b -2(a)y \, dy = -2a \left[ \frac{y^2}{2} \right]_0^b = -ab^2
$$

**On $C_1$ (Top):**

$$
I_1 = \int_a^{-a} (x^2 + b^2) \, dx = \left[ \frac{x^3}{3} + b^2 x \right]_a^{-a} = \left( -\frac{a^3}{3} - ab^2 \right) - \left( \frac{a^3}{3} + ab^2 \right) = -\frac{2a^3}{3} - 2ab^2
$$

**On $C_2$ (Left):**

$$
I_2 = \int_b^0 -2(-a)y \, dy = 2a \int_b^0 y \, dy = 2a \left[ \frac{y^2}{2} \right]_b^0 = 2a \left( 0 - \frac{b^2}{2} \right) = -ab^2
$$

Summing the four line integrals gives the total LHS:

$$
\text{LHS} = I_1 + I_2 + I_3 + I_4 = \left( -\frac{2a^3}{3} - 2ab^2 \right) - ab^2 + \left( \frac{2a^3}{3} \right) - ab^2 = -4ab^2
$$

#### Part 2: Evaluating the Surface Integral (RHS)
We need to compute

$$
\iint_S (\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} \, dS
$$

over the rectangular area $S$.

First, compute the curl ($\nabla \times \mathbf{F}$):

$$
\nabla \times \mathbf{F} = \det
\begin{vmatrix}
\hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
x^2 + y^2 & -2xy & 0
\end{vmatrix}
$$

$$
= \hat{\mathbf{i}}(0 - 0) - \hat{\mathbf{j}}(0 - 0) + \hat{\mathbf{k}}\left( \frac{\partial}{\partial x}(-2xy) - \frac{\partial}{\partial y}(x^2 + y^2) \right)
$$

$$
= \hat{\mathbf{k}}(-2y - 2y) = -4y\hat{\mathbf{k}}
$$

Because the surface lies flat in the $xy$-plane and we traversed the boundary anticlockwise, the outward unit normal points along the positive $z$-axis: $\hat{\mathbf{n}} = \hat{\mathbf{k}}$.

$$
(\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} = (-4y\hat{\mathbf{k}}) \cdot \hat{\mathbf{k}} = -4y
$$

Now, set up the double integral over the rectangular bounds ($x$ from $-a$ to $a$, and $y$ from $0$ to $b$):

$$
\text{RHS} = \int_{-a}^a \int_0^b -4y \, dy \, dx
$$

Integrate with respect to $y$:

$$
\int_0^b -4y \, dy = -4 \left[ \frac{y^2}{2} \right]_0^b = -2b^2
$$

Integrate the result with respect to $x$:

$$
\int_{-a}^a -2b^2 \, dx = -2b^2 \left[ x \right]_{-a}^a = -2b^2 (a - (-a)) = -2b^2 (2a) = -4ab^2
$$

#### Conclusion
We have independently evaluated both sides:

$$
\text{LHS} = -4ab^2 \quad \text{and} \quad \text{RHS} = -4ab^2
$$

Since LHS $=$ RHS, Stokes' Theorem is strictly verified. Notice how much faster the surface integral approach (RHS) was compared to computing four separate line integrals (LHS).

## What Comes Next
In the next lecture, we will verify Stokes' Theorem on a 3D curved surface (a hemisphere) to further validate the theorem and see how to project a curved surface integral to a flat planar boundary.

---

**Navigation**
[< Previous Lecture](09_Volume_Integral.md) | [Index](README.md) | [Next Lecture >](11_Stokes_Theorem_Part2.md)
