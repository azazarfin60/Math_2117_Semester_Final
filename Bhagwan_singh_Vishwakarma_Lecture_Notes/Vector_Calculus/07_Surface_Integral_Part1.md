# Lecture 07: Vector Calculus - Concept of Surface and Volume Integral (Part 1)

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 07 of 14
> **Video**: https://www.youtube.com/watch?v=5BLWsAa3Yr8

---

**Navigation**
[< Previous Lecture](06_Line_Integration.md) | [Index](README.md) | [Next Lecture >](08_Surface_Integral_Part2.md)


---

## Prerequisites
We have completed our study of Line Integrals, which involve integrating a vector field over a one-dimensional path (a curve). Now, we extend our integration to two dimensions (Surface Integrals) and three dimensions (Volume Integrals).

---

## 1. Surface Integration

A surface integral computes the integral of a vector field over a 3D surface $S$. It is equivalent to a double integral in standard calculus, as it requires two parameters to define a surface.

The surface integral of a vector point function $\mathbf{F}$ over a surface $S$ is given by:

$$
\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS
$$

Where:
-   **$\mathbf{F}$** is the vector field.
-   **$\hat{\mathbf{n}}$** is the unit normal vector pointing outward from the surface $S$.
-   **$dS$** is the infinitesimal surface area element of $S$.

### Finding the Unit Normal Vector
If the surface $S$ is represented by a scalar equation $\phi(x, y, z) = c$, then the unit normal vector $\hat{\mathbf{n}}$ is simply the normalized gradient:

$$
\hat{\mathbf{n}} = \frac{\nabla \phi}{|\nabla \phi|}
$$

### Projecting the Surface
Because the surface $S$ exists in 3D space, we cannot integrate $dS$ directly. We must **project** the 3D surface onto one of the 2D coordinate planes ($xy$, $yz$, or $zx$). This allows us to establish the limits of integration for the two projected variables.

The formulas for the projected area element $dS$ are:
1.  **Projection on $xy$-plane**: $dS = \frac{dx \, dy}{\lvert \hat{\mathbf{n}} \cdot \hat{\mathbf{k}} \rvert}$
2.  **Projection on $yz$-plane**: $dS = \frac{dy \, dz}{\lvert \hat{\mathbf{n}} \cdot \hat{\mathbf{i}} \rvert}$
3.  **Projection on $zx$-plane**: $dS = \frac{dz \, dx}{\lvert \hat{\mathbf{n}} \cdot \hat{\mathbf{j}} \rvert}$

*Rule of thumb: The denominator is the dot product of $\hat{\mathbf{n}}$ and the unit vector of the axis orthogonal to the projection plane.*

---

## 2. Volume Integration

Volume integration extends the concept to a three-dimensional region (or volume) $V$. It is represented as a triple integral:

$$
\iiint_V \mathbf{F} \, dV
$$

In Cartesian coordinates, the volume element is simply $dV = dx \, dy \, dz$. 

### Setting Limits
To find the bounds for volume integration:
1.  Project the 3D volume onto a 2D coordinate plane (e.g., the $xy$-plane). The boundary of this 2D shadow provides the limits for two variables (e.g., $x$ and $y$).
2.  The limits for the third variable (e.g., $z$) are defined by the "floor" and "ceiling" surfaces of the volume along that axis.

---

## Solved Problems

### Problem 1: Surface Integral Over a Plane
**Question:** If $\mathbf{F} = 6z\hat{\mathbf{i}} - 4\hat{\mathbf{j}} + y\hat{\mathbf{k}}$, evaluate $\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS$, where $S$ is the portion of the plane $2x + 3y + 6z = 12$ which lies in the first octant.

**Solution:**
**Step 1: Understand the Surface $S$**
The plane $2x + 3y + 6z = 12$ in the first octant ($x,y,z > 0$) forms a triangular surface.
We find its intercepts by setting two variables to 0:
-   $x$-intercept: $(6, 0, 0)$
-   $y$-intercept: $(0, 4, 0)$
-   $z$-intercept: $(0, 0, 2)$

**Step 2: Find the Unit Normal $\hat{\mathbf{n}}$**
Let $\phi = 2x + 3y + 6z - 12$. The gradient is:

$$
\nabla \phi = 2\hat{\mathbf{i}} + 3\hat{\mathbf{j}} + 6\hat{\mathbf{k}}
$$

The magnitude is $\sqrt{2^2 + 3^2 + 6^2} = \sqrt{49} = 7$.

