# Lecture 08: Vector Calculus - Concept of Surface and Volume Integral (Part 2)

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 08 of 14
> **Video**: https://www.youtube.com/watch?v=cHe58sjHmgg

---

**Navigation**
[< Previous Lecture](07_Surface_Integral_Part1.md) | [Index](README.md) | [Next Lecture >](09_Volume_Integral.md)

---

## Prerequisites
In the previous lecture, we established the formula for Surface Integration

$$
\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS
$$

And solved a problem by projecting the 3D surface onto the $xy$-plane. In this lecture, we will demonstrate that the choice of projection plane does not alter the final result, and we will introduce **Spherical Coordinates** to drastically simplify integration over spherical surfaces.

---

## Solved Problems

### Problem 1 (Revisited): Projection on the-plane
**Question:** If

$$
\mathbf{F} = 6z\hat{\mathbf{i}} - 4\hat{\mathbf{j}} + y\hat{\mathbf{k}},
$$

Evaluate

$$
\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS,
$$

Where $S$ is the portion of the plane $2x + 3y + 6z = 12$ in the first octant.

**Solution:**
In the previous lecture, we projected $S$ onto the $xy$-plane and obtained the answer $8$. Let us now verify this by projecting onto the **$yz$-plane**.

**Step 1: The Unit Normal Vector**
We already calculated $\hat{\mathbf{n}}$:

$$
\hat{\mathbf{n}} = \frac{1}{7}(2\hat{\mathbf{i}} + 3\hat{\mathbf{j}} + 6\hat{\mathbf{k}})
$$

**Step 2: Projection on the $yz$-plane**
When projecting onto the $yz$-plane, the area element is:

$$
dS = \frac{dy \, dz}{|\hat{\mathbf{n}} \cdot \hat{\mathbf{i}}|}
$$

Compute the dot product:

$$
\hat{\mathbf{n}} \cdot \hat{\mathbf{i}} = \frac{2}{7}.
$$

So,

$$
dS = \frac{dy \, dz}{2/7} = \frac{7}{2} dy \, dz.
$$

**Step 3: Establish Limits on the $yz$-plane**
Set $x = 0$ in the plane equation: $3y + 6z = 12 \implies y + 2z = 4$.
This line forms a triangle with the $y$ and $z$ axes.
- $y$ varies from $0$ to $4$
- $z$ varies from $0$ to the line

$$
z = 2 - \frac{y}{2}
$$

**Step 4: Compute the Integrand**
We already know

$$
\mathbf{F} \cdot \hat{\mathbf{n}} = \frac{1}{7}(12z - 12 + 6y).
$$

Because we are integrating with respect to $y$ and $z$, there is no $x$ variable to eliminate. We can use this directly!

**Step 5: Evaluate the Integral**

$$
\iint_S (\mathbf{F} \cdot \hat{\mathbf{n}}) \, dS = \int_0^4 \int_0^{2 - y/2} \frac{1}{7}(12z - 12 + 6y) \left( \frac{7}{2} dz \, dy \right)
$$

Cancel the $7$'s and divide the terms by $2$:

$$
= \int_0^4 \int_0^{2 - y/2} (6z - 6 + 3y) \, dz \, dy
$$

Integrating with respect to $z$ first, then $y$, yields **$8$**. The answer is identical to the $xy$-plane projection.

---

### Problem 2: Surface Integral Over a Sphere
**Question:** Evaluate

$$
\iint_S (yz\hat{\mathbf{i}} + zx\hat{\mathbf{j}} + xy\hat{\mathbf{k}}) \cdot d\mathbf{S},
$$

Where $S$ is the surface of the sphere

$$
x^2 + y^2 + z^2 = 1
$$

in the first octant.

*(Note: $d\mathbf{S}$ in bold implies $\hat{\mathbf{n}} \, dS$)*

**Solution:**
Let

$$
\phi = x^2 + y^2 + z^2 - 1.
$$

The gradient is

$$
\nabla \phi = 2x\hat{\mathbf{i}} + 2y\hat{\mathbf{j}} + 2z\hat{\mathbf{k}}.
$$

The magnitude is

$$
\lvert \nabla \phi \rvert = \sqrt{4(x^2 + y^2 + z^2)} = \sqrt{4(1)} = 2.
$$

Thus, the unit normal vector is:

$$
\hat{\mathbf{n}} = \frac{2x\hat{\mathbf{i}} + 2y\hat{\mathbf{j}} + 2z\hat{\mathbf{k}}}{2} = x\hat{\mathbf{i}} + y\hat{\mathbf{j}} + z\hat{\mathbf{k}}
$$

Compute

$$
\mathbf{F} \cdot \hat{\mathbf{n}}:
$$

