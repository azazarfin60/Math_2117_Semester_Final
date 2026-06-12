# Cayley Hamilton Theorem: Solved Problems

**Series**: Matrix Theory
**Lecture**: 10
**YouTube**: https://www.youtube.com/watch?v=FwpnB9cGSLE

---

**Navigation**
[< Previous Lecture](08_Cayley_Hamilton_Theorem_State_and_Prove.md) | [Index](README.md)

## Prerequisites
- Understanding of the Cayley-Hamilton theorem statement.
- Proficiency in matrix multiplication and characteristic equation derivation.

## Core Content

The Cayley-Hamilton theorem is a highly practical tool. Its most prominent application is computing the inverse of a large matrix ($A^{-1}$) efficiently by bypassing the need to compute the cofactor and adjoint matrices.

### Finding the Inverse
According to the theorem, if the characteristic equation is:

$$
a_0 A^n + a_1 A^{n-1} + \dots + a_{n-1} A + a_n I = O
$$

Assuming the matrix is non-singular ($\lvert A \rvert = a_n \neq 0$), we can multiply the entire equation by $A^{-1}$:

$$
(a_0 A^n + a_1 A^{n-1} + \dots + a_n I) A^{-1} = O
$$

$$
a_0 A^{n-1} + a_1 A^{n-2} + \dots + a_{n-1} I + a_n A^{-1} = O
$$

Rearranging the terms to isolate $A^{-1}$:

$$
a_n A^{-1} = -(a_0 A^{n-1} + a_1 A^{n-2} + \dots + a_{n-1} I)
$$

$$
A^{-1} = -\frac{1}{a_n} (a_0 A^{n-1} + a_1 A^{n-2} + \dots + a_{n-1} I)
$$

This allows us to compute $A^{-1}$ using only basic matrix multiplications.

### Solved Problem: Order 2 Matrix
Verify Cayley-Hamilton theorem and find $A^{-1}$ for:

$$
A =
\begin{bmatrix}
1 & 2 \\
-1 & 3
\end{bmatrix}
$$

**1. Characteristic Equation:**

$$
\left| A - \lambda I \right| =
\begin{vmatrix}
1 - \lambda & 2 \\
-1 & 3 - \lambda
\end{vmatrix} = 0
$$

$$
(1 - \lambda)(3 - \lambda) + 2 = 0 \implies \lambda^2 - 4\lambda + 5 = 0
$$

**2. Verification:**
We must show $A^2 - 4A + 5I = O$.

$$
A^2 =
\begin{bmatrix}
1 & 2 \\
-1 & 3
\end{bmatrix} \begin{bmatrix} 1 & 2 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} -1 & 8 \\ -4 & 7 \end{bmatrix}
$$

$$
A^2 - 4A + 5I =
\begin{bmatrix}
-1 & 8 \\
-4 & 7
\end{bmatrix} - \begin{bmatrix} 4 & 8 \\ -4 & 12 \end{bmatrix} + \begin{bmatrix} 5 & 0 \\ 0 & 5 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = O
$$

**3. Finding $A^{-1}$:**
Multiply the identity $A^2 - 4A + 5I = O$ by $A^{-1}$:

$$
A - 4I + 5A^{-1} = O \implies A^{-1} = \frac{1}{5}(4I - A)
$$

$$
4I - A =
\begin{bmatrix}
4 & 0 \\
0 & 4
\end{bmatrix} - \begin{bmatrix} 1 & 2 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} 3 & -2 \\ 1 & 1 \end{bmatrix}
$$

$$
A^{-1} = \frac{1}{5}
\begin{bmatrix}
3 & -2 \\
1 & 1
\end{bmatrix}
$$

### Solved Problem: Order 3 Matrix
Find $A^{-1}$ using Cayley-Hamilton for:

$$
A =
\begin{bmatrix}
1 & 0 & 2 \\
0 & 2 & 1 \\
2 & 0 & 3
\end{bmatrix}
$$

**1. Characteristic Equation:**

$$
\left| A - \lambda I \right| = 0 \implies \lambda^3 - 6\lambda^2 + 7\lambda + 2 = 0
$$

**2. Cayley-Hamilton Application:**
The matrix satisfies $A^3 - 6A^2 + 7A + 2I = O$.
Multiply by $A^{-1}$:

$$
A^2 - 6A + 7I + 2A^{-1} = O \implies A^{-1} = \frac{1}{2}(-A^2 + 6A - 7I)
$$

Compute the required matrix components:

$$
A^2 =
\begin{bmatrix}
5 & 0 & 8 \\
2 & 4 & 5 \\
8 & 0 & 13
\end{bmatrix}
$$

$$
-A^2 + 6A - 7I = -
\begin{bmatrix}
5 & 0 & 8 \\
2 & 4 & 5 \\
8 & 0 & 13
\end{bmatrix} + \begin{bmatrix} 6 & 0 & 12 \\ 0 & 12 & 6 \\ 12 & 0 & 18 \end{bmatrix} - \begin{bmatrix} 7 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 7 \end{bmatrix} = \begin{bmatrix} -6 & 0 & 4 \\ -2 & 1 & 1 \\ 4 & 0 & -2 \end{bmatrix}
$$

$$
A^{-1} = \frac{1}{2}
\begin{bmatrix}
-6 & 0 & 4 \\
-2 & 1 & 1 \\
4 & 0 & -2
\end{bmatrix}
$$

## What Comes Next
This concludes the Matrix Theory lecture series. Mastering these concepts provides the foundational tools necessary for advanced applications in linear algebra.

---

**Navigation**
[< Previous Lecture](08_Cayley_Hamilton_Theorem_State_and_Prove.md) | [Index](README.md)
