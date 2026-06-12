# Lecture 17: Vector Space - Isomorphism of Vector Spaces

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 17 of 27
> **Video**: https://www.youtube.com/watch?v=KgZR5L9jTJA

---

**Navigation**
[< Previous Lecture](16_Kernel_Homomorphism.md) | [Index](README.md) | [Next Lecture >](18_Fundamental_Theorem_Homomorphism.md)

---

## Prerequisites
We know that a linear transformation (or homomorphism) preserves vector space structures (addition and scalar multiplication).
Today, we look at the ultimate form of a linear transformation: an **Isomorphism**. When two spaces are isomorphic, they are algebraically identical.

---

## What is an Isomorphism?

Let $U(F)$ and $V(F)$ be two vector spaces over the same field $F$.
A mapping $f : U \to V$ is an **Isomorphism** if it satisfies three strict conditions:

1.  **It is One-to-One (Injective)**:
    Every input gets a unique output. No two different vectors in $U$ map to the same vector in $V$.

$$
    f(\alpha) = f(\beta) \implies \alpha = \beta
$$

2.  **It is Onto (Surjective)**:
    Every vector in the co-domain $V$ is "hit" by the mapping. The range covers the entire co-domain.
    For every $\beta \in V$, there exists an $\alpha \in U$ such that $f(\alpha) = \beta$.
3.  **It is a Linear Transformation (Homomorphism)**:
    It perfectly preserves linear combinations.

$$
    f(a\alpha + b\beta) = a f(\alpha) + b f(\beta)
$$

If such a mapping exists between two spaces, we say the spaces are **Isomorphic** and we write:

$$
U \cong V
$$

When $U \cong V$, they are algebraically indistinguishable. They have the same dimension, the same number of basis elements, and their vectors behave exactly the same way under addition and scaling. The only difference is the *names* or *labels* given to the vectors.

---

## Theorem 1: Isomorphism and Dimension

This theorem proves that for finite-dimensional spaces, "being isomorphic" is exactly the same as "having the same dimension."

**Statement:** Two finite-dimensional vector spaces over the same field are isomorphic if and only if they have the same dimension.

$$
U \cong V \iff \dim(U) = \dim(V)
$$

### Part 1: Same Dimension Isomorphic
Let $\dim(U) = \dim(V) = n$.
Let $S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace$ be a basis for $U$.
Let $S' = \lbrace \beta_1, \beta_2, \dots, \beta_n \rbrace$ be a basis for $V$.

We define a mapping $f : U \to V$ by matching their basis vectors:

$$
f(a_1\alpha_1 + \dots + a_n\alpha_n) = a_1\beta_1 + \dots + a_n\beta_n
$$

**1. Prove $f$ is One-to-One:**
Assume $f(\alpha) = f(\beta)$.
Let $\alpha = a_1\alpha_1 + \dots + a_n\alpha_n$ and $\beta = b_1\alpha_1 + \dots + b_n\alpha_n$.
Substitute into the assumption:

$$
a_1\beta_1 + \dots + a_n\beta_n = b_1\beta_1 + \dots + b_n\beta_n
$$

Subtract to one side:

$$
(a_1 - b_1)\beta_1 + \dots + (a_n - b_n)\beta_n = \bar{0}'
$$

Because $S'$ is a basis, the $\beta$ vectors are linearly independent. Thus, all coefficients are zero:

$$
a_1 = b_1, \dots, a_n = b_n \implies \alpha = \beta
$$

Thus, $f$ is one-to-one.

**2. Prove $f$ is Onto:**
Take any vector $\gamma \in V$. Since $S'$ is a basis, $\gamma = c_1\beta_1 + \dots + c_n\beta_n$.
Because the coefficients $c_i$ are in the field $F$, we can construct the vector $\alpha = c_1\alpha_1 + \dots + c_n\alpha_n$ in $U$.
By our definition, $f(\alpha) = \gamma$. Thus, every vector in $V$ has a pre-image. $f$ is onto.

**3. Prove $f$ is Linear:**
Let $\alpha, \beta \in U$ and $k, l \in F$.

$$
k\alpha + l\beta = (ka_1 + lb_1)\alpha_1 + \dots + (ka_n + lb_n)\alpha_n
$$

