[← Previous: B11 Cayley-Hamilton Theorem](B11_Cayley_Hamilton_Theorem.md) | [Index](00_Index.md) | [Next: B13 Diagonalization and Matrix ODE →](B13_Diagonalization_Matrix_Exponential_ODE.md)

---

# B12: Adjoint and Inverse of a Matrix

> **Exam Weight**: Tier 1-2 | **Appeared in**: 2017, 2019, 2020, 2021, 2023 | **Typical Marks**: 5–6

Finding the inverse of a matrix is one of the most common exam questions. Two methods exist: the adjoint method and the row operations method. You must know both.

---

## Minors and Cofactors

### Minor

The minor $M_{ij}$ of element $a_{ij}$ in a matrix $A$ is the determinant of the submatrix obtained by deleting row $i$ and column $j$ from $A$.

### Cofactor

The cofactor $C_{ij}$ of element $a_{ij}$ is the signed minor:

$$
C_{ij} = (-1)^{i+j} M_{ij}
$$

The sign follows a checkerboard pattern:

$$
\begin{bmatrix}
+ & - & + \\
- & + & - \\
+ & - & +
\end{bmatrix}
$$

### Example

For matrix:

$$
A =
\begin{pmatrix}
0 & 1 & 2 \\
1 & 2 & 3 \\
3 & 1 & 1
\end{pmatrix}
$$

The minor $M_{11}$ is obtained by deleting row 1 and column 1:

$$
M_{11} =
\begin{vmatrix}
2 & 3 \\
1 & 1
\end{vmatrix} = 2 - 3 = -1
$$

The cofactor $C_{11} = (-1)^{1+1}(-1) = -1$.

---

## Adjoint Matrix

### Definition

The adjoint of a square matrix $A$ (written $\text{adj}(A)$) is the transpose of the cofactor matrix.

**Step 1**: Find all cofactors $C_{ij}$.

**Step 2**: Form the cofactor matrix $C$.

**Step 3**: Transpose it: $\text{adj}(A) = C^T$.

### Key Property

$$
A \cdot \text{adj}(A) = |A| \cdot I
$$

This is the foundation of the adjoint method for finding the inverse.

---

## Inverse by Adjoint Method

### Definition

A square matrix $A$ is invertible if there exists a matrix $B$ such that $AB = BA = I$. This $B$ is called $A^{-1}$.

A matrix is invertible if and only if $\lvert A \rvert \neq 0$.

### Formula

$$
A^{-1} = \frac{1}{|A|} \text{adj}(A)
$$

### Worked Example 1: Adjoint Method (PYQ 2017)

**Problem**: Find the adjoint and inverse of:

$$
A =
\begin{pmatrix}
0 & 1 & 2 \\
1 & 2 & 3 \\
3 & 1 & 1
\end{pmatrix}
$$

**Solution**:

**Step 1**: Find the determinant:

$$
|A| = 0(2-3) - 1(1-9) + 2(1-6) = 0 + 8 - 10 = -2
$$

Since $\lvert A \rvert \neq 0$, the inverse exists.

**Step 2**: Find all cofactors:

$$
C_{11} = +(2-3) = -1, \quad C_{12} = -(1-9) = 8, \quad C_{13} = +(1-6) = -5
$$

$$
C_{21} = -(1-2) = 1, \quad C_{22} = +(0-6) = -6, \quad C_{23} = -(0-3) = 3
$$

$$
C_{31} = +(3-4) = -1, \quad C_{32} = -(0-2) = 2, \quad C_{33} = +(0-1) = -1
$$

**Step 3**: Adjoint = transpose of cofactor matrix:

$$
\text{adj}(A) =
\begin{pmatrix}
-1 & 1 & -1 \\
8 & -6 & 2 \\
-5 & 3 & -1
\end{pmatrix}
$$

**Step 4**: Inverse:

$$
A^{-1} = \frac{1}{-2}
\begin{pmatrix}
-1 & 1 & -1 \\
8 & -6 & 2 \\
-5 & 3 & -1
\end{pmatrix} = \begin{pmatrix} 1/2 & -1/2 & 1/2 \\ -4 & 3 & -1 \\ 5/2 & -3/2 & 1/2 \end{pmatrix}
$$

