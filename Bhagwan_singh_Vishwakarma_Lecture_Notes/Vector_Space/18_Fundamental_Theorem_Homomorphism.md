# Lecture 18: Vector Space - Fundamental Theorem of Vector Space Homomorphism

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 18 of 27
> **Video**: https://www.youtube.com/watch?v=jAH5rcWIyCE

---

**Navigation**
[< Previous Lecture](17_Isomorphism.md) | [Index](README.md) | [Next Lecture >](19_Matrix_Representation.md)

---

## Prerequisites
We know what a quotient space $V/W$ is, and we know that a homomorphism (linear transformation) $T$ has a kernel, which is a subspace of the domain. Today, we connect these two concepts in one of the most important theorems in linear algebra.

Before tackling the main theorem, we prove a preliminary lemma that explains how a quotient space interacts with its parent vector space.

---

## Lemma: The Natural Projection

**Statement:** If $V(F)$ is a vector space and $W$ is its subspace, then the quotient space $V/W$ is a homomorphic image of $V(F)$ with kernel $W$.

**Proof:**
We must define a mapping from $V$ to $V/W$, prove it is a homomorphism, and show its kernel is exactly $W$.

**1. Define the Mapping:**
Let $f : V \to V/W$ be defined by mapping every vector in $V$ to its corresponding coset in $V/W$:

$$
f(\alpha) = W + \alpha \quad \text{for all } \alpha \in V
$$

**2. Verify it is Well-Defined:**
Let $\alpha, \beta \in V$. If $\alpha = \beta$, then adding the subspace $W$ to both yields $W + \alpha = W + \beta$.
Therefore, $f(\alpha) = f(\beta)$. The mapping is perfectly consistent.

**3. Verify it is a Homomorphism (Linear):**
Let $\alpha, \beta \in V$ and $a, b \in F$.

$$
f(a\alpha + b\beta) = W + (a\alpha + b\beta)
$$

Using the rules of coset addition and scalar multiplication in the quotient space:

$$
f(a\alpha + b\beta) = (W + a\alpha) + (W + b\beta) = a(W + \alpha) + b(W + \beta)
$$

$$
f(a\alpha + b\beta) = a f(\alpha) + b f(\beta)
$$

Thus, $f$ is a homomorphism.

**4. Find its Kernel:**
The kernel of $f$ consists of all vectors in $V$ that map to the identity element of $V/W$. The identity element of $V/W$ is the subspace $W$.

$$
\ker(f) = \lbrace \alpha \in V \mid f(\alpha) = W \rbrace
$$

By definition of $f$:

$$
W + \alpha = W
$$

We know from quotient space properties that $W + \alpha = W \iff \alpha \in W$.
Thus, any vector in the kernel must belong to $W$, and any vector in $W$ belongs to the kernel.

$$
\ker(f) = W
$$

The lemma is proven.

---

## The Fundamental Theorem of Homomorphism

This theorem states that if you take any linear mapping, you can "mod out" (divide out) the information destroyed by the mapping (the kernel) to create a perfect one-to-one correspondence (an isomorphism) with the image.

**Statement:** Let $V(F)$ and $U(F)$ be vector spaces, and let $T : V \to U$ be an onto linear transformation (homomorphism) with kernel $W$. Then:

$$
V/W \cong U
$$

*(If $T$ is not onto, the theorem is simply $V/W \cong \text{Im}(T)$).*

**Proof:**
Because $W$ is the kernel of $T$, it is a valid subspace of $V$. Thus, the quotient space $V/W$ exists.
We must construct a new mapping $f : V/W \to U$ and prove it is an isomorphism (well-defined, one-to-one, onto, linear).

**1. Define the Mapping:**
For any coset $W + \alpha \in V/W$, we define its image under $f$ to be the image of its representative vector under $T$:

$$
f(W + \alpha) = T(\alpha)
$$

**2. Verify it is Well-Defined:**
Because a single coset can be represented by many different vectors (e.g., $W + \alpha = W + \beta$), we must ensure our mapping gives the same output regardless of the representative chosen.
Assume two cosets are equal:

$$
W + \alpha = W + \beta
$$

This implies $\alpha - \beta \in W$.
Because $W$ is the kernel of $T$, any vector in $W$ maps to zero under $T$:

$$
T(\alpha - \beta) = \bar{0}'
$$

Since $T$ is linear:

$$
T(\alpha) - T(\beta) = \bar{0}' \implies T(\alpha) = T(\beta)
$$

By the definition of $f$:

$$
f(W + \alpha) = f(W + \beta)
$$

Equal inputs yield equal outputs. The mapping is well-defined.

**3. Verify it is One-to-One:**
We just reverse the well-definedness steps. Assume the outputs are equal:

$$
f(W + \alpha) = f(W + \beta)
$$

$$
T(\alpha) = T(\beta) \implies T(\alpha) - T(\beta) = \bar{0}' \implies T(\alpha - \beta) = \bar{0}'
$$

Because the image of $(\alpha - \beta)$ under $T$ is zero, it belongs to the kernel $W$:

$$
\alpha - \beta \in W
$$

This implies that their cosets are equal:

$$
W + (\alpha - \beta) = W \implies W + \alpha = W + \beta
$$

Equal outputs imply equal inputs. The mapping is one-to-one.

**4. Verify it is Onto:**
Because we assumed the original mapping $T : V \to U$ is onto, for every vector $u \in U$, there exists some $\alpha \in V$ such that $T(\alpha) = u$.
For this vector $\alpha$, the coset $W + \alpha \in V/W$ satisfies:

$$
f(W + \alpha) = T(\alpha) = u
$$

Thus, every element in $U$ is hit by $f$. The mapping is onto.

**5. Verify it is Linear:**
Let $W + \alpha, W + \beta \in V/W$ and $a, b \in F$.

$$
f(a(W + \alpha) + b(W + \beta)) = f((W + a\alpha) + (W + b\beta)) = f(W + (a\alpha + b\beta))
$$

By the definition of $f$:

$$
= T(a\alpha + b\beta)
$$

Because $T$ is linear:

$$
= a T(\alpha) + b T(\beta)
$$

Substitute the definition of $f$ back in:

$$
= a f(W + \alpha) + b f(W + \beta)
$$

Thus, $f$ is a linear transformation.

Since $f$ is well-defined, one-to-one, onto, and linear, it is an isomorphism.

$$
V/W \cong U
$$

## Key Takeaways
*   The **Fundamental Theorem of Homomorphism** bridges vector spaces, quotient spaces, and linear transformations.
*   By forming a quotient space $V/W$ where $W = \ker(T)$, we effectively "collapse" everything that gets mapped to zero into a single identity element. This removes all redundancy, turning the mapping into a perfect one-to-one correspondence (an isomorphism) with the image.

## What Comes Next
With the theoretical framework of linear transformations complete, we will move to Phase 7, where we ground these concepts in computation by investigating **Matrix Representations** and the **Rank-Nullity Theorem**.

---

**Navigation**
[< Previous Lecture](17_Isomorphism.md) | [Index](README.md) | [Next Lecture >](19_Matrix_Representation.md)
