# Lecture 08: Vector Space - Dimension of Sum of Subspaces

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 08 of 27
> **Video**: https://www.youtube.com/watch?v=itCTFw0d4hs

---

**Navigation**
[< Previous Lecture](07_Basis_Finite_Dimensional.md) | [Index](README.md) | [Next Lecture >](09_Theorems_Linear_Span.md)

---

## Prerequisites
We know that the dimension of a vector space is the exact number of vectors in its basis. We also know how to add two vector subspaces together using the linear sum $W_1 + W_2$, and the direct sum $W_1 \oplus W_2$. 

Today, we look at how to calculate the dimension of the resulting combined subspace.

---

## Dimension of the Sum of Subspaces

When we take the linear sum of two subspaces $W_1$ and $W_2$, the dimension of the resulting new subspace is related to the individual dimensions of $W_1$ and $W_2$. However, simply adding their dimensions is not enough, because they might share some vectors. We must subtract the overlap (their intersection).

**Theorem:** Let $W_1$ and $W_2$ be two subspaces of a finite dimensional vector space $V(F)$. The dimension of their linear sum is given by:

$$
\text{dim}(W_1 + W_2) = \text{dim}(W_1) + \text{dim}(W_2) - \text{dim}(W_1 \cap W_2)
$$

This formula works exactly like the principle of inclusion-exclusion in set theory (

$$
\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert
$$

). We add the dimensions of the two individual subspaces, but since the intersection $W_1 \cap W_2$ was counted twice (once in $W_1$ and once in $W_2$), we subtract its dimension to get the correct total.

---

## Special Case: Direct Sum

What happens if the sum is a direct sum?

We know that if $V$ is the direct sum of two subspaces,

$$
V = W_1 \oplus W_2
$$

, it means that every element has a unique representation.
By the direct sum characterization theorem, this uniqueness requires that their intersection contains only the zero vector:

$$
W_1 \cap W_2 = \lbrace \bar{0} \rbrace
$$

Since the set containing only the zero vector has a dimension of exactly zero:

$$
\text{dim}(W_1 \cap W_2) = 0
$$

We substitute this zero back into our main formula:

$$
\text{dim}(W_1 \oplus W_2) = \text{dim}(W_1) + \text{dim}(W_2) - 0
$$

This gives us a very clean and simple result. For a direct sum, the dimension of the combined space is simply the sum of the individual dimensions.

$$
\text{dim}(W_1 \oplus W_2) = \text{dim}(W_1) + \text{dim}(W_2)
$$

---

## Numerical Examples

Let us verify this formula using practical numerical examples.

### Example 1: Sum in 3D Space
Consider the three-dimensional vector space $V_3(\mathbb{R})$. Let us take two subspaces:

$$
W_1 = \lbrace (a, 0, 0) \mid a \in \mathbb{R} \rbrace
$$

$$
W_2 = \lbrace (0, a, b) \mid a, b \in \mathbb{R} \rbrace
$$

**Step 1: Find individual dimensions**
*   $W_1$ has only one free variable ($a$), so it is a one-dimensional subspace:

$$
\text{dim}(W_1) = 1.
$$

*   $W_2$ has two free variables ($a, b$), so it is a two-dimensional subspace:

$$
\text{dim}(W_2) = 2.
$$

**Step 2: Find the intersection**
What points do $W_1$ and $W_2$ have in common?
$W_1$ requires the last two coordinates to be zero. $W_2$ requires the first coordinate to be zero.
To be in both sets, all three coordinates must be zero.

$$
W_1 \cap W_2 = \lbrace (0, 0, 0) \rbrace
$$

Since the intersection contains only the zero vector, its dimension is $0$:

$$
\text{dim}(W_1 \cap W_2) = 0
$$

**Step 3: Calculate the dimension of the sum**
Using our formula:

$$
\text{dim}(W_1 + W_2) = \text{dim}(W_1) + \text{dim}(W_2) - \text{dim}(W_1 \cap W_2)
$$

$$
\text{dim}(W_1 + W_2) = 1 + 2 - 0 = 3
$$

The sum creates a 3-dimensional subspace, which covers the entire space $V_3(\mathbb{R})$. Because the intersection was zero, this was technically a direct sum.

### Example 2: Sum with Overlap in 4D Space
Now consider the four-dimensional vector space $V_4(\mathbb{R})$. Let us take two overlapping subspaces:

$$
W_1 = \lbrace (a, b, 0, 0) \mid a, b \in \mathbb{R} \rbrace
$$

$$
W_2 = \lbrace (0, a, b, c) \mid a, b, c \in \mathbb{R} \rbrace
$$

**Step 1: Find individual dimensions**
*   $W_1$ has two free variables, so

$$
\text{dim}(W_1) = 2.
$$

*   $W_2$ has three free variables, so

$$
\text{dim}(W_2) = 3.
$$

**Step 2: Find the intersection**
What points do they share?
$W_1$ says the 3rd and 4th coordinates must be zero.
$W_2$ says the 1st coordinate must be zero.
The 2nd coordinate is free to be anything in both sets.
Thus, the intersection is:

$$
W_1 \cap W_2 = \lbrace (0, a, 0, 0) \mid a \in \mathbb{R} \rbrace
$$

Because this intersection has one free variable, it is a one-dimensional subspace.

$$
\text{dim}(W_1 \cap W_2) = 1
$$

**Step 3: Calculate the dimension of the sum**

$$
\text{dim}(W_1 + W_2) = \text{dim}(W_1) + \text{dim}(W_2) - \text{dim}(W_1 \cap W_2)
$$

$$
\text{dim}(W_1 + W_2) = 2 + 3 - 1 = 4
$$

The linear sum results in a 4-dimensional subspace, which is the entire space $V_4(\mathbb{R})$.

---

## Key Takeaways
*   The dimension of the linear sum of two subspaces is:

$$
\text{dim}(W_1 + W_2) = \text{dim}(W_1) + \text{dim}(W_2) - \text{dim}(W_1 \cap W_2).
$$

*   If the sum is a **direct sum**, the intersection is zero, so the dimension is just the sum of the individual dimensions.
*   Always find the exact structure of the intersection to determine its dimension before calculating the sum.

## What Comes Next
We will prove several formal theorems regarding the linear span. These proofs will solidify our understanding of how vectors generate spaces before we move on to advanced theorems connecting independence and basis extension.

---

**Navigation**
[< Previous Lecture](07_Basis_Finite_Dimensional.md) | [Index](README.md) | [Next Lecture >](09_Theorems_Linear_Span.md)