---

### Worked Example 2: Rotation Matrix Inverse (PYQ 2020)

**Problem**: Find the adjoint and inverse of:

$$
A =
\begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

**Solution**:

Determinant: $\lvert A \rvert = \cos^2\theta + \sin^2\theta = 1$.

Cofactors:

$$
C_{11} = \cos\theta, \quad C_{12} = -\sin\theta, \quad C_{13} = 0
$$

$$
C_{21} = \sin\theta, \quad C_{22} = \cos\theta, \quad C_{23} = 0
$$

$$
C_{31} = 0, \quad C_{32} = 0, \quad C_{33} = 1
$$

Adjoint (transpose of cofactor matrix):

$$
\text{adj}(A) =
\begin{bmatrix}
\cos\theta & \sin\theta & 0 \\
-\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Since $\lvert A \rvert = 1$:

$$
A^{-1} =
\begin{bmatrix}
\cos\theta & \sin\theta & 0 \\
-\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Notice: $A^{-1} = A^T$. This is because $A$ is an orthogonal matrix (rotation matrix).

---

## Inverse by Row Operations

### The Method

1. Write the augmented matrix $[A \; \lvert  \; I]$.
2. Apply elementary row operations to transform $A$ into $I$.
3. The same operations transform $I$ into $A^{-1}$.
4. When the left side becomes $I$, the right side is $A^{-1}$.

### Worked Example 3: Row Operations (PYQ 2019)

**Problem**: Find the inverse of:

$$
A =
\begin{pmatrix}
1 & 3 & 3 \\
1 & 4 & 3 \\
1 & 3 & 4
\end{pmatrix}
$$

**Solution**:

Set up $[A \lvert  I]$:

$$
\begin{bmatrix}
1 & 3 & 3 & | & 1 & 0 & 0 \\
1 & 4 & 3 & | & 0 & 1 & 0 \\
1 & 3 & 4 & | & 0 & 0 & 1
\end{bmatrix}
$$

Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:

$$
\begin{bmatrix}
1 & 3 & 3 & | & 1 & 0 & 0 \\
0 & 1 & 0 & | & -1 & 1 & 0 \\
0 & 0 & 1 & | & -1 & 0 & 1
\end{bmatrix}
$$

Apply $R_1 \to R_1 - 3R_2$:

$$
\begin{bmatrix}
1 & 0 & 3 & | & 4 & -3 & 0 \\
0 & 1 & 0 & | & -1 & 1 & 0 \\
0 & 0 & 1 & | & -1 & 0 & 1
\end{bmatrix}
$$

Apply $R_1 \to R_1 - 3R_3$:

$$
\begin{bmatrix}
1 & 0 & 0 & | & 7 & -3 & -3 \\
0 & 1 & 0 & | & -1 & 1 & 0 \\
0 & 0 & 1 & | & -1 & 0 & 1
\end{bmatrix}
$$

The inverse is:

$$
A^{-1} =
\begin{pmatrix}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{pmatrix}
$$

---

### Worked Example 4: Row Operations (PYQ 2021)

**Problem**: Find the inverse by row operations:

$$
A =
\begin{pmatrix}
2 & 1 & 2 \\
2 & 2 & 1 \\
1 & 2 & 2
\end{pmatrix}
$$

**Solution**:

Set up $[A \lvert  I]$ and swap $R_1 \leftrightarrow R_3$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
2 & 2 & 1 & | & 0 & 1 & 0 \\
2 & 1 & 2 & | & 1 & 0 & 0
\end{bmatrix}
$$

Apply $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - 2R_1$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
0 & -2 & -3 & | & 0 & 1 & -2 \\
0 & -3 & -2 & | & 1 & 0 & -2
\end{bmatrix}
$$

Scale $R_2 \to -\frac{1}{2}R_2$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
0 & 1 & 3/2 & | & 0 & -1/2 & 1 \\
0 & -3 & -2 & | & 1 & 0 & -2
\end{bmatrix}
$$

