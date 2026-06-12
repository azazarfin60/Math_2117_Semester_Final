[Index](00_Index.md) | [Next: A02 Dot and Cross Product →](A02_Dot_Product_Cross_Product.md)

---

# A01: Vector Basics and Direction Cosines

> **Exam Weight**: Tier 3 | **Appeared in**: 2019, 2020, 2021, 2023 | **Typical Marks**: 3–4

This section covers the absolute basics of vectors: definitions, unit vectors, and direction cosines. These concepts form the foundation for all subsequent vector calculus operations.

---

## Definitions

- **Scalar Quantity**: A physical quantity that has only magnitude but no direction (e.g., Mass, Temperature, Time).
- **Vector Quantity**: A physical quantity that has both magnitude and direction, and obeys vector addition rules (e.g., Velocity, Force, Acceleration).

A vector field

$$
\vec{V}(x, y) = P(x, y)\hat{i} + Q(x, y)\hat{j}
$$

assigns a vector to every point in space.
- A **source** field (e.g.,

$$
\vec{V} = x\hat{i} + y\hat{j}
$$

) has all vectors pointing radially outward.
- A **sink** field (e.g.,

$$
\vec{V} = -x\hat{i} - y\hat{j}
$$

) has all vectors pointing radially inward.

---

## Unit Vectors and Resultants

The **resultant** of two vectors $\vec{r}_1$ and $\vec{r}_2$ is simply their vector sum:

$$
\vec{R} = \vec{r}_1 + \vec{r}_2.
$$

The **unit vector** parallel to any vector $\vec{R}$ is the vector divided by its magnitude:

$$
\hat{u} = \frac{\vec{R}}{\lvert \vec{R} \rvert}
$$

### Worked Example (PYQ 2020)
**Problem**: Find a unit vector parallel to the resultant of

$$
\vec{r}_1 = 2\hat{i} + 4\hat{j} - 5\hat{k}
$$

 and

$$
\vec{r}_2 = \hat{i} + 2\hat{j} + \hat{k}.
$$

**Solution**:

$$
\vec{R} = \vec{r}_1 + \vec{r}_2 = 3\hat{i} + 6\hat{j} - 4\hat{k}
$$

$$
\lvert \vec{R} \rvert = \sqrt{3^2 + 6^2 + (-4)^2} = \sqrt{9 + 36 + 16} = \sqrt{61}
$$

Unit vector

$$
\hat{u} = \frac{3\hat{i} + 6\hat{j} - 4\hat{k}}{\sqrt{61}}
$$

---

## Direction Cosines

Let a position vector be

$$
\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}
$$

with magnitude

$$
r = \sqrt{x^2 + y^2 + z^2}.
$$

The angles $\alpha, \beta, \gamma$ that the vector makes with the positive $x, y, z$ axes respectively are defined by their **direction cosines**:

$$
\cos\alpha = \frac{x}{r}, \quad \cos\beta = \frac{y}{r}, \quad \cos\gamma = \frac{z}{r}
$$

A fundamental identity is that the sum of their squares is always 1:

$$
\cos^2\alpha + \cos^2\beta + \cos^2\gamma = \frac{x^2}{r^2} + \frac{y^2}{r^2} + \frac{z^2}{r^2} = \frac{x^2 + y^2 + z^2}{r^2} = 1
$$

### Worked Example (PYQ 2019)
**Problem**: Find the acute angles which the line joining $P(1, -3, 2)$ and $Q(3, -5, 1)$ makes with the coordinate axes.
**Solution**:

$$
\vec{PQ} = (3 - 1)\hat{i} + (-5 - (-3))\hat{j} + (1 - 2)\hat{k} = 2\hat{i} - 2\hat{j} - \hat{k}
$$

Magnitude

$$
\lvert \vec{PQ} \rvert = \sqrt{4 + 4 + 1} = 3
$$

Direction cosines:

$$
\cos\alpha = \frac{2}{3} \implies \alpha = \cos^{-1}\left(\frac{2}{3}\right)
$$

$$
\cos\beta = -\frac{2}{3}
$$

. For the acute angle, take the absolute value:

$$
\beta = \cos^{-1}\left(\frac{2}{3}\right)
$$

$$
\cos\gamma = -\frac{1}{3}
$$

. For the acute angle, take the absolute value:

$$
\gamma = \cos^{-1}\left(\frac{1}{3}\right)
$$

---

## Exam Patterns
- Direction cosine questions often ask for the acute angle. If your cosine is negative, drop the minus sign before taking the inverse cosine to find the acute angle relative to that axis line.
- Basic definitions (scalar vs vector) sometimes appear as 1-2 mark theoretical add-ons to larger questions.

---

[Index](00_Index.md) | [Next: A02 Dot and Cross Product →](A02_Dot_Product_Cross_Product.md)
