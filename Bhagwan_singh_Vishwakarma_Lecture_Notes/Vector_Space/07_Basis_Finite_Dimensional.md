# Lecture 07: Vector Space - Basis and Finite Dimensional Vector Space

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 07 of 27
> **Video**: https://www.youtube.com/watch?v=pG-IAFOiOw4

---

**Navigation**
[< Previous Lecture](06_Linear_Independence_Dependence.md) | [Index](README.md) | [Next Lecture >](08_Dimension_Sum_Subspace.md)

---

## Prerequisites
We know how to determine if a set of vectors is linearly independent (L.I.) or linearly dependent (L.D.). Today, we look at the properties of these sets and how they lead us to the concept of a basis.

## Properties of Linearly Independent and Dependent Sets
Before defining a basis, let us establish four critical properties of vector sets:

1.  **Subsets of L.I. Sets:** If a set of vectors $S$ is linearly independent, then any subset $S'$ taken from $S$ is also linearly independent.
2.  **Supersets of L.D. Sets:** If a set of vectors $S$ is linearly dependent, then any superset $S_1$ (where $S \subseteq S_1$) is also linearly dependent. Adding more vectors to a dependent set cannot make it independent.
3.  **Redundancy in L.D. Sets:** In any linearly dependent set of vectors

$$
S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace
$$

, there is always at least one vector $\alpha_i$ that can be written as a linear combination of the vectors preceding it.
4.  **Breaking L.I. Sets:** If you take a linearly independent set $S$ and add a new vector $\alpha_m$ that is already in the linear span of $S$, the new, larger set becomes linearly dependent.

---

## Basis of a Vector Space

We know that the linear span $L(S)$ of a set $S$ is the collection of all vectors you can build using $S$.
If $S$ can build the entire vector space $V(F)$ such that $L(S) = V(F)$, we say that $S$ **spans** or **generates** $V(F)$.

A **Basis** is simply the most efficient, minimal set of vectors needed to build the entire space.

Let $V(F)$ be a vector space over the field $F$. A subset $S$ of $V(F)$ is called a **basis** of $V(F)$ if it satisfies two conditions:
1.  **$S$ is a linearly independent set.** (No vector is redundant; there is no wasted effort).
2.  **$L(S) = V(F)$.** (Every element of $V(F)$ can be represented as a linear combination of a finite number of elements of $S$).

### Finite Dimensional Vector Space
A vector space $V(F)$ is called a **finite dimensional vector space** (or finitely generated vector space) if there exists a finite subset $S$ such that $L(S) = V(F)$.
If the set that generates the whole space has a finite number of elements, the space itself is finite dimensional.

Because a basis generates the space ($L(S) = V(F)$) and is linearly independent, any finite dimensional vector space will have a basis with a finite number of elements.

---

## Dimension of a Vector Space

There are two fundamental theorems regarding the dimension of a space:
1.  Every finite dimensional vector space has at least one basis.
2.  While a vector space can have many different bases, **every basis will have exactly the same number of elements**.

Because this number is strictly fixed, we use it to define the dimension of the space.

**Definition:** The **dimension** of a finite dimensional vector space $V(F)$ is the exact number of elements in its basis.
It is denoted by $\text{dim}(V(F))$ or simply $\text{dim } V$.

### Examples of Standard Dimensions
*   **1D Space:** For the real line $\mathbb{R}$, $\text{dim}(\mathbb{R}) = 1$.
*   **2D Space:** For the coordinate plane $\mathbb{R}^2$, the standard basis is $\lbrace (1, 0), (0, 1) \rbrace$. Thus,

$$
\text{dim}(\mathbb{R}^2) = 2.
$$

*   **3D Space:** For $\mathbb{R}^3$, the standard basis is $\lbrace (1, 0, 0), (0, 1, 0), (0, 0, 1) \rbrace$. Thus,

$$
\text{dim}(\mathbb{R}^3) = 3.
$$

*   **N-Dimensional Space:** For $\mathbb{R}^n$ (the space of $n$-tuples), the standard basis has $n$ elements. Thus,

