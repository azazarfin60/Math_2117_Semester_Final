# Rank of Matrix By Determinant and Echelon Form

**Series**: Matrix Theory
**Lecture**: 03
**YouTube**: https://www.youtube.com/watch?v=DNFrfWb7RpM

---

**Navigation**
[< Previous Lecture](02_Rank_of_Matrix_Concept.md) | [Index](README.md) | [Next Lecture >](04_Rank_by_Normal_Canonical_Form.md)


## Prerequisites
- Understanding of matrix rank and minors.
- Familiarity with elementary row operations.

## Core Content

Calculating the rank of a large matrix by evaluating all possible minors becomes computationally expensive. We use systematic methods like Echelon form to simplify this process.

### Elementary Row Operations
We can transform a matrix into a simpler, equivalent form without changing its rank. The valid elementary row operations are:
1. Interchanging any two rows ($R_i \leftrightarrow R_j$).
2. Multiplying a row by a non-zero scalar ($R_i \to kR_i$).
3. Adding a scalar multiple of one row to another row ($R_i \to R_i + kR_j$).

Two matrices are called equivalent ($A \sim B$) if one can be obtained from the other through a sequence of elementary row operations. Equivalent matrices have the same rank.

### Echelon Form
A matrix is in Echelon form if it satisfies the following conditions:
1. All non-zero rows are above any rows of all zeroes.
2. The leading coefficient (the first non-zero number from the left, also called the pivot) of a non-zero row is always strictly to the right of the leading coefficient of the row above it.
3. All entries in a column below a leading coefficient are zeroes.

### Rank using Echelon Form
To find the rank of a matrix using Echelon form:
1. Apply elementary row operations to transform the matrix into Echelon form.
2. Count the number of non-zero rows in the resulting matrix.
3. The rank of the matrix is equal to the number of non-zero rows.

This method is highly systematic and preferred over the minor method.

## Solved Example

Let us find the rank of matrix $A$:

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 4 & 5 \end{bmatrix}
$$

Apply row operations to make entries below the first pivot zero:

$$
R_2 \to R_2 - 2R_1
$$

$$
R_3 \to R_3 - 3R_1
$$

This gives the equivalent matrix:

$$
A \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & -1 & -2 \\ 0 & -2 & -4 \end{bmatrix}
$$

Apply row operation to make entry below the second pivot zero:

$$
R_3 \to R_3 - 2R_2
$$

This gives the matrix in Echelon form:

$$
A \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & -1 & -2 \\ 0 & 0 & 0 \end{bmatrix}
$$

There are two non-zero rows in the Echelon form matrix.
Therefore, the rank is $\rho(A) = 2$.

## What Comes Next
The next lecture covers the Normal (Canonical) Form method. This technique uses both row and column operations to reduce a matrix into an identity submatrix to read its rank directly.

---

**Navigation**
[< Previous Lecture](02_Rank_of_Matrix_Concept.md) | [Index](README.md) | [Next Lecture >](04_Rank_by_Normal_Canonical_Form.md)
