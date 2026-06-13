# Lecture 02: Rank of Matrix: A Concept

> **Series**: Matrix Theory
> **Lecture**: 02 of 09
> **Video**: https://www.youtube.com/watch?v=h1FgjMdIEJ0

---

**Navigation**
[< Previous Lecture](01_Basics_of_Matrix_and_Determinant.md) | [Index](README.md) | [Next Lecture >](03_Rank_by_Determinant_and_Echelon_Form.md)

---

## Prerequisites
- Understanding of square matrices and determinants.
- Familiarity with expansion of determinants.

---

## 1. Minors and Rank of a Matrix

### Minor of a Matrix
Let $A$ be any matrix (square or rectangular). From this matrix $A$, delete all columns and rows leaving a certain $p$ columns and $p$ rows. Now if $p \ge 1$, then the elements which have been left constitute a square matrix of order $p$. The determinant of this square matrix is called a **minor** of $A$ of order $p$.

For example, given a $3 \times 3$ matrix:

$$
A = \begin{bmatrix} 3 & 2 & 5 \\ -1 & 0 & 6 \\ 7 & 8 & 3 \end{bmatrix}
$$

The largest minor is of order 3:

$$
|A| = \begin{vmatrix} 3 & 2 & 5 \\ -1 & 0 & 6 \\ 7 & 8 & 3 \end{vmatrix}
$$

Examples of minors of order 2 include:

$$
\begin{vmatrix} 3 & 2 \\ -1 & 0 \end{vmatrix}, \quad \begin{vmatrix} 2 & 5 \\ 0 & 6 \end{vmatrix}, \quad \begin{vmatrix} 3 & 5 \\ -1 & 6 \end{vmatrix}
$$

*(Note: Even for a $3 \times 4$ matrix, the largest possible minor is of order 3, because a minor must be a square determinant.)*

### Rank of a Matrix
Let $A$ be any matrix. A number $r$ is called the **rank** of the matrix $A$, denoted by $\rho(A)$, if it satisfies the following two properties:
1. There is at least one minor of $A$ of order $r$ which does not vanish (i.e., is not equal to zero).
2. Every minor of $A$ of order higher than $r$ vanishes (i.e., is equal to zero).

**Important Properties of Rank:**
*   The rank of a zero matrix is zero ($\rho(O) = 0$).
*   The rank of an identity/unit matrix $I_n$ of order $n$ is $n$.
*   The rank of a non-singular square matrix $A$ of order $n$ is $n$, because its determinant $|A| \neq 0$.

### Nullity of a Matrix
Let $A$ be a square matrix of order $n$. Then the number $(n - r)$, where $r$ is the rank of $A$, is called the **nullity** of the matrix $A$.

$$
N(A) = n - \rho(A)
$$

---

## 2. Methods to Find the Rank of a Matrix

Equivalent matrices (matrices transformed by elementary operations) have equal ranks. There are three primary methods to find the rank:
1.  **Determinant Method** (effective mostly for small matrices like $3 \times 3$).
2.  **By Echelon Form of Matrix** (uses only **Row operations**).
3.  **By Normal Form (Canonical Form) of Matrix**.

### Echelon Form
A matrix is in Echelon form if:
1.  All the non-zero rows, if any, precede the zero rows.
2.  The number of zeroes preceding the first non-zero element in a row is less than the number of such zeroes in the succeeding row.
3.  The first non-zero element in each row is unity ($1$).

**Example of Echelon Form:**

$$
\begin{bmatrix} 1 & 5 & 6 & 7 & 0 & 8 \\ 0 & 1 & 2 & 5 & -1 & 2 \\ 0 & 0 & 0 & 1 & 2 & 4 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}
$$

> [!NOTE]
> If a matrix is in Echelon form, the **rank of the matrix is equal to the number of non-zero rows** in it.

### Normal Form (Canonical Form)
If $A$ is a matrix of order $m \times n$ and rank $r$, then $A$ can be reduced by the application of elementary transformations (both row and column) to any of the following block forms:

1.  $\begin{bmatrix} I_r & 0 \\ 0 & 0 \end{bmatrix}$
2.  $\begin{bmatrix} I_r \\ 0 \end{bmatrix}$
3.  $\begin{bmatrix} I_r & 0 \end{bmatrix}$
4.  $[I_r]$

where $I_r$ is an identity matrix of order $r$, and $0$ represents zero matrices of appropriate dimensions.

---

## 3. Numerical Problem 1: Rank by Echelon Form

**Problem:** Find the rank of the matrix:

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 4 & 2 \\ 2 & 6 & 5 \end{bmatrix}
$$

**Solution:**
We apply elementary row operations to reduce $A$ to Echelon form.

**Step 1:** Use the $1$ in the first row to zero out the elements below it.
Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - 2R_1$:

$$
A \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & 2 & -1 \\ 0 & 2 & -1 \end{bmatrix}
$$

**Step 2:** Use the second row to zero out the element below it.
Apply $R_3 \to R_3 - R_2$:

$$
A \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & 2 & -1 \\ 0 & 0 & 0 \end{bmatrix}
$$

The matrix is now in Echelon form (the leading element in row 2 can be made 1 by dividing, but it is not strictly necessary to determine the number of non-zero rows).
There are exactly **$2$ non-zero rows**.

Thus, the rank of the matrix is:

$$
\rho(A) = 2
$$

---

**Navigation**
[< Previous Lecture](01_Basics_of_Matrix_and_Determinant.md) | [Index](README.md) | [Next Lecture >](03_Rank_by_Determinant_and_Echelon_Form.md)
