# Lecture 20: Vector Space - Inverse of Linear Transformation

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 20 of 27
> **Video**: https://www.youtube.com/watch?v=bXeQILCHnVY

---

**Navigation**
[< Previous Lecture](19_Matrix_Representation.md) | [Index](README.md) | [Next Lecture >](21_Rank_Nullity_Theorem.md)

---

## Prerequisites
We know how to represent a linear transformation $T : V \to W$ as a matrix $[T]$. Today, we will learn how to reverse this mapping. Finding the **Inverse Linear Transformation** $T^{-1}$ means finding a mapping that takes vectors from the co-domain back to their original vectors in the domain.

---

## Condition for Invertibility

Let $T : V \to W$ be a linear transformation.
For $T$ to have an inverse $T^{-1} : W \to V$, the transformation must be a perfect one-to-one correspondence (an isomorphism). Practically, when working with matrix representations, this means:

1.  **Square Matrix Requirement**: The dimension of the domain must equal the dimension of the co-domain. For a transformation $T : V \to V$, its matrix $A = [T]_B$ will be a square matrix.
2.  **Non-Singularity**: The determinant of the transformation matrix must be non-zero.

$$
    |A| \neq 0
$$

    If $\lvert A \rvert \neq 0$, the linear transformation is called **non-singular** and is guaranteed to be invertible. If $\lvert A \rvert = 0$, it is singular and cannot be inverted (information was lost, meaning the kernel is not just the zero vector).

---

## Finding the Inverse Transformation

If the transformation is invertible, its inverse is perfectly represented by the inverse of its matrix.

### The Steps
1.  **Construct the Matrix**: Find the matrix $A = [T]_B$ of the transformation with respect to a given basis (usually the standard basis).
2.  **Verify Non-Singularity**: Compute the determinant $\lvert A \rvert$. Ensure $\lvert A \rvert \neq 0$.
3.  **Compute the Inverse Matrix**: Use the standard formula for matrix inversion:

$$
    A^{-1} = \frac{\text{adj}(A)}{|A|}
$$

    This inverse matrix *is* the matrix representation of the inverse transformation:

$$
    [T^{-1}]_B = A^{-1}
$$

4.  **Derive the Formula**: Multiply the inverse matrix by a general column vector to find the explicit formula for $T^{-1}$:

$$
    T^{-1}(x, y, z) = A^{-1} \begin{bmatrix} x \\ y \\ z \end{bmatrix}
$$

---

## Numerical Example 1

**Problem:** Find the inverse linear transformation $T^{-1}$ for the transformation $T : \mathbb{R}^3 \to \mathbb{R}^3$ defined by:

$$
T(x, y, z) = (2x + y + z, x + y + 2z, x - 2z)
$$

with respect to the standard basis.

**Step 1: Construct the Matrix $A$**
Use the standard basis $B = \lbrace (1, 0, 0), (0, 1, 0), (0, 0, 1) \rbrace$.
Compute the images:
*   $T(1, 0, 0) = (2(1)+0+0, 1+0+0, 1-0) = (2, 1, 1)$
*   $T(0, 1, 0) = (0+1+0, 0+1+0, 0-0) = (1, 1, 0)$
*   $T(0, 0, 1) = (0+0+1, 0+0+2(1), 0-2(1)) = (1, 2, -2)$

Write these coordinate vectors as columns to form the matrix $A$:

$$
A = \begin{bmatrix} 2 & 1 & 1 \\ 1 & 1 & 2 \\ 1 & 0 & -2 \end{bmatrix}
$$

**Step 2: Verify Non-Singularity**
Compute the determinant of $A$:

$$
|A| = 2 \begin{vmatrix} 1 & 2 \\ 0 & -2 \end{vmatrix} - 1 \begin{vmatrix} 1 & 2 \\ 1 & -2 \end{vmatrix} + 1 \begin{vmatrix} 1 & 1 \\ 1 & 0 \end{vmatrix}
$$

$$
|A| = 2(-2) - 1(-4) + 1(-1) = -4 + 4 - 1 = -1
$$

