<!-- Page 081 -->
### Angle between two functions

**Inner product of two functions:**

$$
\langle f, g \rangle = \int_{a}^{b} f(x)g(x) \, dx
$$

where $f$ and $g$ are defined over $[a, b]$.

**Example:**
Let $f(x) = \sin x$ and $g(x) = \cos x$ defined on

$$
[-\frac{\pi}{2}, \frac{\pi}{2}]
$$

.

$$
\langle \sin x, \cos x \rangle = \int_{-\pi/2}^{\pi/2} \sin x \cos x \, dx = 0
$$

(দুইটার মধ্যবর্তী কোণ $90^\circ$)

$$
\langle 1, \sin x \rangle = \int_{-\pi/2}^{\pi/2} 1 \cdot \sin x \, dx = 0
$$

($1$ এবং $\sin x$ এর মধ্যবর্তী কোণ $90^\circ$)

**Fourier basis:**

$$
\lbrace 1, \sin x, \cos x, \sin 2x, \cos 2x, \dots\rbrace
$$

(এর মধ্যে যেকোনো দুইটির মধ্যবর্তী কোণ $90^\circ$)

---

**# Show that $\lbrace(1, 0, 0), (0, 1, 0), (0, 0, 1)\rbrace$ forms an orthonormal basis of $\mathbb{R}^3$.**

*Proof:*
Let,
- $e_1 = (1, 0, 0)$
- $e_2 = (0, 1, 0)$
- $e_3 = (0, 0, 1)$

**Norms of vectors:**
- $\|e_1\| = \sqrt{1^2 + 0^2 + 0^2} = 1$
- $\|e_2\| = \sqrt{0^2 + 1^2 + 0^2} = 1$
- $\|e_3\| = \sqrt{0^2 + 0^2 + 1^2} = 1$

<!-- Page 082 -->
**Angles between vectors:**
-

$$
\cos\theta_{12} = \frac{\langle e_1, e_2 \rangle}{\|e_1\| \|e_2\|} = \frac{0}{1 \cdot 1} = 0 \Rightarrow \theta_{12} = 90^\circ
$$

-

$$
\cos\theta_{23} = \frac{\langle e_2, e_3 \rangle}{\|e_2\| \|e_3\|} = \frac{0}{1 \cdot 1} = 0 \Rightarrow \theta_{23} = 90^\circ
$$

- Similarly, the angle between $e_1$ and $e_3$ is also $90^\circ$.

Since the vectors are mutually orthogonal and each has a unit norm, the basis is orthonormal.
Therefore, $\lbrace(1, 0, 0), (0, 1, 0), (0, 0, 1)\rbrace$ forms an orthonormal basis of $\mathbb{R}^3$.

> [!NOTE]
> $\mathbb{R}^n$ এর orthonormal basis: $\lbrace(1, 0, \dots, 0), (0, 1, \dots, 0), \dots, (0, 0, \dots, 1)\rbrace$ ($n$-tuples).

---

**# Find the distance between $u = (1, 2, 3)$ and $v = (4, 5, 6)$:**

$$
d(u, v) = \|u - v\| = \sqrt{(1-4)^2 + (2-5)^2 + (3-6)^2} = \sqrt{9 + 9 + 9} = \sqrt{27}
$$

(বিয়োগ করে distance বের করতে হয়)

> [!NOTE]
> Origin থেকে distance: $\|u\| = \sqrt{u_1^2 + u_2^2 + \dots + u_n^2}$

---

**# Orthogonal example:**
$u = (2, 1)$, $v = (-1, 2)$
$\mathbb{R}^2$ generate করতে পারবে cause they are orthogonal.

**# Dependent example:**
$u = (1, 1, 1)$, $v = (2, 2, 2)$
They are linearly dependent.

---
*Topics covered in current classes:*
- Echelon form
- System of linear equations
- Matrix form
- Linear mapping
- Symmetric
- Eigenvalues