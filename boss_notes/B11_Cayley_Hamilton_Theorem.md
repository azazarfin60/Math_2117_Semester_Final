[← Previous: B10 Eigenvalues and Eigenvectors](B10_Eigenvalues_Eigenvectors.md) | [Index](00_Index.md) | [Next: B12 Adjoint and Inverse →](B12_Adjoint_Inverse_Matrix.md)

---

# B11: Cayley-Hamilton Theorem

> **Exam Weight**: Tier 2 | **Appeared in**: 2018, 2019, 2024 | **Typical Marks**: 5–6

The Cayley-Hamilton theorem connects a matrix to its own characteristic equation. The exam typically asks you to state the theorem, verify it for a given matrix, and then use it to find the inverse.

---

## Statement

Every square matrix satisfies its own characteristic equation.

If the characteristic equation of matrix $A$ of order $n$ is:

$$
\lambda^n + c_{n-1}\lambda^{n-1} + \dots + c_1\lambda + c_0 = 0
$$

then replacing $\lambda$ with $A$ and the constant term with $c_0 I$ gives:

$$
A^n + c_{n-1}A^{n-1} + \dots + c_1 A + c_0 I = O
$$

where $O$ is the zero matrix.

### Key Idea

The characteristic equation is a polynomial equation in the scalar $\lambda$. The Cayley-Hamilton theorem says the same polynomial, when you plug in the matrix $A$ instead of $\lambda$, gives the zero matrix. Constants become scalar multiples of the identity matrix $I$.

---

## Full Proof

Let $A$ be an $n \times n$ square matrix. Its characteristic polynomial is:

$$
p(\lambda) = |A - \lambda I| = c_0 + c_1\lambda + c_2\lambda^2 + \dots + (-1)^n\lambda^n
$$

The adjoint of the characteristic matrix $(A - \lambda I)$ can be written as a polynomial in $\lambda$:

$$
\text{adj}(A - \lambda I) = B_{n-1}\lambda^{n-1} + B_{n-2}\lambda^{n-2} + \dots + B_0
$$

where $B_0, B_1, \dots, B_{n-1}$ are constant $n \times n$ matrices. This works because each cofactor of $(A - \lambda I)$ is a polynomial in $\lambda$ of degree at most $n - 1$.

By the matrix identity

$$
D \cdot \text{adj}(D) = \lvert D \rvert \cdot I
$$

applied to $D = A - \lambda I$:

$$
(A - \lambda I) \cdot \text{adj}(A - \lambda I) = |A - \lambda I| \cdot I
$$

Substitute both polynomial expressions:

$$
(A - \lambda I)(B_{n-1}\lambda^{n-1} + B_{n-2}\lambda^{n-2} + \dots + B_0) = (c_0 + c_1\lambda + \dots + (-1)^n\lambda^n)I
$$

Expand the left side and equate coefficients of each power of $\lambda$:

For $\lambda^0$:

$$
AB_0 = c_0 I
$$

For $\lambda^1$:

$$
AB_1 - B_0 = c_1 I
$$

For $\lambda^2$:

$$
AB_2 - B_1 = c_2 I
$$

$\vdots$

For $\lambda^{n-1}$:

$$
AB_{n-1} - B_{n-2} = c_{n-1}I
$$

For $\lambda^n$:

$$
-B_{n-1} = (-1)^n I
$$

Now pre-multiply these equations by $I, A, A^2, \dots, A^n$ respectively:

$$
AB_0 = c_0 I
$$

$$
A^2 B_1 - AB_0 = c_1 A
$$

$$
A^3 B_2 - A^2 B_1 = c_2 A^2
$$

$$
\vdots
$$

$$
A^n B_{n-1} - A^{n-1}B_{n-2} = c_{n-1}A^{n-1}
$$

$$
-A^n B_{n-1} = (-1)^n A^n
$$

Add all these equations. The left side telescopes (each $A^k B_{k-1}$ appears with $+$ in one equation and $-$ in the next). Everything cancels:

$$
0 = c_0 I + c_1 A + c_2 A^2 + \dots + (-1)^n A^n = p(A)
$$

