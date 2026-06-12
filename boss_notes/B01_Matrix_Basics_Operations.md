[Index](00_Index.md) | [Next: B02 Transpose and Symmetric Matrices →](B02_Transpose_Symmetric_SkewSymmetric.md)

---

# B01: Matrix Basics and Operations

> **Exam Weight**: Tier 3 | **Typical Marks**: 2–3 (definition questions)

These fundamentals rarely appear as standalone problems. But they are the foundation for everything else. Knowing them helps you avoid careless mistakes.

---

## What is a Matrix?

A matrix is a rectangular array of numbers arranged in rows and columns. A matrix with $m$ rows and $n$ columns has order $m \times n$.

$$
A = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix}
$$

The element $a_{ij}$ sits in row $i$ and column $j$.

---

## Types of Matrices

| Type | Condition | Example |
|------|-----------|---------|
| **Square** | $m = n$ | 3x3 matrix |
| **Row** | $m = 1$ | $[1 \; 2 \; 3]$ |
| **Column** | $n = 1$ | $[1, 2]^T$ |
| **Diagonal** | $a_{ij} = 0$ for $i \neq j$ | Only diagonal entries non-zero |
| **Scalar** | Diagonal with all diagonal entries equal | $kI$ |
| **Identity** | Diagonal with all 1s | $I_n$ |
| **Null/Zero** | All entries are 0 | $O$ |
| **Upper triangular** | $a_{ij} = 0$ for $i > j$ | Zeros below diagonal |
| **Lower triangular** | $a_{ij} = 0$ for $i < j$ | Zeros above diagonal |

---

## Matrix Operations

### Addition and Subtraction

Add or subtract matrices of the same order by adding or subtracting corresponding entries:

$$
(A + B)_{ij} = a_{ij} + b_{ij}
$$

Addition is commutative: $A + B = B + A$.

### Scalar Multiplication

Multiply every entry by the scalar:

$$
(kA)_{ij} = k \cdot a_{ij}
$$

### Matrix Multiplication

$A$ ($m \times n$) times $B$ ($n \times p$) gives $C$ ($m \times p$). The $(i,j)$-th entry of $C$ is:

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$$

Multiplication is NOT commutative: $AB \neq BA$ in general.

Multiplication IS associative: $(AB)C = A(BC)$.

Multiplication IS distributive: $A(B + C) = AB + AC$.

### Important: Size Compatibility

You can only multiply $A_{m \times n}$ by $B_{n \times p}$. The inner dimensions must match. The result is $m \times p$.

---

## Determinant (Quick Reference)

For a 2x2 matrix:

$$
|A| = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
$$

For a 3x3 matrix, expand along row 1:

$$
|A| = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})
$$

Properties:
- If a row or column is all zeros, $\lvert A \rvert = 0$.
- Swapping two rows changes the sign of the determinant.
- $\lvert AB \rvert = \lvert A \rvert \cdot \lvert B \rvert$.
- $\lvert kA \rvert = k^n \lvert A \rvert$ for an $n \times n$ matrix.

---

[Index](00_Index.md) | [Next: B02 Transpose and Symmetric Matrices →](B02_Transpose_Symmetric_SkewSymmetric.md)
