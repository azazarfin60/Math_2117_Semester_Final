# Lecture 11: Vector Calculus - Concept of Stokes' Theorem (Part 2)

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 11 of 14
> **Video**: https://www.youtube.com/watch?v=P74t2Ix5NZI

---

**Navigation**
[< Previous Lecture](10_Stokes_Theorem_Part1.md) | [Index](README.md) | [Next Lecture >](12_Gauss_Divergence_Theorem_Part1.md)

---

## Prerequisites
In the previous lecture, we verified Stokes' Theorem

$$
\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} \, dS
$$

For a rectangular boundary on a 2D plane. In this lecture, we will verify the theorem for a circular boundary and, most importantly, for a curved 3D surface (a hemisphere) to show that the theorem holds regardless of the surface geometry.

---

## Solved Problems

### Problem 1: Verifying Stokes' Theorem on a Unit Circle
**Question:** Verify Stokes' theorem for the function

$$
\mathbf{F} = (x + 2y)\hat{\mathbf{i}} + (y + 3x)\hat{\mathbf{j}}
$$

where $C$ is the unit circle in the $xy$-plane.

**Solution:**
A unit circle in the $xy$-plane has the equation

$$
x^2 + y^2 = 1
$$

and lies at $z = 0$.

#### Part 1: Evaluating the Line Integral (LHS)
Since $z = 0$, $dz = 0$. The line integral becomes:

$$
\oint_C \mathbf{F} \cdot d\mathbf{r} = \oint_C \left[ (x + 2y)dx + (y + 3x)dy \right]
$$

To evaluate this around the circular boundary, we convert to parametric coordinates. Let $\phi$ be the angle parameter from $0$ to $2\pi$:
*   $x = \cos\phi \implies dx = -\sin\phi \, d\phi$
*   $y = \sin\phi \implies dy = \cos\phi \, d\phi$

Substitute these into the integral:

$$
\int_0^{2\pi} \left[ (\cos\phi + 2\sin\phi)(-\sin\phi) + (\sin\phi + 3\cos\phi)(\cos\phi) \right] d\phi
$$

$$
= \int_0^{2\pi} \left( -\sin\phi\cos\phi - 2\sin^2\phi + \sin\phi\cos\phi + 3\cos^2\phi \right) d\phi
$$

The $-\sin\phi\cos\phi$ terms cancel:

$$
= \int_0^{2\pi} (3\cos^2\phi - 2\sin^2\phi) \, d\phi
$$

Using the identity

$$
\sin^2\phi = 1 - \cos^2\phi:
$$

$$
= \int_0^{2\pi} \left( 3\cos^2\phi - 2(1 - \cos^2\phi) \right) d\phi = \int_0^{2\pi} (5\cos^2\phi - 2) \, d\phi
$$

Convert using the double angle formula

$$
\cos^2\phi = \frac{1 + \cos 2\phi}{2}:
$$

$$
= \int_0^{2\pi} \left( \frac{5}{2}(1 + \cos 2\phi) - 2 \right) d\phi = \int_0^{2\pi} \left( \frac{1}{2} + \frac{5}{2}\cos 2\phi \right) d\phi
$$

Integrate:

$$
\left[ \frac{\phi}{2} + \frac{5}{4}\sin 2\phi \right]_0^{2\pi} = \left( \frac{2\pi}{2} + 0 \right) - (0 + 0) = \pi
$$

So, LHS $= \pi$.

#### Part 2: Evaluating the Surface Integral (RHS)
We evaluate

$$
\iint_S (\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} \, dS
$$

over the flat unit disk bounded by the circle.
First, compute the curl:

$$
\nabla \times \mathbf{F} = \det
\begin{vmatrix}
\hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
x + 2y & y + 3x & 0
\end{vmatrix} = \hat{\mathbf{k}}\left( \frac{\partial}{\partial x}(y + 3x) - \frac{\partial}{\partial y}(x + 2y) \right) = \hat{\mathbf{k}}(3 - 2) = \hat{\mathbf{k}}
$$

Since the surface is flat in the $xy$-plane, the outward unit normal is

$$
\hat{\mathbf{n}} = \hat{\mathbf{k}}.
$$

$$
(\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} = \hat{\mathbf{k}} \cdot \hat{\mathbf{k}} = 1
$$

The integral becomes:

$$
\iint_S 1 \, dS = \text{Area}(S)
$$

Since $S$ is a unit circle ($r=1$), its area is

$$
\pi r^2 = \pi.
$$

So, RHS $= \pi$.
**LHS = RHS**, hence verified.

---

### Problem 2: Verifying Stokes' Theorem on a Hemisphere
**Question:** Verify Stokes' theorem for

$$
\mathbf{F} = y\hat{\mathbf{i}} + z\hat{\mathbf{j}} + x\hat{\mathbf{k}},
$$

Where $S$ is the upper hemisphere

$$
x^2 + y^2 + z^2 = 1 \text{ for } z \ge 0
$$

, and $C$ is its boundary.

**Solution:**
The surface $S$ is a 3D curved hemisphere dome. The boundary $C$ is the base ring of this dome lying in the $xy$-plane, which is exactly the unit circle

$$
x^2 + y^2 = 1
$$

at $z=0$.

#### Part 1: Evaluating the Line Integral (LHS)
Since the boundary $C$ lies entirely in the $xy$-plane, $z = 0$ and $dz = 0$.
The integral

