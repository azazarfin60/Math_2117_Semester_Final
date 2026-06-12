# Lecture 05: Vector Space - Concept of Linear Sum, Direct Sum & Linear Span

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 05 of 27
> **Video**: https://www.youtube.com/watch?v=kSyYgXvBpQQ

---

**Navigation**
[< Previous Lecture](04_Intersection_Union_Subspaces.md) | [Index](README.md) | [Next Lecture >](06_Linear_Independence_Dependence.md)

---

## Prerequisites
Before we dive into creating sums from different subspaces, we need to know how to combine vectors using scalars. This is the foundation for creating sets like the linear span.

## Linear Combination of Vectors
If we are given a set of vectors, we can mix them together using scalars to create a new vector. This process is called forming a linear combination.

Let

$$
\alpha_1, \alpha_2, \ldots, \alpha_n
$$

be vectors in a vector space $V(F)$.
Let $a_1, a_2, \ldots, a_n \in F$ be scalars from our field.

The **linear combination** of these vectors is defined as:

$$
\sum_{i=1}^n a_i \alpha_i = a_1 \alpha_1 + a_2 \alpha_2 + \cdots + a_n \alpha_n = \alpha
$$

Because vector spaces are closed under scalar multiplication and vector addition, the result $\alpha$ is always a new vector that belongs to $V(F)$.

---

## Linear Span of a Set
What happens if we take a set of vectors and form *every possible* linear combination using every possible scalar from the field? We generate a massive set of new vectors. This new set is called the linear span.

Let

$$
S = \lbrace \alpha_1, \alpha_2, \ldots, \alpha_n \rbrace \subseteq V(F)
$$

be a set of vectors.

The **linear span** of $S$, denoted by $L(S)$ or $L[S]$, is the set of all possible linear combinations of the vectors in $S$.

$$
L(S) = \left\lbrace \sum_{i=1}^n a_i \alpha_i \mid a_i \in F \text{ and } \alpha_i \in S \right\rbrace
$$

Since every linear combination gives us a vector in $V(F)$, the linear span is itself a subset of the vector space: $L(S) \subseteq V(F)$. The linear span represents the entire space that can be built or "reached" using just the vectors in $S$.

---

## Linear Sum of Two Subspaces
Now let us look at combining two different subspaces. We already learned that the union of two subspaces is usually not a subspace. However, we can create a new subspace by adding them together element by element.

Let $W_1$ and $W_2$ be two vector subspaces of $V(F)$.

The **linear sum** of $W_1$ and $W_2$ is denoted by $W_1 + W_2$ and is defined as:

$$
W_1 + W_2 = \lbrace \alpha_1 + \beta_1 \mid \alpha_1 \in W_1 \text{ and } \beta_1 \in W_2 \rbrace
$$

In simple terms, you pick one vector from $W_1$ and one vector from $W_2$, add them together, and place the result in the new set.

### Proving the Linear Sum is a Subspace
We can easily prove that $W_1 + W_2$ is a vector subspace of $V(F)$ using the one-step test.

Let us pick two vectors $\alpha$ and $\beta$ from $W_1 + W_2$.
By definition, they must be formed by sums:
*

$$
\alpha = \alpha_1 + \alpha_2
$$

*

$$
\beta = \beta_1 + \beta_2
$$

where $\alpha_1, \beta_1 \in W_1$ and $\alpha_2, \beta_2 \in W_2$.

Now, let $a, b \in F$ be any two scalars. We check their linear combination:

$$
a\alpha + b\beta = a(\alpha_1 + \alpha_2) + b(\beta_1 + \beta_2)
$$

Distribute the scalars:

$$
= (a\alpha_1 + a\alpha_2) + (b\beta_1 + b\beta_2)
$$

Rearrange to group the $W_1$ terms together and the $W_2$ terms together:

$$
= (a\alpha_1 + b\beta_1) + (a\alpha_2 + b\beta_2)
$$

Because $W_1$ is a subspace, the combination $(a\alpha_1 + b\beta_1)$ belongs to $W_1$.
Because $W_2$ is a subspace, the combination $(a\alpha_2 + b\beta_2)$ belongs to $W_2$.

Thus, our new vector $a\alpha + b\beta$ is written exactly as a sum of a vector in $W_1$ and a vector in $W_2$. Therefore:

$$
a\alpha + b\beta \in W_1 + W_2
$$

This proves that the linear sum $W_1 + W_2$ is a vector subspace of $V(F)$.

