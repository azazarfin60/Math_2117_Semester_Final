# Lecture 26: Vector Space - Numerical Problems on Eigenvalues & Eigenvectors of Matrices

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 26 of 27
> **Video**: https://www.youtube.com/watch?v=X7tLRj8Le-8

---

**Navigation**
[< Previous Lecture](25_Eigenvalue_Numericals.md) | [Index](README.md) | [Next Lecture >](27_Diagonalization.md)


---

## Prerequisites
To find the eigenvalues and eigenvectors of a linear transformation, we can find the eigenvalues and eigenvectors of its matrix representation. Today, we focus purely on the computational mechanics of extracting these values from square matrices. This process is the foundational step for matrix diagonalization.

---

## The General Process

Let $A$ be a square matrix.
1.  **Find Eigenvalues**: Solve the characteristic equation for $\lambda$:

$$
    \det(A - \lambda I) = 0
$$

    This yields a polynomial (quadratic for $2 \times 2$, cubic for $3 \times 3$). The roots of this polynomial are the eigenvalues.
2.  **Find Eigenvectors**: For each eigenvalue $\lambda$, solve the homogeneous system of linear equations:

$$
    (A - \lambda I)X = \bar{0}
$$

    Reduce the matrix $(A - \lambda I)$ to row echelon form to find the free variables. Assign values to the free variables to generate linearly independent eigenvectors.

---

## Problem 1: Matrix (Distinct Eigenvalues)

**Given:**

$$
A = \begin{bmatrix} 4 & 2 \\ 3 & 3 \end{bmatrix}
$$

**Step 1: Find Eigenvalues**
Set up the characteristic equation:

$$
\det \begin{bmatrix} 4 - \lambda & 2 \\ 3 & 3 - \lambda \end{bmatrix} = 0
$$

Expand the determinant:

$$
(4 - \lambda)(3 - \lambda) - (3)(2) = 0
$$

$$
\lambda^2 - 7\lambda + 12 - 6 = 0 \implies \lambda^2 - 7\lambda + 6 = 0
$$

Factor the quadratic equation:

$$
(\lambda - 6)(\lambda - 1) = 0
$$

The eigenvalues are **$\lambda_1 = 1$** and **$\lambda_2 = 6$**.

**Step 2: Find Eigenvector for $\lambda = 1$**

$$
(A - 1I)X = \bar{0} \implies \begin{bmatrix} 3 & 2 \\ 3 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Apply row operation $R_2 \to R_2 - R_1$:

$$
\begin{bmatrix} 3 & 2 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies 3x_1 + 2x_2 = 0
$$

We have 1 free variable. Choose $x_1 = 2 \implies x_2 = -3$.
The eigenvector and its eigenspace:

$$
X^{(1)} = \begin{bmatrix} 2 \\ -3 \end{bmatrix}, \quad W_1 = \text{span}\left\lbrace \begin{bmatrix} 2 \\ -3 \end{bmatrix} \right\rbrace
$$

**Step 3: Find Eigenvector for $\lambda = 6$**

$$
(A - 6I)X = \bar{0} \implies \begin{bmatrix} -2 & 2 \\ 3 & -3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Apply row operation $R_2 \to 2R_2 + 3R_1$:

$$
\begin{bmatrix} -2 & 2 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies -2x_1 + 2x_2 = 0 \implies x_1 = x_2
$$

Choose $x_2 = 1 \implies x_1 = 1$.
The eigenvector and its eigenspace:

$$
X^{(2)} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad W_6 = \text{span}\left\lbrace \begin{bmatrix} 1 \\ 1 \end{bmatrix} \right\rbrace
$$

---

## Problem 2: Matrix (Repeated Eigenvalues)

**Given:**

$$
A = \begin{bmatrix} 6 & -2 & 2 \\ -2 & 3 & -1 \\ 2 & -1 & 3 \end{bmatrix}
$$

**Step 1: Find Eigenvalues**

