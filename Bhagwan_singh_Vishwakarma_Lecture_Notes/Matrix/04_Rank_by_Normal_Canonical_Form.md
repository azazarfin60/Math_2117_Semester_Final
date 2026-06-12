# Rank of Matrix By Normal / Canonical Form

**Series**: Matrix Theory
**Lecture**: 04
**YouTube**: https://www.youtube.com/watch?v=gXwEtwX8g8M

---

**Navigation**
[< Previous Lecture](03_Rank_by_Determinant_and_Echelon_Form.md) | [Index](README.md) | [Next Lecture >](05_Consistency_of_Linear_Equations.md)


## Prerequisites
- Knowledge of matrix rank.
- Understanding of elementary row and column operations.

## Core Content

The Normal form, also known as the Canonical form, is a standard form used to determine the rank of a matrix. Unlike the Echelon form which only uses row operations, reducing a matrix to Normal form involves applying both elementary row and elementary column operations.

### Normal Form Definition
Every non-zero matrix $A$ of rank $r$ can be reduced, by a sequence of elementary row and column operations, to one of the following forms:

$$
\begin{bmatrix} I_r & O \\ O & O \end{bmatrix}, \quad \begin{bmatrix} I_r \\ O \end{bmatrix}, \quad \begin{bmatrix} I_r & O \end{bmatrix}, \quad \text{or} \quad I_r
$$

Here, $I_r$ represents an identity matrix of order $r$, and $O$ represents a zero matrix. The value $r$ gives the rank of the original matrix $A$.

### Procedure for Normal Form Reduction
1. Locate a non-zero element in the matrix. If the element $a_{11}$ is not $1$, interchange rows or columns to bring a $1$ to the $(1,1)$ position. This simplifies calculations.
2. Use elementary row operations to make all other elements in the first column zero.
3. Use elementary column operations to make all other elements in the first row zero.
4. Move to the next diagonal element $a_{22}$. Make it $1$ and use row and column operations to clear out the rest of the second column and second row.
5. Repeat this process down the main diagonal until the matrix is reduced to the identity block $I_r$ and zeros everywhere else.

### Advantages of Normal Form
- It provides a definitive, clear-cut identification of rank. The rank is simply the order of the identity submatrix generated.
- It is useful for finding the equivalence matrices $P$ and $Q$ such that $PAQ$ is in Normal form.

## Solved Example

Let us reduce matrix $A$ to Normal form to find its rank:

$$
A = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 5 & 0 \\ 3 & 7 & -1 \end{bmatrix}
$$

Use row operations to clear the first column below the $(1,1)$ pivot:

$$
R_2 \to R_2 - 2R_1
$$

$$
R_3 \to R_3 - 3R_1
$$

$$
A \sim \begin{bmatrix} 1 & 2 & -1 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{bmatrix}
$$

Use column operations to clear the first row to the right of the $(1,1)$ pivot:

$$
C_2 \to C_2 - 2C_1
$$

$$
C_3 \to C_3 + C_1
$$

$$
A \sim \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{bmatrix}
$$

Use row operation to clear below the $(2,2)$ pivot:

$$
R_3 \to R_3 - R_2
$$

$$
A \sim \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}
$$

Use column operation to clear to the right of the $(2,2)$ pivot:

$$
C_3 \to C_3 - 2C_2
$$

$$
A \sim \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}
$$

This is the Normal form block:

$$
\begin{bmatrix} I_2 & O \\ O & O \end{bmatrix}
$$

The identity block is of order $2$. Therefore, the rank is $\rho(A) = 2$.

## What Comes Next
With the foundation of rank established, the next lecture applies these tools to determine the consistency of systems of linear equations using the Rouché-Capelli theorem.

---

**Navigation**
[< Previous Lecture](03_Rank_by_Determinant_and_Echelon_Form.md) | [Index](README.md) | [Next Lecture >](05_Consistency_of_Linear_Equations.md)
