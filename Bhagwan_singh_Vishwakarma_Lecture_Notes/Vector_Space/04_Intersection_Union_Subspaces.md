# Lecture 04: Vector Space - Intersection and Union of Vector Subspaces

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 04 of 27
> **Video**: https://www.youtube.com/watch?v=QZi8OqYSLgU

---

**Navigation**
[< Previous Lecture](03_Vector_Subspace.md) | [Index](README.md) | [Next Lecture >](05_Linear_Sum_Direct_Sum_Span.md)

---

## Prerequisites
We know that a subset $W$ of a vector space $V(F)$ is a subspace if it behaves as a vector space itself. The one-step test says $W$ is a subspace if for all scalars $a, b$ and vectors $\alpha, \beta$ in $W$, the combination $a\alpha + b\beta$ is also in $W$.

Today we will use this theorem to see what happens when we combine two subspaces using intersections and unions.

---

## Intersection of Two Subspaces

When we take the intersection of two vector subspaces, we look at all the vectors they share. We will prove that this intersection forms a brand new subspace.

**Theorem:** Prove that the intersection of two vector subspaces of a vector space is also a vector subspace.

**Proof:**
Let $W_1$ and $W_2$ be two vector subspaces of $V(F)$. We want to prove that $W_1 \cap W_2$ is a vector subspace.

First, we must show that the intersection is not an empty set.
Since $W_1$ and $W_2$ are both subspaces, they act as vector spaces under addition. This means the additive identity, which is the zero vector $\bar{0}$, must exist in both.
*   $\bar{0} \in W_1$
*   $\bar{0} \in W_2$

Since the zero vector is in both sets, it must be in their intersection:

$$
\bar{0} \in W_1 \cap W_2
$$

This proves that $W_1 \cap W_2$ is non-empty.

Now we will use the one-step subspace theorem.
Let us choose two arbitrary vectors $\alpha$ and $\beta$ from the intersection:

$$
\alpha, \beta \in W_1 \cap W_2
$$

Since these vectors are in the intersection, they belong to both sets individually:
*   $\alpha, \beta \in W_1$
*   $\alpha, \beta \in W_2$

Now let us take any two scalars $a, b \in F$.

Since $W_1$ is a subspace, and $\alpha, \beta \in W_1$:

$$
a\alpha + b\beta \in W_1
$$

Since $W_2$ is a subspace, and $\alpha, \beta \in W_2$:

$$
a\alpha + b\beta \in W_2
$$

Because the vector sum $a\alpha + b\beta$ belongs to both $W_1$ and $W_2$, it must belong to their intersection:

$$
a\alpha + b\beta \in W_1 \cap W_2
$$

Thus, by the one-step subspace theorem, the intersection $W_1 \cap W_2$ is a vector subspace of $V(F)$.

---

## Union of Two Subspaces

The union of two sets contains all elements from the first set and all elements from the second set. Unlike the intersection, the union of two subspaces is **not always** a subspace. It only forms a subspace under a specific condition.

**Theorem:** If $W_1$ and $W_2$ are two subspaces of $V(F)$, prove that the union $W_1 \cup W_2$ is a vector subspace of $V(F)$ if and only if $W_1 \subseteq W_2$ or $W_2 \subseteq W_1$.

Because of the "if and only if" condition, we must prove this in both directions.

### Part 1: The condition is sufficient
We start by assuming that one subspace is contained in the other.
Let $W_1 \subseteq W_2$ or $W_2 \subseteq W_1$.

*   If $W_1 \subseteq W_2$, then all elements of $W_1$ are already in $W_2$. Thus, their union is simply the larger set: $W_1 \cup W_2 = W_2$. Since $W_2$ is given as a subspace, the union is a subspace.
*   If $W_2 \subseteq W_1$, then $W_1 \cup W_2 = W_1$. Since $W_1$ is given as a subspace, the union is a subspace.

In both cases, the union is just one of the original subspaces. So $W_1 \cup W_2$ is a subspace.

### Part 2: The condition is necessary
Now we prove the reverse direction. We assume that the union $W_1 \cup W_2$ is a vector subspace, and we must prove that one set is contained in the other ($W_1 \subseteq W_2$ or $W_2 \subseteq W_1$).

We will prove this by contradiction. We assume the opposite is true: neither set is contained in the other.
Suppose $W_1 \not\subseteq W_2$ and $W_2 \not\subseteq W_1$.

What does this mean?
*   Since $W_1$ is not contained in $W_2$, there is some vector $\alpha$ that belongs to $W_1$ but not $W_2$. Let's call this condition (1).
*   Since $W_2$ is not contained in $W_1$, there is some vector $\beta$ that belongs to $W_2$ but not $W_1$. Let's call this condition (2).

Since $\alpha \in W_1$ and $\beta \in W_2$, both vectors must belong to their union:

$$
\alpha, \beta \in W_1 \cup W_2
$$

We assumed that $W_1 \cup W_2$ is a subspace. This means it must be closed under vector addition. So, the sum of these two vectors must be in the union:

$$
\alpha + \beta \in W_1 \cup W_2
$$

If this sum is in the union, it must belong to either $W_1$ or $W_2$. Let us test both possibilities.

**Case A:** Suppose $\alpha + \beta \in W_1$.
We know $W_1$ is a subspace. We also know $\alpha \in W_1$. Because $W_1$ acts as a vector group, the additive inverse $-\alpha$ is also in $W_1$.
Since both $(\alpha + \beta)$ and $-\alpha$ are in $W_1$, their sum must be in $W_1$:

$$
(\alpha + \beta) + (-\alpha) \in W_1
$$

$$
\beta \in W_1
$$

But this directly contradicts condition (2), which states $\beta \notin W_1$.

**Case B:** Suppose $\alpha + \beta \in W_2$.
We know $W_2$ is a subspace, and $\beta \in W_2$. Thus, the additive inverse $-\beta \in W_2$.
Since both $(\alpha + \beta)$ and $-\beta$ are in $W_2$, their sum must be in $W_2$:

$$
(\alpha + \beta) + (-\beta) \in W_2
$$

$$
\alpha \in W_2
$$

But this directly contradicts condition (1), which states $\alpha \notin W_2$.

In both cases, we hit a solid contradiction. Our assumption that neither set was contained in the other must be wrong. Therefore, it is absolutely necessary that $W_1 \subseteq W_2$ or $W_2 \subseteq W_1$. The theorem is proven.

---

## Key Takeaways
*   The **intersection** of two vector subspaces is always a vector subspace.
*   The **union** of two vector subspaces is only a subspace if one is entirely contained within the other.
*   Proof by contradiction is a powerful tool when working with unions.

## What Comes Next
We will continue working with combinations of vectors. In the next lecture, we define what a linear combination is and learn about linear sums and direct sums.

---

**Navigation**
[< Previous Lecture](03_Vector_Subspace.md) | [Index](README.md) | [Next Lecture >](05_Linear_Sum_Direct_Sum_Span.md)
