# Lecture 09: Vector Calculus - Concept of Surface and Volume Integral (Part 3)

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 09 of 14
> **Video**: https://www.youtube.com/watch?v=EWpo_cqinOI

---

**Navigation**
[< Previous Lecture](08_Surface_Integral_Part2.md) | [Index](README.md) | [Next Lecture >](10_Stokes_Theorem_Part1.md)

---

## Prerequisites
In the preceding lectures, we explored surface integrals for flat planes and spherical surfaces. This lecture builds on those concepts to tackle more complex scenarios: evaluating surface integrals over a **closed multi-face surface** (like a cube) and formally calculating a **Volume Integral** over a 3D solid using triple integration.

---

## Solved Problems

### Problem 1: Surface Integral Over a Closed Cube
**Question:** Evaluate

$$
\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS,
$$

Where

$$
\mathbf{F} = 4xz\hat{\mathbf{i}} - y^2\hat{\mathbf{j}} + yz\hat{\mathbf{k}}
$$

and $S$ is the closed surface of the cube bounded by the planes $x = 0$, $x = a$, $y = 0$, $y = a$, $z = 0$, $z = a$.

**Solution:**
The closed surface $S$ of a cube consists of $6$ distinct flat faces. To evaluate the surface integral over $S$, we must evaluate the integral over each of the $6$ faces separately and sum the results.

Since the faces lie on or parallel to the coordinate planes, we don't need to compute gradients. We can directly identify the **outward unit normal vector $\hat{\mathbf{n}}$** by observing which direction points away from the interior of the cube.
The total integral is:

$$
I = I_1 + I_2 + I_3 + I_4 + I_5 + I_6.
$$

**1. Front Face ($x = a$)**
*   **Normal:** Outward normal points in the $+x$ direction, so

$$
\hat{\mathbf{n}} = \hat{\mathbf{i}}.
$$

*   **Area Element:** Projection is on the $yz$-plane, so $dS = dy \, dz$.
*   **Integrand:**

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = 4xz
$$

. Since $x = a$,

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = 4az.
$$

*   **Integral:** 

$$
I_1 = \int_0^a \int_0^a 4az \, dy \, dz = 4a \int_0^a z \, dz \int_0^a dy = 4a \left( \frac{a^2}{2} \right) (a) = 2a^4
$$

**2. Back Face ($x = 0$)**
*   **Normal:** Outward normal points in the $-x$ direction, so

$$
\hat{\mathbf{n}} = -\hat{\mathbf{i}}.
$$

*   **Area Element:** $dS = dy \, dz$.
*   **Integrand:**

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = -4xz
$$

. Since $x = 0$,

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = 0.
$$

*   **Integral:** 

$$
I_2 = 0
$$

**3. Right Face ($y = a$)**
*   **Normal:** Outward normal points in the $+y$ direction, so

$$
\hat{\mathbf{n}} = \hat{\mathbf{j}}.
$$

*   **Area Element:** $dS = dx \, dz$.
*   **Integrand:**

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = -y^2
$$

. Since $y = a$,

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = -a^2.
$$

*   **Integral:** 

$$
I_3 = \int_0^a \int_0^a -a^2 \, dx \, dz = -a^2 (a)(a) = -a^4
$$

**4. Left Face ($y = 0$)**
*   **Normal:** Outward normal points in the $-y$ direction, so

$$
\hat{\mathbf{n}} = -\hat{\mathbf{j}}.
$$

*   **Area Element:** $dS = dx \, dz$.
*   **Integrand:**

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = y^2
$$

. Since $y = 0$,

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = 0.
$$

*   **Integral:** 

$$
I_4 = 0
$$

**5. Top Face ($z = a$)**
*   **Normal:** Outward normal points in the $+z$ direction, so

$$
\hat{\mathbf{n}} = \hat{\mathbf{k}}.
$$

*   **Area Element:** $dS = dx \, dy$.
*   **Integrand:**

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = yz
$$

. Since $z = a$,

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = ay.
$$

*   **Integral:** 

$$
I_5 = \int_0^a \int_0^a ay \, dx \, dy = a \int_0^a y \, dy \int_0^a dx = a \left( \frac{a^2}{2} \right) (a) = \frac{a^4}{2}
$$

**6. Bottom Face ($z = 0$)**
*   **Normal:** Outward normal points in the $-z$ direction, so

$$
\hat{\mathbf{n}} = -\hat{\mathbf{k}}.
$$

*   **Area Element:** $dS = dx \, dy$.
*   **Integrand:**

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = -yz
$$

. Since $z = 0$,

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = 0.
$$

*   **Integral:** 

$$
I_6 = 0
$$

**Total Integral:**
Summing the results from all $6$ faces:

$$
\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS = 2a^4 + 0 - a^4 + 0 + \frac{a^4}{2} + 0 = a^4 + \frac{a^4}{2} = \frac{3a^4}{2}
$$

---

### Problem 2: Volume Integral Over a Solid Cylinder
**Question:** Evaluate

