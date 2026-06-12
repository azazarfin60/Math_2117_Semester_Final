# Lecture 16: Vector Space - Kernel and Range of a Homomorphism

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 16 of 27
> **Video**: https://www.youtube.com/watch?v=NzuTxGGFcrg

---

**Navigation**
[< Previous Lecture](15_Linear_Transformation.md) | [Index](README.md) | [Next Lecture >](17_Isomorphism.md)

---

## Prerequisites
We know that a vector space homomorphism (or linear transformation) is a mapping $f : U \to V$ that preserves vector addition and scalar multiplication. It also maps the zero vector of the domain to the zero vector of the co-domain ($f(\bar{0}) = \bar{0}'$).
Today, we define two critical sets associated with this mapping: the **Kernel** and the **Range**, and prove that they are both vector subspaces.

---

## Definitions

### 1. The Kernel (Null Space)
The Kernel of a homomorphism $f : U \to V$, denoted as $\ker(f)$, $K_f$, or $N_f$, is the set of all vectors in the domain $U$ that get mapped strictly to the zero vector of the co-domain $V$.

$$
\ker(f) = \lbrace \alpha \in U \mid f(\alpha) = \bar{0}' \rbrace
$$

Because $f(\bar{0}) = \bar{0}'$, the zero vector of $U$ is *always* in the kernel. Thus, the kernel is never empty.
The kernel lives entirely within the domain space $U$.

### 2. The Range Space
The Range of a homomorphism $f : U \to V$, denoted as $R_f$, is the set of all vectors in the co-domain $V$ that are actual outputs (images) of the mapping.

$$
R_f = \lbrace \beta \in V \mid \beta = f(\alpha) \text{ for some } \alpha \in U \rbrace
$$

Because the zero vector maps to the zero vector, $\bar{0}'$ is always in the range. Thus, the range is never empty.
The range lives entirely within the co-domain space $V$.

---

## Theorem 1: The Kernel is a Subspace

**Statement:** Let $f : U \to V$ be a vector space homomorphism. The kernel of $f$, $\ker(f)$, is a subspace of the domain vector space $U$.

**Proof:**
To prove a set is a subspace, we must prove that any linear combination of its elements also belongs to the set.
First, we know $\ker(f) \neq \emptyset$ because $\bar{0} \in \ker(f)$.

Let $\alpha, \beta$ be two arbitrary vectors in $\ker(f)$.
Because they are in the kernel, their images are zero:

$$
f(\alpha) = \bar{0}' \quad \text{and} \quad f(\beta) = \bar{0}'
$$

Let $a, b \in F$ be two scalars.
We must check if the linear combination $a\alpha + b\beta$ is in the kernel. We test this by applying the mapping $f$:

$$
f(a\alpha + b\beta) = a f(\alpha) + b f(\beta) \quad \text{(since } f \text{ is linear)}
$$

Substitute our known values for $f(\alpha)$ and $f(\beta)$:

$$
f(a\alpha + b\beta) = a(\bar{0}') + b(\bar{0}') = \bar{0}' + \bar{0}' = \bar{0}'
$$

Because the image of the combination $(a\alpha + b\beta)$ is the zero vector, the combination itself must belong to the kernel.

$$
a\alpha + b\beta \in \ker(f)
$$

Therefore, $\ker(f)$ is a subspace of $U$.

---

## Theorem 2: The Range is a Subspace

**Statement:** Let $f : U \to V$ be a vector space homomorphism. The range of $f$, $R_f$, is a subspace of the co-domain vector space $V$.

**Proof:**
First, we know $R_f \neq \emptyset$ because $\bar{0}' = f(\bar{0})$, so $\bar{0}' \in R_f$.

Let $\beta_1, \beta_2$ be two arbitrary vectors in $R_f$.
Because they are in the range, they must have pre-images in the domain $U$. Let's call their pre-images $\alpha_1$ and $\alpha_2$:

$$
f(\alpha_1) = \beta_1 \quad \text{and} \quad f(\alpha_2) = \beta_2
$$

Let $a, b \in F$ be two scalars.
We must check if the linear combination $a\beta_1 + b\beta_2$ is in the range.
To prove it is in the range, we must find a vector in $U$ that maps to it. Let's guess the linear combination of the pre-images: $a\alpha_1 + b\alpha_2$.
Because $U$ is a vector space, $a\alpha_1 + b\alpha_2$ is definitely a valid vector in $U$.
Let's apply $f$ to it:

$$
f(a\alpha_1 + b\alpha_2) = a f(\alpha_1) + b f(\alpha_2) \quad \text{(since } f \text{ is linear)}
$$

Substitute our known values for the images:

$$
f(a\alpha_1 + b\alpha_2) = a\beta_1 + b\beta_2
$$

This equation proves that $a\beta_1 + b\beta_2$ is the valid output of the input vector $(a\alpha_1 + b\alpha_2)$.
Therefore, it belongs to the range.

$$
a\beta_1 + b\beta_2 \in R_f
$$

Therefore, $R_f$ is a subspace of $V$.

---

## Theorem 3: Injectivity and the Trivial Kernel

This is one of the most powerful theorems in linear algebra. It gives us a very easy way to check if a transformation is one-to-one.

**Statement:** Let $f : U \to V$ be a vector space homomorphism. The mapping $f$ is one-to-one (injective) if and only if the kernel contains *only* the zero vector ($\ker(f) = \lbrace \bar{0} \rbrace$).

**Proof:**
Since this is an "if and only if" theorem, we must prove both directions.

### Part 1: Assume is one-to-one. Prove.
Let $\alpha \in \ker(f)$. By the definition of the kernel:

$$
f(\alpha) = \bar{0}'
$$

We also know a universal property of linear transformations:

$$
f(\bar{0}) = \bar{0}'
$$

We can equate the two expressions:

$$
f(\alpha) = f(\bar{0})
$$

Because we assumed $f$ is one-to-one, distinct inputs must give distinct outputs. If the outputs are equal, the inputs *must* be equal:

$$
\alpha = \bar{0}
$$

Thus, any vector in the kernel must be the zero vector. $\ker(f) = \lbrace \bar{0} \rbrace$.

### Part 2: Assume. Prove is one-to-one.
To prove $f$ is one-to-one, we assume two outputs are equal and prove their inputs must be equal.
Let $\alpha, \beta \in U$ such that:

$$
f(\alpha) = f(\beta)
$$

Subtract $f(\beta)$ from both sides:

$$
f(\alpha) - f(\beta) = \bar{0}'
$$

Use the subtraction property of linear transformations:

$$
f(\alpha - \beta) = \bar{0}'
$$

Because the image of the vector $(\alpha - \beta)$ is the zero vector, it must belong to the kernel:

$$
\alpha - \beta \in \ker(f)
$$

But our assumption is that the kernel *only* contains the zero vector. Therefore, this vector must be zero:

$$
\alpha - \beta = \bar{0}
$$

$$
\alpha = \beta
$$

Since $f(\alpha) = f(\beta)$ implies $\alpha = \beta$, the mapping is one-to-one. The theorem is proven in both directions.

---

## Key Takeaways
*   The **Kernel** ($\ker(f)$) is the set of inputs that get destroyed (mapped to zero). It is a subspace of the domain.
*   The **Range** ($R_f$) is the set of all valid outputs. It is a subspace of the co-domain.
*   A linear transformation is one-to-one if and only if its kernel is "trivial" (meaning $\ker(f) = \lbrace \bar{0} \rbrace$). If any non-zero vector sneaks into the kernel, the mapping is not one-to-one.

## What Comes Next
We will use these concepts to define Isomorphisms (one-to-one and onto linear transformations) and study the Fundamental Theorem of Homomorphism.

---

**Navigation**
[< Previous Lecture](15_Linear_Transformation.md) | [Index](README.md) | [Next Lecture >](17_Isomorphism.md)
