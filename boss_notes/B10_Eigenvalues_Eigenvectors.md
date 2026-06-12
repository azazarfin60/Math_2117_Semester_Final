[← Previous: B09 Homogeneous Systems](B09_Homogeneous_Systems.md) | [Index](00_Index.md) | [Next: B11 Cayley-Hamilton Theorem →](B11_Cayley_Hamilton_Theorem.md)

---

# B10: Eigenvalues and Eigenvectors

> **Exam Weight**: Tier 1 | **Appeared in**: 2017, 2018, 2019, 2020, 2021, 2023, 2024 (all 7 papers) | **Typical Marks**: 5–12

Eigenvalues and eigenvectors appear in every exam. The same 3x3 matrix has even been reused across years. Master the method and you guarantee yourself 5-12 marks.

---

## Core Definitions

### Eigenvalue and Eigenvector

Let $A$ be a square matrix of order $n$. If a non-zero vector $X$ and a scalar $\lambda$ satisfy:

$$
AX = \lambda X
$$

then $\lambda$ is an **eigenvalue** of $A$ and $X$ is the corresponding **eigenvector**.

The eigenvector does not change direction under the matrix transformation. It only gets scaled by the factor $\lambda$.

### Characteristic Matrix

The matrix $A - \lambda I$ is called the characteristic matrix of $A$. Here $I$ is the identity matrix of the same size as $A$.

### Characteristic Polynomial

The determinant $\lvert A - \lambda I \rvert$ is a polynomial in $\lambda$. This polynomial is called the characteristic polynomial.

### Characteristic Equation

Setting the characteristic polynomial equal to zero gives the characteristic equation:

$$
|A - \lambda I| = 0
$$

The roots of this equation are the eigenvalues.

---

## The Working Rule

Follow these three steps for any eigenvalue/eigenvector problem:

**Step 1: Form the characteristic equation.** Write down $A - \lambda I$ and compute its determinant. Set it equal to zero.

**Step 2: Solve the polynomial.** Find all roots

$$
\lambda_1, \lambda_2, \dots, \lambda_n
$$

. These are the eigenvalues.

**Step 3: Find eigenvectors.** For each $\lambda_i$, substitute it into

$$
(A - \lambda_i I)X = 0
$$

. Solve this homogeneous system by row reduction. The non-zero solutions are the eigenvectors.

---

## Properties of Eigenvalues

These properties help you check your answers and sometimes shortcut the calculation:

1. The sum of all eigenvalues equals the trace (sum of diagonal elements) of $A$.

$$
\lambda_1 + \lambda_2 + \dots + \lambda_n = \text{tr}(A) = a_{11} + a_{22} + \dots + a_{nn}
$$

2. The product of all eigenvalues equals the determinant of $A$.

$$
\lambda_1 \cdot \lambda_2 \cdots \lambda_n = |A|
$$

3. For a triangular matrix (upper or lower), the eigenvalues are the diagonal entries.

4. If $\lambda$ is an eigenvalue of $A$, then $\lambda^k$ is an eigenvalue of $A^k$.

5. If $A$ is invertible and $\lambda$ is an eigenvalue, then $\frac{1}{\lambda}$ is an eigenvalue of $A^{-1}$.

6. An $n \times n$ matrix has exactly $n$ eigenvalues (counting multiplicity). They may be real or complex.

7. Eigenvectors corresponding to distinct eigenvalues are always linearly independent.

---

## Worked Example 1: 2x2 Matrix (PYQ 2021)

**Problem**: Find the eigenvalues and eigenvectors of:

$$
A =
\begin{bmatrix}
2 & 3 \\
1 & 4
\end{bmatrix}
$$

**Solution**:

**Step 1**: The characteristic equation is

$$
\lvert A - \lambda I \rvert = 0:
$$

$$
\begin{vmatrix}
2 - \lambda & 3 \\
1 & 4 - \lambda
\end{vmatrix} = 0
$$

$$
(2 - \lambda)(4 - \lambda) - 3 = 0 \implies \lambda^2 - 6\lambda + 5 = 0
$$

**Step 2**: Factor: $(\lambda - 1)(\lambda - 5) = 0$. So

$$
\lambda_1 = 1
$$

and

$$
\lambda_2 = 5.
$$

**Check**: Trace = $2 + 4 = 6 = 1 + 5$. Determinant = $8 - 3 = 5 = 1 \times 5$. Correct.

**Step 3a**: For $\lambda = 1$, solve $(A - I)X = 0$:

$$
\begin{bmatrix}
1 & 3 \\
1 & 3
\end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

This gives $x + 3y = 0 \implies x = -3y$. Let $y = 1$:

