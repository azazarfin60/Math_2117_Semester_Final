[← Previous: B01 Matrix Basics](B01_Matrix_Basics_Operations.md) | [Index](00_Index.md) | [Next: B03 Hermitian and Special Matrices →](B03_Hermitian_SkewHermitian_Special_Matrices.md)

---

# B02: Transpose, Symmetric, and Skew-Symmetric Matrices

> **Exam Weight**: Tier 2 | **Appeared in**: 2018, 2020, 2021 | **Typical Marks**: 3–6

These definitions are easy marks. The decomposition theorem (symmetric + skew-symmetric) has appeared twice.

---

## Transpose of a Matrix

### Definition

The transpose of matrix $A$ (written $A^T$ or $A'$) is obtained by swapping rows and columns. If $A$ is $m \times n$, then $A^T$ is $n \times m$.

The $(i,j)$-th element of $A^T$ equals the $(j,i)$-th element of $A$:

$$
(A^T)_{ij} = a_{ji}
$$

### Properties of Transpose

1. $(A^T)^T = A$
2. $(A + B)^T = A^T + B^T$
3. $(kA)^T = kA^T$
4. $(AB)^T = B^T A^T$ (order reverses)
5. $(A^{-1})^T = (A^T)^{-1}$

---

## Symmetric Matrix

### Definition

A square matrix $A$ is symmetric if it equals its transpose:

$$
A^T = A
$$

This means $a_{ij} = a_{ji}$ for all $i, j$. The matrix is a mirror image across its main diagonal.

### Example

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 5 & 6 \\ 3 & 6 & 9 \end{bmatrix}
$$

Notice: position $(1,2)$ and $(2,1)$ both have 2. Position $(1,3)$ and $(3,1)$ both have 3.

### Key Properties

- Symmetric matrices have only real eigenvalues.
- They can always be diagonalized.
- They are very common in physics and engineering.

---

## Skew-Symmetric Matrix

### Definition

A square matrix $A$ is skew-symmetric if:

$$
A^T = -A
$$

This means $a_{ij} = -a_{ji}$ for all $i, j$. The diagonal entries must be zero (since $a_{ii} = -a_{ii}$ forces $a_{ii} = 0$).

### Example

$$
A = \begin{bmatrix} 0 & -3 & 5 \\ 3 & 0 & -7 \\ -5 & 7 & 0 \end{bmatrix}
$$

All diagonal entries are 0. Each pair of symmetric positions has opposite signs.

---

## Decomposition Theorem (PYQ 2020, 2021 — Repeated)

### Statement

Every square matrix can be uniquely expressed as the sum of a symmetric matrix and a skew-symmetric matrix.

### Proof

Let $A$ be any square matrix. Define:

$$
P = \frac{1}{2}(A + A^T) \quad \text{and} \quad Q = \frac{1}{2}(A - A^T)
$$

**Step 1**: Show $A = P + Q$.

$$
P + Q = \frac{1}{2}(A + A^T) + \frac{1}{2}(A - A^T) = \frac{1}{2}(2A) = A \quad \checkmark
$$

**Step 2**: Show $P$ is symmetric.

$$
P^T = \left[\frac{1}{2}(A + A^T)\right]^T = \frac{1}{2}(A^T + (A^T)^T) = \frac{1}{2}(A^T + A) = P \quad \checkmark
$$

**Step 3**: Show $Q$ is skew-symmetric.

$$
Q^T = \left[\frac{1}{2}(A - A^T)\right]^T = \frac{1}{2}(A^T - A) = -\frac{1}{2}(A - A^T) = -Q \quad \checkmark
$$

**Step 4**: Prove uniqueness. Suppose $A = P' + Q'$ where $P'$ is symmetric and $Q'$ is skew-symmetric.

Taking transpose: $A^T = P' - Q'$.

Adding the two equations: $A + A^T = 2P'$, so $P' = \frac{1}{2}(A + A^T) = P$.

Subtracting: $A - A^T = 2Q'$, so $Q' = \frac{1}{2}(A - A^T) = Q$.

The decomposition is unique.

### Worked Example

Express

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$

as symmetric + skew-symmetric.

Symmetric part:

$$
P = \frac{1}{2}(A + A^T) = \frac{1}{2}\left(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}\right) = \frac{1}{2}\begin{bmatrix} 2 & 5 \\ 5 & 8 \end{bmatrix} = \begin{bmatrix} 1 & 5/2 \\ 5/2 & 4 \end{bmatrix}
$$

Skew-symmetric part:

$$
Q = \frac{1}{2}(A - A^T) = \frac{1}{2}\left(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} - \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}\right) = \frac{1}{2}\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -1/2 \\ 1/2 & 0 \end{bmatrix}
$$

Verify:

$$
P + Q = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = A.
$$

Correct.

---

## Exam Patterns

- "Define symmetric, skew-symmetric, Hermitian matrices" is a 2-3 mark definition question. Write the formula and one example each.
- The decomposition proof (symmetric + skew-symmetric) appeared in 2020 and 2021. Memorize the formulas $P = \frac{1}{2}(A + A^T)$ and $Q = \frac{1}{2}(A - A^T)$.
- The uniqueness part adds 1-2 extra marks if you include it.

---

[← Previous: B01 Matrix Basics](B01_Matrix_Basics_Operations.md) | [Index](00_Index.md) | [Next: B03 Hermitian and Special Matrices →](B03_Hermitian_SkewHermitian_Special_Matrices.md)
