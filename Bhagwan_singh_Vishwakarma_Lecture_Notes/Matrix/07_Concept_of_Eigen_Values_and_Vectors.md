# Concept of Eigen Values and Vectors

**Series**: Matrix Theory
**Lecture**: 07
**YouTube**: https://www.youtube.com/watch?v=GyT-SdFtqq4

---

**Navigation**
[< Previous Lecture](06_Questions_Consistency_of_Linear_Equations.md) | [Index](README.md) | [Next Lecture >](08_Cayley_Hamilton_Theorem_State_and_Prove.md)

## Prerequisites
- Familiarity with matrix determinants and polynomials.
- Ability to solve homogeneous systems of linear equations.

## Core Content

Eigenvalues and eigenvectors are crucial concepts for analyzing linear transformations. They represent scalars and vectors that remain invariant in direction under a given matrix transformation.

### Characteristic Matrix and Equation
Let $A$ be a square matrix of order $n$, let $\lambda$ be an unknown scalar variable, and let $I$ be the identity matrix of the same order as $A$.

The matrix $A - \lambda I$ is called the **characteristic matrix** of $A$.
The polynomial obtained by expanding the determinant $\left\lvert  A - \lambda I \right\rvert $ is called the **characteristic polynomial**.
Equating the characteristic polynomial to zero gives the **characteristic equation**:

$$
\left| A - \lambda I \right| = 0
$$

### Eigenvalues
The roots of the characteristic equation $\left\lvert  A - \lambda I \right\rvert  = 0$ are called the eigenvalues (or characteristic roots, latent values) of matrix $A$.
An $n \times n$ square matrix has exactly $n$ eigenvalues (which may be real or complex, distinct or repeated). Eigenvalues are unique to a given matrix.

### Eigenvectors
For each eigenvalue $\lambda$, there exists a corresponding non-zero column vector $X$ that satisfies the homogeneous system of equations:

$$
(A - \lambda I)X = 0
$$

This vector $X$ is called the eigenvector of $A$ corresponding to the eigenvalue $\lambda$. Eigenvectors are not unique; if $X$ is an eigenvector, then any scalar multiple $kX$ (where $k \neq 0$) is also an eigenvector.

### Working Rule for Eigenvalues and Eigenvectors
1. **Find Characteristic Equation**: Form $\left\lvert  A - \lambda I \right\rvert  = 0$.
2. **Find Eigenvalues**: Solve the polynomial equation for the roots $\lambda_1, \lambda_2, \dots, \lambda_n$.
3. **Find Eigenvectors**: For each root $\lambda_i$, substitute it back into the equation $(A - \lambda_i I)X = 0$. Solve this homogeneous system using row reductions to Echelon form to find the non-zero vector $X$.

### Solved Example
Find the eigenvalues and eigenvectors for:

$$
A = \begin{bmatrix} 5 & 4 \\ 1 & 2 \end{bmatrix}
$$

**Step 1: Characteristic Equation**

$$
\left| A - \lambda I \right| = \begin{vmatrix} 5 - \lambda & 4 \\ 1 & 2 - \lambda \end{vmatrix} = 0
$$

$$
(5 - \lambda)(2 - \lambda) - 4 = 0 \implies \lambda^2 - 7\lambda + 6 = 0
$$

**Step 2: Eigenvalues**
Factoring the equation $(\lambda - 1)(\lambda - 6) = 0$ yields eigenvalues $\lambda = 1, 6$.

**Step 3: Eigenvector for $\lambda = 1$**

$$
(A - 1I)X = \begin{bmatrix} 4 & 4 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Row operations yield $x_1 + x_2 = 0$. Choosing $x_1 = 1$, we get $x_2 = -1$.
Eigenvector

$$
X_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}.
$$


## What Comes Next
The next lecture states and proves the Cayley-Hamilton Theorem, a powerful result connecting a matrix with its own characteristic equation.

---

**Navigation**
[< Previous Lecture](06_Questions_Consistency_of_Linear_Equations.md) | [Index](README.md) | [Next Lecture >](08_Cayley_Hamilton_Theorem_State_and_Prove.md)
