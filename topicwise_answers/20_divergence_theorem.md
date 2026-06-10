# Topic 20: Divergence Theorem

This file contains the organized questions and answers for **Divergence Theorem**, priority ranked as **Priority 20** based on frequency and exam weight.

---

## Q1 (06)

Verify the divergence theorem for $\bar{A} = 4x\hat{i} - 2y^2\hat{j} + z^2\hat{k}$ taken over the region bounded by 

$$
x^2 + y^2 = 4, \quad z = 0, \quad z = 3
$$

.

| | |
|---|---|
| **ID** | PYQ-2018-3b | PYQ-2021-4b |
| **Appeared in** | 2018 Q3(b) [06 marks], 2021 Q4(b) [06 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

The divergence theorem states:

$$
\iiint_V \bar{\nabla} \cdot \bar{A} dV = \iint_S \bar{A} \cdot \hat{n} dS
$$

#### 1. Evaluate Volume Integral

Calculate the divergence of $\bar{A}$:

$$
\bar{\nabla} \cdot \bar{A} = \frac{\partial}{\partial x}(4x) + \frac{\partial}{\partial y}(-2y^2) + \frac{\partial}{\partial z}(z^2) = 4 - 4y + 2z
$$

We use cylindrical coordinates: 

$$
x = r\cos\phi, \quad y = r\sin\phi, \quad z = z
$$

, and $dV = r dr d\phi dz$. The limits are:

$$
r \in [0, 2], \quad \phi \in [0, 2\pi], \quad z \in [0, 3]
$$

Set up the integral:

$$
\iiint_V \bar{\nabla} \cdot \bar{A} dV = \int_{z=0}^3 \int_{\phi=0}^{2\pi} \int_{r=0}^2 (4 - 4r\sin\phi + 2z) r dr d\phi dz
$$

Integrate with respect to $\phi$ first:

$$
\int_0^{2\pi} (4r - 4r^2\sin\phi + 2rz) d\phi = \left[ (4r + 2rz)\phi + 4r^2\cos\phi \right]_0^{2\pi} = 2\pi(4r + 2rz)
$$

Now integrate with respect to $r$:

$$
2\pi \int_0^2 (4r + 2rz) dr = 2\pi \left[ 2r^2 + r^2 z \right]_0^2 = 2\pi(8 + 4z)
$$

Now integrate with respect to $z$:

$$
2\pi \int_0^3 (8 + 4z) dz = 2\pi \left[ 8z + 2z^2 \right]_0^3 = 2\pi(24 + 18) = 84\pi
$$

#### 2. Evaluate Surface Integral

The cylinder surface $S$ has three parts:
1.  Top surface $S\_1$ ($z=3$): The normal vector is $\hat{n} = \hat{k}$.
2.  Bottom surface $S\_2$ ($z=0$): The normal vector is $\hat{n} = -\hat{k}$.
3.  Curved wall $S\_3$ ($x^2 + y^2 = 4$): The normal vector is $\hat{n} = \frac{x\hat{i} + y\hat{j}}{2}$.

Evaluate the top surface integral:

$$
\bar{A} \cdot \hat{n} = \bar{A} \cdot \hat{k} = z^2 = 9
$$

$$
\iint_{S_1} \bar{A} \cdot \hat{n} dS = 9 \iint_{S_1} dS = 9 \times \pi(2)^2 = 36\pi
$$

Evaluate the bottom surface integral:

$$
\bar{A} \cdot \hat{n} = \bar{A} \cdot (-\hat{k}) = -z^2 = 0
$$

$$
\iint_{S_2} \bar{A} \cdot \hat{n} dS = 0
$$

Evaluate the curved wall integral:

$$
\bar{A} \cdot \hat{n} = (4x\hat{i} - 2y^2\hat{j} + z^2\hat{k}) \cdot \left( \frac{x\hat{i} + y\hat{j}}{2} \right) = 2x^2 - y^3
$$

We use cylindrical coordinates: 

$$
x = 2\cos\phi, \quad y = 2\sin\phi, \quad dS = 2 d\phi dz
$$

.

$$
\iint_{S_3} \bar{A} \cdot \hat{n} dS = \int_0^3 \int_0^{2\pi} \left[ 2(4\cos^2\phi) - 8\sin^3\phi \right] 2 d\phi dz
$$

We use the standard integral properties: 

$$
\int_0^{2\pi} \cos^2\phi d\phi = \pi
$$

 and 

$$
\int_0^{2\pi} \sin^3\phi d\phi = 0
$$

.

$$
\iint_{S_3} \bar{A} \cdot \hat{n} dS = \int_0^3 16\pi dz = 48\pi
$$

Add the three surface integrals:

$$
\iint_S \bar{A} \cdot \hat{n} dS = 36\pi + 0 + 48\pi = 84\pi
$$

Both the volume and surface integrals equal $84\pi$. The divergence theorem is verified.

---