So $p(A) = O$. The matrix satisfies its own characteristic equation.

---

## How to Verify the Theorem

The verification problem is a standard exam question. Follow these steps:

1. Find the characteristic equation

$$
\lvert A - \lambda I \rvert = 0.
$$

2. Write the matrix version: replace $\lambda^k$ with $A^k$ and constants with $cI$.
3. Compute $A^2$ by multiplying $A \cdot A$.
4. Compute $A^3$ by multiplying $A^2 \cdot A$ (for 3x3 matrices).
5. Substitute into the equation and verify every entry is zero.

---

## Using Cayley-Hamilton to Find the Inverse

This is the most important application. If the characteristic equation is:

$$
A^n + c_{n-1}A^{n-1} + \dots + c_1 A + c_0 I = O
$$

Multiply both sides by $A^{-1}$:

$$
A^{n-1} + c_{n-1}A^{n-2} + \dots + c_1 I + c_0 A^{-1} = O
$$

Rearrange:

$$
A^{-1} = -\frac{1}{c_0}\left(A^{n-1} + c_{n-1}A^{n-2} + \dots + c_1 I\right)
$$

This requires $c_0 \neq 0$ (which means $\lvert A \rvert \neq 0$, so $A$ must be invertible).

For a 3x3 matrix with equation

$$
A^3 + aA^2 + bA + cI = O:
$$

$$
A^{-1} = -\frac{1}{c}(A^2 + aA + bI)
$$

For a 2x2 matrix with equation

$$
A^2 + aA + bI = O:
$$

$$
A^{-1} = -\frac{1}{b}(A + aI)
$$

---

## Worked Example 1: 2x2 Matrix (Lecture)

**Problem**: Verify Cayley-Hamilton and find $A^{-1}$ for:

$$
A =
\begin{bmatrix}
1 & 2 \\
-1 & 3
\end{bmatrix}
$$

**Solution**:

**Step 1**: Characteristic equation.

$$
|A - \lambda I| = (1 - \lambda)(3 - \lambda) + 2 = \lambda^2 - 4\lambda + 5 = 0
$$

**Step 2**: Matrix equation:

$$
A^2 - 4A + 5I = O.
$$

**Step 3**: Compute $A^2$:

$$
A^2 =
\begin{bmatrix}
1 & 2 \\
-1 & 3
\end{bmatrix}\begin{bmatrix} 1 & 2 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} -1 & 8 \\ -4 & 7 \end{bmatrix}
$$

**Step 4**: Verify:

$$
A^2 - 4A + 5I =
\begin{bmatrix}
-1 & 8 \\
-4 & 7
\end{bmatrix} - \begin{bmatrix} 4 & 8 \\ -4 & 12 \end{bmatrix} + \begin{bmatrix} 5 & 0 \\ 0 & 5 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = O \quad \checkmark
$$

**Step 5**: Find $A^{-1}$. Multiply by $A^{-1}$:

$$
A - 4I + 5A^{-1} = O \implies A^{-1} = \frac{1}{5}(4I - A) = \frac{1}{5}
\begin{bmatrix}
3 & -2 \\
1 & 1
\end{bmatrix}
$$

---

## Worked Example 2: 3x3 Matrix (PYQ 2019)

**Problem**: Verify Cayley-Hamilton for the following matrix and find $A^{-1}$:

$$
A =
\begin{pmatrix}
2 & -1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{pmatrix}
$$

**Solution**:

**Step 1**: Characteristic equation.

$$
|A - \lambda I| = 0 \implies \lambda^3 - 6\lambda^2 + 9\lambda - 4 = 0
$$

**Step 2**: Matrix equation:

$$
A^3 - 6A^2 + 9A - 4I = O.
$$

**Step 3**: Compute $A^2$:

$$
A^2 =
\begin{pmatrix}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{pmatrix}
$$

Compute

$$
A^3 = A^2 \cdot A:
$$

$$
A^3 =
\begin{pmatrix}
22 & -21 & 21 \\
-21 & 22 & -21 \\
21 & -21 & 22
\end{pmatrix}
$$

