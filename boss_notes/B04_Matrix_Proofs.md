[← Previous: B03 Hermitian and Special Matrices](B03_Hermitian_SkewHermitian_Special_Matrices.md) | [Index](00_Index.md) | [Next: B05 Row Echelon Form and Rank →](B05_Row_Echelon_Form_Rank.md)

---

# B04: Matrix Proofs

> **Exam Weight**: Tier 2 | **Appeared in**: 2017, 2018, 2020, 2023 | **Typical Marks**: 3–5

These are standard proofs that appear regularly. They test whether you understand matrix algebra rules. Each proof is short and worth learning by heart.

---

## Proof 1: Transpose of a Product (PYQ 2020)

### Statement

For matrices $A$ (of size $m \times n$) and $B$ (of size $n \times p$):

$$
(AB)^T = B^T A^T
$$

The order reverses when you transpose a product.

### Proof

Let $C = AB$. The $(i,j)$-th element of $C$ is:

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$$

The $(i,j)$-th element of $C^T$ is $c_{ji}$:

$$
(C^T)_{ij} = c_{ji} = \sum_{k=1}^{n} a_{jk} b_{ki}
$$

Now consider $B^T A^T$. Its $(i,j)$-th element is:

$$
(B^T A^T)_{ij} = \sum_{k=1}^{n} (B^T)_{ik}(A^T)_{kj} = \sum_{k=1}^{n} b_{ki} \cdot a_{jk} = \sum_{k=1}^{n} a_{jk} b_{ki}
$$

Since $(C^T)_{ij} = (B^T A^T)_{ij}$ for all $i,j$:

$$
(AB)^T = B^T A^T \qquad \blacksquare
$$

---

## Proof 2: Inverse of a Product (PYQ 2018, 2023 — Repeated)

### Statement

If $A$ and $B$ are non-singular matrices of the same order:

$$
(AB)^{-1} = B^{-1}A^{-1}
$$

### Proof

We show that $B^{-1}A^{-1}$ satisfies the definition of the inverse of $AB$.

**Left product**:

$$
(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I
$$

**Right product**:

$$
(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I
$$

Since $(AB)(B^{-1}A^{-1}) = I$ and $(B^{-1}A^{-1})(AB) = I$:

$$
(AB)^{-1} = B^{-1}A^{-1} \qquad \blacksquare
$$

---

## Proof 3: Power of Inverse (PYQ 2018)

### Statement

For any invertible matrix $A$ and positive integer $n$:

$$
(A^{-1})^n = (A^n)^{-1}
$$

### Proof (by induction)

**Base case** ($n = 1$): $(A^{-1})^1 = (A^1)^{-1}$. True.

**Inductive step**: Assume $(A^{-1})^k = (A^k)^{-1}$ holds for some $k$.

For $n = k + 1$:

$$
(A^{k+1})^{-1} = (A^k \cdot A)^{-1} = A^{-1} \cdot (A^k)^{-1}
$$

using Proof 2. By the inductive hypothesis, $(A^k)^{-1} = (A^{-1})^k$:

$$
A^{-1} \cdot (A^{-1})^k = (A^{-1})^{k+1}
$$

The statement holds for $k + 1$. By induction, it holds for all positive integers $n$.

$$
\blacksquare
$$

---

## Proof 4: Rotation Matrix Property (PYQ 2017)

### Statement

If

$$
A_\alpha =
\begin{pmatrix}
\cos\alpha & \sin\alpha \\
-\sin\alpha & \cos\alpha
\end{pmatrix}
$$

then $A_\alpha \cdot A_\beta = A_{\alpha+\beta} = A_\beta \cdot A_\alpha$.

### Proof

Multiply $A_\alpha \cdot A_\beta$:

$$
A_\alpha \cdot A_\beta =
\begin{pmatrix}
\cos\alpha\cos\beta - \sin\alpha\sin\beta & \cos\alpha\sin\beta + \sin\alpha\cos\beta \\
-\sin\alpha\cos\beta - \cos\alpha\sin\beta & -\sin\alpha\sin\beta + \cos\alpha\cos\beta
\end{pmatrix}
$$

Apply the angle addition formulas:

$$
\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta
$$

$$
\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta
$$

Substitute:

$$
A_\alpha \cdot A_\beta =
\begin{pmatrix}
\cos(\alpha+\beta) & \sin(\alpha+\beta) \\
-\sin(\alpha+\beta) & \cos(\alpha+\beta)
\end{pmatrix} = A_{\alpha+\beta}
$$

Since $\alpha + \beta = \beta + \alpha$:

$$
A_{\alpha+\beta} = A_{\beta+\alpha} = A_\beta \cdot A_\alpha \qquad \blacksquare
$$

---

## Proof 5: Singular Matrix Definition

### Statement

A square matrix $A$ is singular if $\lvert A \rvert = 0$. It is non-singular if $\lvert A \rvert \neq 0$.

A singular matrix has no inverse. A non-singular matrix is invertible and $A^{-1} = \frac{1}{\lvert A \rvert}\text{adj}(A)$.

This definition is often asked as a 1-2 mark opener before a proof question.

---

## Exam Patterns

- The $(AB)^{-1} = B^{-1}A^{-1}$ proof has appeared in 2018 and 2023. This is the most important proof.
- The $(AB)^T = B^T A^T$ proof appeared in 2020.
- The rotation matrix property appeared in 2017.
- These proofs are short (5-8 lines each). Write them neatly with clear steps.
- Always state what you need to prove before starting.

---

[← Previous: B03 Hermitian and Special Matrices](B03_Hermitian_SkewHermitian_Special_Matrices.md) | [Index](00_Index.md) | [Next: B05 Row Echelon Form and Rank →](B05_Row_Echelon_Form_Rank.md)
