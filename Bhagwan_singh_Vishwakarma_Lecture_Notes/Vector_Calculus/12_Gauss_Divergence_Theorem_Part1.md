# Lecture 12: Concept of Gauss Divergence Theorem (Part 1)

> **Series**: Vector Calculus
> **Lecture**: 12 of 14
> **Video**: https://www.youtube.com/watch?v=vZas0kR9cUY

---

**Navigation**
[< Previous Lecture](11_Stokes_Theorem_Part2.md) | [Index](README.md) | [Next Lecture >](13_Gauss_Divergence_Theorem_Part2.md)

---

## Prerequisites
We have already seen how **Stokes' Theorem** relates line integration to surface integration. Now, we introduce the **Gauss Divergence Theorem**, which provides a profound connection between **surface integrals** and **volume integrals**. A strong foundation in double and triple integration bounds is essential here.

---

## Gauss Divergence Theorem

### Statement
Let $V$ be a solid volume bounded by a closed surface $S$. If $\mathbf{F}$ is a continuously differentiable vector point function, then the surface integral of $\mathbf{F}$ over $S$ is equal to the volume integral of the divergence of $\mathbf{F}$ over $V$:
$$
\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS = \iiint_V (\nabla \cdot \mathbf{F}) \, dV
$$
Where:
*   $\iint_S$ denotes the surface integral over the *closed* surface $S$.
*   $\iiint_V$ denotes the triple (volume) integral over the enclosed space $V$.
*   $\hat{\mathbf{n}}$ is the outward-pointing unit normal vector to the surface $S$.
*   $\nabla \cdot \mathbf{F}$ is the divergence (a scalar) of the vector field $\mathbf{F}$.

### Why is this Theorem Useful?
Evaluating a surface integral over a fully closed shape (like a cube, sphere, or tetrahedron) requires calculating the flux across every single bounding face separately. The Gauss Divergence Theorem allows us to bypass this tedious calculation entirely. Instead of integrating over multiple external surfaces, we compute the divergence of the vector field and evaluate a single triple integral over the solid interior volume.

---

## Solved Problems

### Problem 1: Integration over a Tetrahedron
**Question:** Evaluate the surface integral $\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS$, where $\mathbf{F} = (x + y^2)\hat{\mathbf{i}} - 2x\hat{\mathbf{j}} + 2yz\hat{\mathbf{k}}$, and $S$ is the closed surface bounded by the coordinate planes ($x=0, y=0, z=0$) and the plane $2x + y + 2z = 6$.

**Solution:**
The surface $S$ is a tetrahedron. Evaluating this directly would require $4$ separate double integrals (one for each of the $4$ triangular faces). Instead, we will use the Gauss Divergence Theorem to evaluate a single volume integral over the interior space $V$.

**Step 1: Compute the Divergence**
$$
\nabla \cdot \mathbf{F} = \frac{\partial}{\partial x}(x + y^2) + \frac{\partial}{\partial y}(-2x) + \frac{\partial}{\partial z}(2yz) = 1 + 0 + 2y = 1 + 2y
$$
The volume integral is: $\iiint_V (1 + 2y) \, dV$.

**Step 2: Determine Limits of Integration**
We find the intercepts of the plane $2x + y + 2z = 6$:
*   $x$-intercept (set $y=z=0$): $2x = 6 \implies x = 3$
*   $y$-intercept (set $x=z=0$): $y = 6$
*   $z$-intercept (set $x=y=0$): $2z = 6 \implies z = 3$

The limits are established by working from the top down to the base projection:
1.  **$z$-limits:** From the floor ($z=0$) to the slanted roof ($z = \frac{6 - 2x - y}{2}$).
2.  **$y$-limits:** On the floor projection ($z=0$), the plane becomes the line $2x + y = 6 \implies y = 6 - 2x$. So, $y$ goes from $0$ to $6 - 2x$.
3.  **$x$-limits:** From the origin to the $x$-intercept ($x=3$). So, $x$ goes from $0$ to $3$.

**Step 3: Evaluate the Triple Integral**
$$
I = \int_0^3 \int_0^{6-2x} \int_0^{\frac{6-2x-y}{2}} (1 + 2y) \, dz \, dy \, dx
$$

