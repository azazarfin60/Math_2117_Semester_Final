# Lecture 13: Vector Space - Dimension of Sum of Subspaces (Proof)

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 13 of 27
> **Video**: https://www.youtube.com/watch?v=bJcGmEkiyz8

---

**Navigation**
[< Previous Lecture](12_Extension_Theorem_Complementary.md) | [Index](README.md) | [Next Lecture >](14_Quotient_Space_Dimension.md)

---

## Prerequisites
We know the statement of the theorem for the dimension of the linear sum of two subspaces from earlier lectures.
Today, we provide the full, formal proof of this theorem, verifying it with basis extension, and applying it to numerical examples.

---

## Theorem Statement

If $W_1$ and $W_2$ are two subspaces of a finite-dimensional vector space $V(F)$, then:

$$
\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)
$$

---

## The Proof

This proof relies on picking a basis for the intersection of the subspaces, and extending it in two different directions (one for $W_1$ and one for $W_2$). Finally, we combine these extensions to form a basis for the sum $W_1 + W_2$.

### Step 1: Define the Basis for the Intersection
Because $W_1 \cap W_2$ is a subspace, it has a basis. Let the dimension of this intersection be $k$:

$$
\dim(W_1 \cap W_2) = k
$$

Let the basis for this intersection be $S$:

$$
S = \lbrace \gamma_1, \gamma_2, \dots, \gamma_k \rbrace
$$

### Step 2: Extend the Basis for and
The intersection $W_1 \cap W_2$ is fully contained within $W_1$. This means the basis $S$ is a linearly independent subset of $W_1$.
By the **Extension Theorem**, we can extend $S$ to form a complete basis for $W_1$ by adding $n$ vectors:

$$
S_1 = \lbrace \gamma_1, \dots, \gamma_k, \alpha_1, \alpha_2, \dots, \alpha_n \rbrace
$$

Thus, $\dim(W_1) = k + n$.

Similarly, the intersection $W_1 \cap W_2$ is fully contained within $W_2$. We can extend $S$ by adding $m$ vectors to form a complete basis for $W_2$:

$$
S_2 = \lbrace \gamma_1, \dots, \gamma_k, \beta_1, \beta_2, \dots, \beta_m \rbrace
$$

Thus, $\dim(W_2) = k + m$.

Let's look at what we are trying to prove. The right side of our theorem formula is:

$$
\dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2) = (k + n) + (k + m) - k = k + n + m
$$

To prove the theorem, we must prove that the left side, $\dim(W_1 + W_2)$, is also equal to $k + n + m$.

### Step 3: Propose a Basis for
We propose that the set containing all unique vectors from $S_1$ and $S_2$ forms the basis for $W_1 + W_2$:

$$
S' = \lbrace \gamma_1, \dots, \gamma_k, \alpha_1, \dots, \alpha_n, \beta_1, \dots, \beta_m \rbrace
$$

This set has exactly $k + n + m$ elements. We must prove it is a basis by showing it is linearly independent and spans $W_1 + W_2$.

#### Part A: Prove is Linearly Independent
Set a linear combination of all vectors in $S'$ equal to zero:

$$
c_1\gamma_1 + \dots + c_k\gamma_k + a_1\alpha_1 + \dots + a_n\alpha_n + b_1\beta_1 + \dots + b_m\beta_m = \bar{0} \quad \text{--- (1)}
$$

We need to prove that all scalars $c_i, a_j, b_l$ are strictly zero.

Isolate the $\beta$ terms on the left side:

$$
b_1\beta_1 + \dots + b_m\beta_m = -(c_1\gamma_1 + \dots + c_k\gamma_k + a_1\alpha_1 + \dots + a_n\alpha_n) \quad \text{--- (2)}
$$

Look at equation (2).
The right-hand side is built entirely from gammas and alphas, which are the basis vectors of $W_1$. Therefore, this vector lives inside $W_1$.
But the left-hand side is exactly equal to it, so the left-hand side must also live inside $W_1$:

$$
b_1\beta_1 + \dots + b_m\beta_m \in W_1
$$

However, the left-hand side is built entirely from betas. Betas belong to $W_2$. So:

$$
b_1\beta_1 + \dots + b_m\beta_m \in W_2
$$

Because this vector is in both $W_1$ and $W_2$, it must be in their intersection:

$$
b_1\beta_1 + \dots + b_m\beta_m \in W_1 \cap W_2
$$

We already defined the basis of the intersection as $S = \lbrace \gamma_1, \dots, \gamma_k \rbrace$. Thus, this vector can be written as a combination of gammas:

$$
b_1\beta_1 + \dots + b_m\beta_m = d_1\gamma_1 + \dots + d_k\gamma_k \quad \text{(for some scalars } d_i)
$$