$$
\iiint_V (\nabla \cdot \mathbf{F}) \, dV
$$

 where

$$
\mathbf{F} = 4x\hat{\mathbf{i}} - 2y^2\hat{\mathbf{j}} + z^2\hat{\mathbf{k}},
$$

And $V$ is the solid region bounded by the cylinder

$$
x^2 + y^2 = 4
$$

and the planes $z = 0$ and $z = 3$.

**Solution:**
**Step 1: Compute the Integrand ($\nabla \cdot \mathbf{F}$)**
Calculate the divergence of the vector field:

$$
\nabla \cdot \mathbf{F} = \frac{\partial}{\partial x}(4x) + \frac{\partial}{\partial y}(-2y^2) + \frac{\partial}{\partial z}(z^2) = 4 - 4y + 2z
$$

**Step 2: Determine Limits of Integration**
The volume $V$ is a solid cylinder. The height is bounded by the planes $z=0$ and $z=3$. The base of the cylinder on the $xy$-plane is the circle

$$
x^2 + y^2 = 4
$$

(radius $r=2$).
-   **Limits for $z$:** Direct boundary conditions give $z = 0$ to $z = 3$.
-   **Limits for $x$ and $y$:** From the base circle

$$
x^2 + y^2 = 4
$$

, $x$ varies from $-2$ to $2$. For a given $x$, $y$ varies from the lower half of the circle to the upper half, so $y$ goes from $-\sqrt{4 - x^2}$ to $\sqrt{4 - x^2}$.

**Step 3: Setup and Evaluate the Triple Integral**

$$
I = \int_{-2}^2 \int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}} \int_0^3 (4 - 4y + 2z) \, dz \, dy \, dx
$$

**Inner Integration (with respect to $z$):**

$$
\int_0^3 (4 - 4y + 2z) \, dz = \left[ 4z - 4yz + z^2 \right]_0^3 = (12 - 12y + 9) - 0 = 21 - 12y = 3(7 - 4y)
$$

**Middle Integration (with respect to $y$):**
Substitute the result back:

$$
\int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}} 3(7 - 4y) \, dy = 3 \left[ 7y - 2y^2 \right]_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}}
$$

Apply the upper and lower limits:

$$
= 3 \left[ \left( 7\sqrt{4-x^2} - 2(4-x^2) \right) - \left( 7(-\sqrt{4-x^2}) - 2(4-x^2) \right) \right]
$$

The squared terms cancel out:

$$
= 3 \left[ 14\sqrt{4-x^2} \right] = 42\sqrt{4-x^2}
$$

**Outer Integration (with respect to $x$):**
Substitute the result back:

$$
I = \int_{-2}^2 42\sqrt{4-x^2} \, dx
$$

Use the standard integral formula:

$$
\int \sqrt{a^2 - x^2} \, dx = \frac{x}{2}\sqrt{a^2 - x^2} + \frac{a^2}{2}\sin^{-1}\left(\frac{x}{a}\right)
$$

. Here $a = 2$, so

$$
a^2 = 4.
$$

$$
I = 42 \left[ \frac{x}{2}\sqrt{4-x^2} + 2\sin^{-1}\left(\frac{x}{2}\right) \right]_{-2}^2
$$

When evaluating at $x=2$ and $x=-2$, the $\sqrt{4-x^2}$ term becomes $0$.

$$
= 42 \left[ \left( 0 + 2\sin^{-1}(1) \right) - \left( 0 + 2\sin^{-1}(-1) \right) \right]
$$

Since

$$
\sin^{-1}(1) = \frac{\pi}{2}
$$

 and

$$
\sin^{-1}(-1) = -\frac{\pi}{2}:
$$

$$
= 42 \left[ 2\left(\frac{\pi}{2}\right) - 2\left(-\frac{\pi}{2}\right) \right] = 42 [\pi - (-\pi)] = 42(2\pi) = 84\pi
$$

Final Answer: **$84\pi$**

---

## Key Takeaways
*   **Closed Surfaces:** When evaluating a surface integral over a closed shape like a cube, you must evaluate the integral over each individual face and sum the results. The normal vector $\hat{\mathbf{n}}$ must *always* point outward from the enclosed volume.
*   **Volume Integration:** To perform a volume integral over a symmetric solid like a cylinder, start by identifying the constant height bounds for $z$. Then, project the solid onto the $xy$-plane to determine the limits for $x$ and $y$, which often involves circle boundaries.
*   **Sequential Integration:** Always integrate variables with functional limits (like $y = f(x)$) before variables with constant limits.

## What Comes Next
With a firm understanding of Line, Surface, and Volume Integrals, we are now fully equipped to tackle the monumental theorems of Vector Calculus: **Gauss' Divergence Theorem**, **Stokes' Theorem**, and **Green's Theorem**.

---

**Navigation**
[< Previous Lecture](08_Surface_Integral_Part2.md) | [Index](README.md) | [Next Lecture >](10_Stokes_Theorem_Part1.md)
