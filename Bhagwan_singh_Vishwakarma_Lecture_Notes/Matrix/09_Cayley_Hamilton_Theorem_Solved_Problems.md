# Lecture 09: Cayley Hamilton Theorem: Solved Problems

> **Series**: Matrix Theory
> **Lecture**: 09 of 09 (Note: Listed as Lecture-10 in some course materials)
> **Video**: https://www.youtube.com/watch?v=FwpnB9cGSLE

---

**Navigation**
[< Previous Lecture](08_Cayley_Hamilton_Theorem_State_and_Prove.md) | [Index](README.md)

---

## Prerequisites
- Understanding of the Cayley-Hamilton theorem statement.
- Proficiency in matrix multiplication and characteristic equation derivation.

---

## 1. Application: Finding the Inverse of a Matrix
The most prominent application of the Cayley-Hamilton theorem is computing the inverse of a large matrix ($A^{-1}$) efficiently by bypassing the need to compute the cofactor and adjoint matrices.

According to the theorem, every square matrix satisfies its characteristic equation:
$$
a_0 A^n + a_1 A^{n-1} + a_2 A^{n-2} + \ldots + a_{n-1} A + a_n I = O
$$

Assuming the matrix is non-singular ($\lvert A \rvert = a_n \neq 0$), we multiply both sides by $A^{-1}$:
$$
a_0 A^{n-1} + a_1 A^{n-2} + a_2 A^{n-3} + \ldots + a_{n-1} I + a_n A^{-1} = O
$$

Rearranging the terms to isolate $A^{-1}$:
$$
A^{-1} = -\frac{1}{a_n} (a_0 A^{n-1} + a_1 A^{n-2} + \ldots + a_{n-1} I)
$$

---

## 2. Problem 1: Order 2 Matrix

**Problem:** Verify the Cayley-Hamilton Theorem and find $A^{-1}$ for:
$$
A = \begin{bmatrix} 1 & 2 \\ -1 & 3 \end{bmatrix}
$$

**1. Characteristic Equation:**
$$
\lvert A - \lambda I \rvert = \begin{vmatrix} 1 - \lambda & 2 \\ -1 & 3 - \lambda \end{vmatrix} = 0
$$
$$
(1 - \lambda)(3 - \lambda) + 2 = 0 \implies \lambda^2 - 4\lambda + 5 = 0
$$

**2. Verification:**
We must show $A^2 - 4A + 5I = O$. First, calculate $A^2$:
$$
A^2 = \begin{bmatrix} 1 & 2 \\ -1 & 3 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} -1 & 8 \\ -4 & 7 \end{bmatrix}
$$

Substitute into the equation:
$$
A^2 - 4A + 5I = \begin{bmatrix} -1 & 8 \\ -4 & 7 \end{bmatrix} - \begin{bmatrix} 4 & 8 \\ -4 & 12 \end{bmatrix} + \begin{bmatrix} 5 & 0 \\ 0 & 5 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = O
$$
*(Verified)*

**3. Finding $A^{-1}$:**
From $A^2 - 4A + 5I = O$, multiply by $A^{-1}$:
$$
A - 4I + 5A^{-1} = O \implies A^{-1} = \frac{1}{5}(4I - A)
$$
Calculate the inner term:
$$
4I - A = \begin{bmatrix} 4 & 0 \\ 0 & 4 \end{bmatrix} - \begin{bmatrix} 1 & 2 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} 3 & -2 \\ 1 & 1 \end{bmatrix}
$$
Therefore:
$$
A^{-1} = \frac{1}{5} \begin{bmatrix} 3 & -2 \\ 1 & 1 \end{bmatrix}
$$

---

## 3. Problem 2: Order 3 Matrix

**Problem:** Verify the Cayley-Hamilton Theorem and find $A^{-1}$ for:
$$
A = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3 \end{bmatrix}
$$

**1. Characteristic Equation:**
$$
\lvert A - \lambda I \rvert = \begin{vmatrix} 1 - \lambda & 0 & 2 \\ 0 & 2 - \lambda & 1 \\ 2 & 0 & 3 - \lambda \end{vmatrix} = 0
$$
Expanding along the first row:
$$
(1 - \lambda)[(2 - \lambda)(3 - \lambda) - 0] + 2[0 - 2(2 - \lambda)] = 0
$$
$$
(1 - \lambda)(\lambda^2 - 5\lambda + 6) - 4(2 - \lambda) = 0
$$
$$
(6 - 5\lambda + \lambda^2 - 6\lambda + 5\lambda^2 - \lambda^3) - 8 + 4\lambda = 0
$$
$$
-\lambda^3 + 6\lambda^2 - 7\lambda - 2 = 0 \implies \lambda^3 - 6\lambda^2 + 7\lambda + 2 = 0
$$

**2. Verification:**
We must show $A^3 - 6A^2 + 7A + 2I = O$. First, calculate $A^2$ and $A^3$:
$$
A^2 = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3 \end{bmatrix} = \begin{bmatrix} 5 & 0 & 8 \\ 2 & 4 & 5 \\ 8 & 0 & 13 \end{bmatrix}
$$
$$
A^3 = A^2 \cdot A = \begin{bmatrix} 5 & 0 & 8 \\ 2 & 4 & 5 \\ 8 & 0 & 13 \end{bmatrix} \begin{bmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3 \end{bmatrix} = \begin{bmatrix} 21 & 0 & 34 \\ 12 & 8 & 23 \\ 34 & 0 & 55 \end{bmatrix}
$$

Substitute into the equation:
$$
A^3 - 6A^2 + 7A + 2I = \begin{bmatrix} 21 & 0 & 34 \\ 12 & 8 & 23 \\ 34 & 0 & 55 \end{bmatrix} - 6 \begin{bmatrix} 5 & 0 & 8 \\ 2 & 4 & 5 \\ 8 & 0 & 13 \end{bmatrix} + 7 \begin{bmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3 \end{bmatrix} + 2 \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$
$$
= \begin{bmatrix} 21-30+7+2 & 0 & 34-48+14 \\ 12-12 & 8-24+14+2 & 23-30+7 \\ 34-48+14 & 0 & 55-78+21+2 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} = O
$$
*(Verified)*

**3. Finding $A^{-1}$:**
From $A^3 - 6A^2 + 7A + 2I = O$, multiply by $A^{-1}$:
$$
A^2 - 6A + 7I + 2A^{-1} = O \implies 2A^{-1} = -A^2 + 6A - 7I
$$
$$
A^{-1} = \frac{1}{2}(-A^2 + 6A - 7I)
$$

Calculate the inner term:
$$
-A^2 + 6A - 7I = -\begin{bmatrix} 5 & 0 & 8 \\ 2 & 4 & 5 \\ 8 & 0 & 13 \end{bmatrix} + 6 \begin{bmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3 \end{bmatrix} - 7 \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} -6 & 0 & 4 \\ -2 & 1 & 1 \\ 4 & 0 & -2 \end{bmatrix}
$$

Therefore:
$$
A^{-1} = \frac{1}{2} \begin{bmatrix} -6 & 0 & 4 \\ -2 & 1 & 1 \\ 4 & 0 & -2 \end{bmatrix} = \begin{bmatrix} -3 & 0 & 2 \\ -1 & \frac{1}{2} & \frac{1}{2} \\ 2 & 0 & -1 \end{bmatrix}
$$

---

## What Comes Next
This concludes the Matrix Theory lecture series. Mastering these concepts provides the foundational tools necessary for advanced applications in linear algebra.

---

**Navigation**
[< Previous Lecture](08_Cayley_Hamilton_Theorem_State_and_Prove.md) | [Index](README.md)