$$
\det \begin{bmatrix} 6 - \lambda & -2 & 2 \\ -2 & 3 - \lambda & -1 \\ 2 & -1 & 3 - \lambda \end{bmatrix} = 0
$$

Expanding along the first row and simplifying yields the characteristic polynomial:

$$
\lambda^3 - 12\lambda^2 + 36\lambda - 32 = 0
$$

Using trial-and-error, we test $\lambda = 2$:

$$
2^3 - 12(2)^2 + 36(2) - 32 = 8 - 48 + 72 - 32 = 0
$$

Since $\lambda = 2$ is a root, we factor out $(\lambda - 2)$:

$$
(\lambda - 2)(\lambda^2 - 10\lambda + 16) = 0 \implies (\lambda - 2)(\lambda - 2)(\lambda - 8) = 0
$$

The eigenvalues are **$\lambda = 2, 2, 8$**. Notice that $2$ is a repeated eigenvalue.

**Step 2: Find Eigenvector for $\lambda = 8$**

$$
(A - 8I)X = \bar{0} \implies \begin{bmatrix} -2 & -2 & 2 \\ -2 & -5 & -1 \\ 2 & -1 & -5 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$

Reduce to row echelon form:

$$
\begin{bmatrix} -2 & -2 & 2 \\ 0 & -3 & -3 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$

This gives equations:
1.  $-x_1 - x_2 + x_3 = 0$
2.  $-3x_2 - 3x_3 = 0 \implies x_2 = -x_3$

Choose $x_3 = 1 \implies x_2 = -1 \implies x_1 = 2$.

$$
X^{(1)} = \begin{bmatrix} 2 \\ -1 \\ 1 \end{bmatrix}
$$

**Step 3: Find Eigenvectors for the Repeated Eigenvalue $\lambda = 2$**
Because $\lambda = 2$ appears twice (algebraic multiplicity of 2), we anticipate finding 2 free variables (geometric multiplicity of 2).

$$
(A - 2I)X = \bar{0} \implies \begin{bmatrix} 4 & -2 & 2 \\ -2 & 1 & -1 \\ 2 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$

Notice that row 2 and row 3 are scalar multiples of row 1. Reducing the matrix zeros out the bottom two rows entirely:

$$
\begin{bmatrix} 2 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \implies 2x_1 - x_2 + x_3 = 0
$$

We have 3 variables and only 1 equation, meaning we have $3 - 1 = 2$ free parameters. We make two separate sets of choices to find two linearly independent eigenvectors:

*   **Choice A:** Let $x_3 = 1$ and $x_2 = -1$.
    $$2x_1 - (-1) + 1 = 0 \implies 2x_1 = -2 \implies x_1 = -1$$
    $$X^{(2)} = \begin{bmatrix} -1 \\ -1 \\ 1 \end{bmatrix}$$
*   **Choice B:** Let $x_3 = 0$ and $x_2 = 2$.
    $$2x_1 - (2) + 0 = 0 \implies 2x_1 = 2 \implies x_1 = 1$$
    $$X^{(3)} = \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}$$

The eigenspace for $\lambda = 2$ is the span of these two vectors:

$$
W_2 = \text{span}\left\lbrace \begin{bmatrix} -1 \\ -1 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix} \right\rbrace
$$

## Key Takeaways
*   The characteristic polynomial for an $n \times n$ matrix is always of degree $n$, yielding exactly $n$ eigenvalues (some may be repeated or complex).
*   For repeated eigenvalues, if the algebraic multiplicity (how many times the root appears) equals the geometric multiplicity (the number of free variables / linearly independent eigenvectors found), the matrix is well-behaved and diagonalizable.
*   Row reduction is strictly required to find eigenvectors correctly.

## What Comes Next
We will use these matrices of eigenvectors to perform **Diagonalization**, simplifying complex transformations into pure scaling operations.

---

**Navigation**
[< Previous Lecture](25_Eigenvalue_Numericals.md) | [Index](README.md) | [Next Lecture >](27_Diagonalization.md)
