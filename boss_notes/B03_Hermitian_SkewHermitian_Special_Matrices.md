[← Previous: B02 Transpose and Symmetric Matrices](B02_Transpose_Symmetric_SkewSymmetric.md) | [Index](00_Index.md) | [Next: B04 Matrix Proofs →](B04_Matrix_Proofs.md)

---

# B03: Hermitian, Skew-Hermitian, and Special Matrices

> **Exam Weight**: Tier 2 | **Appeared in**: 2018, 2023 | **Typical Marks**: 2–5

Definition questions about matrix types are easy marks. The Hermitian decomposition proof appeared in 2023.

---

## Hermitian Matrix

### Definition

A square matrix $A$ with complex entries is Hermitian if it equals its conjugate transpose:

$$
A^\dagger = (\bar{A})^T = A
$$

Here $\bar{A}$ is the complex conjugate (replace $i$ with $-i$ in every entry). Then $A^\dagger$ transposes the result.

### Properties

- Diagonal entries must be real (since

$$
a_{ii} = \overline{a_{ii}}
$$

implies $a_{ii} \in \mathbb{R}$).
- Off-diagonal entries satisfy

$$
a_{ij} = \overline{a_{ji}}.
$$

- All eigenvalues of a Hermitian matrix are real.

### Example

$$
A =
\begin{pmatrix}
2 & 1+i \\
1-i & 3
\end{pmatrix}
$$

Check:

$$
\bar{A} =
\begin{pmatrix}
2 & 1-i \\
1+i & 3
\end{pmatrix}, \quad (\bar{A})^T = \begin{pmatrix} 2 & 1+i \\ 1-i & 3 \end{pmatrix} = A
$$

Hermitian.

---

## Skew-Hermitian Matrix

### Definition

A square matrix $A$ is skew-Hermitian if:

$$
A^\dagger = -A
$$

### Properties

- Diagonal entries must be pure imaginary or zero (since

$$
\overline{a_{ii}} = -a_{ii}
$$

).
- Off-diagonal entries satisfy

$$
a_{ij} = -\overline{a_{ji}}.
$$

### Example

$$
A =
\begin{pmatrix}
2i & 1+i \\
-1+i & 0
\end{pmatrix}
$$

---

## Hermitian Decomposition Theorem (PYQ 2023)

### Statement

Every square matrix can be expressed as the sum of a Hermitian matrix and a skew-Hermitian matrix.

### Proof

Let $A$ be any square matrix. Define:

$$
P = \frac{1}{2}(A + A^\dagger) \quad \text{and} \quad Q = \frac{1}{2}(A - A^\dagger)
$$

**Show $P$ is Hermitian**:

$$
P^\dagger = \frac{1}{2}(A^\dagger + (A^\dagger)^\dagger) = \frac{1}{2}(A^\dagger + A) = P
$$

**Show $Q$ is skew-Hermitian**:

$$
Q^\dagger = \frac{1}{2}(A^\dagger - (A^\dagger)^\dagger) = \frac{1}{2}(A^\dagger - A) = -Q
$$

And $P + Q = A$.

This is the same structure as the symmetric decomposition. Replace transpose with conjugate transpose.

---

## Special Matrix Types

### Nilpotent Matrix

A square matrix $A$ is nilpotent if there exists a positive integer $k$ such that:

$$
A^k = O
$$

where $O$ is the zero matrix. The smallest such $k$ is the index of nilpotency.

**Example**:

$$
A =
\begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix}. \quad A^2 = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = O.
$$

Nilpotent with index 2.

All eigenvalues of a nilpotent matrix are zero.

### Involutory Matrix

A square matrix $A$ is involutory if:

$$
A^2 = I
$$

This means $A$ is its own inverse:

$$
A^{-1} = A.
$$

**Example**:

$$
A =
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}. \quad A^2 = I.
$$

### Idempotent Matrix

A square matrix $A$ is idempotent if:

$$
A^2 = A
$$

Applying the transformation twice gives the same result as applying it once. Projection matrices are idempotent.

**Example**:

$$
A =
\begin{bmatrix}
1 & 0 \\
0 & 0
\end{bmatrix}. \quad A^2 = A.
$$

The eigenvalues of an idempotent matrix are only 0 or 1.

### Periodic Matrix

A square matrix $A$ is periodic with period $k$ if:

$$
A^{k+1} = A
$$

An idempotent matrix is periodic with period 1.

### Orthogonal Matrix

A square matrix $A$ is orthogonal if:

$$
A^T A = AA^T = I
$$

This means

$$
A^{-1} = A^T
$$

. The columns form an orthonormal set. The determinant is $\pm 1$.

**Example**: Rotation matrices are orthogonal.

### Unitary Matrix

A square matrix $A$ is unitary if:

$$
A^\dagger A = AA^\dagger = I
$$

This is the complex version of orthogonal.

$$
A^{-1} = A^\dagger.
$$

---

## Exam Patterns

- "Define commutative, idempotent, involutory matrix" appeared in 2023 for 2 marks. Just write the definition and one example.
- "Define symmetric, skew-symmetric, Hermitian" appeared in 2018 for 3 marks.
- The Hermitian decomposition proof appeared in 2023 for 5 marks.
- These are easy marks. Memorize the one-line definitions.

---

[← Previous: B02 Transpose and Symmetric Matrices](B02_Transpose_Symmetric_SkewSymmetric.md) | [Index](00_Index.md) | [Next: B04 Matrix Proofs →](B04_Matrix_Proofs.md)