Apply $R_3 \to R_3 + 3R_2$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 0 & 0 & 1 \\
0 & 1 & 3/2 & | & 0 & -1/2 & 1 \\
0 & 0 & 5/2 & | & 1 & -3/2 & 1
\end{bmatrix}
$$

Scale $R_3 \to \frac{2}{5}R_3$, then back-substitute upward. After all operations:

$$
A^{-1} = \frac{1}{5}
\begin{pmatrix}
2 & 2 & -3 \\
-3 & 2 & 2 \\
2 & -3 & 2
\end{pmatrix}
$$

---

### Worked Example 5: Row Operations (PYQ 2023)

**Problem**: Find the inverse by row transformation:

$$
A =
\begin{bmatrix}
1 & 3 & 5 \\
2 & 4 & 5 \\
3 & 7 & 6
\end{bmatrix}
$$

**Solution**:

Set up $[A \lvert  I]$. Apply $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - 3R_1$:

$$
\begin{bmatrix}
1 & 3 & 5 & | & 1 & 0 & 0 \\
0 & -2 & -5 & | & -2 & 1 & 0 \\
0 & -2 & -9 & | & -3 & 0 & 1
\end{bmatrix}
$$

Apply $R_3 \to R_3 - R_2$:

$$
\begin{bmatrix}
1 & 3 & 5 & | & 1 & 0 & 0 \\
0 & -2 & -5 & | & -2 & 1 & 0 \\
0 & 0 & -4 & | & -1 & -1 & 1
\end{bmatrix}
$$

Scale $R_2 \to -\frac{1}{2}R_2$ and $R_3 \to -\frac{1}{4}R_3$. Then back-substitute:

$$
A^{-1} = \frac{1}{8}
\begin{bmatrix}
-11 & 17 & -5 \\
3 & -9 & 5 \\
2 & 2 & -2
\end{bmatrix}
$$

---

## Which Method to Use?

| Method | Best For | Pros | Cons |
|--------|----------|------|------|
| Adjoint | Small matrices, when adjoint is also asked | Gives both adjoint and inverse | Tedious for large matrices (9 cofactors for 3x3) |
| Row operations | Any size matrix, when only inverse is asked | Systematic, fewer calculations | Does not give the adjoint |
| Cayley-Hamilton | When eigenvalues or characteristic equation is already known | Elegant, uses known information | Requires $A^2$ computation |

If the problem says "find adjoint and inverse," use the adjoint method.
If the problem says "find inverse by row operations," use row operations.
If the problem says "verify Cayley-Hamilton and find inverse," use Cayley-Hamilton (see B11).

---

## Important Proofs

### Proof: Inverse of a Product

**Statement**: $(AB)^{-1} = B^{-1}A^{-1}$ (the order reverses).

**Proof**: We need to show that $B^{-1}A^{-1}$ satisfies the definition of the inverse of $AB$.

$$
(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I
$$

$$
(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I
$$

Since $(AB)(B^{-1}A^{-1}) = I$ and $(B^{-1}A^{-1})(AB) = I$, we have $(AB)^{-1} = B^{-1}A^{-1}$.

This proof has appeared in 2018 and 2023.

---

## Exam Patterns

- **Inverse appears in 5 out of 7 papers.** Usually "Find the inverse by row operations" or "Find the adjoint and inverse."
- Row operations method is more common in recent papers (2019, 2021, 2023).
- The adjoint method was popular in older papers (2017, 2020).
- The proof $(AB)^{-1} = B^{-1}A^{-1}$ has appeared twice. Memorize it.
- Always check: $\lvert A \rvert \neq 0$ before attempting inverse. State this explicitly.
- Verify your answer by multiplying $AA^{-1}$ (at least check one row) if time permits.

---

[← Previous: B11 Cayley-Hamilton Theorem](B11_Cayley_Hamilton_Theorem.md) | [Index](00_Index.md) | [Next: B13 Diagonalization and Matrix ODE →](B13_Diagonalization_Matrix_Exponential_ODE.md)