$$
\hat{\mathbf{n}} = \frac{2\hat{\mathbf{i}} + 3\hat{\mathbf{j}} + 6\hat{\mathbf{k}}}{7} = \frac{1}{7}(2\hat{\mathbf{i}} + 3\hat{\mathbf{j}} + 6\hat{\mathbf{k}})
$$

**Step 3: Choose a Projection Plane**
We project the surface $S$ onto the **$xy$-plane**. Let's call this 2D projected region $S_1$.
The projection formula for $dS$ on the $xy$-plane is $dS = \frac{dx \, dy}{\lvert \hat{\mathbf{n}} \cdot \hat{\mathbf{k}} \rvert}$.

$$
\hat{\mathbf{n}} \cdot \hat{\mathbf{k}} = \frac{1}{7}(2\hat{\mathbf{i}} + 3\hat{\mathbf{j}} + 6\hat{\mathbf{k}}) \cdot \hat{\mathbf{k}} = \frac{6}{7}
$$

Thus, $dS = \frac{dx \, dy}{6/7} = \frac{7}{6} dx \, dy$.

**Step 4: Establish Limits of Integration for $S_1$**
On the $xy$-plane ($z=0$), the plane equation becomes $2x + 3y = 12$. This line bounds the triangular region $S_1$.
-   $x$ varies from $0$ to $6$.
-   For a given $x$, $y$ varies from $0$ to the line $y = \frac{12 - 2x}{3}$.

**Step 5: Compute $\mathbf{F} \cdot \hat{\mathbf{n}}$**

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = (6z\hat{\mathbf{i}} - 4\hat{\mathbf{j}} + y\hat{\mathbf{k}}) \cdot \frac{1}{7}(2\hat{\mathbf{i}} + 3\hat{\mathbf{j}} + 6\hat{\mathbf{k}}) = \frac{1}{7}(12z - 12 + 6y)
$$

Because we are integrating with respect to $x$ and $y$, we must eliminate $z$. Using the plane equation $6z = 12 - 2x - 3y$, we substitute $12z$:

$$
12z = 24 - 4x - 6y
$$

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = \frac{1}{7}(24 - 4x - 6y - 12 + 6y) = \frac{1}{7}(12 - 4x)
$$

**Step 6: Evaluate the Double Integral**
Substitute everything into the integral:

$$
\iint_{S_1} \left[ \frac{1}{7}(12 - 4x) \right] \left( \frac{7}{6} dx \, dy \right) = \int_0^6 \int_0^{\frac{12-2x}{3}} \frac{1}{6}(12 - 4x) \, dy \, dx
$$

$$
= \int_0^6 \int_0^{\frac{12-2x}{3}} \left(2 - \frac{2}{3}x\right) \, dy \, dx = \frac{1}{3} \int_0^6 \int_0^{\frac{12-2x}{3}} (6 - 2x) \, dy \, dx
$$

Integrate with respect to $y$ first:

$$
\frac{1}{3} \int_0^6 (6 - 2x) \left[ y \right]_0^{\frac{12-2x}{3}} dx = \frac{1}{3} \int_0^6 (6 - 2x) \left(\frac{12 - 2x}{3}\right) dx
$$

$$
= \frac{1}{9} \int_0^6 4(3 - x)(6 - x) \, dx = \frac{4}{9} \int_0^6 (18 - 9x + x^2) \, dx
$$

Integrate with respect to $x$:

$$
\frac{4}{9} \left[ 18x - \frac{9x^2}{2} + \frac{x^3}{3} \right]_0^6 = \frac{4}{9} \left[ 108 - 162 + 72 \right] = \frac{4}{9} [18] = 8
$$

Final Answer: **8**

---

## Key Takeaways
*   Surface integrals require calculating a unit normal vector ($\hat{\mathbf{n}} = \nabla\phi / \lvert \nabla\phi \rvert$) and computing the dot product $\mathbf{F} \cdot \hat{\mathbf{n}}$.
*   To evaluate the integral, you **must project the 3D surface onto a 2D plane**. This transforms the $dS$ element and defines the integration limits.
*   Once projected, ensure the entire integrand ($\mathbf{F} \cdot \hat{\mathbf{n}}$) is expressed strictly in terms of the two projected variables.

## What Comes Next
We will continue practicing surface integrals in the next lecture by solving more problems and proving that calculating the surface integral via different projection planes yields the exact same result.

---

**Navigation**
[< Previous Lecture](06_Line_Integration.md) | [Index](README.md) | [Next Lecture >](08_Surface_Integral_Part2.md)
