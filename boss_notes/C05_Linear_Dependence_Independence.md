[← Previous: C04 Linear Combination](C04_Linear_Combination_Span.md) | [Index](00_Index.md) | [Next: C06 Basis and Dimension →](C06_Basis_Dimension_Extension.md)

---

# C05: Linear Dependence and Independence

> **Exam Weight**: Tier 1 | **Appeared in**: 2018, 2020, 2021, 2024 | **Typical Marks**: 4–6

A set of vectors is **linearly independent** if no vector in the set can be written as a linear combination of the others. If at least one vector can be, the set is **linearly dependent**.

---

## Definitions and The Determinant Test

**Linearly Independent**: A set of vectors $\lbrace v_1, v_2, \dots, v_n\rbrace$ is linearly independent if the equation $c_1 v_1 + c_2 v_2 + \dots + c_n v_n = 0$ has *only the trivial solution* ($c_1 = c_2 = \dots = c_n = 0$).
**Linearly Dependent**: The set is dependent if the equation has a solution where at least one coefficient is not zero.

### The Determinant Test
If you have exactly $n$ vectors in $\mathbb{R}^n$, you can form an $n \times n$ matrix with the vectors as its rows (or columns).
- If Determinant $\neq 0 \implies$ Linearly **Independent**.
- If Determinant $= 0 \implies$ Linearly **Dependent**.

*(Note: If you are given a theoretical proof question (PYQ 2024) asking you to show why this determinant rule is true, set $a\vec{A} + b\vec{B} + c\vec{C} = 0$, convert it to a homogeneous system, and state that a homogeneous system only has the trivial solution if the determinant of the coefficient matrix is non-zero).*

---

## Worked Example 1: Finding the Dependence Relation (PYQ 2018)

**Problem**: Show that

$$
\vec{A} = 2\hat{i} + \hat{j} - 3\hat{k},
$$


$$
\vec{B} = \hat{i} - 4\hat{k},
$$


$$
\vec{C} = 4\hat{i} + 3\hat{j} - \hat{k}
$$

are linearly dependent, and determine a relation between them.

**Solution**:
**Step 1: Check Determinant**

$$
D = \begin{vmatrix} 2 & 1 & -3 \\ 1 & 0 & -4 \\ 4 & 3 & -1 \end{vmatrix} = 2(0 - (-12)) - 1(-1 - (-16)) - 3(3 - 0) = 24 - 15 - 9 = 0
$$

Since $D = 0$, the vectors are linearly dependent.

**Step 2: Find the Relation**
Set $x\vec{A} + y\vec{B} + z\vec{C} = 0$:

$$
x(2, 1, -3) + y(1, 0, -4) + z(4, 3, -1) = (0,0,0)
$$

This yields the system:
1. $2x + y + 4z = 0$
2. $x + 3z = 0 \implies x = -3z$
3. $-3x - 4y - z = 0$

Substitute $x = -3z$ into Equation 1:

$$
2(-3z) + y + 4z = 0 \implies -6z + y + 4z = 0 \implies y = 2z
$$

Let $z = 1$ (we can pick any non-zero value). This gives $x = -3$ and $y = 2$.
Substitute the coefficients back into the original relation:

$$
-3\vec{A} + 2\vec{B} + 1\vec{C} = 0 \implies \vec{C} = 3\vec{A} - 2\vec{B}
$$

---

## Worked Example 2: Abstract Vectors (PYQ 2020, 2021)

**Problem**: Suppose vectors $u, v, w$ are linearly independent. Show that $u + v, u - v, u - 2v + w$ are also linearly independent.

**Solution**:
Set a linear combination equal to the zero vector:

$$
c_1(u + v) + c_2(u - v) + c_3(u - 2v + w) = 0
$$

Group the terms by the original vectors $u, v, w$:

$$
(c_1 + c_2 + c_3)u + (c_1 - c_2 - 2c_3)v + c_3w = 0
$$

Since we are *given* that $u, v, w$ are linearly independent, the only way their linear combination equals 0 is if their coefficients are exactly 0. Thus:
1. $c_1 + c_2 + c_3 = 0$
2. $c_1 - c_2 - 2c_3 = 0$
3. $c_3 = 0$

Substitute $c_3 = 0$ into the first two equations:

$$
c_1 + c_2 = 0
$$

$$
c_1 - c_2 = 0
$$

Adding them gives $2c_1 = 0 \implies c_1 = 0$. This means $c_2 = 0$.
Since the only solution is $c_1 = c_2 = c_3 = 0$, the new vectors are linearly independent. $\blacksquare$

---

## Exam Patterns
- If you are asked to test 3 vectors in $\mathbb{R}^3$, immediately calculate the determinant.
- If asked to "find a relation", you must set up the $x, y, z$ system, express two variables in terms of the third, arbitrarily set the third to $1$, and write the final formula.
- Abstract linear independence proofs (like Example 2) are extremely common and very easy to score full marks on if you group coefficients properly.

---

[← Previous: C04 Linear Combination](C04_Linear_Combination_Span.md) | [Index](00_Index.md) | [Next: C06 Basis and Dimension →](C06_Basis_Dimension_Extension.md)
