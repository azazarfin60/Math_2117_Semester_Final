[← Previous: A17 Stokes' Theorem](A17_Stokes_Theorem.md) | [Index](00_Index.md) | [Next: A01 Vectors Basics →](A01_Vectors_Basics.md)

---

# A18: Gauss Divergence Theorem

> **Exam Weight**: Tier 1 | **Appeared in**: 2018, 2021 | **Typical Marks**: 6

The Gauss Divergence Theorem relates the flux of a vector field across a closed surface to the volume integral of the divergence inside that surface. It is extremely powerful for converting difficult surface integrals into simple volume integrals.

---

## Statement of the Theorem

Let $V$ be a volume bounded by a closed surface $S$. If $\vec{A}$ is a vector field with continuous first-order partial derivatives, then:

$$
\iint_S \vec{A} \cdot \hat{n} dS = \iiint_V (\nabla \cdot \vec{A}) dV
$$

where $\hat{n}$ is the unit outward normal vector to the surface $S$.

*(Note: The theorem requires a strictly CLOSED surface. If a surface is open, like a hemisphere without its base, you must add the base to close it before applying the theorem).*

---

## Worked Example: Verification (PYQ 2018, 2021)

**Problem**: Verify the divergence theorem for

$$
\vec{A} = 4x\hat{i} - 2y^2\hat{j} + z^2\hat{k}
$$

taken over the region bounded by

$$
x^2 + y^2 = 4, z = 0, z = 3.
$$

**Solution**:

**Step 1: Evaluate the Volume Integral**
Calculate Divergence:

$$
\nabla \cdot \vec{A} = \frac{\partial}{\partial x}(4x) + \frac{\partial}{\partial y}(-2y^2) + \frac{\partial}{\partial z}(z^2) = 4 - 4y + 2z
$$

Set up cylindrical coordinates ($x = r\cos\phi, y = r\sin\phi, z = z, dV = r dr d\phi dz$):
Limits: $r \in [0, 2]$, $\phi \in [0, 2\pi]$, $z \in [0, 3]$.

$$
\iiint_V (\nabla \cdot \vec{A}) dV = \int_0^3 \int_0^{2\pi} \int_0^2 (4 - 4r\sin\phi + 2z) r \, dr \, d\phi \, dz
$$

Integrate w.r.t $\phi$ first (the $\sin\phi$ term evaluates to 0 over $2\pi$):

$$
\int_0^{2\pi} (4r - 4r^2\sin\phi + 2rz) d\phi = 2\pi(4r + 2rz)
$$

Integrate w.r.t $r$:

$$
2\pi \int_0^2 (4r + 2rz) dr = 2\pi [2r^2 + r^2 z]_0^2 = 2\pi(8 + 4z)
$$

Integrate w.r.t $z$:

$$
2\pi \int_0^3 (8 + 4z) dz = 2\pi [8z + 2z^2]_0^3 = 2\pi(24 + 18) = 84\pi
$$

**Step 2: Evaluate the Surface Integral**
The closed cylinder has 3 surfaces: Top ($S_1$), Bottom ($S_2$), and Curved Wall ($S_3$).

- **Top Surface $S_1$ (

$$
z=3, \hat{n}=\hat{k}
$$

)**:

$$
\vec{A} \cdot \hat{k} = z^2 = 3^2 = 9.
$$

  
$$
\iint_{S_1} 9 dS = 9 \times (\text{Area of circle}) = 9 \times \pi(2^2) = 36\pi.
$$

- **Bottom Surface $S_2$ (

$$
z=0, \hat{n}=-\hat{k}
$$

)**:

$$
\vec{A} \cdot (-\hat{k}) = -z^2 = -0^2 = 0.
$$

  
$$
\iint_{S_2} 0 dS = 0.
$$

- **Curved Wall $S_3$

$$
x^2+y^2=4, \hat{n}=\frac{x\hat{i}+y\hat{j}}{2}
$$

**:

$$
\vec{A} \cdot \hat{n} = (4x\hat{i} - 2y^2\hat{j} + z^2\hat{k}) \cdot \left( \frac{x\hat{i} + y\hat{j}}{2} \right) = 2x^2 - y^3.
$$

  In cylindrical ($x=2\cos\phi, y=2\sin\phi, dS = 2 d\phi dz$):

$$
\iint_{S_3} (2x^2 - y^3) dS = \int_0^3 \int_0^{2\pi} \left[ 2(4\cos^2\phi) - 8\sin^3\phi \right] 2 d\phi dz
$$

  We know

$$
\int_0^{2\pi} \cos^2\phi d\phi = \pi
$$

 and

$$
\int_0^{2\pi} \sin^3\phi d\phi = 0.
$$

$$
= \int_0^3 2(8\pi - 0) dz = \int_0^3 16\pi dz = 48\pi
$$

Total Surface Integral = $36\pi + 0 + 48\pi = 84\pi$.

Both integrals equal $84\pi$. The divergence theorem is verified.

---

## The "Big Three" Summary

Vector Calculus revolves around three major integration theorems. Understanding when to use which is critical:

| Theorem | Connects... | Common Use Case |
| :--- | :--- | :--- |
| **Green's** | 1D Closed Line $\iff$ 2D Plane Area | Evaluating planar work integrals. |
| **Stokes'** | 1D Closed Line $\iff$ 3D Open Surface | Evaluating work in 3D space by calculating flux of curl. |
| **Gauss's** | 2D Closed Surface $\iff$ 3D Volume | Evaluating outward flux through a closed solid by integrating divergence. |

---

## Exam Patterns

- Like Green's and Stokes', "verify" means you must compute the volume integral and the surface integral independently.
- The cylinder problem is a classic. Always split the cylinder into top, bottom, and curved surfaces, treating them entirely separately before summing them.
- Cylindrical coordinates ($r, \phi, z$) are absolutely essential here.

---

[← Previous: A17 Stokes' Theorem](A17_Stokes_Theorem.md) | [Index](00_Index.md) | [Next: A01 Vectors Basics →](A01_Vectors_Basics.md)
