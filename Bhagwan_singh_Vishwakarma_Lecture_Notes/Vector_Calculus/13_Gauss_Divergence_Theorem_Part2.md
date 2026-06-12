# Lecture 13: Vector Calculus - Concept of Gauss Divergence Theorem (Part 2)

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 13 of 14
> **Video**: https://www.youtube.com/watch?v=IjWYwfuPBKU

---

**Navigation**
[< Previous Lecture](12_Gauss_Divergence_Theorem_Part1.md) | [Index](README.md) | [Next Lecture >](14_Greens_Theorem.md)

---

## Prerequisites
We previously used the Gauss Divergence Theorem

$$
\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS = \iiint_V (\nabla \cdot \mathbf{F}) \, dV
$$

To evaluate surface integrals by converting them into simpler volume integrals. In this lecture, we will perform a full **verification** of the theorem over a composite surface (a cylinder) and explore a neat trick utilizing the center of gravity to solve cone integrals instantly.

---

## Solved Problems

### Problem 1: Verifying Gauss Divergence Theorem on a Cylinder
**Question:** Verify the divergence theorem for

$$
\mathbf{F} = 4x\hat{\mathbf{i}} - 2y^2\hat{\mathbf{j}} + z^2\hat{\mathbf{k}}
$$

taken over the region bounded by $x^2 + y^2 = 4$, $z=0$, and $z=3$.

**Solution:**
The region is a solid cylinder of radius $R=2$ and height $h=3$. To verify the theorem, we must evaluate both the volume integral (RHS) and the surface integral (LHS) and ensure they are equal.

#### Part 1: Evaluating the Volume Integral (RHS)
First, calculate the divergence of $\mathbf{F}$:

$$
\nabla \cdot \mathbf{F} = \frac{\partial}{\partial x}(4x) + \frac{\partial}{\partial y}(-2y^2) + \frac{\partial}{\partial z}(z^2) = 4 - 4y + 2z
$$

The triple integral is

$$
\iiint_V (4 - 4y + 2z) \, dx \, dy \, dz.
$$

The bounds for the cylinder are:
*   $z$ from $0$ to $3$.
*   $y$ from $-\sqrt{4 - x^2}$ to $\sqrt{4 - x^2}$ (from the circular base).
*   $x$ from $-2$ to $2$.

Integrate with respect to $z$:

$$
\int_0^3 (4 - 4y + 2z) \, dz = \left[ 4z - 4yz + z^2 \right]_0^3 = 12 - 12y + 9 = 21 - 12y = 3(7 - 4y)
$$

Integrate with respect to $y$:

$$
3 \int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}} (7 - 4y) \, dy = 3 \left[ 7y - 2y^2 \right]_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}}
$$

Because $y^2$ is an even function, the subtraction of limits causes the $y^2$ terms to cancel out entirely.

$$
= 3 \left( 14\sqrt{4-x^2} \right) = 42\sqrt{4-x^2}
$$

Integrate with respect to $x$:

$$
I_V = \int_{-2}^2 42\sqrt{4-x^2} \, dx
$$

Using the standard integration formula $\int \sqrt{a^2-x^2} \, dx = \frac{x}{2}\sqrt{a^2-x^2} + \frac{a^2}{2}\sin^{-1}\left(\frac{x}{a}\right)$:

$$
I_V = 42 \left[ \frac{x}{2}\sqrt{4-x^2} + \frac{4}{2}\sin^{-1}\left(\frac{x}{2}\right) \right]_{-2}^2
$$

When evaluated at $x = \pm2$, the square root term becomes $0$.

$$
= 42 \left[ 2\sin^{-1}(1) - 2\sin^{-1}(-1) \right] = 42 \left( 2\left(\frac{\pi}{2}\right) - 2\left(-\frac{\pi}{2}\right) \right) = 42(\pi + \pi) = 84\pi
$$

**So, RHS = $84\pi$.**

#### Part 2: Evaluating the Surface Integral (LHS)
The closed surface $S$ consists of $3$ parts: the bottom base ($S_1$), the top base ($S_2$), and the curved lateral surface ($S_3$).

**1. Bottom Base ($S_1$ at $z=0$):**
*   Outward normal: $\hat{\mathbf{n}}_1 = -\hat{\mathbf{k}}$
*   $\mathbf{F} \cdot \hat{\mathbf{n}}_1 = -z^2$.
*   Since $z=0$ on this surface, the integral is exactly $0$.

**2. Top Base ($S_2$ at $z=3$):**
*   Outward normal: $\hat{\mathbf{n}}_2 = \hat{\mathbf{k}}$
*   $\mathbf{F} \cdot \hat{\mathbf{n}}_2 = z^2$.
*   Since $z=3$, the integrand is $3^2 = 9$.
*   The integral is $9 \times \text{Area}(S_2) = 9 \times (\pi \cdot 2^2) = 36\pi$.