**Inner Integral (w.r.t $z$):**
$$
\int_0^{\frac{6-2x-y}{2}} (1 + 2y) \, dz = (1 + 2y) [z]_0^{\frac{6-2x-y}{2}} = (1 + 2y) \left( \frac{6 - 2x - y}{2} \right)
$$
Expanding this expression gives:
$$
\frac{1}{2} (6 - 2x - y + 12y - 4xy - 2y^2) = \frac{1}{2} (6 - 2x + 11y - 4xy - 2y^2)
$$

**Middle Integral (w.r.t $y$):**
$$
\frac{1}{2} \int_0^{6-2x} (6 - 2x + 11y - 4xy - 2y^2) \, dy = \frac{1}{2} \left[ (6 - 2x)y + \frac{11}{2}y^2 - 2xy^2 - \frac{2}{3}y^3 \right]_0^{6-2x}
$$
Substitute the upper limit $y = 6 - 2x$:
$$
= \frac{1}{2} \left[ (6 - 2x)^2 + \frac{11}{2}(6 - 2x)^2 - 2x(6 - 2x)^2 - \frac{2}{3}(6 - 2x)^3 \right]
$$
Factor out $(6 - 2x)^2$:
$$
= \frac{1}{2} (6 - 2x)^2 \left( 1 + \frac{11}{2} - 2x - \frac{2}{3}(6 - 2x) \right) = \dots \text{(after algebraic expansion)} = -\frac{4}{3}x^3 + 13x^2 - 42x + 45
$$

**Outer Integral (w.r.t $x$):**
$$
\int_0^3 \left(-\frac{4}{3}x^3 + 13x^2 - 42x + 45\right) dx = \left[ -\frac{1}{3}x^4 + \frac{13}{3}x^3 - 21x^2 + 45x \right]_0^3
$$
$$
= -\frac{1}{3}(81) + \frac{13}{3}(27) - 21(9) + 45(3) = -27 + 117 - 189 + 135 = 36
$$

> [!NOTE]
> **Correction:** The original lecture contained an algebraic expansion error here. It incorrectly simplified the polynomial to $-4x^3$ (missing the division by 3) and subsequently forced a flawed arithmetic addition ($-81 + 117 - 189 + 135$) to arrive at the desired final answer of $36$. The mathematical steps have been corrected above to ensure strict logical integrity.

**Final Answer:** $36$

---

### Problem 2: Integration over a Sphere
**Question:** Evaluate the surface integral $\iint_S \mathbf{F} \cdot \hat{\mathbf{n}} \, dS$, where $\mathbf{F} = x\hat{\mathbf{i}} - y\hat{\mathbf{j}} + 2z\hat{\mathbf{k}}$, and $S$ is the boundary of the sphere $x^2 + y^2 + (z - 1)^2 = 1$.

**Solution:**
We use Gauss Divergence Theorem to convert this to a volume integral.

**Step 1: Compute Divergence**
$$
\nabla \cdot \mathbf{F} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(-y) + \frac{\partial}{\partial z}(2z) = 1 - 1 + 2 = 2
$$

**Step 2: Evaluate the Volume Integral**
The integral over the spherical volume $V$ becomes:
$$
\iiint_V (\nabla \cdot \mathbf{F}) \, dV = \iiint_V 2 \, dV = 2 \iiint_V dV
$$
Notice that $\iiint_V dV$ is simply the geometric volume of the solid region $V$.
The region is a sphere with equation $x^2 + y^2 + (z - 1)^2 = 1$, which has a radius $R = 1$ and is centered at $(0,0,1)$.

The geometric volume of a sphere is $V = \frac{4}{3}\pi R^3$. For $R = 1$:
$$
V = \frac{4}{3}\pi (1)^3 = \frac{4}{3}\pi
$$
Substitute this back into the expression:
$$
2 \iiint_V dV = 2(V) = 2 \left( \frac{4}{3}\pi \right) = \frac{8}{3}\pi
$$

**Final Answer:** $\frac{8}{3}\pi$

> [!NOTE]
> This problem demonstrates a massive shortcut: if the divergence $\nabla \cdot \mathbf{F}$ is a constant scalar, you do not need to set up complex integration bounds. You can simply multiply that constant by the known geometric volume formula of the enclosed solid!

## What Comes Next
We will continue practicing the Gauss Divergence Theorem in the next lecture, addressing more advanced verification problems.

---

**Navigation**
[< Previous Lecture](11_Stokes_Theorem_Part2.md) | [Index](README.md) | [Next Lecture >](13_Gauss_Divergence_Theorem_Part2.md)
