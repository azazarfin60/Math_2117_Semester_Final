# Lecture 22: Vector Space - Invertible, Singular & Nonsingular Linear Transformations

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 22 of 27
> **Video**: https://www.youtube.com/watch?v=qIOCtAR0Qw0

---

**Navigation**
[< Previous Lecture](21_Rank_Nullity_Theorem.md) | [Index](README.md) | [Next Lecture >](23_Rank_Nullity_Numericals.md)

---

## Prerequisites
We know how to calculate the inverse of a linear transformation using matrix representations. Today, we formalize the algebraic definitions of invertibility, singularity, and the composition of linear transformations, proving several foundational theorems.

---

## 1. Invertible Linear Transformations

### Definition
A linear transformation $T : U \to V$ is said to be **invertible** if it is a bijective mapping. That means $T$ must satisfy three conditions:
1.  **Linearity**: It preserves addition and scalar multiplication.
2.  **One-to-One (Injective)**: $T(\alpha) = T(\beta) \implies \alpha = \beta$.
3.  **Onto (Surjective)**: For every $\beta \in V$, there exists an $\alpha \in U$ such that $T(\alpha) = \beta$.

If these conditions are met, an inverse mapping $T^{-1} : V \to U$ exists, defined by:

$$
T^{-1}(\beta) = \alpha \iff T(\alpha) = \beta
$$

---

### Theorem 1: Linearity of the Inverse
**Statement:** If $T : V_1 \to V_2$ is an invertible linear transformation, then its inverse $T^{-1} : V_2 \to V_1$ is also a linear transformation.

**Proof:**
We must prove that $T^{-1}$ preserves linear combinations: $T^{-1}(a \alpha' + b \beta') = a T^{-1}(\alpha') + b T^{-1}(\beta')$.
Let $\alpha', \beta' \in V_2$. Because $T$ is onto, they have unique pre-images $\alpha, \beta \in V_1$:

$$
T(\alpha) = \alpha' \implies T^{-1}(\alpha') = \alpha
$$

$$
T(\beta) = \beta' \implies T^{-1}(\beta') = \beta
$$

Let $a, b \in F$. Consider the linear combination $a\alpha + b\beta$ in $V_1$. Apply $T$:

$$
T(a\alpha + b\beta) = aT(\alpha) + bT(\beta) \quad \text{(since } T \text{ is linear)}
$$

Substitute the images:

$$
T(a\alpha + b\beta) = a\alpha' + b\beta'
$$

Apply the inverse mapping $T^{-1}$ to both sides:

$$
a\alpha + b\beta = T^{-1}(a\alpha' + b\beta')
$$

Substitute back the inverse expressions for $\alpha$ and $\beta$:

$$
aT^{-1}(\alpha') + bT^{-1}(\beta') = T^{-1}(a\alpha' + b\beta')
$$

Thus, $T^{-1}$ is a linear transformation.

### Result 2: Composition with the Inverse
If $T : U \to V$ is an invertible linear transformation, then composing it with its inverse yields the identity transformation.

$$
T T^{-1} = I_V \quad \text{and} \quad T^{-1} T = I_U
$$

*(Where $I_V$ and $I_U$ are the identity mappings that do nothing to the vectors in $V$ and $U$ respectively.)*

---

## 2. Singular and Nonsingular Transformations

Let $T : U \to V$ be a linear transformation. Let $\bar{0}$ and $\bar{0}'$ be the zero vectors of $U$ and $V$, respectively.

### Definitions
**1. Singular Transformation:**
$T$ is singular if it maps at least one non-zero vector to the zero vector.
There exists some $\alpha \neq \bar{0}$ such that $T(\alpha) = \bar{0}'$.
*(This means information is lost, and the mapping cannot be reversed.)*

**2. Nonsingular Transformation:**
$T$ is nonsingular if the *only* vector that maps to the zero vector is the zero vector itself.

$$
T(\alpha) = \bar{0}' \implies \alpha = \bar{0}
$$

*(This means the null space (kernel) is trivial: $N(T) = \lbrace \bar{0} \rbrace$.)*

---

### Theorem 2: Nonsingularity and One-to-One
**Statement:** A linear transformation $T : U \to V$ is nonsingular if and only if $T$ is one-to-one (1-1).

**Proof:**
**(Part 1: Nonsingular $\implies$ One-to-One)**
Assume $T$ is nonsingular. Let $T(\alpha) = T(\beta)$.
Subtract to one side:

$$
T(\alpha) - T(\beta) = \bar{0}' \implies T(\alpha - \beta) = \bar{0}'
$$

Because $T$ is nonsingular, any vector mapping to zero must be the zero vector:

$$
\alpha - \beta = \bar{0} \implies \alpha = \beta
$$

Thus, $T$ is one-to-one.

**(Part 2: One-to-One $\implies$ Nonsingular)**
Assume $T$ is one-to-one. We know from linear properties that $T(\bar{0}) = \bar{0}'$.
Suppose there is an $\alpha$ such that $T(\alpha) = \bar{0}'$.
Equating the two:

$$
T(\alpha) = T(\bar{0})
$$

Because $T$ is one-to-one, equal images require equal inputs:

$$
\alpha = \bar{0}
$$

Thus, $T$ is nonsingular. Both directions are proven.

---

## 3. Product (Composition) of Linear Transformations

### Theorem 3: Composition is Linear
**Statement:** If $T : U \to V$ and $S : V \to W$ are two linear transformations, then their composition $ST : U \to W$ is also a linear transformation.

**Proof:**
Let $a, b \in F$ and $\alpha, \beta \in U$. We evaluate the composition on a linear combination:

$$
(ST)(a\alpha + b\beta) = S(T(a\alpha + b\beta))
$$

Because $T$ is linear:

$$
= S(aT(\alpha) + bT(\beta))
$$

Because $S$ is linear:

$$
= aS(T(\alpha)) + bS(T(\beta))
$$

Rewriting using composition notation:

$$
= a(ST)(\alpha) + b(ST)(\beta)
$$

Thus, the composition $ST$ is a linear transformation.

## Key Takeaways
*   **Invertible = Bijective**. A transformation can only be inverted if it is both one-to-one and onto.
*   **Nonsingular = One-to-One**. A transformation is nonsingular if its null space only contains the zero vector. By Theorem 2, this guarantees the transformation is one-to-one.
*   The inverse of a linear mapping is always linear, and the composition of two linear mappings is always linear.

## What Comes Next
We will apply these theorems alongside the Rank-Nullity Theorem to solve numerical problems involving vector spaces.

---

**Navigation**
[< Previous Lecture](21_Rank_Nullity_Theorem.md) | [Index](README.md) | [Next Lecture >](23_Rank_Nullity_Numericals.md)