**3. Curved Lateral Surface ($S_3$ where $x^2 + y^2 = 4$):**
*   Gradient of the surface $g = x^2 + y^2 - 4 = 0$ is

$$
\nabla g = 2x\hat{\mathbf{i}} + 2y\hat{\mathbf{j}}.
$$

*   Outward normal

$$
\hat{\mathbf{n}}_3 = \frac{2x\hat{\mathbf{i}} + 2y\hat{\mathbf{j}}}{\sqrt{4x^2 + 4y^2}} = \frac{x\hat{\mathbf{i}} + y\hat{\mathbf{j}}}{2}.
$$

*

$$
\mathbf{F} \cdot \hat{\mathbf{n}}_3 = (4x\hat{\mathbf{i}} - 2y^2\hat{\mathbf{j}} + z^2\hat{\mathbf{k}}) \cdot \frac{x\hat{\mathbf{i}} + y\hat{\mathbf{j}}}{2} = 2x^2 - y^3.
$$

*   Convert to cylindrical coordinates: $x = 2\cos\theta, y = 2\sin\theta, dS_3 = R \, d\theta \, dz = 2 \, d\theta \, dz$.
*   Limits: $\theta \in [0, 2\pi]$ and $z \in [0, 3]$.

$$
\int_0^{2\pi} \int_0^3 \left( 2(2\cos\theta)^2 - (2\sin\theta)^3 \right) 2 \, dz \, d\theta = \int_0^{2\pi} \int_0^3 (8\cos^2\theta - 8\sin^3\theta) 2 \, dz \, d\theta
$$

$$
= 48 \int_0^{2\pi} (\cos^2\theta - \sin^3\theta) \, d\theta
$$

Since

$$
\int_0^{2\pi} \sin^3\theta \, d\theta = 0
$$

 over a full period, and

$$
\int_0^{2\pi} \cos^2\theta \, d\theta = \pi:
$$

:

$$
= 48(\pi - 0) = 48\pi
$$

**Total Surface Integral:**
$$I_S = I_{S1} + I_{S2} + I_{S3} = 0 + 36\pi + 48\pi = 84\pi$$
**So, LHS = $84\pi$.**

Since LHS = RHS = $84\pi$, the Gauss Divergence Theorem is fully verified!

---

### Problem 2: Center of Gravity Trick for Cones
**Question:** Evaluate

$$
\iint_S (x\hat{\mathbf{i}} + y\hat{\mathbf{j}} + z^2\hat{\mathbf{k}}) \cdot \hat{\mathbf{n}} \, dS,
$$

Where $S$ is the closed surface bounded by the cone $x^2 + y^2 = z^2$ and the plane $z=1$.

**Solution:**
Using the Divergence Theorem, we convert this to a volume integral.

$$
\nabla \cdot \mathbf{F} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(y) + \frac{\partial}{\partial z}(z^2) = 1 + 1 + 2z = 2(1 + z)
$$

The volume integral is:

$$
\iiint_V 2(1 + z) \, dV = 2 \iiint_V dV + 2 \iiint_V z \, dV
$$

We recognize two geometric properties:
1.  $\iiint_V dV$ is the geometric volume $V$ of the cone.
2.  By definition, the $z$-coordinate of the centroid (center of gravity) is

$$
\bar{z} = \frac{\iiint_V z \, dV}{V}.
$$

Therefore, $\iiint_V z \, dV = V\bar{z}$.

Substitute these in:

$$
2V + 2V\bar{z} = 2V(1 + \bar{z})
$$

Now, we simply use the known geometric formulas for a solid cone:
*   The cone has a height $h = 1$ and a base radius $R = 1$ (since $x^2+y^2=z^2$ at $z=1$).
*   The volume of a cone is $V = \frac{1}{3}\pi R^2 h = \frac{1}{3}\pi (1)^2 (1) = \frac{1}{3}\pi$.
*   The center of gravity of a solid right circular cone lies on its axis at $\bar{z} = \frac{3}{4}h$. Since $h=1$, $\bar{z} = \frac{3}{4}$.

Substitute these known values:

$$
\text{Result} = 2 \left( \frac{1}{3}\pi \right) \left( 1 + \frac{3}{4} \right) = \frac{2}{3}\pi \left( \frac{7}{4} \right) = \frac{7}{6}\pi
$$

> [!TIP]
> If a divergence evaluates to a linear coordinate (like $z$), you can often solve the integral instantly by utilizing the formula $V\bar{z}$, bypassing complex integration setups completely!

## What Comes Next
We have completed our study of the Gauss Divergence Theorem. In the final lecture, we will cover **Green's Theorem**, which relates line integrals to double area integrals in the 2D plane.

---

**Navigation**
[< Previous Lecture](12_Gauss_Divergence_Theorem_Part1.md) | [Index](README.md) | [Next Lecture >](14_Greens_Theorem.md)
