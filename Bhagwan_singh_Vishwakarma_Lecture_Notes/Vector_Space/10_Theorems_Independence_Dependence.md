# Lecture 10: Vector Space - Theorems on Linear Independence and Dependence

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 10 of 27
> **Video**: https://www.youtube.com/watch?v=wGiJkeuJDcM

---

**Navigation**
[< Previous Lecture](09_Theorems_Linear_Span.md) | [Index](README.md) | [Next Lecture >](11_Existence_Dimension_Theorem.md)

---

## Prerequisites
We know the basic definitions of linear independence and dependence. A set of vectors is **Linearly Independent (L.I.)** if the only way their linear combination equals the zero vector is when all scalars are zero. They are **Linearly Dependent (L.D.)** if you can make the combination equal to zero using at least one non-zero scalar.

Today, we will prove several theorems that describe the behavior of L.I. and L.D. sets.

---

## Basic Properties

### Property 1: The Zero Vector is Always Linearly Dependent
If a set contains only the zero vector, is it independent or dependent?
Let us form a linear combination:

$$
a \cdot \bar{0} = \bar{0}
$$

We can choose any non-zero scalar for $a$, for example, $a = 2$.

$$
2 \cdot \bar{0} = \bar{0}
$$

Because we found a non-zero scalar that satisfies the equation, the zero vector is, by definition, **Linearly Dependent**.

### Property 2: Any Set Containing the Zero Vector is Linearly Dependent
If a larger set of vectors contains the zero vector, the entire set becomes infected and is classified as linearly dependent.

**Proof:**
Let

$$
S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace
$$

be a set of vectors. Without loss of generality, let the first vector be the zero vector:

$$
\alpha_1 = \bar{0}.
$$

We form the linear combination:

$$
a_1\alpha_1 + a_2\alpha_2 + \dots + a_n\alpha_n = \bar{0}
$$

Because

$$
\alpha_1 = \bar{0}
$$

, we can choose its scalar $a_1$ to be any non-zero number, say

$$
a_1 = 1
$$

. For all the other vectors, we can just choose their scalars to be $0$.

$$
1 \cdot \bar{0} + 0 \cdot \alpha_2 + \dots + 0 \cdot \alpha_n = \bar{0}
$$

Since not all scalars are zero (specifically,

$$
a_1 = 1 \neq 0
$$

), the set $S$ is linearly dependent.

---

## Subsets and Supersets

### Theorem: Any Subset of a Linearly Independent Set is Linearly Independent
If a large group of vectors are all completely independent of each other, taking a smaller group from them will not suddenly make them dependent.

**Proof:**
Let

$$
S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace
$$

be a linearly independent set. By definition, if:

$$
a_1\alpha_1 + a_2\alpha_2 + \dots + a_n\alpha_n = \bar{0} \implies a_1 = a_2 = \dots = a_n = 0
$$

Let $S_1$ be a subset of $S$ containing the first $k$ vectors:

$$
S_1 = \lbrace \alpha_1, \alpha_2, \dots, \alpha_k \rbrace
$$

where $1 < k \le n$.
We want to prove $S_1$ is linearly independent. We set up its linear combination:

$$
a_1\alpha_1 + a_2\alpha_2 + \dots + a_k\alpha_k = \bar{0}
$$

We can rewrite this combination to look like the full set $S$ by adding the missing vectors and giving them scalar coefficients of exactly zero:

$$
a_1\alpha_1 + a_2\alpha_2 + \dots + a_k\alpha_k + 0\cdot\alpha_{k+1} + \dots + 0\cdot\alpha_n = \bar{0}
$$

This is now a linear combination of the full independent set $S$ that equals zero. Because $S$ is linearly independent, *every single scalar* in this equation must be zero.
Therefore:

$$
a_1 = 0, \quad a_2 = 0, \quad \dots, \quad a_k = 0
$$

Since the only solution for the subset's combination is all zeros, the subset $S_1$ is linearly independent.

### Lemma: Any Superset of a Linearly Dependent Set is Linearly Dependent
If a set is already linearly dependent (meaning it has redundant vectors), adding more vectors to it will not magically fix the redundancy.

**Proof:**
Let

$$
S = \lbrace \alpha_1, \dots, \alpha_n \rbrace
$$

be linearly dependent. This means there exist scalars $a_1, \dots, a_n$, not all zero, such that:

$$
a_1\alpha_1 + \dots + a_n\alpha_n = \bar{0}
$$

Let us add a new vector $\alpha$ to create a superset

$$
S_1 = \lbrace \alpha_1, \dots, \alpha_n, \alpha \rbrace.
$$

We can write a combination for $S_1$:

$$
a_1\alpha_1 + \dots + a_n\alpha_n + 0\cdot\alpha = \bar{0}
$$

Because the original scalars $a_1, \dots, a_n$ were not all zero, the scalars in this new equation are also not all zero. Therefore, the superset $S_1$ is linearly dependent.

---

## The Preceding Vector Theorem

This is the most important theorem regarding linear dependence. It states exactly *why* a set is dependent.

**Theorem:** A set of non-zero vectors

$$
S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace
$$

is linearly dependent **if and only if** some vector $\alpha_k$ ($2 \le k \le n$) can be expressed as a linear combination of its preceding vectors (

$$
\alpha_1, \alpha_2, \dots, \alpha_{k-1}
$$

).

Because this is an "if and only if" theorem, we prove both directions.

### Part 1: Assume is Linearly Dependent
We must show one vector is a combination of the ones before it.
Because $S$ is linearly dependent, there exist scalars $a_1, \dots, a_n$ (not all zero) such that:

$$
a_1\alpha_1 + a_2\alpha_2 + \dots + a_n\alpha_n = \bar{0}
$$

Since the vectors are non-zero, $\alpha_1 \neq \bar{0}$.
Let $k$ be the largest index such that its scalar $a_k \neq 0$. (This means for all vectors after $k$, their scalars are zero:

$$
a_{k+1} = 0, \dots, a_n = 0
$$

).
We also know $k > 1$. (If $k=1$, then

$$
a_1\alpha_1 = \bar{0}
$$

. Since $\alpha_1 \neq \bar{0}$, $a_1$ must be $0$, which contradicts our assumption that not all scalars are zero).

So our equation simplifies to:

$$
a_1\alpha_1 + a_2\alpha_2 + \dots + a_k\alpha_k = \bar{0} \quad (\text{where } a_k \neq 0)
$$

Because $a_k \neq 0$, we can isolate $\alpha_k$. First, move the other terms to the right:

$$
a_k\alpha_k = -a_1\alpha_1 - a_2\alpha_2 - \dots - a_{k-1}\alpha_{k-1}
$$

Divide everything by $a_k$:

$$
\alpha_k = \left(-\frac{a_1}{a_k}\right)\alpha_1 + \left(-\frac{a_2}{a_k}\right)\alpha_2 + \dots + \left(-\frac{a_{k-1}}{a_k}\right)\alpha_{k-1}
$$

Thus, we have successfully expressed $\alpha_k$ as a linear combination of its preceding vectors.

### Part 2: Assume is a combination of preceding vectors
We must show the set $S$ is linearly dependent.
Assume:

$$
\alpha_k = c_1\alpha_1 + c_2\alpha_2 + \dots + c_{k-1}\alpha_{k-1}
$$

Move $\alpha_k$ to the right side of the equation:

$$
c_1\alpha_1 + c_2\alpha_2 + \dots + c_{k-1}\alpha_{k-1} - 1\cdot\alpha_k = \bar{0}
$$

Look closely at this linear combination. The scalar coefficient for $\alpha_k$ is exactly $-1$. Since $-1 \neq 0$, the scalars in this combination are **not all zero**.
Therefore, the subset

$$
\lbrace \alpha_1, \dots, \alpha_k \rbrace
$$

is linearly dependent.

Since any superset of a linearly dependent set is also linearly dependent (as proven in our lemma), the full set

$$
S = \lbrace \alpha_1, \dots, \alpha_n \rbrace
$$

is linearly dependent.

---

## Key Takeaways
*   The zero vector destroys independence. Any set containing it is linearly dependent.
*   **Subsets** of independent sets remain independent.
*   **Supersets** of dependent sets remain dependent.
*   A set is linearly dependent if and only if you can build one of its vectors using only the vectors that came before it.

## What Comes Next
We will use these theorems to prove the Existence Theorem, which guarantees that every finitely generated vector space has a basis, and then we will look at the Extension Theorem.

---

**Navigation**
[< Previous Lecture](09_Theorems_Linear_Span.md) | [Index](README.md) | [Next Lecture >](11_Existence_Dimension_Theorem.md)