**Step 4**: Verify. Check diagonal entry $(1,1)$: $22 - 6(6) + 9(2) - 4 = 22 - 36 + 18 - 4 = 0$. Check off-diagonal entry $(1,2)$: $-21 - 6(-5) + 9(-1) - 0 = -21 + 30 - 9 = 0$. All entries verify to zero.

**Step 5**: Find $A^{-1}$. Multiply by $A^{-1}$:

$$
A^2 - 6A + 9I = 4A^{-1}
$$

$$
4A^{-1} =
\begin{pmatrix}
6 & -5 & 5 \\
-5 & 6 & -5 \\
5 & -5 & 6
\end{pmatrix} - \begin{pmatrix} 12 & -6 & 6 \\ -6 & 12 & -6 \\ 6 & -6 & 12 \end{pmatrix} + \begin{pmatrix} 9 & 0 & 0 \\ 0 & 9 & 0 \\ 0 & 0 & 9 \end{pmatrix} = \begin{pmatrix} 3 & 1 & -1 \\ 1 & 3 & 1 \\ -1 & 1 & 3 \end{pmatrix}
$$

$$
A^{-1} = \frac{1}{4}
\begin{pmatrix}
3 & 1 & -1 \\
1 & 3 & 1 \\
-1 & 1 & 3
\end{pmatrix}
$$

---

## Worked Example 3: 3x3 Matrix (PYQ 2024)

**Problem**: Verify Cayley-Hamilton for $A$ and compute $A^{-1}$:

$$
A =
\begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix}
$$

**Solution**:

**Step 1**: Characteristic equation:

$$
\lambda^3 - 7\lambda^2 + 11\lambda - 5 = 0.
$$

**Step 2**: Matrix equation:

$$
A^3 - 7A^2 + 11A - 5I = O.
$$

**Step 3**: Compute:

$$
A^2 =
\begin{bmatrix}
7 & 12 & 6 \\
6 & 13 & 6 \\
6 & 12 & 7
\end{bmatrix}, \quad A^3 = \begin{bmatrix} 32 & 62 & 31 \\ 31 & 63 & 31 \\ 31 & 62 & 32 \end{bmatrix}
$$

**Step 4**: Verify. Entry $(1,1)$: $32 - 49 + 22 - 5 = 0$. Entry $(1,2)$: $62 - 84 + 22 + 0 = 0$. All entries zero.

**Step 5**: Find $A^{-1}$:

$$
5A^{-1} = A^2 - 7A + 11I =
\begin{bmatrix}
7 & 12 & 6 \\
6 & 13 & 6 \\
6 & 12 & 7
\end{bmatrix} - \begin{bmatrix} 14 & 14 & 7 \\ 7 & 21 & 7 \\ 7 & 14 & 14 \end{bmatrix} + \begin{bmatrix} 11 & 0 & 0 \\ 0 & 11 & 0 \\ 0 & 0 & 11 \end{bmatrix} = \begin{bmatrix} 4 & -2 & -1 \\ -1 & 3 & -1 \\ -1 & -2 & 4 \end{bmatrix}
$$

$$
A^{-1} = \frac{1}{5}
\begin{bmatrix}
4 & -2 & -1 \\
-1 & 3 & -1 \\
-1 & -2 & 4
\end{bmatrix}
$$

---

## Exam Patterns

- The typical question is "State and prove Cayley-Hamilton theorem" (6 marks) or "Verify Cayley-Hamilton for matrix $A$ and find $A^{-1}$" (5-6 marks).
- The proof was asked in 2018. Verification was asked in 2019 and 2024.
- When verifying, show $A^2$ computation fully. You can abbreviate $A^3$ by showing a few entries if space is short.
- The inverse step is almost always attached. Do not skip it.
- The matrix from PYQ 2024 ($[2,2,1; 1,3,1; 1,2,2]$) is the same matrix used in the eigenvalue problem. Examiners pair these topics.

---

[← Previous: B10 Eigenvalues and Eigenvectors](B10_Eigenvalues_Eigenvectors.md) | [Index](00_Index.md) | [Next: B12 Adjoint and Inverse →](B12_Adjoint_Inverse_Matrix.md)
