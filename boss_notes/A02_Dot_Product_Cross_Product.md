[← Previous: A01 Vector Basics](A01_Vectors_Basics_Direction_Cosines.md) | [Index](00_Index.md) | [Next: A03 Triple Products →](A03_Triple_Products_Area_Volume.md)

---

# A02: Dot Product and Cross Product

> **Exam Weight**: Tier 2 | **Appeared in**: 2020, 2021, 2023, CT | **Typical Marks**: 3–4

The dot product and cross product are the two fundamental ways to multiply vectors. They have distinct physical interpretations and mathematical properties.

---

## Dot Product (Scalar Product)

**Definition**: $\vec{A} \cdot \vec{B} = \lvert \vec{A} \rvert\lvert \vec{B} \rvert\cos\theta$
- **Output**: A scalar (a number).
- **Physical Significance**: Represents the projection of one vector onto another. It is used to calculate work done by a force ($W = \vec{F} \cdot \vec{d}$).
- **Orthogonality**: If two non-zero vectors are perpendicular (orthogonal), their dot product is 0.

### Worked Example: Mutually Orthogonal Vectors (CT)
**Problem**: Show that

$$
\vec{A} = \frac{1}{3}(2\hat{i} - 2\hat{j} + \hat{k}),
$$

$$
\vec{B} = \frac{1}{3}(\hat{i} + 2\hat{j} + 2\hat{k}),
$$

$$
\vec{C} = \frac{1}{3}(2\hat{i} + \hat{j} - 2\hat{k})
$$

are mutually orthogonal unit vectors.
**Solution**:
Magnitude check for unit vectors:
$\lvert \vec{A} \rvert = \sqrt{(2/3)^2 + (-2/3)^2 + (1/3)^2} = \sqrt{9/9} = 1$. (Same applies for $\vec{B}$ and $\vec{C}$).
Dot product check for orthogonality:
$\vec{A} \cdot \vec{B} = \frac{1}{9}(2(1) + (-2)(2) + 1(2)) = \frac{1}{9}(2 - 4 + 2) = 0$.
$\vec{B} \cdot \vec{C} = \frac{1}{9}(1(2) + 2(1) + 2(-2)) = \frac{1}{9}(2 + 2 - 4) = 0$.
$\vec{C} \cdot \vec{A} = \frac{1}{9}(2(2) + 1(-2) + (-2)(1)) = \frac{1}{9}(4 - 2 - 2) = 0$.
Since all magnitudes are 1 and all dot products are 0, they are mutually orthogonal unit vectors.

---

## Cross Product (Vector Product)

**Definition**: $\vec{A} \times \vec{B} = \lvert \vec{A} \rvert\lvert \vec{B} \rvert\sin\theta \, \hat{n}$
- **Output**: A new vector, perpendicular to the plane containing $\vec{A}$ and $\vec{B}$.
- **Physical Significance**: Represents a rotational effect. It is used to calculate torque ($\vec{\tau} = \vec{r} \times \vec{F}$). The magnitude equals the area of the parallelogram formed by the two vectors.
- **Parallelism**: If two non-zero vectors are parallel, their cross product is $\vec{0}$.

### Worked Example: Finding Perpendicular Vectors (PYQ 2020)
**Problem**: Find a vector of magnitude 5 perpendicular to both

$$
\vec{A} = 2\hat{i} + \hat{j} - 3\hat{k}
$$

 and

$$
\vec{B} = \hat{i} - 2\hat{j} + \hat{k}.
$$

**Solution**:
The cross product yields a perpendicular vector:

$$
\vec{A} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -3 \\ 1 & -2 & 1 \end{vmatrix} = \hat{i}(1 - 6) - \hat{j}(2 - (-3)) + \hat{k}(-4 - 1) = -5\hat{i} - 5\hat{j} - 5\hat{k}
$$

Simplify to a base direction vector

$$
\vec{v} = \hat{i} + \hat{j} + \hat{k}.
$$

Find the unit normal vector $\hat{n}$:

$$
\hat{n} = \pm \frac{\hat{i} + \hat{j} + \hat{k}}{\sqrt{1^2 + 1^2 + 1^2}} = \pm \frac{\hat{i} + \hat{j} + \hat{k}}{\sqrt{3}}
$$

Multiply by the desired magnitude 5:

$$
\vec{P} = \pm \frac{5}{\sqrt{3}}(\hat{i} + \hat{j} + \hat{k})
$$

---

## Exam Patterns
- When asked to find a vector perpendicular to two other vectors, always use the cross product, normalize it to a unit vector, and then multiply by the requested magnitude. Include the $\pm$ sign to show both possible directions.
- "Show vectors are orthogonal" simply means proving their dot product is zero.

---

[← Previous: A01 Vector Basics](A01_Vectors_Basics_Direction_Cosines.md) | [Index](00_Index.md) | [Next: A03 Triple Products →](A03_Triple_Products_Area_Volume.md)
