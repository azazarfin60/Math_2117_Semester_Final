# Lecture 27: Vector Space - Diagonalization of Matrices

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 27 of 27
> **Video**: https://www.youtube.com/watch?v=qMwnGmEXBpY

---

**Navigation**
[< Previous Lecture](26_Matrix_Eigenvalue_Problems.md) | [Index](README.md)

---

## Prerequisites
Diagonalization is the final culmination of our study of eigenvalues and eigenvectors. To prove that a matrix is diagonalizable means to prove that there exists a change of basis (a transition matrix) that transforms the given matrix into a purely diagonal matrix. This greatly simplifies matrix computations, especially matrix exponentiation.

---

## The Working Procedure for Diagonalization

Suppose we want to determine if an $n \times n$ square matrix $A$ is diagonalizable, and if so, perform the diagonalization.

1.  **Characteristic Equation**: Solve $\det(A - \lambda I) = 0$ to find the $n$ eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$.
2.  **Eigenvectors**: For each eigenvalue, solve $(A - \lambda I)X = \bar{0}$ to find the corresponding eigenvectors. We must be able to generate a complete set of $n$ **linearly independent** eigenvectors. If we cannot find $n$ linearly independent eigenvectors, the matrix is *not* diagonalizable.
3.  **Transition (Modal) Matrix ($P$)**: Construct the transition matrix $P$ by placing the $n$ linearly independent eigenvectors as its columns:

$$
P = \begin{bmatrix} X_1 & X_2 & \dots & X_n \end{bmatrix}
$$

4.  **Inverse Modal Matrix ($P^{-1}$)**: Compute the inverse of the transition matrix. For smaller matrices, use the adjoint method:

$$
P^{-1} = \frac{1}{\det(P)} \text{adj}(P)
$$

5.  **Compute $P^{-1} A P$**: Multiply the matrices. If the matrix is diagonalizable, the result will exactly equal a diagonal matrix $D$, whose diagonal entries are the eigenvalues of $A$ in the exact same order as their corresponding eigenvectors appear in $P$.

$$
P^{-1} A P = D = \begin{bmatrix} \lambda_1 & 0 & \dots & 0 \\ 0 & \lambda_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n \end{bmatrix}
$$

---

## Example 1: Diagonalizing a Matrix

**Given:**

$$
A = \begin{bmatrix} 4 & 2 \\ 3 & 3 \end{bmatrix}
$$

From our previous lecture, we already computed:
*   Eigenvalues: $\lambda_1 = 1$, $\lambda_2 = 6$.
*   Eigenvectors:

$$
X_1 = \begin{bmatrix} 2 \\ -3 \end{bmatrix}, \quad X_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

**Step 1: Construct the Modal Matrix $P$**
Place $X_1$ and $X_2$ as columns:

$$
P = \begin{bmatrix} 2 & 1 \\ -3 & 1 \end{bmatrix}
$$

Check linear independence by finding the determinant:

$$
\det(P) = (2)(1) - (1)(-3) = 2 + 3 = 5 \neq 0
$$

Since $\det(P) \neq 0$, the columns are linearly independent.

**Step 2: Find $P^{-1}$**
Find the cofactors to build the adjoint matrix:
*   $P_{11} = 1, \quad P_{12} = 3$
*   $P_{21} = -1, \quad P_{22} = 2$

$$
\text{adj}(P) = \begin{bmatrix} 1 & -1 \\ 3 & 2 \end{bmatrix} \implies P^{-1} = \frac{1}{5} \begin{bmatrix} 1 & -1 \\ 3 & 2 \end{bmatrix}
$$

**Step 3: Evaluate $P^{-1} A P$**
First, multiply $A$ and $P$:

$$
A P = \begin{bmatrix} 4 & 2 \\ 3 & 3 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ -3 & 1 \end{bmatrix} = \begin{bmatrix} (8 - 6) & (4 + 2) \\ (6 - 9) & (3 + 3) \end{bmatrix} = \begin{bmatrix} 2 & 6 \\ -3 & 6 \end{bmatrix}
$$

Next, multiply $P^{-1}$ by the result:

$$
P^{-1} (A P) = \frac{1}{5} \begin{bmatrix} 1 & -1 \\ 3 & 2 \end{bmatrix} \begin{bmatrix} 2 & 6 \\ -3 & 6 \end{bmatrix}
$$

$$
= \frac{1}{5} \begin{bmatrix} (2 + 3) & (6 - 6) \\ (6 - 6) & (18 + 12) \end{bmatrix} = \frac{1}{5} \begin{bmatrix} 5 & 0 \\ 0 & 30 \end{bmatrix}
$$

$$
= \begin{bmatrix} 1 & 0 \\ 0 & 6 \end{bmatrix} = D
$$

Because $P^{-1}AP$ yields a diagonal matrix containing the eigenvalues $1$ and $6$ on the diagonal, we have successfully proven that matrix $A$ is diagonalizable.

---

## Example 2: Matrix with Repeated Eigenvalues

**Given:**

$$
A = \begin{bmatrix} 3 & 2 & 4 \\ 2 & 0 & 2 \\ 4 & 2 & 3 \end{bmatrix}
$$

**Step 1: Eigenvalues and Eigenvectors**
*   **Eigenvalues**: Solving $\det(A - \lambda I) = 0$ gives $\lambda = 8, -1, -1$. (Note that $-1$ is a repeated eigenvalue with algebraic multiplicity 2).
*   **Eigenvector for $\lambda = 8$**: Solving $(A - 8I)X = \bar{0}$ yields:

$$
X_1 = \begin{bmatrix} 2 \\ 1 \\ 2 \end{bmatrix}
$$

*   **Eigenvectors for $\lambda = -1$**: Solving $(A + 1I)X = \bar{0}$ yields the single equation $2x_1 + x_2 + 2x_3 = 0$. By setting $(x_1=1, x_3=0)$ and then $(x_1=0, x_3=1)$, we extract two linearly independent eigenvectors:

$$
X_2 = \begin{bmatrix} 1 \\ -2 \\ 0 \end{bmatrix}, \quad X_3 = \begin{bmatrix} 0 \\ -2 \\ 1 \end{bmatrix}
$$

**Step 2: Modal Matrix $P$**
Place $X_1$, $X_2$, and $X_3$ into the modal matrix:

$$
P = \begin{bmatrix} 2 & 1 & 0 \\ 1 & -2 & -2 \\ 2 & 0 & 1 \end{bmatrix}
$$

**Step 3: Diagonalization**
By computing $P^{-1}$ using the adjoint method and evaluating the product $P^{-1} A P$, we get:

$$
P^{-1} A P = \begin{bmatrix} 8 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{bmatrix} = D
$$

The eigenvalues $8, -1, -1$ perfectly match the order of the eigenvectors in $P$. The matrix $A$ is diagonalizable.

## Key Takeaways
*   **Diagonalization represents a change of basis**: By shifting our perspective to the basis formed by the eigenvectors, the complex transformation $A$ simplifies into a diagonal matrix $D$, which only scales vectors along these specific axes.
*   **A requirement for diagonalization**: You *must* have a full set of $n$ linearly independent eigenvectors for an $n \times n$ matrix to be diagonalizable.

---
*(This concludes the 27-lecture Vector Space series!)*

---

**Navigation**
[< Previous Lecture](26_Matrix_Eigenvalue_Problems.md) | [Index](README.md)