Since $\lvert A \rvert = -1 \neq 0$, the transformation is non-singular and invertible.

**Step 3: Compute the Inverse Matrix $A^{-1}$**
Find the adjoint matrix by computing all 9 cofactors (omitting the tedious arithmetic here):

$$
\text{adj}(A) = \begin{bmatrix} -2 & 2 & 1 \\ 4 & -5 & -3 \\ -1 & 1 & 1 \end{bmatrix}
$$

Calculate the inverse:

$$
A^{-1} = \frac{1}{|A|} \text{adj}(A) = \frac{1}{-1} \begin{bmatrix} -2 & 2 & 1 \\ 4 & -5 & -3 \\ -1 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & -2 & -1 \\ -4 & 5 & 3 \\ 1 & -1 & -1 \end{bmatrix}
$$

**Step 4: Derive the Formula**
Multiply the inverse matrix by $(x, y, z)^T$:

$$
T^{-1}(x, y, z) = \begin{bmatrix} 2 & -2 & -1 \\ -4 & 5 & 3 \\ 1 & -1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix}
$$

Extracting the rows gives the final formula:

$$
T^{-1}(x, y, z) = (2x - 2y - z, -4x + 5y + 3z, x - y - z)
$$

**Verification:**
We know $T(1, 0, 0) = (2, 1, 1)$. Let's plug $(2, 1, 1)$ into our new formula.

$$
T^{-1}(2, 1, 1) = (2(2) - 2(1) - 1, -4(2) + 5(1) + 3(1), 2 - 1 - 1)
$$

$$
T^{-1}(2, 1, 1) = (4 - 2 - 1, -8 + 5 + 3, 0) = (1, 0, 0)
$$

The formula perfectly reverses the transformation!

---

## Numerical Example 2 (Homework)

**Problem:** Let $T : \mathbb{R}^3 \to \mathbb{R}^3$ be a linear transformation defined by:

$$
T(x, y, z) = (3x + z, -2x + y, -x + 2y + 4z)
$$

Prove that $T$ is invertible, and find the formula for $T^{-1}$.

**Solution Outline:**
**1. Matrix representation:**
Compute $T(1,0,0) = (3, -2, -1)$, $T(0,1,0) = (0, 1, 2)$, $T(0,0,1) = (1, 0, 4)$.

$$
A = \begin{bmatrix} 3 & 0 & 1 \\ -2 & 1 & 0 \\ -1 & 2 & 4 \end{bmatrix}
$$

**2. Determinant:**

$$
|A| = 3(4 - 0) - 0 + 1(-4 + 1) = 12 - 3 = 9 \neq 0
$$

Because the determinant is 9 (non-zero), $T$ is invertible.

**3. Adjoint and Inverse:**
Calculating the cofactors gives the adjoint:

$$
\text{adj}(A) = \begin{bmatrix} 4 & 2 & -1 \\ 8 & 13 & -2 \\ -3 & -6 & 3 \end{bmatrix}
$$

$$
A^{-1} = \frac{1}{9} \begin{bmatrix} 4 & 2 & -1 \\ 8 & 13 & -2 \\ -3 & -6 & 3 \end{bmatrix}
$$

**4. Final Formula:**

$$
T^{-1}(x, y, z) = \frac{1}{9} (4x + 2y - z, 8x + 13y - 2z, -3x - 6y + 3z)
$$

## Key Takeaways
*   A linear transformation is invertible (non-singular) if and only if the determinant of its matrix representation is non-zero ($\lvert A \rvert \neq 0$).
*   The matrix of the inverse transformation is exactly the inverse of the original transformation's matrix ($[T^{-1}]_B = [T]_B^{-1}$).
*   Matrix representation turns the complex algebraic problem of reversing a function into the standardized mechanical process of finding a matrix inverse.

---

**Navigation**
[< Previous Lecture](19_Matrix_Representation.md) | [Index](README.md) | [Next Lecture >](21_Rank_Nullity_Theorem.md)