$$
X_1 =
\begin{bmatrix}
-3 \\
1
\end{bmatrix}
$$

**Step 3b**: For $\lambda = 5$, solve $(A - 5I)X = 0$:

$$
\begin{bmatrix}
-3 & 3 \\
1 & -1
\end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

This gives $x - y = 0 \implies x = y$. Let $y = 1$:

$$
X_2 =
\begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

---

## Worked Example 2: 3x3 Matrix (PYQ 2017, 2018 — Repeated)

**Problem**: Find the eigenvalues and eigenvectors of:

$$
A =
\begin{bmatrix}
2 & 2 & 1 \\
1 & 3 & 1 \\
1 & 2 & 2
\end{bmatrix}
$$

This exact matrix appeared in both 2017 (12 marks) and 2018 (6 marks).

**Solution**:

**Step 1**: Compute

$$
\lvert A - \lambda I \rvert = 0:
$$

$$
\begin{vmatrix}
2-\lambda & 2 & 1 \\
1 & 3-\lambda & 1 \\
1 & 2 & 2-\lambda
\end{vmatrix} = 0
$$

Expand the determinant:

$$
(2-\lambda)[(3-\lambda)(2-\lambda) - 2] - 2[(2-\lambda) - 1] + 1[2 - (3-\lambda)] = 0
$$

$$
(2-\lambda)[\lambda^2 - 5\lambda + 4] - 2[1-\lambda] + [\lambda - 1] = 0
$$

After simplification:

$$
\lambda^3 - 7\lambda^2 + 11\lambda - 5 = 0
$$

**Step 2**: Test $\lambda = 1$: $1 - 7 + 11 - 5 = 0$. Yes, it is a root.

Divide by $(\lambda - 1)$:

$$
(\lambda - 1)(\lambda^2 - 6\lambda + 5) = 0 \implies (\lambda - 1)(\lambda - 1)(\lambda - 5) = 0.
$$

Eigenvalues: $\lambda = 1, 1, 5$.

**Check**: Trace = $2 + 3 + 2 = 7 = 1 + 1 + 5$. Correct.

**Step 3a**: For $\lambda = 5$, solve $(A - 5I)X = 0$:

$$
\begin{bmatrix}
-3 & 2 & 1 \\
1 & -2 & 1 \\
1 & 2 & -3
\end{bmatrix}
$$

Swap $R_1 \leftrightarrow R_2$, then $R_2 \to R_2 + 3R_1$, $R_3 \to R_3 - R_1$:

$$
\begin{bmatrix}
1 & -2 & 1 \\
0 & -4 & 4 \\
0 & 4 & -4
\end{bmatrix}
$$

Apply $R_3 \to R_3 + R_2$: row 3 becomes all zeros. From row 2: $y = z$. From row 1: $x = 2y - z = z$.

So $x = y = z$. Let $z = 1$:

$$
X_1 =
\begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix}
$$

**Step 3b**: For $\lambda = 1$ (repeated), solve $(A - I)X = 0$:

$$
\begin{bmatrix}
1 & 2 & 1 \\
1 & 2 & 1 \\
1 & 2 & 1
\end{bmatrix}
$$

All three rows are identical. This gives one equation: $x + 2y + z = 0 \implies x = -2y - z$.

Two free variables ($y$ and $z$). Let $y = s$, $z = t$:

$$
X = s
\begin{bmatrix}
-2 \\
1 \\
0
\end{bmatrix} + t \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}
$$

Two independent eigenvectors:

$$
X_2 =
\begin{bmatrix}
-2 \\
1 \\
0
\end{bmatrix}, \quad X_3 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}
$$

---

## Worked Example 3: 3x3 Matrix (PYQ 2020)

**Problem**: Find eigenvalues and eigenvectors of:

$$
A =
\begin{bmatrix}
1 & 1 & -2 \\
-1 & 2 & 1 \\
0 & 1 & -1
\end{bmatrix}
$$

**Solution**:

**Step 1-2**: The characteristic equation simplifies to:

$$
\lambda^3 - 2\lambda^2 - \lambda + 2 = 0 \implies (\lambda - 1)(\lambda + 1)(\lambda - 2) = 0
$$

Eigenvalues: $\lambda = 1, -1, 2$.

**Step 3a**: For $\lambda = 1$:

$$
\begin{bmatrix}
0 & 1 & -2 \\
-1 & 1 & 1 \\
0 & 1 & -2
\end{bmatrix}
$$

From row 1: $y = 2z$. From row 2: $x = y + z = 3z$. Let $z = 1$:

$$
X_1 =
\begin{bmatrix}
3 \\
2 \\
1
\end{bmatrix}
$$

**Step 3b**: For $\lambda = -1$:

$$
\begin{bmatrix}
2 & 1 & -2 \\
-1 & 3 & 1 \\
0 & 1 & 0
\end{bmatrix}
$$

From row 3: $y = 0$. From row 1: $2x - 2z = 0 \implies x = z$. Let $z = 1$:

$$
X_2 =
\begin{bmatrix}
1 \\
0 \\
1
\end{bmatrix}
$$

**Step 3c**: For $\lambda = 2$:

$$
\begin{bmatrix}
-1 & 1 & -2 \\
-1 & 0 & 1 \\
0 & 1 & -3
\end{bmatrix}
$$

From row 2: $x = z$. From row 3: $y = 3z$. Let $z = 1$:

$$
X_3 =
\begin{bmatrix}
1 \\
3 \\
1
\end{bmatrix}
$$

---

## Worked Example 4: 3x3 Matrix (PYQ 2023)

**Problem**: Find eigenvalues and eigenvectors of:

$$
A =
\begin{bmatrix}
2 & 1 & 1 \\
-1 & 2 & -1 \\
1 & -1 & 2
\end{bmatrix}
$$

**Solution**:

The characteristic equation gives:

$$
(2 - \lambda)(\lambda - 1)(\lambda - 3) = 0
$$

Eigenvalues: $\lambda = 1, 2, 3$.

For $\lambda = 1$: Solving $(A - I)X = 0$ gives $y = 0$, $x = -z$. Eigenvector:

$$
X_1 =
\begin{bmatrix}
-1 \\
0 \\
1
\end{bmatrix}
$$

For $\lambda = 2$: Solving $(A - 2I)X = 0$ gives $x = -z$, $y = -z$. Eigenvector:

$$
X_2 =
\begin{bmatrix}
-1 \\
-1 \\
1
\end{bmatrix}
$$

For $\lambda = 3$: Solving $(A - 3I)X = 0$ gives $x = 0$, $y = -z$. Eigenvector:

$$
X_3 =
\begin{bmatrix}
0 \\
-1 \\
1
\end{bmatrix}
$$

---

## Special Cases

### Triangular Matrices

For any upper or lower triangular matrix, the eigenvalues are the diagonal entries. No computation needed.

**Example** (PYQ 2017): The eigenvalues of:

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & -4 & 2 \\
0 & 0 & 7
\end{pmatrix}
$$

are simply $\lambda = 1, -4, 7$.

### Repeated Eigenvalues

When an eigenvalue has multiplicity $m$ (it appears $m$ times as a root), the number of independent eigenvectors can range from 1 to $m$. If you get fewer than $m$ independent eigenvectors, the matrix cannot be diagonalized. This is important for the diagonalization topic (see B13).

### Complex Eigenvalues

If the characteristic equation has complex roots, the eigenvectors will also have complex entries. Complex eigenvalues always come in conjugate pairs for real matrices. See the class notes for the worked example with

$$
\lambda = \frac{3 \pm i\sqrt{3}}{2}.
$$

---

## Exam Patterns

- **Every paper asks eigenvalues.** The phrasing is always "Find the eigenvalues and eigenvectors of..."
- Usually a 3x3 matrix. Marks range from 5 to 12.
- The same matrix has appeared multiple years (the $[2,2,1; 1,3,1; 1,2,2]$ matrix appeared in 2017 and 2018).
- **Always verify** using trace and determinant. The trace must equal the sum of eigenvalues. The determinant must equal their product.
- For 3x3 matrices, the characteristic polynomial is a cubic. Try integer values (0, 1, 2, -1) first. One root is usually an integer, and you can factor out.
- When solving $(A - \lambda I)X = 0$, you solve a homogeneous system. Use echelon form and express variables in terms of free variables.
- Write eigenvectors with integer entries. Choose the free variable value to avoid fractions.

---

## Eigenvalue Quick-Check Table

For a 3x3 matrix with eigenvalues

$$
\lambda_1, \lambda_2, \lambda_3:
$$

| Property | Formula |
|----------|---------|
| Sum |

$$
\lambda_1 + \lambda_2 + \lambda_3 = a_{11} + a_{22} + a_{33}
$$

|
| Product |

$$
\lambda_1 \cdot \lambda_2 \cdot \lambda_3 = \lvert A \rvert
$$

|
| Sum of products of pairs |

$$
\lambda_1 \lambda_2 + \lambda_1 \lambda_3 + \lambda_2 \lambda_3 =
$$

sum of $2 \times 2$ cofactors |

---

[← Previous: B09 Homogeneous Systems](B09_Homogeneous_Systems.md) | [Index](00_Index.md) | [Next: B11 Cayley-Hamilton Theorem →](B11_Cayley_Hamilton_Theorem.md)
