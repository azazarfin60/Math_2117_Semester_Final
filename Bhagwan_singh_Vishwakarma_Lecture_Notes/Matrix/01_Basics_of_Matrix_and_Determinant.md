# Lecture 01: Basics of Matrix and Determinant

> **Series**: Matrix Theory
> **Lecture**: 01 of 09
> **Video**: https://www.youtube.com/watch?v=2NRTmf4SrlI

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_Rank_of_Matrix_Concept.md)

---

## Prerequisites
- Basic algebra and arithmetic operations.
- Familiarity with basic mathematical notations.

---

## 1. Definition of a Matrix
A matrix is a rectangular array (arrangement) of numbers arranged in rows (horizontal) and columns (vertical). Matrices provide a compact way to represent and work with linear transformations and systems of equations.

An $m \times n$ matrix contains $m$ rows and $n$ columns. The elements are denoted by $a_{ij}$, representing the entry in the $i$-th row and $j$-th column.

$$
A = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix}_{m \times n}
$$

**Examples:**
*   **Example 1 (Square Matrix)**: Number of rows equals number of columns ($3 \times 3$).

$$
A = \begin{bmatrix} 2 & 3 & 4 \\ 6 & -2 & 0 \\ 3 & 8 & -10 \end{bmatrix}
$$

*   **Example 2 (Rectangular Matrix)**: Number of rows does not equal number of columns ($2 \times 3$).

$$
B = \begin{bmatrix} 2 & 3 & 4 \\ 5 & 6 & 7 \end{bmatrix}
$$

---

## 2. Types of Matrices
- **Row Matrix**: A matrix with only one row ($1 \times n$).
  
  $$
  A = \begin{bmatrix} a_1 & a_2 & \dots & a_n \end{bmatrix}_{1 \times n}
  $$

- **Column Matrix**: A matrix with only one column ($n \times 1$).

  $$
  B = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix}_{n \times 1}
  $$

- **Zero (Null) Matrix**: A matrix where all elements are zero.

  $$
  O = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}
  $$

---

## 3. Matrix Determinants
The determinant is a scalar value calculated from a square matrix. While matrices are denoted using square brackets $[A]$ and represent arrays, determinants are denoted using straight vertical lines $|A|$ and represent a single numerical value.

### Order 2 Expansion
For a $2 \times 2$ determinant, we cross-multiply:

$$
\begin{vmatrix} 2 & 3 \\ 5 & -1 \end{vmatrix} = 2(-1) - 3(5) = -2 - 15 = -17
$$

### Order 3 Expansion
For a $3 \times 3$ determinant, we expand along a row or column using the sign convention grid (based on $(-1)^{i+j}$):

$$
\begin{bmatrix} + & - & + \\ - & + & - \\ + & - & + \end{bmatrix}
$$

**Example:**

$$
\left| A \right| = \begin{vmatrix} 5 & 6 & 1 \\ 0 & 2 & 7 \\ -1 & -2 & 6 \end{vmatrix}
$$

Expanding along the first row ($5, 6, 1$):

$$
\left| A \right| = 5 \begin{vmatrix} 2 & 7 \\ -2 & 6 \end{vmatrix} - 6 \begin{vmatrix} 0 & 7 \\ -1 & 6 \end{vmatrix} + 1 \begin{vmatrix} 0 & 2 \\ -1 & -2 \end{vmatrix}
$$

$$
= 5[12 - (-14)] - 6[0 - (-7)] + 1[0 - (-2)]
$$

$$
= 5(26) - 6(7) + 1(2)
$$

$$
= 130 - 42 + 2 = 90
$$

*(Note: Determinants are not directly added or subtracted element-wise like matrices; we generally evaluate their final numerical value first.)*

---

## 4. Matrix Operations

### Matrix Addition
**Condition**: The order of both matrices must be exactly equal.
We add the corresponding elements.

**Example**:
$$
\begin{bmatrix} 2 & 3 \\ 4 & 6 \end{bmatrix} + \begin{bmatrix} -1 & -2 \\ 0 & 3 \end{bmatrix} = \begin{bmatrix} 2 + (-1) & 3 + (-2) \\ 4 + 0 & 6 + 3 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 4 & 9 \end{bmatrix}
$$

### Matrix Multiplication
**Condition**: Multiplication $AB$ is only possible if the number of **columns in the first matrix** equals the number of **rows in the second matrix**.
*   If $A$ has order $m \times n$ and $B$ has order $n \times p$, multiplication $AB$ is possible.
*   The resulting matrix $AB$ will have order $m \times p$.
*   **Non-commutative**: Generally, $AB \neq BA$.

---

## What Comes Next
The next lecture covers the concept of the rank of a matrix. We will define rank using minors and explore the concept of nullity.

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_Rank_of_Matrix_Concept.md)
