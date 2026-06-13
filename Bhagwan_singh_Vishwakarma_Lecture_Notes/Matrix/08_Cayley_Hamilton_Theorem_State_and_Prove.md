# Lecture 08: Cayley Hamilton Theorem: State and Prove

> **Series**: Matrix Theory
> **Lecture**: 08 of 09 (Note: Listed as Lecture-9 in some course materials)
> **Video**: https://www.youtube.com/watch?v=yJUoUn9f2Wo

---

**Navigation**
[< Previous Lecture](07_Concept_of_Eigen_Values_and_Vectors.md) | [Index](README.md) | [Next Lecture >](09_Cayley_Hamilton_Theorem_Solved_Problems.md)

---

## Prerequisites
- Knowledge of characteristic polynomials and characteristic equations.
- Familiarity with matrix cofactors and the adjoint matrix identity $D \cdot \text{adj}(D) = \lvert D \rvert I$.

---

## 1. Statement of the Theorem

**Cayley-Hamilton Theorem**: Every square matrix satisfies its own characteristic equation.

**Mathematical Form:**
Let $A$ be a square matrix of order $n \times n$. Let its characteristic equation be:

$$
\lvert A - \lambda I \rvert = a_0 \lambda^n + a_1 \lambda^{n-1} + a_2 \lambda^{n-2} + \ldots + a_n = 0
$$

Then, replacing the scalar variable $\lambda$ with the matrix $A$ yields a valid matrix identity:

$$
a_0 A^n + a_1 A^{n-1} + a_2 A^{n-2} + \ldots + a_n I = O
$$

where $I$ is the identity matrix of order $n$, and $O$ is the zero matrix of order $n$.

---

## 2. Formal Proof

### Step 1: Defining the Adjoint Polynomial
Let $A$ be an $n \times n$ square matrix with the characteristic equation:
$$
\lvert A - \lambda I \rvert = a_0 \lambda^n + a_1 \lambda^{n-1} + \ldots + a_n = 0
$$

The elements of the characteristic matrix $(A - \lambda I)$ are polynomials in $\lambda$ of degree at most 1. The elements of its adjoint matrix, $\text{adj}(A - \lambda I)$, are the cofactors of $(A - \lambda I)$. Since cofactors are determinants of order $n-1$, they are polynomials in $\lambda$ of degree at most $n - 1$.

Therefore, we can express $\text{adj}(A - \lambda I)$ as a matrix polynomial in $\lambda$:
$$
\text{adj}(A - \lambda I) = B_0 \lambda^{n-1} + B_1 \lambda^{n-2} + B_2 \lambda^{n-3} + \ldots + B_{n-1}
$$
where $B_0, B_1, \ldots, B_{n-1}$ are $n \times n$ matrices whose elements are constant scalars independent of $\lambda$.

### Step 2: Applying the Adjoint Identity
We use the fundamental matrix property for any square matrix $D$:
$$
D \cdot \text{adj}(D) = \lvert D \rvert I
$$

Substituting $D = A - \lambda I$, we get:
$$
(A - \lambda I) \cdot \text{adj}(A - \lambda I) = \lvert A - \lambda I \rvert I
$$

Now, substitute the polynomial expressions into both sides:
$$
(A - \lambda I)(B_0 \lambda^{n-1} + B_1 \lambda^{n-2} + \ldots + B_{n-1}) = (a_0 \lambda^n + a_1 \lambda^{n-1} + \ldots + a_n)I
$$

### Step 3: Equating Coefficients
Expand the left-hand side and equate the matrix coefficients of corresponding powers of $\lambda$ on both sides:

*   For $\lambda^n$:
    $$
    -B_0 = a_0 I
    $$
*   For $\lambda^{n-1}$:
    $$
    A B_0 - B_1 = a_1 I
    $$
*   For $\lambda^{n-2}$:
    $$
    A B_1 - B_2 = a_2 I
    $$
*   ... (continuing the pattern) ...
*   For $\lambda^1$:
    $$
    A B_{n-2} - B_{n-1} = a_{n-1} I
    $$
*   For the constant term ($\lambda^0$):
    $$
    A B_{n-1} = a_n I
    $$

### Step 4: Elimination and Conclusion
To eliminate the $B_i$ matrices, pre-multiply these equations successively by $A^n, A^{n-1}, A^{n-2}, \ldots, A, I$:

$$
-A^n B_0 = a_0 A^n
$$
$$
A^n B_0 - A^{n-1} B_1 = a_1 A^{n-1}
$$
$$
A^{n-1} B_1 - A^{n-2} B_2 = a_2 A^{n-2}
$$
$$
\ldots
$$
$$
A^2 B_{n-2} - A B_{n-1} = a_{n-1} A
$$
$$
A B_{n-1} = a_n I
$$

Now, add all these equations together. 
Notice that on the left-hand side (LHS), the terms cancel each other out in pairs (telescoping sum):
$$
-A^n B_0 + A^n B_0 - A^{n-1} B_1 + A^{n-1} B_1 - A^{n-2} B_2 + \ldots - A B_{n-1} + A B_{n-1} = O
$$

The sum of the right-hand side (RHS) becomes:
$$
a_0 A^n + a_1 A^{n-1} + a_2 A^{n-2} + \ldots + a_{n-1} A + a_n I
$$

Therefore, equating LHS and RHS gives:
$$
a_0 A^n + a_1 A^{n-1} + a_2 A^{n-2} + \ldots + a_n I = O
$$

**Hence Proved.**

---

## What Comes Next
The next lecture applies the Cayley-Hamilton theorem to solve numerical problems. We will use the theorem to verify matrix polynomials and efficiently compute the inverse of matrices without calculating the adjoint.

---

**Navigation**
[< Previous Lecture](07_Concept_of_Eigen_Values_and_Vectors.md) | [Index](README.md) | [Next Lecture >](09_Cayley_Hamilton_Theorem_Solved_Problems.md)