$$
(yz\hat{\mathbf{i}} + zx\hat{\mathbf{j}} + xy\hat{\mathbf{k}}) \cdot (x\hat{\mathbf{i}} + y\hat{\mathbf{j}} + z\hat{\mathbf{k}}) = xyz + xyz + xyz = 3xyz
$$

We need to evaluate:

$$
I = \iint_S 3xyz \, dS.
$$

We will solve this using two different methods to demonstrate the power of coordinate systems.

#### Method 1: Cartesian Projection (on-plane)
Project the sphere onto the $xy$-plane. The projection is a quarter circle (since we are in the first octant) bounded by

$$
x^2 + y^2 = 1.
$$

- $x$ varies from $0$ to $1$.
- $y$ varies from $0$ to $\sqrt{1 - x^2}$.

The area element is

$$
dS = \frac{dx \, dy}{\lvert \hat{\mathbf{n}} \cdot \hat{\mathbf{k}} \rvert}.
$$

Since

$$
\hat{\mathbf{n}} \cdot \hat{\mathbf{k}} = z
$$

, we have

$$
dS = \frac{dx \, dy}{z}.
$$

Substitute into the integral:

$$
I = \iint_{S_1} 3xyz \left( \frac{dx \, dy}{z} \right) = 3 \iint_{S_1} xy \, dx \, dy
$$

Notice how beautifully the $z$ term cancels out! Let's evaluate:

$$
I = 3 \int_0^1 \int_0^{\sqrt{1-x^2}} xy \, dy \, dx = 3 \int_0^1 x \left[ \frac{y^2}{2} \right]_0^{\sqrt{1-x^2}} dx
$$

$$
= \frac{3}{2} \int_0^1 x(1 - x^2) \, dx = \frac{3}{2} \int_0^1 (x - x^3) \, dx
$$

$$
= \frac{3}{2} \left[ \frac{x^2}{2} - \frac{x^4}{4} \right]_0^1 = \frac{3}{2} \left( \frac{1}{2} - \frac{1}{4} \right) = \frac{3}{2} \left( \frac{1}{4} \right) = \frac{3}{8}
$$

#### Method 2: Spherical Polar Coordinates
When integrating over a spherical surface, spherical coordinates simplify the process by removing the need for planar projections entirely.
For a unit sphere ($r=1$):
- $x = \sin\theta \cos\phi$
- $y = \sin\theta \sin\phi$
- $z = \cos\theta$
- The area element $dS = \sin\theta \, d\theta \, d\phi$

For the first octant, the angles $\theta$ and $\phi$ both range from $0$ to $\pi/2$.
Substitute these into

$$
I = \iint_S 3xyz \, dS:
$$

$$
I = 3 \int_0^{\pi/2} \int_0^{\pi/2} (\sin\theta \cos\phi)(\sin\theta \sin\phi)(\cos\theta) (\sin\theta \, d\theta \, d\phi)
$$

Group the terms by variable:

$$
I = 3 \int_0^{\pi/2} \int_0^{\pi/2} (\sin^3\theta \cos\theta) (\sin\phi \cos\phi) \, d\theta \, d\phi
$$

Because the limits are constants, we can separate the integral into the product of two single-variable integrals:

$$
I = 3 \left( \int_0^{\pi/2} \sin^3\theta \cos\theta \, d\theta \right) \left( \int_0^{\pi/2} \sin\phi \cos\phi \, d\phi \right)
$$

Using $u$-substitution ($u=\sin\theta, du=\cos\theta d\theta$ and $v=\sin\phi, dv=\cos\phi d\phi$):

$$
I = 3 \left[ \frac{\sin^4\theta}{4} \right]_0^{\pi/2} \left[ \frac{\sin^2\phi}{2} \right]_0^{\pi/2} = 3 \left( \frac{1}{4} \right) \left( \frac{1}{2} \right) = \frac{3}{8}
$$

---

## Key Takeaways
*   **Projection invariance:** Projecting a 3D surface onto the $xy$, $yz$, or $zx$ planes will always yield the same final integral value, provided the limits and $dS$ conversions are done correctly.
*   **Spherical coordinates:** When the surface $S$ is part of a sphere, substituting $x, y, z$ with spherical coordinates and using

$$
dS = r^2\sin\theta \, d\theta \, d\phi
$$

eliminates the need to project the surface. The entire integral simply becomes a double integral over the angles $\theta$ and $\phi$.

## What Comes Next
We will continue this block with Volume Integration, exploring how to compute triple integrals over 3D volumes.

---

**Navigation**
[< Previous Lecture](07_Surface_Integral_Part1.md) | [Index](README.md) | [Next Lecture >](09_Volume_Integral.md)
