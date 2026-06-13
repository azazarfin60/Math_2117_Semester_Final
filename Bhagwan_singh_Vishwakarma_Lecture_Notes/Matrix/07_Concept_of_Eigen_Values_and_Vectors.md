# Lecture 07: Concept of Eigen Values and Vectors

> **Series**: Matrix Theory
> **Lecture**: 07 of 09
> **Video**: https://www.youtube.com/watch?v=GyT-SdFtqq4

---

**Navigation**
[< Previous Lecture](06_Questions_Consistency_of_Linear_Equations.md) | [Index](README.md) | [Next Lecture >](08_Cayley_Hamilton_Theorem_State_and_Prove.md)

---

## Prerequisites
- Familiarity with matrix determinants and polynomials.
- Ability to solve homogeneous systems of linear equations.

---

## 1. Definitions

### Characteristic Matrix
Let $A$ be a square matrix of order $n$, let $\lambda$ be a scalar (unknown variable), and let $I$ be the identity matrix of the same order as $A$. The matrix:
$$
A - \lambda I
$$
is called the characteristic matrix of $A$.

**Example:**
If $A = \begin{bmatrix} 2 & 3 \\ 4 & 6 \end{bmatrix}$ and $I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$, then:
$$
A - \lambda I = \begin{bmatrix} 2 & 3 \\ 4 & 6 \end{bmatrix} - \lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 - \lambda & 3 \\ 4 & 6 - \lambda \end{bmatrix}
$$

### Characteristic Polynomial & Equation
*   **Characteristic Polynomial**: The determinant of the characteristic matrix, $\lvert A - \lambda I \rvert$, which yields a polynomial in $\lambda$.
*   **Characteristic Equation**: Equating the characteristic polynomial to zero:
$$
\lvert A - \lambda I \rvert = 0
$$

---

## 2. Eigenvalues and Eigenvectors

### Characteristic Roots / Eigenvalues
The roots of the characteristic equation $\lvert A - \lambda I \rvert = 0$ are called characteristic roots, **eigenvalues**, or latent values of matrix $A$. These values are unique for a given matrix.

### Eigenvectors
Let $A$ be a square matrix of order $n$, and $\lambda$ be an eigenvalue of $A$. A **non-zero** column vector:
$$
X = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}
$$
satisfying the relation:
$$
(A - \lambda I)X = 0
$$
is called an **eigenvector** of $A$ corresponding to the eigenvalue $\lambda$.

**Key Properties:**
1.  $(A - \lambda I)X = 0$ is a homogeneous system of linear equations.
2.  The eigenvector $X$ must be non-zero ($X \neq 0$).
3.  The eigenvector corresponding to an eigenvalue is **not unique**. For any scalar $k \neq 0$, $kX$ is also an eigenvector.

---

## 3. Working Rule
1.  **Step 1**: Find the characteristic equation $\lvert A - \lambda I \rvert = 0$.
2.  **Step 2**: Solve the characteristic equation to find eigenvalues $\lambda = \lambda_1, \lambda_2, \ldots, \lambda_n$.
3.  **Step 3**: For each eigenvalue $\lambda_i$, solve the homogeneous system $(A - \lambda_i I)X = 0$ using row operations to reduce the matrix to Echelon form, and choose arbitrary variables to find a non-zero eigenvector $X$.

---

## 4. Solved Problem 1

**Problem:** Find the eigenvalues and eigenvectors of the matrix:
$$
A = \begin{bmatrix} 5 & 4 \\ 1 & 2 \end{bmatrix}
$$

**Step 1: Characteristic Equation**
$$
\lvert A - \lambda I \rvert = 0 \implies \begin{vmatrix} 5 - \lambda & 4 \\ 1 & 2 - \lambda \end{vmatrix} = 0
$$

**Step 2: Solve the determinant**
$$
(5 - \lambda)(2 - \lambda) - 4 = 0
$$
$$
10 - 5\lambda - 2\lambda + \lambda^2 - 4 = 0
$$
$$
\lambda^2 - 7\lambda + 6 = 0
$$

Factoring:
$$
\lambda^2 - 6\lambda - \lambda + 6 = 0
$$
$$
\lambda(\lambda - 6) - 1(\lambda - 6) = 0
$$
$$
(\lambda - 6)(\lambda - 1) = 0
$$
**Eigenvalues:** $\lambda = 1, 6$.

**Step 3: Eigenvectors**

**Case 1: Eigenvector for $\lambda = 1$**
Let the eigenvector be $X_1 = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$. Solve $(A - 1I)X_1 = 0$:
$$
\begin{bmatrix} 5-1 & 4 \\ 1 & 2-1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies \begin{bmatrix} 4 & 4 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Apply row operation $R_1 \to \frac{1}{4} R_1$:
$$
\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Apply row operation $R_2 \to R_2 - R_1$:
$$
\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

This gives the equation $x_1 + x_2 = 0 \implies x_2 = -x_1$.
Choosing $x_1 = 1$ arbitrarily ($x_1 \neq 0$), we get $x_2 = -1$.
$$
X_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$
*(General form is $X_1 = k \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ for $k \neq 0$).*

**Case 2: Eigenvector for $\lambda = 6$**
Let the eigenvector be $X_2 = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$. Solve $(A - 6I)X_2 = 0$:
$$
\begin{bmatrix} 5-6 & 4 \\ 1 & 2-6 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies \begin{bmatrix} -1 & 4 \\ 1 & -4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Apply row operation $R_2 \to R_2 + R_1$:
$$
\begin{bmatrix} -1 & 4 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

This gives the equation $-x_1 + 4x_2 = 0 \implies x_1 = 4x_2$.
Choosing $x_2 = 1$ arbitrarily ($x_2 \neq 0$), we get $x_1 = 4$.
$$
X_2 = \begin{bmatrix} 4 \\ 1 \end{bmatrix}
$$
*(General form is $X_2 = k \begin{bmatrix} 4 \\ 1 \end{bmatrix}$ for $k \neq 0$).*

---

**Navigation**
[< Previous Lecture](06_Questions_Consistency_of_Linear_Equations.md) | [Index](README.md) | [Next Lecture >](08_Cayley_Hamilton_Theorem_State_and_Prove.md)
