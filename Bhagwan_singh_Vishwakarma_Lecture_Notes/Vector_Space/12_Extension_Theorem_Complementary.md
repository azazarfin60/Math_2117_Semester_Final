# Lecture 12: Vector Space - Extension Theorem and Complementary Spaces

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 12 of 27
> **Video**: https://www.youtube.com/watch?v=WBvroWQecEI

---

**Navigation**
[< Previous Lecture](11_Existence_Dimension_Theorem.md) | [Index](README.md) | [Next Lecture >](13_Dimension_Sum_Proof.md)

---

## Prerequisites
We know that every finite-dimensional vector space has a basis (Existence Theorem) and that every basis of a specific space has exactly the same number of elements (Dimension Theorem). 
Today, we look at how to build a basis from scratch if we already have a few linearly independent vectors.

---

## The Extension Theorem

What happens if you have a linearly independent set, but it is too small to span the entire space? Can you force it to become a basis?

**Theorem:** Every linearly independent subset of a finitely generated vector space $V(F)$ is either already a basis of $V$, or can be extended to form a basis of $V$.

**Proof:**
Let $\dim(V) = n$. This means any basis of $V$ must have exactly $n$ elements.
Let

$$
S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_m \rbrace
$$

be a linearly independent subset of $V$. Because it is linearly independent, $m \le n$.
Let

$$
S' = \lbrace \beta_1, \beta_2, \dots, \beta_n \rbrace
$$

be a known basis of $V$.

We will merge these two sets by putting our independent alphas at the front:

$$
S_1 = \lbrace \alpha_1, \dots, \alpha_m, \beta_1, \dots, \beta_n \rbrace
$$

Because $S'$ is a basis, it generates $V$. Since $S'$ is completely inside $S_1$, $S_1$ must also generate $V$. But $S_1$ has $m+n$ elements, which is more than $n$, so it is definitely linearly dependent.

Since $S_1$ is linearly dependent, some vector inside it is a linear combination of its preceding vectors.
Which vector is redundant? It **cannot** be one of the alphas, because the alphas form a linearly independent set on their own. Therefore, the redundant vector must be one of the betas. Let us call it $\beta_i$.

We remove $\beta_i$ to form $S_2$:

$$
S_2 = \lbrace \alpha_1, \dots, \alpha_m, \beta_1, \dots, \beta_{i-1}, \beta_{i+1}, \dots, \beta_n \rbrace
$$

Because the vector we removed was a linear combination of the others, $S_2$ still generates $V$.
If $S_2$ is linearly independent, it is our basis. If not, we repeat the process. We find the next redundant beta vector and remove it. 

We repeat this until the set becomes linearly independent. Because the final set must generate $V$ and be linearly independent, it must contain exactly $n$ elements (by the Dimension Theorem).
Since we never remove any alphas, our final basis will contain all $m$ alphas and exactly $n-m$ betas.
Thus, our original linearly independent set $S$ has been successfully extended into a basis.

---

## The Maximum Size of Independent Sets

If you know the dimension of a space, you immediately know the absolute limit on how many independent vectors you can have.

**Theorem:** If $V(F)$ is a finitely generated vector space of dimension $n$, then any set containing $n+1$ or more vectors is linearly dependent.

**Proof (by contradiction):**
Assume we have a set $S$ with $n+1$ vectors that is linearly independent.
By the Extension Theorem, we can extend $S$ to form a basis of $V$.
Because $S$ already has $n+1$ vectors, the resulting basis must have *at least* $n+1$ vectors.
But the Dimension Theorem states that every basis of $V$ must have exactly $n$ vectors. A basis cannot have $n$ vectors and $n+1$ vectors at the same time.
This is a contradiction. Therefore, our assumption was wrong. Any set with $n+1$ or more vectors must be linearly dependent.

---

## Shortcuts for Finding a Basis

If you know $\dim(V) = n$, you do not always need to check both conditions (independence and spanning) to prove a set of $n$ vectors is a basis. You only need to check one!

### Shortcut 1: Checking Independence Only
**Theorem:** If $\dim(V) = n$, then any set of exactly $n$ linearly independent vectors in $V$ forms a basis of $V$.
**Proof:** Let $S$ have $n$ independent vectors. If $S$ does not span $V$, we could use the Extension Theorem to add vectors to it to make it a basis. But adding vectors would make the basis have more than $n$ elements, violating the Dimension Theorem. Thus, $S$ must already span $V$. It is a basis.