Bring everything to one side:

$$
b_1\beta_1 + \dots + b_m\beta_m - d_1\gamma_1 - \dots - d_k\gamma_k = \bar{0}
$$

This is a linear combination of vectors in $S_2$ (gammas and betas) equaling zero. Since $S_2$ is a basis for $W_2$, its elements are linearly independent. Therefore, every single scalar in this equation must be zero:

$$
b_1 = 0, \dots, b_m = 0 \quad \text{and} \quad d_1 = 0, \dots, d_k = 0
$$

Now substitute $b_1 = \dots = b_m = 0$ back into our very first equation (1). It shrinks to:

$$
c_1\gamma_1 + \dots + c_k\gamma_k + a_1\alpha_1 + \dots + a_n\alpha_n = \bar{0}
$$

This is a linear combination of vectors in $S_1$ (gammas and alphas) equaling zero. Since $S_1$ is a basis for $W_1$, it is independent. Thus:

$$
c_1 = 0, \dots, c_k = 0 \quad \text{and} \quad a_1 = 0, \dots, a_n = 0
$$

We have proven that all scalars are zero. Therefore, $S'$ is **Linearly Independent**.

#### Part B: Prove Spans
Let $\alpha$ be an arbitrary vector in $W_1 + W_2$.
By definition, $\alpha = \alpha' + \beta'$, where $\alpha' \in W_1$ and $\beta' \in W_2$.
Since $S_1$ is the basis for $W_1$, $\alpha'$ is a combination of gammas and alphas.
Since $S_2$ is the basis for $W_2$, $\beta'$ is a combination of gammas and betas.

When we add them together to get $\alpha$, we get a giant combination of gammas, alphas, and betas. Since all of these vectors exist within $S'$, we can build any vector $\alpha \in W_1 + W_2$ using $S'$.
Thus, $S'$ spans $W_1 + W_2$.

Because $S'$ is linearly independent and spans $W_1 + W_2$, it is a basis for $W_1 + W_2$.
Since $S'$ has $k+n+m$ elements:

$$
\dim(W_1 + W_2) = k + n + m = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)
$$

The theorem is proven.

---

## Direct Sum Special Case
If the vector space is the direct sum $W_1 \oplus W_2$, the intersection only contains the zero vector, meaning its dimension is $0$. The formula simplifies to:

$$
\dim(W_1 \oplus W_2) = \dim(W_1) + \dim(W_2)
$$

---

## Numerical Examples

### Example 1: Sum in 3D Space
Let $V_3(\mathbb{R})$ be a 3D space with subspaces:

$$
W_1 = \lbrace (a, 0, 0) \mid a \in \mathbb{R} \rbrace \implies \dim(W_1) = 1
$$

$$
W_2 = \lbrace (0, b, c) \mid b, c \in \mathbb{R} \rbrace \implies \dim(W_2) = 2
$$

The intersection is elements where the 1st coordinate is 0 (from $W_2$) and the last two are 0 (from $W_1$).

$$
W_1 \cap W_2 = \lbrace (0, 0, 0) \rbrace \implies \dim(W_1 \cap W_2) = 0
$$

By the theorem:

$$
\dim(W_1 + W_2) = 1 + 2 - 0 = 3
$$

Since $\dim(W_1 + W_2) = 3 = \dim(V_3(\mathbb{R}))$, their sum spans the entire 3D space.

### Example 2: Sum in 4D Space
Let $V_4(\mathbb{R})$ be a 4D space with subspaces:

$$
W_1 = \lbrace (a, b, 0, 0) \mid a, b \in \mathbb{R} \rbrace \implies \dim(W_1) = 2
$$

$$
W_2 = \lbrace (0, a, b, c) \mid a, b, c \in \mathbb{R} \rbrace \implies \dim(W_2) = 3
$$

The intersection requires the 1st coordinate to be zero (from $W_2$) and the last two to be zero (from $W_1$). Only the 2nd coordinate is free.

$$
W_1 \cap W_2 = \lbrace (0, x, 0, 0) \mid x \in \mathbb{R} \rbrace \implies \dim(W_1 \cap W_2) = 1
$$

By the theorem:

$$
\dim(W_1 + W_2) = 2 + 3 - 1 = 4
$$

Since their sum dimension matches the parent space dimension, their sum spans the entire 4D space.

## What Comes Next
We have completed our investigation of dimensions in vector subspaces. In the next lectures, we will introduce Quotient Spaces and study their dimensional properties.

---

**Navigation**
[< Previous Lecture](12_Extension_Theorem_Complementary.md) | [Index](README.md) | [Next Lecture >](14_Quotient_Space_Dimension.md)
