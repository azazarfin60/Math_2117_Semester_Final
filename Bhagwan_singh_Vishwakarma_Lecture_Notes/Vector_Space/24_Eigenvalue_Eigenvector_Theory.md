# Lecture 24: Vector Space - Eigenvalue & Eigenvector Theory

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 24 of 27
> **Video**: https://www.youtube.com/watch?v=TH2nvOymftc

---

**Navigation**
[< Previous Lecture](23_Rank_Nullity_Numericals.md) | [Index](README.md) | [Next Lecture >](25_Eigenvalue_Numericals.md)


---

## Prerequisites
We now turn our attention from transformations between different vector spaces to transformations from a vector space to itself ($T : V \to V$). These are called **linear operators**. When a linear operator acts on certain special vectors, it doesn't rotate or skew them; it simply scales them. These special vectors are called eigenvectors.

---

## 1. Fundamental Definitions

Let $T : V \to V$ be a linear transformation on an $n$-dimensional vector space $V$ over a field $F$.

### Eigenvalue and Eigenvector
A scalar $\lambda \in F$ is called an **eigenvalue** (or characteristic value) of $T$ if there exists a **non-zero vector** $\alpha \in V$ ($\alpha \neq \bar{0}$) such that:

$$
T(\alpha) = \lambda \alpha
$$

The non-zero vector $\alpha$ is called the **eigenvector** (or characteristic vector) of $T$ corresponding to the eigenvalue $\lambda$.
*(Note: While the eigenvalue $\lambda$ can be zero, the eigenvector $\alpha$ MUST NEVER be the zero vector.)*

### Eigenspace
A single eigenvalue can have multiple eigenvectors associated with it. The set of all eigenvectors corresponding to an eigenvalue $\lambda$, along with the zero vector $\bar{0}$, is called the **Eigenspace** of $\lambda$.

$$
W_\lambda = \lbrace \alpha \in V \mid T(\alpha) = \lambda \alpha \rbrace
$$

### Spectrum
The set of *all* distinct eigenvalues of the linear transformation $T$ is called the **Spectrum** of $T$.

---

## 2. Fundamental Theorems

### Theorem 1: Scalar Multiples of Eigenvectors
**Statement:** If $\alpha$ is an eigenvector of $T$ corresponding to the eigenvalue $\lambda$, then any non-zero scalar multiple $k\alpha$ ($k \in F, k \neq 0$) is also an eigenvector of $T$ corresponding to the same eigenvalue $\lambda$.

**Proof:**
Since $\alpha$ is an eigenvector for $\lambda$:

$$
T(\alpha) = \lambda \alpha \quad (\alpha \neq \bar{0})
$$

Let $k \in F$ with $k \neq 0$. Because $\alpha \neq \bar{0}$ and $k \neq 0$, the scalar multiple $k\alpha \neq \bar{0}$. Let's find the image of $k\alpha$:

$$
T(k\alpha) = k T(\alpha) \quad \text{(since } T \text{ is linear)}
$$

Substitute $T(\alpha) = \lambda \alpha$:

$$
= k(\lambda \alpha)
$$

By associativity and commutativity of scalars in the field $F$:

$$
= (k\lambda) \alpha = (\lambda k) \alpha = \lambda (k\alpha)
$$

Thus, $T(k\alpha) = \lambda (k\alpha)$. Since $k\alpha$ is non-zero, it is an eigenvector corresponding to $\lambda$.

---

### Theorem 2: Uniqueness of Eigenvalues
**Statement:** A single eigenvector $\alpha$ cannot correspond to more than one distinct eigenvalue.

**Proof:**
Let us assume the contrary. Suppose the eigenvector $\alpha$ corresponds to two distinct eigenvalues, $\lambda_1$ and $\lambda_2$ ($\lambda_1 \neq \lambda_2$).
By definition, we have:
1.  $T(\alpha) = \lambda_1 \alpha$
2.  $T(\alpha) = \lambda_2 \alpha$

Because the mapping $T$ is a function, a single input $\alpha$ must have a unique output. Therefore, we can equate the right-hand sides:

$$
\lambda_1 \alpha = \lambda_2 \alpha
$$

Bring all terms to one side:

$$
\lambda_1 \alpha - \lambda_2 \alpha = \bar{0} \implies (\lambda_1 - \lambda_2)\alpha = \bar{0}
$$

By definition, an eigenvector $\alpha$ cannot be the zero vector ($\alpha \neq \bar{0}$). In a vector space, if a scalar times a non-zero vector equals zero, the scalar itself must be zero.

$$
\lambda_1 - \lambda_2 = 0 \implies \lambda_1 = \lambda_2
$$

This contradicts our assumption that $\lambda_1$ and $\lambda_2$ are distinct. Therefore, an eigenvector corresponds to exactly one eigenvalue.

---

### Theorem 3: The Eigenspace is a Subspace
**Statement:** The eigenspace $W_\lambda$ corresponding to an eigenvalue $\lambda$ of a linear transformation $T : V \to V$ is a subspace of the vector space $V$.

**Proof:**
By definition, $W_\lambda = \lbrace \alpha \in V \mid T(\alpha) = \lambda \alpha \rbrace$.
First, note that the zero vector $\bar{0} \in V$ satisfies $T(\bar{0}) = \bar{0} = \lambda\bar{0}$. Thus, $\bar{0} \in W_\lambda$, meaning $W_\lambda$ is non-empty.

To prove it is a subspace, we must show it is closed under linear combinations. Let $\alpha, \beta \in W_\lambda$ and let $a, b \in F$ be any scalars.
Since $\alpha, \beta \in W_\lambda$:
1.  $T(\alpha) = \lambda \alpha$
2.  $T(\beta) = \lambda \beta$

Let's evaluate the transformation on the linear combination $a\alpha + b\beta$:

$$
T(a\alpha + b\beta) = a T(\alpha) + b T(\beta) \quad \text{(since } T \text{ is linear)}
$$

Substitute the equations from above:

$$
= a(\lambda \alpha) + b(\lambda \beta)
$$

Reorder the scalars (since $F$ is a field):

$$
= \lambda(a\alpha) + \lambda(b\beta)
$$

Factor out $\lambda$:

$$
= \lambda(a\alpha + b\beta)
$$

Since $T(a\alpha + b\beta) = \lambda(a\alpha + b\beta)$, the vector $(a\alpha + b\beta)$ satisfies the condition to be in $W_\lambda$. Therefore, $W_\lambda$ is closed under linear combinations and is a valid subspace of $V(F)$.

## Key Takeaways
*   **Eigenvalues** scale **Eigenvectors** without changing their direction.
*   The set of all eigenvectors for a given eigenvalue forms a complete, well-behaved vector subspace called the **Eigenspace**.
*   A single eigenvalue can have infinitely many eigenvectors (Theorem 1 and 3), but a single eigenvector is tied exclusively to one eigenvalue (Theorem 2).

---

**Navigation**
[< Previous Lecture](23_Rank_Nullity_Numericals.md) | [Index](README.md) | [Next Lecture >](25_Eigenvalue_Numericals.md)
