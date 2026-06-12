# Cayley Hamilton Theorem: State and Prove

**Series**: Matrix Theory
**Lecture**: 09
**YouTube**: https://www.youtube.com/watch?v=yJUoUn9f2Wo

---

**Navigation**
[< Previous Lecture](07_Concept_of_Eigen_Values_and_Vectors.md) | [Index](README.md) | [Next Lecture >](09_Cayley_Hamilton_Theorem_Solved_Problems.md)

## Prerequisites
- Knowledge of characteristic polynomials and characteristic equations.
- Familiarity with matrix cofactors and the adjoint matrix identity $A \cdot \text{adj}(A) = \lvert A \rvertI$.

## Core Content

The Cayley-Hamilton theorem is a fundamental theorem in linear algebra that establishes an elegant relationship between a square matrix and its characteristic equation.

### Statement
**Every square matrix satisfies its own characteristic equation.**

If $A$ is a square matrix of order $n \times n$ and its characteristic equation is:

$$
\left| A - \lambda I \right| = a_0\lambda^n + a_1\lambda^{n-1} + a_2\lambda^{n-2} + \dots + a_n = 0
$$

Then replacing the scalar variable $\lambda$ with the matrix $A$ yields a valid matrix identity:

$$
a_0A^n + a_1A^{n-1} + a_2A^{n-2} + \dots + a_nI = O
$$

Where $I$ is the identity matrix and $O$ is the zero matrix of order $n$.

### Proof Analysis
Let $A$ be an $n \times n$ square matrix. Its characteristic equation is a polynomial of degree $n$ in $\lambda$.

The elements of the characteristic matrix $(A - \lambda I)$ are polynomials in $\lambda$ of degree at most $1$. Consequently, the cofactors of $(A - \lambda I)$ are determinants of order $n-1$, meaning they are polynomials in $\lambda$ of degree at most $n-1$.

Since the adjoint matrix $\text{adj}(A - \lambda I)$ is the transpose of the cofactor matrix, its elements are also polynomials of degree at most $n-1$. We can express the adjoint matrix as a polynomial matrix in $\lambda$:

$$
\text{adj}(A - \lambda I) = B_0\lambda^{n-1} + B_1\lambda^{n-2} + \dots + B_{n-1}
$$

Where $B_0, B_1, \dots, B_{n-1}$ are $n \times n$ matrices with scalar entries independent of $\lambda$.

Using the fundamental matrix property for any square matrix $D$, $D \cdot \text{adj}(D) = \left\lvert  D \right\rvert I$. Applying this to $D = A - \lambda I$:

$$
(A - \lambda I) \cdot \text{adj}(A - \lambda I) = \left| A - \lambda I \right|I
$$

Substitute the polynomial expressions:

$$
(A - \lambda I)(B_0\lambda^{n-1} + B_1\lambda^{n-2} + \dots + B_{n-1}) = (a_0\lambda^n + a_1\lambda^{n-1} + \dots + a_n)I
$$

By expanding the left-hand side and equating the matrix coefficients of corresponding powers of $\lambda$ on both sides, we obtain a system of matrix equations. Pre-multiplying these equations by descending powers of $A$ (i.e., $A^n, A^{n-1}, \dots, I$) and adding them together causes a telescoping cancellation of all terms involving $B_i$.

The remaining sum simplifies exactly to:

$$
a_0A^n + a_1A^{n-1} + \dots + a_nI = O
$$

This completes the proof.

## What Comes Next
The next lecture applies the Cayley-Hamilton theorem to solve numerical problems. We will use the theorem to verify matrix polynomials and efficiently compute the inverse of matrices without calculating the adjoint.

---

**Navigation**
[< Previous Lecture](07_Concept_of_Eigen_Values_and_Vectors.md) | [Index](README.md) | [Next Lecture >](09_Cayley_Hamilton_Theorem_Solved_Problems.md)