$$
\text{dim}(\mathbb{R}^n) = n.
$$

---

## Numerical Examples: Finding a Basis

How do we prove a set of vectors is a basis, or find the basis of a generated subspace? We use matrices.

### Example 1: Verifying a Basis
**Question:** Show that the set $S = \lbrace (1, 0, 0), (1, 1, 0), (1, 1, 1) \rbrace$ is a basis for $\mathbb{R}^3(\mathbb{R})$.

**Solution:**
We must check two things: Are there enough vectors to span the space, and are they linearly independent?
Since

$$
\text{dim}(\mathbb{R}^3) = 3
$$

, any basis must have exactly 3 vectors. Our set $S$ has 3 vectors. So, we only need to prove they are linearly independent.

We form the coefficient matrix $A$ using the vectors as rows:

$$
A =
\begin{bmatrix}
1 & 0 & 0 \\
1 & 1 & 0 \\
1 & 1 & 1
\end{bmatrix}
$$

Calculate the determinant $\lvert A \rvert$:

$$
|A| = 1(1 \cdot 1 - 0 \cdot 1) - 0 + 0 = 1
$$

Since

$$
\lvert A \rvert = 1 \neq 0
$$

, the vectors are linearly independent. Because we have 3 linearly independent vectors in a 3-dimensional space, they automatically span the space. Thus, $S$ is a basis for $\mathbb{R}^3(\mathbb{R})$.

### Example 2: Finding the Basis of a Subspace
**Question:** Find a basis and the dimension of the subspace $W$ of $\mathbb{R}^4(\mathbb{R})$ generated by:

$$
\alpha_1 = (1, -2, 5, -3), \quad \alpha_2 = (2, 3, 1, -4), \quad \alpha_3 = (3, 8, -3, 5)
$$

**Solution:**
These three vectors generate $W$. But to find the basis, we must remove any redundant vectors so only the linearly independent ones remain. We do this by reducing their matrix to Echelon form.

Construct matrix $A$ with the vectors as rows:

$$
A =
\begin{bmatrix}
1 & -2 & 5 & -3 \\
2 & 3 & 1 & -4 \\
3 & 8 & -3 & 5
\end{bmatrix}
$$

Apply elementary row operations to create zeros below the leading diagonal (Echelon form).
1. $R_2 \to R_2 - 2R_1$
2. $R_3 \to R_3 - 3R_1$

This simplifies to:

$$
\begin{bmatrix}
1 & -2 & 5 & -3 \\
0 & 7 & -9 & 2 \\
0 & 14 & -18 & 4
\end{bmatrix}
$$

Now, clear the 14 in the third row:
3. $R_3 \to R_3 - 2R_2$

$$
\begin{bmatrix}
1 & -2 & 5 & -3 \\
0 & 7 & -9 & 2 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

The third row became completely zero, meaning vector $\alpha_3$ was redundant (it was a combination of $\alpha_1$ and $\alpha_2$).
The non-zero rows left in the Echelon form give us our linearly independent basis vectors.

$$
\text{Basis}(W) = \lbrace (1, -2, 5, -3), (0, 7, -9, 2) \rbrace
$$

Because there are 2 vectors in this basis, the dimension is:

$$
\text{dim}(W) = 2
$$

---

## Key Takeaways
*   A **basis** is a set of linearly independent vectors that spans the entire vector space.
*   The **dimension** of a space is the exact number of elements in its basis.
*   To check if vectors form a basis, place them in a matrix and check the determinant. If $\lvert A \rvert \neq 0$, they are a basis.
*   To find the basis of a spanned subspace, place the generating vectors in a matrix, reduce to Echelon form, and the remaining non-zero rows form the basis.

## What Comes Next
We now understand how the dimension of a single subspace is calculated. Next, we will learn how to calculate the dimension when we add two subspaces together using the Dimension Sum Theorem.

---

**Navigation**
[< Previous Lecture](06_Linear_Independence_Dependence.md) | [Index](README.md) | [Next Lecture >](08_Dimension_Sum_Subspace.md)