---

## Direct Sum of Two Subspaces
A direct sum is a special, strict version of the linear sum.

Let $W_1$ and $W_2$ be two subspaces of $V(F)$.
The **direct sum** of $W_1$ and $W_2$ is denoted by $W_1 \oplus W_2$.

It is defined identically to the linear sum, but with one critical rule: **every element is uniquely represented**.
This means if you write a vector $\alpha \in W_1 \oplus W_2$ as

$$
\alpha = \alpha_1 + \beta_1
$$

, there is absolutely no other pair of vectors from $W_1$ and $W_2$ that can sum to $\alpha$.

### The Direct Sum Characterization Theorem
This theorem gives us an easy way to check if a regular sum is actually a direct sum.

**Theorem:** A vector space $V$ is the direct sum of $W_1$ and $W_2$ (

$$
V = W_1 \oplus W_2
$$

) if and only if two conditions hold:
1.

$$
V = W_1 + W_2
$$

(It is a linear sum)
2.

$$
W_1 \cap W_2 = \lbrace \bar{0} \rbrace
$$

(Their intersection contains only the zero vector)

**Proof Part 1: Condition is necessary**
Assume

$$
V = W_1 \oplus W_2.
$$

By definition, every element is a sum, so condition 1 (

$$
V = W_1 + W_2
$$

) holds automatically.
To prove condition 2, suppose for a contradiction that the intersection contains a non-zero vector $\alpha \neq \bar{0}$.
Since $\alpha$ is in both $W_1$ and $W_2$, we can write $\alpha$ in two ways:
*   First way: $\alpha = \alpha + \bar{0}$ (where $\alpha \in W_1$ and $\bar{0} \in W_2$)
*   Second way: $\alpha = \bar{0} + \alpha$ (where $\bar{0} \in W_1$ and $\alpha \in W_2$)

This gives us two different representations for the same vector $\alpha$. But we assumed $V$ is a direct sum, which requires uniqueness. This is a contradiction. Thus, our assumption was wrong, and $W_1 \cap W_2$ can only contain the zero vector.

**Proof Part 2: Condition is sufficient**
Assume

$$
V = W_1 + W_2
$$

and

$$
W_1 \cap W_2 = \lbrace \bar{0} \rbrace
$$

. We must prove the representation is unique.
Let us suppose a vector $\alpha$ has two representations:

$$
\alpha = \alpha_1 + \beta_1
$$

$$
\alpha = \alpha_2 + \beta_2
$$

where $\alpha_1, \alpha_2 \in W_1$ and $\beta_1, \beta_2 \in W_2$.

Equate them:

$$
\alpha_1 + \beta_1 = \alpha_2 + \beta_2
$$

Rearrange to put $W_1$ elements on the left and $W_2$ elements on the right:

$$
\alpha_1 - \alpha_2 = \beta_2 - \beta_1
$$

Since $W_1$ is a subspace, the left side $(\alpha_1 - \alpha_2)$ is in $W_1$.
Since $W_2$ is a subspace, the right side $(\beta_2 - \beta_1)$ is in $W_2$.
Because the two sides are equal, this element must belong to both $W_1$ and $W_2$:

$$
\alpha_1 - \alpha_2 \in W_1 \cap W_2
$$

But we assumed the intersection only contains the zero vector. So:

$$
\alpha_1 - \alpha_2 = \bar{0} \implies \alpha_1 = \alpha_2
$$

$$
\beta_2 - \beta_1 = \bar{0} \implies \beta_1 = \beta_2
$$

Since the elements are exactly the same, the representation is unique. Therefore,

$$
V = W_1 \oplus W_2.
$$

---

## Key Takeaways
*   A **linear combination** scales vectors and adds them together.
*   The **linear span** is the set of all possible linear combinations of a set.
*   The **linear sum** $W_1 + W_2$ is always a subspace.
*   A **direct sum** $W_1 \oplus W_2$ is a sum where every element is uniquely formed.
*   A sum is a direct sum if and only if the subspaces share nothing but the zero vector (

$$
W_1 \cap W_2 = \lbrace \bar{0} \rbrace
$$

).

## What Comes Next
Next, we will discuss linear independence and dependence, which helps us understand when vectors are truly unique or if they are just linear combinations of each other.

---

**Navigation**
[< Previous Lecture](04_Intersection_Union_Subspaces.md) | [Index](README.md) | [Next Lecture >](06_Linear_Independence_Dependence.md)
