[← Previous: A15 Volume Integrals](A15_Volume_Integrals.md) | [Index](00_Index.md) | [Next: A17 Stokes' Theorem →](A17_Stokes_Theorem.md)

---

# A16: Green's Theorem

> **Exam Weight**: Tier 1 | **Appeared in**: 2017 (twice), 2019, 2020, 2021, 2023, 2024 | **Typical Marks**: 5–6

Green's theorem relates a line integral around a closed boundary curve $C$ to a double integral over the plane region $R$ bounded by $C$. It is one of the most frequently tested topics.

---

## Statement of the Theorem

Let $R$ be a closed, flat region bounded by a simple, closed curve $C$ in the $xy$-plane. If $P(x,y)$ and $Q(x,y)$ are continuous functions with continuous first-order partial derivatives in $R$, then:

$$
\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy
$$

Here the curve $C$ is traversed in the counterclockwise (positive) direction.

---

## Must-Know Proof (PYQ 2017, 2021, 2024)

You must be able to prove Green's theorem. We split it into two parts:
1. 

$$
\oint_C P dx = -\iint_R \frac{\partial P}{\partial y} dx dy
$$

2. 

$$
\oint_C Q dy = \iint_R \frac{\partial Q}{\partial x} dx dy
$$

**Proof of Part 1**:
Let region $R$ be bounded by curves $y = y_1(x)$ (lower) and $y = y_2(x)$ (upper) from $x=a$ to $x=b$.

Evaluate the double integral:

$$
\iint_R \frac{\partial P}{\partial y} dx dy = \int_a^b \left[ \int_{y_1(x)}^{y_2(x)} \frac{\partial P}{\partial y} dy \right] dx = \int_a^b \left[ P(x, y_2(x)) - P(x, y_1(x)) \right] dx \quad \text{--- (Eq 1)}
$$

Now evaluate the line integral $\oint_C P dx$. The curve $C$ has two paths:
- $C_1$: Along $y_1(x)$ from $a$ to $b$.
- $C_2$: Along $y_2(x)$ from $b$ to $a$.

$$
\oint_C P dx = \int_a^b P(x, y_1(x)) dx + \int_b^a P(x, y_2(x)) dx
$$

Reverse limits on the second integral:

$$
\oint_C P dx = \int_a^b P(x, y_1(x)) dx - \int_a^b P(x, y_2(x)) dx = -\int_a^b \left[ P(x, y_2(x)) - P(x, y_1(x)) \right] dx \quad \text{--- (Eq 2)}
$$

Comparing (Eq 1) and (Eq 2) proves Part 1. By symmetry (bounding $x$ with functions of $y$), Part 2 is proven. Adding them yields Green's theorem.

---

## Worked Example 1: Evaluation (PYQ 2017)

**Problem**: Evaluate

$$
\oint_C (2x + y^2)dx + (3y - 4x)dy
$$

where $C$ is the boundary of the region between $y = x^2$ and $y^2 = x$.

**Solution**:
Identify $P$ and $Q$:
$P = 2x + y^2 \implies \frac{\partial P}{\partial y} = 2y$
$Q = 3y - 4x \implies \frac{\partial Q}{\partial x} = -4$

Apply Green's theorem:

$$
\iint_R (-4 - 2y) dy dx
$$

Limits: The curves intersect at $(0,0)$ and $(1,1)$. For a given $x$, $y$ goes from the lower curve $y=x^2$ to the upper curve $y=\sqrt{x}$.

$$
\int_0^1 \int_{x^2}^{\sqrt{x}} (-4 - 2y) dy dx = \int_0^1 \left[ -4y - y^2 \right]_{x^2}^{\sqrt{x}} dx
$$

$$
= \int_0^1 \left[ (-4\sqrt{x} - x) - (-4x^2 - x^4) \right] dx = \int_0^1 (-4x^{1/2} - x + 4x^2 + x^4) dx
$$

$$
= \left[ -\frac{8}{3}x^{3/2} - \frac{1}{2}x^2 + \frac{4}{3}x^3 + \frac{1}{5}x^5 \right]_0^1 = -\frac{8}{3} - \frac{1}{2} + \frac{4}{3} + \frac{1}{5} = -\frac{49}{30}
$$

---

## Worked Example 2: Verification (PYQ 2020, 2023)

**Problem**: Verify Green's theorem for $\oint_C (xy + y^2)dx + x^2 dy$ where $C$ is bounded by $y = x$ and $y = x^2$.

**Solution**:

**Step 1: Evaluate via Double Integral (Green's Theorem)**
$P = xy + y^2 \implies \frac{\partial P}{\partial y} = x + 2y$
$Q = x^2 \implies \frac{\partial Q}{\partial x} = 2x$

$$
\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 2x - (x + 2y) = x - 2y
$$

Limits: $x$ from 0 to 1, $y$ from $x^2$ to $x$.

$$
\int_0^1 \int_{x^2}^x (x - 2y) dy dx = \int_0^1 \left[ xy - y^2 \right]_{x^2}^x dx = \int_0^1 (0 - (x^3 - x^4)) dx
$$

$$
= \int_0^1 (x^4 - x^3) dx = \left[ \frac{x^5}{5} - \frac{x^4}{4} \right]_0^1 = \frac{1}{5} - \frac{1}{4} = -\frac{1}{20}
$$

**Step 2: Evaluate via Line Integral**
Path 1 ($y = x^2, dy = 2xdx$ from 0 to 1):

$$
\int_0^1 \left[ (x^3 + x^4)dx + x^2(2x dx) \right] = \int_0^1 (3x^3 + x^4) dx = \left[ \frac{3}{4}x^4 + \frac{x^5}{5} \right]_0^1 = \frac{19}{20}
$$

Path 2 ($y = x, dy = dx$ from 1 to 0):

$$
\int_1^0 (x^2 + x^2)dx + x^2 dx = \int_1^0 3x^2 dx = [x^3]_1^0 = -1
$$

Total line integral = $\frac{19}{20} - 1 = -\frac{1}{20}$.

Since both equal $-\frac{1}{20}$, the theorem is verified.

---

## Exam Patterns

- "Verify Green's theorem" means you must compute BOTH the line integral (summing along all paths) and the double integral independently to show they match. This takes time, be careful with signs.
- The proof of Green's theorem is a high-value question. Memorize the algebraic steps for Part 1.
- Sometimes evaluating the double integral just yields the Area of the region (e.g., if $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = -1$). Don't overcomplicate it if it's a known shape like a triangle.

---

[← Previous: A15 Volume Integrals](A15_Volume_Integrals.md) | [Index](00_Index.md) | [Next: A17 Stokes' Theorem →](A17_Stokes_Theorem.md)
