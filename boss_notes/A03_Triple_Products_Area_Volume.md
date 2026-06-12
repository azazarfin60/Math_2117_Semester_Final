[← Previous: A02 Dot and Cross Product](A02_Dot_Product_Cross_Product.md) | [Index](00_Index.md) | [Next: A04 Vector Differentiation →](A04_Vector_Differentiation.md)

---

# A03: Area, Volume, and Triple Products

> **Exam Weight**: Tier 2 | **Appeared in**: 2019, 2020, 2021, 2023 | **Typical Marks**: 3–4

Triple products allow you to find volumes of 3D shapes or determine if three vectors lie in the same flat plane (coplanar). Cross products natively provide the area of 2D shapes.

---

## Area of a Triangle

The magnitude of the cross product of two vectors is the area of the parallelogram they form. Therefore, the area of a triangle formed by two edge vectors is half of that:

$$
\text{Area} = \frac{1}{2}\lvert \vec{A} \times \vec{B} \rvert
$$

### Worked Example (PYQ 2021)
**Problem**: Find the area of a triangle with vertices at $P(3, -1, 2)$, $Q(1, -1, -3)$ and $R(4, -3, 1)$.
**Solution**:
Construct two edge vectors originating from the same point $P$:

$$
\vec{PQ} = (1 - 3)\hat{i} + (-1 - (-1))\hat{j} + (-3 - 2)\hat{k} = -2\hat{i} - 5\hat{k}
$$

$$
\vec{PR} = (4 - 3)\hat{i} + (-3 - (-1))\hat{j} + (1 - 2)\hat{k} = \hat{i} - 2\hat{j} - \hat{k}
$$

Calculate the cross product:

$$
\vec{PQ} \times \vec{PR} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -2 & 0 & -5 \\ 1 & -2 & -1 \end{vmatrix} = \hat{i}(0 - 10) - \hat{j}(2 - (-5)) + \hat{k}(4 - 0) = -10\hat{i} - 7\hat{j} + 4\hat{k}
$$

Find magnitude and area:
$\lvert \vec{PQ} \times \vec{PR} \rvert = \sqrt{(-10)^2 + (-7)^2 + 4^2} = \sqrt{100 + 49 + 16} = \sqrt{165}$
Area $= \frac{\sqrt{165}}{2}$

---

## Scalar Triple Product and Volume

The scalar triple product $\vec{A} \cdot (\vec{B} \times \vec{C})$ calculates the volume of a parallelepiped (a 3D box with sheared sides) whose adjacent edges are $\vec{A}, \vec{B}, \vec{C}$.

It is evaluated as a $3 \times 3$ determinant:

$$
\vec{A} \cdot (\vec{B} \times \vec{C}) = \begin{vmatrix} A_x & A_y & A_z \\ B_x & B_y & B_z \\ C_x & C_y & C_z \end{vmatrix}
$$

**Geometric Proof**:
The cross product $\vec{B} \times \vec{C}$ gives a normal vector whose magnitude is the area of the base. The dot product $\vec{A} \cdot (\vec{B} \times \vec{C})$ projects the third edge $\vec{A}$ onto this normal vector, effectively multiplying the base area by the perpendicular height. Thus:

$$
\text{Volume} = \lvert \vec{A} \cdot (\vec{B} \times \vec{C}) \rvert
$$

### Worked Example: Volume (PYQ 2019)
**Problem**: Find the volume of the parallelepiped whose edges are

$$
\vec{A} = 2\hat{i} - 3\hat{j} + 4\hat{k},
$$


$$
\vec{B} = \hat{i} + 2\hat{j} - \hat{k},
$$


$$
\vec{C} = 3\hat{i} - \hat{j} + 2\hat{k}.
$$

**Solution**:

$$
\vec{A} \cdot (\vec{B} \times \vec{C}) = \begin{vmatrix} 2 & -3 & 4 \\ 1 & 2 & -1 \\ 3 & -1 & 2 \end{vmatrix}
$$

$$
= 2(4 - 1) - (-3)(2 - (-3)) + 4(-1 - 6) = 2(3) + 3(5) + 4(-7) = 6 + 15 - 28 = -7
$$

Volume is the absolute value: $\lvert -7 \rvert = 7$ cubic units.

---

## Coplanar Vectors

If three vectors lie in the exact same plane, the 3D parallelepiped they form has a height of zero. Therefore, its volume is zero.

**Condition for Coplanarity**: Three vectors are coplanar if and only if their scalar triple product is zero.

### Worked Example: Unknown Constant (PYQ 2023)
**Problem**: Find the constant $a$ such that

$$
2\hat{i} - \hat{j} + \hat{k},
$$


$$
\hat{i} + 2\hat{j} - 3\hat{k},
$$


$$
3\hat{i} + a\hat{j} + 5\hat{k}
$$

are coplanar.
**Solution**:
Set the scalar triple product determinant to 0:

$$
\begin{vmatrix} 2 & -1 & 1 \\ 1 & 2 & -3 \\ 3 & a & 5 \end{vmatrix} = 0
$$

$$
2(10 - (-3a)) - (-1)(5 - (-9)) + 1(a - 6) = 0
$$

$$
2(10 + 3a) + 14 + a - 6 = 0 \implies 20 + 6a + 14 + a - 6 = 0 \implies 7a + 28 = 0 \implies a = -4
$$

---

## Exam Patterns
- When given three points and asked for an area, always form two vectors originating from the **same point** (e.g., $\vec{PQ}$ and $\vec{PR}$). Do not cross arbitrary position vectors.
- Scalar triple product calculations are very prone to arithmetic sign errors. Always write out the $2 \times 2$ determinant expansions carefully.

---

[← Previous: A02 Dot and Cross Product](A02_Dot_Product_Cross_Product.md) | [Index](00_Index.md) | [Next: A04 Vector Differentiation →](A04_Vector_Differentiation.md)
