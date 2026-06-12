[← Previous: C08 Kernel and Image](C08_Kernel_Image_Rank_Nullity.md) | [Index](00_Index.md) | [Next: C10 Inner Product Spaces →](C10_Inner_Product_Spaces.md)

---

# C09: Matrix Representation and Change of Basis

> **Exam Weight**: Tier 3 | **Appeared in**: Curriculum Reference | **Typical Marks**: 3–4

Every linear transformation between finite-dimensional vector spaces can be entirely represented by a matrix. Changing the basis of the vector space changes the matrix representation in a predictable way.

---

## Matrix Representation of a Linear Operator

Let $T: V \to V$ be a linear operator on a vector space $V$ with dimension $n$.
Let

$$
B = \lbrace v_1, v_2, \dots, v_n\rbrace
$$

be a basis for $V$.

When you apply the transformation $T$ to the first basis vector $v_1$, the result $T(v_1)$ is still a vector in $V$. Therefore, it can be written as a linear combination of the basis vectors:

$$
T(v_1) = a_{11}v_1 + a_{21}v_2 + \dots + a_{n1}v_n
$$

The coefficients

$$
(a_{11}, a_{21}, \dots, a_{n1})
$$

form the **first column** of the matrix representation $[T]_B$.
You repeat this for every basis vector. The resulting $n \times n$ matrix is the **Matrix Representation** of the linear operator.

---

## Change of Basis Matrix

Suppose you have two different bases for the same vector space $V$: an old basis $B$ and a new basis $B'$.
You can write each vector of the *new* basis $B'$ as a linear combination of the *old* basis $B$. 

Taking the column coefficients of these combinations creates the **Change of Basis Matrix** (or Transition Matrix), denoted as $P$. 
- The matrix $P$ converts coordinates from the new basis to the old basis:

$$
[x]_B = P[x]_{B'}.
$$

- The inverse matrix $P^{-1}$ converts coordinates from the old basis to the new basis:

$$
[x]_{B'} = P^{-1}[x]_B.
$$

---

## Similarity and Matrix Equivalency

When you change the basis of the vector space from $B$ to $B'$, the matrix representation of the linear operator $T$ also changes.

If

$$
[T]_B = A
$$

(the matrix in the old basis) and

$$
[T]_{B'} = C
$$

(the matrix in the new basis), they are related by the formula:

$$
C = P^{-1} A P
$$

Two matrices $A$ and $C$ that satisfy this relationship for some invertible matrix $P$ are called **Similar Matrices**.
Similar matrices represent the *exact same linear transformation*, just viewed from the perspective of two different coordinate systems. Because they represent the same transformation, similar matrices share identical:
- Determinants
- Traces
- Eigenvalues

---

## Exam Patterns
- While deep calculations involving Change of Basis rarely appear in short exams, understanding the formula

$$
C = P^{-1} A P
$$

is critical for diagonalization questions (which appear in the Matrix Theory sections).

---

[← Previous: C08 Kernel and Image](C08_Kernel_Image_Rank_Nullity.md) | [Index](00_Index.md) | [Next: C10 Inner Product Spaces →](C10_Inner_Product_Spaces.md)