### Shortcut 2: Checking Spanning Only
**Theorem:** If $\dim(V) = n$, then any set of exactly $n$ vectors that generates $V$ is a basis of $V$.
**Proof:** Let $S$ have $n$ generating vectors. If $S$ were linearly dependent, we could remove redundant vectors and still generate $V$, leaving us with a generating set of fewer than $n$ vectors. We could then shrink it to a basis with fewer than $n$ elements, violating the Dimension Theorem. Thus, $S$ must be linearly independent. It is a basis.

---

## Unique Representation Theorem

**Theorem:** Let

$$
S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace
$$

be a basis of $V(F)$. Then any vector $\alpha \in V$ can be **uniquely** expressed as a linear combination of the elements of $S$.

**Proof:**
Suppose $\alpha$ can be expressed in two different ways:

$$
\alpha = a_1\alpha_1 + a_2\alpha_2 + \dots + a_n\alpha_n
$$

$$
\alpha = b_1\alpha_1 + b_2\alpha_2 + \dots + b_n\alpha_n
$$

Subtract the two equations:

$$
\bar{0} = (a_1 - b_1)\alpha_1 + (a_2 - b_2)\alpha_2 + \dots + (a_n - b_n)\alpha_n
$$

Because $S$ is a basis, its vectors are linearly independent. The only way their combination equals zero is if all scalar coefficients are exactly zero.

$$
a_1 - b_1 = 0 \implies a_1 = b_1
$$

$$
a_n - b_n = 0 \implies a_n = b_n
$$

The coefficients are identical. The representation is unique.

---

## Subspaces and Dimensions

### Dimension of a Subspace
**Theorem:** If $W$ is a subspace of a finite-dimensional vector space $V(F)$, then $\dim(W) \le \dim(V)$.
**Proof:**
Let $\dim(V) = n$. Because $W$ is inside $V$, any independent set in $W$ is also an independent set in $V$. Since no independent set in $V$ can have more than $n$ vectors, the largest independent set we can find in $W$ can have at most $n$ vectors. Let this maximal independent set have $m$ vectors ($m \le n$). Because it is maximal, adding any other vector from $W$ makes it dependent, meaning it spans $W$. It is a basis for $W$. Thus, $\dim(W) = m \le n$.

### Existence of a Complementary Subspace
**Theorem:** If $W_1$ is a subspace of $V(F)$ where $\dim(V) = n$, there exists another subspace $W_2$ such that the whole space is their direct sum:

$$
V = W_1 \oplus W_2
$$

. Also,

$$
\dim(W_2) = n - \dim(W_1).
$$

**Proof:**
Let

$$
\dim(W_1) = m
$$

. Let

$$
S_1 = \lbrace \alpha_1, \dots, \alpha_m \rbrace
$$

be a basis of $W_1$.
Since $S_1$ is linearly independent in $V$, we use the Extension Theorem to expand it to a full basis of $V$:

$$
S = \lbrace \alpha_1, \dots, \alpha_m, \alpha_{m+1}, \dots, \alpha_n \rbrace
$$

We group the newly added vectors to form our complementary subspace:

$$
W_2 = L(\lbrace \alpha_{m+1}, \dots, \alpha_n \rbrace)
$$

Because $S$ is a basis for $V$, every vector in $V$ can be built uniquely by taking some combination of the first $m$ vectors (which lives in $W_1$) and adding it to a combination of the last $n-m$ vectors (which lives in $W_2$).
Since the representation is unique,

$$
V = W_1 \oplus W_2.
$$

The dimension of $W_2$ is exactly $n - m$, which is $n - \dim(W_1)$.

## Key Takeaways
*   You can always build a full basis starting from any independent set.
*   A space of dimension $n$ cannot hold more than $n$ independent vectors.
*   If you have exactly $n$ vectors in an $n$-dimensional space, checking just independence OR just spanning is enough to prove they are a basis.
*   Coordinates (coefficients) relative to a basis are always unique.
*   Every subspace has a complementary subspace that "fills in the rest" of the main vector space via direct sum.

---

**Navigation**
[< Previous Lecture](11_Existence_Dimension_Theorem.md) | [Index](README.md) | [Next Lecture >](13_Dimension_Sum_Proof.md)