$$
\oint_C \mathbf{F} \cdot d\mathbf{r} = \oint_C (y \, dx + z \, dy + x \, dz)
$$

simplifies to:

$$
\oint_C y \, dx
$$

Using parametric equations for the unit circle $x = \cos\phi \implies dx = -\sin\phi \, d\phi$, and $y = \sin\phi$:

$$
\int_0^{2\pi} \sin\phi (-\sin\phi) \, d\phi = -\int_0^{2\pi} \sin^2\phi \, d\phi = -\int_0^{2\pi} \frac{1 - \cos 2\phi}{2} \, d\phi
$$

$$
= -\frac{1}{2} \left[ \phi - \frac{\sin 2\phi}{2} \right]_0^{2\pi} = -\frac{1}{2} (2\pi - 0) = -\pi
$$

So, LHS $= -\pi$.

#### Part 2: Evaluating the Surface Integral (RHS)
We evaluate

$$
\iint_S (\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} \, dS
$$

over the **curved hemispherical surface**.
Compute the curl:

$$
\nabla \times \mathbf{F} = \det
\begin{vmatrix}
\hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
y & z & x
\end{vmatrix} = \hat{\mathbf{i}}(0 - 1) - \hat{\mathbf{j}}(1 - 0) + \hat{\mathbf{k}}(0 - 1) = -\hat{\mathbf{i}} - \hat{\mathbf{j}} - \hat{\mathbf{k}}
$$

Find the unit normal vector $\hat{\mathbf{n}}$ for the sphere

$$
g(x,y,z) = x^2 + y^2 + z^2 - 1 = 0:
$$

$$
\nabla g = 2x\hat{\mathbf{i}} + 2y\hat{\mathbf{j}} + 2z\hat{\mathbf{k}} \implies \hat{\mathbf{n}} = \frac{\nabla g}{|\nabla g|} = x\hat{\mathbf{i}} + y\hat{\mathbf{j}} + z\hat{\mathbf{k}}
$$

Compute the dot product:

$$
(\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} = (-\hat{\mathbf{i}} - \hat{\mathbf{j}} - \hat{\mathbf{k}}) \cdot (x\hat{\mathbf{i}} + y\hat{\mathbf{j}} + z\hat{\mathbf{k}}) = -(x + y + z)
$$

We convert this to spherical polar coordinates to integrate over the curved surface ($r=1$):
*   $x = \sin\theta\cos\phi$
*   $y = \sin\theta\sin\phi$
*   $z = \cos\theta$
*   $dS = \sin\theta \, d\theta \, d\phi$
*   Limits: $\phi$ from $0$ to $2\pi$ (full circle), $\theta$ from $0$ to $\pi/2$ (upper hemisphere only).

Set up the integral:

$$
\text{RHS} = \int_0^{2\pi} \int_0^{\pi/2} -(\sin\theta\cos\phi + \sin\theta\sin\phi + \cos\theta) \sin\theta \, d\theta \, d\phi
$$

Integrate with respect to $\phi$ first. Over $[0, 2\pi]$, the integral of $\cos\phi$ is $0$, and the integral of $\sin\phi$ is $0$. The only term that survives is the $\cos\theta$ term:

$$
\int_0^{2\pi} \cos\theta \sin\theta \, d\phi = 2\pi\cos\theta\sin\theta
$$

Now integrate with respect to $\theta$:

$$
-\int_0^{\pi/2} 2\pi\cos\theta\sin\theta \, d\theta = -\pi \int_0^{\pi/2} 2\sin\theta\cos\theta \, d\theta = -\pi \int_0^{\pi/2} \sin 2\theta \, d\theta
$$

$$
= -\pi \left[ -\frac{\cos 2\theta}{2} \right]_0^{\pi/2} = \frac{\pi}{2} (\cos\pi - \cos 0) = \frac{\pi}{2} (-1 - 1) = -\pi
$$

So, RHS $= -\pi$.
**LHS = RHS**, hence verified.

---

### Practice Application
**Question:** Evaluate

$$
\oint_C (xy \, dx + xy^2 \, dy)
$$

taken round the positively oriented square with vertices $(1,0)$, $(0,1)$, $(-1,0)$, and $(0,-1)$ by using Stokes' theorem.

**Solution Approach:**
Instead of evaluating $4$ separate line integrals for the square boundary, we use Stokes' Theorem to evaluate the surface integral:
1.

$$
\mathbf{F} = xy\hat{\mathbf{i}} + xy^2\hat{\mathbf{j}}.
$$

2.

$$
\nabla \times \mathbf{F} = (y^2 - x)\hat{\mathbf{k}}.
$$

3.

$$
\hat{\mathbf{n}} = \hat{\mathbf{k}}
$$

(square lies in $xy$-plane).
4.  Integral: $\iint_S (y^2 - x) \, dx \, dy$.
By symmetry, the $\iint_S x \, dx \, dy$ component over the centered square is $0$. 
The remaining integral

$$
4 \int_0^1 \int_0^{1-x} y^2 \, dy \, dx
$$

evaluates to exactly $\frac{1}{3}$.

## What Comes Next
We have completed our study of Stokes' Theorem. In the next phase, we will move on to the **Gauss Divergence Theorem**, which relates surface integrals to volume integrals.

---

**Navigation**
[< Previous Lecture](10_Stokes_Theorem_Part1.md) | [Index](README.md) | [Next Lecture >](12_Gauss_Divergence_Theorem_Part1.md)