Apply $f$:

$$
f(k\alpha + l\beta) = (ka_1 + lb_1)\beta_1 + \dots + (ka_n + lb_n)\beta_n
$$

Split the coefficients:

$$
f(k\alpha + l\beta) = k(a_1\beta_1 + \dots + a_n\beta_n) + l(b_1\beta_1 + \dots + b_n\beta_n) = k f(\alpha) + l f(\beta)
$$

Thus, $f$ is linear. Since $f$ is one-to-one, onto, and linear, $U \cong V$.

### Part 2: Isomorphic Same Dimension
Assume $U \cong V$. This means there exists an isomorphism $f : U \to V$.
Let $\dim(U) = n$, and let $S = \lbrace \alpha_1, \dots, \alpha_n \rbrace$ be its basis.
We map the basis $S$ to $V$ to create a new set:

$$
S' = \lbrace f(\alpha_1), f(\alpha_2), \dots, f(\alpha_n) \rbrace
$$

**1. Prove $S'$ is Linearly Independent:**
Set a linear combination to zero:

$$
a_1 f(\alpha_1) + \dots + a_n f(\alpha_n) = \bar{0}'
$$

Because $f$ is linear, we can pull $f$ outside:

$$
f(a_1\alpha_1 + \dots + a_n\alpha_n) = \bar{0}'
$$

We know $f(\bar{0}) = \bar{0}'$. Since $f$ is one-to-one, equal images mean equal inputs:

$$
a_1\alpha_1 + \dots + a_n\alpha_n = \bar{0}
$$

Because $S$ is a basis of $U$, it is independent, so all coefficients $a_i$ must be zero. Thus, $S'$ is independent.

**2. Prove $S'$ Spans $V$:**
Take any $\gamma \in V$. Because $f$ is onto, there exists $\alpha \in U$ such that $f(\alpha) = \gamma$.
Since $S$ is a basis of $U$, $\alpha = c_1\alpha_1 + \dots + c_n\alpha_n$.
Apply $f$:

$$
\gamma = f(\alpha) = f(c_1\alpha_1 + \dots + c_n\alpha_n) = c_1 f(\alpha_1) + \dots + c_n f(\alpha_n)
$$

This proves any vector $\gamma \in V$ can be built using $S'$.
Thus, $S'$ is a basis for $V$. Since $S'$ contains $n$ elements, $\dim(V) = n$.
Therefore, $\dim(U) = \dim(V)$.

---

## Theorem 2: The Universal Isomorphism

This theorem states that *every* vector space of dimension $n$ is just the standard tuple space $V_n(F)$ in disguise.

**Statement:** Every $n$-dimensional vector space $V(F)$ is isomorphic to the space $V_n(F)$ (the space of $n$-tuples) over the same field $F$.

$$
V(F) \cong V_n(F)
$$

**Proof Sketch:**
Let $S = \lbrace \alpha_1, \dots, \alpha_n \rbrace$ be a basis for $V$.
Any vector $\alpha \in V$ can be uniquely written as $\alpha = a_1\alpha_1 + \dots + a_n\alpha_n$.
Define a mapping $f$ that takes this vector and maps it to a simple $n$-tuple of its coordinates:

$$
f(a_1\alpha_1 + \dots + a_n\alpha_n) = (a_1, a_2, \dots, a_n)
$$

Because coordinates relative to a basis are unique, this mapping is well-defined, one-to-one, onto, and perfectly linear.
Thus, any $n$-dimensional space behaves exactly like the space of $n$-tuples.

## Key Takeaways
*   An **Isomorphism** is a linear transformation that is both one-to-one and onto.
*   If two finite-dimensional spaces share the same field and the same dimension, they are mathematically identical ($U \cong V$).
*   An isomorphism maps a basis of the domain to a basis of the co-domain.

## What Comes Next
We will conclude Phase 6 with the Fundamental Theorem of Homomorphism for vector spaces.

---

**Navigation**
[< Previous Lecture](16_Kernel_Homomorphism.md) | [Index](README.md) | [Next Lecture >](18_Fundamental_Theorem_Homomorphism.md)
